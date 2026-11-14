#!/usr/bin/env python3
"""Lista las charlas publicadas de los eventos de AI Engineer y mantiene su catálogo.

Uso:
    python3 tools/aie_talks.py list        # una línea TSV por charla (id, fecha, evento, título)
    python3 tools/aie_talks.py pendientes  # solo las que no están ingeridas
    python3 tools/aie_talks.py catalogo    # reescribe ai/ai-engineer/catalogo.md

Fuente: canal `AI Engineer` de YouTube (`UCLKPca3kwwd-B59HNr-_lvA`, handle
`@aiDotEngineer`). El catálogo se limita a los dos eventos pedidos, y dentro de cada evento
a sus playlists: la completa y la de charlas online (y los talleres, en NYC), porque la
playlist «completa» no siempre incluye todo lo que se publica suelto.

Las fechas exactas no están en la página de la playlist (solo «4d ago»), así que se leen de la
página de cada vídeo y se guardan en el catálogo. Al regenerar, las fechas ya conocidas no se
vuelven a pedir: el catálogo hace de caché.

No descarga ninguna transcripción. Eso es trabajo de `uv run --project ytpipe ytpipe fetch`,
una charla cada vez.
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESTINO = ROOT / "ai" / "ai-engineer"
CATALOGO = DESTINO / "catalogo.md"
CANAL = "AI Engineer"
CANAL_ID = "UCLKPca3kwwd-B59HNr-_lvA"
FUENTES = {
    "AIE NYC 2026": ["PLLKkCXQeuCis", "PLVanfCmVOgIg", "PLPrARbQ6iscE"],
    "AIE CODE 2026": ["PLZUQJ1aon-40", "PLbhiZl98JSQI"],
}
NO_RECORRER = {".git", ".venv", "node_modules", "ytpipe", ".agents", "__pycache__", ".pytest_cache"}
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
INITIAL_DATA = re.compile(r"var ytInitialData = (\{.*?\});</script>", re.S)
DATE_TEXT = re.compile(r'"dateText":\{"simpleText":"([^"]+)"')
VISIBLE_DATE = re.compile(r"([A-Z][a-z]{2}) (\d{1,2}), (\d{4})")
MESES = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
}
PAUSA = 0.3  # segundos entre peticiones a YouTube


def get(url: str) -> str:
    """Devuelve el HTML de una página de YouTube."""
    request = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"}
    )
    return urllib.request.urlopen(request, timeout=40).read().decode("utf-8", "replace")


def playlist(playlist_id: str) -> tuple[int, int, list[dict]]:
    """Charlas de una playlist: (vídeos que declara, entradas leídas, lista sin repetidos)."""
    html = get(f"https://www.youtube.com/playlist?list={playlist_id}")
    match = INITIAL_DATA.search(html)
    if not match:
        raise ValueError(f"la playlist {playlist_id} no devolvió datos")
    data = json.loads(match.group(1))
    declarado = [int(n.replace(",", "")) for n in re.findall(r'"([\d,]+) videos?"', html)]
    found: list[dict] = []
    seen: set[str] = set()
    leidas = 0

    def walk(node) -> None:
        nonlocal leidas
        if isinstance(node, dict):
            if "lockupViewModel" in node:
                item = node["lockupViewModel"]
                video = item.get("contentId") or ""
                if item.get("contentType", "").endswith("VIDEO") and video:
                    leidas += 1
                if item.get("contentType", "").endswith("VIDEO") and video and video not in seen:
                    seen.add(video)
                    meta = item.get("metadata", {}).get("lockupMetadataViewModel", {})
                    found.append({"id": video, "titulo": meta.get("title", {}).get("content", "")})
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(data)
    time.sleep(PAUSA)
    return (max(declarado) if declarado else 0), leidas, found


def collect() -> tuple[list[dict], list[str]]:
    """Todas las charlas de los eventos registrados, sin repetir id, y los avisos de lectura."""
    seen: set[str] = set()
    found: list[dict] = []
    avisos: list[str] = []
    for evento, playlists in FUENTES.items():
        for playlist_id in playlists:
            declarado, leidas, videos = playlist(playlist_id)
            if declarado > leidas:
                aviso = (
                    f"La playlist `{playlist_id}` declara {declarado} vídeos y YouTube solo "
                    f"entrega {leidas} sin sesión: faltan {declarado - leidas} por enumerar."
                )
                avisos.append(aviso)
                print(f"aviso: {aviso}", file=sys.stderr)
            for item in videos:
                if item["id"] in seen:
                    continue
                seen.add(item["id"])
                found.append({**item, "evento": evento, "playlist": playlist_id})
    return found, avisos


def ingested() -> dict[str, dict]:
    """id → {carpeta, fecha} de cada transcripción del repositorio."""
    done: dict[str, dict] = {}
    for path in ROOT.rglob("transcript.json"):
        if set(path.relative_to(ROOT).parts) & NO_RECORRER:
            continue
        try:
            source = json.loads(path.read_text(encoding="utf-8")).get("source", {})
        except (OSError, ValueError):
            continue
        if source.get("video_id"):
            done[source["video_id"]] = {
                "carpeta": str(path.parent.relative_to(ROOT)),
                "fecha": str(source.get("upload_date", ""))[:10],
            }
    return done


def cached_dates() -> dict[str, str]:
    """Fechas ya conocidas, leídas del catálogo anterior."""
    if not CATALOGO.is_file():
        return {}
    known = {}
    for line in CATALOGO.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\| (\d{4}-\d{2}-\d{2}) \|.*?\[([A-Za-z0-9_-]{11})\]", line)
        if match:
            known[match.group(2)] = match.group(1)
    return known


def published(video_id: str) -> str:
    """Fecha de publicación exacta de un vídeo, leída de su página."""
    try:
        html = get(f"https://www.youtube.com/watch?v={video_id}")
    except (urllib.error.URLError, OSError):
        return ""
    finally:
        time.sleep(PAUSA)
    match = DATE_TEXT.search(html)
    if not match:
        return ""
    visible = VISIBLE_DATE.search(match.group(1))
    if not visible:
        return ""
    month, day, year = visible.groups()
    return f"{year}-{MESES[month]:02d}-{int(day):02d}"


def with_dates(items: list[dict]) -> list[dict]:
    """Rellena la fecha de cada charla: catálogo anterior, transcripción o página del vídeo."""
    known = cached_dates()
    done = ingested()
    for item in items:
        item["fecha"] = (
            item["id"] in done and done[item["id"]]["fecha"]
        ) or known.get(item["id"]) or published(item["id"])
    return items


def write_catalogo(items: list[dict], avisos: list[str] | None = None) -> Path:
    """Reescribe el catálogo markdown con el estado de cada charla."""
    done = ingested()
    rows = sorted(items, key=lambda i: (i.get("fecha") or "0000-00-00", i["titulo"]), reverse=True)
    pending = [i for i in rows if i["id"] not in done]
    por_evento = {evento: sum(1 for i in pending if i["evento"] == evento) for evento in FUENTES}

    lines = [
        "---",
        'title: "Catálogo de charlas de AI Engineer: NYC 2026 y Code Summit 2026"',
        f"date: {date.today().isoformat()}",
        "type: reference",
        "category: ai",
        "tags: [ai-engineer, youtube, charlas, catalogo, agentes, ia]",
        "status: living",
        "---",
        "",
        "# Catálogo de charlas de AI Engineer: NYC 2026 y Code Summit 2026",
        "",
        f"Canal: [{CANAL}](https://www.youtube.com/@aiDotEngineer) (`{CANAL_ID}`).",
        "Lo genera `python3 tools/aie_talks.py catalogo`; no editar a mano.",
        "",
        f"**Charlas con vídeo publicado:** {len(rows)} · **ingeridas:** {len(rows) - len(pending)} · "
        f"**pendientes:** {len(pending)}",
        "",
        "**Pendientes por evento:** "
        + " · ".join(f"{evento}: {total}" for evento, total in por_evento.items()),
        "",
    ]
    if avisos:
        lines += [f"> **Aviso de lectura:** {aviso}" for aviso in avisos] + [""]
    lines += [
        "Sin descargar nada: para ingerir una charla, `uv run --project ytpipe ytpipe fetch "
        "<url> --out ai/ai-engineer --no-open`, una cada vez.",
        "",
        "| Fecha | Evento | Charla | Vídeo | Estado | Carpeta |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in rows:
        folder = done.get(item["id"], {}).get("carpeta", "")
        estado = "ingerida" if folder else "pendiente"
        title = item["titulo"].replace("|", "\\|")
        link = f"https://www.youtube.com/watch?v={item['id']}"
        lines.append(
            f"| {item.get('fecha') or '—'} | {item['evento']} | [{title}]({link}) | "
            f"[{item['id']}]({link}) | {estado} | `{folder or '—'}` |"
        )

    DESTINO.mkdir(parents=True, exist_ok=True)
    CATALOGO.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return CATALOGO


def main(argv: list[str]) -> int:
    command = argv[1] if len(argv) > 1 else "list"
    try:
        items, avisos = collect()
    except (urllib.error.URLError, OSError, ValueError) as error:
        print(f"no pude leer las playlists de YouTube: {error}", file=sys.stderr)
        return 1
    if not items:
        print("ninguna charla encontrada: cambió el HTML o las playlists", file=sys.stderr)
        return 1

    if command == "list":
        items = with_dates(items)
        for item in items:
            print("\t".join([item["id"], item["fecha"], item["evento"], item["titulo"]]))
        print(f"# {len(items)} charlas", file=sys.stderr)
        return 0

    if command == "pendientes":
        done = ingested()
        pendientes = [item for item in items if item["id"] not in done]
        pendientes = with_dates(pendientes)
        pendientes.sort(key=lambda i: (i.get("fecha") or "0000-00-00"), reverse=True)
        for item in pendientes:
            print("\t".join([item["id"], item["fecha"], item["evento"], item["titulo"]]))
        return 0

    if command == "catalogo":
        path = write_catalogo(with_dates(items), avisos)
        print(f"escrito: {path.relative_to(ROOT)} ({len(items)} charlas)")
        return 0

    print(f"comando desconocido: {command} (usa list, pendientes o catalogo)", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

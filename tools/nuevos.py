#!/usr/bin/env python3
"""Lista lo NUEVO: lo publicado después de la última transcripción ingerida.

Uso:
    python3 tools/nuevos.py            # canal + webinars, solo lo posterior a la última ingesta
    python3 tools/nuevos.py --json     # salida para el agente
    python3 tools/nuevos.py --backlog  # cuántos webinars antiguos quedan sin ingerir

Definición de «nuevo»: el vídeo se publicó **desde** la fecha del más reciente que ya está en el
repositorio (por fuente) y no está ingerido. Se compara por ID, así que un vídeo de esa misma fecha
que aún falte entra. No es «lo que falta»: el backlog de 140 webinars de 2023-2025 no es nuevo.

Fuentes:
  - La Pizarra de Andrés: RSS del canal `UCEXbEm8RUvRkKUEo2RjKd9w` (fechas reales, títulos en
    español). `@LaPizarradeAndrésLive` es otro canal y no se ingiere.
  - MyInvestor: catálogo del blog (qué es webinar) cruzado con el RSS del canal
    `UCc9nsd1tjDdw32wLcM5OOWQ` (cuándo se publicó).
  - AI Engineer: charlas de `AIE NYC 2026` y `AIE CODE 2026`, leídas de sus playlists
    (`tools/aie_talks.py`). Es backlog, no goteo: se informa del total pendiente y de las tres
    más recientes, no se listan las 131.

Sin estado: la marca de agua es la fecha de la última transcripción ingerida, así que si el
cron falla dos semanas, la siguiente recupera lo que faltó.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from pathlib import Path

import aie_talks

ROOT = Path(__file__).resolve().parents[1]
VIDEOS = "videos"  # contenedor de las fuentes de vídeo dentro de finance/
CANAL = {"nombre": "La Pizarra de Andrés", "id": "UCEXbEm8RUvRkKUEo2RjKd9w", "carpeta": f"{VIDEOS}/la-pizarra-de-andres"}
WEBINARS = {"nombre": "MyInvestor", "id": "UCc9nsd1tjDdw32wLcM5OOWQ", "carpeta": f"{VIDEOS}/myinvestor-webinars"}
NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}
DIAS_POR_DEFECTO = 7


def feed(channel_id: str) -> list[dict]:
    """Entradas del RSS del canal: fecha, id y título. Sin API key."""
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    request = urllib.request.Request(url, headers={"User-Agent": "investing-meetings"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            root = ET.fromstring(response.read())
    except Exception as error:  # red, XML roto o canal inexistente
        sys.exit(f"no pude leer el RSS de {channel_id}: {error}")
    entries = []
    for entry in root.findall("a:entry", NS):
        published = entry.find("a:published", NS)
        video = entry.find("yt:videoId", NS)
        title = entry.find("a:title", NS)
        if published is None or not published.text or video is None or not video.text:
            continue
        entries.append(
            {
                "fecha": date.fromisoformat(published.text[:10]),
                "id": video.text,
                "titulo": (title.text or "").strip() if title is not None else "",
            }
        )
    return entries


def ingested() -> dict[str, dict]:
    """id → {carpeta, fecha} de cada transcripción del repositorio."""
    return aie_talks.ingested()


def last_date(done: dict[str, dict], carpeta: str) -> date | None:
    """Fecha del vídeo más reciente ya ingerido de esa fuente."""
    dates = [
        date.fromisoformat(item["fecha"])
        for item in done.values()
        if Path(item["carpeta"]).parent.as_posix() == f"finance/{carpeta}" and len(item["fecha"]) == 10
    ]
    return max(dates) if dates else None


def pending_webinars() -> dict[str, dict]:
    """Webinars del catálogo que aún no están ingeridos, con id, título y post."""
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "myinvestor_webinars.py"), "pendientes"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return {}
    out = {}
    for line in result.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            out[parts[0]] = {"titulo": parts[1], "post": parts[2] if len(parts) > 2 else ""}
    return out


def pending_aie() -> list[dict]:
    """Charlas de AI Engineer sin ingerir, la más reciente primero. Sin red, lista vacía."""
    try:
        items, _ = aie_talks.collect()
    except Exception as error:  # una fuente caída no puede tumbar el resto del informe
        print(f"aviso: no pude leer AI Engineer: {error}", file=sys.stderr)
        return []
    done = aie_talks.ingested()
    pending = [item for item in items if item["id"] not in done]
    pending = aie_talks.with_dates(pending)
    pending.sort(key=lambda item: item.get("fecha") or "0000-00-00", reverse=True)
    return pending


def main() -> int:
    parser = argparse.ArgumentParser(description="Qué hay nuevo desde la última ingesta")
    parser.add_argument("--dias", type=int, help="ventana si la fuente no tiene ingesta previa")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--backlog", action="store_true", help="cuenta el backlog antiguo")
    args = parser.parse_args()
    window = timedelta(days=args.dias or DIAS_POR_DEFECTO)

    done = ingested()
    channel_cut = last_date(done, CANAL["carpeta"])
    webinar_cut = last_date(done, WEBINARS["carpeta"])

    channel_new = [
        item
        for item in feed(CANAL["id"])
        if item["id"] not in done and item["fecha"] >= (channel_cut or date.today() - window)
    ]

    catalog = pending_webinars()
    webinar_cut_effective = webinar_cut or date.today() - window
    webinars_new = [
        {**item, "post": catalog[item["id"]]["post"]}
        for item in feed(WEBINARS["id"])
        if item["id"] in catalog and item["fecha"] >= webinar_cut_effective
    ]

    aie = pending_aie()

    if args.json:
        print(
            json.dumps(
                {
                    "canal": CANAL["nombre"],
                    "corte_canal": str(channel_cut) if channel_cut else None,
                    "videos_nuevos": [
                        {**item, "url": f"https://www.youtube.com/watch?v={item['id']}"} for item in channel_new
                    ],
                    "corte_webinars": str(webinar_cut) if webinar_cut else None,
                    "webinars_nuevos": [
                        {**item, "url": f"https://www.youtube.com/watch?v={item['id']}"} for item in webinars_new
                    ],
                    "backlog_webinars": len(catalog),
                    "aie_pendientes": len(aie),
                    "aie_recientes": [
                        {**item, "url": f"https://www.youtube.com/watch?v={item['id']}"} for item in aie[:3]
                    ],
                },
                ensure_ascii=False,
                indent=1,
                default=str,
            )
        )
        return 0

    print(f"{CANAL['nombre']}: {len(channel_new)} nuevos desde {channel_cut or 'sin ingesta previa'}")
    for item in channel_new:
        print(f"  {item['fecha']}  {item['id']}  {item['titulo'][:70]}")
        print(f"              https://www.youtube.com/watch?v={item['id']}")

    print(f"\n{WEBINARS['nombre']}: {len(webinars_new)} nuevos desde {webinar_cut or 'sin ingesta previa'}")
    for item in webinars_new:
        print(f"  {item['fecha']}  {item['id']}  {item['titulo'][:70]}")
        print(f"              https://www.youtube.com/watch?v={item['id']}")

    print(f"\nAI Engineer (NYC 2026 + CODE 2026): {len(aie)} charlas pendientes en el catálogo")
    for item in aie[:3]:
        print(f"  {item['fecha'] or '—'}  {item['id']}  {item['evento']}  {item['titulo'][:60]}")
        print(f"              https://www.youtube.com/watch?v={item['id']}")
    if len(aie) > 3:
        print(f"  y {len(aie) - 3} más: ai/ai-engineer/catalogo.md")

    if args.backlog:
        print(f"\nBacklog antiguo (no es nuevo, no se ingiere solo): {len(catalog)} webinars")
    if not channel_new and not webinars_new and not aie:
        print("\nSin novedades: nada publicado después de la última ingesta.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

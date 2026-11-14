#!/usr/bin/env python3
"""Comprueba que el repositorio cumple su definición de hecho.

Uso:
    python3 tools/verify.py            # contenido (rápido, sin red)
    python3 tools/verify.py --git      # además: árbol limpio y nada sin subir

Comprueba:
  1. Cada carpeta de reunión se llama `YYYY-MM-DD-<slug>`.
  2. Cada `transcript.json` tiene su `summary.md`, y al revés (aviso).
  3. Todo `.md` con frontmatter tiene las seis claves obligatorias.
  4. `INDEX.md` está al día (se regenera en memoria y se compara).
  5. El catálogo de webinars cuadra con las carpetas ingeridas.
  6. Con `--git`: sin cambios sin commitear y sin commits sin subir.

Sale con código 1 si hay algún error. Los avisos no rompen la comprobación.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_index as bi  # noqa: E402

ROOT = bi.ROOT
FOLDER = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$")
NO_EVENT = {"portfolio", "reports", "archivo"}
# Carpetas que agrupan vídeos de una misma fuente: se recorre un nivel más.
CONTAINERS = {"videos"}
KEYS = ("title", "date", "type", "category", "tags", "status")

errors: list[str] = []
warnings: list[str] = []


def event_folders() -> list[Path]:
    found = []
    for category in ("finance", "ai"):
        base = ROOT / category
        if not base.is_dir():
            continue
        for source in sorted(p for p in base.iterdir() if p.is_dir()):
            if source.name in NO_EVENT:
                continue
            if source.name in CONTAINERS:
                # Un contenedor (`finance/videos/`) agrupa fuentes: se baja un nivel más.
                fuentes = sorted(p for p in source.iterdir() if p.is_dir())
            else:
                fuentes = [source]
            for fuente in fuentes:
                if fuente.name in NO_EVENT:
                    continue
                found += [
                    p for p in sorted(fuente.iterdir()) if p.is_dir() and p.name not in NO_EVENT
                ]
    return found


def check_folders() -> None:
    for folder in event_folders():
        rel = folder.relative_to(ROOT)
        if not FOLDER.match(folder.name):
            errors.append(f"{rel}: el nombre no es YYYY-MM-DD-<slug>")
        has_t = (folder / "transcript.json").is_file()
        has_s = (folder / "summary.md").is_file()
        if has_t and not has_s:
            errors.append(f"{rel}: transcript.json sin summary.md")
        if has_s and not has_t:
            warnings.append(f"{rel}: summary.md sin transcript.json (transcripción pegada)")


def check_frontmatter() -> None:
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if any(part in bi.SKIP_DIRS for part in rel.parts):
            continue
        if rel.name in {"README.md", "INDEX.md", "AGENTS.md", "CLAUDE.md"} or ".agents" in rel.parts:
            continue
        data = bi.frontmatter(path)
        if data is None:
            errors.append(f"{rel}: sin frontmatter YAML")
            continue
        missing = [k for k in KEYS if not data.get(k)]
        if missing:
            errors.append(f"{rel}: frontmatter sin {', '.join(missing)}")


def check_index() -> None:
    expected = bi.build(bi.artifacts())
    current = bi.INDEX.read_text(encoding="utf-8") if bi.INDEX.is_file() else ""
    if current != expected:
        errors.append("INDEX.md desactualizado: ejecuta `python3 tools/build_index.py`")


def check_catalog() -> None:
    webinars = ROOT / "finance" / "videos" / "myinvestor-webinars"
    catalog = webinars / "catalogo.md"
    if not catalog.is_file():
        warnings.append("finance/videos/myinvestor-webinars/catalogo.md no existe")
        return
    ingested = len(list(webinars.glob("*/transcript.json")))
    match = re.search(r"\*\*ingeridos:\*\*\s*(\d+)", catalog.read_text(encoding="utf-8"))
    if not match:
        warnings.append("catalogo.md: no encuentro el contador de ingeridos")
    elif int(match.group(1)) != ingested:
        errors.append(
            f"catalogo.md dice {match.group(1)} ingeridos y hay {ingested} carpetas: "
            "ejecuta `python3 tools/myinvestor_webinars.py catalogo`"
        )


def check_aie_catalog() -> None:
    charlas = ROOT / "ai" / "ai-engineer"
    catalog = charlas / "catalogo.md"
    if not catalog.is_file():
        warnings.append("ai/ai-engineer/catalogo.md no existe")
        return
    ingested = len(list(charlas.glob("*/transcript.json")))
    match = re.search(r"\*\*ingeridas:\*\*\s*(\d+)", catalog.read_text(encoding="utf-8"))
    if not match:
        warnings.append("ai/ai-engineer/catalogo.md: no encuentro el contador de ingeridas")
    elif int(match.group(1)) != ingested:
        errors.append(
            f"ai/ai-engineer/catalogo.md dice {match.group(1)} ingeridas y hay {ingested} carpetas: "
            "ejecuta `python3 tools/aie_talks.py catalogo`"
        )


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, check=False
    ).stdout.strip()


def check_git() -> None:
    if not (ROOT / ".git").is_dir():
        warnings.append("no es un repositorio git")
        return
    dirty = git("status", "--porcelain")
    if dirty:
        errors.append(f"árbol de trabajo sucio:\n{dirty}")
    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    ahead = git("rev-list", "--count", f"origin/{branch}..{branch}") if branch != "HEAD" else ""
    if ahead and ahead != "0":
        errors.append(f"{ahead} commits sin subir en {branch}")
    if not git("rev-parse", "--verify", f"origin/{branch}"):
        warnings.append(f"la rama {branch} no existe en origin")
        return


def main(argv: list[str]) -> int:
    check_folders()
    check_frontmatter()
    check_index()
    check_catalog()
    check_aie_catalog()
    if "--git" in argv:
        check_git()

    for message in warnings:
        print(f"⚠️  {message}")
    for message in errors:
        print(f"❌ {message}")

    folders = event_folders()
    summaries = sum(1 for f in folders if (f / "summary.md").is_file())
    print(
        f"\n{len(folders)} carpetas de reunión · {summaries} con resumen · "
        f"{len(errors)} errores · {len(warnings)} avisos"
    )
    print("✅ definición de hecho cumplida" if not errors else "❌ no está listo para subir")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

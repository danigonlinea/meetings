#!/usr/bin/env python3
"""Gestión por lotes de las fichas web del listado de la app MyInvestor.

El estado es el propio sistema de ficheros: una ficha existe si hay un
`<clase>/<ISIN>.md` en finance/fondos-myinvestor/. No hay estado duplicado.

Uso:
    python3 tools/fichas_listado.py estado          # progreso por clase
    python3 tools/fichas_listado.py siguientes 80   # próximos 80 ISIN (JSON)

Prioridad: fondos sin clasificar (clase `pendiente`) -> indexados -> resto por
clase (monetarios, renta-fija, mixtos, rv-*) y TER ascendente dentro de cada grupo.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "finance" / "fondos-myinvestor"
LISTADO = DB / "listado-app" / "fondos.json"

ORDEN = [
    "monetarios", "renta-fija", "mixtos", "rv-global", "rv-usa", "rv-europa",
    "rv-japon", "rv-emergentes", "rv-otros", "sectoriales", "alternativos",
    "pendiente",
]


def cargar() -> list[dict]:
    return json.loads(LISTADO.read_text(encoding="utf-8"))["fondos"]


def fichas_existentes() -> dict[str, str]:
    out = {}
    for p in DB.glob("*/*.md"):
        if p.parent.name == "listado-app":
            continue
        if re.fullmatch(r"[A-Z0-9]{12}", p.stem):
            out[p.stem] = p.parent.name
    return out


def prioridad(f: dict) -> tuple:
    if f["clase"] == "pendiente":
        grupo = 0
    elif f["gestion"] == "indexada":
        grupo = 1
    else:
        grupo = 2
    rango = ORDEN.index(f["clase"]) if f["clase"] in ORDEN else len(ORDEN)
    return (grupo, rango, f["ter"] if f["ter"] is not None else 99.0, f["isin"])


def comprobar() -> int:
    """QA de las fichas web (fuente: listado-app): coherencia y secciones."""
    def fm_completo(p: Path) -> dict:
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---"):
            return {}
        end = text.find("\n---", 3)
        if end == -1:
            return {}
        out = {}
        for line in text[3:end].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                out[k.strip()] = v.strip().strip('"')
        return out

    secciones = [
        "## Qué es y para qué sirve", "## Composición",
        "## Para qué vale en una cartera", "## Comisiones",
        "## Rentabilidad y riesgo", "## Fuentes",
    ]
    fondos = {f["isin"]: f for f in cargar()}
    problemas = []
    n = 0
    for p in sorted(DB.glob("*/*.md")):
        if p.parent.name == "listado-app" or not re.fullmatch(r"[A-Z0-9]{12}", p.stem):
            continue
        fm = fm_completo(p)
        if fm.get("fuente") != "listado-app":
            continue
        n += 1
        rel = p.relative_to(ROOT)
        if fm.get("isin") != p.stem:
            problemas.append(f"{rel}: isin del frontmatter != nombre del archivo")
        if fm.get("clase") != p.parent.name:
            problemas.append(f"{rel}: clase del frontmatter != carpeta")
        if p.stem not in fondos:
            problemas.append(f"{rel}: ISIN fuera del listado")
        texto = p.read_text(encoding="utf-8")
        for s in secciones:
            if s not in texto:
                problemas.append(f"{rel}: falta sección «{s}»")
        if "quefondos" not in texto and "finect" not in texto.lower():
            problemas.append(f"{rel}: sin URLs de fuentes web")
    print(f"Fichas web comprobadas: {n} · problemas: {len(problemas)}")
    for pr in problemas:
        print(" -", pr)
    return 1 if problemas else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("accion", choices=["estado", "siguientes", "comprobar"])
    ap.add_argument("n", nargs="?", type=int, default=80)
    args = ap.parse_args()

    if args.accion == "comprobar":
        return comprobar()

    fondos = cargar()
    hechas = fichas_existentes()
    pendientes = [f for f in fondos if f["isin"] not in hechas]

    if args.accion == "estado":
        total_clase = Counter(f["clase"] for f in fondos)
        hechas_clase = Counter(
            next(f["clase"] for f in fondos if f["isin"] == i)
            for i in hechas
            if any(f["isin"] == i for f in fondos)
        )
        print(f"Fondos del listado: {len(fondos)} · fichas escritas: {len(hechas)} · pendientes: {len(pendientes)}")
        for c in ORDEN:
            if total_clase.get(c):
                print(f"  {c:15s} {hechas_clase.get(c, 0):4d} / {total_clase[c]}")
        fuera = len(hechas) - sum(hechas_clase.values())
        if fuera:
            print(f"  (fichas MCP fuera del listado: {fuera})")
        return 0

    pendientes.sort(key=prioridad)
    sel = pendientes[: args.n]
    print(json.dumps(sel, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())

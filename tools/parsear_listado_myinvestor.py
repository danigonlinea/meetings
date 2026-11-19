#!/usr/bin/env python3
"""Parsea el listado de fondos guardado de la app de MyInvestor (MyInvestor.html).

Fuente: página guardada manualmente de
https://newapp.myinvestor.es/app/explore/investments/funds/search
La tabla trae una fila por fondo (con duplicados por columnas fijas):
Nombre+ISIN, Tipo, Divisa, Categoría Morningstar, NAV, 2026 (YTD), 1A, 3A, 5A,
TER, riesgo SRRI (x/7) y rating Morningstar (estrellas, slider aria).

Salida (en finance/fondos-myinvestor/listado-app/):
  - fondos.json   Base de datos estructurada, un registro por ISIN.
  - catalogo.md   Índice generado agrupado por clase, ordenado por TER.

Los campos que el listado no publica quedan a null y se listan en
`pendientes` de cada fondo. Las categorías sin región/sector declarado
(Equity Miscellaneous, Miscellaneous, Otros, -) quedan con clase
`pendiente` para revisión manual. No se inventa ningún dato.

Uso:
    python3 tools/parsear_listado_myinvestor.py [--html RUTA] [--dry-run]
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "finance" / "fondos-myinvestor" / "listado-app"
DB_DIR = ROOT / "finance" / "fondos-myinvestor"

# Categoría Morningstar -> clase de la base de datos.
# `alternativos` amplía el esquema de clases para este listado: el MCP solo
# declaraba RV/RF/Mixto/Monetario, pero la categoría Morningstar sí distingue
# estrategias alternativas. `pendiente` = falta región/sector para clasificar.
MAPA_CLASE = {
    "monetarios": [
        "Euro Money Market", "US Money Market", "Sterling Money Market",
        "Money Market Miscellaneous", "DINERO EUROPA",
    ],
    "renta-fija": [
        "Europe Fixed Income", "Global Fixed Income", "US Fixed Income",
        "Emerging Markets Fixed Income", "Asia Fixed Income",
        "Japan Fixed Income", "Sterling Fixed Income",
        "Fixed Income Miscellaneous", "Convertibles", "Renta Fija Flexible",
    ],
    "mixtos": [
        "Flexible Allocation", "Moderate Allocation", "Cautious Allocation",
        "Aggressive Allocation", "Allocation Miscellaneous", "Target Date",
        "Guaranteed",
    ],
    "rv-global": ["Global Equity Large Cap", "Global Equity Mid/Small Cap"],
    "rv-usa": [
        "US Equity Large Cap Blend", "US Equity Large Cap Growth",
        "US Equity Large Cap Value", "US Equity Mid Cap", "US Equity Small Cap",
    ],
    "rv-europa": [
        "Europe Equity Large Cap", "Europe Equity Mid/Small Cap",
        "UK Equity Large Cap",
    ],
    "rv-japon": ["Japan Equity"],
    "rv-emergentes": [
        "Global Emerging Markets Equity", "Europe Emerging Markets Equity",
        "Greater China Equity", "India Equity", "Latin America Equity",
        "Africa Equity", "Korea Equity", "Mexico Equity", "Thailand Equity",
    ],
    "rv-otros": [
        "Asia ex-Japan Equity", "Asia Equity",
        "Australia & New Zealand Equity",
    ],
    "sectoriales": [
        "Technology Sector Equity", "Healthcare Sector Equity",
        "Energy Sector Equity", "Financials Sector Equity",
        "Industrials Sector Equity", "Infrastructure Sector Equity",
        "Consumer Goods & Services Sector Equity",
        "Natural Resources Sector Equity", "Precious Metals Sector Equity",
        "Real Estate Sector Equity", "Property-Direct",
    ],
    "alternativos": [
        "Global Macro", "Market Neutral", "Long/Short Equity",
        "Long/Short Credit", "Multialternative", "Alternative Miscellaneous",
        "Options Trading", "Commodities Broad Basket", "Commodities Specified",
    ],
    "pendiente": ["Equity Miscellaneous", "Miscellaneous", "Otros", "-"],
}
CATEGORIA_A_CLASE = {c: clase for clase, cats in MAPA_CLASE.items() for c in cats}

ORDEN_CLASES = [
    "monetarios", "renta-fija", "mixtos", "rv-global", "rv-usa", "rv-europa",
    "rv-japon", "rv-emergentes", "rv-otros", "sectoriales", "alternativos",
    "pendiente",
]
NOMBRE_CLASE = {
    "monetarios": "Monetarios (liquidez)",
    "renta-fija": "Renta fija",
    "mixtos": "Mixtos",
    "rv-global": "Renta variable global",
    "rv-usa": "Renta variable EE. UU.",
    "rv-europa": "Renta variable Europa",
    "rv-japon": "Renta variable Japón",
    "rv-emergentes": "Renta variable emergentes",
    "rv-otros": "Renta variable otras regiones",
    "sectoriales": "Sectoriales y temáticos",
    "alternativos": "Alternativos",
    "pendiente": "Pendientes de clasificar",
}

CAMPOS_NUMERICOS = ["nav", "ytd_2026", "r1a", "r3a", "r5a", "ter", "srri"]


def texto(td: str) -> str:
    t = re.sub(r"<[^>]+>", " ", td)
    return html.unescape(re.sub(r"\s+", " ", t)).strip()


def numero(v: str) -> float | None:
    """Número en formato español: '.' miles, ',' decimal. '-' o vacío -> None."""
    v = v.strip()
    if v in ("", "-", "—"):
        return None
    v = v.replace(".", "").replace(",", ".")
    try:
        return float(v)
    except ValueError:
        return None


def parsear(html_path: Path) -> list[dict]:
    data = html_path.read_text(encoding="utf-8", errors="replace")
    filas = re.findall(r"<tr[^>]*>.*?</tr>", data, re.S)
    vistos: dict[str, dict] = {}
    for fila in filas:
        m = re.search(r"/app/explore/investments/funds/([A-Z0-9]+)\"", fila)
        if not m:
            continue
        isin = m.group(1)
        if isin in vistos:
            continue  # duplicado de columna fija: gana la primera fila completa
        tds = re.findall(r"<td[^>]*>(.*?)</td>", fila, re.S)
        if len(tds) != 12:
            continue
        nombre_m = re.search(r'title="([^"]+)"', tds[0])
        estrellas_m = re.search(r'role="slider"[^>]*aria-valuenow="(\d+)"', tds[0])
        tipo = texto(tds[1])
        categoria = texto(tds[3])
        riesgo = texto(tds[10])
        srri = int(riesgo.split("/")[0]) if re.match(r"^\d/7$", riesgo) else None
        reg = {
            "isin": isin,
            "nombre": html.unescape(nombre_m.group(1)) if nombre_m else None,
            "tipo": tipo,
            "gestion": "indexada" if tipo == "Fondos Indexados" else "activa",
            "divisa": texto(tds[2]),
            "categoria": categoria,
            "clase": CATEGORIA_A_CLASE.get(categoria, "pendiente"),
            "nav": numero(texto(tds[4])),
            "ytd_2026": numero(texto(tds[5])),
            "r1a": numero(texto(tds[6])),
            "r3a": numero(texto(tds[7])),
            "r5a": numero(texto(tds[8])),
            "ter": numero(texto(tds[9])),
            "srri": srri,
            "rating": int(estrellas_m.group(1)) if estrellas_m else None,
        }
        pendientes = [c for c in CAMPOS_NUMERICOS if reg[c] is None]
        if reg["rating"] is None:
            pendientes.append("rating")
        if reg["clase"] == "pendiente":
            pendientes.append("clase")
        reg["pendientes"] = pendientes
        vistos[isin] = reg
    return [vistos[k] for k in sorted(vistos)]


def fichas_mcp_existentes() -> dict[str, str]:
    """ISIN -> ruta relativa de la ficha MCP ya escrita (si existe)."""
    fichas = {}
    for p in DB_DIR.glob("*/*.md"):
        if p.parent.name == "listado-app":
            continue
        if re.fullmatch(r"[A-Z0-9]{12}", p.stem):
            fichas[p.stem] = f"{p.parent.name}/{p.name}"
    return fichas


def fmt(v: float | None, dec: int = 2) -> str:
    if v is None:
        return "—"
    s = f"{v:.{dec}f}".replace(".", ",")
    return s


def generar_catalogo(fondos: list[dict], fecha: str, fichas: dict[str, str]) -> str:
    por_clase = Counter(f["clase"] for f in fondos)
    lineas = [
        "---",
        'title: "Listado de fondos MyInvestor — snapshot de la app"',
        f"date: {fecha}",
        "type: reference",
        "category: finance",
        "tags: [fondos, myinvestor, catalogo, listado]",
        "status: living",
        "---",
        "",
        "# Listado de fondos MyInvestor — snapshot de la app",
        "",
        f"Índice generado por `python3 tools/parsear_listado_myinvestor.py`. No editar a mano.",
        f"Fuente: `MyInvestor.html` (página guardada de la app, snapshot {fecha}).",
        "Datos completos en [`fondos.json`](fondos.json); campos ausentes marcados `—` y pendientes en el JSON.",
        "",
        f"**Fondos: {len(fondos)}** · con ficha MCP previa: {sum(1 for f in fondos if f['isin'] in fichas)}",
        "",
        "| Clase | Fondos |",
        "| --- | --- |",
    ]
    for clase in ORDEN_CLASES:
        if por_clase.get(clase):
            lineas.append(f"| [{NOMBRE_CLASE[clase]}](#{clase}) | {por_clase[clase]} |")
    for clase in ORDEN_CLASES:
        grupo = [f for f in fondos if f["clase"] == clase]
        if not grupo:
            continue
        grupo.sort(key=lambda f: (f["ter"] is None, f["ter"] or 0, f["nombre"] or ""))
        lineas += ["", f"## {clase}", "", f"### {NOMBRE_CLASE[clase]} ({len(grupo)})", ""]
        lineas += [
            "| ISIN | Nombre | Gestión | Divisa | Categoría | TER | 3A anual. | SRRI | ★ |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for f in grupo:
            isin = f["isin"]
            celda_isin = f"[{isin}](../{fichas[isin]})" if isin in fichas else isin
            gestion = "Indexada" if f["gestion"] == "indexada" else "Activa"
            rating = str(f["rating"]) if f["rating"] is not None else "—"
            nombre = (f["nombre"] or "—").replace("|", "\\|")
            lineas.append(
                f"| {celda_isin} | {nombre} | {gestion} | {f['divisa']} | {f['categoria']} "
                f"| {fmt(f['ter'])} | {fmt(f['r3a'])} | {f['srri'] if f['srri'] is not None else '—'} | {rating} |"
            )
    lineas += [
        "",
        "## Notas",
        "",
        "- «Gestión indexada» = columna Tipo «Fondos Indexados» de la app; el resto, «Fondos de inversión» (activa).",
        "- La columna «Div» del listado es la **divisa**, no la política de dividendos: acumulación/distribución queda pendiente.",
        "- ★ = rating Morningstar (1-5) que muestra la app; «—» = sin rating publicado.",
        "- Rentabilidades anualizadas en % (2026 = YTD). TER en %. SRRI en escala 1-7.",
        "- Los fondos con ficha MCP enlazan a ella; el resto solo tiene los datos de este listado.",
        "",
    ]
    return "\n".join(lineas)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--html", default=str(ROOT / "MyInvestor.html"))
    ap.add_argument("--dry-run", action="store_true", help="solo resumen, no escribe")
    args = ap.parse_args()

    html_path = Path(args.html)
    if not html_path.exists():
        print(f"ERROR: no existe {html_path}", file=sys.stderr)
        return 1
    fondos = parsear(html_path)
    fichas = fichas_mcp_existentes()
    for f in fondos:
        f["ficha_mcp"] = fichas.get(f["isin"])

    fecha = date.today().isoformat()
    por_clase = Counter(f["clase"] for f in fondos)
    por_tipo = Counter(f["tipo"] for f in fondos)
    faltantes = Counter()
    for f in fondos:
        for p in f["pendientes"]:
            faltantes[p] += 1

    print(f"Fondos únicos: {len(fondos)}")
    print(f"Por tipo: {dict(por_tipo)}")
    print("Por clase:")
    for clase in ORDEN_CLASES:
        if por_clase.get(clase):
            print(f"  {clase:15s} {por_clase[clase]}")
    print(f"Con ficha MCP previa: {sum(1 for f in fondos if f['ficha_mcp'])}")
    print(f"Campos pendientes (fondos afectados): {dict(faltantes)}")

    if args.dry_run:
        return 0

    DEST.mkdir(parents=True, exist_ok=True)
    doc = {
        "fuente": {
            "url": "https://newapp.myinvestor.es/app/explore/investments/funds/search",
            "fichero": html_path.name,
            "snapshot": fecha,
            "nota": "Página guardada manualmente por el titular; parseada sin acceso automatizado a MyInvestor.",
        },
        "campos_no_publicados": [
            "gestora", "acumulacion_distribucion", "composicion", "comision_gestion",
            "comision_exito", "minimos", "volatilidad", "rentabilidades_anos_naturales",
            "operativa", "fecha_nav",
        ],
        "total": len(fondos),
        "fondos": fondos,
    }
    (DEST / "fondos.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    (DEST / "catalogo.md").write_text(generar_catalogo(fondos, fecha, fichas), encoding="utf-8")
    print(f"Escrito: {DEST / 'fondos.json'} y {DEST / 'catalogo.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

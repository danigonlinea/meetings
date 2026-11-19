#!/usr/bin/env python3
"""Base de datos de fondos de acumulación del catálogo MyInvestor (MCP).

Genera una ficha markdown por fondo en `finance/fondos-myinvestor/<clase>/<ISIN>.md`,
clasificada por su papel en una cartera, más un `catalogo.md` índice y un
`estado.json` que permite reanudar el trabajo por lotes.

Solo fondos de ACUMULACIÓN (`distributing=false`): los que reparten dividendos
se excluyen por regla del titular.

Uso:
    python3 tools/fondos_myinvestor.py iniciar          # crea el estado y la frontera de búsqueda
    python3 tools/fondos_myinvestor.py lote             # procesa el siguiente lote (120 llamadas MCP)
    python3 tools/fondos_myinvestor.py lote --llamadas 60 --fondos 80
    python3 tools/fondos_myinvestor.py catalogo         # regenera solo el índice
    python3 tools/fondos_myinvestor.py estado           # progreso

Estrategia de enumeración: `search_funds` devuelve como mucho 10 fondos pero
informa de `total_found`. Se parte el catálogo por gestora (401 consultas, cada
fondo tiene gestora) y los buckets con más de 10 se subdividen por divisa,
gestión, tipo de activo, geografía, sector, capitalización y renta fija hasta
que cada hoja devuelve ≤10. Los ISIN se deduplican; la cobertura se audita
contra `total_found` global (2.197 acumulación a 2026-11-19).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from myinvestor_mcp import MCP, datos  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "finance" / "fondos-myinvestor"
ESTADO = DB / "estado.json"
CATALOGO = DB / "catalogo.md"

CLASES = [
    "monetarios", "renta-fija", "mixtos", "rv-global", "rv-usa", "rv-europa",
    "rv-japon", "rv-emergentes", "rv-otros", "sectoriales",
]
TITULOS_CLASE = {
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
}

# Dimensiones de subdivisión, en orden. Valores literales del catálogo.
DIM_ORDER = [
    "currency", "management_type", "asset_type", "geography", "sector",
    "market_cap", "fixed_income_type", "credit_quality", "max_ter",
]
DIM_VALUES = {
    "currency": ["EUR", "USD", "GBP", "CHF", "JPY", "AUD", "NOK"],
    "management_type": ["Active", "Index/Passive"],
    "asset_type": ["Renta Variable", "Renta Fija", "Mixto", "Monetario"],
    "market_cap": ["Large Cap", "Mid Cap", "Small Cap"],
    "credit_quality": ["Alto rendimiento"],
    "max_ter": [0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0],
}
# Dimensiones de match parcial: un hijo cuyo valor está contenido en el del
# padre no particiona (casa con un superconjunto) y se salta.
PARTIAL_DIMS = {"geography", "sector", "fixed_income_type", "credit_quality"}

EM_TOKENS = [
    "Mercados emergentes", "China", "India", "Brasil", "México", "Turquía",
    "África", "Vietnam", "Tailandia", "Indonesia", "Corea", "fronterizos",
    "América Latina", "Rusia", "Polonia",
]
EU_TOKENS = [
    "Europa", "España", "Alemania", "Francia", "Italia", "Reino Unido", "Suiza",
    "Noruega", "Suecia", "Nórdico", "Irlanda", "Portugal", "Países Bajos",
    "Bélgica", "Austria", "Dinamarca", "Finlandia", "Grecia", "Luxemburgo",
    "Islandia", "Malta", "Chipre", "Chequia", "Hungría", "Rumanía", "Bulgaria",
    "Croacia", "Eslovaquia", "Eslovenia", "Estonia", "Letonia", "Lituania",
    "Ucrania", "Serbia", "Albania", "Bosnia", "Macedonia", "Montenegro",
    "Kosovo", "Moldavia", "Bielorrusia", "Andorra", "Mónaco", "Liechtenstein",
    "Gibraltar", "Guernsey", "Jersey", "Isla de Man", "Islas Feroe",
    "San Marino", "Vaticano",
]

HOY = date.today().isoformat()


def ahora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# ---------------------------------------------------------------- clasificación

def clasificar(f: dict) -> str:
    at = f.get("asset_type") or ""
    if not at:
        # Fondos sin tipo declarado: se decide por la asignación real.
        eq, bo, ca = f.get("alloc_equity") or 0, f.get("alloc_bond") or 0, f.get("alloc_cash") or 0
        if ca >= 80:
            return "monetarios"
        if bo >= 60 and eq < 40:
            return "renta-fija"
        if eq >= 60:
            at = "Renta Variable"
        else:
            return "mixtos"
    if "Monetario" in at:
        return "monetarios"
    if "Mixto" in at:
        return "mixtos"
    if "Renta Fija" in at and "Renta Variable" not in at:
        return "renta-fija"
    if f.get("sector_or_theme"):
        return "sectoriales"
    geo = f.get("geography") or ""
    if "Global" in geo:
        return "rv-global"
    if any(t in geo for t in EM_TOKENS):
        return "rv-emergentes"
    if "USA" in geo:
        return "rv-usa"
    if "Japón" in geo:
        return "rv-japon"
    if any(t in geo for t in EU_TOKENS):
        return "rv-europa"
    return "rv-otros"


def papel(f: dict, clase: str) -> str:
    """Texto orientativo de papel en cartera, derivado de la clasificación."""
    idx = f.get("management_type") == "Index/Passive"
    base = {
        "monetarios": (
            "Aparcamiento de liquidez y fondo de emergencia: busca preservar el capital "
            "con volatilidad mínima y reembolso rápido. No es un motor de rentabilidad "
            "a largo plazo; su rendimiento sigue a los tipos del mercado monetario."
        ),
        "renta-fija": (
            "Tramo defensivo o de rentas de la cartera: aporta estabilidad frente a la "
            "bolsa y sensibilidad a los tipos de interés. El riesgo concreto depende del "
            "emisor (gubernamental o corporativo), la duración y la calidad crediticia "
            "que se detallan en la composición."
        ),
        "mixtos": (
            "Bolsa y bonos combinados en un solo fondo: perfil intermedio y delegación "
            "del reparto entre activos. Ojo al solapamiento: la parte de bolsa cuenta "
            "como renta variable a efectos del perfil de riesgo de la cartera."
        ),
        "rv-global": (
            "Candidato a núcleo de renta variable: exposición diversificada a la bolsa "
            "mundial en un solo fondo. "
            + ("Al ser indexado, busca replicar el mercado al coste mínimo; es el "
               "ladrillo típico de una cartera pasiva." if idx else
               "La gestión activa selecciona valores dentro del universo global: "
               "puede desviarse del índice en ambos sentidos y cobra más por ello.")
        ),
        "rv-usa": (
            "Exposición concentrada en la bolsa de EE. UU. Complementa o sustituye "
            "parcialmente a un núcleo global, pero un fondo global ya lleva una parte "
            "mayoritaria de EE. UU.: añadirlo aumenta el peso del país, no diversifica."
        ),
        "rv-europa": (
            "Exposición regional a la bolsa europea. Útil para sesgar la cartera hacia "
            "Europa frente a un núcleo global; concentra riesgo regional y divisa EUR."
        ),
        "rv-japon": (
            "Exposición regional a la bolsa japonesa. Satélite geográfico para sesgar "
            "la cartera hacia Japón; riesgo divisa JPY si la clase no está cubierta."
        ),
        "rv-emergentes": (
            "Satélite de crecimiento emergente: mayor potencial a largo plazo a cambio "
            "de más volatilidad y riesgo político, de divisa y de gobierno corporativo. "
            "Tamaño típico de posición minoritario dentro de la parte de bolsa."
        ),
        "rv-otros": (
            "Exposición regional o de área no cubierta por las categorías anteriores "
            "(Asia-Pacífico, Canadá, etc.). Satélite geográfico: revisar solapamiento "
            "con el núcleo global antes de añadirlo."
        ),
        "sectoriales": (
            "Satélite concentrado en un sector o temática: alta convicción y alta "
            "volatilidad relativa. No sustituye a un núcleo diversificado; el ciclo del "
            "sector puede dominar la rentabilidad durante años."
        ),
    }[clase]
    extras = []
    if f.get("fixed_income_credit_quality") and "Alto rendimiento" in f["fixed_income_credit_quality"]:
        extras.append(
            "Lleva crédito de alto rendimiento (high yield): más rentabilidad esperada "
            "a cambio de riesgo de impago y caídas fuertes en crisis."
        )
    if f.get("fixed_income_type") and "inflación" in f["fixed_income_type"]:
        extras.append("Indexado a la inflación: protege el poder adquisitivo del tramo defensivo.")
    if clase.startswith("rv-") and idx:
        extras.append("Gestión indexada: coste bajo y comportamiento pegado a su índice de referencia.")
    if f.get("sustainability_article") in (8, 9, "8", "9"):
        extras.append(f"Artículo {f['sustainability_article']} SFDR: promueve características ESG u objetivo sostenible.")
    return base + (" " + " ".join(extras) if extras else "")


# ---------------------------------------------------------------- render ficha

def num(v, dec=2):
    if v is None:
        return "—"
    try:
        return f"{float(v):,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (TypeError, ValueError):
        return str(v)


def pct(v, dec=2):
    return "—" if v is None else num(v, dec) + " %"


def lista_pct(items):
    if not items:
        return "—"
    return ", ".join(f"{i['name']} ({num(i['pct'], 1)} %)" for i in items)


def fecha_corta(v):
    if not v:
        return "—"
    return str(v)[:10]


def years_since(v):
    if not v:
        return None
    try:
        d = date.fromisoformat(str(v)[:10])
        return (date.today() - d).days / 365.25
    except ValueError:
        return None


def frontmatter(f: dict, clase: str) -> str:
    nombre = (f.get("name") or f["isin"]).replace('"', "'")
    gestora = (f.get("management_company") or "—").replace('"', "'")
    gestion = "indexado" if f.get("management_type") == "Index/Passive" else "activo"
    tags = [clase, gestion, (f.get("currency") or "—").lower()]
    if f.get("sector_or_theme"):
        tags.append("sectorial")
    lineas = [
        "---",
        f'title: "{nombre}"',
        f"date: {HOY}",
        "type: reference",
        "category: finance",
        f"tags: [{', '.join(tags)}]",
        "status: living",
        f"isin: {f['isin']}",
        f'gestora: "{gestora}"',
        f"clase: {clase}",
        f"ter: {f.get('ter') if f.get('ter') is not None else ''}",
        f"r3a: {round(f['return_3y'], 2) if f.get('return_3y') is not None else ''}",
        f"srri: {f.get('risk_indicator') if f.get('risk_indicator') is not None else ''}",
        "---",
    ]
    return "\n".join(lineas)


def render(f: dict) -> tuple[str, str]:
    """Devuelve (clase, markdown completo) de la ficha."""
    clase = clasificar(f)
    f = dict(f)
    nombre = f.get("name") or f["isin"]
    gestion = "indexada (pasiva)" if f.get("management_type") == "Index/Passive" else "activa"
    at = f.get("asset_type") or "tipo no declarado"
    geo = f.get("geography") or "geografía no declarada"
    sector = f.get("sector_or_theme")
    divisa = f.get("currency") or "—"
    gestora = f.get("management_company") or "—"
    anio = date.today().year

    p = [frontmatter(f, clase), "", f"# {nombre}", ""]
    p.append(
        f"`{f['isin']}` · {gestora} · {at} · {geo} · gestión {gestion} · divisa {divisa}"
    )
    p.append("")
    p.append("## Qué es y para qué sirve")
    p.append("")
    tipo = at.lower().replace("mixto, ", "mixto con ")
    prefijo = "de " if at.startswith("Renta") else ""
    resumen = (
        f"Fondo {prefijo}{tipo}"
        + (f" con foco en {geo}" if f.get("geography") else "")
        + f", de gestión {gestion}"
        + (f", sector/temática: {sector}" if sector else "")
        + f", comercializado en MyInvestor en clase de acumulación ({divisa})."
    )
    p.append(resumen)
    if f.get("inception_date"):
        p.append(f"Fecha de lanzamiento de la clase: {fecha_corta(f['inception_date'])}.")
    if f.get("description"):
        p.append("")
        p.append("> " + f["description"].replace("\n", "\n> "))
    p.append("")
    p.append("## Composición")
    p.append("")
    p.append("| Activo | % |")
    p.append("| --- | --- |")
    p.append(f"| Renta variable | {num(f.get('alloc_equity'), 1)} |")
    p.append(f"| Renta fija | {num(f.get('alloc_bond'), 1)} |")
    p.append(f"| Caja y equivalentes | {num(f.get('alloc_cash'), 1)} |")
    p.append(f"| Otros | {num(f.get('alloc_other'), 1)} |")
    p.append("")
    p.append(f"- **Top sectores:** {lista_pct(f.get('top_sectors'))}")
    p.append(f"- **Top regiones:** {lista_pct(f.get('top_regions'))}")
    p.append("- *El catálogo solo publica el top 6 de sectores y regiones; el resto del fondo no está desglosado.*")
    rf = []
    if f.get("fixed_income_type"):
        rf.append(f"tipo: {f['fixed_income_type']}")
    if f.get("fixed_income_term"):
        rf.append(f"plazo: {f['fixed_income_term']}")
    if f.get("fixed_income_credit_quality"):
        rf.append(f"calidad crediticia: {f['fixed_income_credit_quality']}")
    if rf:
        p.append(f"- **Renta fija:** {'; '.join(rf)}.")
    if f.get("market_capitalisation"):
        p.append(f"- **Capitalización:** {f['market_capitalisation']}.")
    if f.get("style"):
        p.append(f"- **Estilo:** {f['style']}.")
    p.append("")
    p.append("## Para qué vale en una cartera")
    p.append("")
    p.append(papel(f, clase))
    p.append("")
    p.append("*Orientación general derivada de la clasificación del catálogo; no es una recomendación de inversión.*")
    p.append("")
    p.append("## Comisiones")
    p.append("")
    p.append("| Concepto | Valor |")
    p.append("| --- | --- |")
    p.append(f"| TER (coste total anual) | {pct(f.get('ter'))} |")
    p.append(f"| Comisión de gestión | {pct(f.get('management_fee'))} |")
    p.append(f"| Comisión de éxito | {pct(f.get('performance_fee'))} |")
    p.append(f"| Mínimo inicial | {f.get('min_initial') or '—'} |")
    p.append(f"| Mínimo adicional | {f.get('min_followup') or '—'} |")
    p.append(f"| Mínimo de reembolso | {f.get('min_redemption') or '—'} |")
    p.append("")
    p.append("## Rentabilidad y riesgo")
    p.append("")
    p.append("| Período | Rentabilidad |")
    p.append("| --- | --- |")
    p.append(f"| YTD ({anio}) | {pct(f.get('ytd'))} |")
    p.append(f"| 1 año (trailing) | {pct(f.get('return_1y'))} |")
    p.append(f"| 3 años anualizada | {pct(f.get('return_3y'))} |")
    p.append(f"| 5 años anualizada | {pct(f.get('return_5y'))} |")
    for i in range(1, 6):
        p.append(f"| Año natural {anio - i} | {pct(f.get(f'return_past_{i}y'))} |")
    p.append("")
    p.append(
        f"- **Volatilidad:** 1A {pct(f.get('volatility_1y'))} · 3A {pct(f.get('volatility_3y'))} · 5A {pct(f.get('volatility_5y'))}"
    )
    p.append(f"- **Riesgo SRRI (1-7):** {f.get('risk_indicator') if f.get('risk_indicator') is not None else '—'}")
    p.append(f"- **NAV:** {num(f.get('nav'), f.get('nav_decimals') or 2)} {divisa} a {fecha_corta(f.get('nav_date'))}")
    p.append("")
    p.append("## Operativa")
    p.append("")
    p.append(
        f"- Hora de corte: {f.get('cutoff_time') or '—'} · suscripción en {f.get('subscription_lag_days') if f.get('subscription_lag_days') is not None else '—'} días · "
        f"reembolso en {f.get('redemption_lag_days') if f.get('redemption_lag_days') is not None else '—'} días · NAV con {f.get('nav_lag_days') if f.get('nav_lag_days') is not None else '—'} días de retraso."
    )
    if f.get("operation_mode"):
        p.append(f"- Modo de operación: {f['operation_mode']}.")
    if f.get("market"):
        p.append(f"- Mercado de referencia: {f['market']}.")
    p.append("")
    pegs = avisos(f)
    if pegs:
        p.append("## Pegas y avisos")
        p.append("")
        for a in pegs:
            p.append(f"- {a}")
        p.append("")
    p.append("## Fuente")
    p.append("")
    p.append(
        f"Catálogo de MyInvestor vía MCP (`mcp.myinvestor.es`), consultado el {HOY}. "
        "Rentabilidades pasadas no garantizan futuras. Los datos pueden cambiar; "
        "regenerar la ficha con `tools/fondos_myinvestor.py` si se necesita al día."
    )
    p.append("")
    return clase, "\n".join(p)


def avisos(f: dict) -> list[str]:
    out = []
    if f.get("warning_text"):
        out.append(f"⚠️ Aviso del catálogo: «{f['warning_text']}»")
    ter, gf = f.get("ter"), f.get("management_fee")
    if ter is None:
        out.append("TER no publicado en el catálogo: el coste total no está verificado.")
    elif gf is not None and ter < gf:
        out.append(
            f"El TER publicado ({num(ter)} %) es inferior a la comisión de gestión ({num(gf)} %): "
            "dato rebajado o estimado; el coste real puede ser mayor."
        )
    if f.get("performance_fee"):
        out.append(f"Cobra comisión de éxito del {num(f['performance_fee'])} % sobre plusvalías (además del TER).")
    edad = years_since(f.get("inception_date"))
    if edad is not None and edad < 3:
        out.append("Historial de la clase inferior a 3 años: no hay rentabilidad a 3A/5A que juzgar.")
    if (f.get("alloc_cash") or 0) >= 99 and "Renta Variable" in (f.get("asset_type") or ""):
        out.append("Cartera sin cargar (caja ≈100 %): lanzamiento reciente, exposición real pendiente.")
    return out


# ---------------------------------------------------------------- estado y lotes

def cargar_estado() -> dict:
    return json.loads(ESTADO.read_text(encoding="utf-8"))


def guardar_estado(e: dict) -> None:
    e["actualizado"] = ahora()
    tmp = ESTADO.with_suffix(".tmp")
    tmp.write_text(json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(ESTADO)


def iniciar() -> int:
    if ESTADO.exists():
        print("estado.json ya existe; usa `lote` para continuar o bórralo para reiniciar.")
        return 1
    mcp = MCP()
    mcp.init()
    r = mcp.tool("search_funds", {"distributing": False, "limit": 1})
    objetivo = (datos(r).get("data") or {}).get("total_found")
    if not objetivo:
        print("no se pudo obtener total_found", file=sys.stderr)
        return 1
    fac = mcp.tool("list_facets", {
        "dimensions": ["management_company", "geography", "sector", "fixed_income_type"],
        "top": 500,
    })
    fd = (datos(fac).get("data") or {}).get("facets") or {}
    gestoras = [(v["value"], v["count"]) for v in fd["management_company"]["values"]]
    gestoras.sort(key=lambda x: x[1])  # las pequeñas primero: fichas tempranas
    dims = dict(DIM_VALUES)
    dims["geography"] = [v["value"] for v in fd["geography"]["values"]]
    dims["sector"] = [v["value"] for v in fd["sector"]["values"]]
    dims["fixed_income_type"] = [v["value"] for v in fd["fixed_income_type"]["values"]]
    e = {
        "objetivo": objetivo,
        "creado": ahora(),
        "actualizado": ahora(),
        "dimensiones": dims,
        "frontera": [
            {"args": {"query": g, "distributing": False}, "dim_idx": 0, "etiqueta": g}
            for g, _ in gestoras
        ],
        "hechos": [],
        "sin_resolver": [],
        "gestoras_sin_match": [],
        "llamadas": 0,
        "completo": False,
    }
    DB.mkdir(parents=True, exist_ok=True)
    guardar_estado(e)
    print(f"iniciado: objetivo {objetivo} fondos de acumulación, {len(gestoras)} gestoras en la frontera.")
    return 0


def hijos(bucket: dict, dims: dict) -> list[dict]:
    """Subdivide un bucket con la siguiente dimensión útil."""
    args = bucket["args"]
    idx = bucket["dim_idx"]
    while idx < len(DIM_ORDER):
        dim = DIM_ORDER[idx]
        if dim in args and dim != "max_ter":
            idx += 1
            continue
        valores = dims.get(dim, [])
        utiles = []
        for v in valores:
            if dim in args:
                padre = args[dim]
                if dim == "max_ter":
                    if v >= padre:  # un tope mayor no particiona
                        continue
                elif isinstance(padre, str) and isinstance(v, str):
                    if v == padre or (dim in PARTIAL_DIMS and v in padre):
                        continue
            utiles.append(v)
        if utiles:
            return [
                {"args": {**args, dim: v}, "dim_idx": idx, "etiqueta": f"{bucket['etiqueta']} · {dim}={v}"}
                for v in utiles
            ]
        idx += 1
    return []


def escribir_ficha(f: dict) -> str:
    clase, md = render(f)
    destino = DB / clase / f"{f['isin']}.md"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(md, encoding="utf-8")
    return clase


def lote(llamadas: int, max_fondos: int) -> int:
    e = cargar_estado()
    if e.get("completo"):
        print(f"COMPLETO: {len(e['hechos'])}/{e['objetivo']} fichas. Nada que hacer.")
        return 0
    hechos = set(e["hechos"])
    dims = e["dimensiones"]
    frontera = e["frontera"]
    mcp = MCP()
    mcp.init()
    nuevas = 0
    usadas = 0
    fallos_seguidos = 0
    while frontera and usadas < llamadas and (not max_fondos or nuevas < max_fondos):
        bucket = frontera.pop(0)
        args = {**bucket["args"], "limit": 10}
        r = None
        for intento in range(3):
            try:
                r = mcp.tool("search_funds", args)
                if r and "result" in r:
                    break
                raise ValueError((r or {}).get("error", "respuesta vacía"))
            except Exception as exc:  # noqa: BLE001
                print(f"  reintento {intento + 1} ({bucket['etiqueta'][:60]}): {exc}", file=sys.stderr)
                time.sleep(2 * (intento + 1))
                try:
                    mcp = MCP()
                    mcp.init()
                except Exception:  # noqa: BLE001
                    pass
        usadas += 1
        e["llamadas"] += 1
        if not r or "result" not in r:
            fallos_seguidos += 1
            frontera.append(bucket)
            if fallos_seguidos >= 5:
                print("demasiados fallos seguidos; se guarda el estado y se aborta el lote.", file=sys.stderr)
                break
            continue
        fallos_seguidos = 0
        data = datos(r).get("data") or {}
        total = data.get("total_found") or 0
        funds = data.get("funds") or []
        if total == 0 and "query" in args and bucket["dim_idx"] == 0:
            e["gestoras_sin_match"].append(args["query"])
        for f in funds:
            if f.get("distributing"):
                continue
            if f["isin"] in hechos:
                continue
            escribir_ficha(f)
            hechos.add(f["isin"])
            nuevas += 1
        if total > 10:
            kids = hijos(bucket, dims)
            if kids:
                frontera.extend(kids)
            else:
                e["sin_resolver"].append({"etiqueta": bucket["etiqueta"], "args": bucket["args"], "total": total})
        if usadas % 10 == 0:
            e["hechos"] = sorted(hechos)
            e["frontera"] = frontera
            guardar_estado(e)
            print(f"  … {usadas} llamadas, {len(hechos)}/{e['objetivo']} fichas, {len(frontera)} buckets pendientes")
        time.sleep(0.25)
    e["hechos"] = sorted(hechos)
    e["frontera"] = frontera
    if not frontera and not e["sin_resolver"]:
        e["completo"] = len(hechos) >= e["objetivo"]
    guardar_estado(e)
    regenerar_catalogo(e)
    print(
        f"lote: +{nuevas} fichas en {usadas} llamadas · total {len(hechos)}/{e['objetivo']} · "
        f"frontera {len(frontera)} · sin resolver {len(e['sin_resolver'])} · "
        f"gestoras sin match {len(e['gestoras_sin_match'])}"
    )
    if e["completo"]:
        print("COMPLETO: base de datos terminada.")
    elif not frontera:
        print(f"ATENCIÓN: frontera vacía pero faltan {e['objetivo'] - len(hechos)} fondos; revisar sin_resolver y gestoras_sin_match.")
    return 0


# ---------------------------------------------------------------- catálogo

FM_KEYS = ("title", "isin", "gestora", "clase", "ter", "r3a", "srri", "date")


def leer_fm(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line.strip())
        if m and m.group(1) in FM_KEYS:
            out[m.group(1)] = m.group(2).strip().strip('"')
    return out


def regenerar_catalogo(e: dict | None = None) -> int:
    if e is None:
        e = cargar_estado()
    filas = []
    for path in DB.rglob("*.md"):
        if path.name in {"catalogo.md", "README.md"}:
            continue
        fm = leer_fm(path)
        if fm.get("isin"):
            fm["ruta"] = path.relative_to(DB).as_posix()
            filas.append(fm)
    por_clase = {c: [] for c in CLASES}
    for fm in filas:
        por_clase.setdefault(fm.get("clase", "rv-otros"), []).append(fm)

    def ter_key(fm):
        try:
            return (0, float(fm["ter"]))
        except (ValueError, KeyError):
            return (1, 0.0)

    lineas = [
        "---",
        'title: "Catálogo de fondos MyInvestor (acumulación)"',
        f"date: {HOY}",
        "type: reference",
        "category: finance",
        "tags: [fondos, myinvestor, catalogo, acumulacion]",
        "status: living",
        "---",
        "",
        "# Catálogo de fondos MyInvestor — solo acumulación",
        "",
        "Índice generado por `python3 tools/fondos_myinvestor.py catalogo`. No editar a mano.",
        "Fondos del catálogo MCP de MyInvestor que **no reparten dividendos** (clase de acumulación).",
        "Una ficha por fondo en `<clase>/<ISIN>.md`, con composición, comisiones, rentabilidad y papel en cartera.",
        "",
        f"**Fichas:** {len(filas)} de {e['objetivo']} · **Estado:** "
        + ("completo" if e.get("completo") else "en construcción por lotes")
        + f" · actualizado {e.get('actualizado', '—')}",
        "",
        "| Clase | Fichas |",
        "| --- | --- |",
    ]
    for c in CLASES:
        if por_clase.get(c):
            lineas.append(f"| [{TITULOS_CLASE[c]}](#{c}) | {len(por_clase[c])} |")
    lineas.append("")
    for c in CLASES:
        grupo = por_clase.get(c) or []
        if not grupo:
            continue
        grupo.sort(key=lambda fm: (ter_key(fm), fm.get("title", "")))
        lineas += [f"## {c}", "", f"### {TITULOS_CLASE[c]} ({len(grupo)})", "",
                   "| Ficha | Nombre | Gestora | TER | 3A anual. | SRRI |",
                   "| --- | --- | --- | --- | --- | --- |"]
        for fm in grupo:
            ter = fm.get("ter") or "—"
            r3a = fm.get("r3a") or "—"
            lineas.append(
                f"| [{fm['isin']}]({fm['ruta']}) | {fm.get('title', '—').replace('|', '/')} | "
                f"{fm.get('gestora', '—').replace('|', '/')} | {ter} | {r3a} | {fm.get('srri') or '—'} |"
            )
        lineas.append("")
    CATALOGO.write_text("\n".join(lineas), encoding="utf-8")
    return len(filas)


def fichas_manuales(isins: list[str]) -> int:
    """Escribe (o reescribe) fichas por ISIN exacto, vía get_funds. Auditoría."""
    e = cargar_estado()
    hechos = set(e["hechos"])
    mcp = MCP()
    mcp.init()
    escritas = 0
    for i in range(0, len(isins), 10):
        r = mcp.tool("get_funds", {"isins": isins[i:i + 10]})
        data = datos(r).get("data") or {}
        for f in data.get("funds") or []:
            if f.get("distributing"):
                print(f"  {f['isin']}: EXCLUIDO (distribuye dividendos)")
                continue
            escribir_ficha(f)
            hechos.add(f["isin"])
            escritas += 1
        for missing in data.get("missing") or []:
            print(f"  {missing}: no está en el catálogo")
    e["hechos"] = sorted(hechos)
    guardar_estado(e)
    regenerar_catalogo(e)
    print(f"fichas escritas: {escritas} · total {len(hechos)}/{e['objetivo']}")
    return 0


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("orden", choices=["iniciar", "lote", "catalogo", "estado", "fichas"])
    ap.add_argument("--llamadas", type=int, default=120)
    ap.add_argument("--fondos", type=int, default=0)
    ap.add_argument("isins", nargs="*", help="ISIN para la orden fichas")
    a = ap.parse_args(argv)
    if a.orden == "iniciar":
        return iniciar()
    if a.orden == "lote":
        return lote(a.llamadas, a.fondos)
    if a.orden == "fichas":
        return fichas_manuales(a.isins)
    if a.orden == "catalogo":
        n = regenerar_catalogo()
        print(f"catalogo.md regenerado: {n} fichas")
        return 0
    e = cargar_estado()
    print(json.dumps({
        "objetivo": e["objetivo"],
        "fichas": len(e["hechos"]),
        "frontera": len(e["frontera"]),
        "llamadas": e["llamadas"],
        "sin_resolver": len(e["sin_resolver"]),
        "gestoras_sin_match": len(e["gestoras_sin_match"]),
        "completo": e["completo"],
        "actualizado": e["actualizado"],
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

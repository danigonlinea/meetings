#!/usr/bin/env python3
"""Termómetro de cartera: re-puntúa las ocho señales de `propuesta-actual.md` §2.

Uso:
    python3 tools/termometro.py                 # con finance/portfolio/termometro-datos.json
    python3 tools/termometro.py --rv 45         # simula otro % de renta variable
    python3 tools/termometro.py --check         # solo comprobaciones (sale 1 si algo no cuadra)

Para qué sirve: el % de RV de la cartera sale de ocho señales con peso (45 % de base más la suma de
las señales). Cada trimestre se vuelven a puntuar y el termómetro dice si el 55 % escrito sigue
saliendo de los datos o si toca revisarlo. No decide: mueve la aritmética y avisa de las incoherencias.

Comprueba tres cosas:
  1. Que la suma de las señales del JSON da el % de RV declarado (base + suma = rv_pct).
  2. Que cada señal sigue coherente con el dato que la activa (carry, HY, prima RV-bono, inflación).
  3. La tabla de caída y retorno para cada nivel de RV, con las fórmulas de §2 del documento.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "finance" / "portfolio" / "termometro-datos.json"

# Señales de §2, en el orden del documento: clave en el JSON, etiqueta y umbral que la haría cambiar.
SENALES = [
    ("coste_real", "Coste real del dinero", "RF por debajo de la inflación"),
    ("prima_credito", "Prima de crédito", "HY OAS > 700 pb"),
    ("valoracion", "Valoración relativa", "S&P 500 −20 % con beneficios intactos"),
    ("concentracion", "Concentración y ciclo de crédito", "evento de crédito materializado"),
    ("riesgo_tipos", "Riesgo de tipos", "inflación < 2 % y BCE bajando"),
    ("aguante", "Capacidad de aguante", "si la caída no se aguanta"),
    ("carry_cobrado", "Carry cobrado de la RF", "por debajo del 2 % a 12 meses"),
    ("prima_rv_bono", "Prima RV-bono", "earnings yield − bono < 1 pp"),
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def drawdown(rv: float) -> float:
    """Caída en un escenario tipo 2008: RV −40 %, RF −3 % (§2 del documento)."""
    return -(0.40 * rv + 0.03 * (100 - rv))


def expected_return(rv: float, ey: float, rf: float, growth: float = 0.0) -> float:
    """RV × earnings yield + RF × carry. Con `growth`, se suma al EY de la RV."""
    return rv / 100 * (ey + growth) + (100 - rv) / 100 * rf


def pct(value: float, digits: int = 2) -> str:
    return f"{value:+.{digits}f}%"


def pts(value: int) -> str:
    return f"{value:+d}" if value else "0"


def checks(d: dict) -> list[str]:
    """Incoherencias entre el dato y los puntos escritos en el JSON."""
    out = []
    s = d["senales"]
    total = sum(s.values())
    if abs(d["base_rv"] + total - d["rv_pct"]) > 0.05:
        out.append(
            f"la suma de señales da {total:+d} y el documento declara {d['rv_pct']:.1f} % "
            f"(base {d['base_rv']:.0f} % + {total:+d} = {d['base_rv'] + total:.0f} %): repuntuar §2"
        )
    if d["rf_cobrado"] < 2 and s["carry_cobrado"] != 3:
        out.append(
            f"la RF cobró {d['rf_cobrado']:.2f} % (<2 %) pero carry_cobrado está en "
            f"{s['carry_cobrado']:+d}: §11.1 pide +3"
        )
    if d["rf_cobrado"] >= 2 and s["carry_cobrado"] == 3:
        out.append(
            f"la RF cobra {d['rf_cobrado']:.2f} % (≥2 %) pero carry_cobrado sigue en +3: la señal caducó"
        )
    if d["hy_oas_pb"] > 700 and s["prima_credito"] > 0:
        out.append(
            f"HY OAS {d['hy_oas_pb']} pb (>700) pero prima_credito sigue en {s['prima_credito']:+d}"
        )
    erp = d["ey_cartera"] - d["bono_10y"]
    if erp < 1 and s["prima_rv_bono"] > -10:
        out.append(
            f"prima RV-bono {erp:+.2f} pp (<1) pero prima_rv_bono está en "
            f"{s['prima_rv_bono']:+d}: §11 pide −10"
        )
    if d["inflacion"] < 2 and s["riesgo_tipos"] > 0:
        out.append(
            f"inflación {d['inflacion']:.1f} % (<2) pero riesgo_tipos sigue en {s['riesgo_tipos']:+d}"
        )
    return out


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Termómetro de cartera")
    parser.add_argument("--rv", type=float, help="porcentaje de renta variable a simular")
    parser.add_argument("--datos", type=Path, default=DATA)
    parser.add_argument("--check", action="store_true", help="solo comprobaciones; sale 1 si falla")
    args = parser.parse_args(argv)

    d = load(args.datos)
    rv = args.rv if args.rv is not None else d["rv_pct"]
    ey, rf, inflacion = d["ey_cartera"], d["rf_ytw"], d["inflacion"]
    s = d["senales"]
    total = sum(s.values())
    problemas = checks(d)

    if args.check:
        for p in problemas:
            print(f"❌ {p}")
        if not problemas:
            print(
                f"✅ {d['fecha']}: base {d['base_rv']:.0f} % {total:+d} = {d['rv_pct']:.1f} % de RV; "
                "señales coherentes con los datos"
            )
        return 1 if problemas else 0

    print(f"## Termómetro · {d['fecha']}\n")
    print("| Señal | Dato de hoy | Puntos | Cambia si |")
    print("| --- | --- | ---: | --- |")
    datos = {
        "coste_real": (
            f"RF {d['rf_ytw']:.2f} % YTW / {d['rf_cobrado']:.2f} % cobrado · "
            f"€STR {d['estr']:.2f} % · inflación {inflacion:.1f} %"
        ),
        "prima_credito": f"HY OAS {d['hy_oas_pb']} pb · BB {d['bb_oas_pb']} pb",
        "valoracion": (
            f"S&P {d['sp500_per']:.1f}x · STOXX {d['stoxx600_per']:.1f}x · EM {d['em_per']:.1f}x"
        ),
        "concentracion": "46 % del S&P en tecnología (dato del corpus)",
        "riesgo_tipos": "BCE restrictivo, depósito 2,50 %",
        "aguante": "colchón fuera, horizonte largo",
        "carry_cobrado": f"{d['rf_cobrado']:.2f} % cobrado a 12 meses",
        "prima_rv_bono": f"EY {ey:.2f} % − bono {d['bono_10y']:.2f} % = {ey - d['bono_10y']:+.2f} pp",
    }
    for key, etiqueta, umbral in SENALES:
        print(f"| {etiqueta} | {datos[key]} | {pts(s[key])} | {umbral} |")
    print(
        f"| | **Suma** | **{total:+d}** | base {d['base_rv']:.0f} % {total:+d} = "
        f"**{d['base_rv'] + total:.0f} %** |"
    )

    print("\n### Derivados\n")
    print(
        f"- Earnings yield S&P 500: {100 / d['sp500_per']:.2f} % ({d['sp500_per']:.1f}x) · "
        f"cartera: {ey:.2f} %"
    )
    print(
        f"- Earnings yield STOXX 600: {100 / d['stoxx600_per']:.2f} % · "
        f"EM: {100 / d['em_per']:.2f} %"
    )
    print(
        f"- RF en términos reales: {pct(d['rf_cobrado'] - inflacion)} cobrado · "
        f"{pct(d['rf_ytw'] - inflacion)} con el YTW"
    )
    print(f"- Prima de riesgo de la RV: {ey - d['bono_10y']:+.2f} pp")

    print("\n### Comprobaciones\n")
    if problemas:
        for p in problemas:
            print(f"- ❌ {p}")
    else:
        print("- ✅ la suma de señales cuadra con el % de RV y cada señal es coherente con su dato")

    print(f"\n### Consecuencias con {rv:.1f} % de RV\n")
    print("| RV | Caída tipo 2008 | Retorno (EY) | Retorno (EY + 4 %) |")
    print("| ---: | ---: | ---: | ---: |")
    for level in sorted({35.0, 45.0, 50.0, 55.0, 60.0, rv}):
        print(
            f"| {level:.1f} % | {drawdown(level):.1f} % | {expected_return(level, ey, rf):.2f} % | "
            f"{expected_return(level, ey, rf, 4.0):.2f} % |"
        )
    print(f"\n> {d['fuente']}. Modelo de §2, no un backtest. El % de RV lo decide el titular.")
    return 1 if problemas else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

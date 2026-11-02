#!/usr/bin/env python3
"""Termómetro de cartera: hace la aritmética de `propuesta-actual.md` §2 y §10.

Uso:
    python3 tools/termometro.py                 # con finance/portfolio/termometro-datos.json
    python3 tools/termometro.py --rv 45         # simula otro % de renta variable

No decide: calcula. El `%` de RV sigue siendo un juicio escrito en la propuesta.
Las fórmulas de caída y retorno son las del documento (modelo propio, no backtest).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "finance" / "portfolio" / "termometro-datos.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def pct(value: float, digits: int = 2) -> str:
    return f"{value:+.{digits}f}%"


def drawdown(rv: float) -> float:
    """Caída estimada en un escenario tipo 2008 (≈ −16% con 35% RV, −27% con 65%)."""
    return -(0.35 * rv + 4)


def expected_return(rv: float) -> float:
    """Retorno nominal esperado del modelo (5,4% con 35% RV, 6,0% con 65%)."""
    return 5.4 + 0.02 * (rv - 35)


def signals(d: dict) -> list[tuple[str, str, str]]:
    """(señal, dato de hoy, umbral del §10 que la haría cambiar de signo)."""
    inflacion = d["inflacion"]
    real_rf = d["rf_cartera"] - inflacion
    real_cash = d["estr"] - inflacion
    ey_sp = 100 / d["sp500_per"]
    ey_eu = 100 / d["stoxx600_per"]
    ey_em = 100 / d["em_per"]
    rows = [
        (
            "Coste real del dinero",
            f"RF de la cartera {real_rf:+.2f}% real (€STR {real_cash:+.2f}%)",
            "RF por debajo de la inflación",
        ),
        (
            "Prima de crédito",
            f"HY OAS {d['hy_oas_pb']} pb · BB {d['bb_oas_pb']} pb",
            "HY OAS > 700 pb",
        ),
        (
            "Valoración relativa",
            f"S&P {d['sp500_per']:.1f}x · STOXX {d['stoxx600_per']:.1f}x · EM {d['em_per']:.1f}x",
            "S&P −20% con beneficios intactos",
        ),
        (
            "Concentración y ciclo de crédito",
            "46% tech en el S&P (juicio, no dato del JSON)",
            "evento de crédito materializado",
        ),
        (
            "Riesgo de tipos",
            "BCE restrictivo (juicio, no dato del JSON)",
            "inflación < 2% y BCE bajando",
        ),
        (
            "Capacidad de aguante",
            "colchón fuera de la cartera, horizonte largo",
            "si el drawdown no se aguanta",
        ),
    ]
    if d.get("bono_10y"):
        erp = ey_sp - d["bono_10y"]
        rows.append(
            ("Prima de riesgo de la RV", f"earnings yield − bono = {erp:+.2f} pp", "ERP < 1 pp")
        )
    return rows


def triggers(d: dict) -> list[str]:
    out = []
    inflacion = d["inflacion"]
    if d["rf_cartera"] < inflacion:
        out.append("RF de la cartera por debajo de la inflación → +3 puntos de RV")
    if d["hy_oas_pb"] > 700:
        out.append("HY OAS > 700 pb → vuelve la prima de crédito (−3 puntos)")
    if inflacion < 2:
        out.append("inflación < 2% → confirmar que el BCE baja antes de aplicar −3")
    if d.get("bono_10y") and 100 / d["sp500_per"] - d["bono_10y"] < 1:
        out.append("prima de riesgo de la RV < 1 pp → −10 puntos")
    return out or ["ningún umbral del §10 cruzado"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Termómetro de cartera")
    parser.add_argument("--rv", type=float, help="% de renta variable a simular")
    parser.add_argument("--datos", type=Path, default=DATA)
    args = parser.parse_args()

    d = load(args.datos)
    rv = args.rv if args.rv is not None else d["rv_pct"]
    inflacion = d["inflacion"]
    real_rf = d["rf_cartera"] - inflacion

    print(f"## Termómetro · {d['fecha']}\n")
    print("| Señal | Dato | Cambia si |")
    print("| --- | --- | --- |")
    for name, value, threshold in signals(d):
        print(f"| {name} | {value} | {threshold} |")

    print("\n### Derivados\n")
    ey_sp = 100 / d["sp500_per"]
    print(f"- Earnings yield S&P 500: {ey_sp:.2f}% ({d['sp500_per']:.1f}x)")
    print(f"- Earnings yield STOXX 600: {100 / d['stoxx600_per']:.2f}%")
    print(f"- Earnings yield EM: {100 / d['em_per']:.2f}%")
    print(f"- RF de la cartera en términos reales: {pct(real_rf)}")
    if d.get("bono_10y"):
        print(f"- Prima de riesgo de la RV: {ey_sp - d['bono_10y']:+.2f} pp")
    else:
        print("- Prima de riesgo de la RV: sin dato (`bono_10y` vacío)")

    print("\n### Umbrales\n")
    for line in triggers(d):
        print(f"- {line}")

    print(f"\n### Consecuencias con {rv:.1f}% de RV\n")
    print("| RV | Caída tipo 2008 | Retorno esperado | Real sobre inflación |")
    print("| ---: | ---: | ---: | ---: |")
    for level in sorted({35, 45, rv, 55, 65}):
        r = expected_return(level)
        print(f"| {level:.1f}% | {drawdown(level):.1f}% | {r:.1f}% | {pct(r - inflacion, 1)} |")

    print("\n> Modelo del documento §2, no un backtest. La decisión del % de RV no sale de aquí.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

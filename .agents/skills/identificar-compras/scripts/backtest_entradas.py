#!/usr/bin/env python3
"""Backtest de la regla de entrada de la skill `identificar-compras`.

Regla base (V2): vela de entrada = mínimo superior al anterior + cierre positivo + volumen > 1,5x
la media de 20. Entrada al cierre de esa vela; stop en el mínimo de la vela; objetivo a R múltiplos
(configurable); horizonte de N velas. Si en la misma vela toca stop y objetivo, se cuenta como pérdida
(criterio conservador).

Variantes:
  V2  solo la vela de entrada con volumen
  V3  V2 + sesgo mensual (cierre por encima de la EMA20 del último mes cerrado)
  V4  V3 + confirmación diaria (cierre sobre EMA9 y EMA20 y parabólica alcista)
  BASE  todas las velas con la misma regla de stop/objetivo (control)

Uso:
    python3 backtest_entradas.py
    python3 backtest_entradas.py --rr 3 --horizonte 30
"""
import argparse
import datetime
import json
import statistics
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
SIMBOLOS = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT",
            "ADAUSDT", "AVAXUSDT", "LINKUSDT", "DOGEUSDT", "QNTUSDT"]


def klines(symbol, interval, limit):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=25) as r:
        raw = json.load(r)
    return [{"t": k[0], "o": float(k[1]), "h": float(k[2]), "l": float(k[3]),
             "c": float(k[4]), "v": float(k[5])} for k in raw]


def ema(v, p):
    out = [None] * len(v)
    if len(v) < p:
        return out
    k = 2 / (p + 1)
    out[p - 1] = sum(v[:p]) / p
    for i in range(p, len(v)):
        out[i] = v[i] * k + out[i - 1] * (1 - k)
    return out


def psar(h, l, step=0.02, mx=0.2):
    n = len(h)
    sar, bull = [None] * n, [None] * n
    up = h[0] >= l[0]
    sar[0], bull[0] = (l[0] if up else h[0]), up
    ep, af = (h[0] if up else l[0]), step
    for i in range(1, n):
        val = sar[i - 1] + af * (ep - sar[i - 1])
        if up:
            val = min(val, l[i - 1], l[i - 2] if i > 1 else l[i - 1])
            if l[i] < val:
                up, val, ep, af = False, ep, l[i], step
            elif h[i] > ep:
                ep, af = h[i], min(af + step, mx)
        else:
            val = max(val, h[i - 1], h[i - 2] if i > 1 else h[i - 1])
            if h[i] > val:
                up, val, ep, af = True, ep, h[i], step
            elif l[i] < ep:
                ep, af = l[i], min(af + step, mx)
        sar[i], bull[i] = val, up
    return sar, bull


def sesgo_mensual(symbol):
    """Devuelve lista de (timestamp_inicio_mes, ema20_mensual) del último mes CERRADO."""
    m = klines(symbol, "1M", 60)
    closes = [x["c"] for x in m]
    e20 = ema(closes, 20)
    return [(m[i]["t"], e20[i]) for i in range(len(m)) if e20[i]]


def evaluar(rows, i, rr, horizonte):
    """Simula una entrada en el cierre de la vela i. Devuelve R realizado."""
    entrada, stop = rows[i]["c"], rows[i]["l"]
    riesgo = entrada - stop
    if riesgo <= 0:
        return None
    objetivo = entrada + rr * riesgo
    fin = min(i + horizonte, len(rows) - 1)
    for j in range(i + 1, fin + 1):
        toca_stop = rows[j]["l"] <= stop
        toca_obj = rows[j]["h"] >= objetivo
        if toca_stop and toca_obj:
            return -1.0          # mismo barrido: conservador
        if toca_stop:
            return -1.0
        if toca_obj:
            return float(rr)
    return (rows[fin]["c"] - entrada) / riesgo


def backtest(symbol, rr, horizonte):
    d = klines(symbol, "1d", 1000)
    if len(d) < 260:
        return None
    c = [x["c"] for x in d]
    h = [x["h"] for x in d]
    l = [x["l"] for x in d]
    v = [x["v"] for x in d]
    e9, e20 = ema(c, 9), ema(c, 20)
    e200 = ema(c, 200)
    _, bull = psar(h, l)
    mens = sesgo_mensual(symbol)

    def sesgo(ts):
        vig = None
        for mt, val in mens:
            if mt <= ts:
                vig = val
            else:
                break
        return vig

    out = {"V2": [], "V3": [], "V4": [], "V5": [], "BASE": []}
    riesgos = []
    for i in range(25, len(d) - horizonte - 1):
        v20 = statistics.fmean(v[i - 19:i + 1])
        r = d[i]
        vela = r["l"] > d[i - 1]["l"] and r["c"] > r["o"] and r["v"] > 1.5 * v20
        base = True
        if vela:
            res = evaluar(d, i, rr, horizonte)
            riesgos.append((r["c"] - r["l"]) / r["c"] * 100)
            if res is not None:
                out["V2"].append((symbol, r["t"], res))
                sm = sesgo(r["t"])
                if e200[i] and r["c"] > e200[i]:
                    out["V5"].append((symbol, r["t"], res))
                if sm and r["c"] > sm:
                    out["V3"].append((symbol, r["t"], res))
                    if e9[i] and e20[i] and r["c"] > e9[i] and r["c"] > e20[i] and bull[i]:
                        out["V4"].append((symbol, r["t"], res))
        if base and i % 3 == 0:          # control: un día de cada tres
            res = evaluar(d, i, rr, horizonte)
            if res is not None:
                out["BASE"].append((symbol, r["t"], res))
    out["_riesgo"] = statistics.fmean(riesgos) if riesgos else None
    return out


def resumen(nombre, trades):
    if not trades:
        print(f"{nombre:6s} sin operaciones")
        return
    rs = [t[2] for t in trades]
    gan = sum(1 for x in rs if x > 0)
    print(f"{nombre:6s} n={len(rs):4d}  acierto {100*gan/len(rs):5.1f}%  "
          f"R medio {statistics.fmean(rs):+5.2f}  R total {sum(rs):+8.1f}  "
          f"mediana {statistics.median(rs):+5.2f}  mejor {max(rs):+5.1f}  peor {min(rs):+5.1f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rr", type=float, default=2.0)
    ap.add_argument("--horizonte", type=int, default=20)
    a = ap.parse_args()
    todo = {"V2": [], "V3": [], "V4": [], "V5": [], "BASE": []}
    riesgos = []
    print(f"Objetivo {a.rr}R · horizonte {a.horizonte} velas · stop en el mínimo de la vela de entrada\n")
    for s in SIMBOLOS:
        try:
            out = backtest(s, a.rr, a.horizonte)
        except Exception as e:
            print(f"{s}: error {e}")
            continue
        if not out:
            continue
        for k in todo:
            todo[k] += out[k]
        if out.get("_riesgo"):
            riesgos.append(out["_riesgo"])
        resumen(s, out["V2"])
    print("-" * 86)
    for k in ("BASE", "V2", "V3", "V4", "V5"):
        resumen(k, todo[k])
    if riesgos:
        print(f"\nRiesgo medio (entrada-mínimo de la vela): {statistics.fmean(riesgos):.1f}% del precio")
    print("\nDetalle de las 6 mejores y 6 peores de V3:")
    v3 = sorted(todo["V3"], key=lambda t: -t[2])
    for sym, ts, r in v3[:6] + v3[-6:]:
        import datetime
        f = datetime.datetime.fromtimestamp(ts / 1000, datetime.timezone.utc).strftime("%Y-%m-%d")
        print(f"  {sym:9s} {f}  {r:+.2f}R")


if __name__ == "__main__":
    main()

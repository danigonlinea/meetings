#!/usr/bin/env python3
"""Backtest de la regla de entrada de la skill `identificar-compras`.

Regla base (V2): vela de entrada = mínimo superior al anterior + cierre positivo + volumen > 1,5x
la media de las 20 velas ANTERIORES (sin contar la propia vela). Entrada al cierre de esa vela;
stop en el mínimo de la vela; objetivo a R múltiplos (configurable); horizonte de N velas.
Si en la misma vela toca stop y objetivo, se cuenta como pérdida (criterio conservador).

Variantes:
  BASE  todas las velas con la misma regla de stop/objetivo (control, una de cada tres)
  V2    solo la vela de entrada con volumen
  V3    V2 + sesgo mensual (cierre por encima de la EMA20 del último mes CERRADO)
  V4    V3 + confirmación diaria (cierre sobre EMA9 y EMA20 y parabólica alcista)
  V5    V2 + EMA200 diaria  ← la regla de la skill
  V6    V5 con subida <100 % en 30 velas
  V7    V5 con subida <150 % en 30 velas

Honestidad de la muestra: las señales se solapan (dos entradas a menos de `horizonte` velas
comparten horizonte), así que la columna `episodios` cuenta los grupos independientes y es el n
que hay que citar. El backtest NO mete costes salvo que se pase --coste.

Uso:
    python3 backtest_entradas.py
    python3 backtest_entradas.py --rr 3 --horizonte 30
    python3 backtest_entradas.py --rr 2 --ultimos-meses 12
    python3 backtest_entradas.py --rr 2 --coste 0.2      # comisión+deslizamiento ida y vuelta, %
"""
import argparse
import datetime
import json
import statistics
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}
SIMBOLOS = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT",
            "ADAUSDT", "AVAXUSDT", "LINKUSDT", "DOGEUSDT", "QNTUSDT"]

DIA_MS = 86400000
BARRAS_DIARIAS = 1600      # margen de calentamiento para la EMA200
INICIO = 400               # primera vela evaluable: 200 del seed + 200 de calentamiento


def klines(symbol, interval, limit, end_ms=None):
    url = (f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"
           f"&limit={limit}" + (f"&endTime={end_ms}" if end_ms else ""))
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = json.load(r)
    return [{"t": int(k[0]), "o": float(k[1]), "h": float(k[2]), "l": float(k[3]),
             "c": float(k[4]), "v": float(k[5])} for k in raw]


def klines_diarias(symbol, total=BARRAS_DIARIAS):
    """Paginado hacia atrás: Binance devuelve 1.000 velas por petición."""
    out, end = [], None
    while len(out) < total:
        lote = klines(symbol, "1d", 1000, end)
        if not lote:
            break
        out = lote + out
        end = lote[0]["t"] - 1
        if len(lote) < 1000:
            break
    return out[-total:]


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
    """[(inicio_de_mes, EMA20 del mes CERRADO anterior)].

    La EMA20 del mes en curso no se conoce hasta que el mes cierra, así que una vela diaria del
    mes M solo puede usar la EMA del mes M-1. Antes se usaba la del mes en curso = look-ahead.
    """
    m = klines(symbol, "1M", 100)
    e20 = ema([x["c"] for x in m], 20)
    return [(m[i]["t"], e20[i - 1]) for i in range(1, len(m)) if e20[i - 1]]


def evaluar(rows, i, rr, horizonte):
    """Simula una entrada en el cierre de la vela i. Devuelve R realizado."""
    entrada, stop = rows[i]["c"], rows[i]["l"]
    riesgo = entrada - stop
    if riesgo <= 0:
        return None
    objetivo = entrada + rr * riesgo
    fin = min(i + horizonte, len(rows) - 1)
    for j in range(i + 1, fin + 1):
        if rows[j]["l"] <= stop:
            return -1.0            # si toca los dos en la misma vela, se cuenta pérdida
        if rows[j]["h"] >= objetivo:
            return float(rr)
    return (rows[fin]["c"] - entrada) / riesgo


def backtest(symbol, rr, horizonte, coste):
    d = klines_diarias(symbol)
    if len(d) < INICIO + horizonte + 2:
        return None, f"serie corta ({len(d)} velas)"
    c = [x["c"] for x in d]
    h = [x["h"] for x in d]
    l = [x["l"] for x in d]
    v = [x["v"] for x in d]
    e9, e20, e200 = ema(c, 9), ema(c, 20), ema(c, 200)
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

    out = {k: [] for k in ("V2", "V3", "V4", "V5", "V6", "V7", "BASE")}
    riesgos = []
    for i in range(INICIO, len(d) - horizonte - 1):
        r = d[i]
        v20 = statistics.fmean(v[i - 20:i])         # 20 velas anteriores, sin la actual
        vela = r["l"] > d[i - 1]["l"] and r["c"] > r["o"] and r["v"] > 1.5 * v20
        if vela:
            res = evaluar(d, i, rr, horizonte)
            if res is not None:
                riesgo_pct = (r["c"] - r["l"]) / r["c"] * 100
                riesgos.append(riesgo_pct)
                t = (symbol, r["t"], res - coste / riesgo_pct if coste else res, riesgo_pct)
                out["V2"].append(t)
                sm = sesgo(r["t"])
                if e200[i] and r["c"] > e200[i]:
                    out["V5"].append(t)
                    mom30 = c[i] / c[i - 30] - 1 if i >= 30 else 99
                    if mom30 < 1.0:          # subida <100 % en 30 velas = ruptura, no vertical
                        out["V6"].append(t)
                    if mom30 < 1.5:
                        out["V7"].append(t)
                if sm and r["c"] > sm:
                    out["V3"].append(t)
                    if e9[i] and e20[i] and r["c"] > e9[i] and r["c"] > e20[i] and bull[i]:
                        out["V4"].append(t)
        if i % 3 == 0:          # control: un día de cada tres
            res = evaluar(d, i, rr, horizonte)
            if res is not None:
                riesgo_pct = (r["c"] - r["l"]) / r["c"] * 100
                out["BASE"].append((symbol, r["t"],
                                    res - coste / riesgo_pct if coste else res, riesgo_pct))
    out["_riesgo"] = statistics.fmean(riesgos) if riesgos else None
    return out, None


def episodios(trades, horizonte):
    """Agrupa señales solapadas (misma racha a menos de `horizonte` velas) = muestra independiente."""
    ts = sorted(trades, key=lambda t: (t[0], t[1]))
    grupos, ini, sym = [], None, None
    for t in ts:
        if sym != t[0] or ini is None or t[1] - ini > horizonte * DIA_MS:
            grupos.append([t])
            ini, sym = t[1], t[0]
        else:
            grupos[-1].append(t)
    return grupos


def resumen(nombre, trades, horizonte=None):
    if not trades:
        print(f"{nombre:8s} sin operaciones")
        return
    rs = [t[2] for t in trades]
    gan = sum(1 for x in rs if x > 0)
    extra = ""
    if horizonte:
        eps = episodios(trades, horizonte)
        extra = (f"  episodios {len(eps):4d}  R 1º del episodio "
                 f"{statistics.fmean([e[0][2] for e in eps]):+5.2f}")
    print(f"{nombre:8s} n={len(rs):4d}  acierto {100*gan/len(rs):5.1f}%  "
          f"R medio {statistics.fmean(rs):+5.3f}  R total {sum(rs):+8.1f}  "
          f"mediana {statistics.median(rs):+5.2f}{extra}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rr", type=float, default=2.0)
    ap.add_argument("--horizonte", type=int, default=20)
    ap.add_argument("--desde", help="solo operaciones con fecha >= YYYY-MM-DD")
    ap.add_argument("--ultimos-meses", type=int,
                    help="atajo de --desde: últimos N meses contados desde hoy (no caduca)")
    ap.add_argument("--coste", type=float, default=0.0,
                    help="comisión + deslizamiento ida y vuelta, en %% del precio (0.2 típico)")
    a = ap.parse_args()

    desde = a.desde
    if a.ultimos_meses:
        desde = (datetime.datetime.now(datetime.timezone.utc)
                 - datetime.timedelta(days=round(30.44 * a.ultimos_meses))).strftime("%Y-%m-%d")

    todo = {k: [] for k in ("V2", "V3", "V4", "V5", "V6", "V7", "BASE")}
    riesgos = []
    print(f"Objetivo {a.rr}R · horizonte {a.horizonte} velas · stop en el mínimo de la vela de entrada"
          f"{f' · coste {a.coste}% ida y vuelta' if a.coste else ' · SIN costes'}"
          f"{f' · desde {desde}' if desde else ''}\n")
    for s in SIMBOLOS:
        try:
            out, err = backtest(s, a.rr, a.horizonte, a.coste)
        except Exception as e:
            print(f"{s}: error {e}")
            continue
        if not out:
            print(f"{s}: {err}")
            continue
        for k in todo:
            todo[k] += out[k]
        if out["_riesgo"]:
            riesgos.append(out["_riesgo"])
        resumen(s, out["V5"])
    print("-" * 112)
    if desde:
        for k in todo:
            todo[k] = [x for x in todo[k]
                       if datetime.datetime.fromtimestamp(x[1] / 1000, datetime.timezone.utc)
                       .strftime("%Y-%m-%d") >= desde]
    for k in ("BASE", "V2", "V3", "V4", "V5", "V6", "V7"):
        resumen(k, todo[k], a.horizonte)
    if riesgos:
        print(f"\nRiesgo medio (entrada-mínimo de la vela): {statistics.fmean(riesgos):.1f}% del precio")
    print("\nDispersión de V5 por par:")
    for s in SIMBOLOS:
        sub = [t for t in todo["V5"] if t[0] == s]
        if sub:
            resumen(f"  {s}", sub)
    v3 = sorted(todo["V3"], key=lambda t: -t[2])
    if v3:
        print("\nDetalle de las 6 mejores y 6 peores de V3:")
        for sym, ts, r, _ in v3[:6] + v3[-6:]:
            f = datetime.datetime.fromtimestamp(ts / 1000, datetime.timezone.utc).strftime("%Y-%m-%d")
            print(f"  {sym:9s} {f}  {r:+.2f}R")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Informe rápido de varios pares /USDT (Binance) en tres temporalidades.

Uso:
    python3 informe_batch.py HYPEUSDT PEPEUSDT QNTUSDT
    python3 informe_batch.py --yahoo HYPE-USD

Por defecto usa klines de Binance (spot). Si un símbolo no existe allí, se salta y lo dice.
Imprime una tabla compacta: orden de medias, parabólica, %B y distancia a la EMA20 por
temporalidad, más el rango de 52 semanas y la posición del precio en la vela en curso.
No decide: los datos y el juicio van separados.
"""
import argparse
import json
import statistics
import sys
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}


# ---------- fuentes ----------
def binance(symbol, interval, limit):
    url = (f"https://api.binance.com/api/v3/klines?symbol={symbol}"
           f"&interval={interval}&limit={limit}")
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=25) as r:
        raw = json.load(r)
    return [{"o": float(k[1]), "h": float(k[2]), "l": float(k[3]), "c": float(k[4])} for k in raw]


def mexc(symbol, interval, limit):
    """MEXC usa el mismo formato de klines que Binance; cubre tokens que Binance no lista."""
    url = (f"https://api.mexc.com/api/v3/klines?symbol={symbol}"
           f"&interval={interval}&limit={limit}")
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=25) as r:
        raw = json.load(r)
    return [{"o": float(k[1]), "h": float(k[2]), "l": float(k[3]), "c": float(k[4])} for k in raw]


def yahoo(symbol, rng, interval):
    url = (f"https://query2.finance.yahoo.com/v8/finance/chart/{symbol}"
           f"?range={rng}&interval={interval}")
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=25) as r:
        d = json.load(r)["chart"]["result"][0]
    q = d["indicators"]["quote"][0]
    out = []
    for i in range(len(d["timestamp"])):
        o, h, l, c = q["open"][i], q["high"][i], q["low"][i], q["close"][i]
        if None in (o, h, l, c):
            continue
        out.append({"o": o, "h": h, "l": l, "c": c})
    return out


# ---------- indicadores ----------
def ema(v, p):
    out = [None] * len(v)
    if len(v) < p:
        return out
    k = 2 / (p + 1)
    out[p - 1] = sum(v[:p]) / p
    for i in range(p, len(v)):
        out[i] = v[i] * k + out[i - 1] * (1 - k)
    return out


def psar(h, l, step=0.02, max_af=0.20):
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
                ep, af = h[i], min(af + step, max_af)
        else:
            val = max(val, h[i - 1], h[i - 2] if i > 1 else h[i - 1])
            if h[i] > val:
                up, val, ep, af = True, ep, h[i], step
            elif l[i] < ep:
                ep, af = l[i], min(af + step, max_af)
        sar[i], bull[i] = val, up
    return sar, bull


def pctb(c, p=20, mult=2.0):
    out = [None] * len(c)
    for i in range(p - 1, len(c)):
        w = c[i - p + 1:i + 1]
        m, sd = statistics.fmean(w), statistics.pstdev(w)
        up, lo = m + mult * sd, m - mult * sd
        out[i] = (c[i] - lo) / (up - lo) * 100 if up > lo else None
    return out


def analyse(rows, tf):
    c = [r["c"] for r in rows]
    h = [r["h"] for r in rows]
    l = [r["l"] for r in rows]
    last = len(c) - 1
    e = {p: ema(c, p) for p in (3, 9, 20, 50, 200)}
    sar, bull = psar(h, l)
    flips = [i for i in range(1, len(rows)) if bull[i] != bull[i - 1]]
    val = lambda x: e[x][last]
    order = sorted([p for p in e if val(p)], key=lambda p: -val(p))
    return {
        "tf": tf, "n": len(rows), "price": c[last],
        "ema": {p: val(p) for p in e},
        # order = periodos ordenados por VALOR de su media, de mayor a menor.
        # Bajista = la más larga arriba (200 > 50 > 20 > 9 > 3). Alcista = lo contrario.
        "bear_order": order == sorted(order, reverse=True),
        "bull_order": order == sorted(order),
        "sar": sar[last], "sar_dir": bull[last],
        "sar_bars": (last - flips[-1]) if flips else None,
        "pctb": pctb(c)[last],
        "d20": (c[last] / val(20) - 1) * 100 if val(20) else None,
        "bar": rows[last],
        "hi": max(h), "lo": min(l),
    }


def line(sym, m, w, d):
    f = lambda x: f"{x:.6g}" if x is not None else "—"
    ordm = lambda b: "bajista" if b["bear_order"] else ("alcista" if b["bull_order"] else "mixto")
    p = m["price"]
    print(f"\n## {sym} — {f(p)}")
    gp = lambda x: "—" if x is None else f"{x:+.1f}%"
    for b, name in ((m, "M"), (w, "S"), (d, "D")):
        pb = "—" if b["pctb"] is None else f"{b['pctb']:.0f}"
        print(f"{name}: orden {ordm(b):8s} | EMA20 {f(b['ema'][20])} (dist {gp(b['d20'])}) "
              f"| EMA50 {f(b['ema'][50])} | EMA200 {f(b['ema'][200])} "
              f"| SAR {f(b['sar'])} {'alc' if b['sar_dir'] else 'baj'} ({b['sar_bars']} velas) "
              f"| %B {pb} | velas {b['n']}")
    print(f"52s: máx {f(d['hi'])} / mín {f(d['lo'])} · precio a {(p/d['hi']-1)*100:+.1f}% del máx "
          f"y {(p/d['lo']-1)*100:+.1f}% del mín")
    print(f"Vela diaria en curso: O {f(d['bar']['o'])} H {f(d['bar']['h'])} "
          f"L {f(d['bar']['l'])} C {f(d['bar']['c'])}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("symbols", nargs="+")
    ap.add_argument("--yahoo", action="store_true")
    a = ap.parse_args()
    for sym in a.symbols:
        try:
            if a.yahoo:
                m = analyse(yahoo(sym, "10y", "1mo"), "M")
                w = analyse(yahoo(sym, "5y", "1wk"), "S")
                d = analyse(yahoo(sym, "1y", "1d"), "D")
            else:
                src = binance
                try:
                    m = analyse(binance(sym, "1M", 120), "M")
                    w = analyse(binance(sym, "1w", 260), "S")
                    d = analyse(binance(sym, "1d", 730), "D")
                except Exception:
                    src = mexc
                    m = analyse(mexc(sym, "1M", 120), "M")
                    w = analyse(mexc(sym, "1W", 260), "S")   # MEXC usa 1W en mayúscula
                    d = analyse(mexc(sym, "1d", 730), "D")
                line.__globals__["FUENTE"] = src.__name__
            line(sym, m, w, d)
        except Exception as e:
            print(f"\n## {sym} — SIN DATOS ({type(e).__name__}: {str(e)[:60]})")


if __name__ == "__main__":
    main()

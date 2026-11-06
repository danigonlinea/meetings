#!/usr/bin/env python3
"""Informe de un activo en tres temporalidades (mensual, semanal, diaria) con los
indicadores del método: EMA 3/9/20/50/200, Parabolic SAR y %B de Bollinger.

Uso:
    python3 informe_activo.py HBAR-USD
    python3 informe_activo.py BTC-USD --json

No decide: imprime los datos y la posición del precio dentro de cada rango, que es
lo que el método usa como «sentimiento». El juicio va en el informe escrito.
"""
import argparse
import json
import statistics
import sys
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}


def fetch(symbol, rng, interval):
    url = (f"https://query2.finance.yahoo.com/v8/finance/chart/{symbol}"
           f"?range={rng}&interval={interval}")
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    res = data["chart"]["result"][0]
    q = res["indicators"]["quote"][0]
    rows = []
    for i, ts in enumerate(res["timestamp"]):
        o, h, l, c = q["open"][i], q["high"][i], q["low"][i], q["close"][i]
        if None in (o, h, l, c):
            continue
        rows.append({"o": o, "h": h, "l": l, "c": c})
    return rows, res["meta"]


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
    sar = [None] * n
    bull = [None] * n
    up = h[0] >= l[0]
    sar[0], bull[0] = (l[0] if up else h[0]), up
    ep, af = (h[0] if up else l[0]), step
    for i in range(1, n):
        val = sar[i - 1] + af * (ep - sar[i - 1])
        if up:
            if i >= 1:
                val = min(val, l[i - 1])
            if i >= 2:
                val = min(val, l[i - 2])
            if l[i] < val:
                up, val, ep, af = False, ep, l[i], step
            elif h[i] > ep:
                ep, af = h[i], min(af + step, max_af)
        else:
            if i >= 1:
                val = max(val, h[i - 1])
            if i >= 2:
                val = max(val, h[i - 2])
            if h[i] > val:
                up, val, ep, af = True, ep, h[i], step
            elif l[i] < ep:
                ep, af = l[i], min(af + step, max_af)
        sar[i], bull[i] = val, up
    return sar, bull


def bollinger(c, p=20, mult=2.0):
    pct_b, upper, lower = [None] * len(c), [None] * len(c), [None] * len(c)
    for i in range(p - 1, len(c)):
        w = c[i - p + 1:i + 1]
        m = statistics.fmean(w)
        sd = statistics.pstdev(w)
        upper[i], lower[i] = m + mult * sd, m - mult * sd
        rng = upper[i] - lower[i]
        pct_b[i] = (c[i] - lower[i]) / rng * 100 if rng else None
    return upper, lower, pct_b


def dec(p):
    return 5 if p < 1 else (3 if p < 10 else 2)


def block(symbol, label, rng, interval):
    rows, meta = fetch(symbol, rng, interval)
    c = [r["c"] for r in rows]
    h = [r["h"] for r in rows]
    l = [r["l"] for r in rows]
    last = len(c) - 1
    price = c[last]
    d = dec(price)
    emas = {p: ema(c, p) for p in (3, 9, 20, 50, 200)}
    sar, bull = psar(h, l)
    up, lo, pct = bollinger(c)
    flips = [i for i in range(1, len(rows)) if bull[i] != bull[i - 1]]
    pos = (price - rows[last]["l"]) / (rows[last]["h"] - rows[last]["l"]) * 100 \
        if rows[last]["h"] > rows[last]["l"] else None
    out = {
        "temporalidad": label, "velas": len(rows), "precio": price,
        "ema3": emas[3][last], "ema9": emas[9][last], "ema20": emas[20][last],
        "ema50": emas[50][last] if len(c) >= 50 else None,
        "ema200": emas[200][last] if len(c) >= 200 else None,
        "sar": sar[last], "sar_dir": "alcista" if bull[last] else "bajista",
        "sar_bars": (last - flips[-1]) if flips else None,
        "pct_b": pct[last], "banda_sup": up[last], "banda_inf": lo[last],
        "pos_rango": pos,
        "ultimas": [(r["o"], r["h"], r["l"], r["c"]) for r in rows[-3:]],
        "max": max(h), "min": min(l),
    }
    out["dist_ema20"] = (price / emas[20][last] - 1) * 100 if emas[20][last] else None
    if out["ema200"]:
        out["dist_ema200"] = (price / out["ema200"] - 1) * 100
    return out


def show(b, d):
    f = lambda x: "—" if x is None else f"{x:,.{d}f}"
    p = lambda x: "—" if x is None else f"{x:+.1f}%"
    print(f"\n### {b['temporalidad']}  ({b['velas']} velas)")
    print(f"Precio {f(b['precio'])}")
    print(f"EMA3 {f(b['ema3'])} · EMA9 {f(b['ema9'])} · EMA20 {f(b['ema20'])}"
          f" · EMA50 {f(b['ema50'])} · EMA200 {f(b['ema200'])}")
    orden = sorted([("3", b["ema3"]), ("9", b["ema9"]), ("20", b["ema20"]),
                    ("50", b["ema50"]), ("200", b["ema200"])],
                   key=lambda x: -(x[1] or 0))
    print("Orden de medias: " + " > ".join(f"EMA{k}" for k, v in orden if v))
    print(f"Parabólica {f(b['sar'])} ({b['sar_dir']}, {b['sar_bars']} velas desde el giro)")
    print(f"%B {b['pct_b']:.0f}% · banda {f(b['banda_inf'])}–{f(b['banda_sup'])}")
    print(f"Posición en la vela actual: {b['pos_rango']:.0f}% del rango")
    print(f"Distancia a EMA20 {p(b['dist_ema20'])}"
          + (f" · a EMA200 {p(b.get('dist_ema200'))}" if b.get("dist_ema200") is not None else ""))
    print(f"Máx {f(b['max'])} / mín {f(b['min'])} del tramo")
    print("Últimas velas (O/H/L/C):")
    for o, h, l, c in b["ultimas"]:
        print(f"  {f(o)}  {f(h)}  {f(l)}  {f(c)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("symbol")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    try:
        mensual = block(a.symbol, "MENSUAL (10 años)", "10y", "1mo")
        semanal = block(a.symbol, "SEMANAL (5 años)", "5y", "1wk")
        diaria = block(a.symbol, "DIARIA (1 año)", "1y", "1d")
    except Exception as e:
        sys.exit(f"no hay datos para {a.symbol}: {e}")
    if a.json:
        print(json.dumps([mensual, semanal, diaria], indent=2, default=str))
        return
    d = dec(mensual["precio"])
    print(f"# {a.symbol} — {mensual['precio']:,.{d}f}")
    for b in (mensual, semanal, diaria):
        show(b, d)
    print("\n### Niveles del método")
    print(f"Máximo y mínimo de 12 meses: {diaria['max']:,.{d}f} / {diaria['min']:,.{d}f}")
    o, h, l, c = mensual["ultimas"][-1]
    print(f"Vela mensual en curso (O/H/L/C): {o:,.{d}f} / {h:,.{d}f} / {l:,.{d}f} / {c:,.{d}f}")
    print(f"Última vela mensual cerrada: {mensual['ultimas'][-2]}")
    print(f"Última vela semanal cerrada: {semanal['ultimas'][-2]}")


if __name__ == "__main__":
    main()

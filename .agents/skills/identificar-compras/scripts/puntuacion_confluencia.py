#!/usr/bin/env python3
"""Puntuación de confluencia (8 condiciones) por día, para localizar el momento de compra.

Uso:
    python3 puntuacion_confluencia.py QNTUSDT --desde 2026-10-01 --hasta 2026-10-30
    python3 puntuacion_confluencia.py BTCUSDT --dias 60

Condiciones (una por columna):
  1 Precio > EMA200 diaria            5 Parabólica diaria alcista
  2 Precio > EMA20 diaria             6 Vela de entrada (mínimo > anterior y cierre > apertura)
  3 Precio > EMA50 diaria             7 Volumen > 1,5x la media de 20
  4 EMA3 > EMA9 diaria                8 4 h alineada: >=80 % de las barras del día sobre su EMA20 y SAR alcista

Contexto (no puntúa, filtra): semanal EMA3>EMA9>EMA20>EMA50 con parabólica alcista = la tendencia mayor
sigue viva, así que la corrección es zona de compra y no cambio de tendencia. Y distancia a la EMA20
diaria: si es mayor del ~25 %, la subida es vertical y no se compra aunque el score sea alto.
"""
import argparse
import datetime
import json
import statistics
import urllib.request
from collections import defaultdict

UA = {"User-Agent": "Mozilla/5.0"}


def kl(symbol, interval, limit):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = json.load(r)
    return [{"t": int(k[0]), "o": float(k[1]), "h": float(k[2]), "l": float(k[3]),
             "c": float(k[4]), "v": float(k[5])} for k in raw]


def kl_rango(symbol, interval, start_ms, end_ms):
    """Descarga paginada: Binance devuelve 1.000 velas por petición."""
    out, cur = [], start_ms
    while cur < end_ms:
        url = (f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}"
               f"&startTime={cur}&endTime={end_ms}&limit=1000")
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = json.load(r)
        if not raw:
            break
        out += [{"t": int(k[0]), "o": float(k[1]), "h": float(k[2]), "l": float(k[3]),
                 "c": float(k[4]), "v": float(k[5])} for k in raw]
        cur = raw[-1][0] + 1
        if len(raw) < 1000:
            break
    return out


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
    sar, bl = [None] * n, [None] * n
    up = h[0] >= l[0]
    sar[0], bl[0] = (l[0] if up else h[0]), up
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
        sar[i], bl[i] = val, up
    return sar, bl


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("symbol")
    ap.add_argument("--desde")
    ap.add_argument("--hasta")
    ap.add_argument("--dias", type=int, default=0)
    a = ap.parse_args()

    if a.desde and a.hasta:
        ini = int(datetime.datetime.strptime(a.desde, "%Y-%m-%d")
                  .replace(tzinfo=datetime.timezone.utc).timestamp() * 1000)
        fin = int(datetime.datetime.strptime(a.hasta, "%Y-%m-%d")
                  .replace(tzinfo=datetime.timezone.utc).timestamp() * 1000)
        margen = 300 * 86400000          # 300 velas diarias previas para que las EMAs existan
        d = kl_rango(a.symbol, "1d", ini - margen, fin)
        h4_raw = kl_rango(a.symbol, "4h", ini - 30 * 86400000, fin)
        w_raw = kl_rango(a.symbol, "1w", ini - 400 * 7 * 86400000, fin)
    else:
        d, h4_raw, w_raw = kl(a.symbol, "1d", 500), kl(a.symbol, "4h", 700), kl(a.symbol, "1w", 200)
    c = [x["c"] for x in d]
    h = [x["h"] for x in d]
    l = [x["l"] for x in d]
    v = [x["v"] for x in d]
    E = {p: ema(c, p) for p in (3, 9, 20, 50, 200)}
    sar, bl = psar(h, l)

    # semanal: régimen mayor
    w = w_raw
    Ew = {p: ema([x["c"] for x in w], p) for p in (3, 9, 20, 50)}
    sarw, blw = psar([x["h"] for x in w], [x["l"] for x in w])

    # 4 h: alineación intradía
    h4 = h4_raw
    c4 = [x["c"] for x in h4]
    e204 = ema(c4, 20)
    _, bl4 = psar([x["h"] for x in h4], [x["l"] for x in h4])
    byday = defaultdict(list)
    for i, x in enumerate(h4):
        day = datetime.datetime.fromtimestamp(x["t"] / 1000, datetime.timezone.utc).strftime("%Y-%m-%d")
        byday[day].append(i)

    def alineacion4(day):
        ids = byday.get(day, [])
        if not ids:
            return 0, 0
        ok = sum(1 for i in ids if e204[i] and c4[i] > e204[i] and bl4[i])
        return ok, len(ids)

    print(f"{'fecha':11s}{'cierre':>9s}{'E20':>8s}{'dist':>7s}  " +
          " ".join(f"{n}" for n in ("200", "20", "50", "3>9", "SAR", "vela", "vol", "4h")) +
          "  score")
    mejores = []
    for i, x in enumerate(d):
        day = datetime.datetime.fromtimestamp(x["t"] / 1000, datetime.timezone.utc).strftime("%Y-%m-%d")
        if a.desde and day < a.desde:
            continue
        if a.hasta and day > a.hasta:
            continue
        if a.dias and i < len(d) - a.dias:
            continue
        if E[200][i] is None:
            continue
        vr = v[i] / statistics.fmean(v[i - 19:i + 1])
        n4, t4 = alineacion4(day)
        cond = [c[i] > E[200][i], c[i] > E[20][i], c[i] > E[50][i], E[3][i] > E[9][i], bl[i],
                (x["l"] > d[i - 1]["l"] and c[i] > x["o"]), vr > 1.5, (t4 > 0 and n4 >= 0.8 * t4)]
        score = sum(1 for k in cond if k)
        dist = (c[i] / E[20][i] - 1) * 100
        marcas = " ".join(" ✓  " if k else " ·  " for k in cond)
        print(f"{day:11s}{c[i]:9.2f}{E[20][i]:8.2f}{dist:+6.0f}%  {marcas}  {score}/8")
        mejores.append((score, day, c[i], dist))
    mejores.sort(reverse=True)
    print("\nMejores días:")
    for s, day, px, dist in mejores[:5]:
        print(f"  {day}  {s}/8  cierre {px:.2f}  distancia a EMA20 {dist:+.0f}%")
    if mejores:
        s, day, px, dist = mejores[0]
        if dist > 25:
            print(f"\n⚠️  El mejor día ({day}) está un {dist:+.0f}% sobre su EMA20: subida fuerte. "
                  "NO descarta la compra (medido: +0,18R, igual que pegado a la EMA20); ajusta el tamaño.")


if __name__ == "__main__":
    main()

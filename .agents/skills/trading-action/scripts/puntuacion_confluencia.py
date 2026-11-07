#!/usr/bin/env python3
"""Puntuación de confluencia (8 condiciones) por día, para localizar el momento de compra.

Uso:
    python3 puntuacion_confluencia.py QNTUSDT --desde 2026-10-01 --hasta 2026-10-30
    python3 puntuacion_confluencia.py BTCUSDT --dias 60

Condiciones (una por columna):
  1 Precio > EMA200 diaria            5 Parabólica diaria alcista
  2 Precio > EMA20 diaria             6 Vela de entrada (mínimo > anterior y cierre > apertura)
  3 Precio > EMA50 diaria             7 Volumen > 1,5x la media de las 20 velas ANTERIORES
  4 EMA3 > EMA9 diaria                8 4 h alineada: >=80 % de las barras del día sobre su EMA20
                                         y con SAR alcista (solo si el día ya ha cerrado)

Columnas extra:
  perm  permiso semanal: la última semana CERRADA mantiene EMA3>EMA9>EMA20>EMA50 con parabólica
        alcista. Si la semanal está girada, el día no habilita compra aunque puntúe 8/8.

El signo `?` marca un dato que aún no existe (día en curso): esa casilla NO cuenta como cumplida y
el score sale con asterisco. El marcador NO es un permiso de entrada: la entrada la da el gate
medido (EMA200 diaria + vela de entrada + volumen) y el score ordena calidad y tamaño. La distancia
a la EMA20 diaria es un aviso de tamaño, no un veto: comprar a más del 25 % rinde igual que pegado
a ella (medido sobre la regla V5 del backtest).
"""
import argparse
import datetime
import json
import statistics
import time
import urllib.request
from collections import defaultdict

UA = {"User-Agent": "Mozilla/5.0"}
BASES = ("https://api.binance.com", "https://api.mexc.com")   # mismo formato de klines
DIA_MS = 86400000
DIAS_CALENTAMIENTO = 500      # velas diarias previas al inicio de la ventana
MIN_CALENTAMIENTO = 150       # barras tras el seed de la EMA200 para fiarse del día


def kl(symbol, interval, limit):
    """Últimas `limit` velas, con MEXC como respaldo cuando Binance no sirve el par."""
    for b in BASES:
        url = f"{b}/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = json.load(r)
            if isinstance(raw, list) and raw:
                return [{"t": int(k[0]), "o": float(k[1]), "h": float(k[2]),
                         "l": float(k[3]), "c": float(k[4]), "v": float(k[5])} for k in raw]
        except Exception:
            continue
    raise SystemExit(f"no hay klines para {symbol} ni en Binance ni en MEXC")


def kl_rango(symbol, interval, start_ms, end_ms):
    """Descarga paginada (1.000 velas por petición), con el mismo respaldo."""
    out, cur, base = [], start_ms, None
    while cur < end_ms:
        raw = None
        for b in ([base] if base else BASES):
            url = (f"{b}/api/v3/klines?symbol={symbol}&interval={interval}"
                   f"&startTime={cur}&endTime={end_ms}&limit=1000")
            try:
                req = urllib.request.Request(url, headers=UA)
                with urllib.request.urlopen(req, timeout=30) as r:
                    raw = json.load(r)
                base = b
                break
            except Exception:
                continue
        if not raw or not isinstance(raw, list):
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


def regimen_semanal(w, dias_ms):
    """Para cada día devuelve (permitido|None, motivo) usando la última semana CERRADA.

    Una vela semanal empieza en w[k]['t'] y cierra 7 días después: hasta que cierra no se puede
    usar. Antes esto se calculaba en el script y no se usaba nunca.
    """
    cw = [x["c"] for x in w]
    Ew = {p: ema(cw, p) for p in (3, 9, 20, 50)}
    _, blw = psar([x["h"] for x in w], [x["l"] for x in w])
    out, k = [], -1
    for t in dias_ms:
        while k + 1 < len(w) and w[k + 1]["t"] + 7 * DIA_MS <= t:
            k += 1
        if k < 0:
            out.append((None, "sin historia semanal"))
            continue
        a3, a9, a20, a50 = Ew[3][k], Ew[9][k], Ew[20][k], Ew[50][k]
        if a3 is None or a9 is None or a20 is None or a50 is None:
            out.append((None, "sin 50 semanas para la EMA50 semanal"))
            continue
        orden = a3 > a9 > a20 > a50
        out.append((bool(orden and blw[k]), "semanal OK" if orden and blw[k] else "semanal girada"))
    return out


def fmt_precio(x):
    """Precio con los decimales que hagan falta: 0,0720 no puede salir como 0,07."""
    if abs(x) < 0.01:
        return f"{x:.6f}"
    if abs(x) < 1:
        return f"{x:.4f}"
    if abs(x) < 10:
        return f"{x:.3f}"
    return f"{x:.2f}"


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
        d = kl_rango(a.symbol, "1d", ini - DIAS_CALENTAMIENTO * DIA_MS, fin + DIA_MS)
        h4_raw = kl_rango(a.symbol, "4h", ini - 30 * DIA_MS, fin + DIA_MS)
        w_raw = kl_rango(a.symbol, "1w", ini - 400 * 7 * DIA_MS, fin + DIA_MS)
    else:
        d, h4_raw, w_raw = kl(a.symbol, "1d", 900), kl(a.symbol, "4h", 900), kl(a.symbol, "1w", 300)

    c = [x["c"] for x in d]
    h = [x["h"] for x in d]
    l = [x["l"] for x in d]
    v = [x["v"] for x in d]
    E = {p: ema(c, p) for p in (3, 9, 20, 50, 200)}
    sar, bl = psar(h, l)
    ahora = int(time.time() * 1000)

    c4 = [x["c"] for x in h4_raw]
    e204 = ema(c4, 20)
    _, bl4 = psar([x["h"] for x in h4_raw], [x["l"] for x in h4_raw])
    byday = defaultdict(list)
    for i, x in enumerate(h4_raw):
        day = datetime.datetime.fromtimestamp(x["t"] / 1000, datetime.timezone.utc).strftime("%Y-%m-%d")
        byday[day].append(i)

    perm = regimen_semanal(w_raw, [x["t"] for x in d])

    def casilla4(day, cerrada):
        ids = byday.get(day, [])
        if not cerrada or len(ids) < 4:      # día en curso (o serie incompleta): no se puntúa
            return None, len(ids)
        ok = sum(1 for i in ids if e204[i] and c4[i] > e204[i] and bl4[i])
        return ok >= 0.8 * len(ids), len(ids)

    print(f"{'fecha':11s}{'cierre':>9s}{'E20':>8s}{'dist':>7s}  " +
          " ".join(f"{n}" for n in ("200", "20", "50", "3>9", "SAR", "vela", "vol", "4h")) +
          "  score  perm")
    mejores, saltados = [], 0
    for i, x in enumerate(d):
        day = datetime.datetime.fromtimestamp(x["t"] / 1000, datetime.timezone.utc).strftime("%Y-%m-%d")
        if a.desde and day < a.desde:
            continue
        if a.hasta and day > a.hasta:
            continue
        if a.dias and i < len(d) - a.dias:
            continue
        if E[200][i] is None or i < 200 + MIN_CALENTAMIENTO:
            saltados += 1
            continue
        cerrada = x["t"] + DIA_MS <= ahora
        v20 = statistics.fmean(v[i - 20:i])          # 20 velas anteriores, sin la propia
        c4ok, _ = casilla4(day, cerrada)
        cond = [c[i] > E[200][i], c[i] > E[20][i], c[i] > E[50][i], E[3][i] > E[9][i], bl[i],
                (x["l"] > d[i - 1]["l"] and c[i] > x["o"]), v[i] > 1.5 * v20, c4ok]
        score = sum(1 for k in cond if k is True)
        incompleto = any(k is None for k in cond)
        dist = (c[i] / E[20][i] - 1) * 100
        marcas = " ".join(" ✓  " if k is True else (" ?  " if k is None else " ·  ") for k in cond)
        p = perm[i][0]
        print(f"{day:11s}{fmt_precio(c[i]):>9s}{fmt_precio(E[20][i]):>8s}{dist:+6.0f}%  {marcas}  "
              f"{score}/8{'*' if incompleto else ' '}  "
              f"{'?' if p is None else ('OK' if p else 'girada')}")
        if not incompleto:
            mejores.append((score, day, c[i], dist, p))
    mejores.sort(reverse=True)
    if mejores:
        print("\nMejores días (solo días cerrados):")
        for s, day, px, dist, p in mejores[:5]:
            print(f"  {day}  {s}/8  cierre {fmt_precio(px)}  distancia a EMA20 {dist:+.0f}%  "
                  f"permiso semanal {'OK' if p else 'girada'}")
        s, day, px, dist, p = mejores[0]
        if dist > 25:
            print(f"\n⚠️  El mejor día ({day}) está un {dist:+.0f}% sobre su EMA20: NO descarta la "
                  "compra (medido: rinde igual que pegado a ella); reduce el tamaño.")
        if not p:
            print(f"Nota: el mejor día ({day}) tiene la semanal girada. Medido sobre la regla V5, "
                  "comprar con la semanal girada rinde igual o mejor (n=327, +0,26R) que con ella "
                  "alineada (n=186, +0,17R): la semanal es contexto y tamaño, no un veto. La regla "
                  "que sí filtra es la EMA200 diaria.")
    if saltados:
        print(f"\n({saltados} día(s) omitido(s) por falta de {MIN_CALENTAMIENTO} velas de "
              "calentamiento para la EMA200)")
    print("\n* = día en curso: la casilla de 4 h y la vela diaria no han cerrado y no cuentan.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Indicadores técnicos sobre velas mensuales (o semanales/diarias) desde Yahoo Finance.

Uso:
    python3 tecnicos.py AMZN              # mensual, 10 años
    python3 tecnicos.py NVDA --interval 1wk --range 5y
    python3 tecnicos.py AMZN --tail 12 --json

Calcula, sin dependencias externas (solo stdlib):
  - EMA 3, 9 y 20 sobre el cierre (configurable con --emas)
  - Parabolic SAR de Wilder (paso 0,02 / máximo 0,20)
  - Bandas de Bollinger SMA(20) ± 2σ con %B y ancho en % (configurable con --bb)

Los precios vienen de query2.finance.yahoo.com/v8/finance/chart, que NO necesita
crumb ni cookies (a diferencia de quoteSummary). Los precios están ajustados por
split, no por dividendo: para una empresa que reparte, usa --adjusted para verlo.
"""
import argparse
import json
import sys
import time
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}


def fetch(symbol, rng, interval):
    url = (f"https://query2.finance.yahoo.com/v8/finance/chart/{symbol}"
           f"?range={rng}&interval={interval}&events=div|split")
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=25) as r:
        data = json.load(r)
    res = data["chart"]["result"][0]
    q = res["indicators"]["quote"][0]
    rows = []
    for i, ts in enumerate(res["timestamp"]):
        o, h, l, c = q["open"][i], q["high"][i], q["low"][i], q["close"][i]
        if None in (o, h, l, c):
            continue
        rows.append({
            "ts": ts,
            "date": time.strftime("%Y-%m", time.gmtime(ts)),
            "o": o, "h": h, "l": l, "c": c,
            "v": q["volume"][i] or 0,
        })
    # Yahoo a veces repite el mes en curso como dos barras (la del mes y la del
    # último precio). Se fusionan: apertura de la primera, cierre de la última.
    # Ojo: la clave depende de la temporalidad. Agrupar por mes en semanal o diaria
    # aplastaba 260 velas semanales de 5 años en 61 — la serie quedaba falsa.
    clave = "%Y-%m" if interval == "1mo" else "%Y-%m-%d"
    for r in rows:
        r["date"] = time.strftime(clave, time.gmtime(r["ts"]))
    merged = []
    for r in rows:
        if merged and merged[-1]["date"] == r["date"]:
            m = merged[-1]
            m["h"] = max(m["h"], r["h"])
            m["l"] = min(m["l"], r["l"])
            m["c"] = r["c"]
            m["v"] += r["v"]
        else:
            merged.append(r)
    meta = res["meta"]
    return merged, meta


def ema(values, period):
    """EMA clásica: semilla en la SMA de los `period` primeros cierres."""
    out = [None] * len(values)
    if len(values) < period:
        return out
    k = 2.0 / (period + 1)
    seed = sum(values[:period]) / period
    out[period - 1] = seed
    for i in range(period, len(values)):
        out[i] = values[i] * k + out[i - 1] * (1 - k)
    return out


def psar(high, low, step=0.02, max_af=0.20):
    """Parabolic SAR de Wilder. Devuelve (sar[], tendencia[]) con None al inicio."""
    n = len(high)
    sar: list = [None] * n
    bull: list = [None] * n
    if n < 2:
        return sar, bull
    up = high[0] >= low[0]
    sar[0] = low[0] if up else high[0]
    bull[0] = up
    ep = high[0] if up else low[0]
    af = step
    for i in range(1, n):
        prev = sar[i - 1]
        val = prev + af * (ep - prev)
        if up:
            # el SAR no puede entrar en el rango de las dos velas anteriores
            if i >= 1:
                val = min(val, low[i - 1])
            if i >= 2:
                val = min(val, low[i - 2])
            if low[i] < val:                 # giro a bajista
                up = False
                val = ep
                ep = low[i]
                af = step
            else:
                if high[i] > ep:
                    ep = high[i]
                    af = min(af + step, max_af)
        else:
            if i >= 1:
                val = max(val, high[i - 1])
            if i >= 2:
                val = max(val, high[i - 2])
            if high[i] > val:                # giro a alcista
                up = True
                val = ep
                ep = high[i]
                af = step
            else:
                if low[i] < ep:
                    ep = low[i]
                    af = min(af + step, max_af)
        sar[i] = val
        bull[i] = up
    return sar, bull


def bollinger(closes, period=20, mult=2.0):
    """Bandas de Bollinger clásicas: SMA(period) ± mult · desviación típica poblacional.

    Devuelve dict con listas alineadas al cierre:
      media[], sup[], inf[], pct_b[] (posición dentro de la banda, 0-100),
      ancho[] (anchura de la banda en % del precio: la medida de volatilidad/riesgo).
    %B y ancho son adimensionales: sirven igual en una acción de 300 que en un cripto
    de 0,000005. La desviación es poblacional (pstdev), que es la convención de Bollinger
    y la que usa el gráfico.
    """
    n = len(closes)
    media = [None] * n
    sup = [None] * n
    inf = [None] * n
    pct_b = [None] * n
    ancho = [None] * n
    if n < period:
        return {"media": media, "sup": sup, "inf": inf, "pct_b": pct_b, "ancho": ancho}
    for i in range(period - 1, n):
        w = closes[i - period + 1:i + 1]
        m = sum(w) / period
        var = sum((x - m) ** 2 for x in w) / period
        sd = var ** 0.5
        media[i], sup[i], inf[i] = m, m + mult * sd, m - mult * sd
        rng = sup[i] - inf[i]
        pct_b[i] = (closes[i] - inf[i]) / rng * 100 if rng else None
        ancho[i] = rng / m * 100 if m else None
    return {"media": media, "sup": sup, "inf": inf, "pct_b": pct_b, "ancho": ancho}


def percentil(valores, x):
    """Percentil (0-100) de x dentro de la serie, para leer si el ancho es compresión
    o expansión respecto a su propia historia. Sin numpy: ordenar y contar."""
    v = [y for y in valores if y is not None]
    if not v or x is None:
        return None
    menores = sum(1 for y in v if y < x)
    return menores / (len(v) - 1) * 100 if len(v) > 1 else 0.0


def regimen_volatilidad(pct):
    if pct is None:
        return None
    if pct <= 25:
        return "compresión (squeeze)"
    if pct >= 75:
        return "expansión"
    return "normal"


def dec_for(price: float) -> int:
    """Decimales según la magnitud: 5 para cripto barata, 3 para <10, 2 para el resto."""
    if price < 1:
        return 5
    if price < 10:
        return 3
    return 2


def fmt(x, dec=2):
    return "—" if x is None else f"{x:,.{dec}f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("symbol")
    ap.add_argument("--range", default="10y")
    ap.add_argument("--interval", default="1mo", choices=["1d", "1wk", "1mo", "3mo"])
    ap.add_argument("--emas", default="3,9,20")
    ap.add_argument("--tail", type=int, default=10)
    ap.add_argument("--step", type=float, default=0.02)
    ap.add_argument("--max-af", type=float, default=0.20)
    ap.add_argument("--bb", default="20,2",
                    help="Bandas de Bollinger: periodo,multiplicador (por defecto 20,2)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    rows, meta = fetch(a.symbol, a.range, a.interval)
    if len(rows) < 25:
        sys.exit(f"solo {len(rows)} velas: no hay histórico suficiente")

    closes = [r["c"] for r in rows]
    highs = [r["h"] for r in rows]
    lows = [r["l"] for r in rows]
    periods = [int(p) for p in a.emas.split(",")]
    emas = {p: ema(closes, p) for p in periods}
    sar, bull = psar(highs, lows, a.step, a.max_af)

    try:
        bb_period, bb_mult = a.bb.split(",")
        bb_period, bb_mult = int(bb_period), float(bb_mult)
    except ValueError:
        sys.exit("--bb se escribe periodo,multiplicador (p. ej. 20,2)")
    if bb_period < 2:
        sys.exit("--bb: el periodo mínimo son 2 velas")
    bb = bollinger(closes, bb_period, bb_mult)

    last = len(rows) - 1
    price = closes[last]
    # percentil del ancho contra su propia historia (200 velas previas, sin la actual):
    # es lo que dice si la volatilidad está comprimida o expandida, no el ancho en sí
    ventana = bb["ancho"][max(0, last - 200):last]
    pct_ancho = percentil(ventana, bb["ancho"][last])
    res = {
        "symbol": meta.get("symbol", a.symbol),
        "interval": a.interval,
        "currency": meta.get("currency"),
        "last_date": rows[last]["date"],
        "price": price,
        "emas": {f"ema{p}": emas[p][last] for p in periods},
        "sar": sar[last],
        "sar_trend": "alcista" if bull[last] else "bajista",
        "bb": {
            "periodo": bb_period, "mult": bb_mult,
            "media": bb["media"][last], "sup": bb["sup"][last], "inf": bb["inf"][last],
            "pct_b": bb["pct_b"][last], "ancho_pct": bb["ancho"][last],
            "ancho_percentil": pct_ancho,
            "regimen": regimen_volatilidad(pct_ancho),
            "posicion_en_banda": "superior" if (bb["pct_b"][last] or 0) > 50 else "inferior",
        },
    }
    # velas desde el último giro del SAR
    flips = [i for i in range(1, len(rows)) if bull[i] != bull[i - 1]]
    res["sar_flip_date"] = rows[flips[-1]]["date"] if flips else None
    res["bars_since_flip"] = (last - flips[-1]) if flips else None

    if a.json:
        print(json.dumps(res, indent=2, default=str))
        return

    print(f"{res['symbol']} · {a.interval} · {res['currency']} · "
          f"{len(rows)} velas · última {rows[last]['date']}")
    print(f"Precio {fmt(price)}  |  " +
          "  ".join(f"EMA{p} {fmt(emas[p][last])}" for p in periods) +
          f"  |  SAR {fmt(sar[last])} ({res['sar_trend']})")
    b = res["bb"]
    print(f"Bollinger ({bb_period},{bb_mult:g}σ)  {fmt(b['inf'])} – {fmt(b['sup'])}"
          f"  |  media {fmt(b['media'])}"
          f"  |  ancho {b['ancho_pct']:.1f} % del precio"
          f"  |  %B {b['pct_b']:.0f} %  |  ancho pctl {b['ancho_percentil']:.0f}"
          f" ({b['regimen']})")
    print()
    head = f"{'fecha':<12}{'open':>10}{'high':>10}{'low':>10}{'close':>10}" + \
           "".join(f"{'EMA'+str(p):>10}" for p in periods) + \
           f"{'SAR':>10}{'tend':>8}{'BBinf':>11}{'BBsup':>11}{'%B':>6}"
    print(head)
    print("-" * len(head))
    for i in range(max(0, len(rows) - a.tail), len(rows)):
        pb = bb["pct_b"][i]
        pb_txt = "—" if pb is None else f"{pb:.0f}"
        print(f"{rows[i]['date']:<12}{rows[i]['o']:>10.2f}{rows[i]['h']:>10.2f}"
              f"{rows[i]['l']:>10.2f}{rows[i]['c']:>10.2f}" +
              "".join(f"{fmt(emas[p][i]):>10}" for p in periods) +
              f"{fmt(sar[i]):>10}{('alcista' if bull[i] else 'bajista'):>8}"
              f"{fmt(bb['inf'][i]):>11}{fmt(bb['sup'][i]):>11}{pb_txt:>6}")

    # señales de una línea
    print()
    orden = " > ".join(f"EMA{p}" for p in sorted(periods, key=lambda p: -emas[p][last]))
    print(f"Orden de EMAs (de mayor a menor): {orden}")
    print(f"Precio sobre EMA{sorted(periods)[0]}: "
          f"{'sí' if price > emas[sorted(periods)[0]][last] else 'no'} · "
          f"distancia al SAR: {(price / sar[last] - 1) * 100:+.1f}%")
    if res["sar_flip_date"]:
        print(f"Último giro del SAR: {res['sar_flip_date']} "
              f"({res['bars_since_flip']} velas desde el giro)")
    print(f"Bollinger — suelo {fmt(b['inf'])} · techo {fmt(b['sup'])} · "
          f"rango {b['ancho_pct']:.1f} % del precio"
          f" · precio en la mitad {b['posicion_en_banda']} (%B {b['pct_b']:.0f} %)")
    print(f"Volatilidad: {b['regimen']} — el ancho está en el percentil "
          f"{b['ancho_percentil']:.0f} de las últimas {len(ventana)} velas. "
          f"Describe; no predice.")


if __name__ == "__main__":
    main()

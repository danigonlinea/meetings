#!/usr/bin/env python3
"""Velas OHLCV en vivo para cualquier temporalidad, cripto o acción.

Uso:
    python3 velas.py PEPEUSDT --interval 1m
    python3 velas.py BTCUSDT --interval 5m --gate --taker-bps 5
    python3 velas.py 1000PEPEUSDT --interval 15m --velas 20 --json
    python3 velas.py AAPL --interval 5m --mercado yahoo
    python3 velas.py ETHUSDT --interval 1m --watch 30

Qué imprime: las velas pedidas (apertura, máximo, mínimo, cierre, volumen), la vela
en curso con su progreso, y los indicadores del método (EMA 3/9/20/50/200, ATR,
parabólica 0,02/0,20, VWAP del día, volumen relativo). Con --gate añade la cuenta de
coste de `trader-scalping` y el veredicto comprar/vender/esperar.

No decide por ti y no es asesoramiento: `--gate` es aritmética de costes + una tabla
de condiciones, no una ventaja medida. Sin `--gate` solo entrega datos.

Fuentes: Binance futuros (fapi) y spot, MEXC contratos, Yahoo (acciones/ETF/índices).
Solo stdlib. Las velas de Binance y MEXC cierran en UTC.
"""
import argparse
import json
import math
import re
import statistics
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

BINANCE_FAPI = "https://fapi.binance.com"
BINANCE_SPOT = "https://api.binance.com"
MEXC = "https://contract.mexc.com"
YAHOO = "https://query2.finance.yahoo.com"

BINANCE_IV = {"1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h",
              "1d", "3d", "1w", "1M"}
YAHOO_IV = {"1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo"}
IV_SECONDS = {"1m": 60, "3m": 180, "5m": 300, "15m": 900, "30m": 1800, "1h": 3600,
              "2h": 7200, "4h": 14400, "6h": 21600, "8h": 28800, "12h": 43200,
              "1d": 86400, "3d": 259200, "1w": 604800, "1M": 2592000}


# ---------------------------------------------------------------- red

def _open(url, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=25) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            body = ""
            try:
                body = e.read().decode()[:200]
            except Exception:
                pass
            last = f"HTTP {e.code} {body}".strip()
            if e.code in (418, 429):
                time.sleep(2 * (i + 1))
                continue
            break
        except Exception as e:  # noqa: BLE001 - se reintenta red
            last = str(e)
            time.sleep(1 + i)
    raise RuntimeError(last or "sin respuesta")


# ---------------------------------------------------------------- resolución de mercado

def _factor(sym):
    """'1000PEPEUSDT' -> ('PEPEUSDT', 1000). Los perpetuos de Binance/MEXC cotizan
    contratos de 1000 (o 1.000.000) unidades; se normaliza el precio a 1 unidad."""
    m = re.match(r"^(\d{3,7})([A-Z].*)$", sym)
    if m and int(m.group(1)) in (100, 1000, 10000, 1000000):
        return m.group(2), int(m.group(1))
    return sym, 1


_LISTADOS = {}


def _binance_has(base, sym=None):
    if base not in _LISTADOS:
        d = _open(f"{base}/fapi/v1/exchangeInfo" if "fapi" in base
                  else f"{base}/api/v3/exchangeInfo")
        _LISTADOS[base] = {s["symbol"] for s in d["symbols"]}
    return _LISTADOS[base]


def resolve(symbol, mercado="auto"):
    """Devuelve {venue, base, symbol(contrato), factor, tipo, fee_bps_defecto}."""
    s = symbol.upper().strip()
    if mercado in ("auto", "yahoo") and not re.fullmatch(r"[A-Z0-9]{2,15}(USDT|USDC|BUSD|USD1)", s):
        return {"venue": "yahoo", "base": YAHOO, "symbol": s, "factor": 1,
                "tipo": "accion", "fee_bps": None}
    if mercado == "yahoo":
        return {"venue": "yahoo", "base": YAHOO, "symbol": s, "factor": 1,
                "tipo": "accion", "fee_bps": None}

    base_sym, factor = _factor(s)
    if mercado in ("auto", "futuros"):
        # futuros de Binance cotizan contratos de 1000/1.000.000 unidades
        fut = _binance_has(BINANCE_FAPI)
        for cand in (s, "1000" + base_sym, "1000000" + base_sym):
            if cand in fut:
                f = _factor(cand)[1]
                return {"venue": "binance-futuros", "base": BINANCE_FAPI, "symbol": cand,
                        "factor": f, "tipo": "cripto", "fee_bps": 5.0}
    if mercado in ("auto", "spot"):
        spot = _binance_has(BINANCE_SPOT, s)
        if base_sym in spot:
            return {"venue": "binance-spot", "base": BINANCE_SPOT, "symbol": base_sym,
                    "factor": 1, "tipo": "cripto", "fee_bps": 10.0}
    if mercado in ("auto", "mexc"):
        d = _open(f"{MEXC}/api/v1/contract/detail")
        pairs = {c["symbol"] for c in d["data"]}
        coin = base_sym[:-4] if base_sym.endswith("USDT") else base_sym.replace("-", "_")
        for par in (f"{coin}_USDT", f"1000{coin}_USDT", f"1000000{coin}_USDT"):
            if par in pairs:
                return {"venue": "mexc", "base": MEXC, "symbol": par,
                        "factor": _factor(par)[1], "tipo": "cripto", "fee_bps": 2.0}
    raise SystemExit(
        f"no encuentro {symbol} en futuros/spot de Binance ni en MEXC. "
        f"Revisa el par (p. ej. PEPEUSDT, 1000PEPEUSDT) o usa --mercado yahoo para acciones.")


# ---------------------------------------------------------------- velas

def _binance_klines(base, symbol, interval, limit):
    d = _open(f"{base}/fapi/v1/klines?symbol={symbol}&interval={interval}&limit={limit}"
              if "fapi" in base else
              f"{base}/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}")
    now = time.time()
    rows = []
    for x in d:
        rows.append({"t": x[0] / 1000.0, "o": float(x[1]), "h": float(x[2]),
                     "l": float(x[3]), "c": float(x[4]), "v": float(x[5]),
                     "cerrada": x[6] / 1000.0 < now})
    return rows


MEXC_IV = {"1m": "Min1", "5m": "Min5", "15m": "Min15", "30m": "Min30", "1h": "Min60",
           "4h": "Hour4", "1d": "Day1"}


def _mexc_klines(symbol, interval, limit):
    if interval not in MEXC_IV:
        raise SystemExit(f"MEXC solo sirve {', '.join(MEXC_IV)} (pide otra temporalidad "
                         f"o usa Binance)")
    now = int(time.time())
    start = now - IV_SECONDS.get(interval, 300) * (limit + 2)
    d = _open(f"{MEXC}/api/v1/contract/kline/{symbol}?interval={MEXC_IV[interval]}"
              f"&start={start}&end={now}")
    data = d["data"]
    rows = []
    for i, t in enumerate(data["time"]):
        rows.append({"t": float(t), "o": float(data["open"][i]), "h": float(data["high"][i]),
                     "l": float(data["low"][i]), "c": float(data["close"][i]),
                     "v": float(data["vol"][i]),
                     "cerrada": t + IV_SECONDS.get(interval, 300) < now})
    return rows[-limit:]


YAHOO_RANGE = {"1m": "7d", "2m": "7d", "5m": "1mo", "15m": "1mo", "30m": "1mo",
               "60m": "3mo", "90m": "3mo", "1h": "3mo", "1d": "2y", "5d": "2y",
               "1wk": "5y", "1mo": "10y"}


def _yahoo_klines(symbol, interval, limit, rango=None):
    iv = {"1h": "60m", "1mo": "1mo"}.get(interval, interval)
    rng = rango or YAHOO_RANGE.get(interval, "1mo")
    d = _open(f"{YAHOO}/v8/finance/chart/{symbol}?range={rng}&interval={iv}")
    res = d["chart"]["result"][0]
    q = res["indicators"]["quote"][0]
    now = time.time()
    secs = IV_SECONDS.get(interval, 60)
    rows = []
    for i, ts in enumerate(res["timestamp"]):
        o, h, l, c = (q["open"][i], q["high"][i], q["low"][i], q["close"][i])
        if None in (o, h, l, c):
            continue
        vol = float(q["volume"][i] or 0)
        # Yahoo cierra la serie con una barra plana de volumen 0 repetida: no es una vela
        if vol == 0 and h == l:
            continue
        rows.append({"t": float(ts), "o": o, "h": h, "l": l, "c": c, "v": vol,
                     "cerrada": ts + secs < now})
    return rows[-limit:], res.get("meta", {})


def _resample(rows, seconds):
    """Reagrupa velas de 1 m en una temporalidad arbitraria de N minutos."""
    out = []
    for r in rows:
        bucket = int(r["t"] // seconds) * seconds
        if out and out[-1]["t"] == bucket:
            b = out[-1]
            b["h"] = max(b["h"], r["h"])
            b["l"] = min(b["l"], r["l"])
            b["c"] = r["c"]
            b["v"] += r["v"]
            b["cerrada"] = b["cerrada"] and r["cerrada"]
        else:
            out.append({"t": float(bucket), "o": r["o"], "h": r["h"], "l": r["l"],
                        "c": r["c"], "v": r["v"], "cerrada": r["cerrada"]})
    return out


def candles(m, interval, limit):
    meta = {}
    if m["venue"] == "yahoo":
        rows, meta = _yahoo_klines(m["symbol"], interval, limit)
        m["_yahoo_meta"] = meta
    elif m["venue"] == "mexc":
        rows = _mexc_klines(m["symbol"], interval, limit)
    else:
        tope = 1500 if "fapi" in m["base"] else 1000
        seg = IV_SECONDS.get(interval, 300)
        # intradía: la serie tiene que cubrir la sesión UTC para que el VWAP sea exacto
        need = limit if seg >= 86400 else max(limit, 86400 // seg + 2)
        if interval in BINANCE_IV:
            rows = _binance_klines(m["base"], m["symbol"], interval, min(tope, need))
        else:
            mm = re.fullmatch(r"(\d+)m", interval)
            if not mm:
                raise SystemExit(f"temporalidad {interval} no válida para Binance: "
                                 f"{', '.join(sorted(BINANCE_IV))} o Nm (p. ej. 45m)")
            secs = int(mm.group(1)) * 60
            raw = _binance_klines(m["base"], m["symbol"], "1m",
                                  min(tope, max(need * (secs // 60), 600)))
            rows = _resample(raw, secs)
            m["_resample"] = f"{mm.group(1)}m desde 1m"
    if not rows:
        raise SystemExit("la fuente no devolvió velas")
    return rows


# ---------------------------------------------------------------- indicadores

def ema(v, p):
    out = [None] * len(v)
    if len(v) < p:
        return out
    k = 2 / (p + 1)
    out[p - 1] = sum(v[:p]) / p
    for i in range(p, len(v)):
        out[i] = v[i] * k + out[i - 1] * (1 - k)
    return out


def atr(rows, p=14):
    if len(rows) < p + 1:
        return None
    trs = []
    for i in range(1, len(rows)):
        h, l, pc = rows[i]["h"], rows[i]["l"], rows[i - 1]["c"]
        trs.append(max(h - l, abs(h - pc), abs(l - pc)))
    a = sum(trs[:p]) / p
    for t in trs[p:]:
        a = (a * (p - 1) + t) / p
    return a


def psar(rows, step=0.02, max_af=0.20):
    h = [r["h"] for r in rows]
    l = [r["l"] for r in rows]
    n = len(rows)
    sar = [None] * n
    bull = [None] * n
    up = h[0] >= l[0]
    sar[0], bull[0] = (l[0] if up else h[0]), up
    ep, af = (h[0] if up else l[0]), step
    for i in range(1, n):
        val = sar[i - 1] + af * (ep - sar[i - 1])
        if up:
            val = min(val, l[i - 1])
            if i >= 2:
                val = min(val, l[i - 2])
            if l[i] < val:
                up, val, ep, af = False, ep, l[i], step
            elif h[i] > ep:
                ep, af = h[i], min(af + step, max_af)
        else:
            val = max(val, h[i - 1])
            if i >= 2:
                val = max(val, h[i - 2])
            if h[i] > val:
                up, val, ep, af = True, ep, h[i], step
            elif l[i] < ep:
                ep, af = l[i], min(af + step, max_af)
        sar[i], bull[i] = val, up
    return sar, bull


def vwap_day(rows, interval):
    """VWAP de la sesión UTC (solo intradía). Con menos velas que la sesión, se marca
    como parcial en vez de dar por bueno un VWAP de medio día."""
    if IV_SECONDS.get(interval, 0) >= 86400:
        return None
    now = datetime.now(timezone.utc)
    day0 = datetime(now.year, now.month, now.day, tzinfo=timezone.utc).timestamp()
    hoy = [r for r in rows if r["t"] >= day0]
    if not hoy:
        return None
    pv = sum(((r["h"] + r["l"] + r["c"]) / 3) * r["v"] for r in hoy)
    vv = sum(r["v"] for r in hoy)
    if not vv:
        return None
    return {"valor": pv / vv, "velas": len(hoy), "completo": rows[0]["t"] <= day0}


# ---------------------------------------------------------------- datos en vivo

def libro(m):
    """Bid/ask y spread. Devuelve None para Yahoo (sin libro gratis)."""
    if m["venue"] == "yahoo":
        meta = m.get("_yahoo_meta", {})
        bid, ask = meta.get("bid"), meta.get("ask")
        if bid and ask:
            return {"bid": bid, "ask": ask}
        return None
    try:
        if m["venue"] == "mexc":
            d = _open(f"{MEXC}/api/v1/contract/ticker?symbol={m['symbol']}")
            bid, ask = float(d["data"]["bid1"]), float(d["data"]["ask1"])
        else:
            d = _open(f"{m['base']}/fapi/v1/ticker/bookTicker?symbol={m['symbol']}"
                      if "fapi" in m["base"] else
                      f"{m['base']}/api/v3/ticker/bookTicker?symbol={m['symbol']}")
            bid, ask = float(d["bidPrice"]), float(d["askPrice"])
        if not bid or not ask:
            return None
        return {"bid": bid / m["factor"], "ask": ask / m["factor"]}
    except Exception:  # noqa: BLE001 - el libro es opcional
        return None


def derivados(m):
    """Funding, próximo cobro, OI y long/short. Solo futuros de Binance."""
    if m["venue"] != "binance-futuros":
        return None
    out = {}
    p = {}
    try:
        p = _open(f"{BINANCE_FAPI}/fapi/v1/premiumIndex?symbol={m['symbol']}")
        out["mark"] = float(p["markPrice"]) / m["factor"]
        out["index"] = float(p["indexPrice"]) / m["factor"]
        out["funding_pct"] = float(p["lastFundingRate"]) * 100
        out["proximo"] = datetime.fromtimestamp(int(p["nextFundingTime"]) / 1000)
    except Exception:  # noqa: BLE001
        pass
    try:
        o = _open(f"{BINANCE_FAPI}/fapi/v1/openInterest?symbol={m['symbol']}")
        if p:
            out["oi_usd"] = float(o["openInterest"]) * float(p["markPrice"])
    except Exception:  # noqa: BLE001
        pass
    try:
        ls = _open(f"{BINANCE_FAPI}/futures/data/globalLongShortAccountRatio"
                   f"?symbol={m['symbol']}&period=5m&limit=1")
        if ls:
            out["long_pct"] = float(ls[-1]["longAccount"]) * 100
    except Exception:  # noqa: BLE001
        pass
    return out or None


def resumen_24h(m):
    try:
        if m["venue"] == "mexc":
            d = _open(f"{MEXC}/api/v1/contract/ticker?symbol={m['symbol']}")["data"]
            f = m["factor"]
            return {"chg": float(d["riseFallRate"]) * 100, "high": float(d["high24Price"]) / f,
                    "low": float(d["low24Price"]) / f, "vol_usd": float(d["amount24"])}
        if m["venue"] == "yahoo":
            return None
        u = (f"{m['base']}/fapi/v1/ticker/24hr?symbol={m['symbol']}" if "fapi" in m["base"]
             else f"{m['base']}/api/v3/ticker/24hr?symbol={m['symbol']}")
        d = _open(u)
        f = m["factor"]
        return {"chg": float(d["priceChangePercent"]), "high": float(d["highPrice"]) / f,
                "low": float(d["lowPrice"]) / f, "vol_usd": float(d["quoteVolume"])}
    except Exception:  # noqa: BLE001
        return None


# ---------------------------------------------------------------- gate (trader-scalping)

def gate(rows, interval, spread_pct, taker_bps, objetivo_atr, vol_ratio, ind):
    """Aritmética de costes + tabla de condiciones de `trader-scalping`. No mide ventaja."""
    cost_pct = 2 * taker_bps / 100 + (spread_pct or 0)
    atr_pct = ind["atr"] / rows[-1]["c"] * 100 if ind["atr"] else None
    objetivo = objetivo_atr * atr_pct if atr_pct else None
    ratio = cost_pct / objetivo * 100 if objetivo else None
    up = rows[-1]["c"] > ind["ema9"]
    slope_up = ind["ema3"] > ind["ema3_3"] if ind["ema3_3"] else None
    vwap_ok = ind["vwap"] is not None

    largo = {
        "EMA3 sobre EMA9": ind["ema3"] > ind["ema9"],
        "pendiente EMA3 positiva": bool(slope_up),
        "parabólica alcista": bool(ind["sar_bull"]),
        "precio sobre VWAP": bool(vwap_ok and rows[-1]["c"] > ind["vwap"]),
        "volumen > 2× media20": vol_ratio > 2,
        "coste ≤ 25 % del objetivo": ratio is not None and ratio <= 25,
    }
    corto = {
        "EMA3 bajo EMA9": ind["ema3"] < ind["ema9"],
        "pendiente EMA3 negativa": slope_up is False,
        "parabólica bajista": not ind["sar_bull"],
        "precio bajo VWAP": bool(vwap_ok and rows[-1]["c"] < ind["vwap"]),
        "volumen > 2× media20": vol_ratio > 2,
        "coste ≤ 25 % del objetivo": ratio is not None and ratio <= 25,
    }
    bloqueos = []
    if atr_pct and atr_pct < 3 * cost_pct:
        bloqueos.append(f"ATR {atr_pct:.2f} % < 3× coste ({3 * cost_pct:.2f} %): el movimiento no paga")
    if atr_pct and spread_pct is not None and spread_pct > 0.3 * atr_pct:
        bloqueos.append(f"spread {spread_pct:.3f} % > 30 % del ATR ({0.3 * atr_pct:.3f} %)")
    if ratio is not None and ratio > 25:
        bloqueos.append(f"coste {cost_pct:.3f} % = {ratio:.0f} % del objetivo ({objetivo:.2f} %)")

    def detalle(d):
        return [f"{'✓' if v else '✗'} {k}" for k, v in d.items()]

    if bloqueos:
        ver = "esperar"
        porque = bloqueos
    elif all(largo.values()):
        ver, porque = "comprar", ["todas las condiciones del largo se cumplen"]
    elif all(corto.values()):
        ver, porque = "vender (corto)", ["todas las condiciones del corto se cumplen"]
    else:
        ver = "esperar"
        porque = ([f"al largo le falta: {', '.join(k for k, v in largo.items() if not v)}"]
                  if ind["ema3"] > ind["ema9"] else
                  [f"al corto le falta: {', '.join(k for k, v in corto.items() if not v)}"])
    return {"coste_pct": cost_pct, "atr_pct": atr_pct, "objetivo_pct": objetivo,
            "coste_sobre_objetivo": ratio, "largo": largo, "corto": corto,
            "bloqueos": bloqueos, "veredicto": ver, "porque": porque,
            "detalle_largo": detalle(largo), "detalle_corto": detalle(corto),
            "mantener": "sí" if up else "no", "precio_sobre_ema9": up}


# ---------------------------------------------------------------- salida

def fmt(x, dec_n):
    return "—" if x is None else f"{x:,.{dec_n}f}"


def fvol(v):
    """Volumen compacto: 290.6 B, 8.0 M, 12.3 k."""
    if v >= 1e9:
        return f"{v / 1e9:,.2f} B"
    if v >= 1e6:
        return f"{v / 1e6:,.2f} M"
    if v >= 1e3:
        return f"{v / 1e3:,.1f} k"
    return f"{v:,.0f}"


def pct(x, dec_n=2):
    return "—" if x is None else f"{x:+.{dec_n}f} %"


def analizar(m, interval, velas_pedidas, taker_bps, objetivo_atr, rango=None):
    rows = candles(m, interval, max(400, velas_pedidas + 220))
    f = m["factor"]
    for r in rows:  # normaliza contratos de 1000 unidades a 1 unidad
        for k in ("o", "h", "l", "c"):
            r[k] /= f
        r["v"] *= f
    c = [r["c"] for r in rows]
    ema3, ema9 = ema(c, 3), ema(c, 9)
    ema20, ema50, ema200 = ema(c, 20), ema(c, 50), ema(c, 200)
    sar, bull = psar(rows)
    a = atr(rows, 14)
    v = vwap_day(rows, interval)
    ult = rows[-1]
    dur = IV_SECONDS.get(interval, 300)
    trans = min(max((time.time() - ult["t"]) / dur, 0.02), 1)
    vols = [r["v"] for r in rows[-21:-1]]
    media20 = statistics.fmean(vols) if vols else 0
    # la vela en curso lleva menos tiempo que las cerradas: se compara contra su
    # parte proporcional, si no el volumen siempre sale bajo y la señal nunca dispara
    vol_ratio = (ult["v"] / trans) / media20 if media20 else 0
    vol_ratio_cerrada = (rows[-2]["v"] / media20) if media20 and len(rows) > 1 else 0
    flips = [i for i in range(1, len(rows)) if bull[i] != bull[i - 1]]
    ind = {"ema3": ema3[-1], "ema9": ema9[-1], "ema20": ema20[-1],
           "ema50": ema50[-1] if len(c) >= 50 else None,
           "ema200": ema200[-1] if len(c) >= 200 else None,
           "ema3_3": ema3[-4] if len(c) >= 4 else None,
           "sar": sar[-1], "sar_bull": bull[-1],
           "sar_bars": (len(rows) - 1 - flips[-1]) if flips else None,
           "atr": a, "vwap": v["valor"] if v else None,
           "vwap_velas": v["velas"] if v else 0,
           "vwap_completo": bool(v and v["completo"]),
           "vol_ratio": vol_ratio, "vol_ratio_cerrada": vol_ratio_cerrada,
           "media20": media20, "progreso": trans}
    lib = libro(m)
    spread_pct = ((lib["ask"] - lib["bid"]) / lib["bid"] * 100) if lib else None
    deriv = derivados(m)
    d24 = resumen_24h(m)
    return {"mercado": m["venue"], "simbolo": m["symbol"], "factor": f,
            "temporalidad": interval, "n": len(rows),
            "resample": m.get("_resample"), "velas": rows, "ind": ind,
            "libro": lib, "spread_pct": spread_pct, "derivados": deriv, "d24": d24,
            "gate": gate(rows, interval, spread_pct, taker_bps, objetivo_atr,
                         vol_ratio, ind),
            "yahoo_meta": m.get("_yahoo_meta")}


def dec_for(p):
    """Decimales para ~5 cifras significativas: PEPE necesita 10, BTC 2, un memecoin
    de 1e-10 necesita 14. Mostrar 0.000005 no dice nada."""
    if p is None or p == 0:
        return 6
    a = abs(p)
    if a >= 1000:
        return 2
    if a >= 1:
        return 3
    return min(14, max(5, 4 - math.floor(math.log10(a))))


def imprimir(r, n_velas):
    ult = r["velas"][-1]
    dec_n = dec_for(ult["c"])
    factor_note = f" · contrato ×{r['factor']} normalizado a 1 unidad" if r["factor"] > 1 else ""
    print(f"# {r['simbolo']} · {r['mercado']} · {r['temporalidad']}{factor_note}")
    if r["resample"]:
        print(f"  (reagrupado: {r['resample']})")
    print(f"  velas: {r['n']} · última {datetime.fromtimestamp(ult['t'], timezone.utc):%Y-%m-%d %H:%M} UTC"
          f" · {'CERRADA' if ult['cerrada'] else 'EN CURSO'}")
    if r["n"] < 200:
        print(f"  ⚠️ serie corta ({r['n']} velas): EMA200 y ATR14 no son fiables; "
              f"el gate de scalping necesita ATR, revísalo en el gráfico.")
    if r["mercado"] == "yahoo":
        print("  ⚠️ Yahoo intradía llega con retraso (~15 min en acciones US): no sirve "
              "para scalping en vivo, solo para contexto.")
    if r["d24"]:
        d = r["d24"]
        print(f"  24 h: {pct(d['chg'])} · máx {fmt(d['high'], dec_n)} · mín {fmt(d['low'], dec_n)}"
              f" · volumen {d['vol_usd'] / 1e6:,.1f} M USD")

    print(f"\n## Velas {r['temporalidad']} (O / H / L / C / V)")
    print("| hora UTC | open | high | low | close | vol |")
    print("|---|---:|---:|---:|---:|---:|")
    for v in r["velas"][-n_velas:]:
        marca = " *" if not v["cerrada"] else ""
        print(f"| {datetime.fromtimestamp(v['t'], timezone.utc):%m-%d %H:%M}{marca} | "
              f"{fmt(v['o'], dec_n)} | {fmt(v['h'], dec_n)} | {fmt(v['l'], dec_n)} | "
              f"{fmt(v['c'], dec_n)} | {fvol(v['v'])} |")
    print("`*` = vela en curso, abierta y sin cerrar (todavía puede cambiar).")

    # progreso de la vela en curso: lo que se mira para no entrar a mitad de barrido
    dur = IV_SECONDS.get(r["temporalidad"], 300)
    ahora = time.time()
    trans = r["ind"]["progreso"]
    rango = ult["h"] - ult["l"]
    pos = (ult["c"] - ult["l"]) / rango * 100 if rango else None
    falta = max(dur - (ahora - ult["t"]), 0)
    print("\n## Vela en curso · progreso")
    if ult["cerrada"]:
        print(f"  la última vela está CERRADA · siguiente apertura en "
              f"{int(falta // 60)}m {int(falta % 60):02d}s")
    else:
        print(f"  recorrido {trans * 100:.0f} % · faltan {int(falta // 60)}m {int(falta % 60):02d}s "
              f"para el cierre · cierre en {fmt(ult['c'], dec_n)} "
              f"({pct((ult['c'] / ult['o'] - 1) * 100)})")
    linea = (f"  rango {fmt(rango, dec_n)} ({rango / ult['c'] * 100 if ult['c'] else 0:.2f} % "
             f"del precio)")
    if pos is not None:
        linea += f" · cierre en el {pos:.0f} % del rango"
    print(linea)

    i = r["ind"]
    print(f"\n## Indicadores")
    print(f"  EMA3 {fmt(i['ema3'], dec_n)} · EMA9 {fmt(i['ema9'], dec_n)} · "
          f"EMA20 {fmt(i['ema20'], dec_n)}"
          + (f" · EMA50 {fmt(i['ema50'], dec_n)}" if i["ema50"] else "")
          + (f" · EMA200 {fmt(i['ema200'], dec_n)}" if i["ema200"] else " · EMA200 sin serie"))
    print(f"  precio vs EMA9 {pct((ult['c'] / i['ema9'] - 1) * 100)} · "
          f"vs EMA20 {pct((ult['c'] / i['ema20'] - 1) * 100)}"
          + (f" · vs EMA200 {pct((ult['c'] / i['ema200'] - 1) * 100)}" if i["ema200"] else ""))
    print(f"  pendiente EMA3 (3 velas) {pct((i['ema3'] / i['ema3_3'] - 1) * 100) if i['ema3_3'] else '—'}")
    print(f"  parabólica {fmt(i['sar'], dec_n)} ({'alcista' if i['sar_bull'] else 'bajista'}, "
          f"{i['sar_bars']} velas desde el giro)")
    if i["atr"]:
        print(f"  ATR14 {fmt(i['atr'], dec_n)} = {i['atr'] / ult['c'] * 100:.2f} % del precio")
    if i["vwap"]:
        nota = "" if i["vwap_completo"] else " · PARCIAL (la serie no llega al inicio de sesión)"
        print(f"  VWAP del día {fmt(i['vwap'], dec_n)} · precio {pct((ult['c'] / i['vwap'] - 1) * 100)}"
              f" ({i['vwap_velas']} velas de sesión{nota})")
    print(f"  volumen: vela en curso proyectado a vela completa / media 20 = "
          f"{i['vol_ratio']:.2f}× · última cerrada = {i['vol_ratio_cerrada']:.2f}×")

    if r["libro"]:
        b = r["libro"]
        print(f"\n## Libro\n  bid {fmt(b['bid'], dec_n)} · ask {fmt(b['ask'], dec_n)} · "
              f"spread {r['spread_pct']:.4f} %")
    d = r["derivados"]
    if d:
        print(f"\n## Futuros")
        if "funding_pct" in d:
            print(f"  funding {d['funding_pct']:+.4f} % cada 8 h"
                  f" (~{d['funding_pct'] * 3 * 365:.1f} % anual) · próximo cobro "
                  f"{d['proximo']:%Y-%m-%d %H:%M} UTC")
        if "oi_usd" in d:
            print(f"  open interest {d['oi_usd'] / 1e6:,.1f} M USD", end="")
            if "long_pct" in d:
                print(f" · cuentas largas {d['long_pct']:.0f} % / cortas {100 - d['long_pct']:.0f} %")
            else:
                print()
        print(f"  mark {fmt(d.get('mark'), dec_n)} · index {fmt(d.get('index'), dec_n)}")


def imprimir_gate(r, taker_bps, objetivo_atr):
    g = r["gate"]
    print(f"\n## Gate de scalping (trader-scalping)")
    print(f"  coste ida+vuelta {g['coste_pct']:.3f} % "
          f"(taker {taker_bps:.2f} bp ×2 + spread {r['spread_pct'] or 0:.3f} %)"
          f" · objetivo {objetivo_atr:.1f}×ATR = {fmt(g['objetivo_pct'], 2)} %"
          + (f" · coste/objetivo {g['coste_sobre_objetivo']:.0f} % (regla ≤ 25 %)"
             if g["coste_sobre_objetivo"] is not None else ""))
    print("\n  Largo:")
    for l in g["detalle_largo"]:
        print(f"    {l}")
    print("  Corto:")
    for l in g["detalle_corto"]:
        print(f"    {l}")
    print(f"\n  **Veredicto: {g['veredicto'].upper()}**")
    for p in g["porque"]:
        print(f"    · {p}")
    print(f"\n  Si ya estás dentro: {'mantener' if g['precio_sobre_ema9'] else 'cerrar'} "
          f"(cierre contra la EMA9 = {fmt(r['ind']['ema9'], dec_for(r['ind']['ema9']))}).")
    print("  Stop 0,3-0,5×ATR; tope 2R de pérdida al día; máx. 3 intentos por activo. "
          "Es aritmética de costes, no ventaja medida.")


def main():
    ap = argparse.ArgumentParser(description="Velas OHLCV en vivo, cualquier temporalidad.")
    ap.add_argument("symbol")
    ap.add_argument("--interval", "-i", default="5m")
    ap.add_argument("--velas", "-n", type=int, default=12, help="velas a imprimir (12)")
    ap.add_argument("--mercado", default="auto",
                    choices=["auto", "futuros", "spot", "mexc", "yahoo"])
    ap.add_argument("--rango", help="rango Yahoo (5d, 1mo, 3mo, 1y…)")
    ap.add_argument("--gate", action="store_true", help="añade la cuenta y el veredicto de scalping")
    ap.add_argument("--taker-bps", type=float, default=None,
                    help="comisión taker por lado en puntos básicos (5 = 0,05 %%)")
    ap.add_argument("--objetivo-atr", type=float, default=1.0,
                    help="objetivo en múltiplos de ATR de la temporalidad (1.0)")
    ap.add_argument("--watch", type=int, metavar="SEG",
                    help="repite la consulta cada N segundos")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    m = resolve(a.symbol, a.mercado)
    fee = a.taker_bps if a.taker_bps is not None else m["fee_bps"]
    if a.gate and fee is None:
        raise SystemExit("para acciones no hay comisión por defecto: pasa --taker-bps "
                         "(p. ej. 5) o quita --gate")
    while True:
        try:
            r = analizar(m, a.interval, a.velas, fee or 0, a.objetivo_atr, a.rango)
        except Exception as e:  # noqa: BLE001
            sys.exit(f"error consultando {a.symbol} {a.interval}: {e}")
        if a.json:
            salida = {k: v for k, v in r.items() if k not in ("velas", "yahoo_meta")}
            salida["velas"] = [{"t": datetime.fromtimestamp(v["t"], timezone.utc).isoformat(),
                                "o": v["o"], "h": v["h"], "l": v["l"], "c": v["c"],
                                "v": v["v"], "cerrada": v["cerrada"]}
                               for v in r["velas"][-a.velas:]]
            print(json.dumps(salida, indent=2, default=str))
        else:
            imprimir(r, a.velas)
            if a.gate:
                imprimir_gate(r, fee or 0, a.objetivo_atr)
            if a.watch:
                print(f"\n(refresco cada {a.watch}s · Ctrl-C para salir)")
        if not a.watch:
            return
        time.sleep(a.watch)


if __name__ == "__main__":
    main()

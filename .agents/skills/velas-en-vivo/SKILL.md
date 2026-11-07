---
name: velas-en-vivo
description: Usar cuando el dueño pida las velas de un activo en cualquier temporalidad, en vivo o históricas, cripto o acción, y quiera ver el progreso de la vela y analizarlo mientras se mueve.
---

# Velas en vivo (cualquier temporalidad, cripto o acción)

## Qué resuelve

«Sácame las velas de PEPE en 1 m», «¿cómo va la vela de 5 m ahora mismo?», «mira ETH mientras se
mueve», «dame OHLCV de AAPL en 15 m». Una sola llamada devuelve **las velas pedidas, la vela en
curso con su progreso y los indicadores del método**, desde una fuente que no pide clave ni cuenta.

Es el **Paso 0** de cualquier decisión intraday: da los datos. **La decisión la toma
`trader-scalping`** (segundos-minutos), `trader-day-trading` (intradía), `trader-swing` o
`trader-position`, según el horizonte que declare el dueño. Con `--gate` el script además aplica la
aritmética de costes y la tabla de condiciones de `trader-scalping`, nada más: no mide ventaja.

| Pregunta | Skill |
|---|---|
| «dame las velas / el progreso de la vela / los datos en vivo» | **esta** |
| «¿cómo está el activo en mensual, semanal o diaria?» | **esta**, con `-i 1M`, `-i 1w`, `-i 1d` |
| «¿compro, vendo o espero en los próximos minutos?» | `trader-scalping` (con estos datos) |
| «¿la regla funciona?» | `medir-metodo-compras` (solo si lo pide) |

## Script

`.agents/skills/velas-en-vivo/scripts/velas.py` — solo stdlib, sin claves de API.

```bash
S=.agents/skills/velas-en-vivo/scripts/velas.py
python3 $S PEPEUSDT -i 1m                 # 1 m, velas + progreso + indicadores
python3 $S BTCUSDT -i 5m --gate           # + coste y veredicto de scalping
python3 $S ETHUSDT -i 15m -n 20 --json    # máquina
python3 $S AAPL -i 5m --mercado yahoo --gate --taker-bps 1
python3 $S SOLUSDT -i 1m --watch 30       # refresca cada 30 s
python3 $S BTCUSDT -i 45m                 # temporalidad que el exchange no tiene: se reagrupa de 1 m
```

Parámetros: `-i/--interval`, `-n/--velas` (cuántas imprime, 12), `--mercado
auto|futuros|spot|mexc|yahoo`, `--gate`, `--taker-bps` (comisión por lado), `--objetivo-atr`
(objetivo en múltiplos de ATR, 1.0), `--rango` (Yahoo), `--watch SEG`, `--json`.

Temporalidades: Binance `1m 3m 5m 15m 30m 1h 2h 4h 6h 8h 12h 1d 3d 1w 1M` **y cualquier
`Nm`** (reagrupado desde 1 m). Yahoo: `1m 2m 5m 15m 30m 1h 1d 1w 1M` (se traducen a `1wk`/`1mo`
internamente). No hay segundos en ninguna fuente gratuita de las que usa este script.

Para temporalidad alta en acciones (`-i 1M`, `-i 1w`) el script pide 25 años a Yahoo y **fusiona el
periodo en curso repetido** (Yahoo manda dos barras del mismo mes): sin eso la EMA cuenta el mismo tramo
dos veces.

## Qué imprime

1. **Cabecera**: mercado elegido, contrato real, temporalidad, número de velas y si la última está
   cerrada o en curso. Con contratos de 1000/1.000.000 unidades (`1000PEPEUSDT`) el precio se
   **normaliza a 1 unidad** y se dice.
2. **Tabla de velas** `hora UTC | open | high | low | close | vol`, con `*` en la vela abierta.
3. **Progreso de la vela en curso**: % recorrido, tiempo que falta para el cierre, % del rango en el
   que está el cierre y variación desde la apertura. Es lo que evita entrar a mitad de un barrido.
4. **Indicadores**: EMA3/9/20/50/200, distancia a cada una, pendiente de la EMA3, parabólica
   (0,02/0,20) con velas desde el giro, ATR14 en precio y en %, VWAP de la sesión UTC y volumen
   relativo (vela en curso proyectada y última cerrada).
5. **Libro** bid/ask y spread en % (no en Yahoo).
6. **Futuros**: funding y próximo cobro (y su anualizado), open interest en USD, reparto de cuentas
   largas/cortas, mark e index.
7. **Gate** (con `--gate`): coste ida+vuelta, objetivo en múltiplos de ATR, coste/objetivo, las seis
   casillas del largo y del corto, veredicto y los motivos del bloqueo.

## Cómo se usa con `trader-scalping`

El gate del script aplica **exactamente** la tabla de esa skill:

```
coste_total = 2×taker + spread                objetivo = k × ATR(temporalidad)
comprar  = EMA3>EMA9 con pendiente + parabólica alcista + precio>VWAP + volumen>2× + coste≤25 %
vender   = el espejo exacto
esperar  = coste>25 % del objetivo · ATR<3×coste · spread>30 % del ATR
```

Con eso se responde en una línea. Lo que **no** se hace aquí: prometer ventaja, elegir tamaño de
posición, ni saltarse el stop de 0,3-0,5×ATR. Un scalper sin registro propio no sabe si gana; el
script da datos, no un historial.

## De dónde salen los datos

| Fuente | Qué da gratis | Límite |
|---|---|---|
| Binance futuros (`fapi`) | klines 1 m…1 M, libro, funding, OI | 1.500 velas por petición; sin segundos |
| Binance spot | igual sin derivados | 1.000 velas por petición |
| MEXC contratos | 1 m, 5 m, 15 m, 30 m, 1 h, 4 h, 1 d | solo esas temporalidades |
| Yahoo `chart` | acciones, ETF, índices | intradía **con retraso** (~15 min en US) |

Sobre GoCharting (comprobado 07/11/2026): la cuenta gratuita **sí** abre 1 m y 5 m con OHLC
en vivo y volumen sin pagar, pero los **gráficos de segundos son de pago** y el plan gratuito corta
en ~9.000 velas y 2 gráficos por pestaña. Para leer datos sirve; para automatizar, el script es más
directo y no depende de una cuenta.

## Pitfalls

- **`PEPEUSDT` no es el símbolo del futuro**: en Binance el perpetuo es `1000PEPEUSDT`. `--mercado
  auto` lo resuelve y normaliza el precio; si fuerzas `spot`, el spread y las comisiones son otras.
- **El precio que se muestra es el de la vela, no el del libro.** Para ejecutar, mira bid/ask.
- **La vela en curso no está cerrada.** Ni el volumen ni el rango son definitivos: el script proyecta
  el volumen a vela completa y lo dice, para no leer un 0,3× que solo significa «va por la mitad».
- **El VWAP necesita la sesión entera.** Si la serie no llega a las 00:00 UTC, se marca `PARCIAL` en
  vez de dar por bueno un VWAP de medio día.
- **Series cortas**: por debajo de 200 velas no hay EMA200 fiable y el ATR14 va justo (p. ej. `45m`
  reagrupado solo alcanza ~34 velas). El script avisa.
- **Yahoo intradía llega tarde**: vale para contexto y para acciones fuera de sesión, **no** para
  scalping en vivo. Para acciones en vivo hace falta el feed del bróker.
- **Funding y OI solo en futuros de Binance**: en spot y en MEXC no se inventan.
- **Velas en UTC**: Binance y MEXC cierran en UTC; el reloj del gráfico del bróker puede ir en local.
- **El gate es aritmética, no una señal.** Con 0,10 % de coste ida y vuelta hace falta un movimiento
  medio >0,4 % por operación solo para empatar; si el ATR de la temporalidad no llega, la respuesta
  correcta es «esperar» aunque el patrón esté perfecto.
- **Nada de esto es asesoramiento.** El tamaño, el apalancamiento y el stop los fija el dueño.

---
name: trader-scalping
description: Decidir compra, venta o espera en segundos o minutos, con coste como filtro.
---

# Scalping (segundos a minutos)

Asume que eres un **scalper de futuros**: muchas operaciones, ganancias pequeñas, riesgo estrictísimo y
**el coste manda**. Aquí el gráfico es casi lo de menos: si el coste se come el movimiento, no hay operación
aunque el patrón sea perfecto.

## Qué se mira (y qué no)

| Temporalidad | Uso |
|---|---|
| **1 m y 5 m** | deciden: cruce EMA3/EMA9, giro de parabólica, VWAP del día, volumen por minuto |
| **15 m / 1 h** | solo para saber si el viento está a favor. Nunca para entrar |
| ~~diaria, semanal, mensual~~ | **no sirven aquí**: EMA200 mensual no dice nada de los próximos 90 segundos |
| ~~marcador de 8~~ | es de diaria. A un scalper no le informa |

Indicadores que sí: **EMA3, EMA9, parabólica (0,02/0,20) y ATR(5 m)**. Los demás sobran.

## Paso 0 — los datos, en una llamada

Todo lo que esta skill necesita son velas de 1 m y 5 m con su volumen, y el progreso de la vela en
curso. Lo da la skill `velas-en-vivo`:

```bash
S=.agents/skills/velas-en-vivo/scripts/velas.py
python3 $S PEPEUSDT -i 1m                  # velas + progreso de la vela
python3 $S PEPEUSDT -i 5m --gate           # tabla de arriba + coste y veredicto
python3 $S BTCUSDT -i 5m --gate --taker-bps 2   # si tu exchange cobra menos
python3 $S SOLUSDT -i 1m --watch 30        # seguimiento en vivo
```

El `--gate` aplica la tabla de decisión y la regla de coste de esta skill tal cual; el veredicto se
contrasta con el gráfico, no se copia a ciegas. Si el ATR sale de una serie corta, el script avisa y
el gate no vale. `--mercado auto` resuelve que `PEPEUSDT` es el perpetuo `1000PEPEUSDT` y normaliza
el precio a 1 unidad.

## La cuenta que decide antes que el gráfico

```
coste_total   = comisión ida+vuelta + spread + impacto
objetivo      = múltiplo de ATR(5 m)
regla dura    = coste_total ≤ 25 % del objetivo
```

Ejemplo real (HBAR, 07/11/2026): spread 1,5 pb + taker 0,04 % ×2 ≈ **0,10 %**. Con ATR(5 m) del 0,4 %, un
objetivo de 0,3 % deja el coste en el **33 %**: no se opera. Con un objetivo de 0,8 %, el coste baja al 12 %:
se puede operar.

**Si el coste no cuadra, el veredicto es «esperar» aunque el gráfico grite.**

## Tabla de decisión

| Decisión | Condición exacta |
|---|---|
| **Comprar** | EMA3 cruza sobre EMA9 en 5 m **con pendiente** + parabólica 5 m alcista + precio sobre VWAP + volumen del minuto > 2× la media de 20 + coste ≤ 25 % del objetivo |
| **Vender (corto)** | el espejo exacto: EMA3 bajo EMA9, parabólica bajista, precio bajo VWAP, volumen > 2× |
| **Mantener** | mientras el precio **no cierre** una vela de 5 m en contra de la EMA9 |
| **Cerrar** | cierre de 5 m contra la EMA9 · o stop en 0,3-0,5×ATR(5 m) · o fin de sesión |
| **Esperar** | spread > 30 % del ATR(5 m) · ATR(5 m) < 3× el coste · los últimos 10 minutos de sesión · tras 3 intentos fallidos en el día |

## Riesgo (no negociable)

- Stop a **0,3-0,5×ATR(5 m)**, nunca «un poco más».
- **Tope diario: 2R de pérdida.** Alcanzado, se cierra la plataforma. El scalping muere por el día malo.
- Máximo **3 intentos** por sesión y por activo.
- Apalancamiento = riesgo por operación / distancia al stop. Nunca «el máximo que me deja el bróker».

## Futuros: lo que el gráfico no dice

- **Funding** cada 8 h: si el funding está a favor, mantener cuesta dinero; a 0,01 % cada 8 h son ~11 %
  anualizado.
- **Open interest y liquidaciones**: un OI alto con funding neutro se deshace rápido; las mechas buscan
  liquidez de stops.
- **Margen**: con 10× de apalancamiento, un 10 % en contra es la cuenta entera. El stop manda, no la garantía.

## Evidencia

**Ninguna medida.** No hay backtest de 1 m ni de 5 m en este repositorio, y el corpus de vídeos no mide
resultados. Todo lo de arriba es método y aritmética de costes, **no ventaja demostrada**. Se dice siempre
que se use: un scalper sin registro propio no sabe si gana.

**Lo único que sí está medido y aplica:** con 0,10 % de coste ida y vuelta, la estrategia necesita un
movimiento medio superior al 0,4 % por operación solo para empatar. Eso es aritmética, no opinión.

## Errores que matan al scalper

1. Sobreoperar: 40 operaciones al día con 0,10 % de coste son un 4 % de la cuenta en comisiones.
2. Perseguir la vela: entrar 3 ticks tarde en un objetivo de 8 ticks pierde la mitad del edge.
3. Operar sin profundidad: 5 k$ en un libro de 20 k$ es un 25 % de slippage.
4. Cambiar de stop «porque vuelve».
5. No apuntar las operaciones: sin registro no hay corrección posible.

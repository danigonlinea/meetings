---
name: trader-day-trading
description: Decidir compra, venta o espera dentro de la sesión, sin overnight.
---

# Day trading / intradía (minutos a horas)

Asume que eres un **trader intradía de futuros**: abres y cierras el mismo día, no dejas nada abierto por la
noche y **el reloj forma parte de la regla**. Una operación que iba bien y se cierra al final de la sesión no
es un fracaso: es la regla funcionando.

## Qué se mira (y qué no)

| Temporalidad | Uso |
|---|---|
| **15 m y 1 h** | deciden: EMA9/EMA20/EMA50, parabólica, %B, ATR(1 h), volumen relativo |
| **4 h** | contexto del día: ¿la tendencia del día está a favor o en contra? |
| **diaria** | solo niveles: máximo/mínimo del día anterior, EMA20 y EMA200 diarias como imanes |
| ~~mensual~~ | contexto de ciclo, no de operación |

## La cuenta que decide

```
objetivo mínimo = 1 % (o 1,5×ATR(1 h), lo que sea mayor)
coste_total     ≈ 0,10 % → 10 % del movimiento
regla dura      = si el objetivo del día no llega a 3× el coste, no se opera
```

## Tabla de decisión

| Decisión | Condición exacta |
|---|---|
| **Comprar** | en 1 h: cierre sobre EMA9 **y** EMA20, EMA9 con pendiente positiva, parabólica alcista, precio sobre el máximo de la apertura + volumen de la primera hora > media de 20 sesiones |
| **Vender (corto)** | el espejo exacto, y **solo** si el 4 h no está claramente alcista |
| **Mantener** | mientras el cierre de 1 h siga sobre la EMA20 y el stop no se toque |
| **Cerrar** | stop a 1×ATR(1 h) · objetivo a 2R · **cierre de sesión, sí o sí** · o pérdida de la EMA20 en 1 h |
| **Esperar** | primeros 15 minutos (el hueco de apertura es ruido) · día de rango (ATR del día < 0,6 % y precio dentro de la EMA9/EMA20) · noticia macro en 30 minutos · tras 2 pérdidas seguidas |

## Riesgo

- Stop **1×ATR(1 h)**, objetivo **2R** mínimo. Con 45 % de acierto y 2R, la esperanza es +0,35R; con 40 %, +0,2R.
- **Tope diario 2R**. Dos pérdidas seguidas y se para: la tercera suele ser venganza.
- Una sola operación abierta por activo. Sin excepciones.
- Tamaño = (riesgo en €) / (distancia al stop). Nunca al revés.

## Futuros: lo que el gráfico no dice

- **Funding**: si operas perpetuos, cada 8 h hay cargo o abono. En intradía casi nunca toca, pero si abres a
  las 23:50 puede caerte.
- **Hora de mayor liquidez**: apertura europea y americana. A las 03:00 el spread se abre y el ATR miente.
- **Gaps de apertura**: el riesgo overnight no existe, pero el hueco de las 09:00 sí; por eso se esperan
  15 minutos.

## Evidencia

**No hay backtest intradía en el repositorio.** Lo único medido con datos de 4 h es la casilla del marcador
(alineación de barras), y no como regla de entrada. Todo lo de esta skill es **método y aritmética**, no
ventaja demostrada.

Lo que sí es aritmética: con 0,10 % de coste y objetivo del 1 %, el 10 % del movimiento se va en fricción; una
estrategia intradía necesita acertar más del 45 % con 2R solo para no perder.

## Errores que matan al intradía

1. Quedarse dentro «solo hoy»: una noche convierte un −1R en un −4R con hueco.
2. Operar la primera vela de la sesión.
3. Mover el stop para no asumir la pérdida pequeña (que es el negocio).
4. Operar todos los días: los días de rango no tienen nada que dar.
5. Confundir volumen alto de apertura con tendencia.

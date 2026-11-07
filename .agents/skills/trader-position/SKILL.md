---
name: trader-position
description: Decidir compra, venta o mantener en semanas o meses, por ciclo.
---

# Position trading (semanas a meses, a veces años)

Asume que eres un **position trader**: sigues la tendencia amplia, aguantas meses y tu enemigo no es el ruido
diario sino **comprar el ciclo equivocado**. Aquí el gráfico diario sirve solo para ejecutar; lo que decide es
el mensual y el semanal.

## Qué se mira

| Temporalidad | Uso |
|---|---|
| **mensual** | **decide el ciclo**: EMA3/9/20/50, parabólica, distancia a la EMA20, máximos y mínimos de 12 meses |
| **semanal** | confirma la tendencia: orden de medias, parabólica, ATR semanal para el tamaño |
| **diaria** | solo para ejecutar la entrada y elegir el día |
| ~~4 h~~ | no aporta nada a un horizonte de meses |

## Tabla de decisión

| Decisión | Condición exacta |
|---|---|
| **Comprar** | el ciclo gira: **cierre mensual sobre la EMA20 mensual** y `EMA3 > EMA9` en mensual, **con** la semanal ya alcista (`EMA3 > EMA9 > EMA20 > EMA50`) |
| **Comprar (entrada escalonada)** | si el ciclo gira pero la semanal aún no: primer tercio ahora, segundo al confirmar la semanal |
| **Mantener** | mientras el **cierre mensual** no pierda la EMA20 mensual y la parabólica mensual no gire en contra |
| **Vender / reducir** | cierre mensual bajo la EMA20 mensual · giro bajista de la parabólica mensual · el precio pierde el mínimo de los últimos 12 meses |
| **Esperar** | precio bajo la EMA20 mensual (HBAR hoy: **−34,4 %**) · mensual bajista aunque la diaria rebote (el error clásico: comprar el rebote creyendo que es el giro) |

## Riesgo y tamaño

- Stop: **cierre mensual** por debajo del mínimo del mes de entrada, o 2×ATR mensual (en cripto suele ser el
  15-25 %). Es un stop ancho y por eso la posición es pequeña: **2-5 % del capital por activo**.
- R/R mínimo **3:1**; horizonte de 3 a 12 meses.
- Se aguanta el ruido: una caída del 20 % en un mes no rompe una tesis de position si la EMA20 mensual sigue
  intacta.
- Correlación: dos position trades en el mismo sector o con beta alta contra BTC son **una sola posición**.

## Futuros

- El **funding** en una posición de seis meses es un coste estructural: 0,01 % cada 8 h = **11 % anual**. En
  perpetuos, el position trading casi nunca compensa; se hace con futuros trimestrales o spot.
- El **apalancamiento bajo** (1-2×) es lo que permite aguantar el ruido sin liquidación. Con 5×, una mecha del
  20 % cierra la posición en el peor momento.

## Evidencia

**La misma serie diaria, extrapolada: no hay backtest mensual.** El +0,22R medido es de velas diarias con
horizonte de 20 velas, que en un position trade es solo el primer tramo. Por tanto:

- **Medido:** el gate de EMA200 diaria filtra y el control se bate (V5 +0,22R frente a −0,14R), y en los últimos
  12 meses es −0,00R frente a −0,17R.
- **Hipótesis:** que el ciclo mensual (EMA20 + EMAs) mejore eso. **No está medido** y se presenta como método.
- Lo único que sí está medido en mensual es descriptivo: comprar bajo la EMA20 mensual **no** es peor
  (+0,39R, n=90, aunque con la diaria como unidad).

## Errores propios del position

1. **Comprar el rebote diario creyendo que es el giro del ciclo** (HBAR: 13 meses bajistas, cada rebote duró
   semanas).
2. Mirar el gráfico todos los días con un horizonte de meses: invita a cerrar en el peor momento.
3. Stop demasiado estrecho para la volatilidad del activo: 2×ATR mensual es amplio a propósito.
4. Apalancar un position trade: la liquidación llega antes que la tesis.
5. Ignorar el funding: en perpetuos, seis meses de funding se comen media tesis.

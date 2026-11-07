---
name: trader-swing
description: Decidir compra, venta, mantener o esperar en días o semanas.
---

# Swing trading (días a semanas)

Asume que eres un **swing trader de futuros**: buscas la oscilación, aguantas de días a semanas y tienes tiempo
para esperar la señal. Es **la única variante con ventaja medida** en este repositorio, y también la única en
la que merece la pena recalcular el backtest.

## Qué se mira

| Temporalidad | Uso |
|---|---|
| **diaria** | decide: gate de EMA200 + vela de entrada + volumen, EMA3/9/20/50, parabólica, ATR14 |
| **semanal** | contexto y caja: `EMA3 > EMA9 > EMA20 > EMA50` y los 3-5 últimos máximos/mínimos |
| **4 h** | solo timing fino y stop más corto |
| **mensual** | solo contexto de ciclo: no veta nada |

Protocolo completo, gate y marcador: skill **`trading-action`**. Aquí solo se fija lo que es propio del swing.

## Tabla de decisión

| Decisión | Condición exacta |
|---|---|
| **Comprar** | gate cumplido (cierre diario sobre **EMA200** + vela de entrada + volumen > 1,5× media de 20) y marcador **8/8** o 7/8 con la 4 h como única casilla vacía |
| **Comprar (media posición)** | 5-6/8 con la vela de entrada en el borde de la caja |
| **Mantener** | mientras el cierre diario siga sobre la **EMA20** y la parabólica diaria no gire a bajista |
| **Vender / cerrar** | cierre diario bajo la EMA20 · giro bajista de la parabólica · rechazo en el borde superior de la caja · objetivo 2R alcanzado |
| **Esperar** | sin gate · precio entre la EMA9 y la EMA20 sin volumen · tercera o posterior señal del mismo movimiento (se compra continuación, mitad de tamaño) |

## Riesgo y tamaño

- Stop: **máximo de la vela de entrada** o **1,5-2×ATR14**, el más cercano de los dos.
- R/R mínimo **2:1**; el objetivo natural es el borde opuesto de la caja semanal.
- Tamaño: con riesgo del 1 % de la cuenta y stop del 7 % (media medida), la posición es el **14 % del capital**.
  Si eso es demasiado, se baja el riesgo, no se sube el stop.
- Duración esperada 5-30 días. Si a los 30 días no ha hecho nada, la tesis caducó: se cierra o se pone a cero.

## Futuros

- **Funding**: en una posición de dos semanas, 0,01 % cada 8 h = **0,42 %** de coste. Se suma al R/R antes de
  entrar.
- **Open interest**: un OI que sube con el precio confirma; que sube con el precio plano avisa de trampa.
- **Apalancamiento**: con 3×, un stop del 7 % es un 21 % de la garantía. El stop define el apalancamiento.

## Evidencia medida (lo que hay)

| Versión | n | Episodios | Acierto | R medio |
|---|--:|--:|--:|--:|
| Control (1 de cada 3 días) | 3.926 | 570 | 29,1 % | −0,14 |
| Vela de entrada + volumen + EMA200 | 513 | 165 | 42,3 % | **+0,22** |

- Con 0,2 % de costes: **+0,18R**. Últimos 12 meses: **−0,00R** frente a −0,17R del control.
- Mediana **−1R**: la operación típica pierde; la ventaja vive en la cola. Eso obliga a no saltarse ninguna
  señal buena y a no promediar a la baja.
- Por activo: BTC +0,49 · SOL +0,47 · AVAX +0,31 · XRP +0,27 · LINK +0,21 · DOGE +0,19 · ADA +0,17 · BNB +0,14 ·
  ETH +0,12 · QNT −0,16. Elegir el activo pesa tanto como el momento.
- Recalcular (solo si el dueño lo pide): skill **`medir-metodo-compras`**.

## Errores propios del swing

1. **Comprar la tercera señal** de un movimiento como si fuera la primera (HBAR dic-2024 a ene-2025: −2 % a
   −50 % al cierre de 60 velas).
2. Convertir un swing en una inversión cuando sale mal: «ya volverá» no es un plan.
3. Saltarse el gate porque «la vela es muy bonita».
4. Ignorar el funding en posiciones de tres semanas.
5. Cerrar en verde por miedo antes de 1R: con 42 % de acierto, cortar las ganadoras rompe la esperanza.

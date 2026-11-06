---
title: "Revisión adversarial del método de entradas, con backtest de 10 pares"
date: 2026-11-06
type: synthesis
category: finance
tags: [analisis-tecnico, revision-adversarial, backtest, cripto, identificar-compras]
status: living
---

# Revisión adversarial del método de compras

Objeto: la skill `identificar-compras` (embudo mensual → semanal → diaria → 4 h, vela de entrada con
volumen, confluencia y R/R). Prueba: **backtest mecánico sobre 10 pares /USDT** de Binance, 1.000 velas
diarias por par (≈ 2,7 años: 2023-11 a 2026-11). Script: `.agents/skills/identificar-compras/scripts/backtest_entradas.py`.
Reproducible con `python3 backtest_entradas.py --rr 2`.

**Veredicto en una línea:** el método **tiene ventaja real pero fina** (+0,18R por operación en su mejor
versión, con 41 % de acierto), y **dos de sus tres filtros no sirven**: el sesgo mensual y la triple
confirmación diaria restan; el que suma es la EMA200. La parte que se sostiene es la vela de entrada con
volumen, no el ritual de temporalidades.

## 1. Cómo se probó (y qué se descarta por diseño)

- **Regla base (V2):** vela con mínimo superior al anterior, cierre positivo y volumen > 1,5× la media de 20.
  Entrada al cierre de esa vela. Stop en el mínimo de la vela. Objetivo a R múltiplos. Horizonte 20 velas.
- **Conservador:** si en la misma vela se tocan stop y objetivo, cuenta como pérdida.
- **Control (BASE):** todas las velas (una de cada tres) con la misma regla de stop/objetivo. Sirve para
  saber si la señal añade algo o si el resultado es del mercado.
- **Lo que no prueba:** intradía (no hay datos públicos de sus operaciones de 1 minuto), ni comisiones
  (0,15 % de ida y vuelta ≈ 0,02R sobre un riesgo medio del 7,3 %: irrelevante para la conclusión).

## 2. Resultado principal

Objetivo 2R, horizonte 20 velas, 10 pares (BTC, ETH, SOL, BNB, XRP, ADA, AVAX, LINK, DOGE, QNT):

| Versión | Filtros añadidos | n | Acierto | R medio | R total |
|---|---|--:|--:|--:|--:|
| **BASE** | ninguna (control) | 3.176 | 27,7 % | **−0,18** | −575 |
| **V2** | vela de entrada + volumen | 535 | 38,3 % | **+0,11** | +57,8 |
| **V3** | V2 + sesgo mensual (precio > EMA20 mensual) | 319 | 35,1 % | **+0,01** | +3,4 |
| **V4** | V3 + cierre sobre EMA9/EMA20 + parabólica diaria | 274 | 36,9 % | **+0,06** | +16,4 |
| **V5** | V2 + precio sobre **EMA200 diaria** | 284 | **41,2 %** | **+0,18** | +52,5 |

**Tres cosas que dice la tabla, y ninguna es cómoda:**

1. **La señal sirve.** El control pierde en todas las configuraciones (−0,18R): el mercado, comprado al azar
   con este stop, no da dinero. La vela de entrada sí (+0,11R).
2. **El sesgo mensual y la confirmación diaria restan.** V3 (+0,01) y V4 (+0,06) son peores que V2 (+0,11):
   los filtros de la skill **eliminan justo las operaciones buenas**. Es la corrección más importante de esta
   revisión.
3. **El filtro que sí suma es la EMA200 diaria** (V5: 41 % de acierto y +0,18R). No es sorprendente —evita
   comprar rebotes en tendencia bajista— pero desmonta la jerarquía que la skill tenía escrita.

## 3. Sensibilidad al objetivo

| Objetivo | V2 | V5 |
|---|---|---|
| 1R | 50,8 % acierto · **+0,03R** | 54,2 % · +0,10R |
| **2R** | 38,3 % · +0,11R | 41,2 % · **+0,18R** |
| 3R | 33,5 % · +0,14R | 35,6 % · +0,21R |

El método es de **cola gorda**: cuanto más lejos el objetivo, mejor la esperanza y peor el acierto. Con 2R y
41 % de acierto, la esperanza es +0,18R por operación; con 1 % de riesgo por operación eso es **+0,18 % por
operación**, no una máquina de hacer dinero.

## 4. Dispersión por activo (V2, 2R)

| Par | n | Acierto | R medio | R total |
|---|--:|--:|--:|--:|
| SOL | 41 | 48,8 % | +0,39 | **+15,9** |
| XRP | 60 | 41,7 % | +0,26 | +15,5 |
| BNB | 63 | 41,3 % | +0,21 | +13,2 |
| LINK | 61 | 37,7 % | +0,13 | +8,2 |
| DOGE | 62 | 38,7 % | +0,11 | +6,8 |
| BTC | 41 | 41,5 % | +0,12 | +5,0 |
| QNT | 55 | 34,5 % | −0,00 | −0,1 |
| ADA | 54 | 33,3 % | −0,01 | −0,6 |
| AVAX | 52 | 36,5 % | −0,05 | −2,5 |
| ETH | 46 | 30,4 % | −0,08 | **−3,6** |

**Cuatro de diez pares pierden dinero con la misma regla.** Elegir el activo importa tanto como el momento:
la señal no convierte en buena una tendencia que no existe. (Cuidado: elegir a posteriori los seis que
ganan es sobreajuste, no una mejora.)

## 5. Ejemplos reales

**Los que funcionaron — BTC, octubre-noviembre de 2024.** Cinco señales seguidas (14/10, 15/10, 06/11,
10/11 y 13/11 de 2024) dieron **+2R cada una**. Eran velas de entrada con volumen dentro de la tendencia que
acababa de superar la EMA200: el filtro de V5 las habría dejado pasar todas.

**El que falló — QNT, 29 y 30 de septiembre de 2026.** Las dos velas cumplían la regla (mínimo superior,
cierre positivo y volumen de 3,9× y 3,5×) y las dos se resolvieron en **−1R**. El motivo está a la vista: se
compró **la parte vertical** de un movimiento que ya llevaba un 4x en dos semanas. Volumen alto no es lo
mismo que volumen sano: en una subida vertical, el 3,9× es distribución, no acumulación.

**La lección de los dos casos:** la regla no distingue «volumen que acompaña una ruptura» de «volumen que
descarga una subida». Esa es la mejora pendiente más importante.

## 6. Mejoras concretas (con el número que las respalda)

1. **Sustituir el filtro mensual por la EMA200 diaria.** +0,18R frente a +0,01R: la misma idea (no comprar
   contra la tendencia) medida de forma que funciona.
2. **Quitar la triple confirmación diaria como filtro de entrada.** V4 (+0,06R) es peor que V2 (+0,11R):
   llega tarde y deja fuera las mejores. Se conserva como **criterio para añadir tamaño**, no para entrar.
3. **Objetivo 2R por defecto y 3R si se tolera un 35 % de acierto.** A 1R la ventaja casi desaparece
   (+0,03R): con objetivos cortos el método no paga el trabajo.
4. **Capar el stop a 2×ATR.** El riesgo medio de la vela de entrada es el **7,3 % del precio**: con 1 % de
   riesgo de cuenta, eso obliga a poner el 13,7 % del capital en una operación. Si la vela es más ancha que
   2×ATR, se salta la señal o se busca la entrada en 4 h.
5. **Añadir un filtro de «no comprar vertical».** Pendiente de probar, pero los dos −1R de QNT vienen de
   ahí: si el precio está a más de 2×ATR de la EMA20 diaria, la vela de entrada no se opera.

## 7. Segunda pasada: la vertical no era el problema, y la ventaja se ha apagado

Dos comprobaciones posteriores, con el mismo script:

**a) La prohibición de comprar vertical no se sostiene.** Repartiendo las 284 operaciones de V5 por distancia
a la EMA20 y por subida en 30 velas:

| Distancia a la EMA20 | n | Acierto | R medio |
|---|--:|--:|--:|
| ≤ 10 % | 95 | 43,2 % | +0,21 |
| 10-25 % | 138 | 39,9 % | +0,17 |
| > 25 % | 51 | 41,2 % | +0,18 |

| Subida en 30 velas | n | Acierto | R medio |
|---|--:|--:|--:|
| 0-25 % | 149 | 43,0 % | +0,24 |
| 25-50 % | 84 | 42,9 % | +0,25 |
| 50-100 % | 29 | 24,1 % | **−0,31** |
| > 100 % | 22 | 45,5 % | +0,24 |

Comprar en vertical funciona igual que comprar tranquilo. El único tramo malo es el intermedio (50-100 % en
un mes), con 29 operaciones: muestra para reducir tamaño, no para vetar. Y el contraejemplo es de manual:
HBAR el 16/11/2024 cerró a 0,090, un 107 % sobre su EMA20, y llegó a 0,392 en veinte velas (**+335 %**).

**b) La ventaja de los últimos doce meses no existe.**

| Periodo | n | Acierto | R medio |
|---|--:|--:|--:|
| completo | 284 | 41,2 % | +0,18 |
| últimos 12 meses | 64 | 32,8 % | **−0,03** |
| últimos 6 meses | 58 | 34,5 % | +0,01 |

Con 64 operaciones no se puede afirmar que el método haya muerto, pero tampoco que esté vivo. Mientras no se
demuestre, se usa como filtro de calidad y no como fuente de esperanza. Comando nuevo: `--desde 2025-11-06`.

## 8. Límites de esta revisión

- **2,7 años y un solo ciclo** (un mercado alcista con una corrección): no cubre 2018 ni 2022.
- **Cinco variantes probadas y elegida la mejor**: es el riesgo clásico de *data snooping*. Que V5 gane en
  los tres objetivos (1R, 2R y 3R) reduce el riesgo, pero **no lo elimina**: falta una prueba fuera de
  muestra (otros pares, otro periodo).
- **Sin intradía y sin comisiones**, ya explicado: no cambia la conclusión pero sí el detalle.
- **Los pares son los grandes**: en monedas pequeñas el volumen y el spread cambian el resultado.

## 9. Qué se cambia en la skill

- Paso 1 (sesgo): deja de ser requisito de entrada; la mensual queda como contexto.
- Paso 3 (confirmación): el filtro pasa a ser **precio sobre EMA200 diaria**; la triple confluencia se
  degrada a criterio para escalar posición.
- Paso 5: la vela de entrada incorpora la condición de EMA200 y la prohibición de comprar vertical.
- Se añade la tabla de resultados y el enlace a este documento.

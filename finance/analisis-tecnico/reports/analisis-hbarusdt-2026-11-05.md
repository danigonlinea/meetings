---
title: "HBAR/USDT — lectura mensual, semanal y diaria (05/11/2026)"
date: 2026-11-05
type: synthesis
category: finance
tags: [analisis-tecnico, hbar, hedera, mensual, semanal, diaria, informe]
status: draft
---

# HBAR/USDT — informe del 05/11/2026

Datos: Yahoo Finance `HBAR-USD` (par equivalente a HBARUSDT; la diferencia con Binance es de céntimos de
milésima), velas mensuales de 10 años, semanales de 5 y diarias de 1. Método: el documentado en
`metodo.md`. **No es asesoramiento.**

Precio de referencia: **0,0681 USD**.

## 1. Las tres vistas, en una tabla

| Vista | EMA3 | EMA9 | EMA20 | EMA50 | EMA200 | Parabólica | %B | Dist. EMA20 | Orden de medias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **Mensual** | 0,0710 | 0,0832 | 0,1036 | 0,1173 | — (sin historia) | 0,1843 bajista, **14 meses** | 26 % | **−34,3 %** | 50 > 20 > 9 > 3 |
| **Semanal** | 0,0703 | 0,0771 | 0,0803 | 0,0973 | 0,1146 | 0,1234 bajista, 3 semanas | 29 % | −15,3 % | 200 > 50 > 20 > 9 > 3 |
| **Diaria** | 0,0687 | 0,0708 | 0,0751 | 0,0803 | 0,0850 | 0,0738 bajista, **giro ayer** | 17 % | −9,4 % | 200 > 50 > 20 > 9 > 3 |

Contexto de rango: máximo de 12 meses **0,1978** (el precio está **−65,6 %** por debajo), mínimo de 12 meses
**0,0643** (el precio está **+5,9 %** por encima). La vela mensual en curso lleva un rango de 0,0673-0,0690:
es un doji, todavía sin dirección.

## 2. Lectura por temporalidad

**Mensual — claramente bajista, sin compra posible.** Las cuatro medias están en orden bajista perfecto
(50 > 20 > 9 > 3) y el precio está por debajo de todas, a un **−34 % de la EMA20**. La parabólica lleva
**14 meses** sin girar. Octubre cerró negativo (0,0718 → 0,0673), y la regla del método es explícita:
*sI la vela del mes cierra negativa, no hay call de compra*. Noviembre va +1,2 % pero dentro del rango y
sin superar ni la EMA3.

**Semanal — la misma estructura, un escalón más cerca.** Orden 200 > 50 > 20 > 9 > 3, precio un **−40,7 %
por debajo de la EMA200**. La caja operativa de las últimas semanas es **0,0667-0,0738**: mientras no se
rompa por arriba, no hay nada que comprar. La parabólica semanal está en 0,1234, tan lejos que no sirve de
gatillo en semanas.

**Diaria — bajista y recién roto.** La parabólica **giró a bajista ayer** (0,0738, el máximo del último
día alcista) y el precio perdió la EMA3 y la EMA9. El %B está en 17 %, bajo pero **no en sobreventa extrema**
(eso exige < 0 %, es decir, por debajo de 0,0644).

## 3. ¿Compra o venta?

**Ni una ni otra: espera.** Y las dos razones salen del propio método:

- **No hay compra** porque el ecosistema está en contra en las tres vistas (medias en orden bajista,
  precio bajo todas, parabólica bajista en las tres). Comprar aquí es el caso que el método prohíbe.
- **No hay venta** porque el precio está a **+5,9 % del mínimo anual**: su primera regla de oro es
  *prohibido vender en el piso*. Abrir corto a 6 % del mínimo de 12 meses con un %B de 17 % es exactamente
  el error que el método señala.

Si hubiera que inclinarse, la balanza está del lado **vendedor en el corto plazo** (parabólica diaria recién
girada, precio bajo EMA3/9) y del lado **neutral en el mensual** (doji en zona de mínimos). Pero ninguna de
las dos es una entrada con el método: es una zona de espera.

## 4. Los disparadores, con nivel

**Para pasar a compra (por orden de importancia):**

| Disparador | Nivel | Qué significa |
|---|---:|---|
| Cierre diario sobre la EMA20 | **0,0751** | primer cambio de sesgo; hoy está un −9,4 % por debajo |
| Giro de la parabólica diaria | **0,0738** | se gira con un máximo diario por encima |
| Confluencia EMA20 semanal = EMA50 diaria | **0,0803** | la resistencia que decide si el rebote es de verdad |
| EMA200 diaria | **0,0850** | solo por encima de aquí se puede hablar de tendencia |
| Capitulación con rechazo en el mínimo anual | **0,0643** | el único largo que el método admite en entorno bajista: mecha por debajo, cierre dentro y %B < 0 |

**Para pasar a venta / seguir corto:**

| Disparador | Nivel | Qué significa |
|---|---:|---|
| Pérdida del mínimo de 12 meses | **0,0643** | rompe estructura; ahí ya no se habla de «piso» |
| Rechazo en 0,0738-0,0751 | zona | dentro de la caja semanal, el techo para recargar cortos |
| Banda inferior semanal | **0,0557** | objetivo si se pierde el mínimo anual |

**Invalidación de todo lo anterior:** un cierre mensual por encima de **0,0832** (EMA9 mensual) cambia el
escenario de fondo y obliga a rehacer el análisis desde la vista mensual.

## 5. Límites de este informe

- El método es de **intradía y de niveles del día siguiente**; aplicado a velas mensuales se usa solo su
  parte de estructura (orden de medias, parabólica, %B, posición en el rango), no sus gatillos de 1 minuto.
- La revisión adversarial (`revision-adversarial.md`) aplica aquí: **ningún nivel de este informe es una
  orden sin stop**. La invalidación de un largo estaría en 0,0643; la de un corto, en 0,0803.
- No hay tamaño de posición en este documento: eso depende de la cuenta y no lo decide el análisis técnico.

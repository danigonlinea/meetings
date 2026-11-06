---
title: "QNT/USDT — cómo se construye la entrada bajando de temporalidad (06/11/2026)"
date: 2026-11-06
type: synthesis
category: finance
tags: [analisis-tecnico, qnt, entrada, temporalidades, multi-temporal, compra]
status: draft
---

# QNT/USDT — de la vela mensual al gatillo

Precio de referencia: **190,70** (06/11/2026, 16:00 UTC). Datos: klines de Binance, mensual, semanal,
diaria y 4 horas. **No es asesoramiento.**

## 1. El problema que planteas, con la cifra delante

La vela mensual de septiembre fue **gigantesca**: abrió en **61,12**, llegó a **373,00** y cerró en
**287,15** — un 6x dentro del mismo mes. Octubre abrió en 287,00 y cerró en **201,11**, con mínimo en
**173,56**.

Quien comprara «porque la mensual es alcista» al cierre de septiembre pagó **287** y vio **−40 %** en tres
semanas. **Tenías razón: la mensual no es una entrada.** La mensual sirve para dos cosas y ninguna es
comprar:

1. **Sesgo:** el precio está por encima de su EMA20 mensual (116,2), así que el sesgo es alcista y solo se
   buscan largos, nunca cortos contra esa estructura.
2. **Niveles grandes:** 373,00 (máximo), 287,15 (cierre de septiembre), 173,56 (mínimo de octubre).

## 2. El embudo, temporalidad por temporalidad

### Semanal — aquí aparece el rango, y es lo que bloquea la compra

| Semana | Máximo | Mínimo | Cierre |
|---|--:|--:|--:|
| 05/10 | 270,14 | 220,63 | 238,68 |
| 12/10 | 243,36 | 181,74 | 192,23 |
| 19/10 | 212,87 | **173,56** | 190,21 |
| 26/10 | 223,96 | 175,15 | 201,73 |
| 02/11 | 210,98 | 185,35 | 190,63 |

Los máximos bajan (270 → 243 → 213 → 224 → 211) y los mínimos suben tras el suelo (173,56 → 175,15 →
185,35): es una **caja que se cierra**, entre **175 y 211**. Esto es lo que la mensual no te dice: en
septiembre hubo tendencia, desde octubre hay **rango**. Comprar en mitad de la caja (190) no tiene ventaja;
la ventaja está en los bordes.

### Diaria — la señal sola falló dos veces

| Fecha | Qué hizo la señal | Qué pasó |
|---|---|---|
| 26/10 | PSAR giró a alcista en **173,56** (el mínimo) y cerró 204,01 sobre EMA9 y EMA20 | subió a **223,96** ese mismo día y se giró a bajista el 30/10 |
| 04/11 | máximo **210,98**, cierre 204,15, sobre EMA20 (197,82) | el 05/11 se dio la vuelta hasta **185,93** |

Dos flips de parabólica en diez días. **Lección: la parabólica no es el gatillo por sí sola** — es la
condición, no la señal. Sin confluencia (nivel + EMA + cierre), dos de dos fueron falsas.

### 4 horas — aquí sí hubo una entrada identificable en tiempo real

- **04/11 08:00:** la parabólica de 4 h **gira a alcista en 185,35** y la vela cierra en **201,71**, por
  encima de la EMA9 (195,21) y de la EMA20 (195,75). **Ese es el gatillo**: rotación + precio sobre las dos
  medias.
- Recorrido: de ~186 a **210,98** (+13 % en 28 horas).
- **05/11 12:00:** la parabólica de 4 h **gira a bajista en 210,98** con cierre en 191,86. **Esa es la
  salida**, y coincidía con el techo de la caja semanal.

Esa es la respuesta a «cómo lo habría identificado»: **sesgo en la mensual, caja en la semanal, gatillo en
4 h, y el techo de la caja como salida.** No hay que adivinar: las tres piezas estaban escritas en el
gráfico antes de que el precio se moviera.

## 3. El protocolo para ahora mismo (precio 190,70)

| Paso | Qué mirar | Nivel | Estado hoy |
|---|---|--:|---|
| 1. Sesgo | Precio sobre EMA20 mensual | 116,2 | ✅ alcista: solo largos |
| 2. Zona | Borde inferior de la caja semanal | 175-186 | ⏳ el precio está en el centro (190,7): sin ventaja |
| 3. Gatillo | PSAR 4 h a alcista + cierre sobre EMA20 4 h | **194,44** | ❌ PSAR 4 h bajista (203,34) y precio por debajo |
| 4. Confirmación | Cierre diario sobre EMA20 y sobre el último máximo | **196,36** y **210,98** | ❌ no |
| 5. Stop | Mínimo de la semana / mínimo de octubre | **185,35** y **173,56** | — |
| 6. Objetivos | Techo de caja → máximo de octubre | **210,98** → **223,96** → 243,36 | — |

**Plan escalonado, si se dan las condiciones:** un tercio al gatillo de 4 h (rotación con cierre sobre
194,44), un tercio al cierre diario sobre 196,36, y el último tercio solo si rompe **223,96** (ahí deja de
ser rango y vuelve a ser tendencia). Stop común bajo **185,35**; si pierde **173,56**, la tesis del rango se
cae y se sale entero.

## 4. Lo que no hay que hacer (y ya se hizo mal en el corpus)

- **Comprar el cierre mensual.** Costó −40 % en tres semanas.
- **Comprar en 210.** Es el techo de la caja, no el suelo: el 04/11 lo tocó y el 05/11 se deshizo.
- **Comprar sin stop.** Los dos flips falsos de la diaria lo demuestran: sin invalidación, el 26/10 y el
  04/11 habrían sido dos pérdidas sin límite.
- **Comprar en el centro del rango.** A 190,70 no hay ni suelo ni techo; el método pide borde o ruptura.

## 5. Lo que este caso enseña del método

1. La temporalidad mayor da **contexto**, no entrada: sesgo y niveles, nada más.
2. Cuando la mensual es gigante, el rango se forma en la semanal; ahí está la caja que sí se puede operar.
3. El gatillo de verdad es la **confluencia** (rotación de parabólica + cierre sobre EMA9/EMA20), y se
   ejecuta en la temporalidad en la que el stop es pequeño: aquí, 4 horas.
4. La salida se pone en el borde opuesto de la caja, no en un número inventado.
5. Y el límite de siempre (`revision-adversarial.md`): acierta niveles, no direcciones. Por eso cada paso
   lleva su stop escrito.

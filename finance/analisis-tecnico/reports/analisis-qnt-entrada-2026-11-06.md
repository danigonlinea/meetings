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

## 7. El mapa de octubre: dónde estaba la compra (y por qué no hubo 6x)

**Primero la corrección de dato:** en octubre QNT **no hizo un 6x**. El 6x fue **septiembre** (mínimo 58,75
→ máximo 373,00 = 6,3x). Octubre fue el mes contrario: abrió en **287,00**, hizo máximo en **307,00** el día
1 y cayó hasta **173,56** el 24 (−40 %), cerrando el mes en **201,11**.

### Día a día, con las señales

| Fecha | Cierre | Señal | Volumen |
|---|--:|---|--:|
| 07/10 | 253,40 | **giro de parabólica a bajista** en 373,00 (fin del tramo de septiembre) | 0,6× |
| 24/10 | 179,26 | mínimo del mes en **173,56** | 0,4× (sin capitulación) |
| 25/10 | 190,21 | **vela de entrada**: mínimo 177,92 > 173,56 y cierre positivo | 0,7× |
| 26/10 | 204,01 | **triple confluencia**: giro de parabólica a alcista (173,56), cierre sobre EMA9 (195,10) y EMA20 (199,10), vela de entrada y **1,8× de volumen** | **1,8×** |
| 27/10 | 199,39 | rechazo en **213,00**: primera salida | 1,0× |
| 30/10 | 192,27 | **giro de parabólica a bajista** en 223,96 (segunda salida) | 1,0× |

### Las tres formas de comprar, con su resultado

| Entrada | Precio | Stop | Riesgo | Objetivo | Recorrido | R/R |
|---|--:|--:|--:|--:|--:|--:|
| **A. El cierre del día de la señal** | 204,01 | 187,79 (mínimo del día) | 7,9 % | 213,00 | +4,4 % | **0,55** ❌ |
| **B. El mínimo superior del 25/10** | 190,21 | 173,50 (bajo el mínimo del mes) | 8,8 % | 223,96 | +17,7 % | **2,0** ✅ |
| C. Aguantar hasta el giro bajista del 30/10 | 204,01 | trailing en la parabólica | — | — | **−5,8 %** | ❌ |

**La respuesta a tu pregunta:** la compra de octubre fue la **B**, el 25 de octubre en **190,21**, con el
mínimo superior al del día anterior — **un día antes** de que la parabólica confi rmara. El día de la señal
completa (26/10) ya se compraba un 7 % más arriba y el recorrido hasta el primer rechazo era menor que el
riesgo. **La señal llega tarde; el mínimo superior llega a tiempo.**

**Y el límite honesto:** aguantar la posición hasta que la parabólica volvió a girar (30/10) daba **−5,8 %**.
En octubre el dinero estaba en **operar el rango 173-224**, no en mantener: comprar el mínimo superior, vender
el rechazo. Quien compró y aguantó sigue hoy prácticamente en el precio de compra (190,95).

### Lo que octubre sí dejó escrito para la próxima

1. **El mínimo del mes se hizo sin volumen** (0,4×): el suelo no avisó. El aviso llegó al día siguiente, con
   la vela de entrada y el 1,8× del 26/10.
2. **La confluencia del 26/10 fue de manual** (parabólica + EMA9 + EMA20 + volumen + mínimo superior) y aun
   así el recorrido hasta el rechazo fue corto: la calidad de la señal no arregla un mal precio de entrada.
3. **En rango, el objetivo es el borde contrario** (213-224), no el máximo histórico. Perseguir el 6x en
   octubre era comprar la continuación de un movimiento que ya había terminado el 7/10.

## 6. ¿Se podía anticipar la vela gigante? Sí, el 18-22 de septiembre

La vela mensual de septiembre **no existió como tal hasta el 24-27**: el día 18 el precio estaba en 63,28 y
el día 30 cerró en 287,15. Lo que sí existía, día a día, era esto:

| Fecha | Cierre | % del día | Volumen | × media (10.769 QNT) |
|---|--:|--:|--:|--:|
| 18/09 | 63,28 | +3,4 % | 22.120 | **2,1×** |
| 21/09 | 66,87 | +4,2 % | 25.585 | **2,4×** |
| 22/09 | 73,85 | +10,4 % | 45.386 | **4,2×** ← rompe el techo del rango 55-68 |
| 24/09 | 90,10 | +27,6 % | 53.387 | 5,0× |
| 25/09 | 98,64 | +9,5 % | 148.391 | 13,8× |
| 26/09 | 151,52 | +53,6 % | 236.043 | 21,9× |
| 27/09 | 286,26 | +88,9 % | 1.013.907 | **94,2×** |

**El volumen fue la señal anterior al precio.** Entre junio y el 15 de septiembre el volumen medio era de
10.769 QNT al día; el 22/09 se multiplicó por 4 y el 27/09 por 94. Quien miraba volumen relativo a su propia
media tenía el aviso **cinco días antes** de que la vela mensual fuese gigante.

### La vela de entrada, probada

La regla que planteas —**mínimo superior al anterior + vela positiva**— con un filtro de volumen (>1,5× la
media de 20 días), medida sobre **964 días** de QNT:

| | Casos | Retorno 10 d medio | Mediana | Casos > +10 % en 10 d | Recorrido máximo medio |
|---|--:|--:|--:|--:|--:|
| **Con señal** | 56 | **+17,9 %** | −1,0 % | **21,4 %** | **+43,3 %** |
| Todos los días | 964 | +2,5 % | −1,8 % | 14,6 % | +14,3 % |

- **La señal habría disparado el 18/09 y el 21/09**, con retorno a 10 días de **+264 %** y **+267 %**. La
  respuesta a tu pregunta es sí: ese momento era identificable.
- **Pero la mediana es −1 %:** la mitad de las señales no dan nada. El resultado medio lo cargan dos o tres
  casos enormes. Es una señal de **cola gorda**, no de acierto frecuente: se gana dejando correr el ganador
  (recorrido máximo +43 % de media frente a +14 % de base) y cortando el resto con stop.
- **Tamaño de muestra:** 1000 velas diarias (QNT cotiza en Binance desde 2023). Suficiente para ver la
  asimetría, corto para afirmar una tasa.

### Dónde estaba la entrada, en la práctica

- **22/09:** ruptura del techo del rango (68,62) con 4,2× de volumen y cierre en 73,85. Stop bajo el mínimo
  de la vela anterior (**65,86**): riesgo 10,8 %. Desde ahí, trailing con la EMA9 o la parabólica.
- **Lo que no se debe hacer:** esperar al cierre de la vela semanal (286,26) o mensual (287,15). Ahí ya se
  había recorrido el 90 % del movimiento y el riesgo estaba en máximos.

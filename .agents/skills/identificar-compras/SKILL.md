---
name: identificar-compras
description: Usar cuando haya que decidir si un activo (cripto o acción) está en momento de compra y con qué niveles, bajando de mensual a semanal, diaria y 4 horas. Define el embudo, la vela de entrada, la confluencia, el R/R mínimo y las prohibiciones, con los umbrales medidos.
---

# Identificar momentos de compra (multi-temporal)

Cripto o acciones, con velas de **mensual, semanal, diaria y 4 horas**. La regla que ordena todo:

> **La EMA200 diaria y la vela de entrada deciden SI. La semanal dice DÓNDE. La mensual solo da contexto.
> La de 4 horas dice CUÁNDO, y es la que fija el stop pequeño.**

Nunca se invierte ese orden y nunca se compra mirando una sola temporalidad. El caso que lo demuestra:
QNT en septiembre de 2026 hizo un 6x (58,75 → 373) y quien compró «porque la mensual era alcista» al cierre
pagó 287 y perdió un 40 % en tres semanas.

## Cuándo se usa

- «¿Está en buen punto de compra?» / «búscame la entrada» / «¿dónde compro?».
- Antes de abrir cualquier posición, también si la idea viene de una recomendación externa.
- **No** se usa para decidir cuánto comprar (eso es gestión de cuenta) ni para predecir el precio.

## Paso 0 — datos (3 minutos)

```bash
# backtest de la regla sobre 10 pares (¿sigue funcionando hoy?)
python3 .agents/skills/identificar-compras/scripts/backtest_entradas.py --rr 2

# puntuación de confluencia día a día (¿cuándo exactamente?)
python3 .agents/skills/identificar-compras/scripts/puntuacion_confluencia.py QNTUSDT --desde 2026-10-01 --hasta 2026-10-30

# un activo, tres temporalidades + %B y posición en la vela
python3 .agents/skills/analisis-tecnico/scripts/informe_activo.py HBAR-USD

# varios pares /USDT de golpe (Binance y, si no existe, MEXC)
python3 .agents/skills/analisis-tecnico/scripts/informe_batch.py HYPEUSDT QNTUSDT
```

Fuentes: klines de Binance (`/api/v3/klines`, gratis, sin clave), MEXC (`/api.mexc.com/api/v3/klines`,
mismo formato) y Yahoo (`query2.finance.yahoo.com/v8/finance/chart`, sin crumb) para acciones y ETF.
**Comprueba la longitud de la serie antes de opinar:** sin 20 velas mensuales no hay EMA20 mensual, y sin
200 diarias no hay EMA200.

## Paso 1 — Contexto (mensual): no es filtro de entrada

| Qué se mira | Regla |
|---|---|
| Precio vs **EMA20 mensual** | por encima → solo largos. Por debajo → no se compra, se espera |
| Orden de medias | `EMA3 > EMA9 > EMA20 > EMA50` = tendencia sana. Al revés = no comprar |
| Parabólica mensual | bajista ≠ prohibición, pero quita urgencia: la media manda |
| Niveles del mes | máximo, mínimo y cierre del mes anterior: son los niveles grandes del año |

**La mensual es CONTEXTO, no filtro.** El backtest (284 operaciones, 10 pares, ver
`reports/revision-adversarial-entradas.md`) demuestra que el sesgo mensual **resta** esperanza (+0,01R
frente a +0,11R sin él): deja fuera las mejores entradas. Sirve para saber si se puede operar en corto y
para situar los niveles grandes, nada más. **El filtro que sí funciona es la EMA200 diaria** (Paso 3).

## Paso 2 — Zona (semanal): aquí está la caja

- Dibuja la **caja** con los 3-5 últimos máximos y mínimos semanales. Si los máximos bajan y los mínimos
  suben, es una **caja que se cierra**: no se compra el centro, se compra el borde.
- **No se compra en mitad del rango.** En el centro no hay ni suelo ni techo: no hay stop lógico.
- El **borde inferior de la caja es la zona de compra**; el borde superior es el **primer objetivo**.
- Si la semana pasada cerró por encima del máximo de la caja con volumen, deja de ser rango y pasa a ser
  tendencia: entonces el objetivo es la proyección del alto de la caja, no el borde.

Ejemplo (QNT, oct-2026): caja **175-211**; comprar en 175-186, primer objetivo 211.

## Paso 3 — Confirmación (diaria): un solo filtro que funciona

**Filtro obligatorio: precio por encima de la EMA200 diaria.** Es el único que mejora la esperanza medida
(41,2 % de acierto y **+0,18R** con él, frente a 38,3 % y +0,11R sin él). Debajo de la EMA200 no se compra:
se está operando un rebote.

**Las tres condiciones de confluencia** (cierre sobre EMA9 y EMA20, parabólica girada a alcista, nivel de
caja o histórico) siguen siendo útiles, pero **para añadir tamaño, no para entrar**: como filtro de entrada
bajan la esperanza de +0,11R a +0,06R porque llegan tarde. Regla: la entrada la da la vela de entrada; la
confluencia decide cuánto se carga en la segunda tanda.

## Paso 3 bis — Puntuación de confluencia (el marcador de 8)

Cuando la pregunta es «¿cuándo exactamente?», se puntúa cada día con ocho casillas y se busca el día en que
se encienden todas. Script: `scripts/puntuacion_confluencia.py`.

| # | Condición |
|--:|---|
| 1 | Precio > **EMA200** diaria |
| 2 | Precio > **EMA20** diaria |
| 3 | Precio > **EMA50** diaria |
| 4 | **EMA3 > EMA9** diaria |
| 5 | **Parabólica** diaria alcista |
| 6 | **Vela de entrada** (mínimo > anterior y cierre > apertura) |
| 7 | **Volumen > 1,5×** la media de 20 |
| 8 | **4 h alineada**: ≥80 % de las barras del día sobre su EMA20 y con SAR alcista |

**Cómo se lee el marcador:**

| Score | Lectura |
|---|---|
| **8/8** | momento certificado: es el día de la compra |
| 7/8 | zona de compra; se espera a que cierre la casilla que falta |
| 5-6/8 | vigilancia. No se compra |
| ≤4/8 | no hay nada que hacer |

**Dos reglas que valen más que el score:**

1. **La de 4 h sola es ruido.** El 21/10/2026 en QNT tenía la de 4 h al 100 % (6 de 6 barras) y el día
   siguiente el precio perdió la EMA9 y cayó un 9 %. Le faltaban la EMA20 diaria, la parabólica y el
   volumen: **4/8**. Sin la diaria completa, la de 4 h no habilita nada.
2. **Distancia a la EMA20: es un aviso, no un veto.** Medido sobre 284 operaciones, comprar a más del 25 %
   sobre la EMA20 da +0,18R, igual que comprar pegado a ella (+0,21R). Sirve para **reducir tamaño**, no para
   descartar. (El 1-6 de octubre QNT puntuaba 6/8 con el precio +63 % sobre su EMA20: eso era la cola de la
   subida de septiembre, pero el 8/8 del 26 de octubre también estaba en una subida fuerte y funcionó.)

**Caso resuelto (QNT, octubre de 2026):** 30 días, un solo 8/8 —el **26/10**, cierre 204,01, con EMA3
cruzando sobre EMA9 por 32 centavos, parabólica girando en 173,56, volumen 1,8× y las 6 barras de 4 h
alineadas—. El segundo mejor día del mes fue 5/8. Detalle: `reports/analisis-qnt-octubre-2026-11-06.md`.

**Capa de permiso (semanal):** si la semanal mantiene `EMA3 > EMA9 > EMA20 > EMA50` con parabólica alcista,
la corrección en diaria es **zona de compra**; si la semanal ya está girada, no hay compra aunque el día
puntee 8/8, porque se está comprando contra la tendencia mayor.

## Paso 4 — Gatillo (4 horas): el precio de la entrada

La temporalidad de 4 h es la que permite **stop pequeño**:

- **Disparador:** giro de la parabólica de 4 h a alcista **y** cierre por encima de EMA9 y EMA20 de 4 h.
- **Entrada:** en el cierre de esa vela o, mejor, en el **retroceso** al nivel (EMA9 de 4 h o apertura de la
  vela del giro).
- **Stop:** bajo el mínimo de la vela del giro, o bajo el mínimo de la caja si es más ajustado.
- Si el stop queda a más del **10 %** del precio, la entrada no es de 4 h: baja a 1 h o espera el retroceso.

## Paso 5 — La vela de entrada: el aviso llega un día antes

**Definición:** vela con **mínimo superior al de la vela anterior** y **cierre positivo** (cierre > apertura),
con **volumen > 1,5 × la media de 20 velas**, y **siempre con el precio sobre la EMA200 diaria**.

**La vertical NO se prohíbe (corrección medida).** Durante un tiempo esta skill decía «no comprar si el
precio está a más de 2×ATR o un 25 % sobre la EMA20». El backtest de 284 operaciones no lo respalda:

| Distancia a la EMA20 | n | Acierto | R medio |
|---|--:|--:|--:|
| ≤ 10 % | 95 | 43,2 % | +0,21 |
| 10-25 % | 138 | 39,9 % | +0,17 |
| **> 25 %** | **51** | **41,2 %** | **+0,18** |

Y por subida en 30 velas: 0-25 % → +0,24R · 25-50 % → +0,25R · **50-100 % → −0,31R (n=29)** · >100 % → +0,24R.
El único tramo malo es el intermedio (n=29, muestra corta). Conclusión operativa: **la vertical no descarta la
compra; el tramo 50-100 % de subida en un mes sí obliga a reducir tamaño**. El caso QNT de septiembre era una
anécdota, no una ley: con la prohibición puesta se habría perdido también la subida de HBAR en noviembre de
2024 (0,090 → 0,392, +335 %).

Medido sobre 964 días de QNT/USDT (Binance, 2023-2026):

| | Casos | Retorno 10 d medio | Mediana | Casos > +10 % en 10 d | Recorrido máximo medio |
|---|--:|--:|--:|--:|--:|
| **Con señal + volumen** | 56 | **+17,9 %** | −1,0 % | **21,4 %** | **+43,3 %** |
| Todos los días | 964 | +2,5 % | −1,8 % | 14,6 % | +14,3 % |

**Cómo se interpreta, sin engañarse:**
- Es una señal de **cola gorda**: la mitad de las veces no pasa nada (mediana −1 %). El resultado lo cargan
  dos o tres casos enormes.
- Por eso **exige stop y dejar correr**: el dinero está en el recorrido máximo (+43 % frente a +14 %), no en
  acertar muchas veces.
- **Llega antes que la parabólica.** En QNT la vela de entrada fue el **25/10** (cierre 190,21) y el giro de
  parabólica el 26/10 (cierre 204,01): comprar en la confirmación pagaba un 7 % más y el recorrido hasta el
  primer rechazo (213) era menor que el riesgo. Regla: **si la vela de entrada aparece en el borde de la
  caja, se compra ahí; la confirmación sirve para añadir, no para entrar.**

## Paso 6 — Tamaño, stop y objetivos (la parte que decide)

| Elemento | Regla |
|---|---|
| **R/R mínimo** | **2:1**. Si el objetivo del borde de la caja no da 2× el riesgo, no se opera |
| **Stop** | bajo el mínimo de la vela de entrada o de la caja. Nunca «un 5 %» arbitrario |
| **Entrada escalonada** | 1/3 en la vela de entrada, 1/3 en el cierre de confirmación diaria, 1/3 en la ruptura del techo de la caja |
| **Salida 1** | el **rechazo del borde superior** de la caja (vender el rechazo, no la figura) |
| **Salida 2** | giro de la parabólica de 4 h a bajista, con trailing |
| **Invalidación** | cierre diario bajo el mínimo de la caja: se sale entero, sin promediar |

Ejemplo numérico del caso QNT (25/10/2026): entrada **190,21**, stop **173,50** (riesgo 8,8 %), objetivo
**223,96** (recorrido 17,7 %), **R/R 2,0**. La misma señal comprada en la confirmación (204,01) daba R/R
**0,55**: se descarta.

## Paso 7 — Las siete prohibiciones

1. **Comprar el cierre de una vela gigante** (mensual o semanal). En QNT costó −40 %.
2. **Comprar en el centro del rango**: sin stop lógico no hay operación.
3. **Comprar con el precio bajo la EMA20 mensual**: eso es un rebote, no una tendencia.
4. **Comprar solo con la parabólica**: dos flips falsos en diez días en QNT.
5. **Comprar sin volumen**: el mínimo de octubre se hizo con 0,4× de volumen y no avisó de nada.
6. **Promediar a la baja** cuando el precio cierra bajo el mínimo de la caja.
7. **Comprar porque «ya ha caído mucho»**: un −90 % puede ser un −95 %.

## Vigencia: el método se comprueba antes de usarlo

La ventaja **no es estable en el tiempo** y hay que mirarla antes de fiarse:

| Periodo | n (V5) | Acierto | R medio |
|---|--:|--:|--:|
| Histórico completo (2,7 años) | 284 | 41,2 % | **+0,18** |
| Últimos 12 meses | 64 | 32,8 % | **−0,03** |
| Últimos 6 meses | 58 | 34,5 % | **+0,01** |

Leído sin adornos: **en el último año el método no tiene ventaja medible**. Puede ser muestra corta (64
operaciones), pero mientras no se demuestre lo contrario se usa como **filtro de calidad** (evita comprar
contra tendencia), no como generador de esperanza. Comprobación obligatoria antes de operar:

```bash
python3 scripts/backtest_entradas.py --rr 2 --desde 2025-11-06
```

## Backtest: qué versión aguanta (10 pares, 1.000 velas diarias, 2R)

| Versión | n | Acierto | R medio |
|---|--:|--:|--:|
| Control (cualquier día) | 3.176 | 27,7 % | −0,18 |
| Vela de entrada + volumen | 535 | 38,3 % | +0,11 |
| + sesgo mensual | 319 | 35,1 % | +0,01 |
| + triple confirmación diaria | 274 | 36,9 % | +0,06 |
| **+ EMA200 diaria** | **284** | **41,2 %** | **+0,18** |

Con 1R: +0,03R · con 2R: +0,18R · con 3R: +0,21R → **objetivo 2R por defecto**. Riesgo medio de la vela de
entrada: **7,3 %**, así que con 1 % de riesgo de cuenta el tamaño sería el 13,7 % del capital: hay que
caparlo o bajar a 4 h. Reproducible: `python3 scripts/backtest_entradas.py --rr 2`.

## Metarregla

**Toda regla de esta skill lleva su `n`.** Si una regla no tiene muestra detrás (o la muestra es menor de 30
operaciones), se escribe como **hipótesis**, no como prohibición. Las que hoy son hipótesis: el corte en 7/8
para precompras, el tramo 50-100 % de subida mensual y la capa semanal de permiso.

## Lo que está medido y lo que no

- **Medido y a favor:** la vela de entrada con volumen **filtrada por EMA200** (tabla de arriba); los niveles
  del método se aciertan con precisión de céntimos en intradía (16 de 19 comprobados en `predicciones.md`).
- **Medido y en contra:** «la anomalía se cierra siempre» es una tautología (el precio vuelve al nivel del
  cruce el 93-99 % de las veces… igual que a cualquier nivel); «la primera vela decide la dirección» no
  predice nada al quitar el solape (51-55 %). Ver `revision-adversarial.md`.
- **No medido:** la tasa de acierto de la confluencia completa a 4 h. No hay serie pública de sus operaciones.

## Salida (qué entregar al usuario)

Un informe corto con: **(1)** tabla de las cuatro temporalidades (orden de medias, parabólica, %B, distancia
a EMA20); **(2)** la caja y sus dos bordes; **(3)** el veredicto en una línea —compra / espera / no—;
**(4)** el **marcador de 8** del día en curso (y del día anterior, para ver el cambio); **(5)** la tabla de
disparadores con nivel, condición y estado; **(6)** stop, objetivos y R/R; **(7)** los avisos de datos
(serie corta, mínimos contaminados por el listado, exchange distinto).

**Si la pregunta es «¿cuándo debería haber comprado?»** (un mes pasado, una caída concreta), la entrega es
la tabla día a día del §Paso 3 bis con el score, los dos mejores días y las trampas descartadas con su
motivo numérico. Ejemplo exacto: `reports/analisis-qnt-octubre-2026-11-06.md`.
Modelo: `finance/analisis-tecnico/reports/analisis-qnt-entrada-2026-11-06.md`.

## Pitfalls

- **Series cortas:** por debajo de 20 velas mensuales no hay EMA20 mensual. Se dice, no se inventa.
- **Mínimos contaminados:** en tokens nuevos el «mínimo de 52 semanas» es la primera hora de cotización
  (BTW 0,002; RAIN 0,0001). No sirve como referencia.
- **Exchange:** cinco de los diez pares del informe de noviembre no estaban en Binance y se leyeron en MEXC.
  Precio y volumen pueden diferir del exchange donde se opere.
- **Fechas en UTC:** las velas de Binance cierran en UTC; la diaria «de hoy» está abierta. No se da por
  cerrada una vela que no lo está.
- **La mensual en curso miente:** un mes a medias es un doji que puede acabar en cualquier sitio. Solo cuenta
  la vela cerrada.
- **No se convierte esto en una certeza.** El propio método acierta niveles y falla escenarios: cada entrada
  va con su stop escrito o no es una entrada.

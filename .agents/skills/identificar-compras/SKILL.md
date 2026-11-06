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

**Prohibición de comprar vertical:** si el precio está a más de **2×ATR** por encima de la EMA20 diaria, la
vela de entrada no se opera. Los dos −1R de QNT (29 y 30/09/2026, con volumen de 3,9× y 3,5×) vienen
exactamente de ahí: en una subida vertical el volumen alto es distribución, no acumulación.

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
**(4)** la tabla de disparadores con nivel, condición y estado; **(5)** stop, objetivos y R/R; **(6)** los
avisos de datos (serie corta, mínimos contaminados por el listado, exchange distinto).
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

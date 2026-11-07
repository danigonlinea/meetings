---
name: identificar-compras
description: Usar cuando haya que decidir si un activo (cripto o acción) está en momento de compra y con qué niveles, bajando de mensual a semanal, diaria y 4 horas. Un gate medido decide la entrada; el marcador de 8 y el resto de capas ordenan tamaño. Cada regla lleva su n.
---

# Identificar momentos de compra (multi-temporal)

Cripto o acciones, con velas de **mensual, semanal, diaria y 4 horas**. La regla que ordena todo:

> **La EMA200 diaria y la vela de entrada deciden SI. La semanal dice DÓNDE y cuánto. La mensual solo
> da contexto. La de 4 horas dice CUÁNDO y ajusta el stop.**

Nunca se invierte ese orden y nunca se compra mirando una sola temporalidad. El caso que lo demuestra:
QNT en septiembre de 2026 hizo un 6x (58,75 → 373) y quien compró «porque la mensual era alcista» al
cierre pagó 287 y perdió un 40 % en tres semanas.

## Cuándo se usa

- «¿Está en buen punto de compra?» / «búscame la entrada» / «¿dónde compro?».
- Antes de abrir cualquier posición, también si la idea viene de una recomendación externa.
- **No** se usa para decidir cuánto comprar (eso es gestión de cuenta) ni para predecir el precio.
- **No hace cálculos de ventaja.** Ni backtests, ni barridos de pares, ni comparaciones: eso es
  `medir-metodo-compras` y solo corre a petición del dueño. Aquí se leen indicadores y se decide la entrada.

## Paso 0 — datos (3 minutos)

**Se calcula solo lo del activo que se pregunta.** No hay barridos, ni backtests, ni comparaciones de pares
en esta skill: la ventaja de la regla se mide aparte, en `medir-metodo-compras`, y **solo si el dueño lo pide**.

```bash
# un activo, tres temporalidades + %B y posición en la vela
python3 .agents/skills/analisis-tecnico/scripts/informe_activo.py HBAR-USD

# marcador día a día del activo preguntado (¿cuándo exactamente?) — Binance y, si el par no está, MEXC
python3 .agents/skills/identificar-compras/scripts/puntuacion_confluencia.py QNTUSDT --desde 2026-10-01 --hasta 2026-10-30

# varios pares /USDT de golpe, solo si pide varios de golpe
python3 .agents/skills/analisis-tecnico/scripts/informe_batch.py HYPEUSDT QNTUSDT
```

**Los indicadores se leen, no se remiden.** Las cifras de esta skill (n, R medio) son referencia histórica:
repetirlas cuesta minutos y no cambia la decisión del día.

**Comprueba la longitud de la serie antes de opinar.** El marcador pide **50 velas mensuales** (la tabla
del Paso 1 usa la EMA50 mensual; con 20 solo hay EMA20), **200 velas diarias** para la EMA200 y **200 más
de calentamiento** para que la EMA200 no arrastre el seed: el script omite los días que no lo cumplen y lo
dice al pie. Menos serie = no hay indicador, no se estima.

## Paso 1 — Contexto (mensual): no filtra nada

| Qué se mira | Para qué sirve |
|---|---|
| Precio vs **EMA20 mensual** | situar la tendencia mayor y los niveles grandes; **no** veta la compra |
| Orden de medias `EMA3 > EMA9 > EMA20 > EMA50` | saber si el ciclo está sano o girado: contexto de tamaño |
| Parabólica mensual | bajista quita urgencia, no prohíbe |
| Niveles del mes | máximo, mínimo y cierre del mes anterior: son los niveles grandes del año |

**La mensual es CONTEXTO y está medido que no discrimina.** Con el sesgo mensual bien calculado (mes
**cerrado**, no el mes en curso):

| Grupo | n | Acierto | R medio |
|---|--:|--:|--:|
| Vela + volumen (V2) | 781 | 40,7 % | +0,18 |
| V2 **+ sesgo mensual** | 463 | 39,7 % | +0,14 |

La diferencia (+0,04R) está dentro del ruido: no suma, no hunde. Y comprar **bajo** la EMA20 mensual, que
antes era prohibición, ha rendido **mejor** que comprar por encima:

| V5 con el precio… | n | Acierto | R medio |
|---|--:|--:|--:|
| sobre la EMA20 mensual | 423 | 41,4 % | +0,19 |
| **bajo la EMA20 mensual** | **90** | **46,7 %** | **+0,39** |

Por eso la mensual no veta nada. **El filtro que sí funciona es la EMA200 diaria** (Paso 3).

## Paso 2 — Zona (semanal): aquí está la caja

Técnica estructural, **sin medición detrás** (va como método, no como regla medida):

- Dibuja la **caja** con los 3-5 últimos máximos y mínimos semanales. Si los máximos bajan y los mínimos
  suben, es una **caja que se cierra**: no se compra el centro, se compra el borde.
- **No se compra en mitad del rango.** En el centro no hay ni suelo ni techo: no hay stop lógico.
- El **borde inferior de la caja es la zona de compra**; el borde superior es el **primer objetivo**.
- Si la semana pasada cerró por encima del máximo de la caja con volumen, deja de ser rango y pasa a ser
  tendencia: entonces el objetivo es la proyección del alto de la caja, no el borde.

Ejemplo (QNT, oct-2026): caja **175-211**; comprar en 175-186, primer objetivo 211.

## Paso 3 — Confirmación (diaria): el gate medido

**La entrada la decide una sola cosa: precio sobre la EMA200 diaria + vela de entrada + volumen.** Es lo
único de esta skill con ventaja medida:

| Regla | n | Episodios | Acierto | R medio |
|---|--:|--:|--:|--:|
| Cualquier día (control) | 3.926 | 570 | 29,1 % | −0,14 |
| Vela de entrada + volumen (V2) | 781 | 271 | 40,7 % | +0,18 |
| **V2 + EMA200 diaria (V5, la regla)** | **513** | **165** | **42,3 %** | **+0,22** |

**`Episodios` es el n honesto:** las señales se solapan (dos entradas a menos de 20 velas comparten
horizonte), así que 513 operaciones son 165 rachas independientes. Cita las dos cifras.

- Bootstrap por bloques de 10 sobre V5: **IC95 del R medio [+0,02, +0,44]**, P(R ≤ 0) = 1,6 %. Significativo,
  pero por los pelos: no es un +0,22 sólido, es un +0,22 con el cero a un paso.
- **Con costes** (comisión + deslizamiento ida y vuelta): a 0,2 % queda +0,18R; a 0,5 %, +0,12R. El edge
  aguanta, pero un tercio se lo come la fricción.
- **La vela sin volumen no vale nada:** misma vela, sobre EMA200, sin el filtro de volumen = **−0,03R**
  (n=997). El volumen no es adorno.

Debajo de la EMA200 no se compra: se está operando un rebote.

**Las tres condiciones de confluencia** (cierre sobre EMA9 y EMA20, parabólica girada a alcista, nivel de
caja o histórico) **no son filtro de entrada**: llegan tarde. Son criterio de **tamaño** (segunda tanda).

## Paso 3 bis — El marcador de 8 no es un permiso de entrada

El marcador ordena la **calidad del día** y el **tamaño**. No autoriza ni veta: la entrada la da el Paso 3 /
Paso 5. Script: `scripts/puntuacion_confluencia.py`.

| # | Condición |
|--:|---|
| 1 | Precio > **EMA200** diaria |
| 2 | Precio > **EMA20** diaria |
| 3 | Precio > **EMA50** diaria |
| 4 | **EMA3 > EMA9** diaria |
| 5 | **Parabólica** diaria alcista |
| 6 | **Vela de entrada** (mínimo > anterior y cierre > apertura) |
| 7 | **Volumen > 1,5×** la media de las **20 velas anteriores** |
| 8 | **4 h alineada**: ≥80 % de las barras del día sobre su EMA20 y con SAR alcista. Solo se puntúa si el día ha cerrado: en curso sale `?` y **no cuenta** |

**Cómo se lee:**

| Score | Lectura |
|---|---|
| **8/8** | día completo: entrada del gate **y** segunda tanda completa |
| **7/8 con la 4 h como única casilla vacía** | mismo caso que 8/8 dentro de la sesión (hipótesis, n=9 fuera de muestra) |
| 5-7/8 | día parcial: la entrada del gate vale igual si la vela de entrada está en el borde; se carga menos |
| ≤4/8 | el día no aporta calidad; **no veta** la entrada del gate (ver el caso QNT de abajo) |

**El caso que zanja la discusión (QNT, octubre de 2026):** el único 8/8 del mes fue el **26/10**, cierre
204,01. Pero la vela de entrada fue el **25/10** (cierre 190,21) y ese día puntuaba **3/8**. Comprar en el
8/8 daba R/R **0,55**; comprar en el 3/8 daba **2,0**. La entrada buena la dio el gate; el marcador llegó un
día tarde. Detalle: `reports/analisis-qnt-octubre-2026-11-06.md`.

**Al listar días de compra NUNCA se filtra por distancia a la EMA20.** El marcador no la incluye y filtrarla
borra los rallies: en HBAR 2024-2025 el corte del 25 % eliminó 8 de 21 días con 8/8, casi todos en la subida
de noviembre-enero. Medido sobre V5 (n=513):

| Distancia a la EMA20 diaria | n | Acierto | R medio |
|---|--:|--:|--:|
| ≤ 10 % | 174 | 42,0 % | +0,21 |
| 10-25 % | 258 | 40,7 % | +0,20 |
| **> 25 %** | **67** | **47,8 %** | **+0,36** |

Es un **aviso de tamaño**, no un veto. Igual con la subida en las 30 velas previas: **ningún tramo es
negativo** (0-25 %: +0,18 · 25-50 %: +0,31 · 50-100 %: +0,15 · >100 %: +0,33), así que la vertical no
descarta la compra. El tramo 50-100 % es el más flojo, pero con n=58 no se sostiene como regla.

**La de 4 h sola es ruido.** El 21/10/2026 en QNT tenía la de 4 h al 100 % (6 de 6 barras) y el día siguiente
el precio perdió la EMA9 y cayó un 9 %. Le faltaban la EMA20 diaria, la parabólica y el volumen: **4/8**. Sin
la diaria completa, la de 4 h no habilita nada.

**La semanal NO es un permiso.** (Corregido.) La columna `perm` del script muestra si la última semana
cerrada mantiene `EMA3 > EMA9 > EMA20 > EMA50` con parabólica alcista, pero medido no discrimina:

| V5 con la semanal… | n | Acierto | R medio |
|---|--:|--:|--:|
| alineada | 186 | 40,3 % | +0,17 |
| **girada** | **327** | **43,4 %** | **+0,26** |

Y la semanal estaba **girada** el 15/11/2024 en HBAR, el caso que esta misma skill usa como prueba del 7/8
(0,072 → +442 % en 60 velas). Un veto semanal habría matado la mejor entrada del libro. Se usa para tamaño y
para leer la caja, no para vetar.

**Orden de las señales dentro de un movimiento** (hipótesis, medida en un solo par): la primera y la segunda
son las buenas (HBAR: 15/11 a 0,072 y 16/11 a 0,090); de la tercera en adelante se compra continuación y el
tamaño baja a la mitad.

## Paso 4 — Gatillo (4 horas): el precio de la entrada

**No medido.** Esto afina la ejecución; los R de esta skill están medidos con entrada al cierre diario y
stop en el mínimo de la vela diaria, no con este gatillo.

- **Disparador:** giro de la parabólica de 4 h a alcista **y** cierre por encima de EMA9 y EMA20 de 4 h.
- **Entrada:** en el cierre de esa vela o, mejor, en el **retroceso** al nivel (EMA9 de 4 h o apertura de la
  vela del giro).
- **Stop:** bajo el mínimo de la vela del giro, o bajo el mínimo de la caja si es más ajustado.
- Si el stop queda a más del **10 %** del precio, la entrada no es de 4 h: baja a 1 h o espera el retroceso.

## Paso 5 — La vela de entrada: el aviso llega un día antes

**Definición:** vela con **mínimo superior al de la vela anterior**, **cierre positivo** (cierre > apertura) y
**volumen > 1,5 × la media de las 20 velas anteriores** (sin contar la propia vela), **siempre con el precio
sobre la EMA200 diaria**. Es el gate del Paso 3 con nombre propio.

**Llega antes que la parabólica.** En QNT la vela de entrada fue el **25/10** (cierre 190,21) y el giro de
parabólica el 26/10 (cierre 204,01): comprar en la confirmación pagaba un 7 % más y el recorrido hasta el
primer rechazo (213) era menor que el riesgo. Regla: **si la vela de entrada aparece en el borde de la caja,
se compra ahí; la confirmación sirve para añadir, no para entrar.**

Estudio de un solo par (QNT/USDT, 964 días; **no lo reproduce ningún script de la skill**, va como
indicativo): con señal + volumen, retorno medio a 10 días **+17,9 %** (mediana −1,0 %, 21,4 % de casos por
encima de +10 %) frente a +2,5 % de todos los días; recorrido máximo medio +43,3 % frente a +14,3 %.

**Cómo se interpreta, sin engañarse:** es una señal de **cola gorda**. La mitad de las veces no pasa nada
(mediana negativa, también en V5: 1R acierta el 54 %, 2R el 42 %, 3R el 37 %). El resultado lo cargan dos o
tres casos enormes, así que **exige stop y dejar correr**: el dinero está en el recorrido, no en acertar mucho.

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

Con el stop en el mínimo de la vela diaria, el riesgo medio es **6,9 %** del precio: con 1 % de riesgo de
cuenta el tamaño sería el 14,5 % del capital, así que hay que caparlo o bajar a 4 h.

## Paso 7 — Las siete prohibiciones

1. **Comprar bajo la EMA200 diaria** (medido: es el único filtro que separa +0,18R de +0,22R; debajo se opera
   un rebote).
2. **Comprar sin volumen**: la misma vela sin el filtro de 1,5× da **−0,03R** (n=997).
3. **Comprar en el centro del rango**: sin stop lógico no hay operación.
4. **Comprar solo con la parabólica**: dos flips falsos en diez días en QNT.
5. **Comprar el cierre de una vela gigante sin vela de entrada ni stop**: en QNT costó −40 %. Ojo: esto **no**
   es un veto a la vertical; medido, comprar a más del 25 % sobre la EMA20 rinde igual o mejor. Lo que se
   prohíbe es comprar **sin gate y sin stop**, no comprar caro.
6. **Promediar a la baja** cuando el precio cierra bajo el mínimo de la caja.
7. **Comprar porque «ya ha caído mucho»**: un −90 % puede ser un −95 %.

## La ventaja medida (referencia, no tarea de esta skill)

| Periodo | n (V5) | Episodios | Acierto | R medio |
|---|--:|--:|--:|--:|
| Histórico completo (~3,3 años) | 513 | 165 | 42,3 % | **+0,22** |
| Últimos 12 meses | 65 | 23 | 33,8 % | **−0,00** |
| Control, últimos 12 meses | 1.147 | 170 | 28,2 % | −0,17 |

Ventaja **fina y apagada en el último año**: bate al control, pero no genera esperanza por sí sola. Se usa como
filtro de calidad. **No se recalcula aquí**: el backtest vive en `medir-metodo-compras` y se ejecuta solo si el
dueño lo pide («mídelo», «¿sigue funcionando?»). Esta skill no lo lanza por iniciativa propia.

## Metarregla

**Toda regla de esta skill lleva su `n`.** Si una regla no tiene muestra detrás (o la muestra es menor de 30
operaciones), se escribe como **hipótesis**, no como prohibición. Hipótesis hoy: el corte en 7/8 como compra
válida (n=9), el orden de las señales dentro de un movimiento (n=1 par), el tramo 50-100 % de subida, el
gatillo de 4 h y toda la capa semanal.

## Lo que está medido y lo que no

- **Medido y a favor:** la vela de entrada con volumen filtrada por EMA200 (Paso 3 y tabla del backtest); el
  volumen como filtro imprescindible; el control batido en todas las ventanas.
- **Medido y en contra:** la mensual no discrimina (+0,14 frente a +0,18) y comprar bajo ella rinde más; la
  semanal no discrimina (+0,17 alineada frente a +0,26 girada); la distancia a la EMA20 no veta; la vertical
  no es mala; en el último año la ventaja absoluta es cero. «La anomalía se cierra siempre» es una tautología
  (el precio vuelve al nivel el 93-99 % de las veces… igual que a cualquier nivel) y «la primera vela decide
  la dirección» no predice nada al quitar el solape (51-55 %). Ver `revision-adversarial.md`.
- **No medido:** el gatillo de 4 h, la caja semanal, el R/R que sale del stop de 4 h y el marcador como
  permiso. No se presentan como ventaja.

## Salida (qué entregar al usuario)

Un informe corto con: **(1)** tabla de las cuatro temporalidades (orden de medias, parabólica, %B, distancia
a EMA20); **(2)** la caja y sus dos bordes; **(3)** el veredicto en una línea —compra / espera / no—;
**(4)** el **marcador de 8** del día en curso y del anterior, con las casillas `?` marcadas como incompletas
y el permiso semanal como contexto, no como veto; **(5)** la tabla de disparadores con nivel, condición y
estado; **(6)** stop, objetivos y R/R; **(7)** los avisos de datos (serie corta, mínimos contaminados por el
listado, exchange distinto).

Si la respuesta incluye una cifra de esperanza, va con su **n, sus episodios y el periodo**. Sin eso, es una
opinión.

**Si la pregunta es «¿cuándo debería haber comprado?»** (un mes pasado, una caída concreta), la entrega es la
tabla día a día del §Paso 3 bis con el score, los dos mejores días cerrados y las trampas descartadas con su
motivo numérico. Ejemplo exacto: `reports/analisis-qnt-octubre-2026-11-06.md`. Modelo:
`finance/analisis-tecnico/reports/analisis-qnt-entrada-2026-11-06.md`.

## Pitfalls

- **Series cortas:** sin 50 velas mensuales no hay EMA50 mensual; sin 200 diarias + 200 de calentamiento no
  hay EMA200 fiable. Se dice, no se inventa: el marcador omite esos días y avisa.
- **La vela de hoy no existe todavía:** ni la diaria ni la casilla de 4 h se dan por cerradas. El marcador
  las marca con `?` y no las cuenta.
- **PSAR es implementación propia** (0,02/0,2) sin contrastar con ninguna referencia: si difiere en un giro,
  cambian las casillas 5 y 8, y con ellas el 8/8. Cuando el score esté justo en 7/8 o 8/8, mira la parabólica
  en el gráfico antes de fiarte.
- **Mínimos contaminados:** en tokens nuevos el «mínimo de 52 semanas» es la primera hora de cotización
  (BTW 0,002; RAIN 0,0001). No sirve como referencia.
- **Exchange:** si el par no está en Binance, el marcador cae a MEXC y lo usa en toda la serie. Precio y
  volumen pueden diferir del exchange donde se opere.
- **Fechas en UTC:** las velas de Binance cierran en UTC.
- **La mensual en curso miente:** un mes a medias es un doji. Solo cuenta la vela cerrada, y el sesgo mensual
  del backtest usa el mes anterior cerrado (usar el mes en curso era look-ahead).
- **El marcador no es un permiso.** Un 3/8 con vela de entrada en el borde ha sido la mejor entrada del
  ejemplo QNT; un 8/8 sin R/R no se opera. Y la semanal girada no veta nada.
- **No se convierte esto en una certeza.** Cada entrada va con su stop escrito o no es una entrada.

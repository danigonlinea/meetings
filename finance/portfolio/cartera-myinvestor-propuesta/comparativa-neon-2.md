---
title: "Opción A frente a cartera-ai-neon-2: las dos carteras que sacaron mejor nota, cara a cara"
date: 2026-11-26
type: portfolio-analysis
category: finance
tags: [cartera, analisis, comparativa, opcion-a, cartera-ai-neon-2, opcion-0, myinvestor, 100k, 15-anos, coste, renta-variable, 2022, materias-primas]
status: final
related:
  - finance/portfolio/cartera-myinvestor-propuesta/propuesta-actual.md
  - finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-neon-2/100k.md
  - finance/laboratorio-carteras/cartera-ai-definitiva-final/auditoria-ranking.md
---
# Opción A frente a `cartera-ai-neon-2`

Análisis técnico sobre fichas del repositorio. **No es asesoramiento financiero**: el % de renta variable
y la cartera que se ejecuta son decisiones del titular.

**Qué se compara.** Las dos carteras que mejor nota sacaron en la auditoría forense del 26/11/2026
([`auditoria-ranking.md`](../../laboratorio-carteras/cartera-ai-definitiva-final/auditoria-ranking.md)),
entre las seis evaluadas: la **Opción A** (`8,71 / 10`, #1), hoy propuesta final de la cartera de MyInvestor,
y **`cartera-ai-neon-2`** (`7,81 / 10`, #3, la mejor de las activas). Las dos sobre el mismo mandato:
`100.000 €` libres para invertir + `10.000 €` intocables en `Groupama Trésorerie IC`, 40 años, 15 años vista
(2026 → 2041), traspasos fiscalmente neutros desde `cartera-actual.md`.

**Antes de la tabla, una identidad que conviene tener clara:** `cartera-ai-neon-2/100k.md` y
`option-0.md` son el **mismo diseño**: el segundo nació del primero el 26/11 y solo cambia la cabecera y
las rutas (diff de 128 líneas, ninguna de composición). Todo lo que aquí se dice de `neon-2` vale para
la Opción 0 del ranking.

---

## 1. Cara a cara con las mismas fórmulas (base `100.000 €`)

| Métrica | **Opción A** (propuesta final) | **`cartera-ai-neon-2`** | Δ |
| --- | --: | --: | --: |
| Fondos / gestoras | **7** / 5 | 13 / 10 | A tiene 6 líneas menos |
| Indexado | **`70,0 %`** (`0,109 %`) | `43,0 %` (`0,160 %`) | +27 pp en A |
| RV real (*look-through*) | `81,03 %` | `84,24 %` | −3,2 pp en A |
| TER fijo | **`0,273 %` → `273 €/año`** | `0,784 %` → `784,10 €/año` | **A ahorra `511 €/año`** |
| Drag acumulado 15 años | **`8.432 €`** | `23.720 €` | **`15.288 €` a favor de A** |
| Comisiones de éxito | `0 / 7` | `0 / 13` | empate |
| EE. UU. sobre la RV | `38,7 %` | **`31,1 %`** | −7,6 pp en B |
| Top 10 tecnológicas US s/ total | `9,31 %` (`9.310 €`) | **`4,24 %`** (`4.238 €`) | B lleva menos de la mitad |
| Small & Mid Caps s/ RV | `≈9,4 %` (los `10.000 €` de `GS Small CORE`, que es `94,35 %` SMID) | **`36,78 %`** | B es una cartera SMID |
| Materias primas / activos reales | `0 %` | **`5 %`** (`+14,83 %` en 2022) | solo B |
| **2022 real** | `−8,96 %` (`−8.960 €`) | **`−5,74 %`** (`−5.736 €`) | **B gana `3.224 €`** |
| Acumulado real 2022 → YTD 2026 | **`+61,54 %`** | `+60,65 %` | +0,9 pp en A |
| Estrés 2008 estricto | **`−32,79 %`** (`−32.790 €`) | `−35,16 %` (`−35.160 €`) | **A gana `2.370 €`** |
| Shock directo Top 10 US (`−50 %`) | `−4,66 %` (`−4.660 €`) | **`−2,12 %`** (`−2.119 €`) | **B gana `2.541 €`** |
| R1 Neutro 15A (6 % RV / 3 % resto, 0 alfa) | **`212.632 €`** | `200.392 €` | **`+12.240 €` en A** |
| R2 Inflacionario (5 % RV / 8 % real / 3 % RF) | `189.338 €` | **`189.605 €`** | `+267 €` en B |
| R3 Rotación Ex-US (4 % US / 7,5 % ex-US / 6,5 % MP) | **`216.227 €`** | `215.878 €` | `+349 €` en A |
| R4 US Boom continúa (8 % US / 5 % ex-US / 2 % MP) | **`216.631 €`** | `197.374 €` | **`+19.257 €` en A** |
| Media de los 4 regímenes | **`208.707 €`** | `200.812 €` | `+7.895 €` en A |
| Peor de los 4 regímenes | `189.338 €` | **`189.605 €`** | `+267 €` en B |
| *Break-even* del bloque activo | **`+0,58 pp/año`** | `+1,20 pp/año` | A exige la mitad |
| Órdenes verificadas al euro | 13 | 18 | A opera en una sesión |

*Cifras de R1-R4, media, suelo, estrés y break-even tomadas de la matriz homogénea de `auditoria-ranking.md`
§2, que aplica la misma fórmula a las seis propuestas; el resto, de los dos documentos. Los documentos
propios redondean distinto en el estrés: la Opción A publica `−32,73 %` (`−32.732 €`) y `neon-2`
`−35,15 %` (`−35.146 €`) con su fórmula estricta. Comprobado en código: con `0 %` de alfa y 6 %/3 %, la
Opción A acaba en ≈`212.700 €` y `neon-2` en ≈`200.390 €`.*

---

## 2. Lo que comparten

- **3 ISIN de 7 y de 13**: `Fidelity MSCI Japan Hedged` (`IE00BYX5NH74`, 8.000 € en las dos),
  `Fidelity MSCI Emerging Markets` (`IE00BYX5M476`, 12.000 € en A frente a 7.000 € en B) y
  `GS Global Small CORE` (`LU1599216113`, 10.000 € en las dos).
- **El mismo punto de partida**: la foto del 30/10/2026, Rock desmontada por traspaso (0 € de IRPF) y los
  `10.000 €` de `Groupama` fuera de la cartera, intocables.
- **El mismo diagnóstico**: las dos nacen de rechazar el MSCI World puro (72 % en EE. UU., 26,6 % en diez
  valores) y de no querer pagar 40-60 % de gestión activa.
- **La misma disciplina de coste declarada**: cero ETFs, cero clases de reparto, cero comisiones de éxito.

---

## 3. La diferencia de fondo: dónde vive el riesgo

| | Opción A | `neon-2` |
| --- | --- | --- |
| **Dónde está la bolsa** | `70 %` en cuatro indexados regionales baratos (`0,109 %`) | `43 %` en cinco indexados (`0,160 %`) |
| **Dónde está la convicción** | `10 %` en **un** fondo (`GS Small CORE`), y con prueba fechada en 2031 | `42 %` en **cinco** motores: `Robeco BP Global Premium` (10 %), `Brandes European Value` (10 %), `GS Small CORE` (10 %), `Wellington Infrastructure` (7 %) y `Ashoka WhiteOak India` (5 %) |
| **Dónde está el escudo** | `20 %`: `DWS Floating Rate Notes` (10 %) + `Cobas Renta` (10 %) | `15 %`: `EDM Renta R` (5 %) + `UBAM USD FRN` (5 %) + `GSQuartix Commodities` (5 %) |
| **Qué protege en un año como 2022** | El bloque corto flotante (`+1,50 %`) | El estilo del bloque activo (`−5,38 %` frente a `−12,85 %` del mundo) **más** las materias primas (`+14,83 %`) |
| **Qué NO tiene** | Materias primas, infraestructura, India, value europeo | Coste bajo, pocas líneas, y un solo gestor del que depender |

Ese cuadro explica las dos cifras que parecen contradecirse: **A cae menos en un 2008 estricto llevando
3,2 pp menos de renta variable, y pierde 3,2 pp en 2022**. No es un error de ninguna de las dos: A tiene `81,03 %` de RV y una caída de 2008
mejor (`−32,79 %` frente a `−35,16 %`), mientras B tiene `84,24 %` de RV y una caída de 2008 peor, pero un
2022 mucho mejor porque su bolsa no es beta pura: value europeo, infraestructura y small caps cayeron la
mitad que el índice en el shock de tipos.

**Y ojo con el 2022: el escudo de B aporta poco en euros.** `15.000 €` al `+4,59 %` son `689 €` frente a los
`300 €` de los `20.000 €` de A al `+1,50 %`: la diferencia del año son `389 €` en el bloque defensivo. Los
`3.224 €` de ventaja vienen del **bloque activo de renta variable**, no de la pólvora.

---

## 4. Ventajas de la propuesta final (Opción A)

1. **Cuesta la mitad o menos, y eso se ve en el saldo final**: `511 €/año` menos de TER y `15.288 €` menos
   de drag a 15 años. Aislando solo el coste (mismo supuesto de mercado para las dos), el TER de `neon-2`
   cuesta ≈`15.000 €` de capital final.
2. **Exige la mitad de alfa para no ser un error**: `+0,58 pp/año` sobre `30.000 €` activos frente a
   `+1,20 pp/año` sobre `42.000 €`, y `+1,33 pp` si el denominador es solo el bloque de RV activa de B.
3. **Gana en 3 de los 4 regímenes** de la matriz homogénea, y por mucho en el que más probable parece a
   15 años (`+19.257 €` si EE. UU. sigue mandando) y en el neutro (`+12.240 €`).
4. **Operativa de una sola sesión y siete líneas**: 13 órdenes, banda de ±5 pp, aportación repartible
   `350/150/120/80/100/100/100 €` y ninguna línea por debajo de `8.000 €`.
5. **La apuesta activa es pequeña y tiene fecha de caducidad**: si `GS Small CORE` no bate a su índice a
   5 años, se traspasa al indexado y el TER total baja a `0,164 %` (`164 €/año`). El error máximo está
   acotado y escrito.

## 5. Ventajas y carencias de `cartera-ai-neon-2`

**Ventajas (reales, no de folleto):**

1. **Es la cartera que mejor aguanta el escenario del que se habla**: `2022` en `−5,74 %` frente a
   `−8,96 %` de A, y un `Top 10` al `4,24 %` del dinero — menos de la mitad que los `9,31 %` de A. Si las
   diez grandes de EE. UU. cayeran un 50 %, B pierde `2.119 €` y A `4.660 €`.
2. **La desconcentración no es un tilt estético**: `68,9 %` de la RV fuera de EE. UU., `36,8 %` en SMID,
   cinco motores ortogonales y ningún sector por encima del `17,5 %` de la RV.
3. **Cubre huecos que A no cubre**: activos reales (`5 %` en materias primas), infraestructura y redes
   (`7 %`), India (`5 %`) y value europeo (`Brandes`, `+19,56 %` YTD).
4. **Cero comisiones de éxito en 13 fondos y cero solape con `cartera-ai-neon`**, que era la condición de
   su encargo.
5. **El acumulado real 2022-2026 es prácticamente el mismo que el de A** (`+60,65 %` frente a `+61,54 %`)
   con `3,2 pp` más de renta variable.

**Carencias:**

1. **Cuesta `0,784 %` y hay que pagarlo 15 años**: `23.720 €` de drag, `511 €/año` más que A. En el caso
   neutro (cero alfa) eso son `12.240 €` menos de capital final.
2. **El `42 %` activo necesita `+1,0 pp/año` de alfa solo para empatar a A** y `+1,20-1,33 pp` para no
   destruir valor frente a su propio índice. Es el punto débil estructural: por encima del `94 %` de los
   gestores activos no bate a su índice a 10-15 años (SPIVA Europe, citado en `ranking-argon.md`).
3. **13 líneas durante 15 años es trabajo**: 18 órdenes, tres mínimos de folleto que condicionan pesos
   (`Brandes` 10.000 USD, `Wellington` 5.000 USD, `GS Small CORE` 5.000 €), aportación mensual en 13
   destinos y un rebalanceo por bandas con más piezas móviles.
4. **El escudo es más volátil de lo que parece**: el `GSQuartix` de materias primas tiene `12 %` de
   volatilidad a 3A y `TER 1,15 %`; con la fórmula estricta de comité el estrés 2008 se va a `−35,16 %`
   (`−35.146 €`), el peor de las seis propuestas. Y `Ashoka India` lleva SRRI 6 y una comisión de éxito
   `Pendiente` en ficha.
5. **Su ventaja de 2022 es un año, no una promesa**: en el régimen inflacionario de la matriz homogénea
   gana a A por `267 €` a 15 años — es decir, todo el aparato de materias primas y ex-US compra
   prácticamente nada en la proyección; su ventaja se concentra en el año malo concreto.

---

## 6. El cruce: el único número que decide entre las dos

Con `0 %` de alfa y el mismo supuesto (6 % RV / 3 % resto), la Opción A acaba con `12.240 €` más. Para
empatar, el bloque del `42 %` de `neon-2` tiene que batir a su índice en **≈`1,0 pp/año neto de su TER`
durante 15 años:

| Alfa anual del bloque activo de `neon-2` | Capital a 15 años | Δ frente a la Opción A |
| --: | --: | --: |
| `0,0 pp` | `200.390 €` | `−12.242 €` |
| `+0,5 pp` | `206.501 €` | `−6.131 €` |
| **`+1,0 pp`** | **`212.787 €`** | **empate** |
| `+1,5 pp` | `219.250 €` | `+6.618 €` |
| `+2,0 pp` | `225.897 €` | `+13.265 €` |
| `+3,0 pp` | `239.758 €` | `+27.126 €` |

Cada punto de alfa del bloque vale `6.400-6.600 €` a 15 años. **No es una diferencia de fondo, es una apuesta
cuantificada**: A paga menos y no necesita que nadie acierte; B necesita que cinco gestores acierten
`1 pp` al año de media. La pregunta no es cuál es mejor cartera, sino si el titular cree que ese `1 pp`
existe — y su propia auditoría ya lo puso en duda al señalar el `+1,20 pp` de alfa de empate como la razón
de que `neon-2` no llegue al podio.

**La segunda pregunta, y es conductual:** ¿qué caída se mira sin vender? A cae `−32.790 €` en un 2008
estricto; B, `−35.146 €`. En 2022, al revés: `−8.960 €` frente a `−5.736 €`. Si el escenario que quita el
sueño es una burbuja tecnológica que estalla, B; si es una recesión deflacionaria, A.

---

## 7. Lo que ninguna de las dos resuelve

- **El colchón no está dimensionado**: las dos dejan `10.000 €` en `Groupama` sin haberlo cruzado con los
  gastos reales (833 €/mes asumidos). Es el pendiente más antiguo de la cartera y no lo arregla ninguna
  de las dos composiciones.
- **La aportación no está decidida**: A documenta el reparto de `1.000 €/mes`; B, el suyo, pero ninguna de
  las dos tiene un mandato de aportación ni fechas.
- **Ambas dependen de que la plataforma siga vendiendo lo mismo**: A necesita confirmar el acceso ómnibus
  a `iShares Developed World S` (mínimo de folleto `200 M€`); B necesita que sigan abiertos `Brandes`,
  `Wellington` y `Ashoka`, y que ninguno entre en soft close en 15 años.
- **Ninguna descuenta comisiones de éxito futuras**: hoy son `0/7` y `0/13`, pero `Ashoka` ya las tiene
  «pendientes» en ficha.

---

## 8. Veredicto

**La propuesta final (Opción A) es la elección defendible** y por eso fue la #1: con el mismo supuesto de
mercado acaba `12.240 €` por delante, cuesta `511 €/año` menos, exige la mitad de alfa, se opera en siete
líneas y tiene la apuesta activa acotada con fecha de revisión. **`cartera-ai-neon-2` es la alternativa
correcta si y solo si el titular quiere pagar `0,5 pp` al año por una cobertura explícita del riesgo
megacap y una cartera que no dependa de la beta estadounidense** — y aun así conviene que sepa que esa
cobertura, en la matriz de cuatro regímenes, se paga con `7.895 €` de media y `19.257 €` si EE. UU. sigue
mandando, a cambio de `267 €` en el régimen inflacionario, `2.541 €` menos de pérdida en un desplome del
Top 10 y `3.224 €` menos de caída en un 2022.

Si el titular quisiera lo mejor de las dos, el camino no es una tercera cartera: es **bajar el peso del
bloque activo de `neon-2`** (por ejemplo al `20-25 %`) dejando su tesis ex-US/SMID y su colchón, y medir
el resultado con este mismo cruce. Esa decisión no está tomada y no la toma este documento.

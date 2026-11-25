---
title: "Auditoría institucional y ranking de las diez carteras definitivas (30-45 % indexado)"
date: 2026-11-25
type: portfolio-research
category: finance
tags: [cartera, auditoria, ranking, cartera-ai-definitivas-estudiar, indexado-30-45, myinvestor, break-even-alpha, look-through, riesgo, cartera-ai-argon]
status: final
related:
  - finance/portfolio/cartera-ai-definitivas-estudiar/README.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-argon/100k.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-hy4-definitiva/100k.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-final-conservadora/100k.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-neon/110k.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-rock-desmontado/100k.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-final-atrevida/110k.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-40-max-index/100k.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-c4-defensiva/100k.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-rock-index-value-todo/100k.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-andres/100k.md
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
  - finance/portfolio/cartera-myinvestor/propuesta-pieza.md
---

# Auditoría institucional y ranking de `cartera-ai-definitivas-estudiar`

Auditoría técnica, cuantitativa y forense de los diez expedientes agrupados en [`finance/portfolio/cartera-ai-definitivas-estudiar/`](README.md) (contenedor de propuestas con un rango objetivo de **30 % a 45 % en fondos indexados**), contrastados frente a la foto real de [`cartera-actual.md`](../cartera-myinvestor/cartera-actual.md), la propuesta viva [`propuesta-pieza.md`](../cartera-myinvestor/propuesta-pieza.md) y las 2.011 fichas individuales verificadas en [`finance/fondos-myinvestor/`](../../fondos-myinvestor/README.md).

---

## 0. Marco de evaluación institucional (los 5 ejes del comité)

Para evaluar y ordenar nueve carteras bajo un criterio de análisis financiero experto —descartando preferencias subjetivas de autor— se auditan cinco dimensiones verificables:

1. **Eficiencia de costes totales (*all-in fee drag*) y *break-even alpha*:** TER fijo ponderado, comisiones de éxito explícitas o implícitas, sobrecostes evitables en la compra de beta y el diferencial anual neto que el bloque activo está obligado a generar solo para empatar con su equivalente indexado frente a la tasa base de fracaso activo (SPIVA Europe mid-2026: 94 %–97,65 % a 10 años).
2. **Arquitectura de factores y *look-through* real:** Exposición subyacente real a renta variable, renta fija y liquidez (`alloc_equity`), peso efectivo de Estados Unidos y de las 10 mayores tecnológicas estadounidenses, diversificación de factores activos (evitando concentrar el 100 % del presupuesto activo en un único factor o geografía) y ausencia de cajones opacos («otros» sin desglosar).
3. **Pureza del escudo defensivo (convexidad en cola: prueba real de 2022 y estrés tipo 2008):** Capacidad del bloque defensivo para preservar capital cuando caen simultáneamente la bolsa y los bonos con duración (escenario 2022) o cuando se cierran los diferenciales de crédito (escenario 2008), penalizando los diseños que disfrazan beta de crédito, convertibles o deuda emergente como si fueran renta fija defensiva.
4. **Ejecutabilidad operativa y fiscal en MyInvestor:** Trazabilidad de órdenes por traspaso entre fondos armonizados (0 € de peaje en IRPF), respeto a mínimos iniciales y adicionales por participación, ausencia de fondos en *soft close* o con penalizaciones de salida y plazos de liquidación.
5. **Integridad forense de los datos:** Exactitud de los saldos de origen, ISINs, políticas de cobertura cambiaria, comisiones publicadas y referencias cruzadas entre documentos del repositorio.

---

## 1. Hallazgos forenses críticos (anomalías detectadas en los ficheros)

Antes de entrar al ranking, la auditoría línea por línea de los documentos revela **cuatro anomalías técnicas** que condicionan la puntuación y la ejecutabilidad inmediata de varias propuestas:

### 1.1. Descuadre forense de saldos e ISINs de origen en el Modo B de `cartera-ai-neon` y en su tabla comparativa
- **Plan de traspasos Modo B inejecutable tal como está redactado ([`cartera-ai-neon/110k.md` §6.2, líneas 276–306](cartera-ai-neon/110k.md#L276-L306)):** Para transformar `cartera-actual.md` (100.000 € + 10.000 € nuevos), el documento asume unos saldos e ISINs de partida que **no coinciden con [`cartera-actual.md`](../cartera-myinvestor/cartera-actual.md#L36-L47)**:
  - Inventa que el titular posee `14.000 €` en `Cobas Internacional C` (`ES0119199000`), `5.000 €` en `NB Next Gen Space` (`IE00050T89N3`), `5.000 €` en `UBS Greater China` (`LU0072913022`), `10.000 €` en `Neuberger Short Duration I` (`IE00BFZMJT78`), `8.000 €` en `DNCA Alpha Bonds B` (`LU1694789535`) y `8.000 €` en `Carmignac Sécurité` (`FR0010149120`).
  - La foto real de [`cartera-actual.md`](../cartera-myinvestor/cartera-actual.md#L36-L47) tiene **`22.000 €` en `Neuberger U` (`IE00BL1GVT98`), `13.000 €` en `DNCA A` (`LU1694789451`), `12.000 €` en `Carmignac Portfolio Credit A` (`LU1623762843`), `8.000 €` en `Gamma Global A` (`ES0140794001`), `2.000 €` en `MyInvestor Value C` (`ES0165243025`) y solo `1.000 €` en cada uno de `Cobas International P` (`LU1598719752`), `NB Space` (`IE00018YKVN0`) y `UBS MSCI China` (`LU1815002040`)**.
- **Citas inexactas a otras carteras del repositorio ([`cartera-ai-neon/110k.md` §5.2, líneas 244–246](cartera-ai-neon/110k.md#L244-L246)):**
  - Atribuye a [`propuesta-pieza.md`](../cartera-myinvestor/propuesta-pieza.md) un «63,00 % indexado y ~80,0 % RV», cuando en realidad tiene **38,3 % indexado y 54,6 % RV**.
  - Atribuye a [`cartera-ai-final-atrevida/110k.md`](cartera-ai-final-atrevida/110k.md) un «~89,5 % RV» y afirma que incluye `Azvalor Internacional` y `Magallanes M`, cuando en realidad tiene **82,15 % RV**, no incluye Azvalor y descartó expresamente `Magallanes M` en su §8 en favor de `Brandes European Value`.
  - Atribuye a [`cartera-ai-hy4-definitiva/100k.md`](cartera-ai-hy4-definitiva/100k.md) un «39,00 % indexado, ~74,1 % RV, TER 0,74 % y uso de `Magallanes ES0159259011`», cuando en realidad tiene **35,00 % indexado, 65,5 % RV, TER 0,537 %** y excluyó expresamente a Magallanes en su §3.

### 1.2. Incumplimiento del rango del contenedor (30–45 %) en el documento base de `cartera-ai-rock-desmontado`
- El contenedor agrupa carteras entre el **30 % y el 45 % de indexado**. Sin embargo, la tabla titular de [`cartera-ai-rock-desmontado/100k.md` (§4, líneas 109–125)](cartera-ai-rock-desmontado/100k.md#L109-L125) construye y ordena el **Nivel A**, que invierte **`62.500 €` de `90.000 €` invertibles en fondos indexados = `69,44 %` indexado (`62,50 %` sobre `100.000 €`)**.
- El Nivel C (`38,3 %` indexado) solo aparece mencionado como variante resumida en su §14 ([líneas 423–434](cartera-ai-rock-desmontado/100k.md#L423-L434)), cuyo desarrollo real son [`propuesta-pieza.md`](../cartera-myinvestor/propuesta-pieza.md) y [`cartera-ai-final-conservadora/100k.md`](cartera-ai-final-conservadora/100k.md).

### 1.3. Infravaloración del TER titular por fondos sin dato publicado en `cartera-ai-andres`
- [`cartera-ai-andres/100k.md` (§2 y §3, líneas 49–80)](cartera-ai-andres/100k.md#L49-L80) declara un TER de **`0,463 %` (`463,30 €/año`)**, pero ese número suma `0,00 €` de coste fijo en dos fondos que representan el **18 % de la cartera (`18.000 €`)**: `MyInvestor Value C` (`8.000 €`) y `Kaizen Global Income` (`10.000 €`), ambos marcados como `no publicado` y ambos con un **9 % de comisión de éxito**.
- Aplicando la comisión real de gestión (~1,35 %–1,45 %), el coste fijo real asciende a **`~0,68 %–0,73 %`** más comisiones de éxito. Adicionalmente, en [`cartera-ai-andres/200k.md` (§1, línea 51)](cartera-ai-andres/200k.md#L51) afirma llevar un «núcleo indexado del 34 %» sumando solo los 5 indexados de RV/REIT (`15 + 6 + 5 + 4 + 4 = 34 %`) y olvidando sumar el `6 %` del indexado de renta fija `iShares Global Aggregate 1-5Y Bond` (**`40,0 %` indexado total**).

### 1.4. Contradicción técnica sobre la cobertura de divisa en `DWS Invest CROCI Japan LCH` (`LU1769942233`)
- Tanto [`cartera-ai-final-atrevida/110k.md` (§8, línea 289)](cartera-ai-final-atrevida/110k.md#L289) como [`cartera-ai-rock-index-value-todo/100k.md` (§5, línea 143)](cartera-ai-rock-index-value-todo/100k.md#L143) afirman que `DWS Invest CROCI Japan LCH` (`LU1769942233`) tiene el **«yen sin cubrir»**.
- Verificada su ficha [`finance/fondos-myinvestor/rv-japon/LU1769942233.md`](../../fondos-myinvestor/rv-japon/LU1769942233.md#L16-L74), la clase **`LCH`** de DWS corresponde a la clase en euros con cobertura de divisa (*Liquid Currency Hedged*), lo que explica que rindiera **+42,90 % en 2023** y **+18,28 % anualizado a 5 años en EUR** durante la fuerte depreciación del yen. Eso sí, su ficha exige un mínimo adicional de **1 participación (`NAV 637,70 €`)**, dato relevante para planes de aportación mensual pequeños.

---

## 2. Matriz comparativa auditada (las 10 carteras cara a cara)

| Pos. | Cartera | Capital base | % Indexado | % RV Real (*look-through*) | % EE. UU. s/RV | TER Fijo Anual | Líneas con Éxito | *Break-Even Alpha* del Bloque Activo | Caída 2008 / Dato 2022 | Nota Global |
| :---: | --- | ---: | ---: | ---: | ---: | ---: | :---: | ---: | ---: | :---: |
| **#1** | [`cartera-ai-argon`](cartera-ai-argon/100k.md) | 100.000 € *(90k + 10k)* | **34,00 %** *(37,78 % s/90k)* | **68,76 %** *(76,40 % s/90k)* | **25,37 %** *(Top10: 6,98 %)* | **0,725 %** *(0,798 % s/90k; 0,685 % var.)* | 1 / 13 *(0 en var.)* | **+0,86 pp/año** *(+1,39 pp s/RV)* | −28,0 % *(2008)* / **−4,54 % (2022)** | **9,5 / 10** |
| **#2** | [`cartera-ai-hy4-definitiva`](cartera-ai-hy4-definitiva/100k.md) | 100.000 € | **35,00 %** | **65,50 %** | 50,0 % *(32,7 % tot.)* | **0,537 %** *(537,10 €)* | **0 / 10** | **+0,84 pp/año** *(s/ 60.000 €)* | −7,97 % *(MaxDD 5A real)* | **9,1 / 10** |
| **#3** | [`cartera-ai-final-conservadora`](cartera-ai-final-conservadora/100k.md) | 100.000 € *(90k + 10k)* | **38,33 %** *(s/ 90k)* | **54,61 %** *(s/ 90k)* | 36,7 % | **0,517 %** *(0,566 % s/90k)* | **0 / 12** | **+0,53 pp/año** *(+1,49 pp s/RV)* | −23,2 % *(−20.885 €)* | **8,8 / 10** |
| **#4** | [`cartera-ai-neon`](cartera-ai-neon/110k.md) | 110.000 € | **32,73 %** | **72,28 %** | **26,37 %** *(Top10: 6,71 %)* | **0,849 %** *(0,771 % var. 0% éx.)* | 2 / 13 *(0 en var.)* | **+1,52 pp/año** *(s/ 44.000 € RV)* | −29,5 % *(2008)* / **−5,10 % (2022)** | **8,6 / 10** *(9,4 en Modo A)* |
| **#5** | [`cartera-ai-rock-desmontado`](cartera-ai-rock-desmontado/100k.md) | 100.000 € *(90k + 10k)* | **69,44 %** *(Nivel A)* | **55,31 %** *(s/ 90k)* | 45,8 % | **0,236 %** *(0,255 % s/90k)* | **0 / 12** | **~0,15 pp/año** *(solo 2 satélites)* | −23,5 % *(−21.118 €)* | **8,3 / 10** *(fuera de banda)* |
| **#6** | [`cartera-ai-final-atrevida`](cartera-ai-final-atrevida/110k.md) | 110.000 € *(100k + 10k)* | **37,27 %** | **82,15 %** | 43,1 % | **0,798 %** *(877,80 €)* | **0 / 12** | **+1,43 pp/año** *(s/ 51.000 € RV)* | −33,4 % *(−36.733 €)* | **7,8 / 10** |
| **#7** | [`cartera-ai-40-max-index`](cartera-ai-40-max-index/100k.md) | 100.000 € / 200.000 € | **40,00 %** | **73,03 %** *(73,6 % 200k)* | ~52,0 % | **0,792 %** *(0,80 % 200k)* | 1 / 9 *(Alken 10 %)* | **+1,17 pp/año** *(s/ 60.000 €)* | −30,0 % *(>32 % c/conv.)* | **6,9 / 10** |
| **#8** | [`cartera-ai-c4-defensiva`](cartera-ai-c4-defensiva/100k.md) | 100.000 € | **44,00 %** | **34,06 %** | **70,13 %** | **0,608 %** *(>1,15 % c/éxito)* | **4 / 8** *(7,5 % a 20 %)* | **>1,20 pp/año** *(incl. éxito)* | −15,1 % *(−15.072 €)* | **6,4 / 10** |
| **#9** | [`cartera-ai-rock-index-value-todo`](cartera-ai-rock-index-value-todo/100k.md) | 100.000 € *(90k + 10k)* | **30,00 %** *(vía Rock)* | **55,51 %** *(s/ 90k)* | 45,5 % | **0,615 %** *(614,70 €)* | **0 / 14** | **+0,70 pp/año** + sobrecoste Rock | −23,5 % *(−21.184 €)* | **5,8 / 10** |
| **#10** | [`cartera-ai-andres`](cartera-ai-andres/100k.md) | 100.000 € / 200.000 € | **38,00 %** *(40 % en 200k)* | **60,31 %** *(60,0 % 200k)* | ~35,0 % | **0,463 %** *(~0,70 % real)* | **2 / 11** *(+2 sin TER)* | No auditable *(18 % sin TER)* | −25,3 % *(−25.315 €)* | **4,9 / 10** |

---

## 3. Razonamiento detallado del ranking (del #1 al #10)

### 🏆 #1. [`cartera-ai-argon/100k.md`](cartera-ai-argon/100k.md) — Nota: 9,5 / 10
**Tesis para el analista:** Sintetiza lo mejor de [`cartera-ai-neon`](cartera-ai-neon/110k.md), [`cartera-ai-hy4-definitiva`](cartera-ai-hy4-definitiva/100k.md) y [`cartera-ai-final-conservadora`](cartera-ai-final-conservadora/100k.md), eliminando las cuatro anomalías forenses detectadas en §1 y cuadrando al euro las **14 órdenes de traspaso** desde [`cartera-actual.md`](../cartera-myinvestor/cartera-actual.md).

- **Por qué alcanza el #1 para un horizonte de 15 años con mercados caros:**
  1. **Tracción agresiva con desconcentración quirúrgica de EE. UU.:** Sube la RV *look-through* al **76,40 % de los 90.000 € invertibles (68,76 % de los 100.000 €)**, pero reduce EE. UU. al **25,37 % de la RV** (`74,63 %` fuera de EE. UU.) y las 10 tecnológicas estadounidenses al **5,33 % de los 90.000 € (4.797 €)**.
  2. **Cuatro indexados con Japón cubierto a EUR (`34.000 €` = `37,78 %` s/90k · `34,00 %` s/100k):** Incorpora el hallazgo [`Fidelity MSCI Japan Index P-ACC-EUR (Hedged)` (`IE00BYX5NH74`)](../../fondos-myinvestor/rv-japon/IE00BYX5NH74.md) al `0,20 %` de TER (+20,14 %/año a 3A, +16,30 %/año a 5A), manteniendo el coste medio del bloque pasivo en **`0,124 %` (`42,20 €/año`)**.
  3. **Cinco motores activos ortogonales con 0 % comisiones de éxito (`35.000 €`):** `M&G European Strategic Value` (+1,78 % en 2022, Sharpe 1,85), `Horos Value Internacional` (+4,90 % en 2022), `Palm Harbour Global Value` (`1,02 %` TER, 0 % éxito — o `Robeco BP Global Premium` con +1,75 % en 2022), `Robeco QI EM Active` (alfa 5A +4,23 pp/año) y `DWS Invest CROCI Japan LCH` (−2,76 % en 2022, +18,28 %/año a 5A, cubierto a EUR).
  4. **Escudo defensivo que ganó +0,83 % en 2022 y protocolo anticrisis:** Conserva intactos los `8.000 €` actuales de `Gamma Global A` (+3,21 % en 2022, Sharpe 2,72) junto a `DWS Floating Rate Notes` (`0,25 %`, −0,90 % en 2022), `Cobas Renta` (`0,33 %`, +3,89 % en 2022) y `Twelve Cat Bond` (+9,27 %/año a 3A), dejando la caída total de la cartera en 2022 en solo **−5,04 % s/90k (−4,54 % s/100k)**.

---

### 🥇 #2. [`cartera-ai-hy4-definitiva/100k.md`](cartera-ai-hy4-definitiva/100k.md) — Nota: 9,1 / 10
**Tesis para el analista:** Es la cartera institucionalmente mejor construida en relación **diversificación de factores / coste total / exigencia de alfa / control de *drawdown***.

- **Cribado sistemático y control del *fee drag* (`0,537 %`, 0 € éxito):** Nace de cruzar las tres familias de cribado de ~2.000 fondos del catálogo (108 finalistas), seleccionando sistemáticamente el vehículo con **menor TER dentro de cada rol activo** y vetando cualquier comisión de éxito.
- **Ortogonalidad real de factores en el bloque activo de RV (30 % del total en 4 motores no solapados):**
  1. *Global Low-Volatility / Conservative:* `Robeco QI Global Conservative Equities D EUR` (`LU0705782398`, 10 %, TER `1,01 %`), que reduce la beta de mercado sin pagar múltiplos de *quality growth* caros.
  2. *Global Small/Mid Deep Value:* `Cobas LUX SICAV — Palm Harbour Global Value F Acc EUR` (`LU1935059029`, 8 %, TER `1,02 %`), que captura la prima *small/mid value* ex-EE. UU. ahorrando entre 57 y 88 pb/año frente a `Horos` (`1,86–1,90 %`), `Magallanes M` (`1,81 %`) o `Sigma` (`1,59 % + 9 % éxito`).
  3. *Quant Multifactor Emerging Markets:* `Robeco QI Emerging Markets Active Equities D EUR` (`LU0329355670`, 7 %, TER `1,52 %`), consenso de las tres variantes de cribado con alfa positivo a 3 y 5 años.
  4. *Activos reales cotizados:* `First Sentier Global Listed Infrastructure I EUR Acc` (`IE00BYSJTY39`, 5 %, TER `1,59 %`).
- **Listón de alfa alcanzable (`+0,84 pp/año`):** A diferencia de las carteras de autor que exigen entre `+1,43 %` y `+1,52 %` anual al bloque activo solo para empatar con un índice, esta estructura reduce el *break-even alpha* a **`+0,84 pp/año`** sobre los 60.000 € activos.
- **Comportamiento verificado en *backtest* (2021–2026):** **+7,99 % anualizado, volatilidad 6,64 %, caída máxima −7,97 % y ratio de Sharpe 1,20** (con `Cobas Renta` al 8 % y `Twelve Cat Bond` al 5 % amortiguando el ciclo de tipos).
- **Puntos débiles a corregir antes de ejecutar:**
  1. Concentra un **17 % (`17.000 €`) en `Neuberger Short Duration Euro Bond I` (`IE00BFZMJT78`)**, que en 2022 cayó −5,68 %; dividir esa posición con `DWS Floating Rate Notes LC` (`LU0034353002`, TER `0,25 %`, −0,90 % en 2022) mejoraría su resistencia ante shocks de tipos.
  2. Falta redactar su tabla operativa de órdenes de traspaso desde [`cartera-actual.md`](../cartera-myinvestor/cartera-actual.md).

---

### 🥈 #2. [`cartera-ai-final-conservadora/100k.md`](cartera-ai-final-conservadora/100k.md) — Nota: 8,8 / 10
**Tesis para el analista:** Es la **mejor cartera de ejecución inmediata por traspaso desde [`cartera-actual.md`](../cartera-myinvestor/cartera-actual.md)** para un mandato conservador-equilibrado (**54,6 % RV**, coste **`0,517 %`** sobre 100k / **`0,566 %`** sobre 90k invertibles).

- **Ingeniería fiscal y operativa impecable:**
  - Cuadra al euro los **22 traspasos en dos fases** desde los saldos reales del 30/10/2026 (`Neuberger U 22.000 €`, `DNCA 13.000 €`, `Carmignac 12.000 €`, `Gamma 8.000 €`, etc.) más el desmontaje sin peaje fiscal de los `30.000 €` de `Rock` a través del monetario puente.
  - Detecta y evita una trampa fiscal clásica en España: no convierte los `11.000 €` ya poseídos en `Neuberger clase U` (`0,38 %`) a `clase I` (`0,25 %`) porque un cambio de clase dentro del mismo fondo tributa como reembolso; en su lugar, usa la `clase I` exclusivamente para los `6.000 €` procedentes de otros fondos, eliminando de paso a `M&G Short Dated` (`0,47 %` y mínimo inicial de `1.000 €`).
  - Reduce la duración de la renta fija de **3,83 años a 1,61 años** (recortando el impacto de +100 pb de tipos de −2.356 € a **−657 €**, una reducción del 72 % del riesgo de tipos).
  - Exige solo **+0,53 pp/año** al bloque no indexado global (55.500 €) para empatar con el Nivel A, y detalla al euro la aportación de `1.000 €/mes` (10 órdenes mensuales + 2 trimestrales de 201 € para `Horos` y `Cobas Renta`).
- **Por qué queda #2 y no #1:**
  1. **Apuesta unifactorial en el bloque activo de RV (`21.000 €`):** Sus tres gestores activos (`Magallanes European M`, `Horos Value Internacional` y `Cobas Large Cap P`) compran el mismo factor (*deep value* europeo/ibérico), solapan en Francia (~19–21 %) y `Cobas Large Cap` presenta un **30,7 % de su cartera en «otros» sin desglosar**. Si el factor *value* europeo sufre un ciclo adverso, las tres líneas caen a la vez.
  2. **Ineficiencia de `Aegon European ABS A` (`8.000 €` al `0,66 %`):** Como reconoce honestamente su §7, el escenario del KID de Aegon proyecta un 2,0 % bruto y 1,3 % neto (la comisión consume un tercio del retorno esperado de esa línea).

---

### 🥉 #3. [`cartera-ai-neon/110k.md`](cartera-ai-neon/110k.md) — Nota: 8,6 / 10 *(9,4 / 10 en Modo A o tras corregir la tabla del §6.2)*
**Tesis para el analista:** Posee **la mejor arquitectura macroeconómica, el mejor control de concentración tecnológica y el mejor escudo defensivo probado en 2022** de todo el repositorio para un inversor de 40 años a 15 años vista (**72,28 % RV real**), pero queda penalizada al #3 por los errores forenses de su §6.2 y §5.2.

- **Por qué su diseño de cartera es extraordinario:**
  1. **Desconcentración quirúrgica de las 10 megacaps tecnológicas de EE. UU.:** Mientras un MSCI World concentra el 72,0 % en EE. UU. y el 26,65 % en sus 10 mayores posiciones, `cartera-ai-neon` reduce el peso de las 10 tecnológicas estadounidenses al **4,85 % del patrimonio total (6,71 % de la RV)**, baja EE. UU. al **26,37 % de la RV** (`73,63 %` fuera de EE. UU.) y eleva la exposición a **Small & Mid Caps al 39,85 % de la RV**.
  2. **Selección activa superior en Europa y Japón:** En lugar de pagar `1,81 %` o `1,95 %` por Magallanes, selecciona **`M&G (Lux) European Strategic Value A EUR Acc` (`LU1670707527`)** (TER `1,65 %`, 0 % éxito, **+1,78 % en 2022**, **+22,43 %/año a 3A**, **+15,16 %/año a 5A**, volatilidad 3A de solo **9,91 %** y **Sharpe 1,85**), combinado con **`Horos Value Internacional`** (+4,90 % en 2022), **`DWS Invest CROCI Japan LCH`** (cubierto a EUR, −2,76 % en 2022, +18,28 %/año a 5A), **`Robeco QI EM Active`** y **`Sigma Internacional`** (o **`Palm Harbour`** al `1,02 %` en la variante 0 % éxito).
  3. **El único escudo defensivo de 30.000 € (27,27 %) que cerró 2022 en positivo (+0,45 %):** Cero renta fija indexada y cero duración larga; combina `DWS Floating Rate Notes` (`0,25 %`, −0,90 % en 2022), `Gamma Global A` (+3,21 % en 2022, Sharpe 2,72 — o `B&H Deuda` al `0,36 %` sin éxito), `Cobas Renta` (`0,33 %`, +3,89 % en 2022), `Twelve Cat Bond` (+9,27 %/año a 3A) y `AXA Trésor Court Terme` (`0,06 %`). Gracias a ello, **toda la cartera (con 72,3 % de RV) habría caído solo −5,10 % en 2022** (frente a −12,84 % del MSCI World), e incorpora un protocolo cuantitativo de rotación anticrisis (§8.2) cuando el MSCI World cae −20 % y −35 %.
  4. **100 % verificada en `finance/fondos-myinvestor/`:** Sus 13 fondos titulares y sus 4 suplentes sin comisión de éxito existen como ficha individual en el catálogo local.
- **Por qué queda #3 y qué requiere:**
  1. **Corregir la tabla de traspasos del Modo B (§6.2):** Debe reescribirse con los saldos reales de `cartera-actual.md` (`Neuberger U 22k`, `DNCA 13k`, `Carmignac Credit 12k`, etc.).
  2. **Activar preferiblemente la variante 0 % comisión de éxito (§2.5):** Sustituir `Sigma` por `Palm Harbour` (`LU1935059029`, TER `1,02 %`, 0 % éxito) baja el coste fijo y reduce el *break-even alpha* del Bloque 2 de `+1,52 %` a `+1,42 %`.

---

### #4. [`cartera-ai-rock-desmontado/100k.md`](cartera-ai-rock-desmontado/100k.md) — Nota: 8,3 / 10 *(Fuera de banda en su versión titular)*
**Tesis para el analista:** Es el **óptimo matemático de costes (`0,236 %` = `236,10 €/año`)** para un perfil 55/45 bajo la hipótesis de eficiencia de mercado (SPIVA), pero **no cumple el mandato del 30–45 % indexado** en el diseño desarrollado en su tabla principal.

- **Fortalezas:** Ahorra **280–380 €/año** frente a las opciones con gestión activa de RV, elimina el riesgo de gestor en renta variable desarrollada/emergente/small-caps/REITs y limita la gestión activa a donde el índice no ofrece alternativa limpia (`Robeco QI European Conservative` para *low-vol* europeo, `Twelve Cat Bond` para riesgo asegurador descorrelacionado y selección de crédito corto en `Neuberger` + `M&G` + `Cobas Renta`).
- **Debilidades:**
  1. **69,44 % indexado sobre 90.000 €:** Excede en casi 25 puntos porcentuales el techo del 45 % del contenedor.
  2. **Riesgo de tipos en crédito indexado:** Incluye `6.000 €` en `iShares Euro IG Corporate Bond Index` con duración ~4,7 años (rentabilidad 1A negativa) y concentra el 65 % del patrimonio invertible en una única gestora (BlackRock/iShares).

---

### #5. [`cartera-ai-final-atrevida/110k.md`](cartera-ai-final-atrevida/110k.md) — Nota: 7,8 / 10
**Tesis para el analista:** Diseño agresivo desde cero (**82,15 % RV real**, `0,798 %` TER, 0 % comisiones de éxito) con excelente transparencia en sus supuestos de rentabilidad esperada (`≈6,1 %` central / `7,4 %` favorable), pero penalizado por **solapamiento caro en `Fundsmith` y escasa reserva defensiva para mercados en múltiplos máximos**.

- **Fortalezas:** Diversifica la renta variable activa en seis vehículos de cinco geografías/estilos sin comisiones de éxito (`Brandes European Value`, `Horos`, `Fundsmith`, `Robeco BP US Large Cap`, `Federated Hermes Asia ex-Japan` y `Nomura Japan Strategic Value Hedged`) y respeta todos los mínimos iniciales (incluidos los `10.000 €` de Brandes).
- **Debilidades técnicas:**
  1. **`Fundsmith Equity T` (`10.000 €` al `1,09 %`) duplica el sesgo del núcleo indexado:** Con un 79,6 % en EE. UU. y 32 % en tecnología, compra la misma exposición geográfica y sectorial que los `25.000 €` del `iShares Developed World` (`0,06 %`), pagando 18 veces más de comisión por un fondo que lleva 5 años rindiendo muy por debajo del índice (+2,9 % anualizado a 5A).
  2. **Error de diagnóstico en Japón (§8):** Descarta `DWS Invest CROCI Japan LCH` (`1,48 %`) afirmando que tiene el «yen sin cubrir» para pagar `1,57 %` en `Nomura Japan Hedged`, cuando la clase `LCH` de DWS sí cubre el yen.
  3. **Exigencia de alfa elevada (`+1,43 pp/año` sobre 51.000 €) y caída severa (−33,4 % = −36.733 €):** Al dejar solo `8.000 €` en crédito corto (`Neuberger I` + `Aegon ABS`), carece de amortiguador táctico real si se entra de golpe antes de una corrección de múltiplos.

---

### #6. [`cartera-ai-40-max-index/100k.md`](cartera-ai-40-max-index/100k.md) (y [`200k.md`](cartera-ai-40-max-index/200k.md)) — Nota: 6,9 / 10
**Tesis para el analista:** Optimiza muy bien el cupo del 40 % indexado (gastándolo íntegro en RV desarrollada y emergente por solo 36 €/año), pero **comete un error clásico de construcción institucional en su 25 % de renta fija: sustituir duración y liquidez defensiva por riesgo de crédito, deuda emergente y convertibles (*wrong-way correlation risk*)**.

- **Fortalezas:** Núcleo pasivo ultra-eficiente (`28 %` World al `0,06 %` + `12 %` EM al `0,16 %`), excelente satélite japonés cubierto a EUR (`Man Japan CoreAlpha D H EUR`, +26,5 % a 3A) y escalado coherente a 200k incorporando `Magallanes Iberian Equity M` (5 %).
- **Debilidades técnicas:**
  1. **El bloque «defensivo» del 25 % tiene alta correlación con la bolsa en estrés:** Asigna `13 %` a `Vontobel Credit Opportunities HI Hedged` (con 27 % en swaps y exposición a Turquía/Brasil), `7 %` a `Vontobel EM Blend HI Hedged` (deuda soberana y corporativa de México, Brasil y Turquía) y `5 %` a `Swisscanto Global Convertible ATH` (bonos convertibles cuya sensibilidad bursátil no aparece en `alloc_equity`). Con **0 % en monetario y 0 % en deuda soberana G7**, en una crisis de liquidez ese 25 % cae al mismo tiempo que el 73 % de RV.
  2. **Sobreprecio en Small Caps europeas y solapamiento en `Fundsmith`:** Paga **`2,10 %` de TER + `10 %` de comisión de éxito** en `Alken Small Cap Europe R` (`8.000 €`), mantiene `12.000 €` en `Fundsmith` (+7,8 % a 3A, rezagado frente al índice) y asume el 31 % opaco en «otros» de `Cobas Large Cap`.

---

### #7. [`cartera-ai-c4-defensiva/100k.md`](cartera-ai-c4-defensiva/100k.md) — Nota: 6,4 / 10
**Tesis para el analista:** Es el único diseño verdaderamente defensivo del grupo (**34,06 % RV real**, caída de manual **−15,07 %**) y utiliza alternativos líquidos con criterio (`Jupiter Merian GEAR` Market Neutral + `Twelve Cat Bond`), pero **falla por una estructura abusiva de comisiones de éxito en el 44 % de la cartera y una ejecución ineficiente de su bloque de renta variable**.

- **Fortalezas:** Baja correlación estructural entre bloques (Market Neutral con beta 0,09 y cinco años naturales positivos consecutivos, bonos catastróficos, retorno absoluto multiestrategia con capacidad de ponerse corto en `Dunas Valor Equilibrado` y duración soberana pura en `iShares Euro Government Bond` al `0,10 %`).
- **Debilidades técnicas:**
  1. **Cuatro comisiones de éxito sobre 8 líneas (44.000 € expuestos a *performance fees*):**
     - `Jupiter Merian GEAR` (`8.000 €`): `1,55 %` TER + **20 % de comisión de éxito**.
     - `Sissener Corporate Bond R` (`12.000 €`): `0,90 %` TER + **20 % de comisión de éxito** sobre Euríbor 3M + 1 % (coste total estimado en KID: **1,70 %/año**).
     - `Dunas Valor Equilibrado R` (`12.000 €`): `1,19 %` TER + **11 % de comisión de éxito** sobre Euríbor + 200 pb (manteniendo un 25 % en liquidez que cobra 1,19 %).
     - `Cartesio X` (`12.000 €`): `0,63 %` TER + **7,5 % de comisión de éxito** (y mínimo inamovible de `6.000 €`).
     - En un año positivo normal (+6 %), el coste efectivo total se dispara de `0,608 %` a **más del `1,15 %–1,35 %` anual**, erosionando severamente la rentabilidad neta de una cartera defensiva.
  2. **Ineficiencia y concentración en el bloque de RV (32.000 €):** Teniendo disponible `iShares Developed World S` al `0,06 %`, utiliza `Vanguard Global Stock` (`IE00B03HD191`) al **`0,18 %`** (pagando el triple por el mismo índice: +38,40 €/año sin contrapartida) y deja el **70,13 % de toda su renta variable concentrada en EE. UU.** (0 % en emergentes y 0 % en small caps).

---

### #8. [`cartera-ai-rock-index-value-todo/100k.md`](cartera-ai-rock-index-value-todo/100k.md) — Nota: 5,8 / 10
**Tesis para el analista:** Queda **estrictamente dominada** por [`cartera-ai-final-conservadora/100k.md`](cartera-ai-final-conservadora/100k.md). Mantener `30.000 €` cautivos en el roboadvisor `Rock` al `0,41 %` y atomizar el resto en 13 fondos activos introduce sobrecostes, riesgo de duración oculto y sobre-fragmentación (*diworsification*).

- **Debilidades estructurales decisivas:**
  1. **El 60 % del riesgo de tipos de toda la cartera está atrapado dentro de `Rock`:** Los `30.000 €` de Rock contienen `6.600 €` en deuda soberana con **duración media de 10,7 años** (incluyendo `3.000 €` en `Vanguard 20+ Year Euro Treasury`, que perdió −17,03 % en 2026), elevando la duración total de la RF a **2,96 años** (−1.185 € por +100 pb, casi el doble que los −657 € de `final-conservadora`).
  2. **Peaje por beta cara:** Paga `0,41 %` (`123 €/año`) en Rock por una exposición indexada que comprada limpia cuesta `0,06 %–0,12 %` (~105 €/año de sobrecoste perpetuo).
  3. **Atomización en 22 fondos subyacentes (13 manuales + 9 internos de Rock):** Para no superar el 30 % indexado, divide los 56.000 € activos en trece líneas con tickets homeopáticos de `2.000 €` a `3.500 €` (`Ashoka WhiteOak EM` en USD sin historial de 5 años y volatilidad del 23,8 %; `Capital Group New Perspective` al `1,59 %` haciendo de cuasi-índice caro; `Fundsmith` solapando EE. UU. con Rock).

---

### #9. [`cartera-ai-andres/100k.md`](cartera-ai-andres/100k.md) (y [`200k.md`](cartera-ai-andres/200k.md)) — Nota: 4,9 / 10
**Tesis para el analista:** Aunque la filosofía macro que inspira el documento (60/40, el indexado como pieza y un 10–12 % de liquidez táctica en `AXA Trésor Court Terme` al `0,05 %`) es sólida, **la selección concreta de vehículos incumple tres estándares institucionales innegociables: transparencia de costes, historial mínimo de 3 años y eficiencia en renta fija**.

- **Debilidades estructurales decisivas:**
  1. **18 % de la cartera (`18.000 €` en 100k; `32.000 €` en 200k) en fondos sin TER publicado en ficha y con <2 años de vida:**
     - `Kaizen Global Income FI` (`ES0156674006`, `10.000 €` = 10 %): nacido en **mayo de 2025** (<18 meses de vida, cero historial a 3/5 años, cero prueba en el mercado bajista de 2022), sin TER publicado en el MCP y con **9 % de comisión de éxito**, llevando un 43 % de RV interna.
     - `MyInvestor Value C FI` (`ES0165243025`, `8.000 €` = 8 %): clase con <3 años de historial, sin TER publicado en el MCP (~1,45 % real) + **9 % de comisión de éxito**.
  2. **Bloque de renta fija activa dominado (`13.000 €` en Ábaco):**
     - `Ábaco Renta Fija Mixta Global C FI` (`ES0140072028`, `7.000 €`): cobra un **TER del `1,51 %`** con SRRI 4 para rendir +0,73 % en el año; como demuestra la auditoría de [`cartera-ai-c4-defensiva/100k.md` (§7, línea 168)](cartera-ai-c4-defensiva/100k.md#L168), queda estrictamente dominado en rentabilidad, riesgo y coste por alternativas como `Cobas Renta` (`0,33 %`) o `Gamma Global` (`0,86 %`).
     - `Ábaco Renta Fija R FI` (`ES0124526015`, `6.000 €`): cobra `0,96 %` de TER por crédito *high yield* concentrado geográficamente (28,7 % España y 8 % Turquía).
  3. **Opacidad y bloqueo en la talla de 200k:** Mantiene el 30,7 % de «otros» sin desglosar en `Cobas Large Cap` (`11 %` en 100k, `9 %` en 200k) e introduce en 200k `Azvalor Internacional` con una **comisión de reembolso del 3,00 % si se sale o traspasa antes de 12 meses**.

---

## 4. Recomendación ejecutiva según el perfil de mandato

1. **Para un perfil equilibrado-dinámico (~65 % RV) que priorice eficiencia institucional, 0 % comisiones de éxito y máxima diversificación de factores activos:**
   - **Ganadora: [#1 `cartera-ai-hy4-definitiva/100k.md`](cartera-ai-hy4-definitiva/100k.md)** (`0,537 %` TER, Sharpe `1,20`).
   - *Único ajuste recomendado antes de lanzar órdenes:* reducir `Neuberger Short Duration Euro Bond I` del 17 % al 9 % e introducir un 8 % en `DWS Floating Rate Notes LC` (`LU0034353002`, TER `0,25 %`) para evitar concentrar el 17 % de la cartera en un único gestor de crédito corto que sufrió −5,68 % en 2022.
2. **Para ejecutar de inmediato el rebalanceo fiscalmente neutro de [`cartera-actual.md`](../cartera-myinvestor/cartera-actual.md) manteniendo el perfil prudente 55/45:**
   - **Ganadora: [#2 `cartera-ai-final-conservadora/100k.md`](cartera-ai-final-conservadora/100k.md)** (`0,517 %` s/100k, duración `1,61 años`). Sus 22 órdenes de traspaso están listas y cuadradas al euro contra tus saldos reales.
3. **Para un horizonte de 15 años a los 40 años (~72 % RV) que busque máxima desconcentración de EE. UU./megacaps tecnológicas y un escudo anticrisis capaz de ganar dinero en años como 2022:**
   - **Ganadora: [#3 `cartera-ai-neon/110k.md`](cartera-ai-neon/110k.md)** ejecutada en su **variante 0 % comisiones de éxito (`0,77 %` TER con `Palm Harbour` y `B&H Deuda`)**, una vez adaptada la tabla de traspasos de su §6.2 a los saldos reales de [`cartera-actual.md`](../cartera-myinvestor/cartera-actual.md).

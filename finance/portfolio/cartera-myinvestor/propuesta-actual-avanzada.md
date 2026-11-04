---
title: "Cartera avanzada: 55/45 con Rock intacta y diez fondos manuales (97.000 €)"
date: 2026-11-04
type: portfolio-proposal
category: finance
tags: [cartera, avanzada, rock, 55-45, diversificacion, indexados, value, renta-fija, cma, vanguard, jpmorgan, gmo, myinvestor]
status: draft
related:
  - finance/portfolio/cartera-myinvestor/propuesta-actual.md
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
  - finance/portfolio/cartera-myinvestor/propuesta-alternativa.md
---

# Cartera avanzada — 04/11/2026

> **Qué es este documento.** Una cartera construida desde cero sobre el capital real: **Rock se queda
> intacta** (30.000 €, decisión del titular del 04/11) y el bloque manual se dimensiona alrededor de ella.
> La vigente sigue siendo la adoptada; esta es una propuesta distinta que, si el titular la aprueba, la
> sustituye. La versión anterior de este fichero (13 fondos repartiendo 97.000 €, con Baelo y sin Rock)
> queda en el historial de git: **no contaba los 30.000 € de Rock en ningún sitio**, así que o sobraba un
> 44 % del capital o la cartera era un 79,3 % de renta variable. Las dos cosas, a la vez, no.
>
> **Método.** Catálogo MyInvestor (2.410 fondos, 6 tipos de activo, 266 indexados) consultado por fichas
> `get_funds` por ISIN el 04/11/2026 y cribado quirúrgico por bloque con `search_funds`. Previsiones
> externas de Vanguard VCMM, J.P. Morgan LTCMA y GMO (§11). Lo que es estimación propia va marcado.
>
> **No es asesoramiento financiero.** Los pesos son una decisión de cartera sobre fichas verificadas; la
> decisión es del titular.

## 1. Los seis principios que la gobiernan

| Principio | De dónde viene | Cómo se aplica aquí |
| --- | --- | --- |
| **El coste es lo único que se controla** | Andrés, 09:12-13:26 | **463,8 €/año = 0,478 %** todo incluido (§6); cero comisiones de éxito en los diez vehículos |
| **La duración es la decisión, no el activo** | Ábaco 15:55 y 46:15; Renta 4 15:35 | RF manual con duración ~2,3 años; el único bono largo de la cartera (20+ euro, 3.000 €) vive dentro de Rock y se acepta como tal |
| **No pagar expectativas que no se controlan** | Horos (Javier Ruiz), 1:00:41 | ≈29,5 % de la RV en EE. UU. frente al 63 % de un ACWI; cero S&P puro en el bloque manual |
| **Comprar donde la valoración paga** | Andrés 9:36; Vanguard y GMO 2026 (§2) | Europa ≈38 % de la RV, emergentes ≈19 %, Japón ≈5 % |
| **El colchón va fuera de la cartera** | Ackman 34:33 | 10.000 € en Groupama Trésorerie, aparte y sin tocar; aquí 4.000 € de liquidez táctica |
| **Diversificar fuentes de retorno, no solo regiones** | Ackman; CBRE y MSCI (§11) | Cuatro fuentes: beneficio empresarial, cupón, renta de alquiler y crédito |

## 2. La decisión que el titular pidió: cuánta renta variable

**55 % de RV / 45 % de RF (look-through consolidado, Rock dentro).** No es una convención: es lo que dicen
las previsiones y lo que aguanta la aritmética.

### 2.1 Lo que dicen las tres casas

| Casa (fecha) | RV EE. UU. | RV no EE. UU. | RF alta calidad | Comentario |
| --- | ---: | ---: | ---: | --- |
| **Vanguard VCMM** (30/09/2026) | 4,8-6,8 % | desarrollados 5,3-7,3 % · emergentes 3,7-5,7 % | agrego EE. UU. 5,1-6,1 % | Su orden de mejor binomio riesgo-retorno: **1) RF alta calidad, 2) value EE. UU., 3) RV desarrollada no EE. UU.** |
| **J.P. Morgan LTCMA 2027** (19/10/2026) | 7,5 % | global 7,5 % · emergentes 7,1 % | — | Un 60/40 en USD al **7,0 %** a 10-15 años; el 55/45 implícito ≈6,8 % |
| **GMO 7 años** (30/09/2026) | **negativa en términos reales** | deep value internacional +3,0 % real · Japan small value +4,4 % · emergentes −0,7 % | bonos EE. UU. +2,5 % real | El único bloque que bate a los bonos es **value y small cap fuera de EE. UU.** |

### 2.2 La aritmética, con el carry que la RF cobra de verdad

RV con *earnings yield* ponderado 6,65 % (estimación propia y conservadora: los múltiplos que cita este
documento —Europa 13,6x, emergentes 10,2x, S&P 18,7x— darían un 7,4 %). RF con **3,55 % cobrado a 12
meses** por las fichas de los cinco vehículos (1.528 € sobre 43.000 €), no con el 4,55 % de la TIR del
Neuberger:

| RV/RF | Caída tipo 2008 | Retorno (EY solo) | Retorno (EY + crecimiento 4 %) | Vol estimada | 20 años (EY+crec.) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 45/55 | −19,6 % | 5,05 % | 7,29 % | 7,0 % | 4,09x |
| 50/50 | −21,5 % | 5,10 % | 7,60 % | 7,6 % | 4,33x |
| **55/45** | **−23,4 %** | **5,26 %** | **7,91 %** | **7,1 %** | **4,58x** |
| 60/40 | −25,2 % | 5,41 % | 8,21 % | 8,9 % | 4,85x |
| 65/35 | −27,1 % | 5,57 % | 8,52 % | 9,6 % | 5,13x |

Si la RF vuelve a su TIR (4,55 %), el 55/45 sube a **5,7 %**: los 0,45 pp de diferencia son el precio de
medir con lo cobrado y no con lo prometido.

**Por qué 55 y no 65:** el premio de la RV sobre el bono de alta calidad es de **1,5-2,5 pp**, no de 4.
Del 55 al 65 se gana 0,15-0,3 pp y se pierden 2 pp más de caída, con GMO dando retorno real negativo a la
bolsa americana. **Por qué 55 y no 45:** la RF en euros cobra ≈0 % real; con horizonte largo y sin
necesidad de vender, el 45 % ya es mucha renta fija para un activo que no da retorno real.

**Suelo conductual, escrito:** a −23,4 % sobre 97.000 € son **−22.700 €**. Si en ese momento se vende, el
modelo no vale y hay que bajar a 45 %. Un modelo que no se aguanta no sirve.

## 3. La cartera

**Rock no se toca: 30.000 € (78 % RV / 22 % RF, 0,41 % todo incluido, 9 fondos indexados).** El bloque
manual se construye con los 67.000 € restantes (60.000 actuales + 7.000 de aportación nueva) y **baja a
43/57** porque Rock ya aporta 23.400 € de bolsa desde su esquina. Sin ese ajuste el consolidado sería
79/21, no 55/45.

### 3.1 Bloque manual — 10 fondos, 67.000 €

| # | Bloque | Fondo | ISIN | € | % manual | % total | TER |
| --: | --- | --- | --- | --: | --: | --: | --: |
| 1 | RV Europa | iShares Europe Index D Acc | IE00BDRK7L36 | 10.500 | 15,7 % | 10,8 % | 0,10 % |
| 2 | RV value Europa | JPMorgan Europe Strategic Value A Acc | LU0210531983 | 4.500 | 6,7 % | 4,6 % | 1,72 % |
| 3 | RV emergentes | iShares Emerging Markets S Acc | IE000QAZP7L2 | 7.000 | 10,4 % | 7,2 % | 0,16 % |
| 4 | Activos reales | iShares Developed Real Estate D Acc | IE00BDRK7P73 | 3.500 | 5,2 % | 3,6 % | 0,17 % |
| 5 | RV value global | Cobas International P | LU1598719752 | 3.500 | 5,2 % | 3,6 % | 2,33 % |
| 6 | RF corta IG | Neuberger Short Duration Euro Bond U | IE00BL1GVT98 | 18.500 | 27,6 % | 19,1 % | 0,38 % |
| 7 | RF flexible | Cobas Renta | ES0119207001 | 8.000 | 11,9 % | 8,2 % | 0,33 % |
| 8 | RF ABS | Aegon European ABS A Acc | IE00BG226Z29 | 5.000 | 7,5 % | 5,2 % | 0,66 % |
| 9 | Crédito nórdico | Sissener Corporate Bond R EUR | LU2262944817 | 2.500 | 3,7 % | 2,6 % | 0,90 % |
| 10 | Liquidez táctica | AXA Trésor Court Terme C | FR0000447823 | 4.000 | 6,0 % | 4,1 % | 0,05 % |
| | **TOTAL MANUAL** | | | **67.000** | **100 %** | **69,1 %** | **0,509 %** |
| | **Rock** (no se toca) | 9 indexados, 78/22 | — | **30.000** | — | **30,9 %** | **0,41 %** |
| | **TOTAL** | | | **97.000** | | **100 %** | **0,478 %** |

**Reparto por mandato (manual):** RV 29.000 € (43,3 %) · RF 38.000 € (56,7 %).
**Reparto look-through consolidado:** RV **53.558 € = 55,2 %** · RF **43.442 € = 44,8 %**, contando Rock
al 78 % y Cobas Renta por su 14,5 % de bolsa. Con el `alloc_equity` estricto de cada ficha la RV es
53.467 € (55,1 %): las dos convenciones coinciden a 0,1 pp, porque aquí no hay satélites cuyo mandato sea
distinto de su composición.

### 3.2 Rock, dentro de la contabilidad y no en la tabla de descartes

| Fondo | € | Bloque |
| --- | --: | --- |
| Fidelity S&P 500 Index P Acc EUR | 9.900 | RV EE. UU. |
| Goldman Sachs Global Enhanced Index SRI I Cap | 4.200 | RV global |
| Vanguard US Government Bond EUR Hedged | 3.600 | RF EE. UU. cubierta |
| iShares Emerging Markets Index D Acc | 3.300 | RV emergentes |
| Vanguard 20+ Year Euro Treasury | 3.000 | RF euro largo |
| Fidelity MSCI Japan Index P Acc | 2.700 | RV Japón |
| Fidelity MSCI Europe Index P Acc | 2.100 | RV Europa |
| Fidelity MSCI Pacific ex-Japan P Acc USD | 600 | RV Pacífico |
| Vanguard US Equity Index EUR Hedged | 600 | RV EE. UU. |

Rock aporta **23.400 € de RV, el 62 % de toda la renta variable de la cartera**, y 6.600 € de RF. Es la
razón por la que el bloque manual no puede ir al 55 %: eso sería el 79 % consolidado. **Lo que Rock sí
aporta:** 14,1 % de emergentes, 11,5 % de Japón y un bono largo que aquí se acepta como parte fija del
diseño. **Lo que cuesta:** 123 €/año (0,41 %) y no poder tocar sus nueve fondos.

## 4. Por qué cada fondo, con el dato delante

| Fondo | El dato que lo justifica | Qué papel juega | La pega, dicha |
| --- | --- | --- | --- |
| **iShares Europe 0,10 %** | 3A +17,58 % · 5A +9,74 % · vol 10,67 % · 99,2 % RV | Beta barata donde la valoración paga (Europa a 13,6x frente a 18,7x del S&P) | 24,7 % servicios financieros y 21,3 % Reino Unido: no es "Europa limpia" |
| **JPM Europe Strategic Value 1,72 %** | 3A +22,65 % · 5A +14,08 % · vol 3A 10,08 % · 24 años de clase · sin comisión de éxito | El value europeo que la cartera defiende, con historial completo | **43,9 % servicios financieros**: es una apuesta al sector, no "Europa barata" en general |
| **iShares EM 0,16 %** | El más barato de los 27 indexados de emergentes del catálogo | Única forma de estar en el 10,2x de emergentes | 42 % del índice es tecnología (Taiwán, Corea) y ~700 € caen en TSMC; Rock lleva otros 3.300 € en el mismo bloque |
| **REITs 0,17 %** | 3A +10,78 % · 5A +0,63 % · 97,4 % inmobiliario · 2022 −20,1 % | Renta de alquiler: la única fuente de retorno que no da ninguna otra posición | Sector con una década mala; no protege en caídas |
| **Cobas International 2,33 %** | 3A +26,47 % · 5A +17,11 % · vol 12,34 %; cero solape con JPM Europe | Value global con energía y shipping (21,7 % energía) | Soft close: se amplía desde los 1.000 € que ya se tienen, no se abre de cero |
| **Neuberger 0,38 %** | 3A +4,31 % · **1A −0,03 %** · **5A +2,23 %** · vol 1,93 % · 2022 −5,68 % · duración 1,95 · TIR 4,65 % | El amortiguador: cupón con duración corta | **19,1 % de la cartera a una sola idea** y en 12 meses ha cobrado −0,03 % |
| **Cobas Renta 0,33 %** | 3A +8,90 % · 5A +6,79 % · vol 2,93 % · **2022 +3,89 %** · 1A +11,7 % · YTD +10,6 % | **RF flexible** de una casa value: el único vehículo del bloque que ganó en 2022 | 28 % en liquidez (lastre), 41,6 % Alemania, **3,9 % Ghana** y 14,5 % de renta variable que aquí se cuenta |
| **Aegon ABS 0,66 %** | 3A +4,38 % · 1A +2,39 % · vol 3A 0,95 % (5A 1,90 %) · 98,6 % titulización | Diversifica el riesgo de crédito fuera del corporativo | 2022 −4,0 % y 5A +2,94 %: cede 1,81 pp frente a un soberano A+ |
| **Sissener 0,90 %** | 3A +6,82 % · 5A +5,53 % · 1A +5,06 % · vol 2,05 % · 2022 +0,19 % | Crédito nórdico: **el mejor vehículo de renta fija de la cartera en las tres ventanas** | 58 % Noruega/Suecia, gestora pequeña y solo 2,6 % de la cartera |
| **AXA Trésor 0,05 %** | 3A +2,95 % · 1A +2,25 % · vol 3A 0,24 % · €STR | Liquidez para rebalancear sin vender RV | Rinde €STR: no es inversión, es munición |

## 5. La renta fija, sin etiquetas

**No hay bloque mixto.** La regla de la casa adoptada el 02/11 —*cada euro es RV o RF*— sigue en pie, y
Cobas Renta entra como **RF flexible contabilizada**: el 14,5 % de su dinero se suma a la renta variable y
el resto a deuda. No es un fondo malo por ser multiactivo; es un fondo malo cuando alguien lo usa para no
contar la bolsa que lleva dentro.

**Por qué cobra menos de lo que promete.** La TIR del bloque se publicó como 4,55 %, que es la del
Neuberger (19,1 % de la cartera). Lo cobrado a 12 meses por los cinco vehículos es **3,55 %**: Neuberger
−0,03 %, Aegon +2,39 %, Sissener +5,06 %, Cobas Renta +11,72 %, AXA +2,25 %. Sobre una inflación del
3,8 % son **−0,25 % real**. La renta fija de esta cartera no está para ganar dinero: está para que el
−23,4 % no se convierta en −40 % y el titular no venda.

**Lo que se probó y no entró** (cribado del 04/11, fichas verificadas):

| Candidato | Ficha | Por qué no |
| --- | --- | --- |
| Vanguard Global Short-Term Corp Bond USD Hedged (IE00BDFB7308) | 0,18 % · 3A **+5,47 %** · 5A +2,68 % · vol 2,32 % | Bate al Neuberger en 3A/5A, pero la clase es **USD** (divisa sin cubrir a EUR para el partícipe) y su 2022 fue **−5,99 %**, peor que el −5,68 % del Neuberger |
| Storm Bond Fund RC EUR (LU0840158819) | 1,06 % + **10 % de éxito** · 3A +5,76 % · 5A +6,04 % · 2022 +5,19 % · vol 1,09 % | Bate al Sissener en 5A y al Aegon en todo, pero es **alto rendimiento nórdico (Noruega 52 %)**: duplicaría el crédito nórdico en vez de diversificar el ABS |
| Lazard Euro Short Duration SRI (FR0013506995) | 0,04 % de TER pero **20 % de éxito** · −15,7 % de liquidez | Apalancado y con comisión de éxito |
| iShares Global Aggregate 1-5Y EUR H (IE0004ZP1ND3) | 0,08 % · 1A **+0,37 %** | La cobertura de divisa se come el cupón; sin historial a 3 años |
| iShares € IG Corporate (IE00BDRK7J14) | 0,12 % · 3A +4,17 % · 5A **+0,13 %** · 2022 **−13,26 %** | Es el TER mínimo en corporativo euro, pero su duración ~5 le costó 13 pp en 2022 |

**Conclusión del cribado:** los cinco vehículos de renta fija se quedan. Nada del catálogo los domina en su
propia función, y los que baten en rentabilidad son otra cosa (divisa, catástrofe o crédito basura).

## 6. Métricas

| Métrica | Valor | Cómo se obtiene |
| --- | ---: | --- |
| Renta variable (look-through) | **55,2 %** (estricto: 55,1 %) | 53.558 € de 97.000; 53.467 € con el `alloc_equity` de cada ficha |
| Renta fija (look-through) | **44,8 %** | 43.442 € |
| TER manual | **340,8 €/año (0,509 %)** | Σ importe × TER de ficha sobre 67.000 € |
| TER Rock | **123,0 €/año (0,41 %)** | 30.000 € × 0,41 % (TER + custodia + gestión) |
| **Coste total** | **463,8 €/año (0,478 %)** | Suma de los dos |
| Comisiones de éxito | **0 €/año** | Ninguno de los diez vehículos las cobra |
| Duración estimada de la RF manual | **≈2,3 años** (inferida) | Neuberger 1,95 · Aegon ~1 · Sissener ~2 · Renta ~3 · AXA ~0 |
| Volatilidad estimada | **≈7,1 %** | RV 12,5 % · RF 2,5 % · correlación 0,1 |
| Caída tipo 2008 (RV −40 %, RF −3 %) | **−23,4 %** | −22.700 € |
| Retorno esperado | **5,3 % nominal** (EY + RF cobrada) · **5,7 %** si la RF vuelve a 4,55 % | §2.2 |
| Real sobre inflación 3,8 % | **+1,5 %** · **+1,9 %** | Retorno − inflación |
| Posiciones | **10 manuales + Rock** | 5 de RV + 5 de RF en el bloque manual |

## 7. Diversificación

### 7.1 Geografía de la RV (look-through, estimación declarada)

| Región | % de la RV | % de la cartera |
| --- | ---: | ---: |
| Europa | ≈38 % | ≈20,9 % |
| **Estados Unidos** | **≈29,5 %** | **≈16,3 %** |
| Emergentes | ≈19,2 % | ≈10,6 % |
| Japón | ≈5,0 % | ≈2,8 % |
| Otros y sin desglosar | ≈8,4 % | ≈4,6 % |

Frente a un MSCI ACWI (63 % EE. UU.), esta cartera lleva **≈33 pp menos de EE. UU.**, y la mitad de esa
diferencia la produce Rock. Es menos extremo de lo que decía la versión anterior («13 % de EE. UU.»),
porque aquel número solo era cierto vendiendo Rock.

### 7.2 Concentraciones que se dicen en voz alta

- **Servicios financieros:** el 43,9 % de JPM Europe Strategic Value son **1.976 €**, el 8,5 % de la RV.
  Es el precio de haber comprado value con historial.
- **Tecnología:** ≈11 % de la RV, casi toda por dentro de Rock (S&P 500 y World al ~31 % de tecnología,
  ficha de iShares Developed World) y del índice de emergentes (42 %).
- **Inmobiliario:** 3.500 € de REITs (6,5 % de la RV) más lo que llevan dentro los value, que no se
  publica: el sector queda en una banda del 7-13 % y no se puede cerrar más.
- **Gestoras del bloque manual:** BlackRock 21.000 € (**21,6 %**), Neuberger 18.500 (19,1 %), Cobas
  11.500 (11,9 %), Aegon 5.000 (5,2 %), JPMorgan 4.500 (4,6 %), AXA 4.000 (4,1 %), Sissener 2.500 (2,6 %).
  Rock añade Fidelity ≈15.300 €, Vanguard ≈7.200 €, BlackRock 3.300 € y Goldman 4.200 €.

### 7.3 Divisas sin cubrir

EUR ≈70 %, USD ≈20 % (casi todo por Rock y por los fondos globales), resto en libras, corona y emergentes.
La exposición al dólar es deliberada y menor que la de un indexado global; el bloque manual, además, no
compra EE. UU. directamente.

## 8. Lo que se descarta, con el número delante

| Descartado | Por qué, en euros o en pp |
| --- | --- |
| **Baelo Patrimonio** (0,64 %) | **2022: −8,3 %**. Se propuso como "amortiguador del bloque de RV" y en el único año de estrés disponible perdió más que el papel que decía cubrir. Es 62,3 % RV, 20 % EE. UU., 12,4 % tecnología y 32 % Alemania: ni defensivo ni "europeo de hecho". Sus 5.000 € se replican con 3.115 € de iShares Europe y 1.785 € de Neuberger por **22 €/año menos** |
| **Vanguard Global Small-Cap** (0,29 %) | Con 29.000 € de RV manual no caben cuatro bloques geográficos y dos factores: 60,9 % EE. UU. y 4.500 € que subían el sesgo americano. Vuelve si el manual pasa de 40.000 € de RV |
| **Fidelity MSCI Japan** (0,10 %) | Rock ya lleva 2.700 € en **el mismo índice** (IE00BYX5N771). Comprarlo aparte duplica la posición, no diversifica |
| **MSCI World / ACWI indexado** | Existe al **0,06 %** (iShares Developed World IE000ZYRH0Q7, 72 % EE. UU., 30,8 % tecnología). Sería más barato que el iShares Europe al 0,10 % y dejaría 45.000 € en el activo con peor previsión de las tres casas |
| **Horos Value Internacional** (1,90 %) | 3A +16,98 % y 5A +11,92 %: pierde las dos ventanas contra Cobas International (26,47 y 17,11) |
| **Fundsmith y Comgest** (calidad) | Fundsmith: 5A +2,73 % y 79,6 % EE. UU. · Comgest: 5A −0,96 %. Comprar calidad americana a 35-40x es lo que Vanguard y GMO señalan como el activo caro |
| **Cat bonds** (Twelve 1,28 %, 3A +9,30 %; GAM 1,41 % + 10 % de éxito) | Lideran el ranking de crédito, pero son otro activo (riesgo de catástrofe) y el reembolso tarda 10 días |
| **Oro** (fondo 1,61-1,66 %; ETF 0,19 %) | El fondo es caro y volátil; el ETF lleva +67,8 % solo en 2025. Se compra diversificación, no un pico |
| **Bonos largos y ligados a inflación euro** | El 20+ europeo hizo −17,03 % en 2026; los ligados dan 0,3-0,5 % real frente al 2,5 % real del bono americano (GMO) |
| **Subir al 65 % de RV** | +0,15 pp de retorno por +2 pp de caída, y con Rock dentro eso exigiría dejar el bloque manual casi sin renta fija |

## 9. Riesgos y límites

- **Rock pesa el 62 % de la renta variable y no se puede tocar.** La cartera no es un 55/45 "de diseño
  propio": la mitad de su bolsa viene de una cartera automatizada con 57 % de EE. UU. Si MyInvestor cambia
  los pesos de Rock, esta cartera cambia sin que nadie la edite.
- **El 55/45 es una decisión, no un dato.** Cambia si cambian las previsiones; si Vanguard y GMO revisan al
  alza la bolsa americana, el 55 deja de estar justificado.
- **La cartera es europea de más (≈38 % de la RV)** y muy poco americana para lo que hace el mundo. Si
  Europa sigue barata cinco años más, se verá mal antes de verse bien.
- **Cobas Renta y Cobas International son dos fondos de la misma casa (11,9 % del manual)** y su
  comportamiento depende de sus gestores.
- **La duración de la RF es inferida.** Solo el Neuberger publica la suya (1,95); Aegon, Sissener y Cobas
  Renta no la dan. El ≈2,3 años es una estimación por familia de activo.
- **Comisiones de entrada desconocidas** en Aegon, Sissener, REITs y Cobas Renta. El Neuberger declara
  «hasta 3 %», pero aquí no se compra: incluso se reduce.
- **Riesgo divisa:** ≈20 % en dólares sin cubrir, la mayor parte dentro de Rock.
- **TSMC:** Taiwán pesa el 27 % del índice de emergentes; entre el fondo manual y Rock son ≈1.850 €.
- **El colchón de 10.000 € sigue sin dimensionar** contra gastos reales; si hay que ampliarlo, sale de esta
  cartera.

## 10. Cuándo se revisa

| Señal | Umbral | Efecto |
| --- | --- | --- |
| Prima de la RV | *Earnings yield* − carry de la RF < 1 pp | Bajar a 45 % de RV |
| **Carry cobrado** | RF cobrada a 12 meses < 2 % (hoy: 3,55 %) | Revisar el bloque entero: es la señal más cerca de dispararse |
| Valoración | S&P −20 % con beneficios intactos | Subir a 60-65 % de RV |
| Crédito | HY OAS > 700 pb | Salir de Sissener y Aegon; volver al monetario |
| Europa | Cinco años más de comportamiento relativo negativo con beneficios intactos | Revisar el ≈38 %: es una tesis, no un dogma |
| Rock | Cambio de composición o de comisión por MyInvestor | Recalcular el look-through y el 55/45 entero |
| Coste | TER > 0,50 % | Barrido del catálogo otra vez |

Trimestral, y además cuando se cumpla cualquiera de las señales. **No se rebalancea por bandas**: se
rebalancea cuando una señal lo dice o cuando un bloque se desvía más de 5 pp.

## 11. Fuentes

- **Fichas MyInvestor MCP, 04/11/2026**, verificadas por ISIN con `get_funds`: iShares Europe
  (IE00BDRK7L36), JPM Europe Strategic Value (LU0210531983), iShares EM (IE000QAZP7L2), REITs
  (IE00BDRK7P73), Cobas International (LU1598719752), Neuberger (IE00BL1GVT98), Cobas Renta
  (ES0119207001), Aegon (IE00BG226Z29), Sissener (LU2262944817), AXA Trésor (FR0000447823). Catálogo por
  `list_facets` (2.410 fondos, 6 tipos de activo, 266 indexados) y `search_funds` por bloque.
  **Límite declarado:** el MCP devolvió `usage limit reached` a mitad de los cribados de mixtos y de renta
  variable, y sus términos prohíben el uso masivo. **No se ha barrido el catálogo entero**; los bloques de
  renta fija y los indexados globales sí quedaron cerrados con fichas.
- **Vanguard**, *Capital Markets Model forecasts* (30/09/2026) y *2026 Economic and Market Outlook*
  (10/12/2025) — orden de binomio riesgo-retorno: RF alta calidad, value EE. UU., RV desarrollada no EE. UU.
- **J.P. Morgan Asset Management**, *2027 Long-Term Capital Market Assumptions* (19/10/2026): ACWI 7,5 %;
  60/40 al 7,0 % a 10-15 años.
- **GMO**, *7-Year Asset Class Real Return Forecasts* (30/09/2026): EE. UU. large negativa en real, deep
  value internacional +3,0 %, Japan small value +4,4 %, bonos EE. UU. +2,5 % real.
- **Transcripciones del repositorio:** La Pizarra de Andrés (coste, S&P no neutral), Ábaco y Renta 4
  (duración), Horos (30/10/2026), Ackman 2012, webinars MyInvestor. Rutas en `INDEX.md`.

## 12. Auditoría de independencia (04/11/2026, segunda pasada)

**El defecto de la versión anterior.** Repartía 97.000 € entre 13 fondos **como si Rock no existiera**.
Rock aparecía una sola vez, en la tabla de descartes, y su 78 % de renta variable no entraba en ningún
look-through: si se mantenía, la cartera era un **79,3 % de RV**, no un 55/45. Se corregía el síntoma
(trece fondos nuevos) y se dejaba intacta la causa (una cartera automatizada que pesa el 31 % del capital).
Además atribuía al titular una petición que no existía («pidió expresamente incluir mixtos»), reabría una
vía que él había rechazado el 03/11 —Cobas Renta + Baelo, 524 €/año— y publicaba el 2022 de Cobas Renta
sin publicar el **−8,3 % de Baelo**, que es el que desmiente el argumento.

**Cribado por rol** (04/11/2026, fichas verificadas una a una):

| Rol | Qué devuelve el cribado | Veredicto |
| --- | --- | --- |
| **RF corta, SRRI ≤2** | Vanguard Global Short-Term Corp **USD** Hedged 0,18 % (3A +5,47 %, 2022 −5,99 %) · Lazard 0,04 % **con 20 % de éxito** · iShares Global Agg 1-5Y EUR H 0,08 % (1A +0,37 %, sin 3A) · Vanguard UK en libras | **Se queda el Neuberger**: los tres más baratos fallan por divisa, por comisión de éxito o por falta de historial |
| **Crédito flexible / ABS** | Storm Bond RC 1,06 % + 10 % de éxito (3A +5,76 %, 5A +6,04 %, 2022 +5,19 %, **Noruega 52 %**) · Pareto Nordic 1,10 % (3A +6,10 %) · Twelve Capital cat bonds 1,28 % (3A +9,30 %) | **Se quedan Aegon y Sissener**: Storm bate al Sissener en 5A pero duplica el mismo riesgo nórdico; los cat bonds son otro activo |
| **Monetario por TER** | AXA Trésor 0,05 % (1A +2,25 %) · Ofi Invest 0,06 % (1A +2,23 %) · Groupama 0,07 % (1A +2,23 %) | **Entra AXA**: gana por 1-2 pb y es la clase que ya se usa |
| **Indexado global por TER** | iShares Developed World S Acc EUR **0,06 %** (IE000ZYRH0Q7) | **No entra**: 72 % EE. UU. Es el precio de la alternativa que este documento descarta, no un hueco |
| **Mixtos** | Cribado incompleto (límite del MCP). Lo verificado: Hamco Global Value, 91,4 % RV, mínimo 100.000 € | **Ninguno entra como bloque**: Cobas Renta va como RF flexible y su bolsa se cuenta |

**Qué cambia frente a la versión anterior:** Rock entra en el cuerpo y en el look-through; Baelo sale; small
cap y Japón salen (Rock ya los cubre o no caben); el bloque manual baja a 43/57; el coste baja de 538,2 € a
**463,8 €** (−74,4 €/año, y el mérito es de Rock, no del diseño); el carry se publica cobrado (3,55 %) y no
prometido (4,55 %). **Qué no cambia:** los cinco vehículos de renta fija, que es la parte del documento que
el cribado confirma entera.

> Estimaciones propias declaradas: volatilidad de la cartera, duración media de la RF, drawdown, retorno
> esperado, geografía y sectores look-through, reparto de Rock por región. Las cifras de ficha son de ficha;
> las de las casas externas, de sus informes. Nadie garantiza ninguna de las dos cosas, y este documento no
> es asesoramiento financiero: la decisión es del titular.

## 13. Hoja de órdenes: del estado actual a esta cartera

**Base:** 67.000 € manuales = 60.000 € invertibles de hoy + 7.000 € de aportación nueva. Los 10.000 € del
colchón (Groupama Trésorerie) **no se tocan** y quedan fuera de la cartera. Todo se ejecuta por **traspaso
entre fondos armonizados: 0 € de impuestos**. La aportación nueva entra como suscripción.

### 13.1 Qué sale y a dónde va

| Origen | ISIN | Saldo hoy | Sale | Se queda | Adónde va |
| --- | --- | --: | --: | --: | --- |
| Gamma Global A | ES0140794001 | 8.000 | **8.000** | 0 | Cobas Renta 8.000 |
| Carmignac Portfolio Credit A | LU1623762843 | 12.000 | **12.000** | 0 | Aegon 5.000 · Sissener 2.500 · AXA 4.000 · REITs 500 |
| DNCA Invest Alpha Bonds A | LU1694789451 | 13.000 | **13.000** | 0 | iShares Europe 10.500 · EM 2.500 |
| Neuberger Short Duration U | IE00BL1GVT98 | 22.000 | **3.500** (parcial) | 18.500 | EM 3.500 |
| MyInvestor Value C | ES0165243025 | 2.000 | **2.000** | 0 | REITs 2.000 |
| NB Next Gen Space Economy | IE00018YKVN0 | 1.000 | **1.000** | 0 | REITs 1.000 |
| UBS MSCI China All Shares | LU1815002040 | 1.000 | **1.000** | 0 | EM 1.000 |
| Cobas International P | LU1598719752 | 1.000 | — | 1.000 | (se amplía con aportación nueva) |
| | | **60.000** | **40.500** | **19.500** | + 7.000 nuevos = **47.500 a invertir** |

### 13.2 Qué se compra

| Destino | ISIN | Ya tienes | Compra | Total | % del manual | TER |
| --- | --- | --: | --: | --: | --: | --: |
| iShares Europe Index D Acc | IE00BDRK7L36 | 0 | 10.500 | 10.500 | 15,7 % | 0,10 % |
| JPMorgan Europe Strategic Value A Acc | LU0210531983 | 0 | 4.500 | 4.500 | 6,7 % | 1,72 % |
| iShares Emerging Markets S Acc | IE000QAZP7L2 | 0 | 7.000 | 7.000 | 10,4 % | 0,16 % |
| iShares Developed Real Estate D Acc | IE00BDRK7P73 | 0 | 3.500 | 3.500 | 5,2 % | 0,17 % |
| Cobas International P | LU1598719752 | 1.000 | 2.500 | 3.500 | 5,2 % | 2,33 % |
| Cobas Renta | ES0119207001 | 0 | 8.000 | 8.000 | 11,9 % | 0,33 % |
| Aegon European ABS A Acc | IE00BG226Z29 | 0 | 5.000 | 5.000 | 7,5 % | 0,66 % |
| Sissener Corporate Bond R EUR | LU2262944817 | 0 | 2.500 | 2.500 | 3,7 % | 0,90 % |
| AXA Trésor Court Terme C | FR0000447823 | 0 | 4.000 | 4.000 | 6,0 % | 0,05 % |
| Neuberger Short Duration U | IE00BL1GVT98 | 22.000 | −3.500 | 18.500 | 27,6 % | 0,38 % |
| | | **23.000** | **47.500** | **67.000** | **100 %** | |

### 13.3 Las trece operaciones, en el orden de la plataforma

| # | Origen | ISIN origen | € | Destino | ISIN destino |
| --: | --- | --- | --: | --- | --- |
| 1 | Gamma Global A | ES0140794001 | 8.000 | Cobas Renta | ES0119207001 |
| 2 | Carmignac Portfolio Credit A | LU1623762843 | 5.000 | Aegon European ABS A Acc | IE00BG226Z29 |
| 3 | Carmignac Portfolio Credit A | LU1623762843 | 2.500 | Sissener Corporate Bond R EUR | LU2262944817 |
| 4 | Carmignac Portfolio Credit A | LU1623762843 | 4.000 | AXA Trésor Court Terme C | FR0000447823 |
| 5 | Carmignac Portfolio Credit A | LU1623762843 | 500 | iShares Developed Real Estate | IE00BDRK7P73 |
| 6 | DNCA Invest Alpha Bonds A | LU1694789451 | 10.500 | iShares Europe Index D Acc | IE00BDRK7L36 |
| 7 | DNCA Invest Alpha Bonds A | LU1694789451 | 2.500 | iShares Emerging Markets S Acc | IE000QAZP7L2 |
| 8 | Neuberger Short Duration U | IE00BL1GVT98 | 3.500 | iShares Emerging Markets S Acc | IE000QAZP7L2 |
| 9 | UBS MSCI China All Shares | LU1815002040 | 1.000 | iShares Emerging Markets S Acc | IE000QAZP7L2 |
| 10 | MyInvestor Value C | ES0165243025 | 2.000 | iShares Developed Real Estate | IE00BDRK7P73 |
| 11 | NB Next Gen Space Economy | IE00018YKVN0 | 1.000 | iShares Developed Real Estate | IE00BDRK7P73 |
| 12 | *Aportación nueva* | — | 4.500 | JPMorgan Europe Strategic Value | LU0210531983 |
| 13 | *Aportación nueva* | — | 2.500 | Cobas International P | LU1598719752 |

**11 traspasos + 2 suscripciones.** Cuadre: Σ sale = 40.500 € · Σ aportación = 7.000 € · Σ compra =
47.500 € · saldos finales = 67.000 €.

### 13.4 Calendario por tandas

| Tanda | Cuándo | Órdenes | Qué se corta |
| --- | --- | --- | --- |
| **1** | Día 1 | 1-5 (Gamma y Carmignac) | **Primero el crédito peor pagado**: Gamma es 81 % high yield de energía y shipping; Carmignac es BBB− con duración 4 y 20 % de comisión de éxito. Entran 8.000 € a RF flexible y 12.000 € a ABS, nórdico y liquidez |
| **2** | Día 1-2 | 6-11 (DNCA, Neuberger parcial, Value, Space, China) | La renta variable vieja y el exceso de corto: 15.500 € a Europa y emergentes, 3.500 € a REITs |
| **3** | Día 2 | 12-13 (aportación nueva) | Los 7.000 € nuevos a value europeo y a ampliar Cobas |

- Un traspaso tarda 2-4 días en acreditarse y **no hace falta tener efectivo en ningún momento**.
- Las órdenes 12 y 13 son suscripciones con dinero nuevo: pueden lanzarse en paralelo a la tanda 1.
- **Corte:** la mayoría de estos fondos cortan a las 12:00-14:00; una orden lanzada después entra con el
  valor liquidativo del día siguiente.

### 13.5 Comprobaciones antes de teclear

| Comprobación | Estado |
| --- | --- |
| ISIN y clase de los 10 fondos en el catálogo MyInvestor | ✅ verificado por `get_funds` el 04/11 |
| Todas las clases son de **acumulación** (`distributing = 0`) | ✅ verificado en ficha |
| Comisión de éxito | ✅ ninguno de los 10 la cobra |
| Reembolso de DNCA, Carmignac, Gamma, UBS China y Space | ✅ 0,00 % verificado el 31/10 |
| **Reembolso de MyInvestor Value C** | ❓ verificar en pantalla antes de la orden 10 |
| Comisión de entrada de Aegon, Sissener, REITs y Cobas Renta | ❓ verificar en pantalla antes de las órdenes 1-5 |
| Ampliación de Cobas International estando en soft close | ⚠️ el titular ya es partícipe (1.000 €); si la plataforma rechaza la suscripción, la orden 13 y la 6 se juntan: DNCA → Cobas 2.500 y DNCA → Europe 8.000 |
| Mínimos: Cobas Renta 100 €, resto ≤ 1 € | ✅ cumplen todas las órdenes |

## 14. Lo que sigue sin decidir

1. **Rock: 30.000 € y sus nueve fondos no se tocan** (decidido el 04/11). Si algún día se quiere bajar su
   78 % de RV, se pide otro perfil a MyInvestor; no se vende desde aquí.
2. **El 55/45 consolidado** es la decisión de este documento. Si el titular prefiere que el 55/45 sea del
   bloque manual (y el consolidado quede en 62/38), cambian el §3 entero y todas las órdenes.
3. **Gastos mensuales:** el colchón de 10.000 € sigue sin dimensionar contra un dato real.
4. **Cobas International en soft close:** confirmar que admite la ampliación de 2.500 €.
5. **Comisiones de entrada** de Aegon, Sissener, REITs y Cobas Renta: si alguna supera el 1 %, esa pata se
   financia desde AXA y no desde Carmignac.
6. **Hay otro anexo vivo en la carpeta** (`propuesta-perplexity.md`, 100.000 € con 45/40/15). Dos carteras
   paralelas acaban siendo dos verdades: antes de ejecutar nada hay que quedarse con una y borrar la otra.

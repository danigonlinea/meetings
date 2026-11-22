---
title: "cartera-ai-fondos-2000-lista-deepseek"
date: 2026-11-20
type: reference
category: finance
tags: [cartera, fondos, myinvestor, cartera-ai-fondos-2000-lista-deepseek, cartera-ai, diversificacion]
status: living
---

# cartera-ai-fondos-2000-lista-deepseek

Cinco carteras **independientes de 100.000 € cada una**, construidas solo con fondos del listado
`finance/fondos-myinvestor/` (2.007 fichas). **Ningún fondo se repite entre las cinco**: 37 líneas,
37 ISIN distintos, comprobados por código también por nombre normalizado y por clase hermana
([`validacion.md`](validacion.md)). No se suman, no se comparan entre sí y no se rebalancea una contra otra.

| Cartera | Criterio | Fondos | RV real | Coste anual | Com. de éxito | Caída de manual |
| --- | --- | --: | --: | --: | --: | --: |
| [`C1-indice-coste-minimo.md`](C1-indice-coste-minimo.md) | solo gestión indexada, la clase operable más barata de cada índice | 8 | 69,47 % | 129,20 € (0,1292 %) | 0 de 8 | −28,68 % |
| [`C2-conviccion-activa.md`](C2-conviccion-activa.md) | ningún indexado: cada línea es un proceso de gestión con evidencia en la ficha | 8 | 97,60 % | 1.434,40 € (1,4344 %) | 2 de 8 | −39,04 % |
| [`C3-equilibrada-credito-activo.md`](C3-equilibrada-credito-activo.md) | 55 % de RV indexada y 45 % en cinco fondos de crédito con gestión activa | 7 | 55,05 % | 492,90 € (0,4929 %) | 1 de 7 | −23,28 % |
| [`C4-defensiva-alternativos.md`](C4-defensiva-alternativos.md) | 34 % de RV real y tres alternativos descorrelacionados, con colchón de deuda pública | 8 | 34,06 % | 607,60 € (0,6076 %) | 4 de 8 | −15,07 % |
| ⚠️ **ganadora** — [`C5-crecimiento-satelites.md`](C5-crecimiento-satelites.md) | cerca del 100 % de RV: núcleo global all-cap barato y cinco satélites con nombre y apellidos | 6 | 99,48 % | 764,60 € (0,7646 %) | 1 de 6 | −39,79 % |

⚠️ **La ganadora es C5** (`C5-crecimiento-satelites.md`, `status: final`): elegida el 20/11/2026 con
horizonte de 15 años y 1.500 €/mes, **pendiente de la revisión del titular y sin órdenes lanzadas**.

Las cinco cubren el espectro completo de riesgo (15 % → 40 % de caída de manual) **sin compartir un
solo fondo**. Y el orden de coste no sigue el orden de riesgo: la cartera más agresiva (C5, 99,48 % de RV)
cuesta la mitad que la cartera de convicción (C2, 97,60 % de RV), porque el 60 % de su dinero está en un
índice al 0,20 %. La defensiva (C4, 607,60 €) cuesta más que la equilibrada (C3, 492,90 €) aunque tiene
menos bolsa, porque cuatro de sus ocho líneas llevan comisión de éxito.

## Mandato

- **Universo:** las 2.007 fichas de `finance/fondos-myinvestor/` (1.980 del listado de la app, 27 del
  MCP y clases hermanas). No hay ETF ni acciones: solo fondos de inversión traspasables.
- **La condición del titular:** entre estas cinco carteras **ningún fondo repetido**. La unicidad es
  interna al encargo: **no se heredó ninguna lista negra** de las carteras anteriores del repositorio.
- **Lista de nombres del titular:** los trece fondos de su captura se evalúan uno a uno más abajo; diez
  entran (uno de ellos como sustituto del mismo equipo) y tres se descartan con el número que los descarta.
- **Solamente clases de acumulación**, por la regla vigente en `finance/portfolio/README.md` §Reglas.
  Los 37 ISIN tienen `distributing: 0` verificado en el MCP el 20/11/2026. El caso que se cae por esta
  regla es el M&G Emerging Markets Bond, que solo existe en clase de reparto.
- **100.000 € por cartera exactos**, en fondos traspasables. Mínimos iniciales, TER, comisiones de éxito
  y avisos verificados en el MCP del 20/11/2026; cada primera orden despeja su mínimo.
- La rentabilidad esperada **no se publica como promesa**: cada documento da el coste verificado, la RV
  real por *look-through* y la caída del escenario de la casa. La decisión y la ejecución son del titular.
  **Ninguna de las cinco está ejecutada.**

## Los trece fondos del listado, uno a uno

Los que el titular puso sobre la mesa, en el orden en que los puso.

| # | Fondo del listado | Qué es en el catálogo | Decisión |
| --: | --- | --- | --- |
| 1 | **Jupiter Merian GEAR** | `IE00BLP5S460` — market neutral, TER 1,55 % + 20 % de éxito | **Entra en C4 al 8 %.** Cinco años naturales positivos seguidos, volatilidad 3A 3,9 %, beta 0,09. Es el único alternativo del catálogo con ese historial. Se paga caro y se dice. |
| 2 | **Merchbanc RF Flexible** | `LU2222028099` — renta fija flexible euro, TER 1,23 % (MCP, no 1,19 %) | **Entra en C3 al 10 %.** 3A +4,4 %, 84 % corporativos, sin restricción de duración. |
| 3 | **Pareto Nordic Cross Credit** | `LU2200514128` — crédito nórdico IG/HY, TER 0,84 % (MCP, no 0,70 %) | **Entra en C3 al 12 %.** Duración de tipos 0,4 años, YTM 3,6 %, top 10 emisores 13,7 %. El mejor carry/volatilidad del bloque. |
| 4 | **Storm Bond** | `LU0840158819` — high yield nórdico, TER 1,06 % + 10 % de éxito | **Entra en C3 al 8 %.** 3A +5,6 % con volatilidad 3A de 1,13 %. |
| 5 | **Cartesio X** | `ES0116567035` — mixto 9 % RV, TER 0,63 % + 7,5 % de éxito | **Entra en C4 al 12 %.** 3A +7,5 % y 2022 de −2,9 %. Mínimo 6.000 €, el más alto de las cinco carteras. |
| 6 | **Algebris Financial Credit** | no está. El catálogo tiene Algebris Global Credit Opportunities R (`IE00BYT35X57`) y Algebris Financial Equity I (`IE00BWY57036`) | **Fuera las dos.** La de crédito: TER 1,60 % + 15 %, mínimo 10.000 €, YTD −2,16 %, ficha genérica que no sostiene la compra. La de renta variable de financieras: 3A +28,6 % con TER 0,91 %, pero mínimo 500.000 € — no es comprable. |
| 7 | **Dunas Valor Equilibrado** | `ES0175414012` — retorno absoluto, 6,4 % RV, TER 1,19 % + 11 % de éxito | **Entra en C4 al 12 %.** 3A +4,7 % con volatilidad 3A 2,05 %; puede ponerse corto de bolsa, cosa que ninguna otra línea hace. |
| 8 | **Sissener Canopus** | no está. El catálogo tiene Sissener Corporate Bond R (`LU2262944817`) | **Entra el sustituto en C4 al 12 %.** Mismo equipo, política de crédito corporativo: 3A +6,7 %, volatilidad 3A 2,06 %. |
| 9 | **Ábaco RF Mixta Global** | `ES0140072028` — mixto 22 % RV, TER 1,51 % | **Fuera.** SRRI 4 con 22 % de RV y 3A +4,01 %: Dunas da 3A +4,68 % con 6,4 % de RV y SRRI 2. Dominado en las tres columnas. |
| 10 | **M&G EM Bond** | `LU1670631107` — solo clase **de reparto** (A EUR Inc) | **Fuera.** La clase de acumulación no está en la plataforma y la casa compra acumulación. Además duración 6,08 años y BBB− medio, que es riesgo de tipos donde el diseño pide carry. |
| 11 | **T. Rowe US Smaller** | `LU0918140210` — small cap USA, TER 1,72 %, mínimo 3.000 € | **Entra en C5 al 8 %.** 3A +11,5 %, 1A +26,3 %. Su 5A de +4,2 % va en la pega. |
| 12 | **Capital Group New Perspective** | `LU1295551144` — global growth, TER 1,59 % | **Entra en C2 al 18 %.** La ficha del repositorio traía la política como «pendiente»; el MCP confirma acumulación. |
| 13 | **Robeco QI EM** | `LU0329355670` — emergente cuantitativo, TER 1,52 % | **Entra en C2 al 12 %.** 3A +18,9 % y 5A +10,1 % frente a +5,9 % del índice a cinco años. |

**Diez de trece entran.** Los tres que no: uno no existe en el catálogo en su versión de crédito
(Algebris Financial Credit; el Sissener Canopus tampoco existe y entra su sustituto del mismo equipo, que
cuenta como usado), otro solo existe en clase de reparto (M&G EM Bond) y el tercero está dominado por otro
fondo del propio listado (Ábaco).

## Solape con las carteras hermanas

El mandato solo prohíbe la repetición **dentro** de estas cinco, así que se cruzó igualmente contra las
dos carpetas hermanas del mismo encargo para publicarlo en lugar de esconderlo:

| ISIN | Fondo | Aquí | En la hermana |
| --- | --- | --- | --- |
| `LU0329355670` | Robeco QI EM Active | C2 (12 %) | `cartera-ai-fondos-2000-lista` C2 y `-glm` C2 |
| `IE00BLP5S460` | Jupiter Merian GEAR | C4 (8 %) | `cartera-ai-fondos-2000-lista` C4 |
| `IE00BD2B9710` | Twelve Capital Cat Bond | C4 (6 %) | `cartera-ai-fondos-2000-lista` C4 |
| `IE00BYSJTY39` | First Sentier Global Listed Infrastructure | C5 (8 %) | `-glm` C4 |
| `IE00BD0NC144` | iShares Euro Gov Inflation-Linked Bond | C1 (8 %) | `-glm` C3 |
| `IE00BD0NC037` | iShares Euro Government Bond | C4 (12 %) | `-glm` C3 |

**6 de 37 líneas** coinciden con alguna hermana; 31 no. Cuatro son fondos que el titular nombró
(Robeco QI EM, Jupiter GEAR) o activos con muy pocos vehículos en el catálogo (cat bonds, infraestructura).
Las dos de deuda pública son clases indexadas al 0,10 %: el sustituto comparable más barato del catálogo
cuesta 0,35-0,39 % (Amundi Core Euro Government AE-C, State Street Euro Core Treasury), es decir
**+35 a +41 €/año** por no repetir un vehículo que es una materia prima. Se repite y se dice, en lugar de
pagar el sobreprecio.

El resto del diseño evita deliberadamente los vehículos de las hermanas: los cuatro núcleos indexados de
estas cinco carteras son cuatro ISIN distintos (iShares Developed World D, Amundi MSCI World IE-C,
Vanguard ESG All Cap y Vanguard Global Stock), cuando lo fácil habría sido usar el mismo en las cuatro.

## Dominancia frente al resto del repositorio

El cruce con las carteras que ya existen, con el número al lado. No se retira ninguna: quitar parte de un
encargo de cinco rompe la premisa del entregable y esa decisión es del titular.

| Cartera | Aquí | La comparable más cercana | Quién gana |
| --- | --- | --- | --- |
| C1 | 69,47 % de RV por 129,20 €/año | `cartera-definitiva-40/`: 83,39 % por 92,00 €/año | **Gana la existente en las dos columnas.** C1 está dominada; su razón de existir es ser la pieza de coste mínimo de un conjunto que no puede repetir fondos, no ser la mejor cartera de índice del repositorio |
| C2 | 97,60 % por 1.434,40 €/año | `cartera-ai-fondos-2000-lista/C2`: 78,65 % por 1.248,60 €/año | No comparable: C2 compra 19 pp más de bolsa por 186 €/año más |
| C3 | 55,05 % por 492,90 €/año | `cartera-ai-definitivas-estudiar/cartera-ai-final-conservadora/`: 54,61 % por 509,70 €/año | **Gana C3**: misma RV, 16,80 €/año menos |
| C4 | 34,06 % por 607,60 €/año | `cartera-ai-fondos-2000-lista/C4`: 35,49 % por 766,10 €/año | **Gana C4**: 1,4 pp menos de RV y 158,50 €/año menos |
| C5 | 99,48 % por 764,60 €/año | `cartera-ai-fondos-2000-lista-glm/C5`: 87,64 % por 942,30 €/año | **Gana C5**: 11,8 pp más de RV y 177,70 €/año menos |

Lo que C1 compra con su sobrecoste no es retorno: es que las otras cuatro carteras puedan tener sus propios
núcleos indexados sin repetir el mismo vehículo. Si el titular prefiere una sola cartera de índice, la
respuesta del repositorio ya está escrita y es `cartera-definitiva-40/`.

## Valoración: por qué C5 es la ganadora

Parámetros del titular (20/11/2026): **horizonte 15 años, aportación de 1.500 €/mes y las comisiones de
éxito no son un veto**. Con esas tres piezas los 100.000 € iniciales son el 27 % del dinero que entra
(370.000 € aportados en 15 años) y el 73 % restante entra a precio de mercado: manda el coste y la
permanencia, no el punto de entrada.

Misma vara para las cinco (RV *look-through* y caída de la casa), y valor final con supuestos declarados
—bolsa 6 %, renta fija 3 %, liquidez 2,5 % brutos anuales—, 100.000 € iniciales + 1.500 €/mes:

| Cartera | RV real | Coste/año | Caída de manual | Valor a 15 años | Diferencia con la ganadora |
| --- | --: | --: | --: | --: | --: |
| **C5 crecimiento** | **99,48 %** | **764,60 €** | **−39,79 %** | **618.617 €** | — |
| C1 índice mínimo | 69,47 % | 129,20 € | −28,68 % | 602.175 € | −16.442 € |
| C2 convicción | 97,60 % | 1.434,40 € | −39,04 % | 574.267 € | −44.349 € |
| C3 equilibrada | 55,05 % | 492,90 € | −23,28 % | 555.037 € | −63.580 € |
| C4 defensiva | 34,06 % | 607,60 € | −15,07 % | 511.446 € | −107.171 € |

**Gana C5, y así queda marcada en la carpeta y en el mapa de carteras** (`status: final`, ⚠️ pendiente de
la revisión del titular, ninguna orden lanzada). Razones, en orden de peso:

1. **Es la única con renta variable alta y coste bajo.** C2 compra el mismo 97,6 % de bolsa por 669,80 €/año
   más, y esa diferencia son 44.349 € a quince años: no es una opinión sobre gestores, es una resta.
2. **El horizonte absuelve a C3 y C4, no las hace ganar.** Con 15 años y aportaciones, un 34 % o un 55 % de
   bolsa deja demasiado dinero sin crecer: 107.171 € y 63.580 € por detrás.
3. **El único rival es C1, y es un rival de escenario.** La cartera de índice gana **si la bolsa renta menos
   del 5,2 % bruto anual** (a 4,5 %: C1 542.147 € frente a C5 532.219 €; a 5,0 %: 561.386 frente a 559.436).
   Por encima de ese punto de cruce, C5 gana y la diferencia crece. Con el histórico largo de la bolsa
   mundial (≈7 % nominal) el escenario base está por encima del cruce.
4. **Las comisiones de éxito ya no descartan nada**, pero siguen contando: C5 solo tiene una línea con éxito
   (DNB, 10 %) frente a las cuatro de C4.

**Lo que hay que poder mirar antes de firmar:** hacia el año 10 el saldo ronda los 400.000 € y una caída del
40 % son −160.000 € en el peor momento. Si eso no se aguanta sin vender, la respuesta no es C5 sino C4, y se
paga con 107.171 € del escenario base.

El plan de aportaciones de C5 —reparto de los 1.500 €/mes por fondo, cadencias y regla de rebalanceo por
entradas— está en su §8, y la aritmética de los tres escenarios en su §9.

## Cómo se ha hecho

1. **Extracción determinista de las 2.007 fichas** (TER, éxito, mínimos, RV/RF/caja, 3A/5A, SRRI,
   avisos) a un JSON de trabajo, para cribar por bloque sin leer 2.007 documentos a mano.
2. **Diseño de cinco criterios distintos** y ajuste de pesos por código hasta clavar 100.000 € y el
   perfil objetivo de cada uno.
3. **Verificación de 54 ISIN en el catálogo MCP de MyInvestor (20/11/2026, 8 llamadas `get_funds`)**:
   acumulación, TER, comisión de éxito, mínimos y avisos. **Seis hallazgos cambiaron el diseño:**
   - La clase Investor del S&P 500 (`IE0032620787`) está **en soft close** → clase Institutional.
   - **Okavango Delta A** está **en soft close** → fuera de C2.
   - **Dodge & Cox Global Stock** tiene **50.000 € de mínimo** → fuera, pese a ser el mejor global barato.
   - **BlueBox Technology I** tiene **150.000 €** y **Algebris Financial Equity I** **500.000 €** → no son comprables.
   - **M&G Japan Smaller** tiene **500.000 €** de mínimo → fuera.
   - **TER al alza** frente a la ficha en Pareto (0,70 → 0,84), Merchbanc (1,19 → 1,23), Valentum
     (1,36 → 1,46), M&G European Strategic Value (1,65 → 1,70) y Dunas (1,27 → 1,19 a la baja). Manda el MCP.
4. **Cuadre y no-repetición comprobados por código sobre el markdown ya escrito**: se parsean las tablas
   de los cinco documentos, no el diccionario de origen. 37 líneas, 37 ISIN, 37 fondos, 5 × 100.000 € exactos.

## Ficheros

- `C1…C5-*.md`: cada cartera entera (decisión, tabla con ISIN y pesos, bloques con su TER medio,
  métricas, geografía *look-through*, razón y pega fondo a fondo, órdenes con hora de corte, descartes
  con número y disparadores de revisión).
- `fondos-revisados.md`: los 37 fondos con TER, éxito, mínimo, corte, exposición y la pega principal,
  más los 12 candidatos descartados con el dato que los descarta.
- `validacion.md` / `validacion.json`: unicidad, cuadre, mínimos y verificación de plataforma.
- `diseno.json`: las cinco carteras en formato máquina.

## Estado

⚠️ **Sin ejecutar y pendiente de la revisión del titular: C5 es la ganadora y no se lanza ninguna orden
hasta esa revisión.** **Parámetros ya fijados el 20/11/2026:** horizonte
de 15 años, aportación de 1.500 €/mes y comisiones de éxito admitidas; con ellos la ganadora es **C5**, que
lleva su plan de aportaciones en el §8. Pendiente de confirmar: colchón fuera de cartera y tolerancia real a
una caída del 40 % (si no se aguanta, la cartera correcta es C4).

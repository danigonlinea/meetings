---
title: "Laboratorio de carteras: veinticinco diseños propios y una cartera de un tercero"
date: 2026-11-26
type: reference
category: finance
tags: [cartera, indice, laboratorio-carteras, cartera-ai-andres, cartera-ai-no-indexados, cartera-ai-no-indexados-2, cartera-ai-no-indexados-3, cartera-ai-no-indexados-4, cartera-ai-no-indexados-5, cartera-ai-40-max-index, cartera-ai-100-index, cartera-ai-100-index-2, cartera-ai-100-index-3, cartera-ai-100-index-4, cartera-ai-100-index-5, cartera-ai-rock-index-value-todo, cartera-ai-rock-desmontado, cartera-ai-final-conservadora, cartera-ai-final-atrevida, cartera-definitiva-40, cartera-de-andres, cartera-ai-c4-defensiva, cartera-ai-azvalor-consejo, cartera-ai-hy4-definitiva, cartera-ai-neon, cartera-ai-neon-2, cartera-ai-definitiva-final, cartera-ai-argon, cartera-ai-carbon, cartera-ai-definitivas-estudiar]
status: living
---
# Laboratorio de carteras: veinticinco diseños propios y una cartera de un tercero

Carteras **estudiadas, no ejecutadas**. Cada carpeta es un diseño completo —mandato, ISIN, coste, caída,
esperanza y órdenes— que se conserva para comparar y para no volver a pagar por una idea ya medida.
Aquí no hay dinero real: nada de esta carpeta se rebalancea ni se suma a las carteras de
[`finance/portfolio/`](../portfolio/README.md), que son solo dos (MyInvestor y Renta 4).

La única cartera que ha salido del laboratorio es la **Opción A** del ranking de
`cartera-ai-definitiva-final/`: promovida el 26/11/2026 y hoy es la **propuesta final de la cartera de
MyInvestor**, en
[`finance/portfolio/cartera-myinvestor-propuesta/`](../portfolio/cartera-myinvestor-propuesta/README.md). Promover es
**mover** el documento, no copiarlo.

**`cartera-ai-definitivas-estudiar/`** agrupa, desde el 22/11/2026, las **doce carteras entre el 30 % y el
45 % de indexado** (neon-2, carbon, argon, neon, 40-max-index, final-conservadora, andres, final-atrevida, hy4-definitiva, rock-desmontado,
rock-index-value-todo y c4-defensiva). El contenedor no consolida nada ni cambia un peso: cada subcarpeta mantiene su
criterio y su documento. Las dos piezas en rango de `finance/portfolio/cartera-myinvestor/` (38,3 % y 34,0 %) **no se mueven**
porque son la cartera viva. Criterio y exclusiones: `cartera-ai-definitivas-estudiar/README.md`.

| Carpeta | Qué es | Documentos |
| --- | --- | --- |
| `cartera-ai-definitiva-final/` | **Contenedor del ranking forense del 26/11/2026** (`100.000 €` libres + `10.000 €` intocables en `Groupama` = `110.000 €`, 15 años). Su **#1, Opción A** (`8,71/10`), salió del laboratorio ese mismo día: hoy es [`finance/portfolio/cartera-myinvestor-propuesta/`](../portfolio/cartera-myinvestor-propuesta/README.md). Las otras cuatro (`opcion-b.md`, `opcion-c.md`, `opcion-d.md` —descartada por no llevar gestión activa en RV— y `opcion-e.md`) están en el historial de git. Queda **#2 Opción 0** (`option-0.md`, `7,81/10`, 13 fondos, `84,24 %` de RV, `0,784 %` TER, 2022 en `−5,74 %`) | `README.md` + `auditoria-ranking.md` + `option-0.md` |
| `cartera-ai-definitivas-estudiar/cartera-ai-andres/` | **Dos tallas** con el criterio de Andrés, sin acciones: `100k.md` (11 fondos, 60,3 % RV, 0,46 %) y `200k.md` (14 fondos, 60,0 %, 0,51 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, órdenes, descartes y señales) |
| `cartera-ai-no-indexados/` | **Dos tallas con dos condiciones únicas**: ningún fondo indexado y ninguno que reparta dividendos (`100k.md`, 10 fondos activos, 80 % RV, 1,37 %; `200k.md`, 12 fondos, 80 %, 1,42 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, razonamiento fondo a fondo, órdenes, aportación mensual y señales) |
| `cartera-ai-definitivas-estudiar/cartera-ai-40-max-index/` | **Dos tallas con otras dos condiciones únicas**: máx. 40 % en indexados y nada que reparta dividendos (`100k.md`, 2 indexados + 7 activos, 40 % indexado exacto, 73,0 % RV, 0,79 %; `200k.md`, 2 + 8 con Iberia, 73,6 %, 0,80 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, razonamiento, órdenes, 2.000 €/mes y señales) |
| `cartera-ai-100-index/` | **Dos tallas con otras dos condiciones únicas**: solo fondos indexados y nada que reparta dividendos (`100k.md`, 7 indexados, 79,9 % RV, 0,1065 %; `200k.md`, 8 indexados con Europa al 5 %, 79,9 %, 0,1085 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, razonamiento, órdenes, 2.000 €/mes y señales) |
| `cartera-ai-100-index-2/` | **Dos tallas con las mismas dos condiciones más una tercera**: solo indexados, nada que reparta dividendos y **ningún fondo ya elegido en otra cartera** (`100k.md`, 6 indexados regionales + 3 de RF, 79,8 % RV, 0,1113 %; `200k.md`, mismos 6 + 4 de RF con deuda emergente, 79,8 %, 0,1128 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, razonamiento fondo a fondo, lista negra verificada, órdenes, 2.000 €/mes y señales) |
| `cartera-ai-100-index-3/` | **Dos tallas con las mismas tres cláusulas, desde cero**: solo indexados, nada que reparta dividendos y **ningún fondo ya elegido en otra cartera** (`100k.md`, 5 indexados regionales + 2 de RF, 79,57 % RV, 0,2086 %; `200k.md`, los mismos 7 con el doble de importe, 0,2086 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, razonamiento fondo a fondo, lista negra verificada por ISIN y por fondo, órdenes, 2.000 €/mes y señales) |
| `cartera-ai-no-indexados-2/` | **Dos tallas con tres condiciones únicas**: nada que reparta dividendos, nada indexado y **ningún fondo ya elegido en otra cartera** (`100k.md`, 9 + 3 fondos, 85 % RV, 1,70 %; `200k.md`, 11 + 3 con Mirabaud e India, 85 %, 1,70 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, razonamiento, órdenes, 2.000 €/mes y señales) |
| `cartera-ai-100-index-4/` | **Dos tallas, desde cero, con las mismas dos condiciones**: solo indexados y nada que reparta dividendos, más la lista negra de los 180 ISIN aplicada por decisión propia (`100k.md`, núcleo ACWI + 2 convicciones + 2 de RF, **85,16 % RV**, **0,3771 %**; `200k.md`, los mismos 5 fondos y pesos, 0,3771 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, razonamiento fondo a fondo, lista negra verificada por ISIN y por fondo, órdenes, 2.000 €/mes y señales) |
| `cartera-ai-100-index-5/` | **Dos tallas, desde cero, con las tres cláusulas**: solo indexados, nada que reparta dividendos y **ningún fondo ya elegido en otra cartera**, esta vez pedido por el titular (`100k.md`, núcleo MSCI World + Europa + emergentes + agregado global cubierto, **84,95 % RV**, **0,1930 %**; `200k.md`, los mismos 4 fondos y pesos, 0,1930 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, razonamiento fondo a fondo, lista negra verificada por ISIN y por fondo, órdenes, 2.000 €/mes y señales) |
| `cartera-ai-no-indexados-3/` | **Dos tallas con dos condiciones únicas, desde cero**: nada que reparta dividendos y **ningún fondo indexado ni ya elegido antes** (`100k.md`, 7 + 3 fondos, 80 % RV, 1,5472 %; `200k.md`, mismos 7 + 3 más crédito corto, 80 %, 1,5268 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, razonamiento fondo a fondo, órdenes, 2.000 €/mes y señales) |
| `cartera-ai-no-indexados-4/` | **Dos tallas con las mismas dos condiciones, desde cero**: nada que reparta dividendos y **ningún fondo indexado ni ya elegido antes** (`100k.md`, 7 + 3 fondos, 70 % RV, 1,5961 %; `200k.md`, 8 + 3 con small caps EE. UU., 70 %, 1,5851 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, razonamiento fondo a fondo, órdenes, 2.000 €/mes y señales) |
| `cartera-definitiva-40/` | **Una talla, 100.000 €, a los 40 años**: la cartera más barata del repositorio con seis indexados y un sesgo europeo declarado —58 % MSCI World al 0,06 %, 10 % emergentes, **10 % Europa**, 6 % small caps, 11 % RF global 1-5 años cubierta y **5 % deuda ligada a inflación**—, **83,39 % de RV real**, **92,00 €/año (0,092 %)**, caída **−33,85 %** y **≈6,06 % esperado**, con plan de aportación y glide de edad | Un fichero (`100k.md`): la cartera entera (ISIN, bloques, geografía y sectores, tres variantes de edad, esperanza con supuestos, tabla de aportaciones, plan completo, 4 órdenes, descartes con número y señales) |
| `cartera-de-andres/` | **Cartera de un tercero**, no del dueño: la cuenta personal de Andrés (La Pizarra) publicada cada mes | `cartera-actual.md` (foto vigente) + `anteriores/` (fotos mensuales congeladas) |
| `cartera-ai-definitivas-estudiar/cartera-ai-final-conservadora/` | **Una talla, 100.000 €**: la cartera del 18/11 con el crédito consolidado en Neuberger (**12 fondos**, **54,6 % de RV**, **509,70 €/año (0,566 %)**, duración 1,61) y **≈4,8 % de rentabilidad esperada anual** con rango 2,3-6,8 % y supuestos escritos | Un fichero (`100k.md`): la cartera entera (ISIN, bloques, coste, duración, rentabilidad esperada con su método, 22 órdenes en dos fases, 1.000 €/mes, descartes con número y señales) |
| `cartera-ai-no-indexados-5/` | **Dos tallas con las mismas dos condiciones, desde cero**: nada que reparta dividendos y **ningún fondo indexado ni ya elegido antes** (`100k.md`, 7 + 3 fondos, 70 % RV, 1,3543 %; `200k.md`, 8 + 3 con Valentum, 70 %, 1,3417 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, razonamiento fondo a fondo, órdenes, 2.000 €/mes y señales) |
| `cartera-ai-definitivas-estudiar/cartera-ai-final-atrevida/` | **Una talla, 110.000 €**: desde cero, con **10.000 € en el monetario** por mandato y 12 fondos sin ETF (**82,15 % de RV real**, **877,80 €/año (0,798 %)**, caída −33,4 %, **≈6,1 % esperado** con rango 4,0-7,4 %) | Un fichero (`110k.md`): la cartera entera (ISIN, bloques, geografía, tilts, rentabilidad esperada con supuestos, 13 órdenes y descartes con número) |
| `cartera-ai-definitivas-estudiar/cartera-ai-rock-index-value-todo/` | **Una talla, 100.000 €**, con **Rock como pieza de indexado** (30 %, intacta), **monetario escalonado de 14.000 €** (Groupama €STR + DWS Euro Ultra Short) y **trece fondos que no replican índices**: 55,5 % de RV real, 0,615 % de coste total, −23,54 % de caída de manual | Un fichero (`100k.md`): la cartera entera (ISIN, razón fondo a fondo, métricas, 17 traspasos, descartes con número y señales) |
| `cartera-ai-definitivas-estudiar/cartera-ai-rock-desmontado/` | **Una talla, 100.000 €**, **Rock desmontado por traspaso** y su cupo gastado en índice limpio: núcleo MSCI World al 0,06 %, emergentes, small caps y REITs indexados, RF corta indexada, monetario de 14.500 € y **dos satélites activos** (Europa low-vol y cat bonds). 55,31 % de RV real, **236,10 €/año (0,236 %)**, −23,46 % de caída | Un fichero (`100k.md`): la cartera entera (ISIN, métricas contra las otras propuestas, 20 traspasos en dos fases y descartes con número) |
| `cartera-ai-azvalor-consejo/` | **Una talla, 100.000 €**, traducida de una entrevista a **Beltrán Parages** (Azvalor, *La Pizarra de Andrés*, 11/2026): todo en equity, beneficio de la duda para el índice y cuatro filtros para la excepción. **60 % indexado** (45 % MSCI World desarrollado al 0,06 % y 15 % Europa al 0,10 %) y **40 % en tres value** (20 % Azvalor Internacional, 10 % Magallanes European, 10 % Cobas Large Cap al 0,96 % en vez de la internacional al 2,33 % y en *soft close*). **93,17 % de RV real, 709 €/año (0,709 %), caída −37,27 % y ≈6,83 % esperado**; cero renta fija, cero monetario y cero comisiones de éxito. Cinco órdenes, una antes de las 09:00 (precio del 0,06 %), y el 20 % de Azvalor cautivo 12 meses por su comisión de reembolso del 3 % | `README.md` de mapa + `100k.md` (la cartera entera: mandato con su precio, ISIN, bloques, geografía y sectores, tilts, variantes, backtest en dos pasadas, esperanza, comparador, órdenes, descartes con número y disparadores) |
| `cartera-ai-definitivas-estudiar/cartera-ai-c4-defensiva/` | **La más defensiva del contenedor**: 100.000 € en ocho fondos, **34,06 % de RV real**, **44,00 % de indexado** (32 % Vanguard Global Stock + 12 % iShares Euro Government), tres alternativos descorrelacionados (market neutral, retorno absoluto y cat bonds) y colchón de deuda pública, **607,60 €/año (0,6076 %)** con cuatro comisiones de éxito y caída −15,07 %. Promovida el 22/11/2026 desde la C4 de `cartera-ai-fondos-2000-lista-deepseek` | `README.md` de mapa + `100k.md` |
| `cartera-ai-definitivas-estudiar/cartera-ai-hy4-definitiva/` | ⚠️ **Cartera finalista, pendiente de la revisión del titular, sin órdenes** (22/11/2026): 100.000 € a 15 años con tope del 35 % en indexados, nacida del cribado de las tres variantes de `cartera-ai-fondos-2000-lista*` (2.007/1.980/2.007 fichas, 108 ISIN finalistas). 65,5 % de RV real, 537,10 €/año (0,537 %), cero comisiones de éxito, +7,99 % anualizado en backtest y 5,11 % neto estimado sin alfa | `README.md` de mapa + `100k.md` |
| `cartera-ai-definitivas-estudiar/cartera-ai-neon-2/` | **Una talla, 100.000 € libres para invertir (+ 10.000 € intocables aparte en `Groupama` = 110.000 €), a 15 años vista (2026 → 2041)** (25/11/2026): nacida desde cero al auditar `finance/portfolio/cartera-myinvestor/propuesta-actual.md` y barrer las **2.007 fichas de `finance/fondos-myinvestor/`** con **0/13 solape respecto a `cartera-ai-neon/`** (18 fondos / 25 ISIN bloqueados por ISIN y clase hermana). **43,00 % de indexado s/100k libres (39,09 % s/110k)** (`43.000 €` al `0,160 %`: `Vanguard Global Stock`, `iShares Europe ex-UK`, `iShares UK`, `Fidelity MSCI Japan EUR Hedged` y `Fidelity MSCI EM`), **42,00 % en 5 motores activos RV 0 % éxito** (`Robeco BP Global Premium`, `Brandes European Value`, `GS Global Small CORE`, `Wellington Enduring Infrastructure` e India contrarian `Ashoka WhiteOak India`) y **15,00 % en escudo antiestanflación sin HY, sin Gamma y sin duplicar monetarios** (`EDM Renta R`, `UBAM USD Floating Rate Notes AHC EUR` y `GSQuartix Modified Strategy Bloomberg Commodity`, en **+4,59 % en 2022**). **84,24 % de RV real s/100k (76,58 % s/110k)**, **68,88 % de la RV fuera de EE. UU.**, **36,78 % SMID**, **top 10 US tech al 4,24 % s/100k (3,85 % s/110k)**, caída en **2022 de −5,74 % s/100k (−5,22 % s/110k)**, **784,10 €/año s/100k (791,10 € = 0,719 % s/110k) y 0/13 comisiones de éxito**, **16 traspasos + 1 suscripción** (`0` órdenes sobre `Groupama`) y **≈6,90 % neto esperado s/100k** (`4,74 %` en test neutro sin alfa) | `README.md` de mapa + `100k.md` + `propuesta-neon-deepseek.md` (variante de 10 líneas) |
| `cartera-ai-definitivas-estudiar/cartera-ai-carbon/` | **Una talla, 100.000 € libres para invertir (+ 10.000 € intocables aparte en `Groupama` = 110.000 €), a 15 años vista (2026 → 2041)** (25/11/2026): nacida de auditar `finance/portfolio/cartera-myinvestor/cartera-actual.md` y barrer las **2.007 fichas de `finance/fondos-myinvestor/`**. **40,00 % de indexado s/100k libres (36,36 % s/110k)** (`40.000 €` al `0,123 %`, con Japón cubierto a EUR al `0,20 %` `IE00BYX5NH74`), **44,00 % en 5 motores activos 0 % éxito** (`Robeco BP Global Premium`, `M&G European Strategic Value`, `Palm Harbour Global Value` al `1,02 %`, `Robeco QI EM Active` y **redes eléctricas/infraestructura física `First Sentier`** `IE00BYSJTY39`) y **16,00 % en escudo antiestanflación sin HY, sin Gamma y sin duplicar monetarios** (`Cobas Renta FI`, `DWS Floating Rate Notes` y `Twelve Cat Bond`). **84,14 % de RV real s/100k (76,49 % s/110k)**, **65,17 % de la RV fuera de EE. UU.**, **top 10 US tech al 5,33 % de 110k**, caída en **2022 de −5,59 % s/100k (−5,05 % s/110k, con Bloque 3 en +0,21 %)**, **776,10 €/año s/100k (783,10 € = 0,712 % s/110k) y 0/12 comisiones de éxito**, **15 traspasos + 2 suscripciones** (`0` órdenes sobre `Groupama`) y **≈6,80 % neto esperado s/100k** | `README.md` de mapa + `100k.md` |
| `cartera-ai-definitivas-estudiar/cartera-ai-argon/` | **Una talla, 100.000 € (90.000 € invertibles + 10.000 € colchón Groupama), a 15 años vista** (25/11/2026): nacida de auditar `propuesta-pieza.md` contra las **2.011 fichas de `finance/fondos-myinvestor/`** y cuadrar los traspasos desde `finance/portfolio/cartera-myinvestor/cartera-actual.md`. **37,78 % de indexado s/90k (34,00 % s/100k)** con Japón cubierto a EUR al 0,20 % (`IE00BYX5NH74`), **38,89 % en 5 motores activos ortogonales con 0 % éxito** (`M&G European Strategic Value`, `Horos`, `Palm Harbour` al 1,02 %, `Robeco QI EM Active`, `DWS CROCI Japan LCH`) y **23,33 % en escudo defensivo y pólvora seca** (`Gamma Global A` 8.000 € intactos, `DWS Floating Rate Notes`, `Cobas Renta`, `Twelve Cat Bond`). **76,40 % de RV real s/90k (68,76 % s/100k)**, **74,63 % de la RV fuera de EE. UU.**, **top 10 US tech reducido al 4,80 % de 100k**, caída en **2022 de −5,04 % s/90k (−4,54 % s/100k, con Bloque 3 en +0,83 %)**, **718,40 €/año (0,798 % s/90k · 0,725 % s/100k)**, **14 traspasos** y **≈6,65 % neto esperado s/90k** | `README.md` de mapa + `100k.md` |
| `cartera-ai-definitivas-estudiar/cartera-ai-neon/` | **Una talla, 110.000 €, 40 años a 15 años vista** (22/11/2026): diseñada para entrar **de golpe** (`9oM4CFH5usw`) o **rebalancear por traspaso `cartera-actual.md`** (100.000 € actuales + 10.000 € nuevos = 110.000 €) usando **solo fondos de `finance/fondos-myinvestor/`**. **32,73 % de indexado como pieza** (36.000 € en MSCI World S + MSCI Europe + Vanguard Small-Cap), **40,00 % en RV activa value/ex-US/SMID** (44.000 € en Horos, M&G European Strategic Value, Sigma, DWS CROCI Japan LCH cubierto a EUR y Robeco QI EM Active) y **27,27 % en escudo defensivo para mercados caros** (30.000 € en DWS Floating Rate Notes, Gamma Global 8.000 € intactos, Cobas Renta, Twelve Cat Bond y AXA Trésor Court Terme). **72,28 % de RV real** con **73,63 % fuera de EE. UU.**, **39,85 % en Small & Mid Caps**, **top 10 tecnológicas de EE. UU. reducido al 4,85 % del total (6,71 % de la RV)**, caída en **2022 de −5,10 %** (con el bloque defensivo en **+0,45 %**), **933,90 €/año (0,85 %)** —o **848,30 €/año (0,77 %)** en variante 0 % éxito con Palm Harbour y B&H Deuda— y **≈6,50 % neto esperado** (282.903 € a 15 años) | `README.md` de mapa + `110k.md` |

`cartera-de-andres/` es material de **análisis**, no una cartera del dueño: no se suma, no se
rebalancea y no compite con las anteriores del dueño. Se actualiza con la skill `cartera-andres` cuando se
ingiere un vídeo de resultados del canal.

`cartera-ai-definitivas-estudiar/cartera-ai-andres/` sigue el criterio de Andrés —gestión activa, sin acciones,
60 % de RV— y no es una versión de ningún otro diseño del árbol: el titular elige una talla y la ejecuta sola.

El 20/11/2026 el titular retiró `cartera-cobas/`, `cartera-horos/` y `cartera-vanguard/`: las tres eran la
respuesta a un mandato de **gestora única** y su criterio —«no tiene sentido una única gestora para una única
cartera»— deja esos diseños fuera del árbol. Los tres documentos siguen en el historial de git. Las cifras que
otras carteras citaban contra ellas (1.278 €/año de Cobas, 1.626,50 € de Horos, 178,50 € de Vanguard y el tilt
de 46,9 % en EE. UU. que costaba ≈0,55 pp/año) se mantienen donde hacían falta, sin enlace: el número no cambia
porque el fichero se haya ido.

El 22/11/2026 el titular retiró **siete carpetas más** con un criterio único: una cartera solo se queda si no
está dominada por otra del árbol en renta variable, coste y esperanza. Fuera `cartera-100k-15-anos/` (74,5 % de RV
y 100,50 €/año frente a los 83,39 % y 92,00 € de `cartera-definitiva-40/`), `cartera-ai/` (74,9 % y 116 €, con
acciones individuales), `cartera-ai-nucleo-satelites/` (84,33 % y 400,80 € con 1,54 pp/año de alfa de empate),
`cartera-ai-letter-keinesei-twitter/` (66,72 % y 1.024,20 €, traducida de un artículo ajeno),
`cartera-indexado-ladrillo-15-anos/` (44,45 % y 1.265,80 € más cinco comisiones de éxito),
`cartera-pizarra-tres-voces/` (72,90 % y 714,30 € con el 49 % en Singular) y `cartera-ai-fondos-2000-lista/`
(sus C2 y C4 quedan por detrás de las hermanas: 1.248,60 € y 766,10 € frente a 1.180,10 € de `-glm` y 607,60 € de
`-deepseek`). Los documentos siguen en el historial de git y las cifras que otras carteras citaban contra ellas se
mantienen donde hacían falta, sin enlace. **`cartera-ai-definitivas-estudiar/` no se toca**: sus nueve carteras entre el 30 % y el 45 % de indexado (incluidas `c4-defensiva` y `neon`) se
quedan y siguen mandando sobre su propio documento.

El mismo día se llevó la criba a las **dos familias de cinco diseños**. De las diez carteras de
`cartera-ai-fondos-2000-lista-deepseek` y `-glm`, una se promovió y nueve se retiraron. La promovida es la **C4 de
deepseek** (44,00 % de indexado, 34,06 % de RV, 607,60 €/año), que pasa a
`cartera-ai-definitivas-estudiar/cartera-ai-c4-defensiva/`: es la única de las diez que cae cerca de la banda de
indexado que el titular estudia —el contenedor sube su techo del 40 % al 45 % por ella— y la única con perfil
defensivo. Se retiran **C1, C2, C3 y C5 de deepseek** (100 %, 0 %, 55 % y 60 % de indexado) y **las cinco de
`-glm`** (100 %, 0 %, 53 %, 17 % y 55 %): ninguna entraba en la banda ni con el techo ampliado, y la C5 —marcada
como elegida el 20/11, 99,48 % de RV y 764,60 €/año— solo ganaba a `cartera-definitiva-40` por encima del 6,93 %
bruto, con el 62 % del dinero en EE. UU. y el 33 % en tecnología. Sus documentos, su `fondos-revisados.md` y su
`validacion.md` siguen en el historial de git.

`cartera-definitiva-40/` es **la cartera de referencia del titular a su edad** (40 años, 19/11/2026) y no nace de
ninguna otra: seis indexados, **92,00 €/año (0,092 %)** —la más barata del repositorio—, **83,39 % de RV real**,
caída **−33,85 %** y **≈6,06 % esperado**. La decisión de diseño es una sola: **cuánta bolsa a los 40**, y la
respuesta es 83/17 con el colchón fuera. **Actualizada el 20/11/2026** tras una crítica externa: fuera el Japón que duplicaba peso, fuera los REITs y fuera la deuda emergente del colchón; dentro Europa al 10 % como único sesgo declarado y un 5 % de ligado a inflación. No hay estilo, ni sector, ni comisión de éxito. Lo demás está escrito como plan: colchón de
6-12 meses fuera, aportación automática mensual —**con 1.000 €/mes el capital a los 67 pasa de ≈502.000 € a
≈1.308.000 €**—, rebalanceo por bandas de ±5 pp con aportaciones y **glide de edad desde los 55** (1 pp/año de RV a
renta fija). Su variante 70/30, para horizontes de 5-7 años, es 99,30 €/año y −28,74 % de caída.

`cartera-ai-no-indexados/` es un tercer diseño independiente del mismo agente, con **dos condiciones únicas
del titular** —ningún fondo indexado, ningún fondo que reparta dividendos— y **ninguna regla heredada** del
resto del repositorio. Dos tallas (100k y 200k), sin acciones y sin ETF. No se suma ni compite con las otras.

`cartera-ai-definitivas-estudiar/cartera-ai-40-max-index/` es el cuarto diseño del mismo agente y no deriva de los anteriores: su mandato es
**máximo 40 % en indexados** (usado al 40,0 % exacto: 28 % MSCI World + 12 % MSCI EM) y **nada que reparta
dividendos**, también sin reglas heredadas. Dos tallas (100k y 200k), sin acciones ni ETF, 73,0–73,6 % de RV
real y 0,79–0,80 % de TER. El techo del 40 % es una obligación viva: si el bloque indexado lo supera por
revalorización, se corrige desviando aportaciones, no vendiendo.

`cartera-ai-100-index/` es el quinto diseño independiente del mismo agente y no deriva de los anteriores: su
mandato son **dos condiciones únicas del titular** —solo fondos indexados y ninguno que reparta dividendos— y
**ninguna regla heredada** del resto del repositorio. Dos tallas (100k y 200k), sin acciones, sin ETF y sin
monetarios. Todo indexado, 79,9 % de RV real y 0,1065–0,1085 % de TER: es la cartera más barata del
repositorio porque el mandato no deja otra cosa que comprar. La talla de 200k añade MSCI Europe al 5 % y baja
el núcleo al 50 %.

`cartera-ai-100-index-2/` es un décimo diseño independiente del mismo agente, **desde cero**, con las dos
condiciones anteriores más una tercera que cambia el resultado: **ningún fondo ya elegido en otra cartera**
(los 136 ISIN del repositorio como lista negra, más comprobación por nombre, gestora y clase hermana). Con el
núcleo global barato, el único pasivo de small caps, el inmobiliario barato y los tres bonos baratos
prohibidos, el MSCI World se **replica con cinco indexados regionales a pesos de índice** (52 % Norteamérica,
9 % Europa ex-UK, 3 % UK, 4 % Japón, 2 % Pacífico ex-Japón) y el bloque de RF se construye con Vanguard y
otras clases: 79,8 % de RV real y 0,1113–0,1128 % de TER. Dos tallas (100k, 9 fondos; 200k, 10 con deuda
emergente en divisa fuerte). Sin small caps y sin ligado a inflación: es lo que queda cuando se prohíben los
fondos ya usados.

`cartera-ai-100-index-3/` es un undécimo diseño independiente del mismo agente, **desde cero** y con las
mismas tres cláusulas que la cartera 2 —solo indexados, nada que reparta, **ningún fondo ya elegido antes**—
pero aplicadas sobre un catálogo **más gastado**: los **159 ISIN** del repositorio dejan **101 fondos indexados
de acumulación libres de verdad**, porque la comprobación se hace también **por fondo** (dos clases del mismo
fondo comparten patrimonio en la ficha, y así caen 62 clases hermanas que por ISIN se habrían colado: los dos
S&P 500 baratos del catálogo, entre ellas). El resultado paga el precio en dos sitios: Norteamérica se compra
al 0,23 % (el índice ancho, sin filtro ESG, con Canadá) y Japón con un índice de transición climática de 4,45 %
de *tracking error*. Siete fondos —cinco regionales más crédito corporativo global y bonos verdes, los dos
cubiertos a euros—, 79,57 % de RV real y **0,2086 % de TER**. Dos tallas (100k y 200k) con las mismas líneas:
el tamaño no desbloquea nada, y la deuda pública euro libre al 0,39 % se rechaza con la cuenta escrita.

`cartera-ai-100-index-4/` es un duodécimo diseño independiente del mismo agente, **desde cero** y con las
mismas dos condiciones de `cartera-ai-100-index/` —solo indexados, nada que reparta—, con la lista negra de los
**180 ISIN** aplicada por decisión propia (no la pidió el titular esta vez). Lo que cambia respecto a las
hermanas `-2` y `-3` es el catálogo: el **núcleo global sigue vivo** (`MyInvestor Mundo Desarrollado y
Emergente`, MSCI ACWI, 0,43 %), así que la cartera no trocea el mundo en cinco regiones sino que se queda en
**cinco líneas**: núcleo al 67 %, dos convicciones escritas (10 % eurozona, 8 % emergentes) y dos mitades de
renta fija en euros (8 % deuda pública, 7 % crédito IG). **85,16 % de RV real y 0,3771 % de TER** en las dos
tallas. Se paga en tres concesiones: cero small caps, cero ligado a inflación y cero inmobiliario (los únicos
indexados del catálogo están elegidos) y Japón sin línea propia, porque el único indexado japonés libre no
nombra su índice en la ficha.

`cartera-ai-no-indexados-2/` es un sexto diseño del mismo agente, hermano del anterior y no derivado de él:
las dos condiciones de `cartera-ai-no-indexados/` —nada indexado, nada que reparta— más una tercera, que
**ningún fondo se repita**. Los 90 ISIN del resto del repositorio se aplicaron como lista negra, así que la
cartera está construida sobre el universo que queda (Kopernik, Sigma, Janus Henderson, Indépendance AM,
Nomura, Japan Deep Value, Federated Hermes, AB, Generali CEE, Mirabaud, Jupiter, Twelve Capital, Man, Nordea
EM Bond). Dos tallas (100k y 200k), 85 % de RV objetivo, 1,6958–1,7030 % de TER.

`cartera-ai-no-indexados-3/` es un séptimo diseño del mismo agente, construido **desde cero** con **dos
condiciones únicas del titular**: nada que reparta dividendos y ningún fondo indexado **ni ya elegido antes**
(los 104 ISIN del repositorio como lista negra). No deriva de las otras carteras y no hereda sus reglas.
Siete motores de RV —global calidad-crecimiento, Europa mid cap, España small/mid, Asia ex-Japón, emergentes,
IA y Japón small/mid— más tres de renta fija (crédito euro IG, high yield y deuda emergente). Dos tallas:
100k (10 fondos, 80 % de RV, 1,5472 %) y 200k (11 fondos con crédito euro a corto plazo, 1,5268 %).

`cartera-ai-no-indexados-4/` es un octavo diseño del mismo agente, también **desde cero** y con las mismas
dos condiciones —nada que reparta dividendos, nada indexado y **ningún fondo ya elegido antes**— pero
aplicadas sobre un catálogo ya muy gastado por las cuatro propuestas hermanas (los **114 ISIN** del
repositorio como lista negra). Lo que queda libre no son fondos globales baratos sino nichos de país,
small caps y un sector, y de ahí la única decisión que se separa de las demás propuestas: **el bloque de
renta variable baja al 70 %** porque el conjunto disponible tiene más riesgo idiosincrático por euro que un
núcleo global. Dos tallas: 100k (10 fondos, 70 % de RV, 1,5961 %) y 200k (11 fondos con small caps de
EE. UU., 1,5851 %). El diseño no hereda ninguna regla del repositorio.

`cartera-ai-no-indexados-5/` es un noveno diseño del mismo agente, también **desde cero** y con las mismas
dos condiciones —nada que reparta dividendos, nada indexado y **ningún fondo ya elegido antes**—, aplicadas
sobre el mismo catálogo ya gastado por las cuatro propuestas hermanas (los **125 ISIN** del repositorio como
lista negra). Comparte con la cartera 4 el 70 % de RV y la razón —lo que queda libre es nicho de país, small
caps y sector—, pero no comparte ni un fondo: el núcleo global pasa a T. Rowe Price Global Value, Europa a
Brandes, EE. UU. a Robeco BP Large Cap, Japón al CROCI de DWS, los emergentes a Ashoka WhiteOak, China a
Schroders, el satélite a Polar Capital Healthcare y la renta fija a Rothschild, DWS y Candriam. **El sesgo
value es deliberado y está escrito**: es lo que deja libre el catálogo cuando se excluyen los indexados y las
casas de crecimiento ya usadas. Dos tallas: 100k (10 fondos, 68,97 % de RV real, 1,3543 %) y 200k (11 fondos
con Valentum, 68,72 %, 1,3417 %).

`cartera-ai-100-index-5/` es un decimotercer diseño independiente del mismo agente, **desde cero** y con las
**tres cláusulas que esta vez pidió el titular**: solo indexados, nada que reparta dividendos y **ningún fondo ya
elegido en ninguna de las carteras del repositorio**. Con el núcleo global barato cerrado (MSCI World al 0,06 %
y al 0,10 %, ACWI, S&P 500, Vanguard regionales: todos son posiciones de otras carteras), la cartera se queda en
**cuatro líneas** y paga 14 pb por no repetir: núcleo MSCI World al 0,20 %, Europa al 0,15 %, emergentes al
0,25 % (MSCI EM SRI Filtered PAB, porque el MSCI EM limpio está usado) y una sola línea de renta fija, el
Bloomberg Global Aggregate cubierto a euros al 0,15 %. **84,95 % de RV real y 0,1930 % de TER** en las dos
tallas. Concesiones escritas: cero small caps, cero inmobiliario, cero ligado a inflación y emergentes con filtro
ESG. Datos del buscador público de la plataforma (2.587 productos), porque el MCP cortó por límite de uso.

`cartera-ai-definitivas-estudiar/cartera-ai-final-conservadora/` es la decimoctava: no nace de cero, sino de
`finance/portfolio/cartera-myinvestor/propuesta-pieza.md` con **un solo cambio** verificado contra el catálogo el 19/11 —el bloque
de crédito corto se consolida en Neuberger (clase I al 0,25 % para el dinero nuevo) y sale M&G (0,47 %, mínimo
1.000 €)—. Doce fondos en trece posiciones, 54,61 % de RV, 509,70 €/año (0,566 %), duración 1,61 y **≈4,8 % de
rentabilidad esperada anual** (2,8 % real) con rango 2,3-6,8 % y sus supuestos escritos. **No es una cartera
«mejor» que el nivel A**: su esperanza es ~0,3 pp inferior a la del indexado puro, y lo que compra con esa
diferencia es la convicción value y la prueba de 2029. Descartados con cifra: Dodge & Cox (mínimo **50.000 €**,
EE. UU. 54,7 %), el REITs institucional al 0,23 % (el que hay ya cuesta 0,17 %) y el ABS de Morgan Stanley al
1,23 %.
`cartera-ai-definitivas-estudiar/cartera-ai-final-atrevida/` es la decimonovena (19/11/2026): nace **desde cero** con solo las condiciones del titular —nada que reparta dividendos, nada de ETF, 110.000 € y 10.000 € en Groupama Trésorerie— y **ninguna regla heredada** (ni 55/45, ni techo de indexado, ni mínimo por línea). Doce fondos al **82,15 % de RV real**, con núcleo indexado al 0,06 % y seis convicciones activas (Brandes, Horos, Fundsmith, Robeco, Hermes Asia, Nomura Japón cubierto), **877,80 €/año (0,798 %)** y **≈6,1 % de esperanza central** (4,0-7,4 %). Su documento escribe en la primera línea que **7-8 % es el escenario favorable y no la mediana**: con las valoraciones de 2026 ninguna cartera diversificada de fondos lo tiene como base, y subir la RV al 100 % solo añadiría +0,18 pp.

`cartera-ai-final-qwen4max/` y `cartera-ai-final-hy3/` se retiraron el **20/11/2026**: las dos ocupaban el mismo
perfil (84,15 % y 84,16 % de RV real), declaraban la misma esperanza (≈6,20 % y ≈6,21 %) y la segunda costaba
**70,90 €/año menos**, así que qwen4max estaba dominada por su propia hermana. Y hy3, la superviviente, está
dominada a su vez por `cartera-definitiva-40/`: **misma renta variable (83,39 % frente a 84,16 %), 92,00 € frente
a 520,60 € por cada 100.000 € invertidos** y 6,06 % frente a 6,21 % de esperanza. El premio entero de hy3 eran
**9.299 € netos a 20 años** —unos 156 €/año— a cambio de que sus tres fondos activos (Brandes, Horos y Nomura,
24.000 €) dieran **≈2,1 pp brutos de alfa** sobre el índice, de los que 1,62 pp se van en pagar su comisión.
Con ellas se va el único representante del perfil «84 % de RV con gestión activa de convicción»: ese perfil queda
servido por `cartera-definitiva-40/` (83,39 %, 92,00 €) y `cartera-ai-100-index-5/` (84,95 %, 193,00 €), y a 6 % bruto de
bolsa la primera es la cartera con **mejor retorno neto esperado de todo el árbol** (5,37 % frente al 5,22 % de
la C5 de `cartera-ai-fondos-2000-lista-deepseek`, que solo gana por encima del 6,93 % bruto). Ese primer puesto
se mide en retorno y coste, **no en diversificación**: `cartera-definitiva-40` tiene el **45,3 % del dinero y el
54,3 % de la renta variable en Estados Unidos** y **diez valores que suman el 15,3 % de la cartera**, porque su
núcleo replica un índice que ya está así; la C5 de deepseek, con 99,5 % de RV, está **peor** en las dos columnas
(62,0 % del dinero en EE. UU. y 33,0 % en tecnología). Reducir la concentración es un tilt con precio, no una
mejora gratuita. Los dos
documentos, con toda su auditoría, siguen en el historial de git.

`cartera-ai-azvalor-consejo/` nace igual de una fuente ajena, pero de una **entrevista de gestor** y no de un
artículo: Beltrán Parages (Azvalor) en *La Pizarra de Andrés* (11/2026), resumida por el titular con la cita
«yo me lo sé porque tengo todo mi dinero aquí». Su primera regla es **todo en equity** y su segunda, que solo un
5 % de los gestores activos bate al índice, así que la cartera pone **60 % en dos indexados** (MSCI World
desarrollado al 0,06 % y Europa al 0,10 %) y **40 % en tres value** que pasan los cuatro filtros del
entrevistado: Azvalor Internacional (39,56 % energía y 20,46 % materiales), Magallanes European y Cobas Large
Cap. **93,17 % de RV real, 709 €/año (0,709 %), caída −37,27 % y ≈6,83 % esperado**, sin renta fija, sin
monetario y sin comisiones de éxito. Lo que la fuente no puede dar está escrito: no compra oro —el fondo de
mineras se descarta—, no entra en China —cero emergentes— y no convierte al índice en enemigo: el 60 % paga el
precio del mercado con 17,67 % de tecnología en la RV, que es exactamente lo que el entrevistado llama caro.

## Reglas del laboratorio

- Las reglas de fondo son las de la cartera viva y aplican aquí igual: **solo clases de acumulación**,
  **un dato, un sitio**, nada se mueve de una carpeta a otra y cada diseño ejecuta por traspaso entre
  fondos armonizados, nunca por reembolso. Están escritas en [`../portfolio/README.md`](../portfolio/README.md#reglas).
- **Un diseño no se reescribe para actualizarlo.** Si cambia el criterio o el catálogo, nace una carpeta
  nueva con sufijo (`-2`, `-3`…): así se distinguen las dos familias de cinco y por eso `cartera-ai-100-index-5`
  no es una versión de `cartera-ai-100-index`.
- **Promover es mover, no copiar.** El documento sale del laboratorio hacia `finance/portfolio/` y aquí
  queda el rastro en una línea, para que el ranking no apunte a un fichero que ya no existe.
- **Ninguna cifra se consolida.** Ni entre diseños ni contra las carteras vivas: los mismos 100.000 €
  aparecen en veinte carpetas y no se suman en ninguna.

## Estado a 26/11/2026

- **`cartera-ai-azvalor-consejo` (20/11/2026, sin ejecutar):** una cartera de 100.000 € traducida de la entrevista a Beltrán Parages (Azvalor, *La Pizarra de Andrés*, 11/2026). **60 % indexado** (45 % iShares Developed World al 0,06 % + 15 % Fidelity MSCI Europe al 0,10 %) y **40 % en tres value** (20 % Azvalor Internacional al 1,88 %, 10 % Magallanes European al 1,95 % y 10 % Cobas Large Cap al 0,96 %) — **el índice es el edificio y el 40 % es la pieza**, con un listón de 1,42 pp/año de alfa bruto y 36.487 € de pérdida a 20 años si no lo alcanza —. **93,17 % de RV real**, **709,00 €/año (0,709 %)**, caída de manual −37,27 % (−37.268 €), **≈6,83 % esperado** (cubre comisión 6,575 %; cero alfa bruto 6,058 %; 100 % índice 6,625 %) y 374.856 € a 20 años. **Cero renta fija, cero monetario, cero emergentes, cero comisiones de éxito**, 5/5 clases de acumulación verificadas en el MCP. Descartados con número: Cobas Internacional (2,33 % y soft close), Cobas Selección (2,05 %), Azvalor Managers (2,32 %), Azvalor Iberia (1,91 %), Magallanes Iberian (1,80 %), Vanguard Global Stock (0,18 %), BGF World Mining (2,06 % y reparte) y Allianz Metals (1,85 %). Prueba de alfa del bloque activo fechada el 30/11/2031 con umbral de 1 pp/año. Pendientes: si los 100.000 € son invertibles, tolerancia al −37 %, aportaciones y fecha de ejecución.

- **`cartera-ai-final-atrevida` (19/11/2026, sin ejecutar):** `110k.md`. Desde cero, 110.000 € con 10.000 en Groupama: **12 fondos**, **82,15 % de RV real**, **877,80 €/año (0,798 %)**, caída de manual −33,4 % (−36.733 €) y **≈6,1 % esperado** (4,1 % real; rango 4,0-7,4 %). **13 órdenes en una sesión**, con Brandes atado a su mínimo de 10.000 €. Descartados con número: Magallanes (peor que Brandes en 3A y 5A), T. Rowe (solapa), Cobas Large Cap (69,3 % de RV), Ashoka EM (USD sin cubrir), CROCI Japón (yen sin cubrir), el Agg 1-5Y (TIR 2,6 %), el bono emergente (6,7 % de vol) y el cat bond (8 días). Pendientes: horizonte del titular, si el monetario es permanente y si habrá aportaciones.

- **`cartera-ai-final-conservadora` (19/11/2026, sin ejecutar):** `100k.md`. La cartera del 18/11 con el
  bloque de crédito consolidado en Neuberger: M&G fuera, su dinero a la **clase I (0,25 %)** y **cero líneas
  con mínimo de 1.000 €**. **12 fondos**, **54,61 % de RV**, **509,70 €/año (0,566 %)**, duración **1,61**
  (−657 € por +100 pb), caída de manual −20.885 € y **≈4,8 % de rentabilidad esperada anual** (2,8 % real;
  rango 2,3-6,8 %, con supuestos y σ ≈9 % escritos). **22 órdenes en dos fases** (16 + 6) y 1.000 €/mes en
  diez líneas mensuales y dos trimestrales. Descartados con número: Dodge & Cox (mínimo 50.000 €), el REITs
  institucional al 0,23 % (el que hay cuesta 0,17 %) y el ABS de Morgan Stanley al 1,23 %. **Pendiente:** sigue
  sin ejecutarse hasta la revisión del titular de la matriz del 18/11.

- **cartera-ai-andres:** dos tallas cerradas el 15/11/2026, sin ejecutar. 100k (11 fondos, 60,3 % de RV,
  0,46 %) y 200k (14 fondos, 60,0 %, 0,51 %), con dos fondos cuyo TER no publica el MCP. Pendientes:
  horizonte real, coste de Myinvestor Value y Kaizen, y si se quiere un bloque de tres acciones.

- **cartera-ai-no-indexados:** dos tallas cerradas el 16/11/2026, sin ejecutar. 100k (10 fondos activos,
  80 % de RV, 1,37 %) y 200k (12 fondos, 80 %, 1,42 %). Pendientes: horizonte, colchón fuera de la cartera y
  cuál de las dos tallas se ejecuta; el coste de Alken lleva comisión de éxito no estimable.

- **cartera-ai-40-max-index:** dos tallas cerradas el 16/11/2026, sin ejecutar. 100k (2 indexados + 7
  activos, 40,0 % indexado, 73,0 % de RV real, 0,79 %) y 200k (2 + 8 con Magallanes Iberia, 73,6 %, 0,80 %).
  Pendientes: horizonte, si el techo del 40 % se queda como restricción permanente y cuál de las dos tallas
  se ejecuta.

- **cartera-ai-100-index:** dos tallas cerradas el 16/11/2026, sin ejecutar. 100k (7 fondos indexados,
  79,9 % de RV real, 0,1065 %) y 200k (8 indexados con Europa al 5 %, 79,9 %, 0,1085 %). Es la cartera más
  barata del repositorio. Pendientes: horizonte, colchón fuera de la cartera, qué talla se ejecuta y si se
  quiere la línea de Europa (que solo existe en la talla de 200k).

- **cartera-ai-no-indexados-3:** dos tallas cerradas el 16/11/2026, sin ejecutar. 100k (7 fondos de RV + 3 de
  RF, 80 % de RV, 1,5472 %) y 200k (11 fondos con Pictet crédito corto, 1,5268 %). Ninguno de los once ISIN
  aparece en otra cartera. Pendientes: horizonte, tolerancia a la caída (−32,6 %), comisión de éxito de
  Okavango y qué talla se ejecuta.

- **cartera-ai-no-indexados-2:** dos tallas cerradas el 16/11/2026, sin ejecutar. 100k (9 fondos de RV + 3 de
  RF, 85 % de RV, 1,6958 %) y 200k (11 + 3 con Mirabaud e India, 85 %, 1,7030 %). Ninguno de los 14 fondos
  aparece en otra cartera del repositorio. Pendientes: horizonte, tolerancia a la caída (−38 %), coste real de
  las tres comisiones de éxito y qué talla se ejecuta.

- **cartera-ai-no-indexados-4:** dos tallas cerradas el 16/11/2026, sin ejecutar. 100k (7 fondos de RV + 3 de
  RF, 70 % de RV, 1,5961 %) y 200k (8 + 3 con small caps de EE. UU., 1,5851 %). Ninguno de los once ISIN
  aparece en otra cartera. Pendientes: horizonte, tolerancia a la caída (−27,9 %), el 18,7 % de caja de
  PIMCO y qué talla se ejecuta.

- **cartera-ai-no-indexados-5:** dos tallas cerradas el 16/11/2026, sin ejecutar. 100k (7 fondos de RV + 3 de
  RF, 68,97 % de RV real, 1,3543 %) y 200k (8 + 3 con Valentum, 68,72 %, 1,3417 %). Ninguno de los once ISIN
  aparece en otra cartera. Pendientes: horizonte, tolerancia a la caída (−28,5 %), las comisiones de éxito de
  Polar y Valentum, el desfase semestral de Japón y qué talla se ejecuta.

- **cartera-ai-100-index-2:** dos tallas cerradas el 16/11/2026, sin ejecutar. 100k (6 indexados regionales +
  3 de RF, 79,79 % de RV real, 0,1113 %) y 200k (mismos 6 + 4 de RF con deuda emergente, 79,79 %, 0,1128 %).
  Ninguno de los diez ISIN aparece en otra cartera. Pendientes: horizonte, tolerancia a la caída (−32,5 %),
  las tres concesiones de la condición 3 (núcleo en cinco regiones, EPRA al 0,34 %, cero small caps), la
  relectura de `management_type` por MCP cuando el límite se reponga y qué talla se ejecuta.

- **cartera-ai-rock-index-value-todo:** una talla cerrada el 16/11/2026, sin ejecutar. 100.000 € con Rock intacta al 30 %, monetario de 14.000 € en dos peldaños y trece fondos activos: 55,5 % de RV real, 0,615 % de coste total, −21.184 € de caída. Pendientes: que Rock se quede como decisión estable, dimensionar el colchón contra gastos reales y qué se hace con la aportación nueva.

- **cartera-ai-rock-desmontado:** una talla, 90.000 € invertibles y 1.000 €/mes, 55,31 % de RV real,
  **236,10 €/año (0,236 %)** y **69,4 % de indexado** (nivel A). **Desbloqueada y no adoptada el 18/11/2026**:
  el titular eligió el nivel C —«el indexado como pieza»— y vive en `finance/portfolio/cartera-myinvestor/propuesta-pieza.md`
  (38,3 % de indexado, 529,90 €/año). Este documento queda como **la alternativa barata** con su número: son
  293,80 €/año menos y +0,53 pp/año de alfa de empate a favor del activo. Parece muerta y está viva: es contra
  la que se mide la cartera vigente en la revisión de octubre de 2029. Pendiente: confirmar que el desmontaje
  de Rock se registra como traspaso al monetario puente.

- **cartera-ai-100-index-3:** dos tallas cerradas el 16/11/2026, sin ejecutar. 100k (5 indexados regionales + 2
  de RF, 79,57 % de RV real, 0,2086 %) y 200k (los mismos siete fondos y pesos, 0,2086 %). Ninguno de los siete
  ISIN aparece en otra cartera, ni por ISIN ni por fondo (62 clases hermanas de fondos usados descartadas por
  patrimonio). Pendientes: horizonte, tolerancia a la caída (−32,4 %), las concesiones de la lista negra
  (Norteamérica al 0,23 % y Japón con 4,45 % de *tracking error*, cero small caps y cero ligado a inflación), la
  relectura de `management_type` por MCP cuando el límite se reponga y qué talla se ejecuta.

- **cartera-ai-100-index-4:** dos tallas cerradas el 16/11/2026, sin ejecutar. 100k (núcleo ACWI al 67 % + 2
  convicciones + 2 de RF, 85,16 % de RV real, 0,3771 %) y 200k (los mismos cinco fondos y pesos, 0,3771 %).
  Ninguno de los cinco ISIN aparece en otra cartera, ni por ISIN ni por fondo (75 clases hermanas descartadas por
  `patrimonio`). Pendientes: horizonte (asumido 15+ años), tolerancia a la caída (−35,5 %), las concesiones
  (cero small caps, cero inflación, cero inmobiliario y Japón sin línea por no nombrar su índice la ficha), la
  relectura de `management_type` por MCP cuando el límite se reponga y qué talla se ejecuta.

- **cartera-ai-100-index-5:** dos tallas cerradas el 16/11/2026, sin ejecutar. 100k (4 fondos: núcleo MSCI World
  al 60 %, Europa al 12 %, emergentes al 13 % y agregado global cubierto a euros al 15 %; 84,95 % de RV real,
  0,1930 %) y 200k (los mismos 4 fondos y pesos, 0,1930 %). Ninguno de los cuatro ISIN es posición de otra
  cartera, ni su clase hermana (comprobado por ISIN, por `patrimonio` y por nombre). Pendientes: horizonte
  (asumido 15+ años), tolerancia a la caída (−35,5 %), las concesiones (cero small caps, cero inmobiliario, cero
  ligado a inflación y emergentes con filtro ESG), la relectura por MCP cuando el límite se reponga y qué talla
  se ejecuta.

- **cartera-definitiva-40 (19/11/2026, sin ejecutar):** `100k.md`. **La cartera de referencia a los 40**: **6
  fondos** (iShares Developed World S 58 % al **0,06 %**, iShares Emerging Markets S 10 %, Fidelity MSCI Europe 10 %, Vanguard Global
  Small-Cap 6 %, iShares Global Aggregate 1-5Y EUR H 11 % e iShares Euro Gov Inflation-Linked 5 %), **83,39 % de RV real**, **92,00 €/año (0,092 %)**,
  caída **−33,85 % (−33.854 €)**, **cero comisiones de éxito** y **≈6,06 % esperado** (3,97-8,15 %). **6 órdenes
  en dos cortes** (09:00 y 16:00), liquidación de 4 días en el núcleo. **Backtest de la estructura en cinco años
  reales** (`backtest_portfolio`, 2021-2026, con las clases antiguas de los mismos índices): **+7,84 % anualizado,
  9,88 % de volatilidad, −12,84 % de máxima caída y 2022 en −11,79 %**. Variantes escritas: 70/30 (99,30 €,
  −28,74 %, 5,61 %) y 100/0 (93,00 €, −39,74 %, 6,70 %). Plan completo: colchón fuera, aportación automática
  (1.000 €/mes → ≈1,31 M € a los 67), rebalanceo por bandas y glide de edad desde los 55. Descartados con número:
  Vanguard World (78 €/año más), Fidelity World (26 € más), REITs (5 % que solo añadían volatilidad), Euro IG
  (crédito en la línea que es colchón), agregado global completo (duración 6-7, cayó en 2022), ligado a inflación
  (0,08 pp de esperanza por 5 % de peso) y las líneas de país (tilt, no diversificación). Pendientes: confirmar
  horizonte 15+ años, colchón fuera y aportación mensual; el TER real de la clase S en pantalla (KID 0,06 % frente
  a `management_fee` 0,09 % de la ficha) y la fecha de ejecución.

- **`cartera-ai-c4-defensiva` (22/11/2026, sin ejecutar):** `100k.md`. La más defensiva del contenedor de estudio: **34,06 % de RV real**, **44,00 % de indexado** (32 % Vanguard Global Stock + 12 % iShares Euro Government), tres alternativos descorrelacionados (market neutral, retorno absoluto y cat bonds) y colchón de deuda pública. **607,60 €/año (0,6076 %)** con cuatro comisiones de éxito, caída −15,07 % y ocho órdenes en una sesión. Promovida desde la C4 de `cartera-ai-fondos-2000-lista-deepseek`; las otras nueve de las dos familias de cinco quedan retiradas. Pendientes: horizonte, aportaciones y aprobación del % de RV.

- **`cartera-ai-hy4-definitiva` (22/11/2026, sin ejecutar):** `100k.md`. ⚠️ Finalista, pendiente de la revisión del titular y sin órdenes. Cribado de las tres variantes de `cartera-ai-fondos-2000-lista*`. 35 % indexado, 65,5 % de RV real, 537,10 €/año (0,537 %) y sin comisiones de éxito. Pendiente: aprobación del % de RV y colchón.

- **`cartera-ai-neon` (22/11/2026, sin ejecutar):** `110k.md`. 110.000 € a 15 años vista (40 → 55 años), diseñada para aportar de golpe (`9oM4CFH5usw`) o rebalancear `finance/portfolio/cartera-myinvestor/cartera-actual.md` (100.000 € actuales + 10.000 € nuevos = 110.000 €, 0 € de impuestos) usando exclusivamente 13 fondos verificados en `finance/fondos-myinvestor/`. **32,73 % de indexado como pieza** (36.000 € al 0,12 %), **40,00 % de convicción activa value/ex-US/SMID** (44.000 € al 1,63 %) y **27,27 % de escudo defensivo y descorrelacionado** (30.000 € al 0,57 %). **72,28 % de RV real**, **73,63 % de la RV fuera de EE. UU.**, **39,85 % en Small & Mid Caps**, **top 10 US tech reducido al 4,85 % del total (6,71 % de la RV)**, caída real en **2022 de −5,10 %** (Bloque 3 en **+0,45 %**), **933,90 €/año (0,85 %)** —o **848,30 €/año (0,77 %)** en variante 0 % éxito con `LU1935059029` y `ES0112618006`— y **≈6,50 % neto esperado** (282.903 € nominales / 201.142 € reales a 15 años). Pendiente: elegir Modo A (de golpe) o Modo B (traspaso desde `cartera-actual.md`) y versión titular o variante 0 % éxito.

- **`cartera-ai-carbon` (25/11/2026, sin ejecutar):** `100k.md`. Auditoría forense de `finance/portfolio/cartera-myinvestor/cartera-actual.md` y diseño agresivo anti-burbuja a 15 años (2026 → 2041) para los **100.000 € libres para invertir** (+ **10.000 € intocables aparte en `Groupama Trésorerie IC`** = **110.000 €** totales) en **12 fondos verificados** de `finance/fondos-myinvestor/` con **0/12 comisiones de éxito** y **cero monetarios duplicados**: **40,00 % de indexado s/100k (36,36 % s/110k)** (40.000 € al 0,123 % con Japón cubierto a EUR al 0,20 % `IE00BYX5NH74`), **44,00 % de convicción activa ortogonal y cuellos de botella físicos** (44.000 € al 1,455 % en `Robeco BP Global Premium`, `M&G European Strategic Value`, `Palm Harbour Global Value`, `Robeco QI EM Active` y `First Sentier Global Listed Infrastructure` `IE00BYSJTY39`) y **16,00 % de escudo antiestanflación y pólvora seca** (16.000 € al 0,543 % en `Cobas Renta FI`, `DWS Floating Rate Notes` y `Twelve Cat Bond`, saliendo por completo de `Gamma`, `Carmignac` y `DNCA`). **84,14 % de RV real s/100k (76,49 % s/110k)**, **65,17 % de la RV fuera de EE. UU.**, **top 10 US tech al 5,33 % de 110k**, caída real en **2022 de −5,59 % s/100k (−5,05 % s/110k, Bloque 3 en +0,21 %)**, **776,10 €/año s/100k (783,10 € = 0,712 % s/110k)**, **≈6,80 % neto esperado s/100k** y **15 traspasos libres de IRPF + 2 suscripciones** (`0` órdenes sobre `Groupama`). Pendiente: verificar boletas de `IE000ZYRH0Q7`/`LU1935059029`/`IE00BYSJTY39` y fijar aportación mensual.

- **`cartera-ai-neon-2` (25/11/2026, sin ejecutar):** `100k.md`. Auditoría de `finance/portfolio/cartera-myinvestor/propuesta-actual.md` y diseño agresivo desde cero a 15 años (2026 → 2041) para los **100.000 € libres para invertir** (+ **10.000 € intocables aparte en `Groupama Trésorerie IC`** = **110.000 €** totales), construido con **0/13 solape respecto a `cartera-ai-neon/`** (los 18 fondos / 25 ISIN de `neon` excluidos por ISIN y clase hermana) tras barrer las 2.007 fichas de `finance/fondos-myinvestor/`. **43,00 % de indexado s/100k (39,09 % s/110k)** (`43.000 €` al `0,160 %`: `Vanguard Global Stock`, `iShares Europe ex-UK`, `iShares UK`, `Fidelity MSCI Japan EUR Hedged` y `Fidelity MSCI EM`), **42,00 % de convicción activa ortogonal RV con 0 % éxito** (`42.000 €` al `1,492 %`: `Robeco BP Global Premium`, `Brandes European Value`, `GS Global Small CORE`, `Wellington Enduring Infrastructure` y `Ashoka WhiteOak India`) y **15,00 % de escudo antiestanflación y pólvora seca** (`15.000 €` al `0,590 %`: `EDM Renta R`, `UBAM USD Floating Rate Notes AHC EUR` y `GSQuartix Modified Strategy Bloomberg Commodity`, en **+4,59 % en 2022**; variante opcional market-neutral con `Jupiter Merian GEAR`). **84,24 % de RV real s/100k (76,58 % s/110k)**, **68,88 % de la RV fuera de EE. UU.**, **36,78 % SMID**, **top 10 US tech al 4,24 % s/100k (3,85 % s/110k)**, caída real en **2022 de −5,74 % s/100k (−5,22 % s/110k)**, **784,10 €/año s/100k (791,10 € = 0,719 % s/110k) y 0/13 comisiones de éxito**, **≈6,90 % neto esperado s/100k** (`271.904 €` a 15A; `200.393 €` en test neutro sin alfa) y **16 traspasos libres de IRPF + 1 suscripción** (`0` órdenes sobre `Groupama`, puente Rock vía `EDM Renta R`), con escalados a `97k` y `90k`. Pendiente: confirmar talla (`100k` con 10k nuevos, `97k` o `90k`), elegir bloque 3 titular o variante market-neutral y revisar en pantalla los mínimos de `Brandes` (`10k USD`), `GS Small CORE` (`5k €`) y `Wellington` (`5k USD`).

- **`cartera-ai-definitiva-final` (26/11/2026):** el contenedor del ranking. Tras `auditoria-ranking.md` se retiraron `opcion-b.md` (#6), `opcion-e.md` (#5), `opcion-c.md` (#4) y `opcion-d.md` (#2, por llevar `0 %` de gestión activa en bolsa) —todas conservadas en el historial de git— y la **#1 Opción A** (`8,71/10`, 7 fondos, `81,03 %` de RV, `0,273 %` de TER, `212.632 €` en test neutro) se promovió el mismo día a `finance/portfolio/cartera-myinvestor-propuesta/`. Aquí queda **Option 0** (`7,81/10`, 13 fondos, `84,24 %` de RV, `0,784 %` TER, 2022 en `−5,74 %`) como finalista en estudio, sin ejecutar.

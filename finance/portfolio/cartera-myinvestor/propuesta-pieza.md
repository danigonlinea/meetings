---
title: "Cartera final: 100.000 €, 38,3 % de indexado como pieza y 23,3 % de convicción activa"
date: 2026-11-18
type: portfolio-proposal
category: finance
tags: [cartera, final, pieza-no-edificio, 38-indexado, value, magallanes, horos, cobas-large-cap, renta-fija, rock-desmontado, traspaso, myinvestor, aportaciones]
status: final
related:
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
  - finance/portfolio/cartera-myinvestor/README.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-rock-desmontado/100k.md
  - finance/portfolio/README.md
---

# Cartera final — 100.000 €, 18/11/2026

> **La decisión en una línea.** Los 100.000 € (90.000 € invertibles + 10.000 € de colchón) se quedan en
> **trece fondos**: **34.500 € de índice (38,3 %, a 0,12 % de media)**, **21.000 € de convicción activa en
> renta variable (23,3 %, a 1,59 %)** y **34.500 € de gestión de crédito y liquidez (38,3 %, a 0,38 %)**.
> **54,6 % de renta variable** en look-through, **529,90 €/año (0,530 %)** de coste total y una caída de
> manual de **−20.885 €**. Rock se desmonta por traspaso (0 € de impuestos).
>
> **Estado: cerrada y final el 18/11/2026, con la revisión del titular pendiente.** No queda ninguna decisión
> de diseño abierta —vehículos, pesos, coste, órdenes, aportaciones, bandas, escenarios y la prueba de 2029
> están escritos—. Pero el titular pidió **revisarla otro día** antes de ejecutarla: **ninguna orden de §9 se
> lanza hasta esa revisión**. Si alguien —persona o agente— abre esta cartera para actuar sobre ella, lo
> primero que tiene que decir es justo eso: **está pendiente de revisión y no se ejecuta todavía**.
>
> **Qué pregunta responde.** `cartera-ai-definitivas-estudiar/cartera-ai-rock-desmontado/100k.md` §14 dejó el diseño aparcado con una sola
> incógnita —cuánto indexado— y tres niveles. Esta cartera es **el nivel C**, el que el titular pidió: el
> índice como **pieza**, no como edificio. Sustituye como vigente a `propuesta-actual.md` (04/11) y retira
> `propuesta-ai.md` (16/11); las dos siguen en el historial de git.
>
> **Método.** Fichas del catálogo MyInvestor por MCP el 18/11/2026 (`get_funds` por ISIN de los trece fondos y
> de los ocho que salen): TER, `alloc_equity`, `distributing`, mínimos, cortes, avisos y top países y
> sectores. Saldos y composición de Rock: `cartera-actual.md` (30/10/2026). Criterio del 55 %:
> `propuesta-actual.md` §2 (04/11/2026). Datos externos con fuente y fecha donde se citan. Los ISIN validan
> dígito de control.
>
> **No es asesoramiento financiero.** La decisión y la ejecución son del titular.

---

## 0. Lo que cambia respecto a lo que hay hoy

| | Hoy (30/10/2026) | **Esta cartera** |
| --- | ---: | ---: |
| Posiciones | 18 (8 manuales + colchón + 9 de Rock) | **13 + colchón** |
| Renta variable (look-through) | 31,6 % | **54,6 %** |
| Indexado | 31.000 € (34,4 %), pero todo dentro de una cartera automatizada al 0,41 % | **34.500 € (38,3 %)** en cinco fondos al 0,06-0,30 % |
| Convicción activa de RV | 5.000 € (cuatro posiciones de 1.000-2.000 €, sin gestión real) | **21.000 €** en tres gestoras con peso |
| Gestión de crédito | 55.000 €, de los que 33.000 € pagan comisión de éxito | **34.500 €**, cero comisiones de éxito |
| Coste | 678,20 €/año (0,678 %) | **529,90 €/año (0,530 %)** |
| Duración de la RF | 3,83 | **1,54** |
| Coste de +100 pb | −2.356 € | **−630 €** |
| Caída tipo 2008 | −13.200 € (−14,7 %) | **−20.885 € (−23,2 %)** |

---

## 1. El mandato, escrito antes de tocar el catálogo

| Lo que pediste (18/11/2026) | Cómo se cumple | Qué cuesta |
| --- | --- | --- |
| **Una cartera, no diecisiete** | Un solo documento vigente en la carpeta, con las órdenes dentro. Las otras propuestas de la carpeta se retiran del árbol (§15) | Nada; se pierden alternativas que ya estaban decididas |
| **El indexado como una pieza, no como el edificio** | **38,3 %** de los 90.000 € invertibles en índice; el 61,7 % restante en gestores con nombre y peso real | **+293,80 €/año** frente al nivel A (69,4 % indexado): el índice deja de ser la mayoría |
| **La más óptima con ese criterio** | Dentro del techo, el índice va donde es más barato y el activo solo donde el índice no llega (§3) | El bloque activo debe batir a su índice en **+0,53 pp/año netos** (o **+1,49 pp** sobre los 21.000 € de convicción: §6) solo para empatar |
| **Preparada para lo que viene** | Seis escenarios con la orden concreta (§11), bandas de rebalanceo (§12), plan de 1.000 €/mes (§10) y la regla que invalida el diseño si el activo no paga (§13) | Nada: es trabajo de revisión, no de coste |
| **100.000 €** | 90.000 € invertibles + 10.000 € de colchón fuera de la base | El colchón no renta: 0,07 % |

**Lo que no he aplicado**, y conviene decirlo: ni tope de número de fondos, ni mínimo por posición, ni veto a
las comisiones de éxito como principio, ni sesgo geográfico predefinido, ni «cero ETF» como eslogan. Se
compran clases de acumulación y solo fondos porque un reparto tributa cada año y un ETF no admite traspaso:
eso es coste, no principio (§15 lo pone en euros).

**Base.** `cartera-actual.md` (30/10/2026): 60.000 € manuales en ocho fondos + 30.000 € de Rock, con 10.000 €
de Groupama fuera. Si los 7.000 € de aportación nueva del `README.md` ya están en la cuenta, el delta se
resuelve aparte sin tocar el diseño (§14).

---

## 2. La cartera

| # | Bloque | Fondo | ISIN | € | % de 90k | TER | €/año | RV |
| --: | --- | --- | --- | --: | --: | --: | --: | --: |
| 1 | **Núcleo RV mundo** (índice) | iShares Developed World Index (IE) S Acc EUR | IE000ZYRH0Q7 | 17.000 | 18,9 % | 0,06 % | 10,20 | 99,3 % |
| 2 | **RV emergentes** (índice) | iShares Emerging Markets Index (IE) S Acc EUR | IE000QAZP7L2 | 6.000 | 6,7 % | 0,16 % | 9,60 | 99,3 % |
| 3 | **RV small caps** (índice) | Vanguard Global Small-Cap Index EUR Acc | IE00B42W4L06 | 4.000 | 4,4 % | 0,29 % | 11,60 | 99,9 % |
| 4 | **Activos reales** (índice) | iShares Developed Real Estate Index (IE) D Acc | IE00BDRK7P73 | 3.500 | 3,9 % | 0,17 % | 5,95 | 98,9 % |
| 5 | **RF corta** (índice) | iShares Global Aggregate 1-5Y Bond S Acc EUR H | IE0004ZP1ND3 | 4.000 | 4,4 % | 0,08 % | 3,20 | 0 % |
| 6 | **Value Europa** (activo) | Magallanes European Equity M FI | ES0159259011 | 9.000 | 10,0 % | 1,81 % | 162,90 | 93,1 % |
| 7 | **Value global small/mid** (activo) | Horos Value Internacional FI | ES0146309002 | 6.000 | 6,7 % | 1,90 % | 114,00 | 90,8 % |
| 8 | **Value global large/mid** (activo) | Cobas LUX – Cobas Large Cap Fund P Acc | LU1598720172 | 6.000 | 6,7 % | 0,96 % | 57,60 | 69,3 % |
| 9 | **RF flexible defensiva** (activo) | Cobas Renta FI | ES0119207001 | 6.000 | 6,7 % | 0,33 % | 19,80 | 14,5 % |
| 10 | **Crédito corto IG** (activo) | Neuberger Short Duration Euro Bond U | IE00BL1GVT98 | 11.000 | 12,2 % | 0,38 % | 41,80 | 0 % |
| 11 | **Crédito corto IG** (activo) | M&G (Lux) Short Dated Corporate Bond A Acc | LU1670718219 | 6.000 | 6,7 % | 0,47 % | 28,20 | 0 % |
| 12 | **Titulizaciones** (activo) | Aegon European ABS Fund A EUR Acc | IE00BG226Z29 | 8.000 | 8,9 % | 0,66 % | 52,80 | 0 % |
| 13 | **Liquidez táctica** (activo) | DWS Euro Ultra Short Fixed Income NC | LU0080237943 | 3.500 | 3,9 % | 0,15 % | 5,25 | 0 % |
| | **Total invertible** | **13 fondos** | | **90.000** | **100 %** | **0,581 %** | **522,90** | |
| *Fuera* | Colchón | Groupama Trésorerie IC | FR0000989626 | 10.000 | — | 0,07 % | 7,00 | 0 % |
| | **Coste del ahorro completo** | | | **100.000** | | **0,530 %** | **529,90** | |

**Reparto estricto por `alloc_equity`:** RV **49.148,80 € (54,61 %)** · RF y caja **40.851,20 € (45,39 %)**.

### 2.1 Los tres bloques, con la etiqueta correcta

«Activo» y «pasivo» son etiquetas de **vehículo**, y usarlas como si midieran la apuesta hace que la cartera
parezca otra cosa. Lo que hay, medido por lo que cada euro tiene que hacer:

| Bloque | € | % de 90k | TER medio | Qué es |
| --- | --: | --: | --: | --- |
| **Índice** | 34.500 | 38,3 % | 0,118 % | Beta comprada al precio mínimo: mundo, emergentes, small caps, inmobiliario y una columna de RF |
| **Convicción activa de RV** | **21.000** | **23,3 %** | **1,593 %** | Las tres gestoras donde se apuesta a que el value paga: Magallanes, Horos, Cobas Large Cap |
| **Gestión de crédito y liquidez** | 34.500 | 38,3 % | 0,379 % | El bloque defensivo entero: Neuberger, M&G, Aegon, Cobas Renta y DWS |

La apuesta activa de verdad son **21.000 € (23,3 %)**, no 55.500 €. El resto de lo no indexado es gestión de
crédito a 0,15-0,66 %, que es otro oficio y mucho más barato. Las dos cifras conviven a propósito: **61,7 %**
dice cuánto capital no replica un índice; **23,3 %** dice cuánto depende del acierto de tres personas.

---

## 3. Dónde va el índice y dónde va el activo

La regla no es «un 38 %», es **qué papel cumple cada euro**. El índice compra lo que el índice hace mejor:
beta ancha, al precio más bajo del catálogo. El activo compra solo lo que un índice no puede dar.

| Papel | Vehículo | Por qué ahí |
| --- | --- | --- |
| Beta del mundo desarrollado | iShares Developed World, 0,06 % | 1.200 empresas de 23 países a 6 pb. Ningún gestor puede batir su propio índice por menos de lo que cuesta intentarlo (SPIVA Europe mid-2026: **97,65 %** de los fondos globales en euros no baten su índice a 10 años) |
| Emergentes | iShares EM, 0,16 % | El bloque más barato del mundo (10,2x) y el más difícil de gestionar activo: 43 % tecnología, Taiwán 28 % + Corea 21 % |
| Prima de tamaño | Vanguard Global Small-Cap, 0,29 % | 4.100 empresas que no están en el núcleo. **Tilt declarado** (§3.2) |
| Renta de alquiler | iShares Developed Real Estate, 0,17 % | Activo real, no bono; 98 % inmobiliario. **Tilt declarado** |
| Columna de la RF | iShares Global Agg 1-5Y EUR H, 0,08 % | Duración corta, miles de emisores, sin riesgo de gestor: es el suelo del bloque defensivo |
| Value Europa con gestor | Magallanes European Equity M, 1,81 % | Europa cotiza a 13,6x frente a 18,7x del S&P 500, y el índice europeo pesa 25 % financieros: un gestor concentrado en industria, materiales y consumo compra otra cosa |
| Value global small/mid | Horos Value Internacional, 1,90 % | España 15 %, Brasil 8 %, Canadá 6 %: países que el MSCI World no pondera y el gestor sí busca |
| Value global large/mid barato | Cobas Large Cap P, 0,96 % | El fondo activo más barato del catálogo en su familia: 96 pb por una cartera value con 18 % energía y 15 % salud |
| Defensa en el año malo | Cobas Renta, 0,33 % | El único vehículo del catálogo que **ganó en 2022** (+3,89 %) con volatilidad del 2,9 % |
| Filtro de emisor en crédito | Neuberger 0,38 % + M&G 0,47 % | El índice compra todos los emisores IG a ese vencimiento; un equipo de crédito descarta los vulnerables. Es el único papel donde el reparto de tareas es a favor del gestor |
| Crédito fuera del corporativo | Aegon European ABS, 0,66 % | 58 % ABS + 35 % RMBS europeas: un activo que el Agg 1-5Y solo tiene al 2 % |
| Liquidez con algo de cupón | DWS Euro Ultra Short, 0,15 % | Segunda rueda de liquidez, duración ≈0 |

**Por qué el índice no es el edificio entero, con el número delante.** Un MSCI World al 100 % no es una
posición neutra en 2026: el top-10 del S&P pesa entre **39 % y 41 %** del índice frente al 18-23 % histórico, y
la tecnología es el **32,1 %** del fondo (ficha de hoy). Poner los 90.000 € ahí es comprar una sola apuesta
—las diez mayores compañías del mundo— con el envoltorio de la diversificación. La cartera *index-first* del
repo (`cartera-ai/100k.md`) es la más barata y sigue siendo válida; **no es esta**, porque el titular ha
decidido que ese riesgo de concentración se reparte.

### 3.1 Geografía de la renta variable: 36,7 % en EE. UU.

Estimación por suma de los `top_regions` de cada ficha, ponderados por su exposición real a bolsa, sobre
49.148,80 € de RV. Es un **suelo de precisión**: dentro del 8,9 % sin desglosar está el 30,7 % de «otros» de
Cobas Large Cap.

| Región | € de RV | % de la RV | Referencia: índice global |
| --- | --: | --: | --: |
| **Estados Unidos** | 18.046 | **36,7 %** | ~63-72 % |
| **Europa** (Francia, Alemania, Reino Unido, Suecia, España, Italia, Suiza) | 15.875 | **32,3 %** | ~15 % |
| **Emergentes** (Brasil, China, India, Taiwán, Corea) | 7.005 | **14,3 %** | ~10 % |
| Japón | 1.790 | 3,6 % | ~5 % |
| Canadá | 1.023 | 2,1 % | ~3 % |
| Pacífico ex-Japón (Australia, Singapur, Hong Kong) | 1.055 | 2,1 % | ~2 % |
| Sin desglosar en las fichas y liquidez de los fondos | 4.362 | 8,9 % | — |

**Es un sesgo deliberado y se puede medir: −26 a −35 pp de EE. UU. y +17 pp de Europa** frente a un índice
global. El argumento es de valoración (13,6x frente a 18,7x) y de concentración del índice. El precio: si el
value europeo se queda atrás durante años, son **21.000 €** expuestos a esa tesis y ninguna otra línea lo
compensa.

### 3.2 Los dos tilts, escritos como apuestas

| Tilt | € | % de la RV | % en el MSCI World | Lo que se paga |
| --- | --: | --: | --: | --- |
| **Inmobiliario desarrollado** | 3.500 | **7,1 %** | ~2 % | 3,5 veces el peso del índice, y ya está dentro del fondo mundial: es sobreponderación pura. Su 5A es **+0,9 %**: una década plana |
| **Small caps** | 4.000 | **8,1 %** | 0 % en el MSCI World (~14 % en un IMI) | 0,29 % de TER (el indexado más caro del bloque), 61 % EE. UU. y solape con el núcleo en las grandes |

No son «diversificación»: son dos apuestas pequeñas y conscientes. La primera compra activos reales; la
segunda, prima de tamaño. Si no se quieren, §14.1 las quita con su número.

---

## 4. Cuánta renta variable, y por qué 54,6

El % de RV es tolerancia al riesgo y no se puntúa. Se mantiene el nivel ya aceptado por escrito el 04/11/2026
—**la misma factura en euros, no el mismo porcentaje**—: el suelo conductual aceptado era −22.700 € sobre
97.000 €; aquí la base invertible son 90.000 € y la caída de manual es **−20.885 €**, **1.815 € menos**.

| RV | RF | Caída 2008 | € sobre 90.000 |
| --: | --: | --: | --: |
| 45 % | 55 % | −19,6 % | −17.680 |
| 50 % | 50 % | −21,5 % | −19.350 |
| **54,6 % (esta)** | **45,4 %** | **−23,2 %** | **−20.885** |
| 60 % | 40 % | −25,2 % | −22.680 |
| 65 % | 35 % | −27,1 % | −24.345 |

Caída = −(40 % × RV + 3 % × RF), la fórmula de la casa para un escenario tipo 2008.

**Por qué no 60 %, que es la misma cifra en euros que el suelo aceptado.** Porque aquí el 61,7 % del capital
está en ocho fondos de siete gestoras: el riesgo que no sale en la fórmula es el idiosincrático, y la cartera
ya paga ese precio en concentración de estilo (§5). Subir 5 pp más de RV sería mover dos riesgos a la vez —más
beta y más gestor— para rascar 0,4 pp de retorno esperado. Si algún día se quiere ese escalón, se sube con un
argumento escrito, no de rebote.

---

## 5. Por qué cada fondo, con la pega en la misma fila

| Fondo | El dato (ficha 18/11) | La pega, dicha |
| --- | --- | --- |
| **iShares Developed World 0,06 %** | RV 99,3 % · EE. UU. 71,7 % · tecnología 32,1 % · mínimo 0 € · corte 09:00 · **sin 3A/5A** | **Es beta pura y está concentrado por construcción**: 72 % EE. UU. y 32 % tecnología. No protege de nada. La clase S es la más barata del catálogo pero no publica historial a 3-5 años (§9.1: comprobar acceso y plan B) |
| **iShares Emerging Markets 0,16 %** | RV 99,3 % · Taiwán 28,2 % + Corea 21,1 % + China 18,6 % · tecnología 43,2 % · vol 1A 27,3 % | **Es semiconductores con países alrededor**; sin 3A/5A publicados |
| **Vanguard Global Small-Cap 0,29 %** | RV 99,9 % · 4.100 empresas · 5A +6,1 % · EE. UU. 60,9 % · mínimo 1 € | **El indexado más caro del bloque** y su 5A es peor que el del núcleo: se paga la prima de tamaño, no un historial |
| **iShares Developed Real Estate 0,17 %** | RV 98,9 % · 5A +0,9 % · 2022 −20,1 % · EE. UU. 64,9 % | **Década plana y es bolsa**: cae con los tipos, no protege de ellos |
| **iShares Global Agg 1-5Y 0,08 %** | RF 98,9 % · gobierno 58 % · 1A +0,1 % · cubierto a euros | **Rinde casi nada** porque incluye deuda pública a tipos bajos: su función es amortiguar |
| **Magallanes European Equity M 1,81 %** | RV 93,1 % · 3A +15,1 % · 5A +11,5 % · 2022 **+4,9 %** · vol 3A 12,7 % · mínimo 1 participación | **Es cíclico, no defensivo** (25 % industria y 29 % materiales). Y existe una **clase P al 1,25-1,30 % que no se puede comprar aquí**: en el catálogo solo están la R (1,95 %) y esta M (1,81 %). Son ≈46 €/año perdidos por acceso, no por elección |
| **Horos Value Internacional 1,90 %** | RV 90,8 % · 3A +17,2 % · 5A +12,0 % · vol 3A 10,8 % · mínimo 100 € → **aportación trimestral** | **1,90 % y 9 % en liquidez**; solapa con Magallanes en Francia (20,7 % y 18,6 %) |
| **Cobas Large Cap P 0,96 %** | RV 69,3 % (+30,7 % «otros») · 3A +29,3 % · 5A +18,1 % · SRRI 5 · mínimo 1 € | **El 31 % que no es RV declarada** (ilíquidos/otros, sin desglosar) y su 1A +33,4 %: comprado después de un año excepcional |
| **Cobas Renta 0,33 %** | 57,5 % RF + 14,5 % RV + 28 % liquidez · **2022 +3,9 %** · 3A +8,9 % · mínimo 100 € → **trimestral** | **La línea más floja del diseño**: 28 % de caja, 42 % Alemania y 3,9 % Ghana sostienen una tesis que descansa en un solo año bueno. La primera que saldría si algo no cuadra |
| **Neuberger Short Duration 0,38 %** | RF 99,4 % · corporativo 76,4 % · TIR 4,65 % · duración 1,95 · rating A− · 1A +0,4 % | **12,2 % de la cartera en una sola idea** y 1A plano: el carry que anuncia su TIR no se está cobrando. No es «cuasi-efectivo»: es crédito |
| **M&G Short Dated 0,47 %** | RF 98,8 % · corporativo 49,6 % · 3A +3,2 % · vol 3A 1,5 % · mínimo 1.000 € → **trimestral** | **Cuatro veces el precio del índice** (0,47 % vs 0,08-0,12 %) y **casi el mismo riesgo que el Neuberger**: dos gestores para un papel parecido. Se paga el filtro de emisor, que no se puede auditar desde fuera |
| **Aegon European ABS 0,66 %** | RF 100 % · ABS 57,7 % + RMBS 35,1 % · 3A +4,4 % · 2022 −4,0 % · vol 3A 1,0 % | **La línea más cara del bloque defensivo y la que peor encaja en su papel**: compra tramos no senior (riesgo de crédito y de titulización) y su KID añade riesgo de liquidez. Su escenario ilustrativo da **2,0 % antes de costes y 1,3 % después**: la comisión se lleva un tercio del retorno esperado de esa línea |
| **DWS Euro Ultra Short 0,15 %** | RF 90,9 % · vol 3A 0,38 % · 1A +2,4 % · mínimo 1 € | **No publica TIR ni duración**; 3.500 € para no vender bolsa en el peor día |

**La pega del bloque activo, en una frase:** los tres fondos de RV activa son **value**, y eso no es una
elección de estilo libre sino lo que deja el catálogo cuando se excluyen los fondos de crecimiento que no baten
a su índice neto de comisión (comprobado ficha a ficha el 16/11/2026; el detalle quedó en el historial, commit
`5fae506`). Consecuencia declarada: **no son tres fuentes de riesgo independientes, son una sola apuesta de
factor repartida en tres gestoras** que además comparten geografía (Magallanes y Horos, Francia) y casa (los
dos Cobas suman 12.000 € = 13,3 % de la cartera). Si el value pasa cinco años por detrás, las tres líneas
fallan a la vez. Lo que se compra con los 293,80 €/año de más son **dos primas distintas** —beta de crecimiento
en el índice y value en el activo—, no cuatro.

---

## 6. El precio del mandato: 38 % indexado frente a 69 % y frente a 100 %

| | Hoy (30/10) | Nivel A (`rock-desmontado`) | Nivel B (≈55 %) | **Esta (nivel C)** |
| --- | ---: | ---: | ---: | ---: |
| Indexado | 34,4 % (todo en Rock, 0,41 %) | **69,4 %** | ≈55 % | **38,3 %** |
| Convicción activa de RV | 5,6 % | ≈10 % | ≈20 % | **23,3 %** |
| Renta variable | 31,6 % | 55,3 % | ≈55 % | **54,6 %** |
| Coste/año (100k) | 678,20 € | **236,10 €** | ≈420 € | **529,90 €** |
| Caída de manual | −13.200 € | −21.118 € | ≈−21.100 € | **−20.885 €** |
| Duración RF | 3,83 | 2,30 | ≈2,3 | **1,54** |
| Líneas | 18 | 12 | ≈12 | **13** |

**Lo que hay que decir sin adornos.** Si el criterio fuera solo coste y esperanza matemática, **ganaría el
nivel A**: 293,80 €/año menos y toda la evidencia de SPIVA de su lado. Esta cartera no es «mejor» en ese
sentido: es la mejor versión del criterio que has pedido. Y ese criterio tiene dos facturas verificables:

- **Coste:** **+293,80 €/año** (529,90 − 236,10).
- **Alfa de empate, con dos denominadores porque los dos importan:**
  - sobre **todo** el bloque no indexado (55.500 €): **+0,53 pp/año** netos;
  - sobre **los 21.000 € de convicción**, que es donde se juega: **+1,49 pp/año** netos. Los tres fondos
    cuestan **334,50 €/año (1,59 %)** y el mismo dinero en un índice costaría **21 €**.
- **Riesgo añadido que no sale en la fórmula:** siete gestoras decidiendo en vez de un índice, y una sola
  prima de estilo en el 23,3 % del patrimonio.

Si esa cuenta no te convence leída así, la decisión no es «esta cartera un poco más barata»: es el nivel A, y
está escrito y auditado en `cartera-ai-definitivas-estudiar/cartera-ai-rock-desmontado/100k.md`.

---

## 7. Coste

| Bloque | € | TER medio | €/año |
| --- | --: | --: | --: |
| Índice (5 fondos) | 34.500 | 0,118 % | **40,55** |
| Convicción activa de RV (3 fondos) | 21.000 | 1,593 % | **334,50** |
| Gestión de crédito y liquidez (5 fondos) | 34.500 | 0,379 % | **147,85** |
| **Total invertible** | **90.000** | **0,581 %** | **522,90** |
| Colchón (Groupama) | 10.000 | 0,07 % | 7,00 |
| **Total 100.000 €** | | **0,530 %** | **529,90** |

- **−148,30 €/año** frente a hoy (678,20 €) con 23 pp más de bolsa.
- **El 64 % del coste (334,50 €) sale de 21.000 €.** Es la misma concentración que la de la convicción: no es
  un accidente, es el mandato.
- **Cero comisiones de éxito** (los tres fondos con éxito de hoy —DNCA 20 %, Carmignac 20 %, Gamma 9 %— están
  entre los que salen) y **cero comisión de suscripción y reembolso** publicada en los trece.
- **La comisión pesa más donde el activo rinde menos.** En el bloque defensivo, 0,38 % de TER medio sobre un
  activo que rinde 2-4 % es entre un 10 % y un 19 % del retorno; en el índice, 0,12 % sobre un activo que
  rinde 6-7 % es menos del 2 %. Ese es el argumento serio para simplificar la RF, no los 5 € de duplicidad.
- **Ninguna cifra de retorno está prometida.** El ahorro de coste es aritmética; el resto, no.

---

## 8. Duración y tipos

| Bloque | € | Duración (años) | Euro-duración | +100 pb |
| --- | --: | --: | --: | --: |
| Neuberger | 11.000 | 1,95 | 21.450 | −215 € |
| M&G Short Dated | 6.000 | ≈1,5 `est.` | 9.000 | −90 € |
| Aegon ABS | 8.000 | ≈1,5 `est.` | 12.000 | −120 € |
| iShares Agg 1-5Y | 4.000 | ≈2,8 `est.` | 11.200 | −112 € |
| Cobas Renta (solo su 57,5 % de RF) | 6.000 | ≈2,5 `est.` | 8.625 | −86 € |
| DWS Ultra Short | 3.500 | ≈0,2 | 700 | −7 € |
| **Total** | **40.851** | **1,54** | **62.975** | **−630 €** |

Hoy son 3,83 años y −2.356 € por cada 100 pb. **El riesgo de tipos baja un 73 %** aunque la cartera tenga 23 pp
más de bolsa: el bono euro a 20+ años de Rock era el 32 % de toda la euro-duración.

---

## 9. Las órdenes — 23 traspasos y una cancelación

**Nada se reembolsa.** Todo son IIC comercializadas por la plataforma: traspaso entre fondos, **0 € de
impuestos**. El desmontaje de Rock va por el monetario puente, que también es traspaso
(`cartera-ai-definitivas-estudiar/cartera-ai-rock-desmontado/100k.md` §3 y la FAQ de la plataforma).

### 9.1 Paso 0 — antes de ordenar nada

- [ ] **Saldos comprobados (30/10):** Neuberger 22.000 · DNCA 13.000 · Carmignac 12.000 · Gamma 8.000 ·
      MyInvestor Value 2.000 · Cobas International 1.000 · NB Next Space 1.000 · UBS MSCI China 1.000 =
      **60.000 €**. Rock **30.000 €**. Groupama **10.000 €**, no se toca.
- [ ] **Colchón dimensionado:** 10.000 € tienen que cubrir 12 meses de gasto real (hoy: 833 €/mes). Si el gasto
      es mayor, el faltante sale antes de ejecutar.
- [ ] **El 0,06 % del Developed World, en pantalla.** Es una clase institucional, sin historial a 3-5 años y con
      mínimo de 200 M€ en la gestora; la plataforma la publica con mínimo 0 €. **Si la app no la ofrece a ese
      coste, las órdenes 1, 2 y 3 van a Fidelity MSCI World Index P Acc (IE00BYX5NX33, 0,12 %: +10,20 €/año
      sobre 17.000 €)**. No se sustituye por una clase más cara sin decirlo.
- [ ] **Traspasabilidad fondo a fondo:** confirmar en la plataforma que los trece destinos son traspasables (los
      españoles lo son por defecto; los irlandeses y luxemburgueses dependen de la comercialización por cuenta
      ómnibus, que es el caso de MyInvestor). Si alguno no lo fuera, se ejecuta cambiando el destino, nunca
      reembolsando.
- [ ] **Comisión de suscripción en pantalla** de los trece destinos. Publicada 0,00 % en todos; si apareciera
      en alguno, no se suscribe y se avisa antes de seguir.
- [ ] **Rock:** «Cancelar cartera» → «**Traspasar a un fondo**». Nunca «recibir el dinero en efectivo»: esa
      opción cristaliza ≈13.650 € de plusvalía y cuesta ≈2.590 € de impuestos.

### 9.2 Fase 1 — el bloque manual, hoy (49.000 €, 17 traspasos)

| # | ☐ | Origen | € | Destino | Antes de |
| --: | :-: | --- | --: | --- | --- |
| 1 | ☐ | Neuberger Short Duration | 8.000 | iShares Developed World | **09:00** |
| 2 | ☐ | DNCA Alpha Bonds | 5.000 | iShares Developed World | **09:00** |
| 3 | ☐ | Carmignac Portfolio Credit | 4.000 | iShares Developed World | **09:00** |
| 4 | ☐ | DNCA Alpha Bonds | 3.000 | iShares Emerging Markets | **09:00** |
| 5 | ☐ | Carmignac Portfolio Credit | 3.000 | iShares Emerging Markets | **09:00** |
| 6 | ☐ | DNCA Alpha Bonds | 4.000 | Magallanes European Equity M | 14:00 |
| 7 | ☐ | Gamma Global | 3.000 | Magallanes European Equity M | 14:00 |
| 8 | ☐ | Carmignac Portfolio Credit | 2.000 | Magallanes European Equity M | 14:00 |
| 9 | ☐ | Gamma Global | 3.000 | Horos Value Internacional | 12:00 |
| 10 | ☐ | Carmignac Portfolio Credit | 3.000 | Horos Value Internacional | 12:00 |
| 11 | ☐ | MyInvestor Value C | 2.000 | Vanguard Global Small-Cap | 16:00 |
| 12 | ☐ | NB Next Generation Space | 1.000 | Vanguard Global Small-Cap | 16:00 |
| 13 | ☐ | UBS MSCI China | 1.000 | Vanguard Global Small-Cap | 16:00 |
| 14 | ☐ | Gamma Global | 2.000 | M&G Short Dated Corporate | 12:00 |
| 15 | ☐ | Neuberger Short Duration | 3.000 | M&G Short Dated Corporate | 12:00 |
| 16 | ☐ | Cobas International P | 1.000 | M&G Short Dated Corporate | 12:00 |
| 17 | ☐ | DNCA Alpha Bonds | 1.000 | DWS Euro Ultra Short | 12:00 |

**Cuadre por origen:** Neuberger 11.000 (conserva 11.000) · DNCA 13.000 · Carmignac 12.000 · Gamma 8.000 ·
MyInvestor Value 2.000 · Space 1.000 · China 1.000 · Cobas International 1.000 = **49.000 €**.
**Cuadre por destino:** World 17.000 · EM 6.000 · Magallanes 9.000 · Horos 6.000 · Small-Cap 4.000 · M&G 6.000
· DWS 1.000 = **49.000 €**.

**Orden dentro de la sesión:** M&G exige **1.000 € de primera aportación**; sus tres órdenes (2.000 + 3.000 +
1.000) las cumplen. Magallanes exige **1 participación** (≈287 €) y su primera orden es de 4.000 €. Horos, Cobas
Renta, Aegon, DWS, Small-Cap y REITs piden 1 € o 100 €: sin restricción. **El corte del destino manda sobre el
del origen:** el Neuberger cierra a las 10:00, así que las órdenes 1 y 2 se meten antes de las 09:00 y ejecutan
el mismo día.

### 9.3 Fase 2 — Rock desde el puente, 5-10 días después (30.000 €, 6 traspasos)

| # | ☐ | Origen | € | Destino | Antes de |
| --: | :-: | --- | --: | --- | --- |
| 18 | ☐ | Monetario puente | 4.000 | iShares Global Aggregate 1-5Y | **09:00** |
| 19 | ☐ | Monetario puente | 3.500 | iShares Developed Real Estate | 12:00 |
| 20 | ☐ | Monetario puente | 6.000 | Cobas Large Cap P | 14:00 |
| 21 | ☐ | Monetario puente | 6.000 | Cobas Renta | 12:00 |
| 22 | ☐ | Monetario puente | 8.000 | Aegon European ABS | 12:00 |
| 23 | ☐ | Monetario puente | 2.500 | DWS Euro Ultra Short | 12:00 |

**Cuadre:** 4.000 + 3.500 + 6.000 + 6.000 + 8.000 + 2.500 = **30.000 €**. Rock a **0**.

### 9.4 Comprobación final

- [ ] World **17.000** · EM **6.000** · Small-Cap **4.000** · REITs **3.500** · Agg 1-5Y **4.000** ·
      Magallanes **9.000** · Horos **6.000** · Cobas Large Cap **6.000** · Cobas Renta **6.000** · Neuberger
      **11.000** · M&G **6.000** · Aegon **8.000** · DWS **3.500** = **90.000 €**.
- [ ] DNCA, Carmignac, Gamma, MyInvestor Value, Space, China y Cobas International a **0**.
- [ ] Groupama **10.000 €** intacto. Rock a 0.
- [ ] RV **54,6 %** / RF y caja **45,4 %** · índice **38,3 %** · coste **529,90 €/año**.
- [ ] Ningún fondo por debajo de un mínimo y ninguna orden con comisión de suscripción.

### 9.5 Lo que no se debe hacer

- **No reembolsar** para suscribir después: se pierde el diferimiento fiscal y se paga el 19-23 %.
- **No cancelar Rock en efectivo.** El puente monetario es la diferencia entre 0 € y ≈2.590 €.
- **No cambiar de clase** un fondo que se queda (equivale a reembolso), aunque sea más barata.
- **No comprar Aegon con más de 8.000 €** ni Cobas Large Cap con más de 6.000 € hasta ver un trimestre.
- **No sustituir ningún fondo por un ETF** del mismo índice: ahorra 5-10 pb y convierte cada rebalanceo en una
  factura.

---

## 10. Los 1.000 €/mes

Diez líneas admiten orden mensual y **tres no**: M&G pide 75 € por aportación (le tocarían 67 €), Horos 100 € y
Cobas Renta 100 €. Esas tres van **trimestrales** y el plan cuadra al céntimo.

| Fondo | Peso | €/mes equivalente | Cadencia | Importe por orden | Mínimo |
| --- | --: | --: | --- | --: | --: |
| iShares Developed World | 18,9 % | 188 | mensual | **188 €** | 0 € |
| Neuberger Short Duration | 12,2 % | 122 | mensual | **122 €** | 1 € |
| Magallanes European Equity M | 10,0 % | 100 | mensual | **100 €** | 0 € |
| Aegon European ABS | 8,9 % | 89 | mensual | **89 €** | 1 € |
| iShares Emerging Markets | 6,7 % | 67 | mensual | **67 €** | 0 € |
| Cobas Large Cap P | 6,7 % | 67 | mensual | **67 €** | 1 € |
| Vanguard Global Small-Cap | 4,4 % | 44 | mensual | **44 €** | 1 € |
| iShares Global Agg 1-5Y | 4,4 % | 44 | mensual | **44 €** | 0 € |
| iShares Developed Real Estate | 3,9 % | 39 | mensual | **39 €** | 1 € |
| DWS Euro Ultra Short | 3,9 % | 39 | mensual | **39 €** | 0 € |
| **Horos Value Internacional** | 6,7 % | 67 | **trimestral** | **201 €** | 100 € |
| **Cobas Renta** | 6,7 % | 67 | **trimestral** | **201 €** | 100 € |
| **M&G Short Dated Corporate** | 6,7 % | 67 | **trimestral** | **201 €** | 75 € |
| **TOTAL** | **100 %** | **1.000** | | | |

**La identidad que tiene que cumplir:** órdenes mensuales **799 €** + trimestrales **603 € / 3 = 201 €** =
**1.000 €/mes**. Ni un euro sin asignar, ninguna orden por debajo de su mínimo.

**Rebalanceo por entradas, no por ventas.** Cada mes, los 1.000 € van a la línea que esté más por debajo de su
peso, medida en euros. Solo se vende si un bloque se desvía más de 5 pp.

**El monetario no es una hucha que crece sin fin.** Los 39 €/mes del DWS mantienen su 3,9 %; si prefieres no
acumular más liquidez —el colchón ya cubre 12 meses—, esos 39 € van al Agg 1-5Y y el plan no cambia.

---

## 11. Prepárate para lo que viene: seis escenarios con la orden dentro

| Escenario | Qué le pasa a esta cartera | Qué se hace |
| --- | --- | --- |
| **Corrección tecnológica / de EE. UU.** (−25-30 % en el índice) | El núcleo es 72 % EE. UU. y 32 % tecnología: es la línea que más cae. El value (industria, materiales, energía) cae menos, y el bloque defensivo casi no se mueve | **Se aporta más al núcleo**, no se vende nada. Si el índice baja 25 %, la aportación mensual de 188 € compra un 33 % más de participación. Se revisa el peso del bloque, no el fondo |
| **Subida de tipos (+100 pb)** | −630 € por el bloque de RF (duración 1,54). Si son +200 pb, ≈−1.260 € | Nada. Es el nivel de tipos que la cartera soporta sin decisión. Solo se actúa si el bono a 10 años pasa del 5 %: entonces el Agg 1-5Y se queda corto y se valora alargar |
| **Evento de crédito (HY/BBB−)** | La cartera **no tiene high yield**: IG corto, titulizaciones y agregado soberano | Nada. Si el spread IG se abre más de 200 pb, se aporta al M&G y al Aegon, que es cuando el filtro de emisor paga |
| **Un gestor activo se queda atrás 2 años seguidos** | El bloque activo pierde su razón de ser y sus 1,81-1,90 % pasan a ser coste puro | Se aplica §13: la línea concreta se traspasa a índice, no se defiende por lealtad |
| **Bolsa plana cinco años** | El value puede seguir barato y no subir; el coste del bloque activo (482 €/año) se come el cupón del bloque defensivo | Es el escenario que exige la prueba de §13 antes de 2029; si el activo no bate, la cartera baja a nivel A/B con la cuenta escrita |
| **Necesitas dinero antes de 10 años** | Vender bolsa en el peor día es lo único que rompe el diseño | Se gasta el colchón (12 meses), luego el DWS (3.500 €) y luego el Agg 1-5Y (4.000 €): **7.500 € sin tocar la bolsa**. Si hace falta más, se revisa el % de RV con argumento escrito, no de urgencia |

**Aportación extra o dinero imprevisto** (una paga, una venta): orden fijo — 1) colchón hasta 12 meses de gasto,
2) núcleo indexado, 3) valor Europa, 4) bloque defensivo. Nunca a un fondo que acaba de subir un 30 %.

---

## 12. Bandas y reglas de rebalanceo

| Bloque | Objetivo | Banda verde | Se corrige con aportaciones | Solo se vende |
| --- | --: | --- | --- | --- |
| Renta variable total | 54,6 % | 50-60 % | fuera de 50-60 % | > 65 % o < 45 % |
| Bloque indexado | 38,3 % | 34-43 % | fuera de esa banda | > 48 % |
| Convicción activa de RV | 23,3 % | 20-27 % | fuera de esa banda | > 30 % |
| Gestión de crédito y liquidez | 38,3 % | 34-43 % | fuera de esa banda | > 48 % |
| Una línea cualquiera | su peso | ±2 pp | se redirige la aportación mensual | > 5 pp de desvío |

Medido **en euros, no en tanto por ciento del bloque**, y siempre por entradas primero: con 1.000 €/mes (1,1 %
del patrimonio) no debería hacer falta vender nunca.

---

## 13. Cuándo se revisa, y qué invalida el diseño

Revisión **trimestral** (enero, abril, julio, octubre). El % de RV no se puntúa: se cambia con un argumento
escrito y fechado.

**La prueba que decide si el nivel C se queda** — porque un bloque activo sin prueba es una colección de
nombres:

1. **Por línea, no por bloque:** cada fondo activo se compara con **su** índice, **neto de su TER**, a tres años
   (primer control: **octubre de 2029**).
2. **Dos años seguidos por debajo de su índice** → la línea se traspasa a índice. Con el número delante: 9.000 €
   de Magallanes a 1,81 % que se van al núcleo al 0,06 % ahorran **157,50 €/año**.
3. **Migración completa:** si a 2029 el bloque activo no cubre el **+1,49 pp/año** sobre sus 21.000 € —o el
   +0,53 pp sobre los 55.500 €, según se mire—, la cartera entera pasa a nivel A. Está escrito **antes** de
   ejecutar, no después.
4. **Cambio de gestor o de estilo** en Magallanes, Horos o Cobas: se revisa esa posición en el trimestre
   siguiente, sin esperar los tres años.
5. **Soft close** (hoy solo afecta a Cobas International, que sale): el fondo se mantiene, no se amplía.

**Chequeos trimestrales, siete y en este orden:**

- [ ] TER y clase de los trece fondos (si aparece una clase más barata del **mismo** fondo, se compara con el
      coste del traspaso: cambiar de clase es un reembolso).
- [ ] `management_type` de los trece, uno a uno: si un «activo» pasa a replicar un índice, entra en la cuenta
      del bloque indexado y la banda del 43 % lo detecta.
- [ ] Pesos contra §12 y desvío por línea.
- [ ] Duración y TIR del bloque de RF (Neuberger y M&G publican; Aegon y el Agg se estiman).
- [ ] **El 30,7 % de «otros» de Cobas Large Cap**: si la ficha lo desglosa y resulta ser bolsa, el 54,6 % de RV
      sube; si es ilíquido, es riesgo que la fórmula de §4 no ve.
- [ ] **Cobas Renta**: la línea con la tesis más fina. Si en dos años no repite la defensa de 2022, sale y su
      importe va al Agg 1-5Y.
- [ ] **Magallanes contra MyInvestor Value**: cada uno neto de su comisión (1,81 % frente a 1,35 % + 9 % de
      éxito), a tres años, contra el mismo índice. Si el de Andbank gana, sustituye al de Magallanes; si empata,
      gana el que no cobra éxito.
- [ ] Colchón contra gasto real, una vez al año.

**Lo que no se revisa:** el rendimiento del núcleo contra «su» índice (es su propio índice), ni el % de RV con
ninguna herramienta.

---

## 14. Cómo crece: 100k → 150k → 200k, los 7.000 € y la variante sin tilts

**La estructura aguanta el crecimiento sin rehacer nada.** Ninguna línea tiene un mínimo que rompa al subir: el
índice puede crecer dentro de su banda hasta ~43 %, y el activo crece con las aportaciones.

| Tamaño | Qué se añade | Qué se paga |
| --- | --- | --- |
| 100.000 € (hoy) | Lo de §2 | 529,90 €/año |
| 150.000 € | Se puede abrir una cuarta convicción (Japón activo o un cuarto value global) y subir Aegon | +0,05-0,10 pp de TER si la línea nueva no es índice |
| 200.000 € | Se separa el núcleo en dos gestoras (iShares + Vanguard Global Stock al 0,18 %) y se añade Europa a índice | +35 €/año por partir BlackRock |

**Si los 7.000 € de aportación nueva del `README.md` (04/11) ya están en la cuenta**, no se rehace el diseño:
entran en las tres líneas más alejadas de su objetivo —**World 3.000 · Magallanes 2.000 · Aegon 2.000**— y la
cartera queda en **97.000 € invertibles**, RV **55,7 %**, índice **38,7 %** y **574,10 €/año (0,592 %)**. Las
órdenes de §9 no cambian.

### 14.1 Variante sin tilts, con su número (no adoptada)

Si en la revisión se decide que el inmobiliario y las small caps no merecen ser apuestas:

| Cambio | € | Coste/año | Efecto |
| --- | --: | --: | --- |
| Small-Cap 4.000 € → Developed World | 4.000 | **−9,20 €** | 12 fondos, RV 54,6 %, índice 38,3 %, coste 513,70 € (0,571 %) |
| REITs 3.500 € → Developed World | 3.500 | **−3,85 €** | 11 fondos, RV 54,4 %, índice 38,3 %, coste 509,85 € (0,567 %) |
| M&G 6.000 € → Neuberger | 6.000 | **−5,40 €** | Quita un gestor de crédito; duración 1,54 → 1,61 |

Las tres juntas dejan **11 fondos y 499,85 €/año (0,555 %)**: **30 €/año** de ahorro. Es una decisión de
simplicidad operativa, no de rentabilidad, y por eso no se toma sola: se toma en la revisión.

---

## 15. Lo que se descarta, con el número

| Candidato | Ficha | Por qué no |
| --- | --- | --- |
| **Rock (cartera automatizada)** | 0,41 % todo incluido | **Índice dentro de una caja**: 0,35 pp más caro que replicar el mismo beta y su RF es deuda pública con duración 10,7 (3.000 € en un 20+ que perdió −17,03 % en 2026). Con Rock dentro, el bloque indexado sería el 66 % del capital y el mandato no cabe |
| **Cobas International P** (ya en cartera) | 2,33 % · soft close · 5A +16,6 % | Su hermano **Cobas Large Cap cuesta 0,96 %** y ha hecho más (5A +18,1 %, 3A +29,3 %): misma casa, mismo estilo, **+68,50 €/año** por el mismo papel. Además el soft close impide crecer en él |
| **iShares Europe / Fidelity Japón / Pacífico ex-Japón** | 0,10-0,13 % | Son más índice, y con el bloque ya al 38,3 % lo que harían es **comerse el cupo**: el sesgo anti-EE. UU. se paga aquí con gestores, no con tres réplicas regionales |
| **Amundi EUR Corporate 1-5Y** | 0,35 % | El mismo riesgo que el Agg 1-5Y al **cuatro veces** el precio (0,08 %) |
| **Robeco QI European Conservative** | 1,01 % | Beta con rebeca: benchmark como objetivo, `tracking error` bajo y 1A dentro de un punto del índice europeo. Es comisión de gestión por el índice, no una convicción |
| **Magallanes clase P** | 1,25-1,30 % | **No está en el catálogo de la plataforma** (solo R 1,95 % y M 1,81 %). Importarla no es una opción: sería un traspaso entre comercializadores |
| **Kaizen Global Income** | TER **no publicado** | Sin coste verificable no se defiende, por segunda vez |
| **MyInvestor Value C** (ya en cartera) | 1,35 % + 9 % de éxito · RV 95,6 % · YTD 2026 +15,6 % · 1A +20,0 % | **Fuera como posición, no condenado.** Su 2026 es bueno (Magallanes +11,4 % y Horos +5,5 % en el mismo año) y el 9 % de éxito es de los bajos del catálogo —el estándar es 20 %—, así que el argumento no es el coste. Es que **no añade un riesgo nuevo** (value europeo small/mid, Alemania 29 % y Francia 23 %, justo entre Magallanes y Horos), **solo publica dos ejercicios** —2025 y 2026, los dos buenos del value— y no hay dato de 2022, y con 2.000 € sería una cuarta convicción decorativa: para tener peso tendría que desplazar a Magallanes, que tiene más historial y menos volatilidad (12,7 % frente a 17,9 %). Entra como candidato en la prueba de 2029 (§13) |
| **Fundsmith · Comgest Growth Europe · Morgan Stanley Global Brands** | 1,09-1,84 % | Ceden al índice a 5 años (+2,9 %, −0,9 %, +1,0 % frente a +9,7 % del europeo y +10,9 % del mundial) |
| **Azvalor Internacional** | mínimo 5.000 € + 3 % de salida bajo 12 meses | 150 € de penalización sobre una posición de 5 % del patrimonio |
| **Cat bonds (Twelve)** | 1,30 % · liquida en 8 días | Su descorrelación es real, pero a 3.000-4.000 € el TER se come el efecto; candidata si la cartera crece a 200k |
| **Oro vía fondo** (DWS, Jupiter) | 1,61-1,66 % · vol 38 % | El físico solo existe como ETF; el fondo es el perfil del NB Space que sale |
| **Acciones sueltas** | — | Sin tesis mantenida, cuatro nombres son riesgo idiosincrático, no diversificación. Viven en `propuesta-acciones.md`, aparte y sin sumar |
| **Nivel A, 69,4 % indexado** | 236,10 €/año | **No se descarta: se aparca con su número.** Es la alternativa si el mandato cambia (§6) |

**Propuestas retiradas del árbol con esta decisión:** `propuesta-ai.md` (16/11, 60/40 en once fondos
**indexados**, 0,224 %) partía de la premisa contraria —el índice como edificio entero— y su contenido útil
está absorbido aquí (el desmontaje de Rock por el puente, el Agg 1-5Y, el Aegon, el M&G y el contraste de los
fondos value). Sigue en el historial de git (último commit con el documento íntegro: `5fae506`), no en la
carpeta: dos hojas que se contradicen son dos verdades, y ya hay una. `propuesta-actual.md` (04/11) queda
marcada como superada y se conserva solo por las citas del criterio del 55 % de su §2.

---

## 16. Lo que queda sin decidir

- **El gasto real mensual** con el que se dimensiona el colchón de 10.000 €: hoy son 833 €/mes asumidos.
- **Si los 7.000 € de aportación nueva están en la cuenta** (§14): cambia el importe, no el diseño.
- **El acceso real al 0,06 % del Developed World** y la traspasabilidad de los trece (§9.1).
- **La comisión de suscripción real en pantalla**: publicada 0,00 %, no verificada en la app.
- **TIR y duración de Aegon, M&G, Agg 1-5Y y DWS no publicadas**: 1,5 / 1,5 / 2,8 / 0,2 años son estimaciones
  declaradas.
- **El 30,7 % de «otros» de Cobas Large Cap**: no es RV declarada; se cuenta como cero bolsa en §4, así que el
  54,6 % de RV es un **suelo**, no un techo.
- **La variante sin tilts de §14.1** (11 fondos, 30 €/año de ahorro): se decide en la revisión.

---

## 17. Resumen para mañana

1. **Comprobar** saldos, colchón, el 0,06 % del World en pantalla, la traspasabilidad y las comisiones (§9.1).
2. **Cancelar Rock** hacia el monetario puente, nunca a efectivo.
3. **17 traspasos** del bloque manual (§9.2), respetando los cortes de 09:00 y 12:00.
4. **Esperar 5-10 días** y hacer los **6 traspasos** desde el puente (§9.3).
5. **Comprobar** los trece saldos (§9.4) y dejar programadas las órdenes del plan de 1.000 €/mes (§10).
6. **Apuntar en el calendario** la revisión de octubre de 2029 (§13): es la fecha en la que esta cartera
   demuestra si los 21.000 € de convicción se pagan o se retiran.

> No es asesoramiento financiero. La decisión y la ejecución son del titular.

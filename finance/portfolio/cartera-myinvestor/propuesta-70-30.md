---
title: "Propuesta 70/30: siete indexados, 69,6 % de RV y 102,85 €/año (90.000 € invertibles)"
date: 2026-11-19
type: portfolio-proposal
category: finance
tags: [cartera, propuesta, myinvestor, 70-30, indexado, ishares, vanguard, sensata, eficiente, diversificada, 40-anos, traspasos]
status: propuesta
related:
  - finance/portfolio/cartera-myinvestor/README.md
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
  - finance/portfolio/cartera-myinvestor/propuesta-pieza.md
  - finance/portfolio/cartera-definitiva-40/100k.md
---

# Propuesta 70/30 — 90.000 € invertibles (+ 10.000 € de colchón)

> **Qué es.** La cartera de la cuenta de MyInvestor **reducida a siete fondos indexados** —de trece, con siete
> gestoras y dos comisiones de éxito—: **42 % MSCI World al 0,06 %**, **10 % Europa**, **9 % emergentes**,
> **9 % small caps globales** y **30 % de renta fija en tres tramos** (agregado global 1-5 años cubierto, crédito
> corporativo euro IG y ligado a inflación eurozona). **95,85 €/año (0,1065 %)** sobre los 90.000 € invertibles y
> **102,85 €/año (0,1029 %)** sobre los 100.000 € del ahorro, colchón incluido. **69,61 % de RV real**, caída de
> manual **−28,75 % (−25.879 €)**, **≈5,72 % de rentabilidad esperada anual** y **cero comisiones de éxito**.
>
> **La única decisión que hay que firmar.** El suelo conductual que aceptaste por escrito el 04/11 era **−22.700 €**.
> Esta cartera lo lleva a **−25.879 €**: **3.179 € más de caída** a cambio de **15 pp más de renta variable**
> (54,61 % → 69,61 %) y **427 €/año menos de coste**. Todo lo demás —los siete fondos, los pesos, los traspasos— es
> consecuencia de esa firma, no al revés: si el suelo no se firma, la variante 60/40 de §3.1 deja la caída en
> **−22.291 €**, que es prácticamente el suelo antiguo.
>
> **Lo que esta cartera NO es.** No lleva convicción activa. La prueba value que la `propuesta-pieza` tiene escrita
> para 2029 —21.000 € en Magallanes, Horos y Cobas con **1,49 pp/año de alfa de empate**— aquí desaparece. Es la
> concesión grande y está en §3 y §7, no escondida: esta cartera compra el mercado al precio del mercado y renuncia
> a batirlo.
>
> **Método.** Fichas del catálogo de MyInvestor por MCP el **19/11/2026** (`python3 tools/myinvestor_mcp.py ficha`,
> ocho ISIN verificados uno a uno: TER, `distributing`, `alloc_equity/bond/cash`, mínimos, cortes, liquidación y
> avisos de *soft close*), más `backtest_portfolio` en dos pasadas —clases reales y clases con historia de los
> mismos índices— y los datos de la cartera de partida de `cartera-actual.md` (foto 30/10/2026). La rentabilidad
> esperada es **estimación del agente con supuestos declarados**.
>
> **No es asesoramiento financiero.** La decisión, el suelo y la ejecución son del titular.

---

## 0. Lo que cambia respecto a lo que hay hoy

| | Hoy (`propuesta-pieza`, 18/11) | Esta propuesta | Diferencia |
| --- | --: | --: | --: |
| Fondos | 13 | **7** | −6 |
| Gestoras | 7 + Rock | **2** (BlackRock y Vanguard) | −5 |
| Comisiones de éxito | 0 en la pieza, pero el bloque de crédito las llevaba en origen | **0** | — |
| Coste del ahorro completo | **529,90 €/año (0,530 %)** | **102,85 €/año (0,1029 %)** | **−427,05 €/año** |
| RV real | 54,61 % (49.149 €) | **69,61 % (62.646 €)** | **+15,0 pp** |
| Caída de manual | −20.885 € | **−25.879 €** | +4.994 € |
| Indexado | 38,3 % | **100 %** | +61,7 pp |
| Traspasos | 23 en dos fases | **12 en dos fases** | −11 |
| Aportación | 1.000 €/mes | 1.000 €/mes | — |

**Los 427 €/año, a 27 años y al 5,72 %, son ≈26.000 €.** Es dinero cierto, no una esperanza.

---

## 1. El mandato

| Lo que pediste | Cómo se cumple | Qué cuesta |
| --- | --- | --- |
| **Sensata** | La decisión de riesgo se toma una vez (69,61 % de RV) y el resto es mecánico: 7 líneas, bandas de ±5 pp, aportación automática | 3.179 € más de caída que tu suelo del 04/11, que hay que firmar |
| **Eficiente** | **102,85 €/año (0,1029 %)** frente a 529,90 €: el 81 % del coste fuera | Renunciar a la prueba value de 2029 (§3) |
| **Diversificada** | 47 países, 13 zonas publicadas (86,6 % de la RV), 7 índices, 3 tramos de renta fija, 2 gestoras | EE. UU. sigue al 50,8 % de la RV y tecnología al 28,0 %: es el peso del mundo |
| Nada que reparta dividendos | Los 8 ISIN con `distributing = 0` verificado hoy (7 de cartera + colchón) | — |
| Sin peaje fiscal | Los 12 traspasos son **entre fondos armonizados**: 0 € de impuestos | Nada |
| Horizonte y tolerancia | **Asumido: 20+ años y capacidad de ver −25.879 € sin vender** | Con 5-7 años, §3.1 (60/40) |

---

## 2. La cartera

| # | Bloque | Fondo | ISIN | € | % de 90k | TER | €/año | RV | Corte | Liquidación |
| --: | --- | --- | --- | --: | --: | --: | --: | --: | --- | --- |
| 1 | **Núcleo RV mundo** (índice) | iShares Developed World Index (IE) S Acc EUR | IE000ZYRH0Q7 | 37.800 | 42,00 % | **0,06 %** | 22,68 | 99,29 % | 09:00 | 4 días |
| 2 | **RV Europa** (índice) | Vanguard European Stock Index EUR Acc | IE0007987708 | 9.000 | 10,00 % | 0,12 % | 10,80 | 99,76 % | 10:00 | 2 días |
| 3 | **RV emergentes** (índice) | iShares Emerging Markets Index (IE) S Acc EUR | IE000QAZP7L2 | 8.100 | 9,00 % | 0,16 % | 12,96 | 99,26 % | 09:00 | 4 días |
| 4 | **RV small caps globales** (índice) | Vanguard Global Small-Cap Index EUR Acc | IE00B42W4L06 | 8.100 | 9,00 % | 0,29 % | 23,49 | 99,94 % | 16:00 | 3 días |
| 5 | **RF agregado global 1-5 años** cubierta a euros | iShares Global Aggregate 1-5Y Bond (IE) S Acc EUR H | IE0004ZP1ND3 | 16.200 | 18,00 % | **0,08 %** | 12,96 | 0 % | 09:00 | 3 días |
| 6 | **RF crédito corporativo euro IG** | iShares Euro Investment Grade Corporate Bond (IE) D Acc EUR | IE00BDRK7J14 | 5.400 | 6,00 % | 0,12 % | 6,48 | 0 % | 09:00 | 3 días |
| 7 | **RF ligada a inflación eurozona** | Vanguard Eurozone Inflation-Linked Bond EUR Acc | IE00B04GQR24 | 5.400 | 6,00 % | 0,12 % | 6,48 | 0 % | 10:00 | 2 días |
| | **Total invertible** | **7 fondos · 2 gestoras · 7 índices** | | **90.000** | **100 %** | **0,1065 %** | **95,85** | **69,61 %** | | |
| *Fuera* | Colchón | Groupama Trésorerie IC | FR0000989626 | 10.000 | — | 0,07 % | 7,00 | 0 % | 09:00 | 0 días |
| | **Coste del ahorro completo** | | | **100.000** | | **0,1029 %** | **102,85** | | | |

- **Los siete son de acumulación y en euros**, `distributing = 0` comprobado hoy, y **ninguno cobra suscripción,
  reembolso ni comisión de éxito**.
- **Mínimos:** 0 € en los cuatro iShares y 1 € en los tres Vanguard. Nada que fraccionar.
- **El colchón no se toca.** Groupama Trésorerie (0,07 %, 84,6 % de caja) se queda donde está: es lo que permite
  aguantar la caída sin vender. Su ficha avisa de que el valor por participación es alto y puede haber diferencias
  por redondeo en los traspasos: con 10.000 € y un VL alto, se traspasa **por importe, no por participaciones**.
- **Un detalle operativo:** el núcleo liquida en **4 días**, más que el resto. Para la aportación mensual da igual;
  para una compra grande, se lanza primero.

### 2.1 Los tres bloques

| Bloque | € | % | TER medio | €/año | Qué es |
| --- | --: | --: | --: | --: | --- |
| **RV núcleo desarrollada** | 37.800 | 42,00 % | **0,06 %** | **22,68** | MSCI World: 1.200 empresas, 23 países, 71,7 % EE. UU. |
| **RV satélites** | 26.100 | 29,00 % | **0,19 %** | **47,25** | Europa 10 % (la única línea en euros de origen), emergentes 9 % y small caps 9 % |
| **Renta fija** | 27.000 | 30,00 % | **0,096 %** | **25,92** | Agregado global corto 18 %, crédito euro IG 6 % y ligado a inflación 6 % |
| **Total** | **90.000** | 100 % | **0,1065 %** | **95,85** | |

- **El 75 % del coste está en el 29 % de satélites** (47,25 € de 95,85 €): Europa, emergentes y small caps cuestan
  0,19 % porque son lo que el núcleo no tiene. Aun así, los tres juntos cuestan 47 €/año: menos que una sola línea
  de cualquier cartera activa del repo.
- **La renta fija cuesta 25,92 €/año por 27.000 €**, y compra tres cosas distintas: 58 % de deuda pública vía el
  agregado global, spread corporativo euro vía el IG y protección real vía el ligado a inflación.

### 2.2 Geografía y sectores de la RV

`top_regions`/`top_sectors` de cada ficha × su `alloc_equity`, sobre **62.646 €** de RV (86,6 % y 82,6 % publicados):

| Zona | € | % de la RV | MSCI ACWI |
| --- | --: | --: | --: |
| **Estados Unidos** | 31.852 | **50,8 %** | ≈63 % |
| Reino Unido | 3.489 | 5,6 % | ≈3 % |
| Japón | 3.245 | 5,2 % | ≈5 % |
| Taiwán | 2.269 | 3,6 % | ≈2 % |
| Suiza | 2.244 | 3,6 % | ≈2 % |
| Alemania | 1.979 | 3,2 % | ≈2 % |
| Corea | 1.695 | 2,7 % | ≈2 % |
| Canadá | 1.564 | 2,5 % | ≈3 % |
| China | 1.499 | 2,4 % | ≈3 % |
| Francia | 1.179 | 1,9 % | ≈2 % |
| Países Bajos / India / España | 2.278 | 3,6 % | — |
| **No clasificado** (colas fuera del *top 6*) | 8.353 | 13,4 % | — |

| Sector | % de la RV |
| --- | --: |
| **Tecnología** | **28,0 %** |
| Servicios financieros | 17,0 % |
| Industria | 12,1 % |
| Salud | 8,8 % |
| Consumo cíclico | 8,0 % |
| Servicios de comunicación | 5,7 % |

### 2.3 Tilts declarados, con su precio

| Tilt | En esta cartera | En el mundo | Precio si no paga |
| --- | --: | --: | --- |
| **EE. UU. a la baja** | 50,8 % de la RV | ≈63 % | Con 2 pp/año de ventaja americana, **≈0,25 pp/año** de la cartera |
| **Europa arriba** | 10 % del dinero (Reino Unido 21,4 %, Suiza 14,9 %, Alemania 13,5 %) | ≈15 % de la RV del ACWI | Es la línea en la divisa del titular, no una apuesta de valor |
| **Small caps** | 9 % del dinero | 0 % en el World | −13,5 % en 2022 y 5A de +5,89 % frente a +10,01 % del World |
| **Emergentes** | 9 % del dinero | ≈12 % del ACWI | Volatilidad 15,9 % y la mitad del bloque en Taiwán + Corea |
| **RF al 30 %** | 27.000 € | 0 % | 5,7 pp de caída menos que una cartera 100 % bolsa (§3) |

- **Sin cobertura de divisa en la RV.** El 50,8 % americano, el 5,2 % japonés y el 3,6 % suizo entran sin cubrir:
  cubrir cuesta TER y devuelve el riesgo al euro. La renta fija global sí está cubierta.

---

## 3. Por qué esta y no las otras dos

| | `propuesta-pieza` (18/11) | **Esta 70/30** | `cartera-definitiva-40` |
| --- | --: | --: | --: |
| RV real | 54,61 % | **69,61 %** | 84,46 % |
| Coste del ahorro | 529,90 € (0,530 %) | **102,85 € (0,1029 %)** | 96,00 € (0,096 %) |
| Caída de manual | −20.885 € | **−25.879 €** | −30.825 € (sobre 90.000 €) |
| Fondos / gestoras | 13 / 7 | **7 / 2** | 4 / 2 |
| Convicción activa | 21.000 € con prueba en 2029 | **ninguna** | ninguna |
| Traspasos | 23 | **12** | 4 |

- **Frente a la pieza, esta cartera cambia dos cosas a la vez y hay que decirlo:** quita el bloque activo (que
  cuesta **482 €/año** en fondos y promete **1,49 pp/año de alfa de empate** sobre 21.000 €) y sube la RV 15 pp.
  Lo primero es un hecho verificable en coste; lo segundo es una decisión de riesgo.
- **Frente a la definitiva-40, esta se queda 15 pp corta de bolsa y paga 6,85 €/año más**, pero baja la caída en
  **4.946 €**. Es exactamente el escalón intermedio: el que se puede firmar hoy sin reescribir el suelo de −22.700 €
  a −34.250 €.
- **Si el titular quiere el salto completo**, la ruta es: esta cartera ahora, y a los 85/15 dentro de 12-24 meses
  —o después de vivir una caída del 20 % sin vender—, cambiando solo los pesos de las mismas siete líneas.

### 3.1 Variante 60/40 (si no se firma el suelo nuevo)

| Línea | € | % de 90k |
| --- | --: | --: |
| iShares Developed World S | 32.400 | 36 % |
| Vanguard European Stock | 7.200 | 8 % |
| iShares Emerging Markets S | 7.200 | 8 % |
| Vanguard Global Small-Cap | 7.200 | 8 % |
| iShares Global Aggregate 1-5Y EUR H | 19.800 | 22 % |
| iShares Euro IG Corporate | 8.100 | 9 % |
| Vanguard Eurozone Inflation-Linked | 8.100 | 9 % |

**99,50 €/año (0,1106 %) · 59,67 % de RV · caída −22,291 % (−20.062 €) · esperanza ≈5,20 %.** Es la versión que
**respeta el suelo del 04/11** (−22.700 €) y sigue costando **430 €/año menos** que la pieza. Si el titular no quiere
firmar 3.179 € más de caída, esta es la cartera, no la 70/30.

---

## 4. Métricas de la cartera

| Métrica | Valor | Cómo se calcula |
| --- | ---: | --- |
| RV real (*look-through*) | **69,61 %** (62.646 €) | Σ importe × `alloc_equity` |
| RF y liquidez | 30,39 % (27.354 €) | Agregado 1-5 años (18,0 %), IG euro (6,0 %) y ligado a inflación (6,0 %) |
| Caída de manual | **−28,75 %** (**−25.879 €**) | −(40 % × RV + 3 % × RF) |
| Estrés de cola (RV al −45 %, RF plana) | −31,32 % (−28.190 €) | — |
| TER medio | **0,1065 %** (95,85 €/año sobre lo invertible) | Σ importe × TER |
| Coste del ahorro completo | **0,1029 %** (102,85 €/año) | Añade el colchón (7,00 €) |
| Posiciones / gestoras / índices | 7 / 2 / 7 | — |
| Duración de la RF | ≈3,2 años ponderada (estimación) | 18 % a ≈2,5 · 6 % a ≈5 · 6 % a ≈7 |
| Liquidez sin tocar bolsa | 10.000 € colchón + 27.000 € de RF (reembolso 2-3 días) | `redemption_lag_days` |
| Comisiones de éxito | **0 €** | `performance_fee: null` en los siete |

### 4.1 La estructura, medida en cinco años reales

`backtest_portfolio` del MCP, **18/11/2021 → 16-17/11/2026**, con estos pesos y las clases con historia de los mismos
índices (Vanguard World, Vanguard Europa, Vanguard EM, small caps, Vanguard short bond hedged, iShares Euro IG y
Vanguard linker):

| Métrica | Valor |
| --- | --: |
| Rentabilidad acumulada / anualizada | **+37,6 %** / **+6,6 %** |
| Volatilidad anualizada | 8,6 % |
| **Máxima caída** | **−12,4 %** |
| Sharpe (libre de riesgo 0) | 0,77 |
| 2022 (el año malo) | **−11,3 %** |
| 2023 / 2024 / 2025 / 2026 (parcial) | +12,9 % / +15,3 % / +7,8 % / +11,3 % |
| Correlación media / más alta / más baja | 0,56 / 0,87 (RF corta y crédito euro) / 0,30 (EM y RF) |

- **La caída de manual (−28,75 %) es un escenario de estrés; la real de los últimos cinco años fue −12,4 %.** Las
  dos van escritas: la primera dice qué hay que poder aguantar, la segunda qué ha pasado hasta hoy.
- **La correlación 0,87 entre la RF corta y el crédito euro dice lo que ya se sabía:** los dos tramos son renta fija
  en euros y se mueven juntos. No se fusionan porque el IG aporta spread y el agregado aporta duración y gobierno.
- **Pasada con las clases reales** (21/08/2025 → 16/11/2026, limitada por el nacimiento de la clase S): +18,1 %
  acumulado, 14,4 % anualizado, 8,1 % de volatilidad y −4,6 % de caída máxima.

---

## 5. Rentabilidad esperada

**Método.** Rentabilidad neta esperada por línea sobre los 90.000 € invertibles. Supuestos: inflación de la eurozona
**2,0 %**; renta fija a TIR actual del índice (agregado corto ≈2,9 %, IG euro ≈3,6 %, ligado a inflación ≈3,4 %
nominal); RV con prima decreciente por valoraciones: **6,5 %** mundo desarrollado, **7,0 %** Europa, **7,5 %**
emergentes y small caps.

| Línea | € | Neto esperado | Aporte |
| --- | --: | --: | --: |
| Developed World S | 37.800 | 6,5 % | 2,73 pp |
| European Stock | 9.000 | 7,0 % | 0,70 pp |
| Emerging Markets S | 8.100 | 7,5 % | 0,68 pp |
| Global Small-Cap | 8.100 | 7,5 % | 0,68 pp |
| Global Aggregate 1-5Y EUR H | 16.200 | 2,9 % | 0,52 pp |
| Euro IG Corporate | 5.400 | 3,6 % | 0,22 pp |
| Eurozone Inflation-Linked | 5.400 | 3,4 % | 0,20 pp |
| **Total** | **90.000** | | **≈5,72 %** |

- **Central 5,72 % nominal / 3,72 % real**, con rango **3,98-7,46 %** (±2,5 pp sobre la RV).
- **Comparación honesta con la pieza: solo dos cosas se pueden comparar sin discutir supuestos.** El **coste**
  (−427,05 €/año, hecho verificado) y la **caída** (+4.994 €, fórmula de la casa). Lo que cada documento llama
  «esperanza» depende de que su bloque rinda lo que asume: la pieza asume más en su crédito (TIR 4,65-6,50 %) y en
  su value; esta asume un índice al 6,5 %. Por eso aquí la esperanza no sube tanto como la RV.
- **El coste ahorrado, a 27 años y al 5,72 %, son ≈26.000 €** de capital final.

---

## 6. Ejecución: 12 traspasos en dos fases

**Todo por traspaso entre fondos armonizados: 0 € de impuestos y 0 € de comisión.** Nada se reembolsa.

### 6.1 Fase 1 — el bloque manual (60.000 €, 11 traspasos)

| # | Origen | € | Destino |
| --: | --- | --: | --- |
| 1 | Neuberger Short Duration Euro Bond U | 16.200 | iShares Global Aggregate 1-5Y EUR H |
| 2 | Neuberger Short Duration Euro Bond U | 5.400 | iShares Euro IG Corporate |
| 3 | Neuberger Short Duration Euro Bond U | 400 | iShares Developed World S |
| 4 | DNCA Invest Alpha Bonds A | 5.400 | Vanguard Eurozone Inflation-Linked |
| 5 | DNCA Invest Alpha Bonds A | 7.600 | iShares Developed World S |
| 6 | Carmignac Portfolio Credit A | 12.000 | iShares Developed World S |
| 7 | Gamma Global A | 8.000 | iShares Developed World S |
| 8 | MyInvestor Value C | 2.000 | iShares Developed World S |
| 9 | Cobas International P | 1.000 | iShares Developed World S |
| 10 | NB Next Gen Space Economy | 1.000 | iShares Developed World S |
| 11 | UBS MSCI China All Shares | 1.000 | iShares Developed World S |
| | **Total** | **60.000** | |

**Antes de ordenar (§9.1 de `propuesta-pieza`, que sigue vigente):** comprobar que los importes salen de la cuenta de
valores a la vista y no de otro traspaso en curso, y que las clases de destino son las de la tabla (los cuatro iShares
tienen clase S o D de acumulación; si la plataforma ofrece otra clase, no se ejecuta hasta verificar su TER).

### 6.2 Fase 2 — Rock, por el puente (30.000 €, 4 traspasos, 5-10 días después)

| # | Origen | € | Destino |
| --: | --- | --: | --- |
| 12 | Rock (9 fondos, desmontaje por traspaso) | 4.800 | iShares Developed World S |
| 13 | Rock | 9.000 | Vanguard European Stock |
| 14 | Rock | 8.100 | iShares Emerging Markets S |
| 15 | Rock | 8.100 | Vanguard Global Small-Cap |
| | **Total** | **30.000** | |

- **Rock se desmonta por traspaso, nunca por reembolso**: el procedimiento paso a paso está en `propuesta-pieza`
  §9.3 y en `cartera-ai-rock-desmontado/`, y el puente monetario evita cualquier hueco fiscal.
- **Ningún fondo de origen está en soft close** salvo Cobas International (1.000 €), que **se puede traspasar
  igualmente**: el soft close limita suscripciones, no reembolsos ni traspasos de salida.

### 6.3 La aportación de 1.000 €/mes

| Destino | €/mes |
| --- | --: |
| iShares Developed World S | 420 |
| Vanguard European Stock | 100 |
| iShares Emerging Markets S | 90 |
| Vanguard Global Small-Cap | 90 |
| iShares Global Aggregate 1-5Y EUR H | 180 |
| iShares Euro IG Corporate | 60 |
| Vanguard Eurozone Inflation-Linked | 60 |

Con 1.000 €/mes (1,1 % del patrimonio al mes) la cartera se rebalancea sola: no hace falta vender nunca, solo
redirigir la aportación al bloque que se haya quedado corto.

---

## 7. Lo que sale, con su número

| Fondo que sale | € | Coste actual | Por qué |
| --- | --: | ---: | --- |
| **Carmignac Portfolio Credit A** | 12.000 | 1,20 % + éxito 20 % | Se queda su función —crédito— en el IG euro al 0,12 %: **129,60 €/año** de coste por 12.000 € que no compran nada que el índice no tenga |
| **DNCA Invest Alpha Bonds A** | 13.000 | 1,31 % + éxito 20 % | Flexible absoluto: TIR 3,97 % y 4,0 de duración, **por debajo del agregado corto en todo menos en el precio**. 170,30 €/año |
| **Gamma Global A** | 8.000 | 0,95 % + éxito 9 % | TIR 8,07 % pero 2,16 de duración y **comisión de éxito**: lo que aporta de más es riesgo de crédito, ya cubierto en IG |
| **MyInvestor Value C** | 2.000 | ≈1,45 % + éxito 9 % | 2.000 € en value español: coste 29 €/año y **el 5 % de la cartera en una prima de estilo** que esta propuesta no compra |
| **Cobas International P** | 1.000 | **2,33 %** | El fondo más caro de la cartera por importe irrelevante: **23,30 €/año por 1.000 €** |
| **NB Next Gen Space Economy** | 1.000 | **1,90 %** | Temático, 35,75 % de volatilidad a 1 año: 19 €/año y un riesgo idiosincrático que no toca |
| **UBS MSCI China All Shares** | 1.000 | 0,30 % | Es barato y es indexado, pero **1.000 € son ruido** y su función (China) ya está en el 9 % de emergentes |
| **Neuberger Short Duration U** | 22.000 → 0 | 0,38 % | Se conserva su función en el agregado corto al 0,08 %: **66 €/año** de diferencia por el mismo riesgo de tipos |
| **M&G Short Dated Corporate / Aegon ABS** (de la pieza) | 14.000 | 0,47 % / 0,66 % | El ABS es la línea que la propia pieza señala como la peor encajada (§5): compra tramos no senior y su KID añade riesgo de liquidez |
| **Magallanes, Horos, Cobas Large Cap** (la convicción de la pieza) | 21.000 | 1,81-1,90 % | **No entran en esta propuesta.** Su alfa de empate es 1,49 pp/año y su prueba es 2029: es una decisión de convicción, no de eficiencia, y quien la quiera tiene `propuesta-pieza.md` con la cuenta escrita |

**Lo que no se descarta:** la renta fija al 30 %. Es la pieza que sostiene el suelo y la que permite rebalancear sin
vender bolsa; su precio está en §3 (5,7 pp de caída menos).

---

## 8. Qué se mide, cuándo y con qué se corrige

| Prueba | Cuándo | Umbral | Qué se hace |
| --- | --- | --- | --- |
| **RV real** | Trimestral | 69,61 %; banda **64-75 %** | Se corrige con la aportación mensual, no vendiendo |
| **Caída vivida** | Si ocurre | −12,4 % real / −28,75 % de manual | No se vende. Se aporta al núcleo y se gastan primero los 27.000 € de RF |
| **Coste** | Anual | 102,85 € (0,1029 %) | Si un TER sube más de 5 pb, se busca la clase equivalente del mismo índice |
| **Índice y `distributing`** | Anual, con el KID | Los de la tabla | Se documenta antes de mantener la línea |
| **Peso de EE. UU.** | Anual | 50,8 %; banda 45-58 % | Si sale de la banda, la aportación va a Europa, no al núcleo |
| **Prueba value (2029)** | Trimestre cerrado a 30/11/2029 | Solo si se hubiera conservado la pieza: **1,49 pp/año** | Aquí no hay nada que probar: esta cartera **renuncia a la prima de estilo**, y eso es un hecho, no un riesgo |
| **Aportación ejecutada** | Mensual | 1.000 €/mes | Si un mes no se aporta, el problema no es la cartera |

---

## 9. Qué queda sin decidir

- **El suelo nuevo.** Esta cartera pide firmar **−25.879 €** (3.179 € más que el suelo de −22.700 €). Si no se firma,
  la variante 60/40 de §3.1 lo respeta y cuesta 99,50 €/año.
- **La convicción activa.** Esta propuesta la elimina entera. Si el titular quiere mantener una parte de la prueba de
  2029, la forma más limpia es conservar **una** de las tres líneas de la pieza (Magallanes, 9.000 €, 1,81 %) y
  compensarla bajando el núcleo: coste +10,80 €/año por cada 1.000 € y **+1,5 pp/año de alfa de empate**, con la
  caída prácticamente igual.
- **Los 1.000 €/mes**: confirmar que siguen y que son automáticos.
- **La duración de la renta fija (≈3,2 años)** es estimación ponderada de los índices replicados, no dato de ficha.
- **La fecha de ejecución.** Ninguna orden de §6 está lanzada.

---

## 10. Lo que este documento no es

No es una promesa de rentabilidad ni asesoramiento financiero. La esperanza de §5 es una **estimación con supuestos
declarados**, y el 7,46 % favorable no es la mediana. Esta cartera **no intenta batir al mercado**: compra índices al
coste más bajo disponible y renuncia expresamente a la prima de estilo y al alfa de gestor. Tampoco protege de una
caída del 40 %: la **−28,75 % de manual** es la cifra que el titular tiene que poder mirar sin vender, y por eso la
decisión de firmarla (o de quedarse en la 60/40) es suya y no del documento.

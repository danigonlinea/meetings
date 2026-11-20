---
title: "C5 — Crecimiento con satélites"
date: 2026-11-20
type: portfolio-proposal
category: finance
tags: [crecimiento, satelites, tecnologia, salud, infraestructura, small-caps, emergentes]
status: propuesta
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/validacion.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/fondos-revisados.md
---

# C5 — Crecimiento con satélites

> **Qué es.** 11 fondos, 100.000 € exactos, **82,95 % de renta variable real** (look-through) y **952,80 €/año (0,9528 %)**. Caída de manual **−33,52 % (33.522 €)** y **≈6,25 % esperado** con los supuestos de §4 (4,18 % pesimista / 7,49 % favorable).
>
> La concentración está escrita: el satélite de tecnología y el de salud son apuestas de sector con mínimo y comisión de éxito en algunos casos. Se compensan con un núcleo barato y con ABS euro en la parte defensiva.
>
> **Método y límite.** Fichas del repo (snapshot de la app 19/11/2026 + MCP 20/11/2026) y cuatro verificaciones web puntuales el 20/11/2026, citadas en §9. **No es asesoramiento financiero**: la decisión y la ejecución son del titular.

---

## 1. Mandato

| Lo que pide el encargo | Cómo se cumple | Qué cuesta |
| --- | --- | --- |
| 100.000 € | 11 líneas que suman exactamente 100.000 € | Nada |
| Cinco carteras sin repetir fondo | 52 ISIN distintos, comprobados por ISIN, nombre y clase hermana | Ninguna línea se abarata con un fondo ya usado |
| Cartera diversificada | 82,95 % de RV, núcleo indexado (35 %) y once líneas con satélites de sector, región y tamaño. Es la cartera con mayor esperanza y también con mayor caída. | Ver §4 |
| Solo fondos del listado | Todos los ISIN están en `finance/fondos-myinvestor/` | Sin ETF ni acciones: traspaso sin peaje fiscal |
| Sin distribución de dividendos | 11/11 clases de acumulación | Nada |

**Supuestos escritos, no reglas heredadas:** horizonte de 15 años o más, colchón de 6-12 meses fuera de la cartera, sin aportaciones modeladas y sin lista negra de carteras anteriores (el mandato solo prohíbe repetir dentro de estas cinco). Si el horizonte es de 5 años, bajar la RV a 40-50 %.

## 2. Cartera

| # | Rol | Fondo | ISIN | € | % | TER | €/año | RV | Mínimo operativo |
| --: | --- | --- | --- | --: | --: | --: | --: | --: | --- |
| 1 | Núcleo MSCI World indexado | Vanguard Global Stock Index Fund EUR Acc | `IE00B03HD191` | 35.000 | 35,00 % | 0,18 % | 63 | 99,96 % | MCP 20/11: 1.00 EUR |
| 2 | RV USA crecimiento activo | T. Rowe Price Funds SICAV - US Blue Chip Equity Fund A (EUR) | `LU1438969195` | 8.000 | 8,00 % | 1,61 % | 129 | 99,52 % | web ficha: 1.000 EUR (Finect) |
| 3 | Satélite tecnología global activo | Polar Capital Global Technology Fund R EUR (Acc) | `IE00BM95B621` | 7.000 | 7,00 % | 1,58 % | 111 | 94,48 % | web ficha: 0.00 EUR |
| 4 | Satélite salud global activo | BlackRock Global Funds - World Healthscience Fund A2 (EUR) | `LU0171307068` | 6.000 | 6,00 % | 1,81 % | 109 | 97,69 % | web ficha: 5.000 USD o equivalente (Finect … |
| 5 | RV emergentes crecimiento activo | Baillie Gifford Worldwide Emerging Markets Leading Companies F … | `IE00BK5TW610` | 7.000 | 7,00 % | 1,60 % | 112 | 99,47 % | web ficha: 1.000 EUR |
| 6 | RV Asia ex-Japón activo | Nordea 1 - Asia ex Japan Equity Fund BP EUR | `LU0173782102` | 5.000 | 5,00 % | 1,84 % | 92 | 96,70 % | web ficha: 0.00 EUR |
| 7 | RV Europa core activo | Goldman Sachs Europe CORE Equity Portfolio Base Acc EUR | `LU0234681749` | 6.000 | 6,00 % | 1,37 % | 82 | 99,71 % | web ficha: 5.000 EUR |
| 8 | Small caps globales activo | Janus Henderson Horizon Global Smaller Companies Fund A2 EUR | `LU1984712320` | 5.000 | 5,00 % | 1,90 % | 95 | 95,50 % | web ficha: 2.500 EUR |
| 9 | Infraestructura cotizada activo | First Sentier Global Listed Infrastructure Fund Class I (Accum … | `IE00BYSJTY39` | 5.000 | 5,00 % | 1,59 % | 80 | 99,40 % | web ficha: 1.00 EUR |
| 10 | Titulizaciones ABS euro activo | Aegon European ABS Fund A EUR Acc | `IE00BG226Z29` | 11.000 | 11,00 % | 0,66 % | 73 | 0,00 % | web ficha: 0.00 EUR |
| 11 | Monetario EUR soberano | Pictet-Sovereign Short-Term Money Market EUR-P | `LU0366536711` | 5.000 | 5,00 % | 0,17 % | 9 | 0,00 % | web ficha: 0.00 EUR |
| | **Total** | **11 fondos** | | **100.000** | **100 %** | **0,9528 %** | **952,80** | **82,95 %** | |

## 3. Bloques por rol

| Bloque | € | % del total | TER medio | €/año |
| --- | --: | --: | --: | --: |
| Convicción activa de RV | 49.000 | 49,00 % | 1,65 % | 809 |
| Índice | 35.000 | 35,00 % | 0,18 % | 63 |
| Crédito y liquidez | 16.000 | 16,00 % | 0,51 % | 81 |

## 4. Métricas

| Métrica | Valor | Cómo se calcula |
| --- | --- | --- |
| RV *look-through* | 82,95 % | Σ importe × RV declarada en la ficha |
| Renta fija | 11,43 % | Σ importe × RF declarada en la ficha |
| Caída de manual | −33,52 % = 33.522 € | −(40 % × RV + 3 % × RF) |
| Coste anual | 952,80 € = 0,9528 % | Σ importe × TER snapshot |
| Duración estimada de la RF | 1,50 años sobre 11.000 €; 0,00 años sobre 5.000 € | +100 pb cuesta 165 € |
| Esperanza central | 6,25 % | Σ importe × retorno esperado por sleeve |
| Escenario pesimista | 4,18 % | RV −2,5 pp de retorno esperado |
| Escenario favorable | 7,49 % | RV +1,5 pp de retorno esperado |
| Indexado | 35,00 % | gestión indexada declarada o índice nombrado en la ficha |

**Supuestos de la esperanza** (estimación del agente, no dato de mercado): RV desarrollada 6,7 %, small caps 7,0 %, emergentes y Asia 7,5 %, Japón 6,7 %, crédito y agregado 2,8-3,2 %, liquidez 2,3 %. La esperanza la decide el % de RV, no la selección de fondos; la prima de convicción está incluida solo donde la ficha declara un sesgo value o de calidad.

## 5. Geografía por *look-through*

| Región declarada | € de RV | % de la RV con desglose |
| --- | --: | --: |
| EE. UU. | 9.410 | 16,45 % |
| Estados Unidos | 2.850 | 4,98 % |
| Asia desarrollada | 1.149 | 2,01 % |
| Japón | 890 | 1,56 % |
| Reino Unido | 456 | 0,80 % |
| Zona Euro | 447 | 0,78 % |
| Canadá | 312 | 0,55 % |
| Australasia | 280 | 0,49 % |
| Zona euro | 110 | 0,19 % |

Base con desglose: 57.206 € de RV (68,97 % de la RV total). Los fondos sin desglose regional no entran en la tabla; es un cálculo derivado de las fichas, no un dato de la gestora.

## 6. Razón fondo a fondo

- **`IE00B03HD191` Vanguard Global Stock Index Fund EUR Acc** — Vanguard Global Stock EUR Acc; warning señala iShares S (usado en C1, fondo distinto). 3A 17,44 % · 5A 10,02 % · vol 11,16 %; TER 0,18 %; MCP 20/11: 1.00 EUR.
- **`LU1438969195` T. Rowe Price Funds SICAV - US Blue Chip Equity Fund A (EUR)** — T. Rowe US Blue Chip A EUR; top10 58.9%, tech 52.3%; 2026 YTD Q5; DD 5A −36.7%. 3A 15,55 % · 5A 5,96 % · vol 18,84 %; TER 1,61 %; web ficha: 1.000 EUR (Finect).
- **`IE00BM95B621` Polar Capital Global Technology Fund R EUR (Acc)** — Polar Global Technology R EUR; éxito 10% (Finect) vs 0% quefondos — presupuestada; Q1 2023-2026. 3A 36,43 % · 5A 16,87 %; TER 1,58 %; web ficha: 0.00 EUR.
- **`LU0171307068` BlackRock Global Funds - World Healthscience Fund A2 (EUR)** — BGF World Healthscience A2 EUR; línea 6.000 € ≥ mínimo; 2025 Q5. 3A 10,50 % · 5A 5,88 %; TER 1,81 %; web ficha: 5.000 USD o equivalente (Finect 0).
- **`IE00BK5TW610` Baillie Gifford Worldwide Emerging Markets Leading Companies Fund A EU …** — BG EM Leading Companies A EUR; vol 31%, tech 42%; Q4 2022/2024. 3A 16,41 % · 5A 3,77 % · vol 19,82 %; TER 1,60 %; web ficha: 1.000 EUR.
- **`LU0173782102` Nordea 1 - Asia ex Japan Equity Fund BP EUR** — Nordea Asia ex-Japan BP EUR; Q1 3A/5A trailing. 3A 18,16 % · 5A 5,73 % · vol 18,79 %; TER 1,84 %; web ficha: 0.00 EUR.
- **`LU0234681749` Goldman Sachs Europe CORE Equity Portfolio Base Acc EUR** — GS Europe CORE Base Acc EUR; línea 6.000 € ≥ mínimo; Q1 2024/2025. 3A 18,48 % · 5A 10,34 % · vol 10,20 %; TER 1,37 %; web ficha: 5.000 EUR.
- **`LU1984712320` Janus Henderson Horizon Global Smaller Companies Fund A2 EUR** — Janus Global Smaller Companies A2; éxito 10% vs benchmark HWM; Q1 2023-2025. 3A 18,72 % · 5A 9,52 % · vol 14,23 %; TER 1,90 %; web ficha: 2.500 EUR.
- **`IE00BYSJTY39` First Sentier Global Listed Infrastructure Fund Class I (Accumulation) …** — First Sentier Global Listed Infra I EUR; Lazard descartado (mín 10.000 GBP). 3A 12,99 % · 5A 7,33 % · vol 11,07 %; TER 1,59 %; web ficha: 1.00 EUR.
- **`IE00BG226Z29` Aegon European ABS Fund A EUR Acc** — Aegon European ABS A EUR; Q1 2022/2026; gestión 1.50% vs TER 0.66% (anomalía, snapshot manda); exit fee discrepante. 3A 4,35 % · 5A 3,00 %; TER 0,66 %; web ficha: 0.00 EUR.
- **`LU0366536711` Pictet-Sovereign Short-Term Money Market EUR-P** — Pictet Sovereign ST MM EUR-P; Q3-4, solo soberano. 3A 2,67 % · 5A 2,03 %; TER 0,17 %; web ficha: 0.00 EUR.

La ficha completa de cada uno, con todas las pegas y fuentes, está en [`fondos-revisados.md`](fondos-revisados.md).

## 7. Ejecución

Dinero nuevo: una orden de suscripción por fondo, sin reembolso previo. La tabla está en el orden en que conviene lanzarla: primero las líneas con mínimo inicial más alto. El corte se lee en la ficha de cada fondo; verificar en pantalla el día de la orden.

| # | Fondo | ISIN | € | Mínimo inicial | Orden |
| --: | --- | --- | --: | --- | --- |
| 1 | Goldman Sachs Europe CORE Equity Portfolio Base Acc EUR | `LU0234681749` | 6.000 | web ficha: 5.000 EUR | Suscribir 6.000 € |
| 2 | BlackRock Global Funds - World Healthscience Fund A2 (EUR) | `LU0171307068` | 6.000 | web ficha: 5.000 USD o equivalente (Finect 0) | Suscribir 6.000 € |
| 3 | Janus Henderson Horizon Global Smaller Companies Fund A2 EUR | `LU1984712320` | 5.000 | web ficha: 2.500 EUR | Suscribir 5.000 € |
| 4 | T. Rowe Price Funds SICAV - US Blue Chip Equity Fund A (EUR) | `LU1438969195` | 8.000 | web ficha: 1.000 EUR (Finect) | Suscribir 8.000 € |
| 5 | Baillie Gifford Worldwide Emerging Markets Leading Companies … | `IE00BK5TW610` | 7.000 | web ficha: 1.000 EUR | Suscribir 7.000 € |
| 6 | Vanguard Global Stock Index Fund EUR Acc | `IE00B03HD191` | 35.000 | MCP 20/11: 1.00 EUR | Suscribir 35.000 € |
| 7 | First Sentier Global Listed Infrastructure Fund Class I (Acc … | `IE00BYSJTY39` | 5.000 | web ficha: 1.00 EUR | Suscribir 5.000 € |
| 8 | Polar Capital Global Technology Fund R EUR (Acc) | `IE00BM95B621` | 7.000 | web ficha: 0.00 EUR | Suscribir 7.000 € |
| 9 | Nordea 1 - Asia ex Japan Equity Fund BP EUR | `LU0173782102` | 5.000 | web ficha: 0.00 EUR | Suscribir 5.000 € |
| 10 | Aegon European ABS Fund A EUR Acc | `IE00BG226Z29` | 11.000 | web ficha: 0.00 EUR | Suscribir 11.000 € |
| 11 | Pictet-Sovereign Short-Term Money Market EUR-P | `LU0366536711` | 5.000 | web ficha: 0.00 EUR | Suscribir 5.000 € |

## 8. Qué se descarta

| Candidato | Razón con número | Solución adoptada |
| --- | --- | --- |
| Lazard Global Listed Infrastructure | mínimo 10.000 GBP; línea de 5.000 € | First Sentier, mínimo 1 € |
| T. Rowe Price / Capital Group en el núcleo | solape con la convicción value ya presente | T. Rowe US Blue Chip se conserva solo como satélite de crecimiento |

## 9. Verificación, revisión y lo que queda abierto

**Web 20/11 — `LU0171307068` (mínimo y política de dividendos).** Ficha oficial BlackRock: «Class A2 (EUR) (Accumulating)», Minimum Initial Investment USD 5.000,00, Ongoing Charges 1,81 %, Management Fee 1,50 %, Performance Fee 0,00 %, desviación 3A 14,20 %, 2022 +0,6 %, 2025 +0,1 %. La línea de 6.000 € cubre el mínimo; el cargo inicial del 5 % del folleto se verifica en pantalla en la plataforma. <https://www.blackrock.com/se/professionals/products/229337/blackrock-world-healthscience-a2-eur-fund>

**Web 20/11 — `IE00BG226Z29` (anomalía de comisiones y cambio de gestora).** Aegon AM anuncia que a partir del 23/11/2026 la gestora del ICAV pasa a Carne Global Fund Managers (Ireland) Limited. La página oficial solo lista las clases USD G/D/X, no la clase EUR A del catálogo; la anomalía TER 0,66 % frente a gestión 1,50 % queda sin resolver y se mantiene el TER del snapshot como coste modelado, con aviso. <https://www.aegonam.com/funds-resources/fixed-income/european-abs-fund/>

**Revisión.** Revisar el 30/11/2027 y cada 12 meses: (a) TER real en pantalla frente al snapshot; (b) comisiones de éxito efectivas; (c) clases hermanas que abaraten una línea sin cambiar de fondo —recuerda que cambiar de clase de un fondo ya comprado es un reembolso—; (d) que ningún fondo pase a distribuir o a tener soft close; (e) en C2/C5, evidencia de cada gestor contra su índice neto de TER.

**Sin decidir:** horizonte real, colchón fuera de la cartera, aportaciones periódicas y fecha de ejecución. Ninguna orden se lanza hasta la revisión del titular.

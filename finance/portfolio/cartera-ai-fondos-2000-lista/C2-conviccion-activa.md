---
title: "C2 — Convicción activa"
date: 2026-11-20
type: portfolio-proposal
category: finance
tags: [gestion-activa, conviccion, value, calidad, global, japon, emergentes]
status: propuesta
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/validacion.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/fondos-revisados.md
---

# C2 — Convicción activa

> **Qué es.** 10 fondos, 100.000 € exactos, **78,65 % de renta variable real** (look-through) y **1.248,60 €/año (1,2486 %)**. Caída de manual **−32,06 % (32.057 €)** y **≈6,26 % esperado** con los supuestos de §4 (4,29 % pesimista / 7,44 % favorable).
>
> Aquí se paga 1,25 % de TER medio por una apuesta explícita: que esos procesos batan a su índice neto de comisión. Si no baten, la cartera es simplemente más cara que la C1; la prueba tiene fecha en §9.
>
> **Método y límite.** Fichas del repo (snapshot de la app 19/11/2026 + MCP 20/11/2026) y cuatro verificaciones web puntuales el 20/11/2026, citadas en §9. **No es asesoramiento financiero**: la decisión y la ejecución son del titular.

---

## 1. Mandato

| Lo que pide el encargo | Cómo se cumple | Qué cuesta |
| --- | --- | --- |
| 100.000 € | 10 líneas que suman exactamente 100.000 € | Nada |
| Dos carteras sin repetir fondo | 21 ISIN distintos, comprobados por ISIN, nombre y clase hermana | Ninguna línea se abarata con un fondo ya usado |
| Cartera diversificada | la renta variable se elige por proceso de gestión con evidencia en la ficha (value, calidad, dividendo creciente, multifactor, cuantitativo), más crédito activo de coste bajo. Ningún indexado. | Ver §4 |
| Solo fondos del listado | Todos los ISIN están en `finance/fondos-myinvestor/` | Sin ETF ni acciones: traspaso sin peaje fiscal |
| Sin distribución de dividendos | 10/10 clases de acumulación | Nada |

**Supuestos escritos, no reglas heredadas:** horizonte de 15 años o más, colchón de 6-12 meses fuera de la cartera, sin aportaciones modeladas y sin lista negra de carteras anteriores (el mandato solo prohíbe repetir dentro de estas dos). Si el horizonte es de 5 años, bajar la RV a 40-50 %.

## 2. Cartera

| # | Rol | Fondo | ISIN | € | % | TER | €/año | RV | Mínimo operativo |
| --: | --- | --- | --- | --: | --: | --: | --: | --: | --- |
| 1 | Núcleo RV global value activo | Robeco BP Global Premium Equities D EUR (Acc) | `LU0203975437` | 20.000 | 20,00 % | 1,46 % | 292 | 98,34 % | web ficha: 0.00 EUR |
| 2 | RV global calidad activo | Fundsmith Equity Fund T EUR Acc | `LU0690375182` | 12.000 | 12,00 % | 1,08 % | 130 | 100,00 % | web ficha: 2.000 EUR (Finect 1.000) |
| 3 | RV global dividendo creciente activo | Guinness Global Equity Income D EUR Accumulation | `IE00BDGV0290` | 10.000 | 10,00 % | 1,27 % | 127 | 99,30 % | web ficha: 0.00 EUR |
| 4 | RV value ibérica/small-mid activo | Horos Value Internacional FI | `ES0146309002` | 8.000 | 8,00 % | 1,86 % | 149 | 90,76 % | web ficha: 100 EUR |
| 5 | RV Japón activo cubierto EUR | Man GLG Japan CoreAlpha Equity Class D H EUR | `IE00B5648R31` | 8.000 | 8,00 % | 1,71 % | 137 | 98,98 % | web ficha: 1.000 EUR |
| 6 | RV emergentes cuantitativo activo | Robeco QI EM Active Equities D EUR | `LU0329355670` | 8.000 | 8,00 % | 1,52 % | 122 | 99,93 % | web ficha: 0.00 EUR |
| 7 | RV Asia ex-Japón activo | Federated Hermes Asia ex-Japan Equity Fund Class R Acc | `IE00B88WFS66` | 6.000 | 6,00 % | 1,58 % | 95 | 98,86 % | MCP 20/11: 0.00 EUR |
| 8 | RV Europa multifactor activo | Allianz Global Investors Fund - Allianz Best Styles Europe Equ … | `LU1019963369` | 8.000 | 8,00 % | 1,37 % | 110 | 99,30 % | web ficha: 0.00 EUR |
| 9 | Crédito euro corto plazo activo | Neuberger Berman Short Duration Euro Bond Fund Class EUR I Acc … | `IE00BFZMJT78` | 12.000 | 12,00 % | 0,25 % | 30 | 0,00 % | MCP 20/11: 1.00 EUR |
| 10 | High yield global cubierto EUR activo | UBAM - Global High Yield Solution AHC EUR | `LU0569862609` | 8.000 | 8,00 % | 0,73 % | 58 | 0,00 % | web ficha: KID sin mínimo |
| | **Total** | **10 fondos** | | **100.000** | **100 %** | **1,2486 %** | **1.248,60** | **78,65 %** | |

## 3. Bloques por rol

| Bloque | € | % del total | TER medio | €/año |
| --- | --: | --: | --: | --: |
| Convicción activa de RV | 80.000 | 80,00 % | 1,45 % | 1.160 |
| Crédito y liquidez | 20.000 | 20,00 % | 0,44 % | 88 |

## 4. Métricas

| Métrica | Valor | Cómo se calcula |
| --- | --- | --- |
| RV *look-through* | 78,65 % | Σ importe × RV declarada en la ficha |
| Renta fija | 19,93 % | Σ importe × RF declarada en la ficha |
| Caída de manual | −32,06 % = 32.057 € | −(40 % × RV + 3 % × RF) |
| Coste anual | 1.248,60 € = 1,2486 % | Σ importe × TER snapshot |
| Duración estimada de la RF | 1,50 años sobre 12.000 €; 3,00 años sobre 8.000 € | +100 pb cuesta 419 € |
| Esperanza central | 6,26 % | Σ importe × retorno esperado por sleeve |
| Escenario pesimista | 4,29 % | RV −2,5 pp de retorno esperado |
| Escenario favorable | 7,44 % | RV +1,5 pp de retorno esperado |
| Indexado | 0,00 % | gestión indexada declarada o índice nombrado en la ficha |

**Supuestos de la esperanza** (estimación del agente, no dato de mercado): RV desarrollada 6,7 %, small caps 7,0 %, emergentes y Asia 7,5 %, Japón 6,7 %, crédito y agregado 2,8-3,2 %, liquidez 2,3 %. La esperanza la decide el % de RV, no la selección de fondos; la prima de convicción está incluida solo donde la ficha declara un sesgo value o de calidad.

## 5. Geografía por *look-through*

| Región declarada | € de RV | % de la RV con desglose |
| --- | --: | --: |
| Estados Unidos | 9.550 | 15,23 % |
| EE. UU. | 8.656 | 13,80 % |
| Zona Euro | 7.075 | 11,28 % |
| Asia desarrollada | 3.788 | 6,04 % |
| Asia emergente | 2.884 | 4,60 % |
| Reino Unido | 2.841 | 4,53 % |
| Japón | 1.276 | 2,04 % |
| Europa ex-Zona Euro | 1.107 | 1,77 % |
| incluye Iberoamérica | 643 | 1,02 % |

Base con desglose: 62.709 € de RV (79,73 % de la RV total). Los fondos sin desglose regional no entran en la tabla; es un cálculo derivado de las fichas, no un dato de la gestora.

## 6. Razón fondo a fondo

- **`LU0203975437` Robeco BP Global Premium Equities D EUR (Acc)** — Robeco BP; prima value 0.5pp declarada como apuesta. 3A 18,34 % · 5A 11,89 %; TER 1,46 %; web ficha: 0.00 EUR.
- **`LU0690375182` Fundsmith Equity Fund T EUR Acc** — Fundsmith; 3A 7.0 / 2025 Q5 — proceso quality, bache reciente escrito. 3A 7,00 % · 5A 2,51 %; TER 1,08 %; web ficha: 2.000 EUR (Finect 1.000).
- **`IE00BDGV0290` Guinness Global Equity Income D EUR Accumulation** — Guinness; SRRI 3. 3A 13,49 % · 5A 9,03 % · vol 10,67 %; TER 1,27 %; web ficha: 0.00 EUR.
- **`ES0146309002` Horos Value Internacional FI** — Horos; 2026 YTD Q5; eurozona 52%, EM 16%, USA 7%. 3A 16,04 % · 5A 11,77 % · vol 10,75 %; TER 1,86 %; web ficha: 100 EUR.
- **`IE00B5648R31` Man GLG Japan CoreAlpha Equity Class D H EUR** — Man GLG CoreAlpha D H EUR; vol 20.45%. 3A 24,22 % · 5A 24,70 % · vol 15,03 %; TER 1,71 %; web ficha: 1.000 EUR.
- **`LU0329355670` Robeco QI EM Active Equities D EUR** — Robeco QI EM Active. 3A 18,89 % · 5A 10,13 % · vol 15,99 %; TER 1,52 %; web ficha: 0.00 EUR.
- **`IE00B88WFS66` Federated Hermes Asia ex-Japan Equity Fund Class R Acc** — Hermes R EUR; MCP TER 1.59 vs snapshot 1.58; manda snapshot; clase F (0.83) mínimo 100k no operable. 3A 18,31 % · 5A 8,75 % · vol 15,87 %; TER 1,58 %; MCP 20/11: 0.00 EUR.
- **`LU1019963369` Allianz Global Investors Fund - Allianz Best Styles Europe Equity AT E …** — Allianz Best Styles Europe AT. 3A 15,57 % · 5A 8,35 % · vol 9,95 %; TER 1,37 %; web ficha: 0.00 EUR.
- **`IE00BFZMJT78` Neuberger Berman Short Duration Euro Bond Fund Class EUR I Accumulatin …** — Neuberger I; 2025 Q1; 2022 −5.59%. 3A 4,34 % · 5A 2,39 %; TER 0,25 %; MCP 20/11: 1.00 EUR.
- **`LU0569862609` UBAM - Global High Yield Solution AHC EUR** — UBAM HY Solution AHC; sintético vía CDS; duración ~3 estimada. 3A 7,09 % · 5A 4,31 % · vol 4,58 %; TER 0,73 %; web ficha: KID sin mínimo.

La ficha completa de cada uno, con todas las pegas y fuentes, está en [`fondos-revisados.md`](fondos-revisados.md).

## 7. Ejecución

Dinero nuevo: una orden de suscripción por fondo, sin reembolso previo. La tabla está en el orden en que conviene lanzarla: primero las líneas con mínimo inicial más alto. El corte se lee en la ficha de cada fondo; verificar en pantalla el día de la orden.

| # | Fondo | ISIN | € | Mínimo inicial | Orden |
| --: | --- | --- | --: | --- | --- |
| 1 | Fundsmith Equity Fund T EUR Acc | `LU0690375182` | 12.000 | web ficha: 2.000 EUR (Finect 1.000) | Suscribir 12.000 € |
| 2 | Man GLG Japan CoreAlpha Equity Class D H EUR | `IE00B5648R31` | 8.000 | web ficha: 1.000 EUR | Suscribir 8.000 € |
| 3 | Horos Value Internacional FI | `ES0146309002` | 8.000 | web ficha: 100 EUR | Suscribir 8.000 € |
| 4 | Neuberger Berman Short Duration Euro Bond Fund Class EUR I A … | `IE00BFZMJT78` | 12.000 | MCP 20/11: 1.00 EUR | Suscribir 12.000 € |
| 5 | Robeco BP Global Premium Equities D EUR (Acc) | `LU0203975437` | 20.000 | web ficha: 0.00 EUR | Suscribir 20.000 € |
| 6 | Guinness Global Equity Income D EUR Accumulation | `IE00BDGV0290` | 10.000 | web ficha: 0.00 EUR | Suscribir 10.000 € |
| 7 | Robeco QI EM Active Equities D EUR | `LU0329355670` | 8.000 | web ficha: 0.00 EUR | Suscribir 8.000 € |
| 8 | Federated Hermes Asia ex-Japan Equity Fund Class R Acc | `IE00B88WFS66` | 6.000 | MCP 20/11: 0.00 EUR | Suscribir 6.000 € |
| 9 | Allianz Global Investors Fund - Allianz Best Styles Europe E … | `LU1019963369` | 8.000 | web ficha: 0.00 EUR | Suscribir 8.000 € |
| 10 | UBAM - Global High Yield Solution AHC EUR | `LU0569862609` | 8.000 | web ficha: KID sin mínimo | Suscribir 8.000 € |

## 8. Qué se descarta

| Candidato | Razón con número | Solución adoptada |
| --- | --- | --- |
| Federated Hermes Asia ex-Japan clase F | TER 0,83 % pero mínimo 100.000 €; la línea es de 6.000 € | se toma la clase R a 1,58 % y se paga 45 €/año de acceso |
| Dodge & Cox / gestoras de valor clásicas | mínimos y solape con el núcleo value | se prefiere Robeco BP value con mínimo 0 € |

## 9. Verificación, revisión y lo que queda abierto

No hizo falta verificación web adicional: todos los campos decisivos estaban en la ficha.

**Revisión.** Revisar el 30/11/2027 y cada 12 meses: (a) TER real en pantalla frente al snapshot; (b) comisiones de éxito efectivas; (c) clases hermanas que abaraten una línea sin cambiar de fondo —recuerda que cambiar de clase de un fondo ya comprado es un reembolso—; (d) que ningún fondo pase a distribuir o a tener soft close; (e) en C2/C5, evidencia de cada gestor contra su índice neto de TER.

**Sin decidir:** horizonte real, colchón fuera de la cartera, aportaciones periódicas y fecha de ejecución. Ninguna orden se lanza hasta la revisión del titular.

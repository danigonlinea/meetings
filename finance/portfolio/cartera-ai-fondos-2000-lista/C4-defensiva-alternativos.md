---
title: "C4 — Defensiva con alternativos"
date: 2026-11-20
type: portfolio-proposal
category: finance
tags: [defensiva, alternativos, cat-bonds, market-neutral, managed-futures, baja-volatilidad]
status: propuesta
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/validacion.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/fondos-revisados.md
---

# C4 — Defensiva con alternativos

> **Qué es.** 11 fondos, 100.000 € exactos, **35,49 % de renta variable real** (look-through) y **766,10 €/año (0,7661 %)**. Caída de manual **−15,51 % (15.514 €)** y **≈3,87 % esperado** con los supuestos de §4 (2,98 % pesimista / 4,40 % favorable).
>
> La caída de manual es −15,51 %, menos de la mitad que en C5. El coste de esa tranquilidad es 0,77 % de TER y una dependencia fuerte de que los alternativos se comporten como se dice en la ficha: los tres tienen comisiones de éxito o estructuras complejas.
>
> **Método y límite.** Fichas del repo (snapshot de la app 19/11/2026 + MCP 20/11/2026) y cuatro verificaciones web puntuales el 20/11/2026, citadas en §9. **No es asesoramiento financiero**: la decisión y la ejecución son del titular.

---

## 1. Mandato

| Lo que pide el encargo | Cómo se cumple | Qué cuesta |
| --- | --- | --- |
| 100.000 € | 11 líneas que suman exactamente 100.000 € | Nada |
| Dos carteras sin repetir fondo | 21 ISIN distintos, comprobados por ISIN, nombre y clase hermana | Ninguna línea se abarata con un fondo ya usado |
| Cartera diversificada | 35,49 % de RV, 43,88 % de renta fija y liquidez, y tres alternativos descorrelacionados (cat bonds, market neutral, managed futures), con dos fondos de baja volatilidad y dos mixtos defensivos. | Ver §4 |
| Solo fondos del listado | Todos los ISIN están en `finance/fondos-myinvestor/` | Sin ETF ni acciones: traspaso sin peaje fiscal |
| Sin distribución de dividendos | 11/11 clases de acumulación | Nada |

**Supuestos escritos, no reglas heredadas:** horizonte de 15 años o más, colchón de 6-12 meses fuera de la cartera, sin aportaciones modeladas y sin lista negra de carteras anteriores (el mandato solo prohíbe repetir dentro de estas dos). Si el horizonte es de 5 años, bajar la RV a 40-50 %.

## 2. Cartera

| # | Rol | Fondo | ISIN | € | % | TER | €/año | RV | Mínimo operativo |
| --: | --- | --- | --- | --: | --: | --: | --: | --: | --- |
| 1 | RV global baja volatilidad activo | Robeco QI Global Conservative Equities D EUR | `LU0705782398` | 18.000 | 18,00 % | 1,01 % | 182 | 99,15 % | web ficha: 0.00 EUR |
| 2 | RV global baja volatilidad activo (2) | AB Low Volatility Eq A EUR | `LU1998907197` | 12.000 | 12,00 % | 1,67 % | 200 | 96,31 % | web ficha: 2.000 EUR / 750 adicional |
| 3 | Mixto cartera permanente (regla fija) | MyInvestor Cartera Permanente | `ES0156572002` | 10.000 | 10,00 % | 0,59 % | 59 | 24,34 % | web ficha: 0.00 EUR |
| 4 | Mixto defensivo value activo | Cobas Renta FI | `ES0119207001` | 10.000 | 10,00 % | 0,31 % | 31 | 14,50 % | MCP ficha: 100 EUR |
| 5 | Cat bonds (alternativo descorrelacionado) | Twelve Capital UCITS ICAV - Twelve Cat Bond Fund P EUR Acc | `IE00BD2B9710` | 5.000 | 5,00 % | 1,30 % | 65 | 0,00 % | MCP ficha: 1 EUR |
| 6 | Market neutral RV (alternativo) | Jupiter Merian Global Equity Absolute Return Fund L (EUR) Hedg … | `IE00BLP5S460` | 5.000 | 5,00 % | 1,55 % | 78 | 44,09 % | web ficha: 500 EUR |
| 7 | Managed futures (alternativo) | MontLake DUNN WMA Institutional UCITS Fund EUR Retail Class Po … | `IE00BWVFLK42` | 5.000 | 5,00 % | 1,34 % | 67 | 0,00 % | MCP 20/11: 1.000 EUR |
| 8 | RF euro ultracorta activo | DWS Euro Ultra Short Fixed Inc NC | `LU0080237943` | 12.000 | 12,00 % | 0,15 % | 18 | 0,00 % | web ficha: 0.00 EUR |
| 9 | RF corto plazo euro activo | Santalucía Renta Fija Corto Plazo Euro MY | `ES0170156048` | 10.000 | 10,00 % | 0,13 % | 13 | 0,00 % | web ficha: 0.00 EUR |
| 10 | Ligado a inflación global corto cubierto EUR | AXA World Funds - Global Inflation Short Duration Bonds A Capi … | `LU1353950725` | 6.000 | 6,00 % | 0,75 % | 45 | 0,00 % | web ficha: 0.00 USD |
| 11 | Monetario EUR | Ofi Invest ISR Monétaire CT E | `FR0010738229` | 7.000 | 7,00 % | 0,12 % | 8 | 0,00 % | MCP ficha: 0.00 EUR |
| | **Total** | **11 fondos** | | **100.000** | **100 %** | **0,7661 %** | **766,10** | **35,49 %** | |

## 3. Bloques por rol

| Bloque | € | % del total | TER medio | €/año |
| --- | --: | --: | --: | --: |
| Mixtos y alternativos | 35.000 | 35,00 % | 0,86 % | 300 |
| Crédito y liquidez | 35.000 | 35,00 % | 0,24 % | 84 |
| Convicción activa de RV | 30.000 | 30,00 % | 1,27 % | 382 |

## 4. Métricas

| Métrica | Valor | Cómo se calcula |
| --- | --- | --- |
| RV *look-through* | 35,49 % | Σ importe × RV declarada en la ficha |
| Renta fija | 43,88 % | Σ importe × RF declarada en la ficha |
| Caída de manual | −15,51 % = 15.514 € | −(40 % × RV + 3 % × RF) |
| Coste anual | 766,10 € = 0,7661 % | Σ importe × TER snapshot |
| Duración estimada de la RF | 0,50 años sobre 5.000 €; 0,50 años sobre 12.000 €; 1,00 años sobre 10.000 €; 2,00 años sobre 6.000 €; 0,00 años sobre 7.000 € | +100 pb cuesta 633 € |
| Esperanza central | 3,87 % | Σ importe × retorno esperado por sleeve |
| Escenario pesimista | 2,98 % | RV −2,5 pp de retorno esperado |
| Escenario favorable | 4,40 % | RV +1,5 pp de retorno esperado |
| Indexado | 0,00 % | gestión indexada declarada o índice nombrado en la ficha |

**Supuestos de la esperanza** (estimación del agente, no dato de mercado): RV desarrollada 6,7 %, small caps 7,0 %, emergentes y Asia 7,5 %, Japón 6,7 %, crédito y agregado 2,8-3,2 %, liquidez 2,3 %. La esperanza la decide el % de RV, no la selección de fondos; la prima de convicción está incluida solo donde la ficha declara un sesgo value o de calidad.

## 5. Geografía por *look-through*

| Región declarada | € de RV | % de la RV con desglose |
| --- | --: | --: |
| EE. UU. | 9.437 | 30,59 % |
| Estados Unidos | 6.437 | 20,86 % |
| Asia desarrollada | 2.348 | 7,61 % |
| Japón | 1.945 | 6,30 % |
| Zona Euro | 1.615 | 5,23 % |
| Reino Unido | 1.250 | 4,05 % |
| Zona euro | 1.169 | 3,79 % |
| Europa ex-euro | 1.165 | 3,78 % |
| Canadá | 1.124 | 3,64 % |

Base con desglose: 30.854 € de RV (86,93 % de la RV total). Los fondos sin desglose regional no entran en la tabla; es un cálculo derivado de las fichas, no un dato de la gestora.

## 6. Razón fondo a fondo

- **`LU0705782398` Robeco QI Global Conservative Equities D EUR** — Robeco QI Global Conservative D; 2022 Q1. 3A 14,26 % · 5A 8,58 %; TER 1,01 %; web ficha: 0.00 EUR.
- **`LU1998907197` AB Low Volatility Eq A EUR** — AB Low Volatility A EUR; 2024 Q1; patrimonio de clase discrepante entre fuentes. 3A 11,21 % · 5A 7,54 % · vol 9,73 %; TER 1,67 %; web ficha: 2.000 EUR / 750 adicional.
- **`ES0156572002` MyInvestor Cartera Permanente** — MyInvestor Cartera Permanente; 27.87% otros ≈ oro físico ETC; RF larga; fondo de autor (R. Ortega). 3A 10,33 % · 5A 3,25 % · vol 6,56 %; TER 0,59 %; web ficha: 0.00 EUR.
- **`ES0119207001` Cobas Renta FI** — Cobas Renta FI; 2022 +3.89%; vol 3A 2.85%; MCP TER 0.33 vs snapshot 0.31. 3A 8,81 % · 5A 6,82 % · vol 2,85 %; TER 0,31 %; MCP ficha: 100 EUR.
- **`IE00BD2B9710` Twelve Capital UCITS ICAV - Twelve Cat Bond Fund P EUR Acc** — Twelve Cat Bond P EUR; MCP TER 1.28 vs snapshot 1.30; reembolso ~10 días (repo). 3A 9,27 % · 5A 6,95 % · vol 2,26 %; TER 1,30 %; MCP ficha: 1 EUR.
- **`IE00BLP5S460` Jupiter Merian Global Equity Absolute Return Fund L (EUR) Hedged Acc** — Jupiter Merian Abs Return L EUR H; éxito 20% HWM; 3A Q1. 3A 10,12 % · 5A 9,68 %; TER 1,55 %; web ficha: 500 EUR.
- **`IE00BWVFLK42` MontLake DUNN WMA Institutional UCITS Fund EUR Retail Class Pooled Sha …** — DUNN WMA EUR Retail; MCP TER 1.08 + éxito 25% vs snapshot 1.34; se presupuesta 1.34 + 25%; 2022 +24.6%. 3A 4,51 % · 5A 5,29 % · vol 9,92 %; TER 1,34 %; MCP 20/11: 1.000 EUR.
- **`LU0080237943` DWS Euro Ultra Short Fixed Inc NC** — DWS Euro Ultra Short NC; 2022 último de categoría (−1.61%); exit fee 2.5% discrepante — verificar. 3A 3,38 % · 5A 2,37 %; TER 0,15 %; web ficha: 0.00 EUR.
- **`ES0170156048` Santalucía Renta Fija Corto Plazo Euro MY** — Santalucía CP Euro MY; sin límite de calidad por política; clase ~10.8 M€. 3A 3,28 % · 5A 2,27 %; TER 0,13 %; web ficha: 0.00 EUR.
- **`LU1353950725` AXA World Funds - Global Inflation Short Duration Bonds A Capitalisati …** — AXA Global Inflation Short Duration A EUR H; 2025 Q1. 3A 1,89 % · 5A 0,30 % · vol 2,09 %; TER 0,75 %; web ficha: 0.00 USD.
- **`FR0010738229` Ofi Invest ISR Monétaire CT E** — Ofi Invest ISR Monétaire CT E; TER ficha MCP 0.06 < gestión 0.11 (pega); snapshot 0.12 manda. 3A 2,88 % · 5A 2,26 % · vol 0,24 %; TER 0,12 %; MCP ficha: 0.00 EUR.

La ficha completa de cada uno, con todas las pegas y fuentes, está en [`fondos-revisados.md`](fondos-revisados.md).

## 7. Ejecución

Dinero nuevo: una orden de suscripción por fondo, sin reembolso previo. La tabla está en el orden en que conviene lanzarla: primero las líneas con mínimo inicial más alto. El corte se lee en la ficha de cada fondo; verificar en pantalla el día de la orden.

| # | Fondo | ISIN | € | Mínimo inicial | Orden |
| --: | --- | --- | --: | --- | --- |
| 1 | AB Low Volatility Eq A EUR | `LU1998907197` | 12.000 | web ficha: 2.000 EUR / 750 adicional | Suscribir 12.000 € |
| 2 | MontLake DUNN WMA Institutional UCITS Fund EUR Retail Class … | `IE00BWVFLK42` | 5.000 | MCP 20/11: 1.000 EUR | Suscribir 5.000 € |
| 3 | Jupiter Merian Global Equity Absolute Return Fund L (EUR) He … | `IE00BLP5S460` | 5.000 | web ficha: 500 EUR | Suscribir 5.000 € |
| 4 | Cobas Renta FI | `ES0119207001` | 10.000 | MCP ficha: 100 EUR | Suscribir 10.000 € |
| 5 | Twelve Capital UCITS ICAV - Twelve Cat Bond Fund P EUR Acc | `IE00BD2B9710` | 5.000 | MCP ficha: 1 EUR | Suscribir 5.000 € |
| 6 | Robeco QI Global Conservative Equities D EUR | `LU0705782398` | 18.000 | web ficha: 0.00 EUR | Suscribir 18.000 € |
| 7 | MyInvestor Cartera Permanente | `ES0156572002` | 10.000 | web ficha: 0.00 EUR | Suscribir 10.000 € |
| 8 | DWS Euro Ultra Short Fixed Inc NC | `LU0080237943` | 12.000 | web ficha: 0.00 EUR | Suscribir 12.000 € |
| 9 | Santalucía Renta Fija Corto Plazo Euro MY | `ES0170156048` | 10.000 | web ficha: 0.00 EUR | Suscribir 10.000 € |
| 10 | AXA World Funds - Global Inflation Short Duration Bonds A Ca … | `LU1353950725` | 6.000 | web ficha: 0.00 USD | Suscribir 6.000 € |
| 11 | Ofi Invest ISR Monétaire CT E | `FR0010738229` | 7.000 | MCP ficha: 0.00 EUR | Suscribir 7.000 € |

## 8. Qué se descarta

| Candidato | Razón con número | Solución adoptada |
| --- | --- | --- |
| Robeco / Fundsmith en baja volatilidad | ya son el núcleo de otras carteras y aquí duplicarían riesgo | AB Low Volatility, con patrimonio discrepante entre fuentes |
| DWS Ultra Short: comisión de reembolso 2,5 % (Finect/FT) | el KID oficial no la confirma | se mantiene el fondo con aviso y verificación en pantalla |

## 9. Verificación, revisión y lo que queda abierto

**Web 20/11 — `LU0080237943` (comisión de reembolso discrepante).** KID oficial DWS de 16/02/2026: «No fees or penalties will be charged by the company for any such transaction», periodo recomendado 183 días, riesgo 1/7 y beneficios reinvertidos. El 2,50 % que publicaban Finect y FT no aparece en el KID; se conserva como discrepancia a verificar en pantalla, no como coste modelado. <https://download.dws.com/download/asset/4b9b6e74-8baa-46ae-971a-c9895905b477?tenant=ActiveEmea>

**Revisión.** Revisar el 30/11/2027 y cada 12 meses: (a) TER real en pantalla frente al snapshot; (b) comisiones de éxito efectivas; (c) clases hermanas que abaraten una línea sin cambiar de fondo —recuerda que cambiar de clase de un fondo ya comprado es un reembolso—; (d) que ningún fondo pase a distribuir o a tener soft close; (e) en C2/C5, evidencia de cada gestor contra su índice neto de TER.

**Sin decidir:** horizonte real, colchón fuera de la cartera, aportaciones periódicas y fecha de ejecución. Ninguna orden se lanza hasta la revisión del titular.

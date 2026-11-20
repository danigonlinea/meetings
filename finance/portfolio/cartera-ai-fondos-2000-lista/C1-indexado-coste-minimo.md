---
title: "C1 — Índice de coste mínimo"
date: 2026-11-20
type: portfolio-proposal
category: finance
tags: [indice, coste-minimo, rv-global, regional, renta-fija-indexada]
status: propuesta
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/validacion.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/fondos-revisados.md
---

# C1 — Índice de coste mínimo

> **Qué es.** 9 fondos, 100.000 € exactos, **77,52 % de renta variable real** (look-through) y **132,20 €/año (0,1322 %)**. Caída de manual **−31,67 % (31.666 €)** y **≈5,99 % esperado** con los supuestos de §4 (4,05 % pesimista / 7,15 % favorable).
>
> La única decisión de esta cartera es pagar el índice más barato operable de cada exposición. No lleva convicción activa: si un gestor bate al índice, aquí no se cobra. El precio de esa elección es renunciar a cualquier alfa y aceptar el 72 % de EE. UU. del MSCI World.
>
> **Método y límite.** Fichas del repo (snapshot de la app 19/11/2026 + MCP 20/11/2026) y cuatro verificaciones web puntuales el 20/11/2026, citadas en §9. **No es asesoramiento financiero**: la decisión y la ejecución son del titular.

---

## 1. Mandato

| Lo que pide el encargo | Cómo se cumple | Qué cuesta |
| --- | --- | --- |
| 100.000 € | 9 líneas que suman exactamente 100.000 € | Nada |
| Cinco carteras sin repetir fondo | 52 ISIN distintos, comprobados por ISIN, nombre y clase hermana | Ninguna línea se abarata con un fondo ya usado |
| Cartera diversificada | todo el vehículo es indexado (100 %) y el TER medio se mantiene por debajo del 0,14 %. Núcleo MSCI World, small caps y tres regiones, con 22,13 % de renta fija indexada. | Ver §4 |
| Solo fondos del listado | Todos los ISIN están en `finance/fondos-myinvestor/` | Sin ETF ni acciones: traspaso sin peaje fiscal |
| Sin distribución de dividendos | 9/9 clases de acumulación | Nada |

**Supuestos escritos, no reglas heredadas:** horizonte de 15 años o más, colchón de 6-12 meses fuera de la cartera, sin aportaciones modeladas y sin lista negra de carteras anteriores (el mandato solo prohíbe repetir dentro de estas cinco). Si el horizonte es de 5 años, bajar la RV a 40-50 %.

## 2. Cartera

| # | Rol | Fondo | ISIN | € | % | TER | €/año | RV | Mínimo operativo |
| --: | --- | --- | --- | --: | --: | --: | --: | --: | --- |
| 1 | Núcleo MSCI World indexado | iShares Developed World Index (IE) Acc EUR clase S | `IE000ZYRH0Q7` | 40.000 | 40,00 % | 0,06 % | 24 | 99,29 % | MCP 20/11: 0.00 EUR |
| 2 | Small caps globales indexado | Vanguard Global Small-Cap Index Fund EUR Acc | `IE00B42W4L06` | 8.000 | 8,00 % | 0,30 % | 24 | 99,94 % | MCP 20/11: 1.00 EUR |
| 3 | Emergentes indexado | Fidelity MSCI Emerging Markets Index Fund P-ACC-EUR | `IE00BYX5M476` | 12.000 | 12,00 % | 0,20 % | 24 | 99,03 % | web ficha: 0.00 EUR |
| 4 | Europa indexado | Fidelity MSCI Europe Index Fund EUR P Acc | `IE00BYX5MD61` | 10.000 | 10,00 % | 0,10 % | 10 | 99,30 % | web ficha: 1.00 EUR |
| 5 | Japón indexado cubierto EUR | Fidelity MSCI Japan Index Fund P-ACC-EUR (hedged) | `IE00BYX5NH74` | 5.000 | 5,00 % | 0,20 % | 10 | 100,00 % | web ficha: 0.00 EUR |
| 6 | Pacífico ex-Japón indexado | Vanguard Pacific ex-Japan Stock Index Fund EUR Acc | `IE0007201266` | 3.000 | 3,00 % | 0,16 % | 5 | 100,00 % | MCP 20/11: 1.00 EUR |
| 7 | Agregado global 1-5 años cubierto EUR | iShares Global Aggregate 1-5 Year bond Index Fund EUR Hedged | `IE0004ZP1ND3` | 12.000 | 12,00 % | 0,08 % | 10 | 0,00 % | MCP 20/11: 0.00 EUR |
| 8 | Gubernamental euro indexado | Amundi Core Euro Government Bond AE-C (Amundi IS JP Morgan EMU … | `LU1050470373` | 6.000 | 6,00 % | 0,35 % | 21 | 0,00 % | MCP 20/11: 0.00 participaciones |
| 9 | Ligado a inflación euro indexado | Vanguard Eurozone Inflation-Linked Bond Index Fund EUR Acc | `IE00B04GQR24` | 4.000 | 4,00 % | 0,12 % | 5 | 0,00 % | MCP 20/11: 1.00 EUR |
| | **Total** | **9 fondos** | | **100.000** | **100 %** | **0,1322 %** | **132,20** | **77,52 %** | |

## 3. Bloques por rol

| Bloque | € | % del total | TER medio | €/año |
| --- | --: | --: | --: | --: |
| Índice | 100.000 | 100,00 % | 0,13 % | 132 |

## 4. Métricas

| Métrica | Valor | Cómo se calcula |
| --- | --- | --- |
| RV *look-through* | 77,52 % | Σ importe × RV declarada en la ficha |
| Renta fija | 21,87 % | Σ importe × RF declarada en la ficha |
| Caída de manual | −31,67 % = 31.666 € | −(40 % × RV + 3 % × RF) |
| Coste anual | 132,20 € = 0,1322 % | Σ importe × TER snapshot |
| Duración estimada de la RF | 2,80 años sobre 12.000 €; 7,00 años sobre 6.000 €; 7,00 años sobre 4.000 € | +100 pb cuesta 1.032 € |
| Esperanza central | 5,99 % | Σ importe × retorno esperado por sleeve |
| Escenario pesimista | 4,05 % | RV −2,5 pp de retorno esperado |
| Escenario favorable | 7,15 % | RV +1,5 pp de retorno esperado |
| Indexado | 100,00 % | gestión indexada declarada o índice nombrado en la ficha |

**Supuestos de la esperanza** (estimación del agente, no dato de mercado): RV desarrollada 6,7 %, small caps 7,0 %, emergentes y Asia 7,5 %, Japón 6,7 %, crédito y agregado 2,8-3,2 %, liquidez 2,3 %. La esperanza la decide el % de RV, no la selección de fondos; la prima de convicción está incluida solo donde la ficha declara un sesgo value o de calidad.

## 5. Geografía por *look-through*

| Región declarada | € de RV | % de la RV con desglose |
| --- | --: | --: |
| Estados Unidos | 28.596 | 38,37 % |
| Zona Euro | 3.257 | 4,37 % |
| Taiwán | 2.911 | 3,91 % |
| China | 2.709 | 3,64 % |
| Japón | 2.304 | 3,09 % |
| Corea del Sur | 2.198 | 2,95 % |
| Europa ex-Zona Euro | 1.549 | 2,08 % |
| India | 1.402 | 1,88 % |
| Canadá | 1.350 | 1,81 % |

Base con desglose: 74.525 € de RV (96,13 % de la RV total). Los fondos sin desglose regional no entran en la tabla; es un cálculo derivado de las fichas, no un dato de la gestora.

## 6. Razón fondo a fondo

- **`IE000ZYRH0Q7` iShares Developed World Index (IE) Acc EUR clase S** — clase S 2025, sin 3A propio; índice MSCI World. Historial no publicado en la ficha; TER 0,06 %; MCP 20/11: 0.00 EUR.
- **`IE00B42W4L06` Vanguard Global Small-Cap Index Fund EUR Acc** — MCP TER 0.29 vs snapshot 0.30; manda snapshot. 3A 16,01 % · 5A 6,07 %; TER 0,30 %; MCP 20/11: 1.00 EUR.
- **`IE00BYX5M476` Fidelity MSCI Emerging Markets Index Fund P-ACC-EUR** — Fidelity P-ACC-EUR. 3A 16,95 % · 5A 6,12 %; TER 0,20 %; web ficha: 0.00 EUR.
- **`IE00BYX5MD61` Fidelity MSCI Europe Index Fund EUR P Acc** — Fidelity P Acc EUR. 3A 15,22 % · 5A 8,96 % · vol 10,04 %; TER 0,10 %; web ficha: 1.00 EUR.
- **`IE00BYX5NH74` Fidelity MSCI Japan Index Fund P-ACC-EUR (hedged)** — factsheet 0.15 vs snapshot 0.20; manda snapshot. 3A 20,14 % · 5A 16,30 %; TER 0,20 %; web ficha: 0.00 EUR.
- **`IE0007201266` Vanguard Pacific ex-Japan Stock Index Fund EUR Acc** — Australia 62%. 3A 13,85 % · 5A 6,68 %; TER 0,16 %; MCP 20/11: 1.00 EUR.
- **`IE0004ZP1ND3` iShares Global Aggregate 1-5 Year bond Index Fund EUR Hedged** — clase S del mismo fondo que D Acc (0.17); se elige la barata operable. Historial no publicado en la ficha; TER 0,08 %; MCP 20/11: 0.00 EUR.
- **`LU1050470373` Amundi Core Euro Government Bond AE-C (Amundi IS JP Morgan EMU Govies …** — duración ~7 estimada (2022 −18.25%); Amundi Prime IE-C descartado por mínimo 500.000. 3A 1,25 % · 5A -3,00 %; TER 0,35 %; MCP 20/11: 0.00 participaciones.
- **`IE00B04GQR24` Vanguard Eurozone Inflation-Linked Bond Index Fund EUR Acc** — Italia 38 Francia 34; duración larga estimada. 3A 1,63 % · 5A -0,90 %; TER 0,12 %; MCP 20/11: 1.00 EUR.

La ficha completa de cada uno, con todas las pegas y fuentes, está en [`fondos-revisados.md`](fondos-revisados.md).

## 7. Ejecución

Dinero nuevo: una orden de suscripción por fondo, sin reembolso previo. La tabla está en el orden en que conviene lanzarla: primero las líneas con mínimo inicial más alto. El corte se lee en la ficha de cada fondo; verificar en pantalla el día de la orden.

| # | Fondo | ISIN | € | Mínimo inicial | Orden |
| --: | --- | --- | --: | --- | --- |
| 1 | Vanguard Global Small-Cap Index Fund EUR Acc | `IE00B42W4L06` | 8.000 | MCP 20/11: 1.00 EUR | Suscribir 8.000 € |
| 2 | Fidelity MSCI Europe Index Fund EUR P Acc | `IE00BYX5MD61` | 10.000 | web ficha: 1.00 EUR | Suscribir 10.000 € |
| 3 | Vanguard Pacific ex-Japan Stock Index Fund EUR Acc | `IE0007201266` | 3.000 | MCP 20/11: 1.00 EUR | Suscribir 3.000 € |
| 4 | Vanguard Eurozone Inflation-Linked Bond Index Fund EUR Acc | `IE00B04GQR24` | 4.000 | MCP 20/11: 1.00 EUR | Suscribir 4.000 € |
| 5 | iShares Developed World Index (IE) Acc EUR clase S | `IE000ZYRH0Q7` | 40.000 | MCP 20/11: 0.00 EUR | Suscribir 40.000 € |
| 6 | Fidelity MSCI Emerging Markets Index Fund P-ACC-EUR | `IE00BYX5M476` | 12.000 | web ficha: 0.00 EUR | Suscribir 12.000 € |
| 7 | Fidelity MSCI Japan Index Fund P-ACC-EUR (hedged) | `IE00BYX5NH74` | 5.000 | web ficha: 0.00 EUR | Suscribir 5.000 € |
| 8 | iShares Global Aggregate 1-5 Year bond Index Fund EUR Hedged | `IE0004ZP1ND3` | 12.000 | MCP 20/11: 0.00 EUR | Suscribir 12.000 € |
| 9 | Amundi Core Euro Government Bond AE-C (Amundi IS JP Morgan E … | `LU1050470373` | 6.000 | MCP 20/11: 0.00 participaciones | Suscribir 6.000 € |

## 8. Qué se descarta

| Candidato | Razón con número | Solución adoptada |
| --- | --- | --- |
| Amundi Prime Euro Gov IE-C | mínimo inicial 500.000 €; no operable con 6.000 € | se tomó Amundi Core Euro Gov AE-C a 0,35 % |
| iShares Global Aggregate D Acc | misma exposición, 0,17 % frente al 0,08 % de la clase S | 13,20 €/año de diferencia en 12.000 € |

## 9. Verificación, revisión y lo que queda abierto

**Web 20/11 — `IE000ZYRH0Q7` (mínimo institucional de la clase S).** Las fichas web publican 200.000.000 (USD en quefondos, EUR en Finect) para la clase S, mientras el dato MCP del 20/11/2026 da 0,00 EUR. Se conserva la clase S por ser la operable en la plataforma y se escribe el mínimo publicado como condición a comprobar en pantalla antes de la primera orden. (fichas del repo + MCP 20/11).

**Revisión.** Revisar el 30/11/2027 y cada 12 meses: (a) TER real en pantalla frente al snapshot; (b) comisiones de éxito efectivas; (c) clases hermanas que abaraten una línea sin cambiar de fondo —recuerda que cambiar de clase de un fondo ya comprado es un reembolso—; (d) que ningún fondo pase a distribuir o a tener soft close; (e) en C2/C5, evidencia de cada gestor contra su índice neto de TER.

**Sin decidir:** horizonte real, colchón fuera de la cartera, aportaciones periódicas y fecha de ejecución. Ninguna orden se lanza hasta la revisión del titular.

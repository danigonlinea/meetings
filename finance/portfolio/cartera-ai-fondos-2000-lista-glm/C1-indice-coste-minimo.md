---
title: "C1 — Índice de coste mínimo (100.000 €)"
date: 2026-11-20
type: portfolio-proposal
category: finance
tags: [indexado, coste-minimo, msci-world, emergentes, small-cap, renta-fija-indexada]
status: propuesta
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/validacion.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/fondos-revisados.md
---

# C1 — Índice de coste mínimo

> **Qué es.** 8 fondos, 100.000 € exactos, **66,54 % de renta variable real** (look-through) y **109,80 €/año (0,1098 %)**. Caída de manual **-27,60 % = 27.599 €** y **≈5,46 % esperado** con los supuestos de §4.
>
> **Criterio.** solo fondos de gestión indexada, la clase más barata operable de cada índice, con RV/RF 65/35.
>
> **Método y límite.** Fichas del repo (snapshot de la app del 19/11/2026) y verificación de los 8 ISIN en el catálogo MCP de MyInvestor el 20/11/2026 (TER, `distributing`, mínimos, avisos). **No es asesoramiento financiero**: la decisión y la ejecución son del titular.

---

## 1. Mandato

| Lo que pide el encargo | Cómo se cumple | Qué cuesta |
| --- | --- | --- |
| 100.000 € | 8 líneas que suman exactamente 100.000 € | Nada |
| Cinco carteras sin repetir fondo entre ellas | 50 ISIN distintos en el encargo, comprobados por ISIN, nombre normalizado y clase hermana (§ de [`validacion.md`](validacion.md)) | Ninguna línea se abarata con un fondo ya usado en otra de las cinco |
| Cartera diversificada | solo fondos de gestión indexada, la clase más barata operable de cada índice, con RV/RF 65/35 | Ver §4 |
| Solo fondos del listado `finance/fondos-myinvestor/` | Los 8 ISIN están en el listado (1.980 fichas) | Sin ETF ni acciones: traspaso sin peaje fiscal |
| Sin distribución de dividendos | 8/8 clases de acumulación (`distributing=0` en el MCP) | Nada |

**Supuestos escritos, no reglas heredadas:** horizonte de 15 años o más (en C4, de 7 años o más), colchón de 6-12 meses fuera de la cartera, sin aportaciones modeladas. **No se heredó ninguna lista negra de carteras anteriores**: la no-repetición vale solo entre estas cinco, y no se aplicó ningún veto más allá del encargo.

## 2. Cartera

| # | Rol | Fondo | ISIN | € | % | TER | €/año | Éxito | RV/RF | Mínimo (MCP) | Corte |
| --: | --- | --- | --- | --: | --: | --: | --: | --: | --- | --- | --- | |
| 1 | Núcleo y satélites indexados de RV | iShares Developed World Index Fund (IE) S Acc EUR | `IE000ZYRH0Q7` | 40.000 | 40 % | 0,06 % | 24,00 | — | RV 99,29 % | 0,00 € | 09:00 |
| 2 | Núcleo y satélites indexados de RV | Fidelity MSCI Emerging Markets Index Fund EUR P Acc | `IE00BYX5M476` | 10.000 | 10 % | 0,20 % | 20,00 | — | RV 99,10 % | 1,00 € | 16:00 |
| 3 | Núcleo y satélites indexados de RV | Vanguard Global Small-Cap Index Fund EUR Acc | `IE00B42W4L06` | 8.000 | 8 % | 0,29 % | 23,20 | — | RV 99,94 % | 1,00 € | 16:00 |
| 4 | Núcleo y satélites indexados de RV | Fidelity MSCI Europe Index Fund EUR P Acc | `IE00BYX5MD61` | 6.000 | 6 % | 0,10 % | 6,00 | — | RV 99,35 % | 1,00 € | 12:00 |
| 5 | Núcleo y satélites indexados de RV | Fidelity MSCI Japan Index Fund EUR P Acc | `IE00BYX5N771` | 3.000 | 3 % | 0,10 % | 3,00 | — | RV 98,50 % | 1,00 € | 16:00 |
| 6 | Renta fija indexada | iShares Global Aggregate 1-5 Year Bond Index (IE) S Acc EUR H | `IE0004ZP1ND3` | 15.000 | 15 % | 0,08 % | 12,00 | — | RF 98,90 % | 0,00 € | 09:00 |
| 7 | Renta fija indexada | iShares Euro Investment Grade Corporate Bond Index Fund (IE) D Acc EUR | `IE00BDRK7J14` | 10.000 | 10 % | 0,12 % | 12,00 | — | RF 99,81 % | 0,00 € | 09:00 |
| 8 | Renta fija indexada | Vanguard Eurozone Inflation-Linked Bond Index Fund EUR Acc | `IE00B04GQR24` | 8.000 | 8 % | 0,12 % | 9,60 | — | RF 100,00 % | 1,00 € | 10:00 |
| | **Total** | **8 fondos** | | **100.000** | **100 %** | **0,1098 %** | **109,80** | | | | |

## 3. Bloques por rol

| Bloque | € | % del total | TER medio | €/año |
| --- | --: | --: | --: | --: |
| Núcleo y satélites indexados de RV | 67.000 | 67,00 % | 0,1137 % | 76,20 |
| Renta fija indexada | 33.000 | 33,00 % | 0,1018 % | 33,60 |

## 4. Métricas

| Métrica | Valor | Cómo se calcula |
| --- | --- | --- |
| RV *look-through* | 66,54 % | Σ importe × RV declarada (MCP 20/11) |
| Renta fija | 32,82 % | Σ importe × RF declarada (MCP 20/11) |
| Liquidez | 0,61 % | Σ importe × liquidez declarada |
| Caída de manual | -27,60 % = 27.599 € | −(40 % × RV + 3 % × RF) |
| Coste anual | 109,80 € = 0,1098 % | Σ importe × TER del MCP |
| Esperanza central | 5,46 % | Σ importe × retorno esperado por sleeve |
| Escenario pesimista | 3,46 % | RV −2,5 pp de retorno esperado |
| Escenario favorable | 6,76 % | RV +1,5 pp de retorno esperado |
| Indexado | 100 % aproximado del importe en réplica de índice | gestión indexada declarada o índice nombrado en la ficha/MCP |

**Supuestos de la esperanza** (estimación del agente, no dato de mercado): RV desarrollada 6,7 %, emergentes/Asia 7,5 %, crédito y agregado 3,0 %, liquidez 2,3 %. La esperanza la decide el % de RV, no la selección de fondos.

**Las comisiones de éxito no están en el coste anual.** Ninguna línea de esta cartera lleva comisión de éxito.

## 5. Geografía por *look-through*

| Región | € de RV | % de la RV con desglose |
| --- | --: | --: |
| Estados Unidos | 33.345 | 50,12 % |
| Japón | 6.254 | 9,40 % |
| Reino Unido | 2.926 | 4,40 % |
| Taiwán | 2.715 | 4,08 % |
| China | 1.893 | 2,84 % |
| Suiza | 1.889 | 2,84 % |
| Corea del Sur | 1.764 | 2,65 % |
| Canadá | 1.646 | 2,47 % |
| Alemania | 1.611 | 2,42 % |
| India | 1.259 | 1,89 % |
| Francia | 787 | 1,18 % |
| Países Bajos | 525 | 0,79 % |

Base con desglose: 66.537 € de RV. Las líneas sin desglose regional no entran en la tabla; cálculo derivado del top de países del MCP, no un dato de la gestora.

## 6. Razón fondo a fondo

- **`IE000ZYRH0Q7` iShares Developed World Index Fund (IE) S Acc EUR** — MSCI World completo al 0,06 %: el vehículo más barato del catálogo para el núcleo. La clase S es de 08/2025, sin historial propio; el fondo matriz va desde 2017 (+14,3 % YTD).
- **`IE00BYX5M476` Fidelity MSCI Emerging Markets Index Fund EUR P Acc** — MSCI EM al 0,20 % y mínimo de 1 €. El propio catálogo avisa de que la clase S de iShares (0,16 %) es más barata para el mismo índice, pero no está en el listado de fichas de este repo.
- **`IE00B42W4L06` Vanguard Global Small-Cap Index Fund EUR Acc** — MSCI World Small Cap al 0,29 %: el tilt de tamaño al precio de índice. Mínimo de folleto de 1 M€ (clase institucional); en MyInvestor se opera desde 1 € (MCP 20/11).
- **`IE00BYX5MD61` Fidelity MSCI Europe Index Fund EUR P Acc** — MSCI Europe al 0,10 % para descentrar el 72 % de EE. UU. del World. Finanzas 24 %, salud 14 %.
- **`IE00BYX5N771` Fidelity MSCI Japan Index Fund EUR P Acc** — MSCI Japan al 0,10 %, sin cubrir divisa (el riesgo EUR/JPY es parte del producto). Industria 22 %, finanzas 19 %, tecnología 19 %.
- **`IE0004ZP1ND3` iShares Global Aggregate 1-5 Year Bond Index (IE) S Acc EUR H** — Agregado global 1-5 años cubierto a euros al 0,08 %: duración corta. El año de la prueba es 2022 (el matriz aguantó mejor que el agregado largo).
- **`IE00BDRK7J14` iShares Euro Investment Grade Corporate Bond Index Fund (IE) D Acc EUR** — Crédito euro IG indexado al 0,12 %. Duración media ~4,4 años: no es liquidez, y el −13,3 % de 2024 anual lo recuerda.
- **`IE00B04GQR24` Vanguard Eurozone Inflation-Linked Bond Index Fund EUR Acc** — Ligada a inflación euro al 0,12 %, 100 % soberano (Italia 38 %, Francia 34 %, España 18 %). 2022: −10,33 %, el precio de la duración.

La ficha completa de cada uno, con pegas y fuentes, está en [`fondos-revisados.md`](fondos-revisados.md).

## 7. Ejecución

Dinero nuevo: una orden de suscripción por fondo, sin reembolso previo, ordenada de mayor lag de suscripción a menor para que ninguna línea quede colgada. Todos los mínimos iniciales están cubiertos por el importe de la línea (el mayor del encargo es 1.000 €, en líneas de ≥2.000 €).

| # | Fondo | ISIN | € | Mínimo | Corte | Suscripción |
| --: | --- | --- | --: | --- | --- | --- |
| 1 | iShares Developed World Index Fund (IE) S Acc EUR | `IE000ZYRH0Q7` | 40.000 | 0,00 € | 09:00 | Suscribir 40.000 € |
| 2 | iShares Global Aggregate 1-5 Year Bond Index (IE) S Acc EUR H | `IE0004ZP1ND3` | 15.000 | 0,00 € | 09:00 | Suscribir 15.000 € |
| 3 | Fidelity MSCI Emerging Markets Index Fund EUR P Acc | `IE00BYX5M476` | 10.000 | 1,00 € | 16:00 | Suscribir 10.000 € |
| 4 | iShares Euro Investment Grade Corporate Bond Index Fund (IE) D Acc EUR | `IE00BDRK7J14` | 10.000 | 0,00 € | 09:00 | Suscribir 10.000 € |
| 5 | Vanguard Global Small-Cap Index Fund EUR Acc | `IE00B42W4L06` | 8.000 | 1,00 € | 16:00 | Suscribir 8.000 € |
| 6 | Fidelity MSCI Japan Index Fund EUR P Acc | `IE00BYX5N771` | 3.000 | 1,00 € | 16:00 | Suscribir 3.000 € |
| 7 | Vanguard Eurozone Inflation-Linked Bond Index Fund EUR Acc | `IE00B04GQR24` | 8.000 | 1,00 € | 10:00 | Suscribir 8.000 € |
| 8 | Fidelity MSCI Europe Index Fund EUR P Acc | `IE00BYX5MD61` | 6.000 | 1,00 € | 12:00 | Suscribir 6.000 € |

## 8. Qué se descarta

| Candidato | Razón con número | Solución adoptada |
| --- | --- | --- |
| Amundi/Fidelity World sin cubrir y clases D/Instl de iShares World | TER 0,12-0,20 % con mínimos de folleto de 100.000-1.000.000 € y sin ventaja sobre la clase S (0,06 %) | se usa la clase S, operable desde 0 € (MCP 20/11) |
| iShares Emerging Markets clase S (IE000QAZP7L2) | el propio catálogo la señala como la más barata del índice (0,16 %), pero no está en el listado de fichas de este repo | se paga +0,04 pp con Fidelity EM (≈10 €/año sobre 10.000 €) |

## 9. Verificación, revisión y lo que queda abierto

**Verificación.** Los 8 ISIN se comprobaron en el catálogo MCP de MyInvestor el 20/11/2026 (`distributing=0`, mínimos, TER, avisos de soft close); no hizo falta verificación web adicional: los campos decisivos estaban en la ficha del repo o en el MCP. El recuento del encargo está en [`validacion.md`](validacion.md).

**Revisión.** Revisar el 30/11/2027 y cada 12 meses: (a) TER real en pantalla frente al MCP; (b) comisiones de éxito efectivas de las líneas que las llevan; (c) clases hermanas que abaraten una línea sin cambiar de fondo —cambiar de clase de un fondo ya comprado es un reembolso—; (d) que ningún fondo pase a distribuir o a soft close; (e) evidencia de cada gestor activo contra su índice neto de TER a tres años.

**Sin decidir:** horizonte real, colchón fuera de la cartera, aportaciones periódicas y fecha de ejecución. Ninguna orden se lanza hasta la revisión del titular.

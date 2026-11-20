---
title: "Validación de cartera-ai-fondos-2000-lista-glm"
date: 2026-11-20
type: validation
category: finance
tags: [validacion, cartera, fondos, myinvestor, mcp]
status: living
---

# Validación

Comprobación por código del encargo del 20/11/2026: **cinco carteras de 100.000 € sobre el listado
`finance/fondos-myinvestor/` sin repetir ningún fondo entre ellas**. Los números de esta página salen
de parsear el markdown de las cinco carteras y el universo de 1.980 fichas, no de memoria.

## Funnel del encargo

| Paso | Fondo… |
| --- | --: |
| Universo: fichas del listado (`fondos.json`, snapshot 19/11/2026) | 1.980 |
| Clases de acumulación (`politica: acumulacion`) | 1.578 |
| Cribas por criterio de cada cartera (indexado más barato operable / evidencia activa / perfil) | — |
| ISIN elegidos en las cinco carteras | **50** |
| Descartes escritos con número en las cinco carteras (§8) | 13 |

## La condición del titular: ningún fondo repetido entre las cinco

| Comprobación | Resultado |
| --- | --- |
| Líneas escritas en las cinco carteras (parseado del markdown) | 50 |
| ISIN distintos | **50 de 50** — 50 líneas / 50 ISIN / 50 fondos |
| Repetidos por ISIN | ninguno |
| Repetidos por nombre normalizado | ninguno |
| Clases hermanas del mismo fondo (nombre base) | ninguna |
| Lista negra heredada de otras carteras del repositorio | **no aplicada**: el mandato solo prohíbe repetir entre las cinco |

**Una anotación honesta:** el ISIN `IE00B88WFS66` (Federated Hermes Asia ex-Japan clase R) también está
en la cartera hermana `cartera-ai-fondos-2000-lista` (su C2). El mandato de este encargo no lo prohíbe:
la no-repetición vale solo entre las cinco carteras nuevas, y se documenta para que nadie busque un
«cero solape con el repo» que nunca se prometió. Con la cartera hermana el solape es 1 de 50; el resto
de carteras del repositorio comparten con C1 el núcleo barato del catálogo (`IE000ZYRH0Q7`,
`IE0004ZP1ND3`, `IE00B42W4L06`, presentes también en `cartera-definitiva-40` y `cartera-ai-100-index`).

## Cuadre por cartera (parseado del markdown, no de la memoria)

| Cartera | Líneas | € | ISIN = diseño | 
| --- | --: | --: | --- |
| C1 Índice de coste mínimo | 8 | 100,000 | sí |
| C2 Convicción activa | 9 | 100,000 | sí |
| C3 Equilibrada 55/45 | 11 | 100,000 | sí |
| C4 Defensiva con alternativos | 14 | 100,000 | sí |
| C5 Crecimiento con satélites | 8 | 100,000 | sí |

## Verificación de plataforma (MCP de MyInvestor, 20/11/2026)

| Comprobación | Resultado |
| --- | --- |
| Llamadas al MCP | 7 × `get_funds` (60 ISIN consultados: los 50 elegidos y los 10 sustitutos/descartes) |
| `distributing=0` (acumulación) | 50 de 50 |
| Soft close | 0 en los elegidos; 1 descubierto y corregido: `IE0007472115` (Vanguard Euro Gov Investor) → se usa la clase nueva `IE0007472990` |
| «Fondo Cerrado» | 1 descubierto y corregido: `ES0112101003` (Avantage Pure Equity) → fuera |
| Mínimo inicial incompatible | 2 descubiertos y corregidos: `LU2339731064` (500.000 €) → fuera; `IE00B8H6X308` clase F (100.000 €) → clase R |
| Divergencias TER ficha vs MCP | 9 anotadas fondo a fondo en [`fondos-revisados.md`](fondos-revisados.md); manda el MCP (20/11) |
| Verificaciones web adicionales | 0: los campos decisivos estaban en la ficha del repo o en el MCP |

## Exposiciones y coste (MCP 20/11/2026)

| Cartera | RV look-through | TER medio | Coste anual | Caída de manual |
| --- | --: | --: | --: | --: |
| C1 | 66.54 % | — | 109.8 € | -27.6 % |
| C2 | 79.81 % | — | 1180.1 € | -32.43 % |
| C3 | 54.38 % | — | 425.0 € | -22.97 % |
| C4 | 34.91 % | — | 727.7 € | -15.34 % |
| C5 | 87.64 % | — | 942.3 € | -35.35 % |

Las comisiones de éxito no están en el coste anual; van en la tabla de cada cartera y se cuantifican
en su §4. El monocargo GSQuartix (commodities, 2.000 € en C4) tiene volatilidad propia que la fórmula
−(40 % RV + 3 % RF) no captura; está anotado en su ficha de [`fondos-revisados.md`](fondos-revisados.md).

*Material de referencia, no consejo de inversión. La decisión y la ejecución son del titular.*

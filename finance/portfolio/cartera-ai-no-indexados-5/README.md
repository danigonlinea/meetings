---
title: "Cartera-ai no indexados 5: mapa de las dos tallas"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai-no-indexados-5, mapa, sin-indexados, sin-dividendos, sin-repetir-fondos, myinvestor]
status: final
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-no-indexados-5/100k.md
  - finance/portfolio/cartera-ai-no-indexados-5/200k.md
---

# Cartera-ai no indexados 5 — mapa

**Qué es.** Dos tallas de una cartera de fondos del catálogo de MyInvestor construida desde cero con
**dos condiciones únicas del titular**:

1. Ningún fondo que reparta dividendos: solo clases de acumulación (`fondoDistribucion = false` en el
   ISIN concreto).
2. Ningún fondo indexado y ningún fondo ya elegido en otra cartera de `finance/portfolio/`. Nada de
   ETF ni de acciones.

**Qué no es.** No hereda ninguna regla del repositorio: ni el 55 % de RV de otras carteras, ni el
criterio de coste mínimo, ni el criterio de Andrés, ni los descartes de las propuestas anteriores. Lo
que hay aquí son decisiones mías con su razón escrita.

**No es asesoramiento financiero.** La decisión es del titular.

## Los dos documentos

| Talla | Fichero | Fondos | RV de bloque | RV real (*look-through*) | TER | Caída de manual |
| --- | --- | --: | --: | --: | --: | --: |
| 100.000 € | `100k.md` | 10 (7 RV + 3 RF) | 70 % | 68,97 % | 1,3543 % | −28,45 % ≈ −28.454 € |
| 200.000 € | `200k.md` | 11 (8 RV + 3 RF) | 70 % | 68,72 % | 1,3417 % | −28,36 % ≈ −56.715 € |

Cada fichero es la cartera entera: ISIN, pesos, razón fondo a fondo, coste, órdenes, aportaciones de
2.000 €/mes, descartes y señales de revisión. Aquí no hay foto que fotografiar: la cartera nace sin
posiciones.

## Qué cambia entre las dos tallas

Una sola línea nueva en la de 200k —**Valentum, small/mid europeo, al 6 %**— y un punto menos en
Europa, EE. UU., Japón, emergentes, China y salud para financiarla. La razón está en el ticket: a
200.000 € un 6 % son 12.000 € y paga el seguimiento; a 100.000 € serían 6.000 € para una cuarta
exposición dentro del mismo bloque de renta variable.

## El diseño en una línea

Núcleo global value (T. Rowe Price), Europa value (Brandes), EE. UU. large value (Robeco BP), Japón
sistemático (DWS CROCI), emergentes (Ashoka WhiteOak), Gran China (Schroder) y un satélite de salud
(Polar Capital) sobre tres tramos de renta fija que no se solapan: crédito euro IG (Rothschild),
crédito euro ultracorto (DWS) y deuda emergente en divisa local (Candriam).

**El sesgo value es deliberado y está escrito, no escondido**: con las dos condiciones aplicadas, el
catálogo libre de gestión activa barata es sobre todo valor, porque las casas de crecimiento ya están
gastadas por las propuestas hermanas. Emergentes, China y salud son la contraparte de crecimiento.

## La lista negra

Se extrajeron **125 ISIN distintos** de las diez carpetas de cartera del repositorio con
`grep -rhoE '[A-Z]{2}[0-9A-Z]{9}[0-9]' finance/portfolio/ | sort -u | wc -l`. Ninguno de los once ISIN
de esta carpeta está en esa lista, y se revisó también por nombre y gestora: la tabla está en
`100k.md` §9.

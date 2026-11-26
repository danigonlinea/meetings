---
title: "Cartera-ai no indexados 4: mapa de las dos tallas"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai-no-indexados-4, mapa, sin-indexados, sin-dividendos, sin-repetir-fondos, myinvestor]
status: final
related: [finance/portfolio/README.md, finance/laboratorio-carteras/cartera-ai-no-indexados-4/100k.md, finance/laboratorio-carteras/cartera-ai-no-indexados-4/200k.md]
---

# Cartera-ai no indexados 4 — mapa

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
| 100.000 € | `100k.md` | 10 (7 RV + 3 RF) | 70 % | 67,49 % | 1,5961 % | −27,86 % ≈ −27.860 € |
| 200.000 € | `200k.md` | 11 (8 RV + 3 RF) | 70 % | 67,72 % | 1,5851 % | −27,95 % ≈ −55.900 € |

Cada fichero es la cartera entera: ISIN, pesos, razón fondo a fondo, coste, órdenes, aportaciones de
2.000 €/mes, descartes y señales de revisión. Aquí no hay foto que fotografiar: la cartera nace sin
posiciones.

## Qué cambia entre las dos tallas

Una sola línea nueva en la de 200k —**Columbia Threadneedle American Smaller Companies al 7 %**— y un
punto menos en el núcleo, Europa, EE. UU. value, Japón, China, India y salud para financiarla. La razón
está en el ticket: a 200.000 € un 7 % son 14.000 € y paga el seguimiento; a 100.000 € serían 7.000 €
para una cuarta exposición dentro del mismo bloque de renta variable.

## La lista negra

Se extrajeron **114 ISIN distintos** de las nueve carpetas de cartera del repositorio con
`grep -rhoE '[A-Z]{2}[0-9A-Z]{9}[0-9]' finance/portfolio/ | sort -u | wc -l`. Ninguno de los once ISIN
de esta carpeta está en esa lista, y se revisó también por nombre de gestora (§9 de cada fichero).

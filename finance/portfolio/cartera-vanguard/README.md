---
title: "Cartera solo Vanguard: mapa de la cartera"
date: 2026-11-19
type: portfolio-proposal
category: finance
tags: [cartera, cartera-vanguard, mapa, vanguard, indexado, gestora-unica, diversificacion, myinvestor, fondos, renta-fija]
status: propuesta
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-vanguard/100k.md
  - finance/portfolio/cartera-cobas/100k.md
  - finance/portfolio/cartera-horos/100k.md
---

# Cartera solo Vanguard — mapa

**Qué es.** Una cartera **desde cero** de **100.000 € con nueve fondos indexados de una sola gestora, Vanguard**:
**40 % MSCI World**, **10 % Europa**, **10 % emergentes**, **10 % small caps globales**, **5 % Japón** y **25 % de
renta fija en cuatro tramos**. **178,50 €/año de coste total (0,1785 %)**, **74,95 % de RV real**, caída de manual
**−30,73 %** y **≈5,9 % de rentabilidad esperada anual** con supuestos escritos.

**Qué la distingue de sus hermanas:**

- De `cartera-cobas/` y `cartera-horos/`: aquellas dos también son una sola gestora, pero con **tres fondos y un
  sesgo** (value ibérico, value small/mid). Aquí la misma restricción se cumple con la casa que tiene **91 fondos
  en catálogo**, y el resultado es una cartera diversificada de verdad: cuatro zonas de bolsa, small caps,
  emergentes y cuatro tipos de renta fija.
- De las `cartera-ai-*/`: aquí **no hay convicción activa**, no hay comisiones de éxito y no hay apuesta de estilo.
  Vanguard solo vende beta; lo único que se decide son los pesos.
- De `cartera-ai-100-index-5/`: esa es la más barata con tres cláusulas (solo indexados, nada que reparta, ningún
  fondo repetido) y cuatro líneas; esta no hereda la lista negra, usa los fondos buenos que ya existen y cambia
  precio por diversificación: **178,50 € frente a 193 €/año** y nueve líneas frente a cuatro.

**Qué condiciones solo vinculan.** Una sola gestora, diversificar y 100.000 €. **Ninguna regla heredada**: no hay
55/45, ni techo de indexado, ni mínimo por línea, ni veto a las comisiones de éxito (no hay ninguna que vetar).

**Lo que este mandato no puede dar.** Diversificación de gestora. Los nueve fondos son de Vanguard: un equipo, una
política de préstamo de valores y un riesgo operativo. Y el 46,9 % de la RV sigue siendo Estados Unidos, la mitad
del 72,7 % que pesa en el MSCI World.

**No es asesoramiento financiero.** La decisión es del titular.

## El documento

| Talla | Fichero | Fondos | RV real (*look-through*) | Coste total | Caída de manual | Rentabilidad esperada |
| --- | --- | --: | --: | --: | --: | --: |
| 100.000 € | `100k.md` | 9 | **74,95 %** | **178,50 €/año (0,1785 %)** | **−30,73 % (−30.733 €)** | **≈5,89 %** (4,02-7,76 %) |

El fichero es la cartera entera: ISIN, pesos, los tres bloques con su coste, la geografía por *look-through*, los
tilts con su precio, la **rentabilidad esperada con sus supuestos**, las **9 órdenes en tres cortes**, dos variantes
(60/40 y seis líneas), los vehículos descartados con su número y las pruebas de §8 con fecha.

## El diseño en una línea

**MSCI World al 40 %** como núcleo (0,18 %); **Europa al 10 %** (0,12 %, la línea más barata y la única en euros),
**emergentes al 10 %** (0,23 %), **small caps globales al 10 %** (0,29 %) y **Japón al 5 %** (0,16 %) para bajar el
peso americano del 72,7 % al 46,9 %; y **25 % de renta fija** en cuatro tramos: agregado global cubierto (11 %),
soberana euro (6 %), ligada a inflación (4 %) y corta global (4 %).

## Los tres avisos que el titular tiene que leer

1. **La diversificación se compra con un tilt.** 27 pp menos de EE. UU. que el índice. Si la bolsa americana sigue
   ganando por 2 pp/año, esa decisión cuesta **≈0,55 pp/año** de la cartera (§2.3).
2. **El 25 % en renta fija renta poco hoy** (3A de +1,61 % a +2,47 % en los cuatro tramos). Está por su papel en la
   caída, no por su rentabilidad: sin ella, la caída de manual pasa de −30,7 % a −40 %.
3. **Una sola gestora es un solo riesgo operativo.** Es lo que el mandato pide y no se puede arreglar dentro de él:
   si Vanguard cambia un índice o una clase, la cartera se adapta a lo que la casa ofrezca.

---
title: "Cartera-ai-andres: dos tallas con el criterio de Andrés"
date: 2026-11-15
type: reference
category: finance
tags: [cartera, indice, cartera-ai-andres, myinvestor, gestion-activa, cartera-ai-definitivas-estudiar]
status: living
related: [finance/portfolio/README.md, finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/README.md, finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-andres/100k.md, finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-andres/200k.md]
---
# Cartera-ai-andres

Cartera de **200.000 €** diseñada por el agente el 15/11/2026 con criterio propio y la experiencia de
Andrés (La Pizarra de Andrés) como material de estudio. **No es una copia de la cartera de Andrés** ni
una segunda versión de `cartera-ai/`: es una cartera distinta, con otro mandato y otro resultado.

## Documentos

| Archivo | Qué es |
| --- | --- |
| `100k.md` | La cartera de **100.000 €**: 11 fondos, 60,3 % de RV, 0,46 % de coste verificado |
| `200k.md` | La cartera de **200.000 €**: 14 fondos, 60,0 % de RV, 0,51 % de coste verificado |

**Un fichero por talla, una cartera por fichero.** No hay foto de saldos: cada cartera nace de cero y las
decisiones son del agente. A 100.000 € el diseño pierde tres líneas (Azvalor, small caps y Europa); a
200.000 € entran, porque el mínimo de 5.000 € de Azvalor pasa de 5 % a 3 %. Cuando se ejecute una y haya
posiciones con precio de compra, se abrirá `cartera-actual-YYYY-MM-DD.md` y solo entonces.

## Reglas

- **Solo fondos del catálogo de MyInvestor**, verificados por ISIN contra el MCP. Ninguna ISIN sin
  comprobar entra en la propuesta.
- **Solo clases de acumulación** (`distributing = 0`) y **sin ETF**: el traspaso entre fondos no tributa
  y es lo que permite rebalancear.
- **El % de RV se mide por look-through**, con el `alloc_equity` de cada ficha. Un mixto etiquetado como
  renta fija puede llevar un 43 % de bolsa dentro.
- **Lo que la ficha no publica va `no publicado`.** Nunca un TER, una comisión o un peso inventado; lo
  derivado se marca como derivado y lo estimado, como estimación.
- **No se consolida** con `finance/portfolio/cartera-myinvestor/`, `finance/portfolio/cartera-renta4/`, `cartera-ai/` ni con
  `cartera-de-andres/`.
- **No es consejo.** La propuesta es del agente; la decisión es del titular.

## Actualización

1. Cuando se ejecute una talla y haya posiciones reales, se abre `cartera-actual-YYYY-MM-DD.md` con los
   saldos y los precios de compra. Hasta entonces, el fichero de cada talla es la única descripción de esa
   cartera.
2. Si cambia un fondo (soft close, cambio de gestor, TER nuevo), se anota en la sección de descartes y
   señales del fichero de su talla, y se fecha.
3. `python3 tools/build_index.py && python3 tools/verify.py` después de cualquier cambio.

## Estado

- **15/11/2026:** dos tallas cerradas, sin ejecutar. **100.000 €**: 11 fondos, 60,3 % de RV, 463,30 €/año
  verificados (0,46 %). **200.000 €**: 14 fondos, 60,0 % de RV, 1.016,20 €/año verificados (0,51 %).
  Pendientes en las dos: coste de Myinvestor Value y Kaizen, horizonte real y si se quiere un bloque de
  acciones (ninguna lo lleva).

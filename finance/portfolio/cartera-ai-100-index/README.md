---
title: "Cartera-ai 100 index: dos tallas (100k y 200k) solo con fondos indexados de acumulación"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai-100-index, solo-indexados, sin-dividendos, acumulacion, myinvestor, 100k, 200k]
status: final
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-100-index/100k.md
  - finance/portfolio/cartera-ai-100-index/200k.md
---

# Cartera-ai 100 index — dos tallas, un mandato de dos frases

Cartera diseñada desde cero el 16/11/2026 con **solo dos condiciones del titular**:

1. **Únicamente fondos indexados** — cero gestión activa, cero ETF, cero acciones, cero monetarios. Los
   vehículos son `Índice/pasivo` por ISIN y su ficha dice qué índice replican.
2. **Ningún fondo que reparta dividendos** — solo clases de acumulación (`distributing = 0` verificado por
   ISIN, no por nombre).

**No se hereda ninguna regla del repositorio.** Ni el 55 % de RV de `cartera-myinvestor/`, ni el coste mínimo
de `cartera-ai/`, ni el 80 % de `cartera-ai-no-indexados/`, ni el techo del 40 % de
`cartera-ai-definitivas-estudiar/cartera-ai-40-max-index/`, ni las prohibiciones de acciones de otras propuestas. Tampoco sus conclusiones.
Lo que no sea una de las dos condiciones, es decisión del agente y va escrita con su razón: pesos, número de
fondos, reparto RV/RF, bloque de renta fija y regla de aportaciones.

## Ficheros

| Fichero | Qué es |
| --- | --- |
| `100k.md` | La cartera de **100.000 €**: 7 fondos indexados (4 de RV + 3 de RF), 79,9 % de RV real, 0,1065 % de TER |
| `200k.md` | La cartera de **200.000 €**: 8 indexados (entra MSCI Europe al 5 % y el núcleo baja al 50 %), 79,9 % de RV real, 0,1085 % |
| `README.md` | Este mapa |

**Un fichero por talla, una cartera por fichero.** El mandato es el mismo; lo que cambia es cuántas líneas
aguanta el tamaño. A 200.000 € entra Europa con 10.000 € (5 %) porque es el umbral que me pido para abrir una
línea cuya exposición ya está dentro del núcleo; a 100.000 € serían 5.000 € y no se abre.

## Cómo está pensada (decisiones del agente, no reglas)

- **80 / 20 de RV/RF** (79,9 / 19,9 % por *look-through*). Sin horizonte declarado, 80 % de RV es el máximo
  que se puede ver caer un tercio (−32,6 %) sin vender; y con 2.000 €/mes, el 20 % de RF es la munición para
  comprar RV en las caídas sin vender RV.
- **Cuatro exposiciones de RV que no se solapan**: mundo desarrollado (núcleo, 0,06 %), emergentes (0,16 %),
  small caps globales (0,29 %, el único pasivo del catálogo) e inmobiliario cotizado (0,17 %). No hay dos
  fondos globales compitiendo por el mismo hueco ni temáticos que apalanquen la tecnología que el índice ya
  lleva al 30,8 %.
- **Renta fija indexada en tres riesgos distintos**: agregado global 1-5 años cubierto a EUR (0,08 %),
  corporativo euro IG (0,12 %) y ligado a la inflación euro (0,12 %). Duración corta a propósito: el bloque
  conservador está para amortiguar, no para añadir volatilidad.
- **Todo por el coste más bajo disponible por ISIN**, no por gestora: se comparan clases hermanas y
  alternativas del mismo índice antes de fijar cada línea (§4 de cada talla, con los descartes nombrados).
- **Sin ETF, sin acciones, sin monetarios**: no son fondos indexados y el ETF no admite traspaso.

## Estado a 16/11/2026

- **Dos tallas cerradas, ninguna ejecutada:** 100k (7 fondos, 0,1065 %, 106,50 €/año) y 200k (8 fondos,
  0,1085 %, 217,00 €/año).
- **Datos de las fichas:** catálogo MyInvestor vía MCP (2.409 fondos, 266 indexados), NAV de 12/11/2026,
  `ter`, `distributing` y `management_type` verificados por ISIN con `get_funds`, no por nombre. Ninguno de
  los ocho vehículos está en *soft close*.
- **Coste verificado al 100 %**: los ocho fondos publican TER; no hay rango ni supuesto.
- **Descartes con nombre:** Vanguard Global Stock Index Investor (*soft close*, 0,18 %), iShares US Index
  S Acc (0,05 %, pero sube la concentración en EE. UU.), Amundi Prime Euro Government Bond y Amundi MSCI
  World SRI (mínimos de 500.000 €), Vanguard Global Bond (agregado completo, más duración), las clases
  *Dist*/*Dis* del mismo índice, y los 2.143 fondos activos del catálogo.
- **Decisión abierta (del titular):** horizonte, si es patrimonio completo, qué talla se ejecuta y si se
  quiere la apuesta de Europa. No se consolida con las otras carteras del repositorio.

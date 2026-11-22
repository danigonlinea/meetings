---
title: "Cartera-ai 40 max index: dos tallas (100k y 200k) con un techo del 40 % en indexados"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai-40-max-index, max-40-indexados, sin-dividendos, acumulacion, myinvestor, 100k, 200k]
status: final
related: [finance/portfolio/README.md, finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-40-max-index/100k.md, finance/portfolio/cartera-ai-definitivas-estudiar/cartera-ai-40-max-index/200k.md]
---

# Cartera-ai 40 max index — dos tallas, un mandato

Cartera diseñada desde cero el 16/11/2026 con **solo dos condiciones del titular**:

1. **Ningún fondo que reparta dividendos** — solo clases de acumulación (`distributing = 0` verificado por
   ISIN en las fichas del catálogo).
2. **Como máximo un 40 % en fondos indexados** — la cartera usa **exactamente 40,0 %** y deja el 60 %
   restante en gestión activa.

Todo lo demás lo decide el agente. **No se hereda ninguna regla de este repositorio**: ni el 55 % de RV de
`cartera-myinvestor/`, ni el coste mínimo de `cartera-ai/`, ni el 80 % de `cartera-ai-no-indexados/`, ni la
prohibición de acciones de otras propuestas. Tampoco se traen sus conclusiones: aquí no hay acciones
porque el mandato habla de fondos, y no hay ETF porque no admiten traspaso.

## Ficheros

| Fichero | Qué es |
| --- | --- |
| `100k.md` | La cartera de **100.000 €**: 2 indexados + 7 activos, 73,0 % de RV real, 0,79 % de TER |
| `200k.md` | La cartera de **200.000 €**: 2 indexados + 8 activos (entra Iberia), 73,6 % de RV real, 0,80 % |
| `README.md` | Este mapa |

**Un fichero por talla, una cartera por fichero.** El mandato es el mismo; lo que cambia es cuántas líneas
aguanta el tamaño. A 200.000 € entra Magallanes Iberian Equity (5 %) y se reparten mejor los pesos de los
motores activos; a 100.000 € esa línea sería un 4 % que no mueve el resultado.

## Cómo está pensada (decisiones del agente, no reglas)

- **El 40 % indexado es el techo y se gasta entero, todo en renta variable** (28 % MSCI World + 12 % MSCI
  Emerging Markets, 0,06 % y 0,16 %). El indexado solo aporta donde la gestión activa no tiene ventaja
  demostrable; en renta fija se queda en 0 porque la selección de crédito es donde el gestor aún cobra por
  algo. Si el bloque pasa del 40 % por revalorización, se corrige desviando aportaciones, no vendiendo.
- **75 % de renta variable como objetivo por bloques** (73,0–73,6 % real por *look-through*). Con 2.000 €/mes
  entrando y sin horizonte declarado, 75 % es el máximo que se puede ver caer −30 % sin vender.
- **Cuatro motores activos de RV, no uno**: calidad-crecimiento (Fundsmith), valor profundo (Cobas), Japón
  cubierto (Man CoreAlpha), Europa small caps (Alken) e Iberia solo en la talla grande (Magallanes). El
  objetivo es que el resultado no dependa de que acierte un estilo.
- **Renta fija activa de duración corta** (crédito global cubierto 13 %, deuda emergente cubierta 7 %) más
  un 4–5 % de convertibles como colchón asimétrico. Nada de agregados de índice.
- **Ningún fondo por encima del 13 %** (el índice desarrollado, 28 %, es la excepción por construcción).
- **Sin temáticos ni sectoriales**: el índice ya lleva 31 % de tecnología; un fondo de IA sería apalancar
  la misma apuesta.

## Estado a 16/11/2026

- **Dos tallas cerradas, ninguna ejecutada:** 100k (9 fondos, 0,79 %) y 200k (10 fondos, 0,80 %).
- **Datos de las fichas:** catálogo MyInvestor vía MCP, NAV de 12–13/11/2026, TER, `distributing` y
  `management_type` verificados por ISIN con `get_funds`, no por nombre.
- **Descartes con nombre:** Vanguard Global Stock Index Investor (en *soft close*), BBVA Bolsa Índice FI
  (indexado etiquetado como activo), Franklin Global Convertible (mínimo posterior de 1.000 €), Alken
  Global Convertible (76 % de RV en ficha), los dos fondos de small caps japonesas (coste y solapamiento).
- **Decisión abierta (del titular):** horizonte, si es patrimonio completo y qué talla se ejecuta. No se
  consolida con las otras carteras del repositorio.

---
title: "Cartera-ai no indexados 3: dos tallas con dos condiciones y cero fondos repetidos, desde cero"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai-no-indexados-3, gestion-activa, sin-indexados, sin-dividendos, sin-repetir-fondos, acumulacion, myinvestor, 100k, 200k]
status: final
related: [finance/portfolio/README.md, finance/portfolio/cartera-ai-no-indexados-3/100k.md, finance/portfolio/cartera-ai-no-indexados-3/200k.md]
---

# Cartera-ai no indexados 3 — dos tallas, dos condiciones, cero fondos repetidos

Cartera diseñada desde cero el 16/11/2026 con **dos condiciones del titular**:

1. **Ningún fondo que reparta dividendos** — solo clases de acumulación (`fondoDistribucion = false`
   comprobado por ISIN en el catálogo).
2. **Ningún fondo indexado y ningún fondo ya elegido antes** — los 104 ISIN de las carteras del repositorio
   se aplicaron como lista negra y se comprobó, además, que ninguna línea replique un índice.

**No se hereda ninguna regla del repositorio.** Ni el 55 % de renta variable de `cartera-myinvestor/`, ni el
coste mínimo de `cartera-ai/`, ni el criterio de Andrés, ni los descartes de las otras carteras. El mandato
del titular manda sobre las convenciones de la casa; aquí lo único que obliga son sus dos condiciones.

## Ficheros

| Fichero | Qué es |
| --- | --- |
| `100k.md` | La cartera de **100.000 €**: 7 fondos de RV + 3 de RF, 80 % de RV objetivo, 1,5472 % de TER |
| `200k.md` | La cartera de **200.000 €**: los mismos 7 + 3 y una pieza nueva de crédito corto, 80 % de RV, 1,5268 % de TER |
| `README.md` | Este mapa |

**Un fichero por talla, una cartera por fichero.** El mandato es el mismo; lo que cambia es cuántas líneas
aguanta el tamaño y, sobre todo, que a 100.000 € una línea de 4.000 € es ruido.

## Cómo está pensada (decisiones mías, no reglas del repo)

- **80 % renta variable / 20 % renta fija.** Sin horizonte declarado y con 2.000 €/mes entrando, el flujo
  nuevo es el colchón; pero un 20 % es el mínimo con el que el bloque defensivo hace algo. La caída de manual
  queda en −32,6 % (−32.600 € a 100k, −65.200 € a 200k).
- **Siete motores de RV, no uno:** global calidad-crecimiento (Natixis WCM), Europa mid cap (Echiquier
  Agenor), España small/mid (Okavango Delta), Asia ex-Japón (M&G Asian), emergentes (M&G Global EM), satélite
  de IA (Polar) y Japón small/mid (Swisscanto/SPARX). Geografías, tamaños y estilos distintos para que el
  resultado no dependa de acertar un solo estilo.
- **La renta fija no es un agregado:** crédito corporativo euro IG, duración corta (solo en 200k), high yield
  y deuda emergente en divisa fuerte.
- **Nada por encima del 15 %** a 100k y del 16 % a 200k. Ningún gestor manda.
- **Un solo temático** (IA, 10 %) porque un tema que puede caer la mitad no puede ser el motor.
- **Sin acciones ni ETF.** El mandato habla de fondos, y un ETF no se traspasa sin peaje fiscal.

## Por qué ninguna línea repite cartera

Los fondos ya usados en el repositorio son los clásicos del catálogo (Fundsmith, Comgest, Cobas, Horos,
Magallanes, Azvalor, Alken, GAM, Vontobel, Fidelity Iberia, DWS, Kaizen, Ábaco, Renta 4, AXA, Nordea,
Mirabaud, Jupiter India, Kopernik, Sigma, Janus Henderson, Indépendance AM, Nomura, Japan Deep Value, BNP
Japan, Man Japan, Federated Hermes, AB, Generali CEE, Twelve Capital, Sissener, los indexados de iShares,
Vanguard, Amundi y Fidelity…). Este diseño se construye **desde el universo que queda**: Natixis/WCM,
Echiquier, Abante, M&G, Polar, Swisscanto/SPARX, T. Rowe Price, BlueBay y DPAM.

## Estado a 16/11/2026

- **Dos tallas cerradas, ninguna ejecutada:** 100k (10 fondos, 1,5472 %) y 200k (11 fondos, 1,5268 %).
- **Datos**: catálogo de MyInvestor, ISIN, TER, mínimos, política de reparto, composición, volatilidad y
  corte verificados por ISIN el 16/11/2026. Un solo dato discrepante declarado: Okavango Delta publica
  1,51 % en la ficha del MCP y 1,41 % en el buscador; se usa el mayor.
- **Decisión abierta (del titular):** qué talla se ejecuta, el horizonte real y la tolerancia a la caída.
  No se consolida con las otras carteras del repositorio.

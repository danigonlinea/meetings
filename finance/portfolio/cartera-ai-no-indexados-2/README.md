---
title: "Cartera-ai no indexados 2: dos tallas (100k y 200k) con tres condiciones y ningún fondo repetido"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai-no-indexados-2, gestion-activa, sin-indexados, sin-dividendos, sin-repetir-fondos, acumulacion, myinvestor, 100k, 200k]
status: final
related: [finance/portfolio/README.md, finance/portfolio/cartera-ai-no-indexados-2/100k.md, finance/portfolio/cartera-ai-no-indexados-2/200k.md]
---

# Cartera-ai no indexados 2 — dos tallas, tres condiciones, cero fondos repetidos

Cartera nueva, diseñada desde cero el 16/11/2026 con **tres condiciones del titular**:

1. **Ningún fondo que reparta dividendos** — solo clases de acumulación (`distributing = 0` verificado en la
   ficha de cada ISIN).
2. **Ningún fondo indexado** — solo gestión activa (`management_type = Activo` verificado en la ficha).
3. **Ningún fondo ya elegido antes** — los 90 ISIN de las ocho carpetas de cartera del repositorio se
   aplicaron como lista negra al screening del catálogo de MyInvestor.

**No se hereda ninguna regla del repositorio.** Ni el coste mínimo de `cartera-ai/`, ni el 55 % de renta
variable de `cartera-myinvestor/`, ni el criterio de Andrés, ni la prohibición de acciones de otras
propuestas. Aquí no hay acciones ni ETF: el mandato habla de **fondos** del catálogo de MyInvestor.

## Ficheros

| Fichero | Qué es |
| --- | --- |
| `100k.md` | La cartera de **100.000 €**: 9 fondos de RV + 3 de RF, 85 % de RV objetivo, 1,6958 % de TER |
| `200k.md` | La cartera de **200.000 €**: 11 fondos de RV + 3 de RF, mismo 85 % objetivo, 1,7030 % de TER |
| `README.md` | Este mapa |

**Un fichero por talla, una cartera por fichero.** El mandato es el mismo; lo que cambia es cuántas líneas
aguanta el tamaño: a 200.000 € entran Europa small/mid «ex-UK» (Mirabaud) e India (Jupiter), porque tickets
de 6.000–10.000 € sí mueven la aguja; a 100.000 € serían ruido con gastos.

## Cómo está pensada (decisiones mías, no reglas del repo)

- **85 % renta variable / 15 % renta fija.** Sin horizonte declarado, sin necesidad de liquidez y con
  2.000 €/mes entrando, el flujo nuevo es el colchón. Al 85 % la caída de manual es del −38 % —el número que
  hay que poder mirar sin vender—; si no se aguanta, el problema es el 85 %, no los fondos.
- **Nueve motores de RV, no uno:** valor global profundo (Kopernik), flexible global (Sigma), small caps
  globales (Janus Henderson), small caps euro (Indépendance AM), Japón en sus dos mitades (Nomura large value
  cubierto + Japan Deep Value small/mid), Asia ex-Japón (Federated Hermes), emergentes de valor (AB) y
  Europa del Este (Generali CEE). El objetivo es que el resultado no dependa de un solo estilo ni de un solo
  país.
- **La renta fija no es un agregado:** cat bonds (riesgo de catástrofe), crédito corporativo euro y deuda
  emergente en divisa fuerte. Tres riesgos que no son bolsa ni tipos del euro.
- **Nada por encima del 14 %** en la talla de 100k y del 12 % en la de 200k.
- **Sin temáticos, sin oro, sin ETF.** Tecnología y salud ya pesan 19–20 % dentro de los fondos elegidos; un
  fondo de IA o de semiconductores sería doblar la apuesta. El oro del catálogo mueve 35–44 % de volatilidad
  por 1,6–2,1 % de coste: es una apuesta direccional, no un diversificador.
- **Divisa:** EUR en todas las clases; Japón con la divisa cubierta y los emergentes sin cubrir, que es donde
  la divisa forma parte de la tesis.

## Por qué ninguna línea repite cartera

Los fondos ya usados en el repositorio son los clásicos del catálogo (Fundsmith, Comgest, Cobas, DWS,
Alken, GAM, Vontobel, Franklin, Azvalor, Horos, Magallanes, MyInvestor Value, Kaizen, Ábaco, Renta 4, AXA,
Groupama, Amundi, iShares, Vanguard, Fidelity, BBVA, Nordea Global Real Estate, Sissener…). Este diseño se
construye **desde el universo que queda**: gestoras medianas con procesos propios (Heptagon/Kopernik,
Singular AM, Indépendance AM, Gesiuris, Mirabaud, Twelve Capital, Man, BlueBay…). Un fondo ya elegido queda
fuera aunque su clase sea distinta; Sissener, por ejemplo, es descarte escrito porque está en la propuesta de
`cartera-myinvestor/`.

## Estado a 16/11/2026

- **Dos tallas cerradas, ninguna ejecutada:** 100k (12 fondos, 1,6958 %) y 200k (14 fondos, 1,7030 %).
- **Datos**: catálogo MyInvestor vía MCP, NAV de 06–13/11/2026, `management_type`, `distributing`, TER,
  mínimos y *look-through* verificados por ISIN con `get_funds`, no por nombre.
- **Decisión abierta (del titular, no del agente):** qué talla se ejecuta, el horizonte real y si estas dos
  tallas conviven con las otras carteras del repositorio. No se consolidan con ellas.

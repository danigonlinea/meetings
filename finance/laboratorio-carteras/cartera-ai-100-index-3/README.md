---
title: "Cartera-ai 100 index 3: dos tallas solo con indexados de acumulación que no estén en ninguna otra cartera"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai-100-index-3, solo-indexados, sin-dividendos, acumulacion, sin-fondos-repetidos, myinvestor, 100k, 200k]
status: final
related: [finance/portfolio/README.md, finance/laboratorio-carteras/cartera-ai-100-index-3/100k.md, finance/laboratorio-carteras/cartera-ai-100-index-3/200k.md]
---

# Cartera-ai 100 index 3 — dos tallas, tres cláusulas

Cartera diseñada **desde cero** el 16/11/2026 con **tres cláusulas del titular** y ninguna otra:

1. **Únicamente fondos indexados** — cero gestión activa, cero ETF, cero acciones, cero monetarios.
2. **Ningún fondo que reparta dividendos** — solo clases de acumulación (`fondoDistribucion = false`
   verificado por ISIN).
3. **Ningún fondo que ya se haya elegido en otra cartera de este repositorio** — los **159 ISIN** de
   `finance/portfolio/` aplicados como lista negra por ISIN **y por fondo** (dos clases del mismo fondo
   comparten patrimonio en la ficha, así que 62 clases hermanas caen con su fondo).

**No se hereda ninguna regla del repositorio.** Ni el 55/45 de `finance/portfolio/cartera-myinvestor/`, ni el coste mínimo de
`cartera-ai/`, ni el 80 % de las hermanas, ni el techo del 40 % de `cartera-ai-definitivas-estudiar/cartera-ai-40-max-index/`, ni el diseño de
`cartera-ai-100-index/` ni el de `cartera-ai-100-index-2/`. Lo que no sea una de las tres cláusulas es decisión
mía, escrita con su razón: pesos, número de fondos, reparto RV/RF, bloque de renta fija y regla de aportaciones.

## Ficheros

| Fichero | Qué es |
| --- | --- |
| `100k.md` | La cartera de **100.000 €**: 7 fondos indexados (5 de RV + 2 de RF), 79,57 % de RV real, 0,2086 % de TER |
| `200k.md` | La cartera de **200.000 €**: **los mismos 7 fondos y pesos**, solo cambian los importes; 0,2086 % |
| `README.md` | Este mapa |

**Un fichero por talla, una cartera por fichero.** Las dos tallas comparten las siete líneas peso por peso: la
lista negra deja el universo sin ninguna pieza que el tamaño desbloquee, así que el doble de dinero no cambia
el diseño (está razonado en `200k.md` §1, incluida la línea de deuda pública que decido no añadir).

## Cómo está pensada (decisiones mías, no reglas)

- **80 / 20 de RV/RF.** Sin horizonte declarado y con 2.000 €/mes entrando, 80 % de RV es lo máximo que se
  puede ver caer un tercio (−32,42 %) sin vender; el 20 % de RF es la munición para comprar RV en las caídas
  sin vender RV.
- **El mundo se replica con cinco indexados regionales**: 52 % Norteamérica (MSCI North America, con Canadá),
  14 % Europa con Reino Unido (MSCI Europe), 4 % Japón, 2 % Pacífico ex-Japón y 8 % emergentes. Son los pesos
  del MSCI ACWI: no es una apuesta, es lo que queda cuando el MSCI World barato, el S&P 500 de Vanguard y el de
  iShares están gastados.
- **Dos riesgos de bono, no uno**: crédito corporativo global IG cubierto a euros (0,14 %) y bonos verdes
  globales cubiertos a euros (soberano, supranacional y agencia, 0,20 %).
- **Sin ETF, sin acciones, sin monetarios**: no son fondos indexados y el ETF no admite traspaso.
- **Las concesiones de la lista negra, por escrito**: núcleo troceado en cinco regiones, réplicas menos
  ajustadas en Japón (4,45 % de *tracking error*) y Norteamérica (2,44 %), y **cero small caps, cero ligado a
  inflación y cero inmobiliario** porque los únicos pasivos del catálogo están ya elegidos.

## Estado a 16/11/2026

- **Dos tallas cerradas, ninguna ejecutada:** 100k (7 fondos, 208,60 €/año, 0,2086 %) y 200k (mismos 7,
  417,20 €/año, 0,2086 %).
- **Datos:** catálogo público del buscador de MyInvestor (2.587 productos, 253 indexados, 224 de acumulación,
  163 libres por ISIN y 101 libres por fondo), instantánea de 16/11/2026. `get_funds` del MCP devolvió límite de
  uso, así que `management_type` no se releyó por ISIN: la prueba de «indexado» es la clasificación de la
  plataforma (`FONDOS_INDEXADOS`) más la descripción, que nombra el índice. Queda pendiente una llamada de 7
  ISIN cuando el límite se reponga.
- **Condición de no repetir verificada por script:** 0 coincidencias por ISIN, 0 por patrimonio, 0 posiciones
  repetidas por nombre; una sola mención previa afecta a los elegidos y está resuelta por escrito (el Vanguard
  European Stock aparecía como alternativa descartada en `cartera-ai-100-index-2/` §3).
- **Decisión abierta (del titular):** horizonte, tolerancia a la caída (−32,4 %), colchón fuera de la cartera,
  qué talla se ejecuta y si acepta las concesiones de `100k.md` §6.

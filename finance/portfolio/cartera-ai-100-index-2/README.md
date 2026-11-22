---
title: "Cartera-ai 100 index 2: dos tallas (100k y 200k) solo con indexados de acumulación que no estén en ninguna otra cartera"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai-100-index-2, solo-indexados, sin-dividendos, acumulacion, sin-fondos-repetidos, myinvestor, 100k, 200k]
status: final
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-100-index-2/100k.md
  - finance/portfolio/cartera-ai-100-index-2/200k.md
---

# Cartera-ai 100 index 2 — dos tallas, tres condiciones

Cartera diseñada **desde cero** el 16/11/2026 con **tres condiciones del titular** y ninguna otra:

1. **Únicamente fondos indexados** — cero gestión activa, cero ETF, cero acciones, cero monetarios.
2. **Ningún fondo que reparta dividendos** — solo clases de acumulación (`fondoDistribucion = false`
   verificado por ISIN).
3. **Ningún fondo que ya se haya elegido en otra cartera de este repositorio** — los **136 ISIN** de
   `finance/portfolio/` aplicados como lista negra, y además comprobados por nombre, gestora y clase
   hermana.

**No se hereda ninguna regla del repositorio.** Ni el 55/45 de `cartera-myinvestor/`, ni el coste mínimo de
`cartera-ai/`, ni el 80 % de las `no-indexados`, ni el techo del 40 % de `cartera-ai-definitivas-estudiar/cartera-ai-40-max-index/`, ni el
diseño de `cartera-ai-100-index/`. Lo que no sea una de las tres condiciones es decisión del agente, escrita
con su razón: pesos, número de fondos, reparto RV/RF, bloque de renta fija y regla de aportaciones.

## Ficheros

| Fichero | Qué es |
| --- | --- |
| `100k.md` | La cartera de **100.000 €**: 9 fondos indexados (6 de RV + 3 de RF), 79,79 % de RV real, 0,1113 % de TER |
| `200k.md` | La cartera de **200.000 €**: 10 indexados (el bloque de RF gana deuda emergente y el bono corto baja al 5 %), 79,79 % de RV real, 0,1128 % |
| `README.md` | Este mapa |

**Un fichero por talla, una cartera por fichero.** Las dos tallas comparten el bloque de RV peso por peso;
lo único que cambia es el número de riesgos del bloque de renta fija.

## Cómo está pensada (decisiones del agente, no reglas)

- **80 / 20 de RV/RF.** Sin horizonte declarado y con 2.000 €/mes entrando, 80 % de RV es lo máximo que se
  puede ver caer un tercio (−32,5 %) sin vender; el 20 % de RF es la munición para comprar RV en las caídas
  sin vender RV.
- **El mundo se replica con cinco indexados regionales** (52 % Norteamérica, 9 % Europa ex-UK, 3 % UK, 4 %
  Japón, 2 % Pacífico ex-Japón). No es una apuesta: son los pesos del MSCI World. Es la consecuencia directa
  de la condición 3, porque el núcleo global barato del catálogo está elegido en tres carteras y el segundo
  más barato es una posición de `cartera-renta4/`.
- **Emergentes al 10 %** (su peso de capitalización mundial) e **inmobiliario cotizado al 5 %** (el único
  indexado EPRA libre; cuesta 0,34 %).
- **Tres riesgos de bono distintos**: agregado global 1-5 años cubierto (0,15 %), deuda pública euro (0,13 %)
  y corporativo euro IG (0,15 %). A 200k se añade deuda emergente en divisa fuerte (0,18 %).
- **Sin ETF, sin acciones, sin monetarios**: no son fondos indexados y el ETF no admite traspaso.
- **Las tres concesiones de la condición 3, por escrito**: núcleo troceado en cinco regiones, inmobiliario al
  doble de precio y **ninguna small cap** (el único pasivo del catálogo está elegido en cuatro carteras).

## Estado a 16/11/2026

- **Dos tallas cerradas, ninguna ejecutada:** 100k (9 fondos, 0,1113 %, 111,30 €/año) y 200k (10 fondos,
  0,1128 %, 225,60 €/año).
- **Datos:** catálogo público del buscador de MyInvestor (2.587 productos, 253 indexados, 224 de acumulación,
  188 libres tras la lista negra), NAV de 12-13/11/2026. `get_funds` del MCP devolvió límite de uso, así que
  `management_type` no se releyó por ISIN: la prueba de «indexado» es la clasificación de la plataforma
  (`FONDOS_INDEXADOS`) más la descripción, que nombra el índice. Queda pendiente una llamada de 10 ISIN
  cuando el límite se reponga.
- **Condición 3 verificada por script y por nombre:** 0 coincidencias de ISIN, 0 posiciones repetidas, y dos
  descartes previos reutilizados con su razón escrita (la clase Acc de Europa ex-UK y la clase Acc del EPRA
  de Amundi).
- **Decisión abierta (del titular):** horizonte, tolerancia a la caída (−32,5 %), colchón fuera de la
  cartera, qué talla se ejecuta y si acepta las tres concesiones de §6 de `100k.md`.

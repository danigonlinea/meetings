---
title: "Cartera-ai 100 index 4: dos tallas solo con indexados de acumulación que no estén en ninguna otra cartera"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai-100-index-4, solo-indexados, sin-dividendos, acumulacion, sin-fondos-repetidos, myinvestor, 100k, 200k]
status: final
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-100-index-4/100k.md
  - finance/portfolio/cartera-ai-100-index-4/200k.md
---

# Cartera-ai 100 index 4 — dos tallas, dos condiciones

Cartera diseñada **desde cero** el 16/11/2026 con **dos condiciones del titular** y ninguna otra:

1. **Únicamente fondos indexados** — cero gestión activa, cero ETF, cero acciones, cero monetarios. Y con una
   exigencia añadida que me pongo yo: **la descripción de cada ficha tiene que nombrar el índice** que replica.
2. **Ninguno que reparta dividendos** — solo clases de acumulación (`fondoDistribucion = false` por ISIN).

La tercera condición que sí tenían las hermanas `-2` y `-3` —ningún fondo ya elegido antes— **también se
aplica** aquí por decisión propia: los **180 ISIN** de `finance/portfolio/` son lista negra, comprobada **por
ISIN y por fondo** (dos clases del mismo fondo comparten `patrimonio`). No la pedía el titular esta vez; se
mantiene porque una cartera nueva que reutilizara fondos de las otras doce dejaría de ser una cartera nueva.

**No se hereda ninguna regla del repositorio.** Ni el 55/45 de `cartera-myinvestor/`, ni el coste mínimo de
`cartera-ai/`, ni el 80 % de las hermanas, ni el techo del 40 % de `cartera-ai-definitivas-estudiar/cartera-ai-40-max-index/`, ni el troceado
regional de `cartera-ai-100-index-2/` y `-3`. Lo que no sea una de esas condiciones es decisión mía, escrita con
su razón.

## Ficheros

| Fichero | Qué es |
| --- | --- |
| `100k.md` | La cartera de **100.000 €**: 5 fondos indexados (3 de RV + 2 de RF), 85,16 % de RV real, 0,3771 % de TER, 377,10 €/año |
| `200k.md` | La cartera de **200.000 €**: **los mismos 5 fondos y pesos**, solo cambian los importes; 0,3771 %, 754,20 €/año |
| `README.md` | Este mapa |

**Un fichero por talla, una cartera por fichero.** Las dos tallas comparten las cinco líneas peso por peso: el
universo libre no tiene ninguna pieza que el tamaño desbloquee, así que el doble de dinero no cambia el diseño
(razonado en `200k.md` §1 y §5, con las cuatro líneas que se rechazan por tamaño y su cuenta).

## Cómo está pensada (decisiones mías, no reglas)

- **Un núcleo global de verdad, no un mundo troceado.** `MyInvestor Mundo Desarrollado y Emergente` replica el
  **MSCI ACWI** al **0,43 %** y está libre: con él, el mundo entero cabe en una orden en euros y el diseño se
  queda en cinco líneas. Las hermanas `-2` y `-3` tenían que trocear el mundo en cinco regiones porque el núcleo
  global estaba gastado; aquí no.
- **85 % de RV / 15 % de RF.** Horizonte asumido largo (15+ años, escrito como asunción porque el titular no lo
  declaró) y 2.000 €/mes entrando: el 85 % es la caída que se puede mirar sin vender, **−35,5 % (−35.548 € en
  100k, −71.095 € en 200k)**. El 15 % de RF en euros es la munición para comprar RV en las caídas sin vender RV.
- **Dos convicciones, y solo dos.** El **10 % en eurozona** (los gastos son en euros y el índice la infrapondera
  frente a su peso económico) y el **8 % en emergentes** (sobreponderación de 1,6 veces, no el doble). Todo lo
  demás va al núcleo: no hay apuesta de sector, ni de estilo, ni de país suelto.
- **La renta fija en euros, en sus dos mitades**: deuda pública de la zona euro (0,36 %) y crédito euro IG
  (0,16 %). El euro aggregate no está libre; estas dos lo reconstruyen sin pagar cobertura de divisa.
- **Lo que se paga por las condiciones**: cero small caps, cero ligado a inflación y cero inmobiliario (los
  únicos indexados del catálogo están ya elegidos) y **Japón sin línea propia** (el único indexado japonés libre
  no nombra su índice en la ficha).

## Estado a 16/11/2026

- **Dos tallas cerradas, ninguna ejecutada:** 100k (5 fondos, 377,10 €/año, 0,3771 %) y 200k (mismos 5, 754,20
  €/año, 0,3771 %).
- **Datos:** catálogo público del buscador de MyInvestor (2.587 productos → 253 indexados → 224 de acumulación →
  221 abiertos → 142 libres por ISIN → **67 libres por fondo** con los 180 ISIN del repositorio como lista negra),
  instantánea de 16/11/2026. `get_funds` del MCP devolvió **límite de uso**, así que `management_type` no se
  releyó por ISIN: la prueba de «indexado» es la clasificación de la plataforma (`FONDOS_INDEXADOS`) más la
  descripción de la ficha, que nombra el índice en las cinco líneas. Queda pendiente una llamada de 5 ISIN
  cuando el límite se reponga.
- **Condición de no repetir verificada por script:** 0 coincidencias de los 5 ISIN en `finance/portfolio/`, 0 por
  `patrimonio`, 0 por nombre o gestora. Una sola mención previa afecta a los elegidos y está resuelta por
  escrito: `MyInvestor Mundo Desarrollado y Emergente` aparecía como **alternativa descartada** en
  `cartera-ai-100-index-3/100k.md` §6, no como posición (`100k.md` §1.1, punto 4).
- **Decisión abierta (del titular):** horizonte, tolerancia a la caída (−35,5 %), colchón fuera de la cartera,
  qué talla se ejecuta y si acepta las concesiones escritas en `100k.md` §6.

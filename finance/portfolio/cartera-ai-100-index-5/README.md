---
title: "Cartera-ai 100 index 5: dos tallas solo con indexados de acumulación que no estén en ninguna otra cartera"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai-100-index-5, solo-indexados, sin-dividendos, acumulacion, sin-fondos-repetidos, myinvestor, 100k, 200k]
status: final
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-100-index-5/100k.md
  - finance/portfolio/cartera-ai-100-index-5/200k.md
---

# Cartera-ai 100 index 5 — dos tallas, dos condiciones

Cartera diseñada **desde cero** el 16/11/2026 con **dos condiciones del titular** y ninguna otra:

1. **Únicamente fondos indexados** — cero gestión activa, cero ETF, cero acciones, cero monetarios. Y con una
   exigencia añadida que me pongo yo: **la descripción de cada ficha tiene que nombrar el índice** que replica.
2. **Ninguno que reparta dividendos** — solo clases de acumulación (`fondoDistribucion = False` por ISIN).

La tercera condición —**ningún fondo ya elegido en otra cartera**— esta vez la pidió el titular, y se aplica con
dureza: los **129 ISIN** que el repositorio tiene como **posición** son lista negra, comprobada **por ISIN y por
fondo** (dos clases del mismo fondo comparten `patrimonio`). El efecto es el que decide toda la cartera: cierra
el núcleo barato del catálogo y obliga a pagar 14 pb más por el MSCI World.

**No se hereda ninguna regla del repositorio.** Ni el 55/45 de `cartera-myinvestor/`, ni el coste mínimo de
`cartera-ai/`, ni el 80 % de las hermanas, ni el techo del 40 % de `cartera-ai-40-max-index/`, ni el troceado
regional de `cartera-ai-100-index-2/`, `-3` y `-4`. Lo que no sea una de esas condiciones es decisión mía,
escrita con su razón.

## Ficheros

| Fichero | Qué es |
| --- | --- |
| `100k.md` | La cartera de **100.000 €**: 4 fondos indexados (3 de RV + 1 de RF), 84,95 % de RV real, 0,1930 % de TER, 193,00 €/año |
| `200k.md` | La cartera de **200.000 €**: **los mismos 4 fondos y pesos**, solo cambian los importes; 0,1930 %, 386,00 €/año |
| `README.md` | Este mapa |

**Un fichero por talla, una cartera por fichero.** Las dos tallas comparten las cuatro líneas peso por peso: el
universo libre no tiene ninguna pieza que el tamaño desbloquee, así que el doble de dinero no cambia el diseño
(razonado en `200k.md` §1).

## Cómo está pensada (decisiones mías, no reglas)

- **Cuatro líneas, no siete.** Con un núcleo global vivo (MSCI World al 0,20 %), el mundo entero cabe en una
  orden y solo quedan dos decisiones que tomar: inclinar a Europa y a emergentes. Todo lo demás va al núcleo.
  Las hermanas `-2` y `-3` troceaban el mundo en cinco regiones porque el núcleo global estaba gastado; aquí no.
- **85 % de RV / 15 % de RF.** Horizonte asumido largo (15+ años, escrito como asunción porque el titular no lo
  declaró) y 2.000 €/mes entrando: el 85 % es la caída que se puede mirar sin vender, **−35,5 % (−35.500 € en
  100k, −71.000 € en 200k)**. El 15 % de RF en el agregado global cubierto a euros es la munición para comprar
  RV en las caídas sin vender RV.
- **Dos inclinaciones, y solo dos.** El **12 % en Europa** (los gastos son en euros y el mundo la deja en ~15 %)
  y el **13 % en emergentes** (1,5 veces su peso, no el doble).
- **Una sola línea de renta fija**: el Bloomberg Global Aggregate cubierto a euros al 0,15 %. Compra deuda
  pública, cuasi-gubernamental, corporativa y titulizada en una orden; las mitades sueltas libres cuestan más.
- **Lo que se paga por las condiciones**: cero small caps, cero inmobiliario, cero ligado a inflación (los únicos
  indexados del catálogo están ya elegidos en otras carteras) y **emergentes con filtro ESG** (el MSCI EM limpio
  está usado; la variante libre más barata paga 5,42 % de *tracking error*).

## Estado a 16/11/2026

- **Dos tallas cerradas, ninguna ejecutada:** 100k (4 fondos, 193,00 €/año, 0,1930 %) y 200k (los mismos 4,
  386,00 €/año, 0,1930 %).
- **Datos:** catálogo público del buscador de MyInvestor (2.587 productos → 253 indexados → 224 de acumulación →
  221 abiertos → 177 libres por ISIN → **121 libres por fondo** con los 129 ISIN en posición como lista negra),
  instantánea de 16/11/2026. **Fuente:** `api.myinvestor.es/cperf-server/rest/public/fondos/find-fondos`, el JSON
  que sirve la propia plataforma; el MCP de MyInvestor cortó por límite de uso a mitad de la búsqueda y no se
  insistió (sus términos prohíben el uso masivo), así que la lectura se hizo contra el buscador público, que es
  la misma fuente que alimenta al MCP.
- **Condición de no repetir verificada por script y a mano:** 0 coincidencias de los 4 ISIN como posición, 0 por
  `patrimonio`, 0 por nombre o gestora. Tres de los cuatro aparecen solo como **alternativa descartada** en otros
  documentos y están resueltos por escrito en `100k.md` §1.1.5; el cuarto no aparece nunca.
- **Decisión abierta (del titular):** horizonte, tolerancia a la caída (−35,5 %), colchón fuera de la cartera,
  qué talla se ejecuta y si acepta las concesiones escritas en `100k.md` §6.

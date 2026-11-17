---
title: "Cartera-ai rock-desmontado: mapa de la cartera"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai-rock-desmontado, mapa, indexado, satelite-activo, rock, monetario, myinvestor]
status: final
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-rock-desmontado/100k.md
  - finance/portfolio/cartera-ai-rock-index-value-todo/100k.md
---

# Cartera-ai rock-desmontado — mapa

**Qué es.** Una cartera de 100.000 € construida sobre la foto de
`cartera-myinvestor/cartera-actual.md` **sin ataduras**: Rock se desmonta por traspaso (0 € de impuestos) y
su cupo de indexado se libera para comprar el núcleo al precio real de un índice.

**Qué la distingue de sus hermanas:**

- De `cartera-ai/` y `cartera-ai-100-index*/` (las indexadas puras): aquí el riesgo es **55,3 % de RV**, no
  el 79-85 %, hay **monetario escalonado** y **cat bonds**; y no hay acciones sueltas.
- De `cartera-ai-rock-index-value-todo/` (la que mantiene Rock): **379 €/año menos** de coste, el mismo
  riesgo, la mitad de duración y dos huecos tapados (small caps y activos reales).
- De las `cartera-ai-no-indexados*/`: nada de sesgo value obligado ni de trece líneas activas; el activo se
  limita a tres papeles donde un índice no llega.

**Qué no es.** No es la cartera vigente del titular (esa es `cartera-myinvestor/propuesta-actual.md`) y no se
ejecuta sobre el mismo dinero a la vez que ella.

**No es asesoramiento financiero.** La decisión es del titular.

## El documento

| Talla | Fichero | Fondos | RV de bloque | RV real (*look-through*) | Coste total | Caída de manual |
| --- | --- | --: | --: | --: | --: | --: |
| 100.000 € (10.000 de colchón aparte) | `100k.md` | 12 | 55 % | 55,31 % | **236,10 €/año (0,236 %)** | −23,46 % ≈ −21.118 € |

El fichero es la cartera entera: ISIN, pesos, razón fondo a fondo con su pega, métricas contra las tres
carteras de referencia, el precio de cada decisión en euros al año, las 20 órdenes en dos fases (Rock por el
monetario puente), descartes con número y señales de revisión.

## El diseño en una línea

Núcleo MSCI World al **0,06 %** (29.000 €) con emergentes al 0,16 %, small caps al 0,30 % y activos reales al
0,17 %; renta fija **indexada y corta** (agregado global 1-5Y al 0,08 % y crédito IG euro al 0,12 %);
monetario en dos peldaños (Groupama €STR + DWS Euro Ultra Short al 0,15 %); y **dos satélites activos con
papel propio**: Robeco QI European Conservative al 1,01 % (sesgo Europa con vol baja) y Twelve Cat Bond al
1,30 % (un activo que no depende de tipos ni de bolsa). Entre los dos cuestan **103 €/año**, y están
cuantificados en §7 de `100k.md` para poder quitarlos si parece caro.

## Las dos variantes que salen de este documento

| Variante | Coste/año | Qué se gana o se pierde |
| --- | ---: | --- |
| **Con Rock** en vez de desmontarla (`cartera-ai-rock-index-value-todo`) | 614,70 € | Se evita la operación, pero vuelven el bono a 20+ años y 379 €/año |
| **100 % indexada**, sin los dos satélites | **126 €** | −110 €/año, pero la cartera queda con World al 63 % de EE. UU. y sin diversificador |

## Cómo se desmonta Rock sin tributar

Cancelar la cartera automatizada **hacia un monetario puente**, no hacia efectivo: eso es traspaso y cuesta
0 €. Vender costaría ≈2.590 € de impuestos sobre ≈13.650 € de plusvalía. La ruta está en `100k.md` §3 y las
órdenes en §8.2; el coste real es quedarse 5-10 días con 30.000 € fuera del mercado.

---
title: "Ranking DeepSeek de las once carteras: cuáles ganan a 15 años y cuáles no tienen sentido hoy"
date: 2026-11-25
type: portfolio-research
category: finance
tags: [cartera, ranking, cartera-ai-definitivas-estudiar, 15-anos, coste, caida, dominancia, punto-de-cruce, myinvestor, ranking-deepseek]
status: final
related:
  - finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/README.md
  - finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/ranking-argon.md
  - finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-carbon/100k.md
  - finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-argon/100k.md
  - finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-final-atrevida/110k.md
  - finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-hy4-definitiva/100k.md
  - finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-rock-desmontado/100k.md
  - finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-neon/110k.md
---

# Ranking DeepSeek: las once carteras ordenadas por euros a 15 años

Comparación de las **once carteras** de [`cartera-ai-definitivas-estudiar/`](README.md) con **un solo criterio y una sola hipótesis**: cuánto dinero queda a 15 años por cada 100.000 €, y a qué precio de caída y de comisión se compra esa cifra. No puntúa señales ni suma notas.

**Qué es y qué no es.** Este documento responde a «¿cuáles ganan y cuáles tienen sentido hoy?». No decide nada y no cambia ninguna propuesta: el % de renta variable es del titular. Es hermano de [`ranking-argon.md`](ranking-argon.md), que ordena las mismas carteras con otro criterio —una nota de comité con cinco ejes: coste, factores, escudo, ejecutabilidad e integridad de datos—, y **los dos discrepan a propósito**: allí `cartera-ai-argon` es la #1 por escudo y ejecutabilidad, y aquí queda la séptima en euros porque compra menos bolsa sobre 100.000 € (ver §7). Ninguno de los dos es «el bueno»: son dos preguntas distintas.

## 1. Método y supuestos

| Pieza | Valor | Por qué |
| --- | --- | --- |
| Bolsa bruta | **6,00 %/año** | Supuesto único para todas; el mismo para las once, para no ordenar por el supuesto de cada documento |
| Renta fija y colchón | **3,00 %/año** | Todo lo que no es bolsa por *look-through* se trata como RF |
| Horizonte | **15 años** | El que declaran las propuestas nuevas (2026 → 2041) |
| Base | **100.000 €** sin aportaciones | `neon` (110.000 €) y `final-atrevida` (110.000 €) se llevan a 100.000 € para comparar |
| Coste | TER ponderado declarado en cada documento | No se añaden comisiones de éxito: donde existen (c4) el coste real es mayor |
| Retorno neto | RV × 6 % + RF × 3 % − TER | Aritmética lineal, sin alfa de ningún gestor |

**No se usan las esperanzas que declara cada documento** (6,65 % en argon y carbon, 6,50 % en neon, 6,1 % en final-atrevida, 5,11 % en hy4, 4,8 % en final-conservadora): cada una sale de un supuesto de bolsa distinto, así que compararlas ordena supuestos, no carteras.

## 2. La tabla, de más a menos euros

| # | Cartera | RV real | TER | €/año | Neto/año | 100k → 15 años | Caída que declara |
| --: | --- | --: | --: | --: | --: | --: | --- |
| 1 | [`cartera-ai-final-atrevida`](cartera-ai-final-atrevida/110k.md) | 82,15 % | 0,798 % | 877,80 | 4,67 % | **198.205 €** | −33,4 % (manual) |
| 2 | [`cartera-ai-carbon`](cartera-ai-carbon/100k.md) | 80,15 % | 0,746 % | 746,20 | 4,66 % | **197.973 €** | −32,65 % (2008) · **−5,20 %** (2022) |
| 3 | [`cartera-ai-hy4-definitiva`](cartera-ai-hy4-definitiva/100k.md) | 65,50 % | 0,537 % | 537,10 | 4,43 % | 191.538 € | máx. −7,97 % (backtest 5A) |
| 4 | [`cartera-ai-rock-desmontado`](cartera-ai-rock-desmontado/100k.md) | 55,31 % | **0,236 %** | 236,10 | 4,42 % | 191.408 € | −23,46 % (manual) |
| 5 | [`cartera-ai-40-max-index`](cartera-ai-40-max-index/100k.md) | 73,03 % | 0,792 % | 792,00 | 4,40 % | 190.739 € | −30,0 % (manual) |
| 6 | [`cartera-ai-andres`](cartera-ai-andres/100k.md) | 60,31 % | 0,463 % | 463,30 | 4,35 % | 189.294 € | −25,3 % (manual) |
| 7 | [`cartera-ai-argon`](cartera-ai-argon/100k.md) | 68,76 % | 0,725 % | 725,40 | 4,34 % | 189.071 € | **−4,54 %** (2022 s/100k) · −28,0 % (2008) |
| 8 | [`cartera-ai-neon`](cartera-ai-neon/110k.md) | 72,28 % | 0,850 % | 933,90 | 4,32 % | 188.544 € | **−5,10 %** (2022) |
| 9 | [`cartera-ai-final-conservadora`](cartera-ai-final-conservadora/100k.md) | 54,61 % | 0,566 % | 509,70 | 4,07 % | 181.982 € | −23,2 % (manual) |
| 10 | [`cartera-ai-rock-index-value-todo`](cartera-ai-rock-index-value-todo/100k.md) | 55,51 % | 0,615 % | 614,70 | 4,05 % | 181.405 € | −23,54 % (manual) |
| 11 | [`cartera-ai-c4-defensiva`](cartera-ai-c4-defensiva/100k.md) | 34,06 % | 0,608 % | 607,60 | 3,41 % | 165.464 € | −15,07 % (manual) |

**Lo primero que dice la tabla:** las cuatro primeras están separadas por **7.000 €** en quince años (un 3,6 %) y la primera y la séptima por **9.100 €**. Con un horizonte así, la bolsa manda y la selección de fondos decora: lo que de verdad separa a estas once carteras es cuánta caída se está dispuesto a mirar, no qué gestor se elige.

## 3. El coste en euros, que es la parte que no se recupera

Comisión acumulada a 15 años sobre 100.000 € con el mismo supuesto:

| Cartera | TER | Comisiones en 15 años |
| --- | --: | --: |
| rock-desmontado | 0,236 % | **6.593 €** |
| andres | 0,463 % | 13.007 € |
| hy4-definitiva | 0,537 % | 15.318 € |
| c4-defensiva | 0,608 % | 15.198 € *(sin contar sus cuatro comisiones de éxito)* |
| final-conservadora | 0,566 % | 15.424 € |
| rock-index-value-todo | 0,615 % | 16.766 € |
| argon | 0,725 % | 20.695 € |
| carbon | 0,746 % | 22.263 € |
| 40-max-index | 0,792 % | 22.896 € |
| final-atrevida | 0,798 % | 23.918 € |
| neon | 0,850 % | **24.406 €** |

La diferencia entre la más barata y la más cara es de **17.800 €** en quince años: más que el 15 % del capital inicial. Y el TER no es todo el coste: no incluye comisiones de éxito, ni los costes de transacción internos de los fondos activos (0,1-0,5 % típico).

## 4. Las que no tienen sentido hoy, con su número

Estos tres veredictos no son de gusto: son comparaciones entre carteras del mismo contenedor, con la misma bolsa y el mismo supuesto.

1. **`rock-index-value-todo` está dominada por `rock-desmontado`.** Misma bolsa (55,51 % frente a 55,31 %, menos de 1 pp) y **2,6 veces el coste** (614,70 €/año frente a 236,10 €). Además arrastra el bono a 20+ años dentro de Rock, que aporta el 60 % del riesgo de tipos de toda la cartera. En quince años: 181.405 € frente a 191.408 €. Para empatar tendría que rendir la bolsa un 192 % anual: **no la alcanza nunca**.
2. **`final-conservadora` está dominada por `rock-desmontado`.** 54,61 % de bolsa frente a 55,31 % —prácticamente la misma—, **el doble de coste** (509,70 € frente a 236,10 €) y peor año malo declarado (−23,2 % frente a −23,46 %, empate). 181.982 € frente a 191.408 €. Su valor real es otro y está en su documento: es la matriz de 12 fondos con el plan de 1.000 €/mes al céntimo.
3. **`c4-defensiva` no encaja en un horizonte de 15 años.** Con 34,06 % de bolsa da 165.464 €, **32.500 € menos que carbon y 25.900 € menos que la más barata**, y paga 0,608 % con cuatro comisiones de éxito encima. Solo tiene sentido si la condición es no ver una caída por encima del 15 %; si la tolerancia admite −23 %, hay una cartera más barata y con más bolsa.

Y dos que no están dominadas pero tampoco aportan: **`40-max-index`** (73 % de bolsa a 0,792 %, sin escudo probado en 2022 y sin el sesgo fuera de EE. UU. de las nuevas) y **`andres`** (60,3 % a 0,463 %, la segunda más barata, pero es una cartera sin bloque defensivo y sin prueba de año malo).

## 5. Dónde está el punto de cruce

La más barata de la tabla (`rock-desmontado`, 55,31 % de bolsa y 0,236 %) gana a casi todas si la bolsa renta poco. El umbral, calculado con las dos comisiones:

| Cartera | Adelanta a `rock-desmontado` si la bolsa bruta anual supera… |
| --- | --: |
| carbon | **5,05 %** |
| final-atrevida | 5,09 % |
| hy4-definitiva | 5,95 % |
| 40-max-index | 6,14 % |
| neon | 6,62 % |
| argon | 6,64 % |
| andres | 7,55 % |

`c4-defensiva` es la excepción y va al revés: con 34,06 % de bolsa solo adelanta a la barata si la bolsa bruta renta **menos del 1,25 % anual**; por encima de eso pierde en euros por llevar 21 pp menos de bolsa.

Traducido: **con la bolsa al 6 % bruto, carbon y final-atrevida son las que más dejan; con la bolsa al 3 %, gana la barata del 55 %** (151.000 € frente a 145.000 € de media en las demás). El escenario no decide la calidad de la cartera: decide cuál conviene.

## 6. Veredicto: qué tiene sentido hoy

Con los mercados en máximos de concentración —46 % del S&P 500 en tecnología, según el [informe semanal del 25/11](../../reports/informe-semanal-2026-11-25.md), la caída de Nvidia de este mes y la revisión de la SEC—, lo que distingue a las tres carteras construidas para ese riesgo es el **año 2022 probado**:

| Si el titular… | La cartera que encaja | Por qué, con su cifra |
| --- | --- | --- |
| quiere la que más deja y aguanta −33 % | **`carbon`** | 197.973 € a 15 años, 0,746 % y un 2022 de −5,20 % con un escudo que ganó +0,16 %; 17 traspasos sin pasar por Hacienda desde la cuenta real |
| quiere el máximo de bolsa y no le importa la caída | `final-atrevida` | 198.205 €, el primero de la tabla, con −33,4 % manual y partiendo de cero |
| quiere el mejor equilibrio coste/riesgo en el medio | **`hy4-definitiva`** | 65,5 % de bolsa a 0,537 %: 191.538 €, y el único backtest con caída máxima del −7,97 % |
| quiere gastar lo mínimo y no necesita más bolsa | `rock-desmontado` | 0,236 % y 6.593 € de comisiones en 15 años, con −23,46 % de caída |
| quiere ejecutarlo desde su cuenta sin tocar Gamma | `argon` | 189.071 € y un 2022 de −4,54 %; 14 traspasos y sus 8.000 € de `Gamma Global A` intactos |
| no puede mirar una caída del 20 % | `c4-defensiva`, sabiendo su precio | −15,07 %, pero 165.464 €: **32.600 € menos** que carbon |

**Ninguna de las once está ejecutada** y ninguna sustituye a `finance/portfolio/cartera-myinvestor/propuesta-pieza.md`, que sigue pendiente de la revisión del titular y es la que se ejecuta si no decide otra cosa.

## 7. Corrección de una cifra que se lee mal entre documentos

`cartera-ai-argon` declara **76,40 % de renta variable real sobre los 90.000 € invertibles**, y ese número aparece en su README y en el mapa de carteras. Sobre los **100.000 € totales** —la base que usan las otras diez— es **68,76 %**, con **0,725 %** de TER y 725,40 €/año, porque 10.000 € viven en `Groupama Trèsorerie`. Comparar su 76,40 % con el 72,28 % de `neon` o el 80,15 % de `carbon` es comparar bases distintas, y es la razón de que este ranking la coloque séptima en euros mientras `ranking-argon.md` la pone primera en su nota de comité: allí pesa el escudo de 2022 (−4,54 %), aquí pesan los euros sobre 100.000 €.

## 8. Lo que falta para decidir

- **Tolerancia en euros, no en porcentaje**: la caída de manual de carbon son −32.654 € sobre 100.000 €. Si esa cifra no se puede mirar sin vender, la discusión es c4-defensiva y su coste de 32.600 €, no el orden de la tabla.
- **Aportación mensual**: este ranking no la incluye. Con 1.000 €/mes durante 15 años, el 73 % del dinero entra después de la primera foto y el coste pesa más: la ventaja de las carteras baratas crece.
- **Colchón fuera de la cartera**: ninguna de las once lo tiene; varias lo suponen (6-12 meses).
- **Qué talla se ejecuta** y sobre qué base (100.000 € actuales, 90.000 € invertibles o 110.000 € con 10.000 € nuevos).

Este documento es análisis de los documentos del propio repositorio, con sus cifras y su fecha. No es asesoramiento y no da órdenes.

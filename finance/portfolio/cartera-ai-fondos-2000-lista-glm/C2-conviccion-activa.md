---
title: "C2 — Convicción activa (100.000 €)"
date: 2026-11-20
type: portfolio-proposal
category: finance
tags: [gestion-activa, value, conviccion, japon, asia, latinoamerica, india]
status: propuesta
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/validacion.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/fondos-revisados.md
---

# C2 — Convicción activa

> **Qué es.** 9 fondos, 100.000 € exactos, **79,81 % de renta variable real** (look-through) y **1.180,10 €/año (1,1801 %)**. Caída de manual **-32,43 % = 32.434 €** y **≈5,93 % esperado** con los supuestos de §4.
>
> **Criterio.** ningún indexado: cada línea es un proceso de gestión con evidencia en la ficha (value, convicción concentrada, cuantitativo), más crédito de coste bajo.
>
> **Método y límite.** Fichas del repo (snapshot de la app del 19/11/2026) y verificación de los 9 ISIN en el catálogo MCP de MyInvestor el 20/11/2026 (TER, `distributing`, mínimos, avisos). **No es asesoramiento financiero**: la decisión y la ejecución son del titular.

---

## 1. Mandato

| Lo que pide el encargo | Cómo se cumple | Qué cuesta |
| --- | --- | --- |
| 100.000 € | 9 líneas que suman exactamente 100.000 € | Nada |
| Cinco carteras sin repetir fondo entre ellas | 50 ISIN distintos en el encargo, comprobados por ISIN, nombre normalizado y clase hermana (§ de [`validacion.md`](validacion.md)) | Ninguna línea se abarata con un fondo ya usado en otra de las cinco |
| Cartera diversificada | ningún indexado: cada línea es un proceso de gestión con evidencia en la ficha (value, convicción concentrada, cuantitativo), más crédito de coste bajo | Ver §4 |
| Solo fondos del listado `finance/fondos-myinvestor/` | Los 9 ISIN están en el listado (1.980 fichas) | Sin ETF ni acciones: traspaso sin peaje fiscal |
| Sin distribución de dividendos | 9/9 clases de acumulación (`distributing=0` en el MCP) | Nada |

**Supuestos escritos, no reglas heredadas:** horizonte de 15 años o más (en C4, de 7 años o más), colchón de 6-12 meses fuera de la cartera, sin aportaciones modeladas. **No se heredó ninguna lista negra de carteras anteriores**: la no-repetición vale solo entre estas cinco, y no se aplicó ningún veto más allá del encargo.

## 2. Cartera

| # | Rol | Fondo | ISIN | € | % | TER | €/año | Éxito | RV/RF | Mínimo (MCP) | Corte |
| --: | --- | --- | --- | --: | --: | --: | --: | --: | --- | --- | --- | |
| 1 | Convicción activa de RV | Cobas LUX SICAV - Palm Harbour Global Value Fund-F Acc EUR | `LU1935059029` | 22.000 | 22 % | 1,02 % | 224,40 | — | RV 96,87 % | 1,00 € | 14:00 |
| 2 | Convicción activa de RV | Robeco BP US Large Cap Equities D € | `LU0474363974` | 14.000 | 14 % | 1,46 % | 204,40 | — | RV 97,11 % | 1,00 € | 14:00 |
| 3 | Convicción activa de RV | Muza FI | `ES0184893008` | 12.000 | 12 % | 1,14 % | 136,80 | 9,00 % | RV 97,02 % | 0,001 participaciones | 12:00 |
| 4 | Convicción activa de RV | Nomura Japan Strategic Value Fund Class A EUR Hedged | `IE00B4NF1620` | 9.000 | 9 % | 1,57 % | 141,30 | — | RV 98,31 % | 0,00 € | 12:00 |
| 5 | Convicción activa de RV | Federated Hermes Asia ex-Japan Equity Fund Class R EUR Acc | `IE00B88WFS66` | 9.000 | 9 % | 1,59 % | 143,10 | — | RV 98,86 % | 0,00 € | 09:00 |
| 6 | Convicción activa de RV | Renta 4 Latinoamérica R FI | `ES0173320039` | 9.000 | 9 % | 1,64 % | 147,60 | 9,00 % | RV 95,30 % | 10,00 € | 12:00 |
| 7 | Convicción activa de RV | Ashoka WhiteOak India Opportunities Fund Class D EUR Acc | `IE00BDR0JY05` | 7.000 | 7 % | 1,05 % | 73,50 | — | RV 99,09 % | 1 participación | 10:00 |
| 8 | Crédito y liquidez de coste bajo | Goldman Sachs AAA ABS - X Cap EUR | `LU1835818565` | 11.000 | 11 % | 0,80 % | 88,00 | — | RF 97,30 % | 0,00 € | 14:00 |
| 9 | Crédito y liquidez de coste bajo | Ostrum Credit Ultra Short Plus R/C (EUR) | `FR001400CFA4` | 7.000 | 7 % | 0,30 % | 21,00 | 20,00 % | RF 85,48 % | 0,00 € | 10:00 |
| | **Total** | **9 fondos** | | **100.000** | **100 %** | **1,1801 %** | **1.180,10** | | | | |

## 3. Bloques por rol

| Bloque | € | % del total | TER medio | €/año |
| --- | --: | --: | --: | --: |
| Convicción activa de RV | 82.000 | 82,00 % | 1,3062 % | 1.071,10 |
| Crédito y liquidez de coste bajo | 18.000 | 18,00 % | 0,6056 % | 109,00 |

## 4. Métricas

| Métrica | Valor | Cómo se calcula |
| --- | --- | --- |
| RV *look-through* | 79,81 % | Σ importe × RV declarada (MCP 20/11) |
| Renta fija | 17,04 % | Σ importe × RF declarada (MCP 20/11) |
| Liquidez | 3,14 % | Σ importe × liquidez declarada |
| Caída de manual | -32,43 % = 32.434 € | −(40 % × RV + 3 % × RF) |
| Coste anual | 1.180,10 € = 1,1801 % | Σ importe × TER del MCP |
| Esperanza central | 5,93 % | Σ importe × retorno esperado por sleeve |
| Escenario pesimista | 3,93 % | RV −2,5 pp de retorno esperado |
| Escenario favorable | 7,23 % | RV +1,5 pp de retorno esperado |
| Indexado | 0 % aproximado del importe en réplica de índice | gestión indexada declarada o índice nombrado en la ficha/MCP |

**Supuestos de la esperanza** (estimación del agente, no dato de mercado): RV desarrollada 6,7 %, emergentes/Asia 7,5 %, crédito y agregado 3,0 %, liquidez 2,3 %. La esperanza la decide el % de RV, no la selección de fondos.

**Las comisiones de éxito no están en el coste anual.** Donde existen se publican en la tabla (§2); en un año bueno añaden hasta ≈3.290 € sobre las líneas que las llevan si todas superan su objetivo, y menos o cero en un año plano.

## 5. Geografía por *look-through*

| Región | € de RV | % de la RV con desglose |
| --- | --: | --: |
| Estados Unidos | 13.461 | 16,87 % |
| España | 8.859 | 11,10 % |
| Japón | 8.697 | 10,90 % |
| India | 7.030 | 8,81 % |
| Corea del Sur | 4.743 | 5,94 % |
| Brasil | 3.671 | 4,60 % |
| Reino Unido | 3.052 | 3,82 % |
| México | 2.980 | 3,73 % |
| China | 2.963 | 3,71 % |
| Francia | 2.792 | 3,50 % |
| Italia | 2.536 | 3,18 % |
| Filipinas | 1.343 | 1,68 % |

Base con desglose: 79.808 € de RV. Las líneas sin desglose regional no entran en la tabla; cálculo derivado del top de países del MCP, no un dato de la gestora.

## 6. Razón fondo a fondo

- **`LU1935059029` Cobas LUX SICAV - Palm Harbour Global Value Fund-F Acc EUR** — Value global de Palm Harbour dentro de Cobas LUX SICAV: 3A +14,5 % y 5A +8,5 % anualizados, mínimos de 1 €. Cartera concentrada en consumo cíclico, industria y materiales.
- **`LU0474363974` Robeco BP US Large Cap Equities D €** — Value de Boston Partners («Tres Círculos»: value + calidad + momentum) en large caps de EE. UU.; 5A +11,2 % anualizados, active share alto declarado, mínimo 1 €.
- **`ES0184893008` Muza FI** — Convicción española-europea: top 10 = 71 % del patrimonio (Atalaya Mining 11 %, Zegona 9,7 %). 2025 +40 %; comisión de éxito del 9 % aparte del TER 1,14 %.
- **`IE00B4NF1620` Nomura Japan Strategic Value Fund Class A EUR Hedged** — Value japonés cubierto a euros: 5A +19,0 % y 3A +19,6 % anualizados. El bache 2026 está escrito: quintil 5 en YTD; la tesis es de ciclo, no de racha.
- **`IE00B88WFS66` Federated Hermes Asia ex-Japan Equity Fund Class R EUR Acc** — Asia ex-Japón con 3A +18,3 % anualizados y rating 5★ en el snapshot. La clase F (TER 0,83 %) exige 100.000 € de mínimo; se paga ≈45 €/año de acceso por la R.
- **`ES0173320039` Renta 4 Latinoamérica R FI** — Latinoamérica pura (Brasil 43 %, México 28 %) con 5A +13,4 % anualizados y rating 5★. Éxito del 9 % en años buenos; mínimo de 10 €.
- **`IE00BDR0JY05` Ashoka WhiteOak India Opportunities Fund Class D EUR Acc** — India por convicción activa (97 % India). Volatilidad 1A del 19,8 % y drawdown −29 % asumidos: es la línea de riesgo alto del bloque.
- **`LU1835818565` Goldman Sachs AAA ABS - X Cap EUR** — ABS AAA euro con duración ~0 al 0,80 %: colchón del bloque activo. Caro para lo que hace (SRRI 1); es el precio de salir del circulante sin duración.
- **`FR001400CFA4` Ostrum Credit Ultra Short Plus R/C (EUR)** — Crédito ultra corto activo: TER 0,30 % + 20 % de éxito sobre el exceso. Si cumple su objetivo (~€STR +0,5 %), el éxito muerde una parte relevante del exceso.

La ficha completa de cada uno, con pegas y fuentes, está en [`fondos-revisados.md`](fondos-revisados.md).

## 7. Ejecución

Dinero nuevo: una orden de suscripción por fondo, sin reembolso previo, ordenada de mayor lag de suscripción a menor para que ninguna línea quede colgada. Todos los mínimos iniciales están cubiertos por el importe de la línea (el mayor del encargo es 1.000 €, en líneas de ≥2.000 €).

| # | Fondo | ISIN | € | Mínimo | Corte | Suscripción |
| --: | --- | --- | --: | --- | --- | --- |
| 1 | Nomura Japan Strategic Value Fund Class A EUR Hedged | `IE00B4NF1620` | 9.000 | 0,00 € | 12:00 | Suscribir 9.000 € |
| 2 | Robeco BP US Large Cap Equities D € | `LU0474363974` | 14.000 | 1,00 € | 14:00 | Suscribir 14.000 € |
| 3 | Goldman Sachs AAA ABS - X Cap EUR | `LU1835818565` | 11.000 | 0,00 € | 14:00 | Suscribir 11.000 € |
| 4 | Federated Hermes Asia ex-Japan Equity Fund Class R EUR Acc | `IE00B88WFS66` | 9.000 | 0,00 € | 09:00 | Suscribir 9.000 € |
| 5 | Ashoka WhiteOak India Opportunities Fund Class D EUR Acc | `IE00BDR0JY05` | 7.000 | 1 participación | 10:00 | Suscribir 7.000 € |
| 6 | Ostrum Credit Ultra Short Plus R/C (EUR) | `FR001400CFA4` | 7.000 | 0,00 € | 10:00 | Suscribir 7.000 € |
| 7 | Cobas LUX SICAV - Palm Harbour Global Value Fund-F Acc EUR | `LU1935059029` | 22.000 | 1,00 € | 14:00 | Suscribir 22.000 € |
| 8 | Muza FI | `ES0184893008` | 12.000 | 0,001 participaciones | 12:00 | Suscribir 12.000 € |
| 9 | Renta 4 Latinoamérica R FI | `ES0173320039` | 9.000 | 10,00 € | 12:00 | Suscribir 9.000 € |

## 8. Qué se descarta

| Candidato | Razón con número | Solución adoptada |
| --- | --- | --- |
| Goldman Sachs US Enhanced Core Equity (LU0082087940) | el MCP publica TER 1,60 % (el snapshot decía 0,70 %) y su descripción es «mejorar el S&P 500 manteniendo composición próxima al índice»: beta mejorada al precio de activo caro | la sustituye Robeco BP US Large Cap (1,46 %), value de proceso propio con active share alto |
| Avantage Pure Equity (ES0112101003) | el MCP lo marca «Fondo Cerrado» —no admite dinero nuevo— | el hueco se cierra subiendo Palm Harbour a 22.000 € |
| MUTUAFONDO RV INT (ES0165194038) | TER 0,91 % pero su cartera es mayoritariamente ETF indexados: beta disfrazada de activo, más cara que el índice | descartado por el criterio de convicción activa |
| Federated Hermes Asia ex-Japan clase F (IE00B8H6X308) | TER 0,83 % pero mínimo inicial de 100.000 € en el MCP; la línea es de 9.000 € | se toma la clase R (1,59 %) y se paga el acceso |

## 9. Verificación, revisión y lo que queda abierto

**Verificación.** Los 9 ISIN se comprobaron en el catálogo MCP de MyInvestor el 20/11/2026 (`distributing=0`, mínimos, TER, avisos de soft close); no hizo falta verificación web adicional: los campos decisivos estaban en la ficha del repo o en el MCP. El recuento del encargo está en [`validacion.md`](validacion.md).

**Revisión.** Revisar el 30/11/2027 y cada 12 meses: (a) TER real en pantalla frente al MCP; (b) comisiones de éxito efectivas de las líneas que las llevan; (c) clases hermanas que abaraten una línea sin cambiar de fondo —cambiar de clase de un fondo ya comprado es un reembolso—; (d) que ningún fondo pase a distribuir o a soft close; (e) evidencia de cada gestor activo contra su índice neto de TER a tres años.

**Sin decidir:** horizonte real, colchón fuera de la cartera, aportaciones periódicas y fecha de ejecución. Ninguna orden se lanza hasta la revisión del titular.

---
title: "C4 — Defensiva con alternativos (100.000 €)"
date: 2026-11-20
type: portfolio-proposal
category: finance
tags: [defensiva, alternativos, low-vol, cat-bonds, market-neutral, monetario]
status: propuesta
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/validacion.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/fondos-revisados.md
---

# C4 — Defensiva con alternativos

> **Qué es.** 14 fondos, 100.000 € exactos, **34,91 % de renta variable real** (look-through) y **727,70 €/año (0,7277 %)**. Caída de manual **-15,34 % = 15.343 €** y **≈4,09 % esperado** con los supuestos de §4.
>
> **Criterio.** ≈35 % de RV en estrategias de baja volatilidad y real assets, y el resto repartido entre mixtos conservadores, retorno absoluto, cat bonds, commodities y liquidez.
>
> **Método y límite.** Fichas del repo (snapshot de la app del 19/11/2026) y verificación de los 14 ISIN en el catálogo MCP de MyInvestor el 20/11/2026 (TER, `distributing`, mínimos, avisos). **No es asesoramiento financiero**: la decisión y la ejecución son del titular.

---

## 1. Mandato

| Lo que pide el encargo | Cómo se cumple | Qué cuesta |
| --- | --- | --- |
| 100.000 € | 14 líneas que suman exactamente 100.000 € | Nada |
| Cinco carteras sin repetir fondo entre ellas | 50 ISIN distintos en el encargo, comprobados por ISIN, nombre normalizado y clase hermana (§ de [`validacion.md`](validacion.md)) | Ninguna línea se abarata con un fondo ya usado en otra de las cinco |
| Cartera diversificada | ≈35 % de RV en estrategias de baja volatilidad y real assets, y el resto repartido entre mixtos conservadores, retorno absoluto, cat bonds, commodities y liquidez | Ver §4 |
| Solo fondos del listado `finance/fondos-myinvestor/` | Los 14 ISIN están en el listado (1.980 fichas) | Sin ETF ni acciones: traspaso sin peaje fiscal |
| Sin distribución de dividendos | 14/14 clases de acumulación (`distributing=0` en el MCP) | Nada |

**Supuestos escritos, no reglas heredadas:** horizonte de 15 años o más (en C4, de 7 años o más), colchón de 6-12 meses fuera de la cartera, sin aportaciones modeladas. **No se heredó ninguna lista negra de carteras anteriores**: la no-repetición vale solo entre estas cinco, y no se aplicó ningún veto más allá del encargo.

## 2. Cartera

| # | Rol | Fondo | ISIN | € | % | TER | €/año | Éxito | RV/RF | Mínimo (MCP) | Corte |
| --: | --- | --- | --- | --: | --: | --: | --: | --: | --- | --- | --- | |
| 1 | RV defensiva (low-vol, real assets) | Robeco QI European Conservative Equities D € | `LU0339661307` | 15.000 | 15 % | 1,01 % | 151,50 | — | RV 99,91 % | 1,00 € | 14:00 |
| 2 | RV defensiva (low-vol, real assets) | iShares Developed Real Estate Index Fund (IE) D Acc EUR | `IE00BDRK7P73` | 9.000 | 9 % | 0,17 % | 15,30 | — | RV 98,94 % | 1,00 € | 12:00 |
| 3 | RV defensiva (low-vol, real assets) | First Sentier Global Listed Infrastructure Fund Class I (Acc) EUR | `IE00BYSJTY39` | 8.000 | 8 % | 1,59 % | 127,20 | — | RV 99,38 % | 1,00 € | 10:00 |
| 4 | Mixtos y retorno absoluto | Acacia Renta Dinámica I FI | `ES0157935026` | 9.000 | 9 % | 0,70 % | 63,00 | — | RV 2,23 % | 1.000,00 € | 10:00 |
| 5 | Mixtos y retorno absoluto | Gesem Moderado Flexible FI | `ES0142046020` | 6.000 | 6 % | 0,60 % | 36,00 | 5,00 % | RV 10,87 % | 1,00 € | 12:00 |
| 6 | Mixtos y retorno absoluto | Attitude Opportunities FI | `ES0111192003` | 5.000 | 5 % | 1,52 % | 76,00 | 9,00 % | RV 40,04 % | 100,00 € | 10:00 |
| 7 | Liquidez y RF de duración corta | AXA Trésor Court Terme C | `FR0000447823` | 8.000 | 8 % | 0,05 % | 4,00 | — | otros | 0,00 € | 10:00 |
| 8 | Liquidez y RF de duración corta | DWS Floating Rate Notes LC | `LU0034353002` | 8.000 | 8 % | 0,25 % | 20,00 | — | RF 88,51 % | 1,00 € | 12:00 |
| 9 | Liquidez y RF de duración corta | Vanguard Euro Government Bond Index Fund EUR Acc (nuevo tras soft close del Investor) | `IE0007472990` | 8.000 | 8 % | 0,12 % | 9,60 | — | RF 100,00 % | 1,00 € | 12:00 |
| 10 | Mixtos y retorno absoluto | Renta 4 Valor Relativo R FI | `ES0128522002` | 8.000 | 8 % | 0,97 % | 77,60 | 9,00 % | RF 99,84 % | 10,00 € | 12:00 |
| 11 | Mixtos y retorno absoluto | Renta 4 Pegasus R FI | `ES0173321003` | 5.000 | 5 % | 0,99 % | 49,50 | 9,00 % | RF 95,17 % | 10,00 € | 12:00 |
| 12 | Alternativos descorrelacionados | Candriam Index Arbitrage Classique en EUR | `FR0010016477` | 4.000 | 4 % | 0,40 % | 16,00 | 20,00 % | RV 4,82 % | 1,00 € | 10:00 |
| 13 | Alternativos descorrelacionados | Fermat UCITS Cat Bond Fund Ordinary USD Acc | `IE000SV333V4` | 5.000 | 5 % | 1,18 % | 59,00 | — | RF 93,91 % | 1,00 € | 10:00 |
| 14 | Alternativos descorrelacionados | GSQuartix Modified Strategy on the Bloomberg Commodity Index TR A EUR | `LU0397155978` | 2.000 | 2 % | 1,15 % | 23,00 | — | otros | 1.000,00 € | 10:00 |
| | **Total** | **14 fondos** | | **100.000** | **100 %** | **0,7277 %** | **727,70** | | | | |

## 3. Bloques por rol

| Bloque | € | % del total | TER medio | €/año |
| --- | --: | --: | --: | --: |
| RV defensiva (low-vol, real assets) | 32.000 | 32,00 % | 0,9187 % | 294,00 |
| Mixtos y retorno absoluto | 33.000 | 33,00 % | 0,9155 % | 302,10 |
| Liquidez y RF de duración corta | 24.000 | 24,00 % | 0,1400 % | 33,60 |
| Alternativos descorrelacionados | 11.000 | 11,00 % | 0,8909 % | 98,00 |

## 4. Métricas

| Métrica | Valor | Cómo se calcula |
| --- | --- | --- |
| RV *look-through* | 34,91 % | Σ importe × RV declarada (MCP 20/11) |
| Renta fija | 46,03 % | Σ importe × RF declarada (MCP 20/11) |
| Liquidez | 16,14 % | Σ importe × liquidez declarada |
| Caída de manual | -15,34 % = 15.343 € | −(40 % × RV + 3 % × RF) |
| Coste anual | 727,70 € = 0,7277 % | Σ importe × TER del MCP |
| Esperanza central | 4,09 % | Σ importe × retorno esperado por sleeve |
| Escenario pesimista | 2,09 % | RV −2,5 pp de retorno esperado |
| Escenario favorable | 5,39 % | RV +1,5 pp de retorno esperado |
| Indexado | 23 % aproximado del importe en réplica de índice | gestión indexada declarada o índice nombrado en la ficha/MCP |

**Supuestos de la esperanza** (estimación del agente, no dato de mercado): RV desarrollada 6,7 %, emergentes/Asia 7,5 %, crédito y agregado 3,0 %, liquidez 2,3 %. La esperanza la decide el % de RV, no la selección de fondos.

**Las comisiones de éxito no están en el coste anual.** Donde existen se publican en la tabla (§2); en un año bueno añaden hasta ≈2.720 € sobre las líneas que las llevan si todas superan su objetivo, y menos o cero en un año plano.

## 5. Geografía por *look-through*

| Región | € de RV | % de la RV con desglose |
| --- | --: | --: |
| Estados Unidos | 10.764 | 33,80 % |
| Reino Unido | 2.723 | 8,55 % |
| Suiza | 2.503 | 7,86 % |
| Francia | 1.853 | 5,82 % |
| Suecia | 1.723 | 5,41 % |
| Alemania | 1.334 | 4,19 % |
| Países Bajos | 1.289 | 4,05 % |
| Japón | 730 | 2,29 % |
| Australia | 499 | 1,57 % |
| México | 398 | 1,25 % |
| Canadá | 326 | 1,02 % |
| Singapur | 303 | 0,95 % |

Base con desglose: 31.842 € de RV. Las líneas sin desglose regional no entran en la tabla; cálculo derivado del top de países del MCP, no un dato de la gestora.

## 6. Razón fondo a fondo

- **`LU0339661307` Robeco QI European Conservative Equities D €** — Low-vol cuantitativo europeo (Robeco QI): reduce volatilidad y añade value+momentum. 3A +15,8 % anualizados con vol 7,7 %; TER 1,01 % (las clases I/C hermanas, a ~0,6 %, no están en la plataforma).
- **`IE00BDRK7P73` iShares Developed Real Estate Index Fund (IE) D Acc EUR** — REITs desarrollados indexados al 0,17 %: real assets sin gestor. 2022 −20,1 %: el tilt inmobiliario paga en subidas de tipos.
- **`IE00BYSJTY39` First Sentier Global Listed Infrastructure Fund Class I (Acc) EUR** — Infraestructura activa (servicios públicos 44 %, industria 37 %): regulada, semifensiva. 3A +13,0 % anualizados; TER 1,59 %.
- **`ES0157935026` Acacia Renta Dinámica I FI** — Mixto conservador español 2/69 con 29 % de liquidez: 3A +4,3 % anualizados con vol 1,4 %. TER no publicado en el MCP (snapshot 0,70 %).
- **`ES0142046020` Gesem Moderado Flexible FI** — Mixto 11/78 con crédito corporativo (59 %): 3A +4,5 % anualizados, éxito del 5 %. Patrimonio pequeño (6,6 M€): riesgo de fusión del compartimento.
- **`ES0111192003` Attitude Opportunities FI** — Retorno absoluto 40/51 con forwards (22 % del sector riesgo): descorrelación declarada. Éxito del 9 %; TER del MCP 1,52 %.
- **`FR0000447823` AXA Trésor Court Terme C** — Monetario que sigue el €STR al 0,05 %: el colchón del bloque. Gobierno relacionado 48 %, sin RV.
- **`LU0034353002` DWS Floating Rate Notes LC** — Flotantes euro al 0,25 %: el cupón se rearma con los tipos, duración ~0. 3A +3,3 % anualizados con vol 0,4 %.
- **`IE0007472990` Vanguard Euro Government Bond Index Fund EUR Acc (nuevo tras soft close del Investor)** — Soberano euro indexado al 0,12 %, la clase nueva del fondo tras el soft close del Investor (el MCP lo avisa literalmente). Duración larga: 2024 −18,3 %.
- **`ES0128522002` Renta 4 Valor Relativo R FI** — Retorno absoluto de crédito euro (España 33 %, Italia 27 %): 5A +1,2 % anualizados, éxito del 9 %. TER 0,97 %.
- **`ES0173321003` Renta 4 Pegasus R FI** — Retorno absoluto de crédito euro, gemelo de criterio del anterior: 3A +3,4 % anualizados, éxito del 9 %. TER 0,99 %.
- **`FR0010016477` Candriam Index Arbitrage Classique en EUR** — Market neutral de arbitraje de índices: 93 % de caja más derivados, objetivo de batir al €STR con vol <1 %. Éxito del 20 %: el coste real supera el TER 0,40 %.
- **`IE000SV333V4` Fermat UCITS Cat Bond Fund Ordinary USD Acc** — Cat bonds USD sin cubrir (Fermat): +10,8 % a 1 año. Clase de 2024: sin 3A/5A ni ciclo completo; el riesgo de catástrofe es descorrelacionado, no ausente.
- **`LU0397155978` GSQuartix Modified Strategy on the Bloomberg Commodity Index TR A EUR** — Commodities mecanizadas sobre el Bloomberg Commodity TR: 5A +7,2 % anualizados con vol 12-16 %. La fórmula de caída no captura esta exposición; se documenta aparte.

La ficha completa de cada uno, con pegas y fuentes, está en [`fondos-revisados.md`](fondos-revisados.md).

## 7. Ejecución

Dinero nuevo: una orden de suscripción por fondo, sin reembolso previo, ordenada de mayor lag de suscripción a menor para que ninguna línea quede colgada. Todos los mínimos iniciales están cubiertos por el importe de la línea (el mayor del encargo es 1.000 €, en líneas de ≥2.000 €).

| # | Fondo | ISIN | € | Mínimo | Corte | Suscripción |
| --: | --- | --- | --: | --- | --- | --- |
| 1 | Fermat UCITS Cat Bond Fund Ordinary USD Acc | `IE000SV333V4` | 5.000 | 1,00 € | 10:00 | Suscribir 5.000 € |
| 2 | iShares Developed Real Estate Index Fund (IE) D Acc EUR | `IE00BDRK7P73` | 9.000 | 1,00 € | 12:00 | Suscribir 9.000 € |
| 3 | First Sentier Global Listed Infrastructure Fund Class I (Acc) EUR | `IE00BYSJTY39` | 8.000 | 1,00 € | 10:00 | Suscribir 8.000 € |
| 4 | GSQuartix Modified Strategy on the Bloomberg Commodity Index TR A EUR | `LU0397155978` | 2.000 | 1.000,00 € | 10:00 | Suscribir 2.000 € |
| 5 | Robeco QI European Conservative Equities D € | `LU0339661307` | 15.000 | 1,00 € | 14:00 | Suscribir 15.000 € |
| 6 | DWS Floating Rate Notes LC | `LU0034353002` | 8.000 | 1,00 € | 12:00 | Suscribir 8.000 € |
| 7 | Candriam Index Arbitrage Classique en EUR | `FR0010016477` | 4.000 | 1,00 € | 10:00 | Suscribir 4.000 € |
| 8 | Vanguard Euro Government Bond Index Fund EUR Acc (nuevo tras soft close del Investor) | `IE0007472990` | 8.000 | 1,00 € | 12:00 | Suscribir 8.000 € |
| 9 | Acacia Renta Dinámica I FI | `ES0157935026` | 9.000 | 1.000,00 € | 10:00 | Suscribir 9.000 € |
| 10 | AXA Trésor Court Terme C | `FR0000447823` | 8.000 | 0,00 € | 10:00 | Suscribir 8.000 € |
| 11 | Renta 4 Valor Relativo R FI | `ES0128522002` | 8.000 | 10,00 € | 12:00 | Suscribir 8.000 € |
| 12 | Gesem Moderado Flexible FI | `ES0142046020` | 6.000 | 1,00 € | 12:00 | Suscribir 6.000 € |
| 13 | Attitude Opportunities FI | `ES0111192003` | 5.000 | 100,00 € | 10:00 | Suscribir 5.000 € |
| 14 | Renta 4 Pegasus R FI | `ES0173321003` | 5.000 | 10,00 € | 12:00 | Suscribir 5.000 € |

## 8. Qué se descarta

| Candidato | Razón con número | Solución adoptada |
| --- | --- | --- |
| Vanguard Euro Government Bond Investor (IE0007472115) | el MCP lo marca en soft close y señala la clase nueva IE0007472990, idéntica en comisiones | se usa la clase nueva |
| MontLake DUNN WMA (gestión de futuros) | fondo válido pero ya elegido en la cartera hermana `cartera-ai-fondos-2000-lista`; aquí no hay lista negra, pero se eligen alternativas del propio catálogo para no clonar el diseño anterior | lo cubren Candriam Index Arbitrage y GSQuartix |
| DIP Paradigma Conservative (LU0804746799) | por debajo de su categoría en 4 de los 5 últimos años naturales | descartado; entra Acacia Renta Dinámica I (+4,3 % anual a 3A) |

## 9. Verificación, revisión y lo que queda abierto

**Verificación.** Los 14 ISIN se comprobaron en el catálogo MCP de MyInvestor el 20/11/2026 (`distributing=0`, mínimos, TER, avisos de soft close); no hizo falta verificación web adicional: los campos decisivos estaban en la ficha del repo o en el MCP. El recuento del encargo está en [`validacion.md`](validacion.md).

**Revisión.** Revisar el 30/11/2027 y cada 12 meses: (a) TER real en pantalla frente al MCP; (b) comisiones de éxito efectivas de las líneas que las llevan; (c) clases hermanas que abaraten una línea sin cambiar de fondo —cambiar de clase de un fondo ya comprado es un reembolso—; (d) que ningún fondo pase a distribuir o a soft close; (e) evidencia de cada gestor activo contra su índice neto de TER a tres años.

**Sin decidir:** horizonte real, colchón fuera de la cartera, aportaciones periódicas y fecha de ejecución. Ninguna orden se lanza hasta la revisión del titular.

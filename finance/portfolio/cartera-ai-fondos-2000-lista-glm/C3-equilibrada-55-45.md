---
title: "C3 — Equilibrada 55/45 (100.000 €)"
date: 2026-11-20
type: portfolio-proposal
category: finance
tags: [equilibrada, mixto, 55-45, fondo-de-fondos, renta-fija]
status: propuesta
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/validacion.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/fondos-revisados.md
---

# C3 — Equilibrada 55/45

> **Qué es.** 11 fondos, 100.000 € exactos, **54,38 % de renta variable real** (look-through) y **425,00 €/año (0,4250 %)**. Caída de manual **-22,97 % = 22.973 €** y **≈4,96 % esperado** con los supuestos de §4.
>
> **Criterio.** ≈55 % de renta variable look-through mezclando núcleo indexado, mixtos activos y renta fija, sin decidir entre todo bolsa y todo bonos.
>
> **Método y límite.** Fichas del repo (snapshot de la app del 19/11/2026) y verificación de los 11 ISIN en el catálogo MCP de MyInvestor el 20/11/2026 (TER, `distributing`, mínimos, avisos). **No es asesoramiento financiero**: la decisión y la ejecución son del titular.

---

## 1. Mandato

| Lo que pide el encargo | Cómo se cumple | Qué cuesta |
| --- | --- | --- |
| 100.000 € | 11 líneas que suman exactamente 100.000 € | Nada |
| Cinco carteras sin repetir fondo entre ellas | 50 ISIN distintos en el encargo, comprobados por ISIN, nombre normalizado y clase hermana (§ de [`validacion.md`](validacion.md)) | Ninguna línea se abarata con un fondo ya usado en otra de las cinco |
| Cartera diversificada | ≈55 % de renta variable look-through mezclando núcleo indexado, mixtos activos y renta fija, sin decidir entre todo bolsa y todo bonos | Ver §4 |
| Solo fondos del listado `finance/fondos-myinvestor/` | Los 11 ISIN están en el listado (1.980 fichas) | Sin ETF ni acciones: traspaso sin peaje fiscal |
| Sin distribución de dividendos | 11/11 clases de acumulación (`distributing=0` en el MCP) | Nada |

**Supuestos escritos, no reglas heredadas:** horizonte de 15 años o más (en C4, de 7 años o más), colchón de 6-12 meses fuera de la cartera, sin aportaciones modeladas. **No se heredó ninguna lista negra de carteras anteriores**: la no-repetición vale solo entre estas cinco, y no se aplicó ningún veto más allá del encargo.

## 2. Cartera

| # | Rol | Fondo | ISIN | € | % | TER | €/año | Éxito | RV/RF | Mínimo (MCP) | Corte |
| --: | --- | --- | --- | --: | --: | --: | --: | --: | --- | --- | --- | |
| 1 | Núcleo indexado de RV | Fidelity MSCI World Index Fund EUR P Acc (Hedged) | `IE00BYX5P602` | 22.000 | 22 % | 0,17 % | 37,40 | — | RV 98,98 % | 1,00 € | 16:00 |
| 2 | Núcleo indexado de RV | Amundi Index Solutions - Amundi Core MSCI Emerging Markets AE-C | `LU0996177134` | 8.000 | 8 % | 0,45 % | 36,00 | — | RV 100,00 % | 0,00 participaciones | 12:00 |
| 3 | Mixtos y value activo | WAM High Conviction A FI | `ES0134751009` | 12.000 | 12 % | 0,50 % | 60,00 | — | RV 52,72 % | 1,00 € | 12:00 |
| 4 | Mixtos y value activo | Gestión Boutique VI Baelo Patrimonio FI | `ES0110407097` | 11.000 | 11 % | 0,64 % | 70,40 | — | RV 60,76 % | 1,00 € | 12:00 |
| 5 | Mixtos y value activo | Gestión Boutique VIII / Inver Value Global Fund FI | `ES0131445142` | 11.000 | 11 % | 1,14 % | 125,40 | 5,00 % | RV 71,71 % | 10,00 € | 12:00 |
| 6 | Mixtos y value activo | Indexa RV mixta internacional 75 FI | `ES0148181003` | 5.000 | 5 % | 0,64 % | 32,00 | — | RV 74,17 % | 10,00 € | 12:00 |
| 7 | Renta fija y colchón | iShares Euro Government Bond Index Fund (IE) D Acc EUR | `IE00BD0NC037` | 9.000 | 9 % | 0,10 % | 9,00 | — | RF 99,92 % | 1,00 € | 09:00 |
| 8 | Renta fija y colchón | iShares US Corporate Bond Index Fund (IE) D Acc EUR | `IE00BDZRPS94` | 9.000 | 9 % | 0,12 % | 10,80 | — | RF 99,77 % | 1,00 € | 09:00 |
| 9 | Renta fija y colchón | CBNK Renta Fija CP Base FI | `ES0126551037` | 6.000 | 6 % | 0,18 % | 10,80 | 9,00 % | RF 71,90 % | 1,00 € | 14:00 |
| 10 | Renta fija y colchón | iShares Euro Government Inflation-Linked Bond Index Fund (IE) D Acc EUR | `IE00BD0NC144` | 5.000 | 5 % | 0,10 % | 5,00 | — | RF 100,00 % | 1,00 € | 09:00 |
| 11 | Renta fija y colchón | GAM Star - GAM Swiss Re Cat Bond Class Ordinary EUR Accumulation Hedged | `IE00B3Q8M574` | 2.000 | 2 % | 1,41 % | 28,20 | 10,00 % | RF 87,78 % | 1,00 € | 12:00 |
| | **Total** | **11 fondos** | | **100.000** | **100 %** | **0,4250 %** | **425,00** | | | | |

## 3. Bloques por rol

| Bloque | € | % del total | TER medio | €/año |
| --- | --: | --: | --: | --: |
| Núcleo indexado de RV | 30.000 | 30,00 % | 0,2447 % | 73,40 |
| Mixtos y value activo | 39.000 | 39,00 % | 0,7379 % | 287,80 |
| Renta fija y colchón | 31.000 | 31,00 % | 0,2058 % | 63,80 |

## 4. Métricas

| Métrica | Valor | Cómo se calcula |
| --- | --- | --- |
| RV *look-through* | 54,38 % | Σ importe × RV declarada (MCP 20/11) |
| Renta fija | 40,66 % | Σ importe × RF declarada (MCP 20/11) |
| Liquidez | 4,05 % | Σ importe × liquidez declarada |
| Caída de manual | -22,97 % = 22.973 € | −(40 % × RV + 3 % × RF) |
| Coste anual | 425,00 € = 0,4250 % | Σ importe × TER del MCP |
| Esperanza central | 4,96 % | Σ importe × retorno esperado por sleeve |
| Escenario pesimista | 2,96 % | RV −2,5 pp de retorno esperado |
| Escenario favorable | 6,26 % | RV +1,5 pp de retorno esperado |
| Indexado | 58 % aproximado del importe en réplica de índice | gestión indexada declarada o índice nombrado en la ficha/MCP |

**Supuestos de la esperanza** (estimación del agente, no dato de mercado): RV desarrollada 6,7 %, emergentes/Asia 7,5 %, crédito y agregado 3,0 %, liquidez 2,3 %. La esperanza la decide el % de RV, no la selección de fondos.

**Las comisiones de éxito no están en el coste anual.** Donde existen se publican en la tabla (§2); en un año bueno añaden hasta ≈1.290 € sobre las líneas que las llevan si todas superan su objetivo, y menos o cero en un año plano.

## 5. Geografía por *look-through*

| Región | € de RV | % de la RV con desglose |
| --- | --: | --: |
| Estados Unidos | 23.837 | 43,83 % |
| Alemania | 2.961 | 5,45 % |
| Taiwán | 2.176 | 4,00 % |
| Canadá | 2.163 | 3,98 % |
| España | 1.930 | 3,55 % |
| China | 1.624 | 2,99 % |
| Japón | 1.505 | 2,77 % |
| Corea del Sur | 1.424 | 2,62 % |
| Italia | 1.402 | 2,58 % |
| India | 1.032 | 1,90 % |
| Suiza | 942 | 1,73 % |
| Francia | 925 | 1,70 % |

Base con desglose: 54.382 € de RV. Las líneas sin desglose regional no entran en la tabla; cálculo derivado del top de países del MCP, no un dato de la gestora.

## 6. Razón fondo a fondo

- **`IE00BYX5P602` Fidelity MSCI World Index Fund EUR P Acc (Hedged)** — MSCI World cubierto a euros al 0,17 % (TER del MCP; el snapshot de la ficha decía 0,20 %): el World más barato disponible del listado sin repetir el de C1.
- **`LU0996177134` Amundi Index Solutions - Amundi Core MSCI Emerging Markets AE-C** — MSCI EM indexado al 0,45 %, el más caro de su lote; se toma porque el más barato (iShares clase S) no está en el listado. 3A +16,7 % anualizados.
- **`ES0134751009` WAM High Conviction A FI** — Mixto de convicción 53/29 con ~15 posiciones de RV y TER 0,50 %: la pieza activa del bloque equilibrado. Historial desde 2022, sin ciclo completo.
- **`ES0110407097` Gestión Boutique VI Baelo Patrimonio FI** — Mixto 61/37 de Antonio Rodríguez Rico («fondo de autor»): 3A +10,3 % anualizados. Riesgo de persona clave: si cambia el gestor, el fondo cambia.
- **`ES0131445142` Gestión Boutique VIII / Inver Value Global Fund FI** — Value global 72/26 del mismo Andbank: 3A +13,0 % anualizados, éxito del 5 %. TER no publicado en el MCP; snapshot 1,14 %.
- **`ES0148181003` Indexa RV mixta internacional 75 FI** — Fondo de fondos indexado 74/24 al 0,64 % (gestión delegada de Indexa en Renta 4): la pieza pasiva de bajo mantenimiento del bloque. Su composición subyacente no es auditable en las fuentes.
- **`IE00BD0NC037` iShares Euro Government Bond Index Fund (IE) D Acc EUR** — Soberano euro indexado al 0,10 %: Francia 25 %, Italia 22 %, Alemania 20 %, España 14 %. Duración larga: 2024 −17,9 %.
- **`IE00BDZRPS94` iShares US Corporate Bond Index Fund (IE) D Acc EUR** — Crédito corporativo USD sin cubrir al 0,12 %. En 2025 la clase cayó −4,9 % en EUR pese al año positivo en USD: la divisa es parte del riesgo.
- **`ES0126551037` CBNK Renta Fija CP Base FI** — Corto plazo euro al 0,18 % + 9 % de éxito. Puede llegar al 49 % en baja calidad: más riesgo del que sugiere el SRRI 2.
- **`IE00BD0NC144` iShares Euro Government Inflation-Linked Bond Index Fund (IE) D Acc EUR** — Ligada a inflación euro indexada (vía swap) al 0,10 %. Duración efectiva ~7 años: no es colchón, es cobertura de inflación con volatilidad.
- **`IE00B3Q8M574` GAM Star - GAM Swiss Re Cat Bond Class Ordinary EUR Accumulation Hedged** — Cat bonds cubiertos a euros (Swiss Re): 3A +9,1 % anualizados, éxito del 10 %. Lag de reembolso de 10 días: no es liquidez de emergencia.

La ficha completa de cada uno, con pegas y fuentes, está en [`fondos-revisados.md`](fondos-revisados.md).

## 7. Ejecución

Dinero nuevo: una orden de suscripción por fondo, sin reembolso previo, ordenada de mayor lag de suscripción a menor para que ninguna línea quede colgada. Todos los mínimos iniciales están cubiertos por el importe de la línea (el mayor del encargo es 1.000 €, en líneas de ≥2.000 €).

| # | Fondo | ISIN | € | Mínimo | Corte | Suscripción |
| --: | --- | --- | --: | --- | --- | --- |
| 1 | GAM Star - GAM Swiss Re Cat Bond Class Ordinary EUR Accumulation Hedged | `IE00B3Q8M574` | 2.000 | 1,00 € | 12:00 | Suscribir 2.000 € |
| 2 | Amundi Index Solutions - Amundi Core MSCI Emerging Markets AE-C | `LU0996177134` | 8.000 | 0,00 participaciones | 12:00 | Suscribir 8.000 € |
| 3 | iShares Euro Government Bond Index Fund (IE) D Acc EUR | `IE00BD0NC037` | 9.000 | 1,00 € | 09:00 | Suscribir 9.000 € |
| 4 | iShares US Corporate Bond Index Fund (IE) D Acc EUR | `IE00BDZRPS94` | 9.000 | 1,00 € | 09:00 | Suscribir 9.000 € |
| 5 | iShares Euro Government Inflation-Linked Bond Index Fund (IE) D Acc EUR | `IE00BD0NC144` | 5.000 | 1,00 € | 09:00 | Suscribir 5.000 € |
| 6 | Fidelity MSCI World Index Fund EUR P Acc (Hedged) | `IE00BYX5P602` | 22.000 | 1,00 € | 16:00 | Suscribir 22.000 € |
| 7 | WAM High Conviction A FI | `ES0134751009` | 12.000 | 1,00 € | 12:00 | Suscribir 12.000 € |
| 8 | Gestión Boutique VI Baelo Patrimonio FI | `ES0110407097` | 11.000 | 1,00 € | 12:00 | Suscribir 11.000 € |
| 9 | Gestión Boutique VIII / Inver Value Global Fund FI | `ES0131445142` | 11.000 | 10,00 € | 12:00 | Suscribir 11.000 € |
| 10 | CBNK Renta Fija CP Base FI | `ES0126551037` | 6.000 | 1,00 € | 14:00 | Suscribir 6.000 € |
| 11 | Indexa RV mixta internacional 75 FI | `ES0148181003` | 5.000 | 10,00 € | 12:00 | Suscribir 5.000 € |

## 8. Qué se descarta

| Candidato | Razón con número | Solución adoptada |
| --- | --- | --- |
| Amundi Prime Euro Government Bond (LU2339731064) | TER 0,05 %, el soberano más barato, pero el MCP publica mínimo inicial de 500.000 € | la sustituye iShares Euro Government Bond D (0,10 %) por 10 €/año más sobre 9.000 € |
| iShares Developed World clase S (IE000ZYRH0Q7) | mismo fondo, otra clase; ya es el núcleo de C1 y entre las cinco carteras no se repite fondo | se usa el World cubierto de Fidelity (0,17 %), que además quita el riesgo divisa del bloque |
| Fondo de fondos de distribución y clases Inc | cualquier clase que reparte | regla de acumulación del repositorio; se descartan aunque sean más baratas |

## 9. Verificación, revisión y lo que queda abierto

**Verificación.** Los 11 ISIN se comprobaron en el catálogo MCP de MyInvestor el 20/11/2026 (`distributing=0`, mínimos, TER, avisos de soft close); no hizo falta verificación web adicional: los campos decisivos estaban en la ficha del repo o en el MCP. El recuento del encargo está en [`validacion.md`](validacion.md).

**Revisión.** Revisar el 30/11/2027 y cada 12 meses: (a) TER real en pantalla frente al MCP; (b) comisiones de éxito efectivas de las líneas que las llevan; (c) clases hermanas que abaraten una línea sin cambiar de fondo —cambiar de clase de un fondo ya comprado es un reembolso—; (d) que ningún fondo pase a distribuir o a soft close; (e) evidencia de cada gestor activo contra su índice neto de TER a tres años.

**Sin decidir:** horizonte real, colchón fuera de la cartera, aportaciones periódicas y fecha de ejecución. Ninguna orden se lanza hasta la revisión del titular.

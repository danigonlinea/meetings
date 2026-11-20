---
title: "C5 — Crecimiento con satélites (100.000 €)"
date: 2026-11-20
type: portfolio-proposal
category: finance
tags: [crecimiento, satelites, tecnologia, oro, infraestructura, iberia, asia]
status: propuesta
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/validacion.md
  - finance/portfolio/cartera-ai-fondos-2000-lista-glm/fondos-revisados.md
---

# C5 — Crecimiento con satélites

> **Qué es.** 8 fondos, 100.000 € exactos, **87,64 % de renta variable real** (look-through) y **942,30 €/año (0,9423 %)**. Caída de manual **-35,35 % = 35.350 €** y **≈6,19 % esperado** con los supuestos de §4.
>
> **Criterio.** ≈88 % de RV: un núcleo ACWI barato y seis satélites sectoriales y regionales con volatilidad propia.
>
> **Método y límite.** Fichas del repo (snapshot de la app del 19/11/2026) y verificación de los 8 ISIN en el catálogo MCP de MyInvestor el 20/11/2026 (TER, `distributing`, mínimos, avisos). **No es asesoramiento financiero**: la decisión y la ejecución son del titular.

---

## 1. Mandato

| Lo que pide el encargo | Cómo se cumple | Qué cuesta |
| --- | --- | --- |
| 100.000 € | 8 líneas que suman exactamente 100.000 € | Nada |
| Cinco carteras sin repetir fondo entre ellas | 50 ISIN distintos en el encargo, comprobados por ISIN, nombre normalizado y clase hermana (§ de [`validacion.md`](validacion.md)) | Ninguna línea se abarata con un fondo ya usado en otra de las cinco |
| Cartera diversificada | ≈88 % de RV: un núcleo ACWI barato y seis satélites sectoriales y regionales con volatilidad propia | Ver §4 |
| Solo fondos del listado `finance/fondos-myinvestor/` | Los 8 ISIN están en el listado (1.980 fichas) | Sin ETF ni acciones: traspaso sin peaje fiscal |
| Sin distribución de dividendos | 8/8 clases de acumulación (`distributing=0` en el MCP) | Nada |

**Supuestos escritos, no reglas heredadas:** horizonte de 15 años o más (en C4, de 7 años o más), colchón de 6-12 meses fuera de la cartera, sin aportaciones modeladas. **No se heredó ninguna lista negra de carteras anteriores**: la no-repetición vale solo entre estas cinco, y no se aplicó ningún veto más allá del encargo.

## 2. Cartera

| # | Rol | Fondo | ISIN | € | % | TER | €/año | Éxito | RV/RF | Mínimo (MCP) | Corte |
| --: | --- | --- | --- | --: | --: | --: | --: | --: | --- | --- | --- | |
| 1 | Núcleo indexado (MSCI ACWI) | MyInvestor Mundo Desarrollado y Emergente FI (réplica MSCI ACWI) | `ES0184894006` | 55.000 | 55 % | 0,56 % | 308,00 | — | RV 97,91 % | 1,00 € | 12:00 |
| 2 | Satélites sectoriales y regionales | Polar Capital Global Technology Fund R Acc | `IE00BM95B621` | 7.000 | 7 % | 1,59 % | 111,30 | — | RV 94,48 % | 1,00 € | 14:00 |
| 3 | Satélites sectoriales y regionales | Wellington Global Health Care Equity Fund USD D Acc | `IE00B00LSD17` | 6.000 | 6 % | 1,74 % | 104,40 | — | RV 98,63 % | 0,00 € | 12:00 |
| 4 | Satélites sectoriales y regionales | Morgan Stanley QuantActive Global Infrastructure Fund AH (EUR) | `LU0512092221` | 6.000 | 6 % | 1,51 % | 90,60 | — | RV 98,30 % | 1,00 € | 12:00 |
| 5 | Satélites sectoriales y regionales | BlackRock Global Funds - World Gold Fund A2 EUR Acc | `LU0171305526` | 5.000 | 5 % | 2,08 % | 104,00 | — | RV 96,01 % | 1,00 € | 10:00 |
| 6 | Satélites sectoriales y regionales | Magallanes Value Investors UCITS Iberian Equity R | `LU1330191898` | 5.000 | 5 % | 2,22 % | 111,00 | — | RV 93,09 % | 100,00 € | 14:00 |
| 7 | Satélites sectoriales y regionales | Robeco Asian Stars Equities D € | `LU0591059224` | 6.000 | 6 % | 1,50 % | 90,00 | 15,00 % | RV 98,44 % | 1 participación | 14:00 |
| 8 | Colchón corto plazo | UBS Corto Plazo B FI | `ES0155598032` | 10.000 | 10 % | 0,23 % | 23,00 | — | RF 97,74 % | 1,00 € | 14:00 |
| | **Total** | **8 fondos** | | **100.000** | **100 %** | **0,9423 %** | **942,30** | | | | |

## 3. Bloques por rol

| Bloque | € | % del total | TER medio | €/año |
| --- | --: | --: | --: | --: |
| Núcleo indexado (MSCI ACWI) | 55.000 | 55,00 % | 0,5600 % | 308,00 |
| Satélites sectoriales y regionales | 35.000 | 35,00 % | 1,7466 % | 611,30 |
| Colchón corto plazo | 10.000 | 10,00 % | 0,2300 % | 23,00 |

## 4. Métricas

| Métrica | Valor | Cómo se calcula |
| --- | --- | --- |
| RV *look-through* | 87,64 % | Σ importe × RV declarada (MCP 20/11) |
| Renta fija | 9,77 % | Σ importe × RF declarada (MCP 20/11) |
| Liquidez | 1,26 % | Σ importe × liquidez declarada |
| Caída de manual | -35,35 % = 35.350 € | −(40 % × RV + 3 % × RF) |
| Coste anual | 942,30 € = 0,9423 % | Σ importe × TER del MCP |
| Esperanza central | 6,19 % | Σ importe × retorno esperado por sleeve |
| Escenario pesimista | 4,19 % | RV −2,5 pp de retorno esperado |
| Escenario favorable | 7,49 % | RV +1,5 pp de retorno esperado |
| Indexado | 55 % aproximado del importe en réplica de índice | gestión indexada declarada o índice nombrado en la ficha/MCP |

**Supuestos de la esperanza** (estimación del agente, no dato de mercado): RV desarrollada 6,7 %, emergentes/Asia 7,5 %, crédito y agregado 3,0 %, liquidez 2,3 %. La esperanza la decide el % de RV, no la selección de fondos.

**Las comisiones de éxito no están en el coste anual.** Donde existen se publican en la tabla (§2); en un año bueno añaden hasta ≈900 € sobre las líneas que las llevan si todas superan su objetivo, y menos o cero en un año plano.

## 5. Geografía por *look-through*

| Región | € de RV | % de la RV con desglose |
| --- | --: | --: |
| Estados Unidos | 46.430 | 52,98 % |
| Canadá | 5.481 | 6,25 % |
| Taiwán | 3.800 | 4,34 % |
| España | 3.299 | 3,76 % |
| Reino Unido | 3.218 | 3,67 % |
| Japón | 3.178 | 3,63 % |
| Corea del Sur | 2.073 | 2,36 % |
| China | 1.618 | 1,85 % |
| Suiza | 1.392 | 1,59 % |
| Portugal | 684 | 0,78 % |
| India | 537 | 0,61 % |
| Australia | 533 | 0,61 % |

Base con desglose: 87.641 € de RV. Las líneas sin desglose regional no entran en la tabla; cálculo derivado del top de países del MCP, no un dato de la gestora.

## 6. Razón fondo a fondo

- **`ES0184894006` MyInvestor Mundo Desarrollado y Emergente FI (réplica MSCI ACWI)** — Núcleo único que replica el MSCI ACWI (desarrollados + emergentes) al 0,56 %: 62 % EE. UU., tecnología 32 %. Es beta pura disfrazada de «activo»; aquí se usa como tal, de forma deliberada.
- **`IE00BM95B621` Polar Capital Global Technology Fund R Acc** — Tecnología global concentrada (87 % sector, 67 % EE. UU.): 3A +36,4 % anualizados con vol 47 % en 1A. El satélite más agresivo de la cartera.
- **`IE00B00LSD17` Wellington Global Health Care Equity Fund USD D Acc** — Salud global activa (98 % sector): 5A +3,4 % anualizados, el bache reciente está escrito. Diversifica del ciclo tecnológico.
- **`LU0512092221` Morgan Stanley QuantActive Global Infrastructure Fund AH (EUR)** — Infraestructura cuantitativa (servicios públicos 51 %, energía 28 %): 3A +9,9 % anualizados. Renombrado QuantActive en 2024; TER 1,51 %.
- **`LU0171305526` BlackRock Global Funds - World Gold Fund A2 EUR Acc** — Oro vía mineras (Canadá 63 %): 3A +40,8 % anualizados con SRRI 6 y vol 50 % en 1A. Satélite de cola de distribución, no núcleo.
- **`LU1330191898` Magallanes Value Investors UCITS Iberian Equity R** — Value ibérico small/mid de Magallanes (España 64 %, Portugal 15 %): 3A +24,1 % anualizados, benchmark 80 % IBEX/20 % PSI. TER 2,22 %: se paga el acceso al mercado local.
- **`LU0591059224` Robeco Asian Stars Equities D €** — Asia ex-Japón contrarian y concentrada (30-50 posiciones): 3A +15,0 % anualizados. Éxito del 15 % sobre la batida al benchmark: el más exigente del lote.
- **`ES0155598032` UBS Corto Plazo B FI** — Corto plazo euro al 0,23 % (bonos corporativos 95 %): el colchón del bloque de crecimiento. 5A +1,8 % anualizados con vol <0,5 %.

La ficha completa de cada uno, con pegas y fuentes, está en [`fondos-revisados.md`](fondos-revisados.md).

## 7. Ejecución

Dinero nuevo: una orden de suscripción por fondo, sin reembolso previo, ordenada de mayor lag de suscripción a menor para que ninguna línea quede colgada. Todos los mínimos iniciales están cubiertos por el importe de la línea (el mayor del encargo es 1.000 €, en líneas de ≥2.000 €).

| # | Fondo | ISIN | € | Mínimo | Corte | Suscripción |
| --: | --- | --- | --: | --- | --- | --- |
| 1 | Morgan Stanley QuantActive Global Infrastructure Fund AH (EUR) | `LU0512092221` | 6.000 | 1,00 € | 12:00 | Suscribir 6.000 € |
| 2 | Robeco Asian Stars Equities D € | `LU0591059224` | 6.000 | 1 participación | 14:00 | Suscribir 6.000 € |
| 3 | BlackRock Global Funds - World Gold Fund A2 EUR Acc | `LU0171305526` | 5.000 | 1,00 € | 10:00 | Suscribir 5.000 € |
| 4 | Magallanes Value Investors UCITS Iberian Equity R | `LU1330191898` | 5.000 | 100,00 € | 14:00 | Suscribir 5.000 € |
| 5 | Polar Capital Global Technology Fund R Acc | `IE00BM95B621` | 7.000 | 1,00 € | 14:00 | Suscribir 7.000 € |
| 6 | Wellington Global Health Care Equity Fund USD D Acc | `IE00B00LSD17` | 6.000 | 0,00 € | 12:00 | Suscribir 6.000 € |
| 7 | MyInvestor Mundo Desarrollado y Emergente FI (réplica MSCI ACWI) | `ES0184894006` | 55.000 | 1,00 € | 12:00 | Suscribir 55.000 € |
| 8 | UBS Corto Plazo B FI | `ES0155598032` | 10.000 | 1,00 € | 14:00 | Suscribir 10.000 € |

## 8. Qué se descarta

| Candidato | Razón con número | Solución adoptada |
| --- | --- | --- |
| Goldman Sachs Global Small Cap CORE (LU0245181838) | la clase aparece como «Close» en el MCP y cuesta 1,92 %: cierre anunciado y precio de activo caro | descartada |
| Goldman Sachs US Small Cap CORE (LU0234682986) | TER 2,00 % en el MCP y clasificado «Índice/pasivo»: small cap indexado al precio máximo | descartado; el tilt de tamaño ya está en C1 y C4 |
| GS Global Future Economic Security (LU2596603436) | TER 0,89 % y tesis interesante, pero `distributing=1` en el MCP: reparte | regla de acumulación: fuera |
| Classes distribution/Inc de cualquier fondo | idem | regla del repositorio |

## 9. Verificación, revisión y lo que queda abierto

**Verificación.** Los 8 ISIN se comprobaron en el catálogo MCP de MyInvestor el 20/11/2026 (`distributing=0`, mínimos, TER, avisos de soft close); no hizo falta verificación web adicional: los campos decisivos estaban en la ficha del repo o en el MCP. El recuento del encargo está en [`validacion.md`](validacion.md).

**Revisión.** Revisar el 30/11/2027 y cada 12 meses: (a) TER real en pantalla frente al MCP; (b) comisiones de éxito efectivas de las líneas que las llevan; (c) clases hermanas que abaraten una línea sin cambiar de fondo —cambiar de clase de un fondo ya comprado es un reembolso—; (d) que ningún fondo pase a distribuir o a soft close; (e) evidencia de cada gestor activo contra su índice neto de TER a tres años.

**Sin decidir:** horizonte real, colchón fuera de la cartera, aportaciones periódicas y fecha de ejecución. Ninguna orden se lanza hasta la revisión del titular.

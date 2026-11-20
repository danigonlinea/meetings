---
title: "C3 — Equilibrada 55/45"
date: 2026-11-20
type: portfolio-proposal
category: finance
tags: [equilibrada, 55-45, mixto-indexado-activo, credito, monetario]
status: propuesta
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/validacion.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/fondos-revisados.md
---

# C3 — Equilibrada 55/45

> **Qué es.** 11 fondos, 100.000 € exactos, **54,75 % de renta variable real** (look-through) y **557,70 €/año (0,5577 %)**. Caída de manual **−23,04 % (23.040 €)** y **≈4,95 % esperado** con los supuestos de §4 (3,58 % pesimista / 5,77 % favorable).
>
> La cobertura del núcleo cambia el perfil: la clase cubierta tuvo peor comportamiento en 2022 que la sin cubrir. Se acepta a cambio de que la parte defensiva y la RV no se muevan en direcciones opuestas por divisa.
>
> **Método y límite.** Fichas del repo (snapshot de la app 19/11/2026 + MCP 20/11/2026) y cuatro verificaciones web puntuales el 20/11/2026, citadas en §9. **No es asesoramiento financiero**: la decisión y la ejecución son del titular.

---

## 1. Mandato

| Lo que pide el encargo | Cómo se cumple | Qué cuesta |
| --- | --- | --- |
| 100.000 € | 11 líneas que suman exactamente 100.000 € | Nada |
| Cinco carteras sin repetir fondo | 52 ISIN distintos, comprobados por ISIN, nombre y clase hermana | Ninguna línea se abarata con un fondo ya usado |
| Cartera diversificada | 54,75 % de RV real (look-through) y 37,97 % de renta fija más liquidez, con el índice cubierto como núcleo y la convicción activa como satélite. Es el punto medio deliberado entre C1 y C5. | Ver §4 |
| Solo fondos del listado | Todos los ISIN están en `finance/fondos-myinvestor/` | Sin ETF ni acciones: traspaso sin peaje fiscal |
| Sin distribución de dividendos | 11/11 clases de acumulación | Nada |

**Supuestos escritos, no reglas heredadas:** horizonte de 15 años o más, colchón de 6-12 meses fuera de la cartera, sin aportaciones modeladas y sin lista negra de carteras anteriores (el mandato solo prohíbe repetir dentro de estas cinco). Si el horizonte es de 5 años, bajar la RV a 40-50 %.

## 2. Cartera

| # | Rol | Fondo | ISIN | € | % | TER | €/año | RV | Mínimo operativo |
| --: | --- | --- | --- | --: | --: | --: | --: | --: | --- |
| 1 | Núcleo MSCI World indexado cubierto EUR | Fidelity MSCI World Index Fund P-ACC-EUR (hedged) | `IE00BYX5P602` | 18.000 | 18,00 % | 0,20 % | 36 | 98,98 % | MCP 20/11: 1.00 EUR |
| 2 | RV Europa baja volatilidad activo | Robeco QI European Conservative Equities D EUR | `LU0339661307` | 8.000 | 8,00 % | 1,01 % | 81 | 99,91 % | web ficha: 0.00 EUR |
| 3 | Emergentes indexado | Vanguard Emerging Markets Stock Index Fund EUR Acc | `IE0031786696` | 8.000 | 8,00 % | 0,23 % | 18 | 100,00 % | MCP 20/11: 1.00 EUR |
| 4 | RV Japón calidad-valor activo | DWS Invest CROCI Japan LCH | `LU1769942233` | 4.000 | 4,00 % | 1,48 % | 59 | 99,70 % | MCP ficha: 0.00 EUR |
| 5 | RV USA dividendo-valor activo | DWS Invest CROCI US Dividends EUR LC | `LU2468423889` | 10.000 | 10,00 % | 1,15 % | 115 | 99,70 % | MCP ficha: 0.00 EUR |
| 6 | RV global sostenible cuantitativo activo | Pictet-Quest Global Sustainable Equities-P EUR | `LU0845340131` | 7.000 | 7,00 % | 1,17 % | 82 | 99,79 % | web ficha: 0.00 EUR |
| 7 | Crédito euro IG indexado | iShares Euro Investment Grade Corporate Bond Index Fund (IE) D … | `IE00BDRK7J14` | 12.000 | 12,00 % | 0,12 % | 14 | 0,00 % | MCP 20/11: 0.00 EUR |
| 8 | Gubernamental euro indexado | State Street EMU Government Bond Index Fund P Acc | `LU0438093006` | 10.000 | 10,00 % | 0,36 % | 36 | 0,00 % | MCP 20/11: 50 EUR |
| 9 | Flotante euro activo | DWS Floating Rate Notes LC | `LU0034353002` | 8.000 | 8,00 % | 0,25 % | 20 | 0,00 % | web ficha: 0.00 EUR |
| 10 | Crédito euro corto plazo activo | ODDO BHF Euro Credit Short Dur CR-EUR | `LU1486845537` | 8.000 | 8,00 % | 0,92 % | 74 | 0,00 % | web ficha: 100 EUR |
| 11 | Monetario EUR | Groupama Entreprises NC | `FR0010288316` | 7.000 | 7,00 % | 0,32 % | 22 | 0,00 % | web ficha: 500 EUR |
| | **Total** | **11 fondos** | | **100.000** | **100 %** | **0,5577 %** | **557,70** | **54,75 %** | |

## 3. Bloques por rol

| Bloque | € | % del total | TER medio | €/año |
| --- | --: | --: | --: | --: |
| Índice | 48.000 | 48,00 % | 0,22 % | 105 |
| Convicción activa de RV | 29.000 | 29,00 % | 1,16 % | 337 |
| Crédito y liquidez | 23.000 | 23,00 % | 0,50 % | 116 |

## 4. Métricas

| Métrica | Valor | Cómo se calcula |
| --- | --- | --- |
| RV *look-through* | 54,75 % | Σ importe × RV declarada en la ficha |
| Renta fija | 37,97 % | Σ importe × RF declarada en la ficha |
| Caída de manual | −23,04 % = 23.040 € | −(40 % × RV + 3 % × RF) |
| Coste anual | 557,70 € = 0,5577 % | Σ importe × TER snapshot |
| Duración estimada de la RF | 4,40 años sobre 12.000 €; 7,00 años sobre 10.000 €; 0,25 años sobre 8.000 €; 1,50 años sobre 8.000 €; 0,00 años sobre 7.000 € | +100 pb cuesta 1.362 € |
| Esperanza central | 4,95 % | Σ importe × retorno esperado por sleeve |
| Escenario pesimista | 3,58 % | RV −2,5 pp de retorno esperado |
| Escenario favorable | 5,77 % | RV +1,5 pp de retorno esperado |
| Indexado | 48,00 % | gestión indexada declarada o índice nombrado en la ficha |

**Supuestos de la esperanza** (estimación del agente, no dato de mercado): RV desarrollada 6,7 %, small caps 7,0 %, emergentes y Asia 7,5 %, Japón 6,7 %, crédito y agregado 2,8-3,2 %, liquidez 2,3 %. La esperanza la decide el % de RV, no la selección de fondos; la prima de convicción está incluida solo donde la ficha declara un sesgo value o de calidad.

## 5. Geografía por *look-through*

| Región declarada | € de RV | % de la RV con desglose |
| --- | --: | --: |
| clasificación FT: Asia desarrollad … | 4.048 | 10,96 % |
| Asia emergente | 2.565 | 6,94 % |
| Latinoamérica | 506 | 1,37 % |
| Oriente Medio | 360 | 0,97 % |

Base con desglose: 36.936 € de RV (67,46 % de la RV total). Los fondos sin desglose regional no entran en la tabla; es un cálculo derivado de las fichas, no un dato de la gestora.

## 6. Razón fondo a fondo

- **`IE00BYX5P602` Fidelity MSCI World Index Fund P-ACC-EUR (hedged)** — Fidelity P hedged; MCP TER 0.17 vs snapshot 0.20; cobertura cambia el perfil (2022 −18.1%). 3A 16,03 % · 5A 8,09 %; TER 0,20 %; MCP 20/11: 1.00 EUR.
- **`LU0339661307` Robeco QI European Conservative Equities D EUR** — Robeco QI European Conservative D. 3A 15,77 % · 5A 8,04 % · vol 7,68 %; TER 1,01 %; web ficha: 0.00 EUR.
- **`IE0031786696` Vanguard Emerging Markets Stock Index Fund EUR Acc** — Vanguard EM EUR Acc; warning señala iShares S (IE000QAZP7L2) que NO está en el listado. 3A 17,14 % · 5A 6,16 %; TER 0,23 %; MCP 20/11: 1.00 EUR.
- **`LU1769942233` DWS Invest CROCI Japan LCH** — DWS CROCI Japan LCH; cobertura EUR no declarada explícitamente en ficha MCP — verificar en pantalla. 3A 18,23 % · 5A 18,13 % · vol 12,45 %; TER 1,48 %; MCP ficha: 0.00 EUR.
- **`LU2468423889` DWS Invest CROCI US Dividends EUR LC** — DWS CROCI US Dividends EUR LC; sin 5A (clase joven). 3A 16,63 % · vol 15,37 %; TER 1,15 %; MCP ficha: 0.00 EUR.
- **`LU0845340131` Pictet-Quest Global Sustainable Equities-P EUR** — Pictet Quest Global Sustainable P. 3A 15,30 % · 5A 9,68 % · vol 11,02 %; TER 1,17 %; web ficha: 0.00 EUR.
- **`IE00BDRK7J14` iShares Euro Investment Grade Corporate Bond Index Fund (IE) D Acc EUR** — duración ~4.4 (ficha); 2022 −13.26%. 3A 3,65 % · 5A 0,06 % · vol 3,44 %; TER 0,12 %; MCP 20/11: 0.00 EUR.
- **`LU0438093006` State Street EMU Government Bond Index Fund P Acc** — State Street EMU Gov P; duración ~7 estimada; JPM Short Duration descartado (mín 35.000). 3A 1,25 % · 5A -3,10 % · vol 4,84 %; TER 0,36 %; MCP 20/11: 50 EUR.
- **`LU0034353002` DWS Floating Rate Notes LC** — DWS Floating Rate Notes LC; 2026 Q1. 3A 3,32 % · 5A 2,54 %; TER 0,25 %; web ficha: 0.00 EUR.
- **`LU1486845537` ODDO BHF Euro Credit Short Dur CR-EUR** — ODDO BHF Euro Credit Short Dur CR; 5A Q1. 3A 3,69 % · 5A 2,61 %; TER 0,92 %; web ficha: 100 EUR.
- **`FR0010288316` Groupama Entreprises NC** — Groupama Entreprises NC; ligeramente por debajo de €STR. 3A 2,73 % · 5A 2,17 % · vol 0,12 %; TER 0,32 %; web ficha: 500 EUR.

La ficha completa de cada uno, con todas las pegas y fuentes, está en [`fondos-revisados.md`](fondos-revisados.md).

## 7. Ejecución

Dinero nuevo: una orden de suscripción por fondo, sin reembolso previo. La tabla está en el orden en que conviene lanzarla: primero las líneas con mínimo inicial más alto. El corte se lee en la ficha de cada fondo; verificar en pantalla el día de la orden.

| # | Fondo | ISIN | € | Mínimo inicial | Orden |
| --: | --- | --- | --: | --- | --- |
| 1 | Groupama Entreprises NC | `FR0010288316` | 7.000 | web ficha: 500 EUR | Suscribir 7.000 € |
| 2 | ODDO BHF Euro Credit Short Dur CR-EUR | `LU1486845537` | 8.000 | web ficha: 100 EUR | Suscribir 8.000 € |
| 3 | State Street EMU Government Bond Index Fund P Acc | `LU0438093006` | 10.000 | MCP 20/11: 50 EUR | Suscribir 10.000 € |
| 4 | Fidelity MSCI World Index Fund P-ACC-EUR (hedged) | `IE00BYX5P602` | 18.000 | MCP 20/11: 1.00 EUR | Suscribir 18.000 € |
| 5 | Vanguard Emerging Markets Stock Index Fund EUR Acc | `IE0031786696` | 8.000 | MCP 20/11: 1.00 EUR | Suscribir 8.000 € |
| 6 | Robeco QI European Conservative Equities D EUR | `LU0339661307` | 8.000 | web ficha: 0.00 EUR | Suscribir 8.000 € |
| 7 | DWS Invest CROCI Japan LCH | `LU1769942233` | 4.000 | MCP ficha: 0.00 EUR | Suscribir 4.000 € |
| 8 | DWS Invest CROCI US Dividends EUR LC | `LU2468423889` | 10.000 | MCP ficha: 0.00 EUR | Suscribir 10.000 € |
| 9 | Pictet-Quest Global Sustainable Equities-P EUR | `LU0845340131` | 7.000 | web ficha: 0.00 EUR | Suscribir 7.000 € |
| 10 | iShares Euro Investment Grade Corporate Bond Index Fund (IE) … | `IE00BDRK7J14` | 12.000 | MCP 20/11: 0.00 EUR | Suscribir 12.000 € |
| 11 | DWS Floating Rate Notes LC | `LU0034353002` | 8.000 | web ficha: 0.00 EUR | Suscribir 8.000 € |

## 8. Qué se descarta

| Candidato | Razón con número | Solución adoptada |
| --- | --- | --- |
| JPMorgan Short Duration | mínimo 35.000 € frente a los 10.000 € de la línea | State Street EMU Gov P, mínimo 50 € |
| iShares EM S (IE000QAZP7L2) | mencionado en la ficha pero no está en el listado | Vanguard EM EUR Acc a 0,23 % |

## 9. Verificación, revisión y lo que queda abierto

**Web 20/11 — `LU1769942233` (cobertura de divisa y coste de la clase LCH).** Factsheet oficial DWS a 30/10/2026: clase LCH (EUR), acumulación, gestión 1,30 %, TER 1,48 %, carga inicial hasta 2 %. La clase LCH es la variante cubierta del yen: su rentabilidad acumulada a 3 años es 81,1 % frente al 55,7 % de la clase LC(EUR) sin cubrir. Queda verificada la cobertura que la ficha MCP no declaraba. <https://download.dws.com/download/asset/6f69b6a8-359f-4a36-bb75-4ef2c26b9fda?tenant=ActiveEmea>

**Revisión.** Revisar el 30/11/2027 y cada 12 meses: (a) TER real en pantalla frente al snapshot; (b) comisiones de éxito efectivas; (c) clases hermanas que abaraten una línea sin cambiar de fondo —recuerda que cambiar de clase de un fondo ya comprado es un reembolso—; (d) que ningún fondo pase a distribuir o a tener soft close; (e) en C2/C5, evidencia de cada gestor contra su índice neto de TER.

**Sin decidir:** horizonte real, colchón fuera de la cartera, aportaciones periódicas y fecha de ejecución. Ninguna orden se lanza hasta la revisión del titular.

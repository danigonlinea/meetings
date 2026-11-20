---
title: "C5 — Crecimiento con satélites · 100.000 €"
date: 2026-11-20
type: reference
category: finance
tags: [cartera, fondos, myinvestor, cartera-ai-fondos-2000-lista-deepseek, c5]
status: living
---

# C5 — Crecimiento con satélites · 100.000 €

Cartera **independiente de 100.000 €**, construida solo con fondos del listado `finance/fondos-myinvestor/`. **Ningún fondo de esta carpeta se repite en las otras cuatro**: el conjunto de las cinco son 37 líneas y 37 ISIN distintos, comprobados por código también por nombre normalizado y por clase hermana ([`validacion.md`](validacion.md)). No se suma ni se compara con las demás.

> **Sin ejecutar.** Ninguna orden lanzada y ninguna decisión tomada: la cartera es del titular y la ejecución también. Los importes mínimos, los TER y las políticas de distribución están verificados en el catálogo MCP de MyInvestor el 20/11/2026; las rentabilidades son las del mismo snapshot y no son una promesa.

## 1. Decisión

99,5 % de renta variable y 0,76 % de coste: el 60 % del dinero está en un solo índice all-cap al 0,20 % y el 40 % restante en cinco satélites que pagan entre 1,35 % y 1,93 %. La cartera de más riesgo de las cinco, y aun así la mitad de cara que la otra cartera de riesgo alto (C2, 1.434,40 €): el núcleo indexado es lo que la sostiene.

| Métrica | Valor |
| --- | --- |
| Importe | 100.000 € |
| Líneas | 6 |
| Coste anual (TER) | 764,60 € (0,7646 %) |
| Renta variable real (*look-through*) | 99,48 % |
| Renta fija | 0,00 % |
| Caída en el escenario de la casa −(40 % × RV + 3 % × RF) | −39,79 % (−39.790 €) |
| Comisiones de éxito | 1 de 6 líneas |

**El criterio:** cerca del 100 % de renta variable en construcción de barra: el 60 % en un núcleo global all-cap al 0,20 % y el 40 % en cinco satélites (tecnología, emergentes activos, small cap americana, Iberia e infraestructura), cada uno con su tamaño, su razón y su pega.

## 2. Composición

| # | Fondo | ISIN | Rol en la cartera | € | % base | TER | €/año |
| --: | --- | --- | --- | --: | --: | --: | --: |
| 1 | Vanguard ESG Developed World All Cap Equity Index Fund EUR Acc | `IE00B5456744` | Núcleo global all-cap | 60.000 | 60,00 % | 0,20 % | 120,00 |
| 2 | DNB Fund - Technology A EUR (Acc) | `LU0302296495` | Satélite tecnología | 10.000 | 10,00 % | 1,56 % | 156,00 |
| 3 | Ashoka WhiteOak ICAV - Ashoka WhiteOak Emerging Markets Equity Fund Class C USD Accumulation | `IE000DDQNQO2` | Satélite emergentes activos | 8.000 | 8,00 % | 1,35 % | 108,00 |
| 4 | T. Rowe Price Funds SICAV - US Smaller Companies Equity Fund A (EUR) | `LU0918140210` | Satélite small cap EE. UU. | 8.000 | 8,00 % | 1,72 % | 137,60 |
| 5 | Fidelity Funds - Iberia Fund A-Acc-EUR | `LU0261948904` | Satélite Iberia | 6.000 | 6,00 % | 1,93 % | 115,80 |
| 6 | First Sentier Global Listed Infrastructure Fund Class I (Accumulation) EUR | `IE00BYSJTY39` | Satélite infraestructura | 8.000 | 8,00 % | 1,59 % | 127,20 |
| | **Total** | | | **100.000** | **100,00 %** | | **764,60** |

**No hay beta emergente indexada en esta cartera.** Se evaluaron el iShares Emerging Markets Institutional (0,32 %, pero es **clase hermana del fondo que usa C1**, y el mandato prohíbe repetir el fondo), el Fidelity MSCI EM EUR (0,20 %, ya elegido en la cartera hermana `-glm`) y el Vanguard ESG Emerging All Cap (0,25 %, pero 41 % en Taiwán y 3A +14,5 % frente al +17,2 % del índice). Ninguno aportaba lo que cuesta: el emergente de C5 es activo, en una sola línea (Ashoka, 8 %).

## 3. Bloques, roles y coste

Los bloques se etiquetan por **rol**, no por vehículo: un fondo de crédito al 0,47 % y un indexado al 0,10 % no son la misma cosa aunque los dos sean «renta fija».

| Bloque | € | % base | TER medio del bloque | €/año |
| --- | --: | --: | --: | --: |
| Núcleo indexado | 60.000 | 60,00 % | 0,200 % | 120,00 |
| Satélites activos | 40.000 | 40,00 % | 1,612 % | 644,60 |

## 4. Métricas de riesgo

- **Renta variable real:** 99,48 %. Suma Σ importe × `alloc_equity` de cada ficha verificada en el MCP, no la etiqueta del catálogo.
- **Caída de manual:** −39,79 %, es decir −39.790 €. Es la fórmula de la casa −(40 % × RV + 3 % × RF): supone que la bolsa cae un 40 % y la renta fija un 3 % a la vez. No es una previsión, es la vara con la que se comparan las cinco carteras.
- **Renta fija:** 0,00 %. Esta cartera no tiene bloque de renta fija: el riesgo es bolsa y nada más, y por eso su caída de manual es la mayor de las cinco.

## 5. Geografía (look-through de la renta variable)

Base: 99.476 € de renta variable (las líneas de renta fija y el market neutral no entran). Pesos aproximados a partir de los `top_regions` de cada ficha del MCP.

| Región | % de la RV | € equivalentes |
| --- | --: | --: |
| Estados Unidos | 62,65 % | 62.317 |
| Europa | 17,90 % | 17.803 |
| Japón | 4,52 % | 4.492 |
| Mercados emergentes | 10,19 % | 10.133 |
| Otras (Canadá, Asia-Pacífico desarrollada, otros) | 4,76 % | 4.730 |

## 6. Razón fondo a fondo

### Vanguard ESG Developed World All Cap Equity Index Fund EUR Acc — 60.000 € (60,00 %) · Núcleo global all-cap

`IE00B5456744` · Vanguard · TER 0,20 % · sin comisión de éxito · mínimo 1,00 € · corte 16:00 · SRRI 4

52 % de núcleo al 0,20 %: FTSE Developed All Cap Choice, es decir **grandes, medianas y pequeñas** de 23 mercados desarrollados, excluyendo fósiles, armamento y conductas controvertidas. Frente al MSCI World del resto de carteras, este añade la pequeña capitalización global en el mismo vehículo, que es lo que una cartera de crecimiento necesita en el núcleo.

**Pega:** El filtro ESG excluye energía y defensa y sobrepondera tecnología (38 %): el núcleo ya viene sesgado hacia el mismo factor que los satélites del fondo. 3A +17,4 %.

### DNB Fund - Technology A EUR (Acc) — 10.000 € (10,00 %) · Satélite tecnología

`LU0302296495` · DNB AM · TER 1,56 % · éxito 10,00 % · mínimo 1.000,00 € · corte 12:00 · SRRI 4

10 % de satélite tecnológico: 55 % tecnología + 19 % comunicación, 70 % EE. UU. y 7 % Suecia; 3A +28,8 % y 5A +18,2 %, el mejor historial del bloque. Se eligió frente a BlueBox I (1,20 %) porque esa clase tiene un mínimo de 150.000 € y no es comprable con 10.000 €, y frente a Polar Capital porque esta cartera ya no repite el fondo de la hermana.

**Pega:** Comisión de éxito del 10 %, SRRI 4 con volatilidad 3A de 17,3 % y un 2022 de −17 %. Un satélite del 10 % que cae un 40 % cuesta 4 puntos a la cartera entera.

### Ashoka WhiteOak ICAV - Ashoka WhiteOak Emerging Markets Equity Fund Class C USD Accumulation — 8.000 € (8,00 %) · Satélite emergentes activos

`IE000DDQNQO2` · White Oak · TER 1,35 % · sin comisión de éxito · mínimo 0,00 € · corte 10:00 · SRRI 4

8 % de emergentes con gestión activa: 3A +20,9 % frente al +17,2 % del índice; India 14 %, Taiwán 25 %, Corea 18 %, China 16 %. Es la apuesta por el fondo que más se separa del índice emergente sin salirse de él, y el contrapunto activo al 8 % de beta emergente del núcleo.

**Pega:** Clase en USD sin cobertura y lanzada en 2022: **no hay historial de un año malo**, que es el único dato que probaría el proceso. TER 1,35 %.

### T. Rowe Price Funds SICAV - US Smaller Companies Equity Fund A (EUR) — 8.000 € (8,00 %) · Satélite small cap EE. UU.

`LU0918140210` · T. Rowe Price · TER 1,72 % · sin comisión de éxito · mínimo 3.000,00 € · corte 12:00 · SRRI 4

8 % de small cap americana: 3A +11,5 %, 2022 −16,2 % y 1A +26,3 %. Es uno de los pocos fondos del catálogo que da pequeña capitalización americana con proceso fundamental y no un ETF caro; y es el vehículo que pedía el listado del titular.

**Pega:** 5A +4,2 %: cinco años por debajo del S&P 500 y del propio Russell 2000. TER 1,72 % sin comisión de éxito, mínimo 3.000 €.

### Fidelity Funds - Iberia Fund A-Acc-EUR — 6.000 € (6,00 %) · Satélite Iberia

`LU0261948904` · FIL · TER 1,93 % · sin comisión de éxito · mínimo 1,00 € · corte 14:00 · SRRI 4

6 % en renta variable ibérica: 79 % España y 16 % Portugal, 3A +26,5 % y 5A +15,9 %. Es el satélite con mejor retorno por unidad de volatilidad del bloque (vol 3A 11,8 %) y el que menos se solapa con el núcleo mundial (0 % de EE. UU.).

**Pega:** TER 1,93 %, el más caro de las cinco carteras, y 37 % en servicios financieros: es un fondo de banca española con utilities al lado. 2022 −11,6 %.

### First Sentier Global Listed Infrastructure Fund Class I (Accumulation) EUR — 8.000 € (8,00 %) · Satélite infraestructura

`IE00BYSJTY39` · First Sentier · TER 1,59 % · sin comisión de éxito · mínimo 1,00 € · corte 10:00 · SRRI 4

8 % en infraestructura cotizada: 44 % utilities + 37 % industria + 12 % energía, 63 % EE. UU.; 3A +13,0 % con volatilidad 3A de 11,1 %, la más baja de los satélites. Aporta flujos regulados y activos reales, que es la exposición que ninguna otra línea de la cartera tiene.

**Pega:** Es el único fondo que coincide con la cartera hermana `-glm` (allí en su C4). Y la infraestructura cotizada no protege de una subida de tipos: 2022 −2,7 % y 2021 +2,1 %.

## 7. Órdenes

Una sola sesión, todas por importe. **La primera orden de cada fondo tiene que despejar su mínimo inicial**, así que el importe de la tabla es el de la primera y única orden de esa línea: no hay fraccionamiento que pueda ser rechazado.

| # | Fondo | Importe | Hora de corte (destino) | Mínimo inicial |
| --: | --- | --: | :--: | --: |
| 1 | Vanguard ESG Developed World All Cap | 60.000 € | 16:00 | 1,00 € |
| 2 | DNB Technology A EUR | 10.000 € | 12:00 | 1.000,00 € |
| 3 | Ashoka WhiteOak EM Equity C | 8.000 € | 10:00 | 0,00 € |
| 4 | T. Rowe US Smaller Companies A EUR | 8.000 € | 12:00 | 3.000,00 € |
| 5 | Fidelity Iberia A-Acc-EUR | 6.000 € | 14:00 | 1,00 € |
| 6 | First Sentier Global Listed Infrastructure I | 8.000 € | 10:00 | 1,00 € |

Sin coste de entrada ni de salida en ninguna de las líneas. La liquidación tarda entre 2 y 4 días según el fondo (Pictet monetario y los fondos españoles liquidan antes; los luxemburgueses con suscripción T+3/T+4, los últimos).

## 8. Qué se descarta

Descartes del universo con el número que los descarta. Los trece fondos que pidió el titular se evalúan uno a uno en el `README.md` de la carpeta.

- **Algebris Global Credit Opportunities R EUR (IE00BYT35X57)** — es el único Algebris de crédito del catálogo y no es el «Algebris Financial Credit» del listado. TER 1,60 % + 15 % de éxito, mínimo 10.000 €, 3A +3,57 % y YTD −2,16 %. Frente a Pareto (0,84 %, 3A +2,90 %, duración 0,4) paga el doble por 0,7 pp más de retorno con riesgo de financieras subordinadas. Su ficha del catálogo es genérica («RF Agregado, Corporativo, Gubernamental») y no permite sostener la compra.
- **Algebris Financial Equity I GBP (IE00BWY57036)** — 3A +28,6 % con TER 0,91 %, el mejor fondo de financieras del catálogo. **No es comprable**: mínimo inicial de 500.000 €.
- **BlueBox Global Technology Fund Class I (LU1793346823)** — TER 1,20 % y 3A +21,4 %, mejor que el satélite elegido. **No es comprable**: mínimo inicial de 150.000 €. Se toma DNB Technology (1,56 %) como sustituto y el precio del acceso es 0,36 pp sobre 10.000 € = 36 €/año.
- **Dodge & Cox Worldwide Global Stock EUR (IE00B55JMJ98)** — TER 0,63 % y 3A +15,1 % con 4A −0,4 %: el mejor fondo global barato del catálogo. **No es comprable en una cartera de cinco**: mínimo inicial de 50.000 €, la mitad de la cartera, y la primera orden tiene que despejarlo.
- **Ábaco Renta Fija Mixta Global C FI (ES0140072028)** — el fondo del listado con peor perfil del bloque: SRRI 4 con solo 22 % de RV, TER 1,51 % y 3A +4,01 %. Dunas Valor Equilibrado da 3A +4,68 % con 6,4 % de RV y SRRI 2. Es dominado en las tres columnas.
- **M&G (Lux) Emerging Markets Bond Fund (LU1670631107)** — en el catálogo solo existe la clase **de distribución** (A EUR Inc): la regla de la casa es acumulación, y la clase de acumulación no está en la plataforma. Además duración 6,08 años y rating medio BBB−, que en una cartera con 45 % de renta fija mete riesgo de tipos donde el diseño pide carry.
- **Sissener Canopus** — no está en el catálogo de MyInvestor. El sustituto es el mismo equipo con política de crédito corporativo (Sissener Corporate Bond R, 0,90 %, 3A +6,7 %), que es la parte de la estrategia que encaja en una cartera defensiva.
- **Okavango Delta A FI (ES0167211038)** — 3A +28,0 % y TER 1,51 %, un historial excelente. **Descartado por soft close**: el aviso del MCP dice «Fondo en Soft Close» y solo admite partícipes existentes.
- **Vanguard U.S. 500 Stock Index Investor EUR (IE0032620787)** — la clase barata del S&P 500 que aparecía en el catálogo está **en soft close**; el propio aviso del MCP remite a la clase Institutional (IE0032126645), que es la que se compra.
- **Morgan Stanley US Growth A (LU0073232471)** — 3A +21,9 % con TER 1,63 %, pero SRRI 6, volatilidad 3A 29,4 %, 4A −60,6 % y 1A −4,2 %. En una cartera de convicción con ocho líneas, una posición del 10 % con esa caída se come el año.
- **Ábaco, Merchbanc, Pareto, Storm, Cartesio, Dunas y Sissener como bloque entero de renta fija** — se evalúan individualmente: cinco de los siete entran en C3 y C4 (Pareto, Storm, Merchbanc, Cartesio, Dunas, Sissener). Los dos que sobran —Ábaco y Algebris— se descartan por número, no por categoría.

## 9. Revisión y disparadores

- **Revisión anual, no trimestral.** Esta cartera no tiene un mecanismo que medir cada trimestre: se revisa una vez al año, o antes si cambia el horizonte, el colchón fuera de cartera o la tolerancia a la caída.
- **Disparador de riesgo:** si la caída real supera el −47,7 % (el escenario de manual con un 20 % de margen), la cartera no se toca: se revisa si el horizonte sigue siendo el mismo. Vender en la caída es la única decisión que la fórmula no contempla.
- **Disparador de coste:** si una línea sube su TER más de 0,25 pp o introduce una comisión de éxito, se compara con la alternativa del catálogo y se traspasa solo si el ahorro supera el coste fiscal de un traspaso (que en fondos es 0 %).
- **Disparador de soft close:** cualquier aviso nuevo de soft close en una línea obliga a buscar sustituto antes de la siguiente aportación, no después de que la app rechace la orden.

---

*Datos de fichas y MCP a 20/11/2026. Rentabilidades pasadas no garantizan futuras. Este documento no es una recomendación de inversión: es el resultado de un encargo con un criterio declarado.*

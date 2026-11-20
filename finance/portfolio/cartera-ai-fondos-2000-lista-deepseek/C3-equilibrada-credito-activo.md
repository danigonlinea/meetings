---
title: "C3 — Equilibrada con crédito activo · 100.000 €"
date: 2026-11-20
type: reference
category: finance
tags: [cartera, fondos, myinvestor, cartera-ai-fondos-2000-lista-deepseek, c3]
status: living
---

# C3 — Equilibrada con crédito activo · 100.000 €

Cartera **independiente de 100.000 €**, construida solo con fondos del listado `finance/fondos-myinvestor/`. **Ningún fondo de esta carpeta se repite en las otras cuatro**: el conjunto de las cinco son 37 líneas y 37 ISIN distintos, comprobados por código también por nombre normalizado y por clase hermana ([`validacion.md`](validacion.md)). No se suma ni se compara con las demás.

> **Sin ejecutar.** Ninguna orden lanzada y ninguna decisión tomada: la cartera es del titular y la ejecución también. Los importes mínimos, los TER y las políticas de distribución están verificados en el catálogo MCP de MyInvestor el 20/11/2026; las rentabilidades son las del mismo snapshot y no son una promesa.

## 1. Decisión

La cartera que reparte el riesgo entre bolsa barata y crédito gestionado: 0,49 % de coste total, la segunda más barata de las cinco, con 55 % de bolsa y cinco gestores de renta fija trabajando en el 45 % restante.

| Métrica | Valor |
| --- | --- |
| Importe | 100.000 € |
| Líneas | 7 |
| Coste anual (TER) | 492,90 € (0,4929 %) |
| Renta variable real (*look-through*) | 55,05 % |
| Renta fija | 42,00 % |
| Caída en el escenario de la casa −(40 % × RV + 3 % × RF) | −23,28 % (−23.278 €) |
| Comisiones de éxito | 1 de 7 líneas |

**El criterio:** 55 % de renta variable en dos índices baratos y 45 % en cinco fondos de crédito con gestión activa (nórdico IG/HY, high yield, flexible, corta duración y corporativo europeo). La renta fija no es un lastre indexado: es donde vive el gestor.

## 2. Composición

| # | Fondo | ISIN | Rol en la cartera | € | % base | TER | €/año |
| --: | --- | --- | --- | --: | --: | --: | --: |
| 1 | Amundi Index Solutions - Amundi Index MSCI World IE-C | `LU0996181599` | Núcleo desarrollado | 47.000 | 47,00 % | 0,20 % | 94,00 |
| 2 | Vanguard Emerging Markets Stock Index Fund EUR Acc | `IE0031786696` | Emergentes | 8.000 | 8,00 % | 0,23 % | 18,40 |
| 3 | Pareto Nordic Cross Credit R EUR | `LU2200514128` | Crédito nórdico duración 0,4 | 12.000 | 12,00 % | 0,84 % | 100,80 |
| 4 | Storm Fund II - Storm Bond Fund RC EUR (Acc) | `LU0840158819` | High yield nórdico | 8.000 | 8,00 % | 1,06 % | 84,80 |
| 5 | Merchbanc FCP Renta Fija Flex A | `LU2222028099` | Renta fija flexible | 10.000 | 10,00 % | 1,23 % | 123,00 |
| 6 | M&G (Lux) Short Dated Corporate Bond Fund EUR A Acc | `LU1670718219` | Crédito corta duración | 8.000 | 8,00 % | 0,47 % | 37,60 |
| 7 | European Specialist Investment Funds - M&G European Credit Investment Fund Class P EUR Acc | `LU2482630162` | Crédito corporativo europeo | 7.000 | 7,00 % | 0,49 % | 34,30 |
| | **Total** | | | **100.000** | **100,00 %** | | **492,90** |

20 % de la cartera está en crédito nórdico (Pareto 12 % + Storm 8 %). Es una concentración regional deliberada, no un descuido: es el mercado donde el carry por unidad de volatilidad es más alto del catálogo. Y se dice aquí porque ningún otro documento lo va a decir.

## 3. Bloques, roles y coste

Los bloques se etiquetan por **rol**, no por vehículo: un fondo de crédito al 0,47 % y un indexado al 0,10 % no son la misma cosa aunque los dos sean «renta fija».

| Bloque | € | % base | TER medio del bloque | €/año |
| --- | --: | --: | --: | --: |
| Renta variable indexada | 55.000 | 55,00 % | 0,204 % | 112,40 |
| Crédito activo | 45.000 | 45,00 % | 0,846 % | 380,50 |

## 4. Métricas de riesgo

- **Renta variable real:** 55,05 %. Suma Σ importe × `alloc_equity` de cada ficha verificada en el MCP, no la etiqueta del catálogo.
- **Caída de manual:** −23,28 %, es decir −23.278 €. Es la fórmula de la casa −(40 % × RV + 3 % × RF): supone que la bolsa cae un 40 % y la renta fija un 3 % a la vez. No es una previsión, es la vara con la que se comparan las cinco carteras.
- **Renta fija:** 42,00 %. La duración no está publicada para todas las líneas; sí lo está para las que importan: Pareto 0,4 años de duración de tipos, Storm y M&G Short Dated en el tramo corto, Twelve en flotante. El único bloque con duración larga es la deuda pública y es explícito en el diseño.

## 5. Geografía (look-through de la renta variable)

Base: 54.981 € de renta variable (las líneas de renta fija y el market neutral no entran). Pesos aproximados a partir de los `top_regions` de cada ficha del MCP.

| Región | % de la RV | € equivalentes |
| --- | --: | --: |
| Estados Unidos | 61,52 % | 33.826 |
| Europa | 13,67 % | 7.517 |
| Japón | 5,13 % | 2.819 |
| Mercados emergentes | 13,97 % | 7.680 |
| Otras (Canadá, Asia-Pacífico desarrollada, otros) | 5,71 % | 3.139 |

## 6. Razón fondo a fondo

### Amundi Index Solutions - Amundi Index MSCI World IE-C — 47.000 € (47,00 %) · Núcleo desarrollado

`LU0996181599` · Amundi · TER 0,20 % · sin comisión de éxito · mínimo 1,00 € · corte 12:00 · SRRI 4

47 % del total: el núcleo de renta variable de la cartera equilibrada, MSCI World al 0,20 %. Es un vehículo distinto de los otros tres núcleos indexados del conjunto (iShares D, Vanguard ESG All Cap y Vanguard Global Stock), de modo que las cinco carteras no comparten ni el fondo que replica el mismo índice.

**Pega:** 0,20 % cuando el mismo índice existe a 0,06 %: 47.000 € × 0,14 pp = 66 €/año de sobrecoste por no repetir vehículo.

### Vanguard Emerging Markets Stock Index Fund EUR Acc — 8.000 € (8,00 %) · Emergentes

`IE0031786696` · Vanguard · TER 0,23 % · sin comisión de éxito · mínimo 1,00 € · corte 16:00 · SRRI 4

8 % de emergentes al 0,23 %, el índice completo (1.100 empresas) y no una selección. En una cartera equilibrada el emergente debe ser beta barata, no una convicción: la convicción ya está en el 47 % de núcleo desarrollado.

**Pega:** Volatilidad 3A 15,9 % y 5A +6,2 %: es el bloque que más ruido añade por unidad de retorno esperado.

### Pareto Nordic Cross Credit R EUR — 12.000 € (12,00 %) · Crédito nórdico duración 0,4

`LU2200514128` · Pareto AM · TER 0,84 % · sin comisión de éxito · mínimo 1,00 participación · corte 10:00 · SRRI 2

12 % en crédito nórdico IG/HY con duración de tipos de 0,4 años y YTM 3,6 %: top 10 emisores solo 13,7 %, y un 2022 de −1,5 % que es la prueba de que la duración casi nula funciona. Es carry con riesgo de crédito, no de tipos — el perfil que necesita una cartera con 55 % de bolsa.

**Pega:** El MCP corrige el TER al alza: 0,84 % y no el 0,70 % de la ficha del repositorio. 41 % en financieras y 13 % en inmobiliario; y hay riesgo de divisa nórdica que la clase EUR no declara cubrir.

### Storm Fund II - Storm Bond Fund RC EUR (Acc) — 8.000 € (8,00 %) · High yield nórdico

`LU0840158819` · Storm Capital Management · TER 1,06 % · éxito 10,00 % · mínimo 0,001 participaciones · corte 10:00 · SRRI 2

8 % en high yield nórdico: 3A +5,6 %, 5A +6,0 % y volatilidad 3A de 1,13 %, un perfil de retorno alto con oscilación mínima que muy pocos fondos de HY consiguen. Complementa a Pareto: mismo mercado, más crédito y menos duración todavía.

**Pega:** Comisión de éxito del 10 % (el MCP la publica; el factsheet decía «see prospectus»), 51 % en Noruega y un 15 % de liquidez que diluye el carry. Dos fondos nórdicos suman 20 % de la cartera en la misma región de crédito.

### Merchbanc FCP Renta Fija Flex A — 10.000 € (10,00 %) · Renta fija flexible

`LU2222028099` · Andbank AM Luxembourg · TER 1,23 % · sin comisión de éxito · mínimo 100,00 € · corte 10:00 · SRRI 2

10 % en renta fija flexible europea sin restricción de duración ni calidad: 84 % corporativos, 3A +4,4 % y un 2022 de −4,6 % contenido. Es la línea que puede mover la duración del bloque cuando el ciclo cambie, algo que un índice no hace.

**Pega:** TER 1,23 % con una comisión de gestión declarada de solo 0,19 %: el resto son gastos del fondo, y el MCP sube el coste frente al 1,19 % de la ficha. 6 % en Rumanía, que no es eurozona aunque la clase lo sea.

### M&G (Lux) Short Dated Corporate Bond Fund EUR A Acc — 8.000 € (8,00 %) · Crédito corta duración

`LU1670718219` · M&G · TER 0,47 % · sin comisión de éxito · mínimo 1.000,00 € · corte 12:00 · SRRI 2

8 % en crédito corporativo de corta duración al 0,47 %: 50 % corporativos + 12 % titulizaciones residenciales + 10 % covered, volatilidad 3A 1,49 % y 3A +3,2 %. Es el bloque que financia la parte de liquidez de la cartera sin renunciar al carry.

**Pega:** 29 % en Reino Unido, que en una cartera denominada en euros es riesgo de divisa asumido; y 3A +3,2 % no cubre la inflación.

### European Specialist Investment Funds - M&G European Credit Investment Fund Class P EUR Acc — 7.000 € (7,00 %) · Crédito corporativo europeo

`LU2482630162` · M&G Luxembourg · TER 0,49 % · sin comisión de éxito · mínimo 1.000,00 € · corte 10:00 · SRRI 2

7 % en crédito corporativo europeo de alta calidad con duración neutra al 0,49 %: 75 % corporativos, 3A +3,6 %, volatilidad 3A 3,48 %. Aporta la parte IG del bloque de crédito, que Pareto y Storm no cubren (los dos son nórdicos y con HY dentro).

**Pega:** Historial de la clase sin 5 años publicados y un 9 % de liquidez. Clase P «limpia»: la comisión de gestión aparece como 0,00 % en el MCP, lo que sugiere un acuerdo de bancaseguros que puede no estar disponible para todos los partícipes.

## 7. Órdenes

Una sola sesión, todas por importe. **La primera orden de cada fondo tiene que despejar su mínimo inicial**, así que el importe de la tabla es el de la primera y única orden de esa línea: no hay fraccionamiento que pueda ser rechazado.

| # | Fondo | Importe | Hora de corte (destino) | Mínimo inicial |
| --: | --- | --: | :--: | --: |
| 1 | Amundi Index MSCI World IE-C | 47.000 € | 12:00 | 1,00 € |
| 2 | Vanguard Emerging Markets | 8.000 € | 16:00 | 1,00 € |
| 3 | Pareto Nordic Cross Credit R | 12.000 € | 10:00 | 1,00 participación |
| 4 | Storm Bond RC EUR | 8.000 € | 10:00 | 0,001 participaciones |
| 5 | Merchbanc Renta Fija Flex A | 10.000 € | 10:00 | 100,00 € |
| 6 | M&G Short Dated Corporate Bond | 8.000 € | 12:00 | 1.000,00 € |
| 7 | M&G European Credit Investment P | 7.000 € | 10:00 | 1.000,00 € |

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
- **Disparador de riesgo:** si la caída real supera el −27,9 % (el escenario de manual con un 20 % de margen), la cartera no se toca: se revisa si el horizonte sigue siendo el mismo. Vender en la caída es la única decisión que la fórmula no contempla.
- **Disparador de coste:** si una línea sube su TER más de 0,25 pp o introduce una comisión de éxito, se compara con la alternativa del catálogo y se traspasa solo si el ahorro supera el coste fiscal de un traspaso (que en fondos es 0 %).
- **Disparador de soft close:** cualquier aviso nuevo de soft close en una línea obliga a buscar sustituto antes de la siguiente aportación, no después de que la app rechace la orden.

---

*Datos de fichas y MCP a 20/11/2026. Rentabilidades pasadas no garantizan futuras. Este documento no es una recomendación de inversión: es el resultado de un encargo con un criterio declarado.*

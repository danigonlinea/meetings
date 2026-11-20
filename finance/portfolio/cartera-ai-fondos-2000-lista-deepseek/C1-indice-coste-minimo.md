---
title: "C1 — Índice de coste mínimo · 100.000 €"
date: 2026-11-20
type: reference
category: finance
tags: [cartera, fondos, myinvestor, cartera-ai-fondos-2000-lista-deepseek, c1]
status: living
---

# C1 — Índice de coste mínimo · 100.000 €

Cartera **independiente de 100.000 €**, construida solo con fondos del listado `finance/fondos-myinvestor/`. **Ningún fondo de esta carpeta se repite en las otras cuatro**: el conjunto de las cinco son 37 líneas y 37 ISIN distintos, comprobados por código también por nombre normalizado y por clase hermana ([`validacion.md`](validacion.md)). No se suma ni se compara con las demás.

> **Sin ejecutar.** Ninguna orden lanzada y ninguna decisión tomada: la cartera es del titular y la ejecución también. Los importes mínimos, los TER y las políticas de distribución están verificados en el catálogo MCP de MyInvestor el 20/11/2026; las rentabilidades son las del mismo snapshot y no son una promesa.

## 1. Decisión

Con 70.000 € en bolsa y 30.000 € en renta fija indexada, la cartera cuesta 129,20 €/año (0,13 %). Es la forma más barata de tener el mundo entero: ninguna línea paga gestión activa, ninguna comisión de éxito y ninguna se solapa con las otras cuatro carteras de este encargo.

| Métrica | Valor |
| --- | --- |
| Importe | 100.000 € |
| Líneas | 8 |
| Coste anual (TER) | 129,20 € (0,1292 %) |
| Renta variable real (*look-through*) | 69,47 % |
| Renta fija | 29,89 % |
| Caída en el escenario de la casa −(40 % × RV + 3 % × RF) | −28,68 % (−28.685 €) |
| Comisiones de éxito | 0 de 8 líneas |

**El criterio:** solo gestión indexada y la clase operable más barata de cada índice: cerca del 70 % de renta variable repartida en cinco índices y el 30 % restante en renta fija indexada. Ninguna decisión de gestor, todo el presupuesto en beta.

## 2. Composición

| # | Fondo | ISIN | Rol en la cartera | € | % base | TER | €/año |
| --: | --- | --- | --- | --: | --: | --: | --: |
| 1 | iShares Developed World Index Fund (IE) D Acc EUR | `IE00BD0NCM55` | Núcleo desarrollado | 40.000 | 40,00 % | 0,12 % | 48,00 |
| 2 | iShares Emerging Markets Index Fund (IE) D Acc EUR | `IE00BYWYCC39` | Emergentes | 8.000 | 8,00 % | 0,20 % | 16,00 |
| 3 | Vanguard U.S. 500 Stock Index Fund EUR Acc (clase Institutional) | `IE0032126645` | EE. UU. (S&P 500) | 8.000 | 8,00 % | 0,10 % | 8,00 |
| 4 | iShares Europe Index Fund (IE) D Acc EUR | `IE00BDRK7L36` | Europa | 8.000 | 8,00 % | 0,10 % | 8,00 |
| 5 | iShares Japan Index Fund (IE) Institutional Acc EUR | `IE00B6RVWW34` | Japón | 6.000 | 6,00 % | 0,18 % | 10,80 |
| 6 | iShares Euro Credit Bond Index Fund (IE) D Acc EUR | `IE00BD0NC698` | Crédito euro IG | 14.000 | 14,00 % | 0,12 % | 16,80 |
| 7 | iShares Euro Government Inflation-Linked Bond Index Fund (IE) D Acc EUR | `IE00BD0NC144` | Deuda pública ligada a inflación | 8.000 | 8,00 % | 0,10 % | 8,00 |
| 8 | iShares Global Aggregate 1-5 Year Bond Index Fund D Acc EUR Hedged | `IE00BMZ3NN11` | Agregado global 1-5 años | 8.000 | 8,00 % | 0,17 % | 13,60 |
| | **Total** | | | **100.000** | **100,00 %** | | **129,20** |

## 3. Bloques, roles y coste

Los bloques se etiquetan por **rol**, no por vehículo: un fondo de crédito al 0,47 % y un indexado al 0,10 % no son la misma cosa aunque los dos sean «renta fija».

| Bloque | € | % base | TER medio del bloque | €/año |
| --- | --: | --: | --: | --: |
| Renta variable indexada | 70.000 | 70,00 % | 0,130 % | 90,80 |
| Renta fija indexada | 30.000 | 30,00 % | 0,128 % | 38,40 |

## 4. Métricas de riesgo

- **Renta variable real:** 69,47 %. Suma Σ importe × `alloc_equity` de cada ficha verificada en el MCP, no la etiqueta del catálogo.
- **Caída de manual:** −28,68 %, es decir −28.685 €. Es la fórmula de la casa −(40 % × RV + 3 % × RF): supone que la bolsa cae un 40 % y la renta fija un 3 % a la vez. No es una previsión, es la vara con la que se comparan las cinco carteras.
- **Renta fija:** 29,89 %. La duración no está publicada para todas las líneas; sí lo está para las que importan: Pareto 0,4 años de duración de tipos, Storm y M&G Short Dated en el tramo corto, Twelve en flotante. El único bloque con duración larga es la deuda pública y es explícito en el diseño.

## 5. Geografía (look-through de la renta variable)

Base: 69.470 € de renta variable (las líneas de renta fija y el market neutral no entran). Pesos aproximados a partir de los `top_regions` de cada ficha del MCP.

| Región | % de la RV | € equivalentes |
| --- | --: | --: |
| Estados Unidos | 52,96 % | 36.793 |
| Europa | 19,27 % | 13.388 |
| Japón | 11,85 % | 8.233 |
| Mercados emergentes | 10,97 % | 7.623 |
| Otras (Canadá, Asia-Pacífico desarrollada, otros) | 4,94 % | 3.434 |

## 6. Razón fondo a fondo

### iShares Developed World Index Fund (IE) D Acc EUR — 40.000 € (40,00 %) · Núcleo desarrollado

`IE00BD0NCM55` · BlackRock · TER 0,12 % · sin comisión de éxito · mínimo 1,00 € · corte 12:00 · SRRI 4

Núcleo de renta variable desarrollada al 0,12 %: replica el MSCI World (1.200 empresas, 72 % en EE. UU., 32 % en tecnología y dominado por las mayores tecnológicas americanas). Se elige la clase D y no la clase S (0,06 %, IE000ZYRH0Q7) para no clonar el vehículo exacto de la cartera hermana `-glm`; el sobrecoste es 40.000 × 0,06 % = 24 €/año.

**Pega:** Concentración del índice: las mayores tecnológicas americanas pesan más que Europa entera. Es beta, no una apuesta de gestor.

### iShares Emerging Markets Index Fund (IE) D Acc EUR — 8.000 € (8,00 %) · Emergentes

`IE00BYWYCC39` · BlackRock · TER 0,20 % · sin comisión de éxito · mínimo 1,00 € · corte 12:00 · SRRI 4

Bloque emergente a 0,20 %. Por qué 8 % y no 10: Taiwán 28 % + Corea 21 % + China 19 % son dos tercios del índice y 43 % del fondo es tecnología, así que el bloque ya es una apuesta sectorial además de geográfica. Se descarta la clase S (IE000QAZP7L2, 0,10 %) por la misma razón que el núcleo: cuesta 8 €/año y evita repetir la hermana.

**Pega:** El índice no es «emergentes» en sentido clásico: es semiconductores asiáticos con una pizca de India y Brasil.

### Vanguard U.S. 500 Stock Index Fund EUR Acc (clase Institutional) — 8.000 € (8,00 %) · EE. UU. (S&P 500)

`IE0032126645` · Vanguard · TER 0,10 % · sin comisión de éxito · mínimo 1,00 € · corte 14:00 · SRRI 4

El S&P 500 al 0,10 %. El hallazgo que cambió la línea: la clase Investor que aparecía en el catálogo (IE0032620787) está **en soft close** y el aviso del propio MCP remite a esta clase Institutional, económicamente equivalente. Es la clase que se compra.

**Pega:** Duplica EE. UU. sobre el núcleo mundial: sin esta línea el bloque americano sería el 47 % de la RV y con ella el 53 %. Es deliberado y se paga en concentración, no en coste.

### iShares Europe Index Fund (IE) D Acc EUR — 8.000 € (8,00 %) · Europa

`IE00BDRK7L36` · BlackRock · TER 0,10 % · sin comisión de éxito · mínimo 1,00 € · corte 09:00 · SRRI 4

Europa al 0,10 %, clase D. Se prefiere al índice de la eurozona porque el MSCI Europe incluye Reino Unido (21,7 %) y Suiza (15,9 %), que es donde está la mitad del value europeo; comprar solo eurozona deja fuera a los dos mayores mercados de la región.

**Pega:** 23 % en servicios financieros: el bloque Europa es en la práctica un fondo de banca y seguros con un 18 % de industria al lado.

### iShares Japan Index Fund (IE) Institutional Acc EUR — 6.000 € (6,00 %) · Japón

`IE00B6RVWW34` · BlackRock · TER 0,18 % · sin comisión de éxito · mínimo 1,00 € · corte 09:00 · SRRI 4

Japón al 0,18 %. La clase Institucional es la operable más barata del índice (la D cuesta 0,10 % pero con mínimo de 100.000 € en la ficha de origen, que la plataforma no aplica pero que no conviene dar por buena sin verla en pantalla).

**Pega:** Sin cobertura de divisa: el yen puede mover el bloque varios puntos en un año sin que el índice se mueva.

### iShares Euro Credit Bond Index Fund (IE) D Acc EUR — 14.000 € (14,00 %) · Crédito euro IG

`IE00BD0NC698` · BlackRock · TER 0,12 % · sin comisión de éxito · mínimo 1,00 € · corte 09:00 · SRRI 2

El bloque de crédito al 0,12 %: 47 % bonos corporativos, 35 % relacionados con gobiernos y 12 % covered bonds. Es el suelo de renta fija de la cartera y el que da el 3 % de la caída en el escenario de estrés.

**Pega:** 3A +2,87 % y 5A −1,08 %: la renta fija europea no ha recuperado el golpe de 2022 y este bloque no es una fuente de retorno, es lastre con renta.

### iShares Euro Government Inflation-Linked Bond Index Fund (IE) D Acc EUR — 8.000 € (8,00 %) · Deuda pública ligada a inflación

`IE00BD0NC144` · BlackRock · TER 0,10 % · sin comisión de éxito · mínimo 1,00 € · corte 09:00 · SRRI 3

8 % en deuda pública ligada a la inflación al 0,10 %. Es el único activo de la cartera que sube si la inflación sorprende al alza, y el escenario que el repositorio da por vigente (BCE con subida esperada, inflación persistente) lo justifica.

**Pega:** No cubre la inflación española sino la de la eurozona; y si la inflación cae, el bono real pierde. 3A +1,44 %.

### iShares Global Aggregate 1-5 Year Bond Index Fund D Acc EUR Hedged — 8.000 € (8,00 %) · Agregado global 1-5 años

`IE00BMZ3NN11` · BlackRock · TER 0,17 % · sin comisión de éxito · mínimo 1,00 € · corte 16:00 · SRRI 2

8 % en agregado global 1-5 años, cubierto a EUR: 58 % deuda pública, 27 % corporativa, duración corta. Es el amortiguador de la cartera: volatilidad 3A 1,78 % y el único bloque que no depende de que el crédito europeo aguante.

**Pega:** 3A +2,20 %: paga 0,17 % por un retorno que en la práctica es el tipo de interés a dos años. Su función es la estabilidad, no la rentabilidad.

## 7. Órdenes

Una sola sesión, todas por importe. **La primera orden de cada fondo tiene que despejar su mínimo inicial**, así que el importe de la tabla es el de la primera y única orden de esa línea: no hay fraccionamiento que pueda ser rechazado.

| # | Fondo | Importe | Hora de corte (destino) | Mínimo inicial |
| --: | --- | --: | :--: | --: |
| 1 | iShares Developed World D Acc | 40.000 € | 12:00 | 1,00 € |
| 2 | iShares Emerging Markets D Acc | 8.000 € | 12:00 | 1,00 € |
| 3 | Vanguard U.S. 500 Institutional | 8.000 € | 14:00 | 1,00 € |
| 4 | iShares Europe D Acc | 8.000 € | 09:00 | 1,00 € |
| 5 | iShares Japan Institutional | 6.000 € | 09:00 | 1,00 € |
| 6 | iShares Euro Credit Bond | 14.000 € | 09:00 | 1,00 € |
| 7 | iShares Euro Gov ILB | 8.000 € | 09:00 | 1,00 € |
| 8 | iShares Global Agg 1-5 A EURH | 8.000 € | 16:00 | 1,00 € |

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
- **Disparador de riesgo:** si la caída real supera el −34,4 % (el escenario de manual con un 20 % de margen), la cartera no se toca: se revisa si el horizonte sigue siendo el mismo. Vender en la caída es la única decisión que la fórmula no contempla.
- **Disparador de coste:** si una línea sube su TER más de 0,25 pp o introduce una comisión de éxito, se compara con la alternativa del catálogo y se traspasa solo si el ahorro supera el coste fiscal de un traspaso (que en fondos es 0 %).
- **Disparador de soft close:** cualquier aviso nuevo de soft close en una línea obliga a buscar sustituto antes de la siguiente aportación, no después de que la app rechace la orden.

---

*Datos de fichas y MCP a 20/11/2026. Rentabilidades pasadas no garantizan futuras. Este documento no es una recomendación de inversión: es el resultado de un encargo con un criterio declarado.*

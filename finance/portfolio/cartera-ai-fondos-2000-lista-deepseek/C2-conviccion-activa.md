---
title: "C2 — Convicción activa · 100.000 €"
date: 2026-11-20
type: reference
category: finance
tags: [cartera, fondos, myinvestor, cartera-ai-fondos-2000-lista-deepseek, c2]
status: living
---

# C2 — Convicción activa · 100.000 €

Cartera **independiente de 100.000 €**, construida solo con fondos del listado `finance/fondos-myinvestor/`. **Ningún fondo de esta carpeta se repite en las otras cuatro**: el conjunto de las cinco son 37 líneas y 37 ISIN distintos, comprobados por código también por nombre normalizado y por clase hermana ([`validacion.md`](validacion.md)). No se suma ni se compara con las demás.

> **Sin ejecutar.** Ninguna orden lanzada y ninguna decisión tomada: la cartera es del titular y la ejecución también. Los importes mínimos, los TER y las políticas de distribución están verificados en el catálogo MCP de MyInvestor el 20/11/2026; las rentabilidades son las del mismo snapshot y no son una promesa.

## 1. Decisión

Es la cartera más cara de las cinco (1,43 %) y la única que no compra un solo índice: todo el presupuesto se va en selección de gestor. A cambio asume 97 % de bolsa sin ninguna cobertura de duración y con dos comisiones de éxito.

| Métrica | Valor |
| --- | --- |
| Importe | 100.000 € |
| Líneas | 8 |
| Coste anual (TER) | 1.434,40 € (1,4344 %) |
| Renta variable real (*look-through*) | 97,60 % |
| Renta fija | 0,13 % |
| Caída en el escenario de la casa −(40 % × RV + 3 % × RF) | −39,04 % (−39.043 €) |
| Comisiones de éxito | 2 de 8 líneas |

**El criterio:** ningún indexado: cada una de las ocho líneas es un proceso de gestión con evidencia en su ficha (value europeo, growth global, small cap, Japón por valoración, emergente cuantitativo, value americano). 97 % de renta variable.

## 2. Composición

| # | Fondo | ISIN | Rol en la cartera | € | % base | TER | €/año |
| --: | --- | --- | --- | --: | --: | --: | --: |
| 1 | Capital Group New Perspective Fund (LUX) B EUR | `LU1295551144` | Núcleo global growth | 18.000 | 18,00 % | 1,59 % | 286,20 |
| 2 | DWS Invest II Global Equity High Conviction Fund LC | `LU0826452848` | Global alta convicción | 14.000 | 14,00 % | 1,60 % | 224,00 |
| 3 | Valentum E FI | `ES0182769002` | Small/mid Europa | 12.000 | 12,00 % | 1,46 % | 175,20 |
| 4 | M&G (Lux) European Strategic Value Fund EUR A Acc | `LU1670707527` | Value Europa | 12.000 | 12,00 % | 1,70 % | 204,00 |
| 5 | DWS Invest CROCI Japan LCH | `LU1769942233` | Japón por valoración | 10.000 | 10,00 % | 1,48 % | 148,00 |
| 6 | Robeco QI Emerging Markets Active Equities D € | `LU0329355670` | Emergentes cuantitativo | 12.000 | 12,00 % | 1,52 % | 182,40 |
| 7 | Mutuafondo Renta Variable Internacional A FI | `ES0165194038` | Global activo barato | 12.000 | 12,00 % | 0,83 % | 99,60 |
| 8 | DWS Invest CROCI US Dividends EUR LC | `LU2468423889` | Value EE. UU. | 10.000 | 10,00 % | 1,15 % | 115,00 |
| | **Total** | | | **100.000** | **100,00 %** | | **1.434,40** |

## 3. Bloques, roles y coste

Los bloques se etiquetan por **rol**, no por vehículo: un fondo de crédito al 0,47 % y un indexado al 0,10 % no son la misma cosa aunque los dos sean «renta fija».

| Bloque | € | % base | TER medio del bloque | €/año |
| --- | --: | --: | --: | --: |
| Convicción global | 44.000 | 44,00 % | 1,386 % | 609,80 |
| Europa y Japón | 34.000 | 34,00 % | 1,551 % | 527,20 |
| Emergentes y EE. UU. | 22.000 | 22,00 % | 1,352 % | 297,40 |

## 4. Métricas de riesgo

- **Renta variable real:** 97,60 %. Suma Σ importe × `alloc_equity` de cada ficha verificada en el MCP, no la etiqueta del catálogo.
- **Caída de manual:** −39,04 %, es decir −39.043 €. Es la fórmula de la casa −(40 % × RV + 3 % × RF): supone que la bolsa cae un 40 % y la renta fija un 3 % a la vez. No es una previsión, es la vara con la que se comparan las cinco carteras.
- **Renta fija:** 0,13 %. Esta cartera no tiene bloque de renta fija: el riesgo es bolsa y nada más, y por eso su caída de manual es la mayor de las cinco.

## 5. Geografía (look-through de la renta variable)

Base: 97.597 € de renta variable (las líneas de renta fija y el market neutral no entran). Pesos aproximados a partir de los `top_regions` de cada ficha del MCP.

| Región | % de la RV | € equivalentes |
| --- | --: | --: |
| Estados Unidos | 35,44 % | 34.593 |
| Europa | 29,70 % | 28.988 |
| Japón | 12,08 % | 11.793 |
| Mercados emergentes | 18,12 % | 17.689 |
| Otras (Canadá, Asia-Pacífico desarrollada, otros) | 4,65 % | 4.535 |

## 6. Razón fondo a fondo

### Capital Group New Perspective Fund (LUX) B EUR — 18.000 € (18,00 %) · Núcleo global growth

`LU1295551144` · Capital International · TER 1,59 % · sin comisión de éxito · mínimo 1,00 € · corte 12:00 · SRRI 4

20 % como núcleo de convicción: proceso de Capital Group, 54 % EE. UU. y 46 % fuera (Francia 6 %, Japón 5 %, Taiwán 5 %), 3A +13,3 % y 5A +4,8 %. La ficha del repositorio lo traía como política «pendiente»: el MCP confirma `distributing: 0` — es de acumulación y por tanto comprable bajo la regla de la casa.

**Pega:** Es la línea más floja del bloque en el año: 1A quintil 4 en su categoría y 2022 −22 %. Se paga 1,59 % por un fondo que en 2025-2026 va por detrás de su índice.

### DWS Invest II Global Equity High Conviction Fund LC — 14.000 € (14,00 %) · Global alta convicción

`LU0826452848` · DWS · TER 1,60 % · sin comisión de éxito · mínimo 1,00 € · corte 14:00 · SRRI 4

14 % en un global de alta convicción que no es un indexado disfrazado: 26 % en emergentes (Corea 10 %, Taiwán 10 %), 22 % en financieras y 16 % en salud, con 3A +24,6 % y 5A +15,3 %. Es el contrapeso a Capital Group: menos EE. UU., más Asia.

**Pega:** YTD +32,6 % y 1A +38,8 %: la mitad de su historial reciente es momentum. Si el ciclo gira, este es el fondo que más devuelve.

### Valentum E FI — 12.000 € (12,00 %) · Small/mid Europa

`ES0182769002` · Valentum AM · TER 1,46 % · éxito 9,00 % · mínimo 1,00 € · corte 12:00 · SRRI —

12 % de small/mid europea de convicción: España 29 %, Alemania 13 %, Bélgica 10 %; 26 % industria. 3A +17,5 % con 1A +28,9 %. Es la apuesta por selección de compañías pequeñas europeas, que es donde el activo tiene más recorrido documentado.

**Pega:** Comisión de éxito del 9 % y un 2022 de −28,2 %. Volatilidad 3A 14,2 %: es la línea que más cae en un escenario de recesión europea.

### M&G (Lux) European Strategic Value Fund EUR A Acc — 12.000 € (12,00 %) · Value Europa

`LU1670707527` · M&G · TER 1,70 % · sin comisión de éxito · mínimo 1.000,00 € · corte 12:00 · SRRI 4

12 % en value europeo de gran capitalización: 3A +22,4 % y 5A +15,2 %, con 2022 positivo (+1,8 %), que es exactamente lo que la cartera necesita para no ser toda growth. El MCP corrige el TER al alza (1,70 % frente a 1,65 % de la ficha); manda el MCP.

**Pega:** TER 1,70 % para un fondo de 21.000 M€ en value europeo: el precio de una estrategia que ya existe en ETF por 0,30 %. Aquí se paga la selección de gestor, no el concepto.

### DWS Invest CROCI Japan LCH — 10.000 € (10,00 %) · Japón por valoración

`LU1769942233` · DWS · TER 1,48 % · sin comisión de éxito · mínimo 0,00 € · corte 14:00 · SRRI 4

10 % en Japón por valoración CROCI (cash return on capital invested), clase cubierta a EUR: 3A +18,2 % y 5A +18,1 %, el historial más regular del bloque. Japón es el mercado donde el activo ha batido a su índice con más consistencia en la última década.

**Pega:** CROCI es una metodología propietaria de DWS y el fondo no publica comisión de éxito ni de gestión en el MCP: 1,48 % es todo lo que se sabe. Sin cobertura de la clase se comía el retorno del yen; con cobertura se paga el coste del forward.

### Robeco QI Emerging Markets Active Equities D € — 12.000 € (12,00 %) · Emergentes cuantitativo

`LU0329355670` · Robeco · TER 1,52 % · sin comisión de éxito · mínimo 1,00 € · corte 14:00 · SRRI 4

12 % en emergentes con proceso cuantitativo declarado (cinco factores equiponderados, tracking error ≈2,5 %): 3A +18,9 % y 5A +10,1 % frente a un índice emergente que a 5 años da +5,9 %. Es el único fondo del universo con alfa emergente verificable a cinco años, y por eso repite respecto a la cartera hermana (única coincidencia del bloque).

**Pega:** 47 % tecnología y 26 % Taiwán: el fondo cuantitativo acaba pareciéndose al índice en lo sectorial. Y su tracking error bajo significa que el alfa máximo que puede dar es pequeño.

### Mutuafondo Renta Variable Internacional A FI — 12.000 € (12,00 %) · Global activo barato

`ES0165194038` · Mutuactivos · TER 0,83 % · éxito 6,00 % · mínimo 10,00 € · corte 13:00 · SRRI 4

12 % en el global activo más barato del bloque: 0,83 % de TER, 3A +15,8 % y 5A +8,4 %, con 74 % EE. UU. y 21 años de historial. Es el «activo de precio de indexado» de la cartera: si el resto del bloque no bate a su índice, este al menos no cuesta como si lo hiciera.

**Pega:** Comisión de éxito del 6 % y una cartera muy parecida al MSCI World: parte de su 3A es beta comprada a precio de gestión activa.

### DWS Invest CROCI US Dividends EUR LC — 10.000 € (10,00 %) · Value EE. UU.

`LU2468423889` · DWS · TER 1,15 % · sin comisión de éxito · mínimo 0,00 € · corte 12:00 · SRRI 4

10 % en value americano con disciplina de dividendo: 22 % consumo defensivo, 21 % salud, 20 % consumo cíclico, 3A +16,6 %. Es el contrapeso barato (1,15 %) a las tres líneas growth del bloque.

**Pega:** YTD +36,1 % tras un 1A de +38,8 %: entra en cartera después de su mejor año, que es el peor momento estadístico para comprar value. Historial de clase desde 2018.

## 7. Órdenes

Una sola sesión, todas por importe. **La primera orden de cada fondo tiene que despejar su mínimo inicial**, así que el importe de la tabla es el de la primera y única orden de esa línea: no hay fraccionamiento que pueda ser rechazado.

| # | Fondo | Importe | Hora de corte (destino) | Mínimo inicial |
| --: | --- | --: | :--: | --: |
| 1 | Capital Group New Perspective B | 18.000 € | 12:00 | 1,00 € |
| 2 | DWS Global Equity High Conviction | 14.000 € | 14:00 | 1,00 € |
| 3 | Valentum E FI | 12.000 € | 12:00 | 1,00 € |
| 4 | M&G European Strategic Value | 12.000 € | 12:00 | 1.000,00 € |
| 5 | DWS CROCI Japan (cubierto EUR) | 10.000 € | 14:00 | 0,00 € |
| 6 | Robeco QI EM Active Equities | 12.000 € | 14:00 | 1,00 € |
| 7 | Mutuafondo RV Internacional | 12.000 € | 13:00 | 10,00 € |
| 8 | DWS CROCI US Dividends | 10.000 € | 12:00 | 0,00 € |

Sin coste de entrada ni de salida en ninguna de las líneas. La liquidación tarda entre 2 y 4 días según el fondo (Pictet monetario y los fondos españoles liquidan antes; los luxemburgueses con suscripción T+3/T+4, los últimos).


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
- **El resto del bloque de renta fija del listado** — Merchbanc, Pareto, Storm y Sissener entran en C3 y C4, y Cartesio y Dunas entran como mixtos defensivos. Ábaco y Algebris se quedan fuera por las cifras de sus propias filas, no por categoría. El bloque no se compra entero porque en una cartera de 100.000 € siete fondos de renta fija serían siete líneas de 7.000 € pagando entre 0,63 % y 1,51 % por hacer el mismo trabajo.

## 9. Revisión y disparadores

- **Revisión anual, no trimestral.** Esta cartera no tiene un mecanismo que medir cada trimestre: se revisa una vez al año, o antes si cambia el horizonte, el colchón fuera de cartera o la tolerancia a la caída.
- **Disparador de riesgo:** si la caída real supera el −46,9 % (el escenario de manual con un 20 % de margen), la cartera no se toca: se revisa si el horizonte sigue siendo el mismo. Vender en la caída es la única decisión que la fórmula no contempla.
- **Disparador de coste:** si una línea sube su TER más de 0,25 pp o introduce una comisión de éxito, se compara con la alternativa del catálogo y se traspasa solo si el ahorro supera el coste fiscal de un traspaso (que en fondos es 0 %).
- **Disparador de soft close:** cualquier aviso nuevo de soft close en una línea obliga a buscar sustituto antes de la siguiente aportación, no después de que la app rechace la orden.

---

*Datos de fichas y MCP a 20/11/2026. Rentabilidades pasadas no garantizan futuras. Este documento no es una recomendación de inversión: es el resultado de un encargo con un criterio declarado.*

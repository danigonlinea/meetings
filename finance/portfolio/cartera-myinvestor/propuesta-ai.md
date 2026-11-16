---
title: "Propuesta AI: 60/40 global indexado en once fondos (90.000 €)"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, propuesta, 60-40, indexado, rock, traspaso, myinvestor, renta-fija, emergentes, reits, small-cap]
status: propuesta
related:
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
  - finance/portfolio/cartera-myinvestor/propuesta-actual.md
---

# Propuesta AI — 16/11/2026

> **Qué es.** Un rediseño desde cero de la cartera de 90.000 € de `cartera-actual.md` (60.000 €
> manuales invertibles + 30.000 € de Rock), con **once fondos indexados**, **59,6 % de renta variable
> en look-through estricto**, **201,80 €/año de coste (0,224 %)** y **cero comisiones de éxito**.
>
> **Qué cambia de raíz.** Rock **se desmonta** sin pagar impuestos: MyInvestor permite cancelar la
> cartera automatizada y traspasar todos sus fondos a un monetario, sin reembolso y por tanto sin
> cristalizar la plusvalía (FAQ oficial, §7.1). Desaparecen los tres fondos de renta fija con
> comisión de éxito (DNCA, Carmignac, Gamma) y las cuatro posiciones de 1.000-2.000 €.
>
> **Método.** Catálogo MyInvestor vía MCP el 16/11/2026 (2.409 fondos, 266 indexados): `list_facets`,
> `search_funds` por bloques y `get_funds` por ISIN. Todos los fondos son de **acumulación**
> (`distributing = 0`, verificado en ficha). Cifras de ficha a 12/11/2026; las estimaciones van
> marcadas **est.** o **inferida**.
>
> **No es asesoramiento financiero.** La decisión y la ejecución son del titular.

---

## 1. Las decisiones, una por línea

| # | Decisión | Por qué, con el número |
| --: | --- | --- |
| 1 | **Rock se desmonta por traspaso, no por venta** | Cancelar Rock cuesta **0 €** de impuestos si se hace por el fondo puente monetario. Vender costaría ≈**2.590 €** (19 % de ≈13.650 € de plusvalía sobre una aportación de ≈16.350 €). Se deja de pagar 0,41 % y se elimina el 10 % del bloque en un bono euro a 20+ años |
| 2 | **RV del 31,6 % al 59,6 %** | La RF cobró 0,4 % a 12 meses con inflación del 3,8 % (−3,4 % real). El colchón de 10.000 € sigue fuera. Con horizonte largo, la RV es la única fuente de retorno real |
| 3 | **Fuera los tres fondos con comisión de éxito** | DNCA (1,31 % + 20 %), Carmignac (1,20 % + 20 %) y Gamma (0,95 % + 9 %): 33.000 € pagando 20 %, 20 % y 9 % del resultado, y el **71 % del coste fijo manual** (390 € de 548 €) |
| 4 | **La RF pasa a 36.000 € cortos y de calidad** | Duración 3,83 → **2,66**; +100 pb cuesta **956 €** en vez de 2.360 €. Fuera Carmignac (BBB−), Gamma (Noruega/Ghana, energía) y DNCA (soberanos G10 con futuros) |
| 5 | **Núcleo indexado global, no una apuesta** | MSCI World 28.000 € al 0,12 % + Europa 6.000 + Japón 3.000 + Emergentes 7.000 + REITs 5.000 + Small Cap 5.000 |
| 6 | **Sesgo anti-EE. UU. moderado, no de 33 pp** | EE. UU. pasa del ≈47 % de la RV al **49,0 %**, frente al ≈64 % de un ACWI: −15 pp, no −33 pp. La valoración justifica un sesgo, no una tesis de una sola dirección |
| 7 | **Cero fondos de reparto y cero ETFs** | Los once fondos son de acumulación. Todo fondo permite **traspaso**; un ETF obligaría a vender y tributar en cada rebalanceo |
| 8 | **Once posiciones, ninguna por debajo de 3.000 €** | Se eliminan las cuatro fragmentarias (1.000-2.000 €) y el número de fondos baja de 17 a 11 con más diversificación real |

---

## 2. Cuánta renta variable, y por qué 60

No hay perfil asignado ni puntuación: hay un criterio y tres supuestos escritos.

**El criterio.** 90.000 € invertibles, 10.000 € de colchón fuera, ingresos estables, sin necesidad de
vender en 10 años. En ese escenario el enemigo no es una caída del 25 % (se recupera), es **perder
poder adquisitivo durante una década**: con inflación del 3,8 %, el 68,4 % en renta fija que hoy tiene
la cartera rinde 5,39 % de TIR, pero después de inflación deja ≈1,6 % real y con riesgo de crédito
dentro. La cartera actual no es conservadora: es **corta en crecimiento y larga en prima de crédito**.

**Los tres supuestos** (si uno es falso, el diseño cambia):

1. **Horizonte ≥ 10 años.** Si el dinero se necesita en 3-5 años, la RV baja al 40-50 %.
2. **El colchón de 10.000 € cubre 6-12 meses de gasto** y no se toca. Sigue sin estar dimensionado
   contra un gasto real: es la primera comprobación antes de ejecutar.
3. **Se aguanta una caída de −22.550 € sin vender.** Es el suelo conductual y está en euros, no en %.

| RV | RF | Caída 2008 | Retorno (solo *earnings yield*) | Retorno (EY + crecimiento 4 %) |
| --: | --: | --: | --: | --: |
| 50 % | 50 % | −19.350 € (−21,5 %) | 5,31 % | 7,31 % |
| 55 % | 45 % | −21.015 € (−23,4 %) | 5,44 % | 7,64 % |
| **59,6 %** | **40,4 %** | **−22.550 € (−25,1 %)** | **5,57 %** | **7,95 %** |
| 65 % | 35 % | −24.345 € (−27,1 %) | 5,71 % | 8,31 % |
| 70 % | 30 % | −26.010 € (−28,9 %) | 5,85 % | 8,65 % |

Caída = −(40 % × RV + 3 % × RF), la fórmula de la casa para un escenario tipo 2008. Retorno =
RV × 6,65 % (*earnings yield* del 04/11/2026) + RF × 3,97 % (carry estimado, §6). **No es un backtest
ni una promesa.** La caída de esta propuesta, **−22.550 €**, es prácticamente la que el titular ya
aceptó por escrito para 97.000 € (−23,4 % = −22.700 €). Se asume **la misma caída en euros** y se
cambia su composición: más bolsa, menos crédito.

**Lo que se paga por el 60 %.** El retorno esperado *solo con carry* baja 0,22 pp (5,79 % → 5,57 %)
porque se renuncia a la TIR alta de Carmignac y Gamma. La cartera solo gana si la bolsa entrega
crecimiento de beneficios; si no lo hace, empata o pierde. Es un cambio de riesgo, no una mejora gratis.

---

## 3. La cartera (90.000 €, once fondos)

| Bloque | Fondo | ISIN | € | % | RV dentro | TER |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| **RV global** | Fidelity MSCI World Index EUR P Acc | IE00BYX5NX33 | 28.000 | 31,1 % | 99,3 % | 0,12 % |
| **RV Europa** | iShares Europe Index D Acc EUR | IE00BDRK7L36 | 6.000 | 6,7 % | 99,2 % | 0,10 % |
| **RV Japón** | Fidelity MSCI Japan Index EUR P Acc | IE00BYX5N771 | 3.000 | 3,3 % | 98,6 % | 0,10 % |
| **RV emergentes** | iShares Emerging Markets Index S Acc EUR | IE000QAZP7L2 | 7.000 | 7,8 % | 100 % | 0,16 % |
| **Activos reales** | iShares Developed Real Estate Index D Acc | IE00BDRK7P73 | 5.000 | 5,6 % | 98,9 % | 0,17 % |
| **RV small cap** | Vanguard Global Small-Cap Index EUR Acc | IE00B42W4L06 | 5.000 | 5,6 % | 99,9 % | 0,29 % |
| **RF corta IG** | Neuberger Short Duration Euro Bond U | IE00BL1GVT98 | 8.000 | 8,9 % | 0 % | 0,38 % |
| **RF corporativa 1-5Y** | Amundi EUR Corporate Bond 1-5Y ESG AE | LU1525412281 | 14.000 | 15,6 % | 0 % | 0,35 % |
| **RF titulizaciones** | Aegon European ABS A EUR Acc | IE00BG226Z29 | 6.000 | 6,7 % | 0 % | 0,66 % |
| **RF ligada a inflación** | iShares Euro Gov Inflation-Linked D Acc | IE00BD0NC144 | 4.000 | 4,4 % | 0 % | 0,10 % |
| **Liquidez operativa** | AXA Trésor Court Terme C | FR0000447823 | 4.000 | 4,4 % | 0 % | 0,05 % |
| | **TOTAL** | | **90.000** | **100 %** | | **0,224 %** |

**Reparto estricto:** RV **53.649 € (59,6 %)** · RF + liquidez **36.351 € (40,4 %)**. El colchón de
10.000 € en Groupama Trésorerie queda **fuera** de la base y no se toca.

**Por qué esos tamaños:**

| Posición | € | En una frase |
| --- | --: | --- |
| MSCI World | 28.000 | El núcleo: 1.200 empresas de 23 países al 0,12 %, sin apuesta de gestor |
| Emergentes | 7.000 | 13 % de la RV: el bloque más barato (10,2x) y el que más crece; 42 % es tecnología |
| Europa | 6.000 | La sobreponderación que paga la valoración (13,6x frente a 18,7x) al 0,10 % |
| Small Cap | 5.000 | El factor que no está en el núcleo: 4.100 empresas fuera del MSCI World |
| REITs | 5.000 | Renta de alquiler y activos reales al 0,17 %, sin dividendo |
| Japón | 3.000 | Diversificador con divisa distinta y gobierno corporativo en mejora |
| Amundi 1-5Y | 14.000 | El corazón del bloque defensivo: 100 % corporativo IG euro, sin gestor |
| Neuberger | 8.000 | La mitad de lo que pesa hoy: mejor carry/riesgo de su familia, pero no el 24 % del capital |
| Aegon ABS | 6.000 | Crédito fuera del corporativo: 58 % ABS + 35 % RMBS, volatilidad 0,98 % |
| Linker | 4.000 | Seguro de inflación, no rentabilidad: 4,4 % del capital |
| AXA Trésor | 4.000 | Colchón operativo para rebalancear sin vender bolsa en el peor día |

---

## 4. Por qué cada fondo, con la pega en la misma fila

| Fondo | El dato | Papel | La pega, dicha |
| --- | --- | --- | --- |
| **Fidelity MSCI World 0,12 %** | 3A +18,93 % · 5A +10,91 % · vol 11,17 % · 72,1 % EE. UU. · 30,4 % tecnología | Núcleo global | **El 72 % es EE. UU. y el 30 % tecnología**; cuesta 6 pb más que el iShares S (0,06 %): 16,80 €/año por historial a 5 años y liquidación en 2 días |
| **iShares Europe 0,10 %** | 3A +17,61 % · 5A +9,81 % · vol 10,30 % | Beta barata donde la valoración paga | **24,7 % servicios financieros y 21,3 % Reino Unido**: no es «Europa limpia» |
| **Fidelity Japan 0,10 %** | 3A +17,54 % · 5A +9,20 % · vol 12,72 % · 98,6 % Japón | Diversificador con otra divisa | 22 % industria y 20 % tecnología; **el yen lleva una década débil y eso resta en euros** |
| **iShares EM S 0,16 %** | 1A +18,37 % · YTD +20,07 % · vol 27,3 % · Taiwán 27 % + Corea 21 % + China 19 % | Única puerta a los emergentes | **42 % tecnología** y sin 3A/5A publicados (clase S reciente); la vol a 1 año es 27 % |
| **iShares Dev. Real Estate 0,17 %** | 3A +10,45 % · 5A +0,92 % · 2022 −20,1 % · 65 % EE. UU. | Activos reales con renta | **Década plana (5A +0,9 %)** y es RV: cae con los tipos, no protege de ellos |
| **Vanguard Global Small-Cap 0,29 %** | 3A +17,95 % · 5A +6,45 % · vol 13,85 % · 4.100 empresas | El tramo que el MSCI World no tiene | **La línea más cara de la RV** y el 61 % es EE. UU.; solapa con el núcleo en las grandes |
| **Neuberger Short Duration 0,38 %** | 3A +4,40 % · 5A +2,30 % · vol 1,97 % · 2022 −5,68 % · TIR 4,65 % · dur. 1,95 | Amortiguador con cupón | **15 % Reino Unido y 14 % EE. UU. de emisores**, 76 % corporativo; 1A +0,44 %: el carry no se está cobrando |
| **Amundi 1-5Y 0,35 %** | 3A +3,48 % · 5A +0,76 % · vol 2,22 % · 2022 −8,92 % · 100 % corporativo IG euro | El riesgo de crédito, sin gestor | **Rinde ≈0,9 pp menos que el Neuberger** a 3A; filtro ESG que excluye emisores; TIR no publicada |
| **Aegon European ABS 0,66 %** | 3A +4,39 % · 5A +3,01 % · vol 0,98 % · 2022 −4,0 % · 58 % ABS + 35 % RMBS | Crédito descorrelacionado | **La línea más cara del bloque (0,66 %)** y 31 % Reino Unido + 23 % Irlanda: es titulización, no bono |
| **iShares Inflation-Linked 0,10 %** | 3A +1,81 % · 5A **−0,77 %** · vol 4,34 % · 2022 −8,7 % | Seguro de inflación | **Cinco años perdiendo**; duración real larga (≈7,5) y la ficha no desglosa la cartera (100 % «otros») |
| **AXA Trésor 0,05 %** | 1A +2,27 % · vol 0,06 % · €STR − 5 pb | Liquidez operativa | **No da retorno real** (2,27 % con inflación 3,8 %); 4,4 % del capital es el precio de no vender bolsa en una caída |

Ninguno reparte dividendos: `distributing = 0` en los once, verificado en ficha el 16/11/2026.

---

## 5. Diversificación, medida

### 5.1 Geografía de la RV (look-through, sobre 53.649 €)

| Región | % de la RV | € |
| --- | ---: | ---: |
| Estados Unidos | **49,0 %** | 26.288 |
| Europa (Reino Unido, Suiza, Alemania, Francia, Países Bajos, España, Italia y otros) | **16,1 %** | 8.609 |
| Emergentes (Taiwán 27 %, Corea 21 %, China 19 %, India 11 %, Brasil 4 %) | **13,1 %** | 7.000 |
| Japón | **10,3 %** | 5.541 |
| Canadá | 2,2 % | 1.155 |
| Pacífico ex-Japón (Australia, Singapur, Hong Kong) | 1,4 % | 763 |
| Otros desarrollados y no desglosado | 8,0 % | 4.294 |

Frente a un MSCI ACWI (≈64 % EE. UU., 15 % Europa, 10 % emergentes, 5 % Japón): **−15 pp de EE. UU.,
+3 pp de emergentes, +5 pp de Japón y Europa en línea**. Es un sesgo por valoración, no una apuesta
contra el dólar.

### 5.2 Sectores de la RV

| Sector | % de la RV |
| --- | ---: |
| Tecnología | 24,9 % |
| Servicios financieros | 15,9 % |
| Industria | 11,2 % |
| Inmobiliario | 9,8 % |
| Salud | 8,1 % |
| Consumo cíclico | 7,8 % |
| Servicios de comunicación | 5,1 % |
| Consumo defensivo | 0,9 % |
| Materiales básicos | 0,8 % |
| Resto y no desglosado | 16,1 % |

Tecnología al 24,9 % frente al 30,8 % de un MSCI World: **6 pp menos** sin renunciar al sector. El
25 % de financieros + industria + inmobiliario es lo que da el perfil distinto al de la cartera actual.

### 5.3 Concentración por gestora

| Gestora | € | % cartera |
| --- | ---: | ---: |
| Fidelity | 31.000 | 34,4 % |
| BlackRock / iShares | 22.000 | 24,4 % |
| Amundi | 14.000 | 15,6 % |
| Neuberger Berman | 8.000 | 8,9 % |
| Aegon | 6.000 | 6,7 % |
| Vanguard | 5.000 | 5,6 % |
| AXA | 4.000 | 4,4 % |

**Fidelity al 34,4 % es la pega de esta cartera**: es un proveedor de fondos índice, sin riesgo de
gestión, pero concentra el 34 % del capital. Si se quiere bajar del 25 %, se parte el núcleo con
`Amundi Index MSCI World IE-C` (LU0996181599, 0,20 %): +6,40 €/año y una línea más.

### 5.4 Divisas (sin cobertura)

EUR ≈ 41 % · USD ≈ 29 % · JPY ≈ 6 % · GBP ≈ 4 % · CHF ≈ 1 % · divisas emergentes ≈ 8 % · CAD y
otros desarrollados ≈ 3 % · no desglosado ≈ 8 %. **No se cubre divisa**: la cobertura a 10 años cuesta
1,5-2 % anual y se come el premio. La cartera no tiene ninguna clase cubierta.

### 5.5 Riesgo de tipos

| Bloque | € | Duración | Euro-duración | +100 pb |
| --- | --: | --: | --: | --: |
| Neuberger | 8.000 | 1,95 | 15.600 | −156 € |
| Amundi 1-5Y | 14.000 | ≈2,9 (est.) | 40.600 | −406 € |
| Aegon ABS | 6.000 | ≈1,5 (est.) | 9.000 | −90 € |
| Linker | 4.000 | ≈7,5 (est.) | 30.000 | −300 € |
| AXA Trésor | 4.000 | 0,1 | 400 | −4 € |
| **Total** | **36.000** | **2,66** | **95.600** | **−956 €** |

La cartera actual tiene 3,83 años de duración y −2.360 € por +100 pb sobre 61.600 € de RF. **El
riesgo de tipos se reduce a menos de la mitad** aunque la cartera tenga 28 pp más de bolsa.

---

## 6. Coste y métricas

### 6.1 Coste verificado

| Fondo | € | TER | €/año |
| --- | --: | --: | --: |
| Fidelity MSCI World | 28.000 | 0,12 % | 33,60 |
| iShares Europe | 6.000 | 0,10 % | 6,00 |
| Fidelity Japan | 3.000 | 0,10 % | 3,00 |
| iShares EM | 7.000 | 0,16 % | 11,20 |
| iShares REITs | 5.000 | 0,17 % | 8,50 |
| Vanguard Small-Cap | 5.000 | 0,29 % | 14,50 |
| Neuberger | 8.000 | 0,38 % | 30,40 |
| Amundi 1-5Y | 14.000 | 0,35 % | 49,00 |
| Aegon ABS | 6.000 | 0,66 % | 39,60 |
| iShares Linker | 4.000 | 0,10 % | 4,00 |
| AXA Trésor | 4.000 | 0,05 % | 2,00 |
| **Total** | **90.000** | **0,224 %** | **201,80** |

TER publicados en las once fichas. **Cero comisiones de éxito.** No se incluye la custodia: si
MyInvestor la cobrara en fondos (0,15 %), serían 135 €/año más; la cartera manual actual se mide sin
ella, así que la comparación es homogénea.

### 6.2 Actual frente a propuesta

| Métrica | Actual (30/10/2026) | **Propuesta** | Delta |
| --- | ---: | ---: | ---: |
| Renta variable (look-through) | 31,6 % | **59,6 %** | +28,0 pp |
| Renta fija + liquidez | 68,4 % | **40,4 %** | −28,0 pp |
| TER anual | 671 € (0,746 %) | **202 € (0,224 %)** | **−469 €/año (−70 %)** |
| Comisiones de éxito | 3 fondos (20 %, 20 %, 9 %) | **0** | — |
| Duración RF | 3,83 | **2,66** | −1,17 |
| Coste de +100 pb | −2.360 € | **−956 €** | +1.404 € |
| Carry RF (TIR ponderada) | 5,39 % = 2.965 € | **3,97 % = 1.428 € (est.)** | −1,42 pp |
| Caída tipo 2008 | −14,7 % = −13.220 € | **−25,1 % = −22.550 €** | −9.330 € |
| Retorno esperado (solo EY) | 5,79 % | **5,57 %** | −0,22 pp |
| Retorno esperado (EY + 4 %) | 7,06 % | **7,95 %** | +0,89 pp |
| Posiciones | 8 manuales + 9 de Rock | **11** | −6 |
| Posición mayor | Neuberger 24,4 % | **MSCI World 31,1 %** (índice) | +6,7 pp |
| EE. UU. dentro de la RV | ≈47 % | **49,0 %** | +2,0 pp |

**El carry es una estimación.** Solo el 4,65 % del Neuberger está publicado (ficha de la gestora a
30/09/2026). Del resto: Amundi 1-5Y **3,90 %** (inferido de su 3A y la curva actual), Aegon **4,30 %**,
linker **4,00 % nominal** (real ≈0,5 % + inflación), AXA **2,30 %** (€STR). Rango razonable del bloque:
**3,8-4,2 % (1.370-1.510 €/año)**. El 3,97 % es el centro, no un dato de ficha.

---

## 7. Lo que se descarta, con el número

### 7.1 Rock: el argumento de la plusvalía ya no aplica

La cartera actual dice que Rock «no se desmonta» porque cristalizaría el +83,44 % acumulado desde
2020. **Eso es verdad solo si se vende.** MyInvestor permite cancelar la cartera automatizada
eligiendo «traspasar todos los fondos a un fondo»: la plataforma traspasa los nueve fondos a un
monetario y desde ahí se traspasan a los fondos que se quieran, **sin impacto fiscal** (plazo máximo
10 días). Es un traspaso entre IIC, no un reembolso.

El precio de no hacerlo: 30.000 € al 0,41 % = **123 €/año**, un 78/22 con el 33 % en S&P 500 y 3.000 €
en un bono euro a 20+ años que perdió **−17,03 %** en 2026, y un bloque que impide rebalancear. El
precio de venderlo en efectivo sería ≈**2.590 €** de impuestos. Por el puente: **0 €**.

### 7.2 Fondos que salen

| Fondo actual | € | Ficha | Por qué sale |
| --- | --: | --- | --- |
| DNCA Alpha Bonds | 13.000 | 1,31 % + éxito 20 % · 3A +4,12 % | Retorno absoluto con 27 % liquidez y futuros; pagar el 20 % del resultado por 4,12 % a 3 años no se defiende |
| Carmignac Credit | 12.000 | 1,20 % + éxito 20 % · BBB− · max DD −17,5 % | Es el risco de crédito de la cartera con comisión de éxito y 22 % liquidez; su TIR 6,5 % es prima de BBB−, no carry libre |
| Gamma Global | 8.000 | 0,95 % + éxito 9 % · TIR 8,07 % | 81 % corporativo con Noruega 17 %, Grecia 8 % y Ghana 8 %; energía y GNL. No es un mixto defensivo |
| MyInvestor Value C | 2.000 | TER **no publicado** | Sin coste verificable no entra en una cartera indexada |
| Cobas International P | 1.000 | 2,33 % · soft close | La línea más cara del catálogo y el 39 % del coste manual para 1.000 €; su alpha no se puede dimensionar |
| NB Next Gen Space | 1.000 | 1,90 % · vol 35,75 % | Temática de 1.000 €: no mueve la cartera y añade el riesgo más alto de la lista |
| UBS MSCI China | 1.000 | 0,30 % | China ya está al 19,5 % del fondo de emergentes; una posición de 1.000 € no diversifica, decora |

### 7.3 Alternativas evaluadas y descartadas

| Candidato | Ficha | Por qué no |
| --- | --- | --- |
| iShares Developed World S (IE000ZYRH0Q7) | **0,06 %** · sin 3A/5A | El más barato del mundo desarrollado, pero la clase S no publica historial a 3-5 años y liquida en 4 días; 6 pb = 16,80 €/año no justifican quedarse sin serie |
| iShares Euro IG Corporate (IE00BDRK7J14) | 0,12 % · 2022 **−13,26 %** | Duración ≈5: perdió 13 pp en 2022. Es el error que el bloque defensivo no debe repetir |
| Vanguard Euro IG (IE00B04FFJ44) | 0,12 % · 2022 **−15,19 %** | Misma duración larga y peor año malo que el Amundi 1-5Y |
| Lazard Euro Short Duration SRI | TER 0,04 % + éxito 20 % · HY | El «TER 0,04 %» no cuadra con una gestión del 0,50 %; calidad crediticia declarada de alto rendimiento |
| iShares Global Aggregate 1-5Y EUR H | 0,08 % · 1A +0,11 % | 36 % EE. UU. y 12,5 % China para rendir 0,11 %: no compite con el 4,65 % del Neuberger |
| Amundi Prime Euro Gov (LU2339731064) | 0,05 % · mínimo **500.000 €** | No es contratable |
| Cobas Large Cap / Selección | 0,96-2,05 % | Value activo con 4-5 años irregulares y coste 8-17 veces el índice europeo |
| Oro vía fondo (DWS, Jupiter) | 1,61-1,66 % · vol 38 % | El único oro del catálogo cuesta 1,6 %, el doble que toda la cartera nueva; el físico solo existe como ETF |
| Cat bonds (GAM, Twelve) | 3A +9-11 % · TER 1,28-1,55 % | Otro activo (ILS), reembolso a 10 días y coste alto para 4-6 % de la cartera |
| ETFs MSCI World ex-USA (XUSE, EXUS) | 0,15 % | Un ETF no admite traspaso: cada rebalanceo tributa al 19-23 % |
| Mixtos baratos tipo Baelo | 0,64 % | Devuelve el control del riesgo a un tercero y duplica el coste del bloque indexado |

### 7.4 ¿Y un fondo value?

**No existe un indexado value en el catálogo.** El único marcado como pasivo, `Core Value Global`
(ES0124101009), es en realidad un fondo español de gestión activa: **TER no publicado**, 8 % de
comisión de éxito, nacido en **febrero de 2026** (9 meses de historial) y 15,3 % en liquidez. No hay
nada que juzgar.

Los value activos que sí existen, con la ficha delante:

| Fondo | TER | 3A | 5A | 2022 | Vol 3A | La pega |
| --- | --: | --: | --: | --: | --: | --- |
| Magallanes European Equity R | 1,95 % | +16,0 % | +11,9 % | +5,2 % | 12,7 % | **70 % en industria, materiales y consumo**; 94 % RV, 6 % liquidez |
| Cobas Palm Harbour Global Value F | 1,02 % | +15,4 % | +8,9 % | −2,6 % | 8,6 % | Global y barato para ser activo, pero **5A 2 pp por debajo del World** |
| Incometric Equam Global Value A | 0,58 % + éxito 8 % | +11,4 % | +7,7 % | −3,7 % | 11,2 % | Small caps Europa, mínimo 1.000 €, **8 % de éxito** |
| Value Tree European Equities | 2,45 % + éxito 5 % | +15,3 % | +6,9 % | −7,6 % | 10,3 % | **«Fondo no traspasable»** en la propia ficha |
| Cobas International P | 2,33 % | +26,5 % | +17,1 % | — | 12,3 % | Soft close y ~40 posiciones: **el único alpha claro, y el más caro** |

El test no es «¿es value?», es **«¿bate a su índice después de 1-2 % de comisión?»**. Magallanes gana
2,1 pp a 5A y pierde 1,6 pp a 3A; Cobas Palm Harbour e Incometric pierden ≈2 pp a 5A; Value Tree ni se
puede traspasar. **El único con alpha verificable es Cobas International** (+17,1 % a 5A frente a
+10,9 % del World), y por eso la propuesta anterior lo mantenía con 5.000 €: aquí se cae por **2,33 %
de TER, soft close y 40 posiciones**.

Lo que la cartera **sí** lleva es el sesgo value barato, sin pagar gestor: Europa al 13,6x con 25 % de
financieros y 19 % de industria, emergentes al 10,2x, small caps con 18,5 % de industria y 13,8 % de
financieros, y el 49 % de EE. UU. en vez del 64 % de un ACWI. Un 6 % en un fondo de 40 valores no
diversifica: sustituye el índice por la opinión de una persona.

Si aun así se quiere uno, el menos malo es **Cobas Palm Harbour Global Value** (1,02 %, global, 5A
+8,9 %, vol 8,6 %, 2022 −2,6 %): 5.000 € que salen del MSCI World, doce líneas y **+45 €/año** de
coste. Es una apuesta declarada, no una mejora: el fondo lleva 2 pp por detrás del índice a 5 años.

---

## 8. Riesgos y límites

- **La caída es real:** −22.550 € en un escenario tipo 2008. Si en ese momento se vende, el diseño no
  vale; la cartera correcta sería 50/50 (−19.350 €). Está escrito antes de ejecutar, no después.
- **Se renuncia a 1,42 pp de carry** (≈500 €/año sobre el bloque de RF actual) a cambio de quitar
  BBB−, Ghana y comisiones de éxito. Si el crédito no se tensa, esta decisión se verá peor durante
  un tiempo. Es una decisión de calidad, no una previsión.
- **El linker puede perder dinero en un shock de tipos** (2022: −8,7 %). Es seguro de inflación a 10
  años, no un amortiguador de 2022.
- **Fidelity al 34,4 %** y **EE. UU. al 49,0 % de la RV**: dos concentraciones declaradas. La primera
  es operativa, la segunda es una apuesta de valoración de 15 pp contra el índice mundial.
- **Emergentes al 13 % de la RV con 42 % de tecnología**: si Taiwán/Semis corrigen, la cartera lo ve.
- **El yen** puede seguir débil y restar al bloque japonés en euros.
- **Rock tarda hasta 10 días** en pasar por el monetario: 30.000 € fuera del mercado ese tiempo.
  Puede pillar una subida o una caída; no se puede eliminar.
- **Comisión de suscripción:** Amundi y Aegon publican máximos de folleto (4,50 % y 5,00 %). Se debe
  comprobar en la app antes de ordenar; si apareciera, son 630 € y 300 €, más que **dos años** de ahorro.
  En ese caso, Amundi → Neuberger (hasta 20.000 €) y Aegon → iShares Euro IG (0,12 %, aceptando
  duración 5).
- **TER sin custodia:** si MyInvestor cobrara custodia en fondos, +135 €/año.
- **Ninguna cifra de retorno está prometida.** El 5,57 % y el 7,95 % salen de dos fórmulas, no de un
  backtest.

---

## 9. Las operaciones

**Todo por traspaso entre fondos armonizados: 0 € de impuestos.** 17 traspasos y una cancelación, en
dos sesiones de órdenes.
La base es `cartera-actual.md` (90.000 €: 60.000 manuales sin el colchón + 30.000 de Rock).

### 9.1 Paso 0 — antes de ordenar nada

- [ ] **Colchón:** confirmar que los 10.000 € de Groupama cubren 6-12 meses de gasto real. No se toca.
- [ ] **Saldos:** Neuberger 22.000 · DNCA 13.000 · Carmignac 12.000 · Gamma 8.000 · MyInvestor Value
      2.000 · Cobas 1.000 · Space 1.000 · China 1.000 = **60.000 €**.
- [ ] **Reembolso 0,00 %** en los ocho fondos que salen (verificado el 31/10/2026 en los cinco
      principales; mirar Cobas, Space y China en la app).
- [ ] **Suscripción:** mirar en la app la comisión de Amundi 1-5Y y Aegon ABS. Si es 0, se sigue; si no,
      se aplica el plan B de §8.
- [ ] **Rock:** «Ver más opciones» → «Cancelar cartera» → «Traspasar a un fondo». No elegir «recibir el
      dinero en efectivo».

### 9.2 Sesión 1 (día 0) — cancelar Rock y 10 traspasos manuales

| # | Origen | € | Destino |
| --: | --- | --: | --- |
| 1 | **Rock** (cancelación → monetario) | 30.000 | AXA Trésor Court Terme (puente) |
| 2 | Neuberger Short Duration | 14.000 | Amundi EUR Corporate 1-5Y |
| 3 | DNCA Alpha Bonds | 13.000 | Fidelity MSCI World |
| 4 | Carmignac Portfolio Credit | 8.000 | Fidelity MSCI World |
| 5 | Carmignac Portfolio Credit | 4.000 | iShares Emerging Markets |
| 6 | Gamma Global | 5.000 | Fidelity MSCI World |
| 7 | Gamma Global | 3.000 | Fidelity MSCI Japan |
| 8 | MyInvestor Value C | 2.000 | iShares Developed Real Estate |
| 9 | Cobas International | 1.000 | Vanguard Global Small-Cap |
| 10 | NB Next Generation Space | 1.000 | Vanguard Global Small-Cap |
| 11 | UBS MSCI China | 1.000 | iShares Europe |

**Cortes (hora límite de la ficha):** iShares Europe y emergentes **09:00**; Neuberger y AXA Trésor
**10:00**; Amundi, Aegon y REITs **12:00**; Fidelity World, Fidelity Japan y Vanguard Small-Cap
**16:00**. El Neuberger se queda con 8.000 €.

### 9.3 Sesión 2 (cuando Rock esté en el monetario, 5-10 días) — 7 traspasos

| # | Origen | € | Destino |
| --: | --- | --: | --- |
| 12 | AXA Trésor (puente Rock) | 2.000 | Fidelity MSCI World |
| 13 | AXA Trésor (puente Rock) | 5.000 | iShares Europe |
| 14 | AXA Trésor (puente Rock) | 3.000 | iShares Emerging Markets |
| 15 | AXA Trésor (puente Rock) | 3.000 | iShares Developed Real Estate |
| 16 | AXA Trésor (puente Rock) | 3.000 | Vanguard Global Small-Cap |
| 17 | AXA Trésor (puente Rock) | 6.000 | Aegon European ABS |
| 18 | AXA Trésor (puente Rock) | 4.000 | iShares Euro Government Inflation-Linked |
| 19 | AXA Trésor (puente Rock) | 4.000 | **se queda** como liquidez operativa |

Si el fondo puente que elige MyInvestor no es AXA Trésor, los 4.000 € de liquidez se quedan en él si
su TER es ≤ 0,10 %; si no, se traspasan a AXA Trésor.

### 9.4 Comprobación final

- [ ] World 28.000 · Europa 6.000 · Japón 3.000 · EM 7.000 · REITs 5.000 · Small 5.000 = **54.000 €**
- [ ] Amundi 14.000 · Aegon 6.000 · Linker 4.000 · AXA 4.000 · Neuberger 8.000 = **36.000 €**
- [ ] **Total 90.000 €.** Rock a 0. DNCA, Carmignac, Gamma, MyInvestor Value, Cobas, Space y China a 0.
- [ ] RV 59,6 % / RF 40,4 %; coste **201,80 €/año**; cero comisiones de éxito.

**Cuadre por origen:** Neuberger 14.000 + DNCA 13.000 + Carmignac 12.000 + Gamma 8.000 + MyInvestor
Value 2.000 + Cobas 1.000 + Space 1.000 + China 1.000 = **52.000 €**; Rock **30.000 €**; total **82.000 €**.
**Cuadre por destino:** RV 54.000 + RF nueva 24.000 (Amundi, Aegon, linker) + liquidez 4.000 =
**82.000 €**. Los 8.000 € del Neuberger no se mueven.

### 9.5 Si ya están los 7.000 € de la aportación nueva

El `README.md` del 04/11/2026 habla de 97.000 € (67.000 manuales + 30.000 Rock) por una aportación de
7.000 € que **no aparece en la foto congelada del 30/10**. Si ya está en la cuenta, se añade sin tocar
el resto: **4.000 € a Fidelity MSCI World y 3.000 € a Amundi 1-5Y**. Queda 97.000 €, 11 posiciones,
**59,4 % de RV** y **203,33 €/año (0,210 %)**.

### 9.6 Lo que no se debe hacer

- **No reembolsar** para suscribir después: se pierde el diferimiento fiscal.
- **No cancelar Rock «en efectivo»**: esa opción sí cristaliza la plusvalía.
- **No cambiar de clase** un fondo que se queda (equivale a reembolso).
- **No comprar Aegon ABS con más de 6.000 €** ni Amundi con más de 14.000 € hasta ver un trimestre.
- **No sustituir ningún fondo por un ETF** del mismo índice: ahorra 5-10 pb y convierte cada
  rebalanceo en una factura.

---

## 10. Cuándo se revisa

Trimestral (enero, abril, julio, octubre) y siempre que cambie horizonte, necesidad de liquidez o
tolerancia. **El 60 % no se repuntúa con ninguna herramienta:** se cambia con un argumento escrito y
fechado.

- **Rock desmontado:** a los 3 meses, comparar el coste real cobrado con el 0,224 % previsto.
- **Amundi 1-5Y:** a los 6 meses, comparar con el Neuberger. Si la brecha a 3A pasa de 1,5 pp, el
  Neuberger recupera peso.
- **Aegon ABS:** si su 3A cae por debajo del Amundi 1-5Y dos trimestres seguidos, sus 0,66 % no se
  defienden y sale.
- **Linker:** a los 24 meses, si no ha batido al monetario con inflación > 3 %, se decide con número.
- **Small Cap y REITs:** si la suma de ambos supera el 14 % de la cartera en una revalorización, se
  recorta al 5 % cada uno.
- **Rebalanceo:** si un bloque se desvía más de 5 pp. Bandas: RV 55-65 %, Europa 5-8 %, EM 6-9 %.
- **Fidelity:** si supera el 35 % de la cartera, se parte el núcleo con Amundi MSCI World.

---

## 11. Fuentes

- **Fichas MyInvestor MCP a 16/11/2026** (NAV 12/11/2026): `list_facets` (2.409 fondos, 266 indexados),
  `search_funds` por bloques, `get_funds` por ISIN de los once fondos. TER, 3A/5A, volatilidad, SRRI,
  países, sectores, mínimo, corte y `distributing = 0`.
- **`cartera-actual.md`** (30/10/2026): saldos, ISIN, composición de Rock, duración y carry.
- **`propuesta-actual.md`** (04/11/2026): *earnings yield* 6,65 %, valoraciones (S&P 500 18,7x, STOXX
  600 13,6x, MSCI EM 10,2x), inflación 3,8 % y €STR/BCE.
- **MyInvestor, FAQ de carteras automatizadas:** cancelar la cartera permite «traspasar todos los
  fondos a un fondo sin impacto fiscal» (fondo puente monetario, plazo máximo 10 días).
- **Comisiones de reembolso:** verificación del 31/10/2026 en los cinco fondos principales que salen.

Límites: TIR y duración de Amundi, Aegon, linker y monetario **no están publicadas** (3,90 %, 4,30 %,
4,00 % y 2,30 %; duraciones 2,9 / 1,5 / 7,5 / 0,1, inferidas); el 44 % de la cartera de Cobas no
desglosa país; la volatilidad y el carry de Rock no se publican; drawdown y retorno esperado son
estimaciones propias; los gastos del colchón siguen sin dimensionar.

> No es asesoramiento financiero. La decisión es del titular.

---
title: "Propuesta de investigación — dos bloques de acumulación, sin acciones que repartan"
date: 2026-11-02
type: portfolio-research
category: finance
tags: [cartera, investigacion, calidad, activos-reales, reits, fundsmith, acumulacion, horizontes, myinvestor]
status: research
related: [finance/portfolio/cartera-myinvestor/cartera-actual.md, finance/portfolio/cartera-myinvestor/propuesta-actual.md, finance/portfolio/cartera-myinvestor/propuesta-alternativa.md]
---

# Propuesta de investigación — 02/11/2026 (reajustada)

> **No es la cartera vigente.** La vigente sigue siendo `propuesta-actual.md` (50,0% RV / 50,0% RF,
> 97.000 €, 8 fondos manuales + Rock). Este documento es una capa de investigación: qué bloques
> aportarían algo que la cartera no tiene, con qué vehículo y a qué precio. Si se adopta, sus
> conclusiones se incorporan a `propuesta-actual.md` y este anexo **se borra** (`git rm`).
>
> **Regla de acumulación (02/11/2026), aplicada a todo: ni fondos ni ETFs ni acciones que repartan
> dividendos.** Eso ha vaciado la versión anterior de este anexo: las cuatro acciones individuales
> (TotalEnergies 4,2 %, LVMH 3,4 %, Microsoft 0,8 %, ASML 0,5 % de rentabilidad por dividendo) y el ETF
> VanEck Global Real Estate (reparto trimestral) **salen**. La satélite de convicción desaparece como
> tal y queda en **dos vehículos de acumulación**, los dos traspasables entre fondos armonizados.
>
> **Incompatible con `propuesta-alternativa.md` (01/11/2026).** Los dos anexos salen de los mismos
> cuatro fondos y ahora además proponen **los mismos dos vehículos** (Fundsmith Acc e iShares REITs
> Acc), con pesos distintos. Se elige uno: esta versión (5.000 €, 19 posiciones) o la mínima de la
> alternativa (REITs 5.000 €, 17 posiciones). **No se ejecutan juntos.**

## 0. Resumen ejecutivo

La cartera vigente está bien construida y es barata (TER 0,655 %, 17 posiciones, 50/50, carry de renta
fija 4,79 %), pero le faltan dos cosas medibles: **0 % de factor calidad** y **0 % de activos reales**.
El tercer hueco que recogía la versión anterior —acciones directas— **deja de existir** con la regla de
acumulación: casi toda acción de calidad reparte dividendo, y las que no lo reparten exigen una tesis
propia que este documento no tiene.

| # | Bloque | Vehículo | ISIN | Tipo | € | % cartera | % RV | TER | Acumula |
|--:|---|---|---|---|---:|---:|---:|---:|---|
| 1 | Calidad global | Fundsmith Equity Fund T EUR Acc | LU0690375182 | Fondo | 3.000 | 3,1 % | 6,2 % | 1,09 % | Sí |
| 2 | Activos reales | iShares Developed Real Estate Index D Acc | IE00BDRK7P73 | Fondo | 2.000 | 2,1 % | 4,1 % | 0,17 % | Sí |

**5.000 € (5,2 % de la cartera, 10,3 % de la RV), financiados con cuatro traspasos y 0 € de impuestos.**
TER, duración y carry de la renta fija no se tocan. El 50/50 se mantiene: la bolsa no sube, se
redistribuye.

## 1. Punto de partida: qué tiene y qué le falta a la cartera actual

| Bloque | Fondo | ISIN | € | Peso | TER |
|---|---|---:|---:|---:|---:|
| RF corta IG | Neuberger Short Duration Euro Bond U | IE00BL1GVT98 | 31.900 | 32,9 % | 0,38 % |
| RF flexible | DNCA Alpha Bonds A | LU1694789451 | 5.000 | 5,2 % | 1,31 % |
| Crédito | Carmignac Credit A | LU1623762843 | 5.000 | 5,2 % | 1,20 % |
| RV value Europa small/mid | MyInvestor Value C | ES0165243025 | 5.000 | 5,2 % | ~1,42 % + 9 % éxito |
| RV value global | Cobas International P | LU1598719752 | 5.000 | 5,2 % | 2,33 % |
| RV small cap global | Vanguard Global Small-Cap Index EUR Acc | IE00B42W4L06 | 3.700 | 3,8 % | 0,29 % |
| RV Europa large cap | Fidelity MSCI Europe Index EUR P Acc | IE00BYX5MD61 | 5.000 | 5,2 % | 0,10 % |
| RV emergentes | iShares Emerging Markets Index S Acc EUR | IE000QAZP7L2 | 6.400 | 6,6 % | 0,16 % |
| Cartera indexada 78/22 | Rock (MyInvestor) | — | 30.000 | 30,9 % | 0,41 % todo incluido |
| | **TOTAL** | | **97.000** | **100 %** | |

### 1.1 Los dos huecos que quedan

| Hueco | Situación | Por qué importa | Qué lo cubre |
|---|---|---|---|
| Factor calidad | 0 % | Toda la RV es indexada o value; no hay compounders de márgenes altos y bajo capital | Fundsmith (fondo, acumulación) |
| Activos reales | 0 % | 0 % inmobiliario, 0 % infraestructura, 0 % oro; la inflación se combate con bonos y valor, no con rentas reales | iShares Developed Real Estate (fondo, acumulación) |
| ~~Acciones directas~~ | 0 % | **Cerrado el 02/11/2026 por la regla de acumulación:** las cuatro ideas de la versión anterior repartían 0,5-4,2 % de dividendo. Las acciones sin dividendo (Berkshire, Amazon, Netflix, Booking, Adyen) necesitan tesis propia con dos fuentes y precio; no se meten «por rellenar» | — |

## 2. Metodología y regla de la casa

1. **Solo clases de acumulación.** Ningún fondo, ETF ni acción que reparta dividendos. En fondos se
   verifica con el campo `distributing` de la ficha; en ETF, con el «Income Treatment» del emisor; en
   acciones, con su política de retribución al accionista.
2. **Evitar la retención en origen.** Un dividendo de una acción extranjera llega ya gravado y tributa
   otra vez en España; con acumulación ese peaje no existe.
3. **Dos fuentes independientes por vehículo**; emisor y proveedor del índice no cuentan como dos.
4. **Hecho / consenso / opinión** etiquetados en cada afirmación relevante.
5. **Traspaso siempre que se pueda.** Un fondo armonizado se traspasa sin tributar; un ETF o una acción
   obligan a reembolsar (peaje fiscal). Es la razón por la que los dos vehículos elegidos son fondos.
6. **Peso pequeño:** entre el 5 % y el 6 % de la cartera, suficiente para que pese y pequeño para que un
   error del gestor no decida la cartera.

Datos: fichas MyInvestor MCP a 28-30/10/2026 y ficha del emisor para el tratamiento de rentas.

## 3. Los dos bloques que entran

### 3.1 Calidad global — Fundsmith Equity Fund T EUR Acc (LU0690375182)

**1. Nombre e ISIN.** Fundsmith Equity Fund T EUR Acc, LU0690375182.
**2. Tipo.** Fondo activo de renta variable global, estilo *quality growth*, **acumulación**.
**3. Horizonte.** Largo plazo (>5 años).

**4. Tesis en tres frases.**
La cartera no tiene ninguna exposición a *quality compounders*: márgenes altos, poco capital y retorno
recurrente. Fundsmith compra ese perfil y lo mantiene con rotación mínima, con Morningstar en **Silver**
y los pilares Process, People y Parent en «Above Average». Llega con el historial reciente malo —**cinco
años seguidos por debajo del MSCI World**—, que es justo cuando entrar en un estilo deja de ser perseguir
el precio.

**5. Métricas clave.**

| Métrica | Valor | Contexto |
|---|---:|---|
| TER | 1,09 % | Gestión 1,00 %; sin comisión de éxito |
| Clase | Acumulación | No reparte: cumple la regla |
| Historial | Desde 2011 | +612,9 % acumulado frente a +467,6 % del índice desde 2010 |
| Rentabilidad | YTD +6,4 % · 1A +7,0 % · 3A +7,8 % anual · 5A +2,9 % anual | Cinco años por debajo del índice |
| Asignación | 100 % RV · USA 79,6 % · Tecnología 32 % · Salud 18 % | Concentración americana alta |
| Volatilidad 3A | 12,9 % | En línea con la RV global |
| Mínimo | 1 € | Sin barrera práctica |

**6. Por qué tiene sentido.** [Hecho] Aporta un estilo que la cartera no tiene y a un peso que no decide
nada (3,1 %). [Consenso] Morningstar mantiene Silver y avisa de que el historial «has been dented by
recent underperformance». [Opinión] Se compra el proceso, no el resultado reciente; si en tres años sigue
por debajo del índice, la tesis no era la calidad sino el gestor.

**7. Respaldo.** Morningstar, «Fundsmith Equity Fund Retains Appeal for Long-Term Investors», 03/06/2026
(https://global.morningstar.com/en-gb/funds/fundsmith-equity-fund-retains-appeal-long-term-investors);
Fidelity International, «Fundsmith Equity Fund: update from Terry Smith», 16/02/2026
(https://www.fidelity.co.uk/markets-insights/investing-ideas/funds/fundsmith-equity-fund-update-from-terry-smith/).
Contrapunto: Trustnet, 27/01/2025
(https://www.trustnet.com/News/13435606/should-you-buy-hold-or-fold-fundsmith-equity/), donde IBOSS duda
de que el fondo se gane la diferencia sobre el ETF de calidad al 0,25 %.

**8. Riesgos.** Persona clave (Terry Smith, 72 años, banquillo corto); 79,6 % en EE. UU.; coste 1,09 %
frente al 0,10-0,29 % del núcleo indexado; riesgo de que el estilo siga rezagado varios años.

**9. Señal de invalidación.** Tres años consecutivos por debajo del MSCI World con rotación creciente o
salida del gestor principal.

**10. Convicción.** **Media.** El bloque es correcto; el vehículo es caro y depende de una persona.

### 3.2 Activos reales — iShares Developed Real Estate Index D Acc (IE00BDRK7P73)

**1. Nombre e ISIN.** iShares Developed Real Estate Index Fund (IE) D Acc EUR, IE00BDRK7P73.
**2. Tipo.** Fondo indexado de renta variable inmobiliaria global (REITs), **acumulación**.
**3. Horizonte.** Largo plazo (>5 años).

**4. Tesis en tres frases.**
Replica el FTSE EPRA Nareit Developed: 97,4 % inmobiliario y ~400 valores, con **TER 0,17 %**. Aporta lo
que la cartera no tiene —rentas de alquiler— y **acumula las rentas en vez de repartirlas**, así que no
hay dividendo que tributar. El sector viene de una década mala y de un 2022-2023 muy duro: no se compra
en máximos.

**5. Métricas clave.**

| Métrica | Valor | Contexto |
|---|---:|---|
| TER | 0,17 % | 8 pb más barato que el ETF VanEck (0,25 %) |
| Clase | Acumulación | Sin reparto; verificado en la ficha del fondo |
| Historial | Desde 2012 | Cumple el filtro de trayectoria |
| Rentabilidad | YTD +10,2 % · 1A +10,8 % · 3A +10,7 % anual | 5A +0,6 % anual: la década mala del sector |
| Composición | USA 64,8 % · Japón 8,0 % · Australia 5,6 % · Singapur 3,4 % | Diversificación limitada por el peso USA |
| Volatilidad 3A | 14,1 % | Sensible a tipos |
| Mínimo | 1 € · corte 12:00 · liquidación 4 días | Sin barrera práctica |

**6. Por qué tiene sentido.** [Hecho] 0,17 % y acumulación: la vía más barata al hueco. [Consenso] Cohen &
Steers («Listed REITs: A strong start to 2026») y SSGA («REIT resilience extends beyond interest rates»,
31/08/2026) ven balances sanos y rentas crecientes. [Contrapunto] S&P Global («European REIT 2026
Mid-Year Outlook: Higher Rates») avisa de coberturas de intereses ajustadas en 2026-2027.

**7. Respaldo.** BlackRock, ficha del fondo a 29/10/2026 (TER 0,17 %, clase D Acc, 97,4 % inmobiliario);
Cohen & Steers, «Listed REITs: A strong start to 2026 and what's driving performance»
(https://www.cohenandsteers.com/insights/listed-reits-a-strong-start-to-2026-and-whats-driving-performance/);
SSGA, 31/08/2026. Contrapunto: S&P Global, informe de REITs europeos 2026.

**8. Riesgos.** Tipos de interés (un 10 años al alza comprime valoraciones y refinanciación); 64,8 % USA;
5 años al 0,6 % anual demuestran que puede pasar una década plana; no protege en una caída de bolsa
(es renta variable).

**9. Señal de invalidación.** Bono alemán a 10 años >4,5-5 % sostenido; recortes de renta o guías a la
baja en varios REITs del índice.

**10. Convicción.** **Media.** Es el hueco correcto; el activo es sensible a tipos y no es un refugio.

### 3.3 La variante barata del bloque de calidad: IS3Q (IE00BP3QZ601)

Mismo estilo al **0,25 %** en vez del 1,09 %: **iShares Edge MSCI World Quality Factor UCITS ETF**
(IS3Q.DE, IE00BP3QZ601), 290 posiciones, 6.000 M€, **acumulación** confirmada en la ficha del emisor
(«Use of Income: Accumulating»).

**La pega, y es la que decide:** es un **ETF**, no un fondo. Comprarlo obliga a reembolsar el fondo de
origen —tributa por la plusvalía latente— así que rompe la regla de la carpeta («traspaso, nunca
reembolso»). Solo tiene sentido con **aportación nueva**.

| Opción | Vehículo | Coste 3.000 €/año | Fiscalidad |
|---|---|---:|---|
| A (con traspaso) | Fundsmith T Acc | 32,7 € | 0 € |
| B (solo con dinero nuevo) | IS3Q Acc (ETF) | 7,5 € | 0 € si no se reembolsa nada |

## 4. Cartera modelo propuesta (97.000 €)

| Bloque | Fondo/Activo | ISIN | € | Peso | TER |
|---|---|---|---:|---:|---:|
| RF corta IG | Neuberger Short Duration Euro Bond U | IE00BL1GVT98 | 31.900 | 32,9 % | 0,38 % |
| RF flexible | DNCA Alpha Bonds A | LU1694789451 | 5.000 | 5,2 % | 1,31 % |
| Crédito | Carmignac Credit A | LU1623762843 | 5.000 | 5,2 % | 1,20 % |
| RV value Europa small/mid | MyInvestor Value C | ES0165243025 | 4.000 | 4,1 % | ~1,42 % + éxito |
| RV value global | Cobas International P | LU1598719752 | 4.000 | 4,1 % | 2,33 % |
| RV small cap global | Vanguard Global Small-Cap Index EUR Acc | IE00B42W4L06 | 2.200 | 2,3 % | 0,29 % |
| RV Europa large cap | Fidelity MSCI Europe Index EUR P Acc | IE00BYX5MD61 | 3.500 | 3,6 % | 0,10 % |
| RV emergentes | iShares Emerging Markets Index S Acc EUR | IE000QAZP7L2 | 6.400 | 6,6 % | 0,16 % |
| **Calidad global** | **Fundsmith Equity Fund T EUR Acc** | **LU0690375182** | **3.000** | **3,1 %** | **1,09 %** |
| **Activos reales** | **iShares Developed Real Estate D Acc** | **IE00BDRK7P73** | **2.000** | **2,1 %** | **0,17 %** |
| Cartera indexada 78/22 | Rock (sin cambios) | — | 30.000 | 30,9 % | 0,41 % |
| | **TOTAL** | | **97.000** | **100 %** | |

**Verificación del 50/50.** RV = Rock 23.400 (78 % de 30.000) + fondos manuales 20.100 + satélite 5.000 =
48.500 € = 50,0 %. RF = Neuberger 31.900 + DNCA 5.000 + Carmignac 5.000 + Rock 6.600 = 48.500 € = 50,0 %.

### 4.1 Cómo se financia: cuatro traspasos, 5.000 €

| # | Origen | ISIN origen | € | Destino | ISIN destino |
|--:|---|---|---:|---|---|
| 1 | Vanguard Global Small-Cap Index EUR Acc | IE00B42W4L06 | 1.500 | Fundsmith Equity Fund T EUR Acc | LU0690375182 |
| 2 | Fidelity MSCI Europe Index EUR P Acc | IE00BYX5MD61 | 1.500 | Fundsmith Equity Fund T EUR Acc | LU0690375182 |
| 3 | MyInvestor Value C | ES0165243025 | 1.000 | iShares Developed Real Estate D Acc | IE00BDRK7P73 |
| 4 | Cobas International P | LU1598719752 | 1.000 | iShares Developed Real Estate D Acc | IE00BDRK7P73 |
| | **Total** | | **5.000** | | |

Los cuatro traspasos son **entre fondos armonizados: 0 € de impuestos**. Salen 1.500 € del small cap
pasivo —la tercera apuesta al mismo factor, 61 % USA—, 1.500 € de Europa large cap, y 1.000 € de cada
value, que se quedan en 4.000 € (por encima del umbral de fragmentación). **No se toca la renta fija ni
Rock.** Pendiente: confirmar el 0 % de reembolso de los cuatro orígenes en la plataforma.

### 4.2 Métricas antes y después

| Métrica | Cartera vigente | **Propuesta** | Diferencia |
|---|---:|---:|---:|
| Renta variable | 50,0 % | **50,0 %** | 0 |
| Activos reales (REITs) | 0 % | **2,1 %** | +2,1 pp |
| Factor calidad (directo) | 0 % | **3,1 %** | +3,1 pp |
| Acciones directas | 0 % | 0 % | 0 (hueco cerrado por la regla) |
| Nº de posiciones | 17 | **19** (17 + 2) | +2 |
| TER con éxito estimado | 0,655 % · 635 €/año | **0,647 % · 628 €/año** | −7 €/año |
| Exposición USA de la RV | 32,5 % | **≈38,1 %** | **+5,6 pp** |
| Caída estimada 2008 | ≈ −21,5 % | **≈ −21,5 %** | igual |
| Duración RF · carry | 3,67 a · 4,79 % | igual | igual |

**El coste real, dicho sin maquillaje:**

- **Sube EE. UU. 5,6 puntos** (32,5 % → 38,1 % de la RV) por Fundsmith (79,6 % USA) y los REITs (64,8 %).
  Sigue por debajo del 63 % de un MSCI World, pero es el movimiento contrario al que la propuesta
  defiende; se compensa en parte porque sale el small cap (61 % USA).
- **Recorta el value un 20 %** (10.000 → 8.000 €). Si el ciclo value sigue delante, esta cartera lo verá
  peor: es una decisión de estilo, no de coste.
- **No diversifica la caída.** Calidad y REITs son renta variable: en un escenario tipo 2008 la cartera
  cae igual. Lo que se compra es diversificación de fuentes de retorno, no protección.
- **El coste total baja en euros** (−7 €/año) porque lo que sale (Cobas al 2,33 %) es más caro que lo que
  entra; pero el peso en gestión activa sube y eso no se mide en el TER.

### 4.3 Versión mínima

Si solo se quiere cubrir un hueco, **REITs 2.000 €** financiados con el small cap pasivo (1.000 €) y
Europa (1.000 €): 18 posiciones, TER ≈0,65 % (635 €/año con la comisión de éxito), USA en ≈33,9 % de la
RV. Es la versión que menos discute con la propuesta vigente.

## 5. Qué se descarta y por qué

| Descartado | Motivo, con el número delante |
|---|---|
| **TotalEnergies (TTE.PA)** | **Reparte 4,2 % de dividendo.** Era la idea de corto plazo de la versión anterior: PER forward 8,3x, Q3 con 9.100 M$ de beneficio y consenso 105-108 $. Con la regla de acumulación, fuera; y su tesis dependía del precio del crudo, no de la empresa |
| **LVMH (MC.PA)** | **Reparte 3,4 %.** Estaba un 35 % por debajo del valor razonable de Morningstar (590 € frente a 385,20 €) y con 5 estrellas; el dividendo la descalifica |
| **Microsoft (MSFT)** | **Reparte 0,8 %.** La mejor combinación de calidad y visibilidad de la lista anterior (ROE 34 %, Azure +40 %, 13 % bajo valor razonable). El dividendo es simbólico, pero la regla no distingue tamaños |
| **ASML (ASML.AS)** | **Reparte 0,5 %.** Monopolio EUV, guía 2026 de 44.000-45.000 M€, pedidos hasta 2028; 40x trailing. Dividendo pequeño, regla estricta: fuera |
| **VanEck Global Real Estate (TRET, NL0009690239)** | Reparto **trimestral** según la ficha del emisor, y 0,25 % frente al 0,17 % del fondo de iShares. Además es ETF: obligaría a reembolso con peaje fiscal |
| **Munich Re (MUV2.DE)** | **Reparte 4,3 %.** Ya estaba fuera de la cartera modelo por cotizar por encima del consenso (567,6 € frente a 560,9 €); la regla la cierra del todo |
| **IS3Q en la cartera modelo** | Producto excelente (0,25 %, 290 posiciones, acumulación) pero **es ETF**: exige reembolso. Se queda como opción B solo con aportación nueva (§3.3) |
| **Comgest Growth Europe (Acc)** | Cumple la regla y es traspasable, pero 1,59 % de TER y +2,8 % anual a 3 años: el hueco de calidad lo cubre Fundsmith con menos coste y más diversificación |
| **Infraestructura cotizada (Lazard / DWS)** | Lazard exige mínimo de 10.000 €; DWS cuesta 1,59 % y tiene 53 % USA. No compensa frente a los REITs al 0,17 % |
| **Oro** | Por fondo, 1,61-1,66 % y volatilidad del 38 %; por ETF físico, +67,8 % en 2025: entrar después de esa subida es perseguir el precio |
| **Salud / India como fondo** | No hay indexados en el catálogo; lo disponible es activo, caro y con historial flojo |
| **Small caps pasivas adicionales** | Ya hay dos value small/mid y una pasiva; añadir más sería la cuarta apuesta al mismo factor |

**Acciones sin dividendo que quedan fuera por falta de tesis, no por la regla:** Berkshire Hathaway,
Amazon, Netflix, Booking y Adyen no reparten. Cada una necesitaría su ficha con dos fuentes, valoración y
señal de invalidación; meterlas «porque no reparten» sería cambiar una regla por un capricho.

## 6. Lo que queda abierto

- **Elección A o B para el bloque de calidad:** Fundsmith por traspaso (32,7 €/año) o IS3Q con dinero
  nuevo (7,5 €/año). No hay tercera vía que sea a la vez barata y exenta de reembolso.
- **Comisión de entrada de Fundsmith y del iShares REITs:** el MCP no la publica; ver en la pantalla de
  suscripción.
- **Comisión de reembolso de los cuatro fondos que ceden** (Vanguard Small-Cap, Fidelity Europe,
  MyInvestor Value, Cobas): no estaban en la lista verificada de la propuesta vigente. Si alguna cobrara,
  ese traspaso se cae.
- **Peso de los REITs:** 2.000 € en esta versión frente a 5.000 € en la mínima de la alternativa.
- **Riesgo de persona clave en Fundsmith:** Terry Smith tiene 72 años y Morningstar ya recortó el pilar
  People; es el motivo para dejarlo en 3.000 € y no en 8.000 €.
- **Si algún día se quiere acción directa,** el filtro pasa a ser: sin dividendo + dos fuentes + precio.
  Berkshire y Amazon son los candidatos obvios y ninguno está analizado aquí.

---

> No es asesoramiento financiero. Los pesos son una decisión de cartera sobre fichas verificadas y fuentes
> citadas, no una previsión de rentabilidad.

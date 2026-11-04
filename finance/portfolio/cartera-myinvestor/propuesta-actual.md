---
title: "Cartera definitiva: 50/50 con ABS y crédito nórdico (97.000 €)"
date: 2026-11-03
type: portfolio-proposal
category: finance
tags: [cartera, definitiva, renta-fija, abs, aegon, sissener, rebalanceo, rock, myinvestor, traspasos, horos]
status: final
related:
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
---

# Cartera definitiva — 03/11/2026

> **Estado: definitiva, adoptada por el titular el 03/11/2026 tras revisión adversarial.** Simplifica la
> propuesta del 31/10 cambiando **dos fondos de renta fija** (entran Aegon European ABS y Sissener
> Corporate Bond en lugar de DNCA Alpha Bonds y Carmignac Portfolio Credit) **y cerrando el único hueco
> de clase de activo que quedaba en 0 %**: entra el bloque indexado de REITs (5.000 €, que sustituye al
> small cap pasivo del plan anterior). La hoja de órdenes definitiva es la de §7: las once órdenes del
> 31/10 quedan sustituidas por las **trece** de aquí. La versión del 31/10 y los anexos absorbidos
> quedan en el historial (§13 y §15). No es asesoramiento financiero; la decisión es del titular.
>
> **Cifras verificadas con la fuente:** los datos de ficha de este documento (Aegon, Sissener, DNCA,
> Carmignac, Neuberger y los REITs IE00BDRK7P73) se re-verificaron el **03/11/2026 contra las fichas
> MyInvestor vía MCP** (`get_funds`, NAV 30/10/2026): TER, comisiones de gestión y éxito,
> rentabilidades 3A/5A y por año natural, volatilidad 3A y 5A, SRRI, sectores, países, mínimos,
> cortes, incept y clase de acumulación. Cuadran todas; la novedad que trae la ficha: la **vol 5A de
> Aegon es 1,90 %** (la 0,95 % a 3 años está suavizada por el precio del ABS). El sello «ninguna
> posición dominada» de §11 se verificó el mismo día con `search_funds` sobre el catálogo.
>
> **Contraste añadido el 04/11/2026:** la charla de Horos del 30/10
> (`finance/la-pizarra-de-andres/2026-10-30-las-empresas-que-todos-ignoran-son-las-mejores-inversiones/`)
> **no cambia ninguna de las trece órdenes**. Aporta una cosa y confirma otra: entra en §14 como
> **testigo externo de carry cobrado** (su fondo de crédito, con duración 2,5 y 4,5 % esperado, lleva
> <2 %), y cierra el descarte de Horos Value Internacional de §12 con la ficha del 04/11 (TER 1,90 %;
> 3A +16,98 %; 5A +11,92 %; Francia 20,7 %, España 15,0 %; 7,2 % EE. UU.). El detalle está en
> `propuesta-alternativa.md` §0.3-§0.4.

## 1. Supuestos

- **107.000 €** totales = 10.000 € de fondo de emergencia en Groupama Trésorerie (fuera de la cartera)
  + **97.000 € invertibles** = **67.000 € manuales** (60.000 actuales + **7.000 de aportación nueva**)
  + 30.000 € en Rock.
- Horizonte largo, inversor español, plataforma MyInvestor, sin necesidad de vender para gastos.
- Todo se ejecuta por **traspaso entre fondos armonizados**: no tributa. Los 7.000 € nuevos entran
  como suscripción.
- **Regla de acumulación (02/11/2026):** ningún fondo, ETF **ni acción** de la cartera reparte
  dividendos; todas las clases son de acumulación (`distributing = 0` verificado en las fichas).
- **Regla de la casa «cada euro es RV o RF»**: no hay bloque mixto. Gamma (81 % de bonos high yield de
  energía, GNL y shipping escondidos bajo la etiqueta mixta) es el motivo por el que existe.

## 2. De dónde sale el 50 % de RV (modelo del 31/10)

**No hay perfil fijo.** El porcentaje de RV sale de seis señales que se pueden medir cada trimestre;
el perfil es la *consecuencia*, no la entrada. Base neutra para horizonte largo: 45 % de RV.

| Señal | Dato a 31/10/2026 | Efecto |
| --- | --- | ---: |
| **Coste real del dinero** | €STR 2,44 % con inflación 3,8 % daría −1,36 % real, **pero en la base no hay monetario**: la RF rinde 4,42-4,79 % → ≈ +0,85 % real | **0** |
| **Prima de crédito** | HY europeo OAS 363 pb (260-300 en normalidad) y BB a 175 pb: no se paga por asumir riesgo de crédito | **+3** |
| **Valoración relativa** | S&P 500 18,7x, STOXX 600 13,6x, MSCI EM 10,2x. Solo se aprovecha comprando Europa y emergentes | **+2** |
| **Concentración y ciclo de crédito** | 46 % del S&P en tecnología, 34 % en siete valores; Ábaco da 60-70 % de probabilidad de evento de crédito en 6-12 meses | **−5** |
| **Riesgo de tipos** | BCE con sesgo restrictivo; los ligados a inflación euro solo dan 0,3-0,5 % real: no hay refugio real en bonos largos | **+2** |
| **Capacidad de aguante** | Colchón aparte, horizonte largo, ingresos estables: no hay obligación de vender en una caída | **+3** |
| | **Total: 45 + 5 = 50 %** | |

**Decisión: 50,0 % de RV (48.500 €) y 50,0 % de RF (48.500 €).** Con la base de 90.000 € quedaba 49,3 %;
la aportación nueva permite cuadrar los importes al decimal. (El 50 % es una **convención de cálculo**
— satélites al 100 %, Rock al 78 % —, no un look-through estricto: pesando la RV real de cada ficha —
Value 95,4 %, Cobas 72,9 % — son 46.965 €, el 48,4 %; la caída estricta ≈ −20,9 %. No rebalancear:
es convención, no desfase.)

> **La señal 1 vale 0, no +5**, y se mide con la RF que la cartera tiene: puntuar con el €STR contra la
> inflación describía el monetario del colchón y llevó una versión anterior al 54,9 %. Y **el carry es
> YTW/dirección, no todavía rentabilidad cobrada** (aviso del 02/11): si el bloque cobrase ~2 % en vez
> de ~4,7 %, se activaría la señal +3 y la cartera iría a ~53 % de RV. Se mide cobrado a 12 meses en la
> primera revisión trimestral (§14). Es la única cifra que puede mover la decisión sin cambiar tesis.

| RV | RF | Caída en un escenario tipo 2008 | Retorno esperado | Real sobre inflación 3,8 % |
| ---: | ---: | ---: | ---: | ---: |
| 35 % | 65 % | −16 % | 5,4 % | +1,6 % |
| 45 % | 55 % | −20 % | 5,6 % | +1,8 % |
| **50 %** | **50 %** | **≈ −21,5 %** | **5,7 % → 5,6 %** | **+1,9 %** |
| 55 % | 45 % | −23 % | 5,8 % | +2,0 % |
| 65 % | 35 % | −27 % | 6,0 % | +2,2 % |

(El retorno esperado a 50 % pasa de 5,7 % a ≈5,6 % con el cambio de RF del 03/11: el retorno no es el
argumento; el riesgo sí, §8.) **Suelo conductual:** si una caída del −21,5 % te haría vender, el modelo
no se aplica tal cual. Baja a 45 % (−20 %) o 35 % (−16 %), por ejemplo recortando emergentes de 6.400
a 4.400 y los REITs a 2.500. Un modelo que no se aguanta no sirve.

## 3. Las reglas que la gobiernan

| Regla | Fuente | Cómo se aplica |
| --- | --- | --- |
| La duración es la decisión, no el activo | Ábaco 15:55 y 46:15; Renta 4 15:35 | ≈3,3 años con Rock (suelo matemático 2,84). El 20+ de Rock (3.000 €) es la única apuesta de duración, dicha en voz alta |
| No tomar riesgo de crédito ahora | Ábaco 28:37 y 36:47 | La pata de crédito queda en Sissener 5.000 € (IG nórdico). Gamma (81 % HY de energía/GNL/shipping) fuera, Carmignac fuera |
| El S&P 500 no es neutral | Andrés 9:36 | No se compra MSCI World: USA queda en 34,5 % de la RV frente al 63-70 % de un índice global |
| El coste se controla; la asignación, no | Andrés 9:12-13:26 | Coste real 584 €/año (0,602 %) tras la revisión final del 03/11 |
| Liquidez con regla escrita | Andrés 23-10 | 10.000 € en Groupama, fuera de la cartera. **Sin dimensionar contra gastos reales** |
| Japón aporta diversificación real | Parages 20-10 (webinar MyInvestor) | Cubierto por índice dentro de Rock; ningún satélite de Japón activo |
| Comprar donde la valoración paga | STOXX 13,6x vs S&P 18,7x; EM 10,2x | 79,4 % de la RV indexada barata; 20,6 % en dos value; emergentes al 10 % |
| Cada euro es RV o RF | regla de la casa (02/11) | Los mixtos baratos se rechazan con el número delante (§13) |

## 4. La cartera (97.000 €)

| Bloque | Fondo | ISIN | € | % | RV dentro | TER |
|---|---|---|---:|---:|---:|---:|
| RF corta IG | Neuberger Short Duration Euro Bond U | IE00BL1GVT98 | 31.900 | 32,9 % | 0 % | 0,38 % |
| RF flexible (ABS) | **Aegon European ABS A EUR Acc** | **IE00BG226Z29** | 5.000 | 5,2 % | 0 % | **0,66 %** |
| Crédito | **Sissener Corporate Bond R EUR** | **LU2262944817** | 5.000 | 5,2 % | 1,6 % | **0,90 %** |
| RV value Europa | MyInvestor Value C | ES0165243025 | 5.000 | 5,2 % | 95,4 % | ~1,42 % + 9 % éxito |
| RV value global | Cobas International P | LU1598719752 | 5.000 | 5,2 % | 72,9 % | 2,33 % |
| **Activos reales (REITs)** | **iShares Developed Real Estate Index D Acc** | **IE00BDRK7P73** | **5.000** | **5,2 %** | **99 %** | **0,17 %** |
| RV Europa | Fidelity MSCI Europe P Acc | IE00BYX5MD61 | 3.700 | 3,8 % | 99,4 % | 0,10 % |
| RV emergentes | iShares Emerging Markets S Acc | IE000QAZP7L2 | 6.400 | 6,6 % | 100 % | 0,16 % |
| Cartera automatizada | Rock 78/22 | — | 30.000 | 30,9 % | 78 % | 0,41 % todo incluido |
| | **TOTAL** | | **97.000** | **100 %** | | |

**Reparto:** RV **48.500 € (50,0 %)** / RF **48.500 € (50,0 %)** con la convención del 31/10 (los
satélites activos cuentan al 100 %, Rock al 78 %). **17 posiciones** (8 manuales + 9 de Rock). Fuera
de la base: 10.000 € de Groupama Trésorerie. **Salen de la cartera actual:** Gamma (81 % HY de
energía/GNL/shipping, el mayor concentrador de riesgo de crédito), NB Space (1.000 € de satélite con
35,7 % de volatilidad: el 1 % del dinero con un cuarto del riesgo) y UBS China (ya está al 19,5 %
dentro del fondo de emergentes; tener estarla aparte duplicaba la posición).

**Por qué esos tamaños en los satélites** (14,1 % de la cartera, 28,2 % de la RV):

| Satélite | € | Por qué ese tamaño |
|---|---:|---|
| MyInvestor Value C | 5.000 | Europa small/mid a 0,8x valor en libros, beta 0,40 (18/10). El value que encaja con la sobreponderación en Europa |
| Cobas International P | 5.000 | Value global con **cero solape** con el anterior (ninguna empresa compartida entre sus top 10; Golar LNG, CK Hutchison, Atalaya, BW Offshore, TGS). Ojo: TGS es también la primera posición de Horos — la apuesta al capex energético es una, no dos (Horos no entra, §12). Ficha advierte soft close próximo: siempre se podrá vender o reembolsar **por traspaso** |
| iShares Developed Real Estate (REITs) | 5.000 | El hueco de activos reales, único escrito como «0 % de clase» que se cierra. Indexado al 0,17 %, sin gestor; se financia con el small cap del plan anterior (3.700 €) y 1.300 € del recorte de Europa large: el 64,8 % USA del bloque se compensa quitando el small cap, 61 % USA. Entra tras 5 años de sector malo (+0,6 % anual), no tras un pico |
| iShares EM | 6.400 | Para el 10 % de cartera contando los 3.300 € de emergentes dentro de Rock (9.700 €). Consecuencias asumidas: 42 % del índice es tecnología (Taiwán, Corea) y ~1.455 € caen en TSMC sola |

## 5. Qué entra y qué sale: los dos de RF por sustitución + los REITs por hueco

| | Sale | Entra | Por qué |
|---|---|---|---|
| **RF flexible** | DNCA Alpha Bonds A<br>1,31 % + 20 % éxito · 3A +4,17 % · **5A +4,75 %** · vol 2,00 % | **Aegon European ABS A EUR Acc**<br>**0,66 % sin éxito** · 3A **+4,38 %** · **5A +2,94 %** · vol 3A **0,95 %** (5A **1,90 %**) | −52 % de coste y de vol a 3A, pero la vol 5A baja solo **−29 %** (1,90 frente a 2,68: la vol 3A del ABS está suavizada); gana 0,21 pp a 3 años y **cede 1,81 pp a 5 años** |
| **Crédito** | Carmignac Portfolio Credit A<br>1,20 % + 20 % éxito · 3A +6,45 % · **5A +1,83 %** · vol 3,62 % · **2022 −13,0 %** | **Sissener Corporate Bond R EUR**<br>**0,90 % sin éxito** · 3A **+6,85 %** · **5A +5,51 %** · vol 3A **2,05 %** (5A **2,75 %**) · **2022 +0,2 %** | Más retorno en las tres ventanas, −43 % de vol a 3A y −50 % a 5A, y no perdió en 2022 |

Una es sustitución de vehículo y la otra no. **Sissener sí**: crédito por crédito, mismos euros, otro
gestor y menos comisión. **Aegon no**: DNCA es 79 % deuda pública G10 con rating A+ y Aegon es ~99 %
titulización; el bloque sigue llamándose «RF flexible» y pesando 5.000 €, pero el activo de dentro es
otro. El **par completo por pata, en euros:** pata Aegon **+48,5 €/año de ahorro** (32,5 TER + 16 de
éxito) frente a −90,5 €/año a 5A (+10,5 a 3A); pata Sissener **+33 €/año de ahorro** y además +20 €/año
a 3A y +184 €/año a 5A. La dominación completa solo la tiene Sissener; Aegon es un cambio de riesgo que
se paga en la ventana 5A (se vigila en §14).

**El tercer fondo que entra, por hueco y no por sustitución:** los REITs (IE00BDRK7P73, indexado
0,17 %) entran 5.000 € financiados con el small cap del plan anterior (3.700 €) y 1.300 € del recorte
de Europa large. No sale ningún fondo de RV que exista hoy y el 50/50 no se toca. La ficha es la del
bloque más castigado del catálogo (5 años +0,6 % anual): el hueco se cierra desde la décima mala, no
desde un pico.

## 6. Métricas frente a la cartera del 31/10

| Métrica | 31/10 | **Definitiva** | Delta |
|---|---:|---:|---:|
| Renta variable | 50,0 % | **50,0 %** | 0 |
| TER puro (sin comisiones de éxito) | 583 €/año (0,601 %) | **532 €/año (0,549 %)** | **−51 €** |
| Comisiones de éxito | ≈86 €/año (DNCA 16 · Carmignac ≈18 · Value 52) | **52 €/año (solo Value)** | **−34 €** |
| **Coste total real** | **≈669 €/año (0,690 %)** | **584 €/año (0,602 %)** | **−85 €/año (−12,7 %)** |
| Activos reales | 0 % | **5,2 % (5.000 € de REITs)** | +5,2 pp |
| VOL de la pata cambiada (3A) | DNCA 2,00 · Carmignac 3,62 | **Aegon 0,95 · Sissener 2,05** | −1,05 y −1,57 pp |
| VOL de la pata cambiada (5A) | DNCA 2,68 · Carmignac 5,54 | **Aegon 1,90 · Sissener 2,75** | −0,78 y −2,79 pp |
| Retorno 3A del bloque de RF (estimado) | 4,60 % | **4,67 %** | +0,07 pp |
| Comportamiento del bloque en 2022 (estimado) | −5,4 % | **−5,0 %** | +0,4 pp |
| Duración estimada de la RF (con Rock) | 3,67 años | **≈3,3 años** (3,2-3,5, inferida) | −0,2 a −0,4 |
| Carry de la RF | 4,79 % (2.007 €) | 4,42-4,67 % (1.852-1.957 €) | −50 a −155 € |
| Drawdown 2008 (RV −40 %, RF −3 %) | −21,5 % | **−21,5 %** | 0 |
| Posiciones | 17 | **17** | 0 |
| EE. UU. dentro de la RV | 32,5 % | **34,5 %** | +2,0 pp |

**Dónde está el ahorro, desglosado:** 51 € de TER (47 del cambio de RF + 4 del recorte small
cap→REITs) y 34 € de comisiones de éxito. La del 31/10 estimaba
el éxito de MyInvestor Value (52 €) pero no el de DNCA y Carmignac, que **cobran el 20 % solo sobre lo
que baten a su índice y con high-water mark**, no sobre el cupón: la ficha de la gestora declara que
DNCA cobró de verdad **0,32 %** (16 €/año sobre 5.000 €) y Carmignac cobra 20 % sobre 75 % ICE BofA
Euro Corporate + 25 % Euro High Yield con clawback de 5 años (≈18 €/año). El coste real de la del
31/10 era **≈669 €/año**, no 635 € ni 715 €.

**Lo que el 2022 esconde.** La mejora de 0,4 pp del bloque sale de que las dos sustituciones se
cancelan: Carmignac −13,0 % → Sissener +0,2 % aporta +660 € y DNCA +6,0 % → Aegon −4,0 % quita −500 €.
A nivel de fondo, el cambio de DNCA es **−10 pp en el peor año**. Si se cambiara solo Carmignac y se
quedara DNCA, el bloque haría **−3,8 %** en vez de −5,0 %.

**Lo que la duración no baja.** De 3,67 a ≈3,3 años (3,2-3,5), no a 2,5: el 77,5 % del riesgo de tipos
está en el Neuberger (35 %) y en Rock (42,5 %), que no se tocan, y los 10.000 € que cambian son el
22,5 %. El suelo matemático de la cartera entera es 2,84 años aunque los dos fondos nuevos tuvieran
duración cero. Cada +100 pb cuesta ≈1.600-1.680 € en vez de 1.778 (100-180 € menos).

**Retorno esperado** (estimación, no backtest): el *earnings yield* ponderado de la RV es **≈6,3-7,0 %**
con los pesos de §10.3 y los múltiplos de §2 (USA 5,35 % a 18,7x, Europa 7,35 % a 13,6x, emergentes
9,80 % a 10,2x, Japón 6,3 %; el 11,5 % sin desglosar se imputa al 6,5 % — el 6,58 % original no se
reproduce tal cual); el carry de la RF baja a 4,42-4,67 %. La cartera parte de **≈5,6 % nominal
(±0,2 pp según cómo se impute el residual)** sin contar crecimiento de beneficios ni cambios de múltiplo. Con el bono
de la RF al 4,67 %, la prima de la RV es 1,6-2,4 pp: la señal de −10 puntos (prima <1 pp) no se activa.

## 7. Las órdenes, paso a paso

Todo se ejecuta **en una semana**, en tres sesiones. **Once traspasos y dos suscripciones**, 43.300 €
(35.000 € que salen de los cinco fondos que se vacían + 7.000 € de aportación nueva + 1.300 € que van
de Europa a los REITs una vez acreditado el primer traspaso). El ritmo queda decidido aquí: la
cartera del 31/10 lo tenía abierto (tres tandas mensuales); los datos favorecen entrar de una vez y la
ventana de crédito de 6-12 meses no se cubre con tres meses. Las casillas «Hecho» pasan de **☐** a
**☑** cuando el titular confirma la operación, y la fecha real se anota en §7.7; los checks de cada
día se marcan con `[x]` al momento. Si algo falla, se escribe al lado qué orden y por qué.

### Paso 0 — Preparación (antes del día 1)

- [ ] Transferir **7.000 €** a la cuenta de MyInvestor y verlos en efectivo.
- [ ] Comprobar los saldos de partida: Neuberger **22.000**, DNCA **13.000**, Carmignac **12.000**,
      Gamma **8.000**, MyInvestor Value **2.000**, Cobas **1.000**, Space **1.000**, China **1.000** =
      **60.000 €**. Rock queda fuera, con 30.000 €.
- [ ] Reembolso: **ya verificado el 31/10** — 0,00 % en Gamma, Space, China, Carmignac y DNCA. Repetir
      solo si alguna ficha ha cambiado desde entonces.
- [ ] Confirmar la **comisión de entrada** de Aegon, Sissener y del REITs (no publicada). Si alguna
      fuera >1 %, no se esquiva entrando en dos tandas (una comisión proporcional se paga igual): se
      acepta o se cambia de destino.
- [ ] Recordar el ⚠️ del **Neuberger: «hasta 3 %»** de entrada = **hasta 297 € una vez** sobre los
      9.900 € que recibe. Es el único coste de entrada conocido del plan.
- [ ] Recordar: **traspaso, nunca reembolso**. Es lo que deja la factura fiscal en 0 €.

### 7.1 Día 1 — 18.700 € · 3 traspasos + 2 suscripciones

| Hecho | # | Origen | ISIN origen | € | Destino | ISIN destino | Antes de |
|:--:|--:|---|---|---:|---|---|---|
| ☐ | 12 | Aportación nueva (efectivo) | — | 4.000 | Cobas International P | LU1598719752 | 14:00 |
| ☐ | 6 | Carmignac Portfolio Credit A | LU1623762843 | 5.000 | Aegon European ABS A | IE00BG226Z29 | 12:00 |
| ☐ | 8 | Carmignac Portfolio Credit A | LU1623762843 | 5.000 | Fidelity MSCI Europe P | IE00BYX5MD61 | 12:00 |
| ☐ | 11 | Aportación nueva (efectivo) | — | 3.000 | MyInvestor Value C | ES0165243025 | 12:00 |
| ☐ | 7 | Carmignac Portfolio Credit A | LU1623762843 | 1.700 | iShares Developed Real Estate | IE00BDRK7P73 | 12:00 |

**Cobas primero, solo por orden operativo.** Su ficha advierte soft close próximo y que *«solo los
inversores que ya sean partícipes podrán seguir invirtiendo»*: el titular ya lo es (1.000 €), así que
la aportación está permitida y el reembolso por traspaso siempre será posible. Se pone primero para no
dejarlo al final. *Carmignac queda con 300 €.*

Checks al cerrar el día 1:

- [ ] Cobas, Aegon, Fidelity Europe, MyInvestor Value y los REITs figuran con importe abierto.
- [ ] Carmignac tiene **300 €** de saldo, ni 0 ni el importe anterior.
- [ ] Los 7.000 € de aportación ya no están en efectivo.
- [ ] Justificantes de los cinco movimientos guardados.

### 7.2 Día 2 o 3 — 13.300 € · 4 traspasos

| Hecho | # | Origen | ISIN origen | € | Destino | ISIN destino | Antes de |
|:--:|--:|---|---|---:|---|---|---|
| ☐ | 4 | DNCA Alpha Bonds A | LU1694789451 | 6.400 | iShares Emerging Markets S | IE000QAZP7L2 | **09:00** |
| ☐ | 5 | DNCA Alpha Bonds A | LU1694789451 | 5.000 | Sissener Corporate Bond R | LU2262944817 | 10:00 |
| ☐ | 2 | DNCA Alpha Bonds A | LU1694789451 | 1.600 | Neuberger Short Duration | IE00BL1GVT98 | 10:00 |
| ☐ | 3 | Carmignac Portfolio Credit A | LU1623762843 | 300 | Neuberger Short Duration | IE00BL1GVT98 | 10:00 |

La de emergentes antes de las **09:00** (es la que corta primero); las otras tres antes de las
**10:00**, que es el corte de DNCA, Sissener y Neuberger.

Checks al cerrar el día 2:

- [ ] Neuberger en **23.900 €** (22.000 + 1.600 + 300; los 8.000 de Gamma entran el día 3, 31.900 es
      el saldo final).
- [ ] iShares Emergentes en **6.400 €**.
- [ ] Sissener en **5.000 €**.
- [ ] DNCA y Carmignac a **0**.

### 7.3 Día 4 o 5 — 11.300 € · 4 traspasos

| Hecho | # | Origen | ISIN origen | € | Destino | ISIN destino | Antes de |
|:--:|--:|---|---|---:|---|---|---|
| ☐ | 1 | Gamma Global A | ES0140794001 | 8.000 | Neuberger Short Duration | IE00BL1GVT98 | 10:00 |
| ☐ | 9 | NB Next Generation Space | IE00018YKVN0 | 1.000 | iShares Developed Real Estate | IE00BDRK7P73 | **12:00** |
| ☐ | 10 | UBS MSCI China | LU1815002040 | 1.000 | iShares Developed Real Estate | IE00BDRK7P73 | **12:00** |
| ☐ | 13 | Fidelity MSCI Europe P | IE00BYX5MD61 | 1.300 | iShares Developed Real Estate | IE00BDRK7P73 | **12:00** |

Gamma corta a las 14:00 pero el destino corta a las 10:00: manda la más temprana. Las órdenes 9, 10 y
13 (destino REITs) van antes de las **12:00**, y la 13 solo cuando el traspaso del día 1 haya
acreditado en Fidelity (lag 2-3 días): por eso cae en la tercera sesión.

Checks al cerrar el día 3:

- [ ] Gamma, Space y China a **0**.
- [ ] Ningún fondo de origen con saldo negativo. Neuberger ya en **31.900 €**.
- [ ] Los REITs en **5.000 €** (1.700 + 1.000 + 1.000 + 1.300).
- [ ] Ocho fondos manuales con su saldo final.

### 7.4 Comprobación final (cuando estén las tres sesiones)

- [ ] Neuberger 31.900 · Aegon 5.000 · Sissener 5.000 · Value 5.000 · Cobas 5.000 · REITs 5.000 ·
      Europa 3.700 · EM 6.400 = **67.000 €** manuales.
- [ ] Rock intacto en **30.000 €**. Total **97.000 €**.
- [ ] RV 50,0 % / RF 50,0 %, con la convención del 31/10 (satélites al 100 %, Rock al 78 %). El
      look-through estricto da 48,4 % de RV (46.965 €): Value es 95,4 % RV y Cobas 72,9 %; con esos
      pesos la caída estimada es ≈ −20,9 %. No se rebalancea: es convención, no desfase.
- [ ] Coste 584 €/año (0,602 %): 532 € de TER + 52 € del éxito del 9 % de MyInvestor Value. Comprobar
      que no quedó ninguna comisión de éxito del 20 %.
- [ ] Los justificantes de los **once traspasos** archivados (son la prueba del 0 % fiscal). Las dos
      suscripciones de 3.000 y 4.000 € son dinero nuevo y no generan diferimiento.

### 7.5 Cuadre por origen y por destino

**Origen:** Gamma 8.000 · DNCA 1.600 + 6.400 + 5.000 = 13.000 · Carmignac 300 + 5.000 + 1.700 + 5.000 =
12.000 · Space 1.000 · China 1.000 · aportación 3.000 + 4.000 = 7.000. **Total 42.000 €**.

**Destino:** Neuberger 8.000 + 1.600 + 300 = **+9.900** (22.000 → 31.900) · Emergentes **6.400** ·
Aegon **5.000** · Sissener **5.000** · REITs 1.700 + 1.000 + 1.000 + 1.300 = **5.000** · Fidelity Europe
**+3.700** (entra 5.000 y manda 1.300 a los REITs) · Value **+3.000** (2.000 → 5.000) · Cobas
**+4.000** (1.000 → 5.000).

### 7.6 Lo que no se debe hacer

- **No reembolsar** para luego suscribir: se pierde el diferimiento fiscal.
- **No cambiar de clase** los fondos que se quedan (equivale a reembolso).
- **No separar la orden 3** (300 €) del resto: es el cuadre de Carmignac.
- **No comprar Aegon ni Sissener con más de 5.000 €** hasta ver un trimestre de comportamiento.

### 7.7 Registro de ejecución

| Sesión | Fecha real | Importe | Estado |
|---|---|---:|---|
| Día 1 | — | 18.700 € | pendiente |
| Día 2-3 | — | 13.300 € | pendiente |
| Día 4-5 | — | 11.300 € | pendiente |

## 8. Por qué es la definitiva, y con qué límite

Porque reduce **riesgo medido** en el bloque de renta fija: la pata cambiada baja 1,05 y 1,57 pp de vol
a 3A (y 0,78 y 2,79 pp a 5A, ficha), el −13,0 % de Carmignac en 2022 queda fuera de la cartera y la
duración baja 0,2-0,4 años. Las vol y las rentabilidades son de ficha; la duración es inferida.

**No** por el argumento que el borrador tenía escrito: el 20 % de éxito **no se cobra sobre el cupón**.
DNCA cobra 20 % de lo que bate a €STR+1,40 % con high-water mark, y su gestora declara 0,32 % cobrado
(16 €/año sobre 5.000 €); Carmignac cobra 20 % sobre 75 % ICE BofA Euro Corporate + 25 % Euro High
Yield con clawback de 5 años (≈18 €/año). Son ≈34 €/año, no 80, y el coste real de la del 31/10 es
≈669 €, no 715 €.

Y tampoco por dominancia: **Aegon no domina a DNCA**. Gana en coste, volatilidad y 3A (+0,21 pp), pero
cede 1,81 pp a cinco años (+2,94 % frente a +4,75 %), que sobre 5.000 € son 90 €/año. La ventana de 5
años incluye un ciclo completo de tipos, así que es la que más pesa en un activo de duración. La pata de
Aegon se adopta como cambio de riesgo (soberano A+ → ABS), no como mejora gratis; su control está en
§14.

**Lo que esta cartera NO gana, dicho claro:** el retorno esperado no sube (≈5,6 % frente a 5,7 %),
porque el carry cae entre 50 y 155 €/año según lo que rinda Aegon, que no publica TIR. No es una cartera
para ganar más: es la misma cartera con menos volatilidad y algo menos de coste. Quien quiera más
rentabilidad tiene que subir la RV, y eso es otra decisión (§2 y §14).

## 9. Riesgos y límites

- **Aegon European ABS no es soberano.** Es titulización: 58 % ABS y 35 % RMBS, con Reino Unido 31 %,
  Irlanda 23 % y Países Bajos 11 %. Su 2022 fue −4,0 % y su 5A solo +2,94 %: es un activo corto y
  seguro, no un refugio que sube cuando los tipos suben. Pierdes el +6,0 % que hizo DNCA en 2022 y
  **1,81 pp anuales a cinco años** (+4,75 % de DNCA frente a +2,94 %), que son 90 €/año sobre 5.000 €.
- **Reabre dos decisiones documentadas de la carpeta, con el permiso del titular (03/11):** la del
  31/10 mantenía DNCA «porque es el único soberano A+», y el anexo de mixtos cerró el tema de estos
  dos fondos por 111 €/año. Este documento unifica ambas: sale el soberano A+, y la variante de
  mixtos se rechaza (§13) porque rompería «cada euro es RV o RF».
- **Sissener concentra 58 % en Noruega y Suecia.** Es crédito nórdico: si ese mercado se abre, cae. Y
  es un fondo pequeño de una gestora nórdica distribuida por FundRock, no una casa global.
- **Ninguno de los dos publica TIR ni duración.** La duración de la cartera baja a ≈3,3 años
  (3,2-3,5) **por inferencia** de la familia del activo, no porque la ficha lo diga. Es el límite
  principal de §6.
- **Comisión de entrada**: desconocida en los dos fondos de RF nuevos, en el REITs y en el Neuberger
  («hasta 3 %» = hasta 297 € una vez). Si Aegon o Sissener cobraran más del 1 %, el ahorro de 85 €/año
  se come el primer año.
- **Riesgo de gestor**: cambiar dos fondos con historial por dos con menos historial (Sissener nació en
  2019) es cambiar track record por coste y volatilidad.
- **El bloque de REITs añade su propio riesgo, y es RV, no renta**: 5 años +0,6 % anual y 2022 −20,1 %
  (ficha), 64,8 % EE. UU. y sensible a los tipos como cualquier inmobiliario cotizado. Aporta *fuentes
  de retorno* distintas (alquileres), no protección en caídas: en un 2008-type la cartera cae igual
  (−21,5 %). Es el precio de cerrar el hueco de activos reales, decidido por el titular el 03/11 y
  vigilado en §14.
- **¿Cubre las divisas la clase EUR?** La ficha no lo dice: el 31 % GBP de Aegon y el ~58 % NOK/SEK de
  Sissener pueden entrar en el retorno sin cobertura (§10.5 los cuenta como exposición sin cubrir).
  Es verifiable en la pantalla de suscripción del bróker, no en el catálogo.
- **El colchón de 10.000 €**: criterio de la clase de Ackman (34:33): 6 meses de gastos, «quizá
  incluso 12». Con 10.000 €, cubre si el gasto mensual está entre 833 € y 1.667 €; si es mayor, el
  colchón se redimensiona contra los extractos **antes de ejecutar §7**: 3.000 € más de colchón son
  3.000 € menos de cartera. Es la única cifra sin dimensionar que puede mover la tabla entera, y la
  decide el titular, no un vídeo.

## 10. Diversificación por bloques

### 10.1 Bloques funcionales

| Bloque | Qué hace | € | % |
|---|---|---:|---:|
| **RF corta corporativa IG** | Amortiguador: duración 1,95, IG, cupón 4,65 % | 31.900 | 32,9 % |
| **RF flexible (ABS)** | Titulizaciones europeas de corta vida, SRRI 2 | 5.000 | 5,2 % |
| **Crédito nórdico** | Corporativo Noruega/Suecia, 88 % bonos, SRRI 2 | 5.000 | 5,2 % |
| **RV value Europa (small/mid)** | Compañías a 0,8x valor en libros, beta 0,40 | 5.000 | 5,2 % |
| **RV value global** | Value global con energía y shipping (22 % energía) | 5.000 | 5,2 % |
| **Activos reales (REITs)** | FTSE EPRA Nareit Developed indexado | 5.000 | 5,2 % |
| **RV Europa large** | MSCI Europe indexado | 3.700 | 3,8 % |
| **RV emergentes** | MSCI EM indexado | 6.400 | 6,6 % |
| **Cartera automatizada** | 78 % RV / 22 % RF en 9 fondos indexados | 30.000 | 30,9 % |

Dentro de Rock: 23.400 € de RV (24,1 % de la cartera) y 6.600 € de RF (6,8 %).

### 10.2 Tipos de activo (todo el look-through)

| Activo | € | % | De dónde |
|---|---:|---:|---|
| Renta variable | 48.500 | 50,0 % | 25.100 manuales + 23.400 de Rock |
| Deuda corporativa | 27.803 | 28,7 % | Neuberger 73,3 % (23.376) + Sissener 88,1 % (4.407) |
| Titulizaciones (ABS/RMBS/MBS) | 10.344 | 10,7 % | Neuberger 17,0 % (5.414: RMBS 7,7 + ABS 6,9 + agencia 3,0) + Aegon 98,6 % (4.930) |
| Deuda soberana | 8.008 | 8,3 % | Rock 6.600 (US Treasury + Euro 20+) + Neuberger 3,9 % (1.231) + Sissener 3,6 % (178) |
| Bonos cubiertos (covered bonds) | 1.674 | 1,7 % | Neuberger 5,2 % |
| Liquidez | 553 | 0,6 % | Sissener 368 (7,4 %) + Neuberger 185 (0,6 %) |
| Sin clasificar en las fichas | 118 | 0,1 % | El 1,6 % de RV dentro de Sissener y redondeos |
| **TOTAL** | **97.000** | **100 %** | |

> **Nota de ficha:** los sectores del Neuberger en el catálogo suman 103,6 % (el RMBS, el ABS y la
> titulización de agencia se solapan entre categorías); las filas del NB se **normalizan a 100 %**
> (corporativo 76,4 → 73,3, titulizaciones 17,7 → 17,0, Gobierno 4,0 → 3,9, cubiertos 5,5 → 5,2).
> El desglose exacto del solape lo daría la ficha de la gestora, no el catálogo del bróker. La ficha
> de Sissener y de Aegon suma 100 % y entra tal cual.

**Lo que hay y lo que no:** hay **inmobiliario cotizado directo** desde el 03/11: el bloque de REITs
(5.000 €, 97,4 % del fondo es inmobiliario por ficha, 5,2 % de la cartera). Sigue sin haber: oro,
materias primas, inmobiliario indirecto vía fondos de small/value (≈0,7 % de la cartera), renta fija
emergente, high yield puro, private equity, cripto y acciones individuales.

### 10.3 Geografía de la renta variable

| Región | % de la RV | % de la cartera |
|---|---:|---:|
| Estados Unidos | 34,5 % | 17,3 % |
| Europa | 26,3 % | 13,2 % |
| Emergentes | 20,4 % | 10,2 % |
| Japón | 6,4 % | 3,2 % |
| Otros desarrollados (Canadá, Australia, Pacífico) | 2,5 % | 1,2 % |
| Sin desglosar en las fichas | 9,8 % | 4,9 % |

El 9,8 % sin desglosar es sobre todo Cobas, que no publica el país del 44 % de su cartera, y el resto
de Rock y de los REITs que no cae en un país concreto. **Frente a un MSCI ACWI (63 % EE. UU., 15 %
Europa, 10 % emergentes), esta cartera lleva 28,5 pp menos de EE. UU., 11,3 pp más de Europa y 10,4
pp más de emergentes.** La tabla se recalculó al entrar los REITs y salir el small cap (03/11): los
REITs aportan 6,7 pp de EE. UU., el small cap que sale llevaba 4,6 — neto +2,0 pp.

Dentro de emergentes: Taiwán 27 %, Corea 21 %, China 19 %, India 11 %, Brasil 4 %, Sudáfrica 3 %.

### 10.4 Geografía de la renta fija

| Zona | € | % de la RF | Emisor típico |
|---|---:|---:|---|
| Eurozona (DE, FR, IT, NL, IE, ES) | 16.100 | 33,3 % | Corporativo IG, covered bonds, RMBS irlandés |
| Estados Unidos | 8.700 | 17,9 % | Corporativo IG (Neuberger 14 %) y Treasury (Rock) |
| Reino Unido | 6.700 | 13,9 % | Corporativo IG y ABS (Aegon 31 %) |
| Nórdicos (NO, SE, DK) | 3.100 | 6,4 % | Crédito nórdico (Sissener 62 %) |
| Canadá y otros | 300 | 0,6 % | Corporativo |
| Sin desglosar | 13.600 | 28,0 % | Resto de Neuberger |

### 10.5 Divisas (sin cobertura)

| Divisa | % de la cartera |
|---|---:|
| EUR | ≈29 % |
| USD | ≈27 % |
| GBP | ≈10 % |
| JPY | ≈3 % |
| NOK y SEK | ≈4 % |
| CHF | ≈1 % |
| Emergentes (TWD, KRW, CNY, INR, BRL, ZAR, HKD) | ≈6 % |
| Mixto / sin desglosar (Cobas no publica el 44 % de su cartera) | ≈20 % |

La cartera **no cubre divisa**: el ~27 % en dólares (los REITs añaden ~1 pp) es una posición deliberada,
no un descuido. Es la palanca que hace que la parte europea y emergente pese cuando el dólar baja.

### 10.6 Sectores de la renta variable (aproximado, top 6 de cada ficha)

| Sector | % de la RV |
|---|---:|
| Tecnología | 20,0 % |
| Consumo cíclico | 11,9 % |
| Servicios financieros | 11,4 % |
| Industria | 11,0 % |
| Inmobiliario | 10,8 % (los REITs: el 97,4 % del fondo es inmobiliario) |
| Salud | 7,5 % |
| Comunicación | 5,1 % |
| Energía | 2,8 % |
| Materiales básicos | 2,0 % |
| Consumo defensivo | 1,2 % |
| Sin desglosar (resto de cada ficha y Rock) | 16,4 % |

Tabla recalculada al salir el small cap y entrar los REITs (03/11; aproximada, top 6 de cada ficha).
La tecnología baja al salir el small sin crecer por los emergentes (42 % del índice: Taiwán y Corea)
y el S&P 500 de Rock: sigue sin ser una apuesta temática.

### 10.7 Estilo y capitalización

| Eje | Reparto |
|---|---|
| Indexado / activo | **79,4 % / 20,6 %** de la RV |
| Value declarado | 20,6 % de la RV (Value + Cobas) |
| Small y mid cap | ≈26 % de la RV (Value 5.000, parte de Cobas; el small cap pasivo salió) |
| Large cap | ≈72 % de la RV |

### 10.8 Concentración por gestora

| Gestora | € | % cartera |
|---|---:|---:|
| Neuberger Berman | 31.900 | 32,9 % |
| Fidelity (directo + dentro de Rock) | 19.000 | 19,6 % |
| BlackRock/iShares (directo + dentro de Rock) | 14.700 | 15,2 % |
| Vanguard (dentro de Rock) | 7.200 | 7,4 % |
| Cobas | 5.000 | 5,2 % |
| Andbank (MyInvestor Value) | 5.000 | 5,2 % |
| Aegon | 5.000 | 5,2 % |
| Sissener / FundRock | 5.000 | 5,2 % |
| Goldman Sachs (dentro de Rock) | 4.200 | 4,3 % |

**La mayor concentración de la cartera es el Neuberger con un 32,9 %.** Es el precio de tener un solo
fondo haciendo de amortiguador; repartirlo entre dos gestoras bajaría ese número pero duplicaría el
número de posiciones y no mejoraría ni el coste ni la TIR.

## 11. Sello del barrido por bloques con el catálogo (03/11/2026)

Ninguna posición está dominada por lo que ofrece el catálogo de MyInvestor. Cada bloque se barrió con
`search_funds` (por TER y por 3A) y con las fichas de los finalistas:

| Posición | Veredicto | Por qué, con el número |
|---|---|---|
| **Neuberger 0,38 %** | Se queda | Los IG indexados euro rinden menos carry a más duración (iShares Euro IG 0,12 %: 3A 4,18, vol 3,53; Vanguard Euro IG: 3A 3,56). El Vanguard similar más barato (0,18 %) solo existe **cubierto** (USD-Hedged 5,68; clase EUR-Hedged 3A 3,78: casi 2 pp de drag es divisa/cobertura). El «0,04 %» de Lazard cobra 0,50 + 20 % de éxito con −15,7 % de liquidez |
| **Fidelity MSCI Europe 0,10 %** | Empata al mínimo | Mismo índice y TER que iShares Europe (IE00BDRK7L36); iShares lleva +0,37 pp a 3A (17,81 vs 17,44) — ruido de tracking, no ahorro garantizado: traspaso sin beneficio cierto |
| **iShares Developed Real Estate 0,17 %** | Se queda (nuevo) | Único indexado de su familia en el catálogo, al mínimo coste; su 5A +0,6 % es el sector en décima mala, no un pico. Entra ciérrando el «0 % de activos reales» con el veredicto del anexo alternativo auditado |
| **iShares EM 0,16 %** | Se queda | El propio catálogo lo marca como el más barato de los 27 indexados de emergentes |
| **Vanguard Small-Cap 0,29 %** | Se queda | Únicas alternativas: clases del mismo fondo; la clase Investor está en soft close y el plan usa la abierta equivalente (IE00B42W4L06) |
| **Aegon European ABS 0,66 %** | Se queda | El catálogo no filtra por titulización; el otro candidato del segmento (Pareto Nordic Cross, vol 3A 0,80) cae por precio suavizado |
| **Sissener 0,90 %** | Se queda | Líder de crédito IG con SRRI 2 (3A 6,85, vol 2,05). Los que le superan en 3A son **cat bonds** (GAM Swiss Re 9,1-11,1, Twelve 9,3): otro activo (ILS, riesgo de catástrofe), TER 1,28-1,55 y reembolso a 10 días |
| **MyInvestor Value** | Se queda | JPM Europe Strategic Value (1,72 %, 3A 23,5, vol 10,1) es otro factor: 43,9 % servicios financieros large cap (ficha); Paradigma Value Catalyst (3A 23,1) es fondo de 2021 con 1,90 % + 10 % de éxito |
| **Cobas International 2,33 %** | Se queda | 3A 26,5 %, 5A 17,1 %, vol 12,3 %: la mejor relación retorno/vol de los value globales del catálogo; soft close literal en la ficha (el traspaso de salida siempre posible) |
| **Rock (automatizada)** | Intocable | Regla de la carpeta: no se desarma una cartera automatizada barata que ya cubre los índices |

**Fuera de este sello por decisión del titular (03/11):** el small cap pasivo salió financiar el bloque
de REITs — era la tercera apuesta al mismo factor (los dos value ya son small/mid) con 61 % USA. Su
veredicto de bloque (única clase abierta) sigue válido; es una decisión de peso, no de calidad.

**Frase firmable:** «de las ocho posiciones manuales, todas están en el mínimo coste disponible para su
índice o función, o fundadas dentro de su segmento; ninguna está dominada; el REITs entra por hueco de
clase al mínimo coste disponible; Rock se rige por su regla propia». Los importes del §4 son los que
manda este sello.

## 12. Lo que se descarta del catálogo

| Candidato | Motivo |
|---|---|
| Vanguard Global Short-Term Corp (USD-Hedged y GBP-Hedged) | El +5,68 % a 3A es en divisa; la clase **EUR Hedged** (la comprable en euros) da 3,78 % — menos que el Neuberger |
| Lazard Euro Short Duration FR0013506995 | TER 0,04 % engañoso: gestión 0,50 % + **20 % de éxito**, −15,7 % de liquidez (apalancado) |
| GAM/Twelve/GAM Credit Opportunities (cat bonds) | Líderes del ranking de crédito por 3A (9,1-11,1 %) pero son bonos de catástrofe (ILS): otro activo, TER 1,28-1,55 y reembolso a 10 días |
| Pareto Nordic Cross Credit LU2023199552 | Volatilidad 3A de 0,80 % en crédito: señal de precio suavizado, no de menos riesgo (el mismo métrico con el que aquí se mira el ABS; por eso las vol van publicadas a 5A también) |
| Vanguard Global Small-Cap IE00B42W4L06 | Sale al financiar los REITs: tercera apuesta al mismo factor (los dos value ya son small/mid) y 61 % USA; su salida no toca el 50/50 |
| JPMorgan Europe Strategic Value LU0210531983 | Otro factor: 43,9 % servicios financieros large cap; la cartera ya lleva valor Europa small/mid |
| Nomura Japan Strategic Value (1,57 %, 3A 23,9 %) | Duplicaría el Japón que Rock ya cubre por índice |
| Paradigma Value Catalyst (1,90 % + 10 % éxito) | Fondo de 2021 y YTD +44 %: sin historial completo, caro para duplicar el value que ya hay |
| Brandes Global Value IE0031573896 | Mínimo 10.000 € y −4,5 pp anuales frente a Cobas |
| iShares MSCI World 0,06 % (IE000ZYRH0Q7) | No es comparable: dejaría la cartera sin emergentes ni small cap (y añadiría EE. UU.) |
| L&G MSCI ACWI IMI 0,16 % (IE0003PI5332) | Nacido en 2025, 14 % en liquidez: sin historial y con lastre de caja |
| Indexados de crédito IG europeo (iShares Euro IG 0,12 %, Vanguard Euro IG, iShares Euro Credit) | Rinden 3,2-4,2 % a 3A con más duración que el Neuberger (4,65 % TIR a duración 1,95): se cede carry por ahorrar TER |
| iShares Euro Gov Inflation-Linked | El trade de Ábaco es deuda americana al 3,1-3,2 % real; el equivalente euro rinde 0,3-0,5 % real y añade duración |
| iShares Global Agg 1-5Y EUR Hedged | El drag de la cobertura a EUR se come el cupón |
| Horos Value Internacional | **Solape doble**: su primera posición es TGS, que ya está en el top 10 de Cobas, y Francia pesa como en MyInvestor Value |
| Azvalor Internacional | Comisión de reembolso del 3 % bajo 12 meses (incompatible con la ejecución) y 60 % energía/materias primas, ciclo que Cobas ya cubre |
| Ábaco Renta Fija R (0,96 %) | 3 años 3,96 % frente al 4,38 % del Neuberger con doble comisión; 22,7 % en liquidez |
| Kaizen Global Income | Un mixto que rompe «cada euro es RV o RF» |
| Mixtos baratos (Cobas Renta 0,33 % + Baelo 0,64 %, 524 €/año) | Vía alternativa sin la regla RV/RF: ~64 €/año más barata que esta cartera, pero cambiaba la regla estructural; rechazada en la adopción del 03/11. Queda como la opción si algún día se levanta la regla |
| Robeco QI Emerging Markets (1,52 %) | Bate al índice a 3 años (23,5 vs 21,1), pero es 10x el coste del indexado |
| Familia «calidad» del catálogo (Wellington Global Quality 1,79 %, MS Global Brands 1,84 %, DWS CROCI 1,49 %, Santalucía Quality 2,10 %, Comgest Growth Global 2,08 %) | Existe, rotulada de verdad (15-26 años de historial) pero cara: pierden 19-709 €/año frente al indexado de Europa y Cobas a 5A. La más fiel a la tesis «marcas con poder de precio» (MS Global Brands, 26 años) es la peor del grupo: 5A +0,97 %, −432 €/año. Sustituir Fidelity Europa por Fundsmith subiría el coste a 637 €/año y EE. UU. a 40,7 % de la RV (lo que §3 prohíbe) |
| Arcus Japan Fund (1,5 %) | Japón ya cubierto por índice; lo comercializa el invitado del webinar |
| Bajar a 35-45 % o subir a 65 % de RV | La RF ya da ≈+0,85 % real; subir añade 6 pp de caída por 0,3 pp de retorno (§2) |

## 13. Qué aportaron los anexos y las revisiones (03/11/2026)

| Hallazgo | Documento | Decisión final | Efecto en las órdenes |
|---|---|---|---|
| El ETF VanEck TRET reparte dividendo trimestral | investigación | **Regla de acumulación** adoptada (fondos, ETF y acciones) | Ninguna: no había ETF en la cartera |
| Las cuatro acciones de la investigación reparten 0,5-4,2 % | investigación | Bloque de acciones directas cerrado | Ninguna |
| El hueco real era **0 % de activos reales** | alternativa (auditada 03/11) | **Se cierra por la vía mínima**: REITs indexados 5.000 € (IE00BDRK7P73, 0,17 %, ficha re-verificada) pagados con el small cap y 1.300 € de Europa; el número del sector (5 años 0,6 %) queda escrito en §9 | Órdenes 7, 9, 10 y 13 |
| Fundsmith (1,09 %) y Comgest Europe como bloque de calidad | alternativa | **No entran por ahora** (revisable en trimestral): el EY/5A de la ficha no sostiene la fila de Comgest (5A −0,94 %) y Fundsmith cede 334 €/año frente al indexado; quedan documentados en el anexo con su papelera Morningstar | Ninguna |
| Tres candidatos de RF barata (Vanguard Short Corp, iShares IG, Amundi) | alternativa | **Confirman el Neuberger** (re-verificado el 03/11, §11). El Amundi pide 500.000 € | Ninguna |
| Fidelity MSCI Japan es el mismo ISIN que dentro de Rock | alternativa | Japón ya cubierto; no se duplica | Ninguna |
| Cobas Renta FI existe al **0,33 %** con 3A ~9 % | incluye-mixto | La vía mixta se **rechaza** al adoptar la avanzada; queda como alternativa si algún día se levanta la regla RV/RF | Ninguna |
| El coste real de las comisiones de éxito del 20 % (DNCA, Carmignac) | incluye-mixto | **Ambos salen** con la adopción del 03/11; queda el 9 % de MyInvestor Value | Órdenes 3, 6-8 y 5 |
| Levantar la regla ahorraba 111 €/año | incluye-mixto | Rechazada por el titular al adoptar la avanzada | Ninguna |
| La cartera entera se podría sustituir por Indexa 75 (0,64 %, 1 posición) | conversación | Rechazado: 73 % de RV (caída −30,2 %) y pierde el sesgo | Ninguna |
| Revisión adversarial del 03/11 sobre el borrador avanzado | revisión en sesión | Duración corregida (≈3,3, no 2,5), vol 5A publicadas, check del día 2 arreglado, §10.2 re-cuadrado con la ficha, cobertura de divisa marcada como límite | Ninguna en importes |
| Contraste con la clase de Ackman (Big Think 2012) | contraste 03/11 | Valida el marco de la cartera (riesgo = caída, no oscilación; colchón 6-12 meses; horizonte 5-10 años); la familia «calidad» del catálogo no entra (§12); convención RV/RF anotada (48,4 % estricto), EY recalculado (≈6,3-7,0 %) y criterio del colchón escrito en §9 | Ninguna en importes: tres correcciones de redacción |

**Ficheros eliminados el 03/11 con contenido absorbido:** `propuesta-actual-avanzada.md` (este cuerpo)
y `propuesta-incluye-mixto.md` (vía de mixtos baratos, fila clave arriba). La propuesta del 31/10
queda en el historial de git. El anexo `propuesta-alternativa.md` sigue vivo como material de
investigación: aporta los REITs (adoptados hoy) y las dos quality (Fundsmith/Comgest), que quedan
revisables en trimestral con su documentación Morningstar.

## 14. Cuándo se revisa

Revisión trimestral y además cuando se cumpla una de estas señales (el modelo del §2 se vuelve a
puntuar entero; las señales no son aditivas):

| Señal | Umbral | Efecto en el % de RV |
| --- | --- | --- |
| Coste real del dinero | La RF de la cartera cae por debajo de la inflación (medido **cobrado**, no YTW) | **+3** → ~53 % |
| Prima de crédito | HY OAS >700 pb | **−3** → ~47 % (vuelve el crédito) |
| Valoración RV | S&P 500 −20 % con beneficios intactos | **+6** → ~56 % |
| Evento de crédito materializado | Spreads >700 pb y default en curso | **+4** → ~54 % |
| Prima de riesgo de la RV | *Earnings yield* − bono <1 pp | **−10** → ~40 % |
| Inflación y tipos | Inflación <2 % y BCE bajando | **−3** → ~47 % |

Además, sobre las tres patas nuevas (Aegon, Sissener, REITs):

- **A los 3 meses de entrar**: comparar Aegon contra DNCA y Sissener contra Carmignac en retorno,
  volatilidad y, si se puede, TIR. Si Aegon rinde por debajo del 3 % anualizado, se vuelve.
- **Si Sissener cae más del 3 % en un mes sin que caiga el crédito europeo**: salir.
- **El bloque de REITs**: si en dos revisiones trimestrales el sector sigue en valores de 2012-2023
  (≈0 % anual) con el resto alcista, se decide con número si se cierra de nuevo el hueco.
- Rebalanceo si algún bloque se desvía >5 pp del objetivo; Rock >10 pp de su 78/22.
- **Si MyInvestor publica TIR o duración** de los fondos nuevos de RF, recalcular §6 con el dato real.

### 14.1 El marcador de carry cobrado (04/11/2026)

La señal «coste real del dinero» se mide **cobrado a 12 meses**, no con el YTW (§2). Para que ese umbral
no se decida de memoria, se fija un **testigo externo** y un número de casa.

| Testigo | Dato | Qué prueba |
| --- | --- | --- |
| **Horos Patrimonio FI**, ficha de la gestora y charla del 30/10 | Duración **2,5 años**, mínimo 80 % RF corporativa, **esperaba 4,5 % neto al lanzar y lleva <2 %** | Un fondo de crédito corto y bien construido puede cobrar la mitad de su carry cuando la deuda pública se tensa: el escenario de la señal **no es teórico** |
| La propia cartera, RF dentro de Rock en 2026 | 3.000 € en el 20+ Euro Treasury (−17,03 % en el año) + 3.600 € en Treasury americano (−7,94 %) = **≈−797 € (−12,1 %)** | La duración larga ya está pagando el precio en casa; el amortiguador corto es el que cobra |
| Consecuencia de la concentración del S&P (advertencia de Ruiz, 30/10) | Top-10 del índice dentro de la cartera: **≈3.570-4.500 € (3,7-4,6 % del total)**, porque el S&P entra solo por el 33 % de Rock | No hay nada que recortar por concentración; solo se vigila, no se actúa |

**Regla escrita.** En la primera revisión trimestral se mide la RF **cobrada a 12 meses**. Si queda
**por debajo del 2 %** —el nivel de Horos Patrimonio, no el 4,42-4,67 % de carry estimado—, se puntúa la
señal **+3** del §2 y la cartera va a **~53 % de RV**. Si cobra el carry previsto (≈4,4-4,7 %), la señal
queda en **0** y no se toca nada. El marcador **no mueve importes hoy**: las trece órdenes de §7 se
ejecutan tal cual.

**Lo que este contraste no autoriza.** Ni acortar la duración por debajo de la actual (Horos falló con
2,5 años, no por tener 3,3), ni comprar Horos Value Internacional (peor 3A y 5A que Cobas, y solape doble
en TGS y en Francia con lo que ya hay), ni adoptar el bloque de calidad de `propuesta-alternativa.md`
(Fundsmith es 79,6 % EE. UU. y 32,2 % tecnología, justo lo que el gestor señala como caro).

## 15. Fuentes, barrido y límites

- **Fichas MyInvestor MCP a 30/10-02/11/2026**, verificadas por ISIN. **Re-verificación con `get_funds`
  (NAV 30/10/2026) el 03/11** de Aegon, Sissener, DNCA, Carmignac, Neuberger y el REITs IE00BDRK7P73
  (junto con los 13 candidatos de calidad del anexo alternativo), más el **barrido por
  bloques con `search_funds`** (índices Europa/EM/small cap, RF corta, crédito corporativo con SRRI 2,
  value): §11. Barrido del catálogo previo: 2.410 fondos, 266 indexados.
- **Fichas legales de quefondos (31/10)**: comisiones de suscripción, reembolso y éxito. **Comisiones
  de éxito de ficha de gestora**: DNCA (20 % sobre €STR+1,40 % con high-water mark, 0,32 % cobrado) y
  Carmignac (20 % sobre ICE BofA Euro Corp + HY, clawback 5 años).
- **Factsheets de gestoras (30/09) y carteras publicadas de Cobas**: TIR, duración, rating y solapes.
- **`sintesis-inversor-2026-10-30.md`** e **`informe-canal-la-pizarra-de-andres-2026-10-30.md`**: tesis
  citadas en las reglas del §3.
- **Charla de Horos (La Pizarra de Andrés, 30/10/2026)**, ingerida en
  `finance/la-pizarra-de-andres/2026-10-30-las-empresas-que-todos-ignoran-son-las-mejores-inversiones/`:
  testigo de carry cobrado de §14.1 y descarte de Horos Value Internacional (§12). Ficha del fondo
  re-verificada con `get_funds` el 04/11/2026 (TER 1,90 %, 3A +16,98 %, 5A +11,92 %, vol 3A 11,02 %,
  Francia 20,7 % · España 15,0 % · Italia 4,2 % · EE. UU. 7,2 %, liquidez 9,2 %, `distributing = 0`).
  La composición de Rock (33 % S&P 500, 10 % 20+ Euro Treasury) se trajo con `search_portfolios` el mismo
  día; el detalle del contraste está en `propuesta-alternativa.md` §0.3-§0.4.
- **Clase de Ackman (Big Think, 2012)**, ingerida en `finance/others/2012-11-27-ackman-finance-basics/`
  y contrastada el 03/11 (`finance/reports/contraste-propuesta-ackman-2026-11-03.md`): criterio del
  colchón (§9), barrido de la familia «calidad» (§12). Su dato de mercado (bono a 10 años ~3 %) está
  1,95 pp por debajo del actual (4,95 %, `^TNX` 03/11) y no se usa como referencia.

Límites: la duración y TIR de Aegon y Sissener **no publicadas** (≈3,3 años inferidos); el retorno 3A y
el 2022 del **bloque** de RF son estimación (la vol y el carry de la RF de Rock no se publican) — las
cifras que deciden son las de **fondo**, que sí son de ficha; los sectores del Neuberger en §10.2 se
normalizan (el catálogo suma 103,6 %); la cobertura de divisa de las clases EUR (GBP de Aegon, NOK/SEK
de Sissener) no está en la ficha; la comisión de entrada de los dos fondos nuevos y de la clase S de
iShares EM, sin dato público; la duración de la RF de Rock es estimada (18 años el 20+, 6 el US
Government); el 65 % USA del GS Global de Rock es estimación; el 44 % de la cartera de Cobas no viene
desglosado por país; el drawdown y el retorno esperado son estimaciones propias; las señales del §2
llevan pesos de juicio, no calibrados con series históricas; los gastos del colchón sin dimensionar.

> No es asesoramiento financiero. Es una cartera construida sobre fichas del bróker y sobre lo que
> cinco profesionales dicen en vídeo, con sus intereses comerciales a la vista. La decisión es del
> titular, y la adoptó el 03/11/2026.

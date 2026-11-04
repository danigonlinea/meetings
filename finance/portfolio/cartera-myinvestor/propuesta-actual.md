---
title: "Cartera definitiva, solo fondos: 55/45 en diez posiciones (97.000 €)"
date: 2026-11-04
type: portfolio-proposal
category: finance
tags: [cartera, definitiva, 55-45, solo-fondos, renta-fija, abs, cobas-renta, reits, japon, pacifico, rock, myinvestor]
status: final
related:
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
  - finance/portfolio/cartera-myinvestor/propuesta-acciones.md
---

# Cartera definitiva, solo fondos — 04/11/2026

> **Qué es.** La cartera vigente y única: **cero ETFs**, todo fondos de inversión (IIC) para que cada
> movimiento sea un traspaso y no tribute. Diez fondos manuales + Rock, **97.000 €**, **55,0 % de RV /
> 45,0 % de RF** en look-through estricto y **424,80 €/año** (0,438 %).
>
> **Qué cambia respecto a la versión anterior (04/11, ocho fondos).** El núcleo desarrollado se
> construye ahora con **tres indexados regionales —Europa, Japón y Pacífico ex-Japón— que replican un
> MSCI World ex USA sin Canadá**, en lugar de un solo fondo de Europa. Es la forma de tener el sesgo
> anti-Estados Unidos sin comprar un ETF. El precio se dice en §10.1: se renuncia a Canadá, porque no
> existe como fondo en este catálogo.
>
> **Qué decide y qué no.** Decide la asignación, los vehículos y los pesos. **No decide** las acciones
> individuales: van aparte (`propuesta-acciones.md`) y no entran en el look-through. **No toca Rock**
> (desmontarla cristalizaría la plusvalía del +83,44 % acumulada desde 2020).
>
> **Método.** Catálogo MyInvestor vía MCP el 04/11/2026: 2.410 fondos, 266 indexados (`list_facets`),
> cribado con `search_funds` y fichas `get_funds` por ISIN (NAV 30/10/2026). Cada cifra es de ficha,
> salvo las marcadas **est.** o **inferida**.
>
> **No es asesoramiento financiero.** La decisión es del titular.

---

## 1. Qué cambia respecto a la cartera del 03/11

| # | Decisión | Por qué |
| --: | --- | --- |
| 1 | **RV del 50 % al 55 %** | Ocho señales de §2 puntúan 55; la RF cobró ≈−2,5 % real en 12 meses |
| 2 | **Sale Sissener** (crédito nórdico) | Su top-10 son bonos HY de energía y shipping, no IG: se pagaba prima de crédito por lo que el diseño decía no comprar |
| 3 | **Entra Cobas Renta** al 0,33 % | Único vehículo de RF del catálogo que **ganó en 2022** (+3,89 %) con vol 2,93 % |
| 4 | **Entra Amundi Euro Corp 1-5Y** al 0,35 % | Indexado de la misma familia que el Neuberger, sin apuesta de gestor: baja la concentración del Neuberger del 32,9 % al 17,5 % |
| 5 | **Sale MyInvestor Value C** | El MCP no publica su TER ni su 3A/5A. Sin coste verificable no se defiende |
| 6 | **El núcleo pasa a Europa + Japón + Pacífico** | Replica el desarrollado ex-USA con fondos al 0,10-0,13 %: Japón 11,2 % y Pacífico 5,5 % de la RV |
| 7 | **Cero ETFs** | Un ETF no admite traspaso: rebalancearlo tributa al 19-23 %. Se pierde Canadá (§10.1) y se gana el 0 % de impuestos en todo |

**Coste total: 424,80 €/año (0,438 %).**

---

## 2. Cuánta renta variable, y por qué 55

**No hay perfil fijo.** El porcentaje sale de ocho señales medibles; el perfil es la consecuencia, no la
entrada. Base neutra para horizonte largo sin necesidad de vender: **45 %**.

| Señal | Dato a 04/11/2026 | Efecto |
| --- | --- | ---: |
| **Coste real del dinero** | TIR de la RF corta 4,24-4,65 % frente a inflación 3,8 % → **+0,4 a +0,8 % real** | **0** |
| **Prima de crédito** | HY europeo OAS 363 pb (normal 260-300) y BB a 175 pb: no se paga por asumir crédito | **+3** |
| **Valoración relativa** | S&P 500 18,7x · STOXX 600 13,6x · MSCI EM 10,2x | **+2** |
| **Concentración y ciclo de crédito** | 46 % del S&P en tecnología, 34 % en siete valores; Ábaco: 60-70 % de probabilidad de evento de crédito en 6-12 meses | **−5** |
| **Riesgo de tipos** | BCE restrictivo (depósito 2,50 %, dos subidas en 2026): no se alarga duración | **+2** |
| **Capacidad de aguante** | Colchón de 10.000 € fuera, ingresos estables, sin obligación de vender | **+3** |
| **Carry cobrado de la RF** | 1A 2026: Neuberger −0,03 %, Aegon +2,39 %, Amundi −0,19 % → por debajo del 2 % cobrado (§11.1) | **+3** |
| **Prima RV-bono** | *Earnings yield* 6,65 % − bono 4,24 % = **2,4 pp** (pánico si <1 pp) | **+2** |
| | **45 + 10 = 55 %** | |

**Decisión: 55,0 % de RV (53.376 €) / 45,0 % de RF (43.624 €)**, look-through estricto por el
`alloc_equity` de cada ficha, Rock al 78 % y Cobas Renta al 14,5 %.

| RV | RF | Caída tipo 2008 | Retorno (EY solo) | Retorno (EY + crecimiento 4 %) |
| ---: | ---: | ---: | ---: | ---: |
| 45 % | 55 % | −19,6 % | 5,05 % | 7,29 % |
| 50 % | 50 % | −21,5 % | 5,10 % | 7,60 % |
| **55 %** | **45 %** | **−23,4 %** | **5,56 %** | **7,76 %** |
| 60 % | 40 % | −25,2 % | 5,41 % | 8,21 % |
| 68 % | 32 % | **−28,0 %** | 5,92 % | 8,68 % |

**Suelo conductual:** −23,4 % sobre 97.000 € son **−22.700 €**. Si en ese momento se vende, el modelo no
vale: baja a 45 %. La última fila está a propósito: bajar la RF a 23.000 € (32 %) cambiaría el perfil a
−28,0 % y **no es lo que esta cartera propone**.

---

## 3. La cartera (97.000 €, diez fondos manuales + Rock)

| Bloque | Fondo | ISIN | € | % total | RV dentro | TER |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| **RF corta IG** | Neuberger Short Duration Euro Bond U | IE00BL1GVT98 | 17.000 | 17,5 % | 0 % | 0,38 % |
| **RF flexible (value)** | Cobas Renta FI | ES0119207001 | 5.000 | 5,2 % | 14,5 % | 0,33 % |
| **RF flexible (ABS)** | Aegon European ABS A EUR Acc | IE00BG226Z29 | 7.000 | 7,2 % | 0 % | 0,66 % |
| **RF corporativa IG 1-5Y** | Amundi EUR Corp Bond 1-5Y ESG AE Acc | LU1525412281 | 7.200 | 7,4 % | 0 % | 0,35 % |
| **RV Europa** | iShares Europe Index D Acc EUR | IE00BDRK7L36 | 10.800 | 11,1 % | 99,2 % | 0,10 % |
| **RV Japón** | Fidelity MSCI Japan Index P Acc EUR | IE00BYX5N771 | 3.000 | 3,1 % | 98,6 % | 0,10 % |
| **RV Pacífico ex-Japón** | Fidelity MSCI Pacific ex Japan P Acc USD | IE00BDZVHT63 | 2.000 | 2,1 % | 99,1 % | 0,13 % |
| **RV emergentes** | iShares Emerging Markets S Acc | IE000QAZP7L2 | 6.000 | 6,2 % | 100 % | 0,16 % |
| **Activos reales (REITs)** | iShares Developed Real Estate D Acc | IE00BDRK7P73 | 4.000 | 4,1 % | 98,9 % | 0,17 % |
| **RV value global** | Cobas International P | LU1598719752 | 5.000 | 5,2 % | 72,9 % | 2,33 % |
| **Cartera automatizada** | Rock 78/22 (9 indexados) | — | 30.000 | 30,9 % | 78 % | 0,41 % todo incluido |
| | **TOTAL** | | **97.000** | **100 %** | | **0,438 %** |

**Reparto estricto:** RV **53.376 € (55,0 %)** · RF **43.624 € (45,0 %)**. Fuera de la base: 10.000 € de
Groupama Trésorerie como colchón.

**El núcleo desarrollado, en tres piezas.** Europa 10.800 · Japón 3.000 · Pacífico 2.000 = **15.800 €
repartidos 68 / 19 / 13**, que es aproximadamente el peso de esas tres regiones en un MSCI World ex USA
(62 / 21 / 10). Lo que falta es Canadá, que no existe como fondo en el catálogo (§10.1).

**Por qué esos tamaños:**

| Posición | € | En una frase |
| --- | --: | --- |
| Neuberger | 17.000 | La mitad de lo que pesaba y aún la mayor: mejor carry/riesgo del catálogo en su familia (TIR 4,65 %, duración 1,95, vol 1,93 %), pero un 33 % del capital en un gestor no se sostiene |
| Cobas Renta | 5.000 | Que el amortiguador funcione en el año malo y que su 4 % en Ghana y su 28 % en liquidez no manden |
| Aegon ABS | 7.000 | Diversifica el crédito fuera del corporativo: 58 % ABS + 35 % RMBS europeas, SRRI 2 |
| Amundi 1-5Y | 7.200 | La versión indexada de la misma idea, sin curva ni derivados |
| iShares Europe | 10.800 | La sobreponderación que la valoración paga: 13,6x frente a 18,7x, a 0,10 % |
| Fidelity Japón | 3.000 | Diversificación real y gobierno corporativo en mejora (tesis del webinar de Parages): 11,2 % de la RV, el doble de su peso mundial |
| Fidelity Pacífico | 2.000 | Completa el mapa desarrollado; **ojo: 63 % Australia y 46 % financieros**, son los bancos australianos |
| EM | 6.000 | 17,4 % de la RV con los 3.300 € que ya hay en Rock; no más, porque el 42 % del índice son semiconductores |
| REITs | 4.000 | El hueco de activos reales al 0,17 %, desde la décima mala del sector |
| Cobas International | 5.000 | El único alpha activo verificable del catálogo (3A +26,5 %, 5A +17,1 %) y cero solape con Europa |

---

## 4. Por qué cada fondo, con la pega en la misma fila

| Fondo | El dato | Papel | La pega, dicha |
| --- | --- | --- | --- |
| **Neuberger 0,38 %** | 3A +4,41 % · 5A +2,24 % · vol 1,93 % · 2022 −5,68 % · TIR 4,65 % · duración 1,95 | Amortiguador con cupón | 17,5 % de la cartera a una sola idea; lleva futuros (largo Schatz / corto Bund); 1A −0,03 % |
| **Cobas Renta 0,33 %** | 3A +8,90 % · 5A +6,79 % · vol 2,93 % · **2022 +3,89 %** · 1A +11,7 % | RF flexible value: el único que ganó en 2022 | 28 % liquidez, 42 % Alemania, 3,9 % Ghana y 14,5 % de bolsa que aquí se cuenta como bolsa |
| **Aegon ABS 0,66 %** | 3A +4,38 % · 5A +2,94 % · vol 3A 0,95 % (5A 1,90 %) · 98,6 % titulización | Crédito fuera del corporativo | 2022 −4,0 %; el 5A revela que el 3A está suavizado |
| **Amundi 1-5Y 0,35 %** | 3A +3,55 % · 5A +0,78 % · vol 2,21 % · 100 % corporativo IG euro 1-5 años | Indexado puro del mismo riesgo | Rinde 0,86 pp menos que el Neuberger a 3A: se paga por quitar riesgo de gestor |
| **iShares Europe 0,10 %** | 3A +17,58 % · 5A +9,74 % · vol 10,67 % · 99,2 % RV | Beta barata donde la valoración paga | 24,7 % financieros y 21,3 % Reino Unido: **no es «Europa limpia»** |
| **Fidelity Japón 0,10 %** | 3A +17,25 % · 5A +9,55 % · vol 3A 13,11 % · 99 % Japón | Diversificador con divisa distinta | 20 % tecnología y 22 % industria; el yen lleva una década débil y eso resta en euros |
| **Fidelity Pacífico 0,13 %** | 3A +16,91 % · 5A +6,50 % · vol 3A 14,87 % · Australia 63 % | Completa el desarrollado ex-USA | **46 % financieros y 63 % Australia**: en la práctica es un fondo de bancos australianos |
| **iShares EM S 0,16 %** | El más barato de los 27 indexados de emergentes | Única puerta al 10,2x | 42 % tecnología (Taiwán, Corea); ~900 € en TSMC sola |
| **REITs 0,17 %** | 3A +10,78 % · 5A +0,63 % · 97 % inmobiliario · 2022 −20,1 % | Renta de alquiler | Década mala, 64,8 % EE. UU. y **es RV** |
| **Cobas International 2,33 %** | 3A +26,47 % · 5A +17,11 % · vol 12,34 % | Alpha activo, cero solape con Europa | 116,50 €/año, el **39 % de todo el coste manual**; soft close |
| **Rock 0,41 %** | 78/22 · 9 indexados · +83,44 % desde 2020 | Cubre USA, Japón, Europa, Pacífico y EM | 6.600 € de RF con un 20+ que perdió −17,03 % en 2026 |

---

## 5. Qué entra y qué sale

| | Sale | Entra | Por qué, con el número |
| --- | --- | --- | --- |
| **Crédito** | **Sissener** 0,90 % · 3A +6,85 % | **Amundi 1-5Y** 0,35 % · 3A +3,55 % | Cambio de activo, no de vehículo: el top-10 del Sissener es HY de energía y shipping (Nynas, Golar, W&T, McDermott; un tercio del fondo). Se renuncia a 3,3 pp de 3A para no comprar lo que la señal de crédito prohíbe |
| **Value Europa** | **MyInvestor Value C** · TER y 3A/5A **no publicados** | **Europa indexada** (0,10 %) + Japón y Pacífico | Sin coste verificable no entra. La tesis se conserva a 1/14 del precio y el hueco de Japón y Pacífico se compra con el ahorro |
| **Concentración RF** | **Neuberger 31.900 €** (32,9 %) | **17.000 €** (17,5 %) | Cuesta ≈37 €/año de carry y compra que ninguna ficha, curva o derivado decida el 33 % del capital |
| **Núcleo geográfico** | **50 % de RV en 8 fondos** | **55 % en 10 fondos** | §2 y §3 |

**Lo que no cambia.** Rock se queda. El colchón sigue fuera y sin dimensionar contra gastos reales. Se
mantienen las reglas: traspaso y nunca reembolso, cero comisiones de éxito, cada euro contabilizado como
RV o RF aunque el vehículo sea mixto (Cobas Renta entra con su 14,5 % sumado a la RV).

---

## 6. Métricas

| Métrica | Cartera del 03/11 | **Definitiva, solo fondos** | Delta |
| --- | ---: | ---: | ---: |
| Renta variable (look-through) | 48,4 % | **55,0 %** | +6,6 pp |
| TER manual | 532 €/año (0,549 %) | **301,80 €/año (0,450 %)** | −230 € |
| Comisiones de éxito | 52 €/año | **0 €/año** | −52 € |
| **Coste total real** | **584 €/año (0,602 %)** | **424,80 €/año (0,438 %)** | **−159 €/año (−27 %)** |
| Duración RF manual | ≈3,3 años | **≈2,3 años** | −1,0 |
| Duración RF total (con Rock) | ≈3,3 años | **≈3,6 años** | +0,3 |
| Impacto +100 pb | −1.600 € | **−1.590 €** | igual |
| Carry YTW de la RF manual | 4,42-4,67 % | **≈4,24 % (1.545 €)** | −0,2 pp |
| Caída tipo 2008 | −20,9 % | **−23,4 %** | −2,5 pp |
| Retorno esperado (EY + carry) | 5,6 % | **5,56 %** | igual |
| Retorno esperado (EY + crecimiento 4 %) | 7,6 % | **7,76 %** | +0,2 pp |
| Posiciones | 8 manuales + Rock | **10 manuales + Rock** | +2 |
| EE. UU. dentro de la RV | 34,5 % | **30,0 %** | −4,5 pp |
| Mayor concentración de gestora | Neuberger 32,9 % | **BlackRock 24,8 %** (todo indexado) | −8,1 pp |

**Lo que la duración no baja.** La RF manual baja a 2,3 años, pero la total sube a 3,6 porque la RF de
Rock (6.600 €, con 3.000 € a 20+ años) pesa más al haber menos RF manual. **El 76 % del riesgo de tipos
vive en Rock.** Cada +100 pb cuesta ≈1.590 €.

**Lo que el 2022 dice de este cambio.** Con RV −25 % y RF −3 %, la cartera del 03/11 perdía 19.600 €;
esta pierde 22.700 € porque lleva 6,6 pp más de bolsa. La contrapartida es +0,2 pp de retorno anual con
crecimiento. **Es un cambio de riesgo, no una mejora gratis.**

---

## 7. Las órdenes

Todo por **traspaso entre fondos armonizados**: 0 € de impuestos. **Catorce órdenes, 49.000 €**, en dos
sesiones.

### Paso 0 — Preparación

- [ ] Transferir **7.000 €** a la cuenta y verlos en efectivo.
- [ ] Comprobar saldos: Neuberger **22.000** · DNCA **13.000** · Carmignac **12.000** · Gamma **8.000** ·
      MyInvestor Value **2.000** · Cobas **1.000** · Space **1.000** · China **1.000** = **60.000 €**.
- [ ] Reembolso **0,00 %** verificado el 31/10 en los cinco fondos que salen.
- [ ] Mirar en la app la **comisión de suscripción de Aegon y Amundi**: su folleto permite hasta 5,00 %
      y 4,50 %, pero MyInvestor solo cobra lo que muestra. Si aparece, se cambia el destino (§8). Los
      otros cinco publican 0,00 %.
- [ ] **Traspaso, nunca reembolso.**

### 7.1 Sesión 1 — 31.000 € · 7 órdenes

| Hecho | # | Origen | € | Destino | Antes de |
|:--:|--:|---|---:|---|---|
| ☐ | 1 | Aportación nueva | 4.000 | Cobas International P | 12:00 |
| ☐ | 2 | Aportación nueva | 3.000 | Fidelity MSCI Japan | 16:00 |
| ☐ | 3 | Neuberger Short Duration | 5.000 | iShares Europe | **09:00** |
| ☐ | 4 | DNCA Alpha Bonds A | 4.800 | iShares Europe | **09:00** |
| ☐ | 5 | Carmignac Portfolio Credit A | 1.000 | iShares Europe | **09:00** |
| ☐ | 6 | DNCA Alpha Bonds A | 4.200 | Amundi EUR Corp 1-5Y | 12:00 |
| ☐ | 7 | Gamma Global A | 3.000 | Amundi EUR Corp 1-5Y | 12:00 |

Cortes: Europa y DNCA a las **09:00**; Amundi, Gamma y Cobas a las 12:00 o 14:00; Japón a las 16:00.

### 7.2 Sesión 2 (2-3 días después) — 18.000 € · 7 órdenes

| Hecho | # | Origen | € | Destino | Antes de |
|:--:|--:|---|---:|---|---|
| ☐ | 8 | DNCA Alpha Bonds A | 4.000 | iShares Emerging Markets S | **09:00** |
| ☐ | 9 | MyInvestor Value C | 2.000 | iShares Emerging Markets S | **09:00** |
| ☐ | 10 | NB Next Generation Space | 1.000 | Fidelity MSCI Pacific ex Japan | 16:00 |
| ☐ | 11 | UBS MSCI China | 1.000 | Fidelity MSCI Pacific ex Japan | 16:00 |
| ☐ | 12 | Carmignac Portfolio Credit A | 7.000 | Aegon European ABS | 12:00 |
| ☐ | 13 | Carmignac Portfolio Credit A | 4.000 | iShares Developed Real Estate | 12:00 |
| ☐ | 14 | Gamma Global A | 5.000 | Cobas Renta | 12:00 |

### 7.3 Comprobación final

- [ ] Neuberger 17.000 · Cobas Renta 5.000 · Aegon 7.000 · Amundi 7.200 · Europa 10.800 · Japón 3.000 ·
      Pacífico 2.000 · EM 6.000 · REITs 4.000 · Cobas Intl 5.000 = **67.000 €**.
- [ ] Rock intacto en **30.000 €**. Total **97.000 €**.
- [ ] DNCA, Carmignac, Gamma, MyInvestor Value, Space y China a **0**.
- [ ] RV 55,0 % / RF 45,0 %. Coste **424,80 €/año**: 301,80 manuales + 123 de Rock.

**Cuadre por origen:** DNCA 13.000 · Carmignac 12.000 · Gamma 8.000 · Neuberger 5.000 · MyInvestor Value
2.000 · Space 1.000 · China 1.000 · aportación 7.000 = **49.000 €**.
**Cuadre por destino:** Aegon 7.000 · Amundi 7.200 · Cobas Renta 5.000 · Europa 10.800 · Japón 3.000 ·
Pacífico 2.000 · EM 6.000 · REITs 4.000 · Cobas Intl +4.000 = **49.000 €**.

### 7.4 Lo que no se debe hacer

- **No reembolsar** para suscribir después: se pierde el diferimiento fiscal.
- **No cambiar de clase** los fondos que se quedan (equivale a reembolso).
- **No comprar Amundi, Aegon ni Cobas Renta con más de 7.500 €** hasta ver un trimestre.
- **No desmontar Rock.**
- **No sustituir ningún fondo por un ETF** del mismo índice: ahorra 5-10 pb y convierte cada rebalanceo
  en una factura.

---

## 8. Riesgos y límites

- **Cobas Renta es un mixto flexible, excepción declarada.** 28 % liquidez, 42 % Alemania, 3,9 % Ghana,
  14,5 % bolsa. Se compra el **+3,89 % de 2022**, no el 5A. Si en dos años no repite esa defensa, sale.
- **Se renuncia a 3,3 pp de 3A al cambiar Sissener por Amundi**, apostando a que eran prima de HY. Si el
  crédito no se tensa, esta decisión se verá peor: es la apuesta macro de Ábaco, no un hecho.
- **Japón al 11,2 % de la RV** (el doble de su peso mundial) y **Pacífico al 5,5 % con 63 % Australia y
  46 % financieros**: dos apuestas declaradas, no neutralidad. Si Japón no revaloriza, la cartera lo ve.
- **No hay Canadá.** Es el precio de no usar ETF (§10.1): 3 % del mercado mundial que no se puede comprar
  con fondos en este catálogo.
- **La duración total sube a 3,6 años** porque Rock concentra el bono largo.
- **BlackRock al 24,8 %** (todo indexado): riesgo operativo, no de exposición.
- **42 % de los emergentes es tecnología** y ~900 € caen en TSMC sola.
- **El colchón de 10.000 € sigue sin dimensionar** contra gastos reales: cubre si el gasto mensual está
  entre 833 € y 1.667 €. Se ajusta **antes** de ejecutar §7.
- **Comisión de entrada: dos fondos tienen máximo de folleto por encima del 1 %.** Verificado el
  04/11/2026 en quefondos, Finect y el PRIIPs de la gestora: **Aegon ABS hasta 5,00 % de suscripción y
  3,00 % de reembolso**; **Amundi 1-5Y hasta 4,50 % y 1,00 %**. Los otros cinco publican **0,00 %**
  (iShares Europe, iShares REITs, Fidelity Japón, Cobas Renta) o no lo publican (Fidelity Pacífico).
  Son **máximos**, no el precio: el PRIIPs de Amundi dice literalmente «this is the most you will be
  charged; the person selling you the product will inform you of the actual charge», y MyInvestor
  declara que «si en la app no aparece comisión de suscripción, es porque no la cobramos». **Si en la
  app apareciera**, serían 350 € sobre Aegon (5 % de 7.000) y 324 € sobre Amundi (4,5 % de 7.200):
  674 €, cuatro veces el ahorro anual. En ese caso no se suscribe: esos 7.000 € van al Neuberger
  (hasta 24.000, con la concentración dicha) y los 7.200 € al iShares Euro IG Corporate.
- **TIR y duración de Aegon, Amundi y Cobas Renta no publicadas**: 2,3 años y 4,24 % son inferidos.
- **Ninguna cifra de retorno está prometida.**

---

## 9. Diversificación

### 9.1 Geografía de la RV (look-through, estimación declarada)

| Región | % de la RV | € |
| --- | ---: | ---: |
| Estados Unidos | **30,0 %** | 16.025 |
| Europa (UK 20 %, Suiza 14 %, Alemania 13 %, Francia 13 %, NL 9 %, ES 6 %) | **26,3 %** | 14.030 |
| **Japón** | **11,2 %** | 5.974 |
| Emergentes (Taiwán, Corea, China, India, Brasil) | **17,4 %** | 9.298 |
| Pacífico ex-Japón (Australia, Singapur, Hong Kong, NZ) | **5,5 %** | 2.938 |
| Canadá y otros | 2,2 % | 1.166 |
| Sin desglosar en las fichas (Cobas no publica el 44 %) | 5,5 % | 2.929 |

Frente a un MSCI ACWI (63 % EE. UU., 15 % Europa, 10 % emergentes, 5 % Japón): **−33 pp de EE. UU.,
+11 pp de Europa, +7 pp de emergentes y +6 pp de Japón.** Esa es la tesis entera, y se puede medir.

### 9.2 Sectores de la RV (aproximado, top 6 de cada ficha)

| Sector | % de la RV |
| --- | ---: |
| Servicios financieros | 17,9 % |
| Tecnología | 15,6 % |
| Industria | 13,0 % |
| Inmobiliario | 9,1 % |
| Salud | 8,3 % |
| Consumo cíclico | 5,4 % |
| Consumo defensivo | 4,6 % |
| Energía | 3,0 % |
| Materiales básicos | 2,4 % |
| Sin desglosar | 20,7 % |

Tecnología al 15,6 % de la RV frente al 30,8 % de un MSCI World.

### 9.3 Concentración por gestora

| Gestora | € | % cartera |
| --- | ---: | ---: |
| BlackRock / iShares | 24.100 | 24,8 % |
| Fidelity | 19.700 | 20,3 % |
| Neuberger Berman | 17.000 | 17,5 % |
| Cobas | 10.000 | 10,3 % |
| Amundi | 7.200 | 7,4 % |
| Vanguard | 7.200 | 7,4 % |
| Aegon | 7.000 | 7,2 % |
| Goldman Sachs | 4.200 | 4,3 % |
| Groupama | 10.000 | — (colchón) |

### 9.4 Divisas (sin cobertura)

EUR ≈34 % · USD ≈24 % · JPY ≈8 % · GBP ≈11 % · emergentes ≈5 % · otros (AUD, SGD, HKD, CAD) ≈4 % ·
sin desglosar ≈14 %. **No se cubre divisa**: la cobertura a 10 años cuesta 1,5-2 % anual y se come el
premio.

---

## 10. Lo que se descarta, con el número

### 10.1 El ETF que se evita, y su precio

`iShares MSCI World ex-USA UCITS ETF (XUSE.AS, IE000R4ZNTN3)` y su gemelo en euros
`Xtrackers MSCI World ex USA 1C (EXUS.DE, IE0006WW1TQ4)`: TER 0,15 %, 731 posiciones, 3.720 y 7.410 M €
de patrimonio. **Eran la forma más limpia de tener el desarrollado ex-USA.** Se descartan por una razón
que no es de coste: **un ETF no admite traspaso**. Cada rebalanceo o cambio de ese bloque tributa al
19-23 % de la plusvalía, justo lo contrario del diseño. El precio de evitarlo son tres cosas:

1. **Canadá desaparece** (3 % del mundo): no hay fondo de Canadá en el catálogo.
2. **Australia viene mezclada** en el Pacífico ex-Japón (63 %) con 46 % de financieros.
3. **Tres fondos en vez de uno** y 0,10-0,13 % de TER en vez de 0,15 %: 3 €/año de ahorro, no un coste.

### 10.2 Fondos descartados

| Candidato | Ficha | Por qué no |
| --- | --- | --- |
| **Sissener Corporate Bond** | 0,90 % · 3A +6,85 % | Top-10 de HY de energía y shipping (Nynas, Golar, W&T, McDermott) |
| **iShares Euro IG Corporate** (IE00BDRK7J14) | 0,12 % · 3A +4,17 % · 2022 −13,26 % | Duración ~5: perdió 13 pp en 2022 |
| **Vanguard Euro IG** (IE00B04FFJ44) | 0,12 % · 3A +3,37 % | Misma duración larga y menos retorno que el Amundi al mismo precio |
| **Vanguard Global Short Corp USD H** (IE00BDFB7308) | 0,18 % · 3A +5,47 % | Clase en USD sin cubrir y 2022 −5,99 % |
| **AXA Trésor Court Terme** (FR0000447823) | 0,05 % · 3A +2,95 % | Liquidez al €STR: el colchón ya está fuera; una segunda reserva duplica la liquidez |
| **Goldman Sachs Global Enhanced Index SRI** (LU2349459045) | **0,19 %** · 3A +19,83 % · **70,8 % EE. UU.** · 33 % tecnología | Es el fondo global más barato del catálogo y el único con Canadá, pero comprarlo en el bloque manual deshace el sesgo anti-EE. UU. que justifica toda la cartera. Se queda solo dentro de Rock |
| **JPM Europe Strategic Value** (LU0210531983) | 1,72 % · 3A +22,65 % | 43,9 % financieros large cap: apuesta sectorial que el índice ya cubre |
| **Fundsmith** (LU0690375182) | 1,09 % · 5A +2,93 % | Cede 334 €/año frente al indexado europeo y es 79,6 % EE. UU. |
| **Comgest Growth Europe** (IE0004766675) | 1,59 % · 5A **−0,94 %** | Cinco años perdiendo contra su propio índice |
| **Morgan Stanley Global Brands** (LU2295319300) | 1,84 % · 5A +0,97 % | La etiqueta «marcas con poder de precio» no paga |
| **Horos Value Internacional** | 1,90 % · 5A +11,92 % | Pierde contra Cobas y solapa TGS y Francia |
| **Azvalor Internacional** | Reembolso 3 % bajo 12 meses | Incompatible con la ejecución |
| **Vanguard Global Small-Cap** (IE00B42W4L06) | 0,29 % · 5A +6,98 % | 61 % EE. UU. y tercera apuesta al mismo factor |
| **iShares Developed World S** (IE000ZYRH0Q7) | **0,06 %** | Dejaría la cartera sin emergentes, sin REITs y con 72 % de EE. UU. |
| **L&G MSCI ACWI IMI** (IE0003PI5332) | 0,16 % · nacido en 2025 · 13 % liquidez | Sin historial y con lastre de caja |
| **Amundi Prime Euro Gov** (LU2339731064) | 0,05 % · mínimo **500.000 €** | No es contratable |
| **Cat bonds** (GAM, Twelve) | 3A +9 a +11 % · TER 1,28-1,55 % | Otro activo (ILS) y reembolso a 10 días |
| **Oro vía fondo** (DWS, Jupiter) | 1,61-1,66 % · vol 38 % | El perfil del NB Space que sale; el físico solo existe como ETF |
| **Mixtos baratos tipo Baelo** | 0,64 % | Ahorra ≈64 €/año y devuelve el control del riesgo a un tercero |

---

## 11. Cuándo se revisa

Trimestral (enero, abril, julio, octubre) y cuando se cumpla una señal. **El modelo de §2 se puntúa
entero: las señales no son aditivas.**

| Señal | Umbral | Efecto |
| --- | --- | ---: |
| Carry cobrado de la RF | Por debajo del 2 % a 12 meses (ya activada en 2026) | **+3** → ~58 % |
| Prima de crédito | HY OAS >700 pb | **−3** → ~52 % |
| Valoración RV | S&P 500 −20 % con beneficios intactos | **+6** → ~61 % |
| Evento de crédito | Spreads >700 pb y default en curso | **+4** → ~59 % |
| Prima RV-bono | *Earnings yield* − bono <1 pp | **−10** → ~45 % |
| Inflación y tipos | Inflación <2 % y BCE bajando | **−3** → ~52 % |

Además, sobre las posiciones nuevas o cambiadas:

- **Cobas Renta:** a los 24 meses, si no defendió en una caída como en 2022, sale al Neuberger.
- **Amundi 1-5Y:** a los 3 meses, comparar con el Neuberger. Si la brecha a 3A pasa de 1,5 pp, el
  Neuberger recupera peso.
- **Japón y Pacífico:** si en dos revisiones Japón no bate al índice mundial y el Pacífico sigue siendo
  un fondo de bancos australianos al 46 %, se consolidan en Europa y emergentes.
- **REITs:** si en dos revisiones el sector sigue en valores de 2012-2023, se decide con número.
- **Rebalanceo** si un bloque se desvía >5 pp; Rock >10 pp de su 78/22.

### 11.1 El marcador de carry cobrado

Se mide **cobrado a 12 meses**, no con el YTW. En 2026 la RF manual cobró ≈1,3 % (Neuberger −0,03 %,
Aegon +2,39 %, Amundi −0,19 %) frente a una inflación del 3,8 %: **−2,5 % real**. Por eso el modelo ya
puntúa +3. Testigo externo: Horos Patrimonio (duración 2,5, 80 % corporativo, esperaba 4,5 % y lleva
<2 %). **Si en enero la RF cobra ≈4,2 %, la señal vuelve a 0 y el modelo baja a 52 %.**

---

## 12. Qué se absorbe de las propuestas anteriores

Las cinco propuestas que convivían en la carpeta se resolvieron aquí y **se borraron** (`git rm`); el
contenido íntegro sigue en el historial de git (commit `50b2e69`).

| Documento | Qué aportaba | Qué se hizo |
| --- | --- | --- |
| `propuesta-actual-avanzada.md` (55/45, 10 fondos) | El 55 % con tres casas de previsiones; Cobas Renta; AXA Trésor | Adoptados el 55 % y Cobas Renta. No adoptados AXA ni JPM Europe Value |
| `propuesta-perplexity.md` (100k, 12 fondos) | El hallazgo de que **Sissener es HY** | Adoptado el hallazgo y su descarte |
| `propuesta-alternativa.md` (activos reales + calidad) | Los REITs al 0,17 % y 13 fichas de calidad | Adoptados los REITs; calidad descartada con número |
| `propuesta-investigacion.md` | La regla de acumulación y el análisis de las cuatro acciones | Adoptada la regla; las acciones van aparte |
| `propuesta-actual.md` del 03/11 (50/50) | Aegon, Sissener, REITs y el barrido por bloques | Aegon y REITs se conservan; Sissener sale por composición |

---

## 13. Fuentes

- **Fichas MyInvestor MCP a 04/11/2026** (NAV 30/10/2026): `list_facets` (2.410 fondos, 266 indexados),
  `search_funds` por bloque, `get_funds` por ISIN de los diez fondos manuales y de los tres de Rock
  reutilizados (GS, Japón, Pacífico). TER, comisiones, 3A/5A anualizadas, vol, SRRI, países, sectores,
  mínimo, corte y `distributing = 0` en los diez.
- **`cartera-actual.md`** (30/10): saldos, ISIN y composición de Rock.
- **`sintesis-inversor-2026-10-30.md`** e **`informe-canal-la-pizarra-de-andres-2026-11-02.md`**:
  principios de §2 y probabilidad de evento de crédito de Ábaco.
- **Parages, webinar MyInvestor 20/10**: tesis de Japón.
- **Horos, La Pizarra 30/10**: testigo de carry cobrado.
- **Ackman (Big Think 2012)**: criterio del colchón y del horizonte.

Límites: duración y TIR de Aegon, Amundi y Cobas Renta **no publicadas** (2,3 años y 4,24 % inferidos);
la vol y el carry de la RF de Rock no se publican; el 44 % de la cartera de Cobas no viene desglosado por
país; comisión de entrada: máximos de folleto verificados y política de MyInvestor citada en §8, pero el cargo real solo se ve en la app; drawdown y retorno esperado son estimaciones
propias; las señales de §2 llevan pesos de juicio; los gastos del colchón siguen sin dimensionar.

> No es asesoramiento financiero. La decisión es del titular.

---
title: "Cartera definitiva: 55/45 con ocho fondos, sin apuestas de crédito (97.000 €)"
date: 2026-11-04
type: portfolio-proposal
category: finance
tags: [cartera, definitiva, 55-45, renta-fija, abs, cobas-renta, reits, rock, myinvestor, traspasos]
status: final
related:
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
  - finance/portfolio/cartera-myinvestor/propuesta-acciones.md
---

# Cartera definitiva — 04/11/2026

> **Qué es este documento.** La cartera vigente y **única**: sustituye a la del 03/11/2026 y absorbe
> las cinco propuestas que convivían en la carpeta. Ocho fondos manuales + Rock, **97.000 €**,
> **54,9 % de RV / 45,1 % de RF** en look-through estricto y **426 €/año** de coste total (0,439 %).
> Las propuestas absorbidas se borraron de la carpeta (`git rm`); su contenido está en §12 y en el
> historial de git (último commit con la carpeta completa: `50b2e69`).
>
> **Qué decide y qué no.** Decide la asignación, los vehículos y los pesos, con libertad total sobre
> el % de RV, de mixtos y de RF. **No decide** las acciones individuales: el titular las lleva como
> bloque de riesgo aparte (`propuesta-acciones.md`) y aquí no entran ni en el cálculo ni en el
> look-through. Tampoco toca Rock (decisión del titular del 04/11: desmontarla cristalizaría la
> plusvalía de +83,44 % acumulada desde 2020).
>
> **Método.** Catálogo MyInvestor completo vía MCP el 04/11/2026: 2.410 fondos, 266 indexados
> (`list_facets`), cribado por bloque con `search_funds` y fichas `get_funds` por ISIN (NAV
> 30/10/2026). Cada cifra de esta propuesta es de ficha, salvo las marcadas **est.** (estimación
> propia) o **inferida**.
>
> **No es asesoramiento financiero.** Los pesos son una decisión de cartera sobre fichas verificadas
> y sobre lo que dicen cinco profesionales en vídeo, con sus intereses comerciales a la vista.

---

## 1. Qué cambia respecto a la cartera del 03/11

Seis decisiones, y ninguna es cosmética:

| # | Decisión | Por qué |
| --: | --- | --- |
| 1 | **RV del 50 % al 55 %** | El modelo de §2 puntúa 55 y la RF cobró ≈−2,5 % real en 12 meses |
| 2 | **Sale Sissener** (crédito nórdico) | Su top-10 son bonos high yield de energía y shipping, no IG: se estaba pagando prima de crédito por lo que el propio diseño decía no comprar |
| 3 | **Entra Cobas Renta** al 0,33 % | Único vehículo de RF del catálogo que **ganó en 2022** (+3,89 %) con vol 2,93 %: es el amortiguador que de verdad amortigua |
| 4 | **Entra Amundi Euro Corp 1-5Y** al 0,35 % | Indexado de la misma familia que el Neuberger, sin apuesta de gestor: baja la concentración del Neuberger del 32,9 % al 17,5 % |
| 5 | **Sale MyInvestor Value C** | El MCP no publica su TER ni su 3A/5A. Un fondo sin coste verificable no se defiende en una cartera definitiva |
| 6 | **Europa large pasa a 13.600 €** (era 3.700) | Es la única sobreponderación con respaldo de valoración (13,6x frente a 18,7x) y cuesta 0,10 % |

**Coste total: 426 €/año (0,439 %) frente a 584 € (0,602 %). −158 €/año, −27 %.** No es el argumento
principal —el principal es el riesgo— pero es el único número que se controla al 100 %.

---

## 2. Cuánta renta variable, y por qué 55

**No hay perfil fijo.** El porcentaje sale de ocho señales medibles; el perfil es la consecuencia, no
la entrada. Base neutra para horizonte largo sin necesidad de vender: **45 %**.

| Señal | Dato a 04/11/2026 | Efecto |
| --- | --- | ---: |
| **Coste real del dinero** | TIR de la RF corta 4,24-4,65 % frente a inflación 3,8 % → **+0,4 a +0,8 % real** | **0** |
| **Prima de crédito** | HY europeo OAS 363 pb (rango normal 260-300) y BB a 175 pb: no se paga por asumir crédito | **+3** |
| **Valoración relativa** | S&P 500 18,7x · STOXX 600 13,6x · MSCI EM 10,2x. Solo se aprovecha comprando fuera de EE. UU. | **+2** |
| **Concentración y ciclo de crédito** | 46 % del S&P en tecnología, 34 % en siete valores; Ábaco da 60-70 % de probabilidad de evento de crédito en 6-12 meses | **−5** |
| **Riesgo de tipos** | BCE con sesgo restrictivo (depósito 2,50 %, dos subidas en 2026): no se alarga duración | **+2** |
| **Capacidad de aguante** | Colchón de 10.000 € fuera de la cartera, ingresos estables, sin obligación de vender | **+3** |
| **Carry cobrado de la RF** | 1A 2026: Neuberger **−0,03 %**, Aegon +2,39 %, Amundi 1-5Y −0,19 %. Por debajo del 2 % cobrado → se activa la regla de §11.1 | **+3** |
| **Prima RV-bono** | *Earnings yield* 6,65 % − bono 4,24 % = **2,4 pp** (el umbral de pánico es <1 pp) | **+2** |
| | **45 + 10 = 55 %** | |

**Decisión: 55,0 % de RV (53.202 €) / 45,1 % de RF (43.798 €) en look-through estricto** — cada fondo
por su `alloc_equity` de ficha, con Rock al 78 % y Cobas Renta al 14,5 %. Con la convención de mando
(los satélites al 100 %) son 54.200 €, el 55,9 %: las dos cifras no coinciden porque Cobas
International solo es 72,9 % bolsa. **Se usa la estricta en todo el documento.**

| RV | RF | Caída tipo 2008 | Retorno (EY solo) | Retorno (EY + crecimiento 4 %) | Real sobre 3,8 % |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 45 % | 55 % | −19,6 % | 5,05 % | 7,29 % | +1,3 % / +3,5 % |
| 50 % | 50 % | −21,5 % | 5,10 % | 7,60 % | +1,3 % / +3,8 % |
| **55 %** | **45 %** | **−23,3 %** | **5,56 %** | **7,76 %** | **+1,8 % / +4,0 %** |
| 60 % | 40 % | −25,2 % | 5,41 % | 8,21 % | +1,6 % / +4,4 % |

**Por qué 55 y no 50.** La RF en euros cobra entre 0,4 y 0,8 pp reales con duración corta; el 45 % de
RF ya es mucha renta fija para un activo que apenas bate a la inflación. **Por qué 55 y no 60.** El
premio de la RV sobre el bono es de 2,4 pp, no de 4: del 55 al 60 se ganan 0,2 pp de retorno y se
pierden 2 pp más de caída, con GMO dando retorno real negativo a la bolsa americana a siete años.

**Suelo conductual, escrito:** −23,3 % sobre 97.000 € son **−22.600 €**. Si en ese momento se vende,
el modelo no vale: baja a 45 % (retirando los 7.000 € de emergentes y 3.500 € de REITs). Un modelo que
no se aguanta no sirve.

---

## 3. La cartera (97.000 €)

| Bloque | Fondo | ISIN | € | % total | RV dentro | TER |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| **RF corta IG** | Neuberger Short Duration Euro Bond U | IE00BL1GVT98 | 17.000 | 17,5 % | 0 % | 0,38 % |
| **RF flexible (value)** | Cobas Renta FI | ES0119207001 | 5.000 | 5,2 % | 14,5 % | 0,33 % |
| **RF flexible (ABS)** | Aegon European ABS A EUR Acc | IE00BG226Z29 | 7.000 | 7,2 % | 0 % | 0,66 % |
| **RF corporativa IG 1-5Y** | Amundi EUR Corp Bond 1-5Y ESG AE Acc | LU1525412281 | 7.400 | 7,6 % | 0 % | 0,35 % |
| **RV Europa large** | iShares Europe Index D Acc EUR | IE00BDRK7L36 | 13.600 | 14,0 % | 99,2 % | 0,10 % |
| **RV emergentes** | iShares Emerging Markets S Acc | IE000QAZP7L2 | 7.000 | 7,2 % | 100 % | 0,16 % |
| **Activos reales (REITs)** | iShares Developed Real Estate D Acc | IE00BDRK7P73 | 5.000 | 5,2 % | 98,9 % | 0,17 % |
| **RV value global** | Cobas International P | LU1598719752 | 5.000 | 5,2 % | 72,9 % | 2,33 % |
| **Cartera automatizada** | Rock 78/22 (9 indexados) | — | 30.000 | 30,9 % | 78 % | 0,41 % todo incluido |
| | **TOTAL** | | **97.000** | **100 %** | | **0,439 %** |

**Reparto estricto:** RV **53.202 € (54,9 %)** · RF **43.798 € (45,1 %)**. **Ocho fondos manuales + Rock.**
Fuera de la base: 10.000 € de Groupama Trésorerie como colchón, sin tocar y sin rebalancear.

**Por qué esos tamaños:**

| Posición | € | El tamaño, en una frase |
| --- | --: | --- |
| Neuberger | 17.000 | La mitad de lo que pesaba y aún es la mayor: es el mejor carry/riesgo del catálogo en su familia (TIR 4,65 %, duración 1,95, vol 1,93 %), pero un 33 % del capital en un solo gestor no se sostiene |
| Cobas Renta | 5.000 | Suficiente para que el amortiguador funcione en el año malo y pequeño para que su 4 % en Ghana y su 28 % en liquidez no manden |
| Aegon ABS | 7.000 | Diversifica el riesgo de crédito fuera del corporativo: 58 % ABS + 35 % RMBS europeas, SRRI 2 |
| Amundi 1-5Y | 7.400 | La versión indexada de la misma idea, sin apuesta de curva ni derivados: convive con el Neuberger en vez de sustituirlo |
| iShares Europe | 13.600 | La sobreponderación que la valoración paga: 13,6x frente a 18,7x del S&P, a 0,10 % |
| EM | 7.000 | 19,4 % de la RV contando los 3.300 € que ya hay dentro de Rock; no más, porque el 42 % del índice son semiconductores |
| REITs | 5.000 | El hueco de activos reales, cerrado al 0,17 % y desde la décima mala del sector |
| Cobas International | 5.000 | El único alpha activo verificable del catálogo (3A +26,5 %, 5A +17,1 %) y cero solape con Europa |

---

## 4. Por qué cada fondo, con la pega en la misma fila

| Fondo | El dato | Papel | La pega, dicha |
| --- | --- | --- | --- |
| **Neuberger 0,38 %** | 3A +4,41 % · 5A +2,24 % · vol 1,93 % · 2022 −5,68 % · TIR 4,65 % · duración 1,95 | Amortiguador: cupón con duración corta | **17,5 % de la cartera a una sola idea**; lleva futuros (largo Schatz / corto Bund) como apuesta de empinamiento de curva; 1A −0,03 % |
| **Cobas Renta 0,33 %** | 3A +8,90 % · 5A +6,79 % · vol 2,93 % · **2022 +3,89 %** · 1A +11,7 % | RF flexible value: el único que ganó en 2022 | 28 % liquidez (lastre), 42 % Alemania, **3,9 % Ghana** y 14,5 % de RV que aquí se cuenta como RV |
| **Aegon ABS 0,66 %** | 3A +4,38 % · 5A +2,94 % · vol 3A 0,95 % (5A 1,90 %) · 98,6 % titulización | Crédito fuera del corporativo: consumo, hipotecas, estudiantes | 2022 −4,0 %, 5A cede 1,81 pp frente a un soberano A+ y el 5A revela que el 3A está suavizado |
| **Amundi 1-5Y 0,35 %** | 3A +3,55 % · 5A +0,78 % · vol 2,21 % · 100 % corporativo IG euro, vencimientos 1-5 años | Indexado puro del mismo riesgo, sin gestor | Rinde 0,86 pp menos que el Neuberger a 3A: se paga por quitar el riesgo de gestor, no por ganar |
| **iShares Europe 0,10 %** | 3A +17,58 % · 5A +9,74 % · vol 10,67 % · 99,2 % RV | Beta barata donde la valoración paga | 24,7 % servicios financieros y 21,3 % Reino Unido: **no es «Europa limpia»** |
| **iShares EM S 0,16 %** | El más barato de los 27 indexados de emergentes del catálogo | Única puerta al 10,2x de emergentes | 42 % tecnología (Taiwán y Corea); ~1.100 € caen en TSMC sola, y Rock lleva otros 3.300 € en el mismo bloque |
| **REITs 0,17 %** | 3A +10,78 % · 5A +0,63 % · 97 % inmobiliario · 2022 −20,1 % | Renta de alquiler: la única fuente de retorno que no da ninguna otra posición | Década mala, 64,8 % EE. UU. y **es RV**: en un 2008 cae como la bolsa |
| **Cobas International 2,33 %** | 3A +26,47 % · 5A +17,11 % · vol 12,34 % · 21,7 % energía | Value global con cero solape con Europa | El fondo más caro de la cartera: **116 €/año, el 27 % de todo el coste**; soft close (solo se amplía desde los 1.000 € que ya se tienen) |
| **Rock 0,41 %** | 78 % RV / 22 % RF · 9 indexados · +83,44 % desde 2020 | Cartera automatizada que ya cubre USA, Japón, Europa, Pacífico y EM | 6.600 € de RF con un bono a 20+ años que perdió −17,03 % en 2026; **no se toca** por la plusvalía latente |

---

## 5. Qué entra y qué sale

| | Sale | Entra | Por qué, con el número |
| --- | --- | --- | --- |
| **Crédito** | **Sissener Corporate Bond R**<br>0,90 % · 3A +6,85 % · 5A +5,51 % · vol 2,05 % | **Amundi EUR Corp 1-5Y**<br>0,35 % · 3A +3,55 % · 5A +0,78 % · vol 2,21 % | No es sustitución de vehículo, es **cambio de activo**: el top-10 del Sissener son bonos HY de energía y shipping (Nynas 11,75 %, Golar LNG 7,75 %, W&T Offshore 10,75 %, McDermott 10,5 %; un tercio del fondo). Su 3A alto era prima de crédito, no carry de calidad. Se renuncia a 3,3 pp de 3A para no comprar lo que la señal «prima de crédito» dice no comprar |
| **RV value Europa** | **MyInvestor Value C**<br>TER **no publicado** · 3A/5A **no publicados** · vol 1A 17,76 % | **iShares Europe** (más peso)<br>0,10 % · 3A +17,58 % · 5A +9,74 % | No se puede defender un fondo cuyo coste no aparece en la plataforma. La tesis (Europa small/mid a 0,8x valor en libros) se conserva, pero se paga a 0,10 % en vez de a ~1,45 % + 9 % de éxito |
| **Peso de RF** | **Neuberger 31.900 €** (era el 32,9 % de la cartera) | **Neuberger 17.000 €** + 14.400 € repartidos entre Cobas Renta, Aegon y Amundi | La mayor concentración de la cartera deja de estar en un solo gestor: 17,5 % frente a 32,9 %. Cuesta ≈37 €/año de carry perdido (5.000 € al diferencial Neuberger-Amundi) y compra que ninguna ficha, ninguna curva y ningún derivado decidan el 33 % del capital |
| **RV total** | **50,0 % de RV** | **54,9 % de RV** | §2 |

**Lo que NO cambia y por qué.** Rock se queda (plusvalía del 83,44 %: desmontarla tributa). El
colchón de 10.000 € se queda fuera de la cartera y sin dimensionar contra gastos reales, que sigue
siendo la única cifra pendiente del titular. Las cinco reglas de la casa (acumulación, traspaso y
nunca reembolso, cada euro es RV o RF, coste verificado, cero comisiones de éxito) siguen en pie: la
de «cada euro es RV o RF» ya no excluye a los mixtos, pero Cobas Renta entra **contabilizado**, con su
14,5 % de bolsa sumado a la RV. No se usa un mixto para esconder bolsa.

---

## 6. Métricas

| Métrica | Cartera del 03/11 | **Definitiva** | Delta |
| --- | ---: | ---: | ---: |
| Renta variable (look-through) | 48,4 % | **54,9 %** | +6,5 pp |
| TER manual | 532 €/año (0,549 %) | **303 €/año (0,452 %)** | −229 € |
| Comisiones de éxito | 52 €/año (Value 9 %) | **0 €/año** | −52 € |
| **Coste total real** | **584 €/año (0,602 %)** | **426 €/año (0,439 %)** | **−158 €/año (−27 %)** |
| Duración RF manual | ≈3,3 años | **≈2,3 años** | −1,0 |
| Duración RF total (con Rock) | ≈3,3 años | **≈3,6 años** | +0,3 |
| Impacto +100 pb | −1.600 € | **−1.590 €** | igual |
| Carry YTW de la RF manual | 4,42-4,67 % | **≈4,24 % (1.545 €)** | −0,2 pp |
| Cobrado 1A de la RF manual | ≈0-3 % | **≈1,3 %** | igual de malo |
| Caída tipo 2008 (RV −40 %, RF −3 %) | −20,9 % | **−23,3 %** | −2,4 pp |
| Retorno esperado (EY + carry) | 5,6 % | **5,56 %** | igual |
| Retorno esperado (EY + crecimiento 4 %) | 7,6 % | **7,76 %** | +0,2 pp |
| Posiciones | 8 manuales + Rock | **8 manuales + Rock** | 0 |
| EE. UU. dentro de la RV | 34,5 % | **31,5 %** | −3,0 pp |
| Mayor concentración de gestora | Neuberger 32,9 % | **BlackRock 29,8 %** (todo indexado) | −3,1 pp |

**Dónde está el ahorro.** 229 € de TER: los 52 € del éxito de MyInvestor Value que desaparecen, 41 €
del cambio Sissener 0,90 % → Amundi 0,35 % sobre 7.400 €, y el resto de bajar el peso de los vehículos
caros (Cobas International pesa lo mismo y sigue costando 116,5 €: es el 27 % de todo el coste).

**Lo que la duración no baja, y hay que decirlo.** La RF manual baja a 2,3 años, pero la **total sube a
3,6** porque la RF dentro de Rock (6.600 €, con 3.000 € en el bono a 20+ años) pesa ahora más al haber
menos RF manual. **El 76 % del riesgo de tipos de la cartera vive en Rock y no se puede tocar.** Cada
+100 pb cuesta ≈1.590 €, el 1,6 % del capital.

**Lo que el 2022 dice de este cambio.** Con RV −25 % y RF −3 %, la cartera del 03/11 perdía 19.600 €;
esta pierde 22.600 € en el mismo escenario, porque lleva 6,5 pp más de bolsa. La contrapartida es el
retorno esperado: +0,2 pp anuales con crecimiento. **Es un cambio de riesgo, no una mejora gratis**, y
por eso §2 tiene un suelo conductual escrito.

---

## 7. Las órdenes, paso a paso

Todo por **traspaso entre fondos armonizados**: 0 € de impuestos. Dos suscripciones con los 7.000 € de
aportación nueva. **Doce órdenes, 49.000 €**, en dos sesiones: la ventana de crédito de 6-12 meses que
cita Ábaco no se cubre entrando en tres tandas mensuales.

### Paso 0 — Preparación

- [ ] Transferir **7.000 €** a la cuenta de MyInvestor y verlos en efectivo.
- [ ] Comprobar saldos: Neuberger **22.000** · DNCA **13.000** · Carmignac **12.000** · Gamma **8.000** ·
      MyInvestor Value **2.000** · Cobas **1.000** · Space **1.000** · China **1.000** = **60.000 €**.
      Rock queda fuera, con 30.000 €.
- [ ] Reembolso: **0,00 %** verificado el 31/10 en Gamma, Space, China, Carmignac y DNCA. Repetir solo si
      alguna ficha ha cambiado.
- [ ] Confirmar la **comisión de entrada** de Aegon, Amundi, iShares Europe, REITs y Cobas Renta (no
      publicada). Si alguna fuera >1 %, se acepta o se cambia de destino; no se esquiva con dos tandas.
- [ ] Recordar el ⚠️ del **Neuberger: «hasta 3 %»** de entrada sobre lo que reciba. Aquí recibe 0 €
      (solo sale), así que este año no aplica.
- [ ] **Traspaso, nunca reembolso.** Es lo que deja la factura fiscal en 0 €.

### 7.1 Sesión 1 — 32.000 € · 6 órdenes

| Hecho | # | Origen | € | Destino | Antes de |
|:--:|--:|---|---:|---|---|
| ☐ | 1 | Aportación nueva (efectivo) | 4.000 | Cobas International P | 12:00 |
| ☐ | 2 | Aportación nueva (efectivo) | 3.000 | iShares Emerging Markets S | **09:00** |
| ☐ | 3 | Neuberger Short Duration | 5.000 | iShares Europe | **09:00** |
| ☐ | 4 | DNCA Alpha Bonds A | 8.600 | iShares Europe | **09:00** |
| ☐ | 5 | DNCA Alpha Bonds A | 4.400 | Amundi EUR Corp 1-5Y | 12:00 |
| ☐ | 6 | Carmignac Portfolio Credit A | 7.000 | Aegon European ABS | 12:00 |

Cortes: emergentes, Europa, DNCA y Neuberger cortan a las **09:00**; Amundi, Aegon y Cobas a las 12:00.
La de emergentes y las de Europa van primero porque son las que cortan antes.

Checks al cerrar la sesión 1: DNCA a **0** · Carmignac en **5.000** · Neuberger en **17.000** ·
Cobas en **5.000** · Europa en **13.600** (ya está completa y no se vuelve a tocar) · Amundi en
**4.400** · Aegon en **7.000** · EM en **3.000**.

### 7.2 Sesión 2 (2-3 días después) — 17.000 € · 6 órdenes

| Hecho | # | Origen | € | Destino | Antes de |
|:--:|--:|---|---:|---|---|
| ☐ | 7 | Carmignac Portfolio Credit A | 5.000 | iShares Developed Real Estate | 12:00 |
| ☐ | 8 | Gamma Global A | 5.000 | Cobas Renta | 12:00 |
| ☐ | 9 | Gamma Global A | 3.000 | Amundi EUR Corp 1-5Y | 12:00 |
| ☐ | 10 | MyInvestor Value C | 2.000 | iShares Emerging Markets S | **09:00** |
| ☐ | 11 | NB Next Generation Space | 1.000 | iShares Emerging Markets S | **09:00** |
| ☐ | 12 | UBS MSCI China | 1.000 | iShares Emerging Markets S | **09:00** |

Gamma corta a las 14:00 pero sus destinos a las 12:00: manda la más temprana. La sesión se separa porque
el saldo residual de Carmignac y los 8.000 € de Gamma solo quedan libres cuando han acreditado los
traspasos de la sesión 1 (lag de 2-3 días); adelantarlos obligaría a dejar saldos negativos.

### 7.3 Comprobación final

- [ ] Neuberger 17.000 · Cobas Renta 5.000 · Aegon 7.000 · Amundi 7.400 · Europa 13.600 · EM 7.000 ·
      REITs 5.000 · Cobas Intl 5.000 = **67.000 €**.
- [ ] Rock intacto en **30.000 €**. Total **97.000 €**.
- [ ] DNCA, Carmignac, Gamma, MyInvestor Value, Space y China a **0**.
- [ ] RV 54,9 % / RF 45,1 % look-through. Coste **426 €/año**: 303 manuales + 123 de Rock.
- [ ] Justificantes de los **diez traspasos** archivados (prueba del 0 % fiscal).

**Cuadre por origen:** DNCA 13.000 · Carmignac 12.000 · Gamma 8.000 · Neuberger 5.000 · MyInvestor
Value 2.000 · Space 1.000 · China 1.000 · aportación 7.000 = **49.000 €**.
**Cuadre por destino:** Aegon 7.000 · Amundi 7.400 · Cobas Renta 5.000 · Europa 13.600 · EM 7.000 ·
REITs 5.000 · Cobas Intl +4.000 = **49.000 €**.

### 7.4 Lo que no se debe hacer

- **No reembolsar** para suscribir después: se pierde el diferimiento fiscal.
- **No cambiar de clase** los fondos que se quedan (equivale a reembolso).
- **No comprar Amundi, Aegon ni Cobas Renta con más de 7.500 €** hasta ver un trimestre.
- **No desmontar Rock.** La plusvalía del 83,44 % es dinero real; el 20+ de su interior se acepta.

---

## 8. Riesgos y límites

- **Cobas Renta es un mixto flexible, y eso es una excepción declarada.** 28 % en liquidez, 42 % en
  Alemania, 3,9 % en Ghana y 14,5 % en bolsa. Su 5A +6,79 % sale de apuestas que pueden no repetirse;
  lo que se compra no es el 5A, es el **+3,89 % de 2022** frente al −5,68 % del Neuberger. Si en dos
  años no repite esa defensa, sale.
- **Se renuncia a 3,3 pp de 3A al cambiar Sissener por Amundi.** La tesis es que esos 3,3 pp eran prima
  de high yield, no carry. Si el crédito se tensa y el HY aguanta, esta decisión se verá peor que la
  anterior: es una apuesta macro (la de Ábaco), no un hecho.
- **La duración total sube a 3,6 años** aunque la manual baje a 2,3, porque Rock concentra el bono
  largo. Es el límite principal de §6 y no tiene arreglo sin tocar Rock.
- **Concentración de proveedor:** BlackRock pasa a ser el 29,8 % (todo indexado). Es riesgo operativo,
  no de exposición; si molesta, la clase europea pasa a Amundi Core MSCI Europe (0,15 %) por +7 €/año.
- **Un 42 % de los emergentes es tecnología.** Comprar emergentes hoy es comprar semiconductores con
  otro nombre (TSMC + Samsung + SK Hynix ≈ 29 % del índice).
- **Europa al 32 % de la RV** (frente al 15 % de un ACWI) es una sobreponderación declarada, no
  neutralidad. Si Europa no revaloriza, esta cartera lo verá peor que un World.
- **El colchón de 10.000 € nunca se dimensionó contra gastos reales.** Cubre si el gasto mensual está
  entre 833 € y 1.667 €. Si es mayor, el colchón se redimensiona **antes** de ejecutar §7: 3.000 € más
  son 3.000 € menos de cartera.
- **Comisión de entrada desconocida** en Amundi, Aegon, Cobas Renta, iShares Europe y REITs. Si alguna
  cobrara más del 1 %, el ahorro de 158 €/año se come el primer año.
- **TIR y duración de Cobas Renta, Aegon y Amundi no publicadas:** la duración de 2,3 años y el carry
  de 4,24 % son **inferidos**, no de ficha.
- **Ninguna cifra de retorno está prometida.** El −23,3 % es una estimación con RV −40 %; el mercado
  puede hacer algo que no está en ninguna tabla.

---

## 9. Diversificación

### 9.1 Bloques funcionales

| Bloque | Qué hace | € | % |
| --- | --- | ---: | ---: |
| RF corta corporativa IG | Amortiguador con cupón, duración 1,95 | 17.000 | 17,5 % |
| RF flexible value | El que ganó en 2022; 14,5 % de bolsa contabilizada | 5.000 | 5,2 % |
| RF flexible ABS | Titulizaciones europeas de corta vida | 7.000 | 7,2 % |
| RF corporativa IG 1-5Y | Indexado del mismo riesgo, sin gestor | 7.400 | 7,6 % |
| RV Europa large | Beta barata donde la valoración paga | 13.600 | 14,0 % |
| RV emergentes | Crecimiento y descorrelación a 10,2x | 7.000 | 7,2 % |
| Activos reales (REITs) | Renta de alquileres | 5.000 | 5,2 % |
| RV value global | Alpha activo verificado, cero solape con Europa | 5.000 | 5,2 % |
| Cartera automatizada | 78 % RV / 22 % RF en 9 indexados | 30.000 | 30,9 % |

### 9.2 Geografía de la RV (look-through, estimación declarada)

| Región | % de la RV | % de la cartera |
| --- | ---: | ---: |
| Europa (Reino Unido 6,4 · Suiza 4,5 · Alemania 4,0 · Francia 3,9 · España 1,8 · resto) | **32,1 %** | 17,6 % |
| Estados Unidos | **31,5 %** | 17,3 % |
| Emergentes (Taiwán, Corea, China, India, Brasil) | **19,4 %** | 10,6 % |
| Japón | **5,1 %** | 2,8 % |
| Otros desarrollados (Canadá, Australia, Pacífico) | 2,9 % | 1,6 % |
| Sin desglosar en las fichas (Cobas no publica el 44 %) | 9,0 % | 4,9 % |

Frente a un MSCI ACWI (63 % EE. UU., 15 % Europa, 10 % emergentes): **−31 pp de EE. UU., +17 pp de
Europa, +9 pp de emergentes.** Esa es la tesis entera de la cartera, y se puede medir.

### 9.3 Sectores de la RV (aproximado, top 6 de cada ficha)

| Sector | % de la RV |
| --- | ---: |
| Servicios financieros | 15,4 % |
| Tecnología | 14,8 % |
| Industria | 12,1 % |
| Inmobiliario | 9,7 % |
| Salud | 8,9 % |
| Consumo defensivo | 5,3 % |
| Consumo cíclico | 4,2 % |
| Energía | 2,6 % |
| Sin desglosar (resto de fichas y Rock) | 27,0 % |

Tecnología al 14,8 % de la RV frente al 30,8 % de un MSCI World: la cartera no compra la tesis de la IA.

### 9.4 Concentración por gestora

| Gestora | € | % cartera | Qué aporta |
| --- | ---: | ---: | --- |
| BlackRock / iShares | 28.900 | 29,8 % | Europa, EM y REITs (manual) + EM de Rock. Todo indexado |
| Neuberger Berman | 17.000 | 17,5 % | RF corta |
| Fidelity | 14.700 | 15,2 % | Solo dentro de Rock (S&P 500, Japón, Europa) |
| Cobas | 10.000 | 10,3 % | Renta (value) + International |
| Amundi | 7.400 | 7,6 % | RF corporativa 1-5Y |
| Vanguard | 7.200 | 7,4 % | Solo dentro de Rock |
| Aegon | 7.000 | 7,2 % | ABS |
| Goldman Sachs | 4.200 | 4,3 % | Dentro de Rock |
| Groupama | 10.000 | — | Colchón, fuera de la cartera |

Ninguna gestora activa pasa del 17,5 %; el 29,8 % de BlackRock son cuatro fondos indexados sin decisión
de gestor.

### 9.5 Divisas (sin cobertura)

| Divisa | % de la cartera |
| --- | ---: |
| EUR | ≈36 % |
| USD | ≈24 % |
| GBP | ≈12 % (Europa 21 % UK + Aegon 31 % UK) |
| JPY | ≈4 % |
| Emergentes (TWD, KRW, CNY, INR, BRL) | ≈6 % |
| NOK / SEK / DKK | ≈3 % |
| Sin desglosar (Cobas) | ≈15 % |

La cartera **no cubre divisa**. Cubrir a 10 años cuesta 1,5-2 % anual en diferencial de tipos y se come
el premio: es una decisión, no un descuido.

---

## 10. Lo que se descarta del catálogo, con el número

| Candidato | Ficha | Por qué no |
| --- | --- | --- |
| **Sissener Corporate Bond** | 0,90 % · 3A +6,85 % · 5A +5,51 % | Su top-10 es HY de energía y shipping (Nynas, Golar, W&T, McDermott): comprar 3A alto con prima de crédito es exactamente lo que la señal 2 prohíbe |
| **iShares Euro IG Corporate** (IE00BDRK7J14) | 0,12 % · 3A +4,17 % · 5A +0,13 % · 2022 −13,26 % | Duración ~5: perdió 13 pp en 2022. El TER mínimo no compensa el riesgo de tipos |
| **Vanguard Euro IG Bond** (IE00B04FFJ44) | 0,12 % · 3A +3,37 % · 5A −0,88 % | Misma duración larga y menos retorno que el Amundi 1-5Y al mismo precio |
| **Vanguard Global Short-Term Corp USD H** (IE00BDFB7308) | 0,18 % · 3A +5,47 % · 2022 −5,99 % | Bate al Neuberger en 3A, pero la clase es USD sin cubrir a EUR y su 2022 fue peor |
| **AXA Trésor Court Terme** (FR0000447823) | 0,05 % · 3A +2,95 % · vol 0,24 % | Liquidez al €STR: no es inversión. El colchón ya está fuera de la cartera; una segunda reserva dentro duplicaría la liquidez |
| **JPM Europe Strategic Value** (LU0210531983) | 1,72 % · 3A +22,65 % · 5A +14,08 % | **43,9 % servicios financieros** large cap: es una apuesta sectorial, y la cartera ya lleva el 24,7 % de financieros en el índice |
| **Fundsmith** (LU0690375182) | 1,09 % · 3A +7,78 % · 5A +2,93 % | Cede 334 €/año frente al indexado europeo en la misma pata y es 79,6 % EE. UU. y 32,2 % tecnología |
| **Comgest Growth Europe** (IE0004766675) | 1,59 % · 3A +2,79 % · 5A **−0,94 %** | Cinco años perdiendo contra el índice de su propia región: no hay caso |
| **Morgan Stanley Global Brands** (LU2295319300) | 1,84 % · 26 años · 5A +0,97 % | La etiqueta «marcas con poder de precio» no paga: +1 % anual en cinco años |
| **Horos Value Internacional** | 1,90 % · 3A +16,98 % · 5A +11,92 % | Pierde las dos ventanas contra Cobas y solapa TGS y Francia con lo que ya hay |
| **Azvalor Internacional** | Reembolso 3 % bajo 12 meses | Incompatible con la ejecución y 60 % energía/materia prima que Cobas ya cubre |
| **Vanguard Global Small-Cap** (IE00B42W4L06) | 0,29 % · 3A +18,64 % · 5A +6,98 % | 61 % EE. UU. y sería la tercera apuesta al mismo factor. Si algún día se quiere tamaño, entra aquí a 0,29 % |
| **iShares Developed World S** (IE000ZYRH0Q7) | **0,06 %**, el más barato del catálogo | Dejaría la cartera sin emergentes, sin REITs y con 72 % de EE. UU.: es otro producto, no una versión barata de este |
| **L&G MSCI ACWI IMI** (IE0003PI5332) | 0,16 % · nacido en 2025 · **13 % liquidez** | Sin historial y con lastre de caja, justo cuando la cartera busca cada décima |
| **Amundi Prime Euro Gov** (LU2339731064) | 0,05 % · mínimo **500.000 €** | No es contratable |
| **Cat bonds** (GAM, Twelve) | 3A +9 a +11 % · TER 1,28-1,55 % | Son bonos de catástrofe (ILS), otro activo, con reembolso a 10 días |
| **Oro vía fondo** (DWS, Jupiter) | 1,61-1,66 % · vol 38 % · SRRI 6 | El perfil del NB Space que sale de la cartera. El físico solo existe como ETF y lleva +67,8 % en 2025 |
| **Mixtos baratos tipo Baelo** | 0,64 % | Ahorra ≈64 €/año frente a esta cartera y devuelve el control del riesgo a un tercero: se rechaza por control, no por la regla |

---

## 11. Cuándo se revisa

Trimestral (enero, abril, julio, octubre) y además cuando se cumpla una señal. **El modelo de §2 se
vuelve a puntuar entero: las señales no son aditivas.**

| Señal | Umbral | Efecto |
| --- | --- | ---: |
| Carry cobrado de la RF | Por debajo del 2 % a 12 meses (ya activada en 2026) | **+3** → ~58 % |
| Prima de crédito | HY OAS >700 pb | **−3** → ~52 % (vuelve el crédito) |
| Valoración RV | S&P 500 −20 % con beneficios intactos | **+6** → ~61 % |
| Evento de crédito | Spreads >700 pb y default en curso | **+4** → ~59 % |
| Prima RV-bono | *Earnings yield* − bono <1 pp | **−10** → ~45 % |
| Inflación y tipos | Inflación <2 % y BCE bajando | **−3** → ~52 % |

Además, sobre las cuatro posiciones nuevas o cambiadas:

- **Cobas Renta:** a los 24 meses, si no ha defendido en un año de caída de bolsa como hizo en 2022,
  sale y su dinero va al Neuberger.
- **Amundi 1-5Y:** a los 3 meses, comparar con el Neuberger en retorno y vol. Si la diferencia a 3A
  supera 1,5 pp de forma sostenida, el Neuberger recupera peso.
- **Sissener (seguimiento de la decisión):** si el HY europeo se tensa (OAS >700 pb), era el momento de
  tenerlo y se anota como error de la señal, no como excusa.
- **REITs:** si en dos revisiones el sector sigue en valores de 2012-2023 con el resto alcista, se
  decide con número si se cierra el hueco.
- **Rebalanceo** si un bloque se desvía >5 pp del objetivo; Rock >10 pp de su 78/22.

### 11.1 El marcador de carry cobrado

La señal se mide **cobrado a 12 meses**, no con el YTW. En 2026 la RF manual ha cobrado ≈1,3 % (Neuberger
−0,03 %, Aegon +2,39 %, Amundi −0,19 %) frente a una inflación del 3,8 %: **−2,5 % real**. Por eso el
modelo ya puntúa +3 arriba. El testigo externo sigue siendo Horos Patrimonio (duración 2,5, 80 %
corporativo, esperaba 4,5 % y lleva <2 %): el escenario no es teórico. **Si en la revisión de enero la
RF cobra el carry previsto (≈4,2 %), la señal vuelve a 0 y el modelo baja a 52 %**: no se sube la RV por
un año malo de precios, se sube porque la RF no está pagando su función.

---

## 12. Qué se absorbe y qué se borra

Las cinco propuestas que convivían en la carpeta se han resuelto aquí. **Se borran del árbol** (`git rm`);
el contenido íntegro sigue en el historial de git (commit `50b2e69`).

| Documento | Qué aportaba | Qué se ha hecho con ello |
| --- | --- | --- |
| `propuesta-actual-avanzada.md` (04/11, 55/45, 10 fondos) | El 55 % de RV con tres casas de previsiones; Cobas Renta como RF flexible; AXA Trésor como liquidez | **Adoptado el 55 %** y Cobas Renta. **No adoptado** AXA Trésor (el colchón ya está fuera) ni JPM Europe Strategic Value (43,9 % financieros) |
| `propuesta-perplexity.md` (04/11, 100k desde cero, 12 fondos) | El hallazgo de que **Sissener es HY** al abrir sus posiciones; la tabla de candidatos descartados por bloque | **Adoptado el hallazgo** y el descarte de Sissener. No adoptado el diseño de 12 fondos: no contaba Rock ni la fiscalidad de desmontarla |
| `propuesta-alternativa.md` (01/11, activos reales + calidad) | Los REITs al 0,17 % y la familia «calidad» con 13 fichas | **Adoptados los REITs** (ya estaban). **Descartada la calidad**: Fundsmith cede 334 €/año y Comgest pierde a 5 años |
| `propuesta-investigacion.md` (02/11, dos bloques de acumulación) | La regla de acumulación y el análisis de las cuatro acciones | **Adoptada la regla**. Las acciones salen de esta cartera por decisión del titular: van en `propuesta-acciones.md` como bloque de riesgo aparte |
| `propuesta-actual.md` del 03/11 (50/50, 8 fondos) | Aegon, Sissener, REITs y el barrido por bloques | **Se conservan Aegon y los REITs**; Sissener sale por composición; el barrido se reutiliza en §10 |

**Lo que se mantiene de todas ellas, porque nadie lo ha refutado:** Rock intacta por la plusvalía; el
colchón fuera de la cartera; traspaso y nunca reembolso; cero comisiones de éxito; y cada euro
contabilizado como RV o RF aunque el vehículo sea mixto.

---

## 13. Fuentes

- **Fichas MyInvestor MCP a 04/11/2026** (NAV 30/10/2026): `list_facets` (2.410 fondos, 266 indexados),
  `search_funds` por bloque y `get_funds` por ISIN de iShares Europe, Cobas Renta, Aegon, Amundi 1-5Y,
  Neuberger, Cobas International, iShares EM y REITs. TER, comisiones, rentabilidades 3A/5A anualizadas,
  vol 3A/5A, SRRI, países, sectores, mínimo, corte y `distributing = 0` en los ocho.
- **`cartera-actual.md`** (30/10): saldos, ISIN y composición de Rock.
- **`finance/reports/sintesis-inversor-2026-10-30.md`** e **`informe-canal-la-pizarra-de-andres-2026-11-02.md`**:
  principios del §2 (coste, duración, valoración, concentración del S&P) y la probabilidad de evento de
  crédito de Ábaco.
- **Horos, La Pizarra de Andrés 30/10/2026**: testigo de carry cobrado (§11.1) y descarte de Horos Value.
- **Parages, webinar MyInvestor 20/10**: Japón (cubierto por índice dentro de Rock).
- **Clase de Ackman (Big Think 2012)**: criterio del colchón y del horizonte.

Límites: la duración y la TIR de Aegon, Amundi 1-5Y y Cobas Renta **no están publicadas** (2,3 años y
4,24 % inferidos); la vol y el carry de la RF de Rock no se publican; el 44 % de la cartera de Cobas no
viene desglosado por país; la comisión de entrada de cinco fondos no es pública; el drawdown y el
retorno esperado son estimaciones propias; las señales del §2 llevan pesos de juicio, no calibrados con
series históricas; los gastos mensuales del colchón siguen sin dimensionar.

> No es asesoramiento financiero. Es una cartera construida sobre fichas del bróker y sobre lo que cinco
> profesionales dicen en vídeo, con sus intereses comerciales a la vista. La decisión es del titular.

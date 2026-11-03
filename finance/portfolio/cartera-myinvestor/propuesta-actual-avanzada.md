---
title: "Propuesta avanzada: 50/50 con renta fija de ABS y crédito nórdico (97.000 €)"
date: 2026-11-03
type: portfolio-proposal
category: finance
tags: [cartera, propuesta, renta-fija, abs, aegon, sissener, rebalanceo, myinvestor, avanzada]
status: propuesta
related:
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
  - finance/portfolio/cartera-myinvestor/propuesta-actual.md
---

# Propuesta avanzada — 03/11/2026

> **Alternativa a la propuesta vigente, pendiente de decisión del titular.** Nace de barrer el catálogo
> completo de MyInvestor (2.410 fondos) posición por posición con el MCP, y cambia **dos fondos de renta
> fija** respecto a `propuesta-actual.md`: entran Aegon European ABS y Sissener Corporate Bond en lugar
> de DNCA Alpha Bonds y Carmignac Portfolio Credit.
>
> Lo que no cambia: el 50/50, Rock, los cinco fondos de renta variable, la aportación de 7.000 € y la
> fiscalidad por traspaso. Lo que sí cambia, y no es un detalle: **las once órdenes de la vigente se
> sustituyen por doce** (35.000 € traspasados en vez de 25.000), y **el DNCA no se cambia por un
> equivalente**: sale el único soberano A+ de la parte manual y entra titulización. Es una rotación de
> soberano a ABS, no un simple cambio de vehículo. Si se adopta, sustituye a `propuesta-actual.md` y este
> fichero se borra.
>
> **Cifras verificadas con la fuente:** los datos de ficha de este documento (Aegon, Sissener, DNCA,
> Carmignac, Neuberger) se re-verificaron el **03/11/2026 contra las fichas MyInvestor vía MCP**
> (`get_funds`, NAV 30/10/2026): TER, comisiones de gestión y éxito, rentabilidades 3A/5A y por año
> natural, volatilidad 3A y 5A, SRRI, sectores, países, mínimos, cortes, incept y clase de acumulación.
> Cuadran todas; la novedad que trae la ficha y no estaba publicada: la **vol 5A de Aegon es 1,90 %**
> (la 0,95 % que se cita a 3 años está suavizada por el precio del ABS).

## 1. Qué cambia: 2 de 8 posiciones, 10.000 € (10,3 % de la cartera)

| | Sale | Entra | Por qué |
|---|---|---|---|
| **RF flexible** | DNCA Alpha Bonds A<br>1,31 % + 20 % éxito · 3A +4,17 % · **5A +4,75 %** · vol 2,00 % | **Aegon European ABS A EUR Acc**<br>**0,66 % sin éxito** · 3A **+4,38 %** · **5A +2,94 %** · vol 3A **0,95 %** (5A **1,90 %**) | −52 % de coste y de vol a 3A, pero la vol 5A baja solo **−29 %** (1,90 frente a 2,68: la vol 3A del ABS está suavizada); gana 0,21 pp a 3 años y **cede 1,81 pp a 5 años** |
| **Crédito** | Carmignac Portfolio Credit A<br>1,20 % + 20 % éxito · 3A +6,45 % · **5A +1,83 %** · vol 3,62 % · **2022 −13,0 %** | **Sissener Corporate Bond R EUR**<br>**0,90 % sin éxito** · 3A **+6,85 %** · **5A +5,51 %** · vol 3A **2,05 %** (5A **2,75 %**) · **2022 +0,2 %** | Más retorno en las tres ventanas, −43 % de vol a 3A y −50 % a 5A (2,75 frente a 5,54), y no perdió en 2022 |

Una es sustitución de vehículo y la otra no. **Sissener sí**: crédito por crédito, mismos euros, otro
gestor y menos comisión. **Aegon no**: DNCA es 79 % deuda pública G10 con rating A+ y Aegon es 99 %
titulización; el bloque sigue llamándose «RF flexible» y pesando 5.000 €, pero el activo de dentro es
otro. Se puede hacer el cambio —menos duración y menos volatilidad—, pero se hace como cambio de riesgo,
no como cambio de gestor.

## 2. La cartera (97.000 €)

| Bloque | Fondo | ISIN | € | % | RV dentro | TER |
|---|---|---|---:|---:|---:|---:|
| RF corta IG | Neuberger Short Duration Euro Bond U | IE00BL1GVT98 | 31.900 | 32,9 % | 0 % | 0,38 % |
| RF flexible (ABS) | **Aegon European ABS A EUR Acc** | **IE00BG226Z29** | 5.000 | 5,2 % | 0 % | **0,66 %** |
| Crédito | **Sissener Corporate Bond R EUR** | **LU2262944817** | 5.000 | 5,2 % | 1,6 % | **0,90 %** |
| RV value Europa | MyInvestor Value C | ES0165243025 | 5.000 | 5,2 % | 95,4 % | ~1,42 % + 9 % éxito |
| RV value global | Cobas International P | LU1598719752 | 5.000 | 5,2 % | 72,9 % | 2,33 % |
| RV small cap | Vanguard Global Small-Cap EUR Acc | IE00B42W4L06 | 3.700 | 3,8 % | 100 % | 0,29 % |
| RV Europa | Fidelity MSCI Europe P Acc | IE00BYX5MD61 | 5.000 | 5,2 % | 99,4 % | 0,10 % |
| RV emergentes | iShares Emerging Markets S Acc | IE000QAZP7L2 | 6.400 | 6,6 % | 100 % | 0,16 % |
| Cartera automatizada | Rock 78/22 | — | 30.000 | 30,9 % | 78 % | 0,41 % todo incluido |
| | **TOTAL** | | **97.000** | **100 %** | | |

**Reparto:** RV **48.500 € (50,0 %)** / RF **48.500 € (50,0 %)**, con la misma convención que la
propuesta vigente (los satélites activos cuentan al 100 %, Rock al 78 %). **17 posiciones** (8
manuales + 9 de Rock). Fuera de la base: 10.000 € de Groupama Trésorerie.

## 3. Métricas: avanzada frente a la vigente

| Métrica | `propuesta-actual` | **Avanzada** | Delta |
|---|---:|---:|---:|
| Renta variable | 50,0 % | **50,0 %** | 0 |
| TER puro (sin comisiones de éxito) | 583 €/año (0,601 %) | **536 €/año (0,552 %)** | **−47 €** |
| Comisiones de éxito reales | ≈86 €/año (DNCA 16 · Carmignac ≈18 · Value 52) | **52 €/año (solo Value)** | **−34 €** |
| **Coste total real** | **≈669 €/año (0,690 %)** | **588 €/año (0,606 %)** | **−81 €/año (−12,1 %)** |
| VOL de la pata cambiada (3A) | DNCA 2,00 · Carmignac 3,62 | **Aegon 0,95 · Sissener 2,05** | −1,05 y −1,57 pp |
| VOL de la pata cambiada (5A) | DNCA 2,68 · Carmignac 5,54 | **Aegon 1,90 · Sissener 2,75** | −0,78 y −2,79 pp |
| Retorno 3A del bloque de RF (estimado) | 4,60 % | **4,67 %** | +0,07 pp |
| Comportamiento del bloque en 2022 (estimado) | −5,4 % | **−5,0 %** | +0,4 pp |
| Duración estimada de la RF (con Rock) | 3,67 años | **≈3,3 años** (3,2-3,5, inferida) | −0,2 a −0,4 |
| Carry de la RF | 4,79 % (2.007 €) | 4,42-4,67 % (1.852-1.957 €) | −50 a −155 € |
| Drawdown 2008 (RV −40 %, RF −3 %) | −21,5 % | **−21,5 %** | 0 |
| Posiciones | 17 | **17** | 0 |
| EE. UU. dentro de la RV | 32,5 % | **32,5 %** | 0 |

**Dónde está el ahorro, desglosado:** 47 € de TER y 34 € de comisiones de éxito. La vigente estimaba
el éxito de MyInvestor Value (52 €) pero no el de DNCA y Carmignac, que **cobran el 20 % solo sobre lo
que baten a su índice y con high-water mark**, no sobre el cupón: la ficha de la gestora declara que
DNCA cobró de verdad **0,32 %** (16 €/año sobre 5.000 €) y Carmignac cobra 20 % sobre 75 % ICE BofA
Euro Corporate + 25 % Euro High Yield con clawback de 5 años (≈18 €/año). El coste real de la vigente
es **≈669 €/año**, no 635 € ni 715 €.

**Lo que el 2022 esconde.** La mejora de 0,4 pp del bloque sale de que las dos sustituciones se
cancelan: Carmignac −13,0 % → Sissener +0,2 % aporta +660 € y DNCA +6,0 % → Aegon −4,0 % quita −500 €.
A nivel de fondo, el cambio de DNCA es **−10 pp en el peor año**. Si se cambiara solo Carmignac y se
quedara DNCA, el bloque haría **−3,8 %** en vez de −5,0 %.

**Lo que la duración no baja.** De 3,67 a ≈3,3 años (3,2-3,5), no a 2,5: el 77,5 % del riesgo de tipos
está en el Neuberger (35 %) y en Rock (42,5 %), que no se tocan, y los 10.000 € que cambian son el 22,5 %.
Con la cartera entera el suelo matemático es 2,84 años aunque los dos fondos nuevos tuvieran duración
cero. Medido en euros, cada +100 pb cuesta ≈1.600-1.680 € en vez de 1.778 (100-180 € menos), no 570 €.

## 4. Las acciones, paso a paso

Todo se ejecuta **en una semana**, en tres sesiones. **Diez traspasos y dos suscripciones**, 42.000 €
(35.000 € que salen de cinco fondos + 7.000 € de aportación nueva). El ritmo es una decisión aparte:
la vigente lo dejó abierto en su §9 (tres tandas mensuales), y aquí se resuelve en una semana sin
discutirlo. Las casillas de la columna «Hecho» pasan de **☐** a **☑** cuando el titular confirma la
operación, y la fecha real se anota en §4.7; las listas de checks
de cada día se marcan con `[x]` en el mismo momento. Si algo falla, se escribe al lado qué orden y por
qué, en vez de marcarla.

### Paso 0 — Preparación (antes del día 1)

- [ ] Transferir **7.000 €** a la cuenta de MyInvestor y verlos en efectivo.
- [ ] Comprobar los saldos de partida: Neuberger **22.000**, DNCA **13.000**, Carmignac **12.000**,
      Gamma **8.000**, MyInvestor Value **2.000**, Cobas **1.000**, Space **1.000**, China **1.000** =
      **60.000 €**. Rock queda fuera, con 30.000 €.
- [ ] Reembolso: **ya verificado el 31/10** — 0,00 % en Gamma, Space, China, Carmignac y DNCA. Repetir
      solo si alguna ficha ha cambiado desde entonces.
- [ ] Confirmar la **comisión de entrada** de Aegon y Sissener (no publicada). Si alguna fuera >1 %, no
      se esquiva entrando en dos tandas (una comisión proporcional se paga igual): se acepta o se
      cambia de destino.
- [ ] Recordar el ⚠️ del **Neuberger: «hasta 3 %»** de entrada = **hasta 297 € una vez** sobre los
      9.900 € que recibe. Es el único coste de entrada conocido del plan.
- [ ] Recordar: **traspaso, nunca reembolso**. Es lo que deja la factura fiscal en 0 €.

### 4.1 Día 1 — 18.700 € · 3 traspasos + 2 suscripciones

| Hecho | # | Origen | ISIN origen | € | Destino | ISIN destino | Antes de |
|:--:|--:|---|---|---:|---|---|---|
| ☐ | 12 | Aportación nueva (efectivo) | — | 4.000 | Cobas International P | LU1598719752 | 14:00 |
| ☐ | 6 | Carmignac Portfolio Credit A | LU1623762843 | 5.000 | Aegon European ABS A | IE00BG226Z29 | 12:00 |
| ☐ | 8 | Carmignac Portfolio Credit A | LU1623762843 | 5.000 | Fidelity MSCI Europe P | IE00BYX5MD61 | 12:00 |
| ☐ | 11 | Aportación nueva (efectivo) | — | 3.000 | MyInvestor Value C | ES0165243025 | 12:00 |
| ☐ | 7 | Carmignac Portfolio Credit A | LU1623762843 | 1.700 | Vanguard Global Small-Cap | IE00B42W4L06 | 16:00 |

**Cobas primero, solo por orden operativo.** Su ficha dice que está en soft close y que *«solo los
inversores que ya sean partícipes podrán seguir invirtiendo»*: el titular ya lo es (1.000 €), así que
la aportación está permitida y no hay ventana que se cierre. Se pone primero para no dejarlo al final.
*Carmignac queda con 300 €.*

Checks al cerrar el día 1:

- [ ] Cobas, Aegon, Fidelity Europe, MyInvestor Value y Small-Cap figuran con importe abierto.
- [ ] Carmignac tiene **300 €** de saldo, ni 0 ni el importe anterior.
- [ ] Los 7.000 € de aportación ya no están en efectivo.
- [ ] Justificantes de los cinco traspasos guardados.

### 4.2 Día 2 o 3 — 13.300 € · 4 traspasos

| Hecho | # | Origen | ISIN origen | € | Destino | ISIN destino | Antes de |
|:--:|--:|---|---|---:|---|---|---|
| ☐ | 4 | DNCA Alpha Bonds A | LU1694789451 | 6.400 | iShares Emerging Markets S | IE000QAZP7L2 | **09:00** |
| ☐ | 5 | DNCA Alpha Bonds A | LU1694789451 | 5.000 | Sissener Corporate Bond R | LU2262944817 | 10:00 |
| ☐ | 2 | DNCA Alpha Bonds A | LU1694789451 | 1.600 | Neuberger Short Duration | IE00BL1GVT98 | 10:00 |
| ☐ | 3 | Carmignac Portfolio Credit A | LU1623762843 | 300 | Neuberger Short Duration | IE00BL1GVT98 | 10:00 |

La de emergentes antes de las **09:00** (es la que corta primero); las otras tres antes de las **10:00**,
que es el corte de DNCA, Sissener y Neuberger.

Checks al cerrar el día 2:

- [ ] Neuberger en **23.900 €** (22.000 + 1.600 + 300; los 8.000 de Gamma entran el día 3, 31.900 es
      el saldo final).
- [ ] iShares Emergentes en **6.400 €**.
- [ ] Sissener en **5.000 €**.
- [ ] DNCA y Carmignac a **0**.

### 4.3 Día 4 o 5 — 10.000 € · 3 traspasos

| Hecho | # | Origen | ISIN origen | € | Destino | ISIN destino | Antes de |
|:--:|--:|---|---|---:|---|---|---|
| ☐ | 1 | Gamma Global A | ES0140794001 | 8.000 | Neuberger Short Duration | IE00BL1GVT98 | 10:00 |
| ☐ | 9 | NB Next Generation Space | IE00018YKVN0 | 1.000 | Vanguard Global Small-Cap | IE00B42W4L06 | 16:00 |
| ☐ | 10 | UBS MSCI China | LU1815002040 | 1.000 | Vanguard Global Small-Cap | IE00B42W4L06 | 16:00 |

Gamma corta a las 14:00 pero el destino corta a las 10:00: manda la más temprana.

Checks al cerrar el día 3:

- [ ] Gamma, Space y China a **0**.
- [ ] Ningún fondo de origen con saldo negativo.
- [ ] Ocho fondos manuales con su saldo final.

### 4.4 Comprobación final (cuando estén las tres sesiones)

- [ ] Neuberger 31.900 · Aegon 5.000 · Sissener 5.000 · Value 5.000 · Cobas 5.000 · Small-Cap 3.700 ·
      Europa 5.000 · EM 6.400 = **67.000 €** manuales.
- [ ] Rock intacto en **30.000 €**. Total **97.000 €**.
- [ ] RV 50,0 % / RF 50,0 % por look-through.
- [ ] Coste 588 €/año (0,606 %): 536 € de TER + 52 € del éxito del 9 % de MyInvestor Value. Comprobar que
      no quedó ninguna comisión de éxito del 20 %.
- [ ] Los justificantes de los **diez traspasos** archivados (son la prueba del 0 % fiscal). Las dos
      suscripciones de 3.000 y 4.000 € son dinero nuevo y no generan diferimiento.

### 4.5 Cuadre por origen y por destino

**Origen:** Gamma 8.000 · DNCA 1.600 + 6.400 + 5.000 = 13.000 · Carmignac 300 + 5.000 + 1.700 + 5.000 =
12.000 · Space 1.000 · China 1.000 · aportación 3.000 + 4.000 = 7.000. **Total 42.000 €**.

**Destino:** Neuberger 8.000 + 1.600 + 300 = **+9.900** (22.000 → 31.900) · Emergentes **6.400** ·
Aegon **5.000** · Sissener **5.000** · Small-Cap 1.700 + 1.000 + 1.000 = **3.700** · Fidelity Europe
**5.000** · Value **+3.000** (2.000 → 5.000) · Cobas **+4.000** (1.000 → 5.000).

### 4.6 Lo que no se debe hacer

- **No reembolsar** para luego suscribir: se pierde el diferimiento fiscal.
- **No cambiar de clase** los fondos que se quedan (equivale a reembolso).
- **No separar la orden 3** (300 €) del resto: es el cuadre de Carmignac.
- **No comprar Aegon ni Sissener con más de 5.000 €** hasta ver un trimestre de comportamiento.

### 4.7 Registro de ejecución

| Sesión | Fecha real | Importe | Estado |
|---|---|---:|---|
| Día 1 | — | 18.700 € | pendiente |
| Día 2-3 | — | 13.300 € | pendiente |
| Día 4-5 | — | 10.000 € | pendiente |

## 5. Qué mejora y qué no frente a `propuesta-actual`

1. **Cuesta 81 €/año menos**: ≈669 € de coste real frente a 588 €. Son 47 € de comisión fija y 34 € de
   éxito, y hay que decirlo entero: **0,083 pp de la cartera**. No es el argumento para ejecutar el plan;
   el argumento es el riesgo (puntos 2 y 3).
2. **La volatilidad baja en las dos patas, y no solo a 3 años**: 2,00 % → 0,95 % y 3,62 % → 2,05 %
   (−52 % y −43 %, ficha). A 5 años el recorte de Aegon es menor (1,90 % frente a 2,68 % de DNCA,
   **−29 %**) porque la vol 3A de un ABS está suavizada por el precio; Sissener sí aguanta (2,75 %
   frente a 5,54 %, −50 %). El bloque rinde **0,07 pp más** a 3 años (4,60 % → 4,67 %, estimado), pero
   **1,81 pp menos a 5 años en la pata de Aegon** (+2,94 % frente a +4,75 % de DNCA), que sobre 5.000 €
   son 90 €/año. Menos riesgo por algo menos de dinero, no gratis.
3. **Mejor comportamiento en el escenario que de verdad importa, pero por una sola de las dos patas**:
   en 2022 la RF vigente hizo −5,4 % y esta −5,0 %. Carmignac perdió 13,0 % y Sissener ganó 0,2 %
   (+660 €); DNCA ganó 6,0 % y Aegon perdió 4,0 % (−500 €). Las dos se cancelan casi enteras. Si se
   cambiara solo Carmignac y se quedara DNCA, el bloque haría **−3,8 %**: cuatro veces mejor.
4. **Baja la duración entre 0,2 y 0,4 años, no 1,2**: de 3,67 a ≈3,3 (3,2-3,5, porque la duración de los
   dos fondos nuevos no se publica). Cada +100 pb cuesta ≈1.600-1.680 € en vez de 1.778 (100-180 €
   menos). El motivo de que sea tan poco es que el 77,5 % del riesgo de tipos está en el Neuberger (35 %)
   y en Rock (42,5 %), que no se tocan: los 10.000 € que cambian son el 22,5 %. El suelo matemático de la
   cartera entera es 2,84 años aunque los dos fondos nuevos tuvieran duración cero.
5. **Menos concentración en un gestor, más concentración en un país**: Carmignac (BBB−, duración 4,0)
   sale y en su lugar hay ABS europeo (58 % ABS + 35 % RMBS; Reino Unido 31 %, Irlanda 23 %) y crédito
   nórdico (88 % corporativos, **Noruega 41 % + Suecia 17 %**). El riesgo de gestor baja; el de geografía
   sube en el bloque de crédito.
6. **No cambia nada de lo que ya funcionaba**: mismo 50/50, mismo Rock, mismos indexados, mismo sesgo
   Europa/emergentes y misma factura fiscal de 0 €. No se toca ninguna posición de renta variable.
7. **Cada euro de la decisión está verificado con la ficha del bróker** (MCP MyInvestor, NAV
   30/10/2026): Aegon 0,66 % TER, 3A +4,38 %, vol 3A 0,95 % (5A 1,90 %), SRRI 2, mínimo 1 €, corte
   12:00; Sissener 0,90 %, 3A +6,85 %, vol 2,05 % (5A 2,75 %), SRRI 2, mínimo 0,001 participaciones,
   corte 10:00. DNCA y Carmignac: TER con 20 % de éxito y rentabilidades idénticas a la ficha.

## 6. Por qué se ejecutaría, y con qué límite

Porque reduce **riesgo medido** en el bloque de renta fija: la pata cambiada baja 1,05 y 1,57 pp de vol
a 3A (y 0,78 y 2,79 pp a 5A, ficha), el −13,0 % de Carmignac en 2022 queda fuera de la cartera y la
duración baja 0,2-0,4 años. Las vol y las rentabilidades son de ficha; la duración es inferida.

**No** por el argumento que este documento tenía escrito: el 20 % de éxito **no se cobra sobre el
cupón**. DNCA cobra 20 % de lo que bate a €STR+1,40 % con high-water mark, y su gestora declara 0,32 %
cobrado (16 €/año sobre 5.000 €); Carmignac cobra 20 % sobre 75 % ICE BofA Euro Corporate + 25 % Euro
High Yield con clawback de 5 años (≈18 €/año). Son ≈34 €/año, no 80, y el coste real de la vigente es
≈669 €, no 715 €.

Y tampoco por dominancia: **Aegon no domina a DNCA**. Gana en coste, volatilidad y 3A (+0,21 pp), pero
cede 1,81 pp a cinco años (+2,94 % frente a +4,75 %), que sobre 5.000 € son 90 €/año. La ventana de 5
años incluye un ciclo completo de tipos, así que es la que más pesa en un activo de duración. La pata de
Aegon se sostiene como cambio de riesgo (soberano A+ → ABS), no como mejora gratis.

**Lo que esta propuesta NO gana, dicho claro:** el retorno esperado no sube (≈5,6 % frente a 5,7 %),
porque el carry cae entre 50 y 155 €/año según lo que rinda Aegon, que no publica TIR. No es una cartera
para ganar más: es la misma cartera con menos volatilidad y algo menos de coste. Quien quiera más
rentabilidad tiene que subir la RV, y eso es otra decisión (§10 de la vigente).

## 7. Riesgos y límites

- **Aegon European ABS no es soberano.** Es titulización: 58 % ABS y 35 % RMBS, con Reino Unido 31 %,
  Irlanda 23 % y Países Bajos 11 %. Su 2022 fue −4,0 % y su 5A solo +2,94 %: es un activo corto y
  seguro, no un refugio que sube cuando los tipos suben. Pierdes el +6,0 % que hizo DNCA en 2022 y
  **1,81 pp anuales a cinco años** (+4,75 % de DNCA frente a +2,94 %), que son 90 €/año sobre 5.000 €.
- **Esto contradice dos decisiones ya escritas en la carpeta**, y conviene decirlo: `propuesta-actual.md`
  §11 dice que «DNCA se queda porque es el único soberano A+ de la cartera», y `propuesta-incluye-mixto.md`
  cerró la discusión de cambiar esos dos fondos por 111 €/año. Este documento las revisa con otro
  vehículo, no por olvido; pero la decisión de reabrirla es del titular.
- **Sissener concentra 58 % en Noruega y Suecia.** Es crédito nórdico: si ese mercado se abre, cae. Y
  es un fondo pequeño de una gestora nórdica distribuida por FundRock, no una casa global.
- **Ninguno de los dos publica TIR ni duración.** La duración de la cartera baja a ≈3,3 años (3,2-3,5)
  **por inferencia** de la familia del activo, no porque la ficha lo diga. Es el límite principal de §3.
- **Comisión de entrada**: desconocida en los dos fondos nuevos y en el Neuberger («hasta 3 %» = hasta
  297 € una vez). Si Aegon o Sissener cobraran más del 1 %, el ahorro de 81 €/año se come el primer año.
- **Riesgo de gestor**: cambiar dos fondos con historial por dos con menos historial (Sissener nació en
  2019) es cambiar track record por coste y volatilidad.
- **¿Cubre las divisas la clase EUR?** La ficha no lo dice: el 31 % GBP de Aegon y el ~58 % NOK/SEK de
  Sissener pueden entrar en el retorno sin cobertura (§8.5 los cuenta como exposición sin cubrir).
  Es verifiable en la pantalla de suscripción del bróker, no en el catálogo.

## 8. Diversificación por bloques

### 8.1 Bloques funcionales

| Bloque | Qué hace | € | % |
|---|---|---:|---:|
| **RF corta corporativa IG** | Amortiguador: duración 1,95, A−, cupón 4,65 % | 31.900 | 32,9 % |
| **RF flexible (ABS)** | Titulizaciones europeas de corta vida, SRRI 2 | 5.000 | 5,2 % |
| **Crédito nórdico** | Corporativo Noruega/Suecia, 88 % bonos, SRRI 2 | 5.000 | 5,2 % |
| **RV value Europa (small/mid)** | 44 compañías a 0,8x valor en libros, beta 0,40 | 5.000 | 5,2 % |
| **RV value global** | Value global con energía y shipping (22 % energía) | 5.000 | 5,2 % |
| **RV small cap global** | MSCI World Small Cap indexado | 3.700 | 3,8 % |
| **RV Europa large** | MSCI Europe indexado, 350 compañías | 5.000 | 5,2 % |
| **RV emergentes** | MSCI EM indexado, 1.100 compañías | 6.400 | 6,6 % |
| **Cartera automatizada** | 78 % RV / 22 % RF en 9 fondos indexados | 30.000 | 30,9 % |

Dentro de Rock: 23.400 € de RV (24,1 % de la cartera) y 6.600 € de RF (6,8 %).

### 8.2 Tipos de activo (todo el look-through)

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

**Lo que no hay:** oro, materias primas, inmobiliario directo, renta fija emergente, high yield puro,
private equity, cripto, acciones individuales. El inmobiliario solo aparece indirecto: 8,0 % del small
cap y 7,6 % del Value (≈0,7 % de la cartera).

### 8.3 Geografía de la renta variable

| Región | % de la RV | % de la cartera |
|---|---:|---:|
| Estados Unidos | 32,5 % | 16,3 % |
| Europa | 29,0 % | 14,5 % |
| Emergentes | 20,4 % | 10,2 % |
| Japón | 6,6 % | 3,3 % |
| Otros desarrollados (Canadá, Australia, Pacífico) | 2,0 % | 1,0 % |
| Sin desglosar en las fichas | 9,5 % | 4,8 % |

El 9,5 % sin desglosar es sobre todo Cobas, que no publica el país del 44 % de su cartera, y el 6 % de
la RV de Rock que no cae en un país concreto. **Frente a un MSCI ACWI (63 % EE. UU., 15 % Europa, 10 %
emergentes), esta cartera lleva 30,5 pp menos de EE. UU., 14 pp más de Europa y 10,4 pp más de
emergentes.** La renta variable es exactamente la misma que la de la vigente: esta tabla no se mueve al
cambiar dos fondos de renta fija.

Dentro de emergentes: Taiwán 27 %, Corea 21 %, China 19 %, India 11 %, Brasil 4 %, Sudáfrica 3 %.

### 8.4 Geografía de la renta fija

| Zona | € | % de la RF | Emisor típico |
|---|---:|---:|---|
| Eurozona (DE, FR, IT, NL, IE, ES) | 16.100 | 33,3 % | Corporativo IG, covered bonds, RMBS irlandés |
| Estados Unidos | 8.700 | 17,9 % | Corporativo IG (Neuberger 14 %) y Treasury (Rock) |
| Reino Unido | 6.700 | 13,9 % | Corporativo IG y ABS (Aegon 31 %) |
| Nórdicos (NO, SE, DK) | 3.100 | 6,4 % | Crédito nórdico (Sissener 62 %) |
| Canadá y otros | 300 | 0,6 % | Corporativo |
| Sin desglosar | 13.600 | 28,0 % | Resto de Neuberger |

### 8.5 Divisas (sin cobertura)

| Divisa | % de la cartera |
|---|---:|
| EUR | ≈29 % |
| USD | ≈26 % |
| GBP | ≈10 % |
| JPY | ≈3 % |
| NOK y SEK | ≈4 % |
| CHF | ≈1 % |
| Emergentes (TWD, KRW, CNY, INR, BRL, ZAR, HKD) | ≈6 % |
| Mixto / sin desglosar (Cobas no publica el 44 % de su cartera) | ≈21 % |

La cartera **no cubre divisa**: el 26 % en dólares es una posición deliberada, no un descuido. Es la
palanca que hace que la parte europea y emergente pese cuando el dólar baja.

### 8.6 Sectores de la renta variable (aproximado, top 6 de cada ficha)

| Sector | % de la RV |
|---|---:|
| Tecnología | 21,1 % |
| Consumo cíclico | 12,7 % |
| Servicios financieros | 12,5 % |
| Industria | 12,4 % |
| Salud | 8,4 % |
| Comunicación | 5,1 % |
| Energía | 2,8 % |
| Materiales básicos | 2,0 % |
| Inmobiliario | 1,4 % |
| Consumo defensivo | 1,2 % |
| Sin desglosar (resto de cada ficha y Rock) | 20,5 % |

La tecnología pesa 21 % **por los emergentes** (42 % del iShares EM: Taiwán y Corea) y por el S&P 500
de Rock, no por una apuesta temática. Sin ellas, el bloque sería mucho más industrial y financiero.

### 8.7 Estilo y capitalización

| Eje | Reparto |
|---|---|
| Indexado / activo | **79,4 % / 20,6 %** de la RV |
| Value declarado | 20,6 % de la RV (Value + Cobas) |
| Small y mid cap | ≈28 % de la RV (Small 3.700, Value 5.000, parte de Cobas) |
| Large cap | ≈72 % de la RV |

### 8.8 Concentración por gestora

| Gestora | € | % cartera |
|---|---:|---:|
| Neuberger Berman | 31.900 | 32,9 % |
| Fidelity (directo + dentro de Rock) | 20.300 | 20,9 % |
| Vanguard (directo + dentro de Rock) | 10.900 | 11,2 % |
| BlackRock/iShares (directo + dentro de Rock) | 9.700 | 10,0 % |
| Cobas | 5.000 | 5,2 % |
| Andbank (MyInvestor Value) | 5.000 | 5,2 % |
| Aegon | 5.000 | 5,2 % |
| Sissener / FundRock | 5.000 | 5,2 % |
| Goldman Sachs (dentro de Rock) | 4.200 | 4,3 % |

**La mayor concentración de la cartera es el Neuberger con un 32,9 %.** Es el precio de tener un solo
fondo haciendo de amortiguador; repartirlo entre dos gestoras bajaría ese número pero duplicaría el
número de posiciones y no mejoraría ni el coste ni la TIR.

## 9. Lo que no se toca, y por qué (barrido del catálogo)

Ninguna de estas seis posiciones se puede mejorar con lo que hay en MyInvestor, y está comprobado ficha
a ficha sobre 2.410 fondos:

| Posición | Por qué se queda |
|---|---|
| **Neuberger 0,38 %** | No hay RF corta IG mejor. El candidato aparente, Vanguard IE00BDFB7308, es la clase **USD Hedged**: su +5,68 % a 3 años es en dólares; la clase euro da +3,78 % |
| **Fidelity MSCI Europe 0,10 %** | No existe nada por debajo de 0,10 % replicando MSCI Europe. iShares Europe (IE00BDRK7L36) empata al 0,10 % con +0,37 pp a 3A: traspaso sin ahorro |
| **iShares EM 0,16 %** | El propio catálogo lo marca como el más barato para MSCI EM; el resto cuesta +0,04 pp |
| **Vanguard Small-Cap 0,29 %** | Solo hay 7 indexados de small cap y los 4 baratos son el mismo fondo en distintas clases |
| **Cobas International 2,33 %** | Ningún value global bate su retorno/riesgo: Brandes cuesta 1,28 % y cede 4,5 pp anuales; Cobas Palm Harbour duplica la casa |
| **MyInvestor Value** | JPM Europe Strategic Value tiene mejores números (1,72 %, 3A +23,5 %, vol 10,1 %) pero es **otro factor**: 44 % bancos large cap frente a 44 small/mid a 0,8x valor en libros y beta 0,40 |

## 10. Lo que se descarta del barrido del catálogo

| Candidato | Motivo |
|---|---|
| Vanguard Global Short-Term Corp IE00BDFB7308 | Clase USD Hedged: +1,3 pp aparentes que son efecto divisa |
| Lazard Euro Short Duration FR0013506995 | TER 0,04 % engañoso: gestión 0,50 % + **20 % de éxito**, alto rendimiento, −15,7 % de liquidez (apalancado) y +0,87 % el último año |
| Pareto Nordic Cross Credit LU2023199552 | Volatilidad 3A de 0,80 % en crédito: señal de precio suavizado, no de menos riesgo. Es exactamente el métrico con el que aquí se examina el ABS — por eso las vol de las patas se publican también a 5A (§1 y §3) |
| JPMorgan Europe Strategic Value LU0210531983 | Buen fondo, factor equivocado: 44 % bancos, y la cartera ya lleva 23 % de financieras en Fidelity Europe |
| Brandes Global Value IE0031573896 | Mínimo 10.000 € y −4,5 pp anuales frente a Cobas |
| iShares MSCI World 0,06 % (IE000ZYRH0Q7) | No es comparable: dejaría la cartera sin emergentes ni small cap |
| L&G MSCI ACWI IMI 0,16 % (IE0003PI5332) | Nacido en 2025, 14 % en liquidez: sin historial y con lastre de caja |

## 11. Cuándo se revisa

- **A los 3 meses de entrar**: comparar Aegon contra DNCA y Sissener contra Carmignac en retorno,
  volatilidad y, si se puede, en TIR publicada. Si Aegon rinde por debajo del 3 % anualizado, se vuelve.
- **Si Sissener cae más del 3 % en un mes sin que caiga el crédito europeo**: salir.
- **En la revisión trimestral**: el §10 de `propuesta-actual` sigue mandando sobre el porcentaje de RV;
  esta propuesta no lo cambia.
- **Si MyInvestor publica TIR o duración** de los dos fondos nuevos, recalcular §3 con el dato real en
  vez de la inferencia.

## 12. Fuentes y límites

Fichas MyInvestor MCP a 30/10-02/11/2026 de los nueve fondos, verificadas una a una por ISIN (TER, 3A
anualizado, 5A, volatilidad 3A, asignación, países, sectores, mínimo, corte y clase). **Re-verificación
adversarial del 03/11/2026 con `get_funds` (MCP MyInvestor, NAV 30/10/2026)** de Aegon, Sissener, DNCA,
Carmignac y Neuberger: cuadran TER, gestión/éxito, rentabilidades 3A/5A y por año natural, vol 3A y 5A,
SRRI, sectores, países, mínimos, cortes, incept y clase de acumulación. Comisiones de
éxito de la ficha de la gestora: DNCA (20 % sobre €STR+1,40 % con high-water mark, 0,32 % cobrado) y
Carmignac (20 % sobre 75 % ICE BofA Euro Corporate + 25 % Euro High Yield, clawback 5 años). Barrido del
catálogo: 2.410 fondos, 266 indexados. Rentabilidades = pasado anualizado, no previsión. Duración y TIR
de Aegon y Sissener **no publicadas**: los ≈3,3 años de duración son inferencia (rango 3,2-3,5). El
retorno 3A y el comportamiento 2022 del **bloque** de RF son estimación: la vol y el retorno de la RF
de Rock no se publican; las cifras verificadoras del cambio son las de **fondo** (vol, 3A/5A/2022),
que sí son de ficha. El §8.2 normaliza los sectores del Neuberger (suman 103,6 % en el catálogo).
Drawdown y retorno esperado son estimaciones propias con el mismo escenario de la propuesta vigente.

> No es asesoramiento financiero. La decisión es del titular.

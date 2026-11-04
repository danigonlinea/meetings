---
title: "Propuesta definitiva del comité: 45/45/10 con Rock intacta (100.000 €)"
date: 2026-11-04
type: portfolio-proposal
category: finance
tags: [cartera, comite, definitiva, 45-45-10, rock, indexados, renta-fija, myinvestor, auditoria]
status: draft
related:
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
  - finance/portfolio/cartera-myinvestor/propuesta-actual.md
  - finance/portfolio/cartera-myinvestor/propuesta-perplexity.md
  - finance/portfolio/cartera-myinvestor/propuesta-actual-avanzada.md
  - finance/portfolio/cartera-myinvestor/propuesta-alternativa.md
  - finance/portfolio/cartera-myinvestor/propuesta-investigacion.md
---

# Propuesta definitiva — 04/11/2026

> **Qué es este fichero.** El veredicto de una auditoría independiente de las cinco propuestas vivas de
> la carpeta (Renta 4, avanzada, alternativa, investigación y perplexity). **No sustituye a
> `propuesta-actual.md`**, que sigue siendo la adoptada: si el titular la aprueba, sus conclusiones se
> absorben allí y este anexo **se borra** (`git rm`).
>
> **Base de cálculo.** 100.000 € = **30.000 € de Rock, intacta** (decisión del titular del 04/11) +
> **70.000 € manuales** = 60.000 € ya invertidos + 10.000 € de aportación nueva. Los 10.000 € del
> colchón (Groupama Trésorerie) quedan **fuera** y no se tocan. **Ojo con la diferencia de base:** el
> encargo fija 100.000 €, o sea **3.000 € más** que los 7.000 € de aportación que asume
> `propuesta-actual.md` (97.000 €). Si solo entran 7.000 €, la cartera se reescala sobre 97.000 €.
>
> **Verificación.** Las 22 fichas de las cinco propuestas consultadas por ISIN con `get_funds`
> (MyInvestor MCP, 04/11/2026, NAV 30/10). Ningún ISIN falta del catálogo. Los números derivados
> (TER, look-through, duración, gestoras, caída) están recalculados en código, no a mano.
>
> **No es asesoramiento financiero.** Es una propuesta analítica; la idoneidad depende de la
> fiscalidad, la liquidez y el aguante real del titular.

## 1. El veredicto en una línea

De las cinco propuestas, **solo `propuesta-perplexity.md` cumplía a la vez el capital de 100.000 €, el
tope del 15 % por fondo, el 35 % por gestora y la caída del 15-20 %**. La cartera definitiva es ese
esqueleto con seis correcciones, y su bloque manual se reconstruye alrededor de Rock en lugar de
ignorarla.

| Propuesta | Por qué no se ejecuta tal cual |
| --- | --- |
| Renta 4 (Kaizen) | 34.769 € no son 100.000 € ni es la plataforma del encargo; 35,3 % en un solo fondo |
| Avanzada 55/45 | −23,4 % en un 2008, por encima de la tolerancia declarada; Neuberger 19,1 %; 19 posiciones |
| Alternativa 50/50 | 32,9 % en un solo fondo de crédito; Comgest 5A −1,0 % pagando 1,59 % |
| Investigación | Base obsoleta (DNCA/Carmignac, ya sustituidos el 31/10); incompatible con el anexo de la alternativa |
| Perplexity | Única ejecutable: se adopta como base |

## 2. La cartera

| # | Bloque | Fondo | ISIN | Gestora | € | % | TER |
|--:|---|---|---|---|---:|---:|---:|
| 1 | RV global | Vanguard Global Stock Index EUR Acc | IE00B03HD191 | Vanguard | 5.000 | 5,0 % | 0,18 % |
| 2 | RV Europa | iShares Europe Index D Acc | IE00BDRK7L36 | BlackRock | 4.000 | 4,0 % | 0,10 % |
| 3 | RV emergentes | iShares Emerging Markets S Acc | IE000QAZP7L2 | BlackRock | 3.000 | 3,0 % | 0,16 % |
| 4 | RV small caps | Vanguard Global Small-Cap Index EUR Acc | IE00B42W4L06 | Vanguard | 5.000 | 5,0 % | 0,29 % |
| 5 | Activos reales | iShares Developed Real Estate D Acc | IE00BDRK7P73 | BlackRock | 4.600 | 4,6 % | 0,17 % |
| 6 | RF corta IG | Neuberger Short Duration Euro Bond U | IE00BL1GVT98 | Neuberger | 13.000 | 13,0 % | 0,38 % |
| 7 | RF ABS | Aegon European ABS A EUR Acc | IE00BG226Z29 | Aegon | 11.400 | 11,4 % | 0,66 % |
| 8 | RF corp. IG | iShares Euro IG Corporate Bond D Acc | IE00BDRK7J14 | BlackRock | 5.000 | 5,0 % | 0,12 % |
| 9 | RF pública euro | iShares Euro Government Bond D Acc | IE00BD0NC037 | BlackRock | 9.000 | 9,0 % | 0,10 % |
| 10 | Liquidez | AXA Trésor Court Terme C | FR0000447823 | AXA IM | 10.000 | 10,0 % | 0,05 % |
| 11 | *Rock (sin tocar)* | 9 indexados, 78 % RV / 22 % RF | — | MyInvestor | *30.000* | *30,0 %* | *0,41 %* |
| | | **TOTAL** | | | **100.000** | **100 %** | |

**Límites, verificados en código:** 11 posiciones (≤ 15) · fondo mayor 13,0 % (≤ 15 %) · gestoras:
BlackRock 25,6 %, Neuberger 13,0 %, Aegon 11,4 %, Vanguard 10,0 %, AXA 10,0 % (≤ 35 %) · todas las
clases son de acumulación (`distributing = 0` en ficha) · ninguna comisión de éxito.

**Coste:** 184,76 €/año en el bloque manual (0,264 %) + 123,00 € de Rock = **307,76 €/año (0,308 %)**.

## 3. Métricas

| Métrica | Valor |
| --- | ---: |
| Renta variable (look-through, Rock al 78 %) | **45.000 € = 45,0 %** |
| Renta fija (look-through) | **45.000 € = 45,0 %** |
| Liquidez | **10.000 € = 10,0 %** |
| Duración de la RF | **4,76 años** (+100 pb = −2.140 €, 2,1 % de la cartera) |
| TIR estimada de la RF | ≈4,1 % (1.845 €/año) |
| *Carry cobrado a 12 meses* | **−0,4 %** (los tipos subieron 68 pb: se publica la brecha) |
| Retorno esperado (EY 6,6 % + carry) | ≈5,0 % nominal · ≈+1,2 % real sobre inflación 3,8 % |
| Caída tipo 2008 (RV −40 %, RF −3 %) | **−19.400 € (−19,4 %)** |

## 4. Exposición agregada

**Geografía de la RV:** EE. UU. **51 %** · Europa **19 %** · emergentes **15 %** · Japón **11 %** ·
resto 4 %. Frente a un ACWI (63 % EE. UU.), la cartera lleva ≈12 pp menos de EE. UU.: es una
infraponderación **declarada**, no un accidente.

**Sectores de la RV** (estimación; los sectores de Rock no se publican por fondo): tecnología ≈24 % ·
inmobiliario ≈11,7 % · servicios financieros ≈15 % · industria ≈11 % · salud ≈8 %. **El inmobiliario
es la única apuesta sectorial consciente**: 4.600 € de REITs más el 8 % que llevan dentro las small caps.

**Divisa:** ≈63 % en euros (toda la RF y el monetario lo son, con independencia del país del emisor) y
**≈37 % sin cubrir**, todo vía renta variable.

## 5. Escenarios

| Escenario | Impacto |
| --- | ---: |
| Caída tipo 2008 (RV −40 %, RF −3 %) | −19.400 € (−19,4 %) |
| Caída extrema (RV −50 %) | −23.850 € (−23,9 %) |
| Subida de tipos +150 pb + RV −10 % | −7.710 € (−7,7 %) |
| Recesión global suave (RV −25 %, pública +6 %, crédito −5 %) | −12.180 € (−12,2 %) |
| Inflación persistente dos años (nominal) | +3,6 % (**−0,2 % real**) |

## 6. Hoja de órdenes: 12 traspasos + 1 suscripción

Todo entre fondos armonizados: **0 € de impuestos y 0 % de comisión**. El colchón de Groupama no se toca.

| # | Origen | ISIN origen | € | Destino | ISIN destino |
|--:|---|---|---:|---|---|
| 1 | DNCA Invest Alpha Bonds A | LU1694789451 | 5.000 | Vanguard Global Stock Index | IE00B03HD191 |
| 2 | DNCA Invest Alpha Bonds A | LU1694789451 | 3.000 | iShares Emerging Markets S | IE000QAZP7L2 |
| 3 | DNCA Invest Alpha Bonds A | LU1694789451 | 5.000 | Vanguard Global Small-Cap | IE00B42W4L06 |
| 4 | Carmignac Portfolio Credit A | LU1623762843 | 3.600 | iShares Dev Real Estate D | IE00BDRK7P73 |
| 5 | Carmignac Portfolio Credit A | LU1623762843 | 8.400 | Aegon European ABS A | IE00BG226Z29 |
| 6 | Gamma Global A | ES0140794001 | 3.000 | Aegon European ABS A | IE00BG226Z29 |
| 7 | Gamma Global A | ES0140794001 | 5.000 | iShares Euro IG Corporate D | IE00BDRK7J14 |
| 8 | Neuberger Short Duration (parcial) | IE00BL1GVT98 | 9.000 | iShares Euro Government Bond D | IE00BD0NC037 |
| 9 | UBS MSCI China All Shares | LU1815002040 | 1.000 | iShares Europe Index D | IE00BDRK7L36 |
| 10 | MyInvestor Value C | ES0165243025 | 2.000 | iShares Europe Index D | IE00BDRK7L36 |
| 11 | Cobas International P | LU1598719752 | 1.000 | iShares Europe Index D | IE00BDRK7L36 |
| 12 | NB Next Gen Space Economy | IE00018YKVN0 | 1.000 | iShares Dev Real Estate D | IE00BDRK7P73 |
| 13 | *Aportación nueva* | — | 10.000 | AXA Trésor Court Terme C | FR0000447823 |

**Cuadre:** salen 47.000 € de la cartera actual + 10.000 € nuevos = 57.000 € invertidos.
Σ destinos: World 5.000 · Europa 4.000 · EM 3.000 · Small 5.000 · REITs 4.600 · Aegon 11.400 ·
IG 5.000 · Pública 9.000 · AXA 10.000.

### 6.1 Saldos finales (bloque manual, 70.000 €)

| Fondo | Antes | Después |
| --- | ---: | ---: |
| Neuberger Short Duration | 22.000 | 13.000 |
| Vanguard Global Stock | 0 | 5.000 |
| iShares Europe Index | 0 | 4.000 |
| iShares Emerging Markets | 0 | 3.000 |
| Vanguard Global Small-Cap | 0 | 5.000 |
| iShares Dev Real Estate | 0 | 4.600 |
| Aegon European ABS | 0 | 11.400 |
| iShares Euro IG Corporate | 0 | 5.000 |
| iShares Euro Government | 0 | 9.000 |
| AXA Trésor Court Terme | 0 | 10.000 |
| DNCA · Carmignac · Gamma · MyInvestor Value · Cobas · Space · China | 38.000 | 0 |

### 6.2 Tandas

| Tanda | Cuándo | Órdenes | Qué se corta |
| --- | --- | ---: | --- |
| 1 | Día 1 | 1-7 | El crédito peor pagado: DNCA y Carmignac (1,31 y 1,20 % + 20 % de éxito, duración 4) y Gamma (81 % high yield de energía y shipping) |
| 2 | Día 1-2 | 8-12 | Neuberger parcial y las cuatro posiciones pequeñas |
| 3 | En paralelo | 13 | Suscripción con los 10.000 € nuevos |

Un traspaso tarda 2-4 días y no hace falta efectivo en ningún momento. Cortes 09:00-12:00 según fondo.

### 6.3 Antes de teclear

| Comprobación | Estado |
| --- | --- |
| ISIN, clase y acumulación de los 10 fondos | ✅ verificado por `get_funds` el 04/11 |
| Comisión de éxito | ✅ ninguno la cobra |
| Reembolso de DNCA, Carmignac, Gamma, UBS China y Space | ✅ 0,00 % verificado el 31/10 |
| Reembolso de MyInvestor Value C | ❓ verificar en pantalla antes de la orden 10 |
| Comisión de entrada de Aegon, iShares Europe y REITs | ❓ el MCP no la publica; MyInvestor aplica 0 % en fondos |
| Cobas International en soft close | ⚠️ el reembolso por traspaso sí está permitido (ficha) |
| Aportación nueva de 10.000 € | ⚠️ si solo entran los 7.000 € de la vigente, la cartera se reescala sobre 97.000 € |

## 7. Plan de entrada y rebalanceo

- **Entrada:** de golpe el 90 % (RV + RF) y el 10 % restante como liquidez permanente en AXA. El
  escalonado de tres meses no protege de nada que dure tres meses y cuesta ≈0,3 pp de retorno esperado.
- **Si hace falta escalonar por conducta:** 60 % el día 1 + tres tandas de 13.333 € el 1/12/2026,
  2/01/2027 y 1/02/2027, cerrando el 28/02/2027.
- **Rebalanceo:** revisión trimestral; bandas ±5 pp por bloque y ±25 % relativo por fondo; se ejecuta con
  traspasos y con la liquidez, nunca con reembolso.
- **Qué se vigila:** RV real vs 45 % · TER real vs 0,308 % · carry cobrado vs TIR 4,1 % · duración vs
  4,76 · inmobiliario vs 12 % de la RV · drawdown vs −19,4 % · composición de Rock.

## 8. Qué se conserva de cada propuesta

| Origen | Conservado |
| --- | --- |
| Perplexity | El esqueleto 45/45/10, el cribado de RF, la sustitución de Sissener por corporativo IG y los topes de gestora |
| Avanzada | La regla «cada euro es RV o RF», las CMAs de Vanguard/JPM/GMO y el método de look-through |
| Alternativa | Los REITs indexados al 0,17 % (el único hueco real a precio de índice) |
| Investigación | La regla de acumulación verificada ficha a ficha |
| Renta 4 | El criterio de no confundir TER con coste cuando cambia la duración |

## 9. Qué se descarta y qué riesgo resolvía

| Descartado | Qué resolvía eliminarlo |
| --- | --- |
| Kaizen (2025, 9 % de éxito) | 35 % en un fondo sin historial a tres años |
| Fundsmith 1,09 % y Comgest 1,59 % | 5A +2,7 % y −1,0 %: pagar selección que no ha seleccionado |
| Cobas International 2,33 % y Cobas Renta | 116 €/año por 5.000 € y un «mixto» con 28 % de liquidez y 3,9 % Ghana |
| Sissener 0,90 % | High yield de energía y shipping bajo etiqueta de crédito IG |
| DNCA 1,31 % y Carmignac 1,20 % (+20 % de éxito) | Duración 4 y comisión de éxito en un bloque que debe ser corto |
| Bonos ligados a inflación | −8,7 % en 2022: fallaron justo en el escenario que decían cubrir |
| World al 0,06 % (iShares) | Dejaría BlackRock en el 35,6 %, por encima del tope |

## 10. Límites y datos no verificados

- **Geografía y sectores de la RV son estimación**, no dato de ficha: las fichas publican los seis
  primeros países y sectores de cada fondo, y Rock no los publica por fondo. El «≈» es deliberado.
- **Duraciones estimadas**: Aegon ≈2,5, corporativo IG ≈4,5, pública ≈6,5, Treasury USA de Rock ≈7 y
  20+ euro ≈18. Solo el Neuberger publica la suya (1,95).
- **TIR estimada** para Aegon, IG y pública (≈4,3 / 4,1 / 3,3 %); la del Neuberger (4,65 %) es de ficha
  de gestora.
- **Holdings no re-verificados en esta sesión** (el MCP no los publica y fundfacts devuelve 404 para
  estos ISIN). Los hallazgos que se usan —el *steepener* Schatz/Bund del Neuberger, la granularidad del
  ABS de Aegon, el high yield de Sissener— vienen de la verificación del 04/11 documentada en
  `propuesta-perplexity.md`, anexo B.
- **La cartera hereda el riesgo de Rock**: si MyInvestor cambia sus pesos, el look-through cambia sin que
  nadie edite este documento. Y su 20+ euro (3.000 €, duración ≈18) aporta el 25 % de todo el riesgo de
  tipos con el 3 % del capital.
- **No cubre divisa**: ≈37 % del patrimonio en moneda distinta del euro. Es una decisión, no un olvido.

## Fuentes

- **Fichas MyInvestor MCP** (`get_funds`, 04/11/2026, NAV 30/10/2026): TER, comisiones, rentabilidades
  3A/5A anualizadas, volatilidad, SRRI, `alloc_equity`, países, sectores, mínimo y `distributing` de los
  22 ISIN de las cinco propuestas.
- **`cartera-actual.md`** (30/10/2026): saldos reales, composición de Rock y TIR/duración de las
  gestoras a 30/09/2026.
- **`propuesta-perplexity.md`** (04/11/2026): cribado de candidatos y verificación de holdings del anexo B.
- **`propuesta-actual-avanzada.md`** (04/11/2026): CMAs de Vanguard VCMM, J.P. Morgan LTCMA y GMO.
- **Eurostat** (16/10/2026): inflación de la zona euro 3,8 %. **BCE** (30/10/2026): facilidad de depósito
  2,50 %.

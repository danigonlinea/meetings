---
title: "Opción A — Cartera AI 80/20 en 7 fondos (100.000 € libres + 10.000 € intocables en Groupama, 15 años): 70 % indexado regional desconcentrado, 10 % SMID activa y 20 % escudo corto (0,273 % TER)"
date: 2026-11-26
type: portfolio-proposal
category: finance
tags: [cartera, propuesta, opcion-a, myinvestor, 100k, 110k, 40-anos, 15-anos, 80-20, 7-fondos, indexado-regional, small-caps, escudo-corto, cero-exito, traspasos, cartera-ai-80-20-7-fondos]
status: propuesta
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
  - finance/portfolio/cartera-definitiva-40/100k.md
  - finance/portfolio/cartera-ai-definitiva-final/100k.md
  - finance/portfolio/cartera-ai-definitiva-final/opcion-b.md
  - finance/portfolio/cartera-ai-definitiva-final/opcion-c.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/ranking-deepseek.md
  - finance/portfolio/cartera-ai-definitivas-estudiar/ranking-argon.md
---

# Opción A — Cartera AI 80/20 en 7 fondos — 100.000 € libres (+ 10.000 € en Groupama) a 15 años (2026 → 2041)

> **Estado:** **Opción A** (marcada el 26/11/2026, pendiente de ejecución por el titular).

- **Fecha del diseño:** 26/11/2026
- **Perfil:** Inversor de **40 años** con horizonte de **15 años vista (2026 → 2041, hasta los 55 años)** que prioriza renta variable (`~80 %` real), bajo coste compuesto (`<0,30 %` TER), desconcentración de EE. UU. y de las 10 megacaps tecnológicas sin depender de múltiples gestores activos, y sencillez operativa en **7 fondos**.
- **Estructura patrimonial (`110.000 €` totales en MyInvestor):**
  - **Capital invertible (`100.000,00 €`):** `60.000 €` en los 8 fondos manuales de [`cartera-actual.md`](../cartera-myinvestor/cartera-actual.md) + `30.000 €` de `Cartera Rock` desmontados vía traspaso a fondo puente (`0 €` de IRPF) + `10.000 €` de liquidez nueva.
  - **Colchón de emergencia aparte e intocable:** `10.000,00 €` en `Groupama Trésorerie IC` (`FR0000989626`), fuera de la cartera invertible (`0` órdenes).
- **Restricciones cumplidas al 100 %:**
  1. **Solo 7 fondos traspasables de acumulación en EUR** (`politica: acumulacion` / `distributing = 0`), todos verificados en [`finance/fondos-myinvestor/`](../../fondos-myinvestor/README.md).
  2. **`0 %` ETFs**, **`0 %` acciones individuales**, **`0 %` *soft close*** y **`0 / 7` comisiones de éxito**.
  3. **Tamaño mínimo efectivo por línea:** ningún fondo pesa menos del **`8,00 %` (`8.000 €`)**, eliminando *tickets homeopáticos* y simplificando aportaciones mensuales y rebalanceos.
- **Aviso:** Este documento es un análisis técnico de construcción de carteras sobre fichas del repositorio, **no asesoramiento financiero**. La decisión y la ejecución son del titular.

---

## 1. Arquitectura y evolución tras auditoría crítica

Esta propuesta nace del principio de **evitar los dos extremos caros**:
1. **Un indexado 100 % ponderado por capitalización** (`MSCI World` puro) concentra el `72,0 %` en EE. UU. y el `26,6 %` en sus 10 mayores valores tecnológicos en máximos históricos de concentración.
2. **Una cartera de 12–14 fondos con 40–60 % de gestión activa de RV** eleva el coste fijo a `0,72 %–0,85 %` (`20.000 €–24.000 €` acumulados en 15 años, según [`ranking-deepseek.md`](../cartera-ai-definitivas-estudiar/ranking-deepseek.md#L60-L74)) y exige un alfa sostenido que más del 94 % de los gestores activos no logra a 10–15 años (SPIVA Europe, [`ranking-argon.md`](../cartera-ai-definitivas-estudiar/ranking-argon.md#L34)).

La solución intermedia adopta **70 % indexado regional + 10 % activa SMID + 20 % escudo corto activo**, e incorpora tres podas aplicadas tras auditar una versión preliminar de 9 fondos:
- **Fuera materias primas del escudo (`GSQuartix`, `5 %`):** su volatilidad a 3A (`12,00 %`, 1A `16,27 %`, caída `−10,96 %` en 2023) la convierte en cobertura táctica de estanflación, no en preservación de capital fiable ante recesiones deflacionarias.
- **Fuera duplicidad en RV activa (`Palm Harbour Global Value`, `8 %`):** por tamaño reducido (`59,3 M€`), debilidad reciente (`YTD +6,93 %`) y coste añadido, se concentra toda la convicción activa de RV en un único motor contrastado (`GS Global Small CORE`, `3.257 M€`, alfa positivo 1A/3A/5A).
- **Fuera el tramo residual del 5 % en RF indexada 1–5 años (`IE0004ZP1ND3`):** con `5.000 €`, su duración (`2,69` años) apenas mueve el conjunto y añade una octava línea innecesaria; su peso se reparte a partes iguales entre las dos patas del escudo (`10 %` `DWS Floating Rate Notes` + `10 %` `Cobas Renta FI`).

---

## 2. Composición de la cartera (7 fondos · `0,273 %` TER · `0 / 7` éxito)

| # | Bloque | Fondo (ficha verificada) | ISIN | € | % s/ 100k | TER | €/año | RV int. | 2022 | 3A an. | 5A an. | YTD 2026 | Finect |
| --: | --- | --- | --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --- |
| 1 | **Indexado RV** | [iShares Developed World Index (IE) S Acc EUR](../../fondos-myinvestor/rv-global/IE000ZYRH0Q7.md) | `IE000ZYRH0Q7` | 35.000 € | 35,0 % | **0,06 %** | 21,00 € | 100,0 % | *−12,85 %¹* | *+17,44 %¹* | *+10,02 %¹* | +14,33 % | [Finect](https://www.finect.com/fondos-inversion/IE000ZYRH0Q7-Ishares_dev_wld_idx_ie_s_acc_eur) |
| 2 | **Indexado RV** | [Fidelity MSCI Europe Index Fund EUR P Acc](../../fondos-myinvestor/rv-europa/IE00BYX5MD61.md) | `IE00BYX5MD61` | 15.000 € | 15,0 % | 0,10 % | 15,00 € | 99,3 % | −9,29 % | +16,68 % | +9,52 % | +14,90 % | [Finect](https://www.finect.com/fondos-inversion/IE00BYX5MD61-Fidelity_msci_europe_indx_eur_p_acc) |
| 3 | **Indexado RV** | [Fidelity MSCI Emerging Markets Index Fund P-ACC-EUR](../../fondos-myinvestor/rv-emergentes/IE00BYX5M476.md) | `IE00BYX5M476` | 12.000 € | 12,0 % | 0,20 % | 24,00 € | 99,03 % | −15,25 % | +16,95 % | +6,12 % | +14,95 % | [Finect](https://www.finect.com/fondos-inversion/IE00BYX5M476-Fidelity_msci_emerg_mkts_indx_eur_p_acc) |
| 4 | **Indexado RV** | [Fidelity MSCI Japan Index Fund P-ACC-EUR (hedged)](../../fondos-myinvestor/rv-japon/IE00BYX5NH74.md) | `IE00BYX5NH74` | 8.000 € | 8,0 % | 0,20 %² | 16,00 € | ~100,0 % | −6,37 % | **+20,14 %** | **+16,30 %** | +13,89 % | [Finect](https://www.finect.com/fondos-inversion/IE00BYX5NH74-Fidelity_msci_japan_index_eur_p_acc_h) |
| — | *Subtotal 1* | *Pieza indexada regional sin solape de EE. UU. (4 fondos)* | — | *70.000 €* | *70,0 %* | *0,109 %* | *76,00 €* | *69,78 %* | *−11,83 %* | *+17,50 %* | *+9,96 %* | *+14,51 %* | — |
| 5 | **Activa RV** | [Goldman Sachs Global Small CORE Equity Acc EUR](../../fondos-myinvestor/rv-global/LU1599216113.md) | `LU1599216113` | 10.000 € | 10,0 % | 1,39 % | 139,00 € | 98,01 % | −10,26 % | +18,30 % | +9,11 % | +16,71 % | [Finect](https://www.finect.com/fondos-inversion/LU1599216113-Gs_glb_sm_cp_core_eq_othccy_acc_eursnap) |
| — | *Subtotal 2* | *Motor activo SMID multifactor (1 fondo, 0 % éxito)* | — | *10.000 €* | *10,0 %* | *1,390 %* | *139,00 €* | *9,80 %* | *−10,26 %* | *+18,30 %* | *+9,11 %* | *+16,71 %* | — |
| 6 | **Escudo** | [DWS Floating Rate Notes LC](../../fondos-myinvestor/renta-fija/LU0034353002.md) *(también puente de Rock)* | `LU0034353002` | 10.000 € | 10,0 % | 0,25 % | 25,00 € | 0,0 % | −0,90 % | +3,32 % | +2,54 % | +2,14 % | [Finect](https://www.finect.com/fondos-inversion/LU0034353002-Dws_floating_rate_notes_lc) |
| 7 | **Escudo** | [Cobas Renta FI](../../fondos-myinvestor/mixtos/ES0119207001.md) | `ES0119207001` | 10.000 € | 10,0 % | 0,33 % | 33,00 € | 14,5 % | **+3,89 %** | **+8,94 %** | +6,82 % | +11,08 % | [Finect](https://www.finect.com/fondos-inversion/ES0119207001-Cobas_renta_fi) |
| — | *Subtotal 3* | *Escudo corto anti-estanflación y pólvora seca (2 fondos)* | — | *20.000 €* | *20,0 %* | *0,290 %* | *58,00 €* | *1,45 %* | ***+1,50 %*** | *+6,13 %* | *+4,68 %* | *+6,61 %* | — |
| **TOT.** | **Invertible** | **7 fondos · 5 gestoras · 0 % éxito** | — | **100.000 €** | **100,0 %** | **0,273 %** | **273,00 €** | **81,03 %** | **−8,96 %** | **+15,31 %** | **+8,82 %** | **+13,15 %** | — |
| *Fuera* | *Colchón* | *Groupama Trésorerie IC (intacto, 0 órdenes)* | `FR0000989626` | *10.000 €* | — | *0,07 %* | *7,00 €* | *0,0 %* | *~0,00 %* | *+2,98 %* | *—* | *—* | [Finect](https://www.finect.com/fondos-inversion/FR0000989626) |
| **CONS.** | **Total** | **100.000 € libres + 10.000 € colchón aparte** | — | **110.000 €** | — | **0,255 %** | **280,00 €** | **73,66 %** | **−8,15 %** | **+14,19 %** | — | — | — |

*¹ La clase S de `iShares Developed World` nació el 21/08/2025 y no publica 2022, 3A ni 5A propios; las cifras en cursiva usan como proxy del mismo índice MSCI World EUR el historial de `Vanguard Global Stock EUR Acc` (`IE00B03HD191`). ² `Fidelity MSCI Japan Hedged` publica `0,20 %` de TER en MyInvestor/Finect y `0,15 %` de ongoing charges en su factsheet oficial (con `0,15 %`, el TER total de la cartera baja a **`0,269 %` = `269,00 €/año`**).*

---

## 3. Radiografía *look-through* (desconcentración y sesgos declarados)

### 3.1. Clases de activo reales

| Clase de activo subyacente | Importe (€) | % s/ 100k | % s/ 110k (c/ Groupama) |
| --- | --: | --: | --: |
| **Renta variable efectiva (*look-through*)** | **81.030 €** | **81,03 %** | **73,66 %** |
| **Renta fija corta / flotante y liquidez en cartera** | **18.970 €** | **18,97 %** | **17,25 %** |
| **Colchón monetario intocable (`Groupama`)** | *10.000 €* | — | **9,09 %** |
| **Total bajo riesgo + liquidez (con Groupama)** | *28.970 €* | *18,97 %* | **26,34 %** |

### 3.2. Geografía y concentración sobre los `81.030 €` de renta variable

| Métrica | MSCI World puro | `cartera-definitiva-40` | **`cartera-ai-80-20-7-fondos` (s/ RV)** | **`cartera-ai-80-20-7-fondos` (s/ 100k)** |
| --- | --: | --: | --: | --: |
| **Estados Unidos** | 72,0 % | 54,3 % | **38,71 %** (`31.364 €`) | **31,36 %** |
| **Europa (Eurozona + UK + Suiza)** | 15,5 % | 20,2 % | **27,74 %** (`22.480 €`) | **22,48 %** |
| **Mercados Emergentes** | 0,0 % | 11,4 % | **14,78 %** (`11.974 €`) | **11,97 %** |
| **Japón** *(71 % cubierto a EUR)* | 5,8 % | 5,0 % | **13,81 %** (`11.192 €`) | **11,19 %** |
| **Canadá, Australasia y otros desarrollados** | 6,7 % | 9,1 % | **4,96 %** (`4.020 €`) | **4,02 %** |
| **Top 10 megacaps EE. UU.** | 26,6 % | ~15,3 % *(s/100k)* | **11,49 %** (`9.310 €`) | **9,31 %** |
| **Sector Tecnología** | 30,8 % | 29,5 % | **23,83 %** (`19.305 €`) | **19,31 %** |

**Sesgos conscientes declarados:**
- Bajar EE. UU. del `72,0 %` al `38,71 %` de la RV implica sobreponderar deliberadamente **Europa (`27,74 %`)** y **Japón (`13,81 %`)** frente a su capitalización mundial.
- La exposición a Japón (`IE00BYX5NH74`) lleva el **yen cubierto a euros**: elimina la erosión por debilidad del yen, pero renuncia a ganancias cambiarias si el yen se aprecia con fuerza.
- El `10 %` en `GS Global Small CORE` (`LU1599216113`) aporta exposición a EE. UU. (`62,6 %` del fondo), pero exclusivamente en **pequeñas y medianas empresas** (`94,35 %` SMID, mayor posición `1,71 %`, cero solape con las 7 Magníficas).

---

## 4. Estrés, costes y proyecciones a 15 años (2026 → 2041)

### 4.1. Pruebas de caída

- **Escenario estanflación / subida de tipos (prueba 2022):** **`−8,96 %` (`−8.960 €` s/100k · `−8,15 %` s/110k)**, con el Bloque 3 defensivo en **`+1,50 %`** (frente a `−12,85 %` del MSCI World y caídas de doble dígito de los bonos de duración larga).
- **Escenario recesión severa tipo 2008** *(RV `−40 %`, `DWS FRN` `−2 %`, `Cobas Renta` `−7 %` por su `14,5 %` RV y crédito privado)*: **`−32.732 €` (`−32,73 %` s/100k · `−29,76 %` s/110k)**.
- **Shock directo de las 10 megacaps EE. UU. (`−50 %`):** impacto directo de solo **`−4,66 %` (`−4.655 €`)** frente a `−13,3 %` en un MSCI World puro.

### 4.2. Proyecciones a 15 años y comparativa con el repositorio

| Escenario (horizonte 15 años, 100.000 € base) | Retorno neto anual | Capital sin aportaciones | Capital con `1.000 €/mes` *(280k aport.)* |
| --- | --: | --: | --: |
| **Test neutro `ranking-deepseek`** *(6,0 % RV / 3,0 % escudo, `0 %` alfa)* | **5,16 %** | **212.632 €** | **480.811 €** |
| **Escenario central** *(7,2 % RV global-SMID / 3,2 % escudo)* | **6,17 %** | **245.423 €** | **536.251 €** |

Comparación directa bajo la **misma hipótesis neutra de [`ranking-deepseek.md`](../cartera-ai-definitivas-estudiar/ranking-deepseek.md)** (`6 %` RV / `3 %` resto, `0 %` alfa):

| Cartera | Fondos | % Indexado | RV real | TER | Comisiones 15A | 100k → 15 años |
| --- | :-: | --: | --: | --: | --: | --: |
| [`cartera-definitiva-40`](../cartera-definitiva-40/100k.md) | 6 | 100,0 % | 83,39 % | 0,092 % | ~2.900 € | ~221.800 € |
| **`cartera-ai-80-20-7-fondos` (esta propuesta)** | **7** | **70,0 %** | **81,03 %** | **0,273 %** | **8.432 €** | **212.632 €** |
| [`cartera-ai-definitiva-final` (`100k.md`)](./100k.md) | 13 | 43,0 % | 84,24 % | 0,784 % | ~22.500 € | 200.393 € |
| [`cartera-ai-final-atrevida`](../cartera-ai-definitivas-estudiar/cartera-ai-final-atrevida/110k.md) | 12 | 37,3 % | 82,15 % | 0,798 % | 23.918 € | 198.205 € |
| [`cartera-ai-carbon`](../cartera-ai-definitivas-estudiar/cartera-ai-carbon/100k.md) | 12 | 40,0 % | 80,15 % | 0,746 % | 22.263 € | 197.973 € |

- **Sobrecoste frente a una cartera 100 % indexada al `0,10 %`:** solo **`173,00 €/año`**, lo que fija un ***break-even alpha* de apenas `+0,58 pp/año`** sobre los `30.000 €` de gestión activa (`GS Global Small CORE` + `DWS FRN` + `Cobas Renta`).

---

## 5. Plan de ejecución desde `cartera-actual.md` (12 traspasos + 1 suscripción · `0 €` IRPF)

`Cartera Rock` (`30.000 €`) se desmonta mediante **«Traspasar a un fondo»** entrando íntegra a `DWS Floating Rate Notes LC` (`LU0034353002`) como fondo puente (`0 €` de IRPF y sin tocar `Groupama`). Todas las órdenes respetan los mínimos iniciales de ficha en su primera entrada (`GS Small CORE` entra con `10.000 €` frente al mínimo de `5.000 €`).

| Fase | Origen | ISIN origen | Destino | ISIN destino | Importe | Tipo |
| :-: | --- | --- | --- | --- | --: | --- |
| **F1** | Cartera Rock (entera) | *9 fondos Rock* | `DWS Floating Rate Notes LC` *(puente)* | `LU0034353002` | 30.000 € | Traspaso |
| **F1** | `Neuberger Short Duration U` | `IE00BL1GVT98` | `iShares Developed World S` | `IE000ZYRH0Q7` | 22.000 € | Traspaso |
| **F1** | `DNCA Invest Alpha Bonds A` | `LU1694789451` | `Fidelity MSCI Europe P` | `IE00BYX5MD61` | 13.000 € | Traspaso |
| **F1** | `Carmignac Portfolio Credit A` | `LU1623762843` | `Fidelity MSCI EM P` | `IE00BYX5M476` | 12.000 € | Traspaso |
| **F1** | `Gamma Global A` | `ES0140794001` | `Fidelity MSCI Japan Hedged P` | `IE00BYX5NH74` | 8.000 € | Traspaso |
| **F1** | `MyInvestor Value C` | `ES0165243025` | `Fidelity MSCI Europe P` | `IE00BYX5MD61` | 2.000 € | Traspaso |
| **F1** | `Cobas International P` | `LU1598719752` | `Cobas Renta FI` | `ES0119207001` | 1.000 € | Traspaso |
| **F1** | `NB Next Gen Space Economy` | `IE00018YKVN0` | `Cobas Renta FI` | `ES0119207001` | 1.000 € | Traspaso |
| **F1** | `UBS MSCI China All Shares` | `LU1815002040` | `Cobas Renta FI` | `ES0119207001` | 1.000 € | Traspaso |
| **F1** | Liquidez nueva | *Cuenta* | `iShares Developed World S` | `IE000ZYRH0Q7` | 10.000 € | Suscripción |
| **F2** | `DWS Floating Rate Notes LC` *(tras liquidar Rock)* | `LU0034353002` | `GS Global Small CORE Acc` | `LU1599216113` | 10.000 € | Traspaso |
| **F2** | `DWS Floating Rate Notes LC` | `LU0034353002` | `Cobas Renta FI` | `ES0119207001` | 7.000 € | Traspaso |
| **F2** | `DWS Floating Rate Notes LC` | `LU0034353002` | `iShares Developed World S` | `IE000ZYRH0Q7` | 3.000 € | Traspaso |

**Verificación de cierre:**
- `iShares Developed World S`: `22.000 + 10.000 + 3.000 = 35.000 €`
- `Fidelity MSCI Europe P`: `13.000 + 2.000 = 15.000 €`
- `Fidelity MSCI EM P`: `12.000 €`
- `Fidelity MSCI Japan Hedged P`: `8.000 €`
- `GS Global Small CORE Acc`: `10.000 €`
- `DWS Floating Rate Notes LC`: `30.000 − 10.000 − 7.000 − 3.000 = 10.000 €`
- `Cobas Renta FI`: `1.000 + 1.000 + 1.000 + 7.000 = 10.000 €`
- `Groupama Trésorerie IC`: `10.000 €` intactos (`0` órdenes).

---

## 6. Operativa, descartes y gobierno a 15 años

### 6.1. Comprobaciones previas obligatorias en MyInvestor
1. **Suscripción bonificada al `0 %` en pantalla:** los folletos de `DWS Floating Rate Notes LC` (hasta `1 %`) y `GS Global Small CORE` (hasta `5,50 %`) declaran comisión máxima de entrada; confirmar `0,00 %` en la boleta previa antes de firmar.
2. **Acceso y custodia en clase S:** `iShares Developed World S` (`IE000ZYRH0Q7`) declara mínimo institucional de `200 M€` en folleto (comercializado en MyInvestor con mínimo `0 €` en MCP); confirmar en pantalla que sigue abierto sin comisión de custodia.
3. **Aportación mensual (ejemplo `1.000 €/mes`):** repartir proporcionalmente entre las 7 líneas (`350 / 150 / 120 / 80 / 100 / 100 / 100 €`) o dirigir la aportación al bloque más alejado de su peso objetivo para rebalancear sin traspasos.

### 6.2. Descartes documentados de esta arquitectura

| Fondo descartado | ISIN | Motivo numérico del descarte |
| --- | --- | --- |
| `GSQuartix Bloomberg Commodity A` | `LU0397155978` | Volatilidad 3A `12,00 %` (`1A 16,27 %`, `2023 −10,96 %`) y TER `1,15 %`: cobertura táctica de inflación, no escudo defensivo fiable. |
| `Palm Harbour Global Value F` | `LU1935059029` | Patrimonio pequeño (`59,3 M€`), YTD `2026 +6,93 %`, sin cobertura en `quefondos`; concentrar la activa RV en `GS Small CORE` ahorra `~82 €/año` y simplifica. |
| `iShares Global Aggregate 1-5Y S EUR H` | `IE0004ZP1ND3` | Con solo un `5 %` (`5.000 €`) su duración (`2,69` años) no mueve el resultado de la cartera y añade una línea extra frente a `10 % DWS + 10 % Cobas Renta`. |
| `iShares Europe Index D` | `IE00BDRK7L36` | Mismo TER (`0,10 %`) que `Fidelity MSCI Europe P`, pero peor 3A/5A (`+15,75 %/+9,20 %` vs `+16,68 %/+9,52 %`), T+3 vs T+2 y concentra más peso en BlackRock. |

### 6.3. Reglas de rebalanceo y revisión
- **Bandas de rebalanceo:** ±5 pp en cualquier línea (o ±5 pp en el bloque RV/Escudo `80/20`), preferiblemente con nuevas aportaciones o mediante traspaso entre fondos (`0 €` IRPF).
- **Gatillo anticrisis (uso de `DWS Floating Rate Notes`):** si el MSCI World cae `≥ −20 %` desde máximos, traspasar `3.000 €` de `DWS FRN` a `iShares Developed World S` y `GS Small CORE`; si alcanza `−35 %`, otros `3.000 €`. **`Groupama Trésorerie IC` (`10.000 €`) nunca se toca para comprar bolsa.**
- **Prueba de alfa del único fondo activo de RV (revisión 2031):** evaluar `GS Global Small CORE` (`LU1599216113`) a 5 años contra `Vanguard Global Small-Cap Index` (`IE00B42W4L06`, TER `0,30 %`); si no supera el índice neto de comisiones tras un ciclo completo, traspasar el `10 %` al indexado de *small caps* y rebajar el TER total de la cartera al **`0,164 %` (`164 €/año`)**.

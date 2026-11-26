---
title: "Auditoría forense y ranking de cartera-ai-definitiva-final (Opción 0 y Opciones A–E)"
date: 2026-11-26
type: portfolio-research
category: finance
tags: [cartera, auditoria, ranking, cartera-ai-definitiva-final, option-0, opcion-a, opcion-b, opcion-c, opcion-d, opcion-e, myinvestor, 15-anos, coste, solape, estres]
status: final
related:
  - finance/laboratorio-carteras/cartera-ai-definitiva-final/README.md
  - finance/laboratorio-carteras/cartera-ai-definitiva-final/option-0.md
  - finance/portfolio/cartera-ai-propuesta/propuesta-actual.md
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
---

# Auditoría forense y ranking de `cartera-ai-definitiva-final`

Auditoría independiente, línea por línea y ficha por ficha (`45` ISIN únicos en `finance/fondos-myinvestor/`), de las **seis carteras** evaluadas en [`cartera-ai-definitiva-final/`](README.md): [`option-0.md`](option-0.md) (antigua `100k.md`), [`propuesta-actual.md`](../../portfolio/cartera-ai-propuesta/propuesta-actual.md) y las cuatro retiradas tras esta auditoría (`opcion-b.md`, `opcion-c.md`, `opcion-d.md` —descartada por el titular al no incluir gestión activa en RV— y `opcion-e.md`, conservadas en el historial de git), contrastadas contra [`cartera-actual.md`](../../portfolio/cartera-myinvestor/cartera-actual.md) bajo el mismo mandato (`100.000 €` libres + `10.000 €` intocables en `Groupama`, horizonte `15` años, `2026 → 2041`).

---

## 1. Hallazgos forenses críticos (errores detectados en los documentos)

Antes de ordenar las carteras, el cruce programático contra las fichas y la aritmética base detecta **seis anomalías materiales** que afectan directamente a la fiabilidad de las tablas publicadas:

### 1.1. Error de doble conteo en `opcion-e.md` *(retirada)* (`+10.166 €` inflados en el escenario inflacionario)
- `opcion-e.md` §7 (L173) y §12 (L290) —y por arrastre la versión anterior de `README.md` y `finance/portfolio/README.md`— publicaban **`4,99 %` neto (`207.600 €`)** en el escenario inflacionario (`5 %` RV / `8 %` activos reales / `3 %` RF).
- **Prueba aritmética del fallo:** para obtener `4,9878 %`, el documento calculó `74,912 % × 5 % + 12,00 % × 8 % + 20,088 % × 3 % − 0,3204 % = 4,9878 %`. El **`7 %` de `BNY Mellon Infrastructure` se contó dos veces** (dentro del `74,91 %` de RV y de nuevo dentro del `12 %` de satélites), haciendo que **los pesos sumen `107,0 %`**.
- **Cálculo corregido (`100 %` exacto):** `67,94 % × 5 % + 11,97 % × 8 % + 20,09 % × 3 % − 0,3204 % = 4,6369 %` → **`197.378 €`** a 15 años (**`10.166 €` menos** que los `207.600 €` publicados). `Opción E` sigue liderando el escenario inflacionario, pero por **`+4.565 €`** frente a `Opción D` (`192.813 €`), no por `+14.800 €`.

### 1.2. Declaraciones falsas de «solape 0» en el contenedor
El cruce exacto de los `45` ISIN muestra que la regla de no solape solo se cumplía en **B** y **C**:

| Par de carteras | Solape real por ISIN | % del patrimonio | Qué afirmaban los documentos |
| --- | --- | --: | --- |
| **Opción 0 ↔ Opción A** | **3 ISIN** (`IE00BYX5M476`, `IE00BYX5NH74`, `LU1599216113`) | `25 %` de 0 / `30 %` de A | El `README.md` anterior afirmaba *«0 con A–E»* (**falso**). |
| **Opción D ↔ Opción E** | **4 ISIN** (`IE00BD0NCM55`, `IE0031786696`, `FR0010738229`, `ES0165142003`) | `100 %` de D / `80 %` de E | `opcion-e.md` (L57, L238, L291) y el `README.md` anterior afirmaban *«0 ISIN con A, B, C, D y 13»* (**falso**; `E` compartía 4 de sus 7 fondos con `D`). |
| **Opción A ↔ Opción D y E** | **0 ISIN, 1 clase hermana** (`IE000ZYRH0Q7` clase S vs `IE00BD0NCM55` clase D) | `35 %` A / `70 %` D / `50 %` E | `opcion-d.md` lo declara bien; `opcion-e.md` L58 afirmaba *«Clases hermanas: 0»* (**falso**). |
| **Opción B y Opción C** | **0 ISIN y 0 clases hermanas** con todas las demás | `0 %` | Verificado al 100 %. |

### 1.3. Incumplimiento de regla EUR y contradicciones internas en `opcion-e.md` *(retirada)*
- **Divisa USD:** `BNY Mellon Global Infrastructure Income Fund USD A Acc` ([`IE00BZ18VV55`](../../fondos-myinvestor/sectoriales/IE00BZ18VV55.md)) es clase **USD sin cubrir** (`divisa USD`), incumpliendo la regla común de EUR.
- **Falsa calificación de gestión:** `opcion-e.md` §5 (L144) afirmaba que `BNY` y `DWS` son *«fondos de índice/gestión sistemática»*; la ficha de `BNY` confirma **gestión activa concentrada** (`top 10 = 56,56 %`, TER `1,97 %`).
- **Tres TER de variantes contradictorios:** `opcion-e.md` §13 (L301) publicaba `0,226 %`, `0,280 %` y `0,308 %` frente a los valores reales de su propia §8 (`0,191 %`, `0,259 %` y `0,318 %`).
- **Comparativa de estrés sesgada:** `opcion-e.md` §6 (L163) afirmaba tener *«el mejor estrés de las cinco»* omitiendo `Opción C` (`−28,72 %` vs `−31,62 %`).

### 1.4. Planes de ejecución incompletos en `opcion-d.md` y `opcion-e.md`
- **Option 0** (`18` órdenes), **Opción A** (`13`), **Opción B** (`17`) y **Opción C** (`16`) presentaban órdenes fondo a fondo desde los `8` manuales de `cartera-actual.md` + `Rock` + `10.000 €` nuevos, **verificadas al euro sin descuadres**. `Opción C` además evitaba expresamente el cambio de clase `Neuberger U → I`.
- **`opcion-d.md` §8 y `opcion-e.md` §8 NO incluían tabla de traspasos fondo a fondo** (solo un resumen agregado de 3 filas) ni designaban qué fondo recibe los `30.000 €` de `Cartera Rock` como puente.

### 1.5. Anomalías de comisiones y datos sin verificar en las fichas subyacentes
- **Comisiones de éxito `Pendiente` (no verificadas al `0 %`):** `Ashoka WhiteOak India D` (`IE00BDR0JY05`, `5 %` en **Option 0**) y `Palm Harbour Global Value F` (`LU1935059029`, `6 %` en **Opción C**). Ambos documentos los computaban como `0 %` éxito verificado.
- **TER publicado inferior a la comisión de gestión (confirmar KID antes de firmar):**
  - `Aegon European ABS A` (`IE00BG226Z29`, `8 %` en **Opción C**): TER `0,66 %` vs gestión `1,50 %` (y reembolso hasta `3 %` en `quefondos`).
  - `Mutuafondo CP D` (`ES0165142003`, `10 %` en **Opción D** y **Opción E**): TER `0,14 %` vs gestión `0,50 %`.
  - `Ofi Invest ISR Monétaire CT E` (`FR0010738229`, `10 %` en **Opción D** y **Opción E**): TER `0,06 %` vs gestión `0,11 %`.
  - `iShares Developed World S` (`IE000ZYRH0Q7`, `35 %` en **Opción A**): TER `0,06 %` vs gestión `0,09 %` en Finect, nacida el 21/08/2025 (sin 3A/5A propios) y mínimo de folleto `200 M€`.
- **Omisión en el `README.md` anterior:** la tabla principal marcaba `Top 10 US s/ total: n/d` para **Opción C**, cuando `opcion-c.md` §3 (L84) sí lo publicaba (**`7,77 %`** s/100k · `7,07 %` s/110k).

---

## 2. Matriz comparativa homogénea (mismas fórmulas para las seis, base `100.000 €`)

Todas las cifras están recalculadas con el mismo modelo sobre las fichas de `finance/fondos-myinvestor/` (`0 %` de alfa de gestor en proyecciones):

| Métrica | **Opción A** | **Opción D** | **Opción 0** | **Opción C** | **Opción E** | **Opción B** |
| --- | --: | --: | --: | --: | --: | --: |
| **Nº de fondos / % Indexado** | **7** / `70,0 %` | **4** / `80,0 %` | 13 / `43,0 %` | 10 / `40,0 %` | 7 / `68,0 %` | 11 / `40,0 %` |
| **RV efectiva (*look-through*)** | `81,03 %` | `80,06 %` | `84,24 %` | `69,52 %` | `74,93 %` *(+5 % MP)* | `80,71 %` |
| **TER fijo / Drag en 15 años** | `0,273 %` / `8.432 €` | **`0,127 %` / `3.946 €`** | `0,784 %` / `23.720 €` | `0,498 %` / `14.468 €` | `0,320 %` / `9.628 €` | `0,847 %` / `25.155 €` |
| **EE. UU. s/RV · Top 10 s/total** | `38,7 %` · `9,31 %` | `63,0 %` · `18,60 %` | `31,1 %` · **`4,24 %`** | `38,8 %` · `7,77 %` | `52,3 %` · `13,30 %` | `30,9 %` · `5,45 %` |
| **2022 real (shock inflación/tipos)** | `−8,96 %` | `−10,64 %` | `−5,74 %` | `−7,21 %` *(s/94 %)* | `−8,24 %` | **`−5,52 %`** |
| **Acumulado real `2022 → YTD 2026`** | **`+61,54 %`** | `+48,64 %` | `+60,65 %` | `+44,69 %` *(s/94 %)* | `+48,62 %` | `+60,08 %` |
| **Estrés 2008 estricto** *(40 % RV, 25 % MP, 2 % RF)* | `−32,79 %` | `−32,42 %` | `−35,16 %` | **`−28,42 %`** | `−31,62 %` | `−32,67 %` |
| **Shock directo Top 10 US (`−50 %`)** | `−4,66 %` | `−9,30 %` | **`−2,12 %`** | `−3,89 %` | `−6,65 %` | `−2,73 %` |
| **R1 — Neutro 15A** *(6 % RV / 3 % resto)* | `212.632 €` | **`216.205 €`** | `200.392 €` | `195.982 €` | `205.750 €` | `195.608 €` |
| **R2 — Inflacionario 15A** *(5 % RV / 8 % real / 3 % RF)* | `189.338 €` | `192.813 €` | `189.605 €` | `177.325 €` | **`197.378 €`** *(corr.)* | `180.248 €` |
| **R3 — Rotación Ex-US 15A** *(4 % US / 7,5 % ex-US / 6,5 % MP)* | **`216.227 €`** | `199.455 €` | `215.878 €` | `198.796 €` | `203.624 €` | `205.327 €` |
| **R4 — US Boom continúa 15A** *(8 % US / 5 % ex-US / 2 % MP)* | `216.631 €` | **`239.227 €`** | `197.374 €` | `199.193 €` | `217.102 €` | `193.941 €` |
| **Media de los 4 regímenes (15A)** | `208.707 €` | **`211.925 €`** | `200.812 €` | `192.824 €` | `205.963 €` | `193.781 €` |
| **Suelo mínimo entre los 4 regímenes** | `189.338 €` | `192.813 €` | `189.605 €` | `177.325 €` | **`197.378 €`** | `180.248 €` |
| ***Break-even* bloque activo vs pasivo `0,10 %`** | `+0,58 pp/año` | `+0,14 pp/año` | `+1,20 pp/año` | `+0,66 pp/año` | `+0,69 pp/año` | `+1,24 pp/año` |
| **Órdenes verificadas al euro** | Sí (`13`) | No *(resumen)* | Sí (`18`) | Sí (`16`) | No *(resumen)* | Sí (`17`) |

---

## 3. Ranking oficial (modelo institucional de 5 ejes)

Ponderación fija: **Coste y *break-even* (`25 %`)** · **Robustez multi-régimen y factores (`25 %`)** · **Protección en cola (`20 %`)** · **Ejecutabilidad operativa (`15 %`)** · **Integridad forense (`15 %`)**.

| Pos. | Cartera | Coste (25 %) | Multi-régimen (25 %) | Cola (20 %) | Operativa (15 %) | Integridad (15 %) | **Nota final** | Veredicto en una línea |
| :-: | --- | --: | --: | --: | --: | --: | :-: | --- |
| **#1** | **[`propuesta-actual.md`](../../portfolio/cartera-ai-propuesta/propuesta-actual.md) — Opción A** | 9,0 | 8,8 | 7,8 | 9,2 | 8,8 | **8,71 / 10** | Mejor equilibrio global: coste de índice (`0,273 %`), desconcentración real, #1 en 2022–2026 (`+61,5 %`) y plan limpio en 7 fondos. |
| **#2** | **`opcion-d.md` *(retirada)* — Opción D** | 9,8 | 8,2 | 6,5 | 7,5 | 9,0 | **8,28 / 10** | Ganadora pura en capital neutro (`216.205 €`), media 4 regímenes (`211.925 €`) y coste (`0,127 %`), pero expuesta al riesgo megacap (`18,6 %`), sin gestión activa en RV y sin desglose de órdenes. |
| **#3** | **[`option-0.md`](option-0.md) — Opción 0** | 5,8 | 8,5 | 8,4 | 8,2 | 8,8 | **7,81 / 10** | La mejor cartera activa anti-burbuja (domina a B en coste, RV y 3 de 4 regímenes), pero lastrada por `13` fondos y `23.720 €` de comisiones a 15A. |
| **#4** | **`opcion-c.md` *(retirada)* — Opción C** | 7,5 | 6,8 | 9,0 | 8,0 | 7,8 | **7,75 / 10** | Ganadora si tu límite conductual es `< −30 %` (`−26,1 %` consolidado en 2008), pero sacrifica `~17k–20k €` a 15A por bajar al `69,5 %` de RV. |
| **#5** | **`opcion-e.md` *(retirada)* — Opción E** | 8,2 | 8,3 | 7,8 | 6,4 | 4,5 | **7,32 / 10** | Buena arquitectura de activos reales (mejor suelo mínimo en los 4 regímenes), pero castigada por el error de `+10.166 €`, falso `0` solape, `BNY` en USD y falta de órdenes. |
| **#6** | **`opcion-b.md` *(retirada)* — Opción B** | 5,0 | 7,4 | 8,6 | 7,4 | 8,8 | **7,25 / 10** | Mejor 2022 (`−5,52 %`) y `0` solape real, pero dominada por Opción 0 en su misma tesis y penalizada por el mayor drag de comisiones (`25.155 €` a 15A). |

---

## 4. Dictamen por cartera (fortalezas, vulnerabilidades y qué corregir)

### #1 — Opción A ([`propuesta-actual.md`](../../portfolio/cartera-ai-propuesta/propuesta-actual.md)) · `8,71 / 10`
- **Por qué gana:** consigue la mayor parte de la desconcentración de las carteras activas (`38,7 %` EE. UU. y `9,31 %` en Top 10) pagando solo `0,273 %` (`8.432 €` en 15 años frente a `23.720 €`–`25.155 €` de 0 y B). Lidera tanto el **acumulado real 2022–2026 (`+61,54 %`)** como el escenario de **Rotación Ex-US (`216.227 €`)**, queda #2 en neutro (`212.632 €`) y se opera en 7 fondos con 13 órdenes cuadradas al euro.
- **Riesgos a vigilar:** `iShares Developed World S` (`35 %`) exige validar acceso ómnibus sin custodia en MyInvestor (mínimo de folleto `200 M€`); `Cobas Renta` (`10 %`) es un mixto (`14,5 %` RV + crédito privado con `3,9 %` Ghana), no pura liquidez sin riesgo; y tiene `0 %` en materias primas/infraestructura si la inflación repunta.

### #2 — Opción D (`opcion-d.md`, retirada) · `8,28 / 10`
- **Por qué es #2:** imbatible en simplicidad (`4` fondos), coste (`0,127 %`) y capital esperado sin apuestas (`216.205 €` neutro; `211.925 €` media de 4 regímenes). Cero riesgo de gestor.
- **Por qué no es #1:** asume íntegro el riesgo de concentración actual (`63 %` EE. UU., `32,5 %` tecnología, `−9,30 %` directo si el Top 10 cae un `50 %`, peor 2022 con `−10,64 %`). Antes de ejecutarla requiere redactar la tabla de traspasos fondo a fondo desde `cartera-actual.md`, elegir puente de `Rock` y verificar en pantalla los mínimos ómnibus (`100k`/`1M`) y el KID de `Ofi` y `Mutuafondo`.

### #3 — Opción 0 ([`option-0.md`](option-0.md)) · `7,81 / 10`
- **Por qué lidera las activas:** si quieres protegerte de una burbuja tecnológica sin bajar la RV (`84,24 %`), **Option 0 domina a Opción B** —lleva `+3,5 pp` más de RV, cuesta `6 pb` menos, protege el Top 10 mejor (`4,24 %` vs `5,45 %`), incorpora materias primas (`5 %` con `+14,83 %` en 2022) y gana a B en 3 de los 4 regímenes y en el acumulado 2022–2026 (`+60,65 %`).
- **Por qué no alcanza el podio superior:** `13` fondos complican el mantenimiento durante 15 años, el peaje de `0,784 %` (`23.720 €` en 15A) exige `+1,20 pp/año` de alfa sostenido sobre el bloque activo, su estrés 2008 estricto es el más profundo (`−35,16 %`) y `Ashoka India` (`5 %`) tiene éxito `Pendiente` y SRRI 6 real.

### #4 — Opción C (`opcion-c.md`, retirada) · `7,75 / 10`
- **Su único mandato legítimo:** es la cartera correcta **solo si el titular no tolera ver `−33.000 €` en una crisis tipo 2008** (`−28.420 €` / `−26,1 %` consolidado con Groupama). Mantiene disciplina de costes (`0,498 %`) y su plan de 16 órdenes es impecable.
- **Coste de esa tranquilidad:** con `69,5 %` de RV queda última en la media de 4 regímenes (`192.824 €`) y en el acumulado 2022–2026 (`+44,69 %`). Antes de ejecutarla hay que verificar la anomalía de costes de `Aegon ABS` (`TER 0,66 %` vs gestión `1,50 %`) y el éxito `Pendiente` de `Palm Harbour`.

### #5 — Opción E (`opcion-e.md`, retirada) · `7,32 / 10`
- **La tesis merece mucho más que el documento:** incluso tras corregir el doble conteo de `+10.166 €`, `Opción E` sigue teniendo **el mejor suelo mínimo entre los 4 regímenes (`197.378 €`)**, gana el escenario inflacionario y ocupa el #3 en media multi-régimen (`205.963 €`).
- **Por qué cae al #5 hoy:** falla la auditoría documental y operativa (doble conteo al `107 %`, falso `0` solape con D, tres variantes con TER erróneo en §13, `BNY` en **USD** al `1,97 %` TER con `5 %` entrada en folleto y falta de plan de traspasos). Si se reescribe sustituyendo `BNY` por infraestructura en EUR más barata (`Wellington` o `First Sentier`) y añadiendo órdenes fondo a fondo, saltaría al rango `~8,1–8,3 / 10`.

### #6 — Opción B (`opcion-b.md`, retirada) · `7,25 / 10`
- **Qué hace bien:** es la que menos cayó en 2022 (`−5,52 %`), la más pura en no repetir fondos (`0` solape real) y tiene 17 órdenes cuadradas al euro.
- **Por qué queda última:** es la más cara (`0,847 %` = `25.155 €` de drag en 15A), exige el mayor alfa de empate (`+1,24 pp/año`), queda última en Neutro (`195.608 €`) y en US Boom (`193.941 €`), y está dominada estratégicamente por **Option 0** (misma convicción anti-burbuja con mejor equilibrio de activos y menos coste) y por **Opción A** (`+17.024 €` más en escenario neutro con 4 fondos menos).

---

## 5. Decisión práctica en 30 segundos

- **Elección por defecto (mejor riesgo/retorno/coste):** **Opción A** (`8,71/10`).
- **Si crees que EE. UU. seguirá mandando y quieres 4 fondos a coste mínimo:** **Opción D** (`8,28/10`), añadiendo la tabla de órdenes fondo a fondo antes de ejecutar.
- **Si tu miedo central es la inflación persistente (`3,5–4 %`):** **Opción E corregida** (cambiando `BNY` USD `1,97 %` por infraestructura en EUR y redactando órdenes).
- **Si no aguantas un `−33 %`:** **Opción C** (`7,75/10`), verificando el KID de `Aegon ABS` y `Palm Harbour`.
- **Descartables hoy frente a las anteriores:** **Opción B** (dominada por Option 0 y Opción A) y **Option 0** salvo que quieras convicción activa máxima asumiendo `13` fondos y `23.720 €` de drag.

> *Análisis técnico y auditoría documental sobre fichas del repositorio (`finance/fondos-myinvestor/`). No constituye asesoramiento financiero personalizado.*

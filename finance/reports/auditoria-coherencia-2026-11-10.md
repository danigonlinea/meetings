---
title: "Auditoría de coherencia: dos verdades sobre la misma cartera"
date: 2026-11-10
type: revision
category: finance
tags: [auditoria, coherencia, cartera, myinvestor, renta4, informes, termometro, glosario]
status: final
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-myinvestor/propuesta-actual.md
  - finance/portfolio/cartera-renta4/propuesta-actual.md
  - finance/reports/contraste-propuesta-ackman-2026-11-03.md
---

# Auditoría de coherencia — 10/11/2026

**Alcance.** Los documentos que dicen qué es verdad: los índices de carpeta, las propuestas de cartera,
los informes de canal, las síntesis, los glosarios y las herramientas. **No** se auditan las
transcripciones ni la calidad de los resúmenes: el objetivo es otro — encontrar dónde el repositorio
afirma dos cosas distintas sobre el mismo hecho.

**Método.** Lectura completa de los 34 artefactos, recálculo de cada suma y ponderación con Python
(cartera, órdenes, costes, duración, pesos), ejecución de `tools/verify.py`, `tools/build_index.py` y
`tools/termometro.py`, y comprobación de cada ruta citada contra el árbol real y de cada referencia a
commit contra `git`.

**Veredicto.** La aritmética de la cartera vigente aguanta casi entera (pesos, TER, RV look-through,
cuadre de las 14 órdenes). Lo que no aguanta es **la capa que describe esa aritmética**: tres
documentos siguen afirmando que la cartera definitiva es la del 03/11 (50/50, Sissener, 588 €/año), y
la herramienta del repositorio mide precisamente esa versión derogada. Hay además errores de suma
localizados en el documento vigente y en el de Renta 4, y un glosario con correcciones pendientes desde
el 11/10 que nadie aplicó.

## Estado a 10/11/2026

El titular fijó la verdad vigente —`propuesta-actual.md` del 04/11, con `propuesta-acciones.md` como
complemento de acciones— y el mismo día se corrigió esto:

| Hallazgo | Estado |
| --- | --- |
| §1 dos verdades sobre la cartera | ✅ README de cartera y `propuesta-acciones.md` al 55/45; avisos de vigencia fechados en el contraste del 03/11 y en la revisión del 02/11; referencia de Renta 4 actualizada |
| §2 subtotales de sesión, Fidelity, carry, euro-duración, tabla de retorno y fila de §11 | ✅ corregidos y verificados con el termómetro |
| §3 termómetro sobre la cartera derogada | ✅ reescrito: re-puntúa las ocho señales, valida la suma (45 + 10 = 55) y reproduce las dos tablas de §2 |
| §4 Renta 4 | ✅ liquidez (4.632 €) y carry (39 / 74 €/año) cuadrados |
| §5 prima francesa | ✅ matizada como dato del 23-10; «15 carpetas» → 14; el minuto 61:01/61:03 se comprobó y los dos son válidos |
| §6 títulos truncados | ✅ arreglados en el frontmatter y en el INDEX |
| §7 rutas del README | ✅ `finance/videos/myinvestor-webinars/` y las seis skills |
| Glosario, 14 etiquetas de plantilla, la sexta propuesta de §12, `AGENTS.md` | ⏳ pendiente |

## 1. Bloqueante — dos verdades sobre la cartera de MyInvestor

La versión vigente es `propuesta-actual.md` del **04/11/2026**: 55,0 % RV / 45,0 % RF, diez fondos
manuales, Sissener fuera, cero ETFs, **424,80 €/año (0,438 %)** y catorce órdenes. Su §12 dice
literalmente que la propuesta del 03/11 (50/50) se borró y que «Sissener sale por composición».
Cuatro documentos siguen contando la historia anterior:

| Documento | Lo que afirma | Lo que dice el documento vigente |
| --- | --- | --- |
| `finance/portfolio/README.md:17` | «**definitiva desde 03/11/2026**: 50/50 con Aegon ABS y Sissener, **588 €/año** de coste real» | 04/11, 55/45, sin Sissener, 424,80 €/año |
| `finance/portfolio/README.md:49-51` | «propuesta cerrada al 50,0 %… **0,655 % de TER, 11 órdenes**… elegir anexo (los dos proponen ya los mismos dos vehículos: **Fundsmith** y los REITs)» | 0,438 %, 14 órdenes, y §10.2 descarta Fundsmith con número («cede 334 €/año») |
| `finance/reports/contraste-propuesta-ackman-2026-11-03.md` | «la cartera definitiva adoptada el 03/11», 50/50, ocho fondos, Neuberger 31.900, Sissener, coste 588 €/año (0,606 %); y dice haber aplicado sus cambios «sobre `propuesta-actual.md` (§1, §2, §6, §9 y §13)» | 55/45, diez fondos, Neuberger 17.000, sin Sissener, 424,80 €; y cita §14 y §10.3, **secciones que no existen** en el documento actual (tiene 13 y los umbrales están en §11) |
| `finance/reports/revision-adversarial-2026-11-02.md` | «El 50/50 y las once órdenes… sin cambios», bloque de RF de 48.500 €, EE. UU. al 32,5 % de la RV | 55/45, 43.624 € de RF, EE. UU. al 30,0 % |

Nadie marcó estos tres últimos como obsoletos: los cuatro están `status: final`. El README de la
carpeta de nivel superior —el que fija el orden de lectura— es el que más se desvía: la subcarpeta
`cartera-myinvestor/README.md` ya está reescrita al 04/11 y las dos afirman cosas incompatibles.

**Agravante interno:** `cartera-myinvestor/propuesta-acciones.md`, fechado el **mismo 04/11**, repite
cinco veces que «no modifica el 50/50» y que «el 50/50 de MyInvestor sigue siendo el núcleo»
(líneas 22, 176, 183, 496, 498, 504). Dos documentos del mismo día no se ponen de acuerdo sobre cuál
es la cartera núcleo.

**Tercero citado:** `cartera-renta4/propuesta-actual.md:190` usa como referencia
`../cartera-myinvestor/propuesta-actual.md` **«(31/10/2026)… objetivo 50/50»**. Ese documento no
existe hoy y la fecha no corresponde a ninguna versión del historial: la de 50/50 era del 03/11.

## 2. Aritmética del documento vigente que no cuadra

Recalculado con los importes del propio §7:

| Qué dice | Qué sale | Consecuencia |
| --- | --- | --- |
| §7.1 «Sesión 1 — **31.000 €** · 7 órdenes» | 4.000+3.000+5.000+4.800+1.000+4.200+3.000 = **25.000** | Se planifica una sesión con 6.000 € de más |
| §7.2 «Sesión 2 — **18.000 €** · 7 órdenes» | 4.000+2.000+1.000+1.000+7.000+4.000+5.000 = **24.000** | Se planifica con 6.000 € de menos; las ocho filas del cuadre por origen sí suman 49.000 |
| §7 «Catorce órdenes, **49.000 €**» | 25.000 + 24.000 = **49.000** | El total es correcto: los dos subtítulos son los que están mal |

Más desviaciones, todas verificadas contra las tablas del propio documento:

1. **§9.3 concentración por gestora.** Fidelity figura con 19.700 € (20,3 %). Sus fondos suman
   9.900+2.700+2.100+600 (Rock) + 3.000 (Japón manual) + 2.000 (Pacífico manual) = **20.300 €**.
   Con la cifra correcta, la columna suma 97.000 €; con la publicada suma **96.400 €** y faltan
   exactamente los 600 € del Pacífico de Rock.
2. **§11.1 carry cobrado.** «En 2026 la RF manual cobró ≈1,3 % (Neuberger −0,03 %, Aegon +2,39 %,
   Amundi −0,19 %)». Ponderado por los importes de §3 (17.000 / 7.000 / 7.200 sobre 36.200) da
   **0,41 %**; media simple, 0,72 %. El 1,3 % no se reproduce con ninguna combinación de sus tres
   cifras, y de él cuelga el «−2,5 % real» y la señal de +3 puntos.
3. **§6 «El 76 % del riesgo de tipos vive en Rock».** Por euro-duración: manual 36.200 × 2,3 = 83.260;
   Rock 3.600 × 6 + 3.000 × 15 = 66.600 → **44 %**, no 76 %. Con las duraciones declaradas el impacto
   de +100 pb es **≈1.500 €**, no los 1.590 € de la tabla.
4. **§11 tabla de revisión.** «Carry cobrado… **+3 → ~58 %**» choca con §2 (ese +3 ya está dentro del
   55) y con §11.1, que dice que si la señal vuelve a 0 «el modelo baja a **52 %**». La fila debería
   decir 52, no 58.

## 3. El termómetro mide la cartera derogada

`tools/termometro.py` se presenta como «la aritmética de `propuesta-actual.md` §2 y §10». Hoy hace lo
contrario:

- `finance/portfolio/termometro-datos.json` es del **31/10** y trae `rv_pct: 50.0` y
  `rf_cartera: 4.79` — la TIR declarada de la cartera del 03/11, no el carry cobrado de la vigente.
- Su salida imprime «RF de la cartera **+0,99 % real**», que es justo la cifra que
  `revision-adversarial-2026-11-02.md` §3.1 declaró inválida (YTW ≠ cobrado) y que la propuesta
  vigente sustituye por **−2,5 % real cobrado** (§11.1) y por 4,24-4,65 % de TIR (§2).
- Por defecto simula **50 %** de RV, no el 55 % decidido.
- Con `--rv 45` y `--rv 55` la tabla de consecuencias **no coincide** con el §2 del documento:

| RV | Caída, termómetro | Caída, propuesta | Retorno, termómetro | Retorno, propuesta |
| --: | --: | --: | --: | --: |
| 45 % | −19,8 % | −19,6 % | 5,6 % | 5,05 % |
| 55 % | −23,2 % | −23,4 % | 5,8 % | 5,56 % |

- `bono_10y` está a `null`, así que imprime «Prima de riesgo de la RV: sin dato» mientras §2 calcula
  +2,4 pp, y no puede disparar el umbral de −10 puntos.
- Docstring y `README.md:116` remiten a los «umbrales del §10»; en el documento vigente §10 es «lo que
  se descarta» y los umbrales están en **§11**. Es numeración de la versión del 03/11.

## 4. Cartera Renta 4

1. **La liquidez no suma (§3.3).** «La cartera tiene **4.632 €** en efectivo y monetarios: **4.272 €**
   en el fondo de 6 Meses y **1.951 €** dentro del propio Kaizen». 4.272 + 1.951 = **6.223 €**. Y
   `cartera-actual.md` §3 también da 4.632 € de liquidez y 13,3 %: una de las dos cifras está mal,
   porque la liquidez de Kaizen (15,8 % de 12.310 = 1.945) ya está dentro de ese 4.632.
2. **Dos carry distintos para los mismos fondos (§2 vs §7).** §2 mide RF R en **+3,5 %** y 6 Meses en
   **+2,9 %** (€STR 2,4 %); §7 justifica el descarte con «renuncia a 1,1 pp de carry (**3,3 % →
   2,2 %**), ~135 €/año». Los 135 € salen de 1,1 pp, pero las dos parejas de tipos no pueden ser
   ciertas a la vez.
3. **Etiqueta de la exposición USA.** `cartera-actual.md` §4 dice «≈56 % de la RV (Rock vía S&P 500 y
   Vanguard US)». 13.230 € sobre la RV total (28.400 €) es **46,6 %**; el 56 % es de la RV de Rock,
   no de la cartera.

Lo que sí cuadra en Renta 4: pesos (8.692,30 + 3.618,16 + 5.913,75 + 12.273,24 + 4.271,75 = 34.769,20),
RV 15,3 % → 21,2 %, coste 264 €/año, plusvalía 638,69 €.

## 5. Informes de canal y síntesis

1. **La prima francesa se contradice en la misma línea.** `sintesis-inversor-2026-10-30.md:54`: «152 pb,
   con OAT ~5 % frente a Bund 3,4 %». La resta da **160 pb**; la tabla de señales del mismo documento
   (línea 108) dice «1,6 puntos según Andrés». Se reproducen las dos versiones sin marcar que el
   hablante se contradice — es el caso que la propia revisión del 30/10 identifica como error suyo
   («calcula 3,2 y concluye 3,5»).
2. **Recuento de carpetas.** `informe-canal-…-2026-11-02.md:19`: «Carpetas del canal leídas: **15**».
   En `finance/videos/la-pizarra-de-andres/` hay **14**, y eran 14 también el 02/11 (las 4 que venían
   de `ai/` están entre ellas). El número no sale ni antes ni después del movimiento.
3. **El minuto de la misma cita.** El informe del 30/10 usa `61:01` y la síntesis `61:03`. Comprobado
   contra la transcripción: la frase arranca en **61:01** («Bueno, yo recomiendo, de hecho,») y la
   cláusula citada cae en **61:03**. No hay error: son dos cortes de la misma frase. Se deja 61:01, que
   es donde empieza.
4. **Clase del fondo sin distinguir.** El informe del 30/10 nombra «MyInvestor Value, FI **clase A**
   (ES0165243009)»; el del 02/11 y el snapshot hablan de «MyInvestor Value **C** (ES0165243025)», que
   es la que está en cartera. Son clases distintas del mismo fondo: el lector no puede saber si el
   invitado y el titular tienen la misma.
5. **Fuentes contadas a ojo.** `propuesta-acciones.md:30`: «17 `summary.md` y 3 informes de
   `finance/reports/`». Hay **18** resúmenes y **7** informes.

## 6. Metadatos e índice

- **Dos títulos truncados y uno con YAML inválido.** `2026-10-15-da-miedo…/summary.md:2`:
  `title: "La Pizarra de Andrés: "Da miedo, pero la IA puede solucionar la economía" (Juan "` — comillas
  sin escapar, cortado a mitad de nombre, mientras que el H1 del mismo fichero dice «(Juan Santamaría)».
  `2026-10-25-…abaco-capital/summary.md:2`: `…la oportunidad que espera en el` (el H1 continúa «en el
  crédito (Ábaco Capital)»). `build_index.py` los propaga tal cual al `INDEX.md`.
- **14 de 34 artefactos llevan etiquetas de plantilla** (`[finance, meeting, transcript]` o
  `[ai, meeting, transcript]`), contra la convención del `README.md`. El índice se vuelve inútil para
  buscar por tema en casi la mitad del repositorio.
- **El glosario lleva un mes sin actualizarse.** `reference/glossary.md` es del 11/10 y el repositorio
  tiene 26 artefactos posteriores. En `Ponentes`, Andrés figura con «Aparece en 2026-10-09; 2026-10-07»
  cuando es el presentador de 14 carpetas; en `Canales`, El Arte de Invertir se sitúa en 2026-10-07,
  pero esa carpeta vive bajo `la-pizarra-de-andres/`.
- **Correcciones pendientes que nunca se aplicaron.** La tabla «Aclaraciones alcanzables» sigue con dos
  ítems del 2026-10-09 en «Pendiente de ajuste»: el resumen mantiene «39 % y 41 %» de concentración
  (el glosario registra que el audio dice «43 de cada 100… en torno al 40») y «el periodo entre 1929 y
  1972» (el glosario pedía separar el crack del 29 del 72 japonés). **Agrava:** esa carpeta no tiene
  `transcript.json` (`verify.py` la marca con aviso), así que la corrección ya no se puede verificar
  contra la fuente.
- Errata menor: `glossary.md:92` «Correxir».

## 7. Rutas y documentos citados que no existen

- `README.md:103` y `AGENTS.md:18` remiten a `finance/myinvestor-webinars/`. La ruta real es
  `finance/videos/myinvestor-webinars/`; la skill `ingest-webinars` ya la tiene bien.
- `README.md:71` lista cuatro skills; `.agents/skills/` tiene seis (`informe-semanal` y
  `cribado-acciones` no aparecen).
- `cartera-myinvestor/cartera-actual.md:119` remite a `cartera-auditoria-2026-10-30.md`, «ahora
  `diagnostico-2026-10-30.md`». Ninguno de los dos existe en la carpeta.
- `cartera-myinvestor/README.md:26` llama a `50b2e69` «último commit con la carpeta completa». Ese
  commit borra `propuesta-definitiva.md`: una **sexta** propuesta que no aparece en la tabla de §12
  (que solo inventaría cinco).

## 8. Lo que se comprobó y sí aguanta

Para que el lector sepa dónde no hay que buscar:

- **Posiciones de MyInvestor:** las once filas de §3 suman 97.000 € exactos; los pesos, la RV dentro de
  cada ficha y el look-through (53.380 € = 55,03 %) son correctos.
- **Coste:** 301,80 € manuales (recálculo fondo a fondo) + 123 € de Rock = 424,80 € = 0,438 % de 97.000 €.
  Cobas International sí es el 38,6 % del coste manual.
- **Cuadre de las órdenes por origen y por destino:** ambos dan 49.000 €, y los saldos de partida suman
  60.000 €. El error está solo en los subtítulos de sesión.
- **Señales de §2:** 0+3+2−5+2+3+3+2 = +10 sobre base 45 → 55 %. Coherente.
- **Renta 4:** verificado arriba salvo los tres puntos de §4.
- **Mecánica del repositorio:** `verify.py` pasa (0 errores; los 2 avisos de transcripción pegada son
  reales), `build_index.py` genera 34 artefactos y `INDEX.md` está sincronizado. Los commits citados
  existen y contienen lo que se dice, salvo el matiz de §7.
- **`catalogo.md`:** 141 webinars, 1 ingerido, 140 pendientes — cuadra con las carpetas.

## 9. Qué arreglar, en este orden

1. **Decidir una sola verdad y propagarla** (es decisión del titular, no del agente): si la vigente es
   la del 04/11, reescribir `finance/portfolio/README.md:17,49-51`, añadir una nota de obsolescencia
   fechada a `contraste-propuesta-ackman-2026-11-03.md` y a `revision-adversarial-2026-11-02.md`, y
   sustituir el «50/50» de las cinco líneas de `propuesta-acciones.md`. Mientras existan, el
   repositorio tiene dos carteras oficiales.
2. **Corregir los dos subtítulos de sesión de §7** (25.000 y 24.000) y la fila de Fidelity de §9.3
   (20.300 € / 20,9 %). Son errores de suma, no de criterio.
3. **Poner el termómetro al día o declararlo histórico:** actualizar `termometro-datos.json` a
   55 % y carry cobrado (4,24 % de TIR o el 1,3 % real si se sostiene), pasar `bono_10y`, alinear las
   dos funciones con la tabla de §2 y renombrar «§10» → «§11».
4. **Renta 4:** fijar la liquidez (4.632 € o 6.223 €) y unificar los tipos de los dos fondos de RF.
5. **Metadatos:** arreglar los dos títulos, sustituir las 15 etiquetas de plantilla y actualizar el
   glosario (ponentes, canales y las dos correcciones pendientes del 10-09).
6. **Rutas:** `finance/videos/myinvestor-webinars/` en `README.md` y `AGENTS.md`; las seis skills en el
   `README.md`.

**Lo que este documento no decide:** cuál de las dos versiones de cartera es la buena, el importe del
colchón y el % de RV. Eso está en `propuesta-actual.md` y es del titular.

> Auditoría de coherencia interna. No es asesoramiento financiero.

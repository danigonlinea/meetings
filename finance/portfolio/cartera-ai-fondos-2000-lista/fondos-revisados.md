---
title: "Revisión en profundidad de los 52 fondos de cartera-ai-fondos-2000-lista"
date: 2026-11-20
type: reference
category: finance
tags: [fondos, revision, myinvestor, comisiones, evidencia, due-diligence]
status: final
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/README.md
---

# Revisión fondo a fondo (52 fondos)

Criba sistemática de las **2.007 fichas** del listado (`fondos_parsed.json`) y lectura de la ficha completa de cada uno de los 52 fondos que finalmente entran en las cinco carteras. Para cada uno: identidad, costes, mínimos, divisa, exposición real, evidencia y pegas. **Ninguna cifra se ha inventado**: lo que la ficha no publica figura como Pendiente o con la fuente que lo contradice.

Orden: por cartera. `MCP` = ficha del catálogo; `web` = quefondos/Finect/folleto citados en la ficha; `snapshot` = dato del listado de la app de 19/11/2026, que manda cuando hay discrepancia.

## C1 — 9 fondos

### iShares Developed World Index (IE) Acc EUR clase S — `IE000ZYRH0Q7`

**Identidad y operativa.** BlackRock Asset Management Ireland Ltd · clase `rv-global` · fuente `listado-app` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Núcleo MSCI World indexado. Importe: 40.000 €. Ficha: `finance/fondos-myinvestor/rv-global/IE000ZYRH0Q7.md`.

**Coste y mínimos.** TER snapshot **0,06 %** (0,06 % (snapshot app; Finect: gastos corrientes 0,060 %)); gestión 0,090 % (Finect); éxito n/a (Finect); mínimo publicado "200.000.000 (quefondos lo publica en USD; tabla de clases de Finect, en EUR)"; mínimo operativo verificado: **MCP 20/11: 0.00 EUR**. NAV 12.231.

**Exposición y evidencia.** RV 99,29 % · RF 0,00 % · 3A Pendiente · 5A Pendiente · SRRI 4. Patrimonio: 26.242,4 M€.

**Regiones.** Estados Unidos 72,0 %; Zona Euro 8,2 %; Japón 5,8 %; Europa ex-Zona Euro 3,9 %; Canadá 3,4 %; Reino Unido 3,4 %; Australasia 1,7 %; Asia Desarrollada 0,9 %. País desarrollado 99,5 %.

**Sectores.** Tecnología 30,8 %; Servicios Financieros 16,3 %; Industriales 10,7 %; Salud 9,2 %; Consumo Cíclico 8,7 %; Servicios de Comunicación 8,0 %; Consumo Defensivo 4,8 %; Energía 4,1 %; Materiales Básicos 3,3 %; Servicios Públicos 2,3 %; Inmobiliario 1,6 %.

**Quién es y para qué sirve.** Clase S en euros del iShares Developed World Index Fund (IE), un fondo indexado que busca replicar el índice MSCI World de renta variable de países desarrollados, invirtiendo en los valores del índice en proporciones similares (réplica física, según la política publicada en quefondos). La clase se constituyó el 21/08/2025 (quefondos; Finect indica 20/08/2025), por lo que el historial es de poco más de un año. Patrimonio del fondo: 26.242,4 M€; patrimonio de la clase: 1.325,3 M€ (Finect, datos a 17/11/2026); quefondos cifra el patrimonio de la clase en 1.375.201,64 miles de euros a 16/11/2026. Categoría VDOS: RVI Global; categoría Morningstar (Finect): RV Global Cap. Grande Blend.

**Lectura para cartera (texto de la ficha).** Papel de **núcleo de renta variable global** para un inversor que quiere exposición a mercados desarrollados con coste mínimo y sin pretensión de batir al índice: es la clase más barata del lote (TER 0,06 %). La clase S está pensada para institucionales (mínimo publicado de 200.000.000, según quefondos en USD y según la tabla de clases de Finect en EUR); su presencia en el listado de la app indica que MyInvestor da acceso a ella, pero el mínimo oficial publicado es una barrera formal a tener en cuenta. La evidencia disponible es corta pero coherente con una réplica del MSCI World: en 2026 (a 1 …

**Pegas detectadas.**
- Historial <3 años: clase constituida en agosto de 2025; sin rentabilidades a 3A/5A ni años naturales completos. Limitación, no promesa.
- Comisiones discrepantes entre fuentes: quefondos publica fija 0,30 % y depósito 0,30 %, mientras Finect da gestión 0,090 %, custodia n/a y gastos corrientes 0,060 % (coincidente con el TER 0,06 % del snapshot, que manda)
- Mínimo institucional: 200.000.000 publicados (USD en quefondos, EUR en Finect); divisa del mínimo inconsistente entre fuentes.
- SRRI discrepante: snapshot 4 vs riesgo 5/7 en Finect; manda el snapshot.
- Concentración: ~72 % EE. UU. y ~31 % tecnología; top 10 posiciones ≈ 26,6 %.
- Divisa sin cubrir: clase EUR sobre cartera mayoritariamente USD; la rentabilidad en euros incorpora el tipo de cambio.
- Fecha de constitución con un día de diferencia entre fuentes (21/08 quefondos, 20/08 Finect).

**Decisión.** clase S 2025, sin 3A propio; índice MSCI World

**Verificación web 20/11/2026.** Las fichas web publican 200.000.000 (USD en quefondos, EUR en Finect) para la clase S, mientras el dato MCP del 20/11/2026 da 0,00 EUR. Se conserva la clase S por ser la operable en la plataforma y se escribe el mínimo publicado como condición a comprobar en pantalla antes de la primera orden. (fichas del repo + MCP 20/11).

### Vanguard Global Small-Cap Index Fund EUR Acc — `IE00B42W4L06`

**Identidad y operativa.** Vanguard Group (Ireland) Limited · clase `rv-global` · fuente `listado-app` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Small caps globales indexado. Importe: 8.000 €. Ficha: `finance/fondos-myinvestor/rv-global/IE00B42W4L06.md`.

**Coste y mínimos.** TER snapshot **0,30 %** (0,30 % (snapshot app)); gestión 0,29 % (quefondos / Finect); éxito n/a (Finect); mínimo publicado "1.000.000,00 EUR (quefondos, clase institucional)"; mínimo operativo verificado: **MCP 20/11: 1.00 EUR**. NAV 426.996.

**Exposición y evidencia.** RV 99,94 % · RF 0,00 % · 3A 16,01 % · 5A 6,07 % · SRRI 4. Patrimonio: 7.100,4 M€.

**Regiones.** Pendiente

**Sectores.** Pendiente

**Quién es y para qué sirve.** Clase de acumulación en EUR del fondo indexado Vanguard Global Small-Cap, que rastrea el **MSCI World Small Cap Index** (pequeñas empresas de mercados desarrollados). Replica el índice invirtiendo en todos sus valores en la misma proporción (o mediante muestreo) y se mantiene plenamente invertido salvo condiciones extraordinarias. Fecha de constitución: 06/12/2012 (quefondos); inicio de clase 11/12/2012 (Finect). Patrimonio del fondo: 7.100,4 M€; de la clase: 1.298,3 M€ (Finect, 18/11/2026).

**Lectura para cartera (texto de la ficha).** Candidato a **satélite de pequeña capitalización global** en clase EUR: aporta el segmento small-cap de los mercados desarrollados que un núcleo MSCI World de gran capitalización no cubre. Para un inversor en EUR es la clase natural del fondo (valor liquidativo en EUR), aunque las divisas subyacentes de la cartera siguen sin cubrir. Encaja para diversificar por tamaño asumiendo más volatilidad. La evidencia es consistente y casi idéntica a la de la clase USD del mismo fondo. TER bajo (0,30 %; gestión 0,29 %). Frente a su categoría VDOS se mantiene en **quintil 2–3 todos los años**: 2026 quinti …

**Pegas detectadas.**
- Mínimo inicial de folleto de 1.000.000 EUR (clase institucional); verificar cómo se comercializa en MyInvestor.
- Volatilidad 1A en quintil 4 (12,67 %): más volátil que la media de su categoría.
- Small-cap más sensible al coste de financiación y al ciclo con tipos al alza.
- Divisas subyacentes de la cartera sin cubrir (aunque la clase sea EUR).
- Rating VDOS (3 ★) distinto del Morningstar del snapshot (4 ★): sistemas diferentes.
- Composición de cartera no disponible (pestaña Finect en JS): campos Pendiente.
- El YTD 2026 del snippet de Finect (+18,70 %) difiere del snapshot (17,29 %) y de quefondos (17,10 %); manda el snapshot.

**Decisión.** MCP TER 0.29 vs snapshot 0.30; manda snapshot

### Fidelity MSCI Emerging Markets Index Fund P-ACC-EUR — `IE00BYX5M476`

**Identidad y operativa.** FIL Investments International (Fidelity) · clase `rv-emergentes` · fuente `listado-app` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Emergentes indexado. Importe: 12.000 €. Ficha: `finance/fondos-myinvestor/rv-emergentes/IE00BYX5M476.md`.

**Coste y mínimos.** TER snapshot **0,20 %** (0,20 % (snapshot app)); gestión 0,20 % (quefondos y Finect); éxito no (Finect: n/a; variable 0,00 % en quefondos); mínimo publicado "0,00 EUR (quefondos)"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 8.204.

**Exposición y evidencia.** RV 99,03 % · RF 0,00 % · 3A 16,95 % · 5A 6,12 % · SRRI 4. Patrimonio: Patrimonio de la clase: 118,1 M€.

**Regiones.** Taiwán 24,50 %, China 22,80 %, Corea del Sur 18,50 %, India 11,80 %, Brasil 4,60 %, Sudáfrica 3,20 %, Arabia Saudí 2,60 %, México 1,80 %, EAU 1,20 %, Malasia 1,10 %, otros 6,70 % (factsheet Fidelity 30/04/2026).

**Sectores.** Tecnología 36,30 %, Financiero 19,40 %, Consumo discrecional 9,30 %, Industrial 7,40 %, Comunicación 6,80 %, Materiales 6,50 %, Energía 3,90 %, Consumo básico 3,20 %, Salud 2,70 %, Utilities 2,20 %, Inmobiliario 1,10 % (factsheet Fidelity 30/04/2026).

**Quién es y para qué sirve.** Fondo indexado (ICAV domiciliada en Irlanda, subfondo de Fidelity UCITS II ICAV) que replica físicamente el MSCI Emerging Markets Index (Net), que cubre empresas de gran y mediana capitalización de países emergentes según criterios de tamaño, liquidez y free float de MSCI. La política busca seguir el índice lo más cerca posible minimizando el tracking error, antes de comisiones y gastos. Clase de acumulación en EUR (divisa base del fondo: USD), constituida el 20/03/2018. Patrimonio de la clase: 118,1 M€ (Finect, 18/11/2026); patrimonio del fondo: 137,0 M€. SFDR artículo 6; réplica física con 1.187 posiciones según el factsheet de 31/10/2026.

**Lectura para cartera (texto de la ficha).** Papel de satélite de renta variable emergente (o núcleo del bloque emergente dentro de una cartera indexada global): da exposición diversificada a ~1.200 empresas de emergentes con un solo producto. Encaja en perfiles con horizonte largo que toleran volatilidad alta y divisa sin cubrir; no es un fondo defensivo ni de liquidez. La evidencia es la de un indexado barato y fiel a su mercado: TER 0,20 % (snapshot), de los más bajos del lote, sin comisiones de suscripción ni reembolso. Frente a la categoría VDOS «RVI Emergentes» queda en quintil 2 en 2022 (-15,25 % vs -19,10 % de la categoría) y 202 …

**Pegas detectadas.**
- SRRI discrepante: snapshot 4, Finect 5/7, KID oficial 4/7. Manda el snapshot (4).
- quefondos a 16/11/2026 marca YTD 2026 del 16,37 % frente al 14,95 % del snapshot (19/11): fechas distintas tras caídas recientes (-4,89 % en 1 mes); manda el snapshot.
- Concentración: TSMC 14 % y sector tecnología 36,3 %; China 22,8 % (riesgo geopolítico/regulatorio).
- Divisa: clase EUR sin cubrir sobre cartera con divisa base USD y divisas emergentes; el efecto divisa entra en la rentabilidad.
- Composición del factsheet a 30/04/2026 (la URL «current» sirvió la versión de abril); el snippet del factsheet de 31/10/2026 confirma patrimonio y 1.187 posiciones, pero no el desglose.
- Finect no renderiza composición (JS); asset allocation tomado del snippet de búsqueda de FT (misma consulta), anotado.
- Rentabilidades anuales del factsheet (2022: -15,0 %; 2023: 5,5 %; 2024: 14,4 %; 2025: 17,7 %) difieren en décimas de las de quefondos por proveedor/metodología; la tabla usa quefondos.

**Decisión.** Fidelity P-ACC-EUR

### Fidelity MSCI Europe Index Fund EUR P Acc — `IE00BYX5MD61`

**Identidad y operativa.** FIDELITY UCITS II ICAV · clase `rv-europa` · fuente `mcp` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Europa indexado. Importe: 10.000 €. Ficha: `finance/fondos-myinvestor/rv-europa/IE00BYX5MD61.md`.

**Coste y mínimos.** TER snapshot **0,10 %** (0,10 %); gestión 0,10 %; éxito —; mínimo publicado "1.00 EUR"; mínimo operativo verificado: **web ficha: 1.00 EUR**. NAV 10.968.

**Exposición y evidencia.** RV 99,30 % · RF 0,00 % · 3A 15,22 % · 5A 8,96 % · vol 10,04 % · SRRI 4. Patrimonio: Pendiente.

**Regiones.** Reino Unido (21,6 %), Suiza (15,7 %), Alemania (13,7 %), Francia (13,2 %), Países Bajos (8,8 %), España (5,9 %)

**Sectores.** Servicios financieros (24,0 %), Industria (18,1 %), Salud (14,0 %), Consumo defensivo (9,1 %), Tecnología (8,6 %), Consumo cíclico (5,9 %)

**Quién es y para qué sirve.** Fondo de renta variable con foco en Europa, de gestión activa, comercializado en MyInvestor en clase de acumulación (EUR). Fecha de lanzamiento de la clase: 2018-03-20. > Seguir el comportamiento del índice MSCI Europe. Este índice agrupa más de 350 empresas de gran y mediana capitalización de 15 países desarrollados europeos (Reino Unido, Francia, Suiza, Alemania, Países Bajos, etc.), cubriendo aproximadamente el 85% de la capitalización del mercado europeo.

**Lectura para cartera (texto de la ficha).** Exposición regional a la bolsa europea. Útil para sesgar la cartera hacia Europa frente a un núcleo global; concentra riesgo regional y divisa EUR. *Orientación general derivada de la clasificación del catálogo; no es una recomendación de inversión.*

**Decisión.** Fidelity P Acc EUR

### Fidelity MSCI Japan Index Fund P-ACC-EUR (hedged) — `IE00BYX5NH74`

**Identidad y operativa.** FIL Investment Management (Luxembourg) S.A., Ireland Branch · clase `rv-japon` · fuente `listado-app` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Japón indexado cubierto EUR. Importe: 5.000 €. Ficha: `finance/fondos-myinvestor/rv-japon/IE00BYX5NH74.md`.

**Coste y mínimos.** TER snapshot **0,20 %** (0,20 % (snapshot app); factsheet de la clase: 0,15 %; Finect/quefondos: 0,20 %); gestión 0,20 % (Finect y quefondos); éxito no (Finect: n/a; quefondos variable 0,00 %); mínimo publicado "0,00 EUR (quefondos)"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 13.658.

**Exposición y evidencia.** RV 100,00 % · RF 0,00 % · 3A 20,14 % · 5A 16,30 % · SRRI 5. Patrimonio: Pendiente.

**Regiones.** Japón 100,2 %.

**Sectores.** Industrials 24,00 %; Financials 18,90 %; Information Technology 17,40 %; Consumer Discretionary 15,20 %; Communication Services 6,50 %; Health Care 5,80 %; Consumer Staples 3,80 %; Materials 3,60 %; Real Estate 1,90 %; Energy 1,00 %; Utilities 1,00 %.

**Quién es y para qué sirve.** Subfondo indexado de Fidelity (ICAV irlandés, Fidelity UCITS II ICAV) que busca replicar, antes de comisiones y gastos, el rendimiento del MSCI Japan Index: empresas de gran y mediana capitalización de Japón que cubren aproximadamente el 85 % del mercado negociado públicamente, según los criterios de tamaño, liquidez y free float de MSCI. Réplica física (mantener las acciones del índice) minimizando el tracking error; la clase P-ACC-EUR (H) acumula dividendos y cubre la divisa a EUR, eliminando la exposición al yen. Constituido el 20/03/2018. Patrimonio del fondo: 560,2 M USD; de esta clase: 143,6 M EUR (factsheet 31/10/2026; quefondos a 28/10/2026: 144,4 M EUR).

**Lectura para cartera (texto de la ficha).** Satélite de renta variable japonesa para quien ya tiene un núcleo global y quiere exposición específica a Japón sin riesgo de divisa: la cobertura a EUR elimina el yen de la ecuación (a cambio de renunciar a posibles ganancias por divisa y asumir el coste de la cobertura). Encaja en perfiles que aceptan volatilidad de bolsa desarrollada de un solo mercado y horizonte largo; no es un fondo defensivo ni de liquidez. La evidencia es sólida en horizontes largos: en la categoría RVI JAPÓN de VDOS, quintil 1 en rentabilidad acumulada a 3 años (94,39 %, ranking 99/648) y a 5 años (127,86 %, ranking 8 …

**Pegas detectadas.**
- Caché de quefondos: la fuente sirvió dos versiones distintas en la misma sesión: una a 28/10/2026 (usada para rentabilidades, rankings, NAV y patrimonio) y otra más antigua a 13/05/2026 (de la que solo se tomaron las com
- TER discrepante: snapshot y Finect/quefondos 0,20 %; el factsheet oficial de la clase (31/10/2026) declara ongoing charges 0,15 %. Manda el snapshot (0,20 %); posible diferencia entre ongoing charges de clase y TER publi
- SRRI discrepante: snapshot 5; Finect 6/7. Manda el snapshot.
- YTD web vs snapshot: quefondos 19,93 % a 28/10/2026 y Finect 17,51 % a 13/11/2026 frente a 13,89 % del snapshot (19/11/2026): caída de la bolsa japonesa en noviembre; manda el snapshot.
- Clase con divisa cubierta: la cobertura reduce el riesgo yen pero limita ganancias por divisa y tiene coste implícito; los rankings VDOS de esta clase ya están en EUR cubierto (sin efecto divisa adicional).
- Concentración geográfica total en Japón y peso relevante de financieras y semiconductores en el top 10.
- Finect no renderiza composición (JS): la composición se tomó del factsheet oficial de Fidelity a 31/10/2026; los datos de ficha de Finect proceden del snippet de búsqueda de su propia URL (anotado).

**Decisión.** factsheet 0.15 vs snapshot 0.20; manda snapshot

### Vanguard Pacific ex-Japan Stock Index Fund EUR Acc — `IE0007201266`

**Identidad y operativa.** Vanguard Group (Ireland) Limited · clase `rv-otros` · fuente `listado-app` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Pacífico ex-Japón indexado. Importe: 3.000 €. Ficha: `finance/fondos-myinvestor/rv-otros/IE0007201266.md`.

**Coste y mínimos.** TER snapshot **0,16 %** (0,16 % (snapshot app); OCF factsheet oficial 0,16 %; gastos corrientes Finect 0,160 %); gestión 0,16 % (quefondos «fija»; Finect 0,160 %); éxito 0,00 % (quefondos «variable»); n/a (Finect); mínimo publicado "1.000.000,00 EUR (quefondos y factsheet); operativa real en MyInvestor: Pendiente"; mínimo operativo verificado: **MCP 20/11: 1.00 EUR**. NAV 372.716.

**Exposición y evidencia.** RV 100,00 % · RF 0,00 % · 3A 13,85 % · 5A 6,68 % · SRRI 4. Patrimonio: Patrimonio de la clase: **369 M€.

**Sectores.** Financieras (46,1 %), Materiales (15,9 %), Industriales (9,3 %), Inmobiliario (6,5 %), Consumo discrecional (6,2 %), Salud (4,2 %), Utilities (3,3 %), Consumo básico (3,0 %), Energía (2,8 %), Servicios de comunicación (2,2 %), Tecnología (0,5 %).

**Quién es y para qué sirve.** Fondo de gestión pasiva que busca crecer a largo plazo replicando el **MSCI Pacific ex Japan Index** (large y mid cap de mercados desarrollados del Pacífico sin Japón): invierte en todos los componentes en su misma proporción y, si no es factible, usa muestreo; permanece plenamente invertido salvo condiciones extraordinarias (quefondos y factsheet oficial). Clase EUR Acc lanzada el **27/02/2014** (factsheet y Finect; quefondos dice 28/02/2014, ver Pegas). Patrimonio de la clase: **369 M€** a 30/09/2026 (factsheet oficial) / 381,3 M€ (Finect); fondo: 3.398 M€ (factsheet 30/09) / 3.579,9 M€ (Finect). Categoría VDOS: **RVI ASIA EX-JAPÓN**; Morningstar: Pacific ex-Japan Equity (snapshot y Finect). Indexado: sí (Finect). **SFDR Artículo 6** (Wealins). El factsheet se marca «solo para inversores profesionales» (MiFID II) como material de marketing; mínimo de folleto de la clase 1.000.000 €.

**Lectura para cartera (texto de la ficha).** Papel de **satélite de renta variable desarrollada Asia-Pacífico ex-Japón**, casi idéntico en exposición al iShares Pacific Index (mismo índice MSCI): 62,5 % Australia, 46,1 % financieras, 15,9 % materiales y 0,5 % tecnología. Diversificador regional y de estilo (value/cíclico, dividendo 3,4 % reinvertido) frente a un núcleo global o USA, a coste de indexado (TER 0,16 %). Clase EUR sin cobertura: expone a AUD, SGD, HKD y NZD. Es la clase «General» (mínimo de folleto 1 M€), no la Institutional Plus. La evidencia en la clase EUR (quefondos a 17/11/2026) replica el patrón del índice: **quintil 1 …

**Pegas detectadas.**
- Caché de quefondos: la primera extracción sirvió datos a 22/10/2026 (YTD 16,18 %, NAV 373,5555); la segunda, a 17/11/2026 (YTD 15,92 %, NAV 372,7161). Se usa la versión del 17/11, más cercana al snapshot.
- YTD muy divergente entre fuentes: snapshot 15,36 % (19/11) vs quefondos 15,92 % (17/11) vs Finect +17,84 % (snippet) / +14,43 % (extracto) vs factsheet 15,25 % (30/09) vs Wealins 16,30 % (20/10). Fechas y bases distintas
- Fecha de constitución discrepante: quefondos 28/02/2014 vs factsheet oficial y Finect 27/02/2014. Se usa la del factsheet.
- VDOS 1 estrella vs Morningstar 3★ (snapshot): VDOS penaliza el quintil 5 de 2025 y la volatilidad relativa en la serie EUR; no mezclar metodologías.
- Efecto divisa en la serie EUR: quintil 1 de 2022 y quintil 5 de 2025 se explican en gran parte por EUR/USD; la comparación vs categoría VDOS mezcla clases de distintas divisas.
- Volatilidad 1A por encima de sus pares (13,30 %, quintil 5 de la categoría).
- Concentración: Australia 62,5 %, financieras 46,1 %, top 10 ~48,2 %; tecnología 0,5 % (no captura rallys growth).
- Mínimo de folleto 1.000.000 € y factsheet «solo profesionales»; mínimo real de MyInvestor no publicado en la web.
- Divisa sin cubrir: clase EUR con subyacentes AUD/SGD/HKD/NZD; el factsheet avisa de riesgo de tipo de cambio.
- Swing pricing: el NAV puede oscilar por suscripciones/reembolsos, añadiendo tracking difference vs el índice (factsheet).
- Patrimonio del fondo divergente por fecha: 3.398 M€ (factsheet 30/09) vs 3.579,9 M€ (Finect); quefondos no publica patrimonio («·»).
- SRRI 4 coincide en snapshot, Finect y factsheet. SFDR Artículo 6 según Wealins (el factsheet no lo declara). Finect no renderiza composición; se usa el factsheet oficial de esta clase exacta (30/09/2026).

**Decisión.** Australia 62%

### iShares Global Aggregate 1-5 Year bond Index Fund EUR Hedged — `IE0004ZP1ND3`

**Identidad y operativa.** BlackRock Asset Management Ireland Limited · clase `renta-fija` · fuente `listado-app` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Agregado global 1-5 años cubierto EUR. Importe: 12.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/IE0004ZP1ND3.md`.

**Coste y mínimos.** TER snapshot **0,08 %** (0,08 % (snapshot app; OCF 0,08 % en iShares; gastos corrientes 0,080 % en Finect)); gestión 0,07 % (iShares, clase S); Finect publica 0,350 % (probablemente el de la clase D; se anota la discrepancia); éxito No (iShares «-»; Finect «n/a»); mínimo publicado "200.000.000 EUR (iShares y Finect, clase S); mínimo posterior 5.000 EUR (iShares)"; mínimo operativo verificado: **MCP 20/11: 0.00 EUR**. NAV 10.087.

**Exposición y evidencia.** RV 0,00 % · RF 98,90 % · duración estimada 2.8 · 3A Pendiente · 5A Pendiente · SRRI 2. Patrimonio: Pendiente.

**Regiones.** Pendiente en desglose por país (iShares no lo publicó en el extracto); las mayores posiciones son deuda de China, EE. UU. y Japón (ver abajo).

**Sectores.** Treasury 56,78 %, Corporates 21,18 %, Government Related 16,51 %, Covered 3,33 %, Securitized 1,47 %, caja/derivados 0,74 % (iShares, 30/10/2026).

**Quién es y para qué sirve.** Fondo indexado UCITS (Irlanda, BlackRock Fixed Income Dublin Funds Plc) que busca replicar la rentabilidad del Bloomberg Global Aggregate 1-5 Year Index invirtiendo, en la medida de lo posible y practicable, en los bonos que lo componen: deuda gubernamental, organismos relacionados, corporativa y titulizada global con vencimientos de 1 a 5 años y calidad investment grade en el momento de compra (factsheet de iShares). Clase S con cobertura de divisa a EUR y acumulación («Use of Income: Accumulating», iShares). El fondo nació el 14/12/2017; esta clase S EUR Hedged arrancó el 21/08/2025 (iShares; Finect la fecha el 20/08/2025). Patrimonio: 1.553,1 M USD el fondo (iShares, 18/11/2026; Finect 1.412,4 M€) y ~28,2-28,9 M€ la clase (Finect 28,2 M€; iShares 28.852.041 €). 4.345 posiciones (iShares, 30/10/2026). SFDR: «Other» (no Artículo 8/9). Morningstar Medalist Rating: Bronze (30/09/2026, iSh …

**Lectura para cartera (texto de la ficha).** Tramo defensivo/núcleo de renta fija: exposición global diversificada (miles de bonos, gobiernos + corporativo IG) a plazo corto-medio (duración ~2,7 años) con divisa cubierta a EUR, pensada como lastre estable de una cartera con RV. Encaja en perfiles conservadores o como contrapeso de bajo coste en cualquier cartera; la propia prensa de Finect lo cita como el fondo de renta fija global corto para perfiles conservadores dentro de la oferta indexada de MyInvestor. La evidencia es de coste y diversificación, no de historial: TER 0,08 % (snapshot, iShares y Finect coinciden), de los más bajos de …

**Pegas detectadas.**
- Historial de la clase S <3 años (21/08/2025): sin 3A, 5A, años naturales ni rating de estrellas; no extrapolar el historial del fondo matriz (2017) a esta clase.
- Mínimo inicial publicado de 200.000.000 € (clase S institucional): comprobar cómo lo comercializa MyInvestor para minoristas.
- Comisión de gestión: iShares 0,07 % vs Finect 0,350 % (Finect parece arrastrar el fee de otra clase; el TER 0,08 % sí coincide en las tres fuentes).
- SRRI: snapshot 2 vs Finect 3/7; se anotan ambos.
- quefondos no tiene el fondo (fuente principal caída para este ISIN); datos web tomados de Finect y de la gestora (iShares/BlackRock).
- Fecha de inicio de clase: 20/08/2025 (Finect) vs 21/08/2025 (iShares); se cita agosto de 2025.
- Rentabilidad trailing baja (1A 0,28 %) pese a YTM 3,87 %: el período de subidas de tipos ha lastrado el precio; el carry no es rentabilidad garantizada.
- Sin desglose regional publicado en las fuentes consultadas (Pendiente).

**Decisión.** clase S del mismo fondo que D Acc (0.17); se elige la barata operable

### Amundi Core Euro Government Bond AE-C (Amundi IS JP Morgan EMU Govies AE-C) — `LU1050470373`

**Identidad y operativa.** Amundi (Amundi Luxembourg SA / Amundi Asset Management) · clase `renta-fija` · fuente `listado-app` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Gubernamental euro indexado. Importe: 6.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/LU1050470373.md`.

**Coste y mínimos.** TER snapshot **0,35 %** (0,35 % (snapshot app; gastos corrientes Finect 0,350 %)); gestión 0,200 % (Finect; fija 0,20 % en quefondos); éxito no (n/a en Finect; variable 0,00 % en quefondos); mínimo publicado "0,00 USD (quefondos)"; mínimo operativo verificado: **MCP 20/11: 0.00 participaciones**. NAV 104.46.

**Exposición y evidencia.** RV 0,00 % · RF 100,00 % · duración estimada 7.0 · 3A 1,25 % · 5A -3,00 % · SRRI 3. Patrimonio: 1.742,5 M€.

**Regiones.** Pendiente (no publicado; el índice cubre los soberanos de la unión monetaria: Alemania, Francia, Italia, España, etc., según la política del índice).

**Sectores.** Pendiente (por política, 100 % deuda pública de la UEM).

**Quién es y para qué sirve.** Subfondo indexado de Amundi Index Solutions que replica el **Bloomberg Euro Treasury 50bn Bond Index**: obligaciones públicas con grado de inversión y tipo fijo emitidas por los países soberanos de la **Unión Monetaria Europea**, minimizando el tracking error. En la app de MyInvestor figura con el nombre antiguo «Amundi IS JP Morgan EMU Govies AE-C»; las fuentes actuales (quefondos y Finect) lo nombran **Amundi Core Euro Government Bond AE Acc** y citan el índice Bloomberg, no JP Morgan. Clase AE-C de acumulación. Constituido el **14/04/2014**. Patrimonio del fondo: 1.742,5 M€; de la clase: 18,9 M€ (Finect, datos a 20/10/2026); quefondos cifra la clase en 19.158,38 miles de euros a 04/11/2026. Categoría VDOS: Deuda Pública Euro; Finect: RF Deuda Pública EUR.

**Lectura para cartera (texto de la ficha).** Núcleo defensivo de renta fija soberana en euros: deuda pública de la UEM sin riesgo divisa para el inversor europeo, el «colchón» clásico frente a la bolsa en carteras indexadas. A diferencia del global cubierto del lote (Amundi GBI Global), aquí no hay coste de cobertura ni riesgo de divisa, pero sí concentración en los emisores de la unión monetaria (con el riesgo de diferencial italiano/francés implícito). Papel defensivo para perfiles moderados y conservadores. La evidencia es de una mediocridad muy consistente: quefondos la sitúa en **quintil 3 en los cinco años naturales (2022–2026) y e …

**Pegas detectadas.**
- Nombre desactualizado en el snapshot de la app («JP Morgan EMU Govies»): el índice actual es el Bloomberg Euro Treasury 50bn Bond Index según quefondos y Finect.
- Deuda pública de duración: 2022 −18,25 % y 5 años en negativo (−3,00 % anualizada, snapshot); en el escenario de tipos al alza es el tramo que sufre.
- Desempeño sistemáticamente en la mediana de su categoría (quintil 3 en todos los años y acumulados publicados): no aporta valor añadido sobre el índice más allá de la réplica.
- Datos de quefondos a 04/11/2026 (desactualizados respecto al snapshot); primera extracción de Finect con datos a 20/10/2026.
- SRRI del snapshot (3) difiere del «Riesgo 4/7» de Finect.
- Composición no disponible: las dos extracciones de Finect devolvieron solo el bloque de comisiones (Pendiente).
- Versiones ETF del mismo fondo con gestión 0,04–0,10 % (tabla de clases de Finect) frente al 0,20 % de esta clase.

**Decisión.** duración ~7 estimada (2022 −18.25%); Amundi Prime IE-C descartado por mínimo 500.000

### Vanguard Eurozone Inflation-Linked Bond Index Fund EUR Acc — `IE00B04GQR24`

**Identidad y operativa.** Vanguard Group (Ireland) Limited · clase `renta-fija` · fuente `listado-app` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Ligado a inflación euro indexado. Importe: 4.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/IE00B04GQR24.md`.

**Coste y mínimos.** TER snapshot **0,12 %** (0,12 % (snapshot app)); gestión 0,12 % (quefondos «fija»; Finect 0,120 %); éxito no (0,00 % variable en quefondos; n/a en Finect); mínimo publicado "1.000.000,00 EUR (mínimo oficial publicado en quefondos)"; mínimo operativo verificado: **MCP 20/11: 1.00 EUR**. NAV 136.731.

**Exposición y evidencia.** RV 0,00 % · RF 100,00 % · duración estimada 7.0 · 3A 1,63 % · 5A -0,90 % · SRRI 3. Patrimonio: patrimonio del fondo **1.682,1 M€.

**Regiones.** Pendiente (por política, bonos soberanos de la zona euro)

**Sectores.** Pendiente

**Quién es y para qué sirve.** Fondo indexado que replica el índice **Bloomberg Global Inflation-Linked: Eurozone – Euro CPI Index**: bonos gubernamentales de la zona euro vinculados a la inflación, denominados en euros y con vencimiento superior a un año, todos con grado de inversión como mínimo. Replica por muestreo representativo y se mantiene plenamente invertido salvo condiciones extraordinarias. Esta es la clase «EUR Acc» (quefondos la denomina «General EUR Cap»), constituida el **31/05/2005**; patrimonio del fondo **1.682,1 M€** y de esta clase **630,0 M€** según Finect. Es la clase principal del mismo fondo cuya clase Investor figura en el lote como IE00B04GQQ17 (rentabilidades trailing idénticas en el snapshot).

**Lectura para cartera (texto de la ficha).** Papel de **cobertura de inflación** dentro del bloque de renta fija: satélite defensivo para proteger poder adquisitivo frente a sorpresas inflacionarias en la eurozona. Soberano y en euros: sin riesgo de divisa ni crédito corporativo relevante. Al ser la clase principal (630,0 M€), es la vía más líquida y extendida de acceder a este índice. Evidencia consistente frente a su categoría VDOS «RF Euro ligada a la inflación»: **quintil 1 en 2023** (6,36 %, ranking 4/70, vs 4,63 % de la categoría) y **quintil 2 en 2024, 2025 y 2026 YTD**. En 2022 cayó -10,33 % (quintil 4), peor que la categoría (-7 …

**Pegas detectadas.**
- Duración larga: en 2022 cayó -10,33 %, peor que su categoría; sensible a subidas de tipos reales.
- El lote incluye otra clase del mismo fondo (IE00B04GQQ17, Investor EUR Acc) con rentabilidades idénticas en el snapshot: son la misma exposición, no diversificación.
- Mínimo oficial publicado de 1.000.000 €; comprobar el mínimo real aplicado por MyInvestor.
- Finect no publica composición de cartera ni Sharpe/máxima caída para este fondo; composición Pendiente.
- Datos web de quefondos a 17/11/2026 y de Finect a 13/11/2026 (snippet); el snapshot (19/11/2026) manda en NAV y rentabilidades trailing.

**Decisión.** Italia 38 Francia 34; duración larga estimada

## C2 — 10 fondos

### Robeco BP Global Premium Equities D EUR (Acc) — `LU0203975437`

**Identidad y operativa.** Robeco Institutional Asset Management B.V. · clase `rv-global` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Núcleo RV global value activo. Importe: 20.000 €. Ficha: `finance/fondos-myinvestor/rv-global/LU0203975437.md`.

**Coste y mínimos.** TER snapshot **1,46 %** (1,46 % (snapshot app; Finect: gastos corrientes 1,460 %)); gestión 1,25 % (quefondos «Fija»; Finect: 1,250 %); éxito 0,00 % (quefondos «Variable»; Finect: n/a); mínimo publicado "0,00 EUR (quefondos)"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 632.1.

**Exposición y evidencia.** RV 98,34 % · RF 0,00 % · 3A 18,34 % · 5A 11,89 % · SRRI 4. Patrimonio: 9.322 M€.

**Regiones.** EE. UU. 44,01 % · Zona Euro 28,06 % · Reino Unido 12,07 % · Japón 6,10 % · Europa ex-Zona Euro 5,63 % · Asia desarrollada 1,78 % · Iberoamérica 0,66 %

**Sectores.** Servicios financieros 26,15 % · Salud 15,86 % · Industrial 13,09 % · Energía 9,85 % · Tecnología 9,83 % · Consumo defensivo 6,53 % · Consumo cíclico 5,89 % · Materiales básicos 5,79 % · Comunicación 4,16 % · Utilities 1,15 %

**Quién es y para qué sirve.** Clase D de acumulación del subfondo UCITS **Robeco BP Global Premium Equities** (constituido el 21/05/2001 según quefondos; clase D desde el 13/12/2004 según Robeco/Finect). Estrategia (quefondos/Robeco): fondo global **all-cap value** sin restricciones, al menos dos tercios del patrimonio en acciones de empresas de todo el mundo (principalmente desarrolladas), seleccionadas por análisis fundamental con valoración atractiva, sólidos fundamentos y mejor impulso («Valuation, Fundamentals, Momentum»). **Benchmark: MSCI World Index (Net Return, EUR)**. El KID de Robeco (snippet, 30/04/2026) lo clasifica **SFDR Artículo 8**, sin política activa de divisa (la exposición viene de la selección de valores), negociación diaria y horizonte recomendado de 5 años. Categoría VDOS: RVI GLOBAL; Finect: RV Global Cap. Grande Value. Patrimonio del fondo: 9.322 M€ (quefondos, 18/11/2026); clase D: 3.107,4 …

**Lectura para cartera (texto de la ficha).** Papel de **núcleo o satélite grande de renta variable global value en euros y de acumulación**: la clase D reinvierte los dividendos sin fricción fiscal, con la misma cartera diversificada del fondo (112 posiciones según factsheet de la clase B, top 10 ~15 %), sesgo a financieras (26 %), salud (16 %) e industriales (13 %), y peso relevante en medianas (41 %). Encaja como contrapeso value a un núcleo global growth/indexado, para perfiles en fase de acumulación con horizonte ≥5 años (el KID recomienda 5 años). La evidencia es sólida frente a su categoría. Snapshot: YTD +16,76 %, 1A +21,07 %, 3A …

**Pegas detectadas.**
- Comisión de depósito discrepante: quefondos 0,00 % vs Finect 0,500 % (custodia). Se anotan ambas; el TER del snapshot (1,46 %) coincide con los gastos corrientes de Finect.
- Alpha negativo vs benchmark: -1,68 a 3A y -0,64 a 5A (Finect): por detrás del MSCI World en el período, aunque quintil 1 vs su categoría de fondos.
- Rezago en rallies growth: 2023 y 2024 en quintil 4 vs categoría VDOS.
- Comisión de suscripción de hasta 5,00 % en la clase; verificar la aplicada por MyInvestor.
- Divisas sin cubrir (USD 44 %, GBP 12 %, JPY 6 %); el KID confirma ausencia de política activa de divisa.
- Concentración sectorial en financieras (26,15 %): sensibilidad a curva de tipos y morosidad.
- Fechas de quefondos: la versión escritorio servía caché del 05/11/2026; se usó la móvil (18/11/2026) para YTD/rankings/1A/3A; el 2022 y el 5A acumulado citados provienen de la escritorio (fechas anotadas). El YTD del sna
- El snippet de Keytrade Bank muestra «ongoing charges 1,90 %» y patrimonio 5.100 M€ (datos de otro distribuidor/fecha, con distribution fee propia); no se usan.
- Fechas de constitución distintas: fondo 21/05/2001 (quefondos) vs clase D 13/12/2004 (Robeco/Finect).

**Decisión.** Robeco BP; prima value 0.5pp declarada como apuesta

### Fundsmith Equity Fund T EUR Acc — `LU0690375182`

**Identidad y operativa.** Fundsmith Investment Services Limited (gestora de la SICAV: Fundrock Management, Apex Group) · clase `rv-global` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV global calidad activo. Importe: 12.000 €. Ficha: `finance/fondos-myinvestor/rv-global/LU0690375182.md`.

**Coste y mínimos.** TER snapshot **1,08 %** (1,08 % (snapshot app; Finect: OGC 1,08 %, TER 1,09 %)); gestión 1,00 % (quefondos «fija»; Finect 1,00 %); éxito 0,00 % (variable, quefondos); mínimo publicado "2.000,00 EUR (quefondos); Finect: mínimo de clase 1.000 € (texto genérico «Mínimo: 0 €») — discrepancia, ver Pegas"; mínimo operativo verificado: **web ficha: 2.000 EUR (Finect 1.000)**. NAV 67.024.

**Exposición y evidencia.** RV 100,00 % · RF 0,00 % · 3A 7,00 % · 5A 2,51 % · SRRI 4. Patrimonio: Pendiente.

**Regiones.** Estados Unidos 79,58 %; Zona Euro 12,97 %; Reino Unido 3,89 %; Asia desarrollada 3,56 % (100 % países desarrollados).

**Sectores.** Tecnología 32,24 %; Salud 17,89 %; Consumo defensivo 15,17 %; Servicios financieros 11,09 %; Servicios de comunicación 9,84 %; Consumo cíclico 9,52 %; Industrial 4,24 %.

**Quién es y para qué sirve.** Clase T en EUR de acumulación del Fundsmith Equity Fund de la SICAV luxemburguesa Fundsmith. Es un feeder: invierte prácticamente todos sus activos en el Fundsmith Equity Fund británico, OICVM principal regulado por la FCA del Reino Unido, que solo mantiene una pequeña cantidad de efectivo para liquidez (quefondos). Objetivo: crecimiento del valor a largo plazo mediante acciones globales, con enfoque de inversor a largo plazo en las posiciones seleccionadas y sin estrategias de trading a corto plazo. Referencia: MSCI World Index (quefondos). Constituido el 2011-11-02 (~15 años de historial). Patrimonio de la clase: 558.012,95 miles de euros (≈558 M€) según quefondos a 2026-11-17; Finect cifra la clase T EUR Acc en 537,98 M€ y el fondo conjunto en 4.396,6 M€. Categoría VDOS: RVI Global; Morningstar/Finect: RV Global Cap. Grande Growth. La cobertura de divisa de la clase EUR no consta en l …

**Lectura para cartera (texto de la ficha).** Núcleo activo de renta variable global quality growth, o satélite de convicción para quien crea en la selección de valores de Fundsmith: cartera concentrada (top 10 = 49,41 %), 100 % desarrollados y ~80 % EE. UU., con tecnología (32 %), salud (18 %) y consumo defensivo (15 %) como pilares. No es un indexado: el objetivo es batir al MSCI World a largo plazo comprando buenas empresas y manteniéndolas, sin trading. SRRI 4 y volatilidad 1A del 13,63 % (quintil 2 de volatilidad = de las más altas de su categoría VDOS): perfil de riesgo medio-alto dentro de la RV global, para horizonte largo. La evi …

**Pegas detectadas.**
- Rentabilidad relativa floja en el ciclo reciente: quintil 5 en 2025 y 3A, quintil 4 en 2024 y 5A vs la categoría VDOS RVI Global; alpha -3,96 a 36M (Finect). El buen momentum de 1/3 meses (quintil 1) no compensa aún el r
- Concentración: top 10 = 49,41 % de la cartera; ~80 % EE. UU.; tecnología 32 %. Un solo gestor/estilo (quality growth) sin diversificación de enfoque.
- Divisa: clase EUR sobre activos mayoritariamente USD; la cobertura de divisa no consta en las fuentes consultadas (ni quefondos ni Finect la mencionan): riesgo EUR/USD no documentado.
- TER 1,08 % (snapshot) frente a 1,09 % TER / 1,08 % OGC de Finect y fija 1,00 % + depósito 0,01 % de quefondos: discrepancias menores entre fuentes.
- Mínimo inicial discrepante: quefondos 2.000 EUR vs Finect clase 1.000 € (texto genérico 0 €).
- Rating Morningstar: snapshot 3 ★ vs Finect 2 ★; VDOS solo 1 estrella. Escalas y fechas distintas; manda el snapshot.
- NAV: quefondos 67,703900 (2026-11-17) y Finect 67,2332 (2026-11-19) difieren del snapshot 67,024 (2026-11-19); manda el snapshot.
- Patrimonio: quefondos ≈558 M€ (clase, 2026-11-17) vs Finect 537,98 M€ (clase) y 4.396,6 M€ (fondo conjunto): cifras y fechas distintas.
- Estructura feeder: la SICAV luxemburguesa invierte casi todo en el fondo británico master; el texto de estrategia de Finect es genérico y cita otro ISIN (LU0690374615, clase distinta del mismo fondo); los datos usados so
- Descripción de Finect desactualizada («Riesgo 6/7», rentabilidad 2021 +28,27 % como reclamo): el SRRI vigente es 4.
- Volatilidad 1A en quintil 2 (de las más altas de la categoría) pese al perfil «quality»: no es un fondo defensivo.

**Decisión.** Fundsmith; 3A 7.0 / 2025 Q5 — proceso quality, bache reciente escrito

### Guinness Global Equity Income D EUR Accumulation — `IE00BDGV0290`

**Identidad y operativa.** Guinness Asset Management Limited · clase `rv-global` · fuente `mcp` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV global dividendo creciente activo. Importe: 10.000 €. Ficha: `finance/fondos-myinvestor/rv-global/IE00BDGV0290.md`.

**Coste y mínimos.** TER snapshot **1,27 %** (1,27 %); gestión 1,00 %; éxito —; mínimo publicado "0.00 EUR"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 26.436.

**Exposición y evidencia.** RV 99,30 % · RF 0,00 % · 3A 13,49 % · 5A 9,03 % · vol 10,67 % · SRRI 3. Patrimonio: Pendiente.

**Regiones.** Estados Unidos (58,0 %), Reino Unido (9,9 %), Suiza (9,0 %), Francia (7,6 %), Suecia (5,4 %), Taiwán, Provincia de China (3,7 %)

**Sectores.** Industria (24,1 %), Tecnología (22,1 %), Consumo defensivo (20,8 %), Salud (15,2 %), Servicios financieros (11,9 %), Servicios de comunicación (3,0 %)

**Quién es y para qué sirve.** Fondo de renta variable con foco en Global, USA, de gestión activa, comercializado en MyInvestor en clase de acumulación (EUR). Fecha de lanzamiento de la clase: 2010-12-31.

**Lectura para cartera (texto de la ficha).** Candidato a núcleo de renta variable: exposición diversificada a la bolsa mundial en un solo fondo. La gestión activa selecciona valores dentro del universo global: puede desviarse del índice en ambos sentidos y cobra más por ello. Artículo 8 SFDR: promueve características ESG u objetivo sostenible. *Orientación general derivada de la clasificación del catálogo; no es una recomendación de inversión.*

**Decisión.** Guinness; SRRI 3

### Horos Value Internacional FI — `ES0146309002`

**Identidad y operativa.** Horos Asset Management SGIIC · clase `rv-global` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV value ibérica/small-mid activo. Importe: 8.000 €. Ficha: `finance/fondos-myinvestor/rv-global/ES0146309002.md`.

**Coste y mínimos.** TER snapshot **1,86 %** (1,86 % (snapshot app; Finect gastos corrientes 1,860 %)); gestión 1,80 % fija (quefondos; Finect 1,800 %); éxito 0,00 % variable (quefondos; Finect: n/a); mínimo publicado "100,00 EUR (quefondos); mínimo a mantener 100,00 EUR"; mínimo operativo verificado: **web ficha: 100 EUR**. NAV 216.915.

**Exposición y evidencia.** RV 90,76 % · RF 0,00 % · 3A 16,04 % · 5A 11,77 % · vol 10,75 % · SRRI 4. Patrimonio: Pendiente.

**Regiones.** Zona Euro (52,15 %), Mercado emergente (16,35 %, incluye Iberoamérica 8,85 %, África 4,24 %, Europa emergente 1,80 %, Asia emergente 1,47 %), Estados Unidos (7,21 %), Canadá (5,61 %), Europa ex-Zona Euro (3,82 %), Asia desarrollada (3,06 %), Reino Unido (2,56 %); 74,40 % países desarrollados

**Sectores.** Consumo cíclico (24,41 %), Servicios financieros (14,93 %), Servicios de comunicación (11,52 %), Industriales (10,49 %), Energía (7,64 %), Tecnología (6,88 %), Materiales básicos (5,81 %), Utilities (3,53 %), Consumo defensivo (2,38 %), Salud (1,83 %), Inmobiliario (1,33 %)

**Quién es y para qué sirve.** Fondo español de renta variable global con filosofía de inversión en valor (value investing): selecciona activos infravalorados por el mercado con alto potencial de revalorización. Al menos el 75 % de la exposición total en renta variable, sin porcentajes predeterminados por emisor, sector, país, divisa o área geográfica (puede asumir riesgo de mercados emergentes y divisas distintas del euro) y sin predeterminación de capitalización (alta, media o baja). Sin benchmark de referencia (quefondos). Constituido el 13/04/2018 (quefondos; Finect cita inicio 21/05/2018). Patrimonio: 413.915,95 miles de euros (quefondos, 18/11/2026); Finect ~399,8 M€ (sin fecha explícita). Clase única. Categoría VDOS: RVI GLOBAL VALOR; Morningstar/Finect: RV Global Cap. Pequeña (el snapshot MyInvestor lo clasifica Global Equity Mid/Small Cap).

**Lectura para cartera (texto de la ficha).** Satélite value de RV global, no núcleo: cartera muy alejada del índice mundial (R² 3A 48,16 %, tracking error ~10,5 %, solo 7 % EE. UU.), concentrada en zona euro (52 %), emergentes (16 %) y mid/small caps (~79 %), con un 9,24 % en caja. Encaja para un perfil dinámico que quiera diversificar un núcleo indexado global con una apuesta activa de valor profundo y geografías olvidadas, asumiendo que el estilo value puede quedarse años fuera de juego y que las small caps europeas/emergentes añaden riesgo de liquidez y divisa. Evidencia buena a medio plazo con bache reciente: en quefondos (RVI GLOBAL …

**Pegas detectadas.**
- TER 1,86 % (snapshot) elevado para RV global; gestión fija 1,80 % + depósito 0,08 % (quefondos). Sin comisión de éxito.
- Bache reciente: 2026 YTD en Q5 (3,56 % web vs 16,86 % categoría) y 1A en Q5; alfa 1A -12,82 e information ratio 1A -1,45 (Finect): el value profundo lleva ~1 año fuera de juego.
- Concentración geográfica: zona euro 52,15 % y emergentes 16,35 %; solo 7,21 % EE. UU. Capitalización: ~79 % mid/small/micro (Medium 43,50 %, Small 21,03 %, Micro 14,57 %): riesgo de liquidez y de ciclo en pequeñas.
- Caja 9,24 % (Finect a 30/06/2026): lastre en subidas de mercado.
- Rating discrepante: snapshot 4★ vs Finect Morningstar 3★; manda el snapshot. VDOS 4★.
- Categoría VDOS (RVI GLOBAL VALOR) ≠ categoría Morningstar (RV Global Cap. Pequeña): los rankings de quefondos lo comparan contra fondos value globales generales, no contra sus pares small cap.
- Fecha de constitución discrepante: quefondos 13/04/2018 vs Finect 21/05/2018.
- Patrimonio: quefondos 413,9 M€ (18/11/2026) vs Finect 399,8 M€ (sin fecha); el snippet de Finect citaba clase 404,8 M€ > fondo 399,8 M€ (inconsistencia de fechas de la fuente).
- Cartera de Finect a 30/06/2026: ~5 meses de antigüedad, puede haber rotado.
- quefondos escritorio sirvió datos a 11/11/2026 (una semana antes del snapshot); se usó el fallback móvil a 18/11/2026. El 2022 y el 5A acumulado se citan de la ficha de escritorio (períodos cerrados/antiguos) con su fech
- Diferencias menores snapshot vs web a 18/11/2026 (YTD 4,31 % vs 3,56 %; 1A 9,20 % vs 9,64 %; NAV 216,915 vs 215,353): un día de valoración; manda el snapshot.

**Decisión.** Horos; 2026 YTD Q5; eurozona 52%, EM 16%, USA 7%

### Man GLG Japan CoreAlpha Equity Class D H EUR — `IE00B5648R31`

**Identidad y operativa.** Man Asset Management (Ireland) Limited · clase `rv-japon` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV Japón activo cubierto EUR. Importe: 8.000 €. Ficha: `finance/fondos-myinvestor/rv-japon/IE00B5648R31.md`.

**Coste y mínimos.** TER snapshot **1,71 %** (1,71 % (snapshot app; Finect 1,710 %; FT 1,71 %)); gestión 1,50 % fija + 0,00 % variable (quefondos; Finect y FT 1,50 %); éxito Pendiente (Finect: n/a; quefondos: variable 0,00 %); mínimo publicado "1.000,00 EUR (quefondos); FT publica 833,00 GBP"; mínimo operativo verificado: **web ficha: 1.000 EUR**. NAV 540.68.

**Exposición y evidencia.** RV 98,98 % · RF 0,00 % · 3A 24,22 % · 5A 24,70 % · vol 15,03 % · SRRI 4. Patrimonio: 3.908,20 M€.

**Regiones.** Pendiente (Japón como mercado principal según la política; sin pesos publicados).

**Sectores.** Pendiente (Finect no publica desglose para esta clase).

**Quién es y para qué sirve.** Fondo de renta variable japonesa de gestión activa (Man GLG): busca alta rentabilidad total a largo plazo seleccionando acciones entre las ~300 mayores por capitalización del mercado de Tokio, con foco en baja relación precio/valor contable (P/V) y alta rentabilidad por dividendo (quefondos). Referencias: Russell/Nomura Large Cap Value Index (Total Return) y TOPIX (quefondos). Puede incluir además instrumentos del mercado monetario, bonos corporativos, convertibles y preferentes (Finect). Categoría VDOS: RVI JAPÓN; Morningstar (Finect/FT): RV Japón Cap. Grande, estilo Large Value (FT). Acumulación (FT). Clase lanzada el 02/03/2010 (quefondos, Finect, FT); gestores: Jeffrey M. Atherton y Emily Badger (FT). Patrimonio del fondo: 3.908,20 M€ (Finect); clase: 107,3 M€ (Finect) / 89,40 M£ (FT, 31/10/2026); quefondos publica 13.684,35 miles de EUR (discrepancia, ver Pegas).

**Lectura para cartera (texto de la ficha).** Satélite de valor japonés de alta convicción (baja P/V + alto dividendo) dentro del universo de las 300 mayores de Tokio, con clase H en EUR. Para quien quiere un sesgo valor disciplinado en Japón y acepta más volatilidad que la media: quefondos la sitúa en el quintil 1 de volatilidad (el más volátil de su categoría, escala inversa). No es un núcleo tranquilo; es un satélite de estilo con historial largo (desde 2010). La evidencia es de las mejores del listado en consistencia: quintil 1 en los tres últimos años naturales — 2023 33,59 % (41/617), 2024 26,62 % (78/665), 2025 33,24 % (9/701) — y …

**Pegas detectadas.**
- Volatilidad alta: quintil 1 (el más volátil) en la escala inversa de quefondos; 20,45 % 1A; máxima caída a 10 años -41,00 % (Finect).
- Rentabilidad 1A discrepante: snapshot 27,44 % y Finect 27,15 % vs quefondos 24,31 % (18/11/2026); posible serie desactualizada en quefondos. Manda el snapshot.
- Patrimonio de clase discrepante: quefondos 13,68 M€ (18/11/2026) vs Finect 107,3 M€ vs FT 89,40 M£ (31/10/2026); quefondos podría reflejar otra clase o dato viejo.
- Rating Morningstar ausente en el snapshot y en Finect (VDOS 5★ no es Morningstar).
- La cobertura de divisa de la clase «H» no está confirmada explícitamente por ninguna fuente consultada (solo la nomenclatura).
- Finect no publica composición ni posiciones; asignación y Sony provienen del snippet de FT (top 5 agregado 17,72 %, sin nombres completos).
- Mínimo inicial discrepante: 1.000 EUR (quefondos) vs 833 GBP (FT).
- Enfriamiento reciente: Q5 a 3 meses y Q4 en YTD 2026 tras tres años de quintil 1.
- El texto de estrategia de Finect cita otro ISIN (IE00BYVDZH74) y un gestor distinto (BNY Mellon, depositario): texto genérico del paraguas; la política específica se toma de quefondos.

**Decisión.** Man GLG CoreAlpha D H EUR; vol 20.45%

### Robeco QI EM Active Equities D EUR — `LU0329355670`

**Identidad y operativa.** Robeco Institutional Asset Management BV · clase `rv-emergentes` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV emergentes cuantitativo activo. Importe: 8.000 €. Ficha: `finance/fondos-myinvestor/rv-emergentes/LU0329355670.md`.

**Coste y mínimos.** TER snapshot **1,52 %** (1,52 % (snapshot app)); gestión 1,25 % fija (quefondos); Finect no publica importe; éxito 0,00 % (quefondos «variable»); mínimo publicado "0,00 EUR (quefondos)"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 366.96.

**Exposición y evidencia.** RV 99,93 % · RF 0,00 % · 3A 18,89 % · 5A 10,13 % · vol 15,99 % · SRRI 4. Patrimonio: Pendiente.

**Sectores.** Tecnología 47,26 %; servicios financieros 19,68 %; consumo cíclico 5,72 %; industriales 5,47 %; materiales básicos 5,42 %; comunicación 4,89 %; salud 4,28 %; consumo defensivo 2,60 %; energía 2,36 %; inmobiliario 1,31 %; utilities 0,50 %.

**Quién es y para qué sirve.** Subfondo de la SICAV Robeco de renta variable emergente con **estrategia cuantitativa de selección de valores** (QI): según quefondos, clasifica los valores por su rendimiento relativo futuro esperado usando tres factores —**valoración, calidad y momento**—, con al menos dos tercios de los activos en renta variable de empresas domiciliadas o con actividad predominante en países emergentes u otros incluidos en el benchmark; busca crecimiento del capital a largo plazo con mejor perfil de sostenibilidad que el índice (promueve características ESG e integra riesgos de sostenibilidad). Benchmark: **MSCI Emerging Markets Index** (quefondos). Finect añade que las inversiones en mercados desarrollados no superarán un tercio de los activos y se realizan en mercados regulados. Constitución: **31/10/2001** (quefondos). Patrimonio: 5.947.613,51 miles de euros (≈5.948 M€) según quefondos a 18/11/2026 …

**Lectura para cartera (texto de la ficha).** Papel de **núcleo emergente activo cuantitativo** para quien quiere gestión sistemática multifactor en lugar de stock-picking discrecional: cartera diversificada (~100 valores implícitos en un fondo de 6.300 M), sesgo a gran capitalización y disciplina de factores sin comisión de éxito. Clase EUR: elimina la capa EUR/USD de las clases dólar, aunque mantiene las divisas emergentes sin cubrir. SRRI 4 del snapshot (Finect publica 6/7; ver Pegas). Encaja como bloque emergente principal de una cartera global para un perfil dinámico con horizonte largo. La evidencia es **de las mejores del lote**: M …

**Pegas detectadas.**
- SRRI discrepante: snapshot 4 vs Finect 6/7. Manda el snapshot.
- TER 1,52 % (snapshot) vs gestión fija 1,25 % (quefondos): se anotan ambos; el TER incluye otros gastos. Caro frente a alternativas indexadas emergentes.
- Suscripción hasta 5,00 % publicada por quefondos: comprobar la comisión real aplicada en MyInvestor antes de suscribir.
- Rentabilidades ligeramente discrepantes snapshot vs web (1A 18,80 vs 18,59; 3A 18,89 vs 18,56): fechas de corte distintas; manda el snapshot.
- Patrimonio: quefondos ≈5.948 M€ (a 18/11/2026) vs Finect ≈6.332 M (sin divisa explícita): probable diferencia clase/fondo o fecha.
- Regiones de Finect con artefacto de clasificación: 48,82 % «Asia desarrollada» y 50,87 % «país desarrollado» en un fondo emergente (probable tratamiento de Corea/TW); se publica tal cual con reserva.
- Concentración sectorial: tecnología 47,26 %; TSMC 9,79 % + Samsung 7,11 % + SK Hynix 5,68 % ≈ 22,6 % en semiconductores; incluye un fondo interno de acciones A chinas (3,24 %).
- 2025 por debajo de la categoría (quintil 4): el proceso puede quedarse atrás en rallys liderados por valores que sus factores no favorecen.
- Divisa: clase EUR sin cobertura de las divisas emergentes subyacentes.

**Decisión.** Robeco QI EM Active

### Federated Hermes Asia ex-Japan Equity Fund Class R Acc — `IE00B88WFS66`

**Identidad y operativa.** Hermes Fund Managers Ireland Ltd (Federated Hermes) · clase `rv-otros` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV Asia ex-Japón activo. Importe: 6.000 €. Ficha: `finance/fondos-myinvestor/rv-otros/IE00B88WFS66.md`.

**Coste y mínimos.** TER snapshot **1,58 %** (1,58 % (snapshot app); Finect TER/ongoing charge 1,58 % (coincide)); gestión 1,50 % (Finect); éxito Pendiente (no publicada); mínimo publicado "Pendiente (Finect no lo publica para esta clase)"; mínimo operativo verificado: **MCP 20/11: 0.00 EUR**. NAV 8.753.

**Exposición y evidencia.** RV 98,86 % · RF 0,00 % · 3A 18,31 % · 5A 8,75 % · vol 15,87 % · SRRI 4. Patrimonio: Pendiente.

**Regiones.** Asia desarrollada 50,76 %, Asia emergente 46,82 %, Japón 1,29 %.

**Sectores.** Tecnología 27,74 %, Servicios financieros 15,62 %, Consumo cíclico 14,17 %, Consumo defensivo 11,01 %, Servicios de comunicación 10,52 %, Industriales 9,12 %, Materiales básicos 6,13 %, Inmobiliario 3,31 %, Energía 1,10 %, Salud 0,16 %.

**Quién es y para qué sirve.** Clase minorista R en euros (sin cobertura de divisa) del fondo Federated Hermes Asia ex-Japan Equity: Finect la identifica como «Class R EUR Accumulating». El fondo busca revalorización del capital a largo plazo (horizonte rodante de 5 años) con al menos el 80 % en acciones y valores vinculados de empresas de Asia ex-Japón, o que obtienen de la región una parte sustancial de sus ingresos, cotizadas en mercados regulados (política según Finect). Categoría en Finect: RV Asia (ex-Japón). Patrimonio del fondo: 5.083,39 M (Finect, sin divisa explícita); el de esta clase: 48,50 M (Finect). Finect marca la clase disponible desde el 31/10/2012 y publica años naturales desde 2013; fecha de constitución exacta: Pendiente. La gestión de la clase R cuesta 1,50 %, el doble que la clase F del mismo fondo (0,75 %). El listado de la app llama igual a esta clase y a la R USD (IE00BBL4VW61): se distinguen …

**Lectura para cartera (texto de la ficha).** Satélite de renta variable asiática ex-Japón para un perfil con tolerancia alta a la volatilidad y horizonte largo; no es núcleo por su concentración regional y sectorial (tecnología 27,74 % + financieras 15,62 %, y Samsung ≈10,6 % sumando ordinarias y preferentes). Es la versión minorista en euros del mismo fondo que en clase F institucional cuesta menos de la mitad: TER 1,58 % vs 0,83–0,87 % de las F (Finect). Quien pueda acceder a la clase F obtiene la misma cartera con ≈0,75 puntos menos de coste anual. La evidencia es buena: rating 5★ en el snapshot, +18,31 % anualizado a 3 años y +8,75 % …

**Pegas detectadas.**
- quefondos no tiene el ISIN (versiones móvil y escritorio consultadas): sin rankings, quintiles ni años naturales VDOS; los años naturales proceden de Finect.
- Coste de clase R: TER 1,58 % frente a 0,83 % de la F USD y 0,86–0,87 % de las F EUR del mismo fondo (Finect/snapshot): ≈0,75 puntos anuales de diferencia por la misma cartera.
- SRRI discrepante: snapshot 4, Finect 6; manda el snapshot.
- Rating discrepante: snapshot 5★, Finect 4★; manda el snapshot.
- Rentabilidades de Finect difieren del snapshot (1A +17,38 % vs +14,27 %; YTD +14,81 % vs +14,23 %; 3A 18,51 % vs 18,31 %; 5A 9,19 % vs 8,75 %, a 18/11/2026); manda el snapshot.
- Concentración: Samsung ≈10,6 % y TSMC ≈10,3 % sumando clases/ADR de la misma compañía (cartera a 30/09/2026).
- Divisa EUR sin cubrir: exposición al vaivén de las divisas asiáticas frente al euro.
- El nombre del listado («Class R Acc») coincide con el de la clase R USD (IE00BBL4VW61): distinguir por ISIN/divisa.

**Decisión.** Hermes R EUR; MCP TER 1.59 vs snapshot 1.58; manda snapshot; clase F (0.83) mínimo 100k no operable

### Allianz Global Investors Fund - Allianz Best Styles Europe Equity AT EUR — `LU1019963369`

**Identidad y operativa.** Allianz Global Investors GmbH · clase `rv-europa` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV Europa multifactor activo. Importe: 8.000 €. Ficha: `finance/fondos-myinvestor/rv-europa/LU1019963369.md`.

**Coste y mínimos.** TER snapshot **1,37 %** (1,37 % (snapshot app; FT ongoing charge 1,37 %; Finect snippet gastos corrientes 1,350 %; Investing.com 1,30 %: ver Pegas)); gestión 1,50 % (quefondos «fija»; Finect 1,500 %; FT «max annual charge 1,50 %»); éxito no (quefondos «variable 0,00 %»; Finect n/a); mínimo publicado "0,00 EUR (quefondos; Finect tabla de clases: 0 € para AT). Investing.com lista 4.000.000 (probablemente otra clase institucional: no aplicado)"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 254.14.

**Exposición y evidencia.** RV 99,30 % · RF 0,00 % · 3A 15,57 % · 5A 8,35 % · vol 9,95 % · SRRI 4. Patrimonio: Patrimonio: clase 27,4 M€.

**Sectores.** Servicios financieros 23,94 %, Industriales 19,39 %, Salud 14,11 %, Tecnología 9,67 %, Consumo defensivo 8,65 %, Consumo cíclico 5,25 %, Energía 5,25 %, Utilities 4,61 %, Materiales básicos 4,23 %, Servicios de comunicación 2,90 %, Inmobiliario 1,20 %.

**Quién es y para qué sirve.** Subfondo de la SICAV luxemburguesa Allianz Global Investors Fund, clase AT de acumulación en EUR. Objetivo: crecimiento del capital a largo plazo mediante la inversión en mercados europeos de renta variable; el gestor puede participar en una **superposición de divisas (currency overlay)** y asumir riesgos cambiarios individuales sobre divisas de estados miembros de la OCDE, incluso sin activos denominados en ellas (quefondos/FT). Referencia: MSCI Europe Total Return Net (Finect: MSCI Europe NR EUR). Constitución: 13/10/2014 (quefondos, Finect y FT coinciden). Gestores: Karsten Niemann (desde 01/07/2015) y Andreas Domke (desde 01/09/2021) según FT. Patrimonio: clase 27,4 M€ (quefondos a 18/11/2026); fondo 1.443,0 M€ (Finect, estado embebido); FT: 1.250 M£ de fondo y 23,65 M£ de clase a 30/09/2026. Categoría VDOS: RVI Europa; Finect/Morningstar: RV Europa Cap. Grande Blend (FT: Europe Larg …

**Lectura para cartera (texto de la ficha).** Papel de **núcleo activo de renta variable europea large cap blend**: cartera diversificada (~97 % Europa desarrollada, top 10 ~24 %), sesgo financiero/industrial/salud, beta 0,91-0,96 y tracking error moderado (2,34 según el snippet de Finect). Encaja como alternativa activa a un indexado MSCI Europe; el enfoque multi-estilo busca no depender de un único factor. Historial de la clase desde 2014 (>10 años). Detalle llamativo: la segunda posición (3,25 %) es un warrant sobre una estrategia hermana de Allianz «powered by Artificial Intelligence»: el fondo incorpora exposición a un modelo cuantit …

**Pegas detectadas.**
- SRRI discrepante: snapshot 4 vs Finect 5/7. Manda el snapshot.
- TER/gestión discrepantes: TER snapshot 1,37 % (FT 1,37 %) vs Finect snippet 1,350 % e Investing.com 1,30 %; la comisión de gestión publicada (1,50 %) supera el TER: posible bonificación de la clase AT o perímetros distin
- NAV/YTD web vs snapshot: Finect da NAV 251,64 y YTD 9,41 % a 19/11/2026 frente a 254,14 y 10,50 % del snapshot (quefondos a 18/11/2026 coincide con el snapshot): posible distinto corte horario; manda el snapshot.
- Patrimonios dispares: clase 27,4 M€ (quefondos 18/11/2026) vs 6,3 M€ (snippet Finect, antiguo) vs 23,65 M£ (FT 30/09/2026); fondo 1.443,0 M€ (Finect estado) vs 1.241,6 M€ (snippet Finect) vs 1.250 M£ (FT). Fechas y perím
- 1A y YTD 2026 por debajo de la categoría (Q3); alpha 1A negativo (-0,86, Finect).
- Segunda posición (3,25 % a 30/09/2026) es un warrant sobre la estrategia «Allianz Europe Equity powered by Artificial Intelligence»: exposición vía derivado a un modelo de la casa, con riesgo específico no desglosado en
- Currency overlay permitido sobre divisas OCDE sin activos subyacentes en ellas: riesgo cambiario adicional gestionado activamente.
- El snippet antiguo de Finect mostraba 2026 +3,17 % y NAV 237,28 € (caché vieja): se usó el estado embebido con datos a 19/11/2026.
- El extracto web por herramienta devolvió 402 (cuota agotada); se usó descarga directa curl + INITIAL_STATE.

**Decisión.** Allianz Best Styles Europe AT

### Neuberger Berman Short Duration Euro Bond Fund Class EUR I Accumulating — `IE00BFZMJT78`

**Identidad y operativa.** Neuberger Berman Asset Management Ireland Limited · clase `renta-fija` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Crédito euro corto plazo activo. Importe: 12.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/IE00BFZMJT78.md`.

**Coste y mínimos.** TER snapshot **0,25 %** (0,25 % (snapshot app; gastos corrientes 0,250 % en Finect)); gestión 0,19 % (quefondos y Finect); éxito 0 % / no (quefondos variable 0,00 %; Finect n/a); mínimo publicado "Pendiente (clase institucional I; Trustnet lista 1.000.000 USD para la clase I, no confirmado para EUR)"; mínimo operativo verificado: **MCP 20/11: 1.00 EUR**. NAV 118.2.

**Exposición y evidencia.** RV 0,00 % · RF 99,40 % · duración estimada 1.5 · 3A 4,34 % · 5A 2,39 % · SRRI 2. Patrimonio: patrimonio de la clase 3.049,4 M€.

**Regiones.** países del gráfico de asignación: EE. UU., Reino Unido, Alemania, Francia, Italia, Irlanda, Suiza, España, Países Bajos, Japón (% no disponibles)

**Sectores.** Pendiente (el gráfico de sectores del product brief no publica los % en el extracto)

**Quién es y para qué sirve.** Subfondo de Neuberger Berman Investment Funds plc que busca batir al efectivo en euros en un período de 1 año, en cualquier entorno de mercado, con una cartera diversificada de deuda euro a corto plazo de tipo fijo y variable. Universo principal: bonos investment grade denominados en euros; duración media objetivo entre 0 y +2 años (contribución del crédito a la duración de spread: −1/+3) y hasta un 20 % táctico en bonos más largos u otras estrategias de renta fija euro. Referencia: Bloomberg Euro Aggregate 1-3 Years (Total Return, EUR), solo comparativa (no está restringido por ella). Gestor principal: Antonio Serpico. Constituido el 31/10/2018; patrimonio de la clase 3.049,4 M€ (quefondos, 17/11/2026; Finect: 3.054,2 M€ clase / 4.387,4 M€ fondo). Artículo 8 SFDR.

**Lectura para cartera (texto de la ficha).** Papel de núcleo defensivo / liquidez mejorada: renta fija euro de duración muy corta con gestión activa de calidad, para quien quiere más carry que un monetario sin asumir duración larga. La clase I es institucional y barata (TER 0,25 %), lo que la hace eficiente como bloque conservador de una cartera diversificada. La evidencia de largo plazo es excelente: en la categoría VDOS RF Euro Corto Plazo, quintil 1 en 2023 (+6,72 %, 18/317), 2024 (+7,37 %, 26/336) y 2025 (+3,86 %, 9/343), y quintil 1 también en 3A (17/325, +13,62 % acumulado vs 9,04 % de la categoría) y 5A (26/289). Rating 5 ★ tanto …

**Pegas detectadas.**
- Momento flojo en 2026: YTD por debajo de la categoría (quintil 4) y últimos 3 meses en quintil 5; el 1A móvil ha caído a quintil 3 pese al excelente 3A/5A.
- 2022 peor que su categoría (−5,59 % vs −3,78 %): el riesgo de crédito/táctico puede amplificar caídas.
- OCF discrepante entre fuentes: 0,25 % (Finect y snapshot) vs 0,27 % (Trustnet, snippet); manda el snapshot.
- Composición poco transparente: los gráficos del product brief (sectores, países) no publican cifras legibles; la lectura core/táctico de vencimientos es inferida del orden del gráfico.
- Hasta 20 % táctico en bonos más largos y exposición a high yield/securitized: más riesgo del que sugiere «short duration».
- YTD web (0,11 % a 17/11/2026, quefondos) ligeramente distinto del snapshot (0,09 % a 19/11/2026): manda el snapshot.

**Decisión.** Neuberger I; 2025 Q1; 2022 −5.59%

### UBAM - Global High Yield Solution AHC EUR — `LU0569862609`

**Identidad y operativa.** UBP Asset Management (Europe) S.A. (Union Bancaire Privée) · clase `renta-fija` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: High yield global cubierto EUR activo. Importe: 8.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/LU0569862609.md`.

**Coste y mínimos.** TER snapshot **0,73 %** (0,73 % (snapshot app)); gestión 0,40 % fija (quefondos); éxito No (variable 0,00 %, quefondos); mínimo publicado "Ninguno (KID: «Minimum initial investment: None»; quefondos 0,00 USD)"; mínimo operativo verificado: **web ficha: KID sin mínimo**. NAV 209.67.

**Exposición y evidencia.** RV 0,00 % · RF 100,00 % · duración estimada 3.0 · 3A 7,09 % · 5A 4,31 % · vol 4,58 % · SRRI 3. Patrimonio: Patrimonio: 245,04 M€.

**Regiones.** Pendiente (el FT tearsheet mostraba 0 % en todas las regiones, calculadas solo con posiciones largas de cartera; exposición high yield vía CDS no se refleja)

**Sectores.** Pendiente (Finect no publica desglose sectorial para este fondo)

**Quién es y para qué sirve.** Subfondo de la SICAV luxemburguesa UBAM que busca crecimiento del capital e ingresos invirtiendo en high yield complementado con deuda soberana y cuasi-soberana en USD. La exposición al high yield se implementa mediante índices CDS (Credit Default Swaps) compensados y diversificados, manteniendo una exposición nominal neta de entre el 80 % y el 120 % al high yield; según el KID, los índices CDS ofrecen exposición líquida al high yield con riesgo de tipos mínimo. Al menos el 50 % de la inversión soberana debe estar en emisores con rating ESG mínimo BBB (MSCI o equivalente); la exposición derivada al high yield queda fuera de la estrategia ESG. SFDR artículo 8. Sin benchmark de referencia. Divisa base del fondo USD; la clase AHC EUR es de acumulación (los ingresos se reinvierten, según el KID de 10/05/2026) y cubre principalmente el riesgo de divisa. Constituido el 03/12/2010 (quefondos). …

**Lectura para cartera (texto de la ficha).** Papel de satélite de carry alto dentro del tramo de renta fija: high yield global con exposición sintética vía CDS y colateral soberano USD, para quien busca más rentabilidad que un crédito IG aceptando riesgo de diferenciales y de ciclo. No es un fondo defensivo ni de liquidez: SRRI 3 y volatilidad de ~4 % anual. La clase cubierta EUR elimina la mayor parte del riesgo de divisa (KID), lo que lo hace utilizable directamente en una cartera en euros. La evidencia es sólida en el medio plazo: quintil 1 VDOS en 2025 (+8,69 % vs -1,42 % de la categoría, ranking 18/879) y en 2023 (+12,40 % vs 6,98 % …

**Pegas detectadas.**
- TER snapshot 0,73 % vs suma de comisiones quefondos (0,40 % gestión + 0,36 % depósito = 0,76 %): pequeña discrepancia, manda el snapshot.
- Exposición high yield sintética vía índices CDS: riesgo de derivados/contraparte y cartera «visible» dominada por Treasuries de colateral; los desgloses de región/sector de las fuentes no reflejan la exposición real al c
- Categoría VDOS global con clases en varias divisas: rankings/quintiles con posible efecto divisa, no comparables directamente con la clase cubierta EUR del snapshot.
- YTD 2026 y últimos 3 meses por detrás de la categoría (quintil 3); 1A quefondos +2,60 % (a 12/11/2026) vs +2,43 % del snapshot (a 19/11/2026), fechas distintas.
- Patrimonio de la serie EUR en quefondos (245 M€) muy inferior al del fondo completo (8.383 M€ en Finect); el dato de Finect del snippet de búsqueda (7.998,1 M€) es más antiguo.
- Comisión de suscripción de hasta 3,00 % publicada por quefondos (verificar si MyInvestor la aplica).
- Sharpe 10A de Finect con fecha 30/09/2021 (dato viejo para ese período); el resto de stats a 31/10/2026.

**Decisión.** UBAM HY Solution AHC; sintético vía CDS; duración ~3 estimada

## C3 — 11 fondos

### Fidelity MSCI World Index Fund P-ACC-EUR (hedged) — `IE00BYX5P602`

**Identidad y operativa.** FIL Investment Management (Luxembourg) S.à r.l. (sucursal Irlanda; quefondos: FIL Investments International / … · clase `rv-global` · fuente `listado-app` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Núcleo MSCI World indexado cubierto EUR. Importe: 18.000 €. Ficha: `finance/fondos-myinvestor/rv-global/IE00BYX5P602.md`.

**Coste y mínimos.** TER snapshot **0,20 %** (0,20 % (snapshot app); gastos corrientes Finect 0,200 %; **OCF factsheet 0,17 %** (a 31/10/2026; discrepancia, ver Pegas)); gestión 0,22 % (quefondos «fija»; Finect 0,220 %); éxito n/a (Finect); quefondos truncado antes de «variable»: Pendiente; mínimo publicado "Pendiente (quefondos truncado antes del mínimo; no publicado en las demás fuentes)"; mínimo operativo verificado: **MCP 20/11: 1.00 EUR**. NAV 11.567.

**Exposición y evidencia.** RV 98,98 % · RF 0,00 % · 3A 16,03 % · 5A 8,09 % · SRRI 4. Patrimonio: **3.679,7 M€.

**Sectores.** Tecnología de la información (29,60 % vs 29,80 %), Financiero (16,00 %), Industriales (10,70 %), Salud (10,10 %), Consumo discrecional (8,60 %), Servicios de comunicación (7,10 %), Consumo básico (5,30 %), **Energía (4,50 %)**, Materiales (3,10 %), Utilities (2,50 %), Inmobiliario (1,60 %). Suma 99,

**Quién es y para qué sirve.** Subfondo de Fidelity UCITS II ICAV (Irlanda, autorizado por el Banco Central de Irlanda; registrado para su comercialización en España en el registro de IIC extranjeras de la CNMV con el nº 1709, factsheet) que busca un rendimiento total que refleje, antes de comisiones y gastos, el del **MSCI World Index** (gran y mediana capitalización de mercados desarrollados que cumplen los criterios de tamaño, liquidez y free float de MSCI: ~85 % del mercado negociado públicamente). Réplica física, siguiendo el índice lo más de cerca posible y minimizando el tracking error (quefondos y KIID). **Clase con cobertura cambiaria a EUR**: usa forwards y futuros de divisa para cubrir el riesgo de las posiciones en divisas distintas de la clase, y futuros de índices para equitizar la caja (KIID); la cobertura reduce el riesgo de pérdidas por tipo de cambio **pero también limita las ganancias por divisa** ( …

**Lectura para cartera (texto de la ficha).** Papel de **núcleo de renta variable global desarrollada con cobertura de divisa a EUR**: para quien quiere el MSCI World sin el vaivén EUR/USD (la cartera es 72,8 % EE. UU.). La cobertura no es gratis ni neutra: reduce las pérdidas por divisa pero también recorta las ganancias (factsheet), y con tipos USD por encima de los EUR el diferencial encarece la cobertura (orientación general derivada del escenario macro). El resultado es un perfil distinto al de las clases sin cubrir del mismo índice: mejor cuando el dólar se debilita, peor cuando se fortalece. La evidencia muestra exactamente ese pat …

**Pegas detectadas.**
- OCF/TER discrepante entre fuentes: snapshot 0,20 % = Finect gastos corrientes 0,200 %, pero el factsheet oficial (31/10/2026) publica «Share Class Ongoing Charges: 0,17 %» y la comisión de gestión es 0,22 % (quefondos/Fi
- Rating Morningstar no disponible (null en el snapshot; pendiente declarado en el lote). VDOS sí lo puntúa con 5 estrellas.
- La cobertura cambia el perfil de rentabilidad: quintil 4 en 2022 (-18,41 %) y 2026 YTD (+7,26 % a 17/11), quintil 3 en 2024, frente a quintil 1 en 2023 y 2025. Con la Fed más restrictiva que el BCE (3,75–4,00 % vs 2,50 %
- Años naturales quefondos vs factsheet: pequeñas diferencias (2022: -18,41 % vs -18,1 %; 2025: 16,88 % vs 16,6 %; 2024: 19,10 % vs 19,5 %): bases de cálculo/redondeo distintas; se reportan ambas con su fuente.
- YTD/1A snapshot vs quefondos: 6,75 %/10,55 % (19/11) vs 7,26 %/9,84 % (17/11): fechas distintas; manda el snapshot.
- Concentración: EE. UU. 72,80 %, tecnología 29,60 %, top 10 27,6 % (factsheet a 31/10/2026). Sin emergentes ni small cap (MSCI World).
- SFDR 6: sin promoción ESG ni integración de riesgos de sostenibilidad (no forman parte de la metodología del índice, factsheet). A diferencia de los ESG del lote, sí tiene energía (4,50 %).
- El texto autogenerado de Finect llama «gestora» a Brown Brothers Harriman Trustee Services (Ireland) Limited: es la depositaria, no la gestora (el campo estructurado y el factsheet dan FIL Investment Management (Luxembou
- Extracto de quefondos truncado: comisión variable, depósito y mínimo inicial no obtenidos → Pendiente.
- NAV de quefondos (17/11) idéntico al snapshot (19/11) pese a las fechas: posible NAV sin actualizar en una de las fuentes; manda el snapshot.

**Decisión.** Fidelity P hedged; MCP TER 0.17 vs snapshot 0.20; cobertura cambia el perfil (2022 −18.1%)

### Robeco QI European Conservative Equities D EUR — `LU0339661307`

**Identidad y operativa.** Robeco Institutional Asset Management BV · clase `rv-europa` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV Europa baja volatilidad activo. Importe: 8.000 €. Ficha: `finance/fondos-myinvestor/rv-europa/LU0339661307.md`.

**Coste y mínimos.** TER snapshot **1,01 %** (1,01 % (snapshot app; coincide con TER/OGC 1,01 % de la clase D en Finect y «ongoing charge 1.01%» de FT)); gestión 0,80 % fija (quefondos y Finect clase D); éxito 0,00 % variable (quefondos); no consta en Finect; mínimo publicado "0,00 EUR (quefondos y Finect)"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 341.26.

**Exposición y evidencia.** RV 99,91 % · RF 0,00 % · 3A 15,77 % · 5A 8,04 % · vol 7,68 % · SRRI 3. Patrimonio: 601,19 M€.

**Regiones.** Zona euro (47,83 %), Europa ex-zona euro (35,67 %), Reino Unido (13,99 %), Europa emergente (2,16 %), Oriente Medio (0,27 %); EE. UU. 0 %

**Sectores.** Servicios financieros (31,00 %), Salud (12,43 %), Industria (11,72 %), Consumo defensivo (10,99 %), Energía (8,63 %), Servicios de comunicación (7,19 %), Tecnología (6,55 %), Servicios públicos (4,79 %), Inmobiliario (4,63 %), Consumo cíclico (1,12 %), Materiales básicos (0,88 %)

**Quién es y para qué sirve.** Fondo de renta variable europea de baja volatilidad: selecciona mediante un modelo cuantitativo acciones europeas con volatilidad inferior a la media del mercado («conservative» = baja volatilidad, no renta fija). Objetivo: crecimiento del capital a largo plazo con un perfil de sostenibilidad mejor que el índice, promoviendo características ESG e integrando riesgos de sostenibilidad. Invierte al menos dos tercios del patrimonio en acciones de empresas constituidas o con actividad preponderante en Europa. Benchmark: MSCI Europe Index (Net Return, EUR). El fondo se constituyó el 31/10/2001 (quefondos); la clase D arranca el 25/01/2008 (Finect/FT). Patrimonio del fondo: 601,19 M€ (Finect) / 596.618,72 miles de euros (quefondos a 18/11/2026); clase D: 105,4 M€ (Finect). Categoría VDOS «RVI Europa» (quefondos); Finect «RV Europa Cap. Grande Blend».

**Lectura para cartera (texto de la ficha).** Núcleo europeo de perfil defensivo: renta variable de baja volatilidad para quien quiera exposición a Europa con menos oscilaciones que el índice (beta 0,72 a 1 año y 0,60 a 3 años según Finect; SRRI 3, el más bajo del lote junto con su categoría de riesgo). Encaja como posición principal de RV europea en carteras moderadas, o como contrapeso defensivo a satellites más agresivos; no es un fondo para maximizar rentabilidad en mercados alcistas fuertes. La evidencia es sólida y larga (clase desde 2008, fondo desde 2001): quintil 1 vs su categoría VDOS (RVI Europa) en rentabilidad acumulada a 1 a …

**Pegas detectadas.**
- TER 1,01 % alto para una estrategia cuantitativa de baja volatilidad: las clases hermanas I (0,58 %) y C/F (0,61 %) del mismo fondo son ~40 % más baratas (Finect); comprobar si MyInvestor ofrece alguna.
- Comisión de suscripción de hasta 5,00 % (quefondos/FT/Finect): verificar si se aplica en MyInvestor.
- Comisión de depósito divergente: 0,00 % (quefondos) vs 0,50 % custodia (Finect clase D).
- Lastre estructural en años alcistas: 2023 quintil 5 (932/1018, +8,69 % vs +14,82 % de la categoría); information ratio negativo a 3A/5A/10A (-0,25/-0,16/-0,31, Finect): a muy largo plazo no bate al índice.
- Concentración sectorial: servicios financieros 31,00 %; sensible a giro de tipos y a morosidad si el endurecimiento frena el crédito.
- Fecha de constitución divergente según qué se mire: fondo 31/10/2001 (quefondos) vs clase D 25/01/2008 (Finect/FT).
- Patrimonio divergente por fecha: 596,6 M€ (quefondos 18/11/2026) vs 601,2 M€ (Finect); clase D 105,4 M€ (snippet Finect).
- El Sharpe a 10 años de Finect tiene fecha 30/09/2021 (dato viejo): no usado.
- VDOS lo clasifica «RVI Europa» (genérica) y le da 3 estrellas, mientras Morningstar (snapshot/Finect) le da 4: ratings de proveedores distintos, no contradictorios.

**Decisión.** Robeco QI European Conservative D

### Vanguard Emerging Markets Stock Index Fund EUR Acc — `IE0031786696`

**Identidad y operativa.** Vanguard Group (Ireland) Limited · clase `rv-emergentes` · fuente `listado-app` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Emergentes indexado. Importe: 8.000 €. Ficha: `finance/fondos-myinvestor/rv-emergentes/IE0031786696.md`.

**Coste y mínimos.** TER snapshot **0,23 %** (0,23 % (snapshot app)); gestión 0,23 % (quefondos y Finect); éxito no (Finect: n/a; variable 0,00 % en quefondos); mínimo publicado "1.000.000,00 EUR según quefondos (FT: 833.270 GBP); operativa MyInvestor: Pendiente"; mínimo operativo verificado: **MCP 20/11: 1.00 EUR**. NAV 285.24.

**Exposición y evidencia.** RV 100,00 % · RF 0,00 % · 3A 17,14 % · 5A 6,16 % · SRRI 4. Patrimonio: 18.086,3 M€.

**Regiones.** clasificación FT: Asia desarrollada 50,60 %, Asia emergente 32,06 %, Latinoamérica 6,33 %, Oriente Medio 4,50 %, otros 6,39 % (FT agrupa Corea/Taiwán en «Asia desarrollada»; snippet).

**Sectores.** Tecnología 44,17 %, Servicios financieros 19,05 %, Consumo cíclico 7,48 %, Industrial 6,05 %, Comunicación 5,84 %, otros 17,31 % (FT, snippet).

**Quién es y para qué sirve.** Clase «General EUR Cap» del mismo fondo que la IE0031786142 (Vanguard Emerging Markets Stock Index Fund, subfondo de Vanguard Investment Series Plc, Irlanda): gestión pasiva que replica el MSCI Emerging Markets Index con adquisición física de una muestra representativa de sus valores, plenamente invertido salvo condiciones extraordinarias. Índice de gran y mediana capitalización emergente; divisa base del fondo USD. Clase constituida el 28/02/2014 (quefondos; Finect dice 27/02/2014). Patrimonio del fondo: 18.086,3 M€; de esta clase: 2.014,0 M€ (Finect), la clase EUR mayor del fondo.

**Lectura para cartera (texto de la ficha).** Papel de satélite de renta variable emergente o núcleo del bloque emergente de una cartera indexada. Es la clase EUR grande del fondo (2.014 M€), con el mismo TER 0,23 % que la clase Investor: a igualdad de coste y cartera, la diferencia práctica está en el rating Morningstar de la clase (4★ en el snapshot frente a 3★ de la Investor) y en las condiciones de acceso. Para perfiles de horizonte largo que toleran volatilidad alta y divisa sin cubrir. Evidencia: quefondos (17/11/2026) muestra el mismo patrón que su clase hermana — quintil 2 en 2022 (-15,12 % vs -19,10 % de la categoría) y 2024 (+14 …

**Pegas detectadas.**
- Mínimo de clase publicado de 1.000.000 EUR (quefondos): verificar condiciones de acceso en MyInvestor.
- Fecha de constitución de la clase: 28/02/2014 (quefondos) vs 27/02/2014 (Finect); Fundsquare da creación de la clase 20/02/2014 y del subfondo 07/06/2006. Diferencias de días entre proveedores.
- quefondos (17/11/2026) da 1A acumulado del 15,18 % frente al 17,40 % del snapshot (19/11): fechas distintas y posible efecto de serie; manda el snapshot.
- Concentración: tecnología 44,17 % y top 5 posiciones 33,68 % (FT); riesgo geopolítico de China.
- Divisa: clase EUR sin cubrir sobre cartera en divisas emergentes (base USD).
- Composición del snippet de FT (Finect no renderiza cartera); top 10 nominal → Pendiente. Cartera común con IE0031786142 e IE0031787223.
- Patrimonio del fondo no consta en quefondos (campo vacío); usado el de Finect.

**Decisión.** Vanguard EM EUR Acc; warning señala iShares S (IE000QAZP7L2) que NO está en el listado

### DWS Invest CROCI Japan LCH — `LU1769942233`

**Identidad y operativa.** DWS Investment S.A. · clase `rv-japon` · fuente `mcp` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV Japón calidad-valor activo. Importe: 4.000 €. Ficha: `finance/fondos-myinvestor/rv-japon/LU1769942233.md`.

**Coste y mínimos.** TER snapshot **1,48 %** (1,48 %); gestión —; éxito —; mínimo publicado "0.00 EUR"; mínimo operativo verificado: **MCP ficha: 0.00 EUR**. NAV 637.7.

**Exposición y evidencia.** RV 99,70 % · RF 0,00 % · 3A 18,23 % · 5A 18,13 % · vol 12,45 % · SRRI 4. Patrimonio: Pendiente.

**Regiones.** Japón (99,7 %)

**Sectores.** Salud (23,1 %), Industria (22,8 %), Consumo cíclico (13,3 %), Servicios financieros (10,5 %), Materiales básicos (7,4 %), Tecnología (6,8 %)

**Quién es y para qué sirve.** Fondo de renta variable con foco en Japón, de gestión activa, comercializado en MyInvestor en clase de acumulación (EUR). Fecha de lanzamiento de la clase: 2018-08-30. > Invierte en compañías japonesas de elevada calidad seleccionadas mediante la metodología CROCI (Cash Return on Capital Invested). El proceso de inversión analiza el valor económico real de las empresas para identificar aquellas que cotizan con valoraciones atractivas frente a sus fundamentales, ofreciendo exposición al mercado japonés a través de un enfoque disciplinado de valoración. El fondo se gestiona de forma activa.

**Lectura para cartera (texto de la ficha).** Exposición regional a la bolsa japonesa. Satélite geográfico para sesgar la cartera hacia Japón; riesgo divisa JPY si la clase no está cubierta. *Orientación general derivada de la clasificación del catálogo; no es una recomendación de inversión.*

**Decisión.** DWS CROCI Japan LCH; cobertura EUR no declarada explícitamente en ficha MCP — verificar en pantalla

**Verificación web 20/11/2026.** Factsheet oficial DWS a 30/10/2026: clase LCH (EUR), acumulación, gestión 1,30 %, TER 1,48 %, carga inicial hasta 2 %. La clase LCH es la variante cubierta del yen: su rentabilidad acumulada a 3 años es 81,1 % frente al 55,7 % de la clase LC(EUR) sin cubrir. Queda verificada la cobertura que la ficha MCP no declaraba. <https://download.dws.com/download/asset/6f69b6a8-359f-4a36-bb75-4ef2c26b9fda?tenant=ActiveEmea>

### DWS Invest CROCI US Dividends EUR LC — `LU2468423889`

**Identidad y operativa.** DWS Investment S.A. · clase `rv-usa` · fuente `mcp` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV USA dividendo-valor activo. Importe: 10.000 €. Ficha: `finance/fondos-myinvestor/rv-usa/LU2468423889.md`.

**Coste y mínimos.** TER snapshot **1,15 %** (1,15 %); gestión —; éxito —; mínimo publicado "0.00 EUR"; mínimo operativo verificado: **MCP ficha: 0.00 EUR**. NAV 143.56.

**Exposición y evidencia.** RV 99,70 % · RF 0,00 % · 3A 16,63 % · 5A Pendiente · vol 15,37 % · SRRI 4. Patrimonio: Pendiente.

**Regiones.** Estados Unidos (97,1 %), Reino Unido (2,6 %)

**Sectores.** Consumo defensivo (22,4 %), Salud (21,2 %), Consumo cíclico (20,0 %), Energía (9,6 %), Tecnología (9,3 %), Materiales básicos (7,4 %)

**Quién es y para qué sirve.** Fondo de renta variable con foco en USA, de gestión activa, comercializado en MyInvestor en clase de acumulación (EUR). Fecha de lanzamiento de la clase: 2018-08-28. > Invierte en compañías estadounidenses con una sólida política de distribución de dividendos y fundamentales robustos. A través de la metodología CROCI (Cash Return on Capital Invested), el fondo identifica empresas con valoraciones atractivas y capacidad de generar caja de forma sostenible, buscando combinar rentabilidad por dividendo y crecimiento del capital. El fondo se gestiona de forma activa.

**Lectura para cartera (texto de la ficha).** Exposición concentrada en la bolsa de EE. UU. Complementa o sustituye parcialmente a un núcleo global, pero un fondo global ya lleva una parte mayoritaria de EE. UU.: añadirlo aumenta el peso del país, no diversifica. *Orientación general derivada de la clasificación del catálogo; no es una recomendación de inversión.*

**Decisión.** DWS CROCI US Dividends EUR LC; sin 5A (clase joven)

### Pictet-Quest Global Sustainable Equities-P EUR — `LU0845340131`

**Identidad y operativa.** Pictet Asset Management (Europe) SA · clase `rv-global` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV global sostenible cuantitativo activo. Importe: 7.000 €. Ficha: `finance/fondos-myinvestor/rv-global/LU0845340131.md`.

**Coste y mínimos.** TER snapshot **1,17 %** (1,17 % (snapshot app)); gestión 2,40 % fija máxima (quefondos; FT publica ongoing charge 1,17 % y max annual charge 2,40 %); éxito 0,00 % (variable, quefondos); mínimo publicado "0,00 EUR (quefondos)"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 359.25.

**Exposición y evidencia.** RV 99,79 % · RF 0,00 % · 3A 15,30 % · 5A 9,68 % · vol 11,02 % · SRRI 4. Patrimonio: Pendiente.

**Regiones.** Estados Unidos (76,21 %), Zona Euro (7,50 %), Japón (6,07 %), Reino Unido (4,91 %), Europa ex-Zona Euro (1,99 %), Asia emergente (1,35 %)

**Sectores.** Tecnología (34,81 %), Servicios financieros (19,94 %), Salud (17,20 %), Industrial (8,34 %), Consumo cíclico (8,18 %), Comunicación (4,85 %)

**Quién es y para qué sirve.** Subfondo de la SICAV Pictet que busca crecimiento del capital invirtiendo principalmente en renta variable y valores similares de sociedades con calidad superior en estabilidad financiera y solvencia, con criterio de sostenibilidad, en todo el mundo (incluidos emergentes). Puede usar derivados para gestión eficiente o cobertura y productos estructurados. Referencia: MSCI World (USD). Constituido el 14/12/2012 (quefondos). Patrimonio de la clase P EUR: 32.449,62 miles de euros (quefondos, 17/11/2026); el fondo completo suma 1.253,7 M€ (Finect). Categoría VDOS: RVI GLOBAL; Morningstar: RV Global Cap. Grande Blend.

**Lectura para cartera (texto de la ficha).** Candidato a núcleo de renta variable global para un perfil dinámico que quiera gestión activa con sesgo de calidad/sostenibilidad: cartera casi 100 % bolsa, muy diversificada por regiones pero con fuerte peso de EE. UU. (76 %) y de tecnología (35 %). La clase P EUR es de acumulación y cotiza en euros, aunque la cartera subyacente es mayoritariamente USD sin cubrir. La evidencia es sólida y consistente: en quefondos queda en quintil 2 de la categoría RVI GLOBAL en 2022, 2023, 2024 y en lo que va de 2026 (solo 2025 flojea, quintil 3: 3,79 % vs 7,13 % de la categoría), y en 5 años acumulados alca …

**Pegas detectadas.**
- TER snapshot 1,17 % vs comisión fija máxima 2,40 % en quefondos: la fija es el máximo del folleto; el coste real publicado (FT ongoing charge) coincide con el snapshot, 1,17 %.
- Rating Morningstar: 4 ★ en el snapshot, 3 ★ en Finect; manda el snapshot.
- Rentabilidades trailing de quefondos (1A 16,68 %, datos a 17/11/2026) difieren del snapshot (18,42 %, 19/11/2026) por fecha de cálculo; manda el snapshot.
- Concentración: 76 % EE. UU. y 35 % tecnología; divisa USD subyacente sin cubrir.
- Tracking error 1A 6,32 % e information ratio 3A -0,48 (Finect): la desviación del índice no siempre ha añadido valor a 3 años.
- Patrimonio de la clase P EUR pequeño (32,4 M€) frente al fondo total (1.253,7 M€).

**Decisión.** Pictet Quest Global Sustainable P

### iShares Euro Investment Grade Corporate Bond Index Fund (IE) D Acc EUR — `IE00BDRK7J14`

**Identidad y operativa.** BlackRock Asset Management Ireland Ltd · clase `renta-fija` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Crédito euro IG indexado. Importe: 12.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/IE00BDRK7J14.md`.

**Coste y mínimos.** TER snapshot **0,12 %** (0,12 % (snapshot app; OCF 0,12 % iShares; gastos corrientes 0,120 % Finect)); gestión 0,09 % (iShares) / 0,150 % (Finect) / 0,15 % fija (quefondos); éxito 0,00 % (iShares «Performance Fee»); variable 0,00 % (quefondos); n/a (Finect); mínimo publicado "100.000,00 EUR (quefondos). Mínimo de MyInvestor: Pendiente"; mínimo operativo verificado: **MCP 20/11: 0.00 EUR**. NAV 10.907.

**Exposición y evidencia.** RV 0,00 % · RF 99,81 % · duración estimada 4.4 · 3A 3,65 % · 5A 0,06 % · vol 3,44 % · SRRI 2. Patrimonio: Pendiente.

**Regiones.** Pendiente (por política, emisores de la UEM y no UEM, incluidos supranacionales; desglose numérico no publicado en las fuentes consultadas)

**Sectores.** Pendiente (el factsheet de iShares los publica en gráfico no textual; Finect no renderiza la composición)

**Quién es y para qué sirve.** Clase D en euros del iShares Euro Investment Grade Corporate Bond Index Fund (IE), subfondo de BlackRock Fixed Income Dublin Funds Plc (Irlanda, UCITS). Gestión pasiva que busca una rentabilidad total (capital + ingresos) que refleje la del índice Bloomberg Euro Aggregate Corporate: invierte predominantemente en los bonos corporativos con grado de inversión denominados en euros y a tipo fijo que componen el índice; puede mantener un bono degradado hasta que sea practicable venderlo (política de quefondos y factsheet iShares). Benchmark: Bloomberg Euro Aggregate Corporate (quefondos) / BBG Euro Corporate Index (EUR) (iShares) / Bloomberg Euro Corp TR EUR (Finect). La clase inició el **09/06/2017** (Finect e iShares; quefondos publica 12/06/2017); el fondo original data del 09/02/2012 (iShares). Patrimonio de la clase: 1.087.496,55 miles de euros (~1.087 M€) a 17/11/2026 (quefondos; Finect …

**Lectura para cartera (texto de la ficha).** Papel de **núcleo de renta fija corporativa en euros** para un inversor que quiere exposición diversificada a crédito investment grade europeo con coste muy bajo (TER 0,12 %) y acepta la volatilidad moderada de la duración media (SRRI 2 en el snapshot, duración efectiva 4,38 años). Encaja como bloque de carry dentro de la parte defensiva de una cartera indexada; no es liquidez ni monetario: con ~4,4 años de duración, el precio se mueve con los tipos. La evidencia es sólida con historial largo (clase desde 2017). Según quefondos (categoría VDOS Deuda Privada Euro), el acumulado a 3 años (11,36 …

**Pegas detectadas.**
- Duración media (~4,4 años) con sesgo alcista de tipos: vulnerable a nuevas subidas del BCE; el −13,26 % de 2022 muestra el riesgo. No es un fondo de liquidez.
- Volatilidad 1A en quintil 4 vs su categoría VDOS (3,55 %, ranking 473/636): más volátil que la media de Deuda Privada Euro.
- 5A anualizado casi plano (0,06 % snapshot): el ciclo de subidas 2022 anuló la rentabilidad a 5 años pese al quintil 2.
- Comisiones discrepantes: gestión 0,09 % (iShares) vs 0,150 % (Finect) vs 0,15 % fija (quefondos); suscripción/reembolso «hasta 3 %/2 %» (quefondos) vs 0,000 % (Finect). TER 0,12 % coincide en snapshot, iShares y Finect;
- Fecha de constitución discrepante: 12/06/2017 (quefondos) vs 09/06/2017 (Finect e iShares).
- Años naturales ligeramente distintos entre fuentes (quefondos vs factsheet iShares, p. ej. 2024: 4,46 % vs 4,74 %): fechas de cálculo distintas; se anotan ambos.
- Composición incompleta: Finect no renderiza la composición (JS); asset allocation, sectores y regiones en % quedan Pendiente. Los gráficos de sectores/rating/vencimientos del factsheet no tienen capa de texto.
- Mínimo inicial de gestora 100.000 EUR; verificar condiciones reales en MyInvestor.
- El extractor web automático falló por límite de uso (402) el 2026-11-19; el factsheet se consultó por descarga directa.

**Decisión.** duración ~4.4 (ficha); 2022 −13.26%

### State Street EMU Government Bond Index Fund P Acc — `LU0438093006`

**Identidad y operativa.** State Street Global Advisors (SSGA Luxembourg SICAV) · clase `renta-fija` · fuente `listado-app` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Gubernamental euro indexado. Importe: 10.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/LU0438093006.md`.

**Coste y mínimos.** TER snapshot **0,36 %** (0,36 % (snapshot app; Finect 0,360 %; factsheet SSGA «Actual TER» 0,36 %)); gestión 0,30 % (quefondos «fija»; Finect 0,300 %; factsheet SSGA 0,3 %); éxito 0,00 % (quefondos «variable»); Finect: n/a; mínimo publicado "50 EUR (Finect y factsheet SSGA); mínimo posterior 50 EUR"; mínimo operativo verificado: **MCP 20/11: 50 EUR**. NAV 12.753.

**Exposición y evidencia.** RV 0,00 % · RF 99,84 % · duración estimada 7.0 · 3A 1,25 % · 5A -3,10 % · vol 4,84 % · SRRI 3. Patrimonio: **532,1 M€.

**Sectores.** 100 % deuda pública (Tesoro 99,87 %, factsheet SSGA).

**Quién es y para qué sirve.** Fondo indexado de la SSGA Luxembourg SICAV (clase P Acc, para todos los inversores) que replica el **FTSE EMU Government Bond Index**, el mercado de bonos soberanos en euros de tipo fijo y grado de inversión según la metodología del índice (política según quefondos y factsheet de SSGA). Constituido el **25/08/2009**. Patrimonio del fondo: **532,1 M€** (Finect) / 526,97 M€ a 30/09/2026 (factsheet SSGA); clase P: 7,4 M€ (Finect). Categoría VDOS: **Deuda Pública Euro**.

**Lectura para cartera (texto de la ficha).** Papel de **núcleo de renta fija soberana euro**: replica todo el mercado de deuda pública de la EMU con una sola posición, diversificada por países (Francia, Italia, Alemania, España suman ~81 %). Es el bloque «renta fija de toda la vida» de una cartera indexada, para perfiles que quieren exposición a tipos euro sin selección activa. Ojo: no es un fondo defensivo de corto plazo; con ~28 % de la cartera a más de 10 años, tiene duración relevante. La evidencia reciente es floja, coherente con el ciclo de tipos: YTD 2026 **−2,42 %** y 1A **−2,84 %** (snapshot), quintil 3 en su categoría VDOS en 2 …

**Pegas detectadas.**
- Riesgo: Finect muestra 4/7; el snapshot de la app da SRRI 3 (manda el snapshot).
- NAV de Finect desactualizado (15/09/2026); quefondos (17/11/2026) coincide con el snapshot.
- Reembolso: Finect publica 2,000 % pero el factsheet de SSGA dice «hasta 0 %» para la clase P; discrepancia sin resolver (probable máximo de folleto vs práctica).
- quefondos no tiene años naturales 2022–2024 ni acumuladas 3A/5A para esta clase (·): consistencia histórica no evaluable por esa vía.
- Patrimonio: quefondos publica 6.364,32 miles de € (parece nivel de clase) vs 532,1 M€ del fondo en Finect y 7,4 M€ de clase; cifras a fechas distintas.
- Comisión de custodia 0,500 % publicada por Finect, inusualmente alta; no corroborada por el factsheet (que no la menciona).
- TER 0,36 % coincide en las tres fuentes, pero es alto para un indexado soberano frente a clases I/B del mismo fondo.
- Duración efectiva no publicada; solo tramos de vencimiento.

**Decisión.** State Street EMU Gov P; duración ~7 estimada; JPM Short Duration descartado (mín 35.000)

### DWS Floating Rate Notes LC — `LU0034353002`

**Identidad y operativa.** DWS Investment S.A. · clase `renta-fija` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Flotante euro activo. Importe: 8.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/LU0034353002.md`.

**Coste y mínimos.** TER snapshot **0,25 %** (0,25 % (snapshot app; gastos corrientes 0,250 % en Finect)); gestión 0,60 % (quefondos «fija» y Finect; ver pega sobre discrepancia con el OCF); éxito 0 % / no (quefondos variable 0,00 %; Finect n/a); mínimo publicado "0,00 EUR (quefondos)"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 94.83.

**Exposición y evidencia.** RV 0,00 % · RF 100,00 % · duración estimada 0.25 · 3A 3,32 % · 5A 2,54 % · SRRI 1. Patrimonio: Patrimonio de la clase: 7.413,5 M€.

**Regiones.** Pendiente

**Sectores.** Pendiente

**Quién es y para qué sirve.** Fondo UCITS luxemburgués (FCP Part 1) de DWS cuyo objetivo es generar rentabilidad en euros con independencia de las fluctuaciones de tipos y divisa: al menos el 70 % del patrimonio en bonos de interés variable (floating rate notes) denominados en euros o cubiertos frente al euro, públicos y corporativos; puede invertir también en convertibles, bonos fijos, fondos e instrumentos del mercado monetario de mercados reconocidos OCDE/G20/UE/Singapur. Sin benchmark de referencia. El KID lo describe como gestión activa con horizonte de inversión recomendado de 183 días y acumulación explícita («returns and gains are not distributed but are reinvested»). Clase LC lanzada en 1991; constitución 15/07/1991. Patrimonio de la clase: 7.413,5 M€ (quefondos, 17/11/2026); Finect: 7.280,9 M€ clase / 14.322,6 M€ fondo (18/11/2026).

**Lectura para cartera (texto de la ficha).** Papel de liquidez remunerada / defensivo puro: los bonos flotantes resetean su cupón con los tipos cortos, por lo que el fondo se comporta casi como un monetario con carry de crédito. SRRI 1 (el más bajo) y volatilidad 1A del 0,23 % lo sitúan en el extremo conservador: encaja como aparcamiento de efectivo o núcleo defensivo para perfiles que no quieren duración. La evidencia es muy sólida y con historial largo (desde 1991). En la categoría VDOS RF Euro (amplia, incluye duraciones largas): quintil 1 en 2026 (43/517, +2,13 % vs −0,39 % de la categoría a 17/11/2026), en el año móvil (39/514) y en …

**Pegas detectadas.**
- Discrepancia de comisiones: gestión 0,60 % (quefondos y Finect) vs TER/OCF 0,25 % (snapshot y Finect); posible bonificación/rebate de la clase LC, sin confirmar en las fuentes. Manda el snapshot (0,25 %).
- quefondos sirvió primero una caché del 13/08/2026 (NAV 94,26, YTD 1,53 %, rating VDOS 2 ★); re-extraída el 2026-11-19 con datos a 17/11/2026 (rating VDOS 5 ★). Se usa la versión fresca.
- Suscripción de hasta 1 % en folleto (Finect la publica como 1,000 %): comprobar si MyInvestor la aplica.
- Sin composición publicada en quefondos/Finect (JS no renderizado): cartera Pendiente; duración ~15,6 meses y cupón ~4,2–4,3 % tomados del snippet del factsheet de Deutsche Bank, sin fecha conocida.
- Rentabilidad ligada a tipos cortos: si el BCE gira a bajadas, el carry cae rápido (coste de oportunidad frente a duraciones largas).
- Categoría VDOS «RF Euro» amplia (mezcla duraciones): los rankings comparan contra fondos muy distintos; el 2023 en quintil 4 refleja ese sesgo, no mala gestión.

**Decisión.** DWS Floating Rate Notes LC; 2026 Q1

### ODDO BHF Euro Credit Short Dur CR-EUR — `LU1486845537`

**Identidad y operativa.** ODDO BHF Asset Management SAS · clase `renta-fija` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Crédito euro corto plazo activo. Importe: 8.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/LU1486845537.md`.

**Coste y mínimos.** TER snapshot **0,92 %** (0,92 % (snapshot app); ongoing charge 0,92 % (FT)); gestión 0,80 % (quefondos «fija»); éxito 0,00 % (quefondos «variable»); mínimo publicado "100,00 EUR (quefondos)"; mínimo operativo verificado: **web ficha: 100 EUR**. NAV 116.795.

**Exposición y evidencia.** RV 0,00 % · RF 96,84 % · duración estimada 1.5 · 3A 3,69 % · 5A 2,61 % · SRRI 2. Patrimonio: Pendiente.

**Regiones.** Pendiente (Finect no publica desglose regional; política sin limitación geográfica, ≥2/3 en euros).

**Sectores.** Pendiente (Finect no publica desglose sectorial).

**Quién es y para qué sirve.** Subfondo de ODDO BHF (SICAV luxemburguesa), clase CR-EUR de acumulación (FT: «Income treatment: Accumulation»). Objetivo según quefondos: elevado nivel de ingresos y crecimiento del capital, invirtiendo al menos dos tercios en renta fija cotizada de sociedades públicas o privadas de cualquier sector, sin limitación geográfica, con al menos dos tercios denominados en euros y al menos dos tercios con vencimiento residual no superior a 4 años. Sin benchmark de referencia. La descripción de Finect añade el perfil de crédito: calificación mínima B3/B-, al menos 20 % del patrimonio en high yield (máximo BB+/Ba1) y venta obligada si un título se rebaja por debajo de B3/B-. Constituido el 02/09/2016 (quefondos; FT fecha la clase el 11/10/2016). Patrimonio: 506.347,21 miles de EUR (quefondos, a 17/11/2026); Finect registra 2.279,1 M€ (sin fecha, probablemente del fondo completo). Categoría VDOS: …

**Lectura para cartera (texto de la ficha).** Papel de núcleo/satélite defensivo de crédito euro a corto plazo: renta fija corporativa con vencimientos cortos (≥2/3 ≤4 años) que busca ingresos estables con sensibilidad a tipos limitada, añadiendo una bolsa de high yield (≥20 %) para mejorar el carry. Encaja para perfiles conservadores-moderados que quieren más rentabilidad que un monetario sin asumir la duración del agregado, y como peldaño intermedio entre monetarios y crédito de medio plazo. Evidencia muy sólida y consistente: en quefondos (RF Euro Medio Plazo) es quintil 1 en cuatro de los cinco años naturales (2022 -3,12 % vs -5,61 % …

**Pegas detectadas.**
- Rating Morningstar bajo y discrepante: 2 ★ snapshot vs 1 ★ Finect, frente a 4 estrellas VDOS y quintiles 1 de quefondos: las metodologías discrepan; manda el snapshot.
- Categoría dispar: VDOS lo clasifica «RF Euro Medio Plazo» y Finect «RF Bonos Alto Rendimiento EUR»; su política (vencimiento residual ≤4 años, ≥20 % HY) es de crédito corto con bolsa HY. Los rankings de quefondos son vs
- Quintil 5 de volatilidad 1A vs su categoría (134/156): dentro de «RF Euro Medio Plazo» hay fondos más cortos/estables.
- Crédito de calidad media-baja: mínimo B3/B-, ≥20 % HY, emisores como Pemex o Teva en el top 10; máxima caída a 10 años -7,66 % (Finect).
- Fechas de constitución dispares: 02/09/2016 (quefondos, fondo) vs 11/10/2016 (FT, clase).
- Patrimonio: quefondos publica 506,3 M€ (17/11/2026) y Finect 2.279,1 M€ sin fecha (probablemente fondo completo vs clase); no comparables directamente.
- La suscripción «hasta 5,00 %» es máximo de folleto; no consta que MyInvestor la aplique.

**Decisión.** ODDO BHF Euro Credit Short Dur CR; 5A Q1

### Groupama Entreprises NC — `FR0010288316`

**Identidad y operativa.** Groupama Asset Management · clase `monetarios` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Monetario EUR. Importe: 7.000 €. Ficha: `finance/fondos-myinvestor/monetarios/FR0010288316.md`.

**Coste y mínimos.** TER snapshot **0,32 %** (0,32 % (snapshot app; Finect gastos corrientes 0,320 %)); gestión 0,580 % (Finect); máx. directa 0,55 % + indirecta 0,00 % + operativa 0,03 % (reporting oficial); quefondos «fi …; éxito No (reporting oficial «Performance fee: No»; quefondos variable 0,00 %; Finect n/a); mínimo publicado "500,00 EUR (quefondos y reporting oficial)"; mínimo operativo verificado: **web ficha: 500 EUR**. NAV 618.58.

**Exposición y evidencia.** RV 0,00 % · RF 3,70 % · 3A 2,73 % · 5A 2,17 % · vol 0,12 % · SRRI 1. Patrimonio: 5.315,84 M€.

**Regiones.** Pendiente en %; el top 10 está dominado por Francia y Reino Unido (emisores).

**Sectores.** Pendiente (desglose no publicado en las fuentes consultadas; por política: ECP/CD bancarios y corporativos, deuda pública y organismos franceses).

**Quién es y para qué sirve.** FCP monetario francés de Groupama AM, creado el 09/03/1998 (la participación NC data de 2006: 14/03/2006 según el reporting oficial, 25/04/2006 según Finect). Objetivo: obtener, mediante gestión activa y para colocaciones a corto plazo (mínimo recomendado 1 mes), un rendimiento ligeramente superior a los tipos del mercado monetario tras gastos; referencia €STR capitalizado (ESTER). Invierte en títulos de crédito negociables (TCN), certificados de depósito, billetes de tesorería, EuroCP, deuda del Estado francés (BTF/BTAN), BMTN y obligaciones a tipo fijo con duración residual < 1 año o a tipo variable referenciadas a Euribor/€STR (política según quefondos). WAM 15,86 días y WAL 92,71 días (factsheet semanal oficial a 07/06/2026). Patrimonio del fondo: 5.315,84 M€ a 30/09/2026 (reporting mensual oficial); clase NC: 2.478.864,26 miles de EUR a 17/11/2026 (quefondos), 2.463,3 M€ según Finec …

**Lectura para cartera (texto de la ficha).** Papel de liquidez/defensivo puro: tesorería en euros con volatilidad casi nula (0,03 % a 1 año según el reporting oficial; 0,05 % según quefondos) y SRRI 1. Es el típico aparcamiento de caja o fondo de emergencia para un perfil conservador, o el estacionamiento temporal de liquidez entre inversiones. Su WAM de ~16 días lo hace casi insensible a subidas de tipos por precio. La evidencia es de un monetario correcto pero sin brillo: quintil 3 en casi todos los años naturales (2023: 3,23 %, 39/88; 2024: 3,75 %, 49/97; 2025: 2,17 %, 67/114) y quintil 2 en 2022 (-0,03 %, 19/84, mejor que la categorí …

**Pegas detectadas.**
- Comisiones discrepantes entre fuentes: gestión 0,580 % (Finect) vs máx. directa 0,55 % (oficial) vs «fija» 1,00 % (quefondos, máximo de folleto). TER 0,32 % coincide en snapshot y Finect; manda el snapshot.
- Suscripción/reembolso: máximos de folleto hasta 0,50 % (quefondos y oficial); Finect publica suscripción 0,500 % y reembolso 0,000 %. Verificar si MyInvestor aplica la comisión de suscripción.
- Rentabilidad sistemáticamente ligeramente por debajo del benchmark €STR capitalizado (exceso negativo en 2018–2025 salvo 2020–2021): el objetivo de batir al mercado monetario tras gastos no se cumple de forma consistente
- Fecha de creación de la participación NC discrepante: 14/03/2006 (oficial) vs 25/04/2006 (Finect).
- Composición completa (asset allocation, sectores, regiones en %) no publicada en las fuentes consultadas; solo top 10 del factsheet de 07/06/2026, que puede no estar al día.
- quefondos mantiene en la política la referencia a EONIA (texto antiguo); el benchmark vigente es €STR capitalizado (oficial y Finect).

**Decisión.** Groupama Entreprises NC; ligeramente por debajo de €STR

## C4 — 11 fondos

### Robeco QI Global Conservative Equities D EUR — `LU0705782398`

**Identidad y operativa.** Robeco Institutional Asset Management B.V. · clase `rv-global` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV global baja volatilidad activo. Importe: 18.000 €. Ficha: `finance/fondos-myinvestor/rv-global/LU0705782398.md`.

**Coste y mínimos.** TER snapshot **1,01 %** (1,01 % (snapshot app; coincide Finect)); gestión 0,80 % (quefondos y Finect); éxito 0,00 % (quefondos); mínimo publicado "0,00 EUR (quefondos)"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 396.51.

**Exposición y evidencia.** RV 99,15 % · RF 0,00 % · 3A 14,26 % · 5A 8,58 % · SRRI 3. Patrimonio: Patrimonio del fondo 570,7 M€.

**Regiones.** EE. UU. 52,88 %, Asia desarrollada 10,32 %, Japón 8,03 %, Zona euro 6,55 %, Europa ex-euro 6,53 %, Canadá 4,59 %. Desarrollado 93,19 % / emergente 5,93 %.

**Sectores.** Tecnología 28,34 %, Servicios financieros 20,75 %, Salud 12,82 %, Industrial 9,53 %, Comunicación 8,33 %, Consumo defensivo 6,79 %, Energía 5,31 %.

**Quién es y para qué sirve.** Subfondo de la SICAV luxemburguesa Robeco Capital Growth Funds: al menos dos tercios del patrimonio en acciones globales seleccionadas por un modelo cuantitativo por su **baja volatilidad esperada** (alta rentabilidad por dividendo, valoración atractiva, momentum y revisiones de analistas), con características ESG. Objetivo: rentabilidad comparable a la bolsa desarrollada con menor riesgo de caída. Benchmark: MSCI All Country World Index (Net Return, EUR). Fondo constituido el 31/10/2001; clase D EUR desde el 14/12/2011 (Robeco). Patrimonio del fondo 570,7 M€ (Finect/Robeco); clase D 56,4 M€ (Finect) / 61,2 M€ (Robeco, 09/11/2026). **La clase D EUR es de acumulación** («Dividend paying: No», Robeco). Categoría VDOS: RVI Global; Morningstar: RV Global Cap. Grande Blend. Clase hermana de la B EUR (LU0705780269, de distribución): misma cartera.

**Lectura para cartera (texto de la ficha).** Papel de **núcleo defensivo de renta variable global** para un perfil moderado-dinámico: exposición a bolsa mundial con volatilidad y caídas muy inferiores a las del índice, en clase de acumulación (diferimiento fiscal de los rendimientos). Es la versión «reinvierte todo» del mismo fondo que la clase B de distribución; para acumular patrimonio a largo plazo, esta D es la más eficiente fiscalmente. Evidencia sólida en riesgo y consistente en rentabilidad: **volatilidad 1A del 5,15 % (quefondos, quintil 5 = el menos volátil de su categoría), beta 0,36 a 1A y 0,48 a 3A (Finect)**; máxima caída 1A …

**Pegas detectadas.**
- Rentabilidad absoluta por debajo del índice en rallies growth (2023 quintil 5, 2025 quintil 3): el coste de la baja volatilidad.
- TER 1,01 %: elevado frente a ETFs globales minimum-volatility.
- Comisión de suscripción de hasta 5 % en folleto: verificar condiciones en la app.
- Comisión de depósito discrepa: quefondos 0,00 % vs Finect 0,50 % (custodian fee).
- Patrimonio: quefondos 573,1 M€ (17/11/2026, fondo completo) vs clase D 56,4 M€ (Finect) / 61,2 M€ (Robeco 09/11/2026).
- Constitución: quefondos da 31/10/2001 (fondo); Robeco da 14/12/2011 para la clase D EUR.
- ~53 % EE. UU. y divisa sin cubrir: exposición EUR/USD relevante.
- No confundir con la clase B EUR (LU0705780269): misma cartera pero de distribución; las rentabilidades de quefondos de la B van sin cupones y parecen peores.

**Decisión.** Robeco QI Global Conservative D; 2022 Q1

### AB Low Volatility Eq A EUR — `LU1998907197`

**Identidad y operativa.** AllianceBernstein · clase `rv-global` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV global baja volatilidad activo (2). Importe: 12.000 €. Ficha: `finance/fondos-myinvestor/rv-global/LU1998907197.md`.

**Coste y mínimos.** TER snapshot **1,67 %** (1,67 % (snapshot app; product report AB 1,67 %)); gestión 1,50 % (quefondos); éxito 0,00 % (quefondos: variable 0,00 %); mínimo publicado "2.000 EUR (quefondos; product report AB: 2.000 EUR inicial / 750 EUR adicional)"; mínimo operativo verificado: **web ficha: 2.000 EUR / 750 adicional**. NAV 29.23.

**Exposición y evidencia.** RV 96,31 % · RF 0,00 % · 3A 11,21 % · 5A 7,54 % · vol 9,73 % · SRRI 4. Patrimonio: Patrimonio de la clase: 151.080 €.

**Regiones.** Estados Unidos 55,70 %; Zona Euro 13,97 %; Reino Unido 10,82 %; Japón 4,43 %; Asia desarrollada 4,38 %; Europa ex-Zona Euro 2,87 %; Canadá 2,64 %; Australasia 1,12 %; Oriente Medio 0,39 %. (96,31 % países desarrollados según Finect.)

**Sectores.** Tecnología 30,22 %; Servicios financieros 20,62 %; Salud 11,41 %; Industriales 10,00 %; Consumo cíclico 7,20 %; Servicios de comunicación 6,51 %; Energía 3,92 %; Consumo defensivo 3,55 %; Utilities 2,43 %; Inmobiliario 0,45 %.

**Quién es y para qué sirve.** Subfondo «Low Volatility Equity Portfolio» de AB SICAV I que busca aumentar el valor de la inversión mediante crecimiento del capital, seleccionando con análisis fundamental bottom-up y un modelo cuantitativo propio de riesgo/rentabilidad valores de alta calidad, baja volatilidad, valoraciones razonables y atractiva rentabilidad al accionista. Invierte en empresas con actividades importantes en países desarrollados y emergentes, de cualquier capitalización y sector; puede incluir convertibles, depositary receipts y ETFs. Referencia: MSCI World. El fondo base es en USD y esta clase A EUR no cubre la divisa. Constituida el 06/06/2019 (quefondos; Finect fecha el inicio el 28/06/2019). Patrimonio de la clase: 151.080 € según quefondos (18/11/2026) vs 8,0 M€ según snippet de Finect y 9,0 M€ (11/06/2026) según product report de AB: discrepancia grande, ver Pegas. Fondo completo 6.190,9 M€ (Fin …

**Lectura para cartera (texto de la ficha).** Papel de **núcleo defensivo de renta variable global** para un inversor en EUR que acepta la exposición al dólar sin cubrir: selección de baja volatilidad y calidad con menor beta que el mercado (beta 0,67 a 1A, 0,73 a 3A según Finect). Quefondos lo clasifica en «RENT. ABSOLUTA. VOLAT. BAJA» (sus rankings son contra esa categoría, no contra RV global); Morningstar lo trata como RV Global Cap. Grande Blend. La evidencia es sólida en su categoría VDOS: quintil 1 en 2026 YTD (10,58 %, ranking 16/122), 2024 (23,34 %, 6/104), 2023 (14,73 %, 8/95) y en acumulados a 1A (11,55 %, 18/122), 3A (37,55 %, …

**Pegas detectadas.**
- Patrimonio de clase muy discrepante: quefondos 151.080 € (18/11/2026) vs Finect 8,0 M€ (snippet) vs AB product report 9,0 M€ (11/06/2026). Si la cifra de quefondos es la correcta, la clase es minúscula (riesgo de cierre/
- Rating discrepante: snapshot 3★ vs Finect 2★ (Morningstar).
- Fecha de inicio discrepante: 06/06/2019 (quefondos) vs 28/06/2019 (Finect).
- Categoría VDOS «Rent. Absoluta Volat. Baja» ≠ «Global Equity Large Cap» del lote: rankings no comparables con fondos de RV global puros.
- Divisa USD sin cubrir para un inversor EUR: añade volatilidad EUR/USD (en 2022 jugó a favor; en 2025 y 2026 la clase cubierta va por delante en YTD).
- Alpha negativo vs benchmark a 1A/3A/5A (Finect) pese a los buenos quintiles VDOS: la categoría de comparación no es el MSCI World.
- TER 1,67 % alto para un perfil defensivo frente a indexados de mínima volatilidad.
- quefondos convierte las series a EUR: al ser la clase ya EUR no hay efecto divisa de conversión, pero el fondo subyacente es USD.

**Decisión.** AB Low Volatility A EUR; 2024 Q1; patrimonio de clase discrepante entre fuentes

### MyInvestor Cartera Permanente — `ES0156572002`

**Identidad y operativa.** Andbank Wealth Management, SGIIC, S.A. · clase `mixtos` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Mixto cartera permanente (regla fija). Importe: 10.000 €. Ficha: `finance/fondos-myinvestor/mixtos/ES0156572002.md`.

**Coste y mínimos.** TER snapshot **0,59 %** (0,59 % (snapshot app; coincide con gastos corrientes 0,590 % de Finect)); gestión 0,50 % fija (quefondos y Finect); éxito 0,00 % variable (quefondos); n/a (Finect); mínimo publicado "0,00 EUR (quefondos); mínimo a mantener 0,00 EUR"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 114.877.

**Exposición y evidencia.** RV 24,34 % · RF 44,16 % · duración estimada 5.0 · 3A 10,33 % · 5A 3,25 % · vol 6,56 % · SRRI 3. Patrimonio: Pendiente.

**Sectores.** Servicios financieros (5,85 % del fondo), Industrial (4,00 %), Tecnología (3,43 %), Salud (2,53 %), Materiales básicos (2,08 %), Consumo cíclico (1,74 %), Consumo defensivo (1,50 %), Energía (1,23 %), Comunicación (1,10 %), Utilities (0,50 %), Inmobiliario (0,38 %).

**Quién es y para qué sirve.** Fondo de autor con alta vinculación al gestor D. Rafael Ortega Salvador que replica la filosofía de la **cartera permanente**: evitar cambios en la asignación de activos, mantener estable el perfil de riesgo y reducir la rotación — «por lo que no realiza una gestión activa» (política según quefondos, pese a la etiqueta «activa» del snapshot). Invierte 0–100 % del patrimonio en IICs (armonizadas o no, del grupo o no de la gestora): 15–35 % de la exposición total en RV de cualquier capitalización, 15–35 % en materias primas (en la práctica, oro físico vía ETCs) y el resto en RF de al menos media calidad crediticia en el momento de la compra, incluidos depósitos e instrumentos monetarios. Riesgo divisa 0–100 %; sin predeterminación de emisor, duración, divisas ni sectores. Referencia: Barclays EUR Aggregate Total Return (75 %) + FTSE World Total Return (25 %). Categoría VDOS «Mixto Flexible …

**Lectura para cartera (texto de la ficha).** Núcleo defensivo «todo terreno»: la cartera permanente clásica (~25 % RV global + ~25 % oro + ~25 % RF larga + liquidez, aquí 24 % RV / 23-28 % oro / 44 % RF / 4 % caja) está diseñada para comportarse razonablemente en cualquier régimen — crecimiento, inflación, deflación, recesión — sin apostar por uno. Encaja como posición central de una cartera conservadora (SRRI 3, volatilidad 1A 8,2 %) o como contrapeso «anti-escenario» junto a RV pura: el oro cubre inflación persistente y riesgo geopolítico, la RF larga cubre recesión/deflación, la RV cubre crecimiento. Es el fondo del lote con filosofía …

**Pegas detectadas.**
- RF larga con el BCE subiendo: 44,16 % en renta fija con posiciones de cupón alto y vencimiento largo (España 5,15 %); duración agregada no publicada. Es el tramo que más sufre en el escenario actual; 2022 ya cayó -12,76
- Fondo de autor: vinculación a Rafael Ortega Salvador (política quefondos); riesgo de persona clave aunque la filosofía sea estática.
- La etiqueta «gestión activa» del snapshot engaña: la política dice expresamente que «no realiza una gestión activa» (asignación permanente estable, baja rotación, vía ETFs/ETCs).
- Categoría divergente: VDOS «Mixto Flexible» vs Morningstar «Mixtos Defensivos EUR - Global» (snapshot «Cautious Allocation»): los rankings VDOS comparan contra fondos más agresivos.
- Beta 1,14–1,48 vs benchmark (Finect), alta para un defensivo: el benchmark 75 % Barclays EUR Aggregate + 25 % FTSE World no representa bien el ~23 % de oro.
- Comisión de depósito divergente: 0,07 % (quefondos) vs 0,100 % custodia (Finect).
- Fecha de constitución divergente: 01/08/2017 (quefondos) vs 22/09/2017 (registro CNMV y Finect).
- Sharpe 1A bajo (0,41) y 5A (0,28): el buen 3A (1,23) depende del gran ciclo del oro 2024-2025; no extrapolar.
- Invierte hasta 100 % vía IICs de terceros: verificar en el folleto que el TER 0,59 % incluye los costes de los ETFs/ETCs subyacentes.

**Decisión.** MyInvestor Cartera Permanente; 27.87% otros ≈ oro físico ETC; RF larga; fondo de autor (R. Ortega)

### Cobas Renta FI — `ES0119207001`

**Identidad y operativa.** Cobas Asset Management · clase `mixtos` · fuente `mcp` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Mixto defensivo value activo. Importe: 10.000 €. Ficha: `finance/fondos-myinvestor/mixtos/ES0119207001.md`.

**Coste y mínimos.** TER snapshot **0,31 %** (0,33 %); gestión —; éxito —; mínimo publicado "100.00 EUR"; mínimo operativo verificado: **MCP ficha: 100 EUR**. NAV 138.518.

**Exposición y evidencia.** RV 14,50 % · RF 57,50 % · duración estimada 2.0 · 3A 8,81 % · 5A 6,82 % · vol 2,85 % · SRRI 3. Patrimonio: Pendiente.

**Regiones.** Alemania (41,6 %), Noruega (9,0 %), España (7,4 %), Ghana (3,9 %), Estados Unidos (2,1 %), Reino Unido (1,6 %)

**Sectores.** Gobierno (61,7 %), Bonos corporativos (16,6 %), Efectivo y equivalentes (7,2 %), Energía (4,4 %), Industria (4,0 %), Salud (3,7 %)

**Quién es y para qué sirve.** Fondo mixto con foco en Alemania, de gestión activa, comercializado en MyInvestor en clase de acumulación (EUR). Fecha de lanzamiento de la clase: 2017-03-03. > Obtener una rentabilidad satisfactoria y sostenida en el tiempo aplicando una filosofía de inversión value. Invierte hasta un 15% en renta variable y el resto en renta fija, principalmente pública y hasta un 25% en deuda privada, en este caso de compañías ya conocidas y analizadas por la gestora en sus carteras de renta variable.

**Lectura para cartera (texto de la ficha).** Bolsa y bonos combinados en un solo fondo: perfil intermedio y delegación del reparto entre activos. Ojo al solapamiento: la parte de bolsa cuenta como renta variable a efectos del perfil de riesgo de la cartera. *Orientación general derivada de la clasificación del catálogo; no es una recomendación de inversión.*

**Decisión.** Cobas Renta FI; 2022 +3.89%; vol 3A 2.85%; MCP TER 0.33 vs snapshot 0.31

### Twelve Capital UCITS ICAV - Twelve Cat Bond Fund P EUR Acc — `IE00BD2B9710`

**Identidad y operativa.** Twelve Capital (UK) Limited · clase `renta-fija` · fuente `mcp` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Cat bonds (alternativo descorrelacionado). Importe: 5.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/IE00BD2B9710.md`.

**Coste y mínimos.** TER snapshot **1,30 %** (1,28 %); gestión 1,10 %; éxito —; mínimo publicado "1.00 EUR"; mínimo operativo verificado: **MCP ficha: 1 EUR**. NAV 142.42.

**Exposición y evidencia.** RV 0,00 % · RF 92,20 % · duración estimada 0.5 · 3A 9,27 % · 5A 6,95 % · vol 2,26 % · SRRI 2. Patrimonio: Pendiente.

**Regiones.** Islas Bermudas (43,3 %), Estados Unidos (37,3 %), Reino Unido (3,7 %), Irlanda (3,1 %), Singapur (1,3 %), Australia (1,0 %)

**Sectores.** Bonos corporativos (89,0 %), Gobierno (9,0 %), Efectivo y equivalentes (1,1 %), Gobierno Relacionado (1,0 %)

**Quién es y para qué sirve.** Fondo de renta fija con foco en Islas Bermudas, USA, de gestión activa, comercializado en MyInvestor en clase de acumulación (EUR). Fecha de lanzamiento de la clase: 2018-02-16.

**Lectura para cartera (texto de la ficha).** Tramo defensivo o de rentas de la cartera: aporta estabilidad frente a la bolsa y sensibilidad a los tipos de interés. El riesgo concreto depende del emisor (gubernamental o corporativo), la duración y la calidad crediticia que se detallan en la composición. *Orientación general derivada de la clasificación del catálogo; no es una recomendación de inversión.*

**Decisión.** Twelve Cat Bond P EUR; MCP TER 1.28 vs snapshot 1.30; reembolso ~10 días (repo)

### Jupiter Merian Global Equity Absolute Return Fund L (EUR) Hedged Acc — `IE00BLP5S460`

**Identidad y operativa.** Jupiter Asset Management (Europe) Limited · clase `alternativos` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Market neutral RV (alternativo). Importe: 5.000 €. Ficha: `finance/fondos-myinvestor/alternativos/IE00BLP5S460.md`.

**Coste y mínimos.** TER snapshot **1,55 %** (1,55 % (snapshot app)); gestión 1,50 % fija (quefondos); éxito 20,00 % sobre resultados positivos anuales entre el fondo y la alta watermark (HWM) (quefondos); mínimo publicado "500,00 EUR (quefondos)"; mínimo operativo verificado: **web ficha: 500 EUR**. NAV 1.963.

**Exposición y evidencia.** RV 44,09 % · RF 23,00 % · 3A 10,12 % · 5A 9,68 % · SRRI 2. Patrimonio: Patrimonio: 2.537,65 M€.

**Sectores.** Financial Services 27,31/19,46 · Technology 24,37/17,42 · Industrials 21,57/15,70 · Consumer Cyclical 18,85/11,68 · Healthcare 18,12/6,93 · Communication Services 10,50/4,36 · Basic Materials 10,05/7,33 · Consumer Defensive 6,68/4,72 · Energy 6,33/5,41 · Real Estate 4,82/2,48 · Utilities 3,38/2,13.

**Quién es y para qué sirve.** Fondo de rentabilidad absoluta que busca el incremento de capital con un estrecho control del riesgo y una correlación baja con los mercados de renta variable y de renta fija, estructurado como una cartera neutral respecto al mercado (quefondos). Toma posiciones largas en valores de renta variable global de larga capitalización que espera que mejoren relativamente y cortas en los que espera que empeoren; al menos el 51 % del valor liquidativo se invierte directamente en renta variable, e incorpora un factor ASG explícito en la construcción de cartera. Su referencia es el tipo efectivo de los fondos federales de EE. UU. (US Effective Federal Funds Rate). Constituido el 03/06/2014. Patrimonio: 2.537,65 M€ (quefondos, 18/11/2026); Finect atribuye 12.678,74 M€ al fondo completo (la diferencia sugiere clase frente a conjunto de clases). Clase de acumulación («Acc»).

**Lectura para cartera (texto de la ficha).** Satélite de rentabilidad absoluta con perfil market neutral: busca rentabilidad positiva con baja correlación a la bolsa y los bonos, por lo que encaja como diversificador en una cartera de renta variable y fija, no como núcleo. Su historial es de los más consistentes de la categoría, con resultados positivos en casi todos los años naturales y un control del riesgo que se refleja en un SRRI bajo (2/7) y una volatilidad contenida (5,12 % a 1 año, quintil 4 de volatilidad, es decir, segundo tramo menos volátil). Para un perfil que quiera reducir la dependencia del mercado sin renunciar a un reto …

**Pegas detectadas.**
- TER 1,55 % (snapshot) más comisión de éxito del 20 % sobre resultados positivos anuales con alta watermark: coste total elevado en años buenos.
- Patrimonio: quefondos 2.537,65 M€ frente a Finect 12.678,74 M€; la discrepancia de ámbito (clase vs fondo completo) es grande y no se ha resuelto con las fuentes consultadas.
- La rentabilidad acumulada a 3 y 5 años de quefondos (33,55 % y 58,69 %) no es anualizada; no debe confundirse con el 10,12 % y 9,68 % anualizados del snapshot.
- Rentabilidades web de quefondos a 18/11/2026, un día antes del snapshot.
- El benchmark que publica quefondos (US Effective Federal Funds Rate) no es el que usa Finect, que no declara benchmark; la comparación de alpha/beta es sobre el benchmark de Finect.

**Decisión.** Jupiter Merian Abs Return L EUR H; éxito 20% HWM; 3A Q1

### MontLake DUNN WMA Institutional UCITS Fund EUR Retail Class Pooled Shares — `IE00BWVFLK42`

**Identidad y operativa.** DUNN Capital Management, LLC · clase `alternativos` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Managed futures (alternativo). Importe: 5.000 €. Ficha: `finance/fondos-myinvestor/alternativos/IE00BWVFLK42.md`.

**Coste y mínimos.** TER snapshot **1,34 %** (1,34 % (snapshot app; Finect no informa de comisión)); gestión Pendiente; éxito Pendiente (no consta en las fuentes consultadas); mínimo publicado "Pendiente"; mínimo operativo verificado: **MCP 20/11: 1.000 EUR**. NAV 128.197.

**Exposición y evidencia.** RV 0,00 % · RF 0,00 % · 3A 4,51 % · 5A 5,29 % · vol 9,92 % · SRRI 3. Patrimonio: patrimonio de 762,40 M€.

**Regiones.** Pendiente.

**Sectores.** Pendiente (el fondo opera con futuros, opciones, swaps y contratos de divisas; Finect no publica composición).

**Quién es y para qué sirve.** Fondo UCITS de seguimiento de tendencias (trend following) gestionado por DUNN Capital Management. Finect lo clasifica como «Systematic Trend USD» y describe una aproximación sistemática y disciplinada para identificar y seguir tendencias en una amplia gama de mercados y clases de activos, con énfasis en los denominados en dólares estadounidenses, utilizando modelos cuantitativos para capturar movimientos direccionales en divisas, materias primas, renta variable y renta fija. El KID de la clase EUR Retail de la misma familia (IE00B6R2T818) indica que las participaciones no pagan ingresos y que el fondo los reinvierte. El NAV de cierre de Finect es de 127,6396 EUR a 18/11/2026, con un patrimonio de 762,40 M€ para el fondo. La política no detalla benchmark de referencia en la fuente consultada.

**Lectura para cartera (texto de la ficha).** Satélite alternativo de seguimiento de tendencias: su objetivo es capturar movimientos direccionales en divisas, materias primas, renta variable y renta fija a través de derivados, con independencia de la dirección del mercado. Su papel en cartera es la descorrelación y la cobertura de colas en episodios de tendencias fuertes (inflación persistente, estrés geopolítico), no la estabilidad ni la liquidez. Encaja en perfiles que aceptan volatilidad alta y un historial irregular a cambio de una fuente de retorno no direccional. La evidencia reciente es desigual: snapshot 1A 8,18 %, 3A 4,51 % anual …

**Pegas detectadas.**
- quefondos no dispone de la ficha: la URL de escritorio devuelve 404 y la versión móvil indica que el fondo con ISIN IE00BWVFLK42 no está disponible. No hay datos de rentabilidades por año natural, composición, comisiones
- SRRI muy discrepante: snapshot 3, Finect 7.
- Rating discrepante: snapshot 4 ★, Finect Morningstar 3 ★.
- Finect no publica composición ni top posiciones para este fondo (estrategia de derivados); la exposición real no es observable en las fuentes.
- El texto estratégico que muestra Finect cita el ISIN IE00B6R2TD68 (otro compartimento de la misma familia), por lo que está desactualizado; el ISIN de la página coincide con el del lote.
- Sin detalle de comisión de gestión, de éxito ni mínimos en Finect; el TER del snapshot es del 1,34 %.
- NAV con fechas distintas: snapshot 128,197 (19/11) y Finect 127,6396 (18/11).

**Decisión.** DUNN WMA EUR Retail; MCP TER 1.08 + éxito 25% vs snapshot 1.34; se presupuesta 1.34 + 25%; 2022 +24.6%

### DWS Euro Ultra Short Fixed Inc NC — `LU0080237943`

**Identidad y operativa.** DWS Investment S.A. (Deutsche Bank) · clase `renta-fija` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RF euro ultracorta activo. Importe: 12.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/LU0080237943.md`.

**Coste y mínimos.** TER snapshot **0,15 %** (0,15 % (snapshot app; gastos corrientes 0,150 % Finect; ongoing charge 0,15 % FT)); gestión 0,10 % (quefondos fija; Finect 0,100 %; FT «Max annual charge» 0,10 %); éxito 0,00 % (quefondos variable); n/a (Finect); mínimo publicado "0,00 EUR (quefondos). Mínimo de MyInvestor: Pendiente"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 85.97.

**Exposición y evidencia.** RV 0,00 % · RF 100,00 % · duración estimada 0.5 · 3A 3,38 % · 5A 2,37 % · SRRI 1. Patrimonio: Pendiente.

**Regiones.** Pendiente en %; por política, emisores OCDE/G20/UE/Singapur con bonos en EUR o cubiertos

**Sectores.** Pendiente (Finect no renderiza la composición; no publicado en quefondos)

**Quién es y para qué sirve.** Clase NC del DWS Euro Ultra Short Fixed Income Fund (Luxemburgo, FCP; subfondo de DWS Invest). Fondo activo cuyo objetivo es generar la mayor apreciación posible del capital a corto plazo: **al menos el 70 % del patrimonio en bonos** (de tipo fijo o variable, y convertibles) negociados en mercados regulados de países OCDE, G20, UE o Singapur, **denominados en euros o cubiertos frente al euro**, además de fondos de inversión (incluidos monetarios), depósitos e instrumentos del mercado monetario (política de quefondos). **Sin benchmark de referencia** (quefondos; Finect: «-»). Constituido el **12/05/1997** (quefondos, Finect y FT coinciden). Patrimonio de la clase: 915.615,94 miles de euros (~915,6 M€) a 17/11/2026 (quefondos; Finect: 912,7 M€); del fondo: 972,9 M€ (Finect). Categoría VDOS: **Monetario Euro**; Morningstar: EUR Ultra Short-Term Bond (FT) / RF Ultra Corto Plazo EUR (Finect). …

**Lectura para cartera (texto de la ficha).** Papel de **liquidez remunerada / defensivo ultra corto** en euros: SRRI **1** en el snapshot (el más bajo) y volatilidad 1A de solo 0,23 % (quefondos, quintil 2 de su categoría). Para aparcar dinero con carry por encima del monetario medio y vaivén mínimo, o como colchón de liquidez de una cartera. **No es un monetario garantizado**: VDOS lo clasifica como Monetario Euro, pero es un fondo de bonos ultra cortos con crédito y convertibles, y en 2022 fue **el último de su categoría** (−1,61 %, ranking 84/84, quintil 5) mientras la categoría caía solo −0,25 %. La evidencia es excelente en el ciclo …

**Pegas detectadas.**
- 2022: último de su categoría (−1,61 %, ranking 84/84, quintil 5, vs −0,25 % de la categoría Monetario Euro). Aunque la duración sea ultra corta, el crédito/convertibles puede hacerlo perder; no es liquidez garantizada pe
- Comisión de reembolso discrepante: 2,500 % (Finect) y 2,50 % exit charge (FT) vs 0,00 % (quefondos). Si se aplicara, penaliza el uso como liquidez táctica; verificar condiciones reales en MyInvestor.
- Sin benchmark ni composición pública: duración efectiva, rating y pesos reales Pendiente; Finect no renderiza la composición (JS). La política admite bonos convertibles y no explicita límite de rating en el extracto de q
- Categorías distintas entre fuentes: VDOS Monetario Euro vs Morningstar EUR Ultra Short-Term Bond; en el lote figura como renta fija (Europe Fixed Income). Los rankings de quefondos son vs monetarios.
- YTD 2026: snapshot 2,15 % vs quefondos 2,14 % (redondeo/fecha); NAV quefondos 85,96 (17/11) vs snapshot/Finect 85,97. Manda el snapshot.
- TER 0,15 % coincide en snapshot, Finect y FT; gestión 0,10 % en las tres fuentes.

**Decisión.** DWS Euro Ultra Short NC; 2022 último de categoría (−1.61%); exit fee 2.5% discrepante — verificar

**Verificación web 20/11/2026.** KID oficial DWS de 16/02/2026: «No fees or penalties will be charged by the company for any such transaction», periodo recomendado 183 días, riesgo 1/7 y beneficios reinvertidos. El 2,50 % que publicaban Finect y FT no aparece en el KID; se conserva como discrepancia a verificar en pantalla, no como coste modelado. <https://download.dws.com/download/asset/4b9b6e74-8baa-46ae-971a-c9895905b477?tenant=ActiveEmea>

### Santalucía Renta Fija Corto Plazo Euro MY — `ES0170156048`

**Identidad y operativa.** Santalucía Asset Management SGIIC · clase `renta-fija` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RF corto plazo euro activo. Importe: 10.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/ES0170156048.md`.

**Coste y mínimos.** TER snapshot **0,13 %** (0,13 % (snapshot app; gastos corrientes 0,130 % Finect)); gestión 0,10 % (quefondos fija; Finect 0,100 %); éxito 0,00 % (quefondos variable); n/a (Finect); mínimo publicado "0,00 EUR; mínimo a mantener 0,00 EUR (quefondos). Mínimo de MyInvestor: Pendiente"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 16.383.

**Exposición y evidencia.** RV 0,00 % · RF 100,00 % · duración estimada 1.0 · 3A 3,28 % · 5A 2,27 % · SRRI 2. Patrimonio: Pendiente.

**Regiones.** principalmente Europa, en menor medida otros OCDE, hasta 10 % emergentes (límites de política, no pesos reales)

**Sectores.** Pendiente (Finect no renderiza la composición; no publicado en quefondos)

**Quién es y para qué sirve.** Clase MY del Santalucía Renta Fija Corto Plazo Euro, FI (España, fondo armonizado según CNMV). Fondo activo que promueve características medioambientales o sociales y mantiene el **100 % de la exposición en renta fija pública y/o privada** (incluidos depósitos e instrumentos del mercado monetario, líquidos): emisores principalmente europeos y en menor medida OCDE, hasta un 10 % puntual en emergentes, **sin predeterminación de calificación crediticia** (puede estar toda la cartera en baja calidad crediticia), **duración media ≤ 1 año** y riesgo divisa ≤ 5 % (política de quefondos). Referencia compuesta: ECB ESTR OIS 50 % + Bloomberg Euro Aggregate 1-3 Year TR Unhedged EUR 47 % + Bloomberg Pan-European High Yield (Euro) TR Unhedged EUR 3 % (quefondos y Finect). El fondo se constituyó el **30/01/2001** (quefondos); el ISIN de la clase MY se emitió el **01/10/2021** (CNMV); Finect publica «f …

**Lectura para cartera (texto de la ficha).** Papel de **liquidez remunerada / defensivo de corto plazo** en euros: duración ≤ 1 año, volatilidad 1A de solo 0,61 % (quefondos) y SRRI 2 en el snapshot. Para un inversor que quiere aparcar dinero con más carry que una cuenta y menos vaivén que la renta fija larga, o como colchón de liquidez dentro de una cartera. Ojo: no es un monetario puro ni está garantizado — la política permite hasta un 100 % en baja calidad crediticia y un 3 % del benchmark es high yield; el −1,85 % de 2022 muestra que puede perder en años de estrés. La evidencia es muy buena con historial suficiente (clase MY desde oc …

**Pegas detectadas.**
- Sin límite de calidad crediticia por política: puede estar toda la cartera en baja calidad crediticia (high yield); hasta 10 % emergentes y 5 % divisa. El −1,85 % de 2022 (mejor que la categoría, pero negativo) muestra q
- Fechas de inicio discrepantes: fondo 30/01/2001 (quefondos), «fecha de inicio» 27/04/2010 (Finect), ISIN de la clase MY emitido el 01/10/2021 (CNMV). La clase MY tiene ~5 años; la serie de 5 años de quefondos coincide co
- Clase pequeña: ~10,8 M€ (quefondos) / 11,0 M€ (Finect) de un fondo de ~291,5 M€.
- Comisión de depósito discrepante: 0,03 % (quefondos) vs 0,025 % custodia (Finect). TER 0,13 % coincide entre snapshot y Finect; manda el snapshot.
- Composición real no disponible: Finect no renderiza la composición (JS); pesos por activo, sectores, regiones, top posiciones, duración efectiva y rating reales quedan Pendiente (solo límites de política).
- Volatilidad 1A en quintil 4 vs su categoría (0,61 %): algo más volátil que la media de RF Euro Corto Plazo, aunque muy baja en absoluto.
- Política de acumulación tomada del snippet de FT («Income treatment: Accumulation»); ni quefondos ni el extracto de Finect la publican.

**Decisión.** Santalucía CP Euro MY; sin límite de calidad por política; clase ~10.8 M€

### AXA World Funds - Global Inflation Short Duration Bonds A Capitalisation EUR (Hedged) — `LU1353950725`

**Identidad y operativa.** BNP Paribas Asset Management (AXA World Funds) · clase `renta-fija` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Ligado a inflación global corto cubierto EUR. Importe: 6.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/LU1353950725.md`.

**Coste y mínimos.** TER snapshot **0,75 %** (0,75 % (snapshot app; coincide con gastos corrientes 0,750 % en Finect)); gestión 0,50 % (quefondos: fija 0,50 %; Finect: 0,500 %); éxito no (0,00 % variable en quefondos; n/a en Finect); mínimo publicado "0,00 USD según quefondos (sin mínimo efectivo publicado)"; mínimo operativo verificado: **web ficha: 0.00 USD**. NAV 106.35.

**Exposición y evidencia.** RV 0,00 % · RF 95,00 % · duración estimada 2.0 · 3A 1,89 % · 5A 0,30 % · vol 2,09 % · SRRI 2. Patrimonio: patrimonio de la clase 132,35 M€.

**Regiones.** Pendiente (emisión OCDE según política; sin desglose regional en la fuente).

**Sectores.** Pendiente (la fuente no desglosa sectores; cartera de bonos ligados a la inflación y derivados).

**Quién es y para qué sirve.** Subfondo de la SICAV luxemburguesa AXA World Funds que busca rendimiento en USD a partir de una cartera de bonos vinculados a la inflación de corta duración gestionada activamente, invirtiendo principalmente en bonos ligados a la inflación emitidos por gobiernos, instituciones públicas o empresas de países de la OCDE (política según quefondos). Su referencia es el Bloomberg World Govt Inflation-Linked 1-5 Yrs Hedged USD. Esta clase es de acumulación en EUR con divisa cubierta. Constituido el 16/02/2016; patrimonio de la clase 132,35 M€ según quefondos a 17/11/2026 (Finect sitúa el patrimonio total del fondo en ~1.397,6 M€).

**Lectura para cartera (texto de la ficha).** Papel de satélite defensivo con cobertura de inflación: renta fija global ligada a la inflación de duración corta y divisa cubierta a EUR, para quien quiere proteger el poder adquisitivo de la parte conservadora de la cartera sin añadir riesgo de tipo de cambio ni de duración larga. No es un fondo de liquidez ni un núcleo de renta fija convencional: su motor es la inflación realizada, no el carry nominal. La evidencia es mixta pero con un punto fuerte claro: en 2025 batió a su categoría VDOS (RFI Global Ligada a la Inflación) con +2,96 % frente a -0,18 % (ranking 19/141, quintil 1), y en el sh …

**Pegas detectadas.**
- SRRI discrepa: snapshot 2 vs Finect 3; manda el snapshot.
- Comisión de depósito/custodia discrepa: quefondos 0,00 % vs Finect 0,050 %.
- Comisión de suscripción de hasta 3,00 % en folleto (quefondos/Finect); comprobar si MyInvestor la aplica.
- Último año y YTD 2026 por detrás de la categoría (quintil 3); Sharpe 1A negativo.
- Cartera intensiva en derivados: largos/cortos elevados en bonos y caja, futuros sobre Schatz/Bobl; el desglose de asset-allocation no es una foto «limpia» de tenencias.
- quefondos etiqueta la gestora como BNP Paribas Asset Management (gama AXA WF integrada en BNP Paribas AM); Finect: BNP PARIBAS ASSET MANAGEMENT Europe.
- Datos de cartera Finect a 31/07/2026 (3 meses de antigüedad respecto al snapshot).

**Decisión.** AXA Global Inflation Short Duration A EUR H; 2025 Q1

### Ofi Invest ISR Monétaire CT E — `FR0010738229`

**Identidad y operativa.** Abeille Vie · clase `monetarios` · fuente `mcp` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Monetario EUR. Importe: 7.000 €. Ficha: `finance/fondos-myinvestor/monetarios/FR0010738229.md`.

**Coste y mínimos.** TER snapshot **0,12 %** (0,06 %); gestión 0,11 %; éxito —; mínimo publicado "0.00 EUR"; mínimo operativo verificado: **MCP ficha: 0.00 EUR**. NAV 1131.52.

**Exposición y evidencia.** RV 0,00 % · RF 3,70 % · 3A 2,88 % · 5A 2,26 % · vol 0,24 % · SRRI 1. Patrimonio: Pendiente.

**Regiones.** Francia (1,9 %), Canadá (0,8 %), Estados Unidos (0,4 %), Luxemburgo (0,3 %), Bélgica (0,2 %), España (0,1 %)

**Sectores.** Efectivo y equivalentes (95,7 %), Bonos corporativos (3,5 %), Gobierno (0,0 %), Gobierno Relacionado (0,0 %)

**Quién es y para qué sirve.** Fondo monetario, de gestión activa, comercializado en MyInvestor en clase de acumulación (EUR). Fecha de lanzamiento de la clase: 1998-04-03.

**Lectura para cartera (texto de la ficha).** Aparcamiento de liquidez y fondo de emergencia: busca preservar el capital con volatilidad mínima y reembolso rápido. No es un motor de rentabilidad a largo plazo; su rendimiento sigue a los tipos del mercado monetario. *Orientación general derivada de la clasificación del catálogo; no es una recomendación de inversión.*

**Pegas detectadas.**
- El TER publicado (0,06 %) es inferior a la comisión de gestión (0,11 %): dato rebajado o estimado; el coste real puede ser mayor.

**Decisión.** Ofi Invest ISR Monétaire CT E; TER ficha MCP 0.06 < gestión 0.11 (pega); snapshot 0.12 manda

## C5 — 11 fondos

### Vanguard Global Stock Index Fund EUR Acc — `IE00B03HD191`

**Identidad y operativa.** Vanguard Group (Ireland) Limited · clase `rv-global` · fuente `listado-app` · indexada · divisa EUR · política **acumulacion**. Rol en la cartera: Núcleo MSCI World indexado. Importe: 35.000 €. Ficha: `finance/fondos-myinvestor/rv-global/IE00B03HD191.md`.

**Coste y mínimos.** TER snapshot **0,18 %** (0,18 % (snapshot app); gastos corrientes Finect 0,180 %; ratio de costes netos Morningstar 0,18 %); gestión 0,18 % (quefondos «fija»; Finect 0,180 %); éxito 0,00 % (quefondos «variable»); n/a (Finect); mínimo publicado "1.000.000,00 EUR (quefondos, mínimo de folleto de la clase); operativa real en MyInvestor: Pendiente"; mínimo operativo verificado: **MCP 20/11: 1.00 EUR**. NAV 63.55.

**Exposición y evidencia.** RV 99,96 % · RF 0,00 % · 3A 17,44 % · 5A 10,02 % · vol 11,16 % · SRRI 4. Patrimonio: **24.320,3 M€.

**Regiones.** Estados Unidos (72,77 %), Zona euro (7,92 %), Japón (5,92 %), Europa ex-euro (3,76 %), Reino Unido (3,34 %).

**Sectores.** Tecnología (32,56 %), Servicios financieros (15,46 %), Industria (10,49 %), Salud (9,20 %), Servicios de comunicación (8,39 %).

**Quién es y para qué sirve.** Fondo indexado que pretende reflejar la rentabilidad del **MSCI World Index** (acciones de medianas y grandes empresas de mercados desarrollados), invirtiendo en todos los valores del índice en su misma proporción (réplica completa) y, si no es posible, mediante muestreo; permanece plenamente invertido salvo condiciones extraordinarias (política de quefondos; Morningstar lo confirma: «full replication strategy»). Constituido el **10/12/2002** (quefondos y Finect). Patrimonio del fondo: **24.320,3 M€** y de la clase EUR Acc: **5.949,6 M€** (Finect a 18/11/2026); Morningstar da activos totales de 26.234,19 M USD y patrimonio de la serie de 5.897,96 M€ a 18/11/2026 (misma magnitud, distinta divisa/fecha). Categoría VDOS: **RVI GLOBAL**; Morningstar: **RV Global Cap. Grande Blend**. Fondo indexado: sí (Finect). Benchmark del fondo: MSCI World NR USD (Morningstar).

**Lectura para cartera (texto de la ficha).** Papel de **núcleo de renta variable global** para un inversor pasivo a largo plazo: un solo fondo da exposición a ~1.500 empresas de mercados desarrollados (según el análisis de Finect, el índice ronda esa cifra) con réplica completa y TER del 0,18 %, de los más baratos del mercado. Encaja como posición central de una cartera indexada, complementada si se quiere con emergentes o small cap, que el MSCI World no cubre. La evidencia es sólida y consistente: VDOS lo sitúa en **quintil 1 en 2024** (+26,50 % vs +21,35 % de categoría, ranking 309/2837) y **quintil 2 en 2022, 2023, 2025 y lo que va de …

**Pegas detectadas.**
- YTD 2026 web divergente entre fuentes: quefondos 14,77 % (a 17/11), snippet Finect +16,13 %, Morningstar 14,59 % (a 18/11). El snapshot (14,59 %) coincide con Morningstar y manda. El 1A de quefondos (16,75 %) también dif
- Concentración: EE. UU. 72,77 %, tecnología 32,56 %, cinco primeras posiciones 20,16 % (cartera a 30/09/2026). Indexarse al MSCI World es hoy casi comprar un índice de EE. UU. (análisis de Finect).
- Cobertura incompleta del mercado global: MSCI World solo desarrollados large/mid; sin emergentes ni small cap.
- Divisa: clase EUR sin cobertura declarada en las fuentes; exposición subyacente mayoritariamente USD → riesgo EUR/USD presente.
- Mínimo de folleto 1.000.000 € (clase institucional «General EUR Cap»); el mínimo real de MyInvestor no consta en la web.
- Volatilidad 1A en quintil 5 vs su categoría VDOS pese al riesgo 3A «inferior a la media» de Morningstar: las categorías VDOS y Morningstar no son comparables entre sí.
- Peaje de réplica: alfa 3A -0,10 vs MSCI World y +/-Ind negativo en 2025 (-1,1) y 2022 (-0,2) (Morningstar a 31/10/2026); es el coste esperado de un indexado, no un defecto de gestión.
- La composición no se renderiza en el extracto de Finect (2 intentos); se usa la ficha Morningstar (su proveedor de datos) a 30/09/2026.

**Decisión.** Vanguard Global Stock EUR Acc; warning señala iShares S (usado en C1, fondo distinto)

### T. Rowe Price Funds SICAV - US Blue Chip Equity Fund A (EUR) — `LU1438969195`

**Identidad y operativa.** T. Rowe Price (Luxembourg) Management S.à r.l. · clase `rv-usa` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV USA crecimiento activo. Importe: 8.000 €. Ficha: `finance/fondos-myinvestor/rv-usa/LU1438969195.md`.

**Coste y mínimos.** TER snapshot **1,61 %** (1,61 % (snapshot app; OGC 1,61 % y TER 1,62 % en Finect; FT y snippet Finect publican ongoing charge 1,65 % — ver Pegas)); gestión 1,50 % (quefondos: fija; Finect: 1,5 %); éxito 0,00 % (quefondos: variable); n/a en Finect; mínimo publicado "1.000 EUR (Finect); quefondos lista «0,00 USD» (divisa errónea, ver Pegas); FT: 833 GBP"; mínimo operativo verificado: **web ficha: 1.000 EUR (Finect)**. NAV 39.68.

**Exposición y evidencia.** RV 99,52 % · RF 0,00 % · 3A 15,55 % · 5A 5,96 % · vol 18,84 % · SRRI 5. Patrimonio: 618,9 M€.

**Sectores.** Tecnología 52,28 %; Servicios de comunicación 16,41 %; Consumo cíclico 12,38 %; Financiero 7,01 %; Salud 5,92 %; Industria 4,82 %; Utilities 0,38 %; Materiales 0,33 %.

**Quién es y para qué sirve.** Clase A en euros (acumulación, confirmada en FT) del subfondo US Blue Chip Equity de la SICAV luxemburguesa T. Rowe Price Funds — **misma cartera que la clase A USD (LU0133085943)**: sus rentabilidades publicadas son casi idénticas (1A 4,26 % EUR vs 4,17 % USD en el snapshot), lo que indica que **la clase EUR no está cubierta**, solo cambia la divisa de denominación. Política según quefondos: incrementar el valor de las acciones a largo plazo con una cartera diversificada y activamente gestionada de **blue chips estadounidenses de gran y mediana capitalización** (capitalización ≥ Russell Mid-cap / S&P Mid-cap 400), con posición de liderazgo, gestión experimentada y fundamentos sólidos; estilo growth (Finect: RV USA Cap. Grande Growth). Referencias: **S&P 500 Net 30 % WHT y Russell 1000 Growth Net 30 % WHT** (quefondos). Gestor: Paul D. Greene desde 01/10/2021 (FT). Constitución de esta c …

**Lectura para cartera (texto de la ficha).** **Papel:** satélite agresivo de renta variable USA growth, versión denominada en EUR para el inversor que prefiere no convertir divisa en la suscripción pero **asumiendo igualmente el riesgo EUR/USD** (clase no cubierta). Cartera muy concentrada en mega-cap tecnológicas (top 10 ~59 %, tecnología 52 %): es una apuesta activa por el liderazgo growth de T. Rowe Price, no un núcleo diversificado. Para perfiles con alta tolerancia al riesgo. **Evidencia:** historial de la clase desde 2016 (~10 años) con extremos marcados, calcado al de la USD: **quintil 1 en 2023 (+44,32 %) y 2024 (+44,01 %)** vs l …

**Pegas detectadas.**
- Clase EUR sin cobertura de divisa: rentabilidades casi idénticas a la clase A USD; el riesgo EUR/USD sigue presente pese a la denominación EUR.
- Concentración extrema: top 10 ~58,9 % (Finect 30/09/2026); tecnología 52,3 %; NVIDIA+Broadcom+AMD ~26,7 %.
- Volatilidad quintil 1 (la más alta de su categoría en 1A), máxima caída 5A −36,71 % (Finect) y −35,74 % en 2022 (quefondos).
- Alpha negativo a 1A/3A/5A (Finect, 31/10/2026); YTD 2026 y 1A en quintil 5 vs categoría VDOS.
- TER discrepante: snapshot/Finect OGC 1,61 % (TER 1,62 %) vs ongoing charge 1,65 % en FT y en el snippet de búsqueda de Finect; manda el snapshot (1,61 %).
- Mínimo y divisa discrepantes: Finect 1.000 EUR vs quefondos «0,00 USD» (etiqueta de divisa errónea en la ficha EUR) vs FT 833 GBP.
- Suscripción hasta 5,00 % (folleto); la operativa de MyInvestor puede diferir.
- Rating Morningstar 3 ★ (snapshot) pese a 4 estrellas VDOS.
- Composición a 30/09/2026 (Finect), tomada de la cartera común con la clase USD; puede no estar al día.

**Decisión.** T. Rowe US Blue Chip A EUR; top10 58.9%, tech 52.3%; 2026 YTD Q5; DD 5A −36.7%

### Polar Capital Global Technology Fund R EUR (Acc) — `IE00BM95B621`

**Identidad y operativa.** Polar Capital LLP · clase `sectoriales` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Satélite tecnología global activo. Importe: 7.000 €. Ficha: `finance/fondos-myinvestor/sectoriales/IE00BM95B621.md`.

**Coste y mínimos.** TER snapshot **1,58 %** (1,58 % (snapshot app); Finect publica gastos corrientes 1,59 %); gestión 1,50 % (quefondos y Finect); éxito 10 % (Finect); quefondos publica variable 0,00 % (discrepancia); mínimo publicado "0,00 EUR (quefondos); Finect: 0 €"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 32.2.

**Exposición y evidencia.** RV 94,48 % · RF 0,00 % · 3A 36,43 % · 5A 16,87 % · SRRI 5. Patrimonio: Patrimonio: 17.093,1 M€.

**Regiones.** EE. UU. 74,10 % · Asia desarrollada 17,37 % · Japón 3,53 % · Zona Euro 2,62 % · Canadá 1,64 %; países desarrollados ~100 %

**Sectores.** Tecnología 87,43 % · Servicios de comunicación 7,85 % · Industriales 4,50 % · Consumo cíclico 1,57 %

**Quién es y para qué sirve.** Clase en EUR de acumulación (R Accumulation) del Polar Capital Global Technology Fund, subfondo irlandés que busca valorización del capital a largo plazo con una cartera mundial de empresas tecnológicas: al menos dos tercios del activo en compañías relacionadas con la tecnología y al menos el 51 % de los activos brutos en renta variable directa, sin límites por región o país (quefondos). Benchmark: Dow Jones Global Technology Net Total Return (quefondos). Clase constituida el 01/07/2020 (quefondos; Finect indica 30/06/2020); el fondo gestiona desde 2009 a través de sus clases hermanas. Patrimonio: 17.093,1 M€ el fondo y 270,3 M€ esta clase (Finect, 19/11/2026); quefondos da 262.940,04 miles de € a 18/11/2026. Comparte cartera con IE00B433M743 (USD dist) e IE00B4468526 (EUR dist).

**Lectura para cartera (texto de la ficha).** Satélite agresivo de tecnología global y la clase más adecuada de las tres para acumular a largo plazo en EUR (no reparte dividendos). Para la parte de mayor riesgo de una cartera: 87,43 % tecnología, sesgo a semiconductores/IA, cortos (7,37 %) y opciones. La clase es joven (2020) pero ya tiene 5 años de historial propio y comparte la cartera y el equipo con clases que gestionan desde 2009. Evidencia de primer nivel. En quefondos (serie EUR): quintil 1 en 2023 (+47,90 %), 2024 (+39,42 %), 2025 (+34,76 %) y YTD 2026 (+29,70 %, ranking 35/885); en 2022 cayó −35,70 % (Q4, peor que el −31,17 % de …

**Pegas detectadas.**
- Clase joven: constituida el 01/07/2020 (quefondos) / 30/06/2020 (Finect); el historial de 5 años es de esta clase, el track record largo (2009) corresponde al fondo vía clases hermanas.
- Comisión de éxito del 10 % (Finect) frente al 0,00 % de variable que publica quefondos: discrepancia entre fuentes.
- TER: 1,58 % (snapshot) vs 1,59 % de gastos corrientes (Finect); además Finect publica un campo TER interno del 1,26 %. Manda el snapshot.
- Volatilidad extrema (46,94 % 1A, quintil 1 de volatilidad) y beta 1,47: correcciones fuertes esperables (−35,70 % en 2022; máxima caída a 5A −36,83 %).
- SRRI discrepante: 5 (snapshot) vs 7 (Finect). Rating discrepante: 4★ (snapshot) vs 5★ (Finect).
- Divisa de la cartera mayoritariamente USD (74,10 % EE. UU.) sin cubrir pese a cotizar en EUR; concentración ~87 % tecnología.
- Posiciones cortas (7,37 %) y opciones sobre acciones: gestión con derivados.
- Patrimonio de la clase modesto (270,3 M€) frente a los ~5.000 M€ de las clases de reparto hermanas.

**Decisión.** Polar Global Technology R EUR; éxito 10% (Finect) vs 0% quefondos — presupuestada; Q1 2023-2026

### BlackRock Global Funds - World Healthscience Fund A2 (EUR) — `LU0171307068`

**Identidad y operativa.** BlackRock (Luxembourg) S.A. · clase `sectoriales` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Satélite salud global activo. Importe: 6.000 €. Ficha: `finance/fondos-myinvestor/sectoriales/LU0171307068.md`.

**Coste y mínimos.** TER snapshot **1,81 %** (1,81 % (snapshot app; coincide con el ongoing charge del folleto de la clase A2 USD)); gestión 1,50 % (quefondos); Finect publica 1,37 % (discrepancia, ver Pegas); éxito no (quefondos: 0,00 %); mínimo publicado "5.000,00 USD o equivalente (quefondos); Finect: 0 €"; mínimo operativo verificado: **web ficha: 5.000 USD o equivalente (Finect 0)**. NAV 76.35.

**Exposición y evidencia.** RV 97,69 % · RF 0,00 % · 3A 10,50 % · 5A 5,88 % · SRRI 4. Patrimonio: 12.670,6 M€.

**Regiones.** EE. UU. 76,94 % · Europa (ex-zona euro) 11,71 % · Reino Unido 4,10 % · Zona euro 1,87 % · Oriente Medio 1,10 % · Asia emergente 1,20 % · Japón 0,79 % · países desarrollados 96,50 %

**Sectores.** Salud 97,69 % (único sector con peso).

**Quién es y para qué sirve.** Compartimento de BlackRock Global Funds que busca maximizar la rentabilidad total invirtiendo al menos el 70 % de los activos totales en renta variable global de empresas cuya actividad predominante es la atención sanitaria, la farmacia, la tecnología y los suministros médicos y el desarrollo de la biotecnología, con criterios ESG (artículo 8 del SFDR). Referencia: MSCI World Health Care (ND, USD). Es la clase A2 en euros del compartimento, constituida el 26/01/2004 (quefondos), dentro de un fondo creado el 06/04/2001. Patrimonio del fondo: 12.670,6 M€ (Finect, 19/11/2026); quefondos da 83.490,49 miles de € para la clase a 18/11/2026. Gestores: Erin Xie y Xiang Liu.

**Lectura para cartera (texto de la ficha).** La vía en euros al mismo compartimento de salud global de BlackRock, sin cobertura cambiaria declarada (la exposición a divisas se gestiona con flexibilidad). Sirve como núcleo posible de la parte sanitaria de una cartera global o como satélite sectorial de gran capitalización farmacéutica. No es un fondo defensivo al uso: concentra el 97,69 % en un sector y sus cuatro primeras posiciones pesan ~31 %, con names expuestos a la política de precios de medicamentos. Su historial es largo (la clase, desde 2004) y su volatilidad, moderada (16,76 % a 1 año). Evidencia irregular, con un 2026 bueno y u …

**Pegas detectadas.**
- NAV: el snapshot (76,35 EUR) reproduce el valor de quefondos a 18/11/2026, pero Finect cotiza 74,57 EUR a 19/11/2026 y BlackRock 77,28 EUR a 13/11/2026. Manda el snapshot.
- La clase es EUR sin cobertura declarada: la exposición neta a USD depende de la gestión flexible de divisas del compartimento, que no está cuantificada en las fuentes consultadas.
- Estadísticas de riesgo/retorno no publicadas por Finect para esta clase; los datos de beta y desviación proceden del folleto de la clase hermana USD (misma cartera).
- Comisión de gestión discrepante: 1,50 % (quefondos) vs 1,37 % (Finect).
- Concentración: 97,69 % en un solo sector; Eli Lilly + J&J + AbbVie + Merck suman 30,68 %.
- Datos de cartera a 30/09/2026 (Finect); quefondos a 18/11/2026.

**Decisión.** BGF World Healthscience A2 EUR; línea 6.000 € ≥ mínimo; 2025 Q5

**Verificación web 20/11/2026.** Ficha oficial BlackRock: «Class A2 (EUR) (Accumulating)», Minimum Initial Investment USD 5.000,00, Ongoing Charges 1,81 %, Management Fee 1,50 %, Performance Fee 0,00 %, desviación 3A 14,20 %, 2022 +0,6 %, 2025 +0,1 %. La línea de 6.000 € cubre el mínimo; el cargo inicial del 5 % del folleto se verifica en pantalla en la plataforma. <https://www.blackrock.com/se/professionals/products/229337/blackrock-world-healthscience-a2-eur-fund>

### Baillie Gifford Worldwide Emerging Markets Leading Companies Fund A EUR Acc — `IE00BK5TW610`

**Identidad y operativa.** Baillie Gifford Investment Management (Europe) Limited · clase `rv-emergentes` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV emergentes crecimiento activo. Importe: 7.000 €. Ficha: `finance/fondos-myinvestor/rv-emergentes/IE00BK5TW610.md`.

**Coste y mínimos.** TER snapshot **1,60 %** (1,60 % (snapshot app)); gestión 1,50 % (quefondos «fija»); éxito 0,00 % (quefondos «variable»); mínimo publicado "1.000,00 EUR (quefondos; puede variar por distribuidor)"; mínimo operativo verificado: **web ficha: 1.000 EUR**. NAV 17.074.

**Exposición y evidencia.** RV 99,47 % · RF 0,00 % · 3A 16,41 % · 5A 3,77 % · vol 19,82 % · SRRI 5. Patrimonio: patrimonio del fondo en 235,4 M€.

**Sectores.** Tecnología 42,06 %, Servicios financieros 13,05 %, Consumo cíclico 11,92 %, Servicios de comunicación 7,09 %, Materiales básicos 6,57 %, Energía 3,65 %, Industriales 3,42 %, Consumo defensivo 2,29 %.

**Quién es y para qué sirve.** Fondo irlandés de Baillie Gifford que busca maximizar el rendimiento total invirtiendo principalmente en empresas que obtienen una parte sustancial de sus ingresos o tienen una proporción sustancial de sus activos en uno o más países emergentes; no se propone concentrar las inversiones en ningún país, mercado o sector concreto (política recogida por quefondos y Finect). Su referencia es el MSCI Emerging Markets Index (quefondos). Constituido el 30/09/2019 (quefondos); clase A EUR de acumulación. Patrimonio: quefondos publica 2.633,84 miles de euros a 18/11/2026; Finect sitúa el patrimonio del fondo en 235,4 M€ (fecha no especificada). En la práctica la cartera está muy escorada a semiconductores y tecnología asiática (ver Composición).

**Lectura para cartera (texto de la ficha).** Satélite de crecimiento dentro de la parte de bolsa emergente: no es un emergente diversificado «de índice», sino una apuesta activa de convicción por compañías líderes, con más del 42 % en tecnología y casi un 30 % del top 10 en tres valores coreanos/taiwaneses de semiconductores. Encaja como posición táctica pequeña para perfiles que toleran volatilidad alta y quieren el sesgo growth/Asia que un indexado emergente estándar no da. La evidencia es mixta y muy cíclica: en 2025 batió a su categoría VDOS (18,95 % vs 19,30 %, ranking 564/1471, quintil 2) y en el último año destaca (23,05 % vs 18,3 …

**Pegas detectadas.**
- Concentración sectorial: tecnología 42,06 % de la cartera (Finect a 30/09/2026) y top 3 (TSMC, SK hynix, Samsung) ~29 %; riesgo de ciclo de semiconductores y geopolítico (Corea/Taiwán/China).
- Volatilidad 1A del 31,05 %, quintil 1 de volatilidad (de los más volátiles de su categoría); caída de -10,35 % en el último mes y -12,54 % en 3 meses (quefondos a 18/11/2026).
- Consistencia irregular: quintil 4 en 2022 y 2024; a 5 años acumulados queda por debajo de la categoría (quintil 3).
- NAV discrepante entre fuentes: snapshot 17,074 y quefondos 17,0736 (18/11) vs Finect 16,7719 (19/11); manda el snapshot. Posible desfase de fecha/serie en Finect.
- Rating Morningstar discrepante: 2★ (snapshot) vs 3★ (Finect); VDOS da 4★.
- Patrimonio: quefondos publica 2,63 M€ (18/11/2026, probablemente de la clase) frente a 235,4 M€ del fondo en Finect; tamaños de fuente distintos, sin fecha común.
- Divisa: clase en EUR pero con exposición total a divisas emergentes sin cubrir.
- quefondos (escritorio y móvil) y Finect consultados el 2026-11-19 con datos a 18-19/11/2026; la cartera de Finect es a 30/09/2026.

**Decisión.** BG EM Leading Companies A EUR; vol 31%, tech 42%; Q4 2022/2024

### Nordea 1 - Asia ex Japan Equity Fund BP EUR — `LU0173782102`

**Identidad y operativa.** Nordea Investment Funds SA · clase `rv-otros` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV Asia ex-Japón activo. Importe: 5.000 €. Ficha: `finance/fondos-myinvestor/rv-otros/LU0173782102.md`.

**Coste y mínimos.** TER snapshot **1,84 %** (1,84 % (snapshot app); gastos corrientes 1,840 % (Finect, coincide); campo «TER» Finect 1,04 % (ver Pegas)); gestión 1,50 % (quefondos «fija» y Finect); éxito 0,00 % (quefondos «variable»); n/a (Finect); mínimo publicado "0,00 EUR (quefondos y Finect); operativa real en MyInvestor: Pendiente"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 43.303.

**Exposición y evidencia.** RV 96,70 % · RF 0,00 % · 3A 18,16 % · 5A 5,73 % · vol 18,79 % · SRRI 4. Patrimonio: Patrimonio de la clase: **25,80 M€.

**Sectores.** Tecnología 42,06 %, Servicios financieros 18,47 %, Consumo cíclico 10,85 %, Industriales 9,94 %, Servicios de comunicación 6,23 %, Salud 3,44 %, Consumo defensivo 3,07 %, Inmobiliario 2,64 %.

**Quién es y para qué sirve.** Subfondo de Nordea 1 que busca crecimiento de la inversión a largo plazo: invierte **al menos el 75 % del patrimonio en renta variable** y valores relacionados emitidos por empresas domiciliadas o con la mayor parte de su actividad en Asia excluido Japón, seleccionando activamente las compañías con mejores perspectivas de crecimiento (quefondos). El snapshot lo nombra «NORDEA ASIAN FOCUS EQ BP EUR» (nombre antiguo de la gama); quefondos y Finect usan ya «Nordea 1 - Asia ex Japan Equity Fund BP EUR». Referencia: **MSCI All Country Asia Ex. Japan - Net Return** (quefondos). Constituido el **15/09/2003** (quefondos y Finect). Patrimonio de la clase: **25,80 M€** (quefondos a 18/11/2026) / 26,28 M€ (Finect); fondo: **95,44 M€** (Finect). Categoría VDOS: RVI ASIA EX-JAPÓN CRECIMIENTO; Morningstar (Finect): RV Asia (ex-Japón). Indexado: no.

**Lectura para cartera (texto de la ficha).** Papel de **satélite de renta variable Asia ex-Japón de gestión activa con el mejor historial relativo del lote**: quintil 1 en los acumulados 3A y 5A vs su categoría VDOS, y quintil 2 en casi todos los años naturales. Cartera más equilibrada que sus pares: 42 % tecnología (vs 44-79 % de otros del lote), 18,5 % financieras, 10,9 % consumo cíclico y presencia de mid/small caps (8,3 %). Encaja como diversificador regional de un núcleo global para perfiles con tolerancia alta a la volatilidad que quieran gestión activa con evidencia de batir a la categoría de forma sostenida. Clase BP retail sin m …

**Pegas detectadas.**
- TER más alto del lote: 1,84 % (snapshot/Finect) + suscripción de hasta el 5 % de folleto; la ventaja vs categoría debe medirse neta de costes.
- Rating divergente: snapshot 4★ vs Finect 3★ Morningstar y VDOS 2 estrellas. Manda el snapshot; metodologías y fechas distintas.
- Alfa negativo a 3A/5A pese a quintiles 1: Finect da alfa -1,40 (3A) y -1,26 (5A) con beta ~1,0: la ventaja acumulada frente a la categoría VDOS no se traduce en alfa positivo vs benchmark en esos períodos; el alfa 1A sí
- Comisiones discrepantes: quefondos depósito 0,00 % vs Finect custodia 0,120 %; el campo «TER» de Finect marca 1,04 % (probablemente clase limpia/retrocesión; no usado; OGC 1,84 % coincide con snapshot).
- Nombre distinto entre fuentes: snapshot «NORDEA ASIAN FOCUS EQ BP EUR» (gama antigua Asian Focus) vs quefondos/Finect «Nordea 1 - Asia ex Japan Equity Fund BP EUR»; mismo ISIN. La descripción de Finect aún dice «Extremo
- Concentración: tecnología 42,06 %, ~30 % en cuatro semiconductoras (TSMC/Samsung/SK hynix/MediaTek); top 10 ≈ 49,4 %.
- Tamaño de clase modesto: 25,80 M€ (quefondos) / 26,28 M€ (Finect); fondo 95,44 M€ (Finect) vs 79,7 M€ (snippet Finect antiguo).
- Divisa sin cubrir: clase EUR sobre subyacentes asiáticos.
- Snippet de Finect con cifras antiguas: «3A 11,39 %», «2026 +10,64 %», «5A +2,36 %» frente a INITIAL_STATE (3A 17,84 % a 19/11) y snapshot (3A 18,16 %): se usa INITIAL_STATE + snapshot.
- Reino Unido 1,02 % en regiones (Finect): posición residual no explicada por la fuente.
- 2025 fue su año más flojo vs categoría (quintil 3): la consistencia no es perfecta.

**Decisión.** Nordea Asia ex-Japan BP EUR; Q1 3A/5A trailing

### Goldman Sachs Europe CORE Equity Portfolio Base Acc EUR — `LU0234681749`

**Identidad y operativa.** Goldman Sachs Asset Management B.V. · clase `rv-europa` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: RV Europa core activo. Importe: 6.000 €. Ficha: `finance/fondos-myinvestor/rv-europa/LU0234681749.md`.

**Coste y mínimos.** TER snapshot **1,37 %** (1,37 % (snapshot app; Finect gastos corrientes 1,370 %: coinciden; factsheet GS a 31/12/2025: 1,41 %)); gestión 1,25 % (quefondos «fija»; Finect 1,250 %; factsheet GS 1,25 %); éxito no (quefondos «variable 0,00 %»; Finect n/a; factsheet GS «N/A»); mínimo publicado "5.000,00 EUR (quefondos)"; mínimo operativo verificado: **web ficha: 5.000 EUR**. NAV 40.05.

**Exposición y evidencia.** RV 99,71 % · RF 0,00 % · 3A 18,48 % · 5A 10,34 % · vol 10,20 % · SRRI 4. Patrimonio: Patrimonio: clase 811,9 M€.

**Sectores.** Servicios financieros 27,87 %, Industriales 18,79 %, Salud 12,59 %, Tecnología 10,73 %, Consumo cíclico 7,11 %, Consumo defensivo 6,19 %, Energía 4,58 %, Materiales básicos 3,77 %, Utilities 2,91 %, Servicios de comunicación 2,76 %, Inmobiliario 0,55 %.

**Quién es y para qué sirve.** Subfondo de Goldman Sachs Funds (SICAV luxemburguesa), clase Base de acumulación en EUR. Objetivo: revalorización del capital a largo plazo invirtiendo en acciones de compañías europeas (domiciliadas en Europa o con la mayor parte de sus beneficios/ingresos allí; puede invertir también en compañías de cualquier parte del mundo). Utiliza la **estrategia CORE, un modelo multifactor propio de Goldman Sachs** que busca predecir rendimientos de los valores; no puede invertir más de un tercio de sus activos en bonos corporativos o gubernamentales. Referencia: MSCI Europe (Total Return Net). Constitución de la clase: 14/11/2005 (quefondos y factsheet GS; Finect da 01/10/1999 como inicio del fondo). Patrimonio: clase 811,9 M€ (quefondos a 18/11/2026); fondo 7.711,9 M€ (Finect; el factsheet GS a 31/12/2025 daba 5.916 M€). Categoría VDOS: RVI Europa; Finect/Morningstar: RV Europa Cap. Grande Blend …

**Lectura para cartera (texto de la ficha).** Papel de **núcleo activo de renta variable europea large cap**: cartera muy diversificada (top 10 ~22-26 %), ~98 % Europa desarrollada, sesgo financiero/industrial (financieras 27,87 %), beta 0,87-0,96 y tracking error moderado (2,60 % a 3A, factsheet GS). Encaja como alternativa activa a un indexado MSCI Europe para quien quiera batir al índice con un modelo cuantitativo disciplinado, asumiendo un TER mayor. Historial largo: clase desde 2005, fondo desde 1999. La evidencia es **sólida y consistente**: quefondos (datos a 18/11/2026, categoría RVI Europa) da **Q1 en 3A acumulados** (66,32 % vs …

**Pegas detectadas.**
- SRRI discrepante: snapshot 4 vs Finect 5/7 y KIID antiguo categoría 5. Manda el snapshot; posible cambio de escala/fecha.
- TER: snapshot y Finect 1,37 % vs factsheet GS 1,41 % (a 31/12/2025): dato de cierre de ejercicio, puede incluir perímetro distinto. Manda el snapshot.
- Depósito/custodia discrepante: quefondos 0,00 % vs Finect 0,500 %. Anotado; el TER del snapshot ya recoge el coste total.
- Costes de transacción del modelo cuantitativo: 0,31 % (factsheet GS), turnover 146 %: el TER no recoge todo el coste de rotación.
- Suscripción hasta 5,50 % y mínimo publicado de 5.000 EUR: verificar condiciones reales en MyInvestor.
- Fechas de inicio distintas: clase 14/11/2005 (quefondos/GS) vs fondo 01/10/1999 (Finect).
- El modelo CORE es propietario y opaco («multifactor que busca predecir rendimientos»): no hay desglose público de factores.
- El extracto web por herramienta devolvió 402 (cuota agotada); se usó descarga directa curl + INITIAL_STATE; el factsheet GS solo se usó vía snippet de búsqueda (cifras concretas).

**Decisión.** GS Europe CORE Base Acc EUR; línea 6.000 € ≥ mínimo; Q1 2024/2025

### Janus Henderson Horizon Global Smaller Companies Fund A2 EUR — `LU1984712320`

**Identidad y operativa.** Janus Henderson Investors · clase `rv-global` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Small caps globales activo. Importe: 5.000 €. Ficha: `finance/fondos-myinvestor/rv-global/LU1984712320.md`.

**Coste y mínimos.** TER snapshot **1,90 %** (1,90 % (snapshot app; coincide Finect «gastos corrientes» 1,900 %)); gestión 1,20 % fija (quefondos y Finect 1,200 %); éxito **10,00 %** sobre resultados positivos del fondo vs su benchmark (quefondos); factsheet/KID: 10 % del exceso s …; mínimo publicado "2.500,00 EUR (quefondos; factsheet: 2.500)"; mínimo operativo verificado: **web ficha: 2.500 EUR**. NAV 53.28.

**Exposición y evidencia.** RV 95,50 % · RF 0,00 % · 3A 18,72 % · 5A 9,52 % · vol 14,23 % · SRRI 4. Patrimonio: Patrimonio de la clase: 422,6 M€.

**Regiones.** Estados Unidos 59,69 %; Japón 12,78 %; Australasia 5,87 %; Zona Euro 5,73 %; Reino Unido 4,52 %; Canadá 4,27 %; Europa ex-Zona Euro 2,29 %; Mercado emergente 0,35 %. País desarrollado 95,15 %.

**Sectores.** Industriales 24,79 %; Servicios financieros 13,88 %; Tecnología 13,15 %; Consumo cíclico 10,65 %; Salud 10,32 %; Materiales básicos 7,33 %; Energía 4,60 %; Consumo defensivo 4,51 %; Comunicación 2,62 %; Inmobiliario 2,19 %; Utilities 0,75 %.

**Quién es y para qué sirve.** Subfondo de la SICAV Janus Henderson Horizon Fund (fabricante: Janus Henderson Investors Europe S.A., según KID), clase A2 EUR constituida el 06/08/2019 (quefondos, Finect, factsheet y FT coinciden; Investing.com la fecha el 08/06/2019, ver Pegas). Busca crecimiento de capital a largo plazo invirtiendo al menos el 80 % del patrimonio en acciones de empresas de pequeña capitalización, de cualquier sector y país: se consideran small caps las que en el momento de la compra están dentro del rango de capitalización del MSCI World Small Cap. Benchmark: MSCI World Small Cap Index; **objetivo de rentabilidad del KID: batir al índice tras comisiones en cualquier período de 5 años**. Clase de acumulación («This share class accumulates income», KID; «Accumulation Net», factsheet). Divisa base del fondo: USD (factsheet); la clase A2 EUR no lleva sufijo de cobertura (a diferencia de las clases HEUR d …

**Lectura para cartera (texto de la ficha).** Papel de **satélite de RV global small caps** para diversificar un núcleo de gran capitalización: cartera 100 % small/mid/micro, muy diversificada (top 10 solo ~21 %), con sesgo a industriales (~25 %, p. ej. Comfort Systems, Sterling Infrastructure), financieras (~14 %) y tecnología (~13 %), y ~60 % EE. UU. más ~13 % Japón. Para un perfil dinámico con horizonte largo que quiera el segmento small cap global gestionado activamente; la clase A2 EUR es de acumulación pero sin cobertura de divisa (fondo base USD), así que añade exposición divisa. El KID fija el objetivo explícito de batir al MSCI W …

**Pegas detectadas.**
- Comisión de éxito del 10 % sobre el exceso de rentabilidad vs el MSCI World Small Cap con high water mark (quefondos, factsheet y KID), adicional al TER 1,90 %: en años buenos el coste total sube notablemente.
- Enfriamiento reciente: 1A y YTD 2026 en quintil 3 vs su categoría; alpha 1A -5,63 (Finect, 31/10/2026) pese a la alpha positiva 3A/5A.
- Beta >1 (1,13 a 1A): más oscilación que el mercado pese a la volatilidad media en su categoría.
- Rating Morningstar discrepa: snapshot 4 ★ vs Finect 5 ★; manda el snapshot. VDOS 4 estrellas.
- Reembolso discrepa: quefondos 1,00 % (<3 meses) vs factsheet «no redemption charge currently»; Finect n/a.
- Equipo gestor ampliado el 30/06/2026 (FT): Nick Sheridan (desde 2019) más Coleman, Beckett, Lee, Duhra y Schaechterle; posible transición de proceso (riesgo a vigilar).
- Divisa sin cubrir: clase A2 EUR sin sufijo de cobertura; divisa base del fondo USD (factsheet).
- NAV: Finect 52,93 EUR (19/11/2026) vs snapshot/quefondos 53,28 EUR: pequeña discrepancia de fuente/fecha.
- Fecha de constitución: 06/08/2019 (quefondos/Finect/factsheet/FT) vs Investing.com 08/06/2019.
- Patrimonio: clase 422,6 M€ (quefondos 18/11/2026) vs 425,3 M€ (snippet Finect) vs 401,4 M (Investing.com, antiguo); fondo 2.329,0 M€ (Finect) vs 2.650 M$ (factsheet 30/09/2026): fechas y divisas distintas.
- Historial de la clase ~7 años (06/08/2019): sin serie 10A.
- Concentración geográfica: ~60 % EE. UU.; sectorial: ~25 % industriales.

**Decisión.** Janus Global Smaller Companies A2; éxito 10% vs benchmark HWM; Q1 2023-2025

### First Sentier Global Listed Infrastructure Fund Class I (Accumulation) EUR — `IE00BYSJTY39`

**Identidad y operativa.** First Sentier Investors (Singapore) · clase `sectoriales` · fuente `mcp` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Infraestructura cotizada activo. Importe: 5.000 €. Ficha: `finance/fondos-myinvestor/sectoriales/IE00BYSJTY39.md`.

**Coste y mínimos.** TER snapshot **1,59 %** (1,59 %); gestión 1,50 %; éxito —; mínimo publicado "1.00 EUR"; mínimo operativo verificado: **web ficha: 1.00 EUR**. NAV 21.638.

**Exposición y evidencia.** RV 99,40 % · RF 0,00 % · 3A 12,99 % · 5A 7,33 % · vol 11,07 % · SRRI 4. Patrimonio: Pendiente.

**Regiones.** Estados Unidos (62,7 %), México (5,0 %), Reino Unido (4,5 %), Canadá (4,1 %), Francia (3,7 %), España (3,2 %)

**Sectores.** Servicios públicos (44,0 %), Industria (36,9 %), Energía (11,8 %), Inmobiliaria (5,1 %), Servicios de comunicación (0,8 %), Tecnología (0,7 %)

**Quién es y para qué sirve.** Fondo de renta variable con foco en USA, de gestión activa, sector/temática: Industria, Infraestructura, Servicios públicos, comercializado en MyInvestor en clase de acumulación (EUR). Fecha de lanzamiento de la clase: 2008-06-27.

**Lectura para cartera (texto de la ficha).** Satélite concentrado en un sector o temática: alta convicción y alta volatilidad relativa. No sustituye a un núcleo diversificado; el ciclo del sector puede dominar la rentabilidad durante años. *Orientación general derivada de la clasificación del catálogo; no es una recomendación de inversión.*

**Decisión.** First Sentier Global Listed Infra I EUR; Lazard descartado (mín 10.000 GBP)

### Aegon European ABS Fund A EUR Acc — `IE00BG226Z29`

**Identidad y operativa.** Aegon Investment Management B.V. (Aegon Asset Management) · clase `renta-fija` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Titulizaciones ABS euro activo. Importe: 11.000 €. Ficha: `finance/fondos-myinvestor/renta-fija/IE00BG226Z29.md`.

**Coste y mínimos.** TER snapshot **0,66 %** (0,66 % (snapshot app; Finect gastos corrientes 0,660 %; ver Pegas)); gestión 1,50 % (quefondos y Finect); éxito n/a (Finect); variable 0,00 % (quefondos); mínimo publicado "0,00 EUR (quefondos)"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 11.696.

**Exposición y evidencia.** RV 0,00 % · RF 100,00 % · duración estimada 1.5 · 3A 4,35 % · 5A 3,00 % · SRRI 2. Patrimonio: Pendiente.

**Sectores.** CLO 24,2 · Consumer Loan 16,6 · RMBS 15,7 · Auto 10,3 · Non-conform 8,6 · Buy-to-let 7,3 · CMBS 6,2 · Credit Card 4,5 · Prime 3,6 · Student Loans 1,3

**Quién es y para qué sirve.** Fondo irlandés (ICAV Aegon Asset Management Europe) que invierte al menos el 70 % de su patrimonio en valores respaldados por activos (ABS): hipotecas residenciales (RMBS) y comerciales (CMBS), préstamos al consumo, automóviles, tarjetas de crédito, estudiantiles y corporativos (CLO/whole business). Al menos el 70 % en bonos con grado de inversión (Baa3/BBB- o superior); emisores principalmente europeos, aunque puede invertir fuera de Europa, en EUR y otras divisas (cubiertas a EUR según factsheet). Sin benchmark de referencia según quefondos; Finect cita «Bloomberg Cap Eur ABS Fix&Float H TR USD» y el factsheet «BBG Euro Fixed and Floating Index». SFDR artículo 8. Fondo constituido el 11/11/2016; clase A iniciada el 23/05/2018 (Finect). Tamaño del fondo ~10.142 M€ (factsheet a 30/09/2026; Finect: 10.167,2 M€); clase A: 134,8 M€ (Finect) vs 11.948,11 miles de € en quefondos (ver Pegas).

**Lectura para cartera (texto de la ficha).** Papel satélite de carry con riesgo de crédito diversificado: un fondo de ABS europeos investment grade (calidad media AA+) con duración de tipos casi nula (0,14 años) pero duración de diferencial ~1,9 años. Es decir, cobra prima de crédito sobre tipos cortos con muy poca sensibilidad a subidas de tipos; encaja como complemento de un núcleo de renta fija para perfiles que quieren yield adicional sin alargar duración, aceptando riesgo de diferencial y de titulización. La evidencia es de las mejores del lote vs su categoría (VDOS Deuda Privada Europa): quintil 1 en 2022 (-4,00 %, ranking 9/88, fr …

**Pegas detectadas.**
- Anomalía de costes: TER snapshot 0,66 % = gastos corrientes Finect 0,660 %, pero la comisión de gestión publicada es 1,50 % (quefondos y Finect). Un TER por debajo de la gestión es anómalo; posible dato erróneo o condici
- Reembolso discrepante: hasta 3,00 % (quefondos) vs 0,000 % (Finect). Suscripción hasta 5,00 % en ambas.
- Patrimonio de clase muy discrepante: quefondos 11.948,11 miles de € (~11,9 M€) a 16/11/2026 vs Finect 134,8 M€; el fondo completo ~10.142-10.167 M€. Posible dato de otra clase o error de quefondos.
- Benchmark discrepante: quefondos «sin benchmark», Finect «Bloomberg Cap Eur ABS Fix&Float H TR USD», factsheet «BBG Euro Fixed and Floating Index».
- Fecha de inicio de clase: Finect 23/05/2018; quefondos solo da la del fondo (11/11/2016). Historial de la clase ~7 años, suficiente.
- Concentración sectorial y geográfica: CLO 24,2 % y Reino Unido 29,8 %; colaterales de consumo e inmobiliario sensibles a una recesión por endurecimiento monetario.
- Composición tomada de la clase hermana B (factsheet 30/09/2026): cartera común, pero sus comisiones (gestión 0,25 %, OCF 0,31 %) y rentabilidades NO son las de esta clase A.
- Finect no renderiza composición (JS); sin asset allocation RV/RF/caja publicado → tabla Pendiente.

**Decisión.** Aegon European ABS A EUR; Q1 2022/2026; gestión 1.50% vs TER 0.66% (anomalía, snapshot manda); exit fee discrepante

**Verificación web 20/11/2026.** Aegon AM anuncia que a partir del 23/11/2026 la gestora del ICAV pasa a Carne Global Fund Managers (Ireland) Limited. La página oficial solo lista las clases USD G/D/X, no la clase EUR A del catálogo; la anomalía TER 0,66 % frente a gestión 1,50 % queda sin resolver y se mantiene el TER del snapshot como coste modelado, con aviso. <https://www.aegonam.com/funds-resources/fixed-income/european-abs-fund/>

### Pictet-Sovereign Short-Term Money Market EUR-P — `LU0366536711`

**Identidad y operativa.** Pictet Asset Management (Europe) SA · clase `monetarios` · fuente `listado-app` · activa · divisa EUR · política **acumulacion**. Rol en la cartera: Monetario EUR soberano. Importe: 5.000 €. Ficha: `finance/fondos-myinvestor/monetarios/LU0366536711.md`.

**Coste y mínimos.** TER snapshot **0,17 %** (0,17 % (snapshot app; coincide con gastos corrientes 0,170 % de Finect); FT muestra ongoing charge 0,18 %); gestión 0,30 % fija (quefondos); 0,300 % (Finect); máx. anual 0,30 % (FT); éxito 0,00 % variable (quefondos); n/a (Finect); mínimo publicado "0,00 EUR (quefondos)"; mínimo operativo verificado: **web ficha: 0.00 EUR**. NAV 108.859.

**Exposición y evidencia.** RV 0,00 % · RF 8,63 % · 3A 2,67 % · 5A 2,03 % · SRRI 1. Patrimonio: 4.803,9 M€.

**Regiones.** Pendiente (FT no renderiza el desglose regional). Emisores visibles en el top 5: Canadá, Suecia y Suiza (Swiss National Bank).

**Sectores.** Pendiente (no publicados; por política, todo es deuda pública/soberana y depósitos).

**Quién es y para qué sirve.** Subfondo monetario de Pictet que busca preservar el capital y la estabilidad de valor, obtener un rendimiento acorde con los tipos de los mercados monetarios y ofrecer liquidez elevada, con una política de reparto de riesgos (quefondos). Solo invierte en depósitos o instrumentos del mercado monetario emitidos o garantizados por un Estado o corporación de derecho público de la OCDE o de Singapur, o por organizaciones internacionales de derecho público de las que formen parte Suiza o un Estado miembro de la UE: es un monetario **exclusivamente soberano/público**, sin crédito bancario ni corporativo privado. WAM ≤ 60 días y WAL ≤ 120 días. Benchmark: EUR GERMAN SOVEREIGN 1M (quefondos); Finect muestra «US GENERIC GOVT 1 MONTH» (discrepancia, ver Pegas). Categoría VDOS «Monetario Euro Corto Plazo» (quefondos) / «Mercado Monetario Corto Plazo EUR» (Finect); Morningstar «EUR Money Market - Sho …

**Lectura para cartera (texto de la ficha).** Papel de liquidez defensiva en euros: aparcamiento de capital y fondo de emergencia con la máxima calidad crediticia dentro de los monetarios (solo deuda pública y organismos internacionales, sin riesgo bancario/corporativo privado). SRRI 1, volatilidad 1A de 0,07 % (quefondos) y duration mínima (WAM ≤ 60 días): el valor liquidativo apenas se mueve. Encaja para quien prioriza preservar el capital y la disponibilidad diaria sobre el carry, y como estacionamiento táctico antes de desplegar a otros activos. La evidencia es de consistencia media, no de liderazgo: rating VDOS 2 estrellas (quefondos …

**Pegas detectadas.**
- Caché antigua de quefondos: la primera extracción devolvió datos a 31/03/2026 (categoría «Monetario Euro», YTD 0,46 %, rankings distintos); se re-extrajo y se usó la versión a 17/11/2026 (categoría «Monetario Euro Corto
- Rating VDOS 2 estrellas y quintiles 3–4 vs categoría: rendimiento de mitad de tabla; el perfil solo-soberano sacrifica carry frente a monetarios con crédito privado.
- Rentabilidad real negativa en el escenario actual: nominal ~2 % (1A 2,07 %) vs inflación eurozona 3,8 % (contexto-macro).
- Comisiones de entrada/salida: Finect publica suscripción 5,000 % y reembolso 1,000 %; quefondos/FT «hasta» 5 % / 1 %. Verificar las aplicadas por MyInvestor: un reembolso del 1 % se comería ~6 meses de carry.
- TER divergente: 0,17 % (snapshot/Finect) vs 0,18 % ongoing charge (FT).
- Benchmark divergente: «EUR GERMAN SOVEREIGN 1M» (quefondos) vs «US GENERIC GOVT 1 MONTH» (Finect); probable error de una de las fuentes.
- Fechas de inicio divergentes: 16/06/2008 (FT), 17/06/2008 (Finect), 18/09/2008 (quefondos, constitución de la clase).
- 2022 cerró en negativo (-0,26 %): con tipos cortos negativos o cercanos a cero, el TER puede volver la rentabilidad neta negativa; no es un fondo «sin riesgo» de pérdida nominal.
- Composición completa (sectores, regiones, top 10) no disponible en Finect (JS); solo top 5 y desglose de activos vía FT, sin fecha de cartera.

**Decisión.** Pictet Sovereign ST MM EUR-P; Q3-4, solo soberano


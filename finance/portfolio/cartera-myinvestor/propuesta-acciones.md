---
title: "Propuesta de acciones sin dividendo — cuatro posiciones y una lista de espera"
date: 2026-11-04
type: portfolio-research
category: finance
tags: [cartera, acciones, sin-dividendo, calidad, tecnologia, value, la-pizarra-de-andres, webinars, myinvestor, propuesta]
status: research
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-myinvestor/propuesta-actual.md
  - finance/la-pizarra-de-andres/2026-10-30-las-empresas-que-todos-ignoran-son-las-mejores-inversiones/summary.md
  - finance/la-pizarra-de-andres/2026-10-22-gestor-de-renta-4-advierte-sobre-una-gran-recesion/summary.md
  - finance/la-pizarra-de-andres/2026-10-15-da-miedo-pero-la-ia-puede-solucionar-la-economia-juan/summary.md
  - finance/myinvestor-webinars/2026-10-20-japon-proxima-gran-oportunidad-en-bolsa/summary.md
---

# Propuesta de acciones sin dividendo — 04/11/2026

> **Qué es.** Una cartera de **acciones individuales**, todas ellas **mencionadas en el corpus del
> repositorio** (La Pizarra de Andrés, webinars de MyInvestor, El Arte de Invertir) y **ninguna que
> reparta dividendos**. Es una propuesta de investigación: no toca las dos carteras existentes, no
> modifica el 50/50 de MyInvestor ni la auditoría de Renta 4 y no se consolida con ellas.
>
> **Qué no es.** No es una recomendación del canal: el corpus **no contiene ninguna acción sin
> dividendo con tesis completa y recomendación explícita**. Lo que hay son carteras de gestores
> (Horos, Arcus, el invitado de la charla de IA) y menciones sueltas de calidad. La propuesta se
> construye sobre esas menciones **más** verificación propia de negocio, múltiplo y precio.
>
> **Fuentes del corpus usadas.** 17 `summary.md` y 3 informes de `finance/reports/`. Se reutilizan
> además el método y las verificaciones de los anexos absorbidos el 04/11/2026 (regla de acumulación,
> ficha por vehículo, etiquetas hecho/consenso/opinión, señal de invalidación); el texto íntegro de
> esos anexos está en el historial de git, commit `50b2e69`, y sus conclusiones en `propuesta-actual.md`.
> Datos de mercado: 04/11/2026, cierre americano en curso; EUR/USD 1,1225.

## 0. Resumen ejecutivo

El corpus nombra **más de 90 compañías cotizadas**. La regla del dividendo no es el cuello de
botella: el cuello es que **casi todas las que no reparten solo aparecen enumeradas de pasada**. Con
mención sustantiva (grado A o B) y sin dividendo hay exactamente **tres**: Amazon, Netflix y
Cloudflare. De ahí sale una cartera de **4 posiciones y 10 % de liquidez**:

| # | Empresa | Ticker | Mercado | Peso | € sobre 20.000 | Acciones | Múltiplo | ¿Comprar hoy? |
|--:|---|---|---|---:|---:|---:|---:|---|
| 1 | Amazon | AMZN | Nasdaq | 30 % | 6.000 | 25 | 21,7x BPA · 16,8x EBITDA | **Sí, en dos tandas** |
| 2 | Netflix | NFLX | Nasdaq | 25 % | 5.000 | 85 | 19,1x BPA · 17,6x EBITDA | **Sí, en dos tandas** |
| 3 | Adobe | ADBE | Nasdaq | 20 % | 4.000 | 17 | 14,3x BPA · **9,5x forward** | **Sí, pero con stop de tesis** |
| 4 | Arista Networks | ANET | NYSE | 15 % | 3.000 | 17 | 50,1x BPA · 36,2x forward | **Solo una tanda; el resto a 150 $** |
| — | Liquidez | — | — | 10 % | ≈2.300 | — | — | Espera a Cloudflare (5/11) y a la 2ª tanda |
| L | *Cloudflare (lista de espera)* | NET | NYSE | *0 %* | *0* | *0* | *285x FCF* | **No a 264 $; ver §5** |

**Múltiplo ponderado de la cartera:** 21,7x beneficios trailing y 20,1x forward sobre el 90 %
invertido (24,1x y 22,3x normalizado al 100 %). Beta ponderada ≈ **1,37** (1,52 sobre lo invertido).

**Las tres conclusiones, sin rodeos.**

1. **La regla del dividendo vacía las mejores tesis del corpus.** Se lleva por delante las dos
   mejores ideas de Horos —**PayPal** (4-5 veces flujo de caja libre) y **Booking** (potencial del
   70 %)— por repartir un 0,93 % y un 0,98 %, y también Tencent, TGS, NTT, Honda, Exor y Ferrari.
   Están en §6 con el número delante para que la decisión sea del titular, no del agente.
2. **La cartera es todo lo contrario de lo que dice el invitado del 30/10.** Javier Ruiz avisa de que
   comprar calidad en EE. UU. ha pasado de 18 a 35-40 veces beneficios. Esta propuesta compra cuatro
   compañías americanas, dos de ellas a más de 30 veces. Se asume y se acota: 20.000 €, no el núcleo.
3. **La evidencia es de grado B y C, y así se dice.** Amazon y Netflix son grado B (calidad mencionada,
   sin recomendación); Adobe y Arista son grado C (enumeradas). El comprar se justifica por los números
   de sus últimas cuentas, que están en §4 y §7, no porque el canal las bendiga.

## 1. Método

### 1.1 Pasos

1. **Extraer el universo.** Se leen los 17 resúmenes y se listan **todas** las compañías cotizadas
   nombradas, con su postura (`recomienda`, `en cartera`, `neutro`, `criticado por caro`,
   `ejemplo negativo`, `idea a estudiar`). Una mención no es una recomendación.
2. **Filtrar por dividendo.** Se comprueba la política de retribución en la ficha de cada una
   (`dividend yield` y fecha del último dividendo), no en el corpus. **Cero excepciones por tamaño**:
   Nvidia reparte un 0,49 % y cae igual que Coca-Cola, que reparte varias veces más.
3. **Filtrar por tesis y precio.** Se pide negocio entendible, cuentas del último trimestre, un
   múltiplo que se pueda defender y una señal de invalidación escrita. Lo que no pasa, va a §6.
4. **Graduar la evidencia.** Es la pieza que evita vender humo:

| Grado | Qué significa | Ejemplos del corpus |
|---|---|---|
| **A** | En cartera del hablante **con tesis y múltiplo** | PayPal, Booking, Tencent, TGS, NTT, Honda, Cloudflare, Exor |
| **B** | Mención de calidad con cifra, sin recomendación explícita | Amazon («magnífica compañía»), Netflix (margen y ARPU como «idea a estudiar») |
| **C** | Solo enumerada en una lista de sector | Adobe, Arista, AMD, Salesforce, Ciena |
| **D** | Descartada o criticada por el propio hablante | Nike, Tesla, CoreWeave, Coca-Cola, Walmart, ASML, Hermès |

5. **Reutilizar lo ya verificado.** De `propuesta-investigacion.md` se toma el formato de ficha, la
   regla de acumulación y la lista de nombres sin dividendo (Berkshire, Amazon, Netflix, Booking,
   Adyen). **Corrección:** aquel anexo daba Booking como «no reparte»; a 04/11/2026 paga **1,68 $
   anuales (0,98 %)** desde 2024. Queda corregido aquí y Booking sale del universo.

### 1.2 Lo que el corpus sí permite afirmar

- Que un gestor profesional tiene una compañía **en cartera** y por qué (Horos, Arcus, el invitado
  de IA). Es información de posicionamiento, no una recomendación al lector.
- Que un invitado califica un negocio de sólido y barato (McDonald's, Amazon) o de caro (Coca-Cola,
  Nike). Es una opinión con fecha.
- Que el canal **desconfía del precio de la calidad americana** y prefiere value europeo, renta fija
  corta y holdings con descuento. Esta propuesta va en contra de esa preferencia y lo dice.

### 1.3 Lo que el corpus no permite

- Fijar pesos: **ningún** invitado da pesos de su cartera salvo Horos con TGS (7 % → 3 %) y Francia
  (un cuarto). Los pesos de §3 son decisión de esta propuesta, no del canal.
- Predecir retornos: no hay una sola cifra de rentabilidad esperada por compañía en todo el corpus.

## 2. El embudo: de más de 90 nombres a 4 posiciones

| Filtro | Nombres | Quién cae |
|---|---:|---|
| Compañías cotizadas nombradas en el corpus | más de 90 | — |
| Con mención **sustantiva** (grado A o B) | ≈20 | el resto solo se enumera en una lista de sector |
| … y **sin dividendo** | **3** | PayPal, Booking, Tencent, TGS, NTT, Honda ya no pasan |
| Enumeradas sin tesis, sin dividendo y con negocio defendible | **+2** | Adobe y Arista entran por mérito propio, no por el corpus |
| Con precio que se pueda pagar hoy | **4** | Cloudflare, a lista de espera (§5) |

Las compañías **sin dividendo** que el corpus menciona, con la evidencia de cada una:

| Empresa | Ticker | Grado | Qué dice el corpus | Decisión |
|---|---|---|:--:|---|
| Amazon | AMZN | B | Renta 4 (22/10): «Compra, es una magnífica compañía», pero «ahora también existe su bono» (35:21) | **Entra 30 %** |
| Netflix | NFLX | B | Renta 4 (22/10): márgenes EBITDA del 25-30 % y 12-13 $ por suscriptor; «idea a estudiar» (37:52) | **Entra 25 %** |
| Cloudflare | NET | **A** | Charla de IA (15/10): «una empresa en cartera» del invitado (línea 87) | Lista de espera |
| Adobe | ADBE | C | Charla de IA (15/10): el marketing es el tercer caso de uso y cita Adobe como referencia (línea 64) | **Entra 20 %** |
| Arista | ANET | C | Charla de IA (15/10): enumerada en «comunicaciones ópticas y redes» (línea 416) | **Entra 15 %** |
| AMD | AMD | C | Burbujas IA (09/10): entre las 10 mayores del S&P tras hacer «un trabajo increíble» | Fuera (§6) |
| Tesla | TSLA | D | Descartada por dos voces: 220 veces beneficios (18/10) y «no entiendo cómo cotiza a estos múltiplos» (22/10) | Fuera (§6) |
| OHLA | OHLA.MC | C | Valor (18/10): 0,7 veces valor en libros, «a ese precio se puede ganar dinero»; idea a estudiar | Fuera (§6) |

**Mencionadas sin cifra ni tesis, y sin dividendo, que no se analizan:** Ciena, Coherent, Lumentum,
Uber, Block, Shopify, Moderna, Oklo y NuScale. Aparecen en enumeraciones de sector (redes ópticas,
software, energía para centros de datos, salud) y ninguna lleva tesis, múltiplo ni postura. Meterlas
«porque no reparten» sería cambiar una regla por un capricho, que es exactamente lo que advierte
`propuesta-investigacion.md` §5.

**Lo que este cuadro dice y no se puede maquillar:** la única compañía con evidencia **grado A y sin
dividendo** es Cloudflare, y cotiza a 285 veces flujo de caja libre. Todas las demás tesis de grado A
del corpus —PayPal, Booking, Tencent, TGS, NTT, Honda, Exor, Ferrari, Bolloré, UMG, Pluxee— **reparten
dividendo**. Por eso la cartera que se propone es de grado B y C: se apoya en el negocio y en el precio
verificados fuera del corpus, no en la bendición del canal.

## 3. La cartera

### 3.1 Pesos y ejecución (ejemplo sobre 20.000 €)

| Empresa | Peso | € objetivo | Precio 04/11 | €/acción | Nº acciones | € reales | % real |
|---|---:|---:|---:|---:|---:|---:|---:|
| Amazon | 30 % | 6.000 | 268,70 $ | 239,38 | 25 | 5.984,62 | 29,9 % |
| Netflix | 25 % | 5.000 | 65,93 $ | 58,74 | 85 | 4.992,65 | 25,0 % |
| Adobe | 20 % | 4.000 | 256,40 $ | 228,43 | 17 | 3.883,26 | 19,4 % |
| Arista | 15 % | 3.000 | 187,53 $ | 167,07 | 17 | 2.840,20 | 14,2 % |
| Liquidez | 10 % | 2.000 | — | — | — | 2.299,28 | 11,5 % |
| **Total** | **100 %** | **20.000** | | | | **20.000** | **100 %** |

**Por qué esos pesos y no otros.** Amazon y Netflix pesan más porque son las dos únicas con
**tesis de negocio** en el corpus y cuentas que la sostienen; Adobe lleva un 20 % porque es la que
cotiza más barata y la que más riesgo de tesis tiene (se compensa con el múltiplo); Arista lleva un
15 % porque es la mejor compañía de las cuatro y la más cara, así que se entra a medias.

**Coste real de entrar**, con la tarifa de MyInvestor (0,12 % + 0,30 % de cambio, mínimo 3 € y
máximo 25 € por operación): **74,21 € estimados, el 0,37 %** de los 20.000 €. En dos tandas, ≈148 €. Sin
custodia, sin mantenimiento y sin comisión por cobro de dividendos (que aquí no hay).

**Alternativa sin liquidez:** repartir el 10 % entre las cuatro (33 / 28 / 22 / 17 %). Sube la beta
y elimina el margen para la segunda tanda de Arista y para la entrada condicional en Cloudflare.
La liquidez aquí **no es un colchón de seguridad**, es una orden pendiente.

### 3.2 Métricas de la cartera

| Métrica | Valor | Comentario |
|---|---:|---|
| Posiciones | 4 | Concentración alta, por construcción (§8) |
| PER trailing ponderado | 21,7x | 24,1x normalizado al 100 % |
| PER forward ponderado | 20,1x | 22,3x normalizado |
| Beta ponderada | 1,37 | 1,52 sobre lo invertido; el 50/50 de MyInvestor estima −21,5 % en un 2008 |
| Moneda | 100 % USD | EUR/USD 1,1225; sin cobertura |
| Sectores | 30 % nube y comercio (AMZN) · 25 % medios (NFLX) · 20 % software (ADBE) · 15 % hardware de red (ANET) | En la práctica, **una sola apuesta: tecnología americana** |
| Dividendo | 0 € | Ninguna de las cuatro retribuye al accionista |

**Lo que no se compra con esta cartera.** Diversificación. Cuatro nombres del mismo mercado y del
mismo bloque temático no diversifican: comparten el ciclo de capex de la IA, el tipo de interés
americano y el dólar. El 50/50 de MyInvestor sigue siendo el núcleo; esto es una satélite de
convicción y se dimensiona como tal.

## 4. Fichas

### 4.1 Amazon (AMZN) — 30 %

**1. Qué dijo el corpus.** [Grado B] El gestor de Renta 4 (22/10/2026) la llama «magnífica
compañía» al comparar comprar la acción o su bono a 10 años al 6 % (35:21). No es una
recomendación: en el mismo vídeo dice «recomiendo que no compre ni uno solo de mis valores». La
otra mención del corpus es el −15 % del día de la entrevista de Horos (22:09), un dato de mercado.

**2. Tesis en tres frases.** AWS ha vuelto a acelerar —**+39,3 %** en el tercer trimestre, la mayor
subida en casi cinco años— y el margen operativo del grupo marca un récord del **13,9 %**. El
negocio minorista ya no es el problema: Norteamérica gana 8.700 M$ frente a 4.800 M$ un año antes.
Lo que se compra es la conversión de un capex brutal (**220.000 M$ en 2026**) en beneficio recurrente
de nube, no el crecimiento de las ventas.

**3. Métricas (04/11/2026).**

| Métrica | Valor |
|---|---:|
| Capitalización | 2,91 billones $ |
| Ingresos últimos 12 meses | 797.460 M$ (+12 % en el trimestre) |
| Beneficio operativo TTM | 104.370 M$ · margen 13,1 % |
| AWS (Q3 2026) | 46.000 M$ · +39,3 % · margen 38,7 % |
| Cartera de pedidos AWS | 578.000 M$ |
| PER trailing | 21,7x |
| PER forward | 27,2x |
| EV/EBITDA | 16,8x |
| ROE / ROIC | 27,4 % / 10,9 % |
| Flujo de caja libre TTM | **−46.890 M$** (capex 215.190 M$) |
| Deuda neta | 190.620 M$ |
| Consenso | 59 analistas, «Strong Buy», objetivo 326,74 $ (+21,5 %) |

**4. El detalle que cambia la lectura del PER.** El beneficio neto TTM de 134.780 M$ incluye
**69.500 M$ de «otros ingresos»**, en su mayoría plusvalías contables de la participación en
Anthropic (acciones preferentes y notas valoradas a 238.700 M$ y 146.200 M$). Sin ese efecto, el
múltiplo real es el **forward de 27,2x**, no el 21,7x de la ficha. Cualquiera que compre «a 21
veces» está comprando un múltiplo que no existe.

**5. ¿Comprar hoy?** **Sí, pero en dos tandas y sabiendo qué se paga.** La compañía está ejecutando
mejor de lo que descuenta el precio (sexto trimestre consecutivo de aceleración de AWS) y el
consenso espera +40 % en 2027 y 2028. El riesgo no es el negocio, es el capex: **flujo de caja libre
negativo y un endeudamiento neto de 124.140 M$ en los últimos doce meses**. Entrada: 15 % del peso
ahora, 15 % tras el cierre del cuarto trimestre (febrero), cuando se vea si el capex empieza a
convertir.

**6. Respaldo externo.**
[Hecho] Amazon IR, «Amazon.com Announces Third Quarter Results», 29/10/2026: margen operativo récord
13,9 %, AWS +39,3 %, guía de Q4 de 240.000-247.000 M$ de ventas y 28.500-33.500 M$ de beneficio
operativo. https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx
[Hecho] CNBC, 29/10/2026: FCF negativo de 42.400 M$ y capex de 220.000 M$ en 2026.
https://www.cnbc.com/2026/10/29/amazon-amzn-q3-earnings-report-2026.html
[Consenso] 59 analistas, objetivo medio 326,74 $ (stockanalysis.com, 04/11/2026).
[Contrapunto] El propio corpus: Horos avisa de que el riesgo de la IA está en **quien la financia**;
Amazon es a la vez cliente y financiador (compra chips y presta a Anthropic).

**7. Riesgos.** (a) El capex de IA no genera retorno y el flujo de caja libre sigue negativo varios
años; (b) concentración del beneficio en AWS mientras el retail aporta márgenes bajos; (c) la
valoración de Anthropic da plusvalías contables que pueden revertir; (d) un 100 % de los ingresos en
dólares.

**8. Señal de invalidación.** Dos trimestres seguidos con AWS creciendo por debajo del 25 % **y**
capex al alza. Ahí la tesis de «convertir capex en beneficio» se rompe y se sale, no se promedia.

**9. Convicción.** **Alta-media.** El negocio es el más sólido de los cuatro; el precio no es una
ganga si se mira el múltiplo correcto.

### 4.2 Netflix (NFLX) — 25 %

**1. Qué dijo el corpus.** [Grado B] Renta 4 (22/10/2026) describe el modelo de suscripción como
espejo de lo que podría ser la IA: **márgenes EBITDA del 25-30 %** y **12-13 $ de ingreso medio por
suscriptor**; lo marca como «idea a estudiar» (37:52). En la charla del 25/10 se la cita como
ejemplo de consumo que «se ha girado» (50:35): es un dato sobre el consumidor, no sobre la compañía.

**2. Tesis en tres frases.** La acción ha caído un **40 % en un año** y un **47 % desde máximos**
mientras el negocio sigue creciendo a doble dígito y con margen operativo del **34,6 %** en el
trimestre. El mercado descuenta un techo de suscriptores y un fracaso publicitario; la compañía entrega
**12.000 M$ de flujo de caja libre** y sube el margen del año al 31,5 %. A 19 veces beneficios y 17,6
veces EBITDA, es la primera vez en años que una compañía de calidad del corpus cotiza a múltiplo de
value.

**3. Métricas (04/11/2026).**

| Métrica | Valor |
|---|---:|
| Capitalización | 271.000 M$ |
| Ingresos TTM | 49.730 M$ · Q3 12.874 M$ (+12 %) |
| Beneficio operativo Q3 | 4.459 M$ (+37 %) · margen **34,6 %** |
| Margen operativo guiado 2026 | 31,5 % (29,5 % en 2025) |
| Flujo de caja libre 2026 (guía) | ≈12.000 M$ |
| PER trailing / forward | 19,1x / 18,4x |
| EV/EBITDA · EV/FCF | 17,6x · 24,7x |
| ROE / ROIC | 53,5 % / 34,1 % |
| Deuda neta / EBITDA | 1,05x |
| Caída 52 semanas | **−39,8 %** (−47 % desde máximos) |
| Consenso | 51 analistas, «Buy», objetivo 84,76 $ (+28,4 %) |

**4. Lo que se ha roto de verdad.** El crecimiento se desacelera trimestre a trimestre: +17,6 %
(Q4 2025), +16,2 %, +13,4 %, **+11,8 %** (Q3 2026). La guía de publicidad baja de 3.000 a **2.700 M$**
por un despliegue más lento de lo previsto, y hay **1.000 despidos** y cambio del jefe de contenido.
No es una empresa en crisis, es una empresa cuyo motor de crecimiento se está agotando.

**5. ¿Comprar hoy?** **Sí, en dos tandas y con la tesis escrita.** Es exactamente el caso que el
corpus enseña a distinguir: PayPal cayó y se abarató; Nike cayó y siguió caro. Aquí el múltiplo sí ha
bajado (de más de 30 a 19) y el beneficio sigue creciendo, pero la desaceleración es real. Entrada:
12,5 % del peso ahora, 12,5 % **solo si** el cuarto trimestre confirma margen ≥26 % y la publicidad
no vuelve a recortarse.

**6. Respaldo externo.**
[Hecho] Carta de accionistas Q3 2026 (vía StockTitan y Morningstar, 20/10/2026): ingresos 12.874 M$,
margen operativo 34,6 %, guía de 51.100 M$ y 31,5 % de margen, FCF ≈12.000 M$ y 15 países nuevos de
publicidad en 2027. https://www.stocktitan.net/news/NFLX/netflix-q3-2026-earnings-revenue-12-billion-35pct-margin.html
[Hecho] Reuters, 20/10/2026: guía de Q4 por debajo del consenso, recorte de publicidad a 2.700 M$,
6 % de plantilla despedida y caída del 40 % en el año.
https://www.reuters.com/business/media-telecom/netflix-issues-weak-fourth-quarter-forecast-company-seeks-kick-start-growth-2026-10-20/
[Contrapunto] Barchart/Yahoo, «Why Now Is Not the Time to Load Up on Netflix Stock»: competencia de
YouTube y TikTok, pérdidas mensuales de suscriptores en EE. UU. durante 2026 y valoración «premium
respecto a pares» con crecimiento modesto.

**7. Riesgos.** (a) El techo de suscriptores en mercados maduros es real; (b) la publicidad no llega
a la escala de YouTube (≈11.000 M$ **por trimestre** frente a 2.700 M$ **al año**); (c) el contenido
es un coste creciente que se come el margen si el crecimiento se para; (d) el precio en dólares.

**8. Señal de invalidación.** Margen operativo anual por debajo del 28 % **o** dos recortes
consecutivos de la guía publicitaria. Con eso, la caída deja de ser una oportunidad y pasa a ser
deterioro (el caso Nike).

**9. Convicción.** **Media-alta.** Es la posición con más margen de mejora y la que más se puede
romper; por eso lleva la entrada partida y una condición escrita.

### 4.3 Adobe (ADBE) — 20 %

**1. Qué dijo el corpus.** [Grado C] En la charla de IA (15/10/2026) el invitado sitúa el marketing
como tercer caso de uso de la IA y cita **Adobe como referencia** del sector (línea 64); en la lista
de software aparece junto a Salesforce y Meta (línea 417). **No hay tesis de inversión**: es una
mención de sector. Todo lo que sigue es análisis propio.

**2. Tesis en tres frases.** Adobe cotiza a **9,5 veces beneficio forward** —frente a una media de
cinco años de 23x— con un negocio que crece al 13 %, un **ROIC del 57 %** y un flujo de caja libre de
10.590 M$. El mercado ha descontado una destrucción por IA generativa que las cuentas todavía no
enseñan: el ARR de productos de IA supera los **650 M$** y crece más del **150 %** anual. Se compra
un compounder de software a múltiplo de empresa en declive, aceptando que puede ser un value trap.

**3. Métricas (04/11/2026).**

| Métrica | Valor |
|---|---:|
| Capitalización | 99.520 M$ |
| Ingresos TTM | 25.970 M$ · Q3 fiscal 6.760 M$ (+13 %) |
| Beneficio operativo | 9.430 M$ · margen 36,3 % |
| Flujo de caja libre | 10.590 M$ · **FCF yield 11,1 %** |
| PER trailing / forward | 14,3x / **9,5x** |
| EV/FCF · EV/EBITDA | 9,2x · 9,8x |
| ROE / ROIC | 61,9 % / 57,2 % |
| Recompra de acciones | −6,2 % de acciones en un año |
| Caída 52 semanas | −24,0 % |
| Consenso | 39 analistas, **«Hold»**, objetivo 268,30 $ (+4,9 %) |

**4. La pega, con nombre y apellido.** El crecimiento del ARR se frena: **10,2 %** en el ejercicio
2026, y el consenso ya descuenta 9 % en 2027 y 8 % en 2028. Wells Fargo la bajó a *Underweight* con
objetivo 225 $; Rothschild & Co Redburn mantiene venta con objetivo **140 $**; HSBC a *Hold* con 267 $.
El consenso está a un +4,9 % del precio: **el mercado no ve el catalizador**, y eso es a la vez el
riesgo y la razón del múltiplo.

**5. ¿Comprar hoy?** **Sí, con posición completa pero stop de tesis.** A 9,5x no se paga el
crecimiento, así que la acción no necesita acelerar para no perder dinero: le basta con cumplir lo
que ya está descontado. **No se promedia a la baja** si la señal de invalidación se cumple. Es la
posición que más se parece a una idea value del corpus (barata con beneficios crecientes, el caso
McDonald's de la charla del 16/10) y la que más se parece a una trampa si el ARR se para.

**6. Respaldo externo.**
[Hecho] Resultados Q3 fiscal 2026 (recogidos por Zacks y Yahoo, octubre 2026): ingresos 6.760 M$,
ARR de IA >650 M$, subida de objetivos anuales y guía de Q4 de 6.800-6.850 M$.
https://finance.yahoo.com/markets/stocks/articles/adobe-drops-29-ytd-buy-171300479.html
[Consenso] Yahoo/TIKR, «Adobe Is Down 30 % This Year. Did Its Last Quarter Show Any Sign of the AI
Threat?»: 9,4x forward frente a media de 23x; recortes de Wells Fargo (225 $) y HSBC (267 $).
https://finance.yahoo.com/markets/stocks/articles/adobe-down-30-did-last-102125145.html
[Contrapunto] Rothschild & Co Redburn mantiene venta con objetivo 140 $ (recogido en el mismo
artículo); 24/7 Wall St. lo lleva al extremo contrario con objetivo 294,54 $ y rating de compra.

**7. Riesgos.** (a) La IA generativa erosiona el modelo de suscripción por asientos sin que se note
en el trimestre; (b) desaceleración del ARR neto nuevo; (c) cambio de consejero delegado y ejecución
de precios; (d) es la única de las cuatro con consenso «Hold»: no hay quien compre por ti.

**8. Señal de invalidación.** Crecimiento de ARR por debajo del 8 % **o** dos trimestres con ARR
neto nuevo por debajo de lo guiado. Si pasa, se sale aunque el múltiplo siga bajo: sería Nike, no
PayPal.

**9. Convicción.** **Media.** El precio es el argumento; el negocio está en duda. Peso limitado al
20 % y sin ampliaciones.

### 4.4 Arista Networks (ANET) — 15 %

**1. Qué dijo el corpus.** [Grado C] Solo aparece **enumerada** entre las «comunicaciones ópticas y
redes» de la charla de IA del 15/10 (línea 416), sin cifra ni postura. La tesis es propia y se apoya
en las cuentas del tercer trimestre, publicadas el 3 de noviembre.

**2. Tesis en tres frases.** Arista es el proveedor de red de los centros de datos de IA: **+58,5 %**
de ingresos en el tercer trimestre, la mayor subida desde su salida a bolsa, con margen operativo del
**43,8 %** y **cero deuda**. La compañía subió la guía anual por cuarta vez (**13.300 M$**, +48 %) y
dio para 2027 unos **18.500 M$** (+38-40 %), con el negocio de redes de IA doblando a 7.000 M$. Es la
mejor compañía de la cartera y la más cara: 50 veces beneficios y 36 veces forward.

**3. Métricas (04/11/2026).**

| Métrica | Valor |
|---|---:|
| Capitalización | 235.850 M$ |
| Ingresos TTM | 11.890 M$ · Q3 3.660 M$ (+58,5 %) |
| Beneficio operativo | 5.210 M$ · margen 43,8 % |
| Flujo de caja libre | 5.020 M$ · margen 42,2 % |
| Caja neta | **14.360 M$** · deuda 0 |
| ROE / ROIC | 33,5 % / 239,9 % |
| PER trailing / forward | 50,1x / 36,2x |
| PEG | 1,31 |
| Guía 2026 / 2027 | 13.300 M$ (+48 %) / ≈18.500 M$ (+38-40 %) |
| Consenso | 30 analistas, «Strong Buy», objetivo 245,43 $ (+31,3 %) |

**4. Por qué no es la primera posición.** Porque todo lo bueno ya está en el precio: sube un 19 % en
un año, cotiza a 36 veces beneficios futuros y su crecimiento depende del mismo capex de IA que el
corpus señala como riesgo. Un PEG de 1,31 no es caro para ese crecimiento, pero exige que 2027 se
cumpla **entero**.

**5. ¿Comprar hoy?** **Solo una tanda (7,5 % del peso) y el resto condicionado.** A 187,53 $ se paga
el escenario central. La segunda mitad entra si el precio corrige a **150 $** (≈−20 %) sin que la guía
de 2027 se toque, o si el cuarto trimestre confirma los 4.000 M$ de ingresos y el margen del 48-49 %.

**6. Respaldo externo.**
[Hecho] Nota de resultados de Arista, 3/11/2026: ingresos de 3.660 M$ (+58,5 %), guía de Q4 de
3.900-4.000 M$ y margen operativo non-GAAP del 48-49 %.
https://www.arista.com/en/company/news/press-release/25025-pr-20261103
[Hecho] Yahoo Finance, 04/11/2026: guía anual elevada a 13.300 M$ (+48 %) y primera guía de 2027 de
≈18.500 M$, con redes de IA doblando a 7.000 M$.
https://finance.yahoo.com/technology/ai/articles/arista-networks-shares-surge-9-133920965.html
[Contrapunto] El corpus (Horos): «no nos gusta pagar por expectativas que no controlamos». Arista es
exactamente eso, con la diferencia de que aquí las expectativas vienen con guía de la compañía.

**7. Riesgos.** (a) Dependencia de unos pocos clientes hiperescaladores; (b) competencia de Broadcom
y de la red propia de Nvidia; (c) el capex de IA se frena y la guía de 18.500 M$ se queda en nada;
(d) múltiplo: una rebaja de crecimiento del 40 % al 25 % justificaría la mitad del precio.

**8. Señal de invalidación.** Guía de 2027 recortada por debajo de 17.000 M$ **o** margen operativo
non-GAAP por debajo del 42 % dos trimestres.

**9. Convicción.** **Media.** Gran negocio, precio exigente, entrada partida.

## 5. Lista de espera: Cloudflare (NET)

Es la única compañía de la cartera que el corpus respalda con **grado A** («una empresa en cartera»
del invitado de la charla de IA, que además describe su uso interno de la IA: el consejero delegado
eliminó el 20 % de los puestos de medición y cree que puede quitar hasta la mitad). Y es, con
diferencia, la más cara de todas:

| Métrica | Valor |
|---|---:|
| Capitalización | 94.070 M$ |
| Ingresos TTM | 2.510 M$ · Q2 +36 % · guía 2026 2.864-2.870 M$ (+32 %) |
| Beneficio neto | **−206 M$** (pérdida) |
| Flujo de caja libre | 342 M$ · **P/FCF 285x** · P/S 38,8x |
| PER forward | 178,6x |
| Retención neta de clientes | 120 % · 4.698 clientes grandes (+27 %) |
| Consenso | «Buy», objetivo 345,16 $ (+30,7 %) |

**Veredicto: no se compra hoy, y menos la víspera de resultados.** Presenta el **5 de noviembre**
(después del cierre). A 285 veces flujo de caja libre se paga el escenario perfecto; el propio corpus
avisa de que «no nos gusta pagar por expectativas que no controlamos». **Regla de entrada escrita:**
entra con un 5 % (financiado con la liquidez) si se cumple **una** de estas dos condiciones: (a) el
precio corrige un 30 % desde 264 $ sin recorte de la guía anual, o (b) el crecimiento de ingresos se
mantiene ≥30 % durante dos trimestres y el margen de flujo de caja libre supera el 15 %.

## 6. Descartadas, con el número delante

### 6.1 Por dividendo (la regla de la casa)

| Empresa | Ticker | Rendimiento | Qué se pierde |
|---|---|---:|---|
| **PayPal** | PYPL | **0,93 %** (0,56 $/año) | **La mejor tesis del corpus**: Horos la tiene en cartera a 4-5 veces FCF de tres años, con 200 y pico millones de usuarios y 70 transacciones al año. Es «la inversión más incómoda» del fondo |
| **Booking** | BKNG | **0,98 %** (1,68 $/año) | Entrada de Horos este año; potencial que el gestor cifra «por decir una cifra» en el 70 % |
| **Prosus** | PRX.AS | **0,79 %** | La vía sin descuento de holding a Tencent (Naspers reparte más) |
| **Tencent** | 0700.HK | **1,32 %** | 9 veces FCF contra valor de empresa a tres años; la valoración más atractiva desde que Horos es accionista |
| **TGS** | TGS.OL | **4,41 %** | Principal posición de Horos, comprada a 3-4 veces FCF de tres años |
| **NTT** | 9432.T | **3,29 %** | Primera posición de Arcus Japan, 1,28 veces valor en libros y PER 11 |
| **Honda** | 7267.T | **3,89 %** | 0,54 veces valor en libros y PER 8 en la cartera de Arcus |
| **Universal Music** | UMG.AS | **2,96 %** | El acceso a UMG vía Bolloré (que también reparte) |
| **Microsoft / Alphabet / Meta / Nvidia** | MSFT, GOOGL, META, NVDA | 0,8 % / 0,30 % / 0,33 % / 0,49 % | Las cuatro reparten, aunque sea simbólico. La regla no distingue tamaños |
| **LVMH / ASML / TotalEnergies** | MC.PA, ASML.AS, TTE.PA | 3,4 % / 0,5 % / 4,2 % | Ya descartadas en `propuesta-investigacion.md` por el mismo motivo |
| **Coca-Cola / McDonald's / Nike** | KO, MCD, NKE | reparten | Además, el corpus las critica por caras o por deterioro |
| **Exor / Ferrari / Antin / Pluxee / Prosegur** | — | `n/d` | Reparten dividendo; la cifra no se verificó en esta pasada y no hace falta: el hecho basta |

**La decisión que queda en manos del titular.** Si la regla admitiera excepciones por rendimiento
simbólico (<1 %), entrarían **PayPal y Booking**, que son las dos mejores tesis del corpus con
diferencia. No se propone: la regla de `finance/portfolio/README.md` es explícita («aunque sea la
clase más barata») y se aplica tal cual. Queda escrito para que la excepción, si algún día se hace,
sea una decisión y no un descuido.

### 6.2 Por tesis o por precio

| Empresa | Motivo, con el número |
|---|---|
| **Cloudflare (NET)** | 285x FCF y PER forward 178x. Lista de espera con regla escrita (§5) |
| **AMD** | Sin dividendo, pero **124x beneficios trailing y 81x EBITDA**, beta 2,54 y +88 % en un año. El corpus solo la enumera: no hay tesis que pague ese múltiplo |
| **Tesla** | Sin dividendo y **descartada explícitamente** por dos voces del corpus: 220 veces beneficios (Carlos, 18/10) y «no entiendo cómo cotiza a estos múltiplos» (Renta 4, 22/10) |
| **OHLA (OHLA.MC)** | Sin dividendo desde 2016, 0,7 veces valor en libros y en la cartera de Andrés, pero capitaliza **482 M€**, PER 34,9x, **−21 % en un año** y volatilidad a tres años del **49,8 %**. Es una apuesta de reestructuración, no una inversión a largo plazo; merece ficha propia, no un hueco en esta cartera |
| **Nike** | El corpus la usa como contraejemplo: cae un 80 % y sigue a 27 veces beneficios y 23 veces EBIT (Horos, 36:51; Carlos, 67:41) |
| **Coca-Cola / Walmart / Costco** | Criticadas por caras: 40 y «30 y pico» veces beneficios (Horos, 1:05:43) |
| **CoreWeave / Oracle (como tesis IA)** | El corpus las señala como el punto de estrés de la financiación de la IA: CDS de CoreWeave a 1.194 pb, cuatro veces los de Oracle (23/10) |
| **Intel** | Suspendió el dividendo, pero cae un 17 % el día de la entrevista y no tiene tesis en el corpus |
| **Arista, Adobe** | Entran con grado C y peso limitado; se documenta aquí que la evidencia es débil |

## 7. Riesgos estructurales de la propuesta

1. **Es la antítesis de la cartera vigente.** El 50/50 de MyInvestor es value + indexado + renta fija
   corta, con 0 % de calidad americana. Esta propuesta es 100 % tecnología americana y dos de las
   cuatro posiciones cotizan por encima de 30 veces beneficios. **No se financia vendiendo el 50/50**:
   o es dinero nuevo, o no se hace.
2. **Concentración.** Cuatro nombres. El propio Andrés avisa: «no deberíais tener gran parte de
   vuestro dinero en una única empresa» (16/10). Con 30 % en Amazon, esta cartera incumple esa regla
   si se compara con un patrimonio completo; es aceptable solo como satélite.
3. **Beta y caída.** Beta ponderada 1,37 (1,52 sobre lo invertido). En un escenario tipo 2008, donde
   el 50/50 estima −21,5 %, esta cartera caería del orden de **−45 % a −55 %**. No es una estimación
   de modelo, es la beta aplicada a una caída de mercado del 35-40 %.
4. **Divisa.** 100 % dólares. EUR/USD a 1,1225; una apreciación del euro del 10 % resta ≈9 % a la
   cartera en euros, sin que ninguna empresa haya hecho nada mal.
5. **Impuesto de sucesiones americano.** Las acciones de compañías estadounidenses son activos
   situados en EE. UU. Para un no residente, el umbral de declaración (formulario 706-NA) es de
   **60.000 $** y el tipo puede llegar al **40 %**, con independencia del bróker donde se custodien.
   Fuente: IRS, «Some nonresidents with U.S. assets must file estate tax returns».
   https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns
   Con 20.000 € no se llega; por encima de 60.000 $ en acciones americanas hay que hablarlo con un
   asesor antes de seguir aportando.
6. **Riesgo de tesis en tres de las cuatro.** Netflix, Adobe y Arista pueden romperse por
   desaceleración. Solo Amazon tiene un foso que el corpus considere estructural (AWS).

## 8. Lo que queda abierto

- **Importe real.** La propuesta está calculada sobre 20.000 €. Si el titular pone otra cifra, los
  pesos se mantienen y las acciones se recalculan.
- **Comisión de cambio y disponibilidad de cada ticker en MyInvestor.** La tarifa publicada es
  0,12 % + 0,30 % de cambio, mínimo 3 € y máximo 25 €, sin custodia; falta confirmar en la pantalla
  de compra que los cuatro valores están operables y el spread del momento.
- **La excepción del dividendo simbólico (PayPal y Booking).** Es la única decisión que cambiaría el
  mapa: dos tesis grado A en lugar de dos grado C.
- **Cloudflare después del 5/11.** Con los resultados en la mano, la regla de entrada de §5 se revisa
  o se mantiene.
- **OHLA.** Merece ficha propia con dos fuentes y precio; hoy no la tiene y por eso no entra.
- **Sucesiones.** Si la cartera crece por encima de 60.000 $, decidir entre asumir el riesgo, reducir
  exposición directa o buscar vehículos UCITS (que no resuelven el dividendo, pero sí la situación).

> No es asesoramiento financiero. Los pesos son una decisión de cartera sobre cuentas publicadas,
> múltiplos verificados el 04/11/2026 y fuentes citadas; no son una previsión de rentabilidad.

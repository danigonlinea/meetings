---
title: "Cartera-ai: 150.000 € en nueve fondos indexados y seis acciones, 75/25"
date: 2026-11-14
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai, 150k, indexados, acumulacion, myinvestor, acciones, diversificacion, 75-25]
status: final
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai/cartera-actual.md
  - finance/portfolio/cartera-myinvestor/propuesta-actual.md
  - finance/portfolio/cartera-myinvestor/propuesta-acciones.md
---

# Cartera-ai — 150.000 €, 14/11/2026

> **Qué es.** Una cartera nueva de **150.000 €** diseñada desde cero con tres reglas del titular:
> todos los fondos tienen que existir en el catálogo de MyInvestor, **ninguno reparte dividendos**
> (solo clases de acumulación) y la composición es libre. Resultado: **9 fondos indexados + 6 acciones**,
> **75,0 % de renta variable / 25,0 % de renta fija** en look-through estricto, **170,10 €/año** de coste
> (0,113 % del total).
>
> **Qué no es.** No es una cartera temática de inteligencia artificial. «cartera-ai» se lee aquí como
> **la cartera diseñada por la IA**, sin tesis sectorial: el encargo pide diversificación, no una apuesta
> por el sector tecnológico. Si el nombre quería decir «cartera de IA», este documento no sirve y hay que
> rehacerlo con otro mandato.
>
> **No se consolida con las otras carteras del repositorio.** Las 97.000 € de MyInvestor, las 34.769 €
> de Renta 4 y estas 150.000 € son patrimonios separados: no se suman, no se comparan y no se rebalancea
> una contra otra (regla de `finance/portfolio/README.md`). El perfil de riesgo se fija aquí, sobre estos
> 150.000 € aislados.
>
> **Método.** Catálogo MyInvestor vía MCP el 14/11/2026: 2.409 fondos, 266 indexados. Todas las fichas
> son de `get_funds`, NAV 11/11/2026. Las seis acciones salen del catálogo de acciones del bróker
> (`get_instruments`, 14/11/2026). Cada cifra de este documento es de ficha; lo que no lo es, va marcado.
>
> **No es asesoramiento financiero.** La decisión es del titular.

---

## 1. Las tres restricciones, y lo que implican

| Restricción del titular | Cómo se cumple | Lo que cuesta |
| --- | --- | --- |
| Todos los fondos, en MyInvestor | 9 ISIN verificados uno a uno contra el catálogo (`get_funds`, sin `missing`) | Nada: los 266 indexados del catálogo dan de sobra |
| Ningún fondo que reparta dividendos | `distributing = 0` en las nueve fichas | Se renuncia a clases «Inc» más baratas en dos casos |
| Composición y perfil libres | 75/25 con 20 % en acciones individuales | Es una decisión, no una restricción: se justifica en §2 |

**Supuestos que el titular no ha dado y que esta propuesta asume** (si alguno es falso, cambia la cartera):

1. **Horizonte ≥ 10 años** y sin necesidad de rescatar estas 150.000 € antes. Si el dinero puede hacer
   falta en 3-5 años, la RV baja a 50-60 % (§2).
2. **Dinero nuevo**, no un traspaso: se entra desde liquidez, así que no hay plusvalía que cristalizar.
3. **Aguante conductual**: la cartera puede caer ≈ −46.000 € en un año malo (§2). Si eso lleva a vender,
   el diseño no vale.

**Sin ETFs.** No es una restricción del titular, es la regla de la casa: un ETF no admite traspaso y
cada rebalanceo tributa al 19-23 %. Todo el bloque de fondos es IIC armonizada.

---

## 2. Cuánta renta variable, y por qué 75

No hay perfil declarado. El 75 % sale de tres hechos medibles y uno conductual:

| Señal | Dato (14/11/2026) | Efecto |
| --- | --- | ---: |
| **Coste real del dinero** | TIR de la RF corta 4,24-4,65 % frente a inflación 3,8 % → solo +0,4 a +0,8 % real (`cartera-myinvestor/propuesta-actual.md`, §2, 04/11/2026) | Empuja a RV |
| **Prima RV-bono** | *Earnings yield* 6,65 % − bono 4,24 % = **2,4 pp** (pánico si < 1 pp) | Empuja a RV |
| **Concentración del índice** | 46 % del S&P en tecnología y 34 % en siete valores; cuatro de las seis acciones de §5 caen −21 % a −43 % en 12 meses | Frena: no se compra el índice puro |
| **Horizonte y liquidez** | ≥10 años, sin rescate previsto, dinero nuevo | Permite 75 % |

**Decisión: 75,0 % de RV (112.500 €) / 25,0 % de RF (37.500 €)**, look-through estricto por el
`alloc_equity` de cada ficha y las acciones al 100 %.

| RV | RF | Caída tipo 2008 | En euros | Retorno (EY solo) | Retorno (EY + crecimiento 4 %) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 50 % | 50 % | −21,5 % | −32.250 | 5,45 % | 7,45 % |
| 60 % | 40 % | −25,2 % | −37.800 | 5,69 % | 8,09 % |
| 70 % | 30 % | −28,9 % | −43.350 | 5,93 % | 8,73 % |
| **75 %** | **25 %** | **−30,8 %** | **−46.125** | **6,05 %** | **9,05 %** |
| 85 % | 15 % | −34,6 % | −51.750 | 6,29 % | 9,69 % |

Caída = −(40 % × RV + 3 % × RF), el escenario de 2008. Retorno = RV × *earnings yield* 6,65 % +
RF × 4,24 %; con crecimiento, se suman 4 puntos al EY de la RV.

**Peor caso con las acciones castigadas.** Si el bloque de acciones cae un 50 % y los fondos de RV un
40 %, la caída es **−32,8 % (−49.125 €)**. Ese es el número que hay que poder mirar sin vender.

**Si el titular prefiere dormir mejor:** mover 15.000 € de RV a RF deja la cartera en 65/35 y la caída
en −27,1 %; mover 22.500 € la deja en 60/40 y −25,2 %. La cartera no cambia de fondos, solo de pesos.

---

## 3. La cartera (150.000 €: 9 fondos + 6 acciones)

| # | Bloque | Vehículo | ISIN / ticker | € | % total | RV dentro | TER |
| --: | --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | **Núcleo global desarrollado** | iShares Developed World Index (IE) S Acc EUR | IE000ZYRH0Q7 | 37.500 | 25,0 % | 99,96 % | 0,06 % |
| 2 | **RV Europa** | Fidelity MSCI Europe Index EUR P Acc | IE00BYX5MD61 | 11.250 | 7,5 % | 99,38 % | 0,10 % |
| 3 | **RV Japón** | Fidelity MSCI Japan Index EUR P Acc | IE00BYX5N771 | 6.000 | 4,0 % | 98,62 % | 0,10 % |
| 4 | **RV Pacífico ex-Japón** | Fidelity MSCI Pacific ex Japan USD P Acc | IE00BDZVHT63 | 3.000 | 2,0 % | 99,06 % | 0,13 % |
| 5 | **RV emergentes** | iShares Emerging Markets (IE) S Acc EUR | IE000QAZP7L2 | 9.750 | 6,5 % | 100 % | 0,16 % |
| 6 | **RV small caps** | Vanguard Global Small-Cap Index EUR Acc | IE00B42W4L06 | 9.000 | 6,0 % | 99,94 % | 0,29 % |
| 7 | **Activos reales (REITs)** | iShares Developed Real Estate D Acc EUR | IE00BDRK7P73 | 6.000 | 4,0 % | 98,85 % | 0,17 % |
| 8 | **RF agregada 1-5Y EUR cubierta** | iShares Global Aggregate 1-5Y Bond S Acc EUR H | IE0004ZP1ND3 | 21.000 | 14,0 % | 0 % | 0,08 % |
| 9 | **RF corporativa EUR 1-5Y** | Amundi EUR Corporate Bond 1-5Y ESG AE Acc | LU1525412281 | 16.500 | 11,0 % | 0 % | 0,35 % |
| 10 | **Acción · conglomerado/financiero** | Berkshire Hathaway B | BRK/B | 5.000 | 3,3 % | 100 % | — |
| 11 | **Acción · consumo y nube** | Amazon | AMZN | 5.000 | 3,3 % | 100 % | — |
| 12 | **Acción · ocio digital** | Netflix | NFLX | 5.000 | 3,3 % | 100 % | — |
| 13 | **Acción · salud** | Intuitive Surgical | ISRG | 5.000 | 3,3 % | 100 % | — |
| 14 | **Acción · pagos (Europa)** | Adyen | ADYEN.AS | 5.000 | 3,3 % | 100 % | — |
| 15 | **Acción · e-commerce (LatAm)** | MercadoLibre | MELI | 5.000 | 3,3 % | 100 % | — |
| | **TOTAL** | **9 fondos + 6 acciones** | | **150.000** | **100 %** | **74,8 %** | **0,113 %** |

**Reparto estricto:** RV **112.230 € (74,8 %)** · RF **37.770 € (25,2 %)**. La diferencia con los 112.500 €
nominales son 270 € de liquidez dentro de las fichas (0,1-1,4 % por fondo).

**Las nueve clases son de acumulación** (`distributing = 0` en las nueve fichas). Ninguna paga cupón ni
dividendo: todo se reinvierte en el valor liquidativo.

---

## 4. Por qué cada fondo, con la pega en la misma fila

| Fondo | El dato (ficha 11/11/2026) | Papel | La pega |
| --- | --- | --- | --- |
| **iShares World S** | TER **0,06 %**, el más barato del catálogo para el MSCI World; 1A +15,5 %; 99,96 % RV | El núcleo: 1.200 empresas de 23 países en un solo fondo | **La clase S no publica 3A/5A** (clase nueva). El fondo existe desde 2010, la clase no tiene historial propio. Alternativa con historial: Fidelity World EUR P Acc (IE00BYX5NX33, 0,12 %, 3A +18,9 %, 5A +11,1 %) por 22,50 €/año más |
| **Fidelity Europe** | TER 0,10 %; 3A +17,4 %; 5A +9,7 %; vol 3A 10,0 % (la más baja de la RV) | 350 empresas de 15 países; sector más expuesto a financieras e industria, no a tecnología | 21,8 % Reino Unido: no es la eurozona, y el fondo lo dice |
| **Fidelity Japan** | TER 0,10 %; 3A +17,1 %; 5A +9,4 %; 98,6 % Japón | Diversificación real: gobierno corporativo en mejora y moneda distinta | SRRI 5 y 22 % industria: es cíclico, no defensivo. El 4 % es techo, no suelo |
| **Fidelity Pacific ex Japan** | TER 0,13 %; 3A +17,2 %; 5A +6,9 % | Completa el mapa desarrollado de Asia-Pacífico | **63 % Australia y 46 % financieras**: en la práctica son bancos australianos. Por eso pesa solo 2 % |
| **iShares Emerging Markets S** | TER 0,16 %; 1A +17,0 %; YTD +18,6 %; 100 % RV | 1.100 empresas; 27 % Taiwán, 20,5 % Corea, 19,5 % China, 11,2 % India | **41,8 % tecnología** (semiconductores) y sin 3A/5A publicados. Es la pieza más volátil de los fondos (vol 1A 27,3 %) |
| **Vanguard Global Small-Cap** | TER 0,29 %; 3A +18,2 %; 5A +6,7 %; 60,9 % EE.UU., 13 % Japón | El tramo que el MSCI World no tiene; 8 % inmobiliario y 12 % salud dentro | Es el fondo más caro de la RV (0,29 %) y el que más sufre en recesión |
| **iShares Developed Real Estate** | TER 0,17 %; 3A +10,4 %; 5A +1,0 %; 97 % inmobiliario | Activos reales con rentas ligadas a la inflación | **5A +1,0 % anual**: el sector lleva una década mala. Se compra por diversificación, no por retorno |
| **iShares Global Agg 1-5Y EUR H** | TER **0,08 %**; SRRI 2; vol 1A 1,7 %; 58 % gobierno, 27 % corporativo | El amortiguador: duración corta y divisa cubierta | Solo +0,41 % en 12 meses: es colchón, no rentabilidad |
| **Amundi EUR Corp 1-5Y ESG** | TER 0,35 %; SRRI 2; 3A +3,5 %; vol 3A 2,2 % | Crédito corporativo europeo a corto plazo, sin riesgo de divisa | Es el fondo más caro de la cartera (58 €/año de los 170) y 0,35 % por un indexado es alto |

---

## 5. Las seis acciones (30.000 €, 20 %)

Todas verificadas en el catálogo de acciones del bróker y **ninguna reparte dividendo** (`dividend_yield`
nulo en las seis fichas; en MELI el último dividendo es de 2017). A 14/11/2026:

| Empresa | Ticker | Mercado | Sector | PER | 1A | Vol 3A | € | La tesis en una línea | La pega / señal de invalidación |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| **Berkshire Hathaway B** | BRK/B | NYSE | Financiero / conglomerado | **14,4x** | +14,1 % (clase A) | 16,7 % | 5.000 | Caja, seguros y ferrocarril: el activo más descorrelacionado de la lista, sin dividendo por diseño | Tamaño: 1,22 billones de dólares. A ese tamaño, el *alpha* de Buffett ya es el del S&P. Se invalida si el *payout* cambia o si la caja se destina a una compra cara |
| **Amazon** | AMZN | Nasdaq | Consumo / nube | 21,0x | +6,9 % | 29,1 % | 5.000 | AWS y publicidad financian el retail; el múltiplo ya no es de empresa de crecimiento | 37,9 % de volatilidad a 1 año y capex de IA sin retorno demostrado. Se invalida si AWS desacelera dos trimestres seguidos |
| **Netflix** | NFLX | Nasdaq | Ocio digital | **18,3x** | **−43,2 %** | 35,7 % | 5.000 | Tras caer un 43 %, paga 18 veces beneficios: el mercado ha dejado de pagar crecimiento | El crecimiento de suscriptores está agotado; el negocio pasa a depender de subir precios y de publicidad. Se invalida si el margen operativo baja de dos dígitos |
| **Intuitive Surgical** | ISRG | Nasdaq | Salud | **54,8x** | −21,4 % | 28,7 % | 5.000 | Cuasi-monopolio en cirugía robótica, ingresos recurrentes por instrumentos | **54,8 veces beneficios es el múltiplo más caro de la cartera**: paga perfección. Se invalida si la adopción de da Vinci 5 se retrasa o entra un competidor serio |
| **Adyen** | ADYEN.AS | Euronext Ámsterdam | Pagos | 25,3x | **−40,4 %** | **57,3 %** | 5.000 | Plataforma de pagos con margen creciente; cae un 40 % y cotiza a 25 veces | **La volatilidad más alta de la cartera (57 % a 3 años)**. Se invalida si el crecimiento de volumen baja del 20 % o si pierde un cliente grande |
| **MercadoLibre** | MELI | Nasdaq | E-commerce / fintech (LatAm) | 40,5x | −28,0 % | 36,8 % | 5.000 | E-commerce + pagos en Latinoamérica, con el negocio financiero creciendo más que el comercial | Riesgo país (Brasil, Argentina, México) y 40 veces beneficios. Se invalida si Mercado Pago se queda sin margen por la competencia o por regulación |

**Lo que hay que decir en voz alta.** Cuatro de las seis (NFLX, ISRG, ADYEN, MELI) vienen de caídas del
21-43 % en doce meses. Comprarlas no es «calidad a buen precio» por definición: es una apuesta a que el
múltiplo deja de comprimirse. Por eso el bloque es el 20 %, no el núcleo, y por eso ninguna posición
individual pasa del 3,3 % del total.

**Reparto del bloque:** 4 EE.UU. (20.000 €), 1 Países Bajos (5.000 €), 1 Latinoamérica cotizada en EE.UU.
(5.000 €). Sectores: consumo 2, financiero 1, salud 1, tecnología 1, ocio digital 1.

---

## 6. Diversificación medida

**Por clase de activo (look-through):** RV 74,8 % · RF 25,2 %. En % de la cartera: núcleo global
desarrollado (World) 25,0 %, Europa 7,5 %, Japón 4,0 %, Pacífico ex-Japón 2,0 %, emergentes 6,5 %,
small caps 6,0 %, inmobiliario 4,0 %, acciones individuales 20,0 %, renta fija 25,0 %.

**Por geografía (región declarada por cada ficha + domicilio de cada acción):**

| Región | € | % cartera |
| --- | ---: | ---: |
| Estados Unidos | 56.400 | 37,6 % |
| Renta fija global y europea | 37.500 | 25,0 % |
| Japón | 9.700 | 6,5 % |
| Taiwán, Corea, China e India | 7.700 | 5,1 % |
| Alemania, Francia, España y resto de Europa | 6.800 | 4,6 % |
| Países Bajos (Adyen) | 5.000 | 3,3 % |
| Uruguay / Latinoamérica (MercadoLibre) | 5.000 | 3,3 % |
| Reino Unido | 4.300 | 2,9 % |
| Suiza | 2.800 | 1,8 % |
| Australia | 2.600 | 1,7 % |
| Brasil, Sudáfrica y resto de emergentes | 2.100 | 1,4 % |
| Canadá | 1.700 | 1,1 % |
| Singapur, Hong Kong y Nueva Zelanda | 1.300 | 0,9 % |
| Suecia y resto desarrollado | 6.200 | 4,1 % |

**Estados Unidos pesa el 37,6 % de la cartera, no el ≈54 % que saldría de un MSCI World puro** con este
75 % de RV. Es una decisión, no un descuido: el índice americano concentra 46 % en tecnología y 34 % en
siete valores, y Europa cotiza a 13,6 veces frente a 18,7 del S&P 500 (datos del 04/11/2026 en
`cartera-myinvestor/propuesta-actual.md`, §2). La contrapartida es que si EE.UU. sigue ganando, esta
cartera lo verá desde lejos.

**Sectores: mínimos declarados, no totales.** Sumando solo las seis primeras posiciones sectoriales que
publica cada ficha (el resto no se declara), la cartera tiene **al menos** 16 % en tecnología, 13 % en
financiero, 11 % en consumo, 8 % en salud, 7 % en industria, 6 % en comunicación y 5 % en inmobiliario.
Son suelos: la exposición real es algo mayor en todos.

**Lo que esta cartera NO tiene:** oro ni materias primas (no hay fondo físico en el catálogo; los de
mineras no son un hedge), energía como bloque (solo la que llevan los índices), ni un fondo activo con
gestor. Cada una se descarta con su motivo en §9.

---

## 7. Coste

| Concepto | €/año | % sobre 150.000 |
| --- | ---: | ---: |
| TER de los nueve fondos (ponderado, 0,142 % sobre 120.000 €) | **170,10** | **0,113 %** |
| Comisión de compra/venta de acciones de MyInvestor | no publicada en el MCP | — |
| Custodia y traspasos de fondos | 0 € en MyInvestor | 0 % |
| **Coste recurrente verificable** | **170,10** | **0,113 %** |

**El desglose:** el Amundi 1-5Y aporta 57,75 € (34 % del coste total con el 11 % del capital) y el
Vanguard Small-Cap 26,10 €. Los siete restantes suman 86,25 €.

**Cuánto cuesta la diversificación:** los 150.000 € en el iShares World al 0,06 % costarían **90 €/año**.
La cartera completa cuesta 80 €/año más y a cambio añade emergentes, small caps, inmobiliario, renta fija
y ocho países que el World no lleva en esa proporción. Ochenta euros al año es ruido; la concentración
del World no lo es.

---

## 8. Ejecución

**15 órdenes, una sesión.** Los fondos se suscriben por importe (no hace falta calcular participaciones);
las acciones, por número entero, con el importe como referencia.

| # | Orden | Importe |
| --: | --- | ---: |
| 1 | Suscribir iShares Developed World Index S Acc EUR (IE000ZYRH0Q7) | 37.500 € |
| 2 | Suscribir Fidelity MSCI Europe Index EUR P Acc (IE00BYX5MD61) | 11.250 € |
| 3 | Suscribir Fidelity MSCI Japan Index EUR P Acc (IE00BYX5N771) | 6.000 € |
| 4 | Suscribir Fidelity MSCI Pacific ex Japan USD P Acc (IE00BDZVHT63) | 3.000 € |
| 5 | Suscribir iShares Emerging Markets S Acc EUR (IE000QAZP7L2) | 9.750 € |
| 6 | Suscribir Vanguard Global Small-Cap EUR Acc (IE00B42W4L06) | 9.000 € |
| 7 | Suscribir iShares Developed Real Estate D Acc EUR (IE00BDRK7P73) | 6.000 € |
| 8 | Suscribir iShares Global Aggregate 1-5Y Bond S Acc EUR H (IE0004ZP1ND3) | 21.000 € |
| 9 | Suscribir Amundi EUR Corporate Bond 1-5Y ESG AE Acc (LU1525412281) | 16.500 € |
| 10-15 | Comprar BRK/B, AMZN, NFLX, ISRG, ADYEN.AS y MELI | 5.000 € cada una |

**Notas de ejecución:**

- **Horarios de corte distintos.** El World y el Amundi cortan a las 09:00; Fidelity y Vanguard a las
  12:00 o 16:00; el Global Agg a las 09:00. Una sola sesión vale, pero el NAV será de días distintos.
  No cambia nada material.
- **Dos tandas si se prefiere.** La mitad ahora y la otra mitad en 30 días reduce el riesgo de entrar
  justo antes de una caída, a cambio de no entrar si sube. Con dinero nuevo y horizonte largo, la
  alternativa neutra es entrar de una vez; la cartera no depende del punto de entrada.
- **Redondeo de acciones.** MyInvestor puede no admitir fracciones: quedarán 50-200 € sueltos por
  redondeo. Se dejan en liquidez o se suman al fondo 1.
- **Antes de la primera orden:** confirmar la comisión de compraventa de acciones y el mínimo por
  operación. No está en el MCP y condiciona si 5.000 € por acción es eficiente.

---

## 9. Qué se descarta, y por qué

| Candidato | Por qué no entra |
| --- | --- |
| **ETFs** (IWDA, VWCE, CSPX) | No admiten traspaso: rebalancear tributa. Los fondos indexados del catálogo replican lo mismo con TER parecido |
| **Fondos que reparten dividendo** | Restricción explícita del titular. Se descartaron clases «Inc» más baratas (p. ej. World USD Inc) |
| **Un solo fondo World** | Sería más simple y costaría 90 €/año, pero deja fuera emergentes, small caps, inmobiliario y el 72 % de EE.UU. se convierte en el 72 % de todo |
| **Cobas International (activo, 2,33 %)** | El único *alpha* activo verificable del catálogo en la cartera de MyInvestor, pero 2,33 % de TER sobre 150.000 € son 350 €/año para una apuesta de gestor que esta cartera no necesita |
| **Oro y mineras** | No hay fondo de oro físico en el catálogo; los de mineras tienen volatilidad de acción, no de refugio |
| **Temáticos (IA, robótica, ciberseguridad, agua)** | 475 fondos de tecnología en el catálogo. Un temático duplica lo que el núcleo ya lleva y añade riesgo de moda; si el titular quiere una apuesta sectorial, va aparte y con importe pequeño |
| **Cartera automatizada (Rock)** | Encaja en la cartera de MyInvestor como vehículo, pero aquí el encargo es una cartera con nombres y pesos explícitos |
| **iShares Euro IG Corporate 0,12 % en vez del Amundi 1-5Y** | Ahorra 38 €/año, pero alarga la duración al tramo completo (3A +4,0 % frente a +3,5 %). Con el BCE restrictivo, no se alarga duración por 38 € |
| **Prosus (PRX.AS)** | Reparte un 0,75 %: incumple la regla del dividendo. Descartada por ficha, no por opinión |
| **Alphabet, Meta, Visa, Mastercard, Salesforce, Booking** | Todas reparten dividendo desde 2024. La regla las excluye aunque sean mejores negocios |

---

## 10. Límites y señales que obligan a revisar

- **Concentración del núcleo:** el iShares World es el 25 % de la cartera y su 72 % es EE.UU. Si el
  S&P 500 corrige, el núcleo corrige con él. No hay cobertura de divisa en la RV: un euro fuerte resta.
- **Seis acciones, seis riesgos de empresa.** Cualquiera puede caer un 50 % y la cartera pierde 1,7
  puntos. No hay stop: la señal es de tesis (§5), no de precio.
- **Renta fija corta:** si los tipos bajan mucho, este 25 % se queda mirando. Si suben, aguanta.
- **Revisión anual, no trimestral.** Bandas: si un bloque se desvía más de 5 puntos de su peso, se
  rebalancea con aportaciones nuevas antes que vendiendo. Los fondos se traspasan sin tributar; las
  acciones no: vender una acción cristaliza plusvalía, así que el rebalanceo se hace con el bloque de
  fondos.
- **Qué invalidaría el diseño:** que el horizonte real sea < 5 años (bajar RV a 50-60 %), que el titular
  no aguante −46.000 € (bajar RV), o que cambie la regla del dividendo.

---

## 11. Lo que sigue sin decidir

1. **Confirmar el horizonte y el aguante** (§1 y §2): es el único dato que puede cambiar los pesos.
2. **Comisión de acciones de MyInvestor** y mínimo por operación, antes de las órdenes 10-15.
3. **Entrada en una o dos tandas** (§8).
4. **Clase del World:** iShares S al 0,06 % (sin 3A/5A de clase) o Fidelity al 0,12 % (con historial).
5. **Si «cartera-ai» quería decir cartera temática de IA**, este documento no es el encargo: habría que
   rehacerlo con un mandato sectorial.

---

## Fuentes

- **MyInvestor MCP**, 14/11/2026: `list_facets` (2.409 fondos, 266 indexados), `search_funds`,
  `get_funds` (9 fichas, NAV 11/11/2026), `get_instruments` (6 acciones, 14/11/2026).
- **Repositorio:** `finance/portfolio/README.md` (regla de acumulación y de no consolidar),
  `cartera-myinvestor/propuesta-actual.md` (señales macro del 04/11/2026: TIR de la RF 4,24-4,65 %,
  inflación 3,8 %, EY 6,65 %, S&P 18,7x, STOXX 13,6x, concentración 46 %/34 %),
  `cartera-myinvestor/propuesta-acciones.md` (fichas previas de Amazon, Netflix, Berkshire y Adyen).
- **Fecha de la foto:** 14/11/2026. Cualquier NAV posterior cambia los importes, no los pesos.

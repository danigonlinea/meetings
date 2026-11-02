---
title: "Propuesta de investigación — siete ideas con sentido de compra hoy"
date: 2026-11-02
type: portfolio-research
category: finance
tags: [cartera, investigacion, acciones, etfs, calidad, valor, activos-reales, lujo, semiconductores, reits, horizontes, myinvestor]
status: research
related: [finance/portfolio/cartera-actual.md, finance/portfolio/propuesta-actual.md, finance/portfolio/propuesta-alternativa.md]
---

# Propuesta de investigación — 02/11/2026

> **No es la cartera vigente.** La cartera vigente sigue siendo `propuesta-actual.md` (50,0% RV / 50,0% RF,
> 97.000 €, 8 fondos manuales + Rock). Este documento es una **capa de investigación**: identifica qué
> acciones y ETFs tendrían sentido de compra hoy, con qué horizonte, con qué respaldo y a qué precio.
> Si se adopta, sus conclusiones se incorporan a `propuesta-actual.md` y este anexo **se borra** (`git rm`).

## 0. Resumen ejecutivo

La cartera actual es sólida y barata (TER 0,655%, 17 posiciones, 50/50, carry de renta fija 4,79%),
pero tiene tres huecos claros: **0% de acciones directas, 0% de factor calidad y 0% de activos reales**.
No propongo reconstruirla. Propongo una **cartera satélite de 9.000 € (9,3% del total)** financiada con
recortes en las posiciones de renta variable más solapadas, manteniendo el 50/50 y sin tocar la renta fija.

| # | Activo | Ticker/ISIN | Tipo | Horizonte | Riesgo | Peso satélite | Convicción |
|--:|---|---|---|---|---|---:|---|
| 1 | TotalEnergies | TTE.PA | Acción | Corto (0-12 m) | Medio | 2.000 € | Media-alta |
| 2 | Microsoft | MSFT | Acción | Medio (1-5 a) | Medio | 2.500 € | Alta |
| 3 | ASML | ASML.AS | Acción | Medio (1-5 a) | Alto | 1.500 € | Media-alta |
| 4 | LVMH | MC.PA | Acción | Largo (>5 a) | Medio-alto | 1.500 € | Media-alta |
| 5 | VanEck Global Real Estate | TRET.DE | ETF | Largo (>5 a) | Medio | 1.500 € | Media |

**Ideas de calidad que quedan fuera de la cartera modelo por tamaño, no por tesis:** Munich Re (MUV2.DE),
porque cotiza por encima del precio objetivo de consenso; e iShares Edge MSCI World Quality Factor (IS3Q.DE),
porque con 1.000 € sería una posición fragmentada. Ambas se documentan en §3.6 y §7.

**La conclusión incómoda:** la bolsa americana cotiza a 18,7x y concentra el 46% del S&P en tecnología.
Comprar MSFT es pagar 26x forward por la mejor empresa del mundo; tiene sentido con un 13% de descuento
sobre valor razonable, pero no es una ganga. Las mejores relaciones riesgo/retorno de esta lista están en
Europa (TTE 8,3x, MUV2 10,6x, LVMH 16,5x) y en activos reales (TRET), no en el índice global.

## 1. Punto de partida: qué tiene y qué le falta a la cartera actual

### 1.1 Lo que hay (97.000 €, 50,0% RV / 50,0% RF)

| Bloque | Fondo | ISIN | € | Peso | TER |
|---|---|---:|---:|---:|---:|
| RF corta IG | Neuberger Short Duration Euro Bond U | IE00BL1GVT98 | 31.900 | 32,9% | 0,38% |
| RF flexible | DNCA Alpha Bonds A | LU1694789451 | 5.000 | 5,2% | 1,31% + éxito |
| Crédito | Carmignac Credit A | LU1623762843 | 5.000 | 5,2% | 1,20% + éxito |
| RV value Europa small/mid | MyInvestor Value C | ES0165243025 | 5.000 | 5,2% | ~1,42% + 9% éxito |
| RV value global | Cobas International P | LU1598719752 | 5.000 | 5,2% | 2,33% |
| RV small cap global | Vanguard Global Small-Cap Index EUR Acc | IE00B42W4L06 | 3.700 | 3,8% | 0,29% |
| RV Europa large cap | Fidelity MSCI Europe Index EUR P Acc | IE00BYX5MD61 | 5.000 | 5,2% | 0,10% |
| RV emergentes | iShares Emerging Markets Index S Acc EUR | IE000QAZP7L2 | 6.400 | 6,6% | 0,16% |
| Cartera indexada 78/22 | Rock (MyInvestor) | — | 30.000 | 30,9% | 0,41% todo incluido |
| | **TOTAL** | | **97.000** | **100%** | |

Datos de `propuesta-actual.md` (31/10/2026) y fichas MyInvestor MCP. Métricas agregadas: TER 0,655%;
carry RF 4,79%; duración 3,67 años; 17 posiciones; caída estimada en escenario 2008 ≈ −21,5%.

### 1.2 Los huecos que esta investigación cubre

| Hueco | Situación actual | Por qué importa | Qué lo cubre |
|---|---|---|---|
| Acciones directas | 0% | Todo el riesgo de empresa se compra a través de fondos; no se puede elegir calidad individual ni aprovechar descuentos concretos | MSFT, ASML, LVMH, TTE |
| Factor calidad | 0% | La cartera es indexada + value; no tiene compounders de márgenes altos y bajo capital | MSFT/LVMH + IS3Q (alternativa) |
| Activos reales | 0% | 0% inmobiliario, 0% infraestructura, 0% oro; la inflación se combate con bonos y valor, no con rentas reales | TRET |
| Cobertura de inflación | 0% ligados a inflación | La inflación de la eurozona se proyecta en 3,0% para 2026 (BCE); la cartera no tiene un activo que pague cupón ligado a IPC | TRET (rentas indexadas) + valoración de §7 |
| Dependencia de Rock | 30,9% en una cartera automatizada 78/22 | Duplica S&P 500, Europa, Japón y emergentes; el 56% de la RV es USA | La satélite añade Europa y activos reales, no más beta USA |

**Restricción autoimpuesta:** no romper el 50/50, no pagar comisiones activas altas (nada por encima del
1,1% salvo el value ya existente), no duplicar exposiciones y no comprar nada que no tenga al menos dos
fuentes independientes. La satélite se financia **solo con recortes de renta variable**, no con renta fija.

## 2. Metodología y reglas de la casa

1. **Dos fuentes independientes por activo.** Para cada idea se citan al menos dos fuentes o expertos
   cualificados con fecha y enlace. Cuando la única fuente es el propio emisor o un consenso agregado,
   se dice y se baja la convicción.
2. **Hecho / consenso / opinión.** Cada afirmación relevante se etiqueta:
   - **[Hecho]** dato verificable en cuentas, ficha del fondo o comunicado de la empresa.
   - **[Consenso]** media o rango de analistas/publicaciones profesionales.
   - **[Opinión]** juicio del analista, con el razonamiento a la vista.
3. **Valoración con margen de seguridad.** No basta con que algo esté barato: se compara PER, PER forward,
   EV/EBITDA, PEG, precio/valor contable, FCF yield y dividend yield con su historia, sus comparables y
   el coste de capital. Si no hay margen, no se compra.
4. **Calidad y solvencia primero.** Deuda neta/EBITDA razonable, cobertura de intereses, FCF positivo,
   ROIC/ROE sostenido, márgenes estables y ventaja competitiva identificable.
5. **Riesgo explícito.** Volatilidad, máxima caída, beta, correlación y divisa. Si el activo está en otra
   divisa, se indica el riesgo cambiario.
6. **Horizonte, no precio.** Corto plazo = 0-12 meses con catalizadores identificables; medio = 1-5 años
   con crecimiento y valoración; largo = más de 5 años con ventaja estructural. No se compra por el
   movimiento reciente.

**Nota sobre datos y fechas.** Precios de Yahoo Finance a 30/10/2026 y 02/11/2026; fichas de fondos y ETFs
de MyInvestor MCP a 28-30/10/2026; valoraciones de Morningstar y precios objetivo de analistas con fechas
entre el 6 y el 30 de octubre de 2026. Las divisas no se cubren salvo que se indique; un inversor en euros
asume riesgo dólar en MSFT, IS3Q y parte de TRET.

## 3. Recomendaciones

### 3.1 TotalEnergies (TTE.PA) — corto plazo con vocación de medio

**1. Nombre y ticker.** TotalEnergies SE, TTE.PA (FR0000120271).
**2. Tipo.** Acción (compañía integrada de energía).
**3. Horizonte.** Corto plazo (0-12 meses) por catalizadores; si el crudo se mantiene, se puede mantener
como posición de medio plazo por dividendo y recompras.

**4. Tesis en tres frases.**
TotalEnergies es la petrolera europea que sigue creciendo producción mientras sus pares la recortan, con
un modelo integrado que le permite generar caja incluso con precios medios. Cotiza a 8,3x beneficio
forward y paga un 4,2% de dividendo con recompras, una combinación poco habitual en el sector. El Q3 2026
batió expectativas (beneficio ajustado 9.100 M$ y caja operativa 12.300 M$) y el consenso de analistas
mantiene objetivos de 105-108 $ frente a ~94 $ del ADR.

**5. Métricas clave actuales.**

| Métrica | Valor | Contexto |
|---|---:|---|
| Capitalización | 188.500 M€ | Large cap europea |
| PER trailing | 10,0x | Sector energía ~11-12x |
| PER forward | 8,34x | Descuento claro vs mercado |
| EV/EBITDA | 4,62x | Uno de los más bajos del sector |
| ROE (ttm) | 17,8% | Sólido para una integrada |
| Deuda/Patrimonio | 46,1% | Manejable; FCF positivo |
| Dividendo | 4,2% | Cubierto por caja |
| Beta 5 años | 0,04 | Correlación baja con bolsa |
| Rentabilidad 1 año | +65,5% EUR | [Hecho] se ha revalorizado mucho; no es una ganga por precio reciente |
| Rentabilidad 3 años | +16,3% anual | Consistente |

**6. Por qué tiene sentido comprar hoy.**
- **[Hecho]** Q3 2026: beneficio neto ajustado 9.100 M$ y flujo de caja 12.300 M$, con mejora trimestral.
- **[Hecho]** Dividendo trimestral mantenido y programa de recompra; la compañía prioriza retorno al
  accionista.
- **[Consenso]** TD Cowen (Buy, 105 $), UBS (Buy) y Mizuho (Buy, 108 $) reiteran; JPMorgan se queda en
  Neutral. El rango recoge el debate entre valor y ciclo.
- **[Opinión]** El mercado descuenta un crudo normalizado; si Brent se mantiene por encima de 70 $, el
  FCF yield supera el 10% y la valoración sigue siendo atractiva. El riesgo no es la empresa, es el precio
  del petróleo.

**7. Respaldo experto (dos fuentes).**
1. **Morningstar**, «TotalEnergies' Growth Targets Look Safely in Sight; Increasing Fair Value Estimate on
   Higher Prices», 28/10/2026. https://www.morningstar.com/stocks/xpar/tte/analysis — sube valor razonable
   y ve los objetivos de crecimiento alcanzables.
2. **TD Cowen / UBS / Mizuho**, recogidos por StreetInsider y Perplexity Finance en octubre de 2026:
   TD Cowen Buy 105 $, Mizuho Buy 108 $, UBS Buy; JPMorgan Neutral como contrapunto.
   https://www.streetinsider.com/Business+Wire/TotalEnergies+SE:+Third+Quarter+2026+Results/27251062.html
   https://www.perplexity.ai/finance/TTE?comparing=TTE,GALP.LS,ENI.MI,5020.T,OMV.DE,MPC
3. **Contrapunto:** JPMorgan Neutral y la propia Morningstar advierten de que la tesis depende del precio
   de la energía; no es una posición defensiva pura.

**8. Riesgos principales.**
- **Ciclo del crudo:** una normalización de Brent a 60-65 $ recorta beneficio y FCF con rapidez.
- **Márgenes de refino:** el Q3 fue excepcional; la reversión puede ser brusca.
- **Transición energética:** riesgo regulatorio y de inversión en renovables.
- **Concentración geográfica y geopolítica:** Oriente Medio, África, LNG.
- **Momentum:** +65,5% en 12 meses; entrar después de una subida fuerte exige estómago.

**9. Señal de salida / invalidación.**
- Brent por debajo de 65 $ de forma sostenida (>2 trimestres) con FCF yield <6%.
- Recorte del dividendo o suspensión de recompras.
- Deuda neta/EBITDA >1,5x o cobertura de intereses <8x.
- Guía de producción a la baja o venta de activos a múltiplos destructivos.

**10. Nivel de convicción.** **Media-alta.** La valoración y la caja son buenas; el ciclo y la subida
reciente impiden ponerla en alta.

---

### 3.2 Microsoft (MSFT) — medio plazo

**1. Nombre y ticker.** Microsoft Corporation, MSFT (US5949181045).
**2. Tipo.** Acción (software y nube).
**3. Horizonte.** Medio plazo (1-5 años).

**4. Tesis en tres frases.**
Microsoft es el compounder más predecible de la gran tecnología: Azure crece por encima del 40%, Office y
Windows generan caja recurrente y el foso económico es amplio. Cotiza un 13% por debajo del valor razonable
de Morningstar (600 $ frente a 521,91 $) después de batir expectativas en el Q1 fiscal 2027. El debate no
es la calidad, es si el capex de 175.000 M$ en IA se convertirá en beneficio o en depreciación.

**5. Métricas clave actuales.**

| Métrica | Valor | Contexto |
|---|---:|---|
| Capitalización | 3.875.800 M$ | Mayor del mundo |
| PER trailing | 27,2x | Prima de calidad |
| PER forward | 26,34x | Descuento moderado vs crecimiento |
| EV/EBITDA | 17,6x | Alto, pero típico de software |
| ROE (ttm) | 34,2% | Excelente |
| Deuda/Patrimonio | 28,5% | Muy baja |
| Crecimiento ingresos (yoy) | 18,8% | Aceleración |
| Dividendo | 0,8% | Simbólico; la caja va a recompras y capex |
| Beta 5 años | 1,04 | En línea con el mercado |
| Valor razonable Morningstar | 600 $ | 4 estrellas, foso amplio, incertidumbre media |
| Descuento actual | ~13% | 521,91 $ (30/10/2026) |

**6. Por qué tiene sentido comprar hoy.**
- **[Hecho]** Q1 fiscal 2027: batió expectativas; la guía apuntaba a un crecimiento de Azure del 44-45% en
  moneda constante tras el 43% del trimestre anterior, y la demanda sigue limitada por capacidad, no por
  pedidos.
- **[Hecho]** Morningstar mantiene valor razonable de 600 $ y foso amplio; el precio está un 13% por debajo.
- **[Consenso]** Wolfe Research subió a Strong Buy el 30/10/2026; JPMorgan Overweight 625 $, Morgan Stanley
  650 $, Deutsche Bank Buy 600 $, Oppenheimer 625 $. El consenso de 57 analistas es compra con objetivo
  medio 609,54 $.
- **[Opinión]** A 26x forward no es barata, pero un crecimiento del 18,8% y un ROE del 34% justifican la
  prima. La compra tiene sentido por el descuento y la visibilidad de Azure, no por el precio reciente.

**7. Respaldo experto (dos fuentes).**
1. **Morningstar**, «Ahead of Earnings: Is Microsoft Stock a Buy, a Sell, or Fairly Valued?», octubre 2026
   (valor razonable 600 $, 4 estrellas, foso amplio). https://global.morningstar.com/en-gb/stocks/ahead-earnings-is-microsoft-stock-buy-sell-or-fairly-valued-2
2. **Wolfe Research**, subida a Strong Buy, 30/10/2026; **JPMorgan** 625 $ y **Morgan Stanley** 650 $,
   recogidos por CNBC y Yahoo Finance el 29-30/10/2026.
   https://www.cnbc.com/2026/10/29/microsoft-beat-the-street-on-earnings-report-heres-what-analysts-say.html
   https://www.marketbeat.com/instant-alerts/analyst-wolfe-research-upgrades-microsoft-nasdaq-msft-to-strong-buy-2026-10-30/
3. **Contrapunto:** el capex de 175.000 M$ y la dependencia de OpenAI son riesgos reales; si Azure se
   desacelera por debajo del 30%, el múltiplo no se sostiene.

**8. Riesgos principales.**
- **Capex y retorno de la IA:** 175.000 M$ anuales; si la monetización llega tarde, el FCF se resiente.
- **Concentración en OpenAI:** cliente y socio a la vez; riesgo de conflicto y de competencia.
- **Valoración:** 26x forward deja poco margen si el crecimiento se normaliza.
- **Regulación:** antitrust en EE.UU. y Europa.
- **Divisa:** el inversor en euros asume riesgo dólar.

**9. Señal de salida / invalidación.**
- Azure <30% de crecimiento en moneda constante durante dos trimestres.
- Capex al alza sin crecimiento de ingresos ni mejora de margen.
- FCF negativo o recorte del programa de recompras.
- Morningstar baja el valor razonable por debajo de 500 $ o retira el foso amplio.

**10. Nivel de convicción.** **Alta.** Es la mejor combinación de calidad, visibilidad y descuento de la
lista, con el permiso explícito de que no es barata.

---

### 3.3 ASML (ASML.AS) — medio plazo

**1. Nombre y ticker.** ASML Holding N.V., ASML.AS (NL0010273215).
**2. Tipo.** Acción (equipos de litografía).
**3. Horizonte.** Medio plazo (1-5 años), con ciclo.

**4. Tesis en tres frases.**
ASML es el único fabricante de litografía EUV del mundo y sus máquinas son un cuello de botella físico para
la IA; el libro de pedidos está cubierto hasta 2028. La guía 2026 se elevó a 44.000-45.000 M€ (+36% anual)
y la compañía tiene caja neta positiva. El problema es el precio: cotiza a 40x trailing y 24,5x forward,
con el consenso de ventas muy por encima de Morningstar; la tesis solo funciona si el ciclo de capex de IA
se prolonga más de lo que el mercado descuenta.

**5. Métricas clave actuales.**

| Métrica | Valor | Contexto |
|---|---:|---|
| Capitalización | 544.500 M€ | Large cap europea |
| PER trailing | 40,4x | Prima de monopolio |
| PER forward | 24,55x | Descuento vs crecimiento |
| EV/EBITDA | 31,9x | Alto |
| ROE (ttm) | 65,6% | Excepcional |
| Deuda/Patrimonio | 8,9% | Caja neta |
| Crecimiento ingresos (yoy) | 55,2% | Fuerte |
| Dividendo | 0,5% | Bajo |
| Beta 5 años | 1,33 | Más volátil que el mercado |
| Precio | ~1.412,8 € | 30/10/2026 |
| Guía 2026 | 44.000-45.000 M€ | [Hecho] elevada desde 43.000-45.000 |
| Pedidos | Cubiertos hasta 2028 | [Hecho] según la compañía |

**6. Por qué tiene sentido comprar hoy.**
- **[Hecho]** La compañía elevó la guía 2026 y declaró que las máquinas EUV están vendidas hasta 2028;
  los clientes empiezan a pedir para 2029-2030.
- **[Consenso]** BofA (Didier Scemama) mantiene Buy con objetivo 2.557 € (06/10/2026); Bernstein (Stacy
  Rasgon) Buy con 2.500 € (16/10/2026); consenso Moderate Buy con objetivo medio 2.079 $ (ADR).
- **[Opinión]** El descuento forward (24,5x para un crecimiento del 36%) es razonable si el ciclo se
  alarga. Pero la acción sube un 51% en 12 meses y Morningstar la ve «fairly valued»: el margen de
  seguridad es fino. Es una compra de calidad, no de valor.

**7. Respaldo experto (dos fuentes).**
1. **Morningstar**, «ASML: What We Think of the Stock After Earnings», octubre 2026 (mantiene valor
   razonable; la demanda fuerte desplaza la atención a 2029-2030).
   https://global.morningstar.com/en-gb/stocks/asml-what-we-think-stock-after-earnings
   Y «ASML Stock Is Up 55% in 2026. Can the Rally Continue?» (sube previsiones a largo plazo).
   https://global.morningstar.com/en-gb/stocks/asml-stock-is-up-55-2026-can-rally-continue
2. **BofA Securities** (Didier Scemama), Buy, objetivo 2.557 €, 06/10/2026.
   https://price-target.com/2026/10/06/174464/
   **Bernstein** (Stacy Rasgon), Buy, objetivo 2.500 €, 16/10/2026.
   https://markets.businessinsider.com/news/stocks/new-buy-rating-for-asml-holding-asml-the-technology-giant-1036638873
3. **Contrapunto y dato contradictorio:** Morningstar, en otra ficha, dice que ASML cotiza «within a
   range we consider fairly valued» a 1.565,90 $; otro artículo de Morningstar la ve «17% below fair
   value». La diferencia depende de la fecha y del precio; el consenso de ventas es mucho más agresivo
   que Morningstar. Se documenta el desacuerdo, no se oculta.

**8. Riesgos principales.**
- **Ciclicidad:** si TSMC/Samsung/Intel recortan capex, los pedidos caen con rapidez.
- **Concentración de clientes:** tres clientes explican la mayor parte de las ventas.
- **China:** controles de exportación y competencia local incipiente.
- **Valoración y expectativas:** 40x trailing; un fallo de guía castiga el múltiplo.
- **Divisa:** ASML.AS cotiza en euros, pero parte de sus ingresos son en dólares; riesgo FX indirecto.

**9. Señal de salida / invalidación.**
- Cancelaciones de pedidos o guía 2027 por debajo de 50.000 M€.
- Margen bruto <50% o presión de precios por competencia china.
- Restricciones de exportación que afecten a EUV/DUV de forma material.
- Morningstar recorta el valor razonable por debajo de 1.200 €.

**10. Nivel de convicción.** **Media-alta.** Monopolio y visibilidad excelentes; precio y ciclo impiden
la convicción alta.

---

### 3.4 LVMH (MC.PA) — largo plazo

**1. Nombre y ticker.** LVMH Moët Hennessy Louis Vuitton, MC.PA (FR0000121014).
**2. Tipo.** Acción (lujo).
**3. Horizonte.** Largo plazo (>5 años), con entrada contraria.

**4. Tesis en tres frases.**
LVMH es la cartera de marcas de lujo más valiosa del mundo, con un foso basado en marcas centenarias,
escasez y poder de fijación de precios. La acción ha caído un 35% en 12 meses por la debilidad de la
demanda china y la moda, hasta 385,20 €, un 35% por debajo del valor razonable de Morningstar (590 €).
Es una compra contraria de calidad: el ciclo chino pesa hoy, pero la franquicia y el balance aguantan.

**5. Métricas clave actuales.**

| Métrica | Valor | Contexto |
|---|---:|---|
| Capitalización | 190.800 M€ | Mayor grupo de lujo |
| PER trailing | 17,8x | Por debajo de su media histórica (~25x) |
| PER forward | 16,48x | Descuento |
| EV/EBITDA | 8,98x | Razonable para lujo |
| ROE (ttm) | 16,6% | Sólido |
| Deuda/Patrimonio | 53,3% | Manejable; FCF positivo |
| Crecimiento ingresos (yoy) | −2,9% | Debilidad cíclica |
| Dividendo | 3,4% | Creciente históricamente |
| Beta 5 años | 0,90 | Menos volátil que el mercado |
| Valor razonable Morningstar | 590 € | 5 estrellas, foso amplio |
| Precio | 385,20 € | 30/10/2026; descuento ~35% |

**6. Por qué tiene sentido comprar hoy.**
- **[Hecho]** Q3 2026: ingresos orgánicos +1%, pero moda y piel −5% orgánico; China cae en la mitad de la
  década porcentual. Dior va positivo en el año y plano en el trimestre, señal de que las nuevas colecciones
  funcionan.
- **[Hecho]** Morningstar mantiene 5 estrellas, foso amplio y valor razonable de 590 € pese a recortar
  previsiones; el precio está muy por debajo.
- **[Consenso]** Bernstein (Callum Elliott) reitera Buy el 19/10/2026; JPMorgan (Chiara Battistini) recorta
  el objetivo a 500 € pero mantiene la tesis; el consenso medio está en 594,7 €. Hay división: Berenberg
  Neutral y AlphaValue ven una recuperación «más gradual».
- **[Opinión]** El mercado está poniendo precio a un escenario de debilidad china prolongada. Si China
  estabiliza y la moda vuelve a crecer, el múltiplo tiene margen para volver a 20-22x. Es una apuesta de
  paciencia, no de trimestre.

**7. Respaldo experto (dos fuentes).**
1. **Morningstar**, «LVMH Stock: Lowering Fair Value Estimate as Chinese Demand Weakens», octubre 2026
   (valor razonable 590 €, 5 estrellas, foso amplio, incertidumbre media).
   https://global.morningstar.com/en-nd/stocks/lvmh-stock-lowering-fair-value-estimate-chinese-demand-weakens
2. **Bernstein** (Callum Elliott), Buy, 19/10/2026, recogido por MarketScreener.
   https://www.marketscreener.com/news/lvmh-receives-a-buy-rating-from-bernstein-ce785cdbda8bf422
   **JPMorgan** (Chiara Battistini), objetivo 500 €, 13/10/2026, recogido por Markets Insider.
   https://markets.businessinsider.com/news/stocks/lvmh-price-target-lowered-to-eur-500-from-eur-525-at-jpmorgan-1036623018
3. **Contrapunto:** Berenberg Neutral y la propia Morningstar reconocen que la recuperación relativa
   «sigue siendo esquiva»; el riesgo chino no está resuelto.

**8. Riesgos principales.**
- **Demanda china:** principal motor de crecimiento; una debilidad prolongada retrasa la recuperación.
- **Ejecución de moda y piel:** la división más rentable sigue cayendo; el turnaround de Dior/LV es clave.
- **Divisa y aranceles:** exposición global; tensiones comerciales.
- **Valoración:** aunque ha caído, 16,5x forward no es «barato» si el crecimiento sigue negativo.
- **Riesgo de marca:** la escasez y el pricing power pueden erosionarse si la demanda se debilita mucho.

**9. Señal de salida / invalidación.**
- Crecimiento orgánico negativo durante dos trimestres consecutivos y moda/piel cayendo >10%.
- Morningstar baja el valor razonable por debajo de 450 € o retira el foso amplio.
- Recorte del dividendo o deterioro del balance (deuda/EBITDA >2,5x).
- Recuperación china que no llega en 2027.

**10. Nivel de convicción.** **Media-alta.** La calidad y el descuento son atractivos; la incertidumbre
china impide la alta.

---

### 3.5 VanEck Global Real Estate UCITS ETF (TRET.DE) — largo plazo

**1. Nombre y ticker.** VanEck Global Real Estate UCITS ETF, TRET.DE (NL0009690239).
**2. Tipo.** ETF indexado de renta variable inmobiliaria global (REITs).
**3. Horizonte.** Largo plazo (>5 años), con papel de activo real.

**4. Tesis en tres frases.**
TRET replica el índice GPR Global Property con ~100 valores, 85% REITs, y un TER de 0,25%. Aporta lo que
la cartera no tiene: rentas de alquiler, diversificación frente a la bolsa y cierta protección ante la
inflación vía rentas indexadas. El sector viene de una década mala y de un 2022-2023 muy duro; la
valoración ha dejado de ser exigente y los balances empiezan a refinanciarse mejor.

**5. Métricas clave actuales.**

| Métrica | Valor | Contexto |
|---|---:|---|
| TER | 0,25% | Barato para un ETF sectorial |
| Patrimonio | 458,7 M€ | Suficiente liquidez |
| Historial | Lanzado en 2011 | Más de 10 años, cumple el filtro de trayectoria |
| Nº de posiciones | ~100 | 85% REITs, 15% no REITs |
| Rentabilidad YTD 2026 | +11,09% | [Hecho] según VanEck a 30/10/2026 |
| Rentabilidad 1 año | +10,8% EUR | Recuperación |
| Rentabilidad 3 años | +13,1% anual | Fuerte desde el suelo de 2023 |
| Composición | Global, USA ~65% | Diversificación geográfica limitada por el peso USA |
| Dividendo | Distribuye rentas | No es acumulación; verificar clase |
| Divisa | EUR (cotización) | Subyacente global con riesgo FX |

**6. Por qué tiene sentido comprar hoy.**
- **[Hecho]** El ETF cuesta 0,25% y tiene 458,7 M€; es la vía barata para el hueco de activos reales.
- **[Hecho]** El sector lleva dos años recuperándose: +11,09% YTD y +13,1% anual a 3 años, después de la
  corrección de 2022-2023. No se compra en máximos históricos.
- **[Consenso]** Cohen & Steers («Listed REITs: A strong start to 2026») y SSGA («REIT resilience extends
  beyond interest rates», 31/08/2026) ven fundamentos inmobiliarios sólidos y balances sanos. Barings
  espera rentas al alza en espacio de calidad con oferta limitada.
- **[Contrapunto]** S&P Global («European REIT 2026 Mid-Year Outlook: Higher Rates») avisa de que los
  ratios de cobertura de intereses seguirán presionados en 2026-2027 para la mitad de los REITs europeos.
  El consenso no es unánime: es un activo sensible a tipos.
- **[Opinión]** Con inflación en el 3,0% y tipos altos, los REITs no son un refugio perfecto, pero sí una
  fuente de rentas reales y diversificación. Peso pequeño (1,5%) y horizonte largo.

**7. Respaldo experto (dos fuentes).**
1. **VanEck**, ficha oficial del ETF a 30/10/2026: TER 0,25%, 458,7 M€, ~100 valores, YTD +11,09%.
   https://www.vaneck.com/uk/en/investments/real-estate-etf/
2. **Cohen & Steers**, «Listed REITs: A strong start to 2026 and what's driving performance», 2026.
   https://www.cohenandsteers.com/insights/listed-reits-a-strong-start-to-2026-and-whats-driving-performance/
   **SSGA**, «REIT resilience extends beyond interest rates», 31/08/2026.
   https://www.ssga.com/us/en/institutional/insights/mind-on-the-market-31-august-2026_msm_moved
3. **Contrapunto:** S&P Global, «European REIT 2026 Mid-Year Outlook: Higher Rates», 2026.
   https://www.spglobal.com/ratings/en/regulatory/article/european-reit-2026-mid-year-outlook-higher-rates-delaying-not-derailing-the-recovery-s101695544

**8. Riesgos principales.**
- **Tipos de interés:** un repunte del bono a 10 años presiona las valoraciones y la refinanciación.
- **Refinanciación:** parte de los REITs europeos tiene vencimientos 2026-2027 con coberturas justas.
- **Ocupación y rentas:** si el ciclo económico se deteriora, la ocupación y la renta caen.
- **Concentración geográfica:** ~65% USA; el riesgo dólar y el ciclo americano pesan.
- **Divisa:** cotiza en euros, pero los activos y dividendos son globales.

**9. Señal de salida / invalidación.**
- Bono alemán a 10 años >4,5-5% de forma sostenida.
- Recortes de dividendo o guías a la baja en varios REITs del índice.
- Ocupación media <90% o morosidad al alza.
- Cambio de metodología del índice o caída del patrimonio por debajo de 200 M€.

**10. Nivel de convicción.** **Media.** Es el hueco correcto, pero el activo es sensible a tipos y la
convicción no es alta.

---

### 3.6 Munich Re (MUV2.DE) — corto/medio plazo (alternativa de calidad)

**1. Nombre y ticker.** Münchener Rückversicherungs-Gesellschaft, MUV2.DE (DE0008430026).
**2. Tipo.** Acción (reaseguro).
**3. Horizonte.** Corto/medio (0-3 años), defensivo.

**4. Tesis en tres frases.**
Munich Re es el mayor reasegurador del mundo, con un modelo de capital ligero y disciplina de suscripción.
Cotiza a 10,6x con un 4,3% de dividendo y una beta de 0,27, lo que la convierte en un activo defensivo
dentro de la cartera. El Q3 2026 batió expectativas (1.700 M€ de beneficio) y elevó la guía anual a
6.600 M€, pero el ciclo de reaseguro se está suavizando y el consenso ya no ve mucho recorrido.

**5. Métricas clave actuales.**

| Métrica | Valor | Contexto |
|---|---:|---|
| Capitalización | 71.300 M€ | Gran reaseguradora |
| PER trailing | 10,6x | Barata vs mercado |
| PER forward | 11,51x | Sin descuento claro |
| EV/EBITDA | 7,37x | Razonable |
| ROE (ttm) | 21,3% | Muy bueno |
| Deuda/Patrimonio | 24,4% | Sólido |
| Dividendo | 4,3% | Atractivo |
| Beta 5 años | 0,27 | Muy defensiva |
| Rentabilidad 1 año | +8,6% EUR | Sin euforia |
| Rentabilidad 3 años | +18,8% anual | Consistente |
| Guía 2026 | 6.600 M€ | [Hecho] elevada el 23/10/2026 |

**6. Por qué tiene sentido comprar hoy.**
- **[Hecho]** Q3 2026: beneficio neto preliminar de 1.700 M€ y guía anual elevada a 6.600 M€.
- **[Hecho]** Barclays subió el objetivo a 594 € (Buy) el 26/10/2026; el consenso medio está en 560,9 €.
- **[Opinión]** La acción cotiza a 567,6 €, por encima del consenso medio pero por debajo de Barclays. El
  margen de seguridad es fino; la tesis es de calidad y dividendo, no de gran descuento. Mejor como
  alternativa defensiva que como compra prioritaria.
- **[Contrapunto]** Jefferies reitera Neutral y KBW mantiene una visión negativa; el ciclo de precios del
  reaseguro se suaviza. El propio Morningstar titula «Soft Cycle Continues».

**7. Respaldo experto (dos fuentes).**
1. **Morningstar**, «Munich Re Earnings: Soft Cycle Continues With Light Large Losses and a Convincing
   Beat», 23/10/2026. https://www.morningstar.com/company-reports/1494139-munich-re-earnings-soft-cycle-continues-with-light-large-losses-and-a-convincing-beat
2. **Barclays**, Buy, objetivo 594 €, 26/10/2026, recogido por Ad-hoc-News.
   https://www.ad-hoc-news.de/boerse/news/corporate-news/barclays-lifts-target-for-munich-re-stock-to-eur-594-00/70415230
3. **Contrapunto:** Jefferies Neutral y KBW negativo, recogidos por MarketScreener el 26/10/2026.
   https://www.marketscreener.com/news/munich-re-jefferies-reaffirms-its-neutral-rating-ce785cdfdb8ef42c

**8. Riesgos principales.**
- **Ciclo de reaseguro:** precios a la baja y mayor competencia.
- **Catástrofes:** un año con grandes siniestros puede borrar el beneficio.
- **Tipos de interés:** menores rendimientos de la cartera de inversión.
- **Valoración:** cotiza por encima del consenso medio; poca margen de seguridad.

**9. Señal de salida / invalidación.**
- Combined ratio >100% o guía anual recortada.
- Guerra de precios en renovaciones de enero.
- Pérdidas por catástrofe superiores al presupuesto.
- El consenso baja el objetivo por debajo de 520 €.

**10. Nivel de convicción.** **Media.** Calidad y dividendo, pero no es una ganga hoy.

---

### 3.7 iShares Edge MSCI World Quality Factor (IS3Q.DE) — largo plazo (alternativa de calidad)

**1. Nombre y ticker.** iShares Edge MSCI World Quality Factor UCITS ETF, IS3Q.DE (IE00BP3QZ601).
**2. Tipo.** ETF indexado de factor calidad.
**3. Horizonte.** Largo plazo (>5 años).

**4. Tesis en tres frases.**
IS3Q replica el índice MSCI World Sector Neutral Quality, que selecciona compañías con alto ROE, beneficios
estables y bajo apalancamiento. Con 290 posiciones, 6.000 M€ y un TER de 0,25%, es la forma barata de
comprar el factor calidad sin pagar el 1,09% de un gestor activo. Históricamente el factor calidad ha
batido a su índice padre en ~50 pb anuales en EE.UU. y ~165 pb en el mundo ex-USA desde 1998.

**5. Métricas clave actuales.**

| Métrica | Valor | Contexto |
|---|---:|---|
| TER | 0,25% | 4 veces más barato que Fundsmith |
| Patrimonio | 6.000 M€ | Muy líquido |
| Nº de posiciones | 290 | Diversificado |
| Rentabilidad 1 año | +18,7% EUR | Fuerte |
| Rentabilidad 3 años | +18,4% anual | Por encima del MSCI World |
| Rentabilidad 5 años | +62,9% acumulada (~10,3% anual) | Competitivo |
| 2022 | −14,8% | Mejor que el S&P (−18%) |
| 2023 | +21,7% | Peor que el S&P (+26%) |
| Composición | ~70% USA | Alta concentración americana |
| Divisa | EUR (cotización) | Subyacente USD |

**6. Por qué tiene sentido comprar hoy.**
- **[Hecho]** El ETF cuesta 0,25% y tiene 6.000 M€ y 290 posiciones; es la puerta barata al factor calidad.
- **[Consenso]** MSCI Research («Repositioning for Slower Growth: The Case for Quality», 16/12/2025)
  documenta la prima de calidad: ~50 pb anuales en EE.UU. y ~165 pb en el mundo ex-USA desde 1998. En
  entornos de crecimiento más lento, las empresas de calidad defensiva suelen batir.
- **[Opinión]** Es una alternativa racional a Fundsmith/Comgest: mismo estilo, sin riesgo de persona clave
  y a una cuarta parte del coste. La pega es la concentración USA y la posibilidad de varios años de
  underperformance del factor.
- **[Contrapunto]** Morningstar evalúa el proceso (Medalist Rating a 31/08/2026), pero el factor calidad no
  es una garantía: puede quedarse rezagado varios años, como en 2023.

**7. Respaldo experto (dos fuentes).**
1. **Morningstar**, ficha de análisis del ETF IWQU/IS3Q, Medalist Rating a 31/08/2026, con evaluación del
   pilar Process. https://www.morningstar.com/etfs/xfra/is3-q/quote
2. **MSCI Research**, «Repositioning for Slower Growth: The Case for Quality», 16/12/2025.
   https://www.msci.com/research-and-insights/blog-post/repositioning-for-slower-growth-the-case-for-quality
3. **Contrapunto:** el propio MSCI reconoce que el factor puede tener largos periodos de underperformance;
   la concentración USA (~70%) añade riesgo país.

**8. Riesgos principales.**
- **Riesgo de factor:** la calidad puede quedar rezagada varios años (2023: +21,7% vs S&P +26%).
- **Concentración USA y tecnología:** ~70% USA; correlación alta con el S&P en caídas.
- **Valoración:** las compañías de calidad cotizan caras; si los tipos suben, el múltiplo se comprime.
- **Crowding:** mucho dinero en el factor calidad puede reducir la prima futura.
- **Divisa:** subyacente en USD; riesgo dólar para el inversor en euros.

**9. Señal de salida / invalidación.**
- Prima de calidad negativa acumulada a 5 años frente al MSCI World.
- Cambio de metodología del índice o subida del TER.
- Caída del patrimonio por debajo de 2.000 M€.
- Concentración de una sola posición >10%.

**10. Nivel de convicción.** **Alta como idea, media como compra hoy.** El producto es excelente, pero
con 1.000 € sería una posición fragmentada; por eso queda fuera de la cartera modelo y se propone para
una aportación nueva o para sustituir parte de Fundsmith si se adopta la cartera alternativa.

## 4. Cartera modelo propuesta (97.000 €)

**Objetivo:** mantener el 50/50 y la renta fija intacta; añadir una satélite de 9.000 € (9,3%) financiada
solo con recortes de renta variable. El núcleo sigue siendo el de `propuesta-actual.md`, con ajustes
mínimos para no duplicar y para reducir la fragmentación.

| Bloque | Fondo/Activo | ISIN/Ticker | € | Peso | TER |
|---|---|---|---:|---:|---:|
| RF corta IG | Neuberger Short Duration Euro Bond U | IE00BL1GVT98 | 31.900 | 32,9% | 0,38% |
| RF flexible | DNCA Alpha Bonds A | LU1694789451 | 5.000 | 5,2% | 1,31% + éxito |
| Crédito | Carmignac Credit A | LU1623762843 | 5.000 | 5,2% | 1,20% + éxito |
| RV value Europa small/mid | MyInvestor Value C | ES0165243025 | 4.000 | 4,1% | ~1,42% + 9% éxito |
| RV value global | Cobas International P | LU1598719752 | 3.500 | 3,6% | 2,33% |
| RV small cap global | Vanguard Global Small-Cap Index EUR Acc | IE00B42W4L06 | 1.200 | 1,2% | 0,29% |
| RV Europa large cap | Fidelity MSCI Europe Index EUR P Acc | IE00BYX5MD61 | 2.000 | 2,1% | 0,10% |
| RV emergentes | iShares Emerging Markets Index S Acc EUR | IE000QAZP7L2 | 5.400 | 5,6% | 0,16% |
| **Satélite — corto** | **TotalEnergies** | **TTE.PA** | **2.000** | **2,1%** | — |
| **Satélite — medio** | **Microsoft** | **MSFT** | **2.500** | **2,6%** | — |
| **Satélite — medio** | **ASML** | **ASML.AS** | **1.500** | **1,5%** | — |
| **Satélite — largo** | **LVMH** | **MC.PA** | **1.500** | **1,5%** | — |
| **Satélite — largo** | **VanEck Global Real Estate** | **TRET.DE** | **1.500** | **1,5%** | **0,25%** |
| Cartera indexada 78/22 | Rock (sin cambios) | — | 30.000 | 30,9% | 0,41% |
| | **TOTAL** | | **97.000** | **100%** | |

**Verificación de la 50/50.** RV = Rock 23.400 (78% de 30.000) + fondos manuales 16.100 + satélite 9.000
= 48.500 € = 50,0%. RF = Neuberger 31.900 + DNCA 5.000 + Carmignac 5.000 + Rock 6.600 = 48.500 € = 50,0%.
La satélite se financia con recortes de RV, así que la renta fija no se toca.

### 4.1 Cómo se financia: siete órdenes, 9.000 €

**Aviso fiscal:** un traspaso solo existe entre fondos armonizados. Para comprar **acciones** hay que
reembolsar el fondo (tributa por la plusvalía latente) y comprar el valor; para comprar **TRET** (ETF)
también se reembolsa y se compra en el bróker. Por tanto, las salidas de fondos no son un traspaso limpio
si el destino es una acción o un ETF. Si se quiere evitar el peaje fiscal, la satélite se construye con
**aportación nueva** y los fondos se dejan intactos.

| # | Origen | ISIN origen | € | Destino | ISIN destino |
|--:|---|---|---:|---|---|
| 1 | Vanguard Global Small-Cap Index EUR Acc | IE00B42W4L06 | 2.500 | Microsoft | US5949181045 |
| 2 | Fidelity MSCI Europe Index P Acc EUR | IE00BYX5MD61 | 2.000 | TotalEnergies | FR0000120271 |
| 3 | Fidelity MSCI Europe Index P Acc EUR | IE00BYX5MD61 | 1.000 | LVMH | FR0000121014 |
| 4 | MyInvestor Value C | ES0165243025 | 500 | LVMH | FR0000121014 |
| 5 | MyInvestor Value C | ES0165243025 | 500 | VanEck Global Real Estate | NL0009690239 |
| 6 | Cobas International P | LU1598719752 | 1.500 | ASML | NL0010273215 |
| 7 | iShares Emerging Markets Index S Acc EUR | IE000QAZP7L2 | 1.000 | VanEck Global Real Estate | NL0009690239 |
| | **Total** | | **9.000** | | |

Salen 2.500 € del small cap (la tercera apuesta al mismo factor), 3.000 € de Europa large cap (se queda
en 2.000 €), 1.000 € de MyInvestor Value (se queda en 4.000 €), 1.500 € de Cobas (se queda en 3.500 €) y
1.000 € de emergentes (se queda en 5.400 €). No se toca la renta fija ni Rock. **Si la plusvalía latente
es alta, la factura fiscal puede comerse el beneficio de la rotación:** calcularla antes de ejecutar y,
si supera el 5% del importe movido, usar aportación nueva o esperar.

### 4.2 Métricas antes/después

| Métrica | Cartera vigente | **Cartera propuesta** | Diferencia |
|---|---:|---:|---:|
| Renta variable | 50,0% | **50,0%** | 0 |
| Activos reales (REITs) | 0% | **1,5%** | +1,5 pp |
| Acciones directas | 0% | **7,7%** (7.500 €) | +7,7 pp |
| Factor calidad (directo) | 0% | **5,7%** (MSFT + LVMH + ASML) | +5,7 pp |
| Nº de posiciones | 17 | **22** (17 + 5) | +5 |
| TER ponderado estimado | 0,655% | **~0,60%** | −0,05 pp |
| Exposición USA de la RV | 32,5% | **~39-40%** | +6,5-7,5 pp |
| Caída estimada 2008 | ≈ −21,5% | **≈ −21,5%** | igual |

**El coste real de la propuesta:**
- **Más USA:** MSFT, IS3Q (si se añade) y TRET son intensivos en EE.UU. La exposición USA de la RV sube
  del 32,5% al ~39-40%, en contra de la tesis de la cartera vigente («el S&P 500 no es neutral»). Se
  compensa en parte porque las acciones europeas (TTE, ASML, LVMH) y TRET no son USA, pero el movimiento
  es real y hay que decirlo.
- **Más complejidad:** de 17 a 22 posiciones; dos de ellas (ASML 1.500 € y LVMH 1.500 €) están en el
  umbral de fragmentación. Si se quiere simplificar, se puede empezar solo con MSFT + TTE + TRET (6.000 €).
- **Riesgo de ejecución fiscal:** los traspasos de fondos son limpios; la compra de acciones desde un
  reembolso de fondo tributa. Verificar plusvalías antes de mover.
- **No diversifica la caída:** las acciones y los REITs son renta variable; en un 2008 la cartera caería
  igual que la vigente. Lo que se compra es diversificación de fuentes de retorno (energía, software,
  semiconductores, lujo, alquileres), no protección.

### 4.3 Si se prefiere una versión mínima

Si no se quiere tocar el value ni el small cap, la versión mínima es **3.000 €**: MSFT 1.500 € + TTE
1.000 € + TRET 500 €, financiados con Fidelity Europe (2.000 €) y emergentes (1.000 €). Deja 19 posiciones,
USA en ~35% de la RV y cubre los tres huecos (acción directa, energía, activo real) con un coste de
ejecución bajo. Es la versión que elegiría si solo se aprueba un cambio.

## 5. Tabla comparativa de todas las opciones

| Activo | Tipo | Horizonte | Valoración | Crecimiento | Solvencia | Rentabilidad | Dividendo | Beta/Vol | Convicción |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| **TTE.PA** | Acción | Corto | PER 10,0x / fwd 8,3x | Ingresos +41,1% yoy | Deuda/Pat. 46,1%; FCF + | ROE 17,8% | 4,2% | Beta 0,04 | Media-alta |
| **MSFT** | Acción | Medio | PER 27,2x / fwd 26,3x; 13% bajo FV | Ingresos +18,8% yoy | Deuda/Pat. 28,5% | ROE 34,2% | 0,8% | Beta 1,04 | Alta |
| **ASML.AS** | Acción | Medio | PER 40,4x / fwd 24,6x | Ingresos +55,2% yoy | Deuda/Pat. 8,9%; caja neta | ROE 65,6% | 0,5% | Beta 1,33 | Media-alta |
| **MC.PA** | Acción | Largo | PER 17,8x / fwd 16,5x; 35% bajo FV | Ingresos −2,9% yoy | Deuda/Pat. 53,3% | ROE 16,6% | 3,4% | Beta 0,90 | Media-alta |
| **TRET.DE** | ETF | Largo | TER 0,25%; 3A +13,1% | Rentas indexadas | 85% REITs; balances diversos | — | Distribuye | Vol sectorial | Media |
| **MUV2.DE** | Acción | Corto/medio | PER 10,6x; consenso 560,9 € | Ingresos +1,3% yoy | Deuda/Pat. 24,4% | ROE 21,3% | 4,3% | Beta 0,27 | Media |
| **IS3Q.DE** | ETF | Largo | TER 0,25%; 3A +18,4% | Calidad (ROE alto) | Bajo apalancamiento | — | — | ~70% USA | Alta idea / media compra |

**Lectura de la tabla.** La mejor relación calidad/precio está en TTE (8,3x con 4,2% de dividendo), MSFT
(13% de descuento con crecimiento del 18,8%) y LVMH (35% de descuento con foso amplio). ASML es la mejor
empresa de la lista, pero no la más barata; MUV2 es la más defensiva, pero ya cotiza en línea con el
consenso. TRET e IS3Q son diversificadores baratos, no generadores de alfa a corto.

## 6. Descartados y por qué

| Descartado | Motivo, con el número delante |
|---|---|
| **Iberdrola (IBE.MC)** | Morningstar la ve «excessively priced in»: PER 29,9x trailing, EV/EBITDA 14,5x, deuda/patrimonio 101,9%. Buena empresa, mal precio. https://morningstar.com/stocks/xmad/ibe/analysis |
| **Bonos ligados a inflación euro (Vanguard IE00B04GQR24)** | TER 0,12% y 33 posiciones, pero Morningstar («Inflation-Linked Bonds' Rally Has Stumbled») avisa de que la subida de tipos resta atractivo; el carry real es 0,3-0,5% y la duración es larga. Es seguro, no rentabilidad. Se puede añadir 1.000 € como cobertura pura, pero no lo pongo en la cartera modelo. https://global.morningstar.com/en-eu/bonds/inflation-linked-bonds-rally-has-stumbled-whats-next |
| **Oro físico (CSGOLD.SW / GBS.MI)** | TER 0,19-0,22%, pero el oro ha caído un 27% desde su máximo de 5.589 $ y sigue sin generar caja. El World Gold Council ve compras de bancos centrales, pero la volatilidad es alta y el precio no está barato. Mejor no incluirlo ahora; si se quiere cobertura, 1-2% máximo. https://www.gold.org/goldhub/research/central-bank-gold-reserves-survey-2026 |
| **Munich Re en la cartera modelo** | La tesis es buena (Q3 beat, guía 6.600 M€, 4,3% dividendo), pero cotiza a 567,6 €, por encima del consenso medio (560,9 €) y con Jefferies Neutral/KBW negativo. Se queda como alternativa defensiva, no como compra prioritaria. |
| **IS3Q en la cartera modelo** | El producto es excelente (TER 0,25%, 290 posiciones), pero con 1.000 € sería una posición fragmentada y la cartera ya tiene calidad vía MSFT/LVMH. Se propone para una aportación nueva o para sustituir Fundsmith si se adopta la cartera alternativa. |
| **Fundsmith / Comgest** | Ya se documentaron en `propuesta-alternativa.md`: 1,09% y 1,59% de TER, riesgo de persona clave y cinco años por debajo del índice. La calidad se compra más barata con IS3Q (0,25%) o directamente con MSFT/LVMH. |
| **Infraestructura cotizada (Lazard / DWS)** | Lazard exige mínimo de 10.000 €; DWS cuesta 1,59% y tiene 53% USA. No compensa frente a TRET (0,25%) para el hueco de activos reales. |
| **Small caps pasivas adicionales** | Ya hay dos value small/mid y una pasiva; añadir más sería la cuarta apuesta al mismo factor. La satélite prioriza calidad y activos reales, no tamaño. |
| **Comprar S&P 500 o MSCI World ahora** | El S&P 500 cotiza a 18,7x con 46% de tecnología; el MSCI World concentra ~70% USA. La cartera ya tiene beta USA vía Rock. Añadir más sería duplicar el riesgo que la propuesta vigente evita. |

## 7. Qué se necesita para ejecutar y qué queda abierto

- **Verificar la disponibilidad real de las acciones en el bróker:** MSFT, ASML.AS, MC.PA y TTE.PA son
  valores europeos/americanos líquidos; MUV2.DE aparece si se busca por ticker, pero no por el nombre
  «Munich Re»; comprobar que sea contratable y en qué mercado antes de incluirlo.
- **Comisión de compra de acciones:** el bróker puede cobrar custodia o corretaje; el TER de un ETF no
  aplica a una acción. Calcular el coste total (comisión + custodia + cambio de divisa).
- **Fiscalidad de los traspasos:** los fondos armonizados se traspasan sin tributar; las acciones no.
  Si se compran acciones con el producto de un reembolso, la plusvalía del fondo tributa. Alternativa:
  construir la satélite con aportación nueva y dejar los fondos intactos.
- **Datos contradictorios que se conservan:** ASML (Morningstar «fairly valued» vs ventas 60-80% por
  encima); MUV2 (consenso 560,9 € vs Barclays 594 € vs Jefferies Neutral); LVMH (Morningstar 590 € vs
  JPMorgan 500 € vs consenso 594,7 €); TTE (consenso Buy vs JPMorgan Neutral y +65,5% en 12 meses).
  No se ocultan: se explican y se baja la convicción cuando el desacuerdo es grande.
- **Riesgo de divisa:** MSFT, IS3Q y parte de TRET están en dólares. Un inversor en euros asume que el
  dólar se mueva en su contra; no se cubre.
- **Riesgo de concentración:** la satélite añade tecnología (MSFT, ASML), lujo (LVMH), energía (TTE) e
  inmobiliario (TRET). Es diversificación por sectores, pero no por factor: casi todo es renta variable.
- **Revisión:** cada trimestre, con resultados y valoraciones. Si una tesis se invalida (Azure <30%,
  China negativa dos trimestres, Brent <65 $, ASML sin pedidos), se vende sin discutir el precio.

## 8. Advertencia

> **Esto es análisis informativo, no asesoramiento financiero personalizado.** No conozco tu situación
> fiscal, tu horizonte real, tu tolerancia a la caída ni tus necesidades de liquidez. Las valoraciones,
> precios objetivo y recomendaciones de analistas son opiniones que cambian; los datos de fondos y ETFs
> pueden quedar desactualizados. Antes de ejecutar, verifica comisiones, fiscalidad, disponibilidad de
> los valores y clase del fondo en tu plataforma. Si una caída del −21,5% te haría vender, no ejecutes
> esta cartera: baja el peso de renta variable y vuelve a calcular.

---
name: analisis-tecnico
description: Usar cuando el dueño pida velas (mensuales, semanales o diarias), EMAs, medias, Parabolic SAR, bandas de Bollinger o «cómo está el gráfico» de una empresa. Calcula los indicadores con un script propio y los interpreta sin inventar señales.
---

# Análisis técnico (velas + EMA3/9/20 + Parabolic SAR + Bollinger)

## Qué resuelve

«¿Cómo cotiza X en velas mensuales?», «dame EMA3, EMA9, EMA20 y las paramétricas SAR»,
«¿cuánta volatilidad y qué rango tiene?», «¿el gráfico acompaña o contradice la tesis?». La respuesta es
**una tabla con las velas y los indicadores**, más dos líneas de lectura. No es una recomendación de compra.

## Frontera: qué se calcula aquí y qué no

| Pregunta | Skill | Calcula |
|---|---|---|
| «¿Cómo está X?» · velas, EMAs, SAR, Bollinger, régimen | **esta** | solo indicadores del activo preguntado |
| «¿Está en punto de compra?» · entrada y niveles | `trading-action` (reparte a `trader-scalping`, `trader-day-trading`, `trader-swing`, `trader-position`) | marcador del activo preguntado |
| «¿Esta regla tiene ventaja?» · backtest, `n`, vigencia | `medir-metodo-compras` | **solo si el dueño lo pide** |

**Regla dura: esta skill no lanza backtests, ni mediciones, ni barridos.** Si hacen falta, se dice qué skill
los tiene y se espera a que el dueño lo pida. Un análisis técnico se entrega en una tabla, no en una simulación.

## Para decidir una compra

Este archivo calcula indicadores. **Para el protocolo de entrada** —gate de EMA200, marcador de 8, caja
semanal, vela de entrada con volumen, R/R mínimo y las prohibiciones— usar la skill `trading-action`.

## Script

`.agents/skills/analisis-tecnico/scripts/tecnicos.py` — solo stdlib, sin pandas ni TA-Lib.

```bash
python3 .agents/skills/analisis-tecnico/scripts/tecnicos.py AMZN              # mensual, 10 años
python3 .agents/skills/analisis-tecnico/scripts/tecnicos.py NVDA --interval 1wk --range 5y
python3 .agents/skills/analisis-tecnico/scripts/tecnicos.py NFLX --tail 12 --emas 3,9,20 --json
python3 .agents/skills/analisis-tecnico/scripts/tecnicos.py TSLA --bb 20,2    # Bollinger por defecto
python3 .agents/skills/analisis-tecnico/scripts/tecnicos.py TSLA --bb 20,2.5  # banda más ancha
```

- Datos: `query2.finance.yahoo.com/v8/finance/chart/<TICKER>` — **no necesita crumb ni cookies**,
  a diferencia de `quoteSummary`, que falla con «Invalid Crumb».
- Precios ajustados por **split**, no por dividendo.
- EMA sembrada con la SMA del periodo (convención estándar).
- Parabolic SAR de Wilder: paso 0,02 y máximo 0,20, con la restricción de no meterse en el rango de
  las dos velas anteriores.

## Cómo se lee (el orden importa)

1. **Alineación de EMAs.** `EMA3 > EMA9 > EMA20` con el precio por encima de las tres = tendencia
   alcista intacta. El orden inverso (`EMA20 > EMA9 > EMA3`) = tendencia bajista. Mezclado = rango o
   giro en curso: se dice «sin tendencia clara», no se fuerza una lectura.
2. **Precio contra EMA3.** Es la que manda en el corto plazo. Precio por debajo de EMA3 en mensual =
   el impulso se ha agotado, aunque la EMA20 siga subiendo.
3. **SAR.** Estar por debajo del SAR en mensual no significa «vende»: significa que el régimen de la
   vela está en bajista. La distancia al SAR mide cuánto falta para que se gire (se gira cuando el
   máximo de la vela supera el SAR). **En mensual el SAR llega tarde**: vale para describir régimen,
   no para poner un stop.
4. **Velas desde el giro.** Un giro de 0-1 velas en mensual es un aviso reciente; uno de 11 velas
   (NFLX, 05/11/2026) es una tendencia bajista consolidada, no una oportunidad por caída.
5. **Bandas de Bollinger: volatilidad y rango.** Dónde está el precio dentro de la banda (%B) y si el
   ancho está comprimido o expandido respecto a su propia historia. Detalle en la sección siguiente.
6. **La vela en curso está sin cerrar.** El último mes se mueve hasta el último día: se dice siempre
   («noviembre va por la mitad») y no se trata como cierre.

### Ejemplo real (05/11/2026, mensual)

| Ticker | Precio | EMA3 | EMA9 | EMA20 | SAR | Lectura |
|---|---:|---:|---:|---:|---:|---|
| AMZN | 259,17 | 253,26 | 249,00 | 235,38 | 286,04 (bajista, giro en octubre) | Tendencia alcista intacta, pero el SAR mensual avisó en octubre y no se ha vuelto a girar |
| NVDA | 183,11 | 197,59 | 199,51 | 181,71 | 243,37 (bajista, giro **este mes**) | Giro bajista recién hecho; EMA3 ya por debajo de EMA9 |
| NFLX | 64,82 | 66,46 | 75,91 | 83,02 | 96,69 (bajista, 11 velas) | Bajista de libro: EMA20 > EMA9 > EMA3 y precio por debajo de las tres |

## Bandas de Bollinger: volatilidad y rango de trading

**Qué son.** La media de 20 cierres (SMA20) y sus dos bandas a ±2 desviaciones típicas de esa misma
ventana: `banda = SMA20 ± 2σ`. El script las calcula con **desviación poblacional** (`pstdev`), que es la
convención de Bollinger y la que usan los gráficos; con desviación muestral las bandas salen algo más
anchas y no cuadra con lo que el dueño ve en pantalla. Configurable con `--bb 20,2` (o `20,2.5`).

**Las tres lecturas, en este orden:**

1. **Ancho de banda = volatilidad.** `ancho % = (banda superior − inferior) / SMA20 × 100`. Es
   adimensional: vale igual para una acción de 300 que para un cripto de 0,000005, y permite comparar el
   activo consigo mismo en el tiempo. **El ancho absoluto no dice nada; su percentil sí.** El script lo
   sitúa contra las últimas 200 velas:

   | Percentil del ancho | Régimen | Lectura |
   |---:|---|---|
   | ≤ 25 | **compresión** | rango estrecho: el mercado no paga el riesgo; los stops ajustados saltan con nada |
   | 25-75 | normal | volatilidad habitual del activo |
   | ≥ 75 | **expansión** | movimiento ya en marcha; entrar tarde paga caro y el stop queda lejos |

2. **%B = posición dentro del rango.** `%B = (cierre − banda inferior) / (banda superior − inferior) × 100`.
   0 es la banda inferior, 100 la superior, 50 la media. Dice **dónde** está el precio en su rango, no
   hacia dónde va. Por encima de 100 o por debajo de 0 el cierre está fuera de las bandas: extensión, no
   señal.

3. **Bandas como rango de trading.** La banda inferior es el suelo estadístico del rango (±2σ) y la
   superior el techo. En un mercado **lateral**, comprar el borde inferior y vender el superior es lo que
   el dueño quiere ver; en **tendencia**, el precio se pega a una banda y las bandas dejan de ser suelo y
   techo: se ensanchan y siguen al precio. Distinguirlo es el paso 1 (ancho) y la alineación de EMAs:
   - EMAs mezcladas + ancho en compresión/normal → rango probable: los bordes sirven.
   - EMA3 > EMA9 > EMA20 con expansión → tendencia: la banda superior no es techo, es donde el precio
     «respira»; vender ahí contra la tendencia es de los errores más caros.

**Lo que las bandas no son.** No son una señal de compra por tocar la banda inferior (en caída libre el
precio camina por debajo durante semanas: NVDA semanal, %B −1 y banda inferior perdiendo). No son un
objetivo de precio: ±2σ asume distribución normal, y las colas del mercado son más gordas (con 2σ
deberían quedar fuera el ~5 % de los cierres; en la práctica quedan más). No predicen: describen.

**Qué se dice en el informe, con las bandas:**

- suelo y techo del rango con precio, y el ancho en % del precio;
- `%B` y en qué mitad está el cierre;
- el régimen (compresión / normal / expansión) **con su percentil y la ventana**;
- si el régimen y la alineación de EMAs se contradicen, se dice («rango estrecho dentro de tendencia
  bajista: el rebote tiene techo en la banda media»), no se elige el que convenga.

**No hay medición detrás.** En este repositorio no hay backtest de Bollinger; va como método de lectura
de volatilidad y rango, igual que el SAR. No se presenta como ventaja ni como permiso de entrada: eso lo
deciden `trading-action` y sus skills de tipo de trader.

## Los cinco modelos de Jesús Navarrete (clase del 09/08/2024)

Documentados en `finance/analisis-tecnico/videos/2024-08-09-5-modelos-aperturas-cierres/summary.md`
(vídeo `96jjClve3fE`). Resumen operativo:

| # | Modelo | Entrada | Salida | Marco |
|--:|---|---|---|---|
| 1 | Velas de entrada / salida | vela de entrada | vela de salida (lápida o libélula) contraria | el mismo día, nunca *overnight* |
| 2 | Rotación de promedios | EMA3 rota contra EMA9 | contra-rotación, en el rechazo del mínimo (largo) o del máximo (corto) | velas de 15/30/60 min |
| 3 | Condición óptima | precio bajo EMA9 (corto) o sobre EMA9 (largo), con Parabólicas sincronizadas | condición óptima contraria | el del *swing*; error asumido del 5 % |
| 4 | Open up / open down | la apertura con hueco | el hueco contrario | obliga a *overnight* |
| 5 | 9 contra 20 | EMA9 rota contra EMA20 | la rotación inversa | **solo velas de 1 minuto** |

Vocabulario del autor: **autocorrección = EMA20** (equilibrio del mercado); **rechazo del mínimo** = mínimo
superior al de la vela anterior; **guía** = rotación pendiente que anticipa; **parabólicas flat** = aviso de
movimiento violento, no señal de entrada. Las Parabólicas **no se usan solas**. La temporalidad elegida fija
la duración del *swing*: con velas de hora son ~3 horas.

## Reglas de la casa

- **El técnico no decide la cartera.** El peso y la entrada los fijan `propuesta-acciones.md` y
  `propuesta-actual.md` con fundamentales y señales de invalidación escritas. El gráfico sirve para
  (a) elegir el momento de una compra ya decidida y (b) describir el régimen cuando el dueño pregunta.
- **Nunca se presenta un patrón como hecho.** «Cruce dorado», «suelo», «ruptura»: se dice qué es
  (dos medias que se cruzan) y no lo que promete.
- **Una caída no es una señal de compra.** Es la lección Nike/PayPal del corpus: hay que distinguir
  «cayó y se abarató» de «cayó porque se deteriora», y eso se ve en las cuentas, no en la vela.
- Si el dueño pide niveles de entrada/salida, se dan **precios concretos** derivados de los
  indicadores (EMA20, SAR, máximo del mes anterior) y se marca que son niveles técnicos, no valores.

## Pitfalls

- **Yahoo repite el mes en curso en dos barras** (la del mes y la del último precio). El script las
  fusiona; si se lee la respuesta cruda, hay que hacerlo a mano o la EMA sale mal. La clave de fusión
  depende de la temporalidad (`%Y-%m` en mensual, `%Y-%m-%d` en diaria/semanal): agrupar por mes en
  semanal aplastaba 262 velas de 5 años en 61 y todos los indicadores salían falsos.
- **Sin histórico no hay indicador:** por debajo de ~25 velas el script se niega. Para EMA20 y para
  Bollinger(20) hacen falta al menos 20 velas, y el percentil del ancho necesita ~200 para significar
  algo; con menos, el régimen de volatilidad sale raro (percentil 0 o 100) y se dice que no hay serie.
- **El ancho de Bollinger no se compara entre activos**, solo consigo mismo: 25 % de ancho es normal en
  NVDA semanal y altísimo en un bono. Siempre con percentil y ventana, nunca «tiene las bandas muy
  anchas» a secas.
- **Bollinger y EMA20 no son lo mismo:** la banda media es la **SMA**20, la EMA20 pondera el reciente.
  En tendencia se separan; no se mezclan como si fueran el mismo nivel.
- **Tickers extranjeros:** el sufijo de plaza es obligatorio (`.MC`, `.DE`, `.AS`, `.L`, `.T`).
  Sin él, Yahoo devuelve otro instrumento o nada.
- **Los splits rompen la serie** si se mezclan fuentes: usa siempre la misma (el `chart` de Yahoo ya
  viene ajustado por split).
- El script no descarga dividendos ni fundamentales: para la ficha completa, `propuesta-acciones.md`
  §4 y la skill `cribado-acciones`.

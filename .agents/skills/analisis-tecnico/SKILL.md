---
name: analisis-tecnico
description: Usar cuando el dueño pida velas (mensuales, semanales o diarias), EMAs, medias, Parabolic SAR o «cómo está el gráfico» de una empresa. Calcula los indicadores con un script propio y los interpreta sin inventar señales.
---

# Análisis técnico (velas + EMA3/9/20 + Parabolic SAR)

## Qué resuelve

«¿Cómo cotiza X en velas mensuales?», «dame EMA3, EMA9, EMA20 y las paramétricas SAR»,
«¿el gráfico acompaña o contradice la tesis?». La respuesta es **una tabla con las velas y los
indicadores**, más dos líneas de lectura. No es una recomendación de compra.

## Script

`.agents/skills/analisis-tecnico/scripts/tecnicos.py` — solo stdlib, sin pandas ni TA-Lib.

```bash
python3 .agents/skills/analisis-tecnico/scripts/tecnicos.py AMZN              # mensual, 10 años
python3 .agents/skills/analisis-tecnico/scripts/tecnicos.py NVDA --interval 1wk --range 5y
python3 .agents/skills/analisis-tecnico/scripts/tecnicos.py NFLX --tail 12 --emas 3,9,20 --json
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
5. **La vela en curso está sin cerrar.** El último mes se mueve hasta el último día: se dice siempre
   («noviembre va por la mitad») y no se trata como cierre.

### Ejemplo real (05/11/2026, mensual)

| Ticker | Precio | EMA3 | EMA9 | EMA20 | SAR | Lectura |
|---|---:|---:|---:|---:|---:|---|
| AMZN | 259,17 | 253,26 | 249,00 | 235,38 | 286,04 (bajista, giro en octubre) | Tendencia alcista intacta, pero el SAR mensual avisó en octubre y no se ha vuelto a girar |
| NVDA | 183,11 | 197,59 | 199,51 | 181,71 | 243,37 (bajista, giro **este mes**) | Giro bajista recién hecho; EMA3 ya por debajo de EMA9 |
| NFLX | 64,82 | 66,46 | 75,91 | 83,02 | 96,69 (bajista, 11 velas) | Bajista de libro: EMA20 > EMA9 > EMA3 y precio por debajo de las tres |

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
  fusiona; si se lee la respuesta cruda, hay que hacerlo a mano o la EMA sale mal.
- **Sin histórico no hay indicador:** por debajo de ~25 velas el script se niega. Para EMA20 mensual
  hacen falta al menos 20 meses, y para que la EMA20 tenga sentido, bastantes más.
- **Tickers extranjeros:** el sufijo de plaza es obligatorio (`.MC`, `.DE`, `.AS`, `.L`, `.T`).
  Sin él, Yahoo devuelve otro instrumento o nada.
- **Los splits rompen la serie** si se mezclan fuentes: usa siempre la misma (el `chart` de Yahoo ya
  viene ajustado por split).
- El script no descarga dividendos ni fundamentales: para la ficha completa, `propuesta-acciones.md`
  §4 y la skill `cribado-acciones`.

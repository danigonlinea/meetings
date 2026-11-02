---
name: revision-cartera
description: Usar cuando toque la revisión trimestral de la cartera, cuando una señal del §10 cruce su umbral o cuando el usuario pregunte "¿toca cambiar el % de RV?". Mide las señales, corre el termómetro y escribe la revisión; la decisión del % sigue siendo del dueño.
---

# Revisión de la cartera

## Metadatos

- Carpeta: `finance/portfolio/`. Propuesta vigente: `propuesta-actual.md` (§2 señales, §10 umbrales).
- Datos del termómetro: `finance/portfolio/termometro-datos.json`.
- Script: `python3 tools/termometro.py`.
- Salida: `finance/portfolio/revision-YYYY-QN.md` con `type: portfolio-review`.
- Esta skill **no decide** el % de RV ni ejecuta órdenes. Mide, calcula y propone.

## Paso 1: Reúne los siete datos

Actualiza `termometro-datos.json` con la fecha de hoy. Cada valor necesita fuente y fecha; sin dato, deja `null` y dilo en la revisión.

| Clave | De dónde sale |
| --- | --- |
| `inflacion` | Último dato interanual de la zona euro (Eurostat/BCE). |
| `estr` | Tipo €STR publicado por el BCE. |
| `rf_cartera` | TIR ponderada de la renta fija de la cartera, de las fichas de los fondos (MyInvestor MCP). |
| `hy_oas_pb`, `bb_oas_pb` | Spreads de crédito europeos (índices ICE BofA vía FRED o equivalente). |
| `sp500_per`, `stoxx600_per`, `em_per` | PER forward de los tres índices. |
| `bono_10y` | Rentabilidad del bono a 10 años de referencia para la prima de riesgo. |
| `rv_pct` | % de RV de la propuesta vigente. |

Reglas que no se negocian:

- **Ninguna cifra sin fuente.** Un dato estimado se marca `estimado` en la revisión.
- **La señal 1 se mide con la RF de la cartera, no con el €STR.** El €STR describe el colchón, que está fuera de la base. Confundirlos fue lo que llevó al 54,9%.
- No cambies la base neutra (45%) ni los pesos sin decirlo en voz alta y sin argumento.

## Paso 2: Corre el termómetro

```bash
python3 tools/termometro.py
python3 tools/termometro.py --rv 45   # escenario alternativo
```

Comprueba a mano los derivados que imprime: earnings yield, RF real y prima de riesgo. Si un número te sorprende, revisa el dato de entrada antes de escribir.

## Paso 3: Escribe la revisión

`finance/portfolio/revision-YYYY-QN.md`, con estas secciones:

1. **Qué ha cambiado** desde la revisión anterior (tabla: señal, antes, ahora, efecto).
2. **La tabla del §2 puntuada**, con el total y el % de RV resultante.
3. **Umbrales cruzados** (salida del script) y qué implican.
4. **Qué se propone** y qué costaría: puntos de caída y de retorno por cada 10 puntos de RV.
5. **Lo que no se puede medir** con los datos de hoy.
6. **Decisión del dueño**: el % de RV y si se ejecuta. Nunca lo rellenes tú.

## Paso 4: Cierra

```bash
python3 tools/build_index.py && python3 tools/verify.py
```

Actualiza el estado en `finance/portfolio/README.md` solo si el dueño aprueba el cambio. Si no hay decisión, el estado sigue siendo el vigente.

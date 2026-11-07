---
name: medir-metodo-compras
description: Medir con datos la ventaja de una regla de compra. Solo a petición.
---

# Medir la ventaja de una regla de compra

**Esta skill no se ejecuta por iniciativa propia.** Solo entra cuando el dueño lo pide explícitamente:
«mídeme esto», «¿tiene ventaja?», «¿sigue funcionando?», «hazme el backtest», «revisión adversarial».
Si la pregunta es «¿cómo está X?» o «¿dónde compro?», se va a `analisis-tecnico` o a `trading-action`
y aquí **no se calcula nada**.

## Qué hace

Convierte una regla de entrada en código y la mide contra un control, con estas decisiones fijas:

| Pieza | Cómo se mide |
|---|---|
| Unidad | **R** (1R = entrada → stop). Nunca porcentajes: mezclan riesgo y resultado |
| Entrada | al cierre de la vela de señal |
| Stop | mínimo de la vela de señal |
| Salida | objetivo a múltiplos de R + horizonte en velas |
| Empate | si la misma vela toca stop y objetivo, **cuenta como pérdida** |
| Control | la misma regla de stop/objetivo comprando un día de cada tres |
| Independencia | se cuenta **episodios** (rachas), no operaciones sueltas: señales solapadas inflan el acierto |
| Costes | `--coste 0.2` (comisión + deslizamiento ida y vuelta) |
| Vigencia | `--ultimos-meses 12` y `6`: la ventaja caduca |

## Comandos

```bash
S=.agents/skills/medir-metodo-compras/scripts/backtest_entradas.py
python3 $S --rr 2                        # histórico completo, 10 pares /USDT
python3 $S --rr 2 --ultimos-meses 12     # ¿sigue viva la ventaja?
python3 $S --rr 2 --coste 0.2            # con comisiones y deslizamiento
python3 $S --rr 3                        # sensibilidad al objetivo
```

Datos: `api.binance.com/api/v3/klines` **paginado** (1.000 velas por petición; hay que recorrer `startTime`
o la serie se corta en silencio). 1.600 velas de calentamiento para que la EMA200 no arrastre el seed.

## Lo medido hoy (07/11/2026, 10 pares, 2R, sin costes)

| Versión | n | Episodios | Acierto | R medio |
|---|--:|--:|--:|--:|
| Control (1 de cada 3 días) | 3.926 | 570 | 29,1 % | −0,14 |
| Vela de entrada + volumen | 781 | 271 | 40,7 % | +0,18 |
| + sesgo mensual (mes cerrado) | 463 | 162 | 39,7 % | +0,14 |
| + triple confirmación diaria | 411 | 138 | 41,4 % | +0,19 |
| **+ EMA200 diaria (V5)** | **513** | **165** | **42,3 %** | **+0,22** |

V5 con IC95 [+0,02, +0,44]. Con 0,2 % de costes: **+0,18R**. Últimos 12 meses: **−0,00R** frente a −0,17R
del control en el mismo mercado. Con 1R: +0,10R · 3R: +0,31R.

**Lectura:** ventaja fina y **apagada en el último año**. Sirve como filtro de calidad, no como generador de
esperanza. Por par: BTC +0,49 (52) · SOL +0,47 (54) · AVAX +0,31 (34) · XRP +0,27 (56) · LINK +0,21 (54) ·
DOGE +0,19 (54) · ADA +0,17 (47) · BNB +0,14 (69) · ETH +0,12 (49) · QNT −0,16 (44).

## Trampas que ya han mordido en este repo

- **Look-ahead.** Usar la EMA20 del mes **en curso** (calculada con el cierre de ese mes) para decidir dentro
  del mes. Se usa siempre la última vela **cerrada**.
- **Media de volumen contaminada.** Incluir la vela de la señal en la media de 20 hace el filtro más estricto
  de lo documentado. Se calcula con las 20 **anteriores**.
- **Calentamiento corto.** Con 1.000 velas y arranque en la 25, la EMA200 sale mal. 1.600 velas y primera
  evaluación en la 400.
- **Solape.** Señales diarias con ventanas de 20 velas: el acierto bruto (72-77 %) se queda en 51-55 % al
  exigir no solapar. Por eso se publican episodios.
- **Tautología.** «El precio vuelve al nivel del cruce» se cumple el 93-99 % de las veces… igual que volver a
  cualquier nivel. Si el control da lo mismo, no hay hallazgo.
- **Sobreajuste.** Probar cinco variantes y quedarse la mejor es *data snooping*. Se declara y se pide muestra
  fuera (otros activos, otro periodo) antes de convertirlo en regla.
- **Confundir la media con la mediana.** +0,22R medio con mediana de −1R es una distribución de cola: la
  operación típica pierde.

## Qué NO se ha medido

- El **gatillo de 4 h** y el stop de 4 h: todos los R publicados usan vela diaria.
- La **caja semanal** y el **R/R** derivado de ella.
- **Acciones**: todo esto es cripto. Las 100 candidatas de `propuesta-acciones.md` siguen sin backtest.
- Los informes de activos concretos (`analisis-hbar-*`, `analisis-pepe-*`, `analisis-qnt-*`) miden el
  **marcador de 8**, no esta regla: son otra pregunta y no se mezclan.

## Cómo se entrega

Números con `n`, episodios, IC si hay muestra, y **la comparación con el control**. Si la ventaja no aparece,
se dice sin maquillar. Cada cifra se puede reproducir con el comando de arriba: si no se reprodujo, no se
publica.

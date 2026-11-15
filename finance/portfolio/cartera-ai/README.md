# Cartera-ai — 150.000 €

Cartera nueva, diseñada desde cero el 14/11/2026 con tres reglas del titular: **todos los fondos
disponibles en MyInvestor**, **ninguno que reparta dividendos** (solo acumulación) y **composición libre**.
Resultado: 9 fondos indexados + 6 acciones, 75 % RV / 25 % RF, 170,10 €/año de coste (0,113 %).

Es un patrimonio **separado** de `cartera-myinvestor/` y `cartera-renta4/`: no se suma, no se compara
y no se rebalancea contra las otras.

## Ficheros

| Fichero | Qué es | ¿Se edita? |
| --- | --- | --- |
| `propuesta-actual.md` | **La cartera**: 15 posiciones con ISIN/ticker, importes, pesos, TER, tesis, ejecución, descartes y pendientes | Sí |
| `README.md` | Este mapa | Sí |

Una sola cartera, un solo documento. La cartera nace de cero y las decisiones son del agente, así que no
hay foto de saldos que mantener aparte: la propuesta **es** la cartera. Cuando se ejecute y existan
posiciones reales con precios de compra, se abrirá `cartera-actual-YYYY-MM-DD.md` con los saldos, y solo
entonces.

## Reglas

- **Solo clases de acumulación.** Ningún fondo que reparta dividendos: se filtra `distributing = 0` en la
  ficha y se descarta el que reparta aunque sea la clase más barata. Ninguna de las seis acciones retribuye
  al accionista.
- **Solo fondos del catálogo de MyInvestor**, verificado por ISIN con `get_funds`, no por nombre.
- **Sin ETFs.** Un ETF no admite traspaso y cada rebalanceo tributa al 19-23 %.
- **Un dato, un sitio.** Pesos, diagnóstico, coste y órdenes viven en `propuesta-actual.md`; no se duplican.
- Rebalanceo **anual** con bandas de ±5 puntos, con aportaciones o traspasos de fondos; nunca vendiendo
  acciones (cristalizaría plusvalía).

## Estado a 14/11/2026

- **Propuesta cerrada:** 75,0 % RV / 25,0 % RF, 170,10 €/año de TER, 15 órdenes en una sesión.
- **Sin ejecutar:** la cuenta está en liquidez. Pendiente confirmar horizonte, comisión de acciones del
  bróker y entrada en una o dos tandas.
- **Decisión abierta:** clase del núcleo (iShares World S al 0,06 %, sin 3A/5A de clase) frente a Fidelity
  World al 0,12 % (con historial). 22,50 €/año de diferencia.

# Cartera-ai — 150.000 €

Cartera nueva, diseñada desde cero el 14/11/2026 con tres reglas del titular: **todos los fondos
disponibles en MyInvestor**, **ninguno que reparta dividendos** (solo acumulación) y **composición libre**.
Resultado: 9 fondos indexados + 6 acciones, 75 % RV / 25 % RF, 170,10 €/año de coste (0,113 %).

Es un patrimonio **separado** de `cartera-myinvestor/` y `cartera-renta4/`: no se suma, no se compara
y no se rebalancea contra las otras.

## Ficheros

| Fichero | Qué es |
| --- | --- |
| `100k.md` | La cartera de **100.000 €**: 7 fondos indexados + 4 acciones, 74,9 % RV, 0,116 % de coste |
| `150k.md` | La cartera de **150.000 €** (la original del 14/11/2026): 9 fondos + 6 acciones, 74,8 % RV, 0,113 % |
| `200k.md` | La cartera de **200.000 €**: misma estructura que la de 150k con las órdenes al doble |
| `README.md` | Este mapa |

**Un fichero por talla, una cartera por fichero.** El mandato es el mismo en las tres; lo que cambia es
cuántas líneas aguanta el tamaño y cuánto pesan los tickets pequeños. A 100.000 € el diseño se simplifica;
a partir de 150.000 € ya no cambia. La cartera nace de cero y las decisiones son del agente, así que no hay
foto de saldos que mantener aparte: cada fichero **es** su cartera. Cuando se ejecute una, se abrirá
`cartera-actual-YYYY-MM-DD.md` con los saldos y los precios de compra, y solo entonces.

## Reglas

- **Solo clases de acumulación.** Ningún fondo que reparta dividendos: se filtra `distributing = 0` en la
  ficha y se descarta el que reparta aunque sea la clase más barata. Ninguna de las acciones retribuye
  al accionista.
- **Solo fondos del catálogo de MyInvestor**, verificado por ISIN con `get_funds`, no por nombre.
- **Sin ETFs.** Un ETF no admite traspaso y cada rebalanceo tributa al 19-23 %.
- **Un dato, un sitio.** Pesos, diagnóstico, coste y órdenes viven en el fichero de su talla; no se duplican.
- Rebalanceo **anual** con bandas de ±5 puntos, con aportaciones o traspasos de fondos; nunca vendiendo
  acciones (cristalizaría plusvalía).

## Estado a 15/11/2026

- **Tres tallas cerradas:** 100k (0,116 %), 150k (0,113 %) y 200k (0,113 %). Ninguna ejecutada.
- **Decisión abierta:** clase del núcleo (iShares World S al 0,06 %, sin 3A/5A de clase) frente a Fidelity
  World al 0,12 % (con historial). 120 €/año de diferencia a 200.000 €.
- **Comisión de compraventa de acciones del bróker:** no publicada en el MCP; pendiente de verificar antes de
  la primera orden.

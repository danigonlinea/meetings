---
title: "Cartera MyInvestor: cómo funciona esta carpeta"
date: 2026-11-18
type: reference
category: finance
tags: [cartera, indice, proceso]
status: living
---
# Cartera MyInvestor: cómo funciona esta carpeta

La cartera de MyInvestor (**100.000 € = 90.000 € invertibles + 10.000 € de colchón**, a 30/10/2026),
dentro de `finance/portfolio/`. Es independiente de `../cartera-renta4/`: no comparten saldos, ni
propuesta, ni cifras. El resto de material financiero (vídeos, webinars, informes) está en las otras
subcarpetas de `finance/`.

## Un documento por papel

| Fichero | Rol | ¿Se edita? |
| --- | --- | --- |
| `cartera-actual.md` | **Fotografía congelada** del estado real a 30/10/2026: saldos, pesos, ISIN, TER, TIR, duración, Rock y consolidado de 90.000 €. Fuente de verdad de las posiciones | **No.** Un cambio de saldos genera `cartera-actual-YYYY-MM-DD.md` |
| `propuesta-pieza.md` | **La cartera vigente y única** (18/11/2026, final): **38,3 % de indexado como pieza**, 61,7 % en tres convicciones value y cinco papeles de crédito, 54,6 % de RV, 529,90 €/año, Rock desmontado por traspaso, 23 órdenes, plan de 1.000 €/mes, seis escenarios preparados y la prueba que invalida el diseño en 2029. **⚠️ Pendiente de la revisión del titular** (pedida el 18/11): **no se ejecuta ninguna orden hasta esa revisión** | **Sí**, es el documento de trabajo |
| `propuesta-actual.md` | **Superada** (04/11/2026, nivel 55/45 con Rock intacto). Se conserva por su **§2**, que es la fuente del criterio del 55 % citado por otras propuestas | **No.** Solo se corrige una errata de datos |
| `propuesta-acciones.md` | **Bloque de riesgo aparte**: cuatro acciones individuales sin dividendo. No forma parte de la cartera de fondos, no entra en su look-through y no se rebalancea contra ella | Sí, pero nunca se suma a la cartera de fondos |

**Una sola propuesta viva.** La carpeta llegó a tener cinco propuestas paralelas con cinco cifras
distintas de la misma cartera; el 04/11/2026 se resolvieron en `propuesta-actual.md` y se borraron. El
**18/11/2026** se repitió el ejercicio con la pregunta que quedaba abierta —cuánto indexado— y
`propuesta-ai.md` (60/40 en once fondos **indexados**, 0,224 %) se retiró por partir de la premisa
contraria a la que el titular eligió. Su contenido íntegro sigue en el historial de git (último commit:
`5fae506`). **No se crean carteras paralelas:** si aparece una idea, o entra en la propuesta vigente o se
descarta con el número delante.

La variante con **Rock como pieza fija y monetario escalonado** vive en su propia carpeta,
`finance/portfolio/cartera-ai-rock-index-value-todo/`, y la de **nivel A (69,4 % indexado)** en
`finance/portfolio/cartera-ai-rock-desmontado/`. Ninguna se ejecuta a la vez que otra: la adoptada es
`propuesta-pieza.md` y las demás quedan como alternativas con su precio escrito.

El diagnóstico, el veredicto frente a las fuentes y las revisiones adversariales **no viven en ficheros
aparte**: sus conclusiones están dentro de la propuesta y el debate que las produjo, en el historial de
git. Un documento por rol evita las dos verdades.

## Estado a 18/11/2026

- **⚠️ Revisión pendiente del titular.** La cartera está cerrada como documento, pero el titular pidió
  revisarla otro día antes de ejecutarla: **las 23 órdenes de §9 no se lanzan hasta entonces**. Si alguien
  pregunta por esta cartera, lo primero que hay que contestar es que está pendiente de revisión.
- **Cartera:** 100.000 € totales = 10.000 € de colchón (Groupama, fuera de la cartera) + 90.000 €
  invertibles (60.000 € manuales + 30.000 € en Rock).
- **Reparto:** **54,6 % de RV / 45,4 % de RF y caja** por look-through; **38,3 % del capital en cinco
  fondos índice** (0,12 % de media) y **61,7 % en ocho activos** (0,87 % de media). Coste total
  **529,90 €/año (0,530 %)**, cero comisiones de éxito.
- **Trece fondos:** World 17.000 · EM 6.000 · Small-Cap 4.000 · REITs 3.500 · Agg 1-5Y 4.000 ·
  Magallanes Europe 9.000 · Horos Value 6.000 · Cobas Large Cap 6.000 · Cobas Renta 6.000 · Neuberger
  11.000 · M&G 6.000 · Aegon ABS 8.000 · DWS Ultra Short 3.500.
- **Ejecución:** **23 traspasos en dos fases** (17 manuales hoy + 6 desde el puente de Rock) y una
  cancelación de cartera automatizada. Traspaso y nunca reembolso: 0 € de impuestos; reembolsar Rock
  costaría ≈2.590 €.
- **Caída estimada tipo 2008: −23,2 % (−20.885 €).** Duración de la RF **1,54** (−630 € por +100 pb).
- **Aportación:** 1.000 €/mes (799 € mensuales + 603 € trimestrales / 3).
- **Pendiente antes de la primera orden:** los **gastos mensuales** (el colchón de 10.000 € nunca se
  dimensionó contra un dato real, hoy 833 €/mes asumidos), la **comisión de suscripción en pantalla** de
  los trece destinos y la confirmación de que los 7.000 € de aportación nueva están en la cuenta
  (`propuesta-pieza.md` §14: entran en World 3.000 · Magallanes 2.000 · Aegon 2.000).

## Reglas de esta carpeta

- Un dato se escribe una vez: la foto en `cartera-actual.md`, la decisión y su porqué en
  `propuesta-pieza.md`. Ningún fichero replica la tabla de posiciones del otro.
- Toda propuesta se ejecuta por **traspaso** entre fondos armonizados, nunca por reembolso.
- Nada se mueve sin verificar antes la clase del fondo y su coste real en la plataforma.
- **Rock sí se desmonta, y sin tributar.** La regla anterior («Rock no se desmonta: la plusvalía se
  cristalizaría») era cierta solo para un reembolso. MyInvestor cancela la cartera automatizada
  traspasando sus nueve fondos a un monetario puente: es traspaso, cuesta **0 €** de impuestos y tarda
  5-10 días. Elegir «recibir el dinero en efectivo» sí cristaliza: esa opción no se usa.
- Las acciones individuales son **otro bloque de riesgo** del titular: no entran en el % de RV de esta
  cartera ni se compensan con ella.

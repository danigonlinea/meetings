---
title: "Cartera MyInvestor: cómo funciona esta carpeta"
date: 2026-11-26
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

**Aquí vive la foto; la propuesta vive al lado.** Desde el 26/11/2026 esta carpeta guarda solo lo que
existe de verdad (saldos, posiciones, ISIN) y la propuesta final está en
[`../cartera-myinvestor-propuesta/`](../cartera-myinvestor-propuesta/README.md).

## Un documento por papel

| Fichero | Rol | ¿Se edita? |
| --- | --- | --- |
| `cartera-actual.md` | **Fotografía congelada** del estado real a 30/10/2026: saldos, pesos, ISIN, TER, TIR, duración, Rock y consolidado de 90.000 €. Fuente de verdad de las posiciones | **No.** Un cambio de saldos genera `cartera-actual-YYYY-MM-DD.md` |
| `README.md` | Este mapa | Sí, si cambia el rol de la carpeta |

| Fuera de esta carpeta | Rol |
| --- | --- |
| `../cartera-myinvestor-propuesta/propuesta-actual.md` | **La propuesta final de esta cartera** (26/11/2026): la Opción A del ranking, 7 fondos, 70 % de indexado regional, 10 % de SMID activa y 20 % de escudo corto, `81,03 %` de RV real y `0,273 %` de TER, sobre los 100.000 € libres + los 10.000 € intocables en `Groupama`. Sin ejecutar |
| `../cartera-myinvestor-propuesta/README.md` | El mapa de esa propuesta y sus pendientes |

**Una sola propuesta.** La carpeta llegó a tener cinco propuestas paralelas con cinco cifras distintas
de la misma cartera; se resolvieron en un único documento y se borraron. El **26/11/2026** se retiraron
las tres que quedaban —`propuesta-actual.md` (55/45 del 04/11), `propuesta-pieza.md` (38,3 % de indexado
como pieza, 18/11) y `propuesta-70-30.md` (alternativa pasiva del 19/11)— junto con
`propuesta-acciones.md`, y el titular eligió la **Opción A** del ranking del laboratorio: es la propuesta
final y vive en la carpeta de al lado. Los cuatro documentos siguen íntegros en el historial de git
(último commit con los tres primeros: `4f8e2bd`). **No se crean carteras paralelas:** si aparece una
idea, o entra en la propuesta vigente o se descarta con el número delante.

Las variantes que se quedaron en el laboratorio siguen ahí con su precio escrito: **Rock como pieza fija
y monetario escalonado** en
`finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-rock-index-value-todo/` y el
**nivel A (69,4 % indexado)** en
`finance/laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-rock-desmontado/`. Ninguna se
ejecuta a la vez que otra: la adoptada es la propuesta final.

El diagnóstico, el veredicto frente a las fuentes y las revisiones adversariales **no viven en ficheros
aparte**: sus conclusiones están dentro de la propuesta y el debate que las produjo, en el historial de
git. Un documento por rol evita las dos verdades.

## Estado a 26/11/2026

- **Foto vigente:** `cartera-actual.md` a 30/10/2026. 100.000 € totales = 10.000 € de colchón (Groupama,
  fuera de la cartera) + 90.000 € invertibles (60.000 € manuales + 30.000 € en Rock), con el inventario
  de los 18 fondos.
- **Propuesta final:** la Opción A, en `../cartera-myinvestor-propuesta/propuesta-actual.md`.
  ⚠️ **Sin ejecutar**: la decisión y la fecha son del titular, y no se lanza ninguna orden hasta
  entonces.
- **Lo que la propuesta cambia respecto a la foto:** Rock se desmonta por el puente monetario
  (**0 € de impuestos**: es traspaso, nunca reembolso) y los 90.000 € invertibles más los 10.000 € que
  hoy son colchón se reparten en siete fondos; el colchón se queda fuera de la cartera.
- **Pendiente antes de la primera orden:** los **gastos mensuales** (el colchón de 10.000 € nunca se
  dimensionó contra un dato real, hoy 833 €/mes asumidos) y la **comisión de suscripción en pantalla** de
  los siete destinos.

## Reglas de esta carpeta

- Un dato se escribe una vez: la foto en `cartera-actual.md`, la decisión y su porqué en
  `../cartera-myinvestor-propuesta/propuesta-actual.md`. Ningún fichero replica la tabla de posiciones
  del otro.
- Toda propuesta se ejecuta por **traspaso** entre fondos armonizados, nunca por reembolso.
- Nada se mueve sin verificar antes la clase del fondo y su coste real en la plataforma.
- **Rock sí se desmonta, y sin tributar.** La regla anterior («Rock no se desmonta: la plusvalía se
  cristalizaría») era cierta solo para un reembolso. MyInvestor cancela la cartera automatizada
  traspasando sus nueve fondos a un monetario puente: es traspaso, cuesta **0 €** de impuestos y tarda
  5-10 días. Elegir «recibir el dinero en efectivo» sí cristaliza: esa opción no se usa.
- Las acciones individuales son **otro bloque de riesgo** del titular: no entran en el % de RV de esta
  cartera ni se compensan con ella.

---
title: "Cartera: MyInvestor (foto + propuesta final) y Renta 4"
date: 2026-11-26
type: reference
category: finance
tags: [cartera, indice, myinvestor, renta4, cartera-myinvestor-propuesta, laboratorio-carteras]
status: living
---
# Cartera: MyInvestor (foto + propuesta final) y Renta 4

Dos patrimonios reales, separados y con foto y propuesta propias. **No se consolidan**: ninguna cifra de
una carpeta se suma, se compara ni se rebalancea contra la otra. Si algún día se quiere la vista conjunta,
se escribe en un documento aparte con su propia fecha.

La cartera de MyInvestor ocupa **dos carpetas**: `cartera-myinvestor/` guarda la **foto** de lo que hay
(saldos, 18 fondos, Rock) y `cartera-myinvestor-propuesta/` la **propuesta final**, la Opción A elegida el
26/11/2026. Renta 4 vive en una sola, con foto y propuesta dentro.

Los otros **veinticinco diseños** (las dos familias de cinco, el contenedor de estudio entre el 30 % y el
45 % de indexado, la cartera de referencia a los 40) y la cartera de un tercero están en
[`finance/laboratorio-carteras/`](../laboratorio-carteras/README.md): se estudian y se comparan, no se
ejecutan y no entran en ninguna cifra de esta carpeta.

| Carpeta | Qué es | Documentos |
| --- | --- | --- |
| `cartera-myinvestor/` | **La foto.** 100.000 € = 90.000 € invertibles (60.000 € manuales + 30.000 € de Rock) + 10.000 € de colchón, a 30/10/2026 | `cartera-actual.md` (inventario de los 18 fondos, con ISIN, TER, TIR y duración) + `README.md` de mapa |
| `cartera-myinvestor-propuesta/` | **La propuesta final de esa cartera (26/11/2026): la Opción A del ranking forense, `8,71/10` sobre seis.** Reparte los 100.000 € libres y deja intocables los 10.000 € de `Groupama` (`110.000 €` totales), 15 años (2026 → 2041): 7 fondos, `70 %` indexado regional desconcentrado, `10 %` de SMID activa y `20 %` de escudo corto (`81,03 %` de RV real, `0,273 %` de TER, 13 órdenes). ⚠️ Sin ejecutar | `README.md` de mapa + `propuesta-actual.md` (la cartera entera) + `comparativa-neon-2.md` (frente a la #3 del ranking) |
| `cartera-renta4/` | 34.769,20 € en cuatro fondos, cuenta de Renta 4 Banco | `cartera-actual.md` (foto 02/11/2026) + `propuesta-2026-11-02.md` (auditoría, rangos de mejora y propuesta del 02/11; historial) + `propuesta-actual.md` (**la propuesta vigente desde el 21/11/2026**: seis fondos sin indexados, Kaizen 25 %, Sigma 26,08 %, Magallanes 12 %, Akira 8 %, RV 50 %, 393,02 €/año y 3,71 % neto) |

Las acciones individuales son un **bloque de riesgo aparte** del titular: no forman parte de ninguna de
las dos carteras, no entran en su look-through y no se rebalancean contra ellas. Su documento de trabajo
(`propuesta-acciones.md`, 04/11/2026) se retiró el 26/11/2026 y sigue en el historial de git.

## Reglas
- **Un dato, un sitio.** En las carteras con dinero real los saldos viven en su `cartera-actual.md` y las
  decisiones en su `propuesta-actual.md`. En MyInvestor, además, **la foto y la propuesta están en
  carpetas distintas**: el saldo no se copia en la propuesta y la propuesta no se copia en la foto. Las
  carteras del laboratorio no tienen foto: nacen de cero y un solo documento es la cartera entera.
- **Nada se mueve de una carpeta a otra.** Un traspaso entre plataformas es un reembolso con peaje
  fiscal; si se plantea, se documenta en las dos propuestas antes de ejecutarlo.
- Cada carpeta ejecuta por **traspaso entre fondos armonizados** (0 € de impuestos), nunca por reembolso.
- Nada se mueve sin verificar antes la clase del fondo y su coste real en la plataforma.
- **Solo clases de acumulación.** Ningún fondo, ETF **ni acción** que reparta dividendos entra en la
  cartera: al buscar vehículos nuevos se filtra `distributing = 0` en la ficha y se descarta el que
  reparta, aunque sea la clase más barata o la única disponible. En un fondo se busca la clase «Acc»; en
  un ETF, la que acumula; en una acción, que no retribuya al accionista. En acciones extranjeras hay
  además retención en origen, así que el coste real de un dividendo es doble. Aplica a búsquedas futuras
  y es motivo de descarte escrito, no criterio implícito.

## Revisión
- Cada cartera se revisa **contra sus propios criterios**, no contra un medidor común: las carteras son
  independientes entre sí y lo que las distingue es el criterio que siguen (horizonte, necesidad de
  liquidez, tolerancia a la caída, coste, estilo).
- El % de renta variable no se puntúa: es una decisión del dueño que se cambia con argumentos, no con una
  suma de señales. El razonamiento con el que se fija el % va escrito en la propuesta vigente de cada
  cartera; los criterios anteriores (el 55 % de MyInvestor del 04/11/2026 y el 38,3 % de indexado del
  18/11) se conservan como historia en el historial de git.
- La revisión trimestral se escribe con la skill `revision-cartera` y se guarda como
  `revision-YYYY-QN.md` en esta carpeta.

## Estado a 26/11/2026

- **MyInvestor (foto 30/10/2026; propuesta final sin ejecutar, ⚠️ pendiente de la decisión del titular):**
  `cartera-myinvestor/cartera-actual.md` para lo que existe y
  `cartera-myinvestor-propuesta/propuesta-actual.md` para la decisión. La foto: 100.000 € = 10.000 € de
  colchón en `Groupama` + 90.000 € invertibles (60.000 € manuales y 30.000 € en Rock), con el inventario
  de los 18 fondos. La propuesta: **7 fondos**, `81,03 %` de RV real, **`0,273 %` de TER** (`8.432 €` de
  drag en 15A), `212.632 €` en el test neutro y `+61,54 %` acumulado real 2022–2026, con 13 órdenes
  cuadradas al euro y traspasos libres de IRPF desde la foto; los 10.000 € de `Groupama` quedan
  **intocables**. Rock se desmonta por el puente monetario (0 € de impuestos; reembolsar costaría
  ≈2.590 €). Frente a las otras cinco propuestas del ranking: `#1` en coste, desconcentración y
  acumulado —auditoría en
  [`../laboratorio-carteras/cartera-ai-definitiva-final/auditoria-ranking.md`](../laboratorio-carteras/cartera-ai-definitiva-final/auditoria-ranking.md).
  Pendientes: decidir y fechar la ejecución, gastos mensuales reales para dimensionar el colchón, la
  comisión de suscripción en pantalla y validar el acceso ómnibus a `iShares Developed World S` (mínimo de
  folleto `200 M€`).

- **Renta 4:** dos propuestas sobre la misma foto. **A corto (historial, 02/11/2026)** (`propuesta-2026-11-02.md`): Kaizen se
  queda y se recorta al 25 %, con 3.618 € a un indexado global (21,2 % de RV, 0,76 %). **A largo plazo (vigente)**
  (`propuesta-actual.md`, 21/11/2026, sin indexados): **Kaizen 25 %**, **Sigma Internacional 26,08 %**,
  **Magallanes European 12 %**, **Akira 8 %**, RF R 17,93 % y 6 Meses 10,99 %; **393,02 €/año (1,130 %)**,
  caída **−21,04 % (−7.315 €)**, **3,71 % neto** (3,22 % con éxito) y seis traspasos. Frente a la misma
  cartera con índice (228,86 €/año y 4,21 %) el mandato cuesta **+164 €/año y −4.461 € a 15 años**. Pendiente:
  adoptarla, el peso de Akira (8 % o 0 %) y verificar la custodia de Akira y la suscripción de AXA.

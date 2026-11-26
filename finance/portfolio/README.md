---
title: "Cartera: las tres carteras vivas (MyInvestor, Renta 4 y la propuesta Opción A)"
date: 2026-11-26
type: reference
category: finance
tags: [cartera, indice, myinvestor, renta4, cartera-ai-propuesta, laboratorio-carteras]
status: living
---
# Cartera: las tres carteras vivas

Tres patrimonios separados, con foto y propuesta propias. **No se consolidan**: ninguna cifra de una
carpeta se suma, se compara ni se rebalancea contra la otra. Si algún día se quiere la vista conjunta,
se escribe en un documento aparte con su propia fecha.

`cartera-myinvestor/` y `cartera-renta4/` son el dinero real, cada una en su plataforma.
`cartera-ai-propuesta/` es la propuesta elegida del laboratorio —la **Opción A** del ranking forense del
26/11/2026—, todavía sin ejecutar.

Los otros **veinticinco diseños** (las dos familias de cinco, el contenedor de estudio entre el 30 % y el
45 % de indexado, la cartera de referencia a los 40) y la cartera de un tercero están en
[`finance/laboratorio-carteras/`](../laboratorio-carteras/README.md): se estudian y se comparan, no se
ejecutan y no entran en ninguna cifra de esta carpeta.

| Carpeta | Qué es | Documentos |
| --- | --- | --- |
| `cartera-myinvestor/` | 100.000 € = 90.000 € invertibles (60.000 € manuales + 30.000 € de Rock) + 10.000 € de colchón | `cartera-actual.md` (foto 30/10) + `propuesta-pieza.md` (**la cartera final desde el 18/11/2026, ⚠️ pendiente de la revisión del titular antes de ejecutar**: 38,3 % de indexado como pieza, 23,3 % de convicción activa, trece fondos, 54,6 % de RV, 529,90 €/año, 23 traspasos en dos fases y 1.000 €/mes) + `propuesta-actual.md` (superada el 18/11, se conserva por su §2: el criterio del 55 %) + `propuesta-70-30.md` (alternativa indexada 70/30 del 19/11 sobre los 90.000 € invertibles: siete fondos indexados, 69,6 % de RV real, 102,85 €/año, caída −25.879 € y 12 traspasos) + `propuesta-acciones.md` (complemento de acciones) |
| `cartera-renta4/` | 34.769,20 € en cuatro fondos, cuenta de Renta 4 Banco | `cartera-actual.md` (foto 02/11/2026) + `propuesta-2026-11-02.md` (auditoría, rangos de mejora y propuesta del 02/11; historial) + `propuesta-actual.md` (**la propuesta vigente desde el 21/11/2026**: seis fondos sin indexados, Kaizen 25 %, Sigma 26,08 %, Magallanes 12 %, Akira 8 %, RV 50 %, 393,02 €/año y 3,71 % neto) |
| `cartera-ai-propuesta/` | **La propuesta elegida del laboratorio (26/11/2026): la Opción A del ranking de `../laboratorio-carteras/cartera-ai-definitiva-final/`, `8,71/10` sobre seis.** `100.000 €` libres + `10.000 €` intocables en `Groupama`, 15 años (2026 → 2041): 7 fondos, `70 %` indexado regional desconcentrado, `10 %` de SMID activa y `20 %` de escudo corto (`81,03 %` de RV real, `0,273 %` de TER, 13 órdenes). Sin ejecutar. | `README.md` de mapa + `propuesta-actual.md` (la cartera entera) |

`propuesta-acciones.md` (04/11/2026) es el **complemento de acciones** de la cartera de MyInvestor, no una
cartera aparte: cuatro acciones individuales sin dividendo mencionadas en el corpus, con ficha,
múltiplo y señal de invalidación, pensadas para convivir con la cartera una vez rebalanceada a 55/45.
No se financia vendiendo ninguna de las dos carteras ni se consolida con ellas, y
`../laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-andres/` no lleva acciones a propósito.

## Reglas
- **Un dato, un sitio.** En las carteras con dinero real los saldos viven en su `cartera-actual.md` y las
  decisiones en el `propuesta-actual.md` de la misma carpeta. **Las carteras `ai` no tienen foto**: nacen
  de cero y las decisiones son del agente, así que un solo documento —`propuesta-actual.md`— es la
  cartera entera. La foto se abre el día que haya posiciones reales con precio de compra.
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
  suma de señales. El razonamiento con el que se fijó el 55 % de `cartera-myinvestor/` está en su §2, como
  historia de esa decisión.
- La revisión trimestral se escribe con la skill `revision-cartera` y se guarda como
  `revision-YYYY-QN.md` en esta carpeta.

## Estado a 26/11/2026

- **MyInvestor (vigente desde el 18/11/2026, ⚠️ pendiente de la revisión del titular):** `propuesta-pieza.md`.
  100.000 € en trece fondos:
  **38,3 % de indexado como pieza** (34.500 € a 0,12 %), 61,7 % activo en tres convicciones value y cinco
  papeles de crédito, **54,6 % de RV**, **529,90 €/año (0,530 %)**, cero comisiones de éxito, duración 1,54
  y caída de manual −20.885 €. Rock se desmonta por el puente monetario (0 € de impuestos): 23 traspasos en
  dos fases y 1.000 €/mes. **El nivel C de `../laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-rock-desmontado/` §14 queda decidido**: el índice
  deja de ser el edificio y paga 293,80 €/año frente al nivel A, con +0,53 pp/año de alfa de empate
  escrito. Pendientes: gastos reales del colchón, comisión de suscripción en pantalla y si los 7.000 € de
  aportación nueva están en la cuenta. Alternativas con su precio: nivel A (`../laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-rock-desmontado/`)
  y Rock fija (`../laboratorio-carteras/cartera-ai-definitivas-estudiar/cartera-ai-rock-index-value-todo/`).

- **Renta 4:** dos propuestas sobre la misma foto. **A corto (historial, 02/11/2026)** (`propuesta-2026-11-02.md`): Kaizen se
  queda y se recorta al 25 %, con 3.618 € a un indexado global (21,2 % de RV, 0,76 %). **A largo plazo (vigente)**
  (`propuesta-actual.md`, 21/11/2026, sin indexados): **Kaizen 25 %**, **Sigma Internacional 26,08 %**,
  **Magallanes European 12 %**, **Akira 8 %**, RF R 17,93 % y 6 Meses 10,99 %; **393,02 €/año (1,130 %)**,
  caída **−21,04 % (−7.315 €)**, **3,71 % neto** (3,22 % con éxito) y seis traspasos. Frente a la misma
  cartera con índice (228,86 €/año y 4,21 %) el mandato cuesta **+164 €/año y −4.461 € a 15 años**. Pendiente:
  adoptarla, el peso de Akira (8 % o 0 %) y verificar la custodia de Akira y la suscripción de AXA.

- **`cartera-ai-propuesta` (26/11/2026, sin ejecutar):** `propuesta-actual.md`. La **Opción A** del ranking forense de `../laboratorio-carteras/cartera-ai-definitiva-final/` (`8,71/10`, #1 de seis), promovida a cartera viva: `100.000 €` libres + `10.000 €` intocables en `Groupama` (`110.000 €`), 15 años (2026 → 2041). **7 fondos**: `70 %` indexado regional desconcentrado (`38,7 %` en EE. UU. y `9,31 %` en el Top 10 US), `10 %` de SMID activa y `20 %` de escudo corto; **`81,03 %` de RV real**, **`0,273 %` de TER** (`8.432 €` de drag en 15A), **`212.632 €`** en test neutro y **`+61,54 %`** acumulado real 2022–2026, con 13 órdenes cuadradas al euro y traspasos libres de IRPF desde `cartera-myinvestor/cartera-actual.md`. La auditoría y el ranking de las otras cinco propuestas están en [`../laboratorio-carteras/cartera-ai-definitiva-final/auditoria-ranking.md`](../laboratorio-carteras/cartera-ai-definitiva-final/auditoria-ranking.md). Pendiente: la decisión del titular y validar en pantalla el acceso ómnibus a `iShares Developed World S` (mínimo de folleto `200 M€`).

---
title: "Cartera: cuatro carteras propias y una de referencia"
date: 2026-11-15
type: reference
category: finance
tags: [cartera, indice, myinvestor, renta4, cartera-ai, cartera-ai-andres, cartera-de-andres]
status: living
---
# Cartera: cuatro carteras propias y una de referencia

Cuatro patrimonios propios separados, con foto y propuesta propias. **No se consolidan**: ninguna cifra de
una carpeta se suma, se compara ni se rebalancea contra la otra. Si algún día se quiere la vista conjunta,
se escribe en un documento aparte con su propia fecha.

| Carpeta | Qué es | Documentos |
| --- | --- | --- |
| `cartera-myinvestor/` | 97.000 € invertibles: 67.000 € manuales + 30.000 € de Rock, más 10.000 € de colchón | `cartera-actual.md` (foto) + `propuesta-actual.md` (**definitiva desde 04/11/2026**: 55/45 en diez fondos solo, 424,80 €/año de coste real, catorce órdenes en §7) + `propuesta-acciones.md` (complemento de acciones) |
| `cartera-renta4/` | 34.769,20 € en cuatro fondos, cuenta de Renta 4 Banco | `cartera-actual.md` (foto 02/11/2026) + `propuesta-actual.md` (auditoría y rangos de mejora) |
| `cartera-ai/` | **Tres tallas del mismo diseño** de coste mínimo: `100k.md` (7 fondos + 4 acciones, 74,9 % RV, 0,116 %), `150k.md` (9 + 6, 74,8 %, 0,113 %) y `200k.md` (9 + 6, 74,8 %, 0,113 %) | Un fichero por talla; cada uno es la cartera entera (ISIN/ticker, órdenes, coste, descartes) |
| `cartera-ai-andres/` | **Dos tallas** con el criterio de Andrés, sin acciones: `100k.md` (11 fondos, 60,3 % RV, 0,46 %) y `200k.md` (14 fondos, 60,0 %, 0,51 %) | Un fichero por talla; cada uno es la cartera entera (ISIN, órdenes, descartes y señales) |
| `cartera-de-andres/` | **Cartera de un tercero**, no del dueño: la cuenta personal de Andrés (La Pizarra) publicada cada mes | `cartera-actual.md` (foto vigente) + `anteriores/` (fotos mensuales congeladas) |

`cartera-de-andres/` es material de **análisis**, no una cartera del dueño: no se suma, no se
rebalancea y no compite con las cuatro anteriores. Se actualiza con la skill `cartera-andres` cuando se
ingiere un vídeo de resultados del canal.

`cartera-ai/` y `cartera-ai-andres/` son dos diseños **independientes** del mismo agente con mandatos
distintos: la primera minimiza coste (indexado + acciones sin dividendo), la segunda sigue el criterio de
Andrés (gestión activa, sin acciones, 60 % de RV). No son dos versiones de lo mismo ni se ejecutan las dos
sobre el mismo dinero: el titular elige una, y dentro de cada una elige la talla.


`propuesta-acciones.md` (04/11/2026) es el **complemento de acciones** de la cartera de MyInvestor, no una
cartera aparte: cuatro acciones individuales sin dividendo mencionadas en el corpus, con ficha,
múltiplo y señal de invalidación, pensadas para convivir con la cartera una vez rebalanceada a 55/45.
No se financia vendiendo ninguna de las dos carteras ni se consolida con ellas. La cartera con acciones
propias y separada es la de `cartera-ai/`; `cartera-ai-andres/` no lleva acciones a propósito.

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

## Estado a 15/11/2026

- **MyInvestor:** propuesta cerrada al 55,0% de RV / 45,0% de RF, 0,438% de TER, 14 órdenes en dos
  sesiones. Pendientes: dimensionar los gastos mensuales del colchón y aguantar el −23,4% (−22.700 €).
- **Renta 4:** auditoría nueva. 15,3% de RV real, 0,83% de coste (287 €/año) y 65,7% del patrimonio en
  bonos corporativos. Recomendación: **Kaizen se queda** y se recorta al 25%, con 3.618 € a un indexado
  global (21,2% de RV, 0,76% de coste). Pendiente: confirmar el recorte y la clase del fondo de destino.
- **cartera-ai:** tres tallas cerradas el 15/11/2026, sin ejecutar. 100k (7 fondos + 4 acciones, 0,116 %),
  150k (9 + 6, 0,113 %) y 200k (9 + 6, 0,113 %). Pendientes: clase del núcleo y comisión de acciones del
  bróker.
- **cartera-ai-andres:** dos tallas cerradas el 15/11/2026, sin ejecutar. 100k (11 fondos, 60,3 % de RV,
  0,46 %) y 200k (14 fondos, 60,0 %, 0,51 %), con dos fondos cuyo TER no publica el MCP. Pendientes:
  horizonte real, coste de Myinvestor Value y Kaizen, y si se quiere un bloque de tres acciones.

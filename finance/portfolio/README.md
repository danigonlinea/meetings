---
title: "Cartera: dos carteras propias y una de referencia"
date: 2026-11-02
type: reference
category: finance
tags: [cartera, indice, myinvestor, renta4, cartera-de-andres]
status: living
---
# Cartera: dos carteras propias y una de referencia

Dos patrimonios separados, con foto y propuesta propias. **No se consolidan**: ninguna cifra de una
carpeta se suma, se compara ni se rebalancea contra la otra. Si algún día se quiere la vista conjunta,
se escribe en un documento aparte con su propia fecha.

| Carpeta | Qué es | Documentos |
| --- | --- | --- |
| `cartera-myinvestor/` | 97.000 € invertibles: 67.000 € manuales + 30.000 € de Rock, más 10.000 € de colchón | `cartera-actual.md` (foto) + `propuesta-actual.md` (**definitiva desde 04/11/2026**: 55/45 en diez fondos solo, 424,80 €/año de coste real, catorce órdenes en §7) + `propuesta-acciones.md` (complemento de acciones) |
| `cartera-renta4/` | 34.769,20 € en cuatro fondos, cuenta de Renta 4 Banco | `cartera-actual.md` (foto 02/11/2026) + `propuesta-actual.md` (auditoría y rangos de mejora) |
| `cartera-de-andres/` | **Cartera de un tercero**, no del dueño: la cuenta personal de Andrés (La Pizarra) publicada cada mes | `cartera-actual.md` (foto vigente) + `anteriores/` (fotos mensuales congeladas) |

`cartera-de-andres/` es material de **análisis**, no una tercera cartera del dueño: no se suma, no se
rebalancea y no compite con las dos anteriores. Se actualiza con la skill `cartera-andres` cuando se
ingiere un vídeo de resultados del canal.


`propuesta-acciones.md` (04/11/2026) es el **complemento de acciones** de la cartera de fondos, no una
tercera cartera: cuatro acciones individuales sin dividendo mencionadas en el corpus, con ficha,
múltiplo y señal de invalidación, pensadas para convivir con la cartera una vez rebalanceada a 55/45.
No se financia vendiendo ninguna de las dos carteras ni se consolida con ellas.

## Reglas

- **Un dato, un sitio.** Los saldos viven en el `cartera-actual.md` de su carpeta; las decisiones, en
  el `propuesta-actual.md` de esa misma carpeta.
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

- `termometro-datos.json` guarda las medidas del día (inflación, €STR, TIR de la RF, spreads y PER).
- `python3 tools/termometro.py` calcula los derivados, comprueba los umbrales del §10 y saca la tabla
  de caída y retorno para cada nivel de RV. No decide.
- La revisión trimestral se escribe con la skill `revision-cartera` y se guarda como
  `revision-YYYY-QN.md` en esta carpeta; el % de RV lo decide el dueño.

## Estado a 10/11/2026

- **MyInvestor:** propuesta cerrada al 55,0% de RV / 45,0% de RF, 0,438% de TER, 14 órdenes en dos
  sesiones. Pendientes: dimensionar los gastos mensuales del colchón y aguantar el −23,4% (−22.700 €).
- **Renta 4:** auditoría nueva. 15,3% de RV real, 0,83% de coste (287 €/año) y 65,7% del patrimonio en
  bonos corporativos. Recomendación: **Kaizen se queda** y se recorta al 25%, con 3.618 € a un indexado
  global (21,2% de RV, 0,76% de coste). Pendiente: confirmar el recorte y la clase del fondo de destino.

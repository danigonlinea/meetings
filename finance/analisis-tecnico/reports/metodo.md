---
title: "El patrón de análisis: método, reglas y orden de trabajo"
date: 2026-11-05
type: synthesis
category: finance
tags: [analisis-tecnico, metodo, reglas, patron, trading, checklist]
status: living
---

# El patrón de análisis

Síntesis de las 10 clases del corpus (26/10 – 04/11/2026) más la clase de referencia del 09/08/2024.
**No es una cartera ni una recomendación:** es el método tal como se aplica, con la evidencia de cuántas
clases lo sostienen y con lo que los datos dicen de él (ver `predicciones.md`).

## 1. La idea central

Todo el método se apoya en una sola creencia, repetida en 7 de 10 clases: **el precio vuelve al punto
donde se abrió una separación de medias** (la «anomalía»). De ahí sale todo lo demás: el cierre de la
posición no se inventa, se espera; el objetivo no se calcula desde el precio actual, se calcula desde el
nivel donde la anomalía se abrió.

Alrededor de ella hay una **jerarquía estricta**: la temporalidad mayor manda, el ecosistema de medias
filtra, las ventanas horarias sitúan, la primera vela decide la dirección y la figura da el gatillo. Nunca
se invierte ese orden.

## 2. Qué se repite, y cuánto pesa

Frecuencia = en cuántas de las 10 clases aparece el concepto usado como herramienta (no solo nombrado).
Una aparición en 1 clase se trata como idea personal; en 7 o más, como **regla del método**.

| Concepto | En | Veredicto |
|---|--:|---|
| Anomalía / «ley quero» | **9/10** | **Regla A** — es el eje; sin anomalía no hay cierre |
| Bandas de Bollinger | **8/10** | **Regla A** — borde de entrada y techo/suelo de la sesión |
| Tercio / Fibonacci | **8/10** | **Regla A** — valida o descarta un movimiento; tercio = retroceso perfecto |
| Rechazo de mínimo / máximo | 7/10 | Regla B — señal de cierre, no de entrada |
| Parabólica | 7/10 | Regla B — condición de giro y calendario, nunca señal aislada |
| Open gap de las 4:00 | 7/10 | Regla B — primer dato del día |
| Históricos / «viejo patrón» | 7/10 | Regla B — los niveles donde ya estuvo el precio son imán |
| EMA 200 | 7/10 | Regla B — soporte y techo; nunca objetivo (se mueve) |
| Vela mensual primero | 6/10 | Regla B — fija el sentimiento de todas las temporalidades |
| Stop-limit / trailing | 6/10 | Regla B — ejecución, no análisis |
| Sideline / zona zombie | 6/10 | Regla B — rango alto = distribución |
| Premarket / ventanas | 6/10 | Regla B — el reloj antes que el precio |
| Hombro (cabeza-hombro) | 5/10 | Regla C — estructura de la mensual |
| Fundamento del día | 5/10 | Regla C — filtro de último minuto, puede anular el gráfico |
| Cruce EMA 3 / 9 | 4/10 | Regla C — gatillo fino, solo en intradía |
| Autocorrección = EMA 20 | 4/10 | Regla C — nivel de equilibrio y de cierre |
| Libélula / lápida | 3/10 | Regla C — figura de vela, exige condición extra |
| Unidad 7 / 12 | 2/10 | Idea personal — reglas numeradas de compra |
| Gaudí / arco catenario | 2/10 | Idea personal — generador de escenarios |
| Swing equivalente | 1/10 | Idea personal — útil, pero no es doctrina |
| Reloj institucional | 1/10 | Idea personal — nombra lo que en otras clases hace sin nombre |

**Lectura:** el núcleo duro del método son **cuatro cosas** —anomalía, bandas, tercio y rechazo—, todas
en 7-9 de 10 clases. Todo lo demás son capas de confirmación o vocabulario propio.

## 3. El orden de trabajo (checklist)

Este es el patrón, en el orden en que él lo ejecuta. Sirve para replicarlo sin saltarse pasos.

1. **Temporalidad mayor primero.** Vela **mensual**: posición del precio dentro de su rango, distancia a
   máximo y mínimo. De ahí sale el sentimiento que se arrastra a todo lo demás. Si la mensual cierra
   negativa, **no hay *call* de compra** aunque el día sea alcista.
2. **Estructura semanal.** Hombro/cabeza de la figura y **cuántas semanas lleva consumidas** el tramo;
   el resto es lo que queda de vida a la anomalía.
3. **Fundamento del día.** Catalizador o ausencia de él (notas, escrutinio, Fed, petróleo). Sin
   catalizador, cualquier avance se mira con sospecha.
4. **El hueco de las 4:00.** Compara cierre de las 20:00 con apertura de las 4:00, lo mide **en centavos**
   y lo clasifica: extraordinario (abre arriba y queda plano) o moderado.
5. **Ventanas.** 4:00–7:00 (premarket no oficial), 7:00–9:30 (oficial), campana. Cada una con su máximo,
   mínimo y probabilidad de recuperación. **La ventana que se ignora es el error del día siguiente.**
6. **Ecosistema.** EMA 20, 50 y 200 del premarket. Si están cruzadas en contra, el escenario alcista queda
   descartado antes de mirar la figura.
7. **Sideline o dirección.** Rango lateral de 90 minutos o más en la parte alta = distribución → **no se
   opera la caja, se espera la ruptura**.
8. **Niveles.** Se construyen por suma: apertura + rango oficial (2,69 en NVDA), + un tercio, + el hueco,
   y los históricos (máximo/mínimo del premarket, cierre de ayer, mínimo de las 4:00).
9. **La primera vela decide.** «Quien avance menos es el que toma la dirección»: si la primera vela
   avanza, se busca histórico más un tic; si retrocede, se busca la banda o la media.
10. **Confirmación triple antes de la orden:** (a) anomalía cerrada o a favor, (b) el nivel coincide con
    banda, histórico o media, (c) la parabólica ya rotó. Sin las tres, no hay operación.
11. **Ejecución stop-limit**, nunca a mercado: gatillo en el nivel, límite unos centavos más allá.
12. **Gestión:** trailing en lugar de objetivo fijo cuando hay noticia; cierre escalonado por tercios;
    cambio de lado en una sola orden al llegar al objetivo del corto; y **si el término cambia, se cierra**.

## 4. Lo que el método exige y casi nunca se escribe en un libro

- **Vender el rechazo, no la figura.** La entrada buena es cuando el precio ya cayó bajo la MA 20 tras
  rechazar el máximo, no cuando aparece el doji.
- **Nunca comprar dentro del rango.** «No voy a abrir dentro del rango en ningún lugar»: solo ruptura o
  absorción en el borde.
- **Prohibido vender en el hueco.** Si ya hay masa en corto, se espera el rebote al nivel para vender con
  ventaja.
- **La media no es objetivo.** Fijar un objetivo contra la EMA 200 no es recomendable porque la media se
  recalcula: en seis horas está en otro sitio.
- **El stop no es un número suelto:** es una línea («si hay ruptura de esa línea, cierro y revierto»).
- **La probabilidad se descarta por riesgo.** Su modelo puede dar 81 %, pero si la etiqueta es «alto
  riesgo» se queda en 33 % y con ese residuo solo se permite un lado.

## 5. Dónde falla el propio método (leer antes de aplicarlo)

1. **Se contradice en el número.** La misma llamada de Bitcoin aparece como **77.000–81.000** en el guion
   y **73.000–81.000** en la locución del mismo vídeo (26/10). El «81.500» de los títulos **no se dice ni
   una vez** en las clases.
2. **Da niveles sin stop.** Varias predicciones documentadas no llevan invalidación explícita; sin stop no
   hay operación, solo opinión.
3. **La precisión intradía depende del gráfico vivo.** Niveles al centavo (213,08 / 219,19 / 209,95) solo
   son reproducibles con el chart abierto y el detalle de 1 minuto; desde el resumen son referencias, no
   órdenes.
4. **El vocabulario propio no está definido.** «Ley quero» y «unidad 12» se usan como si fueran estándar;
   nadie fuera de su aula puede verificar qué son sin sus clases.
5. **El acierto de nivel no equivale a acierto de escenario.** En Bitcoin acertó los dos extremos del
   rango y aun así la tesis de rango se rompió por abajo (ver `predicciones.md`).

## 6. Cómo se juzga

`predicciones.md` recoge cada predicción con objetivo numérico y la contrasta con el precio real. Ese
documento es el que decide si una regla de este método se adopta o se descarta; la frecuencia sola no
basta, porque algo puede repetirse diez veces y estar mal diez veces.

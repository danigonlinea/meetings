---
title: "Análisis técnico: índice de la carpeta"
date: 2026-11-05
type: reference
category: finance
tags: [analisis-tecnico, indice, metodo, trading]
status: living
---

# Análisis técnico — cómo funciona esta carpeta

Cuerpo **independiente** dentro de `finance/`. No se cruza con `finance/la-pizarra-de-andres/`,
`finance/myinvestor-webinars/` ni con `finance/portfolio/`: aquí no se decide ninguna cartera, no se
mide ningún fondo y no se mezclan conclusiones con el corpus fundamental. La única regla compartida es
la de siempre: **ninguna cifra sin respaldo en la transcripción o en el precio real**.

```
finance/analisis-tecnico/
├── videos/     una carpeta por clase: YYYY-MM-DD-<slug>/ con transcript.json + .txt + summary.md
└── reports/    lo que se deduce de las clases (esta carpeta)
```

## Los tres informes

| Fichero | Qué responde | Se actualiza |
|---|---|---|
| `glosario.md` | Qué significa cada término que usa el autor, con la clase y el minuto donde aparece | Al añadir clases con vocabulario nuevo |
| `metodo.md` | El patrón de análisis completo, regla a regla, con la frecuencia que respalda cada una | Al añadir clases; es el documento de trabajo |
| `predicciones.md` | Cada predicción con su nivel, su condición y **qué pasó de verdad** en el precio | Al vencer cada horizonte |
| `revision-adversarial.md` | Si el método aguanta: pruebas con datos de sus dos reglas centrales, errores de concepto y qué se queda y qué se descarta | Al añadir reglas o cerrar una muestra |

## Estado del corpus

- **10 clases** (26/10/2026 – 04/11/2026) de las dos series del canal: «Nvidia, Trading Salvaje» y
  «Bitcoin Anticipation».
- **1 clase de referencia** anterior (09/08/2024), la de los cinco modelos de aperturas y cierres.
- **4 piezas explicativas** (24 y 29/10/2026): tercios operativos, ley de polaridad, leyes estelares y
  «delta neutral». Son guiones comerciales de 6-10 min, pero contienen las definiciones que las clases
  dan por sabidas — y uno de ellos comete un error de categoría documentado en la revisión.
- Todas sin etiquetas de hablante: se atribuyen a Jesús Navarrete.
- Transcripciones automáticas con errores sistemáticos en las cifras (documentados en cada `summary.md`).

## Cómo se usa

1. Para **aplicar** el método: `metodo.md` §3 (checklist) es el orden de trabajo.
2. Para **entender** un término: `glosario.md`.
3. Para **juzgar** si el método acierta: `predicciones.md`, que separa lo que se cumplió de lo que no.
4. Para el detalle de una sesión concreta: el `summary.md` de su carpeta en `videos/`.

## Reglas de esta carpeta

- Una clase, una carpeta. No se reescribe un `transcript.json`.
- Los informes se reescriben en su sitio (son vivos); el detalle histórico queda en git.
- **Lo que se repite no se da por bueno porque se repita:** se marca su frecuencia y se contrasta con el
  precio real. Una regla que aparece en 9 de 10 clases y falla en los datos se escribe como fallo.
- No se importan conclusiones de otras carpetas de `finance/`.

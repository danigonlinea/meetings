---
title: "Auditoría de los 62 resúmenes de La Pizarra de Andrés (mayo–octubre 2026)"
date: 2026-11-14
type: revision
category: finance
tags: [auditoría, resúmenes, la-pizarra-de-andres, fidelidad]
status: final
---

# Auditoría de la ingesta de mayo a octubre de 2026

Revisión de la tanda de 62 vídeos de `finance/videos/la-pizarra-de-andres/` (2026-05-14 a
2026-10-06) descargada el 2026-11-14. Los resúmenes se escribieron por lotes contra
`transcript.json`; esta revisión comprueba lo que un resumen puede falsear sin que se note.

## Qué se comprobó

| Comprobación | Método | Resultado |
| --- | --- | --- |
| Secciones obligatorias | Búsqueda de las 10 secciones del orden de `ingest-meeting` + las 2 de `ingest-channel` en los 62 archivos | 62/62 completos |
| Frontmatter | Primera línea `---` y claves `title`/`date`/`type`/`category`/`tags`/`status`/`source` | 62/62 |
| Palabras corruptas | `grep -n -E '[a-zñáéíóú]+(recently|developer|Opinions|Escape|imagin es|irmado)[a-zñáéíóú]*'` | 0 coincidencias |
| Cifras sin respaldo | Extracción de los números de `## Conclusiones para el inversor`, `## Tips para el inversor` y `## Fondos y acciones mencionados` (sin minutos) y búsqueda en el texto del transcript | 9 avisos en 9 carpetas; 1 error real corregido, el resto son años de contexto o decimales que el audio dice con palabras |
| Coherencia con `tools/verify.py` | Ejecución completa | 0 errores; solo `INDEX.md` desactualizado (regenerado) y 2 avisos preexistentes de transcripciones pegadas |

## Correcciones aplicadas

- `2026-08-30-la-inflacion-vuelve-a-amenazar-tus-inversiones-actualidad`: el resumen decía «el crudo
  por encima de 80»; el audio dice **entre 83 y 88 dólares** y que le gustaría verlo «en los 70 y
  pico». Corregido en dos viñetas (ideas y conclusiones). El 80 era una paráfrasis del agente, no
  un dato del hablante.

## Falsos positivos revisados (no se tocan)

- `2026-07-31`: «5,5 %» y «28,5 %» salen de «el 5 y medio por ciento» y «un 28 y medio» en el audio.
- `2026-05-19`: «13F» es el formulario de la SEC, no una cifra.
- Años de contexto (2021, 2024, 2025, 2008, 1999) usados para enmarcar una acción o una comparación;
  no se presentan como cifra del hablante.

## Riesgos abiertos

- **Sin etiquetas de hablante** en los 62 transcripts: todos los turnos de entrevista van marcados
  `(inferida)` y las conclusiones nombran al hablante solo cuando el audio lo presenta literalmente.
- **Nombres con ASR corrupto** quedan `no verificado` en cada resumen y con su variante en
  `reference/glossary.md`: Nicolás Sinás/Ginás, HWK/ISTIS, Brightgate/Bright Capital, ISAIS.
- `2026-07-14` (Jornadas, 6 h 20): la estructura por ponencias se reconstruyó desde las
  presentaciones de Andrés y los minutos de `segments`, no desde capítulos (el JSON no los trae).
- `2026-09-10`: la pista de subtítulos es una traducción automática al inglés; las citas van
  marcadas como traducción, no como literales del hablante.

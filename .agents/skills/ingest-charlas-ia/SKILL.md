---
name: ingest-charlas-ia
description: Usar cuando el usuario pida ingerir una charla de AI Engineer (eventos NYC 2026 o Code Summit 2026) o "las nuevas de @aiDotEngineer". El catálogo `ai/ai-engineer/catalogo.md` manda qué falta; el resumen es técnico y no lleva tips de inversión.
---

# Ingesta de charlas de AI Engineer

## Metadatos

- Solo este repositorio, `investing-meetings`.
- Fuente: canal `AI Engineer` (`UCLKPca3kwwd-B59HNr-_lvA`, `@aiDotEngineer`).
- Catálogo y estado: `ai/ai-engineer/catalogo.md`, generado por `python3 tools/aie_talks.py catalogo`.
- Carpetas: `ai/ai-engineer/YYYY-MM-DD-<slug>/`.
- Dependencias: `uv` + `ytpipe` (`ytpipe/`), skill `ingest-meeting` (frontmatter y convenciones).

Cubre dos eventos: **AIE NYC 2026** (playlists `PLLKkCXQeuCis`, `PLVanfCmVOgIg`, `PLPrARbQ6iscE`)
y **AIE CODE 2026** (`PLZUQJ1aon-40`, `PLbhiZl98JSQI`). Otras playlists del canal (World's Fair,
Shanghai, tracks sueltos) están fuera del catálogo: si el usuario las pide, se añaden en
`FUENTES` de `tools/aie_talks.py`, no a mano.

## Paso 1: Decide qué charla

```bash
python3 tools/aie_talks.py pendientes   # TSV: id, fecha, evento, título
```

- Si el usuario nombra una charla o pasa una URL, esa.
- Si no, la más reciente por fecha (el TSV ya viene ordenado) — pero **confirma con el usuario**
  antes de descargar más de una.
- Salta siempre lo que ya tenga `transcript.json`; la comparación es por `source.video_id`, nunca
  por título.

## Paso 2: Descarga

```bash
uv run --project ytpipe ytpipe fetch <url> --out ai/ai-engineer --no-open
```

- Una charla cada vez: YouTube responde 429 en paralelo.
- Sin pista de subtítulos: se reporta y se salta. No se resume de memoria.
- No se edita nunca `transcript.json`.

## Paso 3: Resumen

Aplica `ingest-meeting` para el frontmatter y las convenciones, con estas diferencias:

- `category: ai`.
- Sin las secciones de inversión (`## Conclusiones para el inversor`, `## Tips para el inversor`,
  `## Fondos y acciones mencionados`).
- En su lugar, después de `## Resumen ejecutivo`:

| Sección | Qué contiene |
| --- | --- |
| `## Tesis de la charla` | La afirmación central del ponente, en sus palabras. |
| `## Técnicas y decisiones` | Qué construyó, con qué piezas y por qué. Una viñeta por decisión. |
| `## Cifras del hablante` | Tabla: cifra, qué mide, minuto. Solo lo que está en la transcripción. |
| `## Límites que reconoce` | Lo que el ponente dice que no funciona, no escala o no ha probado. |

- Cada afirmación se atribuye por nombre cuando el ponente está identificado en el título o en la
  descripción; si la transcripción no trae etiquetas de hablante, se marca `no atribuible con
  certeza`.
- Las cifras de rendimiento (`latencia`, `tokens`, `%`) se copian con la unidad que dice el
  hablante. Nada de aritmética propia.
- Marca cada inferencia con la palabra `inferida`.

## Paso 4: Cierra

```bash
python3 tools/aie_talks.py catalogo      # la charla pasa a "ingerida"
python3 tools/build_index.py
python3 tools/verify.py
git add -A && git commit -m "Ingerir <charla>" && git push
```

## Guardarraíles

- No descargar el catálogo entero: 131 charlas son backlog, no una tanda.
- No tocar carpetas de otras fuentes.
- Nada de cifras ni citas que no estén en la transcripción.
- Si el catálogo no cuadra con las carpetas, `verify.py` falla: se regenera el catálogo, no se
  edita a mano.

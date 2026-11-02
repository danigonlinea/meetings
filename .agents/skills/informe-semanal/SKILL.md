---
name: informe-semanal
description: Usar cuando corra la revisión semanal de canales (cron del agente cloud) o cuando el usuario pida "qué hay nuevo esta semana" en La Pizarra de Andrés y MyInvestor. Ingiere lo nuevo, escribe el informe semanal con candidatos para la cartera, lo commitea y resume en 5 líneas.
---

# Informe semanal

## Metadatos

- Se ejecuta **sin preguntar nada**. Si algo no cuadra, para y repórtalo.
- Canal principal: `La Pizarra de Andrés`, ID `UCEXbEm8RUvRkKUEo2RjKd9w`.
  `@LaPizarradeAndrésLive` es otro canal: no se ingiere.
- Webinars: `finance/myinvestor-webinars/`, catálogo generado por
  `python3 tools/myinvestor_webinars.py`.
- Salida: `finance/reports/informe-semanal-YYYY-MM-DD.md`, `type: synthesis`.
- Dependencias: `yt-dlp`, `uv` + `ytpipe`, skill `ingest-meeting`, skill `ingest-webinars`.

## Límites duros

- **Máximo 3 piezas por ejecución** (1 del canal + 2 webinars, o 3 vídeos). En serie: YouTube
  responde 429 en paralelo.
- Nada de `--force`. Un `transcript.json` existente no se toca.
- **No se edita `finance/portfolio/propuesta-actual.md` ni se dan órdenes.** El informe propone
  candidatos; la cartera la decide el dueño.
- Una pieza sin subtítulos se salta y se anota; no se resume de memoria.
- La ausencia de novedades es un resultado válido: el informe se escribe igual, con "sin novedades".

## Paso 1: Sincroniza

```bash
git pull --rebase
```

Si falla, para: hay trabajo local sin subir y el rebase lo pisaría.

## Paso 2: Descubre qué falta

```bash
python3 tools/nuevos.py --canal 10
```

Devuelve los IDs del canal que no están en ningún `transcript.json` y los webinars pendientes.
Compara **siempre por ID**, nunca por título.

## Paso 3: Descarga, en serie

```bash
uv run --project ytpipe ytpipe fetch "https://www.youtube.com/watch?v=<id>" \
  --out finance/la-pizarra-de-andres --slug "<tema>" --no-open
```

- El `--slug` sale del título **real** que imprime `ytpipe` (en español), no del título del listado.
- Webinars: `--out finance/myinvestor-webinars` y la skill `ingest-webinars`.
- Clasifica `ai` o `finance` por el tema del vídeo; no preguntes.

## Paso 4: Resume

Aplica `ingest-meeting` a cada carpeta nueva. Ya incluye `## Fondos y acciones mencionados` con
ISIN, clase, comisión, cifra del hablante, postura y minuto.

## Paso 5: Completa las fichas con datos públicos

Para cada vehículo mencionado, en este orden:

| Dato | Fuente | Nota |
| --- | --- | --- |
| ISIN, gestora, categoría, política | CNMV (fondos españoles) o quefondos por ISIN | quefondos responde sin login: `https://www.quefondos.com/es/fondos/ficha/legal.html?isin=<ISIN>` |
| Comisión fija, variable, depósito, **suscripción y reembolso** | quefondos, pestaña «Información legal» | Son las comisiones del fondo, no las de la plataforma |
| Ticker, precio, PER | Yahoo Finance | Para acciones |
| ¿Está en el catálogo de MyInvestor? ¿Qué aplica la plataforma? | **MCP de MyInvestor en local** | El cloud no lo tiene: escribe `no verificado` y márcalo como pendiente |

Reglas:

- `suscripción` y `reembolso` son lo que el usuario pregunta cuando dice «comisiones»: no las omitas.
- Si el fondo no está en MyInvestor, dilo: un candidato que no se puede comprar no es candidato.
- Sin dato → `no verificado`, nunca un número inventado.

## Paso 6: Encaje en la cartera

Lee `finance/portfolio/cartera-myinvestor/cartera-actual.md` y `propuesta-actual.md` (§4, §5, §8,
§10). Para cada candidato escribe:

| Candidato | ISIN | Clase de activo | Solape con la cartera | Coste (TER + entrada/salida) | Encaje | Qué habría que quitar |
| --- | --- | --- | --- | --- | --- | --- |

- **Solape**: compara geografía y sector con los fondos que ya tiene (Rock + 8 manuales).
- **Encaje**: di si cubre un hueco real (geografía, factor, duración) o si duplica.
- **Qué habría que quitar**: si no cabe sin vender algo, dilo. Un candidato que exige vender es una
  decisión, no una mejora gratis.
- Comprueba las señales del §10 con `python3 tools/termometro.py`. Si ninguna cruza su umbral,
  escribe que la cartera no se toca esta semana.

Prohibido: `recomienda` sobre un vehículo, cualquier cifra de rentabilidad futura y modificar la
propuesta. El informe es análisis, no asesoramiento.

## Paso 7: Escribe el informe

`finance/reports/informe-semanal-YYYY-MM-DD.md`:

```yaml
---
title: "Informe semanal — <fecha>"
date: YYYY-MM-DD
type: synthesis
category: finance
tags: [informe-semanal, candidatos, cartera]
status: final
---
```

Secciones, en este orden:

1. **Qué se ha ingerido** — tabla: fecha, fuente, título, minuto de la idea principal.
2. **Lo importante de la semana** — 5-8 viñetas. Solo lo que cambia una decisión, con hablante y minuto.
3. **Fondos y acciones mencionados** — tabla agregada con ISIN, comisiones de suscripción y reembolso, postura.
4. **Candidatos para la cartera** — la tabla del Paso 6 y una frase de veredicto por candidato.
5. **Señales de la cartera** — salida del termómetro y si algún umbral cruzó.
6. **Pendiente de verificar en local** — lo que el cloud no puede comprobar (catálogo MyInvestor, comisión de plataforma).
7. **Sin novedades** (si no hubo nada) — una línea.

## Paso 8: Cierra y sube

```bash
python3 tools/myinvestor_webinars.py catalogo   # solo si tocaste webinars
python3 tools/build_index.py
python3 tools/verify.py                          # si falla, no se sube
git add -A && git commit -m "Informe semanal YYYY-MM-DD"
git push                                         # si lo rechaza: git pull --rebase y repetir
python3 tools/verify.py --git
```

## Paso 9: Informa

- Si hay canal de mensajería configurado (Telegram/Slack), envía el resumen de 5 líneas con el
  enlace al informe del repositorio.
- Si no lo hay, el informe vive en el repo y la sesión del agente cloud queda en la app de Hermes:
  escribe igualmente las 5 líneas como respuesta final, que es lo que se guarda en la sesión.

Formato del resumen:

```text
Semana <fecha>: N piezas ingeridas (X canal, Y webinars), 0 fallos.
Lo importante: <una frase>.
Candidatos: <nombres con ISIN o "ninguno">.
Cartera: <"sin cambios" o la señal que cruzó>.
Commit: <hash>.
```

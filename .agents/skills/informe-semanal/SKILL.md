---
name: informe-semanal
description: Usar cuando corra la revisión semanal de canales (cron del agente cloud) o cuando el usuario diga "haz lo tuyo" o pida "qué hay nuevo esta semana" en La Pizarra de Andrés y MyInvestor. Ingiere lo nuevo, escribe el informe semanal con candidatos para la cartera, lo commitea y resume en 5 líneas.
---

# Informe semanal

## Metadatos

- Se ejecuta **sin preguntar nada**. Gestiona los fallos de consulta según el Paso 2.
- Canal principal: `La Pizarra de Andrés`, ID `UCEXbEm8RUvRkKUEo2RjKd9w`.
  `@LaPizarradeAndrésLive` es otro canal: no se ingiere.
- Webinars: `finance/videos/myinvestor-webinars/`, catálogo generado por
  `python3 tools/myinvestor_webinars.py`.
- Salida: `finance/reports/informe-semanal-YYYY-MM-DD.md`, `type: synthesis`. La carpeta se crea con
  `mkdir -p finance/reports` antes de escribir; el 14/11/2026 se vació y no debe darse por existente.
- Dependencias: `yt-dlp`, `uv` + `ytpipe`, skill `ingest-meeting`, skill `ingest-webinars`.

## Límites duros

- **Solo lo nuevo.** Se ingiere lo que devuelve `python3 tools/nuevos.py`: vídeos publicados
  **desde** la última transcripción ingerida (misma fecha incluida, sin repetir por ID). El backlog
  antiguo (140 webinars de 2023-2025) **no es nuevo** y no se toca en la pasada semanal; si el dueño
  quiere cerrarlo, es un encargo aparte.
- **Máximo 3 piezas por ejecución.** En serie: YouTube responde 429 en paralelo.
- Nada de `--force`. Un `transcript.json` existente no se toca.
- **Referencia de cartera en solo lectura:** usa únicamente
  `finance/portfolio/cartera-myinvestor/cartera-actual.md`. El informe identifica candidatos;
  los cambios y las órdenes los decide el dueño.
- Una pieza sin subtítulos se salta y se anota; no se resume de memoria.
- Si una semana no hay nada publicado, **no se escribe informe ni se commitea**: se responde el
  resumen de 5 líneas con "sin novedades" y se termina. El repo no se llena de ficheros vacíos.

## Paso 1: Sincroniza

```bash
git pull --rebase
```

Si falla, para: hay trabajo local sin subir y el rebase lo pisaría.

## Paso 2: Descubre qué falta

```bash
python3 tools/nuevos.py            # --help: --dias N (ventana si no hay ingesta previa), --json, --backlog
```

Devuelve las piezas de cada fuente publicadas **desde la fecha de su última ingesta**, con fecha,
ID y enlace. Compara por ID. Si una fuente falla, usa los resultados de la otra y anota el fallo
en el informe y en el resumen de cinco líneas. Si ninguna devuelve piezas y hay un fallo,
reporta la consulta incompleta en el resumen de cinco líneas.

Si devuelve "Sin novedades", no escribas informe ni toques el repositorio: da el resumen de 5
líneas con "sin novedades" y termina.

## Paso 3: Descarga, en serie

```bash
CARPETA_TEMPORAL_INGESTA=$(mktemp -d)
uv run --project ytpipe ytpipe fetch "https://www.youtube.com/watch?v=<id>" \
  --out "$CARPETA_TEMPORAL_INGESTA" --slug "<tema>" --lang es --no-open
```

- El `--slug` sale del título **real** que imprime `ytpipe` (en español), no del título del listado.
- **Comprueba `source.language_code` antes de guardar.** Para vídeos en español, descarga
  primero en una carpeta temporal con `--lang es`. Si sale otro idioma, consulta
  `ytpipe languages <url>`. Mueve la carpeta completa a la ruta de la fuente únicamente cuando
  la pista sea la correcta y el destino esté libre. Si no hay pista en español, anótalo y salta la pieza.
- Webinars: `--out finance/videos/myinvestor-webinars` y la skill `ingest-webinars`.
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

Lee `finance/portfolio/cartera-myinvestor/cartera-actual.md`. Para cada candidato escribe:

| Candidato | ISIN | Clase de activo | Solape con la cartera | Coste (TER + entrada/salida) | Encaje |
| --- | --- | --- | --- | --- | --- |

- **Solape**: compara geografía y sector con las posiciones que recoge la foto.
- **Encaje**: di si cubre un hueco real (geografía, factor, duración) o si duplica.
- Si un hecho de la semana afecta a una posición de la foto, indica la posición y la fuente.
  La revisión de la estrategia y del % de RV queda en local.

Describe el encaje con los datos disponibles. Evita recomendar compras o ventas y dar cifras de
rentabilidad futura.

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

1. **Qué se ha ingerido** — tabla: fecha, fuente, título, minuto de la idea principal. Indica si falló una fuente.
2. **Lo importante de la semana** — 5-8 viñetas. Solo lo que cambia una decisión, con hablante y minuto.
3. **Fondos y acciones mencionados** — tabla agregada con ISIN, comisiones de suscripción y reembolso, postura.
4. **Candidatos para la cartera** — la tabla del Paso 6 y una frase de veredicto por candidato.
5. **Cartera de referencia** — hechos que afectan a posiciones de la foto, si los hay.
6. **Pendiente de verificar en local** — lo que el cloud no puede comprobar (catálogo MyInvestor, comisión de plataforma).

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
Semana <fecha>: N piezas ingeridas (X canal, Y webinars), <fallos si los hay>.
Lo importante: <una frase>.
Candidatos: <nombres con ISIN o "ninguno">.
Cartera: <hecho que afecte a una posición de la foto, o "sin novedades">.
Commit: <hash>.
```

# AGENTS.md

Enrutado para agentes. Repositorio `investing-meetings`: transcripciones, resúmenes y análisis
de inversión (`finance/`) e IA (`ai/`).

**Orden de lectura: este archivo → `INDEX.md` → el artefacto concreto.** Si el tema es la
cartera, añade `finance/portfolio/README.md` como cuarto paso.

## 1. Enrutado

| Pregunta del usuario | Ruta | Empezar por |
| --- | --- | --- |
| Su cartera, rebalanceo, traspasos, "¿qué hago con mi dinero?" | `finance/portfolio/` | El `README.md` de la carpeta y luego `cartera-actual.md` → `propuesta-actual.md` |
| Cartera de MyInvestor (manual + Rock) | `finance/portfolio/cartera-myinvestor/` | `propuesta-actual.md` |
| Cartera de Renta 4 Banco | `finance/portfolio/cartera-renta4/` | `propuesta-actual.md` |
| Un fondo, ETF o acción que tiene o le han recomendado | `finance/portfolio/` | Su ficha en el `cartera-actual.md` de la carpeta que lo tenga, luego los `summary.md` que lo nombran |
| Macro, tipos, inflación, renta fija, mercados | `finance/la-pizarra-de-andres/` | `summary.md` más reciente del tema |
| Gestoras, entrevistas, "qué dice MyInvestor" | `finance/myinvestor-webinars/` | `catalogo.md` → carpeta del webinar → `summary.md` |
| Visión consolidada o discrepancias entre vídeos | `finance/reports/` | `informe-canal-*` y `sintesis-inversor-*` |
| Agentes de IA, LLMs, Claude | `ai/dev-docs-explained/` | `summary.md` del vídeo |
| Nombre de una persona, canal o entidad | `reference/glossary.md` | Tabla de ponentes |
| Terminología (IA o finanzas) | `reference/glossary-technical.md` | — |
| Revisión trimestral de la cartera, "¿toca cambiar el % de RV?" | `finance/portfolio/` | `propuesta-actual.md` §2 y §10 → `python3 tools/termometro.py` |

Las dos carteras son independientes: no se suman, ni se comparan, ni se rebalancea una contra la otra.

Si la pregunta cruza `finance/` y `ai/` (p. ej. "¿la burbuja de la IA afecta a mi cartera?"),
responde desde `finance/` y usa `ai/` solo como contexto.

Cada vídeo o reunión es una carpeta `YYYY-MM-DD-<slug>/` con `transcript.json` (fuente de
verdad, nunca se reescribe), la transcripción `.txt` y el `summary.md` que se entrega.
Nombres de carpeta, frontmatter YAML y comandos: `README.md`.

## 2. Reglas que no se negocian

- **`git pull --rebase` antes de tocar nada.** El agente cloud commitea en `main`; sin pull, el
  trabajo local choca. Es el paso 0, no una recomendación.
- **Ninguna cifra sin respaldo** en la transcripción. Sin dato del hablante, el criterio va sin número.
- **Ninguna atribución inventada**: sin etiquetas de hablante, marca `inferida` o `no atribuible con certeza`. Un nombre solo entra si es el presentador del canal, un invitado nombrado o un fondo/gestora nombrados literalmente (ver la regla de atribución de `reference/glossary.md`).
- **Una mención no es una recomendación**: `recomienda` exige cita literal; si el hablante vende el producto, `(lo comercializa)` en la misma fila.
- **Hedges y magnitudes se conservan** ("si no me equivoco", `trillion` = billón).
- Cada tip pertenece a su hablante: el agente no da consejo financiero.
- Tras crear, mover o borrar artefactos: `python3 tools/build_index.py`.

## 3. Skills

- `ingest-meeting` — llega una transcripción y falta `summary.md`. Define las secciones del resumen.
- `ingest-channel` — "los últimos N vídeos de un canal" o un informe de canal.
- `ingest-webinars` — webinars o entrevistas de MyInvestor (lista el catálogo y salta lo ya ingerido).
- `revision-cartera` — revisión trimestral: mide las señales, corre el termómetro y escribe la
  revisión. No decide el % de RV.
- `informe-semanal` — la pasada semanal del agente cloud: descubre, ingiere, escribe el informe con
  candidatos y sube. No pregunta nada.

Las tres primeras escriben en `<categoria>/<fuente>/YYYY-MM-DD-<slug>/` y reutilizan `ingest-meeting`.

## 4. Más detalle

| Archivo | Contiene |
| --- | --- |
| `README.md` | Mapa completo, convenciones de nombres, frontmatter, comandos |
| `INDEX.md` | Todos los artefactos, con ruta, tipo, categoría, fecha, título y tags |
| `finance/portfolio/README.md` | Las dos carteras y sus reglas; cada subcarpeta tiene su propio `README.md` |
| `ytpipe/README.md` | Formato de `transcript.json` y opciones del CLI |

## 5. Definición de hecho

Ningún trabajo está terminado hasta que estas cuatro cosas pasan, en este orden:

```bash
git pull --rebase                # 0. sincroniza con el cloud antes de nada
python3 tools/build_index.py     # 1. índice regenerado
python3 tools/verify.py          # 2. contenido válido (carpetas, resúmenes, frontmatter, catálogo)
git add -A && git commit -m "…"  # 3. commit en imperativo
git push                         # 4. subido
python3 tools/verify.py --git    # árbol limpio y nada sin subir
```

- Si `verify.py` da error, **no se sube**: se arregla o se deja escrito qué falta.
- Los avisos (⚠️) no bloquean: un `summary.md` sin `transcript.json` es una transcripción pegada.
- `INDEX.md` y `catalogo.md` son generados: nunca se resuelven a mano, se regeneran.

## 6. Reparto local / agente cloud

El agente cloud corre 24/7 sobre estos repositorios; esta máquina hace lo que necesita
credenciales, dispositivo o juicio del dueño.

| Trabajo | Dónde | Motivo |
| --- | --- | --- |
| Ingesta de vídeos, webinars, resúmenes, informes de canal, `INDEX.md` | **Cloud** | No pregunta nada, no usa credenciales, es append-only |
| Código de `brisadeconil`, `tinytasste`, `food-recipes-database` | **Cloud** (rama + PR) | El merge a `main` se queda en local |
| Firma Android, Play Console, keystore, emulador, Firebase SA | **Local** | Credenciales y hardware |
| Revisión de cartera, termómetro, órdenes | **Local** | MCP de datos + decisión del dueño |
| Merge a `main` de repos de código | **Local** | Gate humano |

**Excepción de este repositorio:** es datos y documentación, no código desplegable, así que el
agente cloud **empuja directo a `main`**. El resto de repos van por rama y PR.

### Pasada semanal (agente cloud)

El procedimiento completo está en `.agents/skills/informe-semanal/SKILL.md`: sincronizar, descubrir
con `python3 tools/nuevos.py`, ingerir 1-3 piezas en serie, resumir, completar fichas, comparar con
la cartera, escribir el informe, verificar y subir. No se duplica aquí.

Identidades de las fuentes:

| Fuente | Identificador |
| --- | --- |
| La Pizarra de Andrés (la que se ingiere) | canal `UCEXbEm8RUvRkKUEo2RjKd9w` |
| La Pizarra de Andrés Live | canal `UCDpE0dCtPTJZKAr8psiAHQw` — **no se ingiere** |
| MyInvestor | `https://blog.myinvestor.es/escuelamyinvestor/webinars/` |

Límites: nada de cartera desde el cloud; nada de merge a `main` en repos de código; una pieza sin
subtítulos se salta y se reporta, no se resume de memoria.

### Entrega del informe

Sin canal de mensajería configurado, un cron del cloud corre en silencio. Hoy no hay ninguno
conectado: el informe queda en `finance/reports/` y la sesión del agente se lee en la app de Hermes.
Para recibirlo como mensaje hay que conectar Telegram (o Slack) en esa instancia; entonces la skill
`informe-semanal` envía el resumen de 5 líneas.

## 7. Cuándo una señal de cartera obliga a revisar

El termómetro avisa; la decisión es del dueño. Los umbrales están en `propuesta-actual.md` §10 y los
calcula `python3 tools/termometro.py`. La revisión se escribe con la skill `revision-cartera`.

---
name: cribado-acciones
description: Usar cuando el dueño pida buscar, cribar o listar acciones para invertir (por dividendo, calidad, múltiplo, país o "60-100 candidatas"). Barre el universo global, verifica dividendo = 0 y devuelve una tabla con nivel A/B y las fuentes usadas.
---

# Cribado de acciones

## Cuándo se usa

- «Hazme una lista de N acciones que cumplan X» / «busca ideas de compra».
- «¿Qué acciones sin dividendo hay?» / «amplía el universo de `propuesta-acciones.md`».
- Antes de escribir una ficha de 10 puntos: el cribado es el embudo, la ficha es la decisión.

## Reglas duras (no se negocian)

1. **Dividendo = 0, sin excepciones.** Es la regla de `finance/portfolio/README.md` y el dueño la
   confirmó el 05/11/2026: «company stock that distribute dividends stay out of the analysis». Se
   verifica **en dos fuentes** (ficha + histórico de eventos) y se escribe en la tabla el resultado.
   Un rendimiento del 0,3 % también descalifica.
2. **Una mención no es una recomendación y un cribado no es una cartera.** La tabla es el embudo; la
   cartera vive en `propuesta-acciones.md` y solo cambia cuando el dueño lo decide.
3. **Nada de cifras de memoria.** Cada número sale de las fuentes de abajo, con fecha.
4. **El resultado se escribe dentro de `propuesta-acciones.md`** (una sección `§9 Universo cribado`),
   nunca en un fichero nuevo: la carpeta rechaza documentos paralelos.

## Fuentes que funcionan (verificadas el 05/11/2026)

| Fuente | Qué da | Cómo se llama | Fiabilidad |
|---|---|---|---|
| **stockanalysis.com** `/stocks/<TICKER>/statistics/` | ROE, márgenes, crecimiento 3A de consenso, PER forward, PS, PB, FCF, variación 52s, **Dividend Yield** (`n/a` = no reparte) | HTTP desde el navegador (`browser_exec`); el HTML viene renderizado en servidor, no hace falta JS de terceros | Alta. Es la única que he visto dar ficha completa gratis de miles de tickers |
| **stockanalysis.com** `/_api/endpoints/screener/initial?type=stock&countryCode=XX&format=compact` | Universo: símbolo, nombre, capitalización, precio, cambio del día, industria, PER trailing. `countryCode=US` devuelve **todo el mundo** (5.601 filas); otros códigos filtran mal o no filtran | `fetch` desde la propia página de stockanalysis (mismo origen) | Alta para el universo; los `countryCode` distintos de US **no son fiables** |
| **Yahoo Finance** `query2.finance.yahoo.com/v8/finance/chart/<T>?range=3y&interval=1mo&events=div` | **Eventos de dividendo** (0 = no reparte), precio, máximo/mínimo 52 semanas, divisa y plaza en `meta` | `fetch` desde una pestaña de `finance.yahoo.com` (CORS: **solo** desde su propio origen) | Alta para precios y dividendos. `quoteSummary` (fundamentales) **requiere crumb válido y falla** («Invalid Crumb»): no perder tiempo con él |
| **MCP `yahoo-finance`** (ya instalado) | Cotización, histórico, dividendos, splits de un ticker; sirve para verificar 2-3 nombres a mano | `mcp__yahoo_finance__*` | Alta. Bueno para fichas puntuales, **no** para barrer cientos de nombres |
| **web_search / web_extract** | Noticias del día, contexto de la caída, contraste | — | Para el «por qué», no para el dato |

**Nada de esto existe como MCP.** No hay MCP de stockanalysis ni de cribadores; el trabajo en bloque se
hace con navegador. Los MCP financieros útiles que sí existen están en la skill `finance-mcp-catalog`:
`yahoo-finance` (instalado) y **FRED** (gratis con key) para macro: tipos, inflación y **HY OAS**, que
es justo la señal que `propuesta-actual.md` §11 usa para mover el % de RV.

## Receta (la que funcionó)

1. **Universo.** Abrir `https://stockanalysis.com/stocks/screener/` y desde la consola de la página:
   ```js
   fetch('/_api/endpoints/screener/initial?type=stock&countryCode=US&format=compact')
   ```
   Devuelve `data.rows = [symbol, name, marketCap, price, change, industry, volume, peRatio]`.
   **No acepta columnas ni límites**: `c` y `cn` se ignoran, siempre llegan las 5.601 filas.
2. **Embudo barato en Python.** Capitalización ≥ 5.000 M$ y `0 < PER ≤ 60` → ~1.080 nombres.
   Nunca se piden fichas de los 5.601: son miles de peticiones y el sitio empieza a devolver 429.
3. **Filtro de dividendo (el que manda).** En una pestaña de `finance.yahoo.com`:
   ```js
   fetch('https://query2.finance.yahoo.com/v8/finance/chart/'+sym+'?range=3y&interval=1mo&events=div')
   ```
   `Object.keys(res.events.dividends || {}).length === 0` → no reparte. 6 workers en paralelo van a
   ~2 nombres/s: 700 nombres en ~6 minutos. **CORS:** este `fetch` solo funciona desde el propio
   dominio de Yahoo; desde stockanalysis devuelve «Failed to fetch».
4. **Fichas solo de las que sobreviven.** `/stocks/<T>/statistics/` para las ~170 sin dividendo, con
   `DOMParser` y las filas de la tabla:
   ```js
   for (const tr of doc.querySelectorAll('tr')) { const c=[...tr.children].map(x=>x.textContent.trim()); ... }
   ```
   **Ritmo:** 1 petición cada ~1,1 s y 1-3 workers. Con más velocidad el sitio responde 429 y se pierde
   el lote entero.
5. **Máximos de 52 semanas** (para la caída, que es la medida de «oportunidad»): otra vez el `chart`
   de Yahoo con `range=1y&interval=1d` y `meta.fiftyTwoWeekHigh`.
6. **Niveles.** A = cumple los cinco filtros (ROE > 12 %, margen operativo > 10 %, crecimiento 3A > 5 %,
   PER forward < 35×, FCF > 0). B = falla uno solo y se nombra cuál. La tabla final lleva el nivel en
   su propia columna.
7. **Escribir** la sección en `propuesta-acciones.md` y ejecutar la definición de hecho de `AGENTS.md`
   (`build_index.py`, `verify.py`, commit, push, `verify.py --git`).

## Pitfalls (todos me pasaron)

- **`browser_exec` corta las evaluaciones largas** («WebSocket connection closed», timeout de 5 s en
  `Runtime.evaluate`). Patrón que sí aguanta: arrancar el bucle **en segundo plano dentro de la página**
  (`window.__res`, `window.__done`) y devolver `'ok'` al instante; luego hacer *polling* con llamadas
  cortas a `js()` y **guardar a disco en cada vuelta** (`json.load/dump` del lado Python) para que un
  corte no pierda el lote.
- **El `js()` en primer plano solo es seguro con lotes pequeños** (~20-30 nombres y 5 workers). Uno de
  150 puede devolver datos a medias o morir.
- **La sesión de navegador muere sin avisar** (1001 going away). Cada llamada debe empezar con
  `new_tab(...)`/`goto_url(...)`: un `fetch('/api...')` relativo desde una pestaña vacía devuelve HTML y
  el `JSON.parse` explota con «Unexpected token '<'».
- **Cloudflare bloquea `curl`** en stockanalysis («Just a moment...»), pero **no** al navegador real.
  No pierdas tiempo con `curl` ni con `web_extract` para esto.
- **`countryCode` no filtra bien:** `US` = todo el mundo, `DE` devolvió 13.845 filas (no es Alemania) y
  `GB` devolvió 0. El listado resultante es **cotizadas en EE. UU.**, incluidas ADR; decirlo en la tabla
  en vez de venderlo como «global».
- **El PER forward barato no es una ganga.** Charter salió con 2,6× y es deuda: el cribado no mide
  apalancamiento. Escribirlo en los límites y mirar deuda neta/EBITDA en la ficha.
- **La lista de «sin dividendo» caduca.** Se re-verifica cada vez; Booking figuraba como «no reparte» y
  paga 0,98 %, y PayPal, Alphabet, Meta o Nvidia reparten un simbólico que también descalifica.
- **`browser_vault`/logins:** X y Yahoo muestran muro de login en algunas rutas; el perfil público de X
  sí se lee sin sesión (posts recientes, con «Show more» truncado).

## Salida

Tabla markdown con: `# | Ticker | Compañía | Sector | Cap | PER fwd | ROE | Crec. 3A | Caída 52s | Nivel`,
más una sección de «las diez que se mirarían primero» (nivel A, caída ≥ 25 %, PER fwd < 25×,
crecimiento > 8 %) y los límites del cribado. Cierra siempre con «esto es el embudo, no la ficha».

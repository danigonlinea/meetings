---
title: "Listado de fondos MyInvestor — snapshot de la app"
date: 2026-11-19
type: reference
category: finance
tags: [fondos, myinvestor, listado, snapshot]
status: living
---

# Listado de fondos MyInvestor (snapshot de la app)

**1.980 fondos** parseados de `MyInvestor.html`, la página de búsqueda de fondos de la app
(`newapp.myinvestor.es/app/explore/investments/funds/search`) guardada manualmente por el
titular el 2026-11-19. Es una fuente distinta del catálogo MCP: no hay acceso automatizado
a MyInvestor y el volcado MCP sigue detenido (ver el `README.md` del directorio padre).

- **Base de datos:** [`fondos.json`](fondos.json) — un registro por ISIN con todos los campos
  que publica el listado; lo que falta queda a `null` y listado en `pendientes`.
- **Índice:** [`catalogo.md`](catalogo.md), generado y agrupado por clase, ordenado por TER.
  No editar a mano.
- **Regenerar:** `python3 tools/parsear_listado_myinvestor.py` (lee `MyInvestor.html` de la
  raíz del repo, que no se versiona por tamaño; el JSON parseado sí).

## Campos

Publicados por el listado: nombre, ISIN, tipo (`Fondos de inversión` → gestión activa,
`Fondos Indexados` → indexada), divisa, categoría Morningstar, NAV, rentabilidad 2026 (YTD),
1A, 3A y 5A anualizada, TER, riesgo SRRI (1-7) y rating Morningstar (★ 1-5).

**Pendientes en todos los fondos** (el listado no los publica): gestora, política de
acumulación/distribución, composición, comisión de gestión y de éxito, mínimos, volatilidad,
rentabilidades de años naturales, operativa y fecha del NAV. La columna «Div» de la app es
la **divisa**, no los dividendos.

Pendientes por fondo (nº de fondos afectados): rating 426 · 5A 269 · 3A 152 · 1A 36 ·
YTD 32 · NAV 8 · SRRI 2 · TER 1 · clase 31.

## Calidad del snapshot

La app lista también productos **muertos o moribundos**: fondos liquidados o disueltos
(con hecho relevante en CNMV), ISIN cancelados, NAV congelados con un solo partícipe o
patrimonios residuales tras reembolsos masivos. Se concentran sobre todo en la cola de
TER alto de cada clase (p. ej. varios «mixtos» de TER > 2,5 %). Sus rentabilidades del
listado son residuales de liquidación, no operativas. Las fichas web los marcan como
**no invertibles** con la evidencia CNMV; algunos nombres del snapshot están además
obsoletos (fondos renombrados o absorbidos por otro compartimento).

## Clasificación

Misma regla que la base MCP: tipo de activo declarado; dentro de la bolsa,
sector → global → emergentes → EE. UU. → Japón → Europa → otros. Aquí el dato disponible
es la **categoría Morningstar**, con este mapa explícito:

| Clase | Categorías Morningstar | Fondos |
| --- | --- | --- |
| `monetarios` | Euro/US/Sterling Money Market, Money Market Miscellaneous, DINERO EUROPA | 35 |
| `renta-fija` | Europe/Global/US/Emerging Markets/Asia/Japan/Sterling Fixed Income, Fixed Income Miscellaneous, Convertibles, Renta Fija Flexible | 476 |
| `mixtos` | Flexible/Moderate/Cautious/Aggressive Allocation, Allocation Miscellaneous, Target Date, Guaranteed | 305 |
| `rv-global` | Global Equity Large Cap, Global Equity Mid/Small Cap | 308 |
| `rv-usa` | US Equity Large Cap Blend/Growth/Value, US Equity Mid/Small Cap | 119 |
| `rv-europa` | Europe Equity Large Cap, Europe Equity Mid/Small Cap, UK Equity Large Cap | 198 |
| `rv-japon` | Japan Equity | 28 |
| `rv-emergentes` | Global/Europe Emerging Markets Equity, Greater China, India, Latin America, Africa, Korea, Mexico, Thailand Equity | 148 |
| `rv-otros` | Asia ex-Japan Equity, Asia Equity, Australia & New Zealand Equity | 48 |
| `sectoriales` | Technology, Healthcare, Energy, Financials, Industrials, Infrastructure, Consumer Goods & Services, Natural Resources, Precious Metals, Real Estate Sector Equity, Property-Direct | 213 |
| `alternativos` | Global Macro, Market Neutral, Long/Short Equity/Credit, Multialternative, Alternative Miscellaneous, Options Trading, Commodities Broad Basket/Specified | 71 |
| `pendiente` | Equity Miscellaneous, Miscellaneous, Otros, «-» (sin región/sector declarado) | 31 |

Matices del mapa:

- `alternativos` es una clase nueva de este listado: el MCP solo declaraba RV/RF/Mixto/Monetario,
  pero la categoría Morningstar sí distingue estas estrategias. No se fuerzan dentro de «mixtos».
- `Convertibles` va a renta fija (categoría de renta fija en Morningstar); `Guaranteed` y
  `Target Date` a mixtos; `Property-Direct` a sectoriales (inmobiliario).
- `Europe Emerging Markets Equity` va a emergentes, no a Europa, siguiendo la regla de la base.
- `rv-españa` no tiene categoría Morningstar propia: son fondos de bolsa española (IBEX/nacional)
  detectados por su política de inversión dentro de «Europe Equity Large Cap» (caso inicial:
  BBVA Bolsa Índice, ES0110182039). El catálogo agrupa por la clase efectiva de la ficha.
- Los 31 fondos de `pendiente` tienen tipo de activo conocido pero no región/sector; figuran
  al final del catálogo con sus datos para clasificación manual. No se infiere nada del nombre.

## Relación con las fichas MCP

178 de los 1.980 fondos ya tienen ficha MCP en el directorio padre (de las 205 escritas);
el catálogo enlaza a ella desde el ISIN. Las 27 fichas MCP restantes no aparecen en este
listado de la app. El campo `ficha` del JSON guarda la ruta relativa de la ficha cuando existe.

Las fichas web del resto de fondos se escriben en las carpetas de clase del directorio padre
siguiendo [`plantilla-ficha.md`](plantilla-ficha.md), con datos de quefondos.com y Finect
más el contexto de [`contexto-macro.md`](contexto-macro.md). Progreso y lotes:
`python3 tools/fichas_listado.py estado|siguientes N`.

*Datos de referencia a fecha del snapshot; rentabilidades pasadas no garantizan futuras.
No es consejo de inversión.*

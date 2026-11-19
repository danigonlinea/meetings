# Base de datos de fondos MyInvestor (solo acumulación)

> **Estado: PARCIAL Y DETENIDO (2026-11-19).** 205 fichas de 2.197. El volcado se detuvo al
> alcanzar el límite de uso del MCP: sus [términos](https://mcp.myinvestor.es/terms) prohíben
> el acceso automatizado, la extracción sistemática del catálogo y la construcción de bases de
> datos derivadas, y eludir los límites (p. ej. repartiendo lotes en el tiempo) también está
> prohibido. El titular decidió conservar y versionar estas fichas como referencia personal
> asumiendo ese riesgo. **No reanudar el volcado automatizado** (`lote`, cron, scripts) sin
> permiso expreso de MyInvestor/GPTadvisor (info@gptadvisor.com). El uso conversacional puntual
> del MCP en las revisiones de cartera sigue siendo el uso tolerado.

Fichas markdown de los fondos del catálogo MCP de MyInvestor (`mcp.myinvestor.es`)
que **no reparten dividendos**: clase de acumulación (`distributing=false`).
Los que distribuyen cupones o dividendos quedan excluidos por regla del titular.

- **Una ficha por fondo:** `<clase>/<ISIN>.md` — qué es y para qué sirve, composición
  (asignación, top sectores/regiones, detalle de renta fija), para qué vale en una
  cartera (texto orientativo, no recomendación), comisiones (TER, gestión, éxito,
  mínimos), rentabilidad (YTD, 1A/3A/5A y años naturales), volatilidad, SRRI, NAV,
  operativa y pegas detectadas en la ficha.
- **Índice:** [`catalogo.md`](catalogo.md), generado y agrupado por clase, ordenado
  por TER. No editar a mano.
- **Progreso:** `estado.json` guarda la frontera de búsqueda y los ISIN ya escritos;
  el trabajo se hace por lotes reanudables.

## Clases

| Carpeta | Contenido |
| --- | --- |
| `monetarios/` | Liquidez y fondo de emergencia |
| `renta-fija/` | Tramo defensivo: gubernamental, corporativo, agregado, inflación |
| `mixtos/` | Bolsa y bonos combinados |
| `rv-global/` | Bolsa mundial (núcleo típico) |
| `rv-usa/` | Bolsa de EE. UU. |
| `rv-europa/` | Bolsa europea |
| `rv-japon/` | Bolsa japonesa |
| `rv-emergentes/` | Bolsa emergente |
| `rv-otros/` | Otras regiones (Asia-Pacífico, Canadá, …) |
| `sectoriales/` | Sectoriales y temáticos (satélites) |

Regla de clasificación: tipo de activo declarado; si falta, asignación real
(`alloc_equity`/`alloc_bond`/`alloc_cash`). Dentro de la bolsa: sector → global →
emergentes → EE. UU. → Japón → Europa → otros. La etiqueta «Mixto» no decide el
perfil: la ficha publica el % real de bolsa dentro.

## Comandos

```bash
python3 tools/fondos_myinvestor.py estado            # progreso del volcado
python3 tools/fondos_myinvestor.py lote              # siguiente lote (120 llamadas MCP)
python3 tools/fondos_myinvestor.py lote --llamadas 60 --fondos 80
python3 tools/fondos_myinvestor.py catalogo          # regenerar solo el índice
```

El volcado completo son ~2.200 fichas y se hace poco a poco (lotes periódicos).
Cada lote: `git pull --rebase` antes, y al terminar `build_index.py` + `verify.py`
+ commit + push (definición de hecho del repo).

## Fuente y límites

Datos del catálogo MCP de MyInvestor en la fecha que figura en cada ficha.
Rentabilidades pasadas no garantizan futuras. El TER puede venir `null` o por
debajo de la comisión de gestión: la ficha lo marca como pega, no como coste
verificado. Este directorio es material de referencia, no consejo de inversión.

# Plantilla de ficha web — listado-app

Una ficha por fondo en `finance/fondos-myinvestor/<clase>/<ISIN>.md`, misma estructura
que las fichas MCP pero con datos del listado de la app (snapshot 2026-11-19) + web.
Lo que no se encuentre se escribe **Pendiente** (no se deja en blanco ni se inventa).

## Frontmatter (claves obligatorias + extras)

```yaml
---
title: "<nombre del fondo>"
date: 2026-11-19
type: reference
category: finance
tags: [<clase>, <activo|indexado>, <divisa en minúsculas>]
status: living
isin: <ISIN>
gestora: "<gestora o Pendiente>"
clase: <clase = carpeta>
ter: <número o vacío>
r3a: <número o vacío>
srri: <número o vacío>
fuente: listado-app
politica: <acumulacion|distribucion|pendiente>
---
```

## Esqueleto

```markdown
# <nombre>

`<ISIN>` · <gestora> · <tipo de activo> · <geografía/sector> · gestión <activa|indexada> · divisa <X> · <acumulación|distribución|política pendiente>

## Qué es y para qué sirve

<2-4 frases: qué es, política de inversión resumida de la fuente (límites, mercados,
benchmark si lo tiene), fecha de constitución, patrimonio. Sin cifras que no estén
en las fuentes.>

## Composición

| Activo | % |
| --- | --- |
| Renta variable | <x o Pendiente> |
| Renta fija | <x o Pendiente> |
| Caja y equivalentes | <x o Pendiente> |
| Otros | <x o Pendiente> |

- **Top sectores:** <lista con % o Pendiente>
- **Top regiones:** <lista con % o Pendiente>
- **Top posiciones:** <hasta 10 con % o Pendiente>
- **Renta fija:** <tipo, duración, calidad crediticia si la fuente lo dice>
- **Capitalización / estilo:** <si la fuente lo dice>
- *Datos de cartera según <fuente>, a fecha <fecha si consta>; pueden no estar al día.*

## Para qué vale en una cartera

<La sección más importante. 3-4 párrafos cortos:
1. Papel: núcleo / satélite / defensivo / liquidez / cobertura, y para qué perfil de
   inversor encaja (orientación general).
2. Evidencia: qué dicen los números — rentabilidad vs su categoría (ranking y quintil
   de quefondos), consistencia por años naturales, volatilidad, Sharpe/alpha/máxima
   caída si constan, coste TER vs alternativas. Si lo ha hecho bien, decirlo con el
   dato; si no hay histórico (<3 años), marcarlo como limitación, no como promesa.
3. Escenario actual: cómo se comporta este tipo de fondo con el escenario de
   contexto-macro.md (tipos Fed/BCE al alza, inflación persistente): qué le favorece,
   qué le perjudica, en qué giro de ciclo brillaría o sufriría.
4. Por qué podría ser prometedor ahora y sus pegas principales (coste, concentración,
   divisa sin cubrir, historial corto, comisión de éxito…).>

*Orientación general derivada de los datos publicados; no es una recomendación de inversión.*

## Comisiones

| Concepto | Valor |
| --- | --- |
| TER (coste total anual) | <x % (snapshot app)> |
| Comisión de gestión | <x % o Pendiente> |
| Comisión de éxito | <x % / no / Pendiente> |
| Comisión de depósito | <x % o Pendiente> |
| Suscripción / reembolso | <x % o Pendiente> |
| Mínimo inicial | <x o Pendiente> |

## Rentabilidad y riesgo

| Período | Rentabilidad |
| --- | --- |
| YTD (2026) | <snapshot> |
| 1 año (trailing) | <snapshot> |
| 3 años anualizada | <snapshot> |
| 5 años anualizada | <snapshot o Pendiente> |
| Año natural 2025 | <web o Pendiente> |
| Año natural 2024 | <web o Pendiente> |
| Año natural 2023 | <web o Pendiente> |
| Año natural 2022 | <web o Pendiente> |

- **Vs categoría (VDOS):** <ranking/quintil por año si constan; decir si bate a su categoría>
- **Volatilidad:** <1A x % si consta; 3A/5A o Pendiente>
- **Máxima caída / Sharpe:** <si constan en Finect>
- **Riesgo SRRI (1-7):** <snapshot>
- **Rating Morningstar:** <★ del snapshot o Pendiente>
- **NAV:** <snapshot> <divisa> a 2026-11-19 (web: <valor y fecha si difieren>)

## Operativa

<Pendiente salvo que la fuente publique mínimos/suscripción/reembolso útiles;
la operativa específica de MyInvestor (hora de corte, días) no está en la web.>

## Pegas y avisos

- <lista: historial <3 años, TER alto vs categoría, comisión de éxito, datos web
  desactualizados, divisa sin cubrir, concentración sectorial, fuente caída…>

## Fuentes

- Listado de la app MyInvestor, guardado el 2026-11-19 (`MyInvestor.html`, raíz del repo).
- <URL exacta de quefondos consultada> (consultada el 2026-11-19).
- <URL exacta de Finect consultada> (consultada el 2026-11-19).
- <otras URLs realmente consultadas, p. ej. ficha de la gestora>

*Rentabilidades pasadas no garantizan futuras. Datos de referencia, no consejo de inversión.*
```

## Avisos sobre las fuentes (aprendidos en las primeras olas)

- **quefondos sirve a veces caché antigua**: si la fecha de los datos es vieja, repetir
  la extracción; usar la versión más cercana al snapshot y anotar la fecha empleada.
- **quefondos convierte las series de clases USD/GBP/CHF a EUR**: los rankings/quintiles
  incluyen efecto divisa y no son comparables con el snapshot de la clase; anotarlo.
- **quefondos parece excluir cupones en clases de distribución**: sus rentabilidades y
  quintiles quedan por debajo de la realidad; anotarlo como pega, no como mal fondo.
- **Finect suele no renderizar la composición** (carga JS), pero la embebe completa en
  `window.INITIAL_STATE` (JSON doblemente codificado): `curl` de la página +
  `json.loads(json.loads(...))` → `fund.fund.model` trae `breakdown` (asset/sectores/
  regiones), `portfolio` (fecha + top 10), `stats`, comisiones y SRRI. Método preferente;
  fallback: snippet de búsqueda de ESA MISMA URL (anotándolo), factsheets oficiales de la
  gestora, o la ficha de una clase hermana del mismo fondo (cartera común). Si no hay
  nada → `Pendiente`.
- **Finect redirige a veces a otra clase o al ETF**: verificar que el ISIN de la página
  coincide con el del lote antes de usar sus datos.
- **SRRI y comisiones discrepan a menudo** entre snapshot, quefondos y Finect: manda el
  snapshot; anotar ambas cifras en Pegas.

## Reglas

1. **Ninguna cifra sin respaldo**: solo números vistos en las páginas extraídas o en el
   JSON del lote. Nada de memoria del modelo. Lo no encontrado → `Pendiente`.
2. El **snapshot manda** en NAV, YTD, 1A/3A/5A, TER y SRRI (son los datos más frescos,
   2026-11-19). La web añade años naturales, rankings, volatilidad, política, comisiones
   y composición; anotar su fecha cuando conste (hay páginas desactualizadas).
3. **Fuentes reales**: solo URLs que se hayan consultado de verdad. Nunca inventar una
   URL ni un dato «porque suele ser así».
4. Si TER web ≠ TER snapshot, anotar ambos en Pegas (p. ej. clase distinta o dato viejo).
5. La ficha es de **referencia**: el agente no da consejo financiero; la sección de
   cartera es orientación general con el descargo de responsabilidad.
6. Fondo con clase `pendiente` en el lote: investigar la política y asignar la clase
   correcta existente (ver mapa en `listado-app/README.md`); crear la carpeta si no
   existe. La clase del frontmatter = carpeta donde se escribe.

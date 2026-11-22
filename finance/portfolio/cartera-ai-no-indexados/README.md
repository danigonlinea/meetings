---
title: "Cartera-ai no indexados: dos tallas (100k y 200k) en fondos de gestión activa que acumulan"
date: 2026-11-16
type: portfolio-proposal
category: finance
tags: [cartera, cartera-ai-no-indexados, gestion-activa, sin-indexados, sin-dividendos, acumulacion, myinvestor, 100k, 200k]
status: final
related: [finance/portfolio/README.md, finance/portfolio/cartera-ai-no-indexados/100k.md, finance/portfolio/cartera-ai-no-indexados/200k.md]
---

# Cartera-ai no indexados — dos tallas, un mandato

Cartera nueva, diseñada desde cero el 16/11/2026 con **solo dos condiciones del titular**:

1. **Ningún fondo que reparta dividendos** — solo clases de acumulación (`distributing = 0` verificado en la ficha de cada ISIN).
2. **Ningún fondo indexado a un índice** — solo gestión activa (`management_type = Activo` verificado en la ficha de cada ISIN).

Todo lo demás lo decide el agente. **No se hereda ninguna regla de este repositorio**: ni el coste mínimo de
`cartera-ai/`, ni el 55 % de renta variable de `cartera-myinvestor/`, ni el criterio de Andrés, ni la
prohibición de acciones de las otras propuestas. Aquí no hay acciones: el mandato habla de fondos del
catálogo de MyInvestor, y así se queda.

## Ficheros

| Fichero | Qué es |
| --- | --- |
| `100k.md` | La cartera de **100.000 €**: 7 fondos de renta variable + 3 de renta fija, 80 % RV objetivo, 1,37 % de TER |
| `200k.md` | La cartera de **200.000 €**: 9 fondos de RV + 3 de RF, mismo 80 % objetivo, 1,42 % de TER |
| `README.md` | Este mapa |

**Un fichero por talla, una cartera por fichero.** El mandato es el mismo en las dos; lo que cambia es
cuántas líneas aguanta el tamaño. A 200.000 € entran Japón small caps, Iberia y más emergentes, porque
tickets de 8.000–16.000 € sí mueven la aguja; a 100.000 € esas tres líneas serían ruido con gastos.

## Las dos únicas reglas

- **Acumulación, no distribución.** Se descarta la clase que reparta aunque sea la más barata o la única
  visible: por eso entra `Fundsmith Equity T EUR Acc` (1,09 %) y no la clase `T EUR Inc`. Un dividendo
  reparte caja que habrá que recolocar, tributa y rompe el interés compuesto sin aportar nada.
- **Gestión activa, no réplica.** Todo ISIN está verificado como `Activo` en el catálogo. Se descarta
  expresamente `BBVA Bolsa Índice FI` (ES0110182039), que el catálogo etiqueta como activo pero cuya ficha
  dice «seguir el comportamiento del índice IBEX 35»: es un indexado disfrazado y sería la trampa fácil de
  este mandato.

## Cómo está pensada (decisiones del agente, no reglas)

- **80 % renta variable / 20 % renta fija** como objetivo de diseño. Con aportaciones de 2.000 €/mes y sin
  horizonte declarado, 80/20 es el máximo que un particular puede mirar caer un 35 % sin vender.
- **Cuatro motores de RV, no uno:** calidad-crecimiento global (Fundsmith + Comgest), mixto estructural
  (DWS), valor profundo (Cobas) y tres geografías que el núcleo global no cubre bien (Japón, small caps
  europeas, emergentes). El objetivo es que el resultado no dependa de que acierte un único estilo.
- **La renta fija es activa y con duración corta-media**, no un agregado de índice: crédito corporativo
  global cubierto a EUR, deuda emergente cubierta y convertibles. Son los tres sitios donde la gestión
  activa en RF aún paga su comisión.
- **Nada por encima del 22 %**, salvo el núcleo de calidad. Ningún fondo supera el 22 % del total ni el 28 %
  del bloque de RV. Es el límite que evita que un solo gestor o una sola tesis manden en la cartera.
- **Sin temáticos ni sectoriales.** Tecnología ya pesa 30–35 % en el núcleo por construcción; un fondo de IA
  o de semiconductores sería apalancar la misma apuesta, no diversificar.
- **Se conservan las clases en EUR** siempre que existan (Japón y RF cubiertos a EUR); las dos clases en USD
  (Comgest Growth Global) son la única puerta disponible y el riesgo divisa se acepta, no se cubre.

## Estado a 16/11/2026

- **Dos tallas cerradas, ninguna ejecutada:** 100k (10 fondos, 1,37 %) y 200k (12 fondos, 1,42 %).
- **Datos de todas las fichas:** catálogo MyInvestor vía MCP, NAV de 12–13/11/2026, TER y `distributing`
  verificados por ISIN con `get_funds`, no por nombre.
- **Decisión abierta (del titular, no del agente):** si estas dos tallas son patrimonio completo o conviven
  con las otras carteras del repositorio. No se consolidan con ellas.

---
title: "Cartera-ai definitivas a estudiar: las ocho propuestas con 30-45 % de indexado"
date: 2026-11-22
type: reference
category: finance
tags: [cartera, indice, cartera-ai-definitivas-estudiar, indexado-30-45, myinvestor, finalistas]
status: living
---
# Cartera-ai definitivas a estudiar

Contenedor de las carteras del repositorio que invierten **entre el 30 % y el 45 % del patrimonio en fondos
indexados**. Se creó el 22/11/2026 a petición del titular para tenerlas juntas; **no las consolida**: cada
carpeta sigue siendo un patrimonio independiente con su criterio, su fecha y su documento.

El techo era el 40 % hasta el 22/11/2026. Ese día el titular lo subió al 45 % por una sola cartera: la C4 de
`cartera-ai-fondos-2000-lista-deepseek` (44,00 % de indexado), que aporta el único perfil defensivo del grupo
(34,06 % de RV, alternativos descorrelacionados y colchón de deuda pública). Las siete anteriores no se mueven ni
cambian de banda.

| Cartera | % indexado | Qué es | Estado |
| --- | --: | --- | --- |
| `cartera-ai-40-max-index/` | **40,0** (100k y 200k) | Techo del 40 % gastado entero en RV (28 % MSCI World + 12 % emergentes) | Sin ejecutar |
| `cartera-ai-final-conservadora/` | **38,3** | La cartera del 18/11 con el crédito consolidado en Neuberger | Sin ejecutar |
| `cartera-ai-andres/` | **38,0** (100k) · **34,0** (200k) | Criterio de Andrés: el indexado como pieza, no como edificio | Sin ejecutar |
| `cartera-ai-final-atrevida/` | **37,0** | 110.000 € desde cero, 82,15 % de RV real, 46 % en convicción activa | Sin ejecutar |
| `cartera-ai-hy4-definitiva/` | **35,0** | Finalista del cribado de las tres variantes de `cartera-ai-fondos-2000-lista*` | ⚠️ Pendiente de la revisión del titular |
| `cartera-ai-rock-index-value-todo/` | **30,0** | Rock intacta como pieza de indexado; el resto, trece fondos activos | Sin ejecutar |
| `cartera-ai-rock-desmontado/` | **38,3** (nivel C) · **69,4** (nivel A) | Rock desmontado por traspaso; el nivel C es el que eligió el titular | Nivel C decidido, sin ejecutar |
| `cartera-ai-c4-defensiva/` | **44,0** | C4 de la familia deepseek: 34,06 % de RV, alternativos descorrelacionados y colchón de deuda pública; 607,60 €/año | Sin ejecutar |

## Lo que se queda fuera y por qué

- **`cartera-myinvestor/`** tiene dos documentos en el rango (`propuesta-pieza.md`, 38,3 % y
  `propuesta-actual.md`, 34,0 %), pero **no se mueve**: es la carpeta de la cartera viva de MyInvestor y sus
  documentos son los que se ejecutan. Para estudiarlas, se leen en su sitio.
- **Las otras nueve carteras de las dos familias de cinco** — C1, C2, C3 y C5 de
  `cartera-ai-fondos-2000-lista-deepseek` y las cinco de `cartera-ai-fondos-2000-lista-glm` — se retiraron el
  22/11/2026: sus porcentajes de indexado son 0 %, 17 %, 53 %, 55 %, 55 %, 60 % y 100 %, así que ninguna entraba
  en la banda ni con el techo ampliado. Sus documentos siguen en el historial de git.

## Regla

Mover una cartera aquí **no cambia ni un peso**: los números, las órdenes y las pruebas fechadas de cada
documento siguen siendo los suyos. Lo único que comparten es el rango de indexado que el titular quiere
estudiar. Los mapas de cada cartera (`README.md` de cada subcarpeta) siguen siendo la puerta de entrada.

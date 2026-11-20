---
title: "cartera-ai-fondos-2000-lista-glm"
date: 2026-11-20
type: reference
category: finance
status: living
---

# cartera-ai-fondos-2000-lista-glm

Cinco carteras **independientes de 100.000 € cada una**, construidas solo con fondos del listado
`finance/fondos-myinvestor/` (1.980 fichas). **Ningún fondo se repite entre las cinco**: 50 líneas,
50 ISIN distintos, comprobados por código también por nombre normalizado y por clase hermana
([`validacion.md`](validacion.md)). No se suman, no se comparan entre sí y no se rebalancea una contra otra.

| Cartera | Criterio | Fondos | RV real | Coste anual | Caída de manual |
| --- | --- | --: | --: | --: | --: |
| [`C1-indice-coste-minimo.md`](C1-indice-coste-minimo.md) | solo gestión indexada, la clase más barata operable de cada índice | 8 | 66,54 % | 109,80 € (0,1098 %) | −27,60 % |
| [`C2-conviccion-activa.md`](C2-conviccion-activa.md) | ningún indexado: cada línea es un proceso de gestión con evidencia en la ficha | 9 | 79,81 % | 1.180,10 € (1,1801 %) | −32,43 % |
| [`C3-equilibrada-55-45.md`](C3-equilibrada-55-45.md) | ≈55 % de RV look-through con núcleo indexado, mixtos activos y renta fija | 11 | 54,38 % | 425,00 € (0,4250 %) | −22,97 % |
| [`C4-defensiva-alternativos.md`](C4-defensiva-alternativos.md) | ≈35 % de RV en baja volatilidad y real assets, más alternativos descorrelacionados | 14 | 34,91 % | 727,70 € (0,7277 %) | −15,34 % |
| [`C5-crecimiento-satelites.md`](C5-crecimiento-satelites.md) | ≈88 % de RV: núcleo ACWI barato y seis satélites sectoriales y regionales | 8 | 87,64 % | 942,30 € (0,9423 %) | −35,35 % |

Las cinco cubren el espectro completo de riesgo (15 % → 88 % de RV) **sin compartir un solo fondo**:
lo que en una es el núcleo barato, en otra se resuelve con otro vehículo del catálogo.

## Mandato

- **Universo:** las 1.980 fichas de `finance/fondos-myinvestor/` (snapshot de la app 19/11/2026).
  No hay ETF ni acciones: solo fondos de inversión traspasables.
- **La condición del titular:** entre estas cinco carteras **ningún fondo repetido**.
  **No se aplicó la lista negra de otras carteras del repositorio**, porque el mandato no la pidió.
  Una excepción documentada: `IE00B88WFS66` también está en la cartera hermana
  `cartera-ai-fondos-2000-lista` — el solape con esa carpeta es 1 de 50.
- **Solamente clases de acumulación**, por la regla vigente en `finance/portfolio/README.md` §Reglas:
  50 de 50 con `distributing=0` verificado en el MCP.
- **100.000 € por cartera exactos**, en fondos traspasables; mínimos iniciales verificados en el MCP
  del 20/11/2026 (el mayor es 1.000 €, siempre por debajo del importe de su línea).
- La rentabilidad esperada es una **estimación del agente con supuestos declarados**, no una promesa.
  La decisión y la ejecución son del titular. **Ninguna de las cinco está ejecutada.**

## Cómo se ha hecho

1. Extracción determinista de los campos decisivos de las 1.980 fichas (TER, gestión, éxito, mínimos,
   exposición real, evidencia frente a categoría, pegas).
2. Criba por bloque y diseño de cinco criterios distintos; pesos ajustados por código hasta clavar
   100.000 € y el perfil objetivo de cada criterio.
3. **Verificación de los 60 ISIN candidatos en el catálogo MCP de MyInvestor (20/11/2026, 7 llamadas
   `get_funds`)**: acumulación, TER, mínimos y avisos. Cuatro hallazgos cambiaron el diseño:
   un TER 2,3× mayor que el snapshot (GS US Enhanced), un fondo cerrado (Avantage), un soft close
   (Vanguard Euro Gov Investor → clase nueva) y dos mínimos incompatibles (Amundi Prime Gov 500.000 €,
   Hermes clase F 100.000 €). No hizo falta verificación web adicional.
4. Cuadre y no-repetición comprobados por código sobre el markdown ya escrito: 50 líneas, 50 ISIN,
   50 fondos, 5 × 100.000 € exactos.

## Ficheros

- `C1…C5-*.md`: cada cartera entera (mandato, tabla con ISIN, bloques, métricas, geografía
  look-through, razón fondo a fondo, órdenes, descartes con número y revisión).
- `fondos-revisados.md`: los 50 fondos con TER, éxito, exposición, mínimo, corte y evidencia/pega
  principal, más las 12 divergencias TER ficha-MCP.
- `validacion.md` / `validacion.json`: funnel, unicidad, cuadre y verificación de plataforma.
- `diseno.json`: las cinco carteras en formato máquina.

## Estado

Sin ejecutar, a la espera de la revisión del titular. Pendiente de confirmar: horizonte real, colchón
fuera de la cartera, aportaciones periódicas y política personal sobre comisiones de éxito. El encargo
es la misma petición del 20/11/2026 que produjo `cartera-ai-fondos-2000-lista/` (dos carteras tras
retirar tres por no aportar); este diseño entrega las cinco y deja la comparación entre ambos al titular.

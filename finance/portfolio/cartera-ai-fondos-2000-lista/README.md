# cartera-ai-fondos-2000-lista

Dos carteras **independientes de 100.000 € cada una**, construidas solo con fondos del listado
`finance/fondos-myinvestor/`. **Ningún fondo se repite entre las dos**: 21 líneas, 21 ISIN distintos,
comprobados también por nombre normalizado y por clase hermana.
No se suman, no se comparan entre sí y no se rebalancea una contra otra.

| Cartera | Criterio | Fondos | RV real | TER medio | Coste | Caída de manual |
| --- | --- | --: | --: | --: | --: | --: |
| [`C2-conviccion-activa.md`](C2-conviccion-activa.md) | la renta variable se elige por proceso de gestión con evidencia en la ficha (value, calidad, dividendo creciente, multifactor, cuantitativo), más crédito activo de coste bajo. Ningún indexado. | 10 | 78,65 % | 1,2486 % | 1.248,60 €/año | −32,06 % (32.057 €) |
| [`C4-defensiva-alternativos.md`](C4-defensiva-alternativos.md) | 35,49 % de RV, 43,88 % de renta fija y liquidez, y tres alternativos descorrelacionados (cat bonds, market neutral, managed futures), con dos fondos de baja volatilidad y dos mixtos defensivos. | 11 | 35,49 % | 0,7661 % | 766,10 €/año | −15,51 % (15.514 €) |

## Por qué quedan dos y no cinco

El encargo del 20/11/2026 pedía cinco criterios. Tras cruzarlas contra las carteras que ya existían en
`finance/portfolio/` se retiraron **C1, C3 y C5** el mismo 20/11/2026: no aportaban nada que no estuviera
ya resuelto, y en dos casos a peor precio.

| Retirada | Con qué se comparó | El número |
| --- | --- | --- |
| **C1 — Índice de coste mínimo** | `cartera-ai-100-index/` (mismo mandato: solo indexado, solo acumulación) y `cartera-definitiva-40/` | C1: 77,52 % de RV por 132,20 €/año. `100-index`: 79,79 % por 106,50 €/año. `definitiva-40`: 83,39 % por 92,00 €/año y ≈6,06 % esperado. Pagaba 25,70 €/año más por 2,3 pp menos de bolsa. |
| **C3 — Equilibrada 55/45** | `cartera-ai-final-conservadora/` y `cartera-myinvestor/propuesta-pieza.md` | C3: 54,75 % de RV por 557,70 €/año. Conservadora: 54,61 % por 509,70 €/año. Pieza vigente: 54,6 % por 529,90 €/año. Mismo perfil de riesgo, más caro y sin decisión nueva. |
| **C5 — Crecimiento con satélites** | `cartera-ai-final-hy3/` y `cartera-ai-final-qwen4max/` (ambas retiradas el 20/11/2026) y `cartera-ai-final-atrevida/` | C5: 82,95 % de RV por 952,80 €/año y ≈6,25 % esperado. hy3: 84,16 % por 527,60 €/año y ≈6,21 %. qwen4max: 84,15 % por 598,50 €/año y ≈6,2 %. El doble de coste para el mismo resultado esperado. |

**Lo que sí aportan las dos que quedan:**

- **C2** es la cartera 100 % activa al 80 % de RV **más barata del repositorio** (1,2486 % frente a
  1,37 % de `cartera-ai-no-indexados/`, 1,35 % de `-5`, 1,55 % de `-3` y 1,60 % de `-4`). Exige +1,12 pp
  de alfa frente a un indexado puro para empatar; la prueba está fechada en su §9.
- **C4** cubre un perfil que no existía: ninguna otra cartera del repositorio está en el 35 % de RV con
  alternativos descorrelacionados. El precio es 0,77 % de TER y tres líneas con comisión de éxito o
  estructura compleja.

Los documentos de C1, C3 y C5, con sus 31 fondos revisados, siguen en el historial de git; no se
mantienen en el árbol porque inducirían a ejecutar una cartera superada.

## Mandato

- **Universo:** las 2.007 fichas de `finance/fondos-myinvestor/` (1.802 del listado de la app, 205 del MCP).
  No hay ETF ni acciones: solo fondos de inversión.
- **La condición del titular para este encargo:** entre estas dos carteras **ningún fondo repetido**.
  No se aplica la lista negra de las otras carteras del repositorio, porque el mandato no la pidió.
- **Solamente clases de acumulación**, por la regla vigente en `finance/portfolio/README.md` §Reglas.
  Las clases de distribución se descartan aunque sean más baratas.
- **100.000 € por cartera exactos**, en fondos traspasables. Importes mínimos verificados en el MCP del
  20/11/2026 o en la ficha web del 19/11/2026; cada línea respeta el suyo.
- La rentabilidad esperada es una **estimación del agente con supuestos declarados**, no una promesa.
  La decisión y la ejecución son del titular. **Ninguna de las dos está ejecutada.**

## Cómo se ha hecho

1. Criba del universo por clase y política de dividendos, con mínimos publicados y avisos de soft close.
2. Lectura de la ficha completa de cada candidata y extracción de TER, gestión, éxito, mínimos, divisa,
   exposición real (RV/RF/caja/otros) y evidencia (3A/5A, volatilidad, años malos).
3. Diseño de cinco criterios distintos y verificación por código de la no-repetición y de los mínimos.
4. Cuatro comprobaciones web puntuales de campos decisivos que quedaban pendientes o discrepantes.
5. Cruce ISIN a ISIN contra las 26 carpetas del repositorio y retirada de las tres que no aportaban.

## Ficheros

- `C2-conviccion-activa.md` y `C4-defensiva-alternativos.md`: la cartera entera (mandato, tabla con ISIN
  y pesos, bloques, métricas, geografía, razón por fondo, órdenes, descartes y revisión).
- `fondos-revisados.md`: revisión de los 21 fondos con cifras citadas de cada ficha.
- `validacion.md` / `validacion.json`: comprobación de no-repetición, mínimos, TER y verificaciones web.
- `diseno.json`: los mismos 21 fondos y pesos en formato máquina.

## Estado

Sin ejecutar, a la espera de la revisión del titular. Pendiente de confirmar: horizonte real, colchón
fuera de la cartera, si habrá aportaciones periódicas y la política de comisiones de éxito en C4.

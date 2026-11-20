# cartera-ai-fondos-2000-lista

Cinco carteras **independientes de 100.000 € cada una**, construidas solo con fondos del listado
`finance/fondos-myinvestor/`. **Ningún fondo se repite entre las cinco**: 52 líneas, 52 ISIN distintos,
52 fondos distintos comprobados también por nombre normalizado y por clase hermana.
No se suman, no se comparan entre sí y no se rebalancea una contra otra.

| Cartera | Criterio | Fondos | RV real | TER medio | Coste | Caída de manual |
| --- | --- | --: | --: | --: | --: | --: |
| [`C1-indexado-coste-minimo.md`](C1-indexado-coste-minimo.md) | todo el vehículo es indexado (100 %) y el TER medio se mantiene por debajo del 0,14 %. Núcleo MSCI World, small caps y tres regiones, con 22,13 % de renta fija indexada. | 9 | 77,52 % | 0,1322 % | 132,20 €/año | −31,67 % (31.666 €) |
| [`C2-conviccion-activa.md`](C2-conviccion-activa.md) | la renta variable se elige por proceso de gestión con evidencia en la ficha (value, calidad, dividendo creciente, multifactor, cuantitativo), más crédito activo de coste bajo. Ningún indexado. | 10 | 78,65 % | 1,2486 % | 1.248,60 €/año | −32,06 % (32.057 €) |
| [`C3-equilibrada-55-45.md`](C3-equilibrada-55-45.md) | 54,75 % de RV real (look-through) y 37,97 % de renta fija más liquidez, con el índice cubierto como núcleo y la convicción activa como satélite. Es el punto medio deliberado entre C1 y C5. | 11 | 54,75 % | 0,5577 % | 557,70 €/año | −23,04 % (23.040 €) |
| [`C4-defensiva-alternativos.md`](C4-defensiva-alternativos.md) | 35,49 % de RV, 43,88 % de renta fija y liquidez, y tres alternativos descorrelacionados (cat bonds, market neutral, managed futures), con dos fondos de baja volatilidad y dos mixtos defensivos. | 11 | 35,49 % | 0,7661 % | 766,10 €/año | −15,51 % (15.514 €) |
| [`C5-crecimiento-satelites.md`](C5-crecimiento-satelites.md) | 82,95 % de RV, núcleo indexado (35 %) y once líneas con satélites de sector, región y tamaño. Es la cartera con mayor esperanza y también con mayor caída. | 11 | 82,95 % | 0,9528 % | 952,80 €/año | −33,52 % (33.522 €) |

## Mandato

- **Universo:** las 2.007 fichas de `finance/fondos-myinvestor/` (1.802 del listado de la app, 205 del MCP).
  No hay ETF ni acciones: solo fondos de inversión.
- **La condición del titular para este encargo:** entre estas cinco carteras **ningún fondo repetido**.
  No se aplica la lista negra de las otras carteras del repositorio, porque el mandato no la pidió.
- **Solamente clases de acumulación**, por la regla vigente en `finance/portfolio/README.md` §Reglas.
  Las clases de distribución se descartan aunque sean más baratas.
- **100.000 € por cartera exactos**, en fondos traspasables. Importes mínimos verificados en el MCP del
  20/11/2026 o en la ficha web del 19/11/2026; cada línea respeta el suyo.
- La rentabilidad esperada es una **estimación del agente con supuestos declarados**, no una promesa.
  La decisión y la ejecución son del titular. **Ninguna de las cinco está ejecutada.**

## Cómo se ha hecho

1. Criba del universo por clase y política de dividendos, con mínimos publicados y avisos de soft close.
2. Lectura de la ficha completa de cada candidata y extracción de TER, gestión, éxito, mínimos, divisa,
   exposición real (RV/RF/caja/otros) y evidencia (3A/5A, volatilidad, años malos).
3. Diseño de cinco criterios distintos y verificación por código de la no-repetición y de los mínimos.
4. Cuatro comprobaciones web puntuales de campos decisivos que quedaban pendientes o discrepantes.

## Ficheros

- `C1-indexado-coste-minimo.md` … `C5-crecimiento-satelites.md`: la cartera entera (mandato, tabla con ISIN
  y pesos, bloques, métricas, geografía, razón por fondo, órdenes, descartes y revisión).
- `fondos-revisados.md`: revisión de los 52 fondos con cifras citadas de cada ficha.
- `validacion.md` / `validacion.json`: comprobación de no-repetición, mínimos, TER y verificaciones web.
- `diseno.json`: los mismos 52 fondos y pesos en formato máquina.

## Estado

Sin ejecutar, a la espera de la revisión del titular. Pendiente de confirmar: horizonte real, colchón
fuera de la cartera, si habrá aportaciones periódicas y la política de comisiones de éxito en C4.

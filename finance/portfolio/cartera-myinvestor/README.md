---
title: "Cartera MyInvestor: cómo funciona esta carpeta"
date: 2026-11-01
type: reference
category: finance
tags: [cartera, indice, proceso]
status: living
---
# Cartera MyInvestor: cómo funciona esta carpeta

La cartera de MyInvestor (97.000 € invertibles = 67.000 € manuales, con los 7.000 € de aportación nueva
incluidos, + 30.000 € de Rock; más 10.000 € de colchón fuera de la base), dentro de `finance/portfolio/`.
Es independiente de `../cartera-renta4/`: no comparten saldos, ni propuesta, ni cifras. El resto de
material financiero (vídeos, webinars, informes) está en las otras subcarpetas de `finance/`.

## Dos documentos vivos… más dos anexos de investigación

| Fichero | Rol | ¿Se edita? |
| --- | --- | --- |
| `cartera-actual.md` | **Fotografía congelada** del estado real: saldos, pesos, ISIN, TER, TIR, duración, Rock y consolidado de 90.000 €. Fuente de verdad | **No.** Un cambio de saldos genera `cartera-actual-YYYY-MM-DD.md` |
| `propuesta-actual.md` | **La cartera vigente**: modelo que decide el % de RV, cartera final con ISIN e importes, órdenes, métricas, coste de la decisión, ejecución, diagnóstico y qué se descarta | **Sí**, es el documento de trabajo |
| `propuesta-alternativa.md` | **Anexo de investigación, no una cartera paralela**: dos carteras posibles sobre la vigente —mínima (REITs indexados al 0,17%, 5.000 €) y ampliada (10 fondos manuales: + Fundsmith 1,09% y Comgest Growth Europe 1,59%)— con pesos, financiación y ocho fuentes. Nace del barrido del catálogo MyInvestor del 01/11/2026 | **No mientras no se adopte.** Si se adopta, sus conclusiones pasan a `propuesta-actual.md` y el fichero **se borra** (`git rm`) |
| `propuesta-investigacion.md` | **Anexo de investigación de dos bloques**, no una cartera paralela: calidad global (Fundsmith T Acc, 1,09 %) y activos reales (iShares Developed Real Estate D Acc, 0,17 %), 5.000 € y 19 posiciones, con dos fuentes por vehículo, riesgos, señal de invalidación y cuatro traspasos. Nace del encargo del 02/11/2026 y se reajustó el mismo día con la regla de acumulación, que vació la satélite de acciones y ETFs | **No mientras no se adopte.** Si se adopta, sus conclusiones pasan a `propuesta-actual.md` y el fichero **se borra** (`git rm`) |

Los anexos existen porque el usuario pidió conservar la investigación con nombres, ISIN, TER y pesos; su
ciclo de vida es corto a propósito: **o se incorporan a la propuesta, o se descartan y desaparecen**. Una
tercera cartera permanente volvería a dejar dos documentos con dos cifras de la misma cartera.

El diagnóstico, el veredicto frente a las fuentes y las revisiones adversariales **no viven en
ficheros aparte**: sus conclusiones están dentro de la propuesta (§2, §5, §7, §8) y el debate que las
produjo, en el historial de git. Un documento por rol evita las dos verdades: la carpeta llegó a tener
tres ficheros con cifras distintas de la misma cartera.

## Estado a 02/11/2026

- **Cartera:** 107.000 € totales = 10.000 € de colchón (Groupama, fuera de la cartera) + 97.000 €
  invertibles (67.000 € manuales, con 7.000 € de aportación nueva, + 30.000 € en Rock).
- **Situación de partida (90k):** 31,6% de renta variable, 68,4% de renta fija, 0,746% de TER y 17
  posiciones.
- **Propuesta (cerrada):** **50,0% de RV / 50,0% de RF**, 0,655% de TER y 17 posiciones. Emergentes al
  10%, dos fondos value (5.000 + 5.000) y small caps en 3.700. Mueve 25.000 € por traspaso (0 € de
  impuestos) + 7.000 € de aportación, en 11 órdenes y tres tandas. Caída esperada ≈ −21,5%.
- **Pendiente antes de la primera orden:** los **gastos mensuales** (el colchón de 10.000 € nunca se
  dimensionó contra un dato real) y confirmar que se aguanta el −21,5%. Comisiones verificadas el
  31/10: 0,00% de reembolso en los cinco fondos que salen; entrada 0,00% salvo el Neuberger («hasta
  3%», máx. 297 €). Falta ver en pantalla la comisión de la clase S de iShares EM.
- **Decisión abierta (anexo del 01/11):** si se añade el bloque de activos reales de
  `propuesta-alternativa.md` —iShares Developed Real Estate (IE00BDRK7P73, 0,17%)— y si la cartera se
  queda en la **versión mínima** (5.000 €, 17 posiciones, 632 €/año) o pasa a la **ampliada** (10 fondos
  manuales, con Fundsmith 3.000 € al 1,09% y Comgest Growth Europe 2.500 € al 1,59%; 19 posiciones,
  662 €/año, USA 37,6% de la RV). Antes de ejecutarlo hay que verificar el reembolso de Vanguard
  Small-Cap, Fidelity Europe, MyInvestor Value y Cobas, y la entrada de los tres fondos nuevos.
- **Investigación abierta (02/11):** `propuesta-investigacion.md` propone **5.000 € en dos vehículos de
  acumulación** —Fundsmith T Acc 3.000 y iShares Developed Real Estate D Acc 2.000— financiados con
  cuatro traspasos (small cap, Europa y 1.000 € de cada value), manteniendo el 50/50 y la RF intacta.
  No ejecutada. Como el anexo del 01/11 ha convergido con ella (mismos dos vehículos, distintos pesos),
  hay **una sola decisión**, no dos: la ampliada de la alternativa (19 posiciones, 662 €/año), la mínima
  de la alternativa (REITs 5.000 €, 17 posiciones, 632 €/año) o estos 5.000 €.

## Reglas de esta carpeta

- Un dato se escribe una vez: la foto en `cartera-actual.md`, la decisión y su porqué en
  `propuesta-actual.md`. Ningún fichero replica la tabla de posiciones del otro.
- Toda propuesta se ejecuta por **traspaso** entre fondos armonizados, nunca por reembolso.
- Nada se mueve sin verificar antes la clase del fondo y su coste real en la plataforma.

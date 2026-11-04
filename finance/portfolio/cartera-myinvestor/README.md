---
title: "Cartera MyInvestor: cómo funciona esta carpeta"
date: 2026-11-04
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

## Tres documentos, un papel cada uno

| Fichero | Rol | ¿Se edita? |
| --- | --- | --- |
| `cartera-actual.md` | **Fotografía congelada** del estado real a 30/10/2026: saldos, pesos, ISIN, TER, TIR, duración, Rock y consolidado de 90.000 €. Fuente de verdad de las posiciones | **No.** Un cambio de saldos genera `cartera-actual-YYYY-MM-DD.md` |
| `propuesta-actual.md` | **La cartera vigente y única** (04/11/2026): modelo de RV con ocho señales, ocho fondos manuales, doce órdenes, métricas, riesgos, descartes y revisión trimestral | **Sí**, es el documento de trabajo |
| `propuesta-acciones.md` | **Bloque de riesgo aparte**: cuatro acciones individuales sin dividendo. No forma parte de la cartera de fondos, no entra en su look-through y no se rebalancea contra ella | Sí, pero nunca se suma a la cartera de fondos |

**Ya no hay anexos.** La carpeta llegó a tener cinco propuestas paralelas con cinco cifras distintas de
la misma cartera. El 04/11/2026 se resolvieron todas en `propuesta-actual.md` y se borraron (`git rm`);
su contenido íntegro sigue en el historial de git (último commit con la carpeta completa: `50b2e69`) y
el resumen de lo que aportó cada una está en §12 de la propuesta. **No se crean carteras paralelas:** si
aparece una idea, o entra en la propuesta o se descarta con el número delante.

El diagnóstico, el veredicto frente a las fuentes y las revisiones adversariales **no viven en ficheros
aparte**: sus conclusiones están dentro de la propuesta (§2, §5, §8, §10) y el debate que las produjo, en
el historial de git. Un documento por rol evita las dos verdades.

## Estado a 04/11/2026

- **Cartera:** 107.000 € totales = 10.000 € de colchón (Groupama, fuera de la cartera) + 97.000 €
  invertibles (67.000 € manuales, con 7.000 € de aportación nueva, + 30.000 € en Rock).
- **Reparto:** **54,9 % de RV / 45,1 % de RF** (look-through estricto, Rock dentro). Coste total
  **426 €/año (0,439 %)**: 303 € manuales y 123 € de Rock. Cero comisiones de éxito.
- **Ocho fondos manuales + Rock:** Neuberger 17.000 · Cobas Renta 5.000 · Aegon ABS 7.000 · Amundi
  Euro Corp 1-5Y 7.400 · iShares Europe 13.600 · iShares EM 7.000 · iShares REITs 5.000 · Cobas
  International 5.000.
- **Ejecución:** doce órdenes (dos suscripciones y **diez traspasos**, 49.000 €) en dos sesiones.
  Traspaso y nunca reembolso: 0 € de impuestos.
- **Caída estimada tipo 2008: −23,3 % (−22.600 €).** Es el precio de entrada y está escrito como suelo
  conductual en §2 de la propuesta.
- **Pendiente antes de la primera orden:** los **gastos mensuales** (el colchón de 10.000 € nunca se
  dimensionó contra un dato real) y confirmar que se aguanta el −23,3 %. Comisiones verificadas el 31/10:
  0,00 % de reembolso en los cinco fondos que salen. Falta ver en pantalla la comisión de entrada de
  Aegon, Amundi, iShares Europe, REITs y Cobas Renta.

## Reglas de esta carpeta

- Un dato se escribe una vez: la foto en `cartera-actual.md`, la decisión y su porqué en
  `propuesta-actual.md`. Ningún fichero replica la tabla de posiciones del otro.
- Toda propuesta se ejecuta por **traspaso** entre fondos armonizados, nunca por reembolso.
- Nada se mueve sin verificar antes la clase del fondo y su coste real en la plataforma.
- **Rock no se desmonta**: la plusvalía de +83,44 % acumulada desde 2020 se cristalizaría. Su 78/22 y su
  bono a 20+ años se aceptan como parte del diseño, y por eso el 76 % del riesgo de tipos vive ahí.
- Las acciones individuales son **otro bloque de riesgo** del titular: no entran en el % de RV de esta
  cartera ni se compensan con ella.

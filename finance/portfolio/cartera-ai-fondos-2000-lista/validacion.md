---
title: "Validación del diseño cartera-ai-fondos-2000-lista"
date: 2026-11-20
type: reference
category: finance
tags: [validacion, myinvestor, fondos, no-repeticion, auditoria]
status: final
related:
  - finance/portfolio/README.md
  - finance/portfolio/cartera-ai-fondos-2000-lista/README.md
---

# Validación del diseño

**Resultado: 0 errores y 0 avisos.** 21 fondos distintos, 21 líneas, 21 identidades normalizadas. Ningún fondo se usa en las dos carteras, ni por ISIN, ni por nombre normalizado, ni por clase hermana conocida.

> **Alcance.** El encargo del 20/11/2026 pedía cinco carteras. Ese mismo día se retiraron C1, C3 y C5 por no aportar frente a carteras ya existentes del repositorio; el detalle y los números están en el `README.md` de esta carpeta. Esta validación cubre las dos vigentes: C2 y C4, 21 fondos.

## Comprobaciones ejecutadas

- ISIN único en las 2 carteras
- nombre de fondo normalizado único (21/21)
- clases hermanas conocidas: ninguna cruzada entre carteras
- 100.000 € exactos por cartera y 21 líneas
- TER del diseño = TER del snapshot de la ficha en los 21 fondos
- 21/21 con política de acumulación y ficha presente en el repo
- importe de cada línea >= mínimo inicial verificado (MCP 20/11 o ficha web 19/11)

## Errores

Ninguno.

## Avisos

Ninguno.

## Verificación puntual en internet (20/11/2026)

Solo campos decisivos que la ficha del repo dejaba como pendientes o discrepantes. No se ha hecho un barrido web de los 21 fondos.

**LU0080237943 — comisión de reembolso discrepante.** KID oficial DWS de 16/02/2026: «No fees or penalties will be charged by the company for any such transaction», periodo recomendado 183 días, riesgo 1/7 y beneficios reinvertidos. El 2,50 % que publicaban Finect y FT no aparece en el KID; se conserva como discrepancia a verificar en pantalla, no como coste modelado.
Fuente: <https://download.dws.com/download/asset/4b9b6e74-8baa-46ae-971a-c9895905b477?tenant=ActiveEmea>

## Retiradas

Las verificaciones web de `LU1769942233` (C3) y `LU0171307068` (C5) quedan en el historial de git junto con sus documentos; esos fondos ya no forman parte del diseño y no se validan aquí.

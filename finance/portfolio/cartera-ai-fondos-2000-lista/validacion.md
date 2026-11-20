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

**Resultado: 0 errores y 0 avisos.** 52 fondos distintos, 52 líneas, 52 identidades normalizadas. Ningún fondo se usa en dos de las cinco carteras, ni por ISIN, ni por nombre normalizado, ni por clase hermana conocida.

## Comprobaciones ejecutadas

- ISIN único en las 5 carteras
- nombre de fondo normalizado único (52/52)
- clases hermanas conocidas: ninguna cruzada entre carteras
- 100.000 € exactos por cartera y 52 líneas
- TER del diseño = TER del snapshot de la ficha en los 52 fondos
- 52/52 con política de acumulación y ficha presente en el repo
- importe de cada línea >= mínimo inicial verificado (MCP 20/11 o ficha web 19/11)

## Errores

Ninguno.

## Avisos

Ninguno.

## Verificación puntual en internet (20/11/2026)

Solo campos decisivos que la ficha del repo dejaba como pendientes o discrepantes. No se ha hecho un barrido web de los 52 fondos.

**LU1769942233 — cobertura de divisa y coste de la clase LCH.** Factsheet oficial DWS a 30/10/2026: clase LCH (EUR), acumulación, gestión 1,30 %, TER 1,48 %, carga inicial hasta 2 %. La clase LCH es la variante cubierta del yen: su rentabilidad acumulada a 3 años es 81,1 % frente al 55,7 % de la clase LC(EUR) sin cubrir. Queda verificada la cobertura que la ficha MCP no declaraba.
Fuente: <https://download.dws.com/download/asset/6f69b6a8-359f-4a36-bb75-4ef2c26b9fda?tenant=ActiveEmea>

**LU0171307068 — mínimo y política de dividendos.** Ficha oficial BlackRock: «Class A2 (EUR) (Accumulating)», Minimum Initial Investment USD 5.000,00, Ongoing Charges 1,81 %, Management Fee 1,50 %, Performance Fee 0,00 %, desviación 3A 14,20 %, 2022 +0,6 %, 2025 +0,1 %. La línea de 6.000 € cubre el mínimo; el cargo inicial del 5 % del folleto se verifica en pantalla en la plataforma.
Fuente: <https://www.blackrock.com/se/professionals/products/229337/blackrock-world-healthscience-a2-eur-fund>

**LU0080237943 — comisión de reembolso discrepante.** KID oficial DWS de 16/02/2026: «No fees or penalties will be charged by the company for any such transaction», periodo recomendado 183 días, riesgo 1/7 y beneficios reinvertidos. El 2,50 % que publicaban Finect y FT no aparece en el KID; se conserva como discrepancia a verificar en pantalla, no como coste modelado.
Fuente: <https://download.dws.com/download/asset/4b9b6e74-8baa-46ae-971a-c9895905b477?tenant=ActiveEmea>

**IE00BG226Z29 — anomalía de comisiones y cambio de gestora.** Aegon AM anuncia que a partir del 23/11/2026 la gestora del ICAV pasa a Carne Global Fund Managers (Ireland) Limited. La página oficial solo lista las clases USD G/D/X, no la clase EUR A del catálogo; la anomalía TER 0,66 % frente a gestión 1,50 % queda sin resolver y se mantiene el TER del snapshot como coste modelado, con aviso.
Fuente: <https://www.aegonam.com/funds-resources/fixed-income/european-abs-fund/>

**IE000ZYRH0Q7 — mínimo institucional de la clase S.** Las fichas web publican 200.000.000 (USD en quefondos, EUR en Finect) para la clase S, mientras el dato MCP del 20/11/2026 da 0,00 EUR. Se conserva la clase S por ser la operable en la plataforma y se escribe el mínimo publicado como condición a comprobar en pantalla antes de la primera orden.
Fuente: fichas del repo y dato MCP 20/11/2026.


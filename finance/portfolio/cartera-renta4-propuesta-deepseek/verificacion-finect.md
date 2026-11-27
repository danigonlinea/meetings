---
title: "Verificación en Finect y Renta 4 de los fondos de la propuesta DeepSeek (27/11/2026)"
date: 2026-11-27
type: reference
category: finance
tags: [cartera, renta4, finect, verificacion, isin, comisiones, custodia, disponibilidad]
status: living
---
# Verificación en Finect y Renta 4 — 27/11/2026

Evidencia usada para la hoja [`propuesta-actual.md`](propuesta-actual.md). El criterio de
disponibilidad es la **columna «Dónde lo puedes comprar» de la tabla de clases de Finect**: el logo de
Renta 4 Banco aparece en las clases que el bróker comercializa. Se contrasta con `financial-hub.es`
(que lista los comercializadores por ISIN) y con `r4.com` / `finantres.com` para la custodia.

## 1. Fondos de la cartera

| ISIN | Fondo | ¿R4? | Evidencia | Gastos corrientes | Gestión | Custodia de R4 | Suscripción | Mínimo de clase |
| --- | --- | :-: | --- | --: | --: | --: | --: | --: |
| `IE00BYX5NX33` | Fidelity MSCI World Index EUR P Acc | **Sí** | Logo R4 en Finect + `r4.com` | 0,100 % | 0,120 % | **0,19 % + IVA** | 0,000 % | 0 € (50 € en R4) |
| `IE0031786696` | Vanguard Emerging Markets Stock Index EUR Acc | **Sí** | Logo R4 en Finect + financial-hub «Renta 4 Banco» | 0,230 % | 0,230 % | **0,19 % + IVA** | 0,000 % | 1.000.000 € de folleto; 10 € de plataforma |
| `LU0203975437` | Robeco BP Global Premium Equities D EUR | **Sí** | Logo R4 en Finect + `r4.com/.../LU0203975437` | 1,460 % | 1,250 % | 0 % del bróker (Finect publica 0,500 % de custodia del fondo) | 5,000 % máx. de folleto | 0 € |
| `ES0156674006` | Kaizen Global Income FI | **Ya en cartera** | Renta 4 Gestora | 0,960 % | 1,250 % + **9 % éxito** | 0 % | 0 % | 10 € |
| `ES0128520006` | Renta 4 Renta Fija 6 Meses FI | **Ya en cartera** | Renta 4 Gestora | 0,310 % | — | 0 % | 0 % | 10 € |

## 2. Fondos descartados por disponibilidad o coste

| ISIN | Fondo | ¿R4? | Qué dice la evidencia | Consecuencia |
| --- | --- | :-: | --- | --- |
| `IE00BYX5M476` | Fidelity MSCI Emerging Markets P Acc | **No** | Finect: solo logo de EBN Banco, sin R4 | El bloque emergente va con Vanguard (0,23 % vs 0,20 %) |
| `IE000ZYRH0Q7` | iShares Developed World Index (IE) S Acc | **No** | Finect: solo EBN Banco; mínimo de folleto 200 M€ | Descartado; el núcleo va con Fidelity |
| `LU1599216113` | GS Global Small Cap CORE Acc EUR Snap | **Sí** | Finect: logo R4; gastos 1,390 %; mínimo 5.000 € | Descartado por coste/etiqueta, no por acceso |
| `IE00B42W4L06` | Vanguard Global Small-Cap Index EUR Acc | **Sí** | Finect: logo R4; gastos 0,290 %; mínimo de folleto 1 M€ | Aparcado para cuando la cartera pase de 50.000 € |
| `IE00BYX5MD61` | Fidelity MSCI Europe Index EUR P Acc | **Sí** | Finect: logo R4; gastos 0,100 %; mínimo 0 € | Plan B del bloque emergente |
| `ES0107479000` | Akira Global Value FI | **Sí** | Renta 4 Gestora; 1,480 % + 9 % éxito; 47,6 % liquidez | Descartado por historial, coste y solape con Kaizen |

## 3. Comisiones de Renta 4 que se suman al fondo

- **Custodia sobre clases limpias indexadas: 0,15 %–0,19 % + IVA al año.** Fuentes:
  `invertirindexado.es/broker/renta4` (02/11/2026) y `finantres.com/fondos-indexados-renta-4`
  (30/10/2026). La ficha concreta de cada fondo manda; en la clase de Fidelity MSCI World la custodia
  publicada es 0,19 %.
- **Suscripción y reembolso de fondos: 0 %** en la operativa de Renta 4; el folleto del fondo puede
  permitir un máximo (Robeco 5,00 %, GS 5,50 %, AXA 3,00 %) que hay que confirmar en pantalla.
- **Cuota de 3 €/mes:** posible salvo condiciones (invertirindexado). La hoja de tarifas v1/7/2026 de
  Renta 4 la exime si la cuenta solo tiene fondos (`cartera-actual.md` §4). Confirmar.
- **Efecto en esta cartera:** 0,19 % + IVA sobre 22.252,28 € de bloque indexado = **≈51 €/año**
  (0,147 % de la cartera). Sin IVA, el coste total de la cartera baja de 0,621 % a 0,595 %.

## 4. Lo que no se ha podido verificar

| Dato | Por qué |
| --- | --- |
| Mínimo real de `IE0031786696` en la plataforma de R4 | Finect publica el mínimo de folleto (1 M€) y financial-hub confirma que R4 lo comercializa; el mínimo operativo (10 €) es el que anuncia R4 para indexados, pero no está en la ficha del ISIN |
| Custodia exacta por ISIN en la ficha de R4 | `r4.com` devuelve error 500 al intentar leer la ficha desde fuera de la sesión; se usa la política general (0,19 %) y la ficha de Fidelity citada por finantres |
| Comisión de suscripción de AXA para esta clase | El folleto permite hasta 3,00 %; no consta la aplicada por R4 |
| OGC definitivo de Kaizen | 0,96 % publicado frente a 1,25 % + 0,10 % = 1,35 % de folleto |

## 5. Historial

- 27/11/2026 — creación. Consultas a Finect (fichas y tablas de clases), financial-hub, r4.com,
  invertirindexado y finantres; fichas MCP `get_funds` del 25/11/2026.

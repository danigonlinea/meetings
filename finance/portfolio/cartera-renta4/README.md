---
title: "Cartera Renta 4: cómo funciona esta carpeta"
date: 2026-11-02
type: reference
category: finance
tags: [cartera, renta4, indice, proceso]
status: living
---
# Cartera Renta 4: cómo funciona esta carpeta

La cartera de Renta 4 Banco (34.769,20 €; cuatro fondos a 02/11/2026, seis en la propuesta vigente). Es independiente de `../cartera-myinvestor/`:
no comparte saldos, ni propuesta, ni cifras.

| Fichero | Rol | ¿Se edita? |
| --- | --- | --- |
| `cartera-actual.md` | **Foto congelada** del estado a 02/11/2026: saldos, pesos, OGC, look-through, duración estimada | **No.** Un cambio de saldos genera `cartera-actual-YYYY-MM-DD.md` |
| `propuesta-actual.md` | **La propuesta vigente (21/11/2026)**: seis fondos sin indexados, Kaizen al 25 %, Sigma 26,08 %, Magallanes 12 %, Akira 8 %, RF R 17,93 % y 6 Meses 10,99 %; RV 50 %, 393,02 €/año, 3,71 % neto y seis traspasos | **Sí** |
| `propuesta-80-20.md` | **Alternativa atrevida 80/20 (26/11/2026, 7–8 años)**: cinco fondos con indexado + value + small caps globales, Kaizen al 15 % y 10 % de pólvora seca, sin Akira; RV 80,48 %, 297,97 €/año (0,857 %), 4,99 % neto neutro y seis traspasos. Pendiente de decidir si sustituye a `propuesta-actual.md` | **Sí** |
| `propuesta-neon.md` | **Propuesta definitiva Neon «Cero Solape con Kaizen» 84/16 (27/11/2026, 7–8 años)**: síntesis ganadora tras revisión adversarial en cinco fondos y cuatro gestoras (`Fidelity World 46 %`, `Robeco BP Value 20 %`, `Vanguard EM 14 %`, `Kaizen 10 %`, `R4 6 Meses 10 %`), sin Akira; RV 83,79 %, **224,03 €/año (`0,644 %` con IVA en custodia)**, 5,33 % neto neutro y seis traspasos | **Sí** |
| `propuesta-2026-11-02.md` | **Historial**: la auditoría y la propuesta v2 del 02/11/2026 (Kaizen al 25 % y 3.618 € a un indexado). Superada el 21/11/2026. Se conserva por su análisis de la renta fija y la clase de Fidelity verificada | **No** |

## Estado a 02/11/2026

- **Foto:** 15,3% RV / 70,2% RF / 13,3% liquidez / 1,2% otros. 0,83% de coste (287 €/año).
  65,7% del patrimonio en bonos corporativos; Kaizen es el 35,4% de la cartera.
- **Diagnóstico:** concentración en crédito corporativo euro, un fondo de 2025 haciendo de RV + RF +
  liquidez, y 15,3% de RV que no cubre la inflación del 3,8%.
- **Propuesta vigente (21/11/2026, sin indexados):** Kaizen 25 %, Sigma Internacional 26,08 %, Magallanes
  European 12 %, Akira 8 %, RF R 17,93 % y 6 Meses 10,99 %. **RV 50 %, 393,02 €/año (1,130 %), caída −7.315 €
  y 3,71 % neto** (3,22 % con comisión de éxito). Seis traspasos y 0 € de impuestos.

## Pendiente

- **Adoptar la propuesta** (`propuesta-actual.md`): si se adopta, `propuesta-2026-11-02.md` queda como historial.
- **Decidir el peso de Akira**: 8 % (propuesto) o 0 %; su hueco iría a Sigma y al crédito corto.
- **Decidir el nivel de RV**: 50 % (propuesto, caída −7.315 €) o 40 % con las mismas líneas.
- Verificar la **custodia de Akira** en R4 y la **comisión de suscripción de AXA** antes de la orden 1.
- Confirmar ISIN de Sigma y Magallanes en pantalla y verificar el OGC real de Kaizen (0,96 % publicado vs
  1,25 % + 0,10 % declarados).

## Reglas de esta carpeta

- Las cifras de esta carpeta no se consolidan con las de MyInvestor. Si se quiere la vista conjunta,
  va en un documento aparte con su fecha.
- Todo se ejecuta por **traspaso entre fondos armonizados**, nunca por reembolso.
- Nada se mueve sin verificar antes la clase del fondo y su coste real en Renta 4.

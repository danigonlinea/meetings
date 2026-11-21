---
title: "Cartera Renta 4: cómo funciona esta carpeta"
date: 2026-11-02
type: reference
category: finance
tags: [cartera, renta4, indice, proceso]
status: living
---
# Cartera Renta 4: cómo funciona esta carpeta

La cartera de Renta 4 Banco (34.769,20 € en cuatro fondos). Es independiente de `../cartera-myinvestor/`:
no comparte saldos, ni propuesta, ni cifras.

| Fichero | Rol | ¿Se edita? |
| --- | --- | --- |
| `cartera-actual.md` | **Foto congelada** del estado a 02/11/2026: saldos, pesos, OGC, look-through, duración estimada | **No.** Un cambio de saldos genera `cartera-actual-YYYY-MM-DD.md` |
| `propuesta-actual.md` | **La propuesta viva a corto**: veredicto, problemas, rangos de mejora (4 niveles), recomendación, órdenes, descartes y límites | **Sí** |
| `propuesta-largo-plazo.md` | **La propuesta a largo plazo (21/11/2026)**: Kaizen al 25 %, RV del 15 % al 50 %. **Vigente: la variante sin indexados de §11** (Sigma Internacional 26,08 %, Magallanes European 12 %, Akira 8 %, RF R 17,93 % y 6 Meses 10,99 %; 393,02 €/año). §3-§4 quedan como referencia del precio de ese mandato. **No sustituye a `propuesta-actual.md`** hasta que el titular la adopte | **Sí** |

## Estado a 02/11/2026

- **Foto:** 15,3% RV / 70,2% RF / 13,3% liquidez / 1,2% otros. 0,83% de coste (287 €/año).
  65,7% del patrimonio en bonos corporativos; Kaizen es el 35,4% de la cartera.
- **Diagnóstico:** concentración en crédito corporativo euro, un fondo de 2025 haciendo de RV + RF +
  liquidez, y 15,3% de RV que no cubre la inflación del 3,8%.
- **Propuesta (v2):** **Kaizen se queda**; se recorta del 35,4% al 25% y los 3.618 € del recorte van a
  un indexado global. Queda en 21,2% de RV, 0,76% de coste (264 €/año) y caída esperada del −10,8%.
  Alternativas en la tabla de niveles (Kaizen al 30%, al 15%, y liquidez a RV).

## Pendiente

- **Decidir el nivel de RV a largo plazo** (`propuesta-largo-plazo.md` §2): 50 % (recomendado, caída
  −7.343 €) o 40 % (−6.043 €). Es la única decisión que cambia la cartera; el resto son consecuencias.
- **Decidir Akira**: 8 % en la variante sin indexados, o 0 % (su hueco iría a Sigma y al crédito corto).
- **Confirmar el mandato sin indexados**: si se mantiene, la cartera a ejecutar es la de §11 y la de §3 deja
  de ser operativa. Cuesta +164 €/año y −0,50 pp de esperanza frente a la indexada.
- Verificar la **custodia de Akira** en R4 y la **comisión de suscripción de AXA** antes de la orden 1.
- Confirmar el recorte de Kaizen: 25 % (recomendado en las dos propuestas) o 30 % (suave).
- Clase de Fidelity **verificada** en r4.com (30/10/2026): IE00BYX5NX33, mínimo 50 €, OGC 0,10% +
  custodia 0,19%.
- Verificar el OGC real de Kaizen (0,96% publicado vs 1,25% + 0,10% declarados).

## Reglas de esta carpeta

- Las cifras de esta carpeta no se consolidan con las de MyInvestor. Si se quiere la vista conjunta,
  va en un documento aparte con su fecha.
- Todo se ejecuta por **traspaso entre fondos armonizados**, nunca por reembolso.
- Nada se mueve sin verificar antes la clase del fondo y su coste real en Renta 4.

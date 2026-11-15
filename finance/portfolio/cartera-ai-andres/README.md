# Cartera-ai-andres

Cartera de **200.000 €** diseñada por el agente el 15/11/2026 con criterio propio y la experiencia de
Andrés (La Pizarra de Andrés) como material de estudio. **No es una copia de la cartera de Andrés** ni
una segunda versión de `cartera-ai/`: es una cartera distinta, con otro mandato y otro resultado.

## Documentos

| Archivo | Qué es |
| --- | --- |
| `cartera-actual.md` | Foto inicial del 15/11/2026: liquidez y cero posiciones. Congelada. |
| `propuesta-actual.md` | El diseño completo: 14 fondos con ISIN, pesos, coste, órdenes, descartes y señales de revisión. |

## Reglas

- **Solo fondos del catálogo de MyInvestor**, verificados por ISIN contra el MCP. Ninguna ISIN sin
  comprobar entra en la propuesta.
- **Solo clases de acumulación** (`distributing = 0`) y **sin ETF**: el traspaso entre fondos no tributa
  y es lo que permite rebalancear.
- **El % de RV se mide por look-through**, con el `alloc_equity` de cada ficha. Un mixto etiquetado como
  renta fija puede llevar un 43 % de bolsa dentro.
- **Lo que la ficha no publica va `no publicado`.** Nunca un TER, una comisión o un peso inventado; lo
  derivado se marca como derivado y lo estimado, como estimación.
- **No se consolida** con `cartera-myinvestor/`, `cartera-renta4/`, `cartera-ai/` ni con
  `cartera-de-andres/`.
- **No es consejo.** La propuesta es del agente; la decisión es del titular.

## Actualización

1. Cuando se ejecute, la foto nueva se crea como `cartera-actual-YYYY-MM-DD.md` con los saldos reales y
   la de hoy se conserva.
2. Si cambia un fondo (soft close, cambio de gestor, TER nuevo), se anota en `propuesta-actual.md` §9 y
   se fecha.
3. `python3 tools/build_index.py && python3 tools/verify.py` después de cualquier cambio.

## Estado

- **15/11/2026:** propuesta cerrada, sin ejecutar. 200.000 €, 14 fondos, 60,0 % de RV por look-through,
  1.016,20 €/año verificados (0,51 %) y 1.336-1.496 € si los dos fondos sin TER publicado costaran un
  1,0-1,5 %. Pendientes: horizonte real, coste de Myinvestor Value y Kaizen, y si el titular quiere un
  bloque de acciones (el diseño no lo lleva).

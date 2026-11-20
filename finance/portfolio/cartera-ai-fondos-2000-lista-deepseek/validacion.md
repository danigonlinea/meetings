---
title: "Validación — cartera-ai-fondos-2000-lista-deepseek"
date: 2026-11-20
type: reference
category: finance
tags: [cartera, validacion, cartera-ai-fondos-2000-lista-deepseek]
status: living
---

# Validación

Todo lo de esta página se comprueba **parseando el markdown ya escrito** de los cinco documentos,
no el diccionario que los generó: si una tabla está mal, el test falla.

## Cuadre y coste

| Cartera | Líneas | Total | Coste anual | TER medio | RV real |
| --- | --: | --: | --: | --: | --: |
| C1 | 8 | 100.000 € | 129,20 € | 0,1292 % | 69,47 % |
| C2 | 8 | 100.000 € | 1.434,40 € | 1,4344 % | 97,60 % |
| C3 | 7 | 100.000 € | 492,90 € | 0,4929 % | 55,05 % |
| C4 | 8 | 100.000 € | 607,60 € | 0,6076 % | 34,06 % |
| C5 | 6 | 100.000 € | 764,60 € | 0,7646 % | 99,48 % |

- **37 líneas, 37 ISIN distintos, 37 fondos distintos.**
- Cada línea: €/año = importe × TER, y % de la base = importe / 100.000. Comprobado línea a línea.
- Cada primera orden despeja el mínimo inicial del fondo (comparado contra el importe de su línea).

## ✅ Sin errores

Cuadre, coste, porcentajes, mínimos, unicidad de ISIN y de nombre normalizado: todo pasa.

## Unicidad

Comprobada de tres formas: ISIN exacto, nombre normalizado (sin «Fund», «FI», clase ni divisa) y
raíz de nombre por gestora, para cazar clases hermanas del mismo fondo.

- ISIN: 37 distintos sobre 37 líneas.
- Nombres normalizados: 37 distintos sobre 37 líneas.
- Avisos de posible clase hermana: 1. El único que queda (`IE00BD0NC144` deuda
  ligada a la inflación frente a `IE00BD0NC037` deuda nominal) es un falso positivo: son índices distintos,
  no clases del mismo fondo. El test **sí cazó un duplicado real** en la primera pasada — el iShares
  Emerging Markets D Acc de C1 y el Institutional Acc de C5 eran dos clases del mismo fondo — y C5 se
  rehizo para eliminarlo.

## Verificación de plataforma (MCP MyInvestor, 20/11/2026)

54 ISIN en 8 llamadas `get_funds`. De los 37 elegidos, todos tienen `distributing: 0`.
Los hallazgos que cambiaron el diseño:

| Fondo | Hallazgo | Efecto |
| --- | --- | --- |
| Vanguard U.S. 500 Investor `IE0032620787` | soft close | se sustituye por la clase Institutional `IE0032126645` |
| Okavango Delta A `ES0167211038` | soft close | fuera de C2 |
| Dodge & Cox Global Stock `IE00B55JMJ98` | mínimo 50.000 € | fuera, pese a ser el global más barato |
| BlueBox Technology I 150.000 € y Algebris Financial Equity I 500.000 € | mínimos inalcanzables | fuera de C5 |

## Solape con las carteras hermanas

6 de 37 líneas coinciden con alguna de las dos carpetas hermanas del mismo encargo:

| ISIN | Aquí | En la hermana |
| --- | --- | --- |
| `IE00BD0NC144` | C1 | cartera-ai-fondos-2000-lista-glm/C3 |
| `LU0329355670` | C2 | cartera-ai-fondos-2000-lista/C2 |
| `IE00BLP5S460` | C4 | cartera-ai-fondos-2000-lista/C4 |
| `IE00BD2B9710` | C4 | cartera-ai-fondos-2000-lista/C4 |
| `IE00BD0NC037` | C4 | cartera-ai-fondos-2000-lista-glm/C3 |
| `IE00BYSJTY39` | C5 | cartera-ai-fondos-2000-lista-glm/C4 |

El mandato solo exigía unicidad interna; se publica el cruce porque un lector del repositorio lo va a hacer igual.

*Validación regenerable; los datos de plataforma son del 20/11/2026.*

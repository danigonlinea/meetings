---
name: cartera-andres
description: Usar cuando se ingiera un vídeo de resultados mensuales de La Pizarra de Andrés o cuando haya que actualizar, consultar o analizar la cartera personal del canal (finance/portfolio/cartera-de-andres/).
---

# Cartera de Andrés

## Metadatos

- Carpeta: `finance/portfolio/cartera-de-andres/`.
- Vigente: `cartera-actual.md` (`status: living`). Histórico: `anteriores/` (`status: superseded`).
- Fuente de verdad: los `summary.md` de `finance/videos/la-pizarra-de-andres/YYYY-MM-DD-*/`.
- Script de cierre: `python3 tools/build_index.py && python3 tools/verify.py`.
- Esta skill **no decide** nada sobre la cartera del dueño ni propone réplicas. Documenta y analiza una
  cartera de un tercero.

## Cuándo se dispara

- Se acaba de ingerir un vídeo de La Pizarra cuyo título o contenido sea de resultados mensuales.
- El usuario pregunta por la cartera de Andrés, sus posiciones, sus pesos o su histórico.

## Paso 1: leer el vídeo

Del `summary.md` recién ingerido, extraer **solo lo que el hablante dice**:

| Campo | Dónde suele estar |
| --- | --- |
| Patrimonio de la cuenta | «Cifras y datos citados» |
| Rentabilidad del mes y del MSCI World | «Resumen ejecutivo» |
| Desde inicio / base 100 / ventaja vs índice | «Cifras y datos citados» |
| Cambios de posiciones (entradas y salidas) | «Resumen ejecutivo» y «Lo que el vídeo descarta» |
| Fondos nombrados y cifras | «Fondos y acciones mencionados» |
| Pesos declarados | raros: buscar «%», «peso», importes |

Reglas de precisión del repo, sin excepción:

- **Ningún peso inventado.** Si no hay cifra, `no publicado`. Si se calcula desde un importe declarado,
  marcar **derivado** con la fórmula.
- **Una mención no es una recomendación.**
- **Las cifras que no cuadran se conservan** y se listan en la sección de inconsistencias.
- Cada dato lleva el minuto y el vídeo del que sale.

## Paso 2: archivar la versión vigente

```bash
cp finance/portfolio/cartera-de-andres/cartera-actual.md \
   finance/portfolio/cartera-de-andres/anteriores/YYYY-MM-DD-resultados-<mes>.md
```

En la copia: cambiar `status: living` por `status: superseded`, ajustar `date` a la fecha del vídeo y
el `title`, y añadir al final la línea `> Sustituida por la foto de <mes> (<archivo>).`

Nunca se edita una foto archivada para «actualizarla»: si un dato se corrige, se corrige en la vigente
y se deja constancia.

## Paso 3: reescribir `cartera-actual.md`

1. `title`, `date` y `source` con el vídeo nuevo.
2. §1 composición: añadir, quitar o renombrar vehículos; actualizar importes y pesos declarados.
3. §2 serie mensual: una fila nueva. No reescribir las filas anteriores.
4. §3 cambios: una fila si hubo entrada o salida, con motivo declarado.
5. §4 señales: revisar si cambia la concentración o el solapamiento.
6. §5 inconsistencias: añadir las del mes.

## Paso 4: cerrar

```bash
python3 tools/build_index.py
python3 tools/verify.py
```

Si `verify.py` da error, no se sube: se arregla o se deja escrito qué falta.

## Pitfalls

- **No confundir esta cartera con `cartera-myinvestor/`.** Son patrimonios distintos; la de Andrés no
  se suma, no se rebalancea y no se compara con la del dueño.
- **No completar pesos por inferencia silenciosa.** El bloque de acciones ha dado cifras
  contradictorias (Nextil 50.000 € frente a «100.000 € en acciones»); ambas se conservan marcadas.
- **El fondo de energía de Robeco salió en junio de 2026** y no debe reaparecer como posición actual.
- **Horos:** la clase no está verificada (Value Nacional en junio, Internacional en el traspaso,
  «value español» en agosto). No fijar una clase sin respaldo.
- **Los vídeos de tertulia del canal no son resultados** y no actualizan la ficha: solo los de la serie
  mensual.

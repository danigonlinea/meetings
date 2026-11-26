---
name: revision-cartera
description: Usar cuando toque la revisión trimestral de una cartera o cuando el usuario pregunte "¿toca cambiar el % de RV?". Revisa cada cartera contra sus propios criterios y escribe la revisión; no puntúa señales y no decide.
---

# Revisión de la cartera

## Metadatos

- Carpeta: `finance/portfolio/`. Cada cartera viva tiene su propio fichero: `cartera-myinvestor/`,
  `cartera-renta4/` y `cartera-ai-propuesta/` (la Opción A del ranking del 26/11/2026). Los diseños
  descartados o a estudio no se revisan aquí: viven en `finance/laboratorio-carteras/`.
- Salida: `finance/portfolio/revision-YYYY-QN.md` con `type: portfolio-review`.
- Esta skill **no decide** el % de RV ni ejecuta órdenes. Ordena los hechos y escribe la revisión.

## Regla de oro

**Las carteras son independientes y lo único que las distingue es el criterio que siguen.** No hay medidor
común, ni índice de temperatura, ni puntuación de señales que mueva el % de renta variable. El % es una
decisión del dueño y se cambia con un argumento escrito y fechado.

No inventes un instrumento para justificar un cambio. Si el dueño quiere cambiar el %, escribe el argumento
(horizonte, liquidez, tolerancia, coste, estilo) y la fecha; el número es suyo.

## Paso 1: Fija el criterio de cada cartera

Antes de mirar ningún dato, escribe en la revisión **qué criterio sigue cada cartera**, sacado de su propio
documento y no de una plantilla:

| Cartera | Criterio que sigue | Qué la haría cambiar |
| --- | --- | --- |
| `cartera-myinvestor/` | 55/45 en diez fondos solo, coste real mínimo, colchón fuera | Que cambie el horizonte, la necesidad de liquidez o la tolerancia declarada |
| `cartera-renta4/` | Auditoría de una cuenta heredada: recortar el peso en bonos corporativos | Que se ejecute el recorte o cambie la clase de destino |
| `cartera-ai-definitivas-estudiar/cartera-ai-andres/<talla>.md` | Criterio de Andrés: núcleo indexado pequeño, gestión activa, RF y liquidez | Que cambie el mandato, el horizonte o el coste de un vehículo |

Si una cartera no tiene criterio escrito, eso es el hallazgo de la revisión: se escribe antes de proponer
nada.

## Paso 2: Comprueba los hechos de cada cartera

Solo datos con fuente y fecha; sin dato, `no verificado`:

- **Posiciones y pesos** de su fichero, contra las fichas de la plataforma (MyInvestor MCP o Renta 4).
- **Coste real** (TER + comisiones de la plataforma) y si alguna clase ha cambiado de precio.
- **Deriva de pesos**: qué bloque se ha separado más de 5 pp de lo escrito.
- **Caída asumida** con las dos fórmulas de la cartera: −(40 % × RV + 3 % × RF) y el caso estresado.
- **Vehículos**: *soft close*, cambio de gestor, cambio de política, historial que ya se puede juzgar.

## Paso 3: Escribe la revisión

`finance/portfolio/revision-YYYY-QN.md`, con estas secciones:

1. **Criterio de cada cartera** (tabla del Paso 1, actualizada).
2. **Hechos que han cambiado** desde la revisión anterior, con fuente y fecha.
3. **Qué se separa de su criterio**, cartera por cartera. Si nada, se dice.
4. **Qué se propone** y qué costaría en caída y en retorno.
5. **Lo que no se puede saber** con los datos de hoy.
6. **Decisión del dueño**: el % de RV y si se ejecuta. Nunca lo rellenes tú.

## Paso 4: Cierra

```bash
python3 tools/build_index.py && python3 tools/verify.py
```

Actualiza el estado en `finance/portfolio/README.md` solo si el dueño aprueba el cambio. Si no hay decisión,
el estado sigue siendo el vigente.

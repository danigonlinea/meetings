# Cartera de Andrés

Cartera **personal de un tercero**: la que Andrés (La Pizarra de Andrés) publica cada mes en su canal.
Se guarda aquí para analizarla, no para replicarla ni para mezclarla con las carteras del dueño.

## Documentos

| Archivo | Qué es |
| --- | --- |
| `cartera-actual.md` | La foto vigente, siempre la última. Si lees un solo archivo, es este. |
| `anteriores/` | Una foto por mes cerrado, congelada. No se editan: cuando cambia la cartera, se archiva la versión anterior aquí. |

## Reglas

- **Un dato, un sitio.** Los importes y pesos viven en `cartera-actual.md`; el histórico, en
  `anteriores/`.
- **Ningún peso inventado.** Andrés no publica pesos por fondo. Lo que no dice va `no publicado`; lo
  que se calcula a partir de cifras declaradas va marcado **derivado**.
- **Toda cifra lleva su vídeo y su minuto.** Sin transcripción que lo respalde, no entra.
- **Las inconsistencias se conservan**, no se corrigen ni se promedian (§5 de `cartera-actual.md`).
- **No se consolida** con `cartera-myinvestor/` ni con `cartera-renta4/`: son patrimonios distintos y
  esta es una referencia externa.
- **No es consejo.** El autor avisa de que su cartera no es replicable; esta carpeta documenta, no
  propone.

## Actualización

Cuando se ingiere un vídeo de resultados mensuales:

1. Leer el `summary.md` del vídeo y extraer: patrimonio, rentabilidad del mes, MSCI World, desde
   inicio, cambios de posiciones, fondos nombrados y cifras nuevas.
2. Archivar la versión vigente en `anteriores/YYYY-MM-DD-resultados-<mes>.md` con
   `status: superseded`.
3. Reescribir `cartera-actual.md` con la foto nueva.
4. `python3 tools/build_index.py && python3 tools/verify.py`.

El procedimiento completo está en la skill `.agents/skills/cartera-andres/SKILL.md`.

## Serie disponible

| Mes cerrado | Foto | Vídeo |
| --- | --- | --- |
| Mayo 2026 | `anteriores/2026-05-31-resultados-mayo.md` | `2026-05-31-demasiada-rentabilidad-para-ser-verdad-resultados-de-mayo` |
| Junio 2026 | `anteriores/2026-07-02-resultados-junio.md` | `2026-07-02-el-mercado-empieza-a-ralentizarse-peligro-resultados-de-junio` |
| Julio 2026 | `anteriores/2026-08-02-resultados-julio.md` | `2026-08-02-batiendo-a-los-mercados-globales-resultados-de-la-cartera` |
| Agosto 2026 | `anteriores/2026-09-01-resultados-agosto.md` | `2026-09-01-sigue-siendo-mi-cartera-mejor-que-los-indices-resultados` |
| Septiembre 2026 | `anteriores/2026-10-02-resultados-septiembre.md` | `2026-10-02-que-ha-pasado-con-la-cartera-nuestro-peor-mes-resultados` |
| Octubre 2026 | **vigente**: `cartera-actual.md` | `2026-11-01-estoy-perdiendo-dinero-con-mis-inversiones-resultados-octubre` |

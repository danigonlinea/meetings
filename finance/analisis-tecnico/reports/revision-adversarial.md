---
title: "Revisión adversarial del método de análisis técnico"
date: 2026-11-05
type: synthesis
category: finance
tags: [analisis-tecnico, revision-adversarial, veredicto, trading, evidencia]
status: living
---

# Revisión adversarial

Objeto: el método de análisis técnico documentado en las 10 clases del 26/10–04/11/2026 y en las 4 piezas
explicativas del canal (añadidas el 05/11 para tener las definiciones que las clases dan por sabidas).
Corpus: 14 vídeos, ~85.000 palabras. Escala: independiente de `finance/la-pizarra-de-andres/` y de la
cartera; aquí solo se juzga el método.

## Veredicto en una línea

**La estructura es buena y la evidencia no existe:** el orden de análisis y la disciplina de ejecución son
los de un operador profesional, pero las «leyes» con las que se vende el método no sobreviven a una prueba
con datos — una es una tautología y la otra se cae al quitar el solape.

---

## 1. Lo que sí es sólido (steelman)

Hay que decirlo antes de atacar, porque el esqueleto es defendible:

1. **Orden top-down correcto.** Mensual → semanal → sesión → gatillo. Es exactamente el orden que enseña
   cualquier libro serio de análisis multi-temporal; él lo aplica sin saltárselo.
2. **Perfilar la sesión antes de mirar el precio.** Separar premarket no oficial (4:00-7:00), oficial
   (7:00-9:30) y campana, con máximo, mínimo y probabilidad de cada tramo, es una práctica real de mesa
   institucional. Es lo más valioso del corpus.
3. **Confluencia como filtro.** Exige que el nivel coincida con banda, histórico o media antes de entrar.
   Eso evita el 90 % de las entradas por corazonada.
4. **Disciplina de ejecución.** Stop-limit en vez de mercado (la vela de apertura negocia máximo y mínimo
   en segundos), trailing en lugar de objetivo fijo cuando hay noticia, cierre escalonado por tercios,
   «si el término cambia, se cierra». Esto es gestión de riesgo de verdad.
5. **Rechazo explícito del relato fácil:** «no se vende en el piso», «no se abre dentro del rango»,
   «no se compra la libélula en entorno negativo». Son tres errores clásicos del minorista y los tres
   están prohibidos en el método.

## 2. Los ataques, con números

### 2.1 «La anomalía se cierra siempre, con un 100 % de certeza»

Es la piedra angular: si el precio vuelve al punto donde se cruzaron las medias, la posición perdedora
tiene un cierre objetivo. Se probó con datos diarios de 10 años: tras cada cruce EMA3/EMA9, ¿el precio
revisita el nivel del cruce?

| Activo | Cruces | Vuelve en 10 velas | **Control** (nivel cualquiera) | Vuelve en 20 velas | **Control** |
|---|--:|--:|--:|--:|--:|
| NVDA | 275 | 93 % | **93 %** | 95 % | **95 %** |
| AMZN | 295 | 94 % | **96 %** | 95 % | **97 %** |
| MSFT | 290 | 97 % | **93 %** | 97 % | **96 %** |
| BTC-USD | 388 | 99 % | **98 %** | 99 % | **98 %** |
| SPY | 267 | 93 % | **90 %** | 95 % | **93 %** |

**El hallazgo:** el nivel del cruce se revisita tanto como cualquier nivel arbitrario del mismo día. La
frase «cierra con un 100 % de certeza» es literalmente verdadera y **completamente inútil**: en series que
oscilan, casi cualquier precio reciente se vuelve a tocar en 10-20 velas. No es una ley del mercado, es
aritmética del ruido. Y él la usa para justificar mantener una posición perdedora («no tengo cierre»).

### 2.2 «La primera vela decide la dirección del día»

Probado con velas horarias de dos años (724 sesiones por activo):

| Activo | Acierto bruto | **Sin solape** (1ª hora vs resto del día) |
|---|--:|--:|
| SPY | 72 % | **55 %** |
| NVDA | 77 % | **51 %** |
| AMZN | 75 % | **51 %** |
| BTC-USD | 56 % | **51 %** |

**El hallazgo:** el 72-77 % es un artefacto —la primera hora forma parte del día, así que «acierta» por
construcción—. Quitando el solape queda una moneda al aire. La regla **no predice**: describe lo que ya
pasó.

### 2.3 Los niveles son buenos; los escenarios, no

De `predicciones.md`: **16 de 19 predicciones comprobables se cumplieron**, y casi todas son niveles
intradía al centavo (aperturas de NVDA con 3-8 centavos de error, 219,19 exacto, 77.000 de Bitcoin al
dólar). Los tres fallos y el error grave son de dirección a varios días:

- el rango **77.000-81.000** de Bitcoin se tocó por los dos lados y **se rompió por abajo** (05/11: 75.919);
- la ruptura de **220,19** en NVDA no llegó (máximo 219,99);
- del 02/11 al 05/11 NVDA cayó de 207 a **181,60 (−12 %)** sin aviso.

Ninguna de esas predicciones publicadas lleva **stop**. Un nivel sin invalidación no es una operación, es
una opinión con decimales.

### 2.4 Un error de categoría: «delta neutral»

El vídeo explicativo define bien el delta neutral (opciones, delta ≈ 0, theta, gamma, *iron condors*) y
**dos minutos después** llama «modelo delta neutral» a un sistema **direccional intradía en acciones**.
Son opuestos: una posición delta neutral es insensible a la dirección; el modelo que describe apuesta a
que el precio cae. Cuando un método confunde su propia terminología, el resto de las etiquetas deja de ser
información y pasa a ser marca.

### 2.5 Jerga que sustituye a la definición

«Ley quero», «GPS quero», «trinchera estelar», «arco catenario», «identidad Gaudí», «unidad 12»,
«consenso del Coliseo», «Hércules». Ninguna se define con una fórmula en 14 vídeos. Cuando algo no se
puede escribir como condición, no se puede verificar ni enseñar: solo se puede creer.

### 2.6 Evidencia circular

En el vídeo de los tres tercios, la prueba de que el escenario bajista es correcto es que **él está al
100 % en corto** y que existe una «unanimidad del Coliseo». La posición del que enseña no valida el
análisis; es al contrario, el análisis debería validar la posición.

### 2.7 Sesgo de publicación

Cuatro de las diez clases están dedicadas, total o parcialmente, a **celebrar el *call* del 26/10**. No hay
ni una clase dedicada a revisar un fallo. En el propio corpus, el rango de Bitcoin se rompió y el tema no
se retoma.

### 2.8 Lo que parece propio es el toolbox estándar

EMA 3/9/20/50/200, Parabolic SAR de Wilder (0,02/0,2), %B de Bollinger (lo llama «ley estelar número dos»),
tercios de Fibonacci, retroceso a la media, *measured move*. Todo es instrumental público y bien
documentado. **Su aportación real es el ritual de preparación y el vocabulario, no el indicador.** Eso no
es un defecto —un método es a menudo un ritual que hace disciplinado a un operador—, pero desmonta la
pretensión de «matemática pura» y de método cuantitativo propio.

### 2.9 Cuatro de las once piezas son anuncios

Los vídeos cortos (tercios, polaridad, leyes estelares, delta neutral) dedican entre un 30 % y un 40 % de
su duración a la «beca completa» y a «la comunidad educativa más grande de YouTube, Instagram y TikTok».
Se han ingerido igualmente porque contienen las definiciones que las clases no dan, pero **no son material
formativo: son contenido comercial**.

## 3. Qué queda en pie

| Componente | Veredicto | Por qué |
|---|---|---|
| Orden top-down (mensual → intradía) | **Se queda** | Coherente con la práctica profesional |
| Perfilado de la sesión por ventanas | **Se queda** | Aportación real y operativa |
| Confluencia de niveles | **Se queda** | Filtro razonable, reduce entradas impulsivas |
| Ejecución stop-limit / trailing / cierre por tercios | **Se queda** | Gestión de riesgo correcta |
| «Prohibido vender en el piso» / no operar el rango | **Se queda** | Evita los tres errores clásicos del minorista |
| La «anomalía» como cierre garantizado | **Se descarta** | Indistinguible de un nivel cualquiera (test 1) |
| «La primera vela decide la dirección» | **Se descarta como predicción** | 51-55 % sin solape (test 2) |
| Las «leyes estelares» y su vocabulario | **Se descarta** | Sin fórmula verificable en 14 vídeos |
| «Delta neutral» aplicado a un modelo direccional | **Se descarta** | Error de categoría |
| Predicciones sin stop | **Se descarta** | No son operaciones, son opiniones |

## 4. Cómo se arreglaría (tres cambios)

1. **Convertir cada regla en hipótesis con muestra y control.** «La anomalía se cierra» pasa a «el precio
   revisita el nivel del cruce en X % de los casos, frente a Y % de un nivel arbitrario». Con eso se
   descubre que no aporta, y se deja de usar como razón para no cerrar una pérdida.
2. **Toda predicción con stop y tamaño.** Sin invalidación y sin euros por operación no hay forma de
   calcular expectativa; es lo que separa un método de un pronóstico.
3. **Separar formación de marketing y renombrar la jerga.** Un método que se enseña con nombres comerciales
   no se puede auditar por terceros.

## 5. Recomendación práctica

**Usa el proceso, no las leyes.** El valor transferible son las cuatro primeras filas de la tabla del §3:
preparar la sesión, mapear confluencias, ejecutar con órdenes limitadas y no perseguir el precio. Todo lo
que venga envuelto en «certeza», «ley» o nombre propio se queda fuera hasta que se pueda medir.

## 6. Cómo se han hecho las pruebas (reproducible)

- **Datos:** `query2.finance.yahoo.com/v8/finance/chart/<TICKER>` (sin crumb), diario a 10 años y horario a
  730 días. Activos: NVDA, AMZN, MSFT, SPY, BTC-USD.
- **Test 1:** EMA3 y EMA9 sobre cierre; en cada cruce se toma el cierre de esa vela como nivel y se comprueba
  si el máximo (cruce bajista) o el mínimo (cruce alcista) lo alcanza en 5, 10 y 20 velas. Control: mismo
  número de barras aleatorias, nivel = cierre de esa barra, dirección aleatoria.
- **Test 2:** barras horarias agrupadas por sesión; retorno de la primera hora frente al retorno del día
  (con y sin solape) y frente al retorno del **resto** del día.
- **Límites:** muestra de 5 activos y dos años de horario; no cubre intradía de 1 minuto, que es donde él
  opera. Los tests desmienten las dos reglas **como afirmaciones generales**, no prueban que su operativa
  de 1 minuto no funcione: simplemente, no hay datos públicos para probarla y él no los publica.

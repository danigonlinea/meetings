---
title: "Propuesta-perplexity: cartera de 100.000 € desde cero (MyInvestor)"
date: 2026-11-04
type: portfolio-proposal
category: finance
tags: [cartera, propuesta, myinvestor, 100k, indexados, renta-fija, reits, emergentes, japon, escenarios]
status: draft
related:
  - finance/portfolio/cartera-myinvestor/cartera-actual.md
  - finance/portfolio/cartera-myinvestor/propuesta-actual.md
  - finance/reports/sintesis-inversor-2026-10-30.md
  - finance/reports/informe-canal-la-pizarra-de-andres-2026-11-02.md
---

# Propuesta «perplexity» — 100.000 € desde cero

> **Qué es este fichero.** Un diseño **de cero** para 100.000 €, no una iteración de la cartera
> vigente. No sustituye a `propuesta-actual.md` (que sigue siendo la adoptada) ni mueve ninguna
> posición: si algún día se adopta, sus conclusiones se absorben allí y este anexo se borra. Como
> manda la carpeta, aquí no hay dos verdades: la foto real está en `cartera-actual.md` y la
> decisión vigente en `propuesta-actual.md`.
>
> **Cómo se ha construido.** Datos de ficha **MyInvestor vía MCP a 04/11/2026** (`get_funds`,
> NAV 30/10/2026) para los 12 fondos y para todos los candidatos de descarte: TER, comisiones,
> rentabilidades 3A/5A **anualizadas**, volatilidad 3A, SRRI, países, sectores, mínimo inicial y
> clase de acumulación. Datos de mercado a **03-04/11/2026** (BCE, Bund, EUR/USD, múltiplos).
> Todo lo que el MCP no publica va marcado como **estimado** en su casilla.
>
> **Corrección del 04/11/2026 (misma sesión).** Al abrir las posiciones reales de cada fondo
> (Anexo B) se cae **Sissener Corporate Bond**: su top-10 son bonos high yield de energía y shipping
> (Nynas 11,75 %, Golar LNG 7,75 %, W&T Offshore 10,75 %, McDermott 10,5 %), no crédito IG nórdico.
> Lo sustituye **iShares Euro Investment Grade Corporate Bond D Acc (IE00BDRK7J14, 0,12 %)**. Efecto:
> TER 0,229 % → **0,190 %**, duración 2,84 → **3,03 años**, y el bloque de crédito pasa a ser IG de
> verdad. Cifras actualizadas en §D, §E, §F y §G.
>
> **No es asesoramiento financiero.** Es una propuesta analítica; la idoneidad depende de la
> fiscalidad, la liquidez y el aguante real del titular.

---

## A. Diagnóstico actual de mercados (a 04/11/2026)

1. **El BCE sigue subiendo.** Facilidad de depósito **2,50 %**, MRO 2,65 %: segunda subida de 2026
   (septiembre). El mercado ya no descuenta recortes, descuenta que el 2,50 % es un suelo, no un techo.
2. **La inflación europea no ha vuelto al objetivo.** ≈**3,8 %** en la zona euro (último dato
   cruzado en `propuesta-actual.md`, 31/10/2026) frente a un tipo de depósito del 2,50 %: el tipo
   **real es negativo (~−1,3 %)**. El monetario cobra 2,2-3,0 % nominal y pierde poder adquisitivo.
3. **El Bund a 10 años está en 3,33 %** (03/11/2026), +0,68 pp en un año. La deuda pública europea
   vuelve a pagar; ya no es solo un refugio, es una fuente de rentabilidad.
4. **EE. UU. es el punto de tensión.** Treasuries por encima del 5 % a 10 y 30 años y **un tercio de
   la deuda venciendo en dos años** (Renta 4, 25:00, vía `sintesis-inversor-2026-10-30`). Cada
   refinanciación es una prueba de mercado.
5. **La bolsa americana no está cara por múltiplo, está cara por concentración.** S&P 500 a
   **18,1-18,7×** beneficio forward (03/11/2026; dos fuentes), cerca del percentil 19 de su rango a
   cinco años. El riesgo no es el precio medio: es que **diez compañías son ~la mitad del índice**
   (Ruiz, 1:04:59) y que tecnología pesa ~46 % del S&P (Andrés, 9:36). Comprar el índice es comprar
   una tesis sobre la IA.
6. **Europa y emergentes cotizan con descuento.** STOXX 600 ≈**13,6×**, MSCI EM ≈**10,2×** frente a
   18× de EE. UU. El *earnings yield* de Europa (≈7,4 %) duplica el del bono americano.
7. **El dólar está fuerte.** EUR/USD **1,1179** (03/11) y 1,1237 (04/11); el euro cede ~2,2 % en doce
   meses. Un inversor en euros que compra activos USA **no cubre**: el tipo de cambio es una pata
   más del retorno, y hoy juega a favor del activo americano, no del euro.
8. **El crédito no paga.** HY europeo con OAS ≈**363 pb** cuando el rango normal es 260-300 pb; BB a
   175 pb. Asumir riesgo de crédito para cobrar 60 pb de más no es una decisión de rentabilidad, es
   una decisión de fe.
9. **La renta fija corta de calidad vuelve a competir con la bolsa.** La RF corta IG de la cartera
   tiene TIR ≈**4,65 %** (ficha de gestora 30/09/2026) frente a un *earnings yield* del S&P del
   ≈5,5 %: el premio por arriesgar en bolsa es de **1-2 pp**, no de 4.
10. **La duración es la decisión, no el activo.** Un bono a 10 años con duración 7,5 pierde 7,5 % por
    cada +100 pb; el 30 años americano al 5,40 % tiene duración ~15 y volatilidad ~10 %, casi la de
    la bolsa (Renta 4, 15:35-15:48).
11. **Los gestores del canal están divididos y eso es información, no ruido.** Renta 4 ya está en la
    parte larga; Ábaco espera a que el crédito se abra (estanflación, 1,3-1,5 de duración); el value
    está al 100 % en bolsa. Tres diagnósticos parecidos, tres *trades* opuestos.
12. **Crédito privado y deuda ligada a la IA.** Ábaco da **60-70 % de probabilidad de evento de
    crédito en 6-12 meses**; CoreWeave ha caído ~50 % y su deuda pasó del 8-9 % al 15-16 % (Ruiz,
    57:26-58:29). El riesgo de cola no está en la bolsa grande, está en el apalancamiento.
13. **Geopolítica con dos focos abiertos** (Oriente Medio y aranceles) que se transmiten por el
    petróleo y las cadenas de suministro, no por los beneficios del trimestre.
14. **El escenario base no es ni recesión ni euforia: es lateral con tipos altos.** Con el premio de
    la RV en 1-2 pp, la cartera tiene que ganar por **carry, coste y diversificación**, no por acertar
    la dirección.
15. **Consecuencia para el diseño:** 45-50 % de RV como motor, 40 % de RF corta y de calidad que
    cobra 3,5-4,5 %, 15 % de liquidez con regla escrita y cero apuestas direccionales. El objetivo no
    es maximizar el retorno esperado, es **sobrevivir a los cuatro escenarios con el mismo dinero
    dentro**.

---

## B. Principios aplicados de «La Pizarra de Andrés»

Extraídos del corpus ya ingerido (`sintesis-inversor-2026-10-30`, `informe-canal-2026-11-02`). Son
**criterios del canal**, no recomendaciones personalizadas: Andrés avisa de que su cartera no es
replicable (07:50) y de que el riesgo real supera la volatilidad que mide (11:00).

| Principio | Dónde se dice | Cómo se aplica aquí | Dónde NO se sigue |
| --- | --- | --- | --- |
| **La indexación es la base, pero no es neutral** | Andrés 03:50 y 09:36; Ruiz 1:04:59 | 45.000 € de RV en índices; **EE. UU. al 39 % de la RV** frente al 72 % de un MSCI World puro | No se compra un S&P 500 ni un World a secas: el World va al 15 % y se diluye con Europa, Japón, EM y small caps |
| **El coste es lo único que se controla al 100 %** | Andrés 1:40-10:05 | TER ponderado **0,190 % = 190 €/año** sobre 100.000 € (45 % del capital a 0,10-0,29 %) | No se paga un 2,33 % de Cobas ni un 1,09 % de Fundsmith para comprar el mismo beta |
| **La duración es la decisión** | Renta 4 15:35; Ruiz 1:07:55-1:09:46 | Duración agregada de la RF **≈3,03 años**; +100 pb = **−1.665 €** (1,7 % de la cartera) | No se apuesta por el 20+ años ni por el 30 años americano |
| **No se cobra riesgo de crédito sin prima** | Ábaco 28:37 y 36:47 (vía síntesis) | Crédito solo **25 %** de la cartera y todo IG: corto (14), ABS (6), nórdico (5) | Fuera híbridos con 80 % de high yield escondido bajo etiqueta «mixto» |
| **La liquidez tiene regla escrita** | Andrés 23/10 | **15.000 €** en monetario (15 %), con uso definido (§H), no como ocurrencia | No se trata el colchón como si fuera cartera |
| **Lo pequeño está castigado y eso se paga con tiempo** | Andrés 02:25 | Small caps al **5 %** (11 % de la RV), no al 20 % | No se convierte el castigo en una apuesta: 5.000 € y fuera |
| **Japón aporta diversificación real** | Parages, webinar 20/10 | Fidelity MSCI Japan 4.000 € (**13 % de la RV**, el doble de su peso mundial) | Es la única sobreponderación por país y está declarada como tal, con límite 15 % |
| **Medir el proceso, no la racha** | Andrés 12:05 | Revisión trimestral con seis señales medidas (§H), no con titulares | No se rebalancea por un mes malo |
| **El value no se copia, se compara** | Andrés 05:24 (Cobas/AzValor «lo están haciendo muy bien») | Se descarta con el número delante: Cobas 2,33 % TER, Fundsmith 1,09 % con 3A +6,96 % | No entra ningún value activo: el estilo se compra a 0,10 % vía Europa |

---

## C. Arquitectura de cartera por bloques

Perfil: **moderado con sesgo de largo plazo**, horizonte 7-10 años, tolerancia a caídas del 15-20 %.

| # | Bloque | Función | % | € |
| --- | --- | --- | ---: | ---: |
| 1 | RV global desarrollada (World + Europa + Japón) | Motor de crecimiento, con sesgo deliberado fuera de EE. UU. | 27 % | 27.000 |
| 2 | RV emergentes | Crecimiento y descorrelación; valoración 10,2× | 7 % | 7.000 |
| 3 | RV small caps globales | Prima de tamaño y beta distinto al large cap | 5 % | 5.000 |
| 4 | Activos reales — REITs desarrollados | Renta inmobiliaria, cobertura parcial de inflación | 6 % | 6.000 |
| 5 | RF corta y crédito IG (corta + ABS + corporativo IG) | Carry 3,5-4,5 % con duración ≈2,9 | 25 % | 25.000 |
| 6 | RF gubernamental euro + ligada a inflación | Amortiguador en recesión y seguro de inflación | 15 % | 15.000 |
| 7 | Liquidez táctica (monetario) | Reserva para aportaciones y oportunidades | 15 % | 15.000 |
| | **Total** | | **100 %** | **100.000** |

**Por qué 45 % de RV y no 50 o 55.** El ancla es la caída, no el retorno. Con RV −40 % y RF −3 %
(un 2008 con crédito), la cartera pierde **−19,2 % (−19.200 €)**, justo en el borde alto de lo que el
titular dice aguantar. Con 50 % serían −21,5 % y con 55 %, −23,4 %: se gana 0,2-0,3 pp de retorno
esperado por cada 5 puntos y se pierden 2 pp de caída. Con un premio RV-bono de solo 1-2 pp (§A.9),
ese intercambio no compensa.

---

## D. Fondos seleccionados y asignación exacta

| # | Bloque | Fondo | ISIN | Gestora | € | % | TER |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| 1 | RV global | Fidelity MSCI World Index Fund EUR P Acc | IE00BYX5NX33 | Fidelity | 15.000 | 15,0 % | 0,12 % |
| 2 | RV Europa | Fidelity MSCI Europe Index Fund EUR P Acc | IE00BYX5MD61 | Fidelity | 8.000 | 8,0 % | 0,10 % |
| 3 | RV Japón | Fidelity MSCI Japan Index Fund EUR P Acc | IE00BYX5N771 | Fidelity | 4.000 | 4,0 % | 0,10 % |
| 4 | RV emergentes | iShares Emerging Markets Index Fund (IE) S Acc EUR | IE000QAZP7L2 | BlackRock | 7.000 | 7,0 % | 0,16 % |
| 5 | RV small caps | Vanguard Global Small-Cap Index Fund EUR Acc | IE00B42W4L06 | Vanguard | 5.000 | 5,0 % | 0,29 % |
| 6 | Activos reales | iShares Developed Real Estate Index Fund (IE) D Acc EUR | IE00BDRK7P73 | BlackRock | 6.000 | 6,0 % | 0,17 % |
| 7 | RF corta IG | Neuberger Short Duration Euro Bond Fund EUR U Acc | IE00BL1GVT98 | Neuberger Berman | 14.000 | 14,0 % | 0,38 % |
| 8 | RF ABS | Aegon European ABS Fund A EUR Acc | IE00BG226Z29 | Aegon | 6.000 | 6,0 % | 0,66 % |
| 9 | RF corporativa IG | iShares Euro Investment Grade Corporate Bond Index (IE) D Acc EUR | IE00BDRK7J14 | BlackRock | 5.000 | 5,0 % | 0,12 % |
| 10 | RF gubernamental | iShares Euro Government Bond Index Fund (IE) D Acc EUR | IE00BD0NC037 | BlackRock | 10.000 | 10,0 % | 0,10 % |
| 11 | RF inflación | iShares Euro Government Inflation-Linked Bond Index (IE) D Acc | IE00BD0NC144 | BlackRock | 5.000 | 5,0 % | 0,10 % |
| 12 | Liquidez | Groupama Trésorerie IC | FR0000989626 | Groupama | 15.000 | 15,0 % | 0,07 % |
| | | **TOTAL** | | | **100.000** | **100 %** | **0,190 %** |

**Comprobaciones de las restricciones:**

- Suma exacta: 15.000+8.000+4.000+7.000+5.000+6.000+14.000+6.000+5.000+10.000+5.000+15.000 = **100.000 €**.
- **12 posiciones** (rango pedido: 8-15). Ninguna por encima del **15 %** (máximo: World y Groupama, 15,0 %).
- **Gestora máxima: BlackRock 33 %** (EM + REITs + gubernamental + corporativo IG), Fidelity 26 %,
  Groupama 15 %, Neuberger 14 %, Vanguard 6 %, Aegon 6 %. Ninguna llega al 35 %.
- Todas las clases son de **acumulación** (`distributing = 0` verificado en `get_funds`).
- Todos los mínimos iniciales son **≤ 1 €** salvo Groupama (0,001 participaciones). Ninguno exige 10.000 €.

---

## E. Justificación de cada fondo (con la pega en la misma fila)

**1. Fidelity MSCI World (15 %).** Núcleo. 3A +18,7 %, 5A +11,0 % anualizados, vol 3A 11,4 %,
1.200 empresas, TER 0,12 %. **Pega:** 72 % EE. UU. y 30 % tecnología; por eso se queda en el 15 % y no
es la cartera entera. Alternativa más barata: iShares Developed World S (0,06 %) — se descarta
**solo** por concentración de gestora (habría dejado BlackRock al 34 %) y porque su clase no tiene 3A/5A
propios publicados. Diferencia de coste: 15 €/año.

**2. Fidelity MSCI Europe (8 %).** La sobreponderación con mejor respaldo de valoración (13,6×),
TER 0,10 %, vol 3A 10,4 %, 3A +16,5 %. Financials 23 %, industria 18 %, salud 14 %, tecnología solo 9 %:
es el contrapeso natural al World. **Pega:** 22 % Reino Unido y 16 % Suiza, así que **no todo es euro**;
y Europa crece poco: se compra barato, no se compra crecimiento.

**3. Fidelity MSCI Japan (4 %).** Diversificador real, TER 0,10 %, 3A +17,2 %, vol 3A 13,1 %.
Japón cotiza con descuento, tiene gobierno corporativo en mejora y una divisa que en escenarios de
aversión al riesgo se comporta distinto al dólar. **Pega:** con 4.000 € el peso en la RV sube al 13,2 %,
el doble de su peso mundial; es una **sobreponderación declarada**, con límite del 15 % de la RV.

**4. iShares Emerging Markets S Acc (7 %).** La clase más barata del fondo (0,16 %; la D cuesta 0,20 %),
mismo índice MSCI EM: 27 % Taiwán, 21 % Corea, 19 % China, 11 % India. 3A +20,1 % en la clase D.
**Pega doble:** **42 % tecnología** (es una apuesta tecnológica con otro nombre: TSMC y Samsung) y la
clase S **no publica 3A/5A propios**; se usa la D como referencia de comportamiento. Si el titular
prefiere historial completo, la D cuesta 4 pb más (≈3 €/año).

**5. Vanguard Global Small-Cap (5 %).** Único indexado global de small caps del catálogo (el iShares
World Small Cap no aparece en el buscador). 3A +17,3 %, vol 3A 14,5 %, 1.600+ empresas, TER 0,29 %.
**Pega:** 61 % EE. UU. — añade beta, no diversificación geográfica — y el TER es el más alto del bloque
de RV; se limita al 5 % por eso.

**6. iShares Developed Real Estate D Acc (6 %).** 97 % inmobiliario cotizado, TER 0,17 %, 3A +10,8 %,
rentas ligadas a inflación vía alquileres. **Pega:** 65 % EE. UU., 5A +0,6 % (2022 fue −20 % en el año
natural), y con tipos altos el sector sufre: es cobertura de inflación, no refugio. Peso limitado al 6 %.

**7. Neuberger Short Duration Euro Bond U (14 %).** La espina dorsal de la RF: 76 % corporativo IG,
duración 1,95, rating medio A−, TIR 4,65 % (30/09/2026), vol 3A 1,93 %, TER 0,38 %. Paga 2,38 pp de
TIR por año de duración, el mejor carry/riesgo del catálogo en su categoría. **Pega:** 14 % EE. UU. y
15 % Reino Unido en emisores (divisa del fondo EUR, riesgo de crédito extranjero) y un 4 % de gobierno.

**8. Aegon European ABS (6 %).** 58 % ABS + 35 % RMBS sin agencia, todo europeo, duración corta,
TIR declarada ~4,3 % (estimada a partir de la ficha; el MCP no publica TIR), 3A +4,4 %, vol 3A 0,95 %
(**5A 1,90 %**: el precio del ABS suaviza la serie corta). **Pega:** TER 0,66 %, el más caro del bloque
corto más caro de la cartera, y la liquidez de los ABS no es la de un bono de gobierno; se limita al 6 %.

**9. iShares Euro Investment Grade Corporate Bond D Acc (5 %).** Deuda corporativa euro **IG** al
0,12 %, 100 % bonos corporativos, 3A +4,2 % y 5A +0,1 %, vol 3A 3,5 %, duración ≈4,5 (estimada).
Sustituye a Sissener tras abrir sus posiciones: lo que parecía «crédito nórdico IG» es **high yield de
energía y shipping** (Nynas 11,75 %, Golar LNG 7,75 %, W&T Offshore 10,75 %, McDermott 10,5 %; top-10 =
30 % del fondo). **Pega:** 20 % de emisores estadounidenses en euros y duración mayor que el bloque
corto, que sube la duración agregada de 2,84 a 3,03 años.

**10. iShares Euro Government Bond D Acc (10 %).** Deuda pública euro (Francia 25, Italia 22, Alemania
20, España 14), TER 0,10 %, duración ≈6,5 (estimada; el MCP no la publica), TIR ≈3,3 % implícita del
Bund. **Pega:** es el único bloque que en 2022 perdió −17,9 % y el que más sufre si los tipos suben
otros 150 pb (−9,8 % de sí mismo). Se queda en el 10 % porque su papel es el escenario de recesión,
no el de tipos altos.

**11. iShares Euro Govt Inflation-Linked D Acc (5 %).** Ligados a la inflación de la zona euro, TER
0,10 %. Es el único seguro directo contra el escenario de inflación persistente. **Pega:** la ficha
del MCP viene **incompleta** (sin países ni desglose; `alloc_other` 100 %), la duración es larga
(≈7 estimada) y arrastra −8,7 % en 2022. 5 % es una póliza, no una posición de convicción.

**12. Groupama Trésorerie IC (15 %).** Monetario estándar, sensibilidad 0,11, 85 % liquidez, TER
**0,07 %**, 3A +3,0 %. Es el vehículo más barato de la plataforma y la reserva táctica. **Pega:** con
inflación del 3,8 % pierde ~1,3 % real al año; su función no es rentar, es estar disponible.

### Candidatos evaluados y descartados (por bloque)

| Bloque | Candidato | ISIN | Dato que decide | Veredicto |
| --- | --- | --- | --- | --- |
| RV global | iShares Developed World S Acc | IE000ZYRH0Q7 | TER 0,06 % (el más barato) | **Descartado**: sin 3A/5A de la clase y dejaría BlackRock al 34 % del capital |
| RV global | Vanguard Global Stock Index EUR Acc | IE00B03HD191 | TER 0,18 %, 3A +18,7 % | Descartado: 6 pb más caro que Fidelity por el mismo índice |
| RV global | Amundi Index MSCI World IE-C | LU0996181599 | TER 0,20 % | Descartado: más caro y con retención luxemburguesa |
| RV Europa | Amundi Core MSCI Europe IE-C | LU0389811539 | TER 0,15 %, 3A +17,6 % | Descartado: 5 pb más que Fidelity y misma exposición |
| RV EM | iShares Emerging Markets D Acc | IE00BYWYCC39 | TER 0,20 %, 3A +20,1 %, 5A +7,6 % | Alternativa con historial completo; cuesta 4 pb más |
| RV EM | Vanguard EM Stock Index Investor | IE0031786142 | TER 0,23 % | Descartado por coste |
| Small caps | iShares MSCI World Small Cap | — | No existe en el catálogo (`resolve_funds`: sin coincidencias) | Hueco no cubierto por otra vía |
| Activos reales | BGF World Gold A2 | LU0171305526 | TER **2,08 %**, mineras no oro físico | **Descartado**: no es el activo que dice ser, y a ese precio |
| Activos reales | iShares Dev. Real Estate Institutional | IE00B83YJG36 | TER 0,23 % | Descartado: 6 pb más que la clase D por el mismo fondo |
| RF corta | AXA Court Terme AC / Ofi ISR Monétaire CT | FR0000288946 / FR0010738229 | TER 0,07 % / 0,06 % | Descartados como **sustitutos del monetario**, no del crédito corto: son 74 % deuda pública a muy corto |
| RF crédito | Sissener Corporate Bond R | LU2262944817 | 3A +6,8 % pero **top-10 = HY de energía/shipping** (Nynas, Golar, W&T, McDermott) | **Descartado por composición**: no es IG; su TIR alta era prima de riesgo de crédito, no carry de calidad |
| RF crédito | DNCA Invest Alpha Bonds A | LU1694789451 | 1,31 % + 20 % éxito | Descartado: soberanos G10 con coberturas; el coste no se justifica |
| RF crédito | Carmignac Portfolio Credit A | LU1623762843 | 1,20 % + 20 % éxito, BBB−, max DD −17,5 % | Descartado: riesgo de crédito peor pagado que la alternativa corta |
| RF gubernamental | Amundi Prime Euro Government Bond IE-C | LU2339731064 | TER 0,05 %, **mínimo 500.000 €** | **Descartado por mínimo**, no por precio |
| RF gubernamental | Vanguard Euro Government Bond Investor | IE0007472115 | TER 0,12 % | Descartado: **en soft close**; el nuevo ISIN (IE0007472990) cuesta lo mismo que el iShares |
| RV value | Cobas International P | LU1598719752 | TER 2,33 %, 3A +26,5 % | Descartado por coste: 2,33 % sobre 5.000 € son 116 €/año para un estilo que se compra a 0,10 % |
| RV value | Fundsmith Equity T Acc | LU0690375182 | TER 1,09 %, 3A **+6,96 %** | Descartado: por debajo del World (18,7 %) pagando 1 pp más |
| RV value | MyInvestor Value C | ES0165243025 | **TER no publicado en el MCP** | Descartado: sin coste verificable no entra en una cartera nueva |

---

## F. Exposición agregada y análisis de riesgos

### F.1 Por clase de activo

| Bloque | € | % cartera |
| --- | ---: | ---: |
| Renta variable | 45.000 | **45,0 %** |
| Renta fija | 40.000 | **40,0 %** |
| Liquidez / monetario | 15.000 | **15,0 %** |
| **Total** | **100.000** | **100 %** |

### F.2 Regiones de la renta variable (look-through, Σ importe × país de cada ficha)

| Región | % de la RV | € | vs MSCI ACWI |
| --- | ---: | ---: | ---: |
| Estados Unidos | **39,4 %** | 17.750 | 63 % → **−24 pp** |
| Europa (Reino Unido 5,9 · Suiza 3,7 · Alemania 3,1 · Francia 2,3 · Holanda 1,6 · España 1,0 · resto) | **25,9 %** | 11.650 | 15 % → **+11 pp** |
| Japón | **13,2 %** | 5.930 | 5 % → **+8 pp** |
| Emergentes (Taiwán 4,2 · Corea 3,2 · China 3,0 · India 1,8 · Brasil 0,6 · otros) | **14,0 %** | 6.300 | 10 % → **+4 pp** |
| Canadá + Australia | 2,8 % | 1.250 | ≈5 % → −2 pp |
| Resto sin desglosar en las fichas | 4,5 % | 2.120 | — |
| **Total** | **≈99,8 %** | 45.000 | (0,2 % de redondeo: cada vector suma 100 % de su fondo) |

**Las tres sobreponderaciones están declaradas, no escondidas:** Europa (+11 pp), Japón (+8 pp) y
emergentes (+4 pp) se financian con EE. UU. (−24 pp). Si el titular no quiere *tilt*, el World sube al
20 % y Europa baja al 4 %: misma caída, 0,4 pp menos de retorno esperado por la valoración.

### F.3 Divisas (efecto sobre un inversor en euros)

Ningún fondo cubre el tipo de cambio: la clase es EUR, la exposición no.

| Divisa de los activos | % de la cartera | Comentario |
| --- | ---: | --- |
| EUR | ≈53 % | RV euro (3,6 k) + toda la RF gubernamental, ligada, corporativa IG y el monetario |
| USD | ≈20 % | 17,7 k de RV + emisores USA en Neuberger y en el corporativo IG (estos, en bonos denominados en euros) |
| JPY | ≈6 % | Fidelity Japan + la parte japonesa de World, small caps y REITs |
| GBP / CHF | ≈4,3 % | Reino Unido y Suiza de Europa + emisores de Neuberger/Aegon |
| Emergentes (TWD, KRW, CNY, INR, BRL…) | ≈6,3 % | Bloque EM, sin cobertura |
| Otros (CAD, AUD, SEK, NOK, DKK) | ≈9 % | Small caps y REITs |
| **No euro (total)** | **≈47 %** | Frente al ~65 % de una cartera 100 % MSCI World |

**Qué significa en la práctica:** si el euro se aprecia un 10 % frente a todas las divisas, la cartera
pierde ~5 % sin que ningún activo se mueva. Si el euro se deprecia, gana. Con horizonte 7-10 años y
aportaciones periódicas, la divisa se diversifica sola; con 100.000 € de golpe, **no se cubre** porque
la cobertura a 10 años cuesta 1,5-2 % anual en tipos (el diferencial euro-dólar) y se come el premio.

### F.4 Sectores de la renta variable

| Sector | % de la RV |
| --- | ---: |
| Tecnología | 21,7 % |
| Servicios financieros | 15,6 % |
| Industria | 11,6 % |
| **Inmobiliario** | **13,9 %** |
| Salud | 7,7 % |
| Consumo cíclico | 6,3 % |
| Comunicación | 4,2 % |
| Resto (consumo defensivo, energía, materiales, utilities) | 19,0 % |

**Dos avisos con número:** tecnología al 21,7 % (frente al 31 % de un World puro: se reduce, no se
elimina) e **inmobiliario al 13,9 %**, que es el efecto de sumar REITs (13,3 %) + el 8 % de small caps
+ el 2 % de Europa. Es una apuesta sectorial consciente; si el titular no la quiere, los 6.000 € de
REITs vuelven a Europa y el sector baja al 1 %.

### F.5 Concentración por gestora y por fondo

| Gestora | € | % |
| --- | ---: | ---: |
| BlackRock | 33.000 | 33,0 % |
| Fidelity | 26.000 | 26,0 % |
| Groupama | 15.000 | 15,0 % |
| Neuberger Berman | 14.000 | 14,0 % |
| Vanguard | 6.000 | 6,0 % |
| Aegon | 6.000 | 6,0 % |

Dos gestoras suman el 59 %, pero **no comparten producto**: BlackRock aporta EM, REITs, deuda pública
y crédito IG; Fidelity aporta World, Europa y Japón. El riesgo de «un solo proveedor» es operativo, no de
exposición.

### F.6 Métricas de la cartera

| Métrica | Valor | Cómo se ha calculado |
| --- | --- | --- |
| TER ponderado | **0,190 % = 190 €/año** | Σ importe × TER de los 12 fondos (fichas 30/10/2026) |
| Comisión de éxito | **0 €** | Ninguno de los 12 cobra comisión de éxito |
| Duración de la RF | **≈3,03 años** | Σ importe × duración / 55.000; duraciones de Aegon, corporativo IG, gubernamental y ligada **estimadas** (el MCP no las publica) |
| Impacto +100 pb | **−1.665 €** (−1,7 % de la cartera) | Σ importe × duración × 0,01 |
| TIR/carry de la RF | **≈3,45 % = 1.899 €/año** | Neuberger 4,65 % (ficha 30/09) · Aegon ~4,3 % est. · corporativo IG ~4,0 % est. · gubernamental 3,3 % · ligada 2,0 % · monetario 2,4 % |
| *Earnings yield* de la RV | **≈6,68 %** | 1/PER por bloque: World 5,6 % · Europa 7,35 % · Japón 6,5 % est. · EM 9,8 % · small 6,0 % est. · REITs 5,5 % est. |
| Retorno esperado nominal base | **≈4,9 %** | 0,45 × 6,68 % + 0,55 × 3,45 % (solo *earnings yield* + carry) |
| Retorno esperado con crecimiento nominal 4 % | **≈6,7 %** | Añade 4 % de crecimiento a la RV; es una estimación, no un backtest |
| Real sobre inflación 3,8 % | **+1,2 % a +3,0 %** | Según el escenario anterior |

---

## G. Escenarios de estrés

Supuestos fijos para poder comparar: RV −40 % (o el que se indique), RF −3 %, monetario 0 %.

| Escenario | Qué pasa | Cálculo | Impacto | Cartera resultante |
| --- | --- | --- | ---: | ---: |
| **1. Caída fuerte de bolsa (tipo 2008)** | RV −40 %, crédito −3 %, monetario intacto | 45.000×(−40 %) + 40.000×(−3 %) | **−19.200 € (−19,2 %)** | 80.800 € |
| **2. Caída extrema (−50 %)** | Como 2008 pero sin recuperación rápida | 45.000×(−50 %) + 40.000×(−3 %) | −23.700 € (−23,7 %) | 76.300 € |
| **3. Inflación persistente (4-5 % dos años)** | RV nominal +4 %/año, REITs +5 %, ligados +4 %, RF nominal 3,5 %, monetario 2,5 % | Σ por bloque | **≈+1,5 %/año nominal, −2,5 % real** | ~101.500 € en 12 meses |
| **4. Subida de tipos +150 pb** | RF −4,5 % (3,03 × 1,5) = −2.497 €, RV −10 % por devaluación de múltiplos | 40.000×(−4,5 %) + 45.000×(−10 %) | **−7.000 € (−7,0 %)** | 93.000 € |
| **5. Recesión global suave** | RV −25 %, gubernamental +6 %, crédito −5 %, monetario 0 | 45.000×(−25 %) + 15.000×(+6 %) + 25.000×(−5 %) | **−11.600 € (−11,6 %)** | 88.400 € |
| **6. Mercado lateral 3 años** | RV +2 %/año, RF cobra carry 3,45 % | 3 × (0,45×2 % + 0,55×3,45 %) | **≈+2,8 %/año** | ~108.600 € |

**Lo que estos números dicen y lo que no.** El escenario 1 es el que manda: **−19,2 % es el precio de
entrada** a esta cartera y está en el límite de lo que el titular declara aguantar. Si en una caída real
vendería, la cartera correcta no es esta: es 40/60 (−17,8 %) quitando Japón y REITs. Los escenarios 3 y
6 son los que justifican la RF corta: **en inflación y en lateral, el carry es lo que paga las facturas**,
no la bolsa.

---

## H. Plan de inversión y rebalanceo

### H.1 ¿De golpe o escalonado?

**De golpe el 85 %, con el 15 % restante como liquidez permanente.** Motivos, en orden:

1. **Los datos favorecen entrar de una vez.** El coste esperado de estar fuera del mercado pesa más que
   el de entrar en mal momento; el escalonado en 3 tandas añade ~0,3 pp de rentabilidad esperada
   negativa y no protege de nada que dure 3 meses.
2. **El escalonado solo tiene sentido si cubre el riesgo que se cita.** Tres compras mensuales no
   protegen de un evento de crédito a 6-12 meses (el riesgo que Ábaco pone en el 60-70 %). Si se quiere
   protección, son 9-12 meses, y entonces se renuncia a un año de mercado por una probabilidad que no se
   puede medir. No se hace.
3. **La liquidez no es un timer, es una regla.** Los 15.000 € de Groupama tienen tres usos escritos y
   ninguno es «esperar a que baje»:
   - **Aportaciones programadas**: 500 €/mes durante 24 meses (12.000 €) a los bloques que se desvíen
     más de 2 pp de su objetivo.
   - **Oportunidad con umbral**: si el MSCI World cae ≥15 % desde el máximo, se despliegan 5.000 € a
     World y 5.000 € a Europa/EM en dos tandas (no todo el primer día).
   - **Colchón de imprevistos**: mínimo 5.000 € intocables; si se usan, se reponen antes de reanudar
     aportaciones.

### H.2 Calendario de entrada (3 órdenes, una semana)

| # | Cuándo | Qué | € |
| --- | --- | --- | ---: |
| 1 | Día 1 | Fidelity World 15.000 + Fidelity Europe 8.000 + Fidelity Japan 4.000 | 27.000 |
| 2 | Día 1 | iShares EM 7.000 + Vanguard Small-Cap 5.000 + iShares REITs 6.000 | 18.000 |
| 3 | Día 2-3 | Neuberger 14.000 + Aegon ABS 6.000 + iShares Corp IG 5.000 + iShares Euro Govt 10.000 + Linker 5.000 + Groupama 15.000 | 55.000 |

Comisiones de entrada: **0 %** en los 12 fondos (MyInvestor no cobra suscripción). Cortes: 09:00-16:00
según ficha, con 2-4 días de *lag* de suscripción. No hace falta tener efectivo extra.

### H.3 Reglas de revisión

- **Frecuencia:** revisión **trimestral** (enero, abril, julio, octubre) + una revisión extraordinaria si
  se cruza un umbral.
- **Qué se mide cada trimestre:** (1) peso de RV vs 45 %; (2) TER real vs 0,190 %; (3) TIR cobrada a 12
  meses de la RF vs 3,45 % estimado; (4) duración de la RF vs 3,03; (5) drawdown de la cartera vs
  −19,2 % de referencia; (6) peso por gestora y por región.
- **Cuándo se rebalancea:** bandas de **±5 pp absolutas por bloque** (RV 40-50 %, RF 35-45 %,
  liquidez 10-20 %) y **±25 % relativo por posición** (p. ej. World entre 11.250 y 18.750 €). Se
  rebalancea **con aportaciones y con traspasos**, nunca por reembolso: los traspasos entre fondos
  armonizados no tributan.
- **Qué NO se hace en pánico:** no se vende en la caída, no se cambia de fondo por un año malo, no se
  añade un satélite temático «porque está cayendo», no se cubre la divisa a posteriori y no se toca el
  monetario para comprar más bolsa salvo que se cumpla el umbral de −15 % escrito arriba.
- **Señal de revisión de la RV:** si la TIR de la RF corta cae por debajo del 2 % **cobrado**, el premio
  de la bolsa sube y el modelo pasa a 50 % de RV (traspasando 5.000 € de Neuberger a World/Europa). Si
  la TIR sube por encima del 5,5 % cobrado, se baja a 40 %.

---

## I. Advertencias, limitaciones y datos no disponibles

**Datos que el MCP no publica y aquí van marcados como estimados:**

| Dato | Estado |
| --- | --- |
| TIR (YTW) de Aegon, corporativo IG, gubernamental y ligada | **No publicado** por el MCP. Se usan ~4,3 %, ~4,0 %, 3,3 % y 2,0 % (ficha de gestora 30/09 y Bund 10 años). Es la cifra que más afecta al carry: si la RF cobra 2 pp menos, el retorno esperado de la cartera baja ~1,1 pp |
| Duración de Aegon, corporativo IG, gubernamental y ligada | **No publicada**. Se usan 2,5 / 4,5 / 6,5 / 7,0 años. El shock de +100 pb (−1.665 €) es una estimación, no una cifra de ficha |
| Rating medio de la RF | Publicado solo para Neuberger (A−, ficha de gestora). Aegon y el corporativo IG no lo dan en el MCP |
| Máxima caída histórica | El MCP **no tiene campo de max drawdown**. Se usan los años naturales (2022: gubernamental −17,9 %, REITs −20,1 %, Aegon −4,0 %) |
| 3A/5A de las clases S de BlackRock (World y EM) | **No publicadas** (clases nuevas). Se usa la clase D como referencia del mismo fondo |
| Tamaño (AUM) de los fondos | No disponible en el MCP; no se ha podido verificar el patrimonio de cada fondo |
| Comisión de suscripción/reembolso | El MCP no la da por clase. MyInvestor aplica 0 % en fondos; **verificar en pantalla** antes de la primera orden, en especial Neuberger (la propuesta vigente documenta «hasta 3 %», máx. 297 €) |

**Limitaciones del diseño:**

1. **Japón al 13,2 % de la RV y Europa al 25,9 % son sobreponderaciones**, no neutralidad. Un inversor
   que quiera el mercado tal cual debe usar un ACWI, no esta cartera.
2. **REITs al 6 % dejan inmobiliario en el 13,9 % de la RV.** Es un sesgo sectorial real.
3. **El bloque EM es 42 % tecnología:** comprar emergentes hoy es comprar semiconductores, no consumo
   interno. Está en el diseño, pero se dice.
4. **52 % de la cartera en divisa no euro**, sin cobertura. Es una decisión, no un olvido.
5. **Ningún activo real no cotizado ni oro físico.** El único oro del catálogo en formato fondo es
   BGF World Gold (mineras, 2,08 %); el oro físico solo existe como ETC/ETF, fuera del envoltorio de
   fondos y con otra fiscalidad. El hueco se declara, no se rellena con un sustituto caro.
6. **El 7-10 % de retorno no está garantizado.** La cartera puede dar −19 % en un año y +4 % real en
   diez; el orden de los factores importa y no se controla.
7. **Idoneidad:** la fiscalidad del titular (traspasos, plusvalías latentes si migra desde la cartera
   actual), sus necesidades de liquidez y el aguante real del −19 % no se pueden verificar desde aquí.

---

## Anexo B. Qué hay dentro de cada fondo (posiciones reales)

Última ficha publicada por la gestora o por FundFacts / FT Markets. **Las posiciones completas no se
publican** (el World tiene 1.253, el EM 1.179); aquí van las diez mayores, que es lo que explica el
comportamiento y los solapamientos. Fecha de los datos: **30/09/2026** cuando la fuente la declara
(FundFacts); sin fecha visible en la página de FT.

### B.1 Renta variable

| Fondo | 10 mayores posiciones (peso) | Top-10 | Nº posiciones | Patrimonio |
| --- | --- | ---: | ---: | ---: |
| **Fidelity MSCI World** (IE00BYX5NX33) | NVIDIA 5,8 · Apple 5,4 · Microsoft 4,0 · Alphabet 4,0 · Amazon 2,6 · Meta 1,7 · Broadcom 1,7 · Micron 1,3 · Tesla 1,1 · AMD 1,1 | 28,7 % | 1.253 | USD 3,5 bn |
| **Fidelity MSCI Europe** (IE00BYX5MD61) | ASML 5,1 · HSBC 2,5 · Roche 2,2 · Shell 2,0 · Novartis 1,9 · AstraZeneca 1,8 · Nestlé 1,7 · Siemens 1,6 · SAP 1,6 · Santander 1,5 | 21,9 % | 389 | EUR 264,6 m |
| **Fidelity MSCI Japan** (IE00BYX5N771) | Mitsubishi UFJ 4,7 · Toyota 3,3 · Tokyo Electron 3,1 · Sumitomo Mitsui 3,0 · Advantest 3,0 · Hitachi 2,9 · SoftBank 2,8 · Recruit 2,6 · Sony 2,6 · Kioxia 2,5 | 30,5 % | 169 | USD 551,1 m |
| **iShares EM S Acc** (IE000QAZP7L2) | TSMC 15,63 · Samsung 7,55 · SK Hynix 5,90 · Tencent 2,74 · Alibaba 1,86 · MediaTek 1,82 · Delta Electronics 0,94 · Samsung (sin voto) 0,94 · China Construction Bank 0,86 · Hon Hai 0,79 | 39,0 % | 1.179 | EUR 790,8 m |
| **Vanguard Global Small-Cap** (IE00B42W4L06) | Moderna 0,63 · Tenet Healthcare 0,21 · Guardant Health 0,21 · Viatris 0,20 · US Foods 0,20 · resto muy repartido | 2,4 % | ≈1.600 | n/d |
| **iShares Developed Real Estate** (IE00BDRK7P73) | Welltower 8,17 · Prologis 6,48 · Equinix 5,05 · Simon Property 3,32 · Digital Realty 3,29 · resto: REITs de salud, logística y centros de datos | 38,2 % | n/d | n/d |

**Lectura rápida:** el World y el Europe no comparten **ni una** de sus diez primeras posiciones (el
solape es de índice, no de nombres: ASML, HSBC o Nestlé pesan poco en el World) — es la prueba de que
la sobreponderación europea no duplica el núcleo. El EM es **TSMC + Samsung + SK Hynix = 29 %**: con
1.179 posiciones, un tercio del fondo está en tres fabricantes de semiconductores.

### B.2 Renta fija y liquidez

| Fondo | 10 mayores posiciones (peso) | Top-10 | Naturaleza |
| --- | --- | ---: | --- |
| **Neuberger Short Duration** (IE00BL1GVT98) | Futuro Euro Schatz **+9,58** · Futuro Euro Bund **−9,57** · Futuro Euro Bobl −4,90 · UBS Switzerland 1,64 · Futuro OAT −1,13 · Nykredit 0,95 · Verizon 0,88 · Athene 0,88 · Supernova 0,86 · HSBC 0,82 | ≈0,0 % neto | Crédito corto + **sobreponderación de curva**: largo Schatz, corto Bund/Bobl. No es «RF pasiva»: hay una apuesta de empinamiento de la curva euro |
| **Aegon European ABS** (IE00BG226Z29) | Futuro Bobl 1,61 · Pavillion Consumer 2025-1 4,93 % 1,21 · FCT Crédit Agricole Habitat 3,06 % 1,10 · Green Lion 2024-1 2,90 % 1,08 · SLM Student Loan 2,87 % 0,93 · Green Lion 2023-1 0,91 · Olympia 0,84 · Jupiter Mortgage 0,74 · Santander 0,70 · BPCE 0,68 | 9,8 % | Titulizaciones europeas: consumo, hipotecas, estudiantes. Máxima granularidad del bloque |
| **iShares Euro IG Corporate** (IE00BDRK7J14) | BlackRock ICS Euro Liquidity 0,26 · Amazon 0,09 · AB InBev 0,09 (×2) · Verizon 0,08 · JPMorgan 0,08 (×2) · Morgan Stanley 0,08 · AB InBev 0,08 · Amazon 0,08 | 1,0 % | 100 % corporativo IG, muy repartido: ninguna posición llega al 0,3 % |
| **iShares Euro Government Bond** (IE00BD0NC037) | Ocho bonos franceses entre 0,72 % y 0,98 % (cupones 0,75-3,5 %), todos «France (Republic Of)» | 8,4 % | Deuda pública euro; Francia es el 25 % del fondo, Italia 22 %, Alemania 20 %, España 14 % |
| **iShares Euro Govt Inflation-Linked** (IE00BD0NC144) | **Sin desglose publicado** (FT devuelve el propio fondo como única posición) | n/d | Bonos ligados a la inflación de la zona euro |
| **Groupama Trésorerie** (FR0000989626) | National Bank of Canada 0,8 · Veolia 0,8 · Bank of America 0,7 · TD Bank 0,6 · Wells Fargo 0,6 · BFCM 0,6 · Deutsche Bank 0,6 · RBC 0,6 · TD Bank 0,6 · MUFG London 0,6 | 6,5 % | Papel comercial y depósitos bancarios a muy corto plazo, 273 posiciones |

**Dos cosas que esta tabla cambia y que el documento ya incorpora:** el Neuberger no es un fondo de
bonos quieto (lleva un *steepener* Schatz/Bund con el 15 % del patrimonio en futuros, en neto casi
cero) y el que iba a ser el satélite de crédito «IG nórdico» (Sissener) tenía un top-10 de high yield
de energía y shipping — **por eso está fuera y su hueco lo ocupa el corporativo IG indexado**.

## Anexo A. Relación con la cartera actual (solo para el debate, no para ejecutar)

Se ha diseñado **sin heredar nada**; este anexo solo dice qué pasaría si se comparara con
`cartera-actual.md` (90.000 € + 10.000 € de colchón).

| Tema | Cartera actual | Esta propuesta |
| --- | --- | --- |
| RV | 31,6 % (con Rock) | **45 %** |
| RF + liquidez | 68,4 % | 55 % |
| TER | 0,913 % sobre 60 k invertibles / 0,678 % sobre 100 k | **0,190 %** |
| Posiciones | 17 (8 manuales + 9 de Rock) | 12 |
| Duración RF | 3,83 años | 3,03 años |
| USA en la RV | ≈56 % | 39,4 % |
| Coche automático | Rock 78/22 (0,41 % todo incluido) | No se usa: todo manual |
| Fondos que coinciden | Neuberger, Groupama, Fidelity Europe, iShares EM | 4 de 12 |

**Lo que la propuesta gana:** 190 €/año de coste frente a 678 € (488 € menos), una caída esperada
similar con 13 pp más de RV (porque Rock tiene 78 % de bolsa y aquí la RF es más corta), y una
exposición a EE. UU. 17 pp menor. **Lo que pierde:** simplicidad —12 fondos manuales que hay que
rebalancear a mano— y la comodidad del 15 % de liquidez, que hay que gestionar con disciplina.
**Lo que no cambia:** sigue sin haber value activo, ni oro, ni apalancamiento, y la decisión del % de
RV sigue siendo del titular.

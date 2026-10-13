---
id: h05-m01
type: moeilijk
kort: Moeilijke zaken
titel: Antennelengte berekenen, stap voor stap
uba_ref: hfst. 3.4 en 5.2
checkvragen: []
examenvragen: []
---
Bijna elke antenne is een **deel van een golflengte**: een halve (dipool), een kwart (kwartgolf, groundplane) of vijf achtste (5/8 λ). Kun je de golflengte uitrekenen, dan kun je dus elke antennelengte uitrekenen.

:::formule
λ = 300 ÷ f
dipool = λ ÷ 2
kwartgolf = λ ÷ 4
5/8 λ = λ × 5 ÷ 8
--
λ = golflengte in meter (m) · f = frequentie in megahertz (MHz)
:::

### Het stappenplan

1. **Zet de frequentie in MHz.** Staat ze in kHz, deel dan door 1 000 (7 100 kHz = 7,1 MHz).
2. **Reken de golflengte uit**: λ = 300 ÷ f.
3. **Neem het juiste deel**: ÷ 2 voor een dipool, ÷ 4 voor een kwartgolf, × 5 ÷ 8 voor een 5/8 λ.
4. **Maak het antwoord handig**: 0,52 m = 52 cm.
5. **Controleer met gezond verstand**: HF-antennes zijn meters tot tientallen meters lang, VHF-antennes ongeveer een meter of minder.

### Uitgewerkt voorbeeld 1: dipool voor 14 MHz

1. f = 14 MHz.
2. λ = 300 ÷ 14 ≈ **21,4 m**.
3. Dipool: 21,4 ÷ 2 ≈ **10,7 m**.
4. Twee draden van ongeveer 5,35 m.
5. Tientallen meters op HF: klopt.

### Uitgewerkt voorbeeld 2: kwartgolf voor 145 MHz

1. f = 145 MHz.
2. λ = 300 ÷ 145 ≈ **2,07 m**.
3. Kwartgolf: 2,07 ÷ 4 ≈ **0,52 m**.
4. 0,52 m = **52 cm**. Dat is ongeveer de lengte van een magneetvoetantenne op het dak van een auto.
5. VHF, minder dan een meter: klopt.

### Uitgewerkt voorbeeld 3: 5/8 λ voor 145 MHz

1. f = 145 MHz.
2. λ ≈ 2,07 m.
3. 5/8 λ: 2,07 × 5 = 10,35. Gedeeld door 8 ≈ **1,29 m**.
4. Ongeveer 1,3 m: langer dan de kwartgolf van voorbeeld 2. Klopt, want 5/8 is meer dan 2/8.

| Frequentie | λ | Dipool (λ/2) | Kwartgolf (λ/4) |
|---|---|---|---|
| 3,6 MHz (80 m) | 83 m | 42 m | 21 m |
| 7 MHz (40 m) | 43 m | 21 m | 11 m |
| 14 MHz (20 m) | 21 m | 10,7 m | 5,4 m |
| 28 MHz (10 m) | 10,7 m | 5,4 m | 2,7 m |
| 145 MHz (2 m) | 2,07 m | 1,03 m | 52 cm |
| 435 MHz (70 cm) | 69 cm | 34 cm | 17 cm |

:::valkuil
- Verwar **λ/2** (dipool) en **λ/4** (kwartgolf) niet: de kwartgolf is half zo lang als de dipool.
- Vergeet niet eerst om te zetten naar **MHz**. 300 ÷ 7 100 (kHz) geeft onzin.
:::

<details class="zelf" markdown="1"><summary>Zelf proberen: hoe lang is een dipool voor 30 MHz?</summary>

λ = 300 ÷ 30 = 10 m. Dipool = 10 ÷ 2 = **5 m**.

</details>
<details class="zelf" markdown="1"><summary>Zelf proberen: hoe lang is een kwartgolf voor 7 500 kHz?</summary>

7 500 kHz = 7,5 MHz. λ = 300 ÷ 7,5 = 40 m. Kwartgolf = 40 ÷ 4 = **10 m**.

</details>
<details class="zelf" markdown="1"><summary>Zelf proberen: een dipool is 2 m lang. Voor welke frequentie?</summary>

Een dipool is λ/2, dus λ = 2 × 2 = 4 m. f = 300 ÷ 4 = **75 MHz**.

</details>

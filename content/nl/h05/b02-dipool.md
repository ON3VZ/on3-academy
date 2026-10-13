---
id: h05-b2
type: brokje
kort: De dipool
titel: De dipool: de basis van alle antennes
uba_ref: hfst. 5.2, p. 17 en 18
checkvragen: [C-h05-2a, C-h05-2b, C-h05-2c]
examenvragen: [O163, O152, O153, O159]
---
:::kern
Een **dipool** is een draad of buis die in het **midden** onderbroken is. Op die onderbreking (het **voedingspunt**) komt de kabel naar de zender. Is de dipool **een halve golflengte (λ/2)** lang, dan is hij in resonantie en werkt hij het best.
:::

{{svg:h05-dipool|Links horizontaal opgehangen, rechts verticaal. Het blijft dezelfde antenne.}}

:::formule
lengte dipool = λ ÷ 2 = 150 ÷ f
--
lengte in meter (m) · f = frequentie in megahertz (MHz) · 150 is de helft van 300
:::

### Uitgewerkt voorbeeld
"Je wilt een dipool voor 10 MHz. Hoe lang moet hij zijn?"

1. Golflengte: λ = 300 ÷ 10 = **30 m**.
2. Halve golflengte: 30 ÷ 2 = **15 m**.
3. De dipool is dus 15 m lang: twee draden van 7,5 m, met het voedingspunt in het midden.

| Band | Frequentie | Dipool (150 ÷ f) |
|---|---|---|
| 80 m | 3,6 MHz | ongeveer 42 m |
| 40 m | 7,1 MHz | ongeveer 21 m |
| 20 m | 14,2 MHz | ongeveer 10,6 m |
| 2 m | 145 MHz | ongeveer 1 m |

### Hoe ziet de stroom eruit?

- In het **midden** is de stroom het **grootst**.
- Aan de **uiteinden** is de stroom **nul**: daar kan hij nergens meer heen.
- Daartussen loopt hij op en af als een halve sinus. Precies één halve golf past op een halve-golf-dipool.

{{foto:h05-dipool.png|Een dipool in het echt: twee buizen, in het midden een kastje waar de coax in gaat.}}

:::valkuil
Een "λ/2-dipool" is een **halve** golflengte, niet een volledige en ook geen kwart. De naam zegt het al: λ/2 = lambda gedeeld door 2.
:::

:::weetje
In de praktijk maak je een draaddipool een paar procent korter dan 150 ÷ f, en knip je hem op maat terwijl je de SWR meet (zie de pagina over SWR). Voor het examen volstaat "ongeveer een halve golflengte".
:::

<details class="zelf" markdown="1"><summary>Zelf proberen: hoe lang is een dipool voor 7,5 MHz?</summary>

λ = 300 ÷ 7,5 = 40 m. De helft: **20 m**. Of rechtstreeks: 150 ÷ 7,5 = 20 m.

</details>
<details class="zelf" markdown="1"><summary>Zelf proberen: hoe lang is een dipool voor 150 MHz?</summary>

150 ÷ 150 = **1 m**.

</details>

### Antennes herkennen op een tekening
Op het examen moet je antennes herkennen. Kijk bij deze tekening naar B en C: het zijn allebei dipolen (één streep met een onderbreking in het midden).

{{svg:h05-antennes-abcd-1|A: 5/8 λ met spoel. B: horizontale dipool. C: verticale dipool. D: yagi.}}

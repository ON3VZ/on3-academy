---
id: h05-b6
type: brokje
kort: ERP
titel: ERP: effectief uitgestraald vermogen
uba_ref: hfst. 5.5, p. 22
checkvragen: [C-h05-6a, C-h05-6b, C-h05-6c]
examenvragen: [O170, O171]
---
:::kern
**ERP** (Effective Radiated Power, in het Nederlands **EUV**: effectief uitgestraald vermogen) zegt hoeveel vermogen je met een **gewone dipool** zou nodig hebben om in de voorkeurrichting even sterk te zijn. Je berekent het met een **vermenigvuldiging**.
:::

:::formule
ERP = P × G
--
ERP in watt (W) · P = vermogen dat aan de antenne geleverd wordt, in watt · G = winst van de antenne (een getal zonder eenheid, tegenover een dipool)
:::

{{svg:h05-erp|10 W in een yagi met winst 5 is in de voorkeurrichting even sterk als 50 W in een dipool.}}

### Uitgewerkt voorbeeld
"Een antenne met winst 5 krijgt 10 W. Hoeveel is de ERP?"

1. Gegeven: P = 10 W, G = 5.
2. Formule: ERP = P × G.
3. ERP = 10 × 5 = **50 W**.
4. Betekenis: wie in de voorkeurrichting luistert, hoort jou even sterk als iemand met 50 W in een gewone dipool.

:::vergelijk Vergelijk met
De zaklamp van de vorige pagina. De lamp zelf verbruikt evenveel, maar door het spiegeltje lijkt ze in één richting veel feller. ERP is "hoe fel lijkt het in die richting".
:::

:::valkuil
- Het is **maal**, geen plus, geen min en geen deling. Bij 10 W en winst 4 is het antwoord 40 W, niet 14 W, 6 W of 2,5 W.
- ERP is een **rekengetal**. Er gaat niet echt 50 W de lucht in: je zender levert nog altijd 10 W.
:::

<details class="zelf" markdown="1"><summary>Zelf proberen: 25 W in een antenne met winst 3. ERP?</summary>

ERP = 25 × 3 = **75 W**.

</details>
<details class="zelf" markdown="1"><summary>Zelf proberen: je wilt 100 W ERP met een antenne met winst 4. Hoeveel vermogen moet je leveren?</summary>

P = ERP ÷ G = 100 ÷ 4 = **25 W**.

</details>

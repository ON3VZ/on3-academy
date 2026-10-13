---
id: h05-b10
type: brokje
kort: Symmetrisch en balun
titel: Symmetrische en asymmetrische antennes, de balun
uba_ref: hfst. 5.5, p. 23
checkvragen: [C-h05-10a, C-h05-10b, C-h05-10c]
examenvragen: [O175, O176, O177, O178, O179]
---
:::kern
Een antenne is **symmetrisch** als de delen links en rechts van het voedingspunt elkaars **spiegelbeeld** zijn. Zijn de twee delen verschillend, dan is ze **asymmetrisch**. Wil je een symmetrische antenne (een dipool) aan een asymmetrische kabel (coax) hangen, dan gebruik je een **balun**.
:::

{{svg:h05-symmetrie|Links twee gelijke helften, rechts een staaf en een grondvlak: twee verschillende delen.}}

| Symmetrisch | Asymmetrisch |
|---|---|
| λ/2-dipool (horizontaal of verticaal) | λ/4 ground plane |
| yagi (de straler is een dipool) | 5/8 λ |
| | eindgevoede langedraad |

### Coax is asymmetrisch
Een coaxkabel heeft binnenin een **draad** en rondom een **buis** (de afscherming). Twee verschillende delen: asymmetrisch.

- Bij een **asymmetrische antenne** past dat goed: de **binnengeleider** gaat naar de **straler**, de **afscherming** naar het **grondvlak**, de radialen of de aarding.
- Bij een **dipool** zijn beide helften gelijk. Hang je de coax er rechtstreeks aan, dan werkt het wel, maar gaat de **buitenkant van de afscherming meestralen**. Gevolg: meer kans op **storingen** (zie hoofdstuk 7, EMC).

{{svg:h05-balun|De balun zit tussen de coax en het midden van de dipool.}}

:::formule
balun = **bal**anced → **un**balanced
--
balanced = symmetrisch (de dipool) · unbalanced = asymmetrisch (de coax)
:::

:::vergelijk Vergelijk met
Een stekkeradapter op reis: het toestel en het stopcontact passen niet op elkaar, de adapter maakt de overgang. De balun is de adapter tussen een symmetrische antenne en een asymmetrische kabel.
:::

:::valkuil
Een **yagi** is symmetrisch, hoewel hij er ingewikkeld uitziet: kijk naar het gevoede element, dat is een dipool. Een **5/8 λ** en een **ground plane** zijn asymmetrisch, ook al staan ze mooi rechtop.
:::

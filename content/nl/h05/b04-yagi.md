---
id: h05-b4
type: brokje
kort: Yagi, rondstraler en richtantenne
titel: Rondstralers en richtantennes
uba_ref: hfst. 5.2, p. 18 en 19
checkvragen: [C-h05-4a, C-h05-4b, C-h05-4c]
examenvragen: [O154, O158, O164, O165, O166, O167, O168, O169]
---
:::kern
Een **rondstraler** (omnidirectionele antenne) zendt in alle richtingen van de windroos even sterk. Een **richtantenne** bundelt het vermogen in één richting. De bekendste richtantenne is de **yagi**.
:::

### De yagi
{{svg:h05-yagi|Bovenaanzicht: achteraan de reflector, dan de gevoede straler, vooraan de directoren.}}

| Onderdeel | Plaats | Lengte |
|---|---|---|
| **reflector** | achter de straler | iets **langer** dan de straler |
| **straler** | het element waar de coax aan hangt | een dipool |
| **director(en)** | vóór de straler | iets **korter** dan de straler |
| **drager (boom)** | de buis waar alles op vastzit | |

- De straling gaat naar de kant van de **directoren**.
- Alleen de straler is aangesloten. Reflector en directoren "duwen" de golf naar voren.

{{foto:h05-yagi.png|Een yagi op een mast: veel evenwijdige staven op één drager.}}

### Winst
Omdat de yagi het vermogen in één richting bundelt, komt er in **die** richting veel meer signaal aan dan met een gewone dipool. Dat noemen we de **winst** van de antenne. De antenne maakt geen extra vermogen: ze stuurt hetzelfde vermogen gewoon gerichter weg.

:::vergelijk Vergelijk met
Een gewone lamp tegenover een zaklamp. De lamp verlicht de hele kamer een beetje. De zaklamp heeft geen sterkere lamp, maar een spiegeltje dat het licht bundelt: in één richting is het veel feller, ernaast is het donker.
:::

Bij ontvangen werkt het ook: de yagi hoort de gewenste richting beter en **onderdrukt storing** uit andere richtingen.

### Stralingsdiagram: van bovenaf bekeken
{{svg:h05-straling|De blauwe vlek toont hoe ver het signaal in elke richting komt.}}

| Rondstralend (omnidirectioneel) | Niet rondstralend |
|---|---|
| verticale λ/2-dipool | **horizontale** λ/2-dipool (2 voorkeurrichtingen, dwars op de draad) |
| λ/4 ground plane | **yagi** (1 voorkeurrichting) |
| 5/8 λ (verticaal) | eindgevoede langedraad |

:::valkuil
Een **horizontale** dipool is **geen** rondstraler (als hij minstens een halve golflengte hoog hangt): hij straalt vooral dwars op de draad. Een **verticale** dipool is wel een rondstraler. Let op het woord horizontaal of verticaal in de vraag.
:::

:::weetje
De winst van een yagi komt **alleen** door het bundelen. Niet door het metaal waarvan hij gemaakt is, en ook niet door de polarisatie.
:::

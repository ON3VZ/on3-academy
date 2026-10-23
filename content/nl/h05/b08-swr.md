---
id: h05-b8
type: brokje
kort: SWR
titel: SWR: past de antenne bij de zender?
uba_ref: hfst. 5.4, p. 21 en 22
checkvragen: [C-h05-8a, C-h05-8b, C-h05-8c, C-h05-8d]
examenvragen: [O172, O173, O180, O181, O182]
---
:::kern
Past de antenne goed bij de zender en de frequentie, dan gaat bijna al het vermogen naar de antenne. Past ze niet goed, dan **komt een deel terug** naar de zender: dat heet **gereflecteerd vermogen**. De **SWR** (Standing Wave Ratio, Nederlands: **SGV**, staande golf verhouding) vertelt hoeveel er terugkomt. Je meet ze met een **SWR-meter**.
:::

{{svg:h05-swr|Heen gaat het vermogen naar de antenne, terug komt wat de antenne niet opneemt.}}

:::vergelijk Vergelijk met
Water dat je door een tuinslang in een emmer giet. Is de emmer goed onder de slang gezet, dan komt al het water erin. Staat hij scheef, dan spat een deel terug. Hoe meer er terugspat, hoe slechter de "aanpassing", hoe hoger de SWR.
:::

### De getallen
| SWR | Betekenis |
|---|---|
| **1 : 1** (1/1) | perfect: er komt niets terug |
| **1,5 : 1 of lager** | zeer goed: moderne zenders geven hun volle vermogen |
| **tot 2 : 1** | in de praktijk nog aanvaardbaar (gemeten aan de uitgang van de zender) |
| hoger dan 2 : 1 | boven ongeveer 1,5 : 1 regelen veel moderne zenders hun vermogen al automatisch terug; boven 2 : 1 is de SWR in de praktijk te hoog |
| **oneindig** | alles komt terug |

### Waarom is een hoge SWR slecht?

- Het teruggekaatste vermogen wordt in de zender omgezet in **warmte**.
- Is het te veel, dan kan de **eindtrap** (RF-vermogenversterker) van de zender **beschadigd** raken.

### Wat betekent een hoge SWR?
De SWR-meter toont of het **antennesysteem** (antenne + kabel) **aangepast** is aan de zender. Meet je plots een hoge SWR op een frequentie die vroeger goed was, dan zit de fout meestal in de **antenne** of in de **transmissielijn** (kabel, connector). **Niet** in de zender.

:::valkuil
- Een hoge SWR wijst naar de **antenne of de kabel**, nooit naar de microfoonversterker, de modulator of de eindtrap.
- Een SWR-meter meet niets over overmodulatie, frequentiezwaai of frequentiestabiliteit. Hij meet alleen of de antenne past.
:::

### De antenne moet passen bij de frequentie
Een antennesysteem moet geschikt zijn voor **de frequentie waarop je zendt**. Het maakt niet uit welk merk zender je hebt of welke modulatie (SSB, CW, FM) je gebruikt. Is de antenne niet geschikt voor die frequentie, dan is ze **niet aangepast** aan de zender en werkt ze **niet efficiënt**.

### Afregelen op de laagste SWR
Bij een dipool kun je de lengte aanpassen:

1. Zend kort met laag vermogen en lees de SWR af.
2. **Stop met zenden** voor je aan de antenne komt. Raak een antenne nooit aan tijdens het zenden.
3. Maak de antenne een beetje korter of langer.
4. Meet opnieuw. Herhaal tot de SWR zo laag mogelijk is.

Is de SWR het laagst op een **lagere** frequentie dan gewenst, dan is de antenne te lang: inkorten. Ligt het minimum **hoger**, dan is ze te kort.

:::weetje Geen examenstof: waarom "staande golf"?
De heengaande en teruggekaatste golf lopen door elkaar in de kabel. Daardoor is de spanning niet overal even groot: er ontstaat een golfpatroon dat "stilstaat".

{{svg:h05-swr-staand|Spanning langs de kabel bij SWR 1, 2 en oneindig.}}

SWR = U<sub>max</sub> ÷ U<sub>min</sub>. Bij SWR 1 is de spanning overal gelijk. Bij SWR oneindig zakt ze op sommige plaatsen tot nul.
:::

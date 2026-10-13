---
id: h05-b7
type: brokje
kort: Coax en connectoren
titel: De kabel naar de antenne: coax en connectoren
uba_ref: hfst. 5.3, p. 20
checkvragen: [C-h05-7a, C-h05-7b, C-h05-7c]
examenvragen: [O138, O139, O140, O141, O142, O143, O144, O145]
---
:::kern
De zender staat binnen, de antenne buiten. De kabel ertussen heet de **transmissielijn** (ook voedingslijn). Die moet het vermogen met **zo weinig mogelijk verlies** naar de antenne brengen en mag **zelf niet uitstralen**. Daarvoor gebruiken we bijna altijd **coaxkabel** (kort: coax), omdat die goed **afgeschermd** is.
:::

{{svg:h05-coax|De vier lagen van een coaxkabel.}}

| Laag | Waarvan? | Wat doet ze? |
|---|---|---|
| binnengeleider | koperdraad in het midden | draagt het signaal |
| diëlektricum | isolerend materiaal (kunststof) | houdt de binnengeleider precies in het midden |
| afscherming | vlechtwerk van dunne koperdraadjes | houdt het signaal **binnen** de kabel en storing **buiten** |
| mantel | buitenste laag kunststof | beschermt tegen weer en vooral **water** |

:::vergelijk Vergelijk met
Een waterleiding in een tunnel. Het water (het signaal) stroomt door de buis in het midden. De tunnelwand (de afscherming) zorgt dat er niets naar buiten lekt en dat er van buiten niets binnenkomt.
:::

:::valkuil
Een gewoon netsnoer (twee- of drie-aderig) of "een waterdichte kabel" is **niet** geschikt. Coax kies je niet omdat hij goedkoop, soepel of waterdicht is, maar om zijn **afscherming**. En een coax mag het signaal juist **niet** uitstralen: dat is het werk van de antenne.
:::

### Connectoren
Aan de uiteinden van de coax komen **connectoren** (stekkers). Je gebruikt alleen connectoren die **speciaal voor RF** (radiofrequentie) gemaakt zijn. Een willekeurige stekker die het vermogen aankan, volstaat niet.

{{foto:h05-connectoren-overzicht.jpg|PL259, BNC en N, telkens het kabeldeel en (bij PL259 en BNC) het chassisdeel.}}

| Connector | Herken je aan | Gebruik |
|---|---|---|
| **PL259** | dikke stekker met een **schroefring** en een pin in het midden. Het chassisdeel (SO239) is vierkant met vier gaatjes | HF, meest gebruikt in de shack |
| **BNC** | kleiner, met een **bajonetsluiting**: duwen en een kwartslag draaien | meetapparatuur, portofoons |
| **N** | groter, schroefring, waterdicht | VHF en UHF, buiten |
| **SMA / RP SMA** | heel klein, met schroefdraad | SDR-ontvangers, portofoons |

Voor het examen moet je zeker **PL259** en **BNC** herkennen.

{{foto:h05-connectoren-abcd-1.png|Vier kabelconnectoren: A is een BNC, C is een PL259. B (cinch) en D (DIN) zijn geen RF-connectoren.}}

{{foto:h05-connectoren-abcd-2.png|Vier chassisdelen: B is het chassisdeel voor een PL259, C is een BNC. A (jack) en D (DIN) zijn audio of data.}}

### De afscherming goed aansluiten
De afscherming moet **rondom** goed vastzitten aan de connector. Anders lekt er RF-signaal **uit** de kabel (je stoort andere toestellen) of lekt er storing **in**.

{{foto:h05-pl259-fout-goed.jpg|Links fout: de afscherming zit niet goed vast. Rechts goed: de connector is netjes op de kabel gemonteerd.}}

:::weetje
Hoe je zelf een PL259 of N-connector op een coax monteert, staat stap voor stap in het handboek (hoofdstuk 12, HowTo kabels en connectoren). Dat is geen examenstof, maar wel handig voor later.
:::

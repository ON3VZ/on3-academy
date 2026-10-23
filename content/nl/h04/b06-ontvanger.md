---
id: h04-b6
type: brokje
kort: De ontvanger
titel: De ontvanger, onderdeel per onderdeel
uba_ref: hfst. 4.3, p. 16
checkvragen: [C-h04-6a, C-h04-6b, C-h04-6c]
examenvragen: [O121, O122, O123, O124, O125, O126, O127, O128, O129, O130, O131, O132, O133, O135, O136]
---
:::kern
Een ontvanger doet het omgekeerde van een zender. De antenne vangt radiogolven op, de ontvanger kiest het gewenste signaal, haalt er de spraak of data weer uit en maakt die luid genoeg voor een luidspreker of hoofdtelefoon.
:::

{{svg:ontvanger|De weg van het signaal: van links (antenne) naar rechts (luidspreker).}}

| Onderdeel | Wat doet het? | Verbonden met |
|---|---|---|
| antenne | vangt de radiogolven op en maakt er een klein elektrisch signaal van | alleen de transmissielijn |
| transmissielijn | brengt het signaal van de antenne naar de ontvanger (coax) | antenne en afstemming + RF-versterking |
| afstemming + RF-versterking | kiest **het ene signaal** dat je wilt horen uit alle signalen (afstemmen) en versterkt het | transmissielijn en demodulator |
| demodulator (detector) | haalt de spraak of data **uit** de radiogolf | afstemming + RF-versterking en audioversterker |
| audioversterker | maakt de spraak luid genoeg | demodulator en luidspreker |
| luidspreker of hoofdtelefoon | maakt er weer geluid van. Bij data gaat het signaal naar een computer | alleen de audioversterker |

### De drie trappen
| Trap | Plaats | Wat gebeurt er? |
|---|---|---|
| 1e trap | **ingangstrap** | afstemming (en RF-versterking) |
| 2e trap | tussen ingang en uitgang | demodulatie |
| 3e trap | **uitgangstrap** | audioversterking |

:::vergelijk Vergelijk met
Je staat op een druk feest en wilt één vriend verstaan. Eerst richt je je aandacht op hem en negeer je de rest: dat is **afstemmen**. Dan haal je de woorden uit het geroezemoes: dat is **demoduleren**. Hoort je buur het niet goed, dan herhaal je het luider: dat is **audioversterking**.
:::

{{svg:zender-ontvanger|Vereenvoudigd: de frequentiegenerator, de microfoon en de transmissielijn van de zender zijn weggelaten. Het volledige blokschema van de zender staat bij "De zender". De demodulator doet het omgekeerde van de modulator.}}

:::valkuil
Afstemmen gebeurt **vooraan** (ingangstrap), niet in de demodulator en niet in de audioversterker. En de antenne hangt **enkel** aan de transmissielijn, nooit rechtstreeks aan een ander blok.
:::

### Symbolen in het schema
| Onderdeel | Symbool |
|---|---|
| antenne | {{svg:sym-antenne}} |
| microfoon | {{svg:sym-microfoon}} |
| luidspreker | {{svg:sym-luidspreker}} |

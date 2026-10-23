---
id: h04-b3
type: brokje
kort: SSB, CW, data
titel: SSB, CW en data
uba_ref: hfst. 4, p. 14 tot 16
checkvragen: [C-h04-3a, C-h04-3b, C-h04-3c, C-h04-3d]
examenvragen: [O107, O108, O109, O110, O111, O112]
---
<h3>SSB: AM zonder het overbodige</h3>
<div class="card kern"><b class="k">Kern</b>
Een AM-signaal bestaat uit <b>3 stukken</b>: de draaggolf, een onderste zijband en een bovenste zijband. De draaggolf bevat <b>geen</b> boodschap. Beide zijbanden bevatten <b>dezelfde</b> boodschap. SSB (<i>single sideband</i>, enkelzijband) laat de draaggolf en één zijband weg en stopt al het vermogen in de zijband die overblijft.
</div>

:::gevorderd
<div class="figwrap">{{svg:spectrum-am-ssb}}<div class="figcap">Spectrum: horizontaal de frequentie, verticaal het vermogen. Voorbeeld met spraak tot 3 kHz rond 7,100 MHz.</div></div>
:::

<div class="tbl"><table>
<tr><th>Afkorting</th><th>Betekenis</th><th>Wat blijft over</th></tr>
<tr><td>SSB</td><td>single sideband, enkelzijband</td><td>één zijband</td></tr>
<tr><td>USB</td><td>upper sideband</td><td>de zijband boven de draaggolf</td></tr>
<tr><td>LSB</td><td>lower sideband</td><td>de zijband onder de draaggolf</td></tr>
</table></div>

<div class="formula"><div class="f">P<small>AM</small> ≈ 6 × P<small>SSB</small></div>
<div class="leg">Om even sterk over te komen als 10 W SSB heb je ongeveer 60 W AM nodig. De berekening staat bij "Moeilijke zaken".</div></div>

:::gevorderd
Afspraak onder radioamateurs: onder 10 MHz gebruik je meestal <b>LSB</b>, vanaf 10 MHz meestal <b>USB</b>.
:::

<h3>CW: de eenvoudigste modulatie</h3>
<div class="card kern"><b class="k">Kern</b>
Bij CW (morse) zet je de draaggolf gewoon <b>aan en uit</b> op het ritme van de morsetekens. Kort aan = punt, lang aan = streep.
</div>

:::gevorderd
Je gebruikt een seinsleutel in plaats van een microfoon.
:::

<h3>Data: computer in plaats van microfoon</h3>
<div class="figwrap">{{svg:data-tnc}}<div class="figcap">Bij datacommunicatie stuurt de computer de zender aan via een modem of TNC.</div></div>
<ol class="steps">
<li><span>De computer maakt <b>bits</b>: nullen en enen.</span></li>
<li><span>Een radiomodem of <b>TNC</b> (Terminal Node Controller) maakt daar <b>audiotonen</b> van: één toon voor een 0, een andere toon voor een 1. Een modem maakt dus geen RF-signaal, alleen tonen.</span></li>
<li><span>Die tonen gaan de zender in alsof het je stem was.</span></li>
</ol>

:::gevorderd
De zender werkt verder in SSB of FM, zoals ook in de tekening staat.
:::
<div class="card"><span class="extra-tag">weetje</span>Moderne digitale modes zoals FT8 gebruiken geen aparte TNC meer. De geluidskaart van de computer maakt de tonen.</div>

<h3>Alle signalen naast elkaar</h3>
<div class="figwrap">{{svg:signalen}}<div class="figcap">Zo zien de vier soorten er op een tekening uit.</div></div>

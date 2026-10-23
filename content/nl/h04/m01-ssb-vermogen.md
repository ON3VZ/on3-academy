---
id: h04-moeilijk
type: moeilijk
kort: Moeilijke zaken
titel: Waarom is SSB 6 keer zuiniger?
uba_ref: hfst. 4, p. 14 tot 16
checkvragen: []
examenvragen: []
---
<p>Het handboek zegt: SSB is ongeveer <b>6 keer efficiënter</b> dan AM. 10 W SSB komt even sterk over als 60 W AM. Dat moet je kennen. Wie wil weten waar die factor 6 vandaan komt, vindt hieronder de achtergrond.</p>

:::gevorderd
<h3>Stap voor stap</h3>
<ol class="steps">
<li><span>Neem een AM-zender van <b>60 W</b> die volledig gemoduleerd is (100 %).</span></li>
<li><span>Dat vermogen wordt over 3 stukken verdeeld. De draaggolf krijgt <b>2/3</b>: 60 × 2/3 = <b>40 W</b>.</span></li>
<li><span>Elke zijband krijgt <b>1/6</b>: 60 × 1/6 = <b>10 W</b> per zijband.</span></li>
<li><span>De ontvanger heeft maar één zijband nodig om je te verstaan. Het nuttige deel is dus <b>10 W</b>.</span></li>
<li><span>Een SSB-zender van <b>10 W</b> stopt al zijn vermogen in die ene zijband. Resultaat: even sterk als 60 W AM.</span></li>
</ol>

<div class="tbl"><table>
<tr><th>AM 60 W</th><th>Vermogen</th><th>Nuttig?</th></tr>
<tr><td>draaggolf</td><td>40 W</td><td>nee, geen boodschap</td></tr>
<tr><td>onderste zijband</td><td>10 W</td><td>dubbel, zelfde boodschap</td></tr>
<tr><td>bovenste zijband</td><td>10 W</td><td><b>ja</b></td></tr>
</table></div>

<h3>Waar ligt mijn SSB-signaal?</h3>
<div class="formula"><div class="f">USB: f = f<small>display</small> + f<small>audio</small></div>
<div class="f">LSB: f = f<small>display</small> − f<small>audio</small></div>
<div class="leg">f<small>display</small> = de frequentie op je scherm. f<small>audio</small> = de toonhoogte van je stem of toon.</div></div>

<div class="card"><b class="k">Uitgewerkt voorbeeld</b>
<ol class="steps">
<li><span>Display: <b>14,200 MHz</b>, mode USB. Je fluit een toon van 1 kHz.</span></li>
<li><span>USB, dus optellen: 14,200 MHz + 0,001 MHz.</span></li>
<li><span>Je signaal ligt op <b>14,201 MHz</b>.</span></li>
</ol>
</div>

<h3>Bandbreedte</h3>
<div class="formula"><div class="f">B<small>AM</small> = 2 × f<small>audio,max</small></div>
<div class="f">B<small>SSB</small> ≈ f<small>audio,max</small></div>
<div class="leg">Spraak tot 3 kHz: AM is 6 kHz breed, SSB ongeveer 3 kHz. SSB neemt dus de helft van de plaats in.</div></div>
:::

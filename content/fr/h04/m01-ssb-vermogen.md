---
id: h04-moeilijk
type: moeilijk
kort: Points difficiles
titel: Pourquoi la SSB est-elle 6 fois plus économe ?
uba_ref: hfst. 4, p. 14 tot 16
checkvragen: []
examenvragen: []
---
<p>Le manuel dit : la SSB est environ <b>6 fois plus efficace</b> que l'AM. 10 W en SSB sont reçus aussi fort que 60 W en AM. C'est ce que vous devez connaître. Si vous voulez savoir d'où vient ce facteur 6, vous trouverez le contexte ci-dessous.</p>

:::gevorderd
<h3>Étape par étape</h3>
<ol class="steps">
<li><span>Prenez un émetteur AM de <b>60 W</b>, modulé à fond (100 %).</span></li>
<li><span>Cette puissance est répartie sur 3 parties. La porteuse reçoit <b>2/3</b> : 60 × 2/3 = <b>40 W</b>.</span></li>
<li><span>Chaque bande latérale reçoit <b>1/6</b> : 60 × 1/6 = <b>10 W</b> par bande latérale.</span></li>
<li><span>Le récepteur n'a besoin que d'une seule bande latérale pour vous comprendre. La partie utile est donc de <b>10 W</b>.</span></li>
<li><span>Un émetteur SSB de <b>10 W</b> met toute sa puissance dans cette seule bande latérale. Résultat : aussi fort que 60 W en AM.</span></li>
</ol>

<div class="tbl"><table>
<tr><th>AM 60 W</th><th>Puissance</th><th>Utile ?</th></tr>
<tr><td>porteuse</td><td>40 W</td><td>non, aucun message</td></tr>
<tr><td>bande latérale inférieure</td><td>10 W</td><td>en double, même message</td></tr>
<tr><td>bande latérale supérieure</td><td>10 W</td><td><b>oui</b></td></tr>
</table></div>

<h3>Où se trouve mon signal SSB ?</h3>
<div class="formula"><div class="f">USB : f = f<small>display</small> + f<small>audio</small></div>
<div class="f">LSB : f = f<small>display</small> − f<small>audio</small></div>
<div class="leg">f<small>display</small> = la fréquence affichée sur votre écran. f<small>audio</small> = la hauteur de votre voix ou de la tonalité.</div></div>

<div class="card"><b class="k">Exemple résolu</b>
<ol class="steps">
<li><span>Affichage : <b>14,200 MHz</b>, mode USB. Vous sifflez une tonalité de 1 kHz.</span></li>
<li><span>USB, donc on additionne : 14,200 MHz + 0,001 MHz.</span></li>
<li><span>Votre signal se trouve sur <b>14,201 MHz</b>.</span></li>
</ol>
</div>

<h3>Largeur de bande</h3>
<div class="formula"><div class="f">B<small>AM</small> = 2 × f<small>audio,max</small></div>
<div class="f">B<small>SSB</small> ≈ f<small>audio,max</small></div>
<div class="leg">Voix jusqu'à 3 kHz : l'AM fait 6 kHz de large, la SSB environ 3 kHz. La SSB prend donc la moitié de la place.</div></div>
:::

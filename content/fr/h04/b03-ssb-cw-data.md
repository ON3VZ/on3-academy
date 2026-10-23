---
id: h04-b3
type: brokje
kort: SSB, CW, données
titel: SSB, CW et données
uba_ref: hfst. 4, p. 14 tot 16
checkvragen: [C-h04-3a, C-h04-3b, C-h04-3c, C-h04-3d]
examenvragen: [O107, O108, O109, O110, O111, O112]
---
<h3>SSB : de l'AM sans le superflu</h3>
<div class="card kern"><b class="k">L'essentiel</b>
Un signal AM se compose de <b>3 parties</b> : la porteuse, une bande latérale inférieure et une bande latérale supérieure. La porteuse ne contient <b>aucun</b> message. Les deux bandes latérales contiennent <b>le même</b> message. La BLU (bande latérale unique, en anglais SSB, <i>single sideband</i>) supprime la porteuse et une bande latérale, et met toute la puissance dans la bande latérale qui reste.
</div>

:::gevorderd
<div class="figwrap">{{svg:spectrum-am-ssb}}<div class="figcap">Spectre : horizontalement la fréquence, verticalement la puissance. Exemple avec une voix jusqu'à 3 kHz autour de 7,100 MHz.</div></div>
:::

<div class="tbl"><table>
<tr><th>Abréviation</th><th>Signification</th><th>Ce qui reste</th></tr>
<tr><td>SSB</td><td>single sideband, bande latérale unique (BLU)</td><td>une seule bande latérale</td></tr>
<tr><td>USB</td><td>upper sideband</td><td>la bande latérale au-dessus de la porteuse</td></tr>
<tr><td>LSB</td><td>lower sideband</td><td>la bande latérale en dessous de la porteuse</td></tr>
</table></div>

<div class="formula"><div class="f">P<small>AM</small> ≈ 6 × P<small>SSB</small></div>
<div class="leg">Pour être reçu aussi fort qu'avec 10 W en SSB, il vous faut environ 60 W en AM. Le calcul se trouve dans « Points difficiles ».</div></div>

:::gevorderd
Convention entre radioamateurs : en dessous de 10 MHz, on utilise généralement la <b>LSB</b>, à partir de 10 MHz généralement l'<b>USB</b>.
:::

<h3>CW : la modulation la plus simple</h3>
<div class="card kern"><b class="k">L'essentiel</b>
En CW (morse), vous <b>allumez et éteignez</b> simplement la porteuse au rythme des signes morse. Allumée brièvement = un point, allumée longtemps = un trait.
</div>

:::gevorderd
Vous utilisez un manipulateur au lieu d'un microphone.
:::

<h3>Données : un ordinateur au lieu d'un microphone</h3>
<div class="figwrap">{{svg:data-tnc}}<div class="figcap">En communication de données, l'ordinateur pilote l'émetteur par l'intermédiaire d'un modem ou d'un TNC.</div></div>
<ol class="steps">
<li><span>L'ordinateur produit des <b>bits</b> : des zéros et des uns.</span></li>
<li><span>Un modem radio ou un <b>TNC</b> (Terminal Node Controller) en fait des <b>tonalités audio</b> : une tonalité pour un 0, une autre tonalité pour un 1. Un modem ne produit donc pas de signal RF, seulement des tonalités.</span></li>
<li><span>Ces tonalités entrent dans l'émetteur comme si c'était votre voix.</span></li>
</ol>

:::gevorderd
L'émetteur continue de fonctionner en SSB ou en FM, comme l'indique aussi le dessin.
:::
<div class="card"><span class="extra-tag">bon à savoir</span>Les modes numériques modernes comme le FT8 n'utilisent plus de TNC séparé. C'est la carte son de l'ordinateur qui produit les tonalités.</div>

<h3>Tous les signaux côte à côte</h3>
<div class="figwrap">{{svg:signalen}}<div class="figcap">Voici à quoi ressemblent les quatre types sur un dessin.</div></div>

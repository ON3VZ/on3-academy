---
id: h04-b4
type: brokje
kort: L'émetteur
titel: L'émetteur, bloc par bloc
uba_ref: hfst. 4, p. 14 tot 16
checkvragen: [C-h04-4a, C-h04-4b, C-h04-4c]
examenvragen: [O082, O083, O084, O085, O086, O087, O088, O089, O090, O091, O092, O093, O094, O095, O096, O097, O098, O099, O100, O101, O102, O113, O114]
---
<div class="figwrap">{{svg:zender}}<div class="figcap">En haut, le signal à haute fréquence voyage de gauche à droite. En bas, votre voix entre dans le schéma.</div></div>

<div class="tbl"><table>
<tr><th>Bloc</th><th>Rôle</th><th>Relié à</th></tr>
<tr><td>générateur de fréquence</td><td>Produit la porteuse et <b>détermine la fréquence d'émission</b>. On l'appelle aussi oscillateur.</td><td>uniquement le modulateur</td></tr>
<tr><td>microphone</td><td>Transforme votre voix en un petit signal électrique.</td><td>uniquement l'amplificateur de microphone</td></tr>
<tr><td>amplificateur de microphone</td><td>Renforce le faible signal du microphone. C'est ici que vous réglez la force de votre modulation.</td><td>microphone et modulateur</td></tr>
<tr><td>modulateur</td><td>Réunit la porteuse et l'audio : c'est ici que se fait <b>la modulation</b>.</td><td>générateur de fréquence, amplificateur de microphone et amplificateur de puissance RF</td></tr>
<tr><td>amplificateur de puissance RF</td><td>Amplifie le signal modulé jusqu'à la <b>puissance souhaitée</b>. On l'appelle aussi étage final ou amplificateur final HF.</td><td>modulateur et ligne de transmission</td></tr>
<tr><td>ligne de transmission</td><td>Amène le signal de l'émetteur à l'antenne. On l'appelle aussi ligne d'alimentation ou câble coaxial.</td><td>amplificateur de puissance RF et antenne</td></tr>
<tr><td>antenne</td><td>Transforme le signal électrique en <b>ondes radio</b>.</td><td>uniquement la ligne de transmission</td></tr>
</table></div>

<div class="card ana"><b class="k">Comparaison</b>
Une entreprise postale. Le <b>générateur de fréquence</b> fournit des enveloppes vides avec une adresse fixe : la fréquence. Vous écrivez une lettre (<b>microphone</b>), qui est recopiée au propre (<b>amplificateur de microphone</b>). Dans le <b>modulateur</b>, la lettre entre dans l'enveloppe. L'<b>amplificateur de puissance RF</b> est le camion au moteur puissant, la <b>ligne de transmission</b> est la route et l'<b>antenne</b> est l'aéroport où tout s'envole.
</div>

<h3>Que détermine le générateur de fréquence, et que ne détermine-t-il pas ?</h3>
<div class="tbl"><table>
<tr><th>Détermine</th><th>Ne détermine pas</th></tr>
<tr><td>la fréquence sur laquelle vous émettez</td><td>le type de modulation (AM, FM, SSB), la puissance d'émission, l'accord entre l'émetteur et l'antenne, le ROS, la qualité de la modulation</td></tr>
</table></div>

<div class="card trap"><b class="k">Piège</b>
Si vous émettez en dehors des bandes amateurs, c'est dû à un <b>générateur de fréquence mal réglé</b>, pas à l'antenne, à la ligne de transmission ou au microphone. Conséquence : vous pouvez <b>perturber d'autres utilisateurs</b>. En dehors de la bande, il n'existe pas d'autres règles ni de règles plus souples.
</div>

<div class="card trap"><b class="k">Attention à votre étage final</b>
Si l'antenne n'est <b>pas bien adaptée</b> à l'émetteur, une partie de la puissance revient vers l'émetteur. L'<b>étage final</b> peut alors être <b>endommagé</b>. La fréquence et la modulation ne changent pas pour autant. Vous en apprendrez davantage dans le chapitre sur les antennes et le ROS.
</div>

<div class="card"><b>Pour les données</b>, l'ordinateur et le modem remplacent le microphone. Le reste du schéma ne change pas.</div>

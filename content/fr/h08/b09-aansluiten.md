---
id: h08-b9
type: brokje
kort: Raccorder et régler
titel: Raccorder la station, mesurer le ROS, régler un dipôle
uba_ref: hfst. 8.6, p. 37 en 38
checkvragen: [C-h08-9a, C-h08-9b, C-h08-9c]
examenvragen: []
---
:::kern
Un émetteur se raccorde à une **alimentation** (avec la **bonne polarité**) et, via le **câble coaxial**, à l'**antenne**. Avec un **ROS-mètre**, vous vérifiez si l'antenne convient. Un dipôle se règle en le raccourcissant ou en l'allongeant pas à pas jusqu'à ce que le ROS soit le plus bas. Cela fait partie de l'**épreuve pratique**.
:::

{{svg:h08-aansluiten|De l'alimentation à l'antenne.}}

### Raccorder
1. Alimentation **éteinte**.
2. Fil rouge (**+**) sur le plus, fil noir (**−**) sur le moins. **À l'inverse, l'émetteur peut être détruit.**
3. Câble coaxial de l'antenne sur la prise d'antenne (généralement à l'arrière), éventuellement via un ROS-mètre et une boîte d'accord.
4. Alimentation allumée, appareil allumé.

### Mesurer le ROS avec un ROS-mètre à bouton de sensibilité
1. Mettez la **sensibilité** au minimum (bouton complètement à gauche).
2. Émettez avec une **faible puissance** : vous protégez ainsi l'émetteur si le ROS se révèle élevé.
3. Ouvrez lentement la sensibilité jusqu'à ce que l'instrument pour la puissance **directe** (forward) soit en **pleine déviation**.
4. Lisez le **ROS** sur l'autre instrument (ou mettez le commutateur sur « reflected »).

Avec un **appareil à aiguilles croisées**, vous lisez le ROS à l'endroit où les deux aiguilles se croisent.

### Régler un dipôle
1. Calculez la longueur : 150 ÷ f (voir chapitre 5).
2. Faites le dipôle **quelques pour cent plus long** : raccourcir est plus facile qu'allonger.
3. Mesurez le ROS et notez-le.
4. **Émetteur éteint.** Raccourcissez les deux moitiés d'environ **1 %**.
5. Mesurez à nouveau. Si le ROS a **baissé**, continuez à raccourcir. S'il a **augmenté**, vous êtes allé trop loin : rallongez-le un peu.
6. Continuez ainsi jusqu'à ce que le ROS ne baisse plus.
7. Revenez en arrière d'un pas **plus petit** (environ un dixième du précédent) et mesurez à nouveau, jusqu'à trouver le minimum.
8. Un ROS inférieur à **1,5 : 1** est généralement suffisant. 1 : 1 n'est pas nécessaire.

:::valkuil Sécurité
**Ne touchez jamais une antenne pendant l'émission.** Elle porte une tension haute fréquence qui peut provoquer des brûlures. Éteignez l'émetteur avant chaque modification.
:::

:::valkuil
Faites les **deux moitiés** du dipôle de la même longueur. Raccourcir une seule moitié rend l'antenne asymétrique (elle n'est plus symétrique).
:::

---
id: h05-b7
type: brokje
kort: Coaxial et connecteurs
titel: Le câble vers l'antenne : coaxial et connecteurs
uba_ref: hfst. 5.3, p. 20
checkvragen: [C-h05-7a, C-h05-7b, C-h05-7c]
examenvragen: [O138, O139, O140, O141, O142, O143, O144, O145]
---
:::kern
L'émetteur est à l'intérieur, l'antenne à l'extérieur. Le câble entre les deux s'appelle la **ligne de transmission** (ou ligne d'alimentation). Elle doit amener la puissance à l'antenne avec **le moins de pertes possible** et ne doit **pas rayonner elle-même**. Pour cela, on utilise presque toujours du **câble coaxial** (en bref : du coaxial), parce qu'il est bien **blindé**.
:::

{{svg:h05-coax|Les quatre couches d'un câble coaxial.}}

| Couche | En quoi ? | Que fait-elle ? |
|---|---|---|
| conducteur central | fil de cuivre au milieu | transporte le signal |
| diélectrique | matériau isolant (plastique) | maintient le conducteur central bien au milieu |
| blindage | tresse de fins fils de cuivre | garde le signal **dans** le câble et les perturbations **dehors** |
| gaine | couche extérieure en plastique | protège contre les intempéries et surtout contre l'**eau** |

:::vergelijk Comparaison
Une conduite d'eau dans un tunnel. L'eau (le signal) coule dans le tuyau au milieu. La paroi du tunnel (le blindage) veille à ce que rien ne fuie vers l'extérieur et que rien n'entre de l'extérieur.
:::

:::valkuil
Un simple cordon secteur (à deux ou trois conducteurs) ou « un câble étanche » ne **convient pas**. On ne choisit pas le coaxial parce qu'il est bon marché, souple ou étanche, mais pour son **blindage**. Et un coaxial ne doit justement **pas** rayonner le signal : c'est le travail de l'antenne.
:::

### Connecteurs
Aux extrémités du coaxial, on met des **connecteurs** (fiches). Utilisez uniquement des connecteurs conçus **spécialement pour la RF** (radiofréquence). Une fiche quelconque qui supporte la puissance ne suffit pas.

{{foto:h05-connectoren-overzicht.jpg|PL259, BNC et N, chaque fois la partie câble et (pour la PL259 et la BNC) la partie châssis.}}

| Connecteur | Se reconnaît à | Usage |
|---|---|---|
| **PL259** | fiche épaisse avec une **bague à visser** et une broche au milieu. La partie châssis (SO239) est carrée avec quatre petits trous | HF, le plus utilisé dans la station (shack) |
| **BNC** | plus petit, avec une **fixation à baïonnette** : pousser et tourner d'un quart de tour | appareils de mesure, portatifs |
| **N** | plus grand, bague à visser, étanche | VHF et UHF, à l'extérieur |
| **SMA / RP SMA** | très petit, avec un filetage | récepteurs SDR, portatifs |

Pour l'examen, vous devez certainement reconnaître la **PL259** et la **BNC**.

{{foto:h05-connectoren-abcd-1.png|Quatre connecteurs de câble : A est une BNC, C est une PL259. B (cinch, RCA) et D (DIN) ne sont pas des connecteurs RF.}}

{{foto:h05-connectoren-abcd-2.png|Quatre parties châssis : B est la partie châssis d'une PL259, C est une BNC. A (jack) et D (DIN) servent à l'audio ou aux données.}}

### Bien raccorder le blindage
Le blindage doit être bien fixé au connecteur **sur tout le pourtour**. Sinon, du signal RF **sort** du câble (vous perturbez d'autres appareils) ou des perturbations **entrent**.

{{foto:h05-pl259-fout-goed.jpg|À gauche, incorrect : le blindage n'est pas bien fixé. À droite, correct : le connecteur est proprement monté sur le câble.}}

:::weetje
Comment monter vous-même une PL259 ou une fiche N sur un coaxial est expliqué pas à pas dans le manuel (chapitre 12, HowTo câbles et connecteurs). Ce n'est pas matière d'examen, mais c'est bien utile pour plus tard.
:::

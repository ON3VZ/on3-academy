---
id: h05-b2
type: brokje
kort: Le dipôle
titel: Le dipôle : la base de toutes les antennes
uba_ref: hfst. 5.2, p. 17 en 18
checkvragen: [C-h05-2a, C-h05-2b, C-h05-2c]
examenvragen: [O163, O152, O153, O159]
---
:::kern
Un **dipôle** est un fil ou un tube interrompu en son **milieu**. C'est à cette interruption (le **point d'alimentation**) qu'arrive le câble venant de l'émetteur. Si le dipôle mesure **une demi-longueur d'onde (λ/2)**, il est en résonance et fonctionne le mieux.
:::

{{svg:h05-dipool|À gauche suspendu à l'horizontale, à droite à la verticale. C'est toujours la même antenne.}}

:::formule
longueur dipôle = λ ÷ 2 = 150 ÷ f
--
longueur en mètres (m) · f = fréquence en mégahertz (MHz) · 150 est la moitié de 300
:::

### Exemple résolu
« Vous voulez un dipôle pour 10 MHz. Quelle longueur doit-il avoir ? »

1. Longueur d'onde : λ = 300 ÷ 10 = **30 m**.
2. Demi-longueur d'onde : 30 ÷ 2 = **15 m**.
3. Le dipôle mesure donc 15 m : deux fils de 7,5 m, avec le point d'alimentation au milieu.

| Bande | Fréquence | Dipôle (150 ÷ f) |
|---|---|---|
| 80 m | 3,6 MHz | environ 42 m |
| 40 m | 7,1 MHz | environ 21 m |
| 20 m | 14,2 MHz | environ 10,6 m |
| 2 m | 145 MHz | environ 1 m |

### À quoi ressemble le courant ?

- Au **milieu**, le courant est le **plus grand**.
- Aux **extrémités**, le courant est **nul** : il ne peut plus aller nulle part.
- Entre les deux, il monte et descend comme une demi-sinusoïde. Exactement une demi-onde tient sur un dipôle demi-onde.

{{foto:h05-dipool.png|Un vrai dipôle : deux tubes, avec au milieu un petit boîtier où entre le coaxial.}}

:::valkuil
Un « dipôle λ/2 » mesure une **demi**-longueur d'onde, pas une longueur d'onde entière et pas non plus un quart. Le nom le dit : λ/2 = lambda divisé par 2.
:::

:::weetje
En pratique, on fait un dipôle filaire quelques pour cent plus court que 150 ÷ f, puis on le coupe à la bonne longueur en mesurant le ROS (voir la page sur le ROS). Pour l'examen, « environ une demi-longueur d'onde » suffit.
:::

<details class="zelf" markdown="1"><summary>Essayez vous-même : quelle est la longueur d'un dipôle pour 7,5 MHz ?</summary>

λ = 300 ÷ 7,5 = 40 m. La moitié : **20 m**. Ou directement : 150 ÷ 7,5 = 20 m.

</details>
<details class="zelf" markdown="1"><summary>Essayez vous-même : quelle est la longueur d'un dipôle pour 150 MHz ?</summary>

150 ÷ 150 = **1 m**.

</details>

### Reconnaître les antennes sur un dessin
À l'examen, vous devez reconnaître des antennes. Sur ce dessin, regardez B et C : ce sont tous deux des dipôles (un trait avec une interruption au milieu).

{{svg:h05-antennes-abcd-1|A : 5/8 λ avec bobine. B : dipôle horizontal. C : dipôle vertical. D : yagi.}}

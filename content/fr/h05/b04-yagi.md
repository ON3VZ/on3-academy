---
id: h05-b4
type: brokje
kort: Yagi, omnidirectionnelle et directive
titel: Antennes omnidirectionnelles et antennes directives
uba_ref: hfst. 5.2, p. 18 en 19
checkvragen: [C-h05-4a, C-h05-4b, C-h05-4c]
examenvragen: [O154, O158, O164, O165, O166, O167, O168, O169]
---
:::kern
Une antenne **omnidirectionnelle** émet avec la même force dans toutes les directions de la rose des vents. Une **antenne directive** concentre la puissance dans une seule direction. L'antenne directive la plus connue est la **yagi**.
:::

### La yagi
{{svg:h05-yagi|Vue de dessus : à l'arrière le réflecteur, puis l'élément rayonnant alimenté, à l'avant les directeurs.}}

| Élément | Position | Longueur |
|---|---|---|
| **réflecteur** | derrière l'élément rayonnant | un peu **plus long** que l'élément rayonnant |
| **élément rayonnant** | l'élément auquel est raccordé le coaxial | un dipôle |
| **directeur(s)** | devant l'élément rayonnant | un peu **plus court(s)** que l'élément rayonnant |
| **support (boom)** | le tube sur lequel tout est fixé | |

- Le rayonnement part du côté des **directeurs**.
- Seul l'élément rayonnant est raccordé. Le réflecteur et les directeurs « poussent » l'onde vers l'avant.

{{foto:h05-yagi.png|Une yagi sur un mât : beaucoup de brins parallèles sur un seul support.}}

### Gain
Comme la yagi concentre la puissance dans une seule direction, il arrive beaucoup plus de signal dans **cette** direction qu'avec un simple dipôle. C'est ce qu'on appelle le **gain** de l'antenne. L'antenne ne crée pas de puissance en plus : elle envoie simplement la même puissance de façon plus ciblée.

:::vergelijk Comparaison
Une lampe ordinaire face à une lampe de poche. La lampe éclaire un peu toute la pièce. La lampe de poche n'a pas d'ampoule plus puissante, mais un petit miroir qui concentre la lumière : dans une direction, c'est beaucoup plus lumineux, à côté il fait sombre.
:::

À la réception aussi : la yagi entend mieux la direction voulue et **atténue les perturbations** venant des autres directions.

### Diagramme de rayonnement : vu d'en haut
{{svg:h05-straling|La tache bleue montre jusqu'où va le signal dans chaque direction.}}

| Omnidirectionnelle | Non omnidirectionnelle |
|---|---|
| dipôle λ/2 vertical | dipôle λ/2 **horizontal** (2 directions privilégiées, perpendiculaires au fil) |
| ground plane λ/4 | **yagi** (1 direction privilégiée) |
| 5/8 λ (verticale) | long fil alimenté en bout |

:::valkuil
Un dipôle **horizontal** n'est **pas** omnidirectionnel (s'il est suspendu à au moins une demi-longueur d'onde de hauteur) : il rayonne surtout perpendiculairement au fil. Un dipôle **vertical**, lui, est omnidirectionnel. Faites attention au mot horizontal ou vertical dans la question.
:::

:::weetje
Le gain d'une yagi vient **uniquement** de la concentration du rayonnement. Pas du métal dont elle est faite, ni de la polarisation.
:::

---
id: h05-b3
type: brokje
kort: Quart d'onde, ground plane, 5/8 λ, long fil
titel: Antennes avec plan de sol ou contrepoids
uba_ref: hfst. 5.2, p. 18 en 19
checkvragen: [C-h05-3a, C-h05-3b, C-h05-3c]
examenvragen: [O155, O156, O157, O160]
---
:::kern
Vous pouvez **couper un dipôle en deux**. Il vous reste alors une moitié (un **quart de longueur d'onde**, λ/4), que vous placez debout sur une surface conductrice. Cette surface joue le rôle de la moitié manquante. Le quart d'onde, la ground plane, la 5/8 λ et le long fil reposent tous sur cette idée.
:::

### 1. Antenne quart d'onde (λ/4)
{{svg:h05-kwartgolf|Le plan de sol reflète le brin. Ensemble, ils sont aussi longs qu'un dipôle.}}

- Un brin de **λ/4** sur un **plan de sol** : une plaque métallique (par exemple le toit d'une voiture) ou des fils posés en étoile dans le sol.
- Le plan de sol agit comme un **miroir** : il crée la moitié manquante.

:::vergelijk Comparaison
Une cuillère à moitié posée contre un miroir : vous voyez une cuillère entière, alors qu'il n'y en a qu'une moitié. Le quart d'onde « se voit » dans le plan de sol et se comporte comme un dipôle complet.
:::

### 2. Antenne ground plane
{{svg:h05-groundplane|Les radians descendent en oblique, à environ 45 degrés.}}

- Un quart d'onde placé **en haut d'un mât**. Le sol est alors trop loin pour servir de miroir.
- C'est pourquoi on fabrique soi-même un plan de sol avec quelques fils de **λ/4 chacun** : les **radians**. Ils descendent généralement en oblique, à environ **45°**.
- Le brin vertical s'appelle l'**élément rayonnant**.

{{foto:h05-groundplane.png|Une vraie ground plane : un brin vers le haut, quelques brins obliques vers le bas.}}

### 3. L'antenne 5/8 λ
{{svg:h05-58|Un long brin avec une bobine en bas : c'est ainsi que vous reconnaissez une 5/8 λ.}}

- Comme un quart d'onde, mais **plus longue : 5/8 de longueur d'onde**.
- Surtout en **VHF et UHF**, un peu meilleure qu'un quart d'onde : le rayonnement part davantage vers l'horizon et moins vers le ciel.
- Cette longueur n'est **pas naturellement en résonance**. Une **bobine** à la base règle ce problème.

### 4. Antenne filaire alimentée en bout (long fil)
{{svg:h05-langdraad|Un seul long fil, alimenté à une extrémité. La terre forme la seconde moitié.}}

- Simplement un **long fil**, par exemple entre deux mâts ou deux arbres, et raccordé à **une seule extrémité**.
- La **terre** sert de contrepoids (la seconde moitié).
- La fréquence de résonance dépend de la **longueur** du fil et de sa **hauteur** au-dessus du sol.

:::valkuil
Reconnaissez-les à leur forme, pas à leur taille :

- **dipôle** : un trait avec une interruption au milieu ;
- **ground plane** : un brin vers le haut + des fils obliques vers le bas ;
- **5/8 λ** : un brin + une **bobine** sur un plan de sol ;
- **long fil** : un long fil entre des mâts, alimenté d'un côté, avec une mise à la terre.
:::

{{svg:h05-antennes-abcd-2|A : 5/8 λ. B : long fil alimenté en bout. C : dipôle vertical. D : ground plane.}}

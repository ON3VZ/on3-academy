---
id: h05-b10
type: brokje
kort: Symétrique et balun
titel: Antennes symétriques et asymétriques, le balun
uba_ref: hfst. 5.5, p. 23
checkvragen: [C-h05-10a, C-h05-10b, C-h05-10c]
examenvragen: [O175, O176, O177, O178, O179]
---
:::kern
Une antenne est **symétrique** si les parties à gauche et à droite du point d'alimentation sont l'**image miroir** l'une de l'autre. Si les deux parties sont différentes, elle est **asymétrique**. Si vous voulez raccorder une antenne symétrique (un dipôle) à un câble asymétrique (un coaxial), vous utilisez un **balun**.
:::

{{svg:h05-symmetrie|À gauche, deux moitiés identiques. À droite, un brin et un plan de sol : deux parties différentes.}}

| Symétrique | Asymétrique |
|---|---|
| dipôle λ/2 (horizontal ou vertical) | ground plane λ/4 |
| yagi (l'élément rayonnant est un dipôle) | 5/8 λ |
| | long fil alimenté en bout |

### Le coaxial est asymétrique
Un câble coaxial a un **fil** à l'intérieur et un **tube** tout autour (le blindage). Deux parties différentes : asymétrique.

- Avec une **antenne asymétrique**, cela convient bien : le **conducteur central** va vers l'**élément rayonnant**, le **blindage** vers le **plan de sol**, les radians ou la mise à la terre.
- Avec un **dipôle**, les deux moitiés sont identiques. Si vous y raccordez directement le coaxial, cela fonctionne, mais l'**extérieur du blindage se met à rayonner** aussi. Conséquence : plus de risques de **perturbations** (voir chapitre 7, CEM).

{{svg:h05-balun|Le balun se place entre le coaxial et le milieu du dipôle.}}

:::formule
balun = **bal**anced → **un**balanced
--
balanced = symétrique (le dipôle) · unbalanced = asymétrique (le coaxial)
:::

:::vergelijk Comparaison
Un adaptateur de prise en voyage : l'appareil et la prise de courant ne vont pas ensemble, l'adaptateur fait la transition. Le balun est l'adaptateur entre une antenne symétrique et un câble asymétrique.
:::

:::valkuil
Une **yagi** est symétrique, même si elle a l'air compliquée : regardez l'élément alimenté, c'est un dipôle. Une **5/8 λ** et une **ground plane** sont asymétriques, même si elles sont bien droites.
:::

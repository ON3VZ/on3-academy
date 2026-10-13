---
id: h05-b1
type: brokje
kort: Que fait une antenne ?
titel: Que fait une antenne ?
uba_ref: hfst. 5.1, p. 17
checkvragen: [C-h05-1a, C-h05-1b, C-h05-1c]
examenvragen: [O146, O147, O148, O161, O162]
---
:::kern
Une antenne est un **convertisseur**. À l'émission, elle transforme un signal électrique en onde radio. À la réception, elle transforme une onde radio en signal électrique. La même antenne fait les deux : c'est pourquoi une seule antenne suffit à la maison pour émettre et recevoir.
:::

{{svg:h05-omzetter|À gauche, l'antenne émet. À droite, elle reçoit. C'est chaque fois le même type d'antenne.}}

| Lors de | De | Vers |
|---|---|---|
| l'émission | signal électrique (venant de l'émetteur, par le coaxial) | onde radio (dans l'air) |
| la réception | onde radio (venant de l'air) | signal électrique (par le coaxial vers le récepteur) |

### Résonance : l'antenne a sa « propre » fréquence
Chaque antenne fonctionne le mieux sur une fréquence bien précise : sa **fréquence de résonance**. À cette fréquence, presque toute la puissance part dans l'air. Plus vous vous en éloignez, plus il y a de pertes.

:::vergelijk Comparaison
Une corde de guitare. Quand vous la pincez, elle donne toujours la même note. Une corde **plus longue** donne une note **plus grave**. Pour une antenne, c'est pareil : une antenne **plus longue** correspond à une fréquence **plus basse**.
:::

{{svg:h05-resonantie|L'onde ne tient exactement sur l'antenne que si la longueur est la bonne.}}

- La plage autour de la fréquence de résonance où les pertes restent faibles s'appelle la **bande passante** de l'antenne.
- Si vous voulez émettre bien en dehors de cette bande passante, il vous faut un **réseau d'adaptation** (une boîte d'accord, voir plus loin) ou une antenne conçue spécialement pour cela.

### Pourquoi les antennes HF sont-elles si grandes et les antennes VHF si petites ?
La longueur d'une antenne dépend de la **longueur d'onde**. Fréquence basse (HF, ondes courtes) = onde longue = grande antenne. Fréquence haute (VHF, UHF) = onde courte = petite antenne.

{{svg:h05-grootte|Un dipôle pour le 80 m mesure plus de 40 mètres, pour le 2 m même pas un mètre et demi.}}

:::valkuil
Grande ou petite, le **fonctionnement est le même**. Une antenne HF ne fonctionne pas « autrement » qu'une antenne VHF, et la différence de taille n'a rien à voir avec la polarisation. Seule la longueur d'onde détermine la dimension.
:::

:::weetje
La conversion se fait **dans l'antenne**. Pas dans la ligne de transmission (qui ne fait que transporter le signal), et pas non plus dans le modulateur ou le démodulateur.
:::

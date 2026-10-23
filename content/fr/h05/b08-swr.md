---
id: h05-b8
type: brokje
kort: ROS
titel: ROS : l'antenne convient-elle à l'émetteur ?
uba_ref: hfst. 5.4, p. 21 en 22
checkvragen: [C-h05-8a, C-h05-8b, C-h05-8c, C-h05-8d]
examenvragen: [O172, O173, O180, O181, O182]
---
:::kern
Si l'antenne convient bien à l'émetteur et à la fréquence, presque toute la puissance va vers l'antenne. Si elle ne convient pas bien, **une partie revient** vers l'émetteur : c'est la **puissance réfléchie**. Le **ROS** (rapport d'ondes stationnaires, en anglais **SWR**, Standing Wave Ratio) indique quelle quantité revient. On le mesure avec un **ROS-mètre**.
:::

{{svg:h05-swr|À l'aller, la puissance va vers l'antenne. Au retour revient ce que l'antenne n'absorbe pas.}}

:::vergelijk Comparaison
De l'eau que vous versez avec un tuyau d'arrosage dans un seau. Si le seau est bien placé sous le tuyau, toute l'eau y entre. S'il est de travers, une partie rejaillit. Plus il en rejaillit, plus l'« adaptation » est mauvaise, plus le ROS est élevé.
:::

### Les chiffres
| ROS | Signification |
|---|---|
| **1 : 1** (1/1) | parfait : rien ne revient |
| **1,5 : 1 ou moins** | très bon : les émetteurs modernes délivrent toute leur puissance |
| **jusqu'à 2 : 1** | encore acceptable en pratique (mesuré à la sortie de l'émetteur) |
| plus de 2 : 1 | au-delà d'environ 1,5 : 1, beaucoup d'émetteurs modernes réduisent déjà automatiquement leur puissance ; au-delà de 2 : 1, le ROS est trop élevé en pratique |
| **infini** | tout revient |

### Pourquoi un ROS élevé est-il mauvais ?

- La puissance réfléchie est transformée en **chaleur** dans l'émetteur.
- S'il y en a trop, l'**étage final** (amplificateur de puissance RF) de l'émetteur peut être **endommagé**.

### Que signifie un ROS élevé ?
Le ROS-mètre montre si le **système d'antenne** (antenne + câble) est **adapté** à l'émetteur. Si vous mesurez soudain un ROS élevé sur une fréquence qui était bonne avant, le défaut se trouve généralement dans l'**antenne** ou dans la **ligne de transmission** (câble, connecteur). **Pas** dans l'émetteur.

:::valkuil
- Un ROS élevé désigne l'**antenne ou le câble**, jamais l'amplificateur micro, le modulateur ou l'étage final.
- Un ROS-mètre ne mesure rien concernant la surmodulation, l'excursion de fréquence ou la stabilité de fréquence. Il mesure uniquement si l'antenne est adaptée.
:::

### L'antenne doit convenir à la fréquence
Un système d'antenne doit convenir à **la fréquence sur laquelle vous émettez**. Peu importe la marque de votre émetteur ou la modulation utilisée : BLU (bande latérale unique, en anglais SSB), CW ou FM. Si l'antenne ne convient pas à cette fréquence, elle n'est **pas adaptée** à l'émetteur et ne fonctionne **pas efficacement**.

### Régler pour le ROS le plus bas
Avec un dipôle, vous pouvez ajuster la longueur :

1. Émettez brièvement à faible puissance et lisez le ROS.
2. **Arrêtez d'émettre** avant de toucher l'antenne. Ne touchez jamais une antenne pendant l'émission.
3. Raccourcissez ou rallongez un peu l'antenne.
4. Mesurez à nouveau. Recommencez jusqu'à ce que le ROS soit le plus bas possible.

Si le ROS est le plus bas sur une fréquence **plus basse** que souhaitée, l'antenne est trop longue : raccourcissez-la. Si le minimum se trouve **plus haut**, elle est trop courte.

:::weetje Hors matière d'examen : pourquoi « onde stationnaire » ?
L'onde aller et l'onde réfléchie se superposent dans le câble. La tension n'est donc pas partout la même : il apparaît un motif d'onde qui « reste sur place ».

{{svg:h05-swr-staand|Tension le long du câble pour un ROS de 1, de 2 et infini.}}

ROS = U<sub>max</sub> ÷ U<sub>min</sub>. Avec un ROS de 1, la tension est partout la même. Avec un ROS infini, elle tombe à zéro à certains endroits.
:::

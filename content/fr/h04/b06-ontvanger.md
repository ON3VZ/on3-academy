---
id: h04-b6
type: brokje
kort: Le récepteur
titel: Le récepteur, bloc par bloc
uba_ref: hfst. 4.3, p. 16
checkvragen: [C-h04-6a, C-h04-6b, C-h04-6c]
examenvragen: [O121, O122, O123, O124, O125, O126, O127, O128, O129, O130, O131, O132, O133, O135, O136]
---
:::kern
Un récepteur fait l'inverse d'un émetteur. L'antenne capte les ondes radio, le récepteur choisit le signal voulu, en extrait à nouveau la parole ou les données et les rend assez fortes pour un haut-parleur ou un casque.
:::

{{svg:ontvanger|Le chemin du signal : de la gauche (antenne) vers la droite (haut-parleur).}}

| Bloc | Que fait-il ? | Relié à |
|---|---|---|
| antenne | capte les ondes radio et en fait un petit signal électrique | uniquement la ligne de transmission |
| ligne de transmission | amène le signal de l'antenne au récepteur (câble coaxial) | antenne et accord + amplification RF |
| accord + amplification RF | choisit **le seul signal** que vous voulez entendre parmi tous les signaux (accorder) et l'amplifie | ligne de transmission et démodulateur |
| démodulateur (détecteur) | extrait la parole ou les données **de** l'onde radio | accord + amplification RF et amplificateur audio |
| amplificateur audio | rend la parole assez forte | démodulateur et haut-parleur |
| haut-parleur ou casque | en refait du son. Pour les données, le signal va vers un ordinateur | uniquement l'amplificateur audio |

### Les trois étages
| Étage | Place | Que se passe-t-il ? |
|---|---|---|
| 1er étage | **étage d'entrée** | accord (et amplification RF) |
| 2e étage | entre l'entrée et la sortie | démodulation |
| 3e étage | **étage de sortie** | amplification audio |

:::vergelijk Comparaison
Vous êtes à une fête bruyante et vous voulez comprendre un ami. D'abord, vous concentrez votre attention sur lui et vous ignorez le reste : c'est **l'accord**. Ensuite, vous extrayez ses mots du brouhaha : c'est **la démodulation**. Si votre voisin n'entend pas bien, vous répétez plus fort : c'est **l'amplification audio**.
:::

{{svg:zender-ontvanger|Simplifié : le générateur de fréquence, le microphone et la ligne de transmission de l'émetteur sont omis. Le schéma complet de l'émetteur se trouve dans « L'émetteur ». Le démodulateur fait l'inverse du modulateur.}}

:::valkuil
L'accord se fait **à l'avant** (étage d'entrée), pas dans le démodulateur ni dans l'amplificateur audio. Et l'antenne est reliée **uniquement** à la ligne de transmission, jamais directement à un autre bloc.
:::

### Symboles du schéma
| Bloc | Symbole |
|---|---|
| antenne | {{svg:sym-antenne}} |
| microphone | {{svg:sym-microfoon}} |
| haut-parleur | {{svg:sym-luidspreker}} |

---
id: h03-b02-voorvoegsels
type: brokje
kort: Milli, kilo, méga
titel: Grands et petits nombres : milli, kilo et méga
uba_ref: hfst. 3.2, p. 11
checkvragen: [C-h03-04, C-h03-05, C-h03-06]
examenvragen: []
---
:::kern
Pour ne pas devoir écrire sans cesse beaucoup de zéros, on place une lettre devant l'unité. **k** (kilo) signifie mille fois plus, **M** (méga) un million de fois plus, **m** (milli) mille fois moins.
:::

| Préfixe | Lettre | Signifie | Exemple |
|---|---|---|---|
| milli | m | × 0,001 (un millième) | 20 mA = 0,020 A |
| kilo | k | × 1 000 | 4,7 kΩ = 4 700 Ω |
| méga | M | × 1 000 000 | 14 MHz = 14 000 000 Hz |

{{svg:h03-voorvoegsels|Chaque marche de l'escalier correspond à un facteur 1000.}}

### Comment convertir, étape par étape
1. Regardez si vous allez vers une unité **plus grande** ou **plus petite**.
2. Vers une unité plus petite (par exemple de A vers mA) : le nombre devient **plus grand**, donc **fois 1000**. Déplacez la virgule de 3 rangs vers la droite.
3. Vers une unité plus grande (par exemple de mA vers A) : le nombre devient **plus petit**, donc **divisé par 1000**. Déplacez la virgule de 3 rangs vers la gauche.

:::vergelijk Comparaison avec les distances
1 kilomètre, c'est 1000 mètres. 1 millimètre, c'est un millième de mètre. Avec les volts, les ampères et les ohms, cela fonctionne exactement de la même façon.
:::

:::valkuil
**m** et **M** se ressemblent beaucoup, mais la différence est d'un milliard de fois. 5 mW (milliwatt), c'est un murmure ; 5 MW (mégawatt), c'est une centrale électrique.
:::

### Le tableau de conversion
Avec ce tableau, plus besoin de réfléchir à « fois » ou « divisé par ». Chaque colonne est un préfixe. **E** représente l'unité sans préfixe (V, A, Ω, W, Hz). Chaque colonne compte 3 cases, car entre deux préfixes il y a chaque fois un facteur 1000.

1. Placez le nombre dans le tableau : le **dernier chiffre avant la virgule** va dans la première case de la colonne de votre unité.
2. Placez la **virgule après la première case** de la colonne vers laquelle vous voulez aller.
3. Complétez les cases vides entre le nombre et la nouvelle virgule avec des **zéros**.
4. Lisez le nombre.

Essayez vous-même : tapez un nombre, choisissez l'unité de départ et l'unité d'arrivée. La virgule rouge montre où se place la virgule.

<div class="omreken" data-waarde="1" data-van="" data-naar="m" data-eenheid="V"></div>

### S'entraîner avec le tableau
Complétez et cliquez sur Vérifier. En cas d'erreur, vous voyez le tableau avec l'explication. Vous pouvez utiliser une virgule ou un point.

<div class="omreken-oef" data-oef='[["4,7","k","","Ω"],["20","m","","A"],["0,5","","m","A"],["1500","","k","V"],["14","M","k","Hz"],["3500","k","M","Hz"],["145,5","M","k","Hz"],["0,002","","m","A"],["250","m","","W"],["10","k","","Ω"],["7,1","M","","Hz"],["2200","","k","Ω"]]'></div>

:::weetje Encore plus petit et encore plus grand
À l'examen, vous n'avez besoin que de milli, kilo et méga. En pratique, vous rencontrerez aussi **µ** (micro, encore 1000 fois plus petit que milli) et **G** (giga, 1000 fois plus grand que méga). Le tableau fonctionne de la même façon avec eux.
:::

<div class="omreken-oef" data-oef='[["470","µ","m","A"],["1,2","G","M","Hz"]]'></div>

<details class="zelf" markdown="1"><summary>Essayez vous-même : convertissez 150 mA en ampères.</summary>

150 mA vers une unité plus grande, donc divisé par 1000 : **0,15 A**.

</details>
<details class="zelf" markdown="1"><summary>Essayez vous-même : convertissez 1,5 kV en volts.</summary>

Vers une unité plus petite, donc fois 1000 : **1 500 V**.

</details>

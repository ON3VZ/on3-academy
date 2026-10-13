---
id: h05-b6
type: brokje
kort: PAR (ERP)
titel: PAR : puissance apparente rayonnée
uba_ref: hfst. 5.5, p. 22
checkvragen: [C-h05-6a, C-h05-6b, C-h05-6c]
examenvragen: [O170, O171]
---
:::kern
La **PAR** (puissance apparente rayonnée, en anglais **ERP**, Effective Radiated Power) indique quelle puissance il vous faudrait avec un **simple dipôle** pour avoir la même force dans la direction privilégiée. Vous la calculez par une **multiplication**.
:::

:::formule
PAR = P × G
--
PAR en watts (W) · P = puissance fournie à l'antenne, en watts · G = gain de l'antenne (un nombre sans unité, par rapport à un dipôle)
:::

{{svg:h05-erp|10 W dans une yagi de gain 5, c'est aussi fort dans la direction privilégiée que 50 W dans un dipôle.}}

### Exemple résolu
« Une antenne de gain 5 reçoit 10 W. Quelle est la PAR ? »

1. Données : P = 10 W, G = 5.
2. Formule : PAR = P × G.
3. PAR = 10 × 5 = **50 W**.
4. Signification : celui qui écoute dans la direction privilégiée vous entend aussi fort que quelqu'un qui émet 50 W dans un simple dipôle.

:::vergelijk Comparaison
La lampe de poche de la page précédente. L'ampoule elle-même consomme autant, mais grâce au petit miroir elle paraît beaucoup plus lumineuse dans une direction. La PAR, c'est « à quel point cela paraît lumineux dans cette direction ».
:::

:::valkuil
- C'est une **multiplication**, pas une addition, une soustraction ou une division. Avec 10 W et un gain de 4, la réponse est 40 W, pas 14 W, 6 W ou 2,5 W.
- La PAR est une **valeur de calcul**. Il ne part pas réellement 50 W dans l'air : votre émetteur fournit toujours 10 W.
:::

<details class="zelf" markdown="1"><summary>Essayez vous-même : 25 W dans une antenne de gain 3. PAR ?</summary>

PAR = 25 × 3 = **75 W**.

</details>
<details class="zelf" markdown="1"><summary>Essayez vous-même : vous voulez 100 W de PAR avec une antenne de gain 4. Quelle puissance devez-vous fournir ?</summary>

P = PAR ÷ G = 100 ÷ 4 = **25 W**.

</details>

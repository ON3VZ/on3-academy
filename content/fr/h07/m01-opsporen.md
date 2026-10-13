---
id: h07-m01
type: moeilijk
kort: Points difficiles
titel: Localiser une perturbation, pas à pas
uba_ref: hfst. 7
checkvragen: []
examenvragen: []
---
La CEM semble difficile parce qu'on ne voit pas la perturbation. Avec un ordre fixe, vous trouverez presque toujours la solution. Vous cherchez à chaque fois une seule chose : **par quel chemin** le signal entre-t-il ?

### Plan par étapes : votre émetteur perturbe un appareil
1. **Notez quand cela se produit.** Sur quelle bande, avec quelle modulation (SSB, FM, CW) et avec quelle puissance ? La perturbation n'apparaît-elle que quand vous émettez ?
2. **Émettez sur une charge fictive (dummy load).** Si la perturbation disparaît, elle vient par l'antenne (le rayonnement). Si elle reste, quelque chose fuit par vos propres câbles ou votre alimentation.
3. **Réduisez la puissance.** La perturbation diminue-t-elle ? Vous avez alors une première solution de secours et vous savez que c'est une question de force de votre signal.
4. **Chez l'appareil perturbé, débranchez les câbles un par un** (câble d'antenne, câble de haut-parleur, câble de téléphone). Si la perturbation disparaît avec un câble précis, vous avez trouvé le chemin.
5. **Placez sur ce câble un tore de ferrite ou un filtre adapté, le plus près possible de l'appareil.**
6. **Vérifiez votre propre station** : antenne plus haute et plus loin de la maison, antenne symétrique (dipôle avec balun), bonne terre HF.
7. **Vous ne vous en sortez pas ?** Demandez de l'aide à la section UBA ou à la commission CEM de l'UBA, puis à l'IBPT.

### Exemple détaillé
« Le voisin entend votre voix dans sa chaîne stéréo quand vous émettez sur 40 m en SSB avec 100 W. »
1. Quand ? 40 m, SSB, 100 W. La SSB est la modulation qui donne le plus de risque de perturbation.
2. Sur une charge fictive, la perturbation disparaît : elle vient du rayonnement de l'antenne.
3. Avec 25 W, c'est déjà beaucoup moins : c'est une question de force du signal.
4. Avec le voisin : sans les câbles de haut-parleurs, c'est silencieux. Les **câbles de haut-parleurs** se comportent comme une antenne.
5. Des tores de ferrite sur les câbles de haut-parleurs, tout près de l'amplificateur du voisin. Problème résolu.
6. En plus : remplacer votre fil alimenté en bout par un dipôle, plus haut et plus loin de la maison.

:::valkuil
Travaillez toujours **avec** le voisin et ne touchez à ses appareils qu'avec son accord. N'ouvrez jamais un appareil qui fonctionne sur 230 V et ne construisez pas vous-même de filtres pour le réseau électrique.
:::

### Plan par étapes : votre récepteur est perturbé
1. **Écoutez avec votre récepteur sur batterie** et coupez un par un les circuits de la maison au tableau électrique (demandez de l'aide si vous ne savez pas comment le faire en sécurité). Si la perturbation disparaît, la source se trouve sur ce circuit.
2. **Sur ce circuit, débranchez les appareils un par un.** Les sources fréquentes sont les chargeurs, les lampes LED, les panneaux solaires (onduleur) et les ordinateurs.
3. **Traitez** la source avec un tore de ferrite sur son câble, éloignez votre antenne ou remplacez l'appareil.

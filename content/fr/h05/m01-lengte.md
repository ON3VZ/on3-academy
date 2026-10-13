---
id: h05-m01
type: moeilijk
kort: Points difficiles
titel: Calculer la longueur d'une antenne, pas à pas
uba_ref: hfst. 3.4 en 5.2
checkvragen: []
examenvragen: []
---
Presque toutes les antennes sont une **fraction de longueur d'onde** : une demie (dipôle), un quart (quart d'onde, ground plane) ou cinq huitièmes (5/8 λ). Si vous savez calculer la longueur d'onde, vous pouvez donc calculer la longueur de n'importe quelle antenne.

:::formule
λ = 300 ÷ f
dipôle = λ ÷ 2
quart d'onde = λ ÷ 4
5/8 λ = λ × 5 ÷ 8
--
λ = longueur d'onde en mètres (m) · f = fréquence en mégahertz (MHz)
:::

### La méthode

1. **Mettez la fréquence en MHz.** Si elle est en kHz, divisez par 1 000 (7 100 kHz = 7,1 MHz).
2. **Calculez la longueur d'onde** : λ = 300 ÷ f.
3. **Prenez la bonne fraction** : ÷ 2 pour un dipôle, ÷ 4 pour un quart d'onde, × 5 ÷ 8 pour une 5/8 λ.
4. **Rendez la réponse pratique** : 0,52 m = 52 cm.
5. **Vérifiez avec bon sens** : les antennes HF mesurent de quelques mètres à des dizaines de mètres, les antennes VHF environ un mètre ou moins.

### Exemple résolu 1 : dipôle pour 14 MHz

1. f = 14 MHz.
2. λ = 300 ÷ 14 ≈ **21,4 m**.
3. Dipôle : 21,4 ÷ 2 ≈ **10,7 m**.
4. Deux fils d'environ 5,35 m.
5. Des dizaines de mètres en HF : c'est correct.

### Exemple résolu 2 : quart d'onde pour 145 MHz

1. f = 145 MHz.
2. λ = 300 ÷ 145 ≈ **2,07 m**.
3. Quart d'onde : 2,07 ÷ 4 ≈ **0,52 m**.
4. 0,52 m = **52 cm**. C'est à peu près la longueur d'une antenne à base magnétique sur le toit d'une voiture.
5. VHF, moins d'un mètre : c'est correct.

### Exemple résolu 3 : 5/8 λ pour 145 MHz

1. f = 145 MHz.
2. λ ≈ 2,07 m.
3. 5/8 λ : 2,07 × 5 = 10,35. Divisé par 8 ≈ **1,29 m**.
4. Environ 1,3 m : plus long que le quart d'onde de l'exemple 2. C'est logique, car 5/8 est plus que 2/8.

| Fréquence | λ | Dipôle (λ/2) | Quart d'onde (λ/4) |
|---|---|---|---|
| 3,6 MHz (80 m) | 83 m | 42 m | 21 m |
| 7 MHz (40 m) | 43 m | 21 m | 11 m |
| 14 MHz (20 m) | 21 m | 10,7 m | 5,4 m |
| 28 MHz (10 m) | 10,7 m | 5,4 m | 2,7 m |
| 145 MHz (2 m) | 2,07 m | 1,03 m | 52 cm |
| 435 MHz (70 cm) | 69 cm | 34 cm | 17 cm |

:::valkuil
- Ne confondez pas **λ/2** (dipôle) et **λ/4** (quart d'onde) : le quart d'onde est deux fois plus court que le dipôle.
- N'oubliez pas de convertir d'abord en **MHz**. 300 ÷ 7 100 (kHz) donne un résultat absurde.
:::

<details class="zelf" markdown="1"><summary>Essayez vous-même : quelle est la longueur d'un dipôle pour 30 MHz ?</summary>

λ = 300 ÷ 30 = 10 m. Dipôle = 10 ÷ 2 = **5 m**.

</details>
<details class="zelf" markdown="1"><summary>Essayez vous-même : quelle est la longueur d'un quart d'onde pour 7 500 kHz ?</summary>

7 500 kHz = 7,5 MHz. λ = 300 ÷ 7,5 = 40 m. Quart d'onde = 40 ÷ 4 = **10 m**.

</details>
<details class="zelf" markdown="1"><summary>Essayez vous-même : un dipôle mesure 2 m. Pour quelle fréquence ?</summary>

Un dipôle mesure λ/2, donc λ = 2 × 2 = 4 m. f = 300 ÷ 4 = **75 MHz**.

</details>

# ON3 Academy

Studieplatform voor het Belgische ON3-examen (klasse C). Statische website, installeerbaar als app (PWA) en offline bruikbaar. Geen account: voortgang blijft in de browser.

> Enkel een hulpmiddel. De officiële bronnen en de actuele wetgeving primeren. Niet verbonden met het BIPT.

## Lokaal bekijken
- Snel: dubbelklik `index.html` (werkt zonder server, maar zonder offline-modus).
- Met offline-modus: in deze map `python3 -m http.server 8000` en surf naar http://localhost:8000

## Inhoud aanpassen
1. Tekst per brokje: `content/nl/<hoofdstuk>/*.md` (front matter bovenaan, daarna Markdown of HTML).
   - Eigen blokken: `:::kern Titel` ... `:::`, ook `vergelijk`, `valkuil`, `weetje`, `formule`.
   - Tekening invoegen: `{{svg:naam|onderschrift}}` (bestand `assets/svg/naam.svg`).
2. Hoofdstuk-instellingen (leerdoelen, volgorde, flashcards, samenvatting): `content/nl/<hoofdstuk>/hoofdstuk.json`.
3. Vragen: `data/vragen-origineel.json` (originelen: vraag, opties en juist antwoord NIET wijzigen), `data/vragen-extra.json` (altijd `bron: extra`), `data/vragen-check.json`.
   - `status`: `ok`, `dubbel`, `verouderd` of `controle`. Enkel `ok` wordt getoond.
4. Daarna altijd: `python3 tools/build.py` (maakt `js/content.js` en `sw.js` opnieuw). Vereist `pip install markdown`.

## Publiceren (GitHub Pages)
Zet de inhoud van deze map in de root van de repo, Settings > Pages > Deploy from branch > main / root.

## Structuur
```
index.html  css/  js/app.js  js/content.js (gegenereerd)  sw.js (gegenereerd)
content/nl|fr/  data/  assets/svg|icons|foto/  tools/build.py
```

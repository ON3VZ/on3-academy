"""Tekeningen hoofdstuk 15 (Wetgeving). Schrijft naar assets/svg/."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg_h03 import svg, t, line, ARROW, OUT
from svg_h05 import blok, pijl


def piramide():
    w, h = 760, 380
    b = ARROW
    lagen = [("WET", "wet van 13 juni 2005", "gemaakt door het parlement", 120),
             ("KB", "KB van 18 december 2009", "de Koning (de regering)", 220),
             ("MB", "ministerieel besluit", "een minister", 320),
             ("BIPT", "besluit van de Raad van het BIPT", "bv. frequentietabel, examenregeling", 420)]
    cx = 250
    for i, (k, n, s, wd) in enumerate(lagen):
        y = 30 + i * 82
        b += f'<path d="M{cx-wd/2},{y+70} L{cx-wd/2+50},{y} L{cx+wd/2-50},{y} L{cx+wd/2},{y+70} Z" class="{"sb" if i==0 else "box"}"/>' if False else ""
        b += f'<rect x="{cx-wd/2}" y="{y}" width="{wd}" height="66" rx="8" class="{"sb" if i < 2 else "box"}"/>'
        b += t(cx, y + 42, k, "lbl big mono", "middle")
        b += t(cx + 225, y + 28, n, "lbl b") + t(cx + 225, y + 50, s, "lbl s")
    b += f'<line x1="40" y1="350" x2="40" y2="40" class="dim" marker-end="url(#pijl)"/>'
    b += t(30, 200, "hoger", "lbl s b", "middle").replace('text-anchor="middle"', 'text-anchor="middle" transform="rotate(-90 30 200)"')
    b += t(380, 372, "Een lagere regel mag nooit in strijd zijn met een hogere.", "lbl b accent2", "middle")
    return svg(w, h, "Rangorde van de regels", "Van boven naar onder: wet, koninklijk besluit, ministerieel besluit, besluit van de Raad van het BIPT. Een lagere regel mag niet in strijd zijn met een hogere.", b)


def stations():
    w, h = 760, 300
    b = ARROW
    rij = [("vast", "blijvend op één", "bepaalde plaats", "nee", "op die plaats"),
           ("transportabel", "kan verplaatst", "worden", "ja", "enkel stilstaand"),
           ("mobiel", "ingebouwd in", "een voertuig", "ja", "rijdend of stilstaand"),
           ("draagbaar", "los van een", "voertuig", "ja", "lopend of stilstaand")]
    b += t(20, 30, "soort station", "lbl s b") + t(220, 30, "wat is het?", "lbl s b") + t(420, 30, "verplaatsbaar?", "lbl s b") + t(560, 30, "gebruiken", "lbl s b")
    for i, (n, a1, a2, v, g) in enumerate(rij):
        y = 46 + i * 62
        b += f'<rect x="10" y="{y}" width="740" height="54" rx="8" class="{"box" if i%2==0 else "cell"}"/>'
        b += t(24, y + 33, n, "lbl b mono accent2") + t(220, y + 24, a1, "lbl") + t(220, y + 44, a2, "lbl")
        b += t(450, y + 33, v, "lbl b", "middle") + t(560, y + 33, g, "lbl b")
    return svg(w, h, "Vier soorten radiostations", "Vast: blijvend op één plaats. Transportabel: verplaatsbaar maar enkel gebruikt als het stilstaat. Mobiel: ingebouwd in een voertuig, rijdend of stilstaand. Draagbaar: los van een voertuig, in beweging of stilstaand.", b)


def frequenties():
    w, h = 760, 290
    b = ARROW
    k = [("exclusief", "één houder", "in een bepaalde zone", "hoge dienstkwaliteit", "beschermd", "green"),
         ("gemeenschappelijk", "verscheidene houders", "in een zelfde zone, rekening met bezetting", "normale dienstkwaliteit", "geen bescherming", "accent2"),
         ("collectief", "verscheidene houders", "overal, zonder rekening met bezetting", "geen recht op kwaliteit", "geen enkele bescherming", "red")]
    for i, (n, a, z, q, bs, c) in enumerate(k):
        x = 15 + i * 250
        b += f'<rect x="{x}" y="15" width="230" height="260" rx="12" class="box"/>'
        b += t(x + 115, 50, n, "lbl b " + c, "middle")
        b += t(x + 115, 90, a, "lbl b", "middle") + t(x + 115, 112, z.split(",")[0], "lbl s", "middle")
        if "," in z: b += t(x + 115, 130, z.split(",")[1].strip(), "lbl s", "middle")
        b += t(x + 115, 175, q, "lbl", "middle")
        b += t(x + 115, 225, bs, "lbl b " + c, "middle")
    b += t(380, 252, "tegen de andere netten", "lbl s", "middle")
    b += t(630, 252, "tegen eender welke storing", "lbl s", "middle")
    return svg(w, h, "Drie soorten frequenties", "Exclusief: één houder, hoge kwaliteit, beschermd. Gemeenschappelijk: verscheidene houders, normale kwaliteit, geen bescherming tegen de andere netten op dezelfde frequentie. Collectief: verscheidene houders overal, geen recht op kwaliteit, geen enkele bescherming.", b)


def traject():
    w, h = 760, 470
    b = ARROW
    st = [("1", "Opleiding", "bij een erkende vereniging, ook zonder lid te zijn", "art. 17/4"),
          ("2", "Praktische proef", "bij de vereniging: attest, 1 jaar geldig", "examenreglement"),
          ("3", "Theorie-examen bij het BIPT", "minstens 12 jaar, dossierrecht bij inschrijving", "art. 17/2, 35"),
          ("4", "Getuigschrift", "van aspirant privaat radiotelefonist", "BIPT-document"),
          ("5", "Bedieningscertificaat + roepnaam", "5 jaar geldig, verlengbaar", "art. 6/1, 17/1"),
          ("6", "Stationsvergunning (5e categorie)", "eerst certificaat, jaarlijks recht", "art. 17/5, 37")]
    for i, (n, a, s, r) in enumerate(st):
        y = 12 + i * 76
        b += f'<rect x="90" y="{y}" width="660" height="62" rx="10" class="box"/>'
        b += f'<circle cx="50" cy="{y+31}" r="20" class="sb"/>' + t(50, y + 37, n, "lbl b", "middle")
        b += t(108, y + 27, a, "lbl b") + t(108, y + 49, s, "lbl s") + t(738, y + 27, r, "lbl s mono accent2", "end")
    return svg(w, h, "Van kandidaat tot vergunninghouder", "Zes stappen: opleiding, praktische proef, theorie-examen, getuigschrift, bedieningscertificaat met roepnaam, stationsvergunning.", b)


def sancties():
    w, h = 760, 430
    b = ARROW
    rij = [("§ 1", "50 tot 50 000 EUR", "", "storing, apparatuur, noodseinen, afluisteren, verkoop (15, 32, 33, 35, 41, 42)"),
           ("§ 2", "200 tot 2 000 EUR", "8 dagen tot 1 jaar", "zender houden of gebruiken zonder vergunning (13/1)"),
           ("§ 3", "500 tot 50 000 EUR", "1 tot 4 jaar", "bedrieglijk communiceren om voordeel te halen"),
           ("§ 3bis", "50 tot 300 EUR", "15 dagen tot 2 jaar", "overlast of schade aan je correspondent"),
           ("§ 4", "verbeurdverklaring", "altijd", "toestel dat niet voldoet aan art. 32, 33, 35 of 37")]
    b += t(20, 22, "Wet van 13 juni 2005, art. 145", "lbl b") + t(110, 50, "geldboete", "lbl s b") + t(290, 50, "gevangenis", "lbl s b") + t(450, 50, "waarvoor?", "lbl s b")
    for i, (p, g, c, w_) in enumerate(rij):
        y = 60 + i * 70
        b += f'<rect x="10" y="{y}" width="740" height="60" rx="8" class="{"box" if i%2==0 else "cell"}"/>'
        b += t(24, y + 36, p, "lbl b mono accent2") + t(110, y + 36, g, "lbl b") + t(290, y + 36, c, "lbl b red")
        woorden = w_.split(" "); r1, r2 = "", ""
        for wd in woorden:
            if len(r1) + len(wd) < 36 and not r2: r1 += wd + " "
            else: r2 += wd + " "
        b += t(450, y + 27, r1.strip(), "lbl s") + t(450, y + 46, r2.strip(), "lbl s")
    b += t(380, 420, "Gevangenisstraf en boete samen, of één van beide (behalve § 1 en § 4).", "lbl s", "middle")
    return svg(w, h, "Straffen in de wet", "Tabel met de straffen van artikel 145: paragraaf 1 boete 50 tot 50 000 euro; paragraaf 2 boete 200 tot 2 000 euro en 8 dagen tot 1 jaar; paragraaf 3 boete 500 tot 50 000 euro en 1 tot 4 jaar; paragraaf 3bis 50 tot 300 euro en 15 dagen tot 2 jaar; paragraaf 4 verbeurdverklaring.", b)


def dossierrecht():
    w, h = 760, 250
    b = ARROW
    b += t(20, 28, "Aanvraag ingediend ... werkdagen voor de gewenste datum", "lbl b")
    x0, x1 = 40, 720
    b += line(x0, 120, x1, 120, "wire thick")
    zones = [(40, 360, "20 of meer", "× 1", "normaal dossierrecht", "box"),
             (360, 600, "minder dan 20", "× 2", "verdubbeld", "cell"),
             (600, 720, "minder dan 5", "× 5", "vervijfvoudigd", "sb")]
    for a, z, n, f, s, c in zones:
        b += f'<rect x="{a}" y="70" width="{z-a}" height="50" class="{c}"/>'
        b += t((a + z) / 2, 102, f, "lbl big mono", "middle")
        b += t((a + z) / 2, 148, n, "lbl b", "middle") + t((a + z) / 2, 168, s, "lbl s", "middle")
    b += t(720, 60, "gewenste datum", "lbl s b", "end")
    b += t(380, 210, "Tijdelijke vergunning: grenzen van 5 en 2 werkdagen in plaats van 20 en 5.", "lbl accent2 b", "middle")
    b += t(380, 236, "Wijziging van een vergunning: de helft van het dossierrecht. (KB art. 35)", "lbl s", "middle")
    return svg(w, h, "Te laat aanvragen kost meer", "Tijdlijn: 20 werkdagen of meer voor de datum gewoon dossierrecht, minder dan 20 werkdagen het dubbele, minder dan 5 werkdagen het vijfvoudige. Bij tijdelijke vergunningen 5 en 2 werkdagen.", b)


def main():
    files = {"h15-piramide": piramide(), "h15-stations": stations(), "h15-frequenties": frequenties(),
             "h15-traject": traject(), "h15-sancties": sancties(), "h15-dossierrecht": dossierrecht()}
    for k, v in files.items():
        open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(v)
    print(len(files), "tekeningen")


if __name__ == "__main__":
    main()

"""Tekeningen hoofdstuk 1 en 2. Schrijft naar assets/svg/."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg_h03 import svg, t, line, path, ARROW, OUT
from svg_h05 import blok, pijl


def facetten():
    w, h = 760, 300
    b = ARROW
    items = [("verbindingen", "met amateurs over de", "hele wereld"), ("zelf bouwen", "antennes en toestellen", "maken en verbeteren"),
             ("experimenteren", "nieuwe technieken", "en digitale modes"), ("propagatie", "begrijpen hoe ver", "radiogolven komen")]
    for i, (a, s1, s2) in enumerate(items):
        x = 20 + (i % 2) * 370
        y = 30 + (i // 2) * 130
        b += f'<rect x="{x}" y="{y}" width="350" height="110" rx="12" class="box"/>'
        b += t(x + 175, y + 42, a, "lbl b", "middle") + t(x + 175, y + 68, s1, "lbl s", "middle") + t(x + 175, y + 86, s2, "lbl s", "middle")
    b += t(380, 292, "niet toegelaten: commercie (geld verdienen). Taboe: politiek en geloof.", "lbl b red", "middle")
    return svg(w, h, "Wat doet een radioamateur", "Vier vakken: verbindingen over de hele wereld, zelf bouwen, experimenteren, propagatie. Daaronder: geen commercie, geen politiek of geloof.", b)


def traject():
    w, h = 760, 360
    b = ARROW
    st = [("1", "Leren", "zelfstudie of cursus bij een erkende vereniging"),
          ("2", "Examen afleggen", "praktische proef (erkende vereniging), daarna theorie bij het BIPT (30 vragen)"),
          ("3", "Getuigschrift", "je bent geslaagd"),
          ("4", "Bedieningscertificaat + roepnaam", "aanvragen bij het BIPT: je mag zenden (ON3...)"),
          ("5", "Stationsvergunning", "om zelf een station te hebben en te gebruiken")]
    for i, (n, a, s) in enumerate(st):
        y = 15 + i * 68
        b += f'<rect x="90" y="{y}" width="620" height="54" rx="10" class="box"/>'
        b += f'<circle cx="55" cy="{y+27}" r="20" class="sb"/>' + t(55, y + 33, n, "lbl b", "middle")
        b += t(110, y + 24, a, "lbl b") + t(110, y + 44, s, "lbl s")
    return svg(w, h, "Van kandidaat tot radioamateur", "Vijf stappen: leren (zelfstudie of cursus), praktische proef en theorie-examen, getuigschrift, bedieningscertificaat met roepnaam, stationsvergunning.", b)


def klassen():
    w, h = 760, 300
    b = ARROW
    data = [("C", "basiscertificaat", "8 banden", "25 W HF, 50 W VHF/UHF", "enkel gekochte toestellen", 140),
            ("B", "CEPT Novice", "12 banden", "max 100 W", "gekochte toestellen, niet wijzigen", 180),
            ("A", "HAREC", "26 of meer banden", "max 1500 W", "zelf bouwen en wijzigen mag", 220)]
    for i, (k, n, bnd, p, z, hh) in enumerate(data):
        x = 30 + i * 240
        y = 270 - hh
        b += f'<rect x="{x}" y="{y}" width="220" height="{hh}" rx="10" class="box"/>'
        b += t(x + 110, y + 34, f"klasse {k}", "lbl big", "middle")
        b += t(x + 110, y + 56, n, "lbl s", "middle")
        b += t(x + 110, y + 82, bnd, "lbl b", "middle")
        b += t(x + 110, y + 102, p, "lbl s", "middle")
        b += t(x + 110, y + 124, z, "lbl s", "middle")
    b += pijl(40, 20, 720, 20)
    b += t(380, 14, "hoe hoger de klasse, hoe meer banden en vermogen", "lbl s", "middle")
    return svg(w, h, "Drie klassen", "Drie trappen: klasse C (8 banden, 25 tot 50 W), klasse B (12 banden, 100 W), klasse A (26 of meer banden, 1500 W, zelf bouwen).", b)


def roepnaam():
    w, h = 760, 230
    b = ARROW
    delen = [("ON", "land", "België: ON tot OT", 160), ("3", "cijfer", "één cijfer", 90), ("XYZ", "letters", "één tot drie letters", 170), ("/P", "aanhangsel", "waar je zendt (soms)", 140)]
    x = 60
    for i, (s, n, u, wd) in enumerate(delen):
        cls = "sb" if i < 3 else "cell"
        b += f'<rect x="{x}" y="40" width="{wd}" height="80" rx="10" class="{cls}"/>'
        b += t(x + wd / 2, 96, s, "lbl big mono", "middle")
        b += t(x + wd / 2, 150, n, "lbl b", "middle") + t(x + wd / 2, 172, u, "lbl s", "middle")
        x += wd + 20
    b += t(380, 214, "ON3XYZ/P = Belgische radioamateur, draagbaar station", "lbl b accent2", "middle")
    return svg(w, h, "Opbouw van een roepnaam", "Een roepnaam bestaat uit landprefix ON, een cijfer 3, letters XYZ en eventueel een aanhangsel /P.", b)


BANDEN = [("80 m", "3,500 tot 3,800 MHz", "P", "25 W"), ("40 m", "7,000 tot 7,100 MHz", "PEX", "25 W"), ("40 m", "7,100 tot 7,200 MHz", "S", "25 W"),
          ("30 m", "10,100 tot 10,150 MHz", "S", "25 W"), ("20 m", "14,000 tot 14,350 MHz", "PEX", "25 W"), ("15 m", "21,000 tot 21,450 MHz", "PEX", "25 W"),
          ("10 m", "28,000 tot 29,700 MHz", "PEX", "25 W"), ("2 m", "144 tot 146 MHz", "PEX", "50 W"), ("70 cm", "430 tot 440 MHz", "P", "50 W")]
KL = {"PEX": "var(--primary)", "P": "var(--cyan)", "S": "var(--amber)"}


def banden():
    w, h = 760, 60 + 40 * len(BANDEN)
    b = t(20, 28, "Klasse C: waar mag je zenden?", "lbl b")
    b += t(560, 28, "status", "lbl s b", "middle") + t(690, 28, "max", "lbl s b", "middle")
    for i, (n, f, st, p) in enumerate(BANDEN):
        y = 50 + i * 40
        b += f'<rect x="20" y="{y}" width="720" height="32" rx="6" class="cell"/>'
        b += t(36, y + 22, n, "lbl b mono") + t(130, y + 22, f, "lbl")
        b += f'<rect x="520" y="{y+5}" width="80" height="22" rx="11" style="fill:{KL[st]};opacity:.85"/>' + f'<text x="560" y="{y+21}" text-anchor="middle" style="fill:#fff;font-weight:700;font-size:13px;font-family:var(--f-mono)">{st}</text>'
        b += t(690, y + 22, p, "lbl b", "middle")
    return svg(w, h, "Frequentietabel klasse C", "Negen rijen: acht banden van 80 m tot 70 cm, met status en maximum vermogen. HF 25 W, VHF en UHF 50 W.", b)


def main():
    files = {"h01-facetten": facetten(), "h02-traject": traject(), "h02-klassen": klassen(), "h02-roepnaam": roepnaam(), "h02-banden": banden()}
    for k, v in files.items():
        open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(v)
    print(len(files), "tekeningen")


if __name__ == "__main__":
    main()

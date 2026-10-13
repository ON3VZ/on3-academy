"""Tekeningen hoofdstuk 8 (Operating procedures). Schrijft naar assets/svg/."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg_h03 import svg, t, line, path, ARROW, OUT
from svg_h05 import blok, pijl, golfjes

ANT = "ant"


def antenne(x, y):
    return line(x, y, x, y - 30, ANT) + line(x, y - 18, x - 12, y - 34, ANT) + line(x, y - 18, x + 12, y - 34, ANT)


def auto(x, y):
    return (f'<path d="M{x},{y} l0,-18 l20,0 l14,-16 l40,0 l14,16 l20,0 l0,18 z" class="cell" style="stroke:var(--text);stroke-width:2"/>'
            f'<circle cx="{x+22}" cy="{y}" r="8" class="symfill"/><circle cx="{x+86}" cy="{y}" r="8" class="symfill"/>')


def qso():
    w, h = 760, 470
    b = ARROW
    stappen = [("1", "Luisteren", "is de frequentie vrij? Luister eerst een tijdje."),
               ("2", "Vragen", "\"Is deze frequentie in gebruik? Dit is ON3XYZ.\""),
               ("3", "Oproepen (CQ)", "\"CQ CQ CQ, dit is ON3XYZ ... die roept en luistert.\""),
               ("4", "Iemand antwoordt", "noteer zijn roepnaam, geef een rapport"),
               ("5", "Uitwijken (QSY)", "op VHF/UHF: weg van de oproepfrequentie"),
               ("6", "Afsluiten", "groeten, roepnamen herhalen, in het logboek")]
    for i, (n, a, s) in enumerate(stappen):
        y = 20 + i * 74
        b += f'<rect x="90" y="{y}" width="620" height="56" rx="10" class="box"/>'
        b += f'<circle cx="55" cy="{y+28}" r="20" class="sb"/>' + t(55, y + 34, n, "lbl b", "middle")
        b += t(110, y + 24, a, "lbl b") + t(110, y + 44, s, "lbl s")
    return svg(w, h, "Verloop van een verbinding", "Zes stappen: luisteren, vragen of de frequentie vrij is, CQ roepen, antwoord, uitwijken, afsluiten.", b)


def repeater():
    w, h = 760, 320
    b = ARROW
    b += line(0, 280, 760, 280, "wire")
    b += '<path d="M240,280 Q380,40 520,280 Z" class="cell"/>'
    b += line(380, 165, 380, 95, "wire thick") + antenne(380, 95)
    b += f'<rect x="352" y="160" width="56" height="34" rx="6" class="box"/>' + t(380, 182, "rep.", "lbl s b", "middle")
    b += t(380, 300, "heuvel of hoog gebouw", "lbl s", "middle")
    b += auto(30, 270) + antenne(80, 236)
    b += auto(620, 270) + antenne(670, 236)
    b += f'<path d="M95,190 Q220,90 360,60" class="w-amber" style="stroke-width:3" marker-end="url(#pijl)"/>'
    b += t(130, 210, "zendt op", "lbl s") + t(130, 228, "145,000 MHz", "lbl b mono accent2")
    b += f'<path d="M400,60 Q540,90 660,190" class="w-green" style="stroke-width:3" marker-end="url(#pijl)"/>'
    b += t(520, 210, "repeater zendt op", "lbl s") + t(520, 228, "145,600 MHz", "lbl b mono green")
    b += t(380, 26, "verschil = shift = 600 kHz", "lbl b", "middle")
    b += t(80, 300, "station A", "lbl s", "middle") + t(670, 300, "station B", "lbl s", "middle")
    b += t(130, 246, "+ 1750 Hz of CTCSS", "lbl s") + t(130, 262, "om de repeater te openen", "lbl s")
    return svg(w, h, "Repeater", "Station A zendt op 145,000 MHz naar een repeater op een heuvel. De repeater zendt hetzelfde uit op 145,600 MHz, zodat station B het ontvangt.", b)


SEG14 = [(14000, 14060, "CW (contest)", "cw"), (14060, 14070, "CW", "cw"), (14070, 14099, "digitaal, CW", "dig"),
         (14099, 14101, "IBP", "bak"), (14101, 14112, "dig., fonie, CW", "dig"), (14112, 14125, "fonie, CW", "fon"),
         (14125, 14300, "fonie (contest), CW", "fon"), (14300, 14350, "fonie, CW", "fon")]
SEG144 = [(144000, 144035, "EME", "bak"), (144035, 144150, "CW", "cw"), (144150, 144400, "SSB", "fon"),
          (144400, 144500, "bakens", "bak"), (144500, 144800, "alle modes", "all"), (144800, 144990, "digitaal", "dig"),
          (144990, 145194, "FM rep. ingang", "fm"), (145194, 145594, "FM", "fm"), (145594, 145800, "FM rep. uitgang", "fm"),
          (145800, 146000, "satelliet", "bak")]
KLEUR = {"cw": "var(--cyan)", "dig": "var(--primary)", "bak": "var(--text3)", "fon": "var(--amber)", "fm": "var(--red)", "all": "#8b6cf0"}


def bandplan(seg, titel, f0, f1, ticks, w=760, h=190):
    b = t(20, 28, titel, "lbl b")
    x0, x1 = 30, 730
    sx = lambda f: x0 + (f - f0) / (f1 - f0) * (x1 - x0)
    for i, (a, z, n, k) in enumerate(seg):
        xa, xz = sx(a), sx(z)
        b += f'<rect x="{xa:.1f}" y="60" width="{xz-xa:.1f}" height="40" style="fill:{KLEUR[k]};opacity:.75;stroke:var(--surface);stroke-width:1"/>'
        xm = (xa + xz) / 2
        yy = 122 if i % 2 == 0 else 146
        b += line(xm, 100, xm, yy - 14, "guide2")
        b += f'<circle cx="{xm:.1f}" cy="{yy-5}" r="10" class="sb"/>' + t(xm, yy, str(i + 1), "lbl s b", "middle")
    for f in ticks:
        x = sx(f)
        b += line(x, 52, x, 60, "axis2") + t(x, 46, f"{f}", "lbl s mono", "middle")
    b += t(380, h - 8, "frequentie in kHz, van laag naar hoog. De nummers staan in de tabel eronder.", "lbl s", "middle")
    return svg(w, h, titel, "Balk met de genummerde segmenten van het bandplan, van laag naar hoog.", b)


def smeter():
    w, h = 760, 260
    b = ARROW
    cx, cy, r = 380, 230, 190
    b += f'<path d="M{cx-r*math.cos(math.radians(30)):.0f},{cy-r*math.sin(math.radians(30)):.0f} A{r},{r} 0 0 1 {cx+r*math.cos(math.radians(30)):.0f},{cy-r*math.sin(math.radians(30)):.0f}" class="sym"/>'
    labels = ["1", "3", "5", "7", "9", "+20", "+40", "+60"]
    vals = [1, 3, 5, 7, 9, 11, 13, 15]
    for lab, v in zip(labels, vals):
        a = math.radians(150 - (v - 1) / 14 * 120)
        x1, y1 = cx + r * math.cos(a), cy - r * math.sin(a)
        x2, y2 = cx + (r - 14) * math.cos(a), cy - (r - 14) * math.sin(a)
        b += line(x1, y1, x2, y2, "wire")
        cls = "lbl b mono red" if v > 9 else "lbl b mono"
        b += t(cx + (r + 18) * math.cos(a), cy - (r + 18) * math.sin(a) + 5, lab, cls, "middle")
    a = math.radians(150 - (9 - 1) / 14 * 120)
    b += line(cx, cy, cx + (r - 20) * math.cos(a), cy - (r - 20) * math.sin(a), "w-red")
    b += f'<circle cx="{cx}" cy="{cy}" r="7" class="symfill"/>'
    b += t(cx - 110, cy - 20, "S-meter", "lbl b", "middle")
    b += t(40, 60, "elk S-punt hoger =", "lbl s") + t(40, 78, "2 × zoveel spanning", "lbl b")
    b += t(720, 60, "boven S9: in dB", "lbl s", "end") + t(720, 78, "(+20, +40, +60)", "lbl s", "end")
    return svg(w, h, "S-meter", "Een S-meter met schaal S1 tot S9 en daarboven +20, +40, +60 dB. De naald staat op S9.", b)


def ptt():
    w, h = 760, 230
    b = ARROW
    b += f'<rect x="40" y="60" width="80" height="120" rx="30" class="cell" style="stroke:var(--text);stroke-width:2"/>'
    b += f'<rect x="28" y="100" width="14" height="40" rx="4" class="box"/>' + t(20, 94, "PTT", "lbl s b", "middle")
    b += t(80, 200, "microfoon", "lbl s", "middle")
    for i, (n, d) in enumerate([("audio", "het spraaksignaal (heel klein)"), ("massa", "gemeenschappelijke draad"), ("PTT", "drukknop: zender aan/uit")]):
        y = 80 + i * 40
        b += line(120, y, 520, y, "wire") + t(130, y - 6, n, "lbl s b") + t(220, y - 6, d, "lbl s")
    b += blok(520, 60, 180, 120, "zender|microfoon-|aansluiting")
    return svg(w, h, "Microfoon en PTT", "Een microfoon met PTT-knop en drie draden naar de zender: audio, massa en PTT.", b)


def aansluiten():
    w, h = 760, 240
    b = ARROW
    b += blok(10, 120, 120, 56, "voeding|13,8 V")
    b += line(130, 138, 180, 138, "w-red") + t(155, 130, "+ rood", "lbl s red", "middle")
    b += line(130, 158, 180, 158, "wire") + t(155, 176, "− zwart", "lbl s", "middle")
    b += blok(180, 110, 130, 76, "zender-|ontvanger")
    b += line(310, 148, 350, 148, "feed")
    b += blok(350, 120, 110, 56, "SWR-|meter")
    b += line(460, 148, 500, 148, "feed")
    b += blok(500, 120, 90, 56, "ATU")
    b += line(590, 148, 690, 148, "feed") + line(690, 148, 690, 90, "feed") + antenne(690, 90)
    b += t(640, 136, "coax", "lbl s", "middle")
    b += t(380, 40, "Juiste polariteit! Plus aan plus, min aan min.", "lbl b red", "middle")
    b += t(380, 222, "volgorde: voeding, zender, (SWR-meter), (ATU), coax, antenne", "lbl s", "middle")
    return svg(w, h, "Station aansluiten", "Voeding met rode plus en zwarte min naar de zender, dan SWR-meter, ATU, coax en antenne.", b)


def main():
    files = {"h08-qso": qso(), "h08-repeater": repeater(),
             "h08-bandplan-14": bandplan(SEG14, "Bandplan 20 m (14 MHz)", 14000, 14350, [14000, 14060, 14099, 14125, 14230, 14300, 14350]),
             "h08-bandplan-144": bandplan(SEG144, "Bandplan 2 m (144 MHz)", 144000, 146000, [144000, 144150, 144400, 144800, 145200, 145600, 146000]),
             "h08-smeter": smeter(), "h08-ptt": ptt(), "h08-aansluiten": aansluiten()}
    for k, v in files.items():
        open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(v)
    print(len(files), "tekeningen")


if __name__ == "__main__":
    main()

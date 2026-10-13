"""Tekeningen hoofdstuk 9 (Veiligheid). Schrijft naar assets/svg/."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg_h03 import svg, t, line, path, ARROW, OUT, s_zekering
from svg_h05 import blok, pijl, grond

ANT = "ant"


def persoon(x, y, s=1.0):
    """staand mannetje, voeten op (x,y)"""
    h = 90 * s
    return (f'<circle cx="{x}" cy="{y-h}" r="{11*s}" class="sym"/>'
            + line(x, y - h + 11 * s, x, y - 35 * s, "sym") + line(x, y - 35 * s, x - 14 * s, y, "sym") + line(x, y - 35 * s, x + 14 * s, y, "sym")
            + line(x, y - h + 28 * s, x - 30 * s, y - h + 40 * s, "sym") + line(x, y - h + 28 * s, x + 22 * s, y - h + 44 * s, "sym"))


def gevaren():
    w, h = 760, 250
    b = ARROW
    b += t(190, 30, "HOGE SPANNING", "lbl b red", "middle")
    b += f'<path d="M190,60 l-24,56 h20 l-14,56 l40,-72 h-22 l16,-40 z" class="sb" style="fill:var(--amber);opacity:.9;stroke:var(--text)"/>'
    b += t(190, 210, "gevaar voor elektrocutie", "lbl b", "middle") + t(190, 230, "(stroom door je lichaam)", "lbl s", "middle")
    b += line(380, 20, 380, 230, "guide2")
    b += t(570, 30, "GROTE STROOM", "lbl b red", "middle")
    b += f'<path d="M570,180 c-40,-20 -30,-60 -10,-90 c0,30 20,30 20,10 c10,20 30,40 10,80 z" class="sb" style="fill:var(--red);opacity:.85"/>'
    b += t(570, 210, "gevaar voor oververhitting", "lbl b", "middle") + t(570, 230, "en brand", "lbl s", "middle")
    return svg(w, h, "Twee gevaren", "Links: hoge spanning geeft gevaar voor elektrocutie. Rechts: grote stroom geeft oververhitting en brand.", b)


def aarding():
    w, h = 760, 320
    b = ARROW
    for k, (titel, geaard) in enumerate([("ZONDER aarding", False), ("MET aarding", True)]):
        x0 = 20 + k * 380
        b += t(x0 + 170, 28, titel, "lbl b " + ("green" if geaard else "red"), "middle")
        b += line(x0, 280, x0 + 340, 280, "wire")
        b += f'<rect x="{x0+40}" y="110" width="130" height="90" rx="8" class="box"/>' + t(x0 + 105, 150, "toestel", "lbl b", "middle") + t(x0 + 105, 170, "met defect", "lbl s red", "middle")
        b += f'<path d="M{x0+150},118 l10,26 l-8,0 l12,30" class="w-red" style="stroke-width:3"/>'
        b += line(x0 + 40, 150, x0 + 10, 150, "wire") + t(x0 + 10, 140, "230 V", "lbl s")
        if geaard:
            b += line(x0 + 105, 200, x0 + 105, 262, "wire thick") + grond(x0 + 105, 264, 30)
            b += f'<path d="M{x0+115},205 L{x0+115},255" class="w-green" style="stroke-width:3" marker-end="url(#pijl)"/>'
            b += t(x0 + 105, 304, "stroom via de aarding", "lbl s green", "middle")
            b += persoon(x0 + 270, 280) + t(x0 + 270, 304, "veilig", "lbl b green", "middle")
        else:
            b += persoon(x0 + 220, 280)
            b += f'<path d="M{x0+170},170 L{x0+196},178 L{x0+220},210 L{x0+226},275" class="w-red" style="stroke-width:3" marker-end="url(#pijl)"/>'
            b += t(x0 + 240, 150, "stroom door", "lbl s red") + t(x0 + 240, 166, "de persoon", "lbl s red")
            b += t(x0 + 220, 304, "levensgevaarlijk", "lbl b red", "middle")
    return svg(w, h, "Veiligheidsaarding", "Links raakt iemand een defect toestel zonder aarding aan: de stroom gaat door de persoon. Rechts heeft het toestel een aarding: de stroom gaat via de aarding.", b)


def zekering():
    w, h = 760, 200
    b = ARROW
    b += blok(20, 70, 120, 60, "voeding|of batterij")
    b += line(140, 100, 260, 100, "wire")
    b += s_zekering(300, 100)
    b += t(300, 70, "zekering", "lbl b", "middle")
    b += line(340, 100, 480, 100, "wire")
    b += blok(480, 70, 140, 60, "toestel")
    b += t(380, 170, "De zekering zit in de toevoer, zo dicht mogelijk bij de bron.", "lbl", "middle")
    b += t(380, 190, "Bij een te grote stroom brandt of springt ze: de stroom stopt.", "lbl s", "middle")
    return svg(w, h, "Zekering", "Voeding, dan een zekering, dan het toestel.", b)


def stekker():
    w, h = 760, 300
    b = ARROW
    b += f'<rect x="440" y="80" width="200" height="150" rx="40" class="cell" style="stroke:var(--text);stroke-width:2"/>'
    b += t(540, 262, "stekker (achterkant open)", "lbl s", "middle")
    b += f'<circle cx="490" cy="160" r="12" class="sym"/>' + t(490, 196, "fase", "lbl s", "middle")
    b += f'<circle cx="590" cy="160" r="12" class="sym"/>' + t(590, 196, "nul", "lbl s", "middle")
    b += f'<rect x="525" y="96" width="30" height="20" rx="4" class="sym"/>' + t(562, 112, "aarding", "lbl s")
    draden = [("blauw", "#2B6CB0", "nul (netspanning)", 50, "M30,50 H590 V148"),
              ("bruin", "#8B5A2B", "fase (netspanning)", 100, "M30,100 H490 V148"),
              ("geel-groen", "#9ACD32", "aarding (veiligheid)", 250, "M30,250 H420 V230 Q420,200 540,200 V116")]
    for n, c, rol, y, d in draden:
        b += f'<path d="{d}" style="fill:none;stroke:{c};stroke-width:7"/>'
        if n == "geel-groen":
            b += f'<path d="{d}" style="fill:none;stroke:#E6C619;stroke-width:7;stroke-dasharray:10 10"/>'
        b += t(30, y - 12, n, "lbl b") + t(130, y - 12, rol, "lbl s")
    return svg(w, h, "Netstekker aansluiten", "Bruin is de fase, blauw is de nul, geel-groen is de aarding.", b)


def ongeval():
    w, h = 760, 300
    b = ARROW
    stappen = [("1", "Spanning UIT", "stekker uit of de centrale schakelaar / zekering uit", "red"),
               ("2", "Pas dan aanraken", "nooit eerder: anders word je zelf slachtoffer", ""),
               ("3", "Hulp bellen: 112", "ook als het slachtoffer zich goed voelt", ""),
               ("4", "Eerste hulp", "volgens wat je geleerd hebt, tot de hulpdiensten er zijn", "")]
    for i, (n, a, s, c) in enumerate(stappen):
        y = 20 + i * 68
        b += f'<rect x="90" y="{y}" width="620" height="54" rx="10" class="box"/>'
        b += f'<circle cx="55" cy="{y+27}" r="20" class="sb"/>' + t(55, y + 33, n, "lbl b", "middle")
        b += t(110, y + 24, a, "lbl b " + c) + t(110, y + 44, s, "lbl s")
    return svg(w, h, "Ongeval met elektriciteit", "Vier stappen: spanning uit, pas dan aanraken, 112 bellen, eerste hulp.", b)


def shack():
    w, h = 760, 380
    b = ARROW
    b += line(0, 340, 760, 340, "wire")
    # huis
    b += f'<path d="M60,200 L200,110 L340,200" class="sym"/><rect x="60" y="200" width="280" height="140" class="cell"/>'
    b += blok(90, 260, 120, 50, "shack")
    # mast + antenne
    b += line(420, 340, 420, 60, "wire thick") + line(380, 60, 416, 60, ANT) + line(424, 60, 460, 60, ANT)
    b += t(470, 64, "antenne hoog", "lbl s")
    # bliksem
    b += f'<path d="M480,0 l-20,30 h14 l-14,26" class="w-red" style="stroke-width:3"/>'
    b += t(492, 30, "bliksem slaat in op hoge punten", "lbl s red")
    # coax naar huis via protector
    b += line(420, 80, 380, 80, "feed") + line(380, 80, 380, 290, "feed")
    b += f'<rect x="364" y="290" width="32" height="24" rx="4" class="box"/>' + t(380, 372, "bliksembeveiliging + aardpen", "lbl s", "middle")
    b += line(380, 314, 380, 340, "wire thick") + grond(380, 342, 26)
    b += line(364, 302, 210, 285, "feed")
    # hoogspanningslijn
    b += line(620, 340, 620, 80, "wire") + line(590, 90, 650, 90, "wire") + line(560, 96, 760, 96, "w-red")
    b += t(700, 120, "bovengrondse", "lbl s", "middle") + t(700, 136, "elektriciteitslijn", "lbl s", "middle")
    b += f'<line x1="440" y1="180" x2="610" y2="180" class="dim" marker-start="url(#pijl)" marker-end="url(#pijl)"/>'
    b += t(525, 172, "ruim afstand houden", "lbl b accent2", "middle")
    b += persoon(510, 340, 0.8) + persoon(560, 340, 0.8)
    b += t(535, 365, "nooit alleen", "lbl s b", "middle")
    return svg(w, h, "Veilige opstelling", "Een huis met shack, een antenne op een mast met bliksembeveiliging en aardpen, op ruime afstand van een bovengrondse elektriciteitslijn, twee personen bij het opbouwen.", b)


def main():
    files = {"h09-gevaren": gevaren(), "h09-aarding": aarding(), "h09-zekering": zekering(), "h09-stekker": stekker(),
             "h09-ongeval": ongeval(), "h09-shack": shack()}
    for k, v in files.items():
        open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(v)
    print(len(files), "tekeningen")


if __name__ == "__main__":
    main()

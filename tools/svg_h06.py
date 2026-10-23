"""Tekeningen hoofdstuk 6 (Propagatie). Schrijft naar assets/svg/."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg_h03 import svg, t, line, path, ARROW, OUT
from svg_h05 import blok, pijl, golfjes

ANT = "ant"


def mast(x, y, h=50):
    return line(x, y, x, y - h, "wire thick") + line(x, y - h, x, y - h - 16, ANT) + line(x, y - h - 8, x - 9, y - h - 20, ANT) + line(x, y - h - 8, x + 9, y - h - 20, ANT)


def straal(x1, y1, x2, y2, cls="w-amber", dash=False):
    st = ' style="stroke-dasharray:6 5"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"{st} marker-end="url(#pijl)"/>'


def basis():
    w, h = 760, 300
    b = ARROW
    # 1 rechtlijnig en zwakker
    b += t(20, 28, "1. rechtdoor, steeds zwakker", "lbl b accent2")
    b += mast(40, 120, 40)
    for i, sw in enumerate([5, 3.5, 2.2, 1.2]):
        x0 = 70 + i * 50
        b += f'<line x1="{x0}" y1="70" x2="{x0+40}" y2="70" class="w-amber" style="stroke-width:{sw}"/>'
    b += pijl(270, 70, 290, 70)
    b += t(170, 100, "dik = sterk, dun = zwak", "lbl s", "middle")
    # 2 weerkaatst
    b += t(330, 28, "2. weerkaatst", "lbl b accent2")
    b += f'<rect x="500" y="40" width="16" height="110" class="cell"/>'
    b += straal(340, 60, 498, 100) + straal(498, 100, 360, 140)
    b += t(508, 170, "wand", "lbl s", "middle")
    # 3 afgebogen
    b += t(560, 28, "3. afgebogen", "lbl b accent2")
    b += f'<path d="M560,150 L640,150 L640,80 L660,80 L660,150 Z" class="cell"/>'
    b += f'<path d="M570,70 L640,70 Q680,70 700,120" class="w-amber" marker-end="url(#pijl)"/>'
    b += t(660, 190, "rond een rand", "lbl s", "middle")
    b += line(20, 215, 740, 215, "guide2")
    b += t(380, 245, "Een radiogolf gedraagt zich zoals licht:", "lbl b", "middle")
    b += t(380, 270, "rechtdoor, tenzij ze weerkaatst of afgebogen wordt, en hoe verder, hoe zwakker.", "lbl", "middle")
    return svg(w, h, "Hoe een radiogolf zich verplaatst", "Drie gevallen: rechtdoor en steeds zwakker, weerkaatst tegen een wand, afgebogen rond een rand.", b)


def schaduw():
    w, h = 760, 280
    b = ARROW
    yg = 230
    b += '<path d="M330,160 L740,168 L740,230 L392,230 Z" class="sb" style="opacity:.35"/>'
    b += line(10, yg, 750, yg, "wire")
    b += mast(70, yg, 60)
    b += '<path d="M260,230 Q330,90 400,230 Z" class="cell"/>'
    b += t(330, 205, "heuvel", "lbl b", "middle")
    b += straal(80, 156, 740, 166)
    b += straal(80, 152, 600, 70)
    b += t(600, 200, "schaduwzone", "lbl b red", "middle")
    b += t(600, 218, "zwak of geen signaal", "lbl s", "middle")
    b += mast(500, yg, 30) + t(500, yg + 22, "ontvanger", "lbl s", "middle")
    b += t(70, yg + 22, "zender", "lbl s", "middle")
    return svg(w, h, "Schaduwzone achter een heuvel", "Een zender links, een heuvel in het midden. Achter de heuvel ligt een schaduwzone met weinig of geen ontvangst.", b)


def gebouw():
    w, h = 760, 300
    b = ARROW
    b += f'<rect x="300" y="40" width="260" height="220" class="cell"/>'
    b += f'<rect x="296" y="40" width="12" height="220" class="symfill" opacity="0.7"/>'
    b += f'<rect x="296" y="110" width="12" height="60" class="sb"/>'
    b += t(318, 62, "muur (beton)", "lbl s b red") + t(318, 104, "raam (glas)", "lbl s b green") + t(318, 250, "muur (beton)", "lbl s b red")
    b += straal(40, 140, 500, 140)
    b += straal(40, 75, 290, 75, "w-red") + t(160, 65, "botst op de muur", "lbl s", "middle")
    b += straal(40, 210, 290, 210, "w-red") + t(160, 200, "botst op de muur", "lbl s", "middle")
    b += t(160, 130, "gaat door het glas", "lbl s", "middle")
    b += t(430, 190, "binnen: het best", "lbl s", "middle") + t(430, 206, "bij het raam", "lbl s", "middle")
    b += mast(690, 260, 120) + t(690, 284, "buitenantenne: best", "lbl s", "middle")
    return svg(w, h, "Radiogolven en gebouwen", "Een muur van beton houdt de golf grotendeels tegen, een glazen raam laat ze door.", b)


def horizon():
    w, h = 760, 300
    b = ARROW
    R = 1600
    cx, cy = 380, 250 + R
    pts = [(cx + R * math.sin(a), cy - R * math.cos(a)) for a in [i / 100 * 0.5 - 0.25 for i in range(101)]]
    b += f'<path d="{path(pts)} L760,300 L0,300 Z" class="cell"/>'
    b += t(60, 290, "aarde (bol)", "lbl s")

    def grondpunt(x):
        a = math.asin((x - cx) / R)
        return cx + R * math.sin(a), cy - R * math.cos(a)

    def raak(xa, hgt):
        x0, y0 = grondpunt(xa)
        xt, yt = x0, y0 - hgt
        d = math.hypot(xt - cx, yt - cy)
        ang = math.atan2(yt - cy, xt - cx) + math.acos(R / d)
        return (x0, y0, xt, yt, cx + R * math.cos(ang), cy + R * math.sin(ang))
    x0, y0, xt, yt, tx, ty = raak(110, 30)
    b += line(x0, y0, xt, yt, "wire thick") + t(x0 - 6, yt - 6, "lage antenne", "lbl s", "end")
    b += f'<line x1="{xt:.0f}" y1="{yt:.0f}" x2="{tx:.0f}" y2="{ty:.0f}" class="w-red" style="stroke-dasharray:6 5"/>'
    b += f'<circle cx="{tx:.0f}" cy="{ty:.0f}" r="5" class="symfill"/>' + t(tx, ty + 24, "horizon (laag)", "lbl s red", "middle")
    x0, y0, xt, yt, tx, ty = raak(160, 75)
    b += line(x0, y0, xt, yt, "wire thick") + t(xt + 10, yt, "hoge antenne", "lbl s")
    b += f'<line x1="{xt:.0f}" y1="{yt:.0f}" x2="{tx:.0f}" y2="{ty:.0f}" class="w-green"/>'
    b += f'<circle cx="{tx:.0f}" cy="{ty:.0f}" r="5" class="symfill"/>' + t(tx, ty + 24, "horizon (hoog)", "lbl s green", "middle")
    b += t(560, 40, "VHF en UHF: niet veel verder", "lbl b", "middle")
    b += t(560, 62, "dan de horizon.", "lbl b", "middle")
    b += t(560, 90, "Hogere antenne = verdere horizon.", "lbl", "middle")
    return svg(w, h, "Horizon", "Een lage en een hoge antenne op de bolle aarde. De lijn vanaf de hoge antenne raakt de aarde veel verder weg.", b)


def hoogte_vermogen():
    w, h = 760, 260
    b = ARROW
    b += t(190, 28, "antenne hoger", "lbl b green", "middle")
    b += mast(80, 200, 110) + mast(300, 200, 110)
    b += f'<line x1="100" y1="90" x2="280" y2="90" class="w-green" marker-start="url(#pijl)" marker-end="url(#pijl)"/>'
    b += t(190, 80, "zenden én ontvangen beter", "lbl s", "middle")
    b += t(570, 28, "meer vermogen", "lbl b accent2", "middle")
    b += blok(420, 150, 90, 46, "1 kW")
    b += mast(540, 200, 40) + mast(700, 200, 40)
    b += f'<line x1="560" y1="150" x2="680" y2="150" class="w-amber" style="stroke-width:3" marker-end="url(#pijl)"/>'
    b += t(620, 132, "jij wordt beter gehoord", "lbl s", "middle")
    b += f'<line x1="680" y1="180" x2="560" y2="180" class="w-red" marker-end="url(#pijl)"/>'
    b += t(620, 214, "jij hoort de ander niet beter", "lbl s red", "middle")
    b += t(380, 248, "Daarom: eerst de antenne hoger, pas dan meer vermogen.", "lbl b", "middle")
    return svg(w, h, "Antenne hoger of meer vermogen", "Links: een hogere antenne helpt in beide richtingen. Rechts: meer vermogen helpt alleen bij zenden.", b)


def ionosfeer():
    w, h = 760, 330
    b = ARROW
    R = 1500
    cx, cy = 380, 260 + R

    def pt(a, r):
        return cx + r * math.sin(a), cy - r * math.cos(a)

    def boog(r, a0=-0.28, a1=0.28, n=100):
        return [pt(a0 + (a1 - a0) * i / n, r) for i in range(n + 1)]
    b += f'<path d="{path(boog(R+150) + boog(R+200, 0.28, -0.28))} Z" class="sb"/>'
    b += t(380, 82, "ionosfeer: lagen geladen gas op 70 tot 400 km hoogte", "lbl b", "middle")
    b += f'<path d="{path(boog(R))} L760,330 L0,330 Z" class="cell"/>'
    b += t(560, 318, "aarde", "lbl s", "middle")
    a = [-0.22, -0.02, 0.18]
    pts = [pt(a[0], R), pt((a[0] + a[1]) / 2, R + 150), pt(a[1], R), pt((a[1] + a[2]) / 2, R + 150), pt(a[2], R)]
    b += f'<path d="{path(pts)}" class="w-amber" style="stroke-width:3" marker-end="url(#pijl)"/>'
    b += t(pts[0][0], pts[0][1] + 24, "zender", "lbl s b", "middle")
    b += t(pts[4][0], pts[4][1] + 24, "ontvanger ver weg", "lbl s b", "middle")
    p0 = pts[0]
    b += f'<line x1="{p0[0]:.0f}" y1="{p0[1]:.0f}" x2="{p0[0]+40:.0f}" y2="30" class="w-green" style="stroke-dasharray:6 5" marker-end="url(#pijl)"/>'
    b += t(p0[0] + 50, 30, "VHF: gaat erdoor, de ruimte in", "lbl s green")
    return svg(w, h, "Ionosfeer", "Een HF-golf kaatst terug op de ionosfeer en komt ver weg weer op aarde, eventueel meerdere keren. Een VHF-golf gaat door de ionosfeer heen.", b)


def dagnacht():
    w, h = 760, 340
    b = ARROW
    for k, (titel, dlaag) in enumerate([("OVERDAG", True), ("'S NACHTS", False)]):
        x0 = 20 + k * 380
        b += t(x0 + 170, 28, titel, "lbl b accent2", "middle")
        b += line(x0, 260, x0 + 340, 260, "wire")
        b += f'<rect x="{x0}" y="60" width="340" height="{36 if dlaag else 24}" class="sb"/>'
        b += t(x0 + 5, 52, "F-laag" + ("" if dlaag else " (dunner)"), "lbl s")
        if dlaag:
            b += f'<rect x="{x0}" y="170" width="340" height="22" class="cell"/>'
            b += t(x0 + 335, 186, "D-laag", "lbl s", "end")
            b += f'<path d="M{x0+30},258 L{x0+90},175" class="w-red" style="stroke-width:3"/>'
            b += f'<path d="M{x0+130},258 L{x0+210},64 L{x0+290},258" class="w-amber" style="stroke-width:3" marker-end="url(#pijl)"/>'
            b += t(x0 + 30, 282, "lage freq.: opgeslokt", "lbl s red")
            b += t(x0 + 250, 300, "hoge freq.: terug", "lbl s", "middle")
        else:
            b += t(x0 + 335, 186, "geen D-laag", "lbl s", "end")
            b += f'<path d="M{x0+20},258 L{x0+100},84 L{x0+180},258" class="w-amber" style="stroke-width:3" marker-end="url(#pijl)"/>'
            b += f'<path d="M{x0+220},258 L{x0+290},40" class="w-green" style="stroke-dasharray:6 5" marker-end="url(#pijl)"/>'
            b += t(x0 + 100, 282, "lage freq.: komt ver", "lbl s", "middle")
            b += t(x0 + 260, 282, "boven ±12 MHz:", "lbl s green", "middle") + t(x0 + 260, 298, "gaat erdoor", "lbl s green", "middle")
    b += t(380, 330, "D-laag = slokt lage frequenties op. F-laag = kaatst terug.", "lbl b", "middle")
    return svg(w, h, "Ionosfeer overdag en 's nachts", "Overdag slokt de D-laag lage frequenties op en kaatst de F-laag hoge frequenties terug. 's Nachts is de D-laag weg en gaan hoge frequenties door de F-laag.", b)


def zonnecyclus():
    w, h = 760, 250
    b = ARROW
    b += line(60, 200, 730, 200, "axisline") + f'<line x1="60" y1="200" x2="60" y2="30" class="axisline" marker-end="url(#pijlas)"/>'
    b += f'<line x1="60" y1="200" x2="740" y2="200" class="axisline" marker-end="url(#pijlas)"/>'
    b += t(70, 30, "aantal zonnevlekken", "lbl s")
    b += t(735, 225, "tijd (jaren)", "lbl s", "end")
    pts = []
    for i in range(301):
        u = i / 300
        yrs = u * 26
        v = max(0, math.sin(math.pi * ((yrs - 1) % 11) / 11)) ** 1.6
        pts.append((60 + 660 * u, 195 - 115 * v))
    b += f'<path d="{path(pts)}" class="w-green"/>'
    x1 = 60 + 660 * (6.5 / 26); x2 = 60 + 660 * (17.5 / 26)
    b += f'<line x1="{x1:.0f}" y1="40" x2="{x2:.0f}" y2="40" class="dim" marker-start="url(#pijl)" marker-end="url(#pijl)"/>'
    b += t((x1 + x2) / 2, 32, "ongeveer 11 jaar", "lbl b accent2", "middle")
    b += t(x1 + 50, 92, "maximum:", "lbl s") + t(x1 + 50, 108, "HF-banden ver open", "lbl s")
    b += t(60 + 660 * (12 / 26) + 20, 175, "minimum", "lbl s")
    return svg(w, h, "Zonnevlekkencyclus", "Het aantal zonnevlekken stijgt en daalt in een cyclus van ongeveer 11 jaar.", b)


def main():
    files = {"h06-basis": basis(), "h06-schaduw": schaduw(), "h06-gebouw": gebouw(), "h06-horizon": horizon(),
             "h06-hoogte-vermogen": hoogte_vermogen(), "h06-ionosfeer": ionosfeer(), "h06-dagnacht": dagnacht(),
             "h06-zonnecyclus": zonnecyclus()}
    for k, v in files.items():
        open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(v)
    print(len(files), "tekeningen")


if __name__ == "__main__":
    main()

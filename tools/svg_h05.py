"""Tekeningen hoofdstuk 5 (Antennes en kabels). Schrijft naar assets/svg/."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg_h03 import svg, t, line, path, ARROW, OUT

ANT = "ant"


def golfjes(x, y, n=3, r0=14, dr=12, rechts=True, cls="w-amber"):
    """concentrische boogjes (radiogolven) vanaf punt x,y"""
    s = ""
    for i in range(n):
        r = r0 + i * dr
        if rechts:
            s += f'<path d="M{x+r*0.6:.1f},{y-r*0.8:.1f} A{r},{r} 0 0 1 {x+r*0.6:.1f},{y+r*0.8:.1f}" class="{cls}"/>'
        else:
            s += f'<path d="M{x-r*0.6:.1f},{y-r*0.8:.1f} A{r},{r} 0 0 0 {x-r*0.6:.1f},{y+r*0.8:.1f}" class="{cls}"/>'
    return s


def blok(x, y, w, h, tekst):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="box"/>'
    regels = tekst.split("|")
    y0 = y + h / 2 + 5 - (len(regels) - 1) * 9
    for i, r in enumerate(regels):
        s += t(x + w / 2, y0 + i * 18, r, "lbl b", "middle")
    return s


def pijl(x1, y1, x2, y2, cls="arrow"):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}" marker-end="url(#pijl)"/>'


def maat(x1, x2, y, tekst, boven=True):
    """maatlijn met pijlen aan beide kanten"""
    ty = y - 8 if boven else y + 20
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" class="dim" marker-start="url(#pijl)" marker-end="url(#pijl)"/>'
            + t((x1 + x2) / 2, ty, tekst, "lbl accent2 b", "middle"))


def maat_v(x, y1, y2, tekst, links=True):
    tx = x - 10 if links else x + 10
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" class="dim" marker-start="url(#pijl)" marker-end="url(#pijl)"/>'
            + t(tx, (y1 + y2) / 2 + 5, tekst, "lbl accent2 b", "end" if links else "start"))


def spoel_v(x, y, n=4, r=7):
    """verticale spoel van y (boven) naar beneden, n windingen"""
    d = f"M{x},{y}"
    for i in range(n):
        d += f" a{r},{r} 0 1 1 0,{2*r}"
    return f'<path d="{d}" class="sym"/>'


def grond(x, y, w=30):
    return line(x - w / 2, y, x + w / 2, y) + line(x - w / 3, y + 6, x + w / 3, y + 6) + line(x - w / 6, y + 12, x + w / 6, y + 12)


# ------------------------------------------------------------------ figuren

def omzetter():
    w, h = 760, 220
    b = ARROW
    b += blok(20, 70, 120, 60, "zender")
    b += line(140, 100, 230, 100, "feed") + line(230, 100, 230, 60, "feed")
    b += line(230, 60, 230, 20, ANT) + line(230, 34, 214, 14, ANT) + line(230, 34, 246, 14, ANT)
    b += golfjes(240, 30, 4, 18, 16)
    b += line(530, 60, 530, 20, ANT) + line(530, 34, 514, 14, ANT) + line(530, 34, 546, 14, ANT)
    b += golfjes(520, 30, 4, 18, 16, rechts=False)
    b += line(530, 60, 530, 100, "feed") + line(530, 100, 620, 100, "feed")
    b += blok(620, 70, 120, 60, "ontvanger")
    b += t(380, 30, "radiogolf", "lbl b accent2", "middle")
    b += pijl(330, 60, 430, 60)
    b += t(185, 150, "elektrisch", "lbl s", "middle") + t(185, 166, "signaal", "lbl s", "middle")
    b += t(575, 150, "elektrisch", "lbl s", "middle") + t(575, 166, "signaal", "lbl s", "middle")
    b += t(230, 200, "zendantenne: elektrisch → golf", "lbl b", "middle")
    b += t(530, 200, "ontvangstantenne: golf → elektrisch", "lbl b", "middle")
    return svg(w, h, "Antenne als omzetter", "Links zet de antenne een elektrisch signaal om in een radiogolf, rechts gebeurt het omgekeerde.", b)


def halve_sinus(x0, x1, ybase, amp, cls="w-green", n=40, f0=0.0, f1=1.0):
    pts = []
    for i in range(n + 1):
        u = f0 + (f1 - f0) * i / n
        pts.append((x0 + (x1 - x0) * i / n, ybase - amp * math.sin(math.pi * u)))
    return f'<path d="{path(pts)}" class="{cls}"/>'


def resonantie():
    w, h = 760, 330
    b = ARROW
    rijen = [("juiste lengte", 80, 680, "de halve golf past precies: nul aan beide uiteinden", "lbl b green"),
             ("te kort", 170, 590, "de antenne stopt voor de golf rond is", "lbl b red"),
             ("te lang", 40, 720, "de antenne is langer dan de halve golf", "lbl b red")]
    for i, (naam, xa, xb, uitleg, cls) in enumerate(rijen):
        y = 80 + i * 100
        b += t(20, y - 50, naam, cls)
        b += halve_sinus(80, 680, y, 42, "env")
        b += line(xa, y, 375, y, ANT) + line(385, y, xb, y, ANT)
        b += f'<circle cx="380" cy="{y}" r="3" class="symfill"/>'
        b += t(380, y + 22, uitleg, "lbl s", "middle")
    b += t(380, 318, "stippellijn = stroom in de antenne bij de gewenste frequentie (een halve golf)", "lbl s", "middle")
    return svg(w, h, "Resonantie van een dipool", "Drie dipolen: juiste lengte, te kort en te lang, met de halve golf van de stroom als stippellijn.", b)


def grootte():
    banden = [("80 m", 3.6), ("40 m", 7.1), ("20 m", 14.2), ("10 m", 28.5), ("2 m", 145.0), ("70 cm", 435.0)]
    w, h = 760, 60 + 46 * len(banden)
    b = t(20, 28, "lengte van een halve-golf-dipool (λ/2 = 150 / f)", "lbl b")
    schaal = 500 / 42.0
    for i, (n, f) in enumerate(banden):
        y = 55 + i * 46
        lengte = 150 / f
        b += t(20, y + 18, n, "lbl b mono")
        b += t(78, y + 18, f"{str(f).replace('.', ',')} MHz", "lbl s mono")
        b += f'<rect x="170" y="{y+4}" width="{max(lengte*schaal,2):.1f}" height="18" rx="3" class="{"sb" if f < 30 else "cell"}"/>'
        txt = f"{lengte:.1f}".replace(".", ",") + " m" if lengte >= 1 else f"{lengte*100:.0f} cm"
        b += t(178 + max(lengte * schaal, 2), y + 18, txt, "lbl b")
    b += t(20, h - 6, "HF (kortegolf) bovenaan, VHF en UHF onderaan: zelfde soort antenne, alleen veel kleiner", "lbl s")
    return svg(w, h, "Antennelengte per band", "Staafdiagram: een dipool voor 80 m is ruim 40 meter, voor 2 m ongeveer 1 meter.", b)


def dipool():
    w, h = 760, 330
    b = ARROW
    b += t(20, 30, "horizontale dipool", "lbl b accent2")
    b += line(40, 120, 312, 120, ANT) + line(328, 120, 600, 120, ANT)
    b += halve_sinus(40, 600, 120, 60, "env")
    b += t(320, 52, "stroom: grootst in het midden", "lbl s", "middle")
    b += t(40, 145, "0", "lbl s", "middle") + t(600, 145, "0", "lbl s", "middle")
    b += line(312, 120, 312, 175, "feed") + line(328, 120, 328, 175, "feed")
    b += t(320, 195, "voedingspunt: naar zender / ontvanger", "lbl s", "middle")
    b += maat(40, 600, 240, "λ/2 (een halve golflengte)")
    b += t(690, 30, "verticale dipool", "lbl b accent2", "middle")
    b += line(690, 50, 690, 172, ANT) + line(690, 188, 690, 310, ANT)
    b += line(690, 172, 735, 172, "wire") + line(690, 188, 735, 188, "wire")
    return svg(w, h, "Dipool", "Een dipool is in het midden onderbroken en gevoed. Lengte een halve golflengte. Stroom is maximaal in het midden en nul aan de uiteinden.", b)


def ant_58(x, ybot, hoogte=150, label=True):
    """5/8 λ: grondvlak, spoel, straler"""
    s = line(x - 40, ybot, x + 40, ybot, "wire thick")
    s += line(x, ybot, x, ybot - 18, ANT) + spoel_v(x, ybot - 18 - 56, 4, 7).replace('class="sym"', 'class="sym"')
    s += line(x, ybot - 18 - 56, x, ybot - hoogte, ANT)
    if label:
        s += t(x + 16, ybot - 40, "SPOEL", "lbl s b") + t(x, ybot + 22, "GRONDVLAK", "lbl s b", "middle")
    return s


def gp(x, ytop, hoogte=110, rad=70):
    s = line(x, ytop, x, ytop + hoogte, ANT)
    yb = ytop + hoogte
    for dx, dy in [(-rad, rad * 0.9), (rad, rad * 0.9), (-rad * 0.45, rad * 1.05), (rad * 0.45, rad * 1.05)]:
        s += line(x, yb, x + dx, yb + dy, ANT)
    return s


def yagi_persp(x, y, s=1.0):
    """yagi schuin van boven gezien: boom + 4 elementen"""
    out = ""
    bx0, by0, bx1, by1 = x - 70 * s, y + 35 * s, x + 70 * s, y - 35 * s
    out += line(bx0, by0, bx1, by1, "wire")
    for i, L in enumerate([1.1, 1.0, 0.9, 0.85]):
        cx = bx0 + (bx1 - bx0) * i / 3
        cy = by0 + (by1 - by0) * i / 3
        dx, dy = 75 * s * L, 30 * s * L
        out += line(cx - dx, cy - dy, cx + dx, cy + dy, ANT)
    return out


def abcd1():
    w, h = 760, 260
    b = ""
    b += ant_58(80, 200, 170)
    b += line(210, 110, 302, 110, ANT) + line(312, 110, 404, 110, ANT)
    b += line(480, 40, 480, 106, ANT) + line(480, 116, 480, 182, ANT)
    b += yagi_persp(650, 110, 0.72)
    for x, l in [(80, "A"), (307, "B"), (480, "C"), (650, "D")]:
        b += t(x, 252, f"({l})", "lbl big", "middle")
    return svg(w, h, "Vier antennes A tot D", "A: antenne met spoel op grondvlak. B: horizontale dipool. C: verticale dipool. D: antenne met vier elementen op een drager.", b)


def abcd2():
    w, h = 760, 280
    b = ""
    b += ant_58(80, 210, 180)
    # eindgevoede draad
    b += line(230, 70, 230, 220, "wire thick") + line(420, 70, 420, 220, "wire thick")
    b += line(230, 70, 420, 70, ANT)
    b += f'<path d="M230,70 Q215,140 205,195" class="ant"/>'
    b += line(205, 195, 205, 205, "wire") + grond(205, 205, 22)
    b += t(240, 214, "MAST", "lbl s b") + t(410, 214, "MAST", "lbl s b", "end")
    b += line(520, 50, 520, 136, ANT) + line(520, 146, 520, 232, ANT)
    b += gp(660, 40, 100, 70)
    for x, l in [(80, "A"), (325, "B"), (520, "C"), (660, "D")]:
        b += t(x, 272, f"({l})", "lbl big", "middle")
    return svg(w, h, "Vier antennes A tot D (tweede reeks)", "A: antenne met spoel op grondvlak. B: draad tussen twee masten, aan één kant gevoed. C: verticale dipool. D: verticale staaf met vier schuine draden.", b)


def kwartgolf():
    w, h = 760, 330
    b = ARROW
    x, yg = 230, 190
    b += f'<rect x="60" y="{yg}" width="340" height="12" class="cell"/>'
    b += t(230, yg + 34, "grondvlak (metalen plaat of draden in de grond)", "lbl s", "middle")
    b += line(x, yg - 4, x, 40, ANT)
    b += line(x, 300, x, yg + 44, "ghost")
    b += maat_v(x - 40, 40, yg - 4, "λ/4")
    b += t(x + 14, 60, "straler", "lbl b")
    b += t(x + 14, 290, "spiegelbeeld", "lbl s")
    b += t(x + 14, 306, "(bestaat niet echt)", "lbl s")
    b += f'<circle cx="{x}" cy="{yg-4}" r="5" class="symfill"/>' + t(x + 12, yg - 12, "voedingspunt (coax)", "lbl s")
    b += t(470, 70, "Het grondvlak werkt als een spiegel.", "lbl b")
    b += t(470, 96, "Samen met zijn spiegelbeeld gedraagt", "lbl")
    b += t(470, 118, "een kwartgolf zich als een dipool", "lbl")
    b += t(470, 140, "van een halve golflengte.", "lbl")
    b += t(470, 180, "λ/4 + λ/4 (spiegel) = λ/2", "lbl b mono accent2")
    return svg(w, h, "Kwartgolfantenne", "Een verticale staaf van een kwart golflengte op een grondvlak. Het grondvlak vormt het spiegelbeeld, samen een halve golflengte.", b)


def groundplane():
    w, h = 760, 320
    b = ARROW
    x = 230
    b += gp(x, 30, 140, 110)
    b += t(x + 14, 60, "straler (λ/4)", "lbl b")
    b += t(x + 115, 290, "radialen (elk λ/4)", "lbl b")
    b += line(x, 170, x, 300, "feed") + t(x - 10, 315, "coax naar zender", "lbl s", "end")
    b += f'<path d="M{x+40},{170+36} A50,50 0 0 0 {x+52},{170}" class="w-amber"/>'
    b += t(x + 70, 200, "± 45°", "lbl s b accent2")
    b += t(450, 70, "Een kwartgolf hoog op een mast.", "lbl b")
    b += t(450, 96, "De grond is te ver weg, dus maken", "lbl")
    b += t(450, 118, "schuine draden (radialen) het", "lbl")
    b += t(450, 140, "grondvlak.", "lbl")
    b += t(450, 176, "Rondstraler, verticaal gepolariseerd.", "lbl s")
    return svg(w, h, "Groundplane-antenne", "Verticale straler van een kwart golflengte met schuin naar beneden hangende radialen, ongeveer 45 graden.", b)


def vijfachtste():
    w, h = 760, 330
    b = ARROW
    x, yb = 200, 290
    b += line(x - 70, yb, x + 70, yb, "wire thick")
    b += line(x, yb, x, yb - 20, ANT) + spoel_v(x, yb - 76, 4, 7) + line(x, yb - 76, x, 30, ANT)
    b += t(x + 18, yb - 44, "spoel", "lbl b")
    b += t(x, yb + 26, "grondvlak", "lbl s", "middle")
    b += maat_v(x - 40, 30, yb - 4, "5/8 λ")
    b += f'<circle cx="{x}" cy="{yb-2}" r="5" class="symfill"/>' + t(x + 80, yb - 12, "voedingspunt (coax)", "lbl s")
    b += t(420, 70, "Langer dan een kwartgolf (5/8 in plaats", "lbl")
    b += t(420, 92, "van 2/8). Bundelt de straling beter", "lbl")
    b += t(420, 114, "naar de horizon.", "lbl")
    b += t(420, 150, "Niet vanzelf in resonantie:", "lbl b")
    b += t(420, 172, "de spoel onderaan brengt hem op", "lbl")
    b += t(420, 194, "de juiste frequentie.", "lbl")
    b += t(420, 230, "Herken hem aan: lange staaf + spoel.", "lbl b accent2")
    return svg(w, h, "5/8 λ-antenne", "Verticale straler van vijf achtste golflengte met een spoel onderaan op een grondvlak.", b)


def langdraad():
    w, h = 760, 280
    b = ARROW
    b += line(200, 60, 200, 240, "wire thick") + line(620, 60, 620, 240, "wire thick")
    b += line(200, 60, 620, 60, ANT)
    b += f'<path d="M200,60 Q175,130 160,190" class="ant"/>'
    b += blok(40, 170, 100, 46, "zender")
    b += line(140, 193, 160, 193, "wire")
    b += line(90, 216, 90, 236, "wire") + grond(90, 236, 30)
    b += t(110, 262, "aarding (tegengewicht)", "lbl s")
    b += t(410, 48, "lange draad", "lbl b", "middle")
    b += t(212, 236, "mast", "lbl s b") + t(608, 236, "mast", "lbl s b", "end")
    b += t(410, 120, "Eén kant gevoed, de aarde dient als", "lbl", "middle")
    b += t(410, 142, "tweede helft. De lengte én de hoogte", "lbl", "middle")
    b += t(410, 164, "boven de grond bepalen de frequentie.", "lbl", "middle")
    return svg(w, h, "Eindgevoede draadantenne", "Een lange draad tussen twee masten, aan één uiteinde verbonden met de zender, met de aarde als tegengewicht.", b)


def yagi():
    w, h = 760, 330
    b = ARROW
    y0 = 165
    b += line(80, y0, 600, y0, "wire thick")
    els = [(120, 230, "reflector", "iets langer"), (260, 205, "straler", "dipool, gevoed"),
           (400, 180, "director", "iets korter"), (530, 165, "director", "nog korter")]
    for x, L, n, u in els:
        half = L / 2
        if n == "straler":
            b += line(x, y0 - half, x, y0 - 6, ANT) + line(x, y0 + 6, x, y0 + half, ANT)
            b += line(x, y0 + 4, x - 30, y0 + 40, "feed")
            b += t(x - 34, y0 + 60, "coax", "lbl s", "end")
        else:
            b += line(x, y0 - half, x, y0 + half, ANT)
        b += t(x, y0 - half - 22, n, "lbl b", "middle")
        b += t(x, y0 - half - 6, u, "lbl s", "middle")
    b += t(330, y0 + 22, "drager (boom)", "lbl s", "middle")
    b += pijl(620, y0, 740, y0, "dim")
    b += t(680, y0 - 12, "richting", "lbl b accent2", "middle") + t(680, y0 + 26, "straling", "lbl b accent2", "middle")
    b += t(380, 316, "bovenaanzicht: de golf vertrekt naar de kant van de directoren", "lbl s", "middle")
    return svg(w, h, "Yagi-antenne", "Bovenaanzicht van een yagi: reflector achteraan, gevoede straler, directoren vooraan. De straling gaat naar de kant van de directoren.", b)


def polair(cx, cy, r, f, n=180):
    pts = []
    for i in range(n + 1):
        a = 2 * math.pi * i / n
        rr = r * f(a)
        pts.append((cx + rr * math.cos(a), cy - rr * math.sin(a)))
    return f'<path d="{path(pts)} Z" class="sb"/>'


def straling():
    w, h = 760, 330
    b = ARROW
    cx = [130, 380, 630]
    cy, r = 160, 95
    for x in cx:
        b += f'<circle cx="{x}" cy="{cy}" r="{r}" class="guide2" fill="none"/>'
        b += line(x - r - 8, cy, x + r + 8, cy, "guide2") + line(x, cy - r - 8, x, cy + r + 8, "guide2")
    # rondstraler
    b += polair(cx[0], cy, r * 0.8, lambda a: 1)
    b += f'<circle cx="{cx[0]}" cy="{cy}" r="5" class="symfill"/>'
    # horizontale dipool langs x-as: straling dwars (y-richting): |sin a|
    b += polair(cx[1], cy, r * 0.95, lambda a: abs(math.sin(a)) ** 1.0)
    b += line(cx[1] - 45, cy, cx[1] + 45, cy, ANT)
    # yagi wijst naar rechts
    def yg(a):
        v = max(math.cos(a), 0) ** 3
        terug = 0.18 * max(-math.cos(a), 0) ** 2
        return max(v, terug)
    b += polair(cx[2] - 40, cy, r * 1.25, yg)
    b += line(cx[2] - 40, cy - 22, cx[2] - 40, cy + 22, ANT) + line(cx[2] - 60, cy, cx[2] - 10, cy, "wire")
    b += line(cx[2] - 25, cy - 18, cx[2] - 25, cy + 18, ANT)
    labels = [("rondstraler", "verticale antenne"), ("horizontale dipool", "2 voorkeurrichtingen"), ("yagi", "1 voorkeurrichting")]
    for x, (a, s) in zip(cx, labels):
        b += t(x, 290, a, "lbl b", "middle") + t(x, 310, s, "lbl s", "middle")
    b += t(380, 26, "bovenaanzicht: hoe ver het signaal in elke richting komt", "lbl s", "middle")
    return svg(w, h, "Stralingsdiagrammen", "Bovenaanzicht van drie stralingsdiagrammen: een cirkel voor een verticale rondstraler, een acht dwars op een horizontale dipool en één grote lob voor een yagi.", b)


def polarisatie():
    w, h = 760, 300
    b = ARROW
    # horizontaal: liggend vlak (parallellogram) met sinus erin
    b += t(190, 28, "horizontale antenne", "lbl b accent2", "middle")
    b += f'<path d="M40,150 L300,150 L360,110 L100,110 Z" class="cell"/>'
    b += line(30, 130, 80, 130, ANT)
    pts = []
    for i in range(81):
        u = i / 80
        x = 80 + 250 * u
        dy = 20 * math.sin(2 * math.pi * 2 * u)
        pts.append((x + dy * 1.5 * -1, 130 + dy))
    b += f'<path d="{path(pts)}" class="w-green"/>'
    b += t(190, 190, "de golf trilt horizontaal", "lbl", "middle")
    b += t(190, 212, "(liggend, zoals de antenne)", "lbl s", "middle")
    # verticaal
    b += t(570, 28, "verticale antenne", "lbl b accent2", "middle")
    b += line(430, 90, 430, 170, ANT)
    pts = []
    for i in range(81):
        u = i / 80
        pts.append((440 + 270 * u, 130 - 40 * math.sin(2 * math.pi * 2 * u)))
    b += f'<path d="{path(pts)}" class="w-green"/>'
    b += t(570, 190, "de golf trilt verticaal", "lbl", "middle")
    b += t(570, 212, "(rechtop, zoals de antenne)", "lbl s", "middle")
    b += t(380, 268, "Polarisatie = de richting waarin de golf trilt = de richting van de antenne.", "lbl b", "middle")
    return svg(w, h, "Polarisatie", "Links een horizontale antenne met een horizontaal trillende golf, rechts een verticale antenne met een verticaal trillende golf.", b)


def erp():
    w, h = 760, 270
    b = ARROW
    b += blok(20, 50, 120, 56, "zender|10 W")
    b += line(140, 78, 230, 78, "feed")
    b += yagi_persp(300, 78, 0.6)
    b += t(300, 140, "yagi, winst 5", "lbl b", "middle")
    b += pijl(380, 78, 480, 78, "dim")
    b += t(560, 70, "ERP = 10 W × 5", "lbl b mono", "middle") + t(560, 96, "= 50 W", "lbl big", "middle")
    b += line(20, 170, 740, 170, "guide2")
    b += blok(20, 190, 120, 56, "zender|50 W")
    b += line(140, 218, 260, 218, "feed") + line(200, 200, 256, 200, ANT) + line(264, 200, 320, 200, ANT) + line(260, 218, 260, 200, "feed")
    b += t(260, 250, "gewone dipool", "lbl b", "middle")
    b += t(380, 222, "= in de voorkeurrichting even sterk als boven", "lbl s")
    return svg(w, h, "ERP", "Boven: 10 watt in een yagi met winst 5 geeft een ERP van 50 watt. Onder: dat is even sterk als 50 watt in een gewone dipool.", b)


def coax():
    w, h = 760, 300
    b = ARROW
    y = 110
    # zijaanzicht, getrapt gestript
    b += f'<rect x="420" y="{y-46}" width="300" height="92" rx="8" class="symfill" opacity="0.85"/>'
    b += f'<rect x="300" y="{y-38}" width="130" height="76" class="cell"/>'
    b += '<defs><pattern id="vlecht" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="10" class="wire" style="stroke-width:3"/></pattern></defs>'
    b += f'<rect x="300" y="{y-38}" width="130" height="76" fill="url(#vlecht)" class="sym"/>'
    b += f'<rect x="170" y="{y-28}" width="140" height="56" class="box"/>'
    b += f'<rect x="40" y="{y-6}" width="140" height="12" class="carrier"/>'
    b += f'<rect x="40" y="{y-6}" width="140" height="12" fill="var(--amber)"/>'
    lab = [(90, "binnengeleider", "koper: draagt het signaal"), (240, "diëlektricum", "isolatie: houdt de kern in het midden"),
           (365, "afscherming", "vlechtwerk: houdt het signaal binnen"), (570, "mantel", "buitenkant: tegen water en weer")]
    for i, (x, n, u) in enumerate(lab):
        yy = 210 + (i % 2) * 44
        b += line(x, y + (10 if i == 0 else 30 if i == 1 else 40 if i == 2 else 48), x, yy - 18, "guide2")
        b += t(x, yy, n, "lbl b", "middle") + t(x, yy + 18, u, "lbl s", "middle")
    b += t(380, 30, "coaxkabel, laag per laag afgestript", "lbl s", "middle")
    return svg(w, h, "Opbouw van coaxkabel", "Van binnen naar buiten: binnengeleider, diëlektricum, afscherming en mantel.", b)


def swr_pijlen():
    w, h = 760, 230
    b = ARROW
    b += blok(20, 90, 130, 60, "zender")
    b += line(150, 120, 560, 120, "feed")
    b += line(560, 120, 560, 60, "feed") + line(560, 60, 560, 20, ANT) + line(560, 34, 544, 14, ANT) + line(560, 34, 576, 14, ANT)
    b += golfjes(575, 30, 3, 16, 14)
    b += f'<line x1="180" y1="90" x2="520" y2="90" class="dim" style="stroke-width:4" marker-end="url(#pijl)"/>'
    b += t(330, 76, "heengaand vermogen (naar de antenne)", "lbl b accent2", "middle")
    b += f'<line x1="520" y1="155" x2="300" y2="155" class="limit" style="stroke-width:3;stroke-dasharray:none" marker-end="url(#pijl)"/>'
    b += t(410, 182, "gereflecteerd vermogen (terug naar de zender)", "lbl b red", "middle")
    b += t(350, 138, "transmissielijn (coax)", "lbl s", "middle")
    b += t(380, 216, "Hoe meer er terugkomt, hoe hoger de SWR.", "lbl", "middle")
    return svg(w, h, "Heengaand en gereflecteerd vermogen", "Het vermogen gaat van de zender naar de antenne. Als de antenne niet goed past, komt een deel terug naar de zender.", b)


def swr_staand():
    w, h = 760, 230
    b = ARROW
    panelen = [("SWR = 1", 0.0), ("SWR = 2", 1 / 3), ("SWR = oneindig", 1.0)]
    for i, (n, gamma) in enumerate(panelen):
        x0, y0, pw, ph = 20 + i * 250, 30, 220, 150
        b += f'<rect x="{x0}" y="{y0}" width="{pw}" height="{ph}" class="cell"/>'
        b += t(x0 + 8, y0 + 18, "spanning", "lbl s")
        pts = []
        for k in range(101):
            u = k / 100
            v = abs(complex(math.cos(2 * math.pi * 1.5 * u), math.sin(2 * math.pi * 1.5 * u)) + gamma * complex(math.cos(-2 * math.pi * 1.5 * u), math.sin(-2 * math.pi * 1.5 * u)))
            pts.append((x0 + 10 + (pw - 20) * u, y0 + ph - 15 - (ph - 50) * v / 2))
        b += f'<path d="{path(pts)}" class="w-green"/>'
        b += t(x0 + pw / 2, y0 + ph + 26, n, "lbl b", "middle")
        b += t(x0 + pw / 2, y0 + ph + 44, "plaats op de kabel →", "lbl s", "middle")
    return svg(w, h, "Staande golf", "Spanning langs de kabel: vlak bij SWR 1, golvend bij SWR 2, volle bogen bij SWR oneindig.", b)


def atu():
    w, h = 760, 250
    b = ARROW
    b += blok(10, 120, 110, 56, "zender")
    b += line(120, 148, 160, 148, "feed")
    b += blok(160, 120, 110, 56, "SWR-|meter")
    b += line(270, 148, 310, 148, "feed")
    b += blok(310, 120, 100, 56, "ATU")
    b += line(410, 148, 640, 148, "feed")
    b += line(640, 148, 640, 90, "feed") + line(640, 90, 640, 40, ANT) + line(640, 56, 622, 34, ANT) + line(640, 56, 658, 34, ANT)
    b += maat(10, 410, 100, "SWR hier 1 : 1 (zender tevreden)")
    b += f'<line x1="412" y1="200" x2="640" y2="200" class="limit" marker-start="url(#pijl)" marker-end="url(#pijl)"/>'
    b += t(526, 226, "SWR hier blijft wat ze was", "lbl b red", "middle")
    b += t(526, 136, "coax", "lbl s", "middle")
    return svg(w, h, "ATU", "Zender, SWR-meter, ATU, coax en antenne. Tussen zender en ATU wordt de SWR 1 op 1, tussen ATU en antenne verandert er niets.", b)


def symmetrie():
    w, h = 760, 300
    b = ARROW
    # dipool
    b += t(190, 28, "symmetrisch", "lbl b green", "middle")
    b += line(40, 120, 180, 120, ANT) + line(200, 120, 340, 120, ANT)
    b += line(190, 60, 190, 180, "guide")
    b += t(110, 108, "helft 1", "lbl s", "middle") + t(270, 108, "helft 2", "lbl s", "middle")
    b += t(190, 210, "dipool, yagi:", "lbl b", "middle")
    b += t(190, 230, "links = spiegelbeeld van rechts", "lbl s", "middle")
    # gp
    b += t(570, 28, "asymmetrisch", "lbl b red", "middle")
    b += line(570, 50, 570, 140, ANT)
    b += f'<rect x="490" y="140" width="160" height="10" class="cell"/>'
    b += t(590, 80, "straler", "lbl s") + t(660, 150, "grondvlak", "lbl s")
    b += t(570, 210, "kwartgolf, groundplane, 5/8 λ,", "lbl b", "middle")
    b += t(570, 230, "langedraad: twee ongelijke delen", "lbl s", "middle")
    b += t(380, 280, "Coax is ook asymmetrisch: binnen een draad, buiten een buis.", "lbl b accent2", "middle")
    return svg(w, h, "Symmetrisch en asymmetrisch", "Links een dipool met twee gelijke helften, rechts een staaf met een grondvlak: twee verschillende delen.", b)


def balun():
    w, h = 760, 230
    b = ARROW
    b += blok(20, 120, 110, 56, "zender")
    b += line(130, 148, 330, 148, "feed")
    b += t(230, 136, "coax (asymmetrisch)", "lbl s", "middle")
    b += blok(330, 120, 100, 56, "balun")
    b += line(380, 120, 380, 70, "wire") + line(372, 120, 372, 70, "wire")
    b += line(80, 60, 372, 60, ANT) + line(380, 60, 680, 60, ANT)
    b += line(372, 70, 372, 60, "wire") + line(380, 70, 380, 60, "wire")
    b += t(380, 38, "dipool (symmetrisch)", "lbl b", "middle")
    b += t(460, 150, "balun = balanced → unbalanced", "lbl b accent2")
    b += t(460, 172, "voorkomt dat de buitenkant", "lbl s")
    b += t(460, 190, "van de coax meestraalt", "lbl s")
    return svg(w, h, "Balun", "Een coaxkabel gaat via een balun naar het midden van een dipool.", b)


def dummy():
    w, h = 760, 270
    b = ARROW
    b += blok(20, 30, 110, 56, "zender")
    b += line(130, 58, 260, 58, "feed")
    b += line(260, 58, 260, 20, ANT) + line(260, 34, 244, 14, ANT) + line(260, 34, 276, 14, ANT)
    b += golfjes(272, 30, 4, 16, 14)
    b += t(400, 64, "antenne: vermogen wordt uitgestraald", "lbl")
    b += line(20, 125, 740, 125, "guide2")
    b += blok(20, 160, 110, 56, "zender")
    b += line(130, 188, 260, 188, "feed")
    b += f'<rect x="260" y="150" width="120" height="76" rx="10" class="cell"/>'
    b += f'<rect x="290" y="179" width="60" height="18" class="sym"/>'
    b += line(260, 188, 290, 188, "wire") + line(350, 188, 365, 188, "wire")
    b += t(320, 244, "afgeschermde weerstand", "lbl s", "middle")
    for i in range(3):
        b += f'<path d="M{300+i*20},146 q-6,-10 0,-20 q6,-10 0,-20" class="w-red"/>'
    b += t(400, 182, "dummy load: vermogen wordt warmte,", "lbl")
    b += t(400, 204, "er gaat niets de lucht in", "lbl b")
    return svg(w, h, "Dummy load", "Boven: zender aan een antenne, er vertrekken radiogolven. Onder: zender aan een dummy load, het vermogen wordt warmte.", b)


def main():
    files = {"h05-omzetter": omzetter(), "h05-resonantie": resonantie(), "h05-grootte": grootte(), "h05-dipool": dipool(),
             "h05-antennes-abcd-1": abcd1(), "h05-antennes-abcd-2": abcd2(), "h05-kwartgolf": kwartgolf(),
             "h05-groundplane": groundplane(), "h05-58": vijfachtste(), "h05-langdraad": langdraad(), "h05-yagi": yagi(),
             "h05-straling": straling(), "h05-polarisatie": polarisatie(), "h05-erp": erp(), "h05-coax": coax(),
             "h05-swr": swr_pijlen(), "h05-swr-staand": swr_staand(), "h05-atu": atu(), "h05-symmetrie": symmetrie(),
             "h05-balun": balun(), "h05-dummyload": dummy()}
    for k, v in files.items():
        open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(v)
    print(len(files), "tekeningen")


if __name__ == "__main__":
    main()

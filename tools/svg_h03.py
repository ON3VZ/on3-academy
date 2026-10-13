"""Tekeningen hoofdstuk 3 (Basis elektriciteit). Schrijft naar assets/svg/.
Gebruikt de CSS-klassen van css/style.css zodat alles in licht en donker leesbaar is."""
import math, os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "svg")


def svg(w, h, title, desc, body):
    return (f'<svg class="fig" viewBox="0 0 {w} {h}" role="img" xmlns="http://www.w3.org/2000/svg">'
            f'<title>{title}</title><desc>{desc}</desc>{body}</svg>')


def t(x, y, s, cls="lbl", a="start"):
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{a}">{s}</text>'


def line(x1, y1, x2, y2, cls="wire"):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"/>'


def path(pts):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)


ARROW = ('<defs><marker id="pijl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
         '<path d="M0,0 L10,5 L0,10 z" class="dimhead"/></marker>'
         '<marker id="pijlas" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">'
         '<path d="M0,0 L10,5 L0,10 z" class="axhead"/></marker></defs>')

# ---------- symbolen (horizontaal, middelpunt cx,cy) ----------

def s_batterij(cx, cy, v=False):
    # lange streep = +, korte dikke = -
    return (line(cx - 40, cy, cx - 6, cy) + f'<line x1="{cx-6}" y1="{cy-26}" x2="{cx-6}" y2="{cy+26}" class="wire"/>'
            + f'<line x1="{cx+6}" y1="{cy-13}" x2="{cx+6}" y2="{cy+13}" class="wire thick"/>' + line(cx + 6, cy, cx + 40, cy))


def s_batterij_v(cx, cy):
    # verticaal: + boven
    return (line(cx, cy - 40, cx, cy - 6) + f'<line x1="{cx-26}" y1="{cy-6}" x2="{cx+26}" y2="{cy-6}" class="wire"/>'
            + f'<line x1="{cx-13}" y1="{cy+6}" x2="{cx+13}" y2="{cy+6}" class="wire thick"/>' + line(cx, cy + 6, cx, cy + 40))


def s_lamp(cx, cy):
    r = 18
    return (line(cx - 40, cy, cx - r, cy) + f'<circle cx="{cx}" cy="{cy}" r="{r}" class="sym"/>'
            + line(cx - 12.7, cy - 12.7, cx + 12.7, cy + 12.7) + line(cx - 12.7, cy + 12.7, cx + 12.7, cy - 12.7) + line(cx + r, cy, cx + 40, cy))


def s_weerstand(cx, cy):
    return line(cx - 40, cy, cx - 22, cy) + f'<rect x="{cx-22}" y="{cy-9}" width="44" height="18" class="sym"/>' + line(cx + 22, cy, cx + 40, cy)


def s_weerstand_v(cx, cy):
    return line(cx, cy - 40, cx, cy - 22) + f'<rect x="{cx-9}" y="{cy-22}" width="18" height="44" class="sym"/>' + line(cx, cy + 22, cx, cy + 40)


def s_zekering(cx, cy):
    return line(cx - 40, cy, cx + 40, cy) + f'<rect x="{cx-22}" y="{cy-9}" width="44" height="18" class="sym"/>'


def s_schakelaar(cx, cy):
    return (line(cx - 40, cy, cx - 20, cy) + f'<circle cx="{cx-16}" cy="{cy}" r="4" class="sym"/>'
            + line(cx - 16, cy, cx + 18, cy - 18) + f'<circle cx="{cx+18}" cy="{cy}" r="4" class="symfill"/>' + line(cx + 18, cy, cx + 40, cy))


def s_microfoon(cx, cy):
    return (f'<line x1="{cx-20}" y1="{cy-20}" x2="{cx-20}" y2="{cy+20}" class="wire"/>'
            + f'<circle cx="{cx-2}" cy="{cy}" r="18" class="sym"/>' + line(cx + 16, cy, cx + 40, cy))


def s_luidspreker(cx, cy):
    return (line(cx - 40, cy, cx - 16, cy) + f'<rect x="{cx-16}" y="{cy-12}" width="12" height="24" class="sym"/>'
            + f'<path d="M{cx-4},{cy-12} L{cx+14},{cy-26} L{cx+14},{cy+26} L{cx-4},{cy+12}" class="sym"/>')


def s_antenne(cx, cy):
    return line(cx, cy + 30, cx, cy - 26) + line(cx, cy + 4, cx - 18, cy - 26) + line(cx, cy + 4, cx + 18, cy - 26)


def s_aarding(cx, cy):
    return (line(cx, cy - 26, cx, cy) + line(cx - 20, cy, cx + 20, cy) + line(cx - 13, cy + 8, cx + 13, cy + 8) + line(cx - 6, cy + 16, cx + 6, cy + 16))


SYMBOLEN = [("batterij", s_batterij, "spanningsbron"), ("gloeilamp", s_lamp, ""), ("weerstand", s_weerstand, ""),
            ("zekering", s_zekering, "draad door het blokje"), ("schakelaar", s_schakelaar, "stroomonderbreker"),
            ("microfoon", s_microfoon, ""), ("luidspreker", s_luidspreker, ""), ("antenne", s_antenne, ""), ("aarding", s_aarding, "")]


def symbool_los(naam, f):
    return svg(160, 90, f"Symbool", "Een schemasymbool.", f(80, 45))


def symbolentabel():
    w, h = 760, 420
    b = ""
    for i, (naam, f, noot) in enumerate(SYMBOLEN):
        col, row = i % 3, i // 3
        x, y = 20 + col * 245, 15 + row * 135
        b += f'<rect x="{x}" y="{y}" width="230" height="120" rx="10" class="cell"/>'
        b += f(x + 115, y + 52)
        b += t(x + 115, y + 102, naam, "lbl b", "middle")
        if noot:
            b += t(x + 115, y + 117, noot, "lbl s", "middle")
    return svg(w, h, "De 9 te kennen symbolen", "Batterij, gloeilamp, weerstand, zekering, schakelaar, microfoon, luidspreker, antenne en aarding.", b)


def kring_zaklamp():
    w, h = 760, 300
    b = ARROW
    # rechthoekige kring: batterij links (verticaal), schakelaar boven, lamp rechts
    b += s_batterij_v(140, 150)
    b += line(140, 110, 140, 50) + line(140, 50, 320, 50)
    b += s_schakelaar(360, 50)
    b += line(400, 50, 560, 50) + line(560, 50, 560, 110)
    # lamp verticaal
    b += f'<circle cx="560" cy="150" r="20" class="sym"/>' + line(546, 136, 574, 164) + line(546, 164, 574, 136)
    b += line(560, 130, 560, 110) + line(560, 170, 560, 250) + line(560, 250, 140, 250) + line(140, 250, 140, 190)
    b += t(110, 140, "+", "lbl big", "middle") + t(110, 178, "−", "lbl big", "middle")
    b += t(186, 156, "batterij", "lbl b") + t(186, 176, "spanning U", "lbl s")
    b += t(360, 30, "schakelaar", "lbl b", "middle")
    b += t(596, 146, "lampje", "lbl b") + t(596, 166, "weerstand R", "lbl s")
    b += f'<line x1="250" y1="72" x2="310" y2="72" class="dim" marker-end="url(#pijl)"/>' + t(280, 92, "stroom I", "lbl s accent2", "middle")
    b += f'<line x1="430" y1="228" x2="370" y2="228" class="dim" marker-end="url(#pijl)"/>'
    b += t(650, 250, "gesloten kring:", "lbl s") + t(650, 268, "stroom loopt rond", "lbl s")
    return svg(w, h, "Zaklamp als schema", "Batterij, schakelaar en lampje in een gesloten kring. De stroom loopt van plus via schakelaar en lampje terug naar min.", b)


def schema_ur():
    # het schema uit de examenvragen: batterij + weerstand, met U en I
    w, h = 520, 300
    b = ARROW
    b += s_batterij_v(130, 150) + line(130, 110, 130, 50) + line(130, 50, 380, 50) + line(380, 50, 380, 110)
    b += s_weerstand_v(380, 150) + line(380, 190, 380, 250) + line(380, 250, 130, 250) + line(130, 250, 130, 190)
    b += t(100, 140, "+", "lbl big", "middle") + t(100, 176, "−", "lbl big", "middle")
    b += t(170, 156, "U", "lbl big") + t(170, 178, "spanning (V)", "lbl s")
    b += t(410, 156, "R", "lbl big") + t(410, 178, "weerstand (Ω)", "lbl s")
    b += f'<line x1="220" y1="72" x2="290" y2="72" class="dim" marker-end="url(#pijl)"/>' + t(255, 96, "I  stroom (A)", "lbl s accent2", "middle")
    b += t(255, 285, "P = vermogen dat de weerstand verbruikt (W)", "lbl s", "middle")
    return svg(w, h, "Schema batterij en weerstand", "Een batterij met spanning U is verbonden met een weerstand R. Er loopt een stroom I.", b)


def water():
    w, h = 760, 320
    b = ARROW
    # watertoren links, buis, vernauwing, kraan
    b += '<rect x="40" y="40" width="120" height="160" rx="8" class="tank"/>'
    b += '<rect x="44" y="80" width="112" height="116" rx="4" class="water"/>'
    b += t(100, 230, "watertoren", "lbl b", "middle") + t(100, 250, "hoogte = druk", "lbl s", "middle")
    b += '<path d="M160,170 L300,170 L330,182 L470,182 L500,170 L700,170" class="pipe"/>'
    b += '<path d="M160,196 L300,196 L330,186 L470,186 L500,196 L700,196" class="pipe"/>'
    b += f'<line x1="200" y1="183" x2="270" y2="183" class="flow" marker-end="url(#pijl)"/>'
    b += f'<line x1="540" y1="183" x2="640" y2="183" class="flow" marker-end="url(#pijl)"/>'
    b += t(400, 160, "smalle buis", "lbl b", "middle") + t(400, 214, "remt de stroom af", "lbl s", "middle")
    b += t(590, 160, "water stroomt", "lbl b", "middle")
    # vertaling
    rows = [("druk van het water", "spanning U", "volt (V)"), ("hoeveel water per seconde", "stroom I", "ampère (A)"), ("hoe smal de buis", "weerstand R", "ohm (Ω)")]
    y = 252
    for a, c, e in rows:
        b += t(260, y, a, "lbl s") + t(470, y, "→  " + c, "lbl b") + t(640, y, e, "lbl s mono")
        y += 22
    return svg(w, h, "Elektriciteit als water", "Een watertoren met een buis die op één plaats smal wordt. Druk is spanning, stroming is stroom, de smalle buis is weerstand.", b)


def driehoek(top, l, r, titel, desc):
    w, h = 760, 270
    b = ""
    def tri(x0, cover=None):
        s = f'<path d="M{x0+110},20 L{x0+210},200 L{x0+10},200 Z" class="tri"/>' + line(x0 + 55, 120, x0 + 165, 120, "triline") + line(x0 + 110, 120, x0 + 110, 200, "triline")
        s += t(x0 + 110, 98, top, "lbl trilbl" + (" dim2" if cover == "t" else ""), "middle")
        s += t(x0 + 65, 178, l, "lbl trilbl" + (" dim2" if cover == "l" else ""), "middle")
        s += t(x0 + 155, 178, r, "lbl trilbl" + (" dim2" if cover == "r" else ""), "middle")
        return s
    b += tri(10)
    b += t(120, 232, "de driehoek", "lbl b", "middle")
    # drie bedekte versies klein
    for i, (c, f) in enumerate([("t", f"{top} = {l} × {r}"), ("l", f"{l} = {top} ÷ {r}"), ("r", f"{r} = {top} ÷ {l}")]):
        x = 270 + i * 165
        rx, ry = {"t": (84, 58), "l": (39, 138), "r": (129, 138)}[c]
        b += f'<g transform="translate({x},40) scale(0.62)">{tri(0, c)}<rect x="{rx}" y="{ry}" width="52" height="50" rx="10" class="finger"/></g>'
        b += t(x + 68, 200, f, "lbl b mono", "middle")
    b += t(515, 240, "Leg je vinger op wat je zoekt. Wat overblijft, is de formule.", "lbl s", "middle")
    return svg(w, h, titel, desc, b)


def polariteit():
    w, h = 760, 260
    b = ""
    def kring(x, ding, omgekeerd, ok):
        s = f'<rect x="{x}" y="20" width="170" height="160" rx="10" class="cell"/>'
        s += line(x + 40, 60, x + 130, 60) + line(x + 40, 140, x + 130, 140)
        # batterij verticaal links
        s += line(x + 40, 60, x + 40, 92) + f'<line x1="{x+22}" y1="{92}" x2="{x+58}" y2="{92}" class="wire"/>'
        s += f'<line x1="{x+31}" y1="{104}" x2="{x+49}" y2="{104}" class="wire thick"/>' + line(x + 40, 104, x + 40, 140)
        s += t(x + 16, 90, "−" if omgekeerd else "+", "lbl b", "middle") + t(x + 16, 116, "+" if omgekeerd else "−", "lbl b", "middle")
        if ding == "lamp":
            s += line(x + 130, 60, x + 130, 82) + f'<circle cx="{x+130}" cy="100" r="18" class="sym"/>' + line(x + 117, 87, x + 143, 113) + line(x + 117, 113, x + 143, 87) + line(x + 130, 118, x + 130, 140)
        else:
            s += line(x + 130, 60, x + 130, 72) + f'<rect x="{x+104}" y="72" width="52" height="56" rx="6" class="sym"/>' + t(x + 130, 104, "radio", "lbl s", "middle") + line(x + 130, 128, x + 130, 140)
            s += t(x + 118, 86, "+", "lbl s", "middle")
        s += t(x + 85, 210, "werkt" if ok else "kapot mogelijk", "lbl b " + ("green" if ok else "red"), "middle")
        s += t(x + 85, 230, ("lamp" if ding == "lamp" else "radio") + (", omgekeerd" if omgekeerd else ""), "lbl s", "middle")
        return s
    b += kring(10, "lamp", False, True) + kring(200, "lamp", True, True) + kring(390, "radio", False, True) + kring(580, "radio", True, False)
    return svg(w, h, "Polariteit", "Een lamp brandt in beide richtingen. Een radio werkt maar in één richting en kan kapot gaan als je plus en min omwisselt.", b)


def ac_dc():
    w, h = 760, 250
    b = ARROW
    for x0, titel in ((40, "DC: gelijkspanning"), (420, "AC: wisselspanning")):
        b += f'<line x1="{x0}" y1="200" x2="{x0}" y2="30" class="axisline" marker-end="url(#pijlas)"/>'
        b += f'<line x1="{x0}" y1="120" x2="{x0+310}" y2="120" class="axisline" marker-end="url(#pijlas)"/>'
        b += t(x0 + 8, 36, "U", "lbl b") + t(x0 + 305, 140, "t", "lbl b", "end")
        b += t(x0 + 155, 235, titel, "lbl b", "middle")
    b += line(40, 70, 330, 70, "w-amber thickw") + t(60, 62, "altijd even groot, altijd +", "lbl s")
    pts = [(420 + i / 300 * 290, 120 - 60 * math.sin(2 * math.pi * 2 * i / 300)) for i in range(301)]
    b += f'<path d="{path(pts)}" class="w-amber thickw"/>' + t(450, 205, "wisselt telkens van + naar −", "lbl s")
    return svg(w, h, "DC en AC", "Links gelijkspanning: een rechte lijn boven nul. Rechts wisselspanning: een golf die boven en onder nul gaat.", b)


def sinus_voorbeeld():
    w, h = 760, 330
    x0, y0, W, A = 100, 165, 560, 110
    b = ARROW
    b += f'<line x1="{x0}" y1="{y0+A+30}" x2="{x0}" y2="{y0-A-30}" class="axisline" marker-end="url(#pijlas)"/>'
    b += f'<line x1="{x0}" y1="{y0}" x2="{x0+W+50}" y2="{y0}" class="axisline" marker-end="url(#pijlas)"/>'
    b += t(x0 - 10, y0 - A - 38, "spanning (V)", "lbl b") + t(x0 + W + 50, y0 - 12, "tijd (s)", "lbl b", "end")
    b += t(x0 - 10, y0 - A + 5, "+10", "lbl s mono", "end") + t(x0 - 10, y0 + 5, "0", "lbl s mono", "end") + t(x0 - 10, y0 + A + 5, "−10", "lbl s mono", "end")
    b += line(x0, y0 - A, x0 + W, y0 - A, "guide2") + line(x0, y0 + A, x0 + W, y0 + A, "guide2")
    # 2 perioden van 0,2 s => as tot 0,4 s
    pts = [(x0 + i / 600 * W, y0 - A * math.sin(2 * math.pi * 2 * i / 600)) for i in range(601)]
    b += f'<path d="{path(pts)}" class="w-amber thickw"/>'
    for k, lab in ((0.5, "0,2"), (1.0, "0,4")):
        b += line(x0 + k * W, y0 - 5, x0 + k * W, y0 + 5, "axisline") + t(x0 + k * W + 8, y0 + 20, lab + " s", "lbl s mono")
    xa = x0 + W / 8
    b += f'<line x1="{xa}" y1="{y0-4}" x2="{xa}" y2="{y0-A+4}" class="dim" marker-start="url(#pijl)" marker-end="url(#pijl)"/>'
    b += t(xa + 12, y0 - A / 2, "amplitude = 10 V", "lbl b accent2")
    yp = y0 + A + 24
    b += f'<line x1="{x0+3}" y1="{yp}" x2="{x0+W/2-3}" y2="{yp}" class="dim" marker-start="url(#pijl)" marker-end="url(#pijl)"/>'
    b += t(x0 + W / 4, yp + 22, "periode T = 0,2 s", "lbl b accent2", "middle")
    return svg(w, h, "Sinus met waarden", "Een sinus met amplitude 10 volt en periode 0,2 seconde. Er passen 5 perioden in één seconde: 5 hertz.", b)


def golfvormen_letters():
    w, h = 760, 200
    b = ""
    cells = []
    def cell(x, pts, letter):
        return f'<path d="{path(pts)}" class="w-amber thickw"/>' + line(x, 90, x + 170, 90, "axis") + t(x + 85, 185, letter, "lbl big", "middle")
    n = 200
    # A: vervormde golf (hobbel)
    A = [(15 + i / n * 170, 90 - 55 * (math.sin(2 * math.pi * i / n) + 0.35 * math.sin(4 * math.pi * i / n)) / 1.2) for i in range(n + 1)]
    B = [(205 + i / n * 170, 90 - 55 * abs(math.sin(2 * math.pi * i / n))) for i in range(n + 1)]
    Cc = [(395 + i / n * 170, 90 - 55 * math.sin(2 * math.pi * i / n)) for i in range(n + 1)]
    D = [(585, 140), (585, 35), (670, 35), (670, 145), (755, 145), (755, 35)]
    b += cell(15, A, "A") + cell(205, B, "B") + cell(395, Cc, "C") + cell(585, D, "D")
    return svg(w, h, "Vier golfvormen", "Vier golfvormen A, B, C en D. Alleen C is een zuivere sinus.", b)


def frequentieschaal():
    w, h = 760, 300
    import math as m
    def X(f):  # log schaal 10 Hz .. 10 GHz
        return 30 + (m.log10(f) - 1) / 9 * 700
    b = ARROW
    b += f'<line x1="30" y1="150" x2="740" y2="150" class="axisline" marker-end="url(#pijlas)"/>'
    for f, lab in ((10, "10 Hz"), (1e3, "1 kHz"), (1e6, "1 MHz"), (1e9, "1 GHz")):
        b += line(X(f), 145, X(f), 155, "axisline") + t(X(f), 172, lab, "lbl s mono", "middle")
    def band(f1, f2, y, hgt, cls, lab, sub=""):
        s = f'<rect x="{X(f1):.1f}" y="{y}" width="{X(f2)-X(f1):.1f}" height="{hgt}" rx="4" class="{cls}"/>'
        s += t((X(f1) + X(f2)) / 2, y + hgt / 2 + 5, lab, "lbl b", "middle")
        if sub:
            s += t((X(f1) + X(f2)) / 2, y - 6, sub, "lbl s mono", "middle")
        return s
    b += band(100, 15e3, 95, 36, "bandaf", "AF: hoorbaar", "100 Hz tot 15 kHz")
    b += band(300, 3e3, 40, 30, "bandsp", "spraak", "300 Hz tot 3 kHz")
    b += band(3e6, 30e6, 190, 36, "bandhf", "HF", "3 tot 30 MHz")
    b += band(30e6, 300e6, 190, 36, "bandvhf", "VHF", "")
    b += band(300e6, 3000e6, 190, 36, "banduhf", "UHF", "")
    b += t((X(30e6) + X(300e6)) / 2, 244, "30 tot 300 MHz", "lbl s mono", "middle")
    b += t((X(300e6) + X(3e9)) / 2, 262, "300 tot 3000 MHz", "lbl s mono", "middle")
    b += t(X(5e6), 290, "RF: radiofrequenties (vanaf ongeveer 10 kHz)", "lbl s", "middle")
    b += line(X(50), 140, X(50), 160, "dim") + t(X(50), 196, "lichtnet", "lbl s accent2", "middle") + t(X(50), 212, "50 Hz", "lbl s accent2", "middle")
    return svg(w, h, "Frequentieschaal", "Een schaal van laag naar hoog: lichtnet 50 hertz, hoorbaar geluid, spraak, en de radiobanden HF, VHF en UHF.", b)


def golflengte():
    w, h = 760, 260
    x0, y0, W, A = 40, 120, 680, 60
    b = ARROW
    pts = [(x0 + i / 600 * W, y0 - A * math.sin(2 * math.pi * 2 * i / 600 + math.pi / 2)) for i in range(601)]
    b += line(x0, y0, x0 + W, y0, "axis") + f'<path d="{path(pts)}" class="w-amber thickw"/>'
    b += line(x0, y0 - A, x0, y0 - A - 30, "guide") + line(x0 + W / 2, y0 - A, x0 + W / 2, y0 - A - 30, "guide")
    b += f'<line x1="{x0+3}" y1="{y0-A-22}" x2="{x0+W/2-3}" y2="{y0-A-22}" class="dim" marker-start="url(#pijl)" marker-end="url(#pijl)"/>'
    b += t(x0 + W / 4, y0 - A - 32, "golflengte λ (lambda), in meter", "lbl b accent2", "middle")
    b += t(x0, 225, "Horizontaal staat hier afstand, niet tijd: zo ver reist de golf tijdens één trilling.", "lbl s")
    b += t(x0, 246, "De golf reist altijd aan de lichtsnelheid: 300 000 km per seconde.", "lbl s")
    return svg(w, h, "Golflengte", "Een golf in de ruimte. De afstand tussen twee toppen is de golflengte lambda.", b)


def voorvoegsels():
    w, h = 760, 230
    b = ARROW
    stappen = [("m", "milli", "0,001"), ("", "basis", "1"), ("k", "kilo", "1 000"), ("M", "mega", "1 000 000")]
    for i, (s, n, v) in enumerate(stappen):
        x = 15 + i * 190
        b += f'<rect x="{x}" y="40" width="130" height="90" rx="10" class="cell"/>'
        b += t(x + 65, 82, s or "V, A, Ω, W", "lbl big" if s else "lbl b", "middle") + t(x + 65, 106, n, "lbl b", "middle") + t(x + 65, 124, "× " + v, "lbl s mono", "middle")
        if i < 3:
            b += f'<line x1="{x+134}" y1="66" x2="{x+186}" y2="66" class="dim" marker-end="url(#pijl)"/>' + t(x + 160, 56, "÷ 1000", "lbl s mono", "middle")
            b += f'<line x1="{x+186}" y1="106" x2="{x+134}" y2="106" class="dim" marker-end="url(#pijl)"/>' + t(x + 160, 126, "× 1000", "lbl s mono", "middle")
    b += t(380, 170, "Naar rechts (grotere eenheid): getal wordt kleiner, delen door 1000.", "lbl s", "middle")
    b += t(380, 192, "Naar links (kleinere eenheid): getal wordt groter, maal 1000.", "lbl s", "middle")
    b += t(380, 220, "Let op: kleine m = milli, grote M = mega. Een miljard keer verschil!", "lbl b red", "middle")
    return svg(w, h, "Voorvoegsels", "Een trap van milli naar basis naar kilo naar mega, telkens een factor 1000.", b)


def main():
    files = {
        "h03-kring-zaklamp": kring_zaklamp(), "h03-schema-ur": schema_ur(), "h03-water": water(),
        "h03-driehoek-ohm": driehoek("U", "I", "R", "Driehoek van Ohm", "Driehoek met U boven, I en R onder. Bedek wat je zoekt."),
        "h03-driehoek-p": driehoek("P", "U", "I", "Driehoek van vermogen", "Driehoek met P boven, U en I onder. Bedek wat je zoekt."),
        "h03-polariteit": polariteit(), "h03-ac-dc": ac_dc(), "h03-sinus-voorbeeld": sinus_voorbeeld(),
        "h03-golfvormen-letters": golfvormen_letters(), "h03-frequentieschaal": frequentieschaal(),
        "h03-golflengte": golflengte(), "h03-voorvoegsels": voorvoegsels(), "h03-symbolen": symbolentabel(),
    }
    for naam, f, _ in SYMBOLEN:
        files["sym-" + naam] = symbool_los(naam, f)
    for k, v in files.items():
        open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(v)
    print(len(files), "tekeningen")


if __name__ == "__main__":
    main()

"""Tekeningen hoofdstuk 7 (EMC). Schrijft naar assets/svg/."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg_h03 import svg, t, line, path, ARROW, OUT
from svg_h05 import blok, pijl, golfjes, grond

ANT = "ant"


def huis(x, y, w=200, h=150):
    return (f'<path d="M{x},{y} L{x+w/2},{y-60} L{x+w},{y}" class="sym"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="cell"/>')


def antenne(x, y):
    return line(x, y, x, y - 30, ANT) + line(x, y - 18, x - 12, y - 34, ANT) + line(x, y - 18, x + 12, y - 34, ANT)


def wegen():
    w, h = 760, 360
    b = ARROW
    # zendantenne links
    b += line(70, 300, 70, 110, "wire thick") + antenne(70, 110)
    b += golfjes(80, 90, 4, 16, 16)
    b += t(70, 325, "jouw zendantenne", "lbl s b", "middle")
    # huis buur
    b += huis(300, 150, 420, 170)
    b += t(510, 120, "huis van de buur", "lbl s", "middle")
    # toestellen
    b += blok(330, 230, 100, 50, "tv")
    b += blok(470, 230, 100, 50, "radio")
    b += blok(610, 230, 90, 50, "telefoon")
    # kabels
    b += line(380, 230, 380, 170, "wire") + antenne(380, 120).replace("ant", "wire") + line(380, 170, 380, 120, "wire")
    b += t(392, 165, "tv-antennekabel", "lbl s")
    b += line(520, 280, 520, 312, "wire") + line(520, 312, 640, 312, "wire") + t(580, 306, "luidspreker", "lbl s", "middle")
    b += line(655, 230, 655, 175, "wire") + line(655, 175, 715, 175, "wire") + t(700, 168, "telefoonlijn", "lbl s", "end")
    b += line(310, 300, 330, 280, "wire") + line(300, 300, 300, 320, "wire") + t(296, 336, "elektriciteitsnet", "lbl s", "end")
    # pijlen: opgepikt via draden
    b += f'<path d="M140,160 Q260,140 372,150" class="w-red" style="stroke-dasharray:6 5" marker-end="url(#pijl)"/>'
    b += f'<path d="M140,250 Q220,300 296,306" class="w-red" style="stroke-dasharray:6 5" marker-end="url(#pijl)"/>'
    b += f'<path d="M140,205 Q300,200 466,248" class="w-red" marker-end="url(#pijl)"/>'
    b += t(170, 236, "rechtstreeks (VHF/UHF)", "lbl s red")
    b += t(380, 30, "Draden die geen antenne zijn, pikken toch het signaal op", "lbl b", "middle")
    return svg(w, h, "Hoe storing binnenkomt", "Een zendantenne naast een huis. Het signaal komt binnen via de tv-antennekabel, het elektriciteitsnet, luidspreker- en telefoondraden, en op VHF en UHF ook rechtstreeks in het toestel.", b)


def plaats():
    w, h = 760, 320
    b = ARROW
    for k, (titel, goed) in enumerate([("meer kans op storing", False), ("minder kans op storing", True)]):
        x0 = 20 + k * 380
        b += t(x0 + 170, 28, titel, "lbl b " + ("green" if goed else "red"), "middle")
        b += line(x0, 280, x0 + 350, 280, "wire")
        b += huis(x0 + 20, 190, 130, 90)
        if not goed:
            b += line(x0 + 160, 280, x0 + 160, 170, "wire thick")
            b += line(x0 + 120, 205, x0 + 160, 170, ANT) + line(x0 + 160, 170, x0 + 330, 160, ANT)
            b += line(x0 + 330, 160, x0 + 330, 280, "wire thick")
            b += t(x0 + 245, 150, "eindgevoede draad", "lbl s", "middle")
            b += t(x0 + 245, 300, "laag, vlak bij het huis", "lbl s", "middle")
        else:
            b += line(x0 + 290, 280, x0 + 290, 70, "wire thick")
            b += line(x0 + 210, 70, x0 + 286, 70, ANT) + line(x0 + 294, 70, x0 + 345, 70, ANT)
            b += t(x0 + 270, 58, "dipool", "lbl s", "middle")
            b += t(x0 + 245, 300, "hoog, ver van het huis", "lbl s", "middle")
    return svg(w, h, "Plaats en soort antenne", "Links een eindgevoede draad laag naast het huis: meer kans op storing. Rechts een dipool hoog en verder weg: minder kans.", b)


def filter_plaats():
    w, h = 760, 260
    b = ARROW
    for k, (titel, goed) in enumerate([("FOUT", False), ("GOED", True)]):
        y = 70 + k * 110
        b += t(20, y - 30, titel, "lbl b " + ("green" if goed else "red"))
        b += f'<rect x="20" y="{y-20}" width="60" height="40" rx="6" class="cell"/>' + t(50, y + 5, "230 V", "lbl s", "middle")
        b += blok(600, y - 30, 140, 60, "gestoord|toestel")
        b += line(80, y, 600, y, "wire thick")
        fx = 110 if not goed else 520
        b += f'<rect x="{fx}" y="{y-16}" width="56" height="32" rx="5" class="box"/>' + t(fx + 28, y + 5, "filter", "lbl s b", "middle")
        if not goed:
            b += f'<path d="M260,{y-40} q20,-12 40,0 t40,0 t40,0" class="w-red"/>'
            b += t(370, y + 30, "het snoer na de filter pikt opnieuw signaal op", "lbl s red", "middle")
        else:
            b += t(330, y + 30, "filter zo dicht mogelijk bij het toestel", "lbl s green", "middle")
    b += t(50, y - 30 + 220, "stopcontact", "lbl s", "middle")
    return svg(w, h, "Waar zet je een filter", "Boven fout: filter bij het stopcontact. Onder goed: filter vlak bij het gestoorde toestel.", b)


def ferriet():
    w, h = 760, 240
    b = ARROW
    cx, cy = 230, 120
    b += f'<ellipse cx="{cx}" cy="{cy}" rx="70" ry="80" class="sym" style="stroke-width:26;stroke:var(--text3);opacity:.6"/>'
    # kabel enkele keren rond
    b += f'<path d="M20,{cy+40} C120,{cy+40} 150,{cy-70} {cx},{cy-60} C{cx+60},{cy-50} {cx+40},{cy+50} {cx},{cy+40} C{cx-40},{cy+30} {cx-30},{cy-40} {cx+10},{cy-30} C{cx+60},{cy-20} {cx+120},{cy+30} 460,{cy+30}" class="w-green" style="stroke-width:5"/>'
    b += t(cx, cy + 112, "ferrietring", "lbl b", "middle")
    b += t(20, cy + 64, "naar het stopcontact", "lbl s")
    b += t(460, cy + 54, "naar het toestel", "lbl s", "end")
    b += t(490, 60, "Kabel een paar keer door", "lbl")
    b += t(490, 82, "een ferrietring: dat werkt", "lbl")
    b += t(490, 104, "als smoorspoel.", "lbl")
    b += t(490, 134, "HF-stroom: afgeremd.", "lbl b")
    b += t(490, 156, "230 V of audio: gaat door.", "lbl b")
    b += t(490, 190, "Veilig: je knipt niets door.", "lbl b green")
    return svg(w, h, "Ferrietring", "Een kabel die enkele keren door een ferrietring is gewikkeld. Dat remt HF-stroom op de kabel af.", b)


def aarding():
    w, h = 760, 330
    b = ARROW
    b += line(20, 280, 740, 280, "wire")
    b += f'<rect x="20" y="280" width="720" height="40" class="cell"/>'
    b += t(40, 306, "aarde", "lbl s")
    b += f'<rect x="60" y="80" width="320" height="200" class="cell" style="opacity:.5"/>'
    b += t(220, 70, "shack", "lbl s", "middle")
    b += blok(120, 160, 140, 56, "zender")
    # goede RF-aarding: kort, dik, recht naar aardpen buiten
    b += line(260, 200, 420, 200, "wire thick") + line(420, 200, 420, 300, "wire thick")
    b += line(420, 280, 420, 315, "wire thick")
    b += f'<path d="M435,215 L435,268" class="w-green" style="stroke-width:3" marker-end="url(#pijl)"/>'
    b += t(458, 236, "eigen RF-aarding:", "lbl b green") + t(458, 256, "kort en dik naar een aardpen", "lbl s green")
    # lichtnet aarding
    b += line(160, 216, 160, 250, "wire") + line(160, 250, 80, 250, "wire") + f'<rect x="66" y="240" width="16" height="20" class="box"/>'
    b += t(90, 272, "stopcontact (aarding lichtnet)", "lbl s red")
    b += t(450, 100, "Zonder RF-aarding zoekt HF-stroom", "lbl")
    b += t(450, 122, "een weg via de aarding van het", "lbl")
    b += t(450, 144, "lichtnet, naar andere toestellen.", "lbl")
    return svg(w, h, "RF-aarding", "De zender heeft een eigen korte en dikke aardingsdraad naar een aardpen. Zo gaat HF-stroom niet via de aarding van het lichtnet.", b)


def stappen():
    w, h = 760, 430
    b = ARROW
    rijen = [("1", "Buur klaagt over storing", "rustig blijven, niet afwimpelen"),
             ("2", "Samen bekijken", "wanneer stoort het? bij welke band, welk vermogen?"),
             ("3", "Eerst je eigen station nakijken", "zie de pagina \"storing opsporen\""),
             ("4", "Hulp van de UBA-sectie", "ervaren radioamateurs in de buurt"),
             ("5", "EMC-commissie van de UBA", "specialisten, gratis advies"),
             ("6", "Klacht bij het BIPT", "formulier: klacht over storingen"),
             ("7", "NCS komt meten ter plaatse", "werkt je station volgens de regels? dan niets te vrezen")]
    for i, (n, a, s) in enumerate(rijen):
        y = 20 + i * 58
        b += f'<rect x="90" y="{y}" width="580" height="46" rx="10" class="box"/>'
        b += f'<circle cx="60" cy="{y+23}" r="18" class="sb"/>' + t(60, y + 29, n, "lbl b", "middle")
        b += t(110, y + 20, a, "lbl b") + t(110, y + 38, s, "lbl s")
    return svg(w, h, "Stappen bij een storingsklacht", "Zeven stappen van de klacht van de buur tot een controle door het NCS van het BIPT.", b)


def main():
    files = {"h07-wegen": wegen(), "h07-plaats": plaats(), "h07-filter": filter_plaats(), "h07-ferriet": ferriet(),
             "h07-aarding": aarding(), "h07-stappen": stappen()}
    for k, v in files.items():
        open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(v)
    print(len(files), "tekeningen")


if __name__ == "__main__":
    main()

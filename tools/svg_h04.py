"""Tekeningen hoofdstuk 4.3 (ontvanger). Schrijft naar assets/svg/."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg_h03 import svg, t, line, ARROW, OUT


def ant(x, y):  # antennesymbool, voet op (x,y)
    return line(x, y, x, y - 46, "ant") + line(x, y - 30, x - 16, y - 54, "ant") + line(x, y - 30, x + 16, y - 54, "ant")


def spk(x, y):  # luidspreker, ingang links op (x,y)
    return (f'<rect x="{x}" y="{y-11}" width="11" height="22" class="sym"/>'
            f'<path d="M{x+11},{y-11} L{x+28},{y-24} L{x+28},{y+24} L{x+11},{y+11}" class="sym"/>')


def blok(x, y, w, tekst, letter=None, h=70):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="box"/>'
    if letter:
        return s + t(x + w / 2, y + h / 2 + 9, letter, "lbl big", "middle")
    regels = tekst.split("|")
    y0 = y + h / 2 + 5 - (len(regels) - 1) * 9
    for i, r in enumerate(regels):
        s += t(x + w / 2, y0 + i * 18, r, "lbl b", "middle")
    return s


def ontvanger(letters=False):
    w, h = 760, 230
    y = 90
    b = ARROW
    b += ant(40, y + 35)
    b += f'<polyline points="40,{y+35} 40,{y+60} 120,{y+60} 120,{y+35} 130,{y+35}" class="feed"/>'
    b += blok(130, y, 160, "afstemming|+ RF-versterking", "C" if letters else None)
    b += f'<line x1="290" y1="{y+35}" x2="340" y2="{y+35}" class="arrow" marker-end="url(#pijl)"/>'
    b += blok(340, y, 150, "demodulator", "D" if letters else None)
    b += f'<line x1="490" y1="{y+35}" x2="540" y2="{y+35}" class="arrow" marker-end="url(#pijl)"/>'
    b += blok(540, y, 140, "audio-|versterker", "E" if letters else None)
    b += line(680, y + 35, 700, y + 35) + spk(700, y + 35)
    if letters:
        b += t(62, y - 30, "A", "lbl big") + t(80, y + 92, "B", "lbl big", "middle") + t(745, y + 10, "F", "lbl big", "end")
    else:
        b += t(62, y - 22, "antenne", "lbl b") + t(80, y + 92, "transmissielijn", "lbl b", "middle") + t(715, y - 12, "luidspreker", "lbl b", "middle")
        b += t(210, y + 118, "1e trap", "lbl s accent2", "middle") + t(415, y + 118, "2e trap", "lbl s accent2", "middle") + t(610, y + 118, "3e trap", "lbl s accent2", "middle")
        b += t(210, y + 136, "ingangstrap", "lbl s", "middle") + t(415, y + 136, "midden", "lbl s", "middle") + t(610, y + 136, "uitgangstrap", "lbl s", "middle")
    return svg(w, h, "Blokschema ontvanger", "Antenne, transmissielijn, afstemming en RF-versterking, demodulator, audioversterker, luidspreker.", b)


def spiegel():
    w, h = 760, 330
    b = ARROW
    # zender bovenaan, links naar rechts
    b += t(20, 30, "ZENDER", "lbl b accent2")
    b += blok(20, 45, 130, "microfoon-|versterker") + blok(190, 45, 130, "modulator") + blok(360, 45, 140, "RF-vermogen-|versterker")
    b += f'<line x1="150" y1="80" x2="188" y2="80" class="arrow" marker-end="url(#pijl)"/><line x1="320" y1="80" x2="358" y2="80" class="arrow" marker-end="url(#pijl)"/>'
    b += line(500, 80, 600, 80) + ant(600, 80) + t(590, 40, "antenne", "lbl s", "end")
    # golf
    b += '<path d="M650,50 q10,-10 20,0 t20,0 t20,0 t20,0" class="w-amber thickw"/>'
    b += t(690, 74, "radiogolf", "lbl s", "middle")
    # ontvanger onderaan, rechts naar links leesbaar maar zelfde volgorde gespiegeld
    b += t(20, 190, "ONTVANGER", "lbl b accent2")
    b += ant(600, 280) + line(600, 280, 500, 280) + t(590, 240, "antenne", "lbl s", "end")
    b += '<path d="M730,240 q-10,-10 -20,0 t-20,0 t-20,0 t-20,0" class="w-amber thickw"/>'
    b += blok(360, 245, 140, "afstemming|+ RF-versterking") + blok(190, 245, 130, "demodulator") + blok(20, 245, 130, "audio-|versterker")
    b += f'<line x1="358" y1="280" x2="322" y2="280" class="arrow" marker-end="url(#pijl)"/><line x1="188" y1="280" x2="152" y2="280" class="arrow" marker-end="url(#pijl)"/>'
    # spiegellijnen
    b += line(255, 117, 255, 243, "guide") + t(265, 182, "modulator ↔ demodulator: elkaars omgekeerde", "lbl s accent2")
    return svg(w, h, "Zender en ontvanger gespiegeld", "Bovenaan de zender, onderaan de ontvanger. De demodulator doet het omgekeerde van de modulator.", b)


def main():
    files = {"ontvanger": ontvanger(False), "ontvanger-letters": ontvanger(True), "zender-ontvanger": spiegel()}
    for k, v in files.items():
        open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(v)
    print(len(files), "tekeningen")


if __name__ == "__main__":
    main()

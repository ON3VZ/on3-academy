"""Tekeningen hoofdstuk 11 (Q-codes). Schrijft naar assets/svg/."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg_h03 import svg, t, line, ARROW, OUT
from svg_h05 import pijl


def vraagmed():
    w, h = 760, 250
    b = ARROW
    for k, (code, soort, vb, kl) in enumerate([("QRM ?", "VRAAG (met vraagteken)", "Heb je last van storing?", "accent2"),
                                              ("QRM", "MEDEDELING (zonder vraagteken)", "Ik heb last van storing.", "green")]):
        x = 20 + k * 380
        b += f'<rect x="{x}" y="20" width="340" height="210" rx="12" class="box"/>'
        b += t(x + 170, 62, soort, "lbl s b", "middle")
        b += f'<rect x="{x+90}" y="80" width="160" height="62" rx="10" class="sb"/>'
        b += t(x + 170, 123, code, "lbl big mono " + kl, "middle")
        b += t(x + 170, 180, "betekent:", "lbl s", "middle") + t(x + 170, 204, vb, "lbl b", "middle")
    return svg(w, h, "Vraag of mededeling", "Links QRM met vraagteken: heb je last van storing? Rechts QRM zonder vraagteken: ik heb last van storing.", b)


def gesprek():
    w, h = 760, 420
    b = ARROW
    regels = [("A", "CQ CQ CQ, dit is ON3AAA, QRZ?", "wie roept mij?"),
              ("B", "ON3AAA, dit is ON3BBB. Uw QTH?", "wat is uw locatie?"),
              ("A", "Mijn QTH is Gent. Mijn rapport voor u is 59.", "locatie en leesbaarheid"),
              ("B", "QSL, 59. Ik gebruik 25 W, QRP is het niet.", "ontvangst bevestigd"),
              ("A", "QRM hier, ik moet QSY naar 14,250.", "storing, andere frequentie"),
              ("B", "QSL. 73 en tot de volgende, ON3BBB uit.", "bevestigd, groeten")]
    for i, (wie, tekst, uitleg) in enumerate(regels):
        y = 15 + i * 66
        links = wie == "A"
        x = 20 if links else 140
        b += f'<rect x="{x}" y="{y}" width="600" height="54" rx="12" class="{"box" if links else "cell"}"/>'
        b += f'<circle cx="{x+26}" cy="{y+27}" r="16" class="sb"/>' + t(x + 26, y + 33, wie, "lbl b", "middle")
        b += t(x + 54, y + 24, tekst, "lbl b mono") + t(x + 54, y + 44, uitleg, "lbl s")
    return svg(w, h, "Voorbeeldgesprek met Q-codes", "Zes beurten tussen twee stations A en B met QRZ, QTH, QSL, QRP, QRM, QSY en 73, elk met uitleg.", b)


def main():
    files = {"h11-vraagmededeling": vraagmed(), "h11-gesprek": gesprek()}
    for k, v in files.items():
        open(os.path.join(OUT, k + ".svg"), "w", encoding="utf-8").write(v)
    print(len(files), "tekeningen")


if __name__ == "__main__":
    main()

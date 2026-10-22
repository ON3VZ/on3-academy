"""Maakt bandplan-tekeningen met legende (voor vragen): h08-bandplan-14-vol en h08-bandplan-144-vol, NL en FR.
Bron: de bestaande balk-SVG + de tabel uit de pagina's b04/b05 van hoofdstuk 8. Draai na svg_h08.py."""
import os, re, textwrap
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def schoon(g):
    # uitleg die het antwoord voorzegt weglaten: enkel wat in een bandplan staat
    g = re.sub(r"\s*\((hier|ici)[^)]*\)", "", g)
    g = re.sub(r"\s*:\s*(hier|ici)\b.*$", "", g)
    return re.sub(r"(\d) (\d{3})", "\\1\u00a0\\2", g)  # getallen niet afbreken
def rijen(md):
    out = []
    for l in open(md, encoding="utf-8"):
        m = re.match(r"^\| (\d+) \| ([^|]+) \| ([^|]+) \|", l)
        if m: out.append((m.group(1), m.group(2).strip(), schoon(re.sub(r"\*\*", "", m.group(3)).strip())))
    return out
def maak(svgpad, md, uitpad, voet):
    s = open(svgpad, encoding="utf-8").read()
    s = re.sub(r'<text[^>]*>[^<]*(kHz)[^<]*</text>', "", s, count=1)  # oude voetnoot weg
    y = 196; b = ""
    for nr, rng, gebruik in rijen(md):
        lijnen = textwrap.wrap(gebruik, 62) or [""]
        b += f'<circle cx="40" cy="{y-5}" r="10" class="sb"/><text x="40" y="{y}" class="lbl s b" text-anchor="middle">{nr}</text>'
        b += f'<text x="62" y="{y}" class="lbl s mono">{esc(rng)}</text>'
        for i, l in enumerate(lijnen):
            b += f'<text x="232" y="{y + i*18}" class="lbl s">{esc(l)}</text>'
        y += 18 * len(lijnen) + 10
    b += f'<text x="380" y="{y+8}" class="lbl s" text-anchor="middle">{esc(voet)}</text>'
    h = y + 20
    s = re.sub(r'viewBox="0 0 760 \d+"', f'viewBox="0 0 760 {h}"', s, count=1)
    s = s.replace("</svg>", b + "</svg>")
    open(uitpad, "w", encoding="utf-8").write(s)
for taal, map_, voet in [("nl", "", "frequenties in kHz, van laag naar hoog"), ("fr", "fr", "fréquences en kHz, du bas vers le haut")]:
    d = os.path.join(ROOT, "assets", "svg", map_)
    for naam, pag in [("h08-bandplan-14", "b04-bandplan-14"), ("h08-bandplan-144", "b05-bandplan-144")]:
        maak(os.path.join(d, naam + ".svg"), os.path.join(ROOT, "content", taal, "h08", pag + ".md"), os.path.join(d, naam + "-vol.svg"), voet)
print("ok")

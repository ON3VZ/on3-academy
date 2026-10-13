#!/usr/bin/env python3
"""Bouwt js/content.js uit content/ en data/.

Gebruik (in de map site/):  python3 tools/build.py

- content/<taal>/hoofdstukken.json, ui.json
- content/<taal>/<hoofdstuk>/hoofdstuk.json + pagina's als .md (front matter + Markdown of HTML)
- data/vragen-*.json
- assets/svg/*.svg worden inline gezet via {{svg:naam}} of {{svg:naam|onderschrift}}

Eigen blokken in Markdown:
    :::kern Titel          -> kader met groene bovenrand
    :::vergelijk Titel     -> kader met blauwe bovenrand
    :::valkuil Titel       -> kader met rode bovenrand
    :::formule             -> formulekader (regels = formules, laatste regel na '--' = legende)
    :::weetje              -> geen examenstof
    :::
De output werkt zowel via GitHub Pages als door index.html rechtstreeks te openen.
"""
import json, os, re, sys, hashlib

try:
    import markdown
except ImportError:
    sys.exit("Installeer eerst: pip install markdown")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TALEN = ["nl", "fr"]
BLOK = {"kern": ("card kern", "Kern"), "vergelijk": ("card ana", "Vergelijk met"),
        "valkuil": ("card trap", "Valkuil"), "geheugensteun": ("card kern", "Geheugensteun"),
        "weetje": ("card", "Weetje"), "tekst": ("card wettekst", "Zo staat het er"),
        "impact": ("card impact", "Wat betekent dit voor jou?"), "actueel": ("card actueel", "Actuele wet (stand oktober 2026)")}
BLOK_FR = {"kern": "L'essentiel", "vergelijk": "Comparaison", "valkuil": "Piège", "geheugensteun": "Aide-mémoire",
           "weetje": "Bon à savoir", "tekst": "Le texte dit", "impact": "Qu'est-ce que cela signifie pour vous ?", "actueel": "Loi actuelle (état octobre 2026)"}
TAAL = "nl"  # taal die nu gebouwd wordt


def svg(naam, onderschrift=""):
    p = os.path.join(ROOT, "assets", "svg", naam + ".svg")
    if TAAL != "nl" and os.path.exists(os.path.join(ROOT, "assets", "svg", TAAL, naam + ".svg")):
        p = os.path.join(ROOT, "assets", "svg", TAAL, naam + ".svg")
    if not os.path.exists(p):
        return f'<div class="card trap">Tekening ontbreekt: {naam}</div>'
    cap = f'<div class="figcap">{onderschrift}</div>' if onderschrift else ""
    return f'<div class="figwrap">{open(p, encoding="utf-8").read()}{cap}</div>'


def foto(naam, onderschrift=""):
    p = os.path.join(ROOT, "assets", "foto", naam)
    if not os.path.exists(p):
        return f'<div class="card trap">Foto ontbreekt: {naam}</div>'
    cap = f'<div class="figcap">{onderschrift}</div>' if onderschrift else ""
    return f'<div class="figwrap foto"><img src="assets/foto/{naam}" alt="{onderschrift or naam}" loading="lazy">{cap}</div>'


def blokken(md):
    out, i, lines = [], 0, md.split("\n")
    while i < len(lines):
        m = re.match(r"^:::(\w+)\s*(.*)$", lines[i].strip())
        if m and m.group(1) != "":
            soort, titel = m.group(1), m.group(2)
            body = []
            i += 1
            while i < len(lines) and lines[i].strip() != ":::":
                body.append(lines[i]); i += 1
            if soort == "formule":
                parts = "\n".join(body).split("\n--\n")
                f = "".join(f'<div class="f">{l.strip()}</div>' for l in parts[0].split("\n") if l.strip())
                leg = f'<div class="leg">{parts[1].strip()}</div>' if len(parts) > 1 else ""
                out.append(f'<div class="formula">{f}{leg}</div>')
            else:
                cls, std = BLOK.get(soort, ("card", soort))
                if TAAL == "fr":
                    std = BLOK_FR.get(soort, std)
                inner = markdown.markdown("\n".join(body), extensions=["tables"])
                out.append(f'<div class="{cls}"><b class="k">{titel or std}</b>{inner}</div>')
        else:
            out.append(lines[i])
        i += 1
    return "\n".join(out)


def lijsten(md):
    """python-markdown wil een lege regel voor een lijst; voeg die toe waar ze ontbreekt."""
    out = []
    for l in md.split("\n"):
        if re.match(r"^\s*(- |\d+\. )", l) and out and out[-1].strip() and not re.match(r"^\s*(- |\d+\. )", out[-1]) \
                and not out[-1].strip().startswith((":::", "<", "|")):
            out.append("")
        out.append(l)
    return "\n".join(out)


def lees_md(pad):
    t = open(pad, encoding="utf-8").read()
    meta, body = {}, t
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", t, re.S)
    if m:
        body = m.group(2)
        for line in m.group(1).split("\n"):
            if ":" in line:
                k, v = line.split(":", 1); v = v.strip()
                if v.startswith("[") and v.endswith("]"):
                    v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
                meta[k.strip()] = v
    body = lijsten(body)
    body = re.sub(r"\{\{svg:([\w-]+)(?:\|([^}]*))?\}\}", lambda m: svg(m.group(1), m.group(2) or ""), body)
    body = re.sub(r"\{\{foto:([\w.-]+)(?:\|([^}]*))?\}\}", lambda m: foto(m.group(1), m.group(2) or ""), body)
    body = blokken(body)
    html = markdown.markdown(body, extensions=["tables", "md_in_html"])
    html = html.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    html = re.sub(r'<a href="(https?://[^"]+)">', r'<a href="\1" target="_blank" rel="noopener">', html)
    return meta, html


def schud(q):
    """Eigen vragen: antwoordopties vast maar willekeurig ordenen (zaad = id), zodat het juiste antwoord niet altijd B is.
    Originele vragen blijven onaangeroerd."""
    import hashlib, random
    if len(q.get("opties", [])) != 4:
        return q
    r = random.Random(int(hashlib.md5(q["id"].encode()).hexdigest(), 16))
    orde = list(range(4)); r.shuffle(orde)
    L = "ABCD"
    oud_juist = L.index(q["juist"])
    q = dict(q)
    q["opties"] = [q["opties"][i] for i in orde]
    q["juist"] = L[orde.index(oud_juist)]
    wf = q.get("waarom_fout") or {}
    q["waarom_fout"] = {L[orde.index(L.index(k))]: v for k, v in wf.items()}
    for t in TALEN:
        if t in q and isinstance(q[t], dict):
            v = dict(q[t])
            if len(v.get("opties", [])) == 4:
                v["opties"] = [v["opties"][i] for i in orde]
            if v.get("waarom_fout"):
                v["waarom_fout"] = {L[orde.index(L.index(k))]: x for k, x in v["waarom_fout"].items()}
            q[t] = v
    return q


def main():
    global TAAL
    data = {"talen": {}, "vragen": {}, "svg": {}}
    for taal in TALEN:
        TAAL = taal
        base = os.path.join(ROOT, "content", taal)
        if not os.path.isdir(base):
            continue
        t = {"ui": {}, "hoofdstukken": [], "inhoud": {}}
        if os.path.exists(os.path.join(base, "ui.json")):
            t["ui"] = json.load(open(os.path.join(base, "ui.json"), encoding="utf-8"))
        hp = os.path.join(base, "hoofdstukken.json")
        if os.path.exists(hp):
            t["hoofdstukken"] = json.load(open(hp, encoding="utf-8"))
        for h in t["hoofdstukken"]:
            d = os.path.join(base, h["id"])
            if not os.path.isdir(d):
                continue
            meta = json.load(open(os.path.join(d, "hoofdstuk.json"), encoding="utf-8"))
            meta["pagina_inhoud"] = []
            for p in meta.get("paginas", []):
                m, html = lees_md(os.path.join(d, p + ".md"))
                m["html"] = html
                m["bestand"] = p
                meta["pagina_inhoud"].append(m)
            t["inhoud"][h["id"]] = meta
        data["talen"][taal] = t
    TAAL = "nl"
    vert = {}
    for t in TALEN:
        d = os.path.join(ROOT, "data", t)
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.endswith(".json"):
                    for v in json.load(open(os.path.join(d, f), encoding="utf-8")):
                        vert.setdefault(v["id"], {})[t] = {k: x for k, x in v.items() if k != "id"}
    for f in sorted(os.listdir(os.path.join(ROOT, "data"))):
        if f.endswith(".json"):
            for q in json.load(open(os.path.join(ROOT, "data", f), encoding="utf-8")):
                q.update(vert.get(q["id"], {}))
                if q.get("bron") in ("check", "extra"):
                    q = schud(q)
                data["vragen"][q["id"]] = q
    for f in os.listdir(os.path.join(ROOT, "assets", "svg")):
        if f.endswith(".svg"):
            data["svg"][f[:-4]] = open(os.path.join(ROOT, "assets", "svg", f), encoding="utf-8").read()
    for t in TALEN:
        d = os.path.join(ROOT, "assets", "svg", t)
        if t != "nl" and os.path.isdir(d):
            data["svg_" + t] = {f[:-4]: open(os.path.join(d, f), encoding="utf-8").read() for f in os.listdir(d) if f.endswith(".svg")}
    js = "window.ON3_CONTENT = " + json.dumps(data, ensure_ascii=False) + ";\n"
    open(os.path.join(ROOT, "js", "content.js"), "w", encoding="utf-8").write(js)

    # service worker cachelijst + versie
    files = ["./", "index.html", "css/style.css", "js/app.js", "js/omreken.js", "js/content.js", "manifest.webmanifest",
             "assets/icons/icon-192.png", "assets/icons/icon-512.png"]
    files += ["assets/foto/" + f for f in sorted(os.listdir(os.path.join(ROOT, "assets", "foto")))]
    m = hashlib.md5(js.encode())
    for f in files:
        if f not in ("./", "js/content.js"):
            m.update(open(os.path.join(ROOT, f), "rb").read())
    h = m.hexdigest()[:10]
    sw = open(os.path.join(ROOT, "tools", "sw.template.js"), encoding="utf-8").read()
    sw = sw.replace("__VERSIE__", h).replace("__FILES__", json.dumps(files))
    open(os.path.join(ROOT, "sw.js"), "w", encoding="utf-8").write(sw)
    print(f"content.js gebouwd: {len(data['vragen'])} vragen, {len(data['svg'])} tekeningen, versie {h}")


if __name__ == "__main__":
    main()

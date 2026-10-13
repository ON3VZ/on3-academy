/* Omrekentabel voor voorvoegsels (G M k basis m µ).
   Gebruik in een pagina:
   <div class="omreken" data-waarde="1" data-van="" data-naar="m" data-eenheid="V"></div>   (demo, aanpasbaar)
   <div class="omreken-oef" data-oef='[["4,7","k","","Ω"], ...]'></div>                     (oefeningen) */
(function () {
  "use strict";
  const PREF = [["G", 9], ["M", 6], ["k", 3], ["", 0], ["m", -3], ["µ", -6]];
  const FR = () => (document.documentElement.lang || "").startsWith("fr");
  const W = (nl, fr) => (FR() ? fr : nl);
  const NAAM = new Proxy({ G: "giga", M: "mega", k: "kilo", "": "basis", m: "milli", "µ": "micro" }, { get: (o, k) => (k === "" && FR() ? "base" : o[k]) });
  const POS = []; for (let p = 9; p >= -8; p--) POS.push(p); // 18 kolommen
  const expVan = (v) => PREF.find((x) => x[0] === v)[1];

  // exact getal: {d: "47", e: -1} betekent 47 × 10^-1
  function parse(s) {
    s = String(s).trim().replace(/\s/g, "").replace(".", ",");
    if (!/^\d+(,\d+)?$/.test(s)) return null;
    const [a, b = ""] = s.split(",");
    let d = (a + b).replace(/^0+/, "") || "0";
    let e = -b.length;
    while (d.length > 1 && d.endsWith("0")) { d = d.slice(0, -1); e++; }
    if (d === "0") e = 0;
    return { d, e };
  }
  function toStr(n) {
    if (n.d === "0") return "0";
    let s;
    if (n.e >= 0) s = n.d + "0".repeat(n.e);
    else {
      const k = -n.e;
      s = n.d.length > k ? n.d.slice(0, n.d.length - k) + "," + n.d.slice(n.d.length - k) : "0," + "0".repeat(k - n.d.length) + n.d;
    }
    // duizendtallen leesbaar maken (enkel voor het gehele deel)
    const [g, f] = s.split(",");
    const g2 = g.replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return f ? g2 + "," + f : g2;
  }
  const gelijk = (a, b) => a && b && a.d === b.d && a.e === b.e;
  const naarEenheid = (n, van, naar) => n.d === "0" ? n : { d: n.d, e: n.e + expVan(van) - expVan(naar) };

  function tabel(n, van, naar, eenheid) {
    // cijfers per macht van 10 (in basiseenheid)
    const p0 = n.e + expVan(van);
    const cijfer = {};
    for (let i = 0; i < n.d.length; i++) cijfer[p0 + (n.d.length - 1 - i)] = n.d[i];
    const hoog = p0 + n.d.length - 1, laag = p0;
    const pv = expVan(van), pn = expVan(naar);
    const vul = (p) => p <= Math.max(hoog, pv, pn) && p >= Math.min(laag, pv, pn);
    let kop = "", rij = "";
    PREF.forEach(([v]) => { kop += `<th colspan="3" class="${v === van ? "van" : ""} ${v === naar ? "naar" : ""}">${v || "E"}<small>${NAAM[v]}</small></th>`; });
    POS.forEach((p) => {
      let c = cijfer[p] !== undefined ? cijfer[p] : (vul(p) ? "0" : "");
      const groep = p % 3 === 0 ? " start" : "";
      const nKomma = p === pn ? `<span class="komma naar">,</span>` : "";
      const vKomma = p === pv && pv !== pn ? `<span class="komma van">,</span>` : "";
      rij += `<td class="${groep}${cijfer[p] !== undefined ? " cijfer" : ""}">${c}${nKomma}${vKomma}</td>`;
    });
    return `<div class="omr-leg"><span class="lv">${W("van", "de")}</span><span class="ln">${W("naar", "vers")}</span><span class="lk">${W(", nieuwe komma", ", nouvelle virgule")}</span><span class="lo">${W(", oude komma", ", ancienne virgule")}</span></div><div class="omr-scroll"><table class="omr"><tr>${kop}</tr><tr>${rij}</tr></table></div>`;
  }

  function uitleg(n, van, naar, eenheid) {
    const r = naarEenheid(n, van, naar), stap = expVan(van) - expVan(naar);
    if (FR()) {
      const r2 = stap > 0 ? `de ${stap} rangs vers la <b>droite</b> (unité plus petite : le nombre devient plus grand)` : stap < 0 ? `de ${-stap} rangs vers la <b>gauche</b> (unité plus grande : le nombre devient plus petit)` : "pas";
      return `<ol class="steps">
      <li><span>Placez <b>${toStr(n)}</b> dans le tableau : le dernier chiffre avant la virgule va dans la colonne <b>${van || "E"}</b> (${NAAM[van]}).</span></li>
      <li><span>Complétez les cases vides jusqu'à la colonne <b>${naar || "E"}</b> avec des zéros.</span></li>
      <li><span>Placez la virgule après la colonne <b>${naar || "E"}</b>. La virgule se déplace ${r2}.</span></li>
      <li><span>Lisez le résultat : <b>${toStr(n)} ${van}${eenheid} = ${toStr(r)} ${naar}${eenheid}</b></span></li></ol>`;
    }
    const richting = stap > 0 ? `${stap} plaatsen naar <b>rechts</b> (kleinere eenheid: getal wordt groter)` : stap < 0 ? `${-stap} plaatsen naar <b>links</b> (grotere eenheid: getal wordt kleiner)` : "niet";
    return `<ol class="steps">
      <li><span>Zet <b>${toStr(n)}</b> in de tabel: het laatste cijfer vóór de komma komt in de kolom <b>${van || "E"}</b> (${NAAM[van]}).</span></li>
      <li><span>Vul lege vakjes tot aan de kolom <b>${naar || "E"}</b> aan met nullen.</span></li>
      <li><span>Zet de komma achter de kolom <b>${naar || "E"}</b>. De komma schuift ${richting}.</span></li>
      <li><span>Lees af: <b>${toStr(n)} ${van}${eenheid} = ${toStr(r)} ${naar}${eenheid}</b></span></li></ol>`;
  }

  function demo(el) {
    const eenheid = el.dataset.eenheid || "V";
    const opts = (sel) => PREF.map(([v]) => `<option value="${v}" ${v === sel ? "selected" : ""}>${v}${eenheid}</option>`).join("");
    el.innerHTML = `<div class="omr-form"><label>${W("Getal", "Nombre")} <input type="text" inputmode="decimal" class="w" value="${el.dataset.waarde || "1"}"></label>
      <label>${W("van", "de")} <select class="v">${opts(el.dataset.van || "")}</select></label><label>${W("naar", "vers")} <select class="n">${opts(el.dataset.naar || "m")}</select></label></div>
      <div class="omr-out"></div>`;
    const teken = () => {
      const n = parse(el.querySelector(".w").value), v = el.querySelector(".v").value, t = el.querySelector(".n").value;
      const out = el.querySelector(".omr-out");
      if (!n) { out.innerHTML = `<p class="warn">${W("Typ een getal, bijvoorbeeld 4,7", "Tapez un nombre, par exemple 4,7")}</p>`; return; }
      out.innerHTML = tabel(n, v, t, eenheid) + `<div class="omr-res">${toStr(n)} ${v}${eenheid} = <b>${toStr(naarEenheid(n, v, t))} ${t}${eenheid}</b></div>` + uitleg(n, v, t, eenheid);
    };
    el.querySelectorAll("input,select").forEach((x) => x.addEventListener("input", teken));
    teken();
  }

  function oefeningen(el) {
    let lijst = [];
    try { lijst = JSON.parse(el.dataset.oef); } catch (e) { return; }
    el.innerHTML = "";
    lijst.forEach(([w, van, naar, eenheid], i) => {
      const n = parse(w), juist = naarEenheid(n, van, naar);
      const box = document.createElement("div"); box.className = "omr-oef";
      box.innerHTML = `<div class="omr-vraag"><span class="nr">${i + 1}</span> ${toStr(n)} ${van}${eenheid} = <input type="text" inputmode="decimal" aria-label="${W("antwoord", "réponse")}"> ${naar}${eenheid}
        <button class="btn">${W("Controleer", "Vérifier")}</button></div><div class="omr-fb"></div>`;
      const inp = box.querySelector("input"), fb = box.querySelector(".omr-fb");
      const check = () => {
        const a = parse(inp.value);
        const ok = gelijk(a, juist);
        box.classList.toggle("ok", ok); box.classList.toggle("bad", !ok);
        fb.innerHTML = (ok ? `<div class="verdict ok">${W("JUIST", "CORRECT")}</div>` : `<div class="verdict bad">${a ? W("NOG NIET", "PAS ENCORE") : W("TYP EEN GETAL", "TAPEZ UN NOMBRE")} · ${W("juist is", "la bonne réponse est")} ${toStr(juist)} ${naar}${eenheid}</div>`)
          + tabel(n, van, naar, eenheid) + (ok ? "" : uitleg(n, van, naar, eenheid));
        if (window.ON3_registreer) window.ON3_registreer("OMR-" + w + van + naar + eenheid, ok);
      };
      box.querySelector("button").onclick = check;
      inp.addEventListener("keydown", (e) => { if (e.key === "Enter") check(); });
      el.append(box);
    });
  }

  window.ON3_omreken = function (root) {
    root.querySelectorAll(".omreken").forEach(demo);
    root.querySelectorAll(".omreken-oef").forEach(oefeningen);
  };
  window.ON3_omreken_test = { parse, toStr, naarEenheid };
})();

/* ON3 Academy. Geen frameworks, geen build nodig behalve tools/build.py voor content.js */
(function () {
  "use strict";
  const C = window.ON3_CONTENT;
  const L = ["A", "B", "C", "D"];
  const KEY = "on3.v1";
  const EX_VERDELING = { techniek: 12, wetgeving: 10, procedures: 8 };
  const EX_MINUTEN = 60, EX_NORM = 24;

  /* ---------- opslag ---------- */
  const leeg = () => ({ taal: "nl", mode: "light", disc: null, bezocht: {}, antwoorden: {}, fouten: {}, examens: [], lopend: null });
  let S = leeg();
  try { const r = localStorage.getItem(KEY); if (r) S = Object.assign(leeg(), JSON.parse(r)); } catch (e) {}
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} };

  /* ---------- helpers ---------- */
  const $ = (s, r = document) => r.querySelector(s);
  const el = (tag, attrs = {}, html = "") => { const e = document.createElement(tag); for (const k in attrs) e.setAttribute(k, attrs[k]); if (html) e.innerHTML = html; return e; };
  const T = (k) => { const t = C.talen[S.taal] && C.talen[S.taal].ui[k]; return t || (C.talen.nl.ui[k] || k); };
  const taal = () => (C.talen[S.taal] && C.talen[S.taal].hoofdstukken.length ? C.talen[S.taal] : C.talen.nl);
  const Q = C.vragen;
  const bruikbaar = (id) => Q[id] && (Q[id].status || "ok") === "ok";
  const svg = (naam) => { if (!naam) return ""; const n = naam.replace(/\.svg$/, ""); return (S.taal !== "nl" && C["svg_" + S.taal] && C["svg_" + S.taal][n]) || C.svg[n] || ""; };
  const F = (k, o) => T(k).replace(/\{(\w+)\}/g, (m, x) => (o[x] !== undefined ? o[x] : m));
  const QT = (q) => (S.taal !== "nl" && q[S.taal]) ? Object.assign({}, q, q[S.taal]) : q;
  const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const toast = (msg) => { const t = el("div", { class: "toast" }, msg); document.body.append(t); setTimeout(() => t.remove(), 2600); };
  const kort = (id) => { const t = QT(Q[id]).vraag.replace(/<[^>]+>/g, ""); return t.length > 80 ? t.slice(0, 80) + "…" : t; };

  /* ---------- registratie antwoorden ---------- */
  function registreer(id, ok) {
    const a = S.antwoorden[id] || { pogingen: 0, reeks: 0 };
    a.pogingen++; a.laatst = ok ? "juist" : "fout"; a.reeks = ok ? a.reeks + 1 : 0;
    S.antwoorden[id] = a;
    if (!ok) { const f = S.fouten[id] || { fout: 0, moeilijk: false }; f.fout++; S.fouten[id] = f; }
    else if (S.fouten[id] && a.reeks >= 2) delete S.fouten[id];
    save(); smeter();
  }
  function smeter() {
    const alle = Object.keys(Q).filter(bruikbaar);
    const goed = alle.filter((id) => S.antwoorden[id] && S.antwoorden[id].laatst === "juist").length;
    const pct = alle.length ? goed / alle.length : 0;
    $("#sbar").style.width = Math.round(pct * 100) + "%";
    let s = "S" + Math.max(0, Math.min(9, Math.round((pct / 0.75) * 9)));
    if (pct >= 0.85) s = "S9+10"; if (pct >= 0.95) s = "S9+20";
    $("#sval").textContent = s;
  }

  /* ---------- vraagweergave ---------- */
  function renderVraag(id, holder, opt = {}) {
    if (!Q[id]) return; const q = QT(Q[id]);
    const box = el("div", { class: "q" });
    if (!opt.mode && S.antwoorden[id]) { const a = S.antwoorden[id]; box.append(el("div", { class: "vorig " + (a.laatst === "juist" ? "ok" : "bad") }, F(a.laatst === "juist" ? "vk_juist" : "vk_fout", { n: a.pogingen }))); }
    if (opt.nummer) box.append(el("div", { class: "meta" }, `<span>${opt.nummer} / ${opt.totaal || ""}</span>`));
    box.append(el("div", { class: "txt" }, q.vraag));
    if (q.svg) { const f = el("div", { class: "figwrap" }); f.innerHTML = svg(q.svg); box.append(f); }
    if (q.foto) { const f = el("div", { class: "figwrap foto" }); f.innerHTML = `<img src="assets/foto/${q.foto}" alt="${T("foto_alt")}" loading="lazy">`; box.append(f); }
    const uitleg = el("div", { class: "expl" });
    const knoppen = q.opties.map((o, i) => {
      const b = el("button", { class: "opt" }, `<span class="l">${L[i]}</span><span>${o}</span>`);
      box.append(b); return b;
    });
    const toonUitleg = (gekozen) => {
      const juistI = L.indexOf(q.juist), ok = gekozen === juistI;
      knoppen.forEach((k, j) => { k.disabled = true; if (j === juistI) k.classList.add("ok"); if (j === gekozen && !ok) k.classList.add("bad"); });
      let h = `<div class="verdict ${ok ? "ok" : "bad"}">${gekozen === null ? "" : (ok ? T("juist") : T("fout")) + " · "}${T("juist_is")} ${q.juist}</div>`;
      if (q.uitleg) h += `<p>${q.uitleg}</p>`;
      if (q.waarom_fout) { h += "<ul>"; for (const k of L) if (q.waarom_fout[k]) h += `<li><b>${k}</b>: ${q.waarom_fout[k]}</li>`; h += "</ul>"; }
      uitleg.innerHTML = h;
      if (opt.mode !== "review") {
        const rb = el("button", { class: "btn flagbtn" }, T("opnieuw"));
        rb.onclick = () => { const nieuw = el("div"); box.replaceWith(nieuw); renderVraag(id, nieuw, opt); nieuw.replaceWith(...nieuw.childNodes); };
        uitleg.append(rb);
        const fb = el("button", { class: "btn flagbtn" }, T("markeer"));
        fb.onclick = () => { const f = S.fouten[id] || { fout: 0, moeilijk: false }; f.moeilijk = true; S.fouten[id] = f; if (S.antwoorden[id]) S.antwoorden[id].reeks = 0; save(); fb.textContent = T("gemarkeerd"); fb.disabled = true; };
        uitleg.append(fb);
      }
      uitleg.classList.add("show");
    };
    if (opt.mode === "examen") {
      knoppen.forEach((b, i) => {
        if (opt.gekozen === i) b.classList.add("sel");
        b.onclick = () => { knoppen.forEach((k) => k.classList.remove("sel")); b.classList.add("sel"); opt.onKies && opt.onKies(i); };
      });
    } else if (opt.mode === "review") {
      toonUitleg(opt.gekozen === undefined ? null : opt.gekozen);
    } else {
      knoppen.forEach((b, i) => b.onclick = () => { const ok = L[i] === q.juist; registreer(id, ok); toonUitleg(i); opt.onAntwoord && opt.onAntwoord(ok); });
    }
    box.append(uitleg); holder.append(box);
  }

  /* ---------- hoofdstukdata ---------- */
  function hoofdstukVragen(hid) {
    const h = taal().inhoud[hid]; if (!h) return [];
    const ids = [];
    h.pagina_inhoud.forEach((p) => [].concat(p.checkvragen || [], p.examenvragen || []).forEach((i) => ids.push(i)));
    Object.values(Q).filter((q) => q.bron === "extra" && q.id.startsWith("E-" + hid)).forEach((q) => ids.push(q.id));
    return [...new Set(ids)].filter(bruikbaar);
  }
  function hoofdstukStats(hid) {
    const ids = hoofdstukVragen(hid);
    const gedaan = ids.filter((i) => S.antwoorden[i]).length, goed = ids.filter((i) => S.antwoorden[i] && S.antwoorden[i].laatst === "juist").length;
    return { totaal: ids.length, gedaan, goed, pct: ids.length ? Math.round((goed / ids.length) * 100) : 0 };
  }

  /* ---------- pagina's ---------- */
  const app = $("#app");
  function nav(n) { document.querySelectorAll(".topnav a").forEach((a) => a.classList.toggle("on", a.dataset.nav === n)); }

  /* ---------- installeren als app ---------- */
  let uitnodiging = null;
  window.addEventListener("beforeinstallprompt", (e) => { e.preventDefault(); uitnodiging = e; const k = document.getElementById("instKnop"); if (k) k.classList.remove("hidden"); });
  window.addEventListener("appinstalled", () => { uitnodiging = null; const k = document.getElementById("instKaart"); if (k) k.remove(); });
  const alApp = () => (window.matchMedia && matchMedia("(display-mode: standalone)").matches) || navigator.standalone === true;
  function installKaart() {
    if (alApp()) return null;
    const ua = navigator.userAgent || "";
    const ios = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
    const android = /Android/.test(ua);
    let uitleg;
    if (ios) uitleg = `<p>${T("inst_ios")}</p>`;
    else if (android) uitleg = `<p>${T("inst_android")}</p>`;
    else uitleg = `<p>${T("inst_desktop")}</p><p>${T("inst_ff")}</p>`;
    const k = el("div", { class: "card impact", id: "instKaart" },
      `<h3 style="margin-top:0">${T("inst_titel")}</h3><p>${T("inst_intro")}</p>` +
      `<p><button class="btn pri hidden" id="instKnop">${T("inst_knop")}</button></p>${uitleg}<p class="offl" id="offStatus"></p>`);
    setTimeout(() => {
      const kn = k.querySelector("#instKnop");
      if (uitnodiging) kn.classList.remove("hidden");
      kn.onclick = () => { if (uitnodiging) { uitnodiging.prompt(); uitnodiging.userChoice.then(() => { uitnodiging = null; kn.classList.add("hidden"); }); } };
      const st = k.querySelector("#offStatus");
      if (!("serviceWorker" in navigator) || !location.protocol.startsWith("http")) { st.textContent = T("inst_nee"); return; }
      st.textContent = T("inst_bezig");
      navigator.serviceWorker.ready.then(() => caches.keys()).then((ks) => { st.textContent = ks.length ? T("inst_ok") : T("inst_bezig"); st.classList.toggle("ok", ks.length > 0); }).catch(() => { st.textContent = T("inst_nee"); });
    }, 0);
    return k;
  }

  function frMelding() {
    const m = el("div", { class: "modal" }, `<div class="box"><h2>${T("fr_titel")}</h2><div class="disc-big"><p style="margin:0">${T("fr_melding")}</p></div><p style="margin-top:18px"><button class="btn pri">${T("fr_ok")}</button></p></div>`);
    m.querySelector("button").onclick = () => { S.frGezien = true; save(); m.remove(); };
    document.body.append(m);
  }

  function home() {
    nav("home");
    app.innerHTML = `<div class="hero"><div class="eyebrow">${T("home_eyebrow")}</div><h1>${T("home_titel")}</h1><p style="color:var(--head-text);margin:0">${T("home_intro")}</p></div>`;
    if (S.taal === "fr") app.append(el("div", { class: "card impact" }, `<h3 style="margin-top:0">${T("fr_titel")}</h3><p>${T("fr_melding")}</p>`));
    const ik = installKaart(); if (ik) app.append(ik);
    const grid = el("div", { class: "chapters" });
    taal().hoofdstukken.forEach((h) => {
      if (h.info) { grid.append(el("div", { class: "chap off info" }, `<div class="band">${h.band ? h.band + " · " : ""}${T("hfst")} ${h.nummer}</div><h3>${h.titel}</h3><p>${h.ondertitel}</p><div class="meta"><span class="tag">${T("zie_handboek")}</span></div>`)); return; }
      const st = h.beschikbaar ? hoofdstukStats(h.id) : null;
      const a = el("a", { class: "chap" + (h.beschikbaar ? "" : " off"), href: `#/h/${h.id}` },
        `<div class="band">${h.band ? h.band + " · " : ""}${h.nummer ? T("hfst") + " " + h.nummer : ""}</div><h3>${h.titel}</h3><p>${h.ondertitel}</p>` +
        (st ? `<div class="bar"><i style="width:${st.pct}%"></i></div><div class="meta"><span>${st.goed} / ${st.totaal} ${T("juist_kort")}</span></div>`
            : `<div class="meta"><span class="tag">${T("binnenkort")}</span></div>`));
      grid.append(a);
    });
    app.append(grid);
  }

  function hoofdstuk(hid, pi) {
    nav(hid === "h15" ? "wet" : "home");
    const meta = taal().hoofdstukken.find((h) => h.id === hid), h = taal().inhoud[hid];
    if (!meta || !h) { app.innerHTML = `<div class="card">${T("binnenkort")}</div>`; return; }
    const opPagina = new Set([].concat(...h.pagina_inhoud.map((p) => [].concat(p.checkvragen || [], p.examenvragen || []))));
    const extra = Object.values(Q).filter((q) => q.bron === "extra" && q.id.startsWith("E-" + hid) && bruikbaar(q.id) && !opPagina.has(q.id)).map((q) => q.id);
    const paginas = [{ id: "start", kort: T("starten") }].concat(h.pagina_inhoud.map((p) => ({ id: p.bestand, kort: p.kort, p })), [{ id: "herhaling", kort: T("herhaling") }]);
    if (extra.length) paginas.push({ id: "extra", kort: T("extra_titel") });
    paginas.push({ id: "score", kort: T("score_titel") });
    pi = Math.max(0, Math.min(paginas.length - 1, pi || 0));
    const cur = paginas[pi];
    S.bezocht[hid + "/" + cur.id] = true; save();

    const klaar = (pg) => {
      if (!pg.p) return !!S.bezocht[hid + "/" + pg.id];
      const ids = [].concat(pg.p.checkvragen || [], pg.p.examenvragen || []).filter(bruikbaar);
      return ids.length ? ids.every((i) => S.antwoorden[i]) : !!S.bezocht[hid + "/" + pg.id];
    };
    const nKlaar = paginas.filter(klaar).length, pct = Math.round((nKlaar / paginas.length) * 100);
    const deelKop = (p, i) => (p.p && p.p.deel && (i === 0 || !paginas[i - 1].p || paginas[i - 1].p.deel !== p.p.deel)) ? `<li class="deel">${p.p.deel}</li>` : "";
    const lijst = paginas.map((p, i) => deelKop(p, i) + `<li class="${i === pi ? "cur" : ""} ${klaar(p) ? "done" : ""}"><a href="#/h/${hid}/${i}"><span class="nr">${i === 0 ? "•" : i}</span>${p.kort}${klaar(p) ? ' <span class="ok">✓</span>' : ""}</a></li>`).join("");
    app.innerHTML = `<nav class="crumbs"><a href="#/">${T("nav_home")}</a><span>›</span><a href="#/h/${hid}/0">${meta.nummer ? T("Hfst") + " " + meta.nummer + " " : ""}${meta.titel}</a><span>›</span><b>${cur.kort}</b></nav>
      <div class="hero compact"><div class="eyebrow">${[meta.nummer ? T("Hfst") + " " + meta.nummer : T("starten"), meta.band].filter(Boolean).join(" · ")}</div><h1>${meta.titel}</h1>
      <details class="paglijst"><summary>${F("pagina_van", { i: pi + 1, n: paginas.length })}: <b>${cur.kort}</b> <span class="toon">${T("alle_paginas")} ▾</span></summary><ol>${lijst}</ol></details>
      <div class="prog"><span>${nKlaar} / ${paginas.length} ${T("klaar_kort")}</span><div class="track"><div class="fill" style="width:${pct}%"></div></div><span>${pct} %</span></div></div>`;
    const art = el("div", { class: "article" }); app.append(art);

    if (cur.id === "start") {
      art.innerHTML = `<div class="card kern"><b class="k">${T("leerdoelen")}</b><ol class="steps">${h.leerdoelen.map((l) => `<li><span>${l}</span></li>`).join("")}</ol></div>
        <div class="toc"><span class="lbl-mono">${T("in_hoofdstuk")}</span><ol>${paginas.slice(1).map((p, i) => deelKop(p, i + 1) + `<li><a href="#/h/${hid}/${i + 1}">${p.kort}</a></li>`).join("")}</ol></div>`;
    } else if (cur.p) {
      art.innerHTML = `<div class="eyebrow">${cur.p.deel ? cur.p.deel + " · " : ""}${cur.p.type === "brokje" ? T("blok") : cur.p.kort}</div><h2>${cur.p.titel}</h2>` + cur.p.html;
      const chk = (cur.p.checkvragen || []).filter(bruikbaar), ex = (cur.p.examenvragen || []).filter(bruikbaar);
      if (window.ON3_omreken) window.ON3_omreken(art);
      if (chk.length || ex.length) {
        const s = el("div", { class: "qset" });
        const teken = () => { s.innerHTML = `<div class="qhead">${T("check")} <button class="btn klein" id="allesopnieuw">${T("alles_opnieuw")}</button></div>`; chk.concat(ex).forEach((i) => renderVraag(i, s)); $("#allesopnieuw", s).onclick = () => { teken(); s.scrollIntoView({ behavior: "smooth" }); }; };
        teken(); art.append(s);
      }
    } else if (cur.id === "herhaling") {
      art.innerHTML = `<div class="eyebrow">${T("herhaling")}</div><h2>${T("flashcards")}</h2><div class="fc-grid"></div>
        <div class="card kern" style="margin-top:20px"><b class="k">${T("vijf_zinnen")}</b><ol class="steps">${(h.samenvatting || []).map((l) => `<li><span>${l}</span></li>`).join("")}</ol></div>`;
      const g = $(".fc-grid", art);
      (h.flashcards || []).forEach((f) => { const c = el("div", { class: "fc" }, `<div class="in"><div class="side front">${f.voor}</div><div class="side back">${f.achter}</div></div>`); c.onclick = () => c.classList.toggle("flip"); g.append(c); });
    } else if (cur.id === "extra") {
      art.innerHTML = `<div class="eyebrow">${T("oefenen")}</div><h2>${T("extra_titel")}</h2><p class="ref">${T("extra_info")}</p>`;
      const s = el("div", { class: "qset" });
      const teken = () => { s.innerHTML = `<div class="qhead"><button class="btn klein" id="allesopnieuw">${T("alles_opnieuw")}</button></div>`; extra.forEach((i) => renderVraag(i, s)); $("#allesopnieuw", s).onclick = teken; };
      teken(); art.append(s);
    } else if (cur.id === "score") {
      scorePagina(art, hid, paginas);
    }
    const pager = el("nav", { class: "pager" });
    const pv = el("button", { class: "prev" }, `<small>${T("vorige")}</small><span>${pi > 0 ? "← " + paginas[pi - 1].kort : ""}</span>`);
    const nx = el("button", { class: "next" }, `<small>${T("volgende")}</small><span>${pi < paginas.length - 1 ? paginas[pi + 1].kort + " →" : ""}</span>`);
    if (pi === 0) pv.disabled = true;
    pv.onclick = () => go(`#/h/${hid}/${pi - 1}`);
    if (pi === paginas.length - 1) { nx.innerHTML = `<small>${T("klaar")}</small><span>${T("nav_home")} →</span>`; nx.onclick = () => go("#/"); }
    else nx.onclick = () => go(`#/h/${hid}/${pi + 1}`);
    pager.append(pv, nx); art.append(pager);
    window.scrollTo(0, 0);
  }

  function scorePagina(art, hid, paginas) {
    art.innerHTML = `<div class="eyebrow">${T("sk_eyebrow")}</div><h2>${T("sk_titel")}</h2><div class="card" id="rows"></div>
      <div class="eyebrow" style="margin-top:30px">Quiz</div><h2>${F("quiz_titel", { n: Math.min(10, hoofdstukVragen(hid).filter((i) => !i.startsWith("C-")).length || hoofdstukVragen(hid).length) })}</h2>
      <div class="disc-big">${T("ex_disc")}</div><p><button class="btn pri" id="qs">${T("quiz_start")}</button></p><div id="qb"></div>
      <div class="eyebrow" style="margin-top:30px">${T("hr_eyebrow")}</div><p class="ref">${T("hr_info")}</p><p><button class="btn" id="hreset">${T("hr_knop")}</button></p>`;
    $("#hreset", art).onclick = () => { if (!confirm(T("hr_bevestig"))) return; hoofdstukVragen(hid).forEach((i) => { delete S.antwoorden[i]; delete S.fouten[i]; }); save(); smeter(); toast(T("hr_toast")); hoofdstuk(hid, paginas.length - 1); };
    const rows = $("#rows", art);
    paginas.forEach((pg) => {
      if (!pg.p) return; const ids = [].concat(pg.p.checkvragen || [], pg.p.examenvragen || []).filter(bruikbaar); if (!ids.length) return;
      const d = ids.filter((i) => S.antwoorden[i]), g = d.filter((i) => S.antwoorden[i].laatst === "juist").length;
      rows.append(el("div", { class: "score-row" }, `<span>${pg.kort}</span><span>${g} / ${ids.length} ${T("juist_kort")}${d.length < ids.length ? " · " + (ids.length - d.length) + " " + T("open") : ""}</span>`));
    });
    $("#qs", art).onclick = () => {
      let pool = shuffle(hoofdstukVragen(hid).filter((i) => !i.startsWith("C-"))).slice(0, 10); if (!pool.length) pool = shuffle(hoofdstukVragen(hid)).slice(0, 10);
      const box = $("#qb", art); let i = 0, goed = 0; const fout = [];
      const volgende = () => {
        box.innerHTML = "";
        if (i >= pool.length) { box.append(qsl(goed, pool.length, T("Hfst").toUpperCase() + " " + hid.slice(1), fout)); return; }
        box.append(el("div", { class: "ref" }, `${i + 1} / ${pool.length}`)); const h = el("div"); box.append(h);
        renderVraag(pool[i], h, { onAntwoord: (ok) => { if (ok) goed++; else fout.push(pool[i]); const b = el("button", { class: "btn pri" }, i + 1 < pool.length ? T("volgende") : T("toon_resultaat")); b.onclick = () => { i++; volgende(); }; box.append(b); } });
      };
      volgende();
    };
  }

  function qsl(goed, totaal, label, fout, extraRows = "") {
    const pct = Math.round((goed / totaal) * 100);
    return el("div", { class: "qsl" }, `<div class="hd"><span>${T("qsl_kop")}</span><span>${label}</span></div><div class="big">${goed} / ${totaal}</div>
      <table><tr><td>score</td><td>${pct} %</td></tr><tr><td>${T("qsl_norm")}</td><td>80 % · ${pct >= 80 ? T("ex_geslaagd") : T("ex_niet")}</td></tr>
      <tr><td>${T("qsl_rapport")}</td><td>${pct >= 80 ? T("qsl_59") : pct >= 60 ? T("qsl_57") : T("qsl_33")}</td></tr>${extraRows}</table>
      <p>${fout.length ? F("qsl_fout", { n: fout.length }) : T("qsl_geen")}</p>`);
  }


  /* ---------- oefenen per hoofdstuk ---------- */
  const OEF_N = [10, 20, 30, 0]; // 0 = alle
  const oefS = () => { S.oefen = S.oefen || { best: {}, n: 10, lopend: null, laatste: null }; return S.oefen; };
  const kleur = (pct) => pct === undefined ? "grijs" : pct >= 80 ? "groen" : pct >= 60 ? "oranje" : "rood";
  function oefenen() {
    nav("oefenen"); clearInterval(timerH);
    const O = oefS();
    if (O.lopend) return oefenBezig();
    const hs = taal().hoofdstukken.filter((h) => h.beschikbaar && !h.info && h.id !== "h00").map((h) => ({ h, ids: hoofdstukVragen(h.id) })).filter((x) => x.ids.length);
    const geslaagd = hs.filter((x) => (O.best[x.h.id] || 0) >= 80).length;
    app.innerHTML = `<div class="hero compact"><div class="eyebrow">${T("oef_eyebrow")}</div><h1>${T("oef_titel")}</h1></div><div class="article" id="oa"></div>`;
    const a = $("#oa");
    if (O.laatste) {
      const L = O.laatste, pct = Math.round((L.goed / L.totaal) * 100), meta = hs.find((x) => x.h.id === L.hid);
      const kaart = qsl(L.goed, L.totaal, (meta ? meta.h.titel : L.hid).toUpperCase(), L.ids.filter((id) => L.keuze[id] === undefined || "ABCD"[L.keuze[id]] !== Q[id].juist), `<tr><td>${T("oef_best")}</td><td>${O.best[L.hid]} %</td></tr>`);
      kaart.querySelector("p").innerHTML += L.nieuwRecord ? ` <b>${T("oef_record")}</b>` : "";
      a.append(kaart);
      const d = el("details", { class: "nakijk" }, `<summary>${T("ex_nakijken")}</summary>`);
      const s = el("div", { class: "qset" }); L.ids.forEach((id, i) => renderVraag(id, s, { mode: "review", nummer: i + 1, totaal: L.ids.length, gekozen: L.keuze[id] }));
      d.append(s); a.append(d);
      const rb = el("div", { class: "row" });
      const zelf = el("button", { class: "btn pri" }, T("oef_zelfde")); zelf.onclick = () => oefenStart(L.hid);
      const sluit = el("button", { class: "btn" }, T("oef_sluit")); sluit.onclick = () => { O.laatste = null; save(); oefenen(); };
      rb.append(zelf, sluit); a.append(rb);
    }
    a.append(el("p", { class: "ref" }, T("oef_info")));
    a.append(el("div", { class: "oef-samen" }, F("oef_samen", { g: geslaagd, n: hs.length })));
    const keuze = el("div", { class: "oef-n" }, `<span class="lbl-mono">${T("oef_aantal")}</span>` + OEF_N.map((n) => `<button class="btn klein ${O.n === n ? "on" : ""}" data-n="${n}">${n || T("oef_alle")}</button>`).join(""));
    keuze.querySelectorAll("button").forEach((b) => b.onclick = () => { O.n = +b.dataset.n; save(); oefenen(); });
    a.append(keuze);
    const lijst = el("div", { class: "oef-lijst" });
    hs.forEach(({ h, ids }) => {
      const pct = O.best[h.id], k = kleur(pct);
      const n = O.n ? Math.min(O.n, ids.length) : ids.length;
      const r = el("button", { class: "oef-rij " + k }, `<span class="t"><b>${h.nummer ? T("Hfst") + " " + h.nummer + " · " : ""}${h.titel}</b><small>${F("oef_vragen", { n: ids.length })}</small></span>
        <span class="bar"><i style="width:${pct || 0}%"></i><em></em></span><span class="pct">${pct === undefined ? "-" : pct + " %"}</span><span class="go">${F("oef_start", { n })}</span>`);
      r.onclick = () => oefenStart(h.id);
      lijst.append(r);
    });
    a.append(lijst);
    a.append(el("p", { class: "ref" }, T("oef_legende")));
  }
  function oefenStart(hid) {
    const O = oefS(), alle = shuffle(hoofdstukVragen(hid));
    const ids = O.n ? alle.slice(0, Math.min(O.n, alle.length)) : alle;
    O.laatste = null; O.lopend = { hid, ids, keuze: {}, cur: 0 }; save(); oefenBezig();
  }
  function oefenBezig() {
    const O = oefS(), E = O.lopend, meta = taal().hoofdstukken.find((h) => h.id === E.hid) || { titel: E.hid };
    window.scrollTo(0, 0);
    app.innerHTML = `<div class="exbar"><span><b>${meta.titel}</b></span><span class="ref">${Object.keys(E.keuze).length} / ${E.ids.length} ${T("beantwoord")}</span><button class="btn" id="ostop">${T("oef_stop")}</button></div>
      <div class="qnav">${E.ids.map((id, i) => `<button class="${E.keuze[id] !== undefined ? "ans" : ""} ${i === E.cur ? "cur" : ""}" data-i="${i}">${i + 1}</button>`).join("")}</div><div id="eq"></div>
      <nav class="pager"><button class="prev" id="ep"><small>${T("vorige")}</small><span>←</span></button><button class="next" id="en"><small>${T("volgende")}</small><span>→</span></button></nav>`;
    const id = E.ids[E.cur];
    renderVraag(id, $("#eq"), { mode: "examen", nummer: E.cur + 1, totaal: E.ids.length, gekozen: E.keuze[id], onKies: (i) => { E.keuze[id] = i; save(); oefenBezig(); } });
    app.querySelectorAll(".qnav button").forEach((b) => b.onclick = () => { E.cur = +b.dataset.i; save(); oefenBezig(); });
    $("#ep").disabled = E.cur === 0; $("#ep").onclick = () => { E.cur--; save(); oefenBezig(); };
    if (E.cur === E.ids.length - 1) {
      const open = E.ids.length - Object.keys(E.keuze).length;
      $("#en").innerHTML = `<small>${open ? F("ex_open", { n: open }) : T("ex_alles")}</small><span>${T("oef_klaar")} ✓</span>`;
      $("#en").classList.add("indienen");
      $("#en").onclick = () => { if (!open || confirm(T("ex_bevestig"))) oefenKlaar(); };
    } else $("#en").onclick = () => { E.cur++; save(); oefenBezig(); };
    $("#ostop").onclick = () => { if (confirm(T("oef_stop_ok"))) { O.lopend = null; save(); oefenen(); } };
  }
  function oefenKlaar() {
    const O = oefS(), E = O.lopend; if (!E) return;
    let goed = 0;
    E.ids.forEach((id) => { const ok = E.keuze[id] !== undefined && L[E.keuze[id]] === Q[id].juist; if (ok) goed++; registreer(id, ok); });
    const pct = Math.round((goed / E.ids.length) * 100);
    const nieuw = O.best[E.hid] === undefined || pct > O.best[E.hid];
    if (nieuw) O.best[E.hid] = pct;
    O.laatste = { hid: E.hid, ids: E.ids, keuze: E.keuze, goed, totaal: E.ids.length, nieuwRecord: nieuw };
    O.lopend = null; save(); oefenen();
  }
  /* ---------- foutenlog ---------- */
  function fouten() {
    nav("fouten");
    const ids = Object.keys(S.fouten).filter(bruikbaar);
    app.innerHTML = `<div class="hero compact"><div class="eyebrow">${T("nav_fouten")}</div><h1>${T("fouten_titel")}</h1></div><div class="article" id="fa"></div>`;
    const a = $("#fa");
    if (!ids.length) { a.innerHTML = `<p>${T("fouten_leeg")}</p>`; return; }
    a.innerHTML = `<p class="ref">${T("fouten_info")}</p><ul class="list-plain">${ids.map((id) => `<li>${kort(id)} <span style="color:var(--red)">${S.fouten[id].fout ? F("x_fout", { n: S.fouten[id].fout }) : ""}${S.fouten[id].moeilijk ? " · " + T("moeilijk") : ""}</span></li>`).join("")}</ul>
      <p><button class="btn pri" id="fo">${T("fouten_oefen")}</button></p><div class="qset" id="fs"></div>`;
    $("#fo").onclick = () => { const s = $("#fs"); s.innerHTML = ""; shuffle(ids).forEach((i) => renderVraag(i, s)); };
  }

  /* ---------- proefexamen ---------- */
  function examenPool() {
    const per = {};
    Object.values(Q).forEach((q) => { if ((q.bron === "origineel" || q.bron === "extra") && bruikbaar(q.id) && q.in_examen !== false && q.examendeel) (per[q.examendeel] = per[q.examendeel] || []).push(q.id); });
    let ids = [];
    for (const d in EX_VERDELING) {
      const n = EX_VERDELING[d], alle = per[d] || [];
      const orig = shuffle(alle.filter((i) => Q[i].bron === "origineel")), extra = shuffle(alle.filter((i) => Q[i].bron !== "origineel"));
      const nOrig = Math.min(orig.length, Math.max(Math.ceil(n / 2), Math.round(n * orig.length / Math.max(1, orig.length + extra.length)), n - extra.length));
      ids = ids.concat(orig.slice(0, nOrig), extra.slice(0, n - nOrig));
    }
    return shuffle(ids);
  }
  let timerH = null;
  function examen() {
    nav("examen"); clearInterval(timerH);
    if (S.lopend) return examenBezig();
    app.innerHTML = `<div class="hero compact"><div class="eyebrow">${T("ex_eyebrow")}</div><h1>${T("ex_titel")}</h1></div>
      <div class="article"><p>${T("ex_info")}</p><div class="disc-big">${T("ex_disc")}</div><p><button class="btn pri" id="es">${T("ex_start")}</button></p>
      <h3>${T("ex_historiek")}</h3><div id="eh"></div></div>`;
    $("#eh").innerHTML = S.examens.length ? `<ul class="list-plain">${S.examens.slice().reverse().map((e) => `<li>${new Date(e.datum).toLocaleString(S.taal === "fr" ? "fr-BE" : "nl-BE")} · <b>${e.score} / ${e.totaal}</b> · ${e.score >= EX_NORM ? T("ex_geslaagd") : T("ex_niet")} · ${T("d_techniek")} ${e.per_deel.techniek || 0}/12 · ${T("d_wetgeving")} ${e.per_deel.wetgeving || 0}/10 · ${T("d_procedures")} ${e.per_deel.procedures || 0}/8</li>`).join("")}</ul>` : `<p class="ref">${T("ex_geen")}</p>`;
    $("#es").onclick = () => { const ids = examenPool(); S.lopend = { ids, keuze: {}, start: Date.now(), cur: 0 }; save(); examenBezig(); };
  }
  function examenBezig() {
    const E = S.lopend;
    const tekenen = () => {
      clearInterval(timerH);
      app.innerHTML = `<div class="exbar"><span class="timer" id="tm"></span><span class="ref">${Object.keys(E.keuze).length} / ${E.ids.length} ${T("beantwoord")}</span><button class="btn" id="ind">${T("ex_stop")}</button></div>
        <div class="qnav">${E.ids.map((id, i) => `<button class="${E.keuze[id] !== undefined ? "ans" : ""} ${i === E.cur ? "cur" : ""}" data-i="${i}">${i + 1}</button>`).join("")}</div><div id="eq"></div>
        <nav class="pager"><button class="prev" id="ep"><small>${T("vorige")}</small><span>←</span></button><button class="next" id="en"><small>${T("volgende")}</small><span>→</span></button></nav>`;
      const id = E.ids[E.cur];
      renderVraag(id, $("#eq"), { mode: "examen", nummer: E.cur + 1, totaal: E.ids.length, gekozen: E.keuze[id], onKies: (i) => { E.keuze[id] = i; save(); tekenen(); } });
      app.querySelectorAll(".qnav button").forEach((b) => b.onclick = () => { E.cur = +b.dataset.i; save(); tekenen(); });
      $("#ep").disabled = E.cur === 0;
      $("#ep").onclick = () => { E.cur--; save(); tekenen(); };
      if (E.cur === E.ids.length - 1) {
        // laatste vraag: "Volgende" wordt "Examen indienen"
        const open = E.ids.length - Object.keys(E.keuze).length;
        $("#en").innerHTML = `<small>${open ? F("ex_open", { n: open }) : T("ex_alles")}</small><span>${T("ex_stop")} ✓</span>`;
        $("#en").classList.add("indienen");
        $("#en").onclick = () => { if (confirm(open ? T("ex_bevestig") : T("ex_bevestig_ok"))) examenKlaar(); };
      } else $("#en").onclick = () => { E.cur++; save(); tekenen(); };
      $("#ind").onclick = () => { if (confirm(T("ex_bevestig"))) examenKlaar(); };
      const tik = () => { const rest = E.start + EX_MINUTEN * 60000 - Date.now(); if (rest <= 0) { examenKlaar(); return; } const m = Math.floor(rest / 60000), s = Math.floor((rest % 60000) / 1000); const t = $("#tm"); if (t) { t.textContent = `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`; t.classList.toggle("low", rest < 5 * 60000); } };
      tik(); timerH = setInterval(tik, 1000);
    };
    tekenen();
  }
  function examenKlaar() {
    clearInterval(timerH);
    const E = S.lopend; if (!E) return;
    let goed = 0; const per = {}, fout = [];
    E.ids.forEach((id) => { const ok = E.keuze[id] !== undefined && L[E.keuze[id]] === Q[id].juist; if (ok) { goed++; per[Q[id].examendeel] = (per[Q[id].examendeel] || 0) + 1; } else fout.push(id); registreer(id, ok); });
    S.examens.push({ datum: Date.now(), score: goed, totaal: E.ids.length, per_deel: per, fout });
    S.lopend = null; save();
    app.innerHTML = `<div class="hero compact"><div class="eyebrow">${T("ex_titel")}</div><h1>${goed >= EX_NORM ? T("ex_geslaagd") : T("ex_niet")}</h1></div><div class="article" id="er"></div>`;
    const a = $("#er");
    a.append(qsl(goed, E.ids.length, T("ex_titel").toUpperCase(), fout, `<tr><td>${T("d_techniek")}</td><td>${per.techniek || 0} / 12</td></tr><tr><td>${T("d_wetgeving")}</td><td>${per.wetgeving || 0} / 10</td></tr><tr><td>${T("d_procedures")}</td><td>${per.procedures || 0} / 8</td></tr>`));
    a.append(el("div", { class: "disc-big" }, T("ex_disc")));
    a.append(el("h3", {}, T("ex_nakijken")));
    const s = el("div", { class: "qset" }); E.ids.forEach((id, i) => renderVraag(id, s, { mode: "review", nummer: i + 1, totaal: E.ids.length, gekozen: E.keuze[id] })); a.append(s);
    window.scrollTo(0, 0);
  }

  /* ---------- voortgang ---------- */
  function voortgang() {
    nav("voortgang");
    app.innerHTML = `<div class="hero compact"><div class="eyebrow">${T("nav_voortgang")}</div><h1>${T("vg_titel")}</h1></div><div class="article" id="va"></div>`;
    const a = $("#va");
    const rows = taal().hoofdstukken.filter((h) => h.beschikbaar && !h.info).map((h) => { const s = hoofdstukStats(h.id); return `<div class="score-row"><span>${h.titel}</span><span>${s.goed} / ${s.totaal} ${T("juist_kort")} · ${s.pct} %</span></div>`; }).join("");
    const ex = S.examens.length ? Math.max(...S.examens.map((e) => e.score)) : null;
    a.innerHTML = `<div class="stats"><div class="stat"><div class="n">${Object.keys(S.antwoorden).length}</div><div class="c">${T("vg_beantwoord")}</div></div>
      <div class="stat"><div class="n">${Object.keys(S.fouten).length}</div><div class="c">${T("vg_infout")}</div></div>
      <div class="stat"><div class="n">${S.examens.length}</div><div class="c">${T("vg_examens")}</div></div>
      <div class="stat"><div class="n">${ex === null ? "-" : ex + "/30"}</div><div class="c">${T("vg_beste")}</div></div></div>
      <div class="card">${rows}</div>
      <p class="ref">${T("vg_info")}</p>
      <div class="row"><button class="btn" id="vx">${T("vg_export")}</button><label class="btn">${T("vg_import")}<input type="file" id="vi" accept=".json" hidden></label><button class="btn" id="vf">${T("vg_fwis")}</button><button class="btn" id="ve">${T("vg_ewis")}</button><button class="btn" id="vr">${T("vg_reset")}</button></div>`;
    $("#vf").onclick = () => { if (confirm(T("vg_fwis_ok"))) { S.fouten = {}; save(); voortgang(); toast(T("vg_fwis_toast")); } };
    $("#ve").onclick = () => { if (confirm(T("vg_ewis_ok"))) { S.examens = []; S.lopend = null; save(); voortgang(); toast(T("vg_ewis_toast")); } };
    $("#vx").onclick = () => { const b = new Blob([JSON.stringify(S, null, 1)], { type: "application/json" }); const u = URL.createObjectURL(b); const l = el("a", { href: u, download: "on3-voortgang.json" }); document.body.append(l); l.click(); l.remove(); URL.revokeObjectURL(u); };
    $("#vi").onchange = (e) => { const f = e.target.files[0]; if (!f) return; f.text().then((t) => { try { S = Object.assign(leeg(), JSON.parse(t)); save(); smeter(); voortgang(); toast(T("vg_in_toast")); } catch (x) { toast(T("vg_in_fout")); } }); };
    $("#vr").onclick = () => { if (confirm(T("vg_reset_ok"))) { const keep = { taal: S.taal, mode: S.mode, disc: S.disc }; S = Object.assign(leeg(), keep); save(); smeter(); voortgang(); } };
  }

  /* ---------- router ---------- */
  function go(h) { if (location.hash === h) route(); else location.hash = h; }
  function route() {
    clearInterval(timerH);
    const p = location.hash.replace(/^#\/?/, "").split("/");
    if (p[0] === "h" && p[1]) hoofdstuk(p[1], parseInt(p[2] || "0", 10));
    else if (p[0] === "examen") examen();
    else if (p[0] === "oefenen") oefenen();
    else if (p[0] === "fouten") fouten();
    else if (p[0] === "voortgang") voortgang();
    else home();
  }

  /* ---------- init ---------- */
  function vertaalStatisch() { document.querySelectorAll("[data-t]").forEach((e) => e.innerHTML = T(e.dataset.t)); document.documentElement.lang = S.taal === "fr" ? "fr-BE" : "nl-BE"; }
  document.documentElement.dataset.mode = S.mode;
  $("#themeBtn").onclick = () => { S.mode = S.mode === "dark" ? "light" : "dark"; document.documentElement.dataset.mode = S.mode; save(); };
  document.querySelectorAll(".lang button").forEach((b) => b.onclick = () => {
    if (b.dataset.l === "fr" && !(C.talen.fr && C.talen.fr.hoofdstukken.length)) { toast(T("fr_toast")); return; }
    S.taal = b.dataset.l; save(); document.querySelectorAll(".lang button").forEach((x) => x.classList.toggle("on", x === b)); vertaalStatisch(); route();
    if (S.taal === "fr" && !S.frGezien) frMelding();
  });
  document.querySelectorAll(".lang button").forEach((x) => x.classList.toggle("on", x.dataset.l === S.taal));
  vertaalStatisch();
  if (!S.disc) $("#discModal").classList.remove("hidden");
  $("#discOk").onclick = () => { S.disc = new Date().toISOString(); save(); $("#discModal").classList.add("hidden"); if (S.taal === "fr" && !S.frGezien) frMelding(); };
  if (S.disc && S.taal === "fr" && !S.frGezien) frMelding();
  window.addEventListener("hashchange", route);
  smeter(); route();
  if ("serviceWorker" in navigator && location.protocol.startsWith("http")) navigator.serviceWorker.register("sw.js").catch(() => {});
})();

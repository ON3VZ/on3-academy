// Service worker: maakt de site offline bruikbaar. Gegenereerd door tools/build.py
const VERSIE = "on3-__VERSIE__";
const FILES = __FILES__;
self.addEventListener("install", e => {
  e.waitUntil(caches.open(VERSIE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSIE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  e.respondWith(
    caches.match(e.request, {ignoreSearch: true}).then(r => r || fetch(e.request).then(resp => {
      const kopie = resp.clone();
      const u = new URL(e.request.url); if ((resp.ok || resp.type === "opaque") && (u.origin === location.origin || u.host.startsWith("fonts."))) caches.open(VERSIE).then(c => c.put(e.request, kopie));
      return resp;
    }).catch(() => caches.match("index.html")))
  );
});

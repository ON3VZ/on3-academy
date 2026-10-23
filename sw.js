// Service worker: maakt de site offline bruikbaar. Gegenereerd door tools/build.py
const VERSIE = "on3-c38350506c";
const FILES = ["./", "index.html", "css/style.css", "js/app.js", "js/omreken.js", "js/content.js", "manifest.webmanifest", "assets/icons/icon-192.png", "assets/icons/icon-512.png", "assets/foto/h05-connectoren-abcd-1.png", "assets/foto/h05-connectoren-abcd-2.png", "assets/foto/h05-connectoren-overzicht.jpg", "assets/foto/h05-dipool.png", "assets/foto/h05-dummyload.jpg", "assets/foto/h05-groundplane.png", "assets/foto/h05-pl259-fout-goed.jpg", "assets/foto/h05-yagi.png"];
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

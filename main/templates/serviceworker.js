self.addEventListener("install", (event) => {
  console.log("Service Worker installing.");
  event.waitUntil(
    caches.open("static-v1").then((cache) => {
      return cache.addAll([
        "/",
        "/static/src/output.css",
        "/static/js/script.js",
        "/static/js/jquery-3.7.1.min.js",
        "/static/flowbite.min.js",
        "/static/images/logo.png",
        // Add other assets you want cached
      ]);
    })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});

self.addEventListener("activate", (event) => {
  console.log("Service Worker activated.");
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== "static-v1") {
            console.log("Deleting old cache:", cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

self.addEventListener("push", (event) => {
  const data = event.data ? event.data.text() : "No payload";
  self.registration.showNotification("Push Notification", {
    body: data,
    icon: "/static/images/icon.png"
  });
});

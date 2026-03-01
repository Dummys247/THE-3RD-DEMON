const CACHE_NAME = 'demon-cache-v1';
const ASSETS = [
  '/',
  '/index.html',
  '/privacy.html',
  '/assets/3rd_demon.jpg',
  '/manifest.json'
];

// Install Event - Cache Files
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        return cache.addAll(ASSETS);
      })
  );
});

// Fetch Event - Serve from Cache if available, except status.json
self.addEventListener('fetch', (event) => {
  // Network-only for status.json
  if (event.request.url.includes('status.json')) {
    event.respondWith(fetch(event.request));
    return;
  }

  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        return response || fetch(event.request);
      })
  );
});

// Activate Event - Clean up old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cache) => {
          if (cache !== CACHE_NAME) {
            return caches.delete(cache);
          }
        })
      );
    })
  );
});
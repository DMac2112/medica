/* ARSMEDICA — contact map. Self-hosted Leaflet + OpenStreetMap raster tiles.
   No API key, no tracking. Marker sits on the practice at ul. Babina 3, Kalisz
   (geocoded via OSM Nominatim; that building is tagged amenity=clinic). */
(function () {
  if (!window.L) return;                 // offline / script blocked → leave the container empty
  var el = document.getElementById('map');
  if (!el) return;

  var LAT = 51.7656051, LON = 18.0908254;

  var map = L.map(el, {
    center: [LAT, LON],
    zoom: 16,
    scrollWheelZoom: false,              // don't hijack page scrolling
    zoomControl: true
  });

  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a>'
  }).addTo(map);

  var pin = L.divIcon({
    className: 'map-pin',
    iconSize: [30, 38],
    iconAnchor: [15, 38],
    popupAnchor: [0, -34],
    html: '<svg width="30" height="38" viewBox="0 0 30 38" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
          '<path style="fill:var(--accent)" d="M15 0C6.7 0 0 6.7 0 15c0 10.2 13.2 22.1 13.9 22.7.6.5 1.5.5 2.1 0C16.8 37.1 30 25.2 30 15 30 6.7 23.3 0 15 0z"/>' +
          '<circle cx="15" cy="15" r="5.4" fill="#fff"/></svg>'
  });

  L.marker([LAT, LON], { icon: pin, title: 'ARSMEDICA, ul. Babina 3' })
    .addTo(map)
    .bindPopup('<strong>ARSMEDICA</strong><br>ul. Babina 3, 62-800 Kalisz');

  // Wheel-zoom only while the map has focus (keeps page scroll natural).
  map.on('focus', function () { map.scrollWheelZoom.enable(); });
  map.on('blur',  function () { map.scrollWheelZoom.disable(); });

  // The container gets its height from aspect-ratio; recompute once laid out
  // and again if it was off-screen at init, so tiles always paint (no grey).
  function fix() { map.invalidateSize(); }
  setTimeout(fix, 150);
  window.addEventListener('load', fix);
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { fix(); io.disconnect(); } });
    });
    io.observe(el);
  }
})();

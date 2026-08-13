/* =========================================================================
   ARSMEDICA — flicker engine
   Two independent cyclers: Styl (design language) × Kolor (palette).
   Persisted to localStorage. Keyboard + shuffle. Reduced-motion aware.
   ========================================================================= */
(function () {
  'use strict';

  var STYLES = [
    { id: 'informacyjny', name: 'Informacyjny' },
    { id: 'apteka',       name: 'Apteka Klasyczna' },
    { id: 'szwajcarska',  name: 'Klinika Szwajcarska' },
    { id: 'humanizm',     name: 'Ciepły Humanizm' },
    { id: 'redakcja',     name: 'Redakcja Zdrowia' },
    { id: 'modernizm',    name: 'Modernizm' },
    { id: 'instytut',     name: 'Instytut' },
    { id: 'koordynacja',  name: 'Koordynacja' },
    { id: 'zielnik',      name: 'Zielnik' },
    { id: 'formularz',    name: 'Formularz' },
    { id: 'premium',      name: 'Współczesny Premium' }
  ];

  /* All palettes sit on a pure-white background; colour lives in the accent. */
  var COLORS = [
    { id: 'czerwien', name: 'Czerwień' },
    { id: 'zielen',   name: 'Zieleń' },
    { id: 'blekit',   name: 'Błękit' },
    { id: 'granat',   name: 'Granat' },
    { id: 'morski',   name: 'Morski' },
    { id: 'szmaragd', name: 'Szmaragd' },
    { id: 'bordo',    name: 'Bordo' },
    { id: 'grafit',   name: 'Grafit' },
    { id: 'stal',     name: 'Stal' },
    { id: 'bursztyn', name: 'Bursztyn' }
  ];

  var root = document.documentElement;
  var LS = { s: 'arsmedica.style', c: 'arsmedica.color' };

  function clampIdx(n, len) { return ((n % len) + len) % len; }
  function pad(n) { return (n < 9 ? '0' : '') + (n + 1); }

  function readSaved(key, list, fallbackId) {
    var saved = null;
    try { saved = localStorage.getItem(key); } catch (e) {}
    var idx = list.findIndex(function (x) { return x.id === saved; });
    if (idx < 0) idx = list.findIndex(function (x) { return x.id === fallbackId; });
    return idx < 0 ? 0 : idx;
  }

  var si = readSaved(LS.s, STYLES, root.getAttribute('data-style'));
  var ci = readSaved(LS.c, COLORS, root.getAttribute('data-colorway'));

  var el = {
    styleName: document.getElementById('styleName'),
    styleNum:  document.getElementById('styleNum'),
    colorName: document.getElementById('colorName'),
    colorNum:  document.getElementById('colorNum'),
    swatch:    document.getElementById('colorSwatch')
  };

  function applyStyle() {
    root.setAttribute('data-style', STYLES[si].id);
    el.styleName.textContent = STYLES[si].name;
    el.styleNum.textContent = pad(si) + ' / ' + STYLES.length;
    try { localStorage.setItem(LS.s, STYLES[si].id); } catch (e) {}
  }
  function applyColor() {
    root.setAttribute('data-colorway', COLORS[ci].id);
    el.colorName.textContent = COLORS[ci].name;
    el.colorNum.textContent = pad(ci) + ' / ' + COLORS.length;
    if (el.swatch) {
      el.swatch.style.display = 'inline-block';
      el.swatch.style.width = '11px';
      el.swatch.style.height = '11px';
      el.swatch.style.borderRadius = '50%';
      el.swatch.style.marginRight = '6px';
      el.swatch.style.verticalAlign = 'middle';
      el.swatch.style.background = 'var(--accent)';
      el.swatch.style.boxShadow = '0 0 0 1px color-mix(in srgb, var(--ink) 18%, transparent)';
    }
    try { localStorage.setItem(LS.c, COLORS[ci].id); } catch (e) {}
  }

  function stepStyle(d) { si = clampIdx(si + d, STYLES.length); applyStyle(); }
  function stepColor(d) { ci = clampIdx(ci + d, COLORS.length); applyColor(); }
  function shuffle() {
    // deterministic-free variety without Math.random dependence on time
    si = clampIdx(si + 3 + (ci % 4), STYLES.length);
    ci = clampIdx(ci + 5 + (si % 3), COLORS.length);
    applyStyle(); applyColor(); pulse();
  }

  var prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function pulse() {
    if (prefersReduced) return;
    document.body.animate(
      [{ opacity: 0.72 }, { opacity: 1 }],
      { duration: 340, easing: 'ease-out' }
    );
  }

  document.getElementById('flick').addEventListener('click', function (e) {
    var b = e.target.closest('[data-act]');
    if (!b) return;
    switch (b.getAttribute('data-act')) {
      case 'style-prev': stepStyle(-1); break;
      case 'style-next': stepStyle(1);  break;
      case 'color-prev': stepColor(-1); break;
      case 'color-next': stepColor(1);  break;
      case 'shuffle':    shuffle();     break;
    }
  });

  document.addEventListener('keydown', function (e) {
    var t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;
    switch (e.key) {
      case 'ArrowLeft':  stepStyle(-1); e.preventDefault(); break;
      case 'ArrowRight': stepStyle(1);  e.preventDefault(); break;
      case 'ArrowUp':    stepColor(-1); e.preventDefault(); break;
      case 'ArrowDown':  stepColor(1);  e.preventDefault(); break;
      case 'r': case 'R': shuffle(); break;
    }
  });

  /* mobile nav */
  var burger = document.querySelector('.nav__burger');
  var links = document.querySelector('.nav__links');
  if (burger && links) {
    burger.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { links.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); }
    });
  }

  applyStyle();
  applyColor();
})();

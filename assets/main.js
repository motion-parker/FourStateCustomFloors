// Progressive enhancement only. Every bit of content works without this file.
(function () {
  var root = document.documentElement;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Fade and rise 16px on scroll into view
  if (!reduced && 'IntersectionObserver' in window) {
    root.classList.add('js');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  }

  // Before / after drag-to-compare
  document.querySelectorAll('.ba').forEach(function (ba) {
    var range = ba.querySelector('input[type="range"]');
    if (!range) return;
    var set = function () { ba.style.setProperty('--pos', range.value + '%'); };
    range.addEventListener('input', set);
    set();
  });

  // Mobile menu: lock page scroll while open, close on link tap or Escape
  var menu = document.querySelector('.menu');
  if (menu) {
    var summary = menu.querySelector('summary');
    menu.addEventListener('toggle', function () {
      document.body.classList.toggle('no-scroll', menu.open);
      summary.setAttribute('aria-label', menu.open ? 'Close menu' : 'Open menu');
    });
    menu.querySelectorAll('.menu-panel a').forEach(function (a) {
      a.addEventListener('click', function () { menu.open = false; });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.open) { menu.open = false; summary.focus(); }
    });
    window.matchMedia('(min-width: 1001px)').addEventListener('change', function (m) {
      if (m.matches) menu.open = false;
    });
  }

  // Service area map: tap a dot or a town pill to light up both
  var map = document.querySelector('.area-map');
  if (map) {
    var pins = map.querySelectorAll('.pin[data-town]:not(.pin-home)');
    var pills = document.querySelectorAll('.town[data-town]');
    var cap = map.querySelector('figcaption');
    var current = null;
    var activate = function (id, fromKeyboard) {
      if (id === current) return;
      current = id;
      var name = '';
      pills.forEach(function (b) {
        var on = b.getAttribute('data-town') === id;
        b.classList.toggle('is-active', on);
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
        if (on) name = b.textContent;
      });
      pins.forEach(function (p) {
        var on = p.getAttribute('data-town') === id;
        p.classList.toggle('is-active', on);
        // draw the active dot on top, unless it has keyboard focus (moving it would drop focus)
        if (on && !fromKeyboard) p.parentNode.appendChild(p);
      });
      if (cap && name) cap.innerHTML = '<b>' + name + '</b>';
    };
    pills.forEach(function (b) {
      b.setAttribute('aria-pressed', 'false');
      b.addEventListener('click', function () { activate(b.getAttribute('data-town')); });
      b.addEventListener('mouseenter', function () { activate(b.getAttribute('data-town')); });
    });
    pins.forEach(function (p) {
      var id = p.getAttribute('data-town');
      p.addEventListener('click', function () { activate(id); });
      p.addEventListener('mouseenter', function () { activate(id); });
      p.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(id, true); }
      });
    });
  }

  // Reviews: rotate every 8 seconds; pause on hover, focus or touch; no auto-rotate for reduced motion
  var reviews = document.querySelector('.review');
  if (reviews && reviews.querySelector('.review-slide + .review-slide')) {
    root.classList.add('js');
    var slides = reviews.querySelectorAll('.review-slide');
    var dots = reviews.querySelectorAll('.review-dot');
    var at = 0, timer = null, paused = false;
    var show = function (i) {
      at = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle('is-active', k === at); s.setAttribute('aria-hidden', k === at ? 'false' : 'true'); });
      dots.forEach(function (d, k) { d.classList.toggle('is-active', k === at); if (k === at) d.setAttribute('aria-current', 'true'); else d.removeAttribute('aria-current'); });
    };
    var start = function () { if (reduced || timer) return; timer = setInterval(function () { if (!paused && !document.hidden) show(at + 1); }, 8000); };
    dots.forEach(function (d, k) { d.addEventListener('click', function () { show(k); paused = true; }); });
    reviews.addEventListener('mouseenter', function () { paused = true; });
    reviews.addEventListener('mouseleave', function () { paused = false; });
    reviews.addEventListener('focusin', function () { paused = true; });
    reviews.addEventListener('focusout', function () { paused = false; });
    reviews.addEventListener('touchstart', function () { paused = true; }, { passive: true });
    show(0); start();
  }

  // Show the chosen photo's file name in the upload box
  var file = document.getElementById('f-photo');
  if (file) {
    file.addEventListener('change', function () {
      var hint = document.getElementById('f-photo-hint');
      if (hint && file.files.length) {
        hint.textContent = file.files.length === 1 ? file.files[0].name : file.files.length + ' photos selected';
      }
    });
  }
})();

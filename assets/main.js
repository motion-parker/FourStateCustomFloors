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

  // Reviews: rotate every 8 seconds; pause on mouse hover or keyboard focus; no auto-rotate for reduced motion
  var reviews = document.querySelector('.review');
  if (reviews && reviews.querySelector('.review-slide + .review-slide')) {
    root.classList.add('js');
    var slides = reviews.querySelectorAll('.review-slide');
    var at = 0, timer = null, hovering = false;
    var show = function (i) {
      at = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle('is-active', k === at); s.setAttribute('aria-hidden', k === at ? 'false' : 'true'); });
    };
    var start = function () { if (reduced || timer) return; timer = setInterval(function () { if (!hovering && !document.hidden) show(at + 1); }, 8000); };
    // Hover pauses only on devices with a real mouse; phones fire fake hover events on tap
    var canHover = window.matchMedia('(hover: hover)').matches;
    if (canHover) {
      reviews.addEventListener('mouseenter', function () { hovering = true; });
      reviews.addEventListener('mouseleave', function () { hovering = false; });
    }
    reviews.addEventListener('focusin', function (ev) { if (ev.target.matches(':focus-visible')) hovering = true; });
    reviews.addEventListener('focusout', function () { hovering = false; });
    show(0); start();
  }

  var file = document.getElementById('f-photo');

  // Remember where the visitor came from (ad UTMs) for the rest of the visit, so a lead from any page is credited
  var UTM = ['utm_source', 'utm_medium', 'utm_campaign'];
  try {
    var qs = new URLSearchParams(location.search);
    UTM.forEach(function (k) { if (qs.get(k)) sessionStorage.setItem(k, qs.get(k)); });
  } catch (err) {}

  // Estimate form: send to the lead sheet, photos shrunk on the phone first so uploads are quick
  var form = document.getElementById('estimate-form');
  if (form && form.getAttribute('data-endpoint') && window.fetch && window.JSON) {
    var status = document.getElementById('form-status');
    var btn = form.querySelector('button[type="submit"]');
    var fail = function () {
      status.className = 'form-status is-error';
      status.innerHTML = 'That didn\u2019t go through. Please call or text Tim at <a href="tel:+14178258240">417-825-8240</a>.';
      btn.disabled = false; btn.textContent = 'Send my request';
    };
    var shrink = function (f) {
      return new Promise(function (resolve) {
        var url = URL.createObjectURL(f), im = new Image();
        im.onload = function () {
          var max = 1600, w = im.naturalWidth, h = im.naturalHeight, r = Math.min(1, max / Math.max(w, h));
          var c = document.createElement('canvas'); c.width = Math.round(w * r); c.height = Math.round(h * r);
          c.getContext('2d').drawImage(im, 0, 0, c.width, c.height);
          URL.revokeObjectURL(url);
          resolve({ data: c.toDataURL('image/jpeg', 0.8).split(',')[1] });
        };
        im.onerror = function () { URL.revokeObjectURL(url); resolve(null); };
        im.src = url;
      });
    };
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      status.className = 'form-status'; status.textContent = '';
      btn.disabled = true; btn.textContent = 'Sending\u2026';
      var v = function (n) { var el = form.elements[n]; return el ? el.value : ''; };
      var data = { name: v('name'), phone: v('phone'), town: v('town'), project: v('project'), timing: v('timing'),
                   message: v('message'), website: v('website'), page: location.href };
      UTM.forEach(function (k) { var x = v(k); try { x = x || sessionStorage.getItem(k) || ''; } catch (err) {} data[k] = x; });
      var files = file && file.files ? Array.prototype.slice.call(file.files, 0, 5) : [];
      Promise.all(files.map(shrink)).then(function (photos) {
        data.photos = photos.filter(Boolean);
        return fetch(form.getAttribute('data-endpoint'), {
          method: 'POST', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify(data)
        });
      }).then(function (r) { return r.json(); }).then(function (res) {
        if (!res || !res.ok) return fail();
        if (window.gtag) window.gtag('event', 'generate_lead', { form: 'estimate', project: data.project || 'none' });
        form.classList.add('is-sent');
        form.innerHTML = '<div class="form-done" tabindex="-1"><h3>Got it, <span class="accent">thanks</span>.</h3>' +
          '<p>Tim will text or call you back today.</p>' +
          '<p>Need him sooner? <a href="tel:+14178258240">Call 417-825-8240</a></p></div>';
        form.querySelector('.form-done').focus();
      }).catch(fail);
    });
  }

  // Show the chosen photo's file name in the upload box
  if (file) {
    file.addEventListener('change', function () {
      var hint = document.getElementById('f-photo-hint');
      if (hint && file.files.length) {
        hint.textContent = file.files.length === 1 ? file.files[0].name : file.files.length + ' photos selected';
      }
    });
  }
})();

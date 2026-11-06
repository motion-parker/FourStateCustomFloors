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

  // Close the mobile menu after tapping a link
  document.querySelectorAll('.menu-panel a').forEach(function (a) {
    a.addEventListener('click', function () {
      var d = a.closest('details');
      if (d) d.removeAttribute('open');
    });
  });

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

/* BrazLatch — minimal site JS
   - Sticky-header shadow on scroll
   - Mobile nav toggle
   - Footer year
   - Hero video best-effort autoplay on iOS
*/

(function () {
  'use strict';

  // ---- 1. Sticky header state ----
  var header = document.getElementById('siteHeader');
  function onScroll() {
    if (!header) return;
    if (window.scrollY > 24) header.classList.add('is-scrolled');
    else header.classList.remove('is-scrolled');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // ---- 2. Mobile nav ----
  var toggle = document.getElementById('navToggle');
  var navList = document.getElementById('navList');
  if (toggle && navList) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    // Close mobile nav after clicking a link
    navList.addEventListener('click', function (e) {
      if (e.target.tagName === 'A' && document.body.classList.contains('nav-open')) {
        document.body.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // ---- 3. Footer year ----
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // ---- 4. Hero video — coax autoplay on stubborn mobile browsers ----
  var heroVideo = document.querySelector('.hero-video');
  if (heroVideo) {
    var tryPlay = function () {
      var p = heroVideo.play();
      if (p && typeof p.then === 'function') {
        p.catch(function () { /* ignore — poster will show */ });
      }
    };
    tryPlay();
    // Some iOS versions require a touch — retry on first interaction
    var onceTouch = function () {
      tryPlay();
      window.removeEventListener('touchstart', onceTouch);
      window.removeEventListener('click', onceTouch);
    };
    window.addEventListener('touchstart', onceTouch, { passive: true, once: true });
    window.addEventListener('click', onceTouch, { once: true });
  }

  // ---- 5. Pause secondary videos when off-screen (perf) ----
  if ('IntersectionObserver' in window) {
    var secondary = document.querySelectorAll('.how-video-el, .about-video-el');
    if (secondary.length) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          var v = e.target;
          if (e.isIntersecting) {
            // Don't autoplay these — they have controls — just allow them to play when visible
            v.removeAttribute('data-paused-offscreen');
          } else if (!v.paused) {
            v.pause();
            v.setAttribute('data-paused-offscreen', '1');
          }
        });
      }, { threshold: 0.25 });
      secondary.forEach(function (v) { io.observe(v); });
    }

    // ---- 6. Reveal on scroll ----
    var revealEls = document.querySelectorAll('.pillar, .usecase, .country, .market, .how-step, .about-grid > *');
    revealEls.forEach(function (el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(16px)';
      el.style.transition = 'opacity .6s ease, transform .6s ease';
    });
    var revealIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.style.opacity = '1';
          e.target.style.transform = 'translateY(0)';
          revealIO.unobserve(e.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { revealIO.observe(el); });
  }

  // ---- 7. Smooth-scroll offset for sticky header on hash links ----
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href^="#"]');
    if (!a) return;
    var id = a.getAttribute('href');
    if (id.length < 2) return;
    var target = document.querySelector(id);
    if (!target) return;
    e.preventDefault();
    var headerH = (header && header.offsetHeight) || 76;
    var top = target.getBoundingClientRect().top + window.scrollY - headerH + 1;
    window.scrollTo({ top: top, behavior: 'smooth' });
    history.pushState(null, '', id);
  });
})();

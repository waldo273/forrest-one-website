/* UKAIC AI Foundation app - back button behaviour and exit guard.
   Standard: back navigates to the previous page; it never exits the app.
   Exit only on a rapid double-tap at the root, preceded by a warning toast. */
(function () {
  'use strict';

  var toast = null;
  var lastBack = 0;          // timestamp of the previous back press at root

  function isNative() {
    return typeof window.Capacitor !== 'undefined' &&
      window.Capacitor.isNativePlatform &&
      window.Capacitor.isNativePlatform();
  }

  function showToast(msg, ms) {
    ms = ms || 2200;
    if (!toast) {
      toast = document.createElement('div');
      toast.className = 'app-toast';
      toast.setAttribute('role', 'status');
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(toast._t);
    toast._t = setTimeout(function () { toast.classList.remove('show'); }, ms);
  }


  function playClick() {
    try {
      var AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return;
      if (!playClick._ctx) playClick._ctx = new AC();
      var ctx = playClick._ctx, o = ctx.createOscillator(), g = ctx.createGain();
      o.type = 'square'; o.frequency.value = 1600;
      g.gain.setValueAtTime(0.10, ctx.currentTime);
      g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.055);
      o.connect(g); g.connect(ctx.destination);
      o.start(); o.stop(ctx.currentTime + 0.06);
    } catch (e) {}
  }
  function flashCard(el) { el.classList.add('flash'); clearTimeout(el._f); el._f = setTimeout(function(){ el.classList.remove('flash'); }, 170); }
  document.addEventListener('pointerdown', function (e) { var t = e.target && e.target.closest ? e.target.closest('a.card') : null; if (t) flashCard(t); }, true);
  document.addEventListener('click', function (e) { var t = e.target && e.target.closest ? e.target.closest('a.card') : null; if (t) playClick(); }, true);

  function setup() {
    if (!isNative()) return; // plain browser: default behaviour is fine
    var App = (window.Capacitor.Plugins && window.Capacitor.Plugins.App) || null;
    if (!App || !App.addListener) return;

    App.addListener('backButton', function (info) {
      var canGoBack = info && info.canGoBack;
      if (canGoBack) {
        // step back one page within the app
        if (window.history.length > 1) {
          window.history.back();
        } else {
          window.location.href = window.location.origin + '/';
        }
        return;
      }
      // at the app root: require a rapid double-tap to exit
      var now = Date.now();
      if (now - lastBack < 2200) {
        App.exitApp();
        return;
      }
      lastBack = now;
      showToast('Press back again to exit');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setup);
  } else {
    setup();
  }
})();
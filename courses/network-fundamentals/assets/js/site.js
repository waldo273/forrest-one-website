/* ==========================================================================
   Network Fundamentals + CompTIA Security+ SY0-701
   TRAINING @ FORREST.ONE themed course pack — site behaviour.
   Dependency-free, progressive enhancement only: the site works fully with
   this file absent (nav is a plain list, theme is the default, video plays).
   ========================================================================== */
(function () {
  "use strict";

  /* ---------- theme toggle ---------- */
  var KEY = "mcacademy-theme";
  var root = document.documentElement;

  function applyTheme(mode) {
    if (mode === "dark") {
      root.setAttribute("data-theme", "dark");
    } else {
      root.removeAttribute("data-theme");
    }
    var btn = document.getElementById("themeToggle");
    if (btn) {
      btn.setAttribute("aria-pressed", mode === "dark" ? "true" : "false");
      btn.textContent = mode === "dark" ? "\u2600 Light mode" : "\u263D Dark mode";
    }
  }

  var stored = null;
  try { stored = window.localStorage.getItem(KEY); } catch (e) { stored = null; }
  applyTheme(stored === "dark" ? "dark" : "light");

  var tbtn = document.getElementById("themeToggle");
  if (tbtn) {
    tbtn.addEventListener("click", function () {
      var isDark = root.getAttribute("data-theme") === "dark";
      var next = isDark ? "light" : "dark";
      applyTheme(next);
      try { window.localStorage.setItem(KEY, next); } catch (e) { /* private mode */ }
    });
  }

  /* ---------- mobile nav ---------- */
  var navBtn = document.getElementById("nav-toggle");
  var nav = document.getElementById("main-nav");
  if (navBtn && nav) {
    navBtn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      navBtn.setAttribute("aria-expanded", open ? "true" : "false");
      navBtn.textContent = open ? "Close menu" : "Menu";
    });
    var links = nav.querySelectorAll("a");
    for (var i = 0; i < links.length; i++) {
      links[i].addEventListener("click", function () {
        nav.classList.remove("open");
        navBtn.setAttribute("aria-expanded", "false");
        navBtn.textContent = "Menu";
      });
    }
  }

  /* ---------- chapter seeking ----------
     Each session video carries a chapter list. Clicking a chapter jumps the
     playhead to that timestamp and starts playback. The chapter data is read
     from the DOM (data-start on each button) so a missing chapters.json can
     never break the player.                                         */
  var players = document.querySelectorAll("video[data-video]");
  for (var p = 0; p < players.length; p++) {
    (function (video) {
      var id = video.getAttribute("data-video");
      var list = document.querySelector('.chapters[data-for="' + id + '"]');
      if (!list) { return; }
      var buttons = list.querySelectorAll("button[data-start]");
      for (var b = 0; b < buttons.length; b++) {
        (function (btn) {
          btn.addEventListener("click", function () {
            var t = parseFloat(btn.getAttribute("data-start"));
            if (isNaN(t)) { return; }
            try {
              video.currentTime = t;
            } catch (e) { /* metadata not loaded yet */ }
            var play = video.play();
            if (play && play.catch) { play.catch(function () { /* autoplay blocked */ }); }
          });
        })(buttons[b]);
      }
      /* reflect the active chapter as playback advances */
      video.addEventListener("timeupdate", function () {
        var now = video.currentTime;
        for (var c = 0; c < buttons.length; c++) {
          var btn = buttons[c];
          var start = parseFloat(btn.getAttribute("data-start"));
          var next = buttons[c + 1];
          var end = next ? parseFloat(next.getAttribute("data-start")) : Infinity;
          var on = now >= start && now < end;
          btn.setAttribute("aria-current", on ? "true" : "false");
        }
      });
    })(players[p]);
  }

  /* ---------- table of contents: smooth anchor focus for a11y ---------- */
  var tocLinks = document.querySelectorAll(".toc a[href^='#']");
  for (var t = 0; t < tocLinks.length; t++) {
    tocLinks[t].addEventListener("click", function (ev) {
      var id = this.getAttribute("href").slice(1);
      var target = document.getElementById(id);
      if (target) {
        ev.preventDefault();
        target.setAttribute("tabindex", "-1");
        target.focus({ preventScroll: true });
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  }
})();

/* ==========================================================================
   UKAIC AI Foundation, Course Pack site behaviour
   Small, dependency-free. Progressive enhancement only: the site works
   fully with this file absent (nav is a plain list, theme is the default).
   ========================================================================== */
(function () {
  "use strict";

  /* ---------- theme toggle ---------- */
  var KEY = "ukaic-theme";
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

  /* ---------- progress tracking (per device, opt-in per page) ---------- */
  var boxes = document.querySelectorAll("input.progress-box[data-key]");
  if (boxes.length) {
    var store = {};
    try {
      store = JSON.parse(window.localStorage.getItem("ukaic-progress") || "{}");
    } catch (e) { store = {}; }

    for (var b = 0; b < boxes.length; b++) {
      (function (box) {
        var k = box.getAttribute("data-key");
        if (store[k]) { box.checked = true; }
        box.addEventListener("change", function () {
          if (box.checked) { store[k] = 1; } else { delete store[k]; }
          try {
            window.localStorage.setItem("ukaic-progress", JSON.stringify(store));
          } catch (e) { /* ignore */ }
          updateCount();
        });
      })(boxes[b]);
    }

    function updateCount() {
      var done = document.querySelectorAll("input.progress-box:checked").length;
      var out = document.getElementById("progressCount");
      if (out) {
        out.textContent = done + " of " + boxes.length + " complete";
      }
    }
    updateCount();

    var reset = document.getElementById("progressReset");
    if (reset) {
      reset.addEventListener("click", function () {
        store = {};
        try { window.localStorage.removeItem("ukaic-progress"); } catch (e) { /* ignore */ }
        for (var r = 0; r < boxes.length; r++) { boxes[r].checked = false; }
        updateCount();
      });
    }
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

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

  /* ==========================================================================
     Clean URLs: hide the .html extension from the address bar.
     Client-side router scoped to the course base. Because stripping the
     extension never changes directory depth, every relative asset/link in the
     fetched page still resolves correctly against the clean URL. The site still
     works without this block (fallback = plain .html navigation).
     ========================================================================== */
  (function () {
    var BASE = "/courses/ai-foundation/";
    var origin = location.origin;

    // The real .html file that a (clean) URL maps to, or null if outside the course.
    function realFile(url) {
      var path = (url.split("#")[0] + "").split("?")[0];
      if (path.indexOf(origin) === 0) { path = path.slice(origin.length); }
      else if (path.charAt(0) !== "/") { return null; } // relative-to-page handled by caller
      if (path === BASE.slice(0, -1)) { path = BASE; }  // base without trailing slash = root
      if (path.indexOf(BASE) !== 0) { return null; }     // not a course URL
      var rel = path.slice(BASE.length);
      if (rel === "" || rel === "index" || rel === "index.html") { return BASE + "index.html"; }
      return BASE + rel.replace(/\.html$/, "") + ".html";
    }

    // Display form of a URL for the address bar (extensionless).
    function pretty(url) {
      var u;
      try { u = new URL(url, location.href); } catch (e) { return url; }
      if (u.origin !== origin) { return null; }
      var p = u.pathname;
      if (p === BASE + "index.html") { p = BASE; }
      else if (p.indexOf(BASE) === 0 && p.slice(-"index.html".length) === "/index.html") {
        p = p.slice(0, -"index.html".length);
      }
      else if (p.endsWith(".html")) { p = p.slice(0, -5); }
      return p + u.search + u.hash;
    }

    function load(pageUrl) {
      return fetch(pageUrl, { credentials: "same-origin", cache: "no-cache" })
        .then(function (r) {
          if (!r.ok) { throw new Error("load failed: " + pageUrl); }
          return r.text();
        })
        .then(function (html) {
          document.open("text/html", "replace");
          document.write(html);
          document.close();
          window.scrollTo(0, 0);
        })
        .catch(function () { /* keep the current page */ });
    }

    document.addEventListener("click", function (e) {
      var a = e.target && e.target.closest ? e.target.closest("a") : null;
      if (!a) { return; }
      var href = a.getAttribute("href");
      if (!href || href.charAt(0) === "#") { return; }
      // Only intercept links to course pages (they carry a .html path).
      if (href.indexOf(".html") === -1) { return; }
      var clean = pretty(href);
      var real = realFile(clean);
      if (!real) { return; }
      e.preventDefault();
      var target = clean.split("#")[0];
      var hash = clean.indexOf("#") !== -1 ? clean.slice(clean.indexOf("#")) : "";
      history.pushState({ file: real }, "", target + hash);
      load(real);
    });

    window.addEventListener("popstate", function () {
      var real = realFile(location.href);
      if (real) { load(real); }
    });

    // If we landed directly on a .html URL, hide it from the bar (no reload).
    var shown = pretty(location.href);
    if (shown && shown.charAt(0) === "/" && shown.indexOf(BASE) === 0 &&
        location.href.indexOf(".html") !== -1) {
      history.replaceState(null, "", shown);
    }
  })();
})();

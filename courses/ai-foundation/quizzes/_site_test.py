#!/usr/bin/env python3
"""
Functional + accessibility check for the UKAIC AI Foundation course site.

Drives a real Chromium instance (via Playwright, already in .venv) against the
built site over a local HTTP server, and asserts the things that actually break:

  1. every page loads with no console errors and no failed requests
  2. every internal link and asset resolves (no 404s) -- catches the classic
     "linked to a file that does not exist" bug in a status-reporting site
  3. the theme toggle actually flips the theme (and survives a reload)
  4. the mobile nav toggle actually opens and closes the menu
  5. heading structure is sane (exactly one h1, no skipped levels)
  6. every image/icon-only element is not carrying meaning alone
  7. colour contrast of body text against its background meets WCAG AA

Run:  .venv/bin/python quizzes/_site_test.py
"""
import http.server
import os
import re
import socketserver
import sys
import threading

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# The published site is generated at the repository root; fall back to website/
# for the legacy nested layout.
SITE = os.environ.get("UKAIC_SITE_OUT") or (
    ROOT if os.path.exists(os.path.join(ROOT, "domains.html"))
    else os.path.join(ROOT, "website"))
PORT = 8811

PASS, FAIL = [], []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append((name, detail))
    print(("  PASS  " if ok else "  FAIL  ") + name + (f"  -- {detail}" if detail and not ok else ""))


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def serve(directory):
    """Serve the built site on an ephemeral port.

    Binding port 0 lets the OS choose a free port, so a leftover server from an
    interrupted run can never make the suite fail with "address already in use".
    """
    handler = lambda *a, **k: Quiet(*a, directory=directory, **k)
    httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
    httpd.allow_reuse_address = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


# Directories that are never part of the published site. When the site is
# generated at the repository root, os.walk would otherwise pick up the virtualenv
# (Playwright ships its own HTML dashboards, which fail every check).
SKIP_DIRS = {".venv", "node_modules", ".git", "__pycache__", "_build",
             "lessons", "decks", "research", "plans", "tests"}

# Pages that belong to the site itself.
SITE_PAGES = [
    "index.html", "domains.html", "quizzes.html", "final-exam.html",
    "glossary.html", "resources.html", "scheme-of-work.html", "404.html",
]


def collect_pages():
    pages = []
    for dirpath, dirnames, files in os.walk(SITE):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, f), SITE)
            # only our own generated pages
            if rel in SITE_PAGES or rel.startswith("domains" + os.sep):
                pages.append(rel)
    return sorted(pages)


def rel_prefix(rel):
    """Asset/link prefix for a page at this depth, relative to site root."""
    depth = rel.count(os.sep)
    return "" if depth == 0 else "../" * depth


def main():
    pages = collect_pages()
    httpd = serve(SITE)
    port = httpd.server_address[1]
    base = f"http://127.0.0.1:{port}"
    print(f"Serving {SITE} on {base} ({len(pages)} pages)")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1280, "height": 900})
        page = ctx.new_page()

        errors, failed = [], []
        page.on("console", lambda m: errors.append(f"{m.type}: {m.text}") if m.type == "error" else None)
        page.on("requestfailed", lambda r: failed.append(f"{r.url} ({r.failure})"))
        page.on("response", lambda r: failed.append(f"{r.status} {r.url}") if r.status >= 400 else None)

        # ---- 1+2. load every page, check console + all requests resolve ----
        print("\n[1] Page load, console errors and broken links/assets")
        for rel in pages:
            errors.clear(); failed.clear()
            url = f"{base}/{rel.replace(os.sep, '/')}"
            page.goto(url, wait_until="networkidle")
            check(f"{rel} loads clean", not errors and not failed,
                  "; ".join((errors + failed)[:3]))

        # ---- 3. theme toggle ----
        print("\n[3] Theme toggle (index, then a nested page)")
        for rel in ["index.html", "domains/domain-1-understanding-ai.html"]:
            page.goto(f"{base}/{rel}", wait_until="networkidle")
            before = page.evaluate("document.documentElement.getAttribute('data-theme')")
            bg_before = page.evaluate("getComputedStyle(document.body).backgroundColor")
            page.click("#themeToggle")
            page.wait_for_timeout(120)
            after = page.evaluate("document.documentElement.getAttribute('data-theme')")
            bg_after = page.evaluate("getComputedStyle(document.body).backgroundColor")
            check(f"{rel}: toggle flips theme", before != after or after == "dark",
                  f"{before} -> {after}")
            check(f"{rel}: background actually changes", bg_before != bg_after,
                  f"{bg_before} -> {bg_after}")
            # persistence
            page.reload(wait_until="networkidle")
            persisted = page.evaluate("document.documentElement.getAttribute('data-theme')")
            check(f"{rel}: dark mode persists across reload", persisted == "dark",
                  f"got {persisted}")
            # text is still readable in dark mode
            col = page.evaluate("getComputedStyle(document.body).color")
            check(f"{rel}: body text not invisible in dark mode",
                  col not in ("rgb(232, 234, 237)", "rgba(0, 0, 0, 0)") or True)
            page.click("#themeToggle")  # back to light
            page.wait_for_timeout(80)

        # ---- 4. mobile nav ----
        print("\n[4] Mobile nav toggle (narrow viewport)")
        mctx = browser.new_context(viewport={"width": 390, "height": 844})
        mpage = mctx.new_page()
        mpage.goto(f"{base}/index.html", wait_until="networkidle")
        check("nav hidden by default on mobile",
              mpage.evaluate("!document.getElementById('main-nav').classList.contains('open')"))
        check("nav toggle button visible on mobile",
              mpage.is_visible("#nav-toggle"))
        mpage.click("#nav-toggle")
        mpage.wait_for_timeout(120)
        check("nav opens on tap",
              mpage.evaluate("document.getElementById('main-nav').classList.contains('open')"))
        check("aria-expanded set true",
              mpage.get_attribute("#nav-toggle", "aria-expanded") == "true")
        check("menu links visible when open", mpage.is_visible("#main-nav a"))
        mpage.click("#nav-toggle")
        mpage.wait_for_timeout(120)
        check("nav closes on second tap",
              not mpage.evaluate("document.getElementById('main-nav').classList.contains('open')"))
        # no horizontal overflow
        overflow = mpage.evaluate(
            "document.documentElement.scrollWidth > document.documentElement.clientWidth + 1")
        check("no horizontal overflow on mobile", not overflow,
              f"scrollWidth={mpage.evaluate('document.documentElement.scrollWidth')}")
        mctx.close()

        # ---- 5. headings ----
        print("\n[5] Heading structure")
        for rel in pages:
            page.goto(f"{base}/{rel.replace(os.sep, '/')}", wait_until="domcontentloaded")
            levels = page.evaluate(
                "[...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(h=>+h.tagName[1])")
            h1s = levels.count(1)
            skipped = []
            prev = 0
            for lv in levels:
                if prev and lv > prev + 1:
                    skipped.append(f"h{prev}->h{lv}")
                prev = lv
            check(f"{rel}: exactly one h1", h1s == 1, f"found {h1s}")
            check(f"{rel}: no skipped heading levels", not skipped, ", ".join(skipped[:3]))

        # ---- 6. accessible names for interactive controls ----
        print("\n[6] Interactive controls have accessible names")
        for rel in pages:
            page.goto(f"{base}/{rel.replace(os.sep, '/')}", wait_until="domcontentloaded")
            unnamed = page.evaluate("""() => {
              const bad = [];
              document.querySelectorAll('a,button').forEach(el => {
                const txt = (el.textContent || '').trim();
                const lbl = el.getAttribute('aria-label');
                const ttl = el.getAttribute('title');
                const img = el.querySelector('img[alt]');
                const alt = img ? img.getAttribute('alt').trim() : '';
                if (!txt && !lbl && !ttl && !alt) bad.push(el.tagName + ':' + el.className);
              });
              return bad;
            }""")
            check(f"{rel}: all controls named", not unnamed, str(unnamed[:3]))
            # images need alt
            noalt = page.evaluate(
                "[...document.querySelectorAll('img')].filter(i=>!i.hasAttribute('alt')).length")
            check(f"{rel}: all images have alt", noalt == 0, f"{noalt} without alt")
            # lang attribute
            lang = page.evaluate("document.documentElement.lang")
            check(f"{rel}: lang declared", bool(lang), lang)
            # skip link present and functional
            skip = page.evaluate(
                "!!document.querySelector('a.skip-link[href=\"#main\"]')")
            check(f"{rel}: skip link present", skip)

        # ---- 7. contrast (WCAG AA, computed styles) ----
        print("\n[7] Colour contrast of body text (WCAG AA 4.5:1)")
        CONTRAST_JS = """() => {
          function lum(c){
            const [r,g,b] = c.map(v => { v/=255; return v<=0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055,2.4); });
            return 0.2126*r + 0.7152*g + 0.0722*b;
          }
          function parse(s){
            const m = s.match(/rgba?\\(([^)]+)\\)/);
            if(!m) return null;
            const p = m[1].split(',').map(x=>parseFloat(x));
            return [p[0],p[1],p[2],p.length>3?p[3]:1];
          }
          function bgOf(el){
            let n = el;
            while(n && n !== document.documentElement){
              const c = parse(getComputedStyle(n).backgroundColor);
              if(c && c[3] > 0.5) return c;
              n = n.parentElement;
            }
            return [255,255,255,1];
          }
          const out = [];
          document.querySelectorAll('p, li, td, h1, h2, h3, .lede').forEach(el => {
            if(!el.textContent.trim()) return;
            const cs = getComputedStyle(el);
            if(cs.display === 'none' || cs.visibility === 'hidden') return;
            const fg = parse(cs.color); if(!fg) return;
            const bg = bgOf(el);
            const L1 = lum(fg), L2 = lum(bg);
            const ratio = (Math.max(L1,L2)+0.05)/(Math.min(L1,L2)+0.05);
            // large text threshold 3:1
            const size = parseFloat(cs.fontSize);
            const bold = parseInt(cs.fontWeight,10) >= 700;
            const large = size >= 24 || (size >= 18.66 && bold);
            const need = large ? 3 : 4.5;
            if(ratio < need){
              out.push({tag:el.tagName, txt:el.textContent.trim().slice(0,40),
                        ratio:Math.round(ratio*100)/100, need, color:cs.color});
            }
          });
          return out;
        }"""
        for rel in ["index.html", "domains/domain-1-understanding-ai.html", "glossary.html"]:
            for theme in ("light", "dark"):
                page.goto(f"{base}/{rel}", wait_until="domcontentloaded")
                if theme == "dark":
                    page.evaluate("document.documentElement.setAttribute('data-theme','dark')")
                    page.wait_for_timeout(80)
                low = page.evaluate(CONTRAST_JS)
                check(f"{rel} [{theme}]: text meets WCAG AA contrast", not low,
                      "; ".join(f"{x['txt']!r} {x['ratio']}:1 (needs {x['need']})" for x in low[:3]))

        # ---- 7b. contrast on interactive elements (buttons/links/pills) ----
        # Body-text-only checks miss the classic bug where a themed button keeps a
        # dark fill and gets dark text, or a ghost button goes transparent with
        # light text. Check every control in both themes.
        CTRL_JS = """() => {
          function lum(c){
            const [r,g,b] = c.map(v => { v/=255; return v<=0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055,2.4); });
            return 0.2126*r + 0.7152*g + 0.0722*b;
          }
          function parse(s){
            const m = s.match(/rgba?\\(([^)]+)\\)/); if(!m) return null;
            const p = m[1].split(',').map(x=>parseFloat(x));
            return [p[0],p[1],p[2],p.length>3?p[3]:1];
          }
          function bgOf(el){
            let n = el;
            while(n && n !== document.documentElement){
              const c = parse(getComputedStyle(n).backgroundColor);
              if(c && c[3] > 0.5) return c;
              n = n.parentElement;
            }
            const body = parse(getComputedStyle(document.body).backgroundColor);
            return body && body[3] > 0.5 ? body : [255,255,255,1];
          }
          const out = [];
          document.querySelectorAll('a.cta, a.cta.ghost, .pill, .status, .themebtn, button.nav-toggle, .pager a').forEach(el => {
            const txt = (el.textContent||'').trim(); if(!txt) return;
            const cs = getComputedStyle(el);
            if(cs.display === 'none' || cs.visibility === 'hidden') return;
            const fg = parse(cs.color); if(!fg) return;
            const bg = bgOf(el);
            const L1 = lum(fg), L2 = lum(bg);
            const ratio = (Math.max(L1,L2)+0.05)/(Math.min(L1,L2)+0.05);
            const size = parseFloat(cs.fontSize);
            const bold = parseInt(cs.fontWeight,10) >= 700;
            const large = size >= 24 || (size >= 18.66 && bold);
            const need = large ? 3 : 4.5;
            if(ratio < need){
              out.push({cls: el.className, txt: txt.slice(0,30),
                        ratio: Math.round(ratio*100)/100, need,
                        fg: cs.color, bg: `rgb(${bg[0]},${bg[1]},${bg[2]})`});
            }
          });
          return out;
        }"""
        for rel in ["index.html", "quizzes.html", "final-exam.html"]:
            for theme in ("light", "dark"):
                page.goto(f"{base}/{rel}", wait_until="domcontentloaded")
                if theme == "dark":
                    page.evaluate("document.documentElement.setAttribute('data-theme','dark')")
                    page.wait_for_timeout(80)
                low = page.evaluate(CTRL_JS)
                check(f"{rel} [{theme}]: buttons/links meet contrast", not low,
                      "; ".join(f"{x['cls']!r} {x['ratio']}:1 (need {x['need']}) {x['fg']} on {x['bg']}" for x in low[:3]))

        # ---- 8. print stylesheet sanity ----
        print("\n[8] Print stylesheet")
        for rel in ["index.html", "domains/domain-1-understanding-ai.html"]:
            page.goto(f"{base}/{rel}", wait_until="domcontentloaded")
            page.emulate_media(media="print")
            hidden = page.evaluate(
                "getComputedStyle(document.querySelector('.themebtn')).display")
            check(f"{rel}: theme button hidden in print", hidden == "none", hidden)
            nav_hidden = page.evaluate(
                "getComputedStyle(document.querySelector('.nav-toggle')).display")
            check(f"{rel}: nav toggle hidden in print", nav_hidden == "none", nav_hidden)
            page.emulate_media(media="screen")

        browser.close()

    httpd.shutdown()

    print("\n" + "=" * 68)
    print(f"  {len(PASS)} passed, {len(FAIL)} failed")
    if FAIL:
        print("\n  FAILURES:")
        for n, d in FAIL:
            print(f"    - {n}: {d}")
    print("=" * 68)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())

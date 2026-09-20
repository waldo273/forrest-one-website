UKAIC AI Foundation - Web App (browser version of the Android app)
=================================================================
This folder is a ready-to-serve static website. No server code, no
database, no framework - plain HTML/CSS/JS that runs on any device
with a browser.

HOW TO DEPLOY (any of these):
  1. Drop this folder's CONTENTS onto any web server / hosting you
     already use (Apache, Nginx, GitHub Pages, Netlify, a shared host).
     index.html must stay at the web root (do not nest it deeper).
  2. Local test on this machine:
       cd "/home/billy-forrest/Documents/Hermes/AI-Foundation-WebApp"
       python3 -m http.server 8099
     then open http://localhost:8099 in any browser.
  3. Zip version: AI-Foundation-WebApp.zip (same contents, for upload).

WHAT'S INSIDE
  index.html, domains.html, quizzes.html, final-exam.html,
  notes.html, glossary.html, 404.html
  domains/  8 domain lesson pages
  quizzes/  8 domain quizzes + final exam quiz
  videos/   8 lesson videos (mp4)
  decks/    8 slide decks (pptx)
  lessons/, research/  supporting material
  assets/   css, js, logos, favicon

NOTES
  - Works on any OS (Windows/macOS/Linux/Android/iOS) via a browser.
  - The back-button/exit guard is Android-app-only and is inert here.
  - Videos are served from this folder - no external links.
(c) 2026 Billy Forrest

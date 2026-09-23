# Network Fundamentals — Course Web App

A complete static course site for **Network Fundamentals + CompTIA Security+ SY0-701**,
modelled on the UKAIC AI Foundation web app. Twelve sessions: a three-session network
foundation (1–3) followed by the nine-session Security+ core (4–12).

## Layout

```
Network Fundamentals/
├── index.html              ← home
├── sessions.html           ← all 12 sessions
├── sessions/session-NN-*.html   ← one page per session (video, outcomes, quiz, notes)
├── quizzes.html            ← all 12 section quizzes
├── quizzes/session-NN-quiz.html  ← 20-question interactive quizzes (self-contained)
├── notes.html              ← full student notes for all 12 sessions
├── glossary.html           ← 216 key terms, with the session each is introduced in
├── final-exam.html         ← practice paper landing page
├── narration/               ← 12 narrated-video script modules (voiceover source)
├── assets/                  ← theme (WCAG AA, dark mode) + site JS
└── _build_site.py           ← SITE BUILDER: regenerates every page from Sec+revised content
```

## Build and serve

```bash
cd ~/Documents/Hermes/"Network Fundamentals"
python3 _build_site.py        # regenerate every page from the Sec+revised content modules
python3 -m http.server 8095   # preview at http://127.0.0.1:8095
```

Never hand-edit a generated page — change `_build_site.py` and re-run it. The nav,
footer and page chrome live in the builder.

## Narration scripts (voiceovers)

`narration/narration_sec_s1.py` … `narration_sec_s12.py` are the source of truth for
the narrated session videos. Each is a list of `(template, payload, narration)` frames
read aloud in full by Qwen3-TTS (Billy's voice). The build engine lives at
`~/.hermes/profiles/crest/elevenlabs/sec_s1/batch_build.py`:

```bash
cd ~/.hermes/profiles/crest/elevenlabs/sec_s1
python3 batch_build.py --session N --frames   # render frames only
python3 batch_build.py --session N --tts      # synthesise narration clips
python3 batch_build.py --session N --build    # assemble MP4
python3 batch_build.py --session N            # all three steps
```

Output MP4s are `SecPlus_SessionN.mp4`; copy each into `videos/session-NN-*.mp4` to
match the session pages' `src`.

### Voiceover rules (user-mandated, applied to every module)

1. Open with **"Good day"** — never "good morning".
2. **Never reference courseware timing** — no session length, no break lengths, no
   "before you leave today", no "next session", no classroom durations. The only time
   reference allowed is the video's own length.
3. Use **"session"** and **"video length"** terminology, never "today".
4. Stage directions in square brackets are stripped — never narrated.
5. Abbreviations are written so the TTS reads them as spoken (lowercase for words,
   uppercase all-caps for letter-spelled acronyms).

## Content source

All session content (objectives, teaching notes, student notes, quizzes) is generated
from the Sec+revised content modules at `~/Documents/Hermes/Sec+revised/_build/s01.py`
… `s12.py`. The quizzes are copied verbatim from the Sec+revised session folders.

## Notes

- Vendor-neutral. This is an independent revision pack, not an official CompTIA
  publication, and it is not endorsed by CompTIA.
- Footer branding: `© Billy Forrest`.

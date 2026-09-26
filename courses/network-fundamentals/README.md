# Network Fundamentals + CompTIA Security+ SY0-701

TRAINING @ FORREST.ONE (Fozzie bear) themed course pack. Twelve sessions of three hours:
sessions 1-3 build the **network foundation**, sessions 4-12 cover the
**Security+ SY0-701** syllabus. This pack mirrors the structure of the
UKAIC AI Foundation course pack.

## This is a webapp

Open `index.html` in a browser, or run the preview server for full video
seeking:

```bash
cd ~/Desktop/"Network & Sec +"
python3 serve.py              # http://127.0.0.1:8123
python3 serve.py 9000         # different port
```

**Use `serve.py`, not `python -m http.server`.** The built-in server answers
Range requests with HTTP 200 and no `Content-Range`, so HTML5 video cannot seek
and the chapter buttons do nothing. `serve.py` returns 206 Partial Content and
the videos seek properly. Deployed hosts (nginx, Apache, GitHub Pages,
Cloudflare) all handle ranges correctly, so this only matters for local preview.

## Pages

| Page | What it holds |
|------|---------------|
| `index.html` | Course overview, 12 session cards with cover art |
| `sessions.html` | The 12 sessions grouped into 4 strands |
| `sessions/session-NN-*.html` | Per session: video, materials, progress tracker, core concepts, cautions, exam tips, key terms, self-check, further reading |
| `scheme-of-work.html` | Full delivery plan, per-session outcomes, assessment model |
| `quizzes.html` | 12 interactive quizzes (20 questions each) |
| `final-exam.html` | SY0-701 format, domain weightings, preparation plan |
| `glossary.html` | 216 key terms, A-Z, tagged with the source session |
| `resources.html` | Every file plus the reference texts and RFCs |
| `404.html` | Not-found page |

## Build

```bash
python3 _build_site.py
```

Regenerates all 20 pages from `_data/` plus the on-disk inventory. The resource
links are computed at build time by checking what actually exists, so the site
can never link to a missing file.

```
_data/session_content.json   concepts, cautions, self-check, exam tips, reading
_data/glossary.json          216 term -> definition -> session
_data/frames.json            frame counts and chapter markers per session
```

## Layout

```
assets/css/style.css    the whole MCA theme (charcoal + #C64200 orange-red)
assets/js/site.js       theme toggle, mobile nav, chapter seeking, progress
assets/fozzie/          Fozzie bear brand marks (see note below)
assets/img/             per-session cover art + instructional figures
decks/sessionNN/        objectives, slides (PDF+PPTX), notes, script
quizzes/                12 interactive HTML quizzes
videos/                 12 narrated MP4s + chapter JSON
notes/                  consolidated student notes and handout PDFs
serve.py                local preview server with byte-range support
```

## Branding note

`assets/fozzie/fozzie_logo.png` is the transparent bear head mark.
**It cannot be placed on a dark background**: 62.8% of its opaque pixels are
dark (the black M and A) and 0% are bright, so it vanishes on charcoal.
`assets/fozzie/fozzie_head_wide.png` is the landscape head banner used on slide footers, which
is what the header and footer use. Regenerate the chip if the logo changes.

The brand accent is `#C64200`, sampled from the saturated pixels of the
wordmark, not the crimson first assumed.

## Narration and video pipeline

Audio is generated on the **remote WSL2 box** with Qwen3-TTS (`qwen-tts` conda
env, model `Qwen/Qwen3-TTS-12Hz-1.7B-Base`), cloning the voice from
`~/reference.wav` on that box. There is no cloud TTS provider in this pipeline.

Build scripts live in `~/.hermes/profiles/crest/tts/sec_s1/`:

| Script | Purpose |
|--------|---------|
| `gen_qwen.py` | WSL-side generator (runs inside the qwen-tts env) |
| `run_render_all.sh` | WSL-side batch runner, two sessions at a time |
| `qwen_tts_step.py` | Orchestrator: sync text, render remote, pull back |
| `convert_local.sh` | WAV to MP3 with the local ffmpeg (WSL has none) |
| `build_video.py` | frames + audio -> MP4 + chapter JSON, one session |
| `build_all_videos.sh` | every session whose audio is complete |
| `check_clips.py` | duration audit and targeted re-render of runaways |

**Never run more than two Qwen generations at once**; the WSL GPU contends.

### Two defects that recur, and the guards for them

1. **Runaway clips.** The sampler occasionally renders a line at 2-40x its
   natural duration. `gen_qwen.py` caps `max_new_tokens` per line from the word
   count, which bounds the damage but does not prevent it. `check_clips.py`
   audits every clip against its expected duration and re-renders offenders:
   always run it before building a video.
2. **Byte ranges.** See the server note above.

## Voiceover style rules

- Say "good day", never "good morning" or "good afternoon".
- Never mention courseware timing; only reference the length of the video.
- Natural pace, never sped up, never compressed to a target duration.
- Spell abbreviations the engine would read as letters (`ack`, `syn-ack`).
- Write numeric notation as words (`ten dot ten dot ten dot zero`, `slash twenty-six`).

## Credits

CompTIA and Security+ are trademarks of CompTIA, Inc. This is an independent
training pack and is not endorsed by CompTIA. Course content is original and
vendor-neutral. (c) Billy Forrest.

#!/usr/bin/env python3
"""Network Fundamentals course site builder.

Generates the full static site (index, sessions, quizzes, notes, glossary,
final exam) from the Sec+revised content modules (s01..s12.py) plus the
session quiz HTML files. Mirrors the UKAIC AI Foundation site structure.

Run:  python3 _build_site.py
"""
import os, re, sys, html, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = "/home/billy-forrest/Documents/Hermes/Sec+revised/_build"
QUIZ_SRC = "/home/billy-forrest/Documents/Hermes/Sec+revised"
sys.path.insert(0, SRC)

COURSE = "Network Fundamentals"
COURSE_FULL = "Network Fundamentals + CompTIA Security+ SY0-701"
KICKER = "Network Fundamentals + CompTIA Security+ SY0-701"
FOOTER = "© 2026 Billy Forrest"

# ---------------------------------------------------------------- sessions
SESSIONS = [
    dict(n=1,  slug="session-01-network-foundations",
         title="Network Foundations: Networking Models & IP Addressing"),
    dict(n=2,  slug="session-02-switching-vlans",
         title="Switching, VLANs & Network Architectures"),
    dict(n=3,  slug="session-03-network-services",
         title="Network Services & the Attack Surface"),
    dict(n=4,  slug="session-04-security-concepts",
         title="Fundamental Security Concepts"),
    dict(n=5,  slug="session-05-threats",
         title="Threats, Attack Types & Threat Actors"),
    dict(n=6,  slug="session-06-cryptography",
         title="Cryptography & Public Key Infrastructure"),
    dict(n=7,  slug="session-07-identity-access",
         title="Identity & Access Management"),
    dict(n=8,  slug="session-08-enterprise-network-security",
         title="Enterprise Network Security: Firewalls, IDS, IPS, VPNs & Secure Protocols"),
    dict(n=9,  slug="session-09-endpoint-application-cloud",
         title="Endpoint, Application, Cloud & Virtualisation Security"),
    dict(n=10, slug="session-10-vulnerability-management",
         title="Vulnerability Management, Resiliency & Asset Protection"),
    dict(n=11, slug="session-11-security-operations",
         title="Security Operations: Monitoring, IR & Forensics"),
    dict(n=12, slug="session-12-governance-risk-compliance",
         title="Governance, Risk, Compliance & Exam Consolidation"),
]

# ---------------------------------------------------------------- content
def load_module(n):
    mod = __import__("s%02d" % n)
    return mod

def esc(s):
    return html.escape(str(s), quote=False)

def render_blocks(blocks, depth=0):
    """Render content-module blocks (h1,h2,h3,p,ul,ol,tbl,cal) to HTML."""
    out = []
    for kind, text in blocks:
        if kind == "h1":
            out.append("<h1>%s</h1>" % esc(text))
        elif kind == "h2":
            out.append("<h2>%s</h2>" % esc(text))
        elif kind == "h3":
            out.append("<h3>%s</h3>" % esc(text))
        elif kind == "p":
            out.append("<p>%s</p>" % esc(text))
        elif kind in ("ul", "ol"):
            tag = "ul" if kind == "ul" else "ol"
            items = "".join("<li>%s</li>" % esc(i) for i in text)
            out.append("<%s>%s</%s>" % (tag, items, tag))
        elif kind == "tbl":
            header, rows, widths = text
            thead = "".join("<th>%s</th>" % esc(h) for h in header)
            body = ""
            for r in rows:
                body += "<tr>" + "".join("<td>%s</td>" % esc(c) for c in r) + "</tr>"
            out.append('<div class="tablewrap"><table><thead><tr>%s</tr></thead>'
                       '<tbody>%s</tbody></table></div>' % (thead, body))
        elif kind == "cal":
            title, body = text
            out.append('<div class="note"><h3>%s</h3><p>%s</p></div>' % (esc(title), esc(body)))
    return "\n".join(out)

def learning_outcomes(mod):
    """Extract the learning-outcomes bullet list from OBJECTIVES_SECTIONS."""
    for kind, text in mod.OBJECTIVES_SECTIONS:
        if kind == "ul":
            return text
    return []

def teaching_notes(mod):
    """Extract the 'Core concepts' section from STUDENT_SECTIONS."""
    blocks = []
    started = False
    for kind, text in mod.STUDENT_SECTIONS:
        if kind == "h2" and "Core concepts" in text:
            started = True
            continue
        if started:
            if kind == "h2":
                break
            blocks.append((kind, text))
    return blocks

def key_terms(mod):
    """Extract the key-terms table from STUDENT_SECTIONS."""
    for kind, text in mod.STUDENT_SECTIONS:
        if kind == "tbl":
            header, rows, widths = text
            if header and header[0] == "Term":
                return rows
    return []

def session_areas(mod):
    """Extract the coverage table rows (ID, Area) from OBJECTIVES_SECTIONS."""
    for kind, text in mod.OBJECTIVES_SECTIONS:
        if kind == "tbl":
            header, rows, widths = text
            if header and header[0] == "ID":
                return rows
    return []

# ---------------------------------------------------------------- shell
NAV = [
    ("index.html", "Home"),
    ("sessions.html", "Sessions"),
    ("quizzes.html", "Quizzes"),
    ("final-exam.html", "Final Exam"),
    ("notes.html", "Student Notes"),
    ("glossary.html", "Glossary"),
]

def shell(page, title, desc, current, body, rel=""):
    nav = ['<li><a href="/courses/">Courses</a></li>']
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        nav.append('<li><a href="%s%s"%s>%s</a></li>' % (rel, href.replace('.html',''), cur, label))
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <meta name="description" content="{esc(desc)}"/>
  <title>{esc(title)}</title>
  <link rel="icon" type="image/svg+xml" href="{rel}assets/favicon.svg"/>
  <link rel="stylesheet" href="{rel}assets/css/style.css"/>
  <link rel="stylesheet" href="{rel}assets/css/app.css?v=2"/>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header role="banner">
  <div class="hwrap">
    <div class="brandrow">
      <div class="brand">
        <p class="kicker">{KICKER}</p>
        <p class="sitebrand"><a href="{rel}index">{COURSE}</a></p>
      </div>
      <button class="themebtn" id="themeToggle" type="button" aria-pressed="false">&#9789; Dark mode</button>
    </div>
    <button class="nav-toggle" id="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav">Menu</button>
    <nav class="mainnav" id="main-nav" aria-label="Main">
      <ul>
{chr(10).join(nav)}
      </ul>
    </nav>
  </div>
</header>

<main id="main">
{body}
</main>

<script src="{rel}assets/js/site.js"></script>
<script src="{rel}assets/js/app.js"></script>
<footer role="contentinfo">
  <div class="fwrap">
    <p>{FOOTER}</p>
    <p><strong>{COURSE_FULL}.</strong> Twelve sessions: sessions 1&ndash;3 build the network foundation; sessions 4&ndash;12 cover the Security+ core.</p>
    <p>Training material is original and vendor-neutral. This is an independent revision pack, not an official CompTIA publication, and it is not endorsed by CompTIA.</p>
  </div>
</footer>
</body>
</html>
"""

# ---------------------------------------------------------------- pages
def build_index():
    body = f"""
  <section class="hero">
    <h1>{COURSE}, Course Pack</h1>
    <p class="lede">A complete revision pack for the {COURSE_FULL} course. Twelve sessions, section quizzes, the twelve session videos and a practice paper.</p>
    <div class="pills">
      <span class="pill">12 Sessions</span>
      <span class="pill">Network foundation + Security+ core</span>
      <span class="pill">Vendor-neutral</span>
    </div>
  </section>

  <h2 id="start">Start here</h2>
  <p class="sub">Everything you need, in the order you need it.</p>
  <p>
    <a class="cta" href="sessions">Explore the twelve sessions</a>
    <a class="cta ghost" href="quizzes">Take a section quiz</a>
  </p>

  <div class="note">
    <h2>How the course is organised</h2>
    <p>Sessions 1&ndash;3 build the network foundation: models, addressing, switching, services.
      Sessions 4&ndash;12 cover the Security+ core: fundamental concepts, threats, cryptography,
      identity, network security, endpoint and cloud security, vulnerability management,
      security operations, and governance, risk and compliance.</p>
  </div>
"""
    return shell("index.html", f"{COURSE}, Course Pack",
                 f"Complete revision pack for the {COURSE_FULL} course: twelve sessions, section quizzes and a practice paper.",
                 "index.html", body)

def build_sessions():
    cards = []
    for s in SESSIONS:
        mod = load_module(s["n"])
        areas = session_areas(mod)
        area_list = "".join("<li>%s &mdash; %s</li>" % (esc(a[0]), esc(a[1])) for a in areas)
        cards.append(f"""
    <a class="card" href="sessions/{s['slug']}">
      <span class="weight">Session {s['n']}</span>
      <h2>{esc(s['title'])}</h2>
      <p>{esc(mod.SUBTITLE)}</p>
      <ul>
{area_list}
      </ul>
    </a>""")
    body = f"""
  <section class="hero">
    <h1>The Twelve Sessions</h1>
    <p class="lede">The course is divided into twelve sessions: a three-session network foundation followed by the nine-session Security+ core.</p>
  </section>

  <div class="note">
    <h2>How to read a session</h2>
    <p>Each session page lists the <strong>areas</strong> it covers, the <strong>learning outcomes</strong>
      a candidate should be able to demonstrate, and the <strong>resources</strong> available for that
      session, including the narrated session video and the section quiz.</p>
  </div>

  <div class="grid">
{chr(10).join(cards)}
  </div>"""
    return shell("sessions.html", "The Twelve Sessions, " + COURSE + ", Course Pack",
                 "All twelve sessions of the Network Fundamentals + Security+ course with their areas, learning outcomes and resources.",
                 "sessions.html", body)

def build_session_page(s):
    mod = load_module(s["n"])
    outcomes = learning_outcomes(mod)
    aims = "".join("<li>%s</li>" % esc(o) for o in outcomes)
    notes = render_blocks(teaching_notes(mod))
    areas = session_areas(mod)
    area_pills = "".join('<span class="pill">%s</span>' % esc(a[0]) for a in areas)
    prev = SESSIONS[s["n"] - 2] if s["n"] > 1 else None
    nxt = SESSIONS[s["n"]] if s["n"] < 12 else None
    pager = []
    if prev:
        pager.append('<a class="navbtn" href="%s">&#8592; Session %d</a>' % (prev["slug"], prev["n"]))
    pager.append('<a class="navbtn" href="../sessions">Sessions</a>')
    if nxt:
        pager.append('<a class="navbtn" href="%s">Session %d &#8594;</a>' % (nxt["slug"], nxt["n"]))
    body = f"""
<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="../index">Home</a></li><li><a href="../sessions">Sessions</a></li><li aria-current="page">Session {s['n']}</li></ol></nav>
  <section class="hero">
    <span class="weight" style="font-size:.78rem;font-weight:bold;letter-spacing:1px;text-transform:uppercase;color:#2f6fb5">Session {s['n']} of 12</span>
    <h1>{esc(s['title'])}</h1>
    <p class="lede">{esc(mod.SUBTITLE)}</p>
    <div class="pills">
{area_pills}
    </div>
  </section>
  <h2 id="video">Session video</h2>
  <p class="sub">Narrated walkthrough of this session.</p>
  <video controls preload="metadata" playsinline style="width:100%;max-width:640px;border-radius:8px;display:block" >
    <source src="../videos/{s['slug']}.mp4" type="video/mp4"/>
    Your browser does not support the video tag.
  </video>

  <h2 id="outcomes">Learning outcomes</h2>
  <p class="sub">By the end of this session, candidates will be able to:</p>
  <div class="aims">
    <ul>
{aims}
    </ul>
  </div>
  <h2 id="resources">Section resources</h2>
  <p class="sub">One section quiz for this session.</p>
<ul class="reslist">
      <li><a class="resbtn" href="../quizzes/session-{s['n']:02d}-quiz"><span class="ico" aria-hidden="true">&#10004;</span>Section quiz <span class="status open">Open</span></a></li>
    </ul>

  <h2 id="areas">What this session is about</h2>
  <p class="sub">What this session covers, with teaching notes area by area.</p>
  <div class="teachnotes">
{notes}
  </div>
  <nav class="pager" aria-label="Page navigation">{' '.join(pager)}</nav>
"""
    return shell("sessions/%s.html" % s["slug"],
                 "Session %d: %s, %s, Course Pack" % (s["n"], s["title"], COURSE),
                 mod.SUBTITLE, "sessions.html", body, rel="../")

def build_quizzes():
    cards = []
    for s in SESSIONS:
        cards.append(f"""
    <a class="card" href="quizzes/session-{s['n']:02d}-quiz">
      <span class="weight">Session {s['n']}</span>
      <h2>{esc(s['title'])}</h2>
      <p>Twenty-question interactive quiz with immediate feedback and shuffled questions.</p>
    </a>""")
    body = f"""
  <section class="hero">
    <h1>Section Quizzes</h1>
    <p class="lede">One interactive quiz per session. Twenty questions, immediate feedback, shuffled order.</p>
  </section>

  <div class="note">
    <h2>How the quizzes work</h2>
    <p>Each quiz gives immediate feedback on every answer and explains the distractors as well as the
      correct option. Questions are shuffled on every load. Aim for seventy percent or better before
      moving on.</p>
  </div>

  <div class="grid">
{chr(10).join(cards)}
  </div>"""
    return shell("quizzes.html", "Section Quizzes, " + COURSE + ", Course Pack",
                 "One interactive quiz per session of the Network Fundamentals + Security+ course.",
                 "quizzes.html", body)

def build_notes():
    sections = []
    for s in SESSIONS:
        mod = load_module(s["n"])
        blocks = []
        for kind, text in mod.STUDENT_SECTIONS:
            if kind == "h1":
                continue
            blocks.append((kind, text))
        sections.append('<h2 id="session-%d">Session %d: %s</h2>' % (s["n"], s["n"], esc(s["title"])))
        sections.append(render_blocks(blocks))
    body = f"""
  <section class="hero">
    <h1>Student Notes</h1>
    <p class="lede">The full student notes for all twelve sessions: key terms, core concepts, practical cautions, self-check questions and exam tips.</p>
  </section>
  <div class="toc">
    <h3>Jump to a session</h3>
    <ol>
{chr(10).join('      <li><a href="#session-%d">Session %d: %s</a></li>' % (s["n"], s["n"], esc(s["title"])) for s in SESSIONS)}
    </ol>
  </div>
  <div class="notes-body">
{chr(10).join(sections)}
  </div>"""
    return shell("notes.html", "Student Notes, " + COURSE + ", Course Pack",
                 "Full student notes for all twelve sessions of the Network Fundamentals + Security+ course.",
                 "notes.html", body)

def build_glossary():
    terms = []
    for s in SESSIONS:
        mod = load_module(s["n"])
        for row in key_terms(mod):
            if len(row) >= 2:
                terms.append((esc(row[0]), esc(row[1]), s["n"]))
    # dedupe by term
    seen = {}
    for t, d, n in terms:
        if t not in seen:
            seen[t] = (t, d, n)
    items = "".join('<p class="def"><strong>%s</strong> <span class="area">Session %d</span><br/>%s</p>' % (t, n, d) for t, d, n in sorted(seen.values(), key=lambda x: x[0].lower()))
    body = f"""
  <section class="hero">
    <h1>Glossary</h1>
    <p class="lede">Key terms from across the course, with the session where each is introduced.</p>
  </section>
  <div class="defs">
{items}
  </div>"""
    return shell("glossary.html", "Glossary, " + COURSE + ", Course Pack",
                 "Key terms from the Network Fundamentals + Security+ course with the session where each is introduced.",
                 "glossary.html", body)

def build_final_exam():
    body = f"""
  <section class="hero">
    <h1>Final Exam</h1>
    <p class="lede">A practice paper consolidating the whole course.</p>
  </section>

  <div class="note">
    <h2>About the exam</h2>
    <p>The Security+ SY0-701 examination is 90 questions in 90 minutes, with performance-based
      questions alongside multiple choice, and a pass mark of 750 out of 900. This pack's section
      quizzes and the practice paper prepare candidates for that format.</p>
  </div>

  <p>
    <a class="cta" href="quizzes/session-01-quiz">Start with Session 1</a>
    <a class="cta ghost" href="sessions">Review the sessions</a>
  </p>"""
    return shell("final-exam.html", "Final Exam, " + COURSE + ", Course Pack",
                 "Practice paper for the Network Fundamentals + Security+ course.",
                 "final-exam.html", body)

# ---------------------------------------------------------------- build
def copy_quizzes():
    """Copy the 12 quiz HTML files from Sec+revised into quizzes/."""
    import glob
    for s in SESSIONS:
        # session folders carry topic suffixes: "Session 01 - Network Foundations: ..."
        matches = glob.glob(os.path.join(QUIZ_SRC, "Session %02d*" % s["n"]))
        src = None
        if matches:
            cand = os.path.join(matches[0], "Quiz_Session_%02d.html" % s["n"])
            if os.path.exists(cand):
                src = cand
        dst = os.path.join(ROOT, "quizzes", "session-%02d-quiz.html" % s["n"])
        if src:
            shutil.copy(src, dst)
            print("  quiz %02d -> %s" % (s["n"], os.path.basename(dst)))
        else:
            print("  !! quiz %02d MISSING" % s["n"])

def main():
    os.makedirs(os.path.join(ROOT, "sessions"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "quizzes"), exist_ok=True)
    pages = {
        "index.html": build_index,
        "sessions.html": build_sessions,
        "quizzes.html": build_quizzes,
        "notes.html": build_notes,
        "glossary.html": build_glossary,
        "final-exam.html": build_final_exam,
    }
    for name, fn in pages.items():
        with open(os.path.join(ROOT, name), "w") as f:
            f.write(fn())
        print("  wrote %s" % name)
    for s in SESSIONS:
        with open(os.path.join(ROOT, "sessions", s["slug"] + ".html"), "w") as f:
            f.write(build_session_page(s))
        print("  wrote sessions/%s.html" % s["slug"])
    print("  copying quizzes...")
    copy_quizzes()
    print("done.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build Domain 4 and Domain 6 quizzes, then validate."""
import sys, subprocess, json, re
from pathlib import Path

sys.path.insert(0, "/home/billy-forrest/Documents/Hermes/UKAIC-AI-Foundation/quizzes")
from _build_lib import build
from _q_domain4 import Q4
from _q_domain6 import Q6
from _balance import balance_bank, audit_bank
balance_bank(Q4, seed=411)
balance_bank(Q6, seed=611)

print("Domain 4 question count:", len(Q4))
print("Domain 6 question count:", len(Q6))

p4 = build(
    title="UKAIC AI Foundation — Domain 4 Quiz: Prompt Engineering Fundamentals",
    header="Domain 4 Quiz — Prompt Engineering Fundamentals",
    subtitle="31 questions · 16% of the examination · Pass standard 70%",
    questions=Q4, passmark=70, outfile="domain4-prompt-engineering-quiz.html", seed=4047)

p6 = build(
    title="UKAIC AI Foundation — Domain 6 Quiz: Limitations, Risks & Hallucination",
    header="Domain 6 Quiz — Limitations, Risks &amp; Hallucination",
    subtitle="31 questions · 16% of the examination · Pass standard 70%",
    questions=Q6, passmark=70, outfile="domain6-limitations-hallucination-quiz.html", seed=6031)

# ---------- VALIDATION ----------
print("\n=== VALIDATION ===")
ok = True
for path, src, label in [(p4, Q4, "D4"), (p6, Q6, "D6")]:
    html = path.read_text(encoding="utf-8")
    # 1. no unreplaced markers
    for m in ["__TITLE__","__QJSON__","__N__","__PASS__","__HEADER__","__SUBTITLE__"]:
        if m in html:
            print(f"FAIL {label}: unreplaced {m}"); ok = False
    # 2. question count in embedded JSON
    mm = re.search(r"var Q = (\[.*?\]);\nvar PASS", html, re.S)
    if not mm:
        print(f"FAIL {label}: could not locate Q array"); ok = False; continue
    data = json.loads(mm.group(1))
    if len(data) != 31:
        print(f"FAIL {label}: {len(data)} questions in JSON, expected 31"); ok = False
    else:
        print(f"PASS {label}: 31 questions embedded")
    # 3. every question 4 opts, 4 why, valid ans
    for i, q in enumerate(data):
        if len(q["opts"]) != 4: print(f"FAIL {label} q{i}: {len(q['opts'])} opts"); ok=False
        if len(q["why"]) != 4:  print(f"FAIL {label} q{i}: {len(q['why'])} why"); ok=False
        if not (0 <= q["ans"] <= 3): print(f"FAIL {label} q{i}: ans={q['ans']}"); ok=False
    # 4. answer distribution
    dist = {0:0,1:0,2:0,3:0}
    for q in data: dist[q["ans"]] += 1
    print(f"     {label} answer distribution A/B/C/D = {dist[0]}/{dist[1]}/{dist[2]}/{dist[3]}")
    # 5. accessibility features
    checks = {
        "skip link": 'class="skip-link"' in html,
        "role=banner": 'role="banner"' in html,
        "role=main": 'role="main"' in html,
        "role=radiogroup": 'role="radiogroup"' in html,
        "aria-live": 'aria-live="polite"' in html,
        "prefers-reduced-motion": "prefers-reduced-motion" in html,
        "white bg": "--bg:#ffffff" in html,
        "navy text": "--navy:#002b5c" in html,
        "passcode 1234": "1234" in html,
    }
    for k, v in checks.items():
        if not v: print(f"FAIL {label}: missing {k}"); ok = False
    print(f"PASS {label}: accessibility features present")
    # 6. extract JS and node --check
    scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
    jscode = "\n".join(scripts)
    tmp = Path(f"/tmp/{label}_check.js")
    tmp.write_text(jscode, encoding="utf-8")
    r = subprocess.run(["node","--check",str(tmp)], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAIL {label}: node --check failed\n{r.stderr[:800]}"); ok = False
    else:
        print(f"PASS {label}: JS passes node --check")

print("\nOVERALL:", "ALL CHECKS PASSED" if ok else "FAILURES PRESENT")
sys.exit(0 if ok else 1)

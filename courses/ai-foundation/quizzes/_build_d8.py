#!/usr/bin/env python3
"""Build Domain 8 quiz, then validate structurally."""
import sys, subprocess, json, re
from pathlib import Path

sys.path.insert(0, "/home/billy-forrest/Documents/Hermes/UKAIC-AI-Foundation/quizzes")
from _build_lib import build
from _q_domain8 import Q
from _balance import balance_bank, audit_bank
balance_bank(Q, seed=811)

print("Domain 8 question count:", len(Q))

p8 = build(
    title="UKAIC AI Foundation — Domain 8 Quiz: Ethics, Bias, Responsible AI & Governance",
    header="Domain 8 Quiz — Ethics, Bias, Responsible AI &amp; Governance",
    subtitle="31 questions · 8% of the examination · Pass standard 70%",
    questions=Q, passmark=70, outfile="domain8-ethics-bias-governance-quiz.html", seed=8037)

print("\n=== VALIDATION ===")
ok = True
html = p8.read_text(encoding="utf-8")
for m in ["__TITLE__", "__QJSON__", "__N__", "__PASS__", "__HEADER__", "__SUBTITLE__"]:
    if m in html:
        print(f"FAIL: unreplaced {m}"); ok = False

mm = re.search(r"var Q = (\[.*?\]);\nvar PASS", html, re.S)
if not mm:
    print("FAIL: could not locate Q array"); ok = False
else:
    data = json.loads(mm.group(1))
    print(f"PASS: {len(data)} questions embedded (expected 31)")
    if len(data) != 31: ok = False
    for i, q in enumerate(data):
        if len(q["opts"]) != 4: print(f"FAIL q{i}: {len(q['opts'])} opts"); ok = False
        if len(q["why"]) != 4: print(f"FAIL q{i}: {len(q['why'])} why"); ok = False
        if not (0 <= q["ans"] <= 3): print(f"FAIL q{i}: ans={q['ans']}"); ok = False
        if not q.get("exp"): print(f"FAIL q{i}: no exp"); ok = False
    dist = {0: 0, 1: 0, 2: 0, 3: 0}
    for q in data: dist[q["ans"]] += 1
    print(f"     answer distribution A/B/C/D = {dist[0]}/{dist[1]}/{dist[2]}/{dist[3]}")

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
    if not v: print(f"FAIL: missing {k}"); ok = False
if all(checks.values()): print("PASS: accessibility features present")

scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
tmp = Path("/tmp/D8_check.js")
tmp.write_text("\n".join(scripts), encoding="utf-8")
r = subprocess.run(["node", "--check", str(tmp)], capture_output=True, text=True)
if r.returncode != 0:
    print(f"FAIL: node --check failed\n{r.stderr[:800]}"); ok = False
else:
    print("PASS: JS passes node --check")

print("\nOVERALL:", "ALL CHECKS PASSED" if ok else "FAILURES PRESENT")
sys.exit(0 if ok else 1)

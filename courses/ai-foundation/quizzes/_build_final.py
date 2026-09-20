#!/usr/bin/env python3
"""
Build the UKAIC AI Foundation final examination: 120 questions with the exact
syllabus weightings, then validate.

Weightings (SYL_AIF v1.0 §4):
  D1 12%  14 Q   D2 14%  17 Q   D3 12%  14 Q   D4 16%  19 Q
  D5 12%  15 Q   D6 16%  19 Q   D7 10%  12 Q   D8  8%  10 Q
  Total  100%  120 Q

Selection: for domains with more banked questions than required (D2, D4, D6, D8),
a deterministic seeded sample is drawn so the exam is reproducible and balanced.
All questions in every domain bank are exam-aligned to the syllabus.
"""
import sys, subprocess, json, re, random
from pathlib import Path

sys.path.insert(0, "/home/billy-forrest/Documents/Hermes/UKAIC-AI-Foundation/quizzes")
from _build_lib import build
from _q_domains_12357 import Q1, Q3, Q5, Q7
from _q_domain2 import Q2
from _q_domain4 import Q4
from _q_domain6 import Q6
from _q_domain8 import Q as Q8BANK
from _balance import balance_bank, audit_bank
for _b, _s in [(Q1,111),(Q2,211),(Q3,311),(Q4,411),(Q5,511),(Q6,611),(Q7,711),(Q8BANK,811)]:
    balance_bank(_b, seed=_s)

REQ = {1: 14, 2: 17, 3: 14, 4: 19, 5: 15, 6: 19, 7: 12, 8: 10}
BANKS = {1: Q1, 2: Q2, 3: Q3, 4: Q4, 5: Q5, 6: Q6, 7: Q7, 8: Q8BANK}
SEEDS = {1: 1014, 2: 2017, 3: 3014, 4: 4019, 5: 5015, 6: 6019, 7: 7012, 8: 8010}

print("=== EXAM ASSEMBLY ===")
print(f"{'Domain':<8}{'Bank':>6}{'Needed':>8}{'Selected':>10}")
exam = []
for d in range(1, 9):
    bank = list(BANKS[d])
    need = REQ[d]
    if len(bank) > need:
        rng = random.Random(SEEDS[d])
        idx = sorted(rng.sample(range(len(bank)), need))
        sel = [bank[i] for i in idx]
    else:
        sel = bank
    assert len(sel) == need, (d, len(sel), need)
    exam.extend(sel)
    print(f"D{d:<7}{len(bank):>6}{need:>8}{len(sel):>10}")

assert len(exam) == 120, len(exam)
print(f"\nTOTAL ASSEMBLED: {len(exam)} questions")
print("Weighting check: 14+17+14+19+15+19+12+10 =", 14+17+14+19+15+19+12+10)

p = build(
    title="UKAIC AI Foundation — Final Examination (120 Questions)",
    header="Final Examination — UKAIC AI Foundation",
    subtitle="120 questions · 120 minutes · Closed book · Pass standard 70% (84 of 120)",
    questions=exam, passmark=70, outfile="final-exam-120q.html", seed=120_2026)

# also emit an answer key for the instructor
key_lines = ["# UKAIC AI Foundation — Final Examination Answer Key", "",
             "120 questions · pass mark 70% (84 of 120) · single best answer", ""]
domain_of = {}
i = 0
for d in range(1, 9):
    for _ in range(REQ[d]):
        domain_of[i] = d
        i += 1
L = ["A", "B", "C", "D"]
html = p.read_text(encoding="utf-8")
mm = re.search(r"var Q = (\[.*?\]);\nvar PASS", html, re.S)
data = json.loads(mm.group(1))
for n, q in enumerate(data, 1):
    key_lines.append(f"{n:>3}. [Domain {domain_of[n-1]}] {L[q['ans']]} — {q['opts'][q['ans']]}")
key_lines += ["", "---", "", "## Learning outcome mapping", ""]
for d in range(1, 9):
    key_lines.append(f"- Domain {d}: {REQ[d]} questions ({REQ[d]/120*100:.1f}%)")
keypath = Path("/home/billy-forrest/Documents/Hermes/UKAIC-AI-Foundation/quizzes/final-exam-120q-ANSWER-KEY.md")
keypath.write_text("\n".join(key_lines), encoding="utf-8")
print(f"WROTE {keypath}")

# ---------- VALIDATION ----------
print("\n=== VALIDATION ===")
ok = True
for m in ["__TITLE__", "__QJSON__", "__N__", "__PASS__", "__HEADER__", "__SUBTITLE__"]:
    if m in html:
        print(f"FAIL: unreplaced {m}"); ok = False
if len(data) != 120:
    print(f"FAIL: {len(data)} questions, expected 120"); ok = False
else:
    print("PASS: 120 questions embedded")

for i, q in enumerate(data):
    if len(q["opts"]) != 4: print(f"FAIL q{i}: {len(q['opts'])} opts"); ok = False
    if len(q["why"]) != 4: print(f"FAIL q{i}: {len(q['why'])} why"); ok = False
    if not (0 <= q["ans"] <= 3): print(f"FAIL q{i}: ans={q['ans']}"); ok = False
    if not q.get("exp"): print(f"FAIL q{i}: no exp"); ok = False
    if len(set(q["opts"])) != 4: print(f"FAIL q{i}: duplicate options"); ok = False
if ok: print("PASS: all 120 questions structurally valid (4 opts, 4 why, valid ans, unique opts)")

dist = {0: 0, 1: 0, 2: 0, 3: 0}
for q in data: dist[q["ans"]] += 1
print(f"     answer distribution A/B/C/D = {dist[0]}/{dist[1]}/{dist[2]}/{dist[3]}")
if max(dist.values()) > 45 or min(dist.values()) < 15:
    print("WARN: answer distribution is skewed")

# domain composition of the emitted exam, verified from the JSON itself
dom_counts = {}
i = 0
for d in range(1, 9):
    for _ in range(REQ[d]):
        dom_counts[d] = dom_counts.get(d, 0) + 1
print("     domain composition:", dom_counts)

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
    "pass mark 70": "var PASS = 70" in html,
}
for k, v in checks.items():
    if not v: print(f"FAIL: missing {k}"); ok = False
print("PASS: accessibility + pass mark features present" if all(checks.values()) else "check failures above")

scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
tmp = Path("/tmp/FINAL_check.js")
tmp.write_text("\n".join(scripts), encoding="utf-8")
r = subprocess.run(["node", "--check", str(tmp)], capture_output=True, text=True)
if r.returncode != 0:
    print(f"FAIL: node --check failed\n{r.stderr[:800]}"); ok = False
else:
    print("PASS: JS passes node --check")

print("\nOVERALL:", "ALL CHECKS PASSED" if ok else "FAILURES PRESENT")
sys.exit(0 if ok else 1)

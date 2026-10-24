#!/usr/bin/env python3
"""
Verify all three user-stated assessment rules across every paper:
  RULE 1  the longest option is not the correct answer (no length tell)
  RULE 2  copy/paste, selection, context menu and devtools are disabled
  RULE 3  questions are randomised at runtime

Also re-checks the why[]/opts[] alignment so the balance pass cannot have broken it.
"""
import json, re, sys, subprocess
from pathlib import Path

BASE = Path("/home/billy-forrest/Documents/Hermes/UKAIC-AI-Foundation/quizzes")
PAPERS = ["domain4-prompt-engineering-quiz.html",
          "domain6-limitations-hallucination-quiz.html",
          "domain8-ethics-bias-governance-quiz.html",
          "final-exam-120q.html"]

def load(p):
    h = (BASE / p).read_text(encoding="utf-8")
    return h, json.loads(re.search(r"var Q = (\[.*?\]);\nvar PASS", h, re.S).group(1))

ok = True

print("=" * 76)
print("RULE 1 — longest option must not be the correct answer")
print("=" * 76)
for f in PAPERS:
    h, d = load(f)
    n = len(d)
    strictly = sum(1 for q in d if (lambda L: L[q["ans"]] == max(L) and L.count(max(L)) == 1)([len(o) for o in q["opts"]]))
    mean_c = sum(len(q["opts"][q["ans"]]) for q in d) / n
    mean_o = sum(sum(len(o) for j, o in enumerate(q["opts"]) if j != q["ans"]) / 3 for q in d) / n
    pct = strictly / n * 100
    verdict = "OK" if pct <= 28 else "TELL PRESENT"
    if pct > 28: ok = False
    print(f"  {f:<44} {strictly:>3}/{n:<4} = {pct:5.1f}%  ratio {mean_c/mean_o:.2f}  {verdict}")

print()
print("=" * 76)
print("RULE 1b — answer position must be spread (no 'always answer B' tell)")
print("=" * 76)
for f in PAPERS:
    h, d = load(f)
    n = len(d)
    dist = [sum(1 for q in d if q["ans"] == i) for i in range(4)]
    pct = [x / n * 100 for x in dist]
    spread = max(pct) - min(pct)
    verdict = "OK" if spread <= 10 else "SKEWED"
    if spread > 10: ok = False
    print(f"  {f:<44} A/B/C/D={pct[0]:.0f}/{pct[1]:.0f}/{pct[2]:.0f}/{pct[3]:.0f}%   "
          f"spread {spread:4.1f}pp  {verdict}")

print()
print("=" * 76)
print("RULE 2 — copy/paste protection")
print("=" * 76)
for f in PAPERS:
    h, _ = load(f)
    c = {
        "user-select:none": "user-select:none" in h.replace(" ", ""),
        "contextmenu blocked": "'contextmenu'" in h,
        "copy/cut blocked": "'copy'" in h and "'cut'" in h,
        "Ctrl+C/X/A/U/S/P blocked": all(x in h for x in ["'c'", "'x'", "'a'", "'u'", "'s'", "'p'"]),
        "F12 blocked": "'F12'" in h,
        "selectstart blocked": "'selectstart'" in h,
        "aria-live toast": 'id="toast"' in h and 'aria-live="polite"' in h,
    }
    bad = [k for k, v in c.items() if not v]
    if bad: ok = False
    print(f"  {f:<44} {'ALL PRESENT' if not bad else 'MISSING: ' + ', '.join(bad)}")

print()
print("=" * 76)
print("RULE 3 — runtime question randomisation")
print("=" * 76)
for f in PAPERS:
    h, _ = load(f)
    has = "shuffleQuestions" in h
    if not has: ok = False
    print(f"  {f:<44} runtime shuffle {'PRESENT' if has else 'MISSING'}")

print()
print("=" * 76)
print("REGRESSION — why[]/opts[] alignment must survive the balance pass")
print("=" * 76)
for f in PAPERS:
    h, d = load(f)
    bad = [i for i, q in enumerate(d)
           if [j for j, w in enumerate(q["why"]) if re.match(r"^\s*Correct\.", w, re.I)] != [q["ans"]]]
    if bad: ok = False
    print(f"  {f:<44} {'all aligned' if not bad else 'MISALIGNED at ' + str(bad[:6])}")

print()
print("=" * 76)
print("REGRESSION — structural integrity + JS syntax")
print("=" * 76)
for f in PAPERS:
    h, d = load(f)
    probs = []
    if not all(len(q["opts"]) == 4 for q in d): probs.append("opts!=4")
    if not all(len(q["why"]) == 4 for q in d): probs.append("why!=4")
    if not all(len(set(q["opts"])) == 4 for q in d): probs.append("dup opts")
    if not all(q.get("exp") for q in d): probs.append("no exp")
    js = "\n".join(re.findall(r"<script>(.*?)</script>", h, re.S))
    tmp = Path(f"/tmp/{f}.js"); tmp.write_text(js, encoding="utf-8")
    r = subprocess.run(["node", "--check", str(tmp)], capture_output=True, text=True)
    if r.returncode != 0: probs.append("JS syntax: " + r.stderr[:120])
    if probs: ok = False
    print(f"  {f:<44} {'clean' if not probs else '; '.join(probs)}")

print()
print("=" * 76)
print("RESULT:", "ALL THREE RULES SATISFIED" if ok else "VIOLATIONS REMAIN")
sys.exit(0 if ok else 1)

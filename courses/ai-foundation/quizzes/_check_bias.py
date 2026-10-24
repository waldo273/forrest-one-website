#!/usr/bin/env python3
"""
Longest-answer-bias audit + alignment audit.

Rule (user requirement): "no longest question is the right answer". A learner must
not be able to score well by always picking the longest or most detailed option.

Metrics per paper:
  - correct-is-strictly-longest rate  (random baseline ~25%, flag if >40%)
  - correct-longer-than-mean-distractor rate (baseline ~50%, flag if >70%)
  - mean length gap between correct and mean distractor (flag if >25 chars)
"""
import json, re, sys, statistics
from pathlib import Path

QDIR = Path("/home/billy-forrest/Documents/Hermes/UKAIC-AI-Foundation/quizzes")

PAPERS = [
    "domain4-prompt-engineering-quiz.html",
    "domain6-limitations-hallucination-quiz.html",
    "domain8-ethics-bias-governance-quiz.html",
    "final-exam-120q.html",
]

def load(p):
    h = p.read_text(encoding="utf-8")
    m = re.search(r"var Q = (\[.*?\]);\nvar PASS", h, re.S)
    return json.loads(m.group(1)) if m else None

def audit(path):
    data = load(path)
    if data is None:
        return None, "no Q array found"
    n = len(data)
    strict_longest = 0
    longer_than_mean = 0
    gaps = []
    for q in data:
        L = [len(o) for o in q["opts"]]
        ansl = L[q["ans"]]
        mx = max(L)
        if ansl == mx and L.count(mx) == 1:
            strict_longest += 1
        mean_wrong = statistics.mean([l for i, l in enumerate(L) if i != q["ans"]])
        if ansl > mean_wrong:
            longer_than_mean += 1
        gaps.append(ansl - mean_wrong)
    return {
        "n": n,
        "strict_longest_pct": 100 * strict_longest / n,
        "longer_than_mean_pct": 100 * longer_than_mean / n,
        "mean_gap": statistics.mean(gaps),
    }, None

print("=" * 74)
print("LONGEST-ANSWER-BIAS AUDIT  (user rule: longest option must NOT be the answer)")
print("=" * 74)
allok = True
for name in PAPERS:
    p = QDIR / name
    if not p.exists():
        print(f"SKIP {name}: not present"); continue
    res, err = audit(p)
    if err:
        print(f"FAIL {name}: {err}"); allok = False; continue
    sl, lm, gap = res["strict_longest_pct"], res["longer_than_mean_pct"], res["mean_gap"]
    flags = []
    if sl > 40: flags.append(f"strict-longest {sl:.0f}% > 40%")
    if lm > 70: flags.append(f"longer-than-mean {lm:.0f}% > 70%")
    if gap > 25: flags.append(f"mean gap {gap:.1f} > 25 chars")
    status = "PASS" if not flags else "FAIL"
    if flags: allok = False
    print(f"{status} {name}")
    print(f"      n={res['n']}  strict-longest={sl:.0f}%  longer-than-mean={lm:.0f}%  mean-gap={gap:+.1f} chars")
    for f in flags:
        print(f"      -> {f}")

print("\nBIAS RESULT:", "ALL WITHIN TOLERANCE" if allok else "BIAS PRESENT")
sys.exit(0 if allok else 1)

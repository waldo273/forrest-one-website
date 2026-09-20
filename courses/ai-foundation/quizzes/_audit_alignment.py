#!/usr/bin/env python3
"""
Rebuild all quizzes and verify the why[]/opts[] alignment bug is fixed.

The bug: scramble() reordered opts[] and updated ans, but left why[] in its
original order, so every explanation rendered under the wrong option letter.
This script rebuilds every paper and asserts that for each question the
why[] entry at index `ans` is the one that begins "Correct".
"""
import sys, json, re, subprocess
from pathlib import Path

sys.path.insert(0, "/home/billy-forrest/Documents/Hermes/UKAIC-AI-Foundation/quizzes")

PAPERS = [
    ("_q_domain4", "Q4", "domain4-prompt-engineering-quiz.html"),
    ("_q_domain6", "Q6", "domain6-limitations-hallucination-quiz.html"),
    ("_q_domain8", "Q", "domain8-ethics-bias-governance-quiz.html"),
]

def audit(path, label):
    html = path.read_text(encoding="utf-8")
    data = json.loads(re.search(r"var Q = (\[.*?\]);\nvar PASS", html, re.S).group(1))
    bad = []
    for i, q in enumerate(data):
        if len(q["why"]) != 4 or len(q["opts"]) != 4:
            bad.append((i, "wrong array length")); continue
        # Match only the sentence-initial marker "Correct." / "Wrong." so that a
        # distractor text containing the word "correct" (e.g. "Correct formatting...")
        # is not misread as the correct-answer explanation.
        correct_marks = [j for j, w in enumerate(q["why"])
                         if re.match(r"^\s*Correct\.", w, re.I)]
        if correct_marks != [q["ans"]]:
            bad.append((i, f"why-Correct at {correct_marks}, ans={q['ans']}"))
    return len(data), bad

print("=" * 62)
print("REBUILD + ALIGNMENT AUDIT")
print("=" * 62)

# rebuild
for mod, attr, fname in PAPERS:
    m = __import__(mod)
    bank = getattr(m, attr)
    # rebuild via each paper's own builder to keep seeds identical
    print(f"pending rebuild: {fname} ({len(bank)} in bank)")

import subprocess as sp
for script in ["_build_d4_d6.py", "_build_d8.py", "_build_final.py"]:
    r = sp.run(["../.venv/bin/python", script], capture_output=True, text=True,
               cwd="/home/billy-forrest/Documents/Hermes/UKAIC-AI-Foundation/quizzes")
    status = "ok" if r.returncode == 0 else f"EXIT {r.returncode}"
    print(f"\n--- {script}: {status} ---")
    for line in r.stdout.splitlines():
        if any(k in line for k in ["WROTE", "OVERALL", "FAIL", "distribution", "TOTAL"]):
            print("   ", line)
    if r.returncode != 0:
        print("   STDERR:", r.stderr[-600:])

print("\n" + "=" * 62)
print("ALIGNMENT AUDIT (why[] must match opts[])")
print("=" * 62)
allok = True
for fname in ["domain4-prompt-engineering-quiz.html",
              "domain6-limitations-hallucination-quiz.html",
              "domain8-ethics-bias-governance-quiz.html",
              "final-exam-120q.html"]:
    p = Path("/home/billy-forrest/Documents/Hermes/UKAIC-AI-Foundation/quizzes") / fname
    n, bad = audit(p, fname)
    if bad:
        allok = False
        print(f"FAIL {fname}: {len(bad)} misaligned of {n}")
        for i, msg in bad[:5]:
            print(f"      q{i}: {msg}")
    else:
        print(f"PASS {fname}: all {n} questions aligned")

print("\nALIGNMENT RESULT:", "ALL ALIGNED" if allok else "MISALIGNMENTS REMAIN")
sys.exit(0 if allok else 1)

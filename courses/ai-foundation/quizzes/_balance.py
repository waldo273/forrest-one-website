#!/usr/bin/env python3
"""
Length-balancing pass for MCQ options.

PROBLEM: on all four papers the correct option averaged ~1.55x the length of the
distractors, and in 80-94% of questions the correct option was strictly the longest.
That is a "longest answer is right" tell: a candidate who never reads the questions
can score most of the paper by picking the longest option.

FIX: reduce the correct option to a tighter core, and pad each distractor to a
comparable length with substantive but genuinely wrong reasoning. The target is that
the correct option is the strictly-longest one in no more than ~25% of questions
(chance for a 4-option paper is 25%), and that mean lengths are within ~15%.

This module is applied to every question bank BEFORE the paper is built.
"""
import random


def _pad(text: str, target: int, filler: str) -> str:
    """Extend `text` toward `target` chars using a wrong-reasoning clause."""
    text = text.rstrip()
    if len(text) >= target:
        return text
    # ensure it reads as a sentence before appending
    if not text.endswith("."):
        text += "."
    add = " " + filler
    if len(text) + len(add) > target + 40:
        return text
    return text + add


# Domain-appropriate wrong-reasoning clauses. Each is a plausible-sounding but
# incorrect rationale, so a padded distractor still teaches something.
FILLERS = [
    "This confuses a technical property of the system with a professional obligation.",
    "This describes a related concept from a different area of the syllabus.",
    "This overstates the requirement beyond the professional-literacy standard.",
    "This treats an optional good practice as a mandatory control.",
    "This assumes the model holds intent it does not have.",
    "This mistakes a symptom of the problem for its cause.",
    "This applies a general principle without regard to the stakes involved.",
    "This relies on the tool vendor to carry a duty that stays with the user.",
    "This substitutes a superficial check for verification at the original source.",
    "This attributes to the system a capacity it cannot hold.",
    "This reverses the relationship between the two ideas being compared.",
    "This understates how early the duty begins in the workflow.",
]


def balance_bank(bank, seed=7, max_longest_pct=0.28, verbose=False):
    """Pad distractors so the correct option is not reliably the longest.

    Mutates and returns the bank. `why` entries are left untouched: they explain
    reasoning, and their length is not a visual tell on the option list.
    """
    rng = random.Random(seed)
    fixed = 0
    for q in bank:
        opts = list(q["opts"])
        ans = q["ans"]
        correct = opts[ans]
        others = [o for i, o in enumerate(opts) if i != ans]

        correct_len = len(correct)
        mean_other = sum(len(o) for o in others) / len(others)

        # Target: distractors should be at least as long as the correct option
        # most of the time, so that length carries no signal. Aim a little past
        # the correct option so near-ties (within a few characters) do not leave
        # the correct answer strictly longest.
        target = max(correct_len + 8, int(mean_other) + 8)
        new_others = []
        for o in others:
            if len(o) < target:
                f = FILLERS[rng.randrange(len(FILLERS))]
                o = _pad(o, target, f)
            new_others.append(o)

        rng.shuffle(new_others)
        rebuilt = list(new_others)
        rebuilt.insert(ans, correct)
        q["opts"] = rebuilt
        if rebuilt != opts:
            fixed += 1

    if verbose:
        print(f"  balance_bank: adjusted {fixed}/{len(bank)} questions")
    return bank


def audit_bank(bank, label=""):
    """Report the length tell. Returns (pct_strictly_longest, mean_ratio)."""
    n = len(bank)
    strictly_longest = 0
    for q in bank:
        L = [len(o) for o in q["opts"]]
        mx = max(L)
        if L[q["ans"]] == mx and L.count(mx) == 1:
            strictly_longest += 1
    mean_c = sum(len(q["opts"][q["ans"]]) for q in bank) / n
    mean_o = sum(sum(len(o) for j, o in enumerate(q["opts"]) if j != q["ans"]) / 3
                 for q in bank) / n
    pct = strictly_longest / n * 100
    ratio = mean_c / mean_o
    verdict = "OK" if pct <= 28 else "TELL PRESENT"
    if label:
        print(f"  {label:<22} longest-correct {strictly_longest:>3}/{n} = {pct:5.1f}%  "
              f"len ratio {ratio:.2f}  {verdict}")
    return pct, ratio

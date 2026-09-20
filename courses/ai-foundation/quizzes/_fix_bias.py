#!/usr/bin/env python3
"""
Fix longest-answer bias in a question bank by augmenting distractors.

The defect: because a correct explanation must state why it is right, correct options
drift longer than distractors. A learner can then score well without knowing the
subject. This module lengthens distractors with substantive, plausible elaboration
so option lengths converge, WITHOUT making distractors nonsense.
"""
import re, statistics

def lengths(q):
    return [len(o) for o in q["opts"]]

def report(bank, label):
    n = len(bank)
    longest_correct = sum(1 for q in bank if lengths(q).index(max(lengths(q))) == q["ans"])
    # handle ties: count only unique max
    longest_correct = 0
    for q in bank:
        L = lengths(q)
        mx = max(L)
        if L[q["ans"]] == mx and L.count(mx) == 1:
            longest_correct += 1
    print(f"{label}: correct-is-strictly-longest = {longest_correct}/{n} = {100*longest_correct/n:.0f}%")
    return longest_correct / n

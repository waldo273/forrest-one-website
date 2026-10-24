#!/usr/bin/env python3
"""End-to-end functional test of a Mode C quiz using real Chromium.
Extended to handle 30, 31 and 120 question papers."""
import sys, os
from playwright.sync_api import sync_playwright

import glob
def _chrome():
    """Resolve the newest Playwright Chromium dynamically — the build number
    changes when Playwright updates its bundled browser."""
    cands = sorted(glob.glob("/home/billy-forrest/.cache/ms-playwright/chromium-*/chrome-linux64/chrome"))
    if not cands:
        raise SystemExit("no Playwright Chromium found; run: python -m playwright install chromium")
    return cands[-1]
CHROME = _chrome()
BASE = "http://127.0.0.1:8899/quizzes/"


def test(url, label):
    print(f"\n{'='*60}\nFUNCTIONAL TEST: {label}\n{'='*60}")
    ok = True
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        pg = b.new_page()
        errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.on("console", lambda m: errors.append(f"console.{m.type}: {m.text}")
              if m.type == "error" else None)
        pg.goto(url, wait_until="load")

        def chk(name, cond, extra=""):
            nonlocal ok
            if cond:
                print(f"  PASS  {name} {extra}")
            else:
                print(f"  FAIL  {name} {extra}")
                ok = False

        chk("no JS errors on load", len(errors) == 0, str(errors[:2]))
        chk("question counter rendered",
            "Question 1 of" in pg.inner_text("#counter"), pg.inner_text("#counter"))
        chk("4 options rendered", pg.locator(".opt").count() == 4)
        chk("option letters A-D",
            [x.inner_text() for x in pg.locator(".opt-letter").all()][:4] == ["A.", "B.", "C.", "D."])
        chk("Next disabled before answering", pg.locator("#next").is_disabled())
        chk("Submit hidden on q1", not pg.locator("#submit").is_visible())

        ans_idx = pg.evaluate("Q[0].ans")
        pg.locator(".opt").nth(ans_idx).click()
        chk("all options disabled after answering",
            pg.locator(".opt:disabled").count() == 4)
        chk("Next enabled after answering", not pg.locator("#next").is_disabled())
        chk("analysis block shown", pg.locator(".analysis").count() == 1)
        chk("analysis has 4 why-paragraphs + 2 header paras",
            pg.locator(".analysis p").count() == 6,
            f"got {pg.locator('.analysis p').count()}")
        chk("correct tag present", "Correct" in pg.inner_text(".analysis"))
        chk("running score updated", pg.inner_text("#running").strip() == "Score: 1 / 1",
            pg.inner_text("#running"))

        other = (ans_idx + 1) % 4
        pg.locator(".opt").nth(other).click(force=True)
        chk("answer lock holds (score unchanged)",
            pg.inner_text("#running").strip() == "Score: 1 / 1",
            pg.inner_text("#running"))

        n = pg.evaluate("Q.length")
        # The block above answered Q1 and clicked Next, so the page now shows
        # question 2 (index 1). Answer the remaining questions up to the last,
        # clicking Next after each to advance.
        pg.locator("#next").click()  # advance from Q1 to Q2
        pg.wait_for_function(
            "document.getElementById('counter').textContent.includes('Question 2 of')")
        for i in range(1, n - 1):
            pg.wait_for_function(
                "document.getElementById('counter').textContent"
                f".includes('Question {i+1} of')")
            a = pg.evaluate(f"Q[{i}].ans")
            pg.locator(f"#o{i}_{a}").wait_for(state="visible")
            pg.locator(f"#o{i}_{a}").click()
            pg.locator("#next").click()
        chk("on last question", f"Question {n} of {n}" in pg.inner_text("#counter"),
            pg.inner_text("#counter"))
        chk("Submit visible on last question", pg.locator("#submit").is_visible())
        chk("Next hidden on last question", not pg.locator("#next").is_visible())

        chk("no Previous button exists",
            pg.locator("#prev, .prev-btn, button:has-text('Previous')").count() == 0)
        expected_correct_before_last = n - 1
        chk("running score tracks all answered questions",
            pg.inner_text("#running").strip() == f"Score: {expected_correct_before_last} / {n-1}",
            pg.inner_text("#running"))

        last_ans = pg.evaluate("Q[Q.length-1].ans")
        wrong = (last_ans + 1) % 4
        pg.locator(f"#o{n-1}_{wrong}").click()
        chk("wrong answer scores 0 for that item",
            pg.inner_text("#running").strip() == f"Score: {expected_correct_before_last} / {n}",
            pg.inner_text("#running"))

        pg.locator("#submit").click()
        chk("results panel visible", pg.locator("#results").is_visible())
        chk("quiz panel hidden", not pg.locator("#quiz").is_visible())
        pct = pg.inner_text("#pct")
        chk("percentage displayed", "%" in pct, pct)
        chk("correct count = n-1",
            pg.inner_text("#ncorrect") == str(expected_correct_before_last),
            pg.inner_text("#ncorrect"))
        chk("wrong count = 1", pg.inner_text("#nwrong") == "1", pg.inner_text("#nwrong"))
        chk("total correct", pg.inner_text("#ntotal") == str(n), pg.inner_text("#ntotal"))
        chk("missed list populated", pg.locator("#missed li").count() == 1,
            f"{pg.locator('#missed li').count()} items")
        pct_val = int(pct.replace("%", ""))
        expected = round((expected_correct_before_last / n) * 100)
        chk("percentage maths correct", pct_val == expected, f"{pct_val} vs {expected}")
        chk("PASS/FAIL verdict shown",
            pg.inner_text("#verdictlbl").strip() in ("PASS", "NOT YET"),
            pg.inner_text("#verdictlbl"))

        chk("progressbar aria-valuenow set",
            pg.get_attribute("#pbar", "aria-valuenow") == str(n),
            pg.get_attribute("#pbar", "aria-valuenow"))
        chk("skip link present", pg.locator(".skip-link").count() == 1)
        chk("radiogroup present", pg.locator("[role=radiogroup]").count() >= 1)

        if errors:
            print("  JS ERRORS:", errors[:3])
        b.close()
    return ok


if __name__ == "__main__":
    papers = [
        ("domain4-prompt-engineering-quiz.html", "Domain 4 Quiz (31q)"),
        ("domain6-limitations-hallucination-quiz.html", "Domain 6 Quiz (31q)"),
        ("domain8-ethics-bias-governance-quiz.html", "Domain 8 Quiz (31q)"),
        ("final-exam-120q.html", "FINAL EXAM (120q)"),
    ]
    allok = True
    for f, l in papers:
        allok &= test(BASE + f, l)
    print("\n" + "=" * 60)
    print("FUNCTIONAL RESULT:", "ALL PASSED" if allok else "FAILURES PRESENT")
    sys.exit(0 if allok else 1)

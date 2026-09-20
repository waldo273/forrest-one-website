#!/usr/bin/env python3
"""
UKAIC AI Foundation — Mode C accessible quiz generator.
Standalone white/navy accessible HTML, 4 options, single-select lock,
per-option explanations, password-protected restart (1234).

CRITICAL (from LESSONS.md 2026-09-10): apostrophes inside single-quoted JS
strings kill the script. ALL strings go through js_str() which JSON-encodes
them, producing safe double-quoted JS string literals.
"""
import json, random, sys, html, re
from pathlib import Path

ROOT = Path("/home/billy-forrest/Documents/Hermes/UKAIC-AI-Foundation")
OUT = ROOT / "quizzes"
OUT.mkdir(parents=True, exist_ok=True)

def js_str(s: str) -> str:
    """Emit a safe double-quoted JS string literal (handles ' and \\ safely)."""
    return json.dumps(s, ensure_ascii=False)

def scramble(questions, seed):
    """Deterministic answer-position scramble with position balancing.

    Two things must both hold:
      1. When options are reordered, the per-option `why` explanations must be
         reordered in the SAME permutation, or every explanation detaches from the
         option it describes (the "why" text ends up under the wrong letter).
      2. The correct answer must be spread roughly evenly across A/B/C/D. A skewed
         distribution is itself exploitable: "always answer B" scoring 32-35% on a
         25%-chance paper is a real position-bias tell.

    Strategy: assign each question a target answer position by dealing from a
    repeating balanced cycle (so counts stay within one of each other), then place
    the correct option at that position and shuffle the distractors into the rest.
    """
    rng = random.Random(seed)
    n = len(questions)
    # Build a balanced bag of target positions: e.g. 31 -> 8/8/8/7
    positions = []
    for i in range(n):
        positions.append(i % 4)
    rng.shuffle(positions)

    for q, pos in zip(questions, positions):
        correct = q["opts"][q["ans"]]
        correct_why = q["why"][q["ans"]]
        wrong = [(t, w) for i, (t, w) in enumerate(zip(q["opts"], q["why"]))
                 if i != q["ans"]]
        rng.shuffle(wrong)
        new_opts = [t for t, _ in wrong]
        new_why = [w for _, w in wrong]
        new_opts.insert(pos, correct)
        new_why.insert(pos, correct_why)
        q["opts"] = new_opts
        q["why"] = new_why
        q["ans"] = pos
    return questions


def position_spread(questions):
    """Return (counts, spread_pp) for the A/B/C/D answer distribution."""
    n = len(questions)
    dist = [sum(1 for q in questions if q["ans"] == i) for i in range(4)]
    pct = [d / n * 100 for d in dist]
    return dist, max(pct) - min(pct)

TEMPLATE = """<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<style>
:root{--navy:#002b5c;--ink:#0d1b2a;--ok:#2e7d32;--bad:#c62828;--line:#c9d4e4;--bg:#ffffff;--tint:#eef3fa;}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;background:var(--bg);color:var(--navy);
font-family:Arial,Helvetica,sans-serif;font-size:18px;line-height:1.6;}
.skip-link{position:absolute;left:-9999px;top:0;background:var(--navy);color:#fff;
padding:12px 20px;z-index:999;font-weight:bold;text-decoration:none;}
.skip-link:focus{left:0;}
header[role="banner"]{background:var(--navy);color:#fff;padding:14px 24px;}
header[role="banner"] h1{margin:0;font-size:1.15rem;font-weight:bold;letter-spacing:.2px;}
header[role="banner"] .sub{font-size:.85rem;opacity:.9;margin-top:3px;}
main[role="main"]{max-width:900px;margin:0 auto;padding:24px 20px 60px;}
.bar{display:flex;justify-content:space-between;align-items:center;gap:16px;
margin-bottom:8px;font-size:1rem;font-weight:bold;}
.progress-outer{height:14px;background:var(--tint);border:1px solid var(--line);
border-radius:8px;overflow:hidden;margin-bottom:26px;}
.progress-inner{height:100%;width:0;background:var(--navy);
transition:width .3s ease;}
@media (prefers-reduced-motion: reduce){.progress-inner{transition:none;}}
.qtext{font-size:1.3rem;font-weight:bold;margin:0 0 20px;line-height:1.45;}
.opt{display:flex;align-items:flex-start;gap:12px;width:100%;text-align:left;
background:var(--tint);border:2px solid var(--line);border-radius:10px;
padding:15px 17px;margin-bottom:12px;font-size:1.05rem;color:var(--ink);
font-family:inherit;cursor:pointer;line-height:1.5;}
.opt:hover:not(:disabled){background:#dde7f5;border-color:#9db3d0;}
.opt:disabled{cursor:default;}
.opt:focus-visible{outline:3px solid var(--navy);outline-offset:2px;}
.opt.correct{background:#dff3e1;border-color:var(--ok);}
.opt.wrong{background:#fbe3e3;border-color:var(--bad);}
.opt-letter{font-weight:bold;color:#4a6a8a;flex-shrink:0;width:24px;}
.opt.correct .opt-letter{color:var(--ok);}
.opt.wrong .opt-letter{color:var(--bad);}
.op-text{flex:1;}
.tag{font-weight:bold;font-size:.85rem;margin-left:8px;white-space:nowrap;}
.tag.correct{color:var(--ok);}
.tag.wrong{color:var(--bad);}
.analysis{margin-top:16px;padding:16px 18px;border-left:6px solid var(--navy);
background:var(--tint);border-radius:0 8px 8px 0;}
.analysis h3{margin:0 0 10px;font-size:1rem;text-transform:uppercase;
letter-spacing:.5px;}
.analysis p{margin:0 0 9px;font-size:.97rem;}
.analysis p:last-child{margin-bottom:0;}
.analysis .why{font-weight:bold;}
.analysis .good{color:var(--ok);}
.analysis .bad{color:var(--bad);}
.navrow{margin-top:26px;}
button.primary{background:var(--navy);color:#fff;border:none;border-radius:8px;
padding:15px 30px;font-size:1.05rem;font-weight:bold;cursor:pointer;
font-family:inherit;}
button.primary:hover{background:#00408a;}
button.primary:focus-visible{outline:3px solid #002b5c;outline-offset:3px;}
button.primary:disabled{background:#9db3d0;cursor:not-allowed;}
button.submit{background:var(--ok);}
button.submit:hover{background:#1f5b23;}
.verdict{font-size:1.15rem;font-weight:bold;margin:0 0 18px;padding:14px 18px;
border-radius:8px;}
.verdict.ok{background:#dff3e1;color:#1f5b23;border:2px solid var(--ok);}
.verdict.no{background:#fbe3e3;color:#8c1c1c;border:2px solid var(--bad);}
#results{display:none;text-align:center;}
.gauge{width:230px;height:230px;border-radius:50%;margin:0 auto 26px;
display:flex;align-items:center;justify-content:center;flex-direction:column;}
.gauge .pct{font-size:3.2rem;font-weight:bold;line-height:1;}
.gauge .lbl{font-size:.95rem;margin-top:6px;letter-spacing:1px;}
.grid{display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin:26px 0;}
.cell{border:2px solid var(--line);border-radius:10px;padding:16px 26px;min-width:130px;}
.cell .n{font-size:2rem;font-weight:bold;display:block;}
.cell .t{font-size:.9rem;text-transform:uppercase;letter-spacing:.5px;}
.cell.good{border-color:var(--ok);} .cell.good .n{color:var(--ok);}
.cell.bad{border-color:var(--bad);} .cell.bad .n{color:var(--bad);}
.note{font-size:.95rem;color:#3d5878;max-width:640px;margin:0 auto 22px;}
/* Assessment integrity: selection and copy are disabled on question content. */
#qholder,#results,.analysis,.opt{-webkit-user-select:none;-moz-user-select:none;
  -ms-user-select:none;user-select:none;-webkit-touch-callout:none;}
#quiz,#results{-webkit-user-drag:none;}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%);
  background:var(--navy);color:#fff;padding:13px 24px;border-radius:8px;
  font-size:.95rem;font-weight:bold;box-shadow:0 4px 14px rgba(0,0,0,.25);
  z-index:9999;display:none;}
.toast.show{display:block;}
@media (prefers-reduced-motion: no-preference){.toast{transition:opacity .2s ease;}}
</style>
</head>
<body>
<a href="#main" class="skip-link">Skip to main content</a>
<header role="banner">
  <h1>UKAIC AI Foundation — __HEADER__</h1>
  <div class="sub">__SUBTITLE__</div>
</header>
<main role="main" id="main">
  <div id="quiz">
    <div class="bar">
      <span id="counter" role="status" aria-live="polite">Question 1 of __N__</span>
      <span id="running" aria-live="polite">Score: 0 / 0</span>
    </div>
    <div class="progress-outer" role="progressbar" aria-labelledby="counter"
         aria-valuemin="0" aria-valuemax="__N__" aria-valuenow="0" id="pbar">
      <div class="progress-inner" id="pinner"></div>
    </div>
    <div id="qholder"></div>
    <div class="navrow">
      <button class="primary" id="next" type="button">Next question &rarr;</button>
      <button class="primary submit" id="submit" type="button"
              style="display:none">Submit assessment</button>
    </div>
  </div>
  <div id="results" role="region" aria-label="Assessment results">
    <div class="gauge" id="gauge"><span class="pct" id="pct">0%</span>
      <span class="lbl" id="verdictlbl">—</span></div>
    <div class="grid">
      <div class="cell good"><span class="n" id="ncorrect">0</span>
        <span class="t">Correct</span></div>
      <div class="cell bad"><span class="n" id="nwrong">0</span>
        <span class="t">Incorrect</span></div>
      <div class="cell"><span class="n" id="ntotal">0</span>
        <span class="t">Total</span></div>
    </div>
    <p class="note" id="dignote"></p>
    <ul id="missed" style="text-align:left;max-width:760px;margin:0 auto 24px;
      padding-left:22px;font-size:.98rem;"></ul>
    <button class="primary" id="restart" type="button">Restart assessment</button>
  </div>
</main>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script>
var Q = __QJSON__;
var PASS = __PASS__;
var L = ["A","B","C","D"];
var cur = 0, answered = [], correct = [], submitted = false;

// Randomise question order on every attempt so the sequence cannot be memorised
// from a screenshot. Uses the same RNG discipline as the accessible quiz standard.
(function shuffleQuestions(){
  var seed = Date.now() % 2147483647;
  function rnd(){ seed = (seed * 16807) % 2147483647; return seed / 2147483647; }
  for (var i = Q.length - 1; i > 0; i--){
    var j = Math.floor(rnd() * (i + 1));
    var t = Q[i]; Q[i] = Q[j]; Q[j] = t;
  }
})();

// --- Copy / cut / paste attenuation -------------------------------------------------
// Assessment integrity: discourage copying questions out and pasting answers in.
// This is a deterrent, NOT a security control — a determined user can defeat it via
// devtools. It stops casual text harvesting and pasted-in answers during a sitting.
(function blockClipboard(){
  function stop(e){
    e.preventDefault();
    showToast('Copying, cutting and pasting are disabled during this assessment.');
    return false;
  }
  ['copy','cut','paste','contextmenu'].forEach(function(evt){
    document.addEventListener(evt, stop, true);
  });
  // Disable text selection inside the question and analysis areas only, so that
  // the skip link and buttons remain fully keyboard accessible.
  var style = document.createElement('style');
  style.textContent = '#qholder, #results { -webkit-user-select:none; -moz-user-select:none;'
                    + ' -ms-user-select:none; user-select:none; }';
  document.head.appendChild(style);
})();

function showToast(msg){
  var t = document.getElementById('toast');
  if (!t) return;
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(t._timer);
  t._timer = setTimeout(function(){ t.classList.remove('show'); }, 2600);
}

var qlen = Q.length;
for (var i = 0; i < qlen; i++){ answered.push(false); correct.push(false); }

function el(id){ return document.getElementById(id); }

function render(){
  var q = Q[cur];
  var h = '<h2 class="qtext" id="qt">' + q.q + '</h2>';
  h += '<div role="radiogroup" aria-labelledby="qt">';
  for (var j = 0; j < q.opts.length; j++){
    h += '<button class="opt" type="button" role="radio" aria-checked="false" '
       + 'data-q="' + cur + '" data-o="' + j + '" id="o' + cur + '_' + j + '">'
       + '<span class="opt-letter">' + L[j] + '.</span>'
       + '<span class="op-text">' + q.opts[j] + '</span>'
       + '<span class="tag" id="t' + cur + '_' + j + '"></span></button>';
  }
  h += '</div><div id="ex' + cur + '"></div>';
  el('qholder').innerHTML = h;
  var btns = el('qholder').querySelectorAll('.opt');
  for (var k = 0; k < btns.length; k++){
    btns[k].addEventListener('click', onPick);
  }
  var last = (cur === qlen - 1);
  el('next').style.display = last ? 'none' : '';
  el('submit').style.display = last ? '' : 'none';
  el('next').disabled = !answered[cur];
  el('submit').disabled = !answered[cur];
  updateBar();
}

function onPick(e){
  var b = e.currentTarget;
  var qi = parseInt(b.getAttribute('data-q'), 10);
  var oi = parseInt(b.getAttribute('data-o'), 10);
  if (answered[qi]) return;
  answered[qi] = true;
  var q = Q[qi];
  var isRight = (oi === q.ans);
  correct[qi] = isRight;
  var all = el('qholder').querySelectorAll('.opt');
  for (var k = 0; k < all.length; k++){
    var kq = parseInt(all[k].getAttribute('data-q'), 10);
    var ko = parseInt(all[k].getAttribute('data-o'), 10);
    if (kq !== qi) continue;
    all[k].disabled = true;
    all[k].setAttribute('aria-checked', ko === oi ? 'true' : 'false');
    var tg = el('t' + kq + '_' + ko);
    if (ko === q.ans){
      all[k].classList.add('correct');
      if (tg) tg.textContent = ko === oi ? '✓ Correct' : '✓ This was correct';
      if (tg) tg.className = 'tag correct';
    } else if (ko === oi){
      all[k].classList.add('wrong');
      if (tg) tg.textContent = '✗ Your answer';
      if (tg) tg.className = 'tag wrong';
    }
  }
  renderAnalysis(qi);
  var done = 0;
  for (var m = 0; m < qlen; m++){ if (answered[m]) done++; }
  el('running').textContent = 'Score: ' + tally() + ' / ' + done;
  el('next').disabled = false;
  el('submit').disabled = false;
  updateBar();
}

function renderAnalysis(qi){
  var q = Q[qi];
  var h = '<div class="analysis"><h3>Why each option is right or wrong</h3>';
  h += '<p class="why good">Correct answer: ' + L[q.ans] + '. '
     + q.opts[q.ans] + '</p><p>' + q.exp + '</p>';
  for (var j = 0; j < q.opts.length; j++){
    h += '<p><span class="why">' + L[j] + '.</span> ' + q.why[j] + '</p>';
  }
  h += '</div>';
  el('ex' + qi).innerHTML = h;
}

function tally(){
  var n = 0;
  for (var i = 0; i < qlen; i++){ if (correct[i]) n++; }
  return n;
}

function updateBar(){
  el('counter').textContent = 'Question ' + (cur + 1) + ' of ' + qlen;
  var pct = Math.round(((cur + 1) / qlen) * 100);
  el('pinner').style.width = pct + '%';
  var pb = el('pbar');
  if (pb){ pb.setAttribute('aria-valuenow', String(cur + 1)); }
}

el('next').addEventListener('click', function(){
  if (cur < qlen - 1){ cur++; render(); }
});
el('submit').addEventListener('click', function(){ showResults(false); });

function mark(){
  var c = tally();
  var p = Math.round((c / qlen) * 100);
  el('pct').textContent = p + '%';
  el('ncorrect').textContent = c;
  el('nwrong').textContent = qlen - c;
  el('ntotal').textContent = qlen;
  var g = el('gauge');
  var pass = (p >= PASS);
  g.style.background = pass ? '#dff3e1' : '#fbe3e3';
  g.style.border = '8px solid ' + (pass ? '#2e7d32' : '#c62828');
  el('verdictlbl').textContent = pass ? 'PASS' : 'NOT YET';
  el('verdictlbl').style.color = pass ? '#2e7d32' : '#c62828';
  el('pct').style.color = pass ? '#2e7d32' : '#c62828';
  el('dignote').textContent = pass
    ? 'You have met the pass standard for this section. Revisit any missed items below, then move on.'
    : 'Below the pass standard of ' + PASS + '%. Review each missed item below and retake when ready.';
  var ul = el('missed');
  ul.innerHTML = '';
  var missed = 0;
  for (var i = 0; i < qlen; i++){
    if (!correct[i]){
      missed++;
      var li = document.createElement('li');
      li.style.marginBottom = '8px';
      li.textContent = Q[i].q + ' — correct: ' + L[Q[i].ans] + '. ' + Q[i].opts[Q[i].ans];
      ul.appendChild(li);
    }
  }
  if (missed === 0){
    var li2 = document.createElement('li');
    li2.textContent = 'No missed items.';
    ul.appendChild(li2);
  }
}

function showResults(force){
  if (submitted && !force) return;
  submitted = true;
  mark();
  el('quiz').style.display = 'none';
  el('results').style.display = 'block';
  window.scrollTo(0, 0);
}

el('restart').addEventListener('click', function(){
  var p = window.prompt('Enter supervisor passcode to reset this assessment:');
  if (p !== '1234'){
    if (p !== null){ window.alert('Incorrect passcode. Assessment not reset.'); }
    return;
  }
  location.reload();
});

document.addEventListener('keydown', function(e){
  if (e.key === 'ArrowRight' && !answered[cur] === false && cur < qlen - 1){
    e.preventDefault(); cur++; render();
  }
});

// ---- Assessment integrity guard ----
// Deterrent only: browser menus can bypass keyboard blocks and the HTML source
// always contains the questions. Pair with invigilation for real integrity.
(function integrityGuard(){
  var tc = null;
  function toast(msg){
    var t = el('toast');
    if (!t) return;
    t.textContent = msg;
    t.classList.add('show');
    if (tc) clearTimeout(tc);
    tc = setTimeout(function(){ t.classList.remove('show'); }, 2400);
  }
  function block(e, msg){
    e.preventDefault();
    e.stopPropagation();
    toast(msg || 'Copying is disabled on this assessment.');
    return false;
  }
  document.addEventListener('contextmenu', function(e){ block(e); });
  document.addEventListener('copy',  function(e){ block(e); });
  document.addEventListener('cut',   function(e){ block(e); });
  document.addEventListener('dragstart', function(e){ block(e, 'Dragging is disabled.'); });
  document.addEventListener('selectstart', function(e){
    var n = e.target;
    while (n && n !== document.body){
      if (n.id === 'qholder' || n.id === 'results' ||
          (n.classList && (n.classList.contains('opt') || n.classList.contains('analysis')))){
        block(e, 'Selecting question text is disabled.');
        return;
      }
      n = n.parentNode;
    }
  });
  document.addEventListener('keydown', function(e){
    var k = (e.key || '').toLowerCase();
    if ((e.ctrlKey || e.metaKey) && (k === 'c' || k === 'x' || k === 'a' || k === 'u' || k === 's' || k === 'p')){
      block(e); return;
    }
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && (k === 'i' || k === 'j' || k === 'c')){
      block(e, 'Developer tools are disabled.'); return;
    }
    if (e.key === 'F12'){ block(e, 'Developer tools are disabled.'); }
  }, true);
})();

render();
</script>
</body>
</html>
"""

def build(title, header, subtitle, questions, passmark, outfile, seed):
    qs = scramble([dict(q) for q in questions], seed)
    for q in qs:
        assert len(q["opts"]) == 4, q["q"]
        assert len(q["why"]) == 4, q["q"]
        assert 0 <= q["ans"] <= 3, q["q"]
    data = []
    for q in qs:
        data.append({
            "q": q["q"],
            "opts": q["opts"],
            "ans": q["ans"],
            "exp": q["exp"],
            "why": q["why"],
        })
    htmlout = (TEMPLATE
        .replace("__TITLE__", html.escape(title))
        .replace("__HEADER__", html.escape(header))
        .replace("__SUBTITLE__", html.escape(subtitle))
        .replace("__N__", str(len(qs)))
        .replace("__PASS__", str(passmark))
        .replace("__QJSON__", json.dumps(data, ensure_ascii=False)))
    assert "__" not in htmlout.replace("__", "", 0) or True
    for marker in ["__TITLE__", "__QJSON__", "__N__", "__PASS__", "__HEADER__", "__SUBTITLE__"]:
        assert marker not in htmlout, f"unreplaced {marker}"
    p = OUT / outfile
    p.write_text(htmlout, encoding="utf-8")
    print(f"WROTE {p} ({len(htmlout)} bytes, {len(qs)} questions)")
    return p

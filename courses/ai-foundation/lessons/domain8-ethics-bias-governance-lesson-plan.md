# Domain 8 — Ethics, Bias, Responsible AI & Governance
## Lesson Plan

**Course:** UKAIC AI Foundation
**Domain:** 8 of 8
**Examination weighting:** 8% · 10 of 120 questions
**Syllabus reference:** SYL_AIF v1.0, areas 8.1 to 8.6
**Course duration:** 21 hours total across the eight domains; this domain is a **2-hour 45-minute session** (2h 30m tuition plus a 15-minute consolidation block)
**Level:** Foundation. Understand and apply. No coding, mathematics or legal interpretation required.
**Prepared:** 10 September 2026

---

## 1. Session Overview

Domain 8 carries the smallest examination weighting of the eight domains (8%, 10 questions)
but it holds the course's ethical centre of gravity. Four of the other domains converge here:
Drafting and verification (Domain 5) exist to make AI-assisted work defensible; hallucination
(Domain 6) explains why verification cannot be skipped; data protection and shadow AI (Domain 7)
are the operational face of responsible use; and prompt engineering (Domain 4) determines
whether an output is fit to publish at all. Domain 8 asks the professional question that sits
above all of them: **who is accountable, and can they show their work?**

The domain also carries the most explicit statement of the course's governing principle:
**AI can assist while humans remain accountable.** Every area in this session is a working-out
of that sentence.

### Why this domain is harder to teach than it looks

Candidates find Domain 8 deceptively easy to read and deceptively easy to get wrong on the
examination. Three reasons recur:

1. **The attractive answer is often wrong.** "Cross-check it against another AI" and "the
   system decided, so the supplier is liable" are both highly plausible and both false.
2. **Plausible-sounding governance is not governance.** A policy that exists is not a policy
   that works. A named reviewer is not oversight if the reviewer rubber-stamps.
3. **The regulatory picture moves.** A candidate who memorises a compliance date will be
   wrong within a year. The testable skill is the *shape* of the landscape (risk-based,
   obligations scale with risk), not the date.

### Session-at-a-glance timetable (2h 45m)

| Time | Block | Syllabus area | Format |
|---|---|---|---|
| 0:00–0:10 | Welcome, framing, the accountability question | Orientation | Plenary |
| 0:10–0:40 | **8.1 Bias & Fairness** | 8.1 | Input + demo 1 + discussion 1 |
| 0:40–1:10 | **8.2 Transparency, Accountability & Explainability** | 8.2 | Input + demo 2 + discussion 2 |
| 1:10–1:20 | Break | — | — |
| 1:20–1:50 | **8.3 Human Oversight** | 8.3 | Input + demo 3 + discussion 3 |
| 1:50–2:10 | **8.4 Disclosure** | 8.4 | Input + scenario exercise |
| 2:10–2:30 | **8.5 Policy & Governance** | 8.5 | Input + regulatory landscape briefing |
| 2:30–2:45 | **8.6 Professional Decision Framework** + consolidation | 8.6 | Framework drill + close |

**Assessment:** the Domain 8 quiz (31 questions, 70% pass standard) is released at the end of
the session and completed by candidates in their own time, in line with the course's
"quiz kick-off in class, completion at home" convention.

---

## 2. Learning Outcomes

By the end of this session, candidates will be able to:

| # | Outcome | Syllabus area |
|---|---|---|
| LO1 | Identify the three sources of bias and explain why bias assessment is a duty in people-affecting uses | 8.1 |
| LO2 | State the accountability principle and explain why "the AI did it" is not a defence | 8.2 |
| LO3 | Describe transparency and explainability at Foundation level | 8.2 |
| LO4 | Explain why human oversight is necessary and where automated decisions increase risk | 8.3 |
| LO5 | Apply the "AI proposes, a person decides" principle to a workplace scenario | 8.3 |
| LO6 | Decide when AI use must be disclosed | 8.4 |
| LO7 | Describe the purpose of an organisational AI policy and basic governance | 8.5 |
| LO8 | Outline the high-level, risk-based regulatory picture at awareness level | 8.5 |
| LO9 | Apply the professional decision framework: use / use with verification / escalate / do not use | 8.6 |
| LO10 | Demonstrate the central principle that AI can assist while humans remain accountable | 8.6 |

---

## 3. Block-by-Block Teaching Notes

### Block 1 — Orientation (10 minutes)

**Purpose:** Establish why this domain matters and set up the accountability question that
runs through the session.

**Opening framing (speak):**
> Every domain in this course has asked you to do something with AI. This one asks who
> answers for it. The syllabus puts it in six words: AI assists, humans remain accountable.
> Everything we cover in the next two and a half hours is a working-out of that sentence.

**Key point to land:** Domain 8 is 8% of the examination, the smallest weighting, but it is
the domain that decides whether the other 92% is used defensibly.

---

### Block 2 — 8.1 Bias & Fairness (30 minutes)

**What is tested:** Sources of bias (training data, design choices, deployment context);
real-world impacts (hiring, lending, content); bias assessment as a duty in people-affecting uses.

#### Teaching content

**The three sources of bias.** Candidates must be able to name all three and distinguish them:

| Source | What it means | Worked example |
|---|---|---|
| **Training data** | The model learns historical patterns, including historical unfairness | A screening tool trained on ten years of the company's own hires learns who the company has historically preferred |
| **Design choices** | Decisions about what to optimise, what to include, what to exclude | Optimising for "career continuity" penalises carers and career-breakers |
| **Deployment context** | The same system used somewhere with different stakes or a different population | A model acceptable for internal triage may cause harm if reused for public eligibility decisions |

**The critical teaching point.** Candidates reach for "remove the protected characteristic"
as the fix. This is necessary but not sufficient, because **proxy signals** carry the same
information indirectly. Removing names does not remove the signal carried by institution,
career gaps, phrasing or postcode. Fairness has to be tested on *outcomes*, not asserted
from the removal of a field.

**Grounding evidence (cite in delivery).** Guilbeault, Delecourt and Srinivasa Desikan,
published in *Nature* and reported by Stanford (October 2025), prompted ChatGPT to generate
more than **34,500 resumes across 54 occupations** using typically male or female names. When
the model was then asked to rate those resumes, it **gave older men the highest ratings even
where the underlying information was the same**, having first written work histories that
portrayed women as younger and less experienced. The researchers' conclusion is the teaching
point: over-reliance on simplistic output filters "can miss more nuanced issues such as
gendered ageism", and the bias has to be addressed at a fundamental level. Source: Stanford
Report, "Researchers uncover AI bias against older working women", 17 October 2025.

#### ▶ Demo 1 — The name-swap test (8 minutes)

**Setup:** Prepare two versions of a short, realistic candidate summary. Identical in every
respect except the name. Version A uses a name suggesting a younger candidate; version B uses
a name suggesting an older candidate. Use an approved model.

**Run:** Ask the model, in two separate sessions, to rate each candidate for a mid-level
management role and give a one-paragraph justification.

**What to look for:** Differences in the language used, the emphasis on "energy", "trajectory"
or "experience", and whether the ratings diverge. Note that a single run proves nothing;
variability (syllabus 2.5) means you must run it several times before drawing a conclusion.

**Teaching point to draw out:** This is a *diagnostic demonstration*, not a controlled study.
It shows candidates how easily an automated ranking can be steered by irrelevant information,
and why outcome testing at scale is a professional duty rather than a theoretical one.

**Instructor caveat to state explicitly:** Be careful not to overclaim from a single demo. The
evidence for bias comes from the published research, not from this demonstration. The demo
builds intuition; the research establishes the fact.

#### ▶ Discussion 1 — Where is your organisation exposed? (10 minutes)

Ask candidates to name one real use of AI or automation in their own organisation that affects
a person's opportunities, access or treatment. For each, ask the three questions:

1. What data did it learn from, and whose past does that data encode?
2. What was it optimised for, and what does that optimisation make more likely?
3. Who is affected if it is wrong, and how would anyone find out?

**Facilitation note:** Most groups will surface at least one genuinely uncomfortable case.
Resist resolving them. The examinable skill is the *habit of asking*, not reaching a
comfortable answer.

#### Formative check

> A team removes names and gender markers from applications before AI screening. Why is this
> not proof that the tool is fair?

*Expected answer:* Because correlated features can act as proxies, preserving the same signal
indirectly. Fairness must be tested on outcomes.

---

### Block 3 — 8.2 Transparency, Accountability & Explainability (30 minutes)

**What is tested:** The human or organisation remains accountable, and "the AI did it" is not
a defence; transparency and explainability at Foundation level.

#### Teaching content

**The accountability principle.** State it plainly and repeat it: an AI system cannot hold
legal or professional liability. When a decision causes harm, the accountable party is the
human or organisation that chose to deploy and use the system. "The AI did it" fails not
because it is rude but because it names a party with no standing to answer.

**Why this is the hinge of the whole domain.** Accountability is what makes transparency and
oversight *requirements* rather than virtues. If nobody is accountable, there is no reason to
explain or to supervise. Because somebody is accountable, both become obligations.

**Transparency and explainability at Foundation level.** Explainability here means being able
to give a *meaningful account* of how a decision was reached and what it was based on. It does
**not** mean publishing source code, exposing internal model weights, or promising perfect
reconstruction years later. Candidates must be able to distinguish the professional-literacy
standard from the technical one, because both over-claiming and under-claiming are examinable
errors.

**A common misconception to correct.** "The supplier is liable because they built it."
Supplier liability is a real commercial and regulatory question, but it does **not** remove the
deploying organisation's own accountability. The organisation chose the tool, set the
constraints and used the output.

#### ▶ Demo 2 — The unexplainable decision (8 minutes)

**Setup:** Present a short written decision outcome with no stated basis (for example: "Your
application was declined by our automated system").

**Run:** In pairs, candidates draft the "meaningful account" they would give the affected
person. Then compare against the technical detail a data scientist might produce (model
version, feature weights, confidence score).

**Teaching point to draw out:** The two accounts serve different audiences and only one
discharges the professional duty. Candidates should notice that a confidence score is not an
explanation and that a feature weight is not a reason.

#### ▶ Discussion 2 — The accountability chain (10 minutes)

Present this case, then run a structured 10-minute debate.

> A bank deploys a third-party credit scoring model. An applicant is declined. The bank says
> the model declined them. The vendor says the model is only advisory and the bank decides.

**Questions to work through:**
1. Who is accountable to the applicant, and why?
2. Does the vendor's "advisory only" defence change the answer?
3. What would the bank need to be able to show to answer for the decision?

*Expected landing point:* The bank remains accountable. Advisory status does not transfer
responsibility because the bank chose to act on the advice and cannot delegate accountability
to a system.

**Facilitation note:** This is the single most valuable discussion in the domain. Let candidates
feel the discomfort of the "we just use the tool" position before you dismantle it.

#### Formative check

> A manager says the AI made the decision, so she cannot answer for it. What is wrong with this?

*Expected answer:* Accountability requires a party that can answer for the outcome. The system
cannot, so responsibility remains with the human and the organisation.

---

### Block 4 — 8.3 Human Oversight (30 minutes)

**What is tested:** Why oversight is necessary and where automated decision-making increases
risk; the principle that AI proposes while a person decides and owns the outcome.

#### Teaching content

**The principle.** **AI proposes; a person decides and owns the outcome.** Candidates should
be able to state this and to recognise its inversion in a scenario.

**Where risk increases.** Automated decision-making increases risk where the decision
materially affects a person's **rights, opportunities or safety**. This is the testable
criterion. Note that the criterion is about the *stakes for the individual*, not about the
technology, the cost, or whether the data was internally collected.

**What meaningful oversight is not.**
- It is not a person who clicks "approve" 400 times a day. That is accountability theatre.
- It is not post-hoc review that may or may not happen.
- It is not a person re-doing every calculation the system performed.

**What meaningful oversight is.** The overseer must have the *information*, the *authority*,
the *time* and the *competence* to disagree. Remove any one and oversight is nominal. This
framing is worth writing on the board.

**A teaching point from Domain 6.** "No reported problems" is not evidence of no problems.
Systems fail quietly and consistently. Oversight is the mechanism that converts an unseen
systematic error into a visible one. This is why removing oversight is riskier than it looks.

#### ▶ Demo 3 — Automation bias (8 minutes)

**Setup:** Give candidates a short task with a plausible AI-suggested answer that contains one
embedded error requiring domain knowledge to catch. Ask them to review the output and decide
whether to accept it. Time-limit tightly (3 minutes).

**Run:** Note how many candidates accept the output. Then reveal the error.

**Teaching point to draw out:** This is **automation bias**: the tendency to accept an
automated suggestion because it is fluent and presented as an answer, particularly under time
pressure. Oversight fails here not because the human was absent but because the human was
*persuaded*. This connects directly to Domain 6 (fluency is not accuracy) and explains why
critical evaluation is a trained skill, not a disposition.

#### ▶ Discussion 3 — Where should the human sit? (10 minutes)

Present three uses and ask where oversight should sit and why:

| Use | Candidate reasoning to draw out |
|---|---|
| Automatic approval of expense claims under £500 | Low stakes; oversight may be sampling plus exception handling. Justify the threshold. |
| AI-assisted shortlisting of job applicants | High stakes, people-affecting. Human decides, AI proposes. Bias assessment applies (8.1). |
| AI triaging patients in a clinical setting | Highest stakes. Mandatory verification (6.5). Clinician decides every case. |

**Facilitation note:** The point is not that oversight must be identical everywhere. It is
that oversight should be **proportionate to the stakes**, and candidates must be able to
justify the proportionality rather than assume the tool has settled it.

#### Formative check

> A system approves expense claims automatically and reports no problems. Why is caution
> warranted?

*Expected answer:* Without oversight there is no mechanism to detect systematic error or
unfairness before it affects many people.

---

### Block 5 — 8.4 Disclosure (20 minutes)

**What is tested:** When to disclose AI use: where required, where AI substantially generated
the content, or where non-disclosure would mislead.

#### Teaching content

**The three triggers.** Present them as a decision list:

1. **Where required** — a law, regulation, contract or organisational policy demands it.
2. **Where AI substantially generated the content** — the AI produced the substance, not merely
   assisted with it.
3. **Where non-disclosure would mislead** — a reasonable person would form a different view of
   the content, or of who they are dealing with, if they knew.

**The misleading test is the one to teach.** It handles the cases the first two triggers miss.
A customer who believes they are speaking to a human holds a false belief about the
interaction, whether or not the information given was accurate. A reader who assumes a report
was entirely human-authored holds a false belief about its provenance.

**Where disclosure is not required.** Assistive uses that do not substantially generate content
and do not alter meaning: spelling correction, formatting, locating a source, checking
arithmetic. Candidates must be able to draw this line, because over-disclosure trivialises the
duty.

**Verification and disclosure are separate duties.** This is a common candidate error. Checking
that content is factually correct does **not** discharge the disclosure question, and disclosing
does **not** discharge the verification question. They answer different questions: *is it
true?* and *how was it produced?*

#### Grounding evidence (cite in delivery)

The EU AI Act's transparency obligations (Article 50) apply from **2 August 2026** and are
**not limited to high-risk systems**. They require disclosure in four situations: where AI
interacts directly with people, where AI generates synthetic content, where AI is used for
emotion recognition or biometric categorisation, and where AI creates deepfakes or publishes
text on matters of public interest unless that text has had human review and editorial
responsibility attached. Providers must mark synthetic outputs in machine-readable form. An
important nuance for teaching: the Act's high-risk obligations under Annex III were postponed
by the Digital Omnibus from 2 August 2026 to **2 December 2027**, so organisations should
verify the current position rather than rely on a remembered date. Source: artificialintelligenceact.eu,
"The EU AI Act's Transparency Rules: A Practical Guide to Article 50", 14 May 2026; European
Commission, "Safer and more transparent AI", 2 August 2026.

**Why the moving-date point matters:** the examinable skill is knowing that disclosure
obligations are **risk-based and broadening**, not reciting a deadline.

#### ▶ Exercise — Disclosure call (12 minutes)

Candidates classify each case as **must disclose / consider disclosing / no disclosure needed**,
then justify in one sentence:

| Case | Expected answer |
|---|---|
| A chatbot answers billing queries without identifying itself as AI | Must disclose (misleading about who they are dealing with) |
| A published research summary drafted largely by AI, reviewed by a human editor | Consider disclosing (substantial generation; editorial review informs the judgment) |
| A policy document reformatted by AI with no change to meaning | No disclosure needed (assistive, meaning unchanged) |
| An AI-generated image of a real person used in a training deck | Must disclose (deepfake-style synthetic content of a real person) |
| An email where AI corrected spelling and grammar | No disclosure needed (assistive editing) |

#### Formative check

> A draft was checked for accuracy. Does that remove the need to consider disclosure?

*Expected answer:* No. Accuracy and disclosure are separate obligations answering different
questions.

---

### Block 6 — 8.5 Policy & Governance (20 minutes)

**What is tested:** The purpose of an organisational AI policy and basic governance (oversight,
accountability, review); the high-level, risk-based regulatory picture at awareness level.

#### Teaching content

**The three elements of governance.** Oversight, accountability, review. A policy that lacks
any one of them is incomplete:

- **Oversight** — who watches the use, and how.
- **Accountability** — who answers when it goes wrong, and for what.
- **Review** — how the policy and the systems are revisited as practice and the field change.

**A policy that exists is not a policy that works.** Two years is a long time in this field. A
policy that predates the tools staff now use daily cannot guide their behaviour, and its
silence on a tool is *not* permission. This is the bridge back to shadow AI (7.3): a policy gap
is a reason to escalate, never a licence to proceed on personal judgement.

**The regulatory picture at awareness level.** The examinable shape is:

- **Risk-based** — obligations scale with the risk of the use.
- **Multi-layered** — no single worldwide regime governs all AI use.
- **In motion** — requirements are broadening and deadlines have moved.

Candidates are **not** required to interpret legislation. They are required to recognise that
obligations attach to the *use*, that deploying organisations carry responsibility (not only
developers), and that this is why an organisational policy exists.

**A useful applied insight (not examinable detail).** Most state and national frameworks impose
obligations on the party that **deploys or uses** AI, not only on the party that builds it. For
a business integrating a third-party tool into hiring or clinical workflows, that business is
the regulated deployer. Source: Epstein Becker Green, "AI Legislation: 2026 Legislative Wrap-Up",
22 July 2026.

#### ▶ Discussion 4 — Audit your own policy (8 minutes)

Three questions in small groups:
1. Does your organisation have an AI policy, and when was it last reviewed?
2. Does it name who is accountable, or only what is prohibited?
3. If a colleague wanted to use a tool the policy does not mention, what would they do next —
   and is that the right answer?

**Facilitation note:** Groups frequently discover their policy is a list of prohibitions with no
accountability structure. That discovery is the learning outcome.

#### Formative check

> An employee wants to use an unapproved AI tool. The policy does not mention it. What now?

*Expected answer:* Escalate for approval. A policy gap is a reason to escalate, not to proceed.

---

### Block 7 — 8.6 Professional Decision Framework & Consolidation (15 minutes)

**What is tested:** Applying the framework (use / use with verification / escalate / do not
use), being more cautious when unsure; demonstrating the central principle.

#### Teaching content

**The framework.** Four outcomes, applied with the instruction that **when unsure, be more
cautious**:

| Outcome | When it applies |
|---|---|
| **Use** | Routine, low-stakes, approved tool, no personal or confidential data, no people-affecting decision |
| **Use with verification** | Output will be acted on, shared or published; facts, figures, dates, names, quotes and citations must be checked at source |
| **Escalate** | High stakes, unclear policy, unfamiliar tool, legal or medical territory, or any situation where you are not confident |
| **Do not use** | Prohibited use, confidential data with no approved tool, or a decision that must be made by qualified human expertise |

**The central principle, restated.** AI can assist while humans remain accountable. This is the
sentence the domain exists to justify, and candidates should be able to explain why each of the
four outcomes serves it.

**A closing distinction worth emphasising.** The framework is not a risk-avoidance device. It
is what makes *confident, fast use of AI possible*, because it identifies the cases where
verification and escalation are required and leaves the rest to proceed. Professionals who
lack a framework tend either to over-trust or to avoid the tool. The framework is what allows
neither.

#### ▶ Consolidation drill — The four-outcome sort (10 minutes)

Give candidates eight short scenarios and ask them to assign an outcome and justify it. Suggested
set:

1. Shortening a public-facing document for a general audience → **Use with verification**
2. Drafting a first version of a routine internal update → **Use**
3. Deciding whether to dismiss an employee for misconduct → **Escalate / Do not use** (qualified expertise, high stakes)
4. Pasting a client contract containing personal data into a free public tool → **Do not use**
5. Producing a credit score that affects an applicant → **Escalate** (high stakes, people-affecting, oversight required)
6. Asking an approved tool to suggest a synonym → **Use**
7. Summarising a board-level contract for a decision → **Use with verification** (and read the original, per 5.2)
8. Using an unapproved tool because a colleague recommended it → **Escalate** (approval required)

**Facilitation note:** Push on the justification, not the label. The examination tests
reasoning, and several scenarios have more than one defensible answer if the justification is
sound.

---

## 4. Consolidation Block (15 minutes, included in the timetable as 2:30–2:45)

Run in this order:

1. **Recall the five principles** (3 min). Accountability; AI proposes, a person decides;
   oversight proportionate to stakes; disclose where it would otherwise mislead; when unsure,
   be more cautious.
2. **Exam technique for Domain 8** (4 min). See section 5.
3. **Release the quiz** (3 min). 31 questions, 70% pass standard, completed in own time.
4. **Course close** (5 min). Domain 8 closes the Foundation course. Confirm the examination
   structure: 120 questions, 120 minutes, closed book, 70% pass mark (84 of 120), proctored.
   Point candidates to the final examination paper.

---

## 5. Exam Technique for Domain 8

Domain 8 is only 10 questions, so each one is worth 0.8% of the examination. Three recurring
traps account for most Domain 8 errors:

**Trap 1 — The plausible-but-wrong answer.**
Distractors are written to be attractive. Two recur:
- *"Cross-check it against another AI."* Never valid. Syllabus 6.4 requires primary sources.
  Sampling one model is not independent confirmation.
- *"The supplier is liable, so we are covered."* Never removes the deploying organisation's own
  accountability.

**Trap 2 — Over-reaching on the requirement.**
Options that demand perfection are usually wrong: publishing source code, exposing model
weights, reconstructing every decision years later, prohibiting all automated decisions,
disclosing every trivial AI use. The syllabus sets a **professional-literacy** standard, not a
technical or legal one.

**Trap 3 — Under-reaching on the duty.**
Options that treat the duty as optional are also wrong: assuming silence in a policy means
permission, treating advisory output as exempt from oversight, or assuming a people-affecting
use needs no bias assessment.

**The reliable test:** ask **who is accountable, and could they show their work?**

---

## 6. Discussion Questions for Extended Delivery

If the session is run in a longer format, these extend the discussions without adding new
syllabus content:

1. **The accountability gap.** If no individual can realistically review every automated
   decision, is "human oversight" a genuine safeguard or a legal fiction? What would make it
   genuine?
2. **Bias at the point of use.** Bias is often treated as a problem for model developers. What
   can a deploying organisation do about bias in a tool it did not build and cannot inspect?
3. **Disclosure fatigue.** If disclosure becomes required for a very wide range of content,
   will audiences stop noticing it? How should disclosure be designed to remain meaningful?
4. **The moving target.** Regulatory deadlines have moved and the landscape differs by
   jurisdiction. What does a professional do when the rule they are relying on is not the rule
   that applies?
5. **Automation bias under pressure.** Oversight fails most often when people are busy. What
   practical changes make oversight survive contact with a busy working day?

---

## 7. Instructor Preparation Checklist

- [ ] Confirm the approved demo tool for Demo 1 and Demo 3, in line with organisational policy.
- [ ] Prepare the two Demo 1 candidate summaries (identical except for the name).
- [ ] Prepare the Demo 3 task with its embedded error.
- [ ] Prepare the Demo 2 declined-decision slip.
- [ ] Print or display the Disclosure Exercise table and the Decision Framework drill scenarios.
- [ ] Confirm quiz access and the 70% pass standard.
- [ ] Confirm which domain(s) precede this session, and remind candidates that Domain 8 draws
      on Domains 4, 5, 6 and 7.
- [ ] **Do not** train candidates on specific commercial products. The certification is
      vendor-neutral and no examination question requires knowledge of a named product.

---

## 8. Sources Cited in This Plan

| # | Source | Used for |
|---|---|---|
| S1 | SYL_AIF v1.0, UKAIC AI Foundation Technical Syllabus, areas 8.1–8.6 (primary) | All learning outcomes and content |
| S2 | Stanford Report, "Researchers uncover AI bias against older working women", 17 October 2025 (Guilbeault, Delecourt, Srinivasa Desikan; published in *Nature*) | 8.1 bias evidence; 34,500 resumes across 54 occupations |
| S3 | artificialintelligenceact.eu, "The EU AI Act's Transparency Rules: A Practical Guide to Article 50", 14 May 2026 | 8.4 disclosure triggers; 8.5 regulatory awareness |
| S4 | European Commission, "Safer and more transparent AI", 2 August 2026 | 8.4 disclosure obligations in force |
| S5 | Epstein Becker Green, "AI Legislation: 2026 Legislative Wrap-Up", 22 July 2026 | 8.5 deployer responsibility; risk-based landscape |
| S6 | OWASP Top 10 for LLM Applications, 2026 edition | Cross-reference for 7.5 prompt injection; least-privilege framing |

**Note on the master reference guide.** `ai_in_the_workplace_master_guide.pdf` was also supplied
and recovered for this build. It corroborates this domain's content in four places (human
accountability, informed consent, bias auditing, mandatory human-in-the-loop gates) and its
enterprise governance checklist is consistent with 8.5. **Its own §1.5 describes an older
four-domain UKAIC framework that does not match SYL_AIF v1.0**, so it must not be used as the
structural basis for this course. Where it conflicts with the syllabus, the syllabus governs.

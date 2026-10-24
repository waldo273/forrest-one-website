# Research Notes — UKAIC AI Foundation Course Pack

Compiled 10 September 2026 from live web research. All claims below are sourced and
were captured during this build. Used to add depth and current examples beyond the syllabus.

## 1. The certification itself (primary source)

Source: https://ukaic.org/certifications and https://ukaic.org/
Retrieved: 10 September 2026

- UKAIC is an independent, not-for-profit **membership body** for the UK AI ecosystem.
- Positioning: "Prove what you know, vendor-neutral." Each certification is an
  **independent, industry-recognised examination — not a training course, and not a
  regulated qualification.** Training is delivered separately by authorised providers.
  This directly corroborates syllabus §2 of SYL_AIF v1.0.
- AI Foundation price: **£150**, vendor-neutral, entry-level.
- Pathway: **Foundation → Associate → Practitioner** (Associate and Practitioner listed
  "Coming soon", full syllabi in development at time of capture).
- Stated relationship to external frameworks: works "within existing frameworks such as
  NIST, ISO and the EU AI Act rather than adding another standard of our own."
  → Directly supports Domain 8.5 (high-level, risk-based regulatory picture).
- Membership grades: Affiliate → Associate → Practitioner → Fellow.
- Public briefings available (e.g. The UK AI Briefing); events programme includes a
  UK AI Council Launch Event and The Business Show London 2026.

### Why this matters for the course
The syllabus is deliberately **vendor-neutral and excludes product-specific knowledge**.
Every demo and lab must therefore be framed around *category of tool* and *transferable
technique*, never a named commercial product — otherwise we train learners away from the
exam blueprint.

## 2. Domain 6 — Hallucination: current, citable evidence

### 2.1 Legal sanctions are real and escalating
Source: https://www.haqq.ai/blog/when-ai-lies-to-the-court (retrieved 10 Sep 2026)
- As of April 2026, **1,313 court proceedings** involving AI-fabricated content documented.
- **496 involved licensed attorneys.**
- Single-matter sanctions have reached **USD 55,597**.
- Sanctions across 106 countries; enforcement tracks include monetary fines, mandatory
  CLE, public reprimand, and referral to bar disciplinary authorities.

Source: https://www.damiencharlotin.com/hallucinations/ (live case database, seen 10 Sep 2026)
- Cases dated **August 2026** in US federal and state courts involving fabricated case law.
- *Varma v. The Bank of New York Mellon* (Cal. Ct. App., 27 Aug 2026): appellants
  sanctioned, ordered to pay the respondent's appellate attorney fees, and the court
  forwarded the opinion to the State Bar for possible investigation. Hallmarks attributed
  to generative AI: non-existent cases, quotations not in the cited authorities,
  propositions unsupported by cited cases.
- Indian Supreme Court: set aside a judgment and penalty order where the Customs
  authority's order relied on judgments and articles apparently AI-generated — authorities
  were non-existent, or did not support the propositions attributed to them.

Source: https://arxiv.org/html/2606.21155 — "Who Checks the Citations? Benchmarking
Legal Hallucination Detection"
- Across **eight ChatGPT generations**, legal citation hallucination rates are **not
  consistently decreasing**.
- The verification burden is growing along two compounding dimensions: **more filings**
  and **more citations per filing**.
- Newer models generate *more* citations per document, drawn from a broader and less
  canonical set of cases that are individually **harder to verify**.
- >1,000 filings containing fabricated citations found; growth is year-over-year.

Source: https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more
- Leading legal research tools marketed as "hallucination-free" still hallucinate.
- Benchmarking found leading legal AI tools hallucinate in **1 out of 6 or more** queries.
- Earlier Stanford study of general-purpose chatbots: hallucinated **58%–82%** of the
  time on legal queries.
- Key nuance for teaching: a citation can exist yet not support the proposition
  attributed to it — "hallucination-free" in the narrowest sense is not enough.
- **RAG is not a panacea** — this is the empirical backing for syllabus 3.3's claim that
  RAG "reduces rather than removes error".

Source: https://www.tandfonline.com/doi/full/10.1080/08989621.2026.2645390
- If a published article contains GenAI-hallucinated citations, the researcher would be
  liable for **provable research misconduct** (fabricated data). Academic counterpart to
  the legal sanctions picture.

### 2.2 Teaching implication
Hallucination is not a curiosity — it has a documented, escalating professional penalty.
Learners must internalise **syllabus 6.3**: generated content is not sourced content, and
**citations, statistics, dates and quotes are the highest-risk elements**. Cross-checking
against *another AI* is specifically called out as invalid (syllabus 6.4) — this is
supported by the Stanford finding that RAG-based legal tools still fail.

## 3. Domain 7 — Prompt injection (OWASP, current)

Source: https://genai.owasp.org/llm-top-10/ and
https://www.helpnetsecurity.com/2026/08/06/owasp-2026-llm-top-10-released/
(retrieved 10 Sep 2026)

- OWASP publishes a **Top 10 for LLM Applications**; the **2026 edition** is current.
- **LLM01: Prompt Injection remains the #1 risk.** Ordering below the top two shifted
  more than in past years.
- **LLM02: Sensitive Information Disclosure** is #2.
- Important framing point for teaching: OWASP notes that because teams invest heavily in
  blocking prompt injection, **fewer successful attacks appear in public incident
  databases** — which makes the risk *look* smaller than it is. Absence of incident
  reports is not evidence of safety.
- Prompt Injection now explicitly covers **cross-modal attacks hidden in images or audio**.
- **Data and Model Poisoning** has absorbed fine-tuning subversion.
- LLM07: **System Prompt Leakage** — real incident: an extracted system prompt revealed an
  undisclosed assistant persona name, behavioural constraints, and operational rules,
  causing competitive-intelligence exposure.
- LLM05: **Improper Output Handling** — two-step chain: (1) adversary induces the model to
  generate malicious output via injection/jailbreak; (2) the application passes that
  output downstream and executes it without treating it as untrusted input. Demonstrated
  real-world case: SQL injection achieved through an LLM-powered application layer because
  model-generated queries were treated as trusted.
- Mitigations worth teaching: structural prompt delimiters with explicit trust-level
  markers between system instructions and untrusted content; **least privilege at the tool
  layer — an agent should not have high-risk tools available in the same turn it reads
  untrusted external content.**

### 3.1 Teaching implication
The syllabus tests prompt injection at *(awareness)* level (7.5), so learners need
**recognition, not exploitation**. The OWASP material supplies the authoritative hook:
"the model will be fooled" is a design assumption, not a bug to be patched away. The
least-privilege-in-the-same-turn rule is the single most transferable defence and pairs
directly with syllabus 3.4 (agents require greater human oversight).

## 4. Domain 4 — Prompt engineering: landscape check

Source: https://startbrain.ai/blog/prompt-engineering-course-guide/ and
https://iternal.ai/best-prompt-engineering-courses (retrieved 10 Sep 2026)

- Market consensus: **the best courses teach structured frameworks, not tips and tricks.**
  This validates the syllabus's 4.1 four-component anatomy (task, context, format,
  constraints) as the backbone rather than a bag of prompt "hacks".
- A recurring five-part AI competency framework appears across vendors:
  AI literacy → prompt engineering → critical evaluation → data responsibility →
  governance awareness. This maps almost exactly onto our Domains 1–2, 4, 6, 7, 8 —
  useful as external validation that the syllabus structure matches industry expectation.
- Vendor courses frequently bundle **security and data handling** alongside prompting,
  reinforcing the domain 4/6/7 adjacency.

Source: https://www.ibm.com/think/prompt-engineering — "The 2026 Guide to Prompt
Engineering" (IBM)
- Current emphasis on **multimodal prompting** (combining text, images and other media).
  This supports syllabus 3.2 (multimodal AI) and lets Domain 4 mention that prompting
  extends beyond text.

## 5. Excluded source: `ai_in_the_workplace_master_guide.pdf`

- Attached by the user but **never landed on disk**. Searched: the full home tree, the
  Hermes attachment cache (`~/.hermes/profiles/crest/attachments/`), `/tmp`, `/var/tmp`.
- The existing attachment cache contains only unrelated cybersecurity PDFs.
- **All content in this pack is therefore derived from SYL_AIF v1.0 plus the web sources
  cited above.** No content is attributed to the master guide. If it is re-supplied, the
  lesson content (not the exam-aligned structure) should be deepened from it.

## 7. UPDATE — `ai_in_the_workplace_master_guide.pdf` RECOVERED (10 Sep 2026)

Section 5 of this document recorded the master guide as "never landed on disk". **That is now
superseded.** The 21-page guide was recovered from the professor profile's image cache
(`/home/billy-forrest/.hermes/profiles/professor/images/pdf_p*_20260910_15223*.png`) and read
page by page. It is a 9-page master reference plus a 12-page syllabus render. Contents:

- §1 AI Architecture, Mechanics & Core Landscape — 4-tier spectrum (Classical Automation,
  Gen AI, Agentic AI, Advanced AI/AGI), 3-stage conceptual pipeline, development lifecycle
  (architecture → pre-training → instruction fine-tuning → RLHF → inference), and the
  **4 Memory Layers** table (parametric, working, external long-term/RAG, execution state)
  with separate Gen AI and Agentic AI failure modes per layer.
- §2 Effective Prompt Engineering — the **RTCF framework** (Role, Context, Task, Constraints,
  Format) **plus a Fallback Route** element; task-overloading remedies (prompt chaining,
  text chunking, RAG); and an anti-pattern table (Google Search prompt, Everything Bagel,
  Premise-Poisoned Query, No-Escape Query, Unbounded Code Dump) with corrective fixes.
- §3 Limitations & Hallucination — technical triggers of context loss (context window
  saturation / "lost in the middle", max token output cutoff, safety policy tripwires,
  stop-sequence collision, conversational amnesia); hallucination examples (ghost reference,
  contractual distortion, arithmetic fragility, phantom software APIs, biographical
  confabulation); and a 3-tier verification framework (manual HITL, prompt-based,
  automated).
- §4 Security, Privacy, Governance & Ethics — indirect prompt injection vectors "hidden in
  plain sight" (CV injection, quoted support thread, calendar invitation, zero-width Unicode,
  markdown/HTML comments, fake confidentiality footer); a PII/IP/least-privilege/regulatory
  governance table; and four ethical pillars (human accountability, informed consent,
  bias auditing, mandatory HITL gates) with an enterprise deployment checklist.

**Reconciliation note for course authors.** The master guide's §1.5 describes a *four-domain*
UKAIC framework (Understanding AI/Automation/ML; Applied GenAI & Prompting;
Ethics/Bias/Privacy/Regulation; Workplace Governance & Business Cases). That is **not the
current eight-domain SYL_AIF v1.0 structure** and must not be used to build the exam-aligned
course. It is useful as an alternative crosswalk only. Treat SYL_AIF v1.0 as authoritative for
all structure and weightings.

**Two content conflicts to teach explicitly rather than smooth over:**
1. The guide's RTCF table includes a **Fallback Route** as a prompt element. Syllabus 4.1 names
   **four** components (task, text, format, constraints). Foundation exam answers must follow the
   syllabus; the fallback permission is best taught as a 4.6 fault-fix technique, not a fifth
   component.
2. The guide's §3.3 lists **automated detectors** (logprobs, SelfCheckGPT, RAG faithfulness
   metrics). Syllabus 6.4 explicitly rejects cross-checking against *another AI* as a
   verification method. Reconcile precisely: sampling the *same* model for contradiction is not
   independent confirmation. Automated metrics are diagnostic signals, not verification.

## 8. Domain 8 — Ethics, bias, governance: research findings (10 Sep 2026)

### 8.1 Bias — peer-reviewed evidence at scale
Source: https://news.stanford.edu/stories/2025/10/ai-llms-age-bias-older-working-women-research
(Guilbeault, Delecourt, Srinivasa Desikan; published in *Nature*; retrieved 10 Sep 2026)
- ChatGPT prompted to generate **more than 34,500 unique resumes across 54 occupations**
  using typically male or female names.
- It wrote work histories portraying hypothetical women as **younger and less experienced**.
- Asked to rate those resumes, it **gave older men the highest ratings even where the
  underlying information was identical**.
- Analysis covered **1.4 million+ images and videos** plus **nine LLMs**; gendered age bias
  appears in text alone, "woven into the fabric of how we categorise and interpret people".
- Researchers criticise reliance on output filters as **"simplistic"**, missing nuanced bias
  such as gendered ageism: "the bias has to be addressed at a fundamental level."
- Directly supports syllabus 8.1 (sources of bias; real-world impacts in hiring) and the
  teaching point that removing an obvious field is not proof of fairness.

Source: https://www.sciencedirect.com/science/article/pii/S2590291125008113
- AI-driven HRM systems: discrimination risk embedded in recruitment tools and HR analytics.

### 8.4 Disclosure — Article 50 in force, and the date trap
Source: https://artificialintelligenceact.eu/transparency-rules-article-50/ (14 May 2026)
- Article 50 transparency obligations apply from **2 August 2026**.
- They apply to **ALL** AI systems used in the four covered situations, **not just high-risk**.
- The four situations: (1) AI interacts directly with people; (2) AI generates synthetic
  content; (3) emotion recognition or biometric categorisation; (4) deepfakes and text
  published on matters of public interest.
- **Providers** must mark generative outputs in machine-readable form and make them
  detectable as AI-generated. **Deployers** must disclose deepfakes and inform people exposed
  to emotion recognition or biometric categorisation.
- **Exception:** public-interest text does not require disclosure if it has been subject to
  human review with editorial responsibility attached.
- Confirmed by the Commission: https://commission.europa.eu/news-and-media/news/safer-and-more-transparent-ai-2026-08-02_en
- Transparency obligations are the **second most common compliance trigger** after AI
  literacy, affecting ~33% of respondents.

**Critical nuance for teaching (the date trap):**
- Annex III high-risk obligations were **postponed from 2 August 2026 to 2 December 2027**
  by the Digital Omnibus (a 16-month deferral). Article 6(1)/Annex I high-risk duties move
  to 2 August 2028. Sources: https://artificialintelligenceact.eu/high-level-summary/ and
  https://www.insideglobaltech.com/2026/05/28/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/
- Consequence: teaching a memorised compliance date is actively harmful. The examinable
  skill is knowing that obligations are **risk-based, broadening, and subject to movement**.

### 8.5 Governance — deployer responsibility and the risk-based patchwork
Source: https://www.ebglaw.com/insights/publications/ai-legislation-2026-legislative-wrap-up
(22 July 2026)
- With no comprehensive federal AI statute, states have produced a **patchwork** of
  obligations varying by jurisdiction, sector and use case.
- **Deployers, not just developers, bear compliance responsibility.** An organisation that
  integrates a third-party AI tool into hiring or clinical workflows is the regulated party.
- Employment AI regulation has moved to a **second generation**: auditing, reporting and
  affirmative anti-discrimination obligations, not merely disclosure.
- Health care is the most active arena: multiple states now prohibit AI as the **sole basis**
  for coverage denials and require human review of AI-assisted determinations.
- Directly supports syllabus 8.5 and the lesson-plan point that policy gaps belong with the
  organisation, which is the body able to assess and accept the risk.

Source: https://www.employmentlawletter.com/2026/05/connecticuts-ai-responsibility-and-transparency-act-key-impacts-on-the-workplace/
- Connecticut SB 5: disclosure and notice for automated tools in recruiting or personnel
  decisions; **using such tools is not a defence to discrimination claims**; from 1 October
  2026 certain WARN notices must disclose whether layoffs relate to AI use.
- Strong external corroboration of syllabus 8.2 ("the AI did it" is not a defence).

### 8.2 / 8.3 — accountability and oversight
Sources: https://aigovernancedesk.com/human-in-the-loop-oversight-frameworks-ai-governance/
and https://www.moodys.com/web/en/us/insights/ai/human-in-the-loop-why-human-oversight-still-matters-in-ai-driven-risk-and-compliance.html
- Human oversight is framed as far more than an override button: it is a combination of
  design, data and organisational mechanisms (EU AI Act Article 14 framing).
- Accountability remains a human responsibility because systems may analyse at scale but
  cannot answer for outcomes. Reinforces the syllabus's 8.2 and 8.6 principle.

## 9. Sources index — Domain 8 additions

| # | Source | Supports |
|---|---|---|
| S13 | https://news.stanford.edu/stories/2025/10/ai-llms-age-bias-older-working-women-research | 8.1 bias evidence (34,500 resumes / 54 occupations) |
| S14 | https://www.sciencedirect.com/science/article/pii/S2590291125008113 | 8.1 HRM discrimination risk |
| S15 | https://artificialintelligenceact.eu/transparency-rules-article-50/ | 8.4 disclosure triggers |
| S16 | https://commission.europa.eu/news-and-media/news/safer-and-more-transparent-ai-2026-08-02_en | 8.4 obligations in force |
| S17 | https://artificialintelligenceact.eu/high-level-summary/ | 8.5 high-risk timetable (Dec 2027) |
| S18 | https://www.insideglobaltech.com/2026/05/28/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/ | 8.5 Digital Omnibus deferral |
| S19 | https://www.ebglaw.com/insights/publications/ai-legislation-2026-legislative-wrap-up | 8.5 deployer responsibility, risk-based landscape |
| S20 | https://www.employmentlawletter.com/2026/05/connecticuts-ai-responsibility-and-transparency-act-key-impacts-on-the-workplace/ | 8.2 "not a defence", 8.4 employment disclosure |

## 6. Sources index

| # | Source | Supports |
|---|---|---|
| S1 | https://ukaic.org/certifications | Course framing, exam-not-course model, pathway |
| S2 | https://ukaic.org/ | Governance context, NIST/ISO/EU AI Act alignment |
| S3 | https://www.haqq.ai/blog/when-ai-lies-to-the-court | 6.1–6.3 sanction evidence |
| S4 | https://www.damiencharlotin.com/hallucinations/ | 6.2–6.3 live case law |
| S5 | https://arxiv.org/html/2606.21155 | 6.1 hallucination not self-correcting |
| S6 | https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more | 3.3, 6.4 RAG is not a panacea |
| S7 | https://www.tandfonline.com/doi/full/10.1080/08989621.2026.2645390 | 6.5 mandatory-verification contexts |
| S8 | https://genai.owasp.org/llm-top-10/ | 7.5 prompt injection |
| S9 | https://www.helpnetsecurity.com/2026/08/06/owasp-2026-llm-top-10-released/ | 7.4–7.5 current threat ordering |
| S10 | https://repello.ai/blog/owasp-llm-top-10-2026 | 7.5 mitigations, LLM05/LLM07 detail |
| S11 | https://startbrain.ai/blog/prompt-engineering-course-guide/ | 4.1 framework validation |
| S12 | https://www.ibm.com/think/prompt-engineering | 3.2, 4.x multimodal prompting |

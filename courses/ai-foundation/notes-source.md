# UKAIC AI Foundation: Student Notes and Revision Guide
## For the UKAIC AI Foundation examination (syllabus reference SYL_AIF v1.0). Complete study notes across all eight domains, written to the knowledge and awareness levels of the exam. No coding or mathematics required. No question in the exam requires knowledge of any specific commercial AI product.

## How to use this guide

This guide follows the official UKAIC AI Foundation technical syllabus domain by domain. Each domain is shown with its exam weighting and question count, and every sub area is covered with concise revision notes distilled from the "what is tested" column of the syllabus.

- Work through the domains in order, then revise the glossary and the decision framework at the back.
- Sub areas marked **awareness** are tested only at a recognition level: you need to recognise and identify the concept, not explain it in depth.
- The exam is closed book. Revise so that definitions, lists and the decision framework are recallable without notes.

## The exam at a glance

| Attribute | Specification |
|---|---|
| Awarding body | UK AI Council (UKAIC) |
| Syllabus reference | SYL_AIF v1.0 |
| Component | One written multiple choice paper |
| Questions | 120 multiple choice questions, single best answer |
| Pass mark | 70% (84 of 120) |
| Duration | 120 minutes |
| Delivery | Supervised and proctored, administered by authorised providers |
| Book | Closed book |
| Prerequisites | None |
| Vendor neutrality | No question requires knowledge of any specific commercial AI product |
| Level | Foundation: understand and apply concepts, not engineer or specialise |

## Domain weighting

The examination is weighted across the eight domains as follows. The practical competencies of effective use and verification carry the greatest weight, so prompt engineering (Domain 4) and limitations and verification (Domain 6) are the heaviest areas.

| Domain | Weighting | Questions |
|---|---|---|
| 1. Understanding AI: The Big Picture | 12% | 14 |
| 2. How AI Works (Without the Maths) | 14% | 17 |
| 3. The AI Landscape and Generative AI | 12% | 14 |
| 4. Prompt Engineering Fundamentals | 16% | 19 |
| 5. Working with AI Day to Day | 12% | 15 |
| 6. Limitations, Risks and Hallucination | 16% | 19 |
| 7. AI Security, Privacy and Data | 10% | 12 |
| 8. Ethics, Bias, Responsible AI and Governance | 8% | 10 |
| **Total** | **100%** | **120** |

---

## Domain 1. Understanding AI: The Big Picture

This domain builds accurate, vendor neutral vocabulary and framing for artificial intelligence. It corrects common misconceptions and makes sure you can talk about AI precisely.

### 1.1 Defining AI

- AI is a broad term for systems that perform tasks that normally require human intelligence.
- Most modern AI **learns patterns from data** to make predictions, generate content, or take actions. This is the working definition you should hold: AI learns patterns from data to predict, generate, or act.
- **What AI is not:** AI is not conscious, it is not infallible, and it is not "magic". It is a statistical tool that can make mistakes.
- Some systems are **rule based** rather than learning systems (they follow fixed instructions rather than learning from data). Recognise that both exist.
- A simple explanation can still be accurate: "simple is not wrong". Do not assume a plain explanation is incorrect just because it is short.


### 1.2 AI, ML, Deep Learning and Generative AI

- The four terms nest inside each other:
  - **AI** is the largest umbrella term.
  - **Machine learning (ML)** is a subset of AI: algorithms that learn from data.
  - **Deep learning** is a subset of ML: models with many layers inspired loosely by the structure of the brain.
  - **Generative AI** and **large language models (LLMs)** are a subset of deep learning that create new content.
- In other words: AI contains machine learning, which contains deep learning, which contains generative AI and LLMs.
- The four terms are often wrongly used as synonyms. You should be able to spot when a claim or product description uses them imprecisely.
- Precision matters when reading tool claims, vendor marketing, and media coverage: "AI powered" marketing often means a narrower technology underneath.


### 1.3 Narrow vs General AI

- **Narrow AI (weak AI / ANI):** systems designed for a specific task. They are capable within their domain but limited outside it. Examples include spam filtering, image recognition in medical diagnostics, and language translation.
- **General AI (strong AI / AGI):** a hypothetical system able to perform any intellectual task a human can. It is a research goal, not a current product.
- **All commercial AI today is narrow AI.** Apply the "narrow or general?" test to dramatic claims: any claim that a current product is truly general, conscious, or human-like should be treated with suspicion.


### 1.4 Everyday AI

- Narrow AI is already embedded in routine tools that most people use daily without noticing: spam filtering, search ranking, navigation, and recommendation systems.
- Awareness point: most professionals are already daily AI users, even if they would not describe themselves that way.


---

## Domain 2. How AI Works (Without the Maths)

This domain gives you an accurate, non mathematical model of how AI produces outputs and where it is unreliable. No maths is required, but you need the concepts precisely.

### 2.1 Models, Training and Inference

- A **model** is a set of learned values (called **parameters**), not a database of stored answers. It does not look up answers; it produces them from what it learned.
- **Training** is the process of learning the model from a dataset (adjusting the parameters so the model gets better at the task).
- **Inference** is using the trained model to produce an output from a new input.
- **Parameters** (at Foundation level) are the adjustable values learned during training. They are what the model actually is.


### 2.2 How Language Models Generate Text

- Language models work by **next token prediction**: producing the most likely continuation of the prompt and the text generated so far.
- Output is **generated, not retrieved**: the model creates text word by word; it is not pulling a stored answer out of a database.
- Because it is generated, **fluency does not guarantee accuracy**. A fluent sentence can still be wrong.
- The mechanism is more sophisticated than simple autocomplete, but the model has **no built in fact checker**. It is not checking facts as it writes.


### 2.3 Tokens and the Context Window

- **Tokens** are the basic unit of text a model reads and writes. A token is often a word or part of a word, not a whole sentence or page.
- The **context window** is the model's short term working memory: the fixed amount of text (tokens) it can consider at once.
- Exceeding the context window has effects: earlier detail may be "forgotten", and very long pastes can crowd out or push out your instructions.
- Practical ways to work within the window: keep prompts concise, put key instructions at the start or end (where they are most likely to be attended to), and chunk large inputs into separate smaller requests.


### 2.4 Knowledge Cut off

- A base model has **no knowledge of events after its training date** (its knowledge cut off).
- Time sensitive questions are therefore unreliable from the base model alone, because the model may be answering about a world state it has never seen.
- Some applications add **live search** on top of the model to bring in up to date information, but the base model itself remains frozen at its training date.


### 2.5 Variability and Embeddings

- Identical prompts can produce **different answers** because generation uses sampling: the model draws from a range of likely next tokens, influenced by settings such as the "temperature" (how random or creative the output is).
- Distinguish the **model** from the **application** built around it. The same model can power different apps with different guardrails, prompts, and interfaces.
- **Embeddings** (awareness): a way of representing the meaning of text as numbers, so that related items sit close together in a numerical space. Used for search and for finding similar content.


---

## Domain 3. The AI Landscape and Generative AI

This domain is a vendor neutral map of AI capabilities and how to choose the right category of tool. It stresses choosing a category, not a specific product.

### 3.1 Generative AI and Output Types

- **Generative** means producing new content, as opposed to classifying or labelling existing content.
- The major **output types** generative AI can produce: **text, image, audio/voice, video, and code**.


### 3.2 Foundation Models and Multimodal AI (both awareness)

- **Foundation models** (awareness): large, general purpose models adapted to many different tasks, rather than built for one task.
- **Multimodal AI** (awareness): AI that handles more than one type of input or output, for example text and images together.

### 3.3 Retrieval Augmented Generation (RAG)

- The **grounding problem**: a model generating from memory alone can produce answers not tied to real, current, or specific sources.
- **RAG** is a technique that first **retrieves relevant sources** (for example documents or web pages) and then **generates an answer grounded in those sources**.
- RAG improves **freshness and grounding**, but it **reduces rather than removes** error. Grounded output can still be wrong if the retrieved sources are wrong or misused.


### 3.4 AI Agents (awareness)

- An **AI agent** is a multi step, tool using system that pursues a goal, as opposed to a single turn assistant that just answers one question.
- Agents take actions and use tools across several steps.
- Because agents take actions, they **require greater human oversight**; an autonomous agent doing real work needs monitoring.

### 3.5 Model, Application and Service (awareness)

- Distinguish three layers:
  - The **model**: the engine that produces output.
  - The **application**: the interface the user interacts with.
  - The **AI enabled service**: the broader product or service the model powers.
- **Open weight / self hosted** versus **hosted** options (awareness): self hosting gives more control and data residency but needs setup and maintenance; hosted options are easier but data may leave your control. Trade offs: control and data residency versus convenience and maintenance.

### 3.6 Selecting a Tool Category

- Choose an appropriate **category of tool**, not a specific product.
- Decide using four factors: **capability, cost, data sensitivity, and organisational approval**.
- Whether an AI tool is appropriate depends on what it can do, what it costs, how sensitive the data is, and whether the organisation has approved its use.


---

## Domain 4. Prompt Engineering Fundamentals

This is the highest leverage practical skill in the exam, so it carries the most questions. You must be able to construct effective prompts and to improve weak ones.

### 4.1 Anatomy of a Prompt

- A strong prompt has four components:
  - **Task:** what you want the model to do.
  - **Context:** the background information the model needs.
  - **Format:** how you want the output arranged (for example a list, a table, or email style).
  - **Constraints:** limits and requirements (for example length, tone, what to exclude).
- To construct an effective prompt, state all four components clearly.


### 4.2 Role and Audience

- Assigning a **role** or **persona** to the model shapes the register of the output (for example "act as a senior editor").
- **Naming the audience** shapes depth and tone (for example "explain to a non technical reader").
- Role and audience together control how formal, how detailed, and how accessible the output is.

### 4.3 Few shot Prompting

- **Zero shot** prompting gives the model no examples and asks it to do the task directly.
- **Few shot** prompting gives the model one or more examples before asking it to do the task.
- Use examples to **calibrate style, format, and tone**: a couple of worked examples show the model exactly what you expect.
- Use few shot prompting when you need a specific style or format that the model is unlikely to guess from a description alone.


### 4.4 Structure and Decomposition

- **Request structured output**, for example tables, headed sections, or bullet lists, so the result is easy to scan and use.
- **Decompose** a complex task into ordered steps: break a large task into a sequence of smaller instructions.
- Ask for a **plan or reasoning** where useful, so the model works through a task methodically rather than guessing the whole answer at once.

### 4.5 Iterative Refinement

- Treat the **first output as a draft**, not the finished answer.
- **Refine through specific, corrective follow up prompts**: point out what is wrong and what to change (for example "shorten this to five sentences" or "remove the jargon").
- Understand prompting as a **conversation that builds on previous responses**, not a single one way request.


### 4.6 Common Prompting Faults

- Diagnose and correct these faults:
  - **Vague:** too general, no clear task (for example "give me info about sales").
  - **Overloaded:** too many instructions at once, so the model cannot do all of them.
  - **Leading:** the prompt steers the model toward a desired answer rather than asking for a fair analysis.
  - **Unformatted:** no requested structure, so the output is unstructured.
  - **"One and done":** giving up after the first weak output instead of refining it.


---

## Domain 5. Working with AI Day to Day

This domain applies AI to real professional work, with the judgement and habits that keep it safe. It stresses that you own the output.

### 5.1 Drafting and Rewriting

- Use AI to produce **first drafts** and to **reshape content**: shortening, re levelling for an audience, or changing tone or format.
- Always **review and personalise** AI output rather than using it unchanged. The output is a starting point, not the final product.

### 5.2 Summarising

- Use AI to produce **directed, audience targeted summaries** (for example "summarise for a busy executive in three bullets").
- Be aware of the limitation: **summaries can omit critical detail**.
- For high stakes documents, **read the original**, do not rely on a summary alone.


### 5.3 Ideation, Planning and Research Assistance

- Use AI as a **thinking partner** for ideas and planning, with **human ownership** of the result. The plan and decision are yours.
- Treat **research assistance** as a **starting point to verify**, not as an authoritative source.

### 5.4 Appropriate Use

- Decide when AI is suitable and when **human expertise, conventional tools, or authoritative sources** should lead.
- The decision depends on the **task and the stakes**: the higher the stakes, the more you need human expertise and verification.


### 5.5 The Verification Habit

- **Verify** facts, figures, dates, names, quotes, and citations **before acting on or sharing** AI output.
- Understand that **the user, not the AI, remains accountable** for what is produced and shared. "The AI did it" is not a defence.

### 5.6 Personal Prompt Library (awareness)

- The purpose of saving and organising **reusable prompts and templates** for recurring tasks: speed, consistency, and quality across repeated work.
- Awareness level: know that a personal prompt library stores reusable prompts for recurring tasks.

---

## Domain 6. Limitations, Risks and Hallucination

Critical evaluation and verification are core professional competencies and carry heavy weight in the exam. This domain is about spotting when AI is wrong.

### 6.1 Hallucination

- **Hallucination** is confident, fluent output that is **factually wrong, with no signal that anything is amiss**. The model does not flag that it is uncertain or mistaken.
- It is **inherent to how language models work** (probabilistic next token prediction), not an occasional bug that can be fully fixed.


### 6.2 Stale Information and Fabrication

- **Stale (out of date) output** arises from the knowledge cut off: the model cannot know events after its training date.
- **Fabrication:** the model can invent statistics, citations, quotes, and case studies that look authoritative but do not exist.

### 6.3 Provenance and Citation Checking

- Generated content is **not the same as sourced content**. A model generating prose is not checking a library.
- **Citations, statistics, and quotes are high risk**, because they are exactly the kinds of items the model will fabricate fluently.
- **Confirm important information at its original source** (the real document, dataset, or person), not from the model's claim.


### 6.4 Reducing the Risk

- Reduce hallucination risk by:
  - **Grounding prompts in real content** (paste in the actual documents to summarise, not "tell me about your documents").
  - Asking the model to **flag uncertainty** where it is not sure.
  - **Cross checking against primary sources**, not against another AI (an AI checking an AI can compound the error).
  - **Keeping a human in the loop** to review before the output is used.


### 6.5 Mandatory Verification Contexts

- Recognise contexts where verification is **mandatory**:
  - **Legal**
  - **Medical**
  - **Financial**
  - **Safety**
  - **HR / people decisions**
  - **Anything published externally**
- In these contexts, unverified AI output is not acceptable as a basis for action.

---

## Domain 7. AI Security, Privacy and Data

This domain is about protecting information and recognising AI enabled threats at a professional literacy level.

### 7.1 Protecting Information

- Do **not** enter into public or unapproved AI tools:
  - **Personal data**
  - **Confidential and commercially sensitive information**
  - **Credentials** (passwords, keys)
  - **Confidential documents**
- The default rule: **when in doubt, leave it out**. If you are not sure whether something can be shared with an AI tool, do not enter it.


### 7.2 Data Handling by AI Services

- **Third party services may transmit, store, or use inputs** according to their own terms and conditions.
- Basic concepts: **data retention** (how long inputs are kept) and **data residency** (where data is stored, which may be another country).
- **Organisational policy governs use**: what you may enter into which tool is set by your organisation, and you must comply.

### 7.3 Shadow AI

- **Shadow AI** is unapproved AI use outside organisational oversight: using tools the organisation has not sanctioned, often with data the organisation has not approved.
- It creates risk because there is no oversight of what data is exposed or how the tool behaves.
- Use **approved tools**, and **seek approval for new ones**. Treat a **policy gap as a reason to escalate** (ask), not as a reason to proceed on your own.


### 7.4 AI Enabled Threats (awareness)

- Recognise **deepfakes** (realistic fake images, audio, or video), **impersonation**, and **AI assisted phishing and social engineering**.
- For **unexpected or urgent requests** (for example a manager urgently asking for a payment or credentials), **verify through a separate, trusted channel**, not by replying to the same message.

### 7.5 Prompt Injection (awareness)

- **Prompt injection** is malicious instructions hidden inside content that the AI processes, designed to override the AI's intended behaviour (for example hidden text in a document that tells the AI to reveal data or ignore instructions).
- Be cautious with **untrusted content** (content of unknown origin that the AI reads) and keep **oversight of AI actions**.
- Awareness level: recognise what prompt injection is and the need for caution with untrusted content.

---

## Domain 8. Ethics, Bias, Responsible AI and Governance

Responsible use, oversight, disclosure, and a professional decision framework. Fewer questions, but the framework is central and often tested.

### 8.1 Bias and Fairness

- Bias has multiple **sources**: the **training data**, the **design choices**, and the **deployment context**.
- Bias produces **real world impacts** in people affecting uses such as **hiring, lending, and content**.
- **Bias assessment is a duty** in people affecting uses of AI: if AI affects people, you must assess and mitigate bias.


### 8.2 Transparency, Accountability and Explainability

- **The human or organisation remains accountable.** "The AI did it" is **not a defence**.
- **Transparency:** being open about when and how AI is used.
- **Explainability** (at Foundation level): the ability to give a reasonable account of why an AI produced a particular result.

### 8.3 Human Oversight

- **Human oversight is necessary** because AI, left to decide alone, can act in ways humans would not choose.
- Automated decision making raises risk where it affects people with no human review.
- The central principle: **AI proposes, while a person decides and owns the outcome.**


### 8.4 Disclosure

- Disclose AI use **where required, where AI substantially generated the content, or where non disclosure would mislead**.
- If a reader would reasonably assume a human wrote or created something, and a machine produced it, you should disclose.

### 8.5 Policy and Governance (policy full, regulatory picture awareness)

- An **organisational AI policy** sets out how AI may and may not be used, what tools are approved, and what data may be entered.
- Basic **governance** provides **oversight, accountability, and review** of AI use in the organisation.
- The **high level, risk based regulatory picture** (awareness): regulators take a risk based approach, with heavier expectations where AI affects people or safety. UKAIC works within existing frameworks such as NIST, ISO and the EU AI Act.

### 8.6 Professional Decision Framework

- Apply the four category framework for any AI task:
  - **Use:** the task is appropriate, low risk, and the AI is competent for it.
  - **Use with verification:** the output matters, so check facts and sources before acting.
  - **Escalate:** you are unsure whether AI is appropriate, the policy is unclear, or the task is beyond your judgement. Ask before proceeding.
  - **Do not use:** the task is unsafe, high stakes without verification possible, or prohibited by policy.
- **Be more cautious when unsure.** When in doubt, escalate or do not use.
- The framework demonstrates the central principle: **AI can assist while humans remain accountable.**


---

## Exam strategy and high yield tips

- **Domains 4 and 6 together are one third of the exam** (32% combined). Spend revision time on prompt engineering and on limitations, hallucination and verification.
- **Definitions matter.** Many questions test whether you can recall a definition exactly: hallucination, tokens, context window, inference vs training, narrow vs general AI.
- **Know your lists.** The output types (text, image, audio, video, code); the four prompt components (task, context, format, constraints); the data that must not be entered; the sources of bias.
- **The decision framework** (use, use with verification, escalate, do not use) is the most portable concept in the exam. Apply it to any scenario question.
- **Accountability always sits with the human or organisation.** Choose the option where a person verifies, decides, and owns the outcome.
- **Vendor neutral:** answers reference categories and practices, never a specific commercial product. Choose the option that is about the general concept, not a brand.
- **Simple is not wrong.** Prefer the plain, accurate, measured option over a dramatic or overclaimed one.

## Glossary of key terms

| Term | Meaning |
|---|---|
| Artificial intelligence (AI) | Systems that learn patterns from data to predict, generate content, or take actions |
| Machine learning (ML) | A subset of AI: algorithms that learn from data |
| Deep learning | A subset of ML: multi layered neural networks |
| Generative AI | Deep learning that produces new content (text, image, audio, video, code) |
| Large language model (LLM) | A deep learning model that recognises, summarises, translates, predicts and generates text on huge datasets |
| Model | A set of learned values (parameters) that produces outputs, not a database of answers |
| Parameter | An adjustable value learned during training |
| Training | Learning the model from a dataset |
| Inference | Using the trained model to produce an output |
| Token | The basic unit of text a model reads and writes |
| Context window | The model's short term working memory (fixed number of tokens it can consider) |
| Knowledge cut off | The date after which a base model has no knowledge |
| Embedding | A numerical representation of meaning so related items sit close together |
| Temperature | A setting controlling randomness or creativity of generation |
| Foundation model | A large, general purpose model adapted to many tasks |
| Multimodal AI | AI handling more than one type of input or output |
| Retrieval augmented generation (RAG) | Retrieving relevant sources, then generating an answer grounded in them |
| AI agent | A multi step, tool using system that pursues a goal |
| Hallucination | Confident, fluent output that is factually wrong with no signal of error |
| Zero shot prompting | Prompting with no examples |
| Few shot prompting | Prompting with one or more worked examples |
| Prompt injection | Malicious instructions hidden in content the AI processes |
| Shadow AI | Unapproved AI use outside organisational oversight |
| Deepfake | Realistic fake image, audio, or video of a person |
| Narrow AI | AI designed for a specific task, limited outside it |
| General AI (AGI) | A hypothetical AI able to perform any intellectual task a human can |
| Human in the loop | Keeping a person reviewing and deciding on AI output |

## Quick revision checklist

- I can define AI and say what it is not, and that "simple is not wrong".
- I can order AI, ML, deep learning and generative AI from broadest to most specific.
- I can distinguish narrow AI from general AI and state that all current AI is narrow.
- I can distinguish training from inference, and know a model is parameters, not a database.
- I can explain next token prediction and that fluency does not guarantee accuracy.
- I can define tokens and the context window, and describe what happens when it is exceeded.
- I can explain the knowledge cut off and why time sensitive questions are unreliable from the base model.
- I can describe variability (temperature) and that the model differs from the application.
- I can name the generative output types and explain what "generative" means.
- I can explain RAG: retrieve sources then generate a grounded answer; it reduces, not removes, error.
- I can describe agents and why they need more human oversight.
- I can list the four prompt components and build a prompt from them.
- I can set a role and audience, and use few shot prompting with examples.
- I can decompose complex tasks and refine output through follow ups.
- I can diagnose vague, overloaded, leading, unformatted and one and done prompts.
- I can use AI for drafting, summarising and ideation while owning and personalising the output.
- I know summaries can omit detail and that I must read high stakes originals.
- I have the verification habit and know the user, not the AI, is accountable.
- I can define hallucination and know why it is inherent, not a fixable bug.
- I know citations, statistics, quotes and dates are high risk and I check the original source.
- I know mandatory verification contexts: legal, medical, financial, safety, HR, and external publication.
- I protect personal, confidential, secret and credential data: when in doubt, leave it out.
- I can explain data handling by AI services, retention, residency, and organisational policy.
- I can recognise shadow AI, deepfakes and prompt injection, and escalate policy gaps.
- I can explain the sources of bias and the duty to assess bias in people affecting uses.
- I know that the human or organisation stays accountable and that "the AI did it" is no defence.
- I apply human oversight: AI proposes, a person decides and owns the outcome.
- I know when to disclose AI use.
- I can classify any task into use, use with verification, escalate, or do not use.
- I know the exam format: 120 questions, 70% pass, 120 minutes, closed book.

###### Good luck with your revision. See you at the exam.
#!/usr/bin/env python3
"""
Domain 8 — Ethics, Bias, Responsible AI & Governance
Question bank. 31 questions covering syllabus 8.1-8.6.

Every option carries an explanation of why it is right or wrong (q["why"], 4 entries).
Exam-aligned: no question requires knowledge of a specific commercial product.
"""

Q = [
# ---------------- 8.1 Bias & Fairness ----------------
{
 "q": "A recruitment team uses an AI screening tool trained on the company's own ten years of successful hires. It consistently ranks men above women for engineering roles, even though qualifications are equivalent. What is the most accurate description of what has happened?",
 "opts": [
   "The tool has learned patterns from historical data that reflect past hiring bias, so it reproduces and can amplify that bias at scale",
   "The tool has developed its own opinion about which candidates are better, so it should be asked to explain its reasoning",
   "The tool is malfunctioning and a software update will remove the pattern",
   "The tool is neutral; the outcome reflects genuine differences in candidate quality"
 ],
 "ans": 0,
 "exp": "Bias in AI commonly enters through the training data. Where historical hiring outcomes favoured one group, a model trained to reproduce those outcomes learns the same preference and can apply it consistently and at scale. This is a data and design problem, not a bug or a malfunction.",
 "why": [
   "Correct. Historical data carries historical bias; the model learns and scales that pattern.",
   "Wrong. Models do not hold opinions. They reproduce statistical patterns in their training data. This framing also invites the false comfort that an explanation will resolve the issue.",
   "Wrong. Reframing bias as a malfunction suggests a patch will fix it. Bias arises from data and design choices, so it requires review of those choices, not only a software update.",
   "Wrong. The question states qualifications are equivalent, so the difference in ranking is not explained by candidate quality. Neutrality of the tool cannot be assumed from the fact that it is automated."
 ]
},
{
 "q": "Under syllabus area 8.1, a bias assessment is described as a duty in which circumstances?",
 "opts": [
   "In uses that affect people, such as hiring, lending or access to services",
   "Whenever an AI tool is used for any purpose at all",
   "Only where legislation has already been breached",
   "Only when a model has been trained on data the organisation collected itself"
 ],
 "ans": 0,
 "exp": "Bias assessment is a duty where AI is used in ways that affect people, because the harm falls on individuals. Hiring, lending and access to services are the syllabus examples. It is not triggered by every possible use, nor only after a breach.",
 "why": [
   "Correct. People-affecting uses are where bias does real harm and where the duty applies.",
   "Wrong. Too broad. The syllabus ties the duty to people-affecting uses, not to any conceivable use of AI.",
   "Wrong. This is backwards. Assessment exists to prevent harm and demonstrate responsible use, not to respond only once the law has already been broken.",
   "Wrong. The source of the training data is not the trigger. The question is whose interests are at stake in the use."
 ]
},
{
 "q": "Which of the following is NOT identified in the syllabus as a source of bias?",
 "opts": [
   "The speed at which the model produces its output",
   "Training data",
   "Design choices made when building the system",
   "The context in which the system is deployed"
 ],
 "ans": 0,
 "exp": "The syllabus identifies three sources of bias: training data, design choices and deployment context. The processing speed of a model is not a source of bias, although it can reduce the opportunity for review.",
 "why": [
   "Correct. Speed is not a source of bias in the syllabus. It is a factor that can make oversight harder, which is a Domain 8.3 point.",
   "Wrong. Training data is explicitly named as a source of bias.",
   "Wrong. Design choices are explicitly named as a source of bias.",
   "Wrong. Deployment context is explicitly named as a source of bias. A model that behaves acceptably in one setting can cause harm in another."
 ]
},
{
 "q": "An AI tool used to shortlist job applicants was tested and found to select men at a notably higher rate than women with comparable qualifications. The organisation decides to keep using it but to remove names and gender markers from applications before screening. What is the best assessment?",
 "opts": [
   "Removing obvious markers may help but does not prove the tool is fair, because bias can persist through proxy signals in the remaining data",
   "The fix is sufficient, because the model can no longer see gender",
   "The fix is unnecessary, because the tool is only advisory",
   "The organisation should stop using AI in hiring entirely, since no AI tool can be made fair"
 ],
 "ans": 0,
 "exp": "Blinding obvious markers is a reasonable mitigation but not proof of fairness. Correlated features such as career gaps, institution names or phrasing can act as proxies that preserve the bias. Fairness has to be tested on outcomes, not assumed from the removal of a field.",
 "why": [
   "Correct. Removing a field reduces but does not eliminate the risk of proxy discrimination. Outcome testing is still required.",
   "Wrong. This mistakes an unobservable field for an unlearned pattern. Proxies can carry the same signal indirectly.",
   "Wrong. Advisory status does not remove the duty of care. An advisory ranking still steers human decisions and can cause the same harm.",
   "Wrong. Overcorrects. Bias can be assessed, mitigated and monitored. Abandoning the tool is one option, not the only defensible one."
 ]
},
{
 "q": "Which statement best reflects the relationship between bias and the deployment context?",
 "opts": [
   "A system that performs acceptably in one setting can cause harm in another, so context is part of the bias assessment",
   "A system that is unbiased in testing is unbiased everywhere, because bias is a property of the model alone",
   "Deployment context matters only for systems that make decisions without any human involvement",
   "Deployment context is a legal question and therefore outside a Foundation-level syllabus"
 ],
 "ans": 0,
 "exp": "The syllabus names deployment context as a source of bias. The same model can be harmless in a low-stakes setting and harmful in one that affects people's opportunities or safety, so the setting is part of the assessment.",
 "why": [
   "Correct. Context changes the stakes and can change the outcome, so it belongs in the assessment.",
   "Wrong. Bias is not a fixed property of a model alone. It emerges from the interaction of data, design and use.",
   "Wrong. Human involvement can reduce risk but does not make context irrelevant. An advised human can still be misled.",
   "Wrong. The syllabus tests bias assessment as a professional duty at Foundation level. High-level awareness of the regulatory picture appears separately at 8.5."
 ]
},

# ---------------- 8.2 Transparency, Accountability & Explainability ----------------
{
 "q": "An AI-assisted decision leads to a customer being denied a service. When challenged, a staff member says 'the system made that decision, so it is not something I can answer for.' Why is this not an acceptable response?",
 "opts": [
   "Because the human or the organisation remains accountable; 'the AI did it' is not a defence",
   "Because the system is a legal person and should be pursued directly",
   "Because the staff member should have overridden every AI recommendation",
   "Because customers are not entitled to any explanation of automated decisions"
 ],
 "ans": 0,
 "exp": "Accountability stays with the human and the organisation. An AI system cannot hold responsibility, so attributing the outcome to the system simply relocates blame to something that cannot answer for it. This is the central principle of syllabus 8.2.",
 "why": [
   "Correct. The AI cannot bear accountability, so the person and organisation that deployed it remain answerable.",
   "Wrong. AI systems are not legal persons and cannot be held liable. This misconception is exactly what the syllabus guards against.",
   "Wrong. Overstating the duty. Oversight means meaningful review of material decisions, not a requirement to overrule every recommendation.",
   "Wrong. This contradicts 8.2 and 8.4. Transparency and explainability at Foundation level exist precisely so decisions can be accounted for."
 ]
},
{
 "q": "What does 'explainability' mean at Foundation level in this syllabus?",
 "opts": [
   "Being able to give a meaningful account of how a decision was reached and what it was based on",
   "Publishing the full source code of the model",
   "Revealing the exact numerical weights inside the neural network",
   "Guaranteeing that every AI decision can be perfectly reconstructed years later"
 ],
 "ans": 0,
 "exp": "At Foundation level, explainability means being able to give a meaningful account of a decision: what information informed it and how it was arrived at. It is a professional-literacy standard, not a demand for source code or internal weights.",
 "why": [
   "Correct. Explainability is about giving a meaningful account of the basis for a decision.",
   "Wrong. Publishing source code is not required and would not by itself explain a decision. Many systems are also third-party services the organisation does not own.",
   "Wrong. Model weights are technical detail well beyond Foundation level and, on their own, do not explain a particular outcome in professional terms.",
   "Wrong. Perfect reconstruction is a much stronger standard than the syllabus requires and is often technically impossible."
 ]
},
{
 "q": "A manager is told that an automated tool rejected a large batch of applications. She asks for the criteria used. Which of the following best describes why this question matters?",
 "opts": [
   "Transparency and explainability allow the decision to be justified and reviewed, which is what makes accountability possible",
   "Because the criteria are the intellectual property of the organisation and must be protected",
   "Because a written reason removes any need for further human judgement",
   "Because automated decisions of any kind are prohibited without written reasons"
 ],
 "ans": 0,
 "exp": "Transparency and explainability are the mechanisms through which accountability becomes real. Without a defensible account of the criteria, nobody can review the decision or answer for it.",
 "why": [
   "Correct. Being able to state and review the basis of a decision is what makes the accountable party able to answer for it.",
   "Wrong. Protecting intellectual property is a separate concern and does not remove the need to account for a decision affecting a person.",
   "Wrong. A stated reason is a starting point for review, not a substitute for judgement. The human still owns the outcome.",
   "Wrong. The syllabus does not prohibit automated decisions. It requires oversight, transparency and accountability for them."
 ]
},

# ---------------- 8.3 Human Oversight ----------------
{
 "q": "Which statement best captures the relationship between AI and human decision-makers in the syllabus's oversight principle?",
 "opts": [
   "AI proposes while a person decides and owns the outcome",
   "AI decides while a person reviews the decision afterwards if time allows",
   "AI and the person share accountability equally for the decision",
   "A person must personally perform every calculation the AI would otherwise do"
 ],
 "ans": 0,
 "exp": "The syllabus states the principle directly: AI proposes, a person decides and owns the outcome. Oversight means the human holds the decision and the accountability, not that the human re-does the work.",
 "why": [
   "Correct. This is the syllabus formulation and the cleanest statement of meaningful oversight.",
   "Wrong. Post-hoc review that may not happen is not oversight. The human must be positioned to decide, not merely to audit afterwards.",
   "Wrong. Accountability cannot be shared with a system that cannot bear it. It rests with the human and the organisation.",
   "Wrong. Overstating the requirement. Oversight is about ownership of the decision, not duplication of every computation."
 ]
},
{
 "q": "In which situation does automated decision-making most clearly increase risk?",
 "opts": [
   "Where the decision materially affects a person's rights, opportunities or safety",
   "Where the decision is made quickly and cheaply",
   "Where the decision concerns an internal administrative matter",
   "Where the decision is based on data the organisation collected itself"
 ],
 "ans": 0,
 "exp": "Risk rises with the stakes for the individual. Decisions that materially affect people's rights, opportunities or safety are where automated decisions most clearly increase risk and where human oversight matters most.",
 "why": [
   "Correct. High stakes for the individual is the factor that most clearly increases risk.",
   "Wrong. Speed and cost are efficiency factors. They do not by themselves determine the risk to a person.",
   "Wrong. Internal administrative matters are generally lower stakes, though the principle still applies. They are not where risk most clearly increases.",
   "Wrong. The origin of the data does not determine the stakes. The nature of the decision and its effect on people does."
 ]
},
{
 "q": "An organisation deploys a tool that automatically approves or declines expense claims up to £500, with no human review, and reports no problems. What is the strongest reason for caution?",
 "opts": [
   "The absence of human oversight removes the ability to catch systematic errors or unfair patterns before they affect many people",
   "The tool will certainly be biased against every employee",
   "Automated approval is always unlawful below any monetary threshold",
   "Because the tool processes personal data, it cannot be used at all"
 ],
 "ans": 0,
 "exp": "No reported problems is not evidence of no problems. Without oversight, systematic errors or unfair patterns can be applied consistently to many people before anyone notices. Oversight provides the detection mechanism.",
 "why": [
   "Correct. Removing oversight removes the mechanism that catches systematic error and unfairness.",
   "Wrong. Overstating the claim. Bias is a risk to be assessed, not a certainty to be assumed.",
   "Wrong. The syllabus does not set monetary thresholds or prohibit automated approval as such. The concern is oversight proportionate to stakes.",
   "Wrong. Processing personal data is governed by policy and law (Domain 7), but it does not make the use impossible. Many uses are lawful and appropriate."
 ]
},

# ---------------- 8.4 Disclosure ----------------
{
 "q": "A customer service chatbot handles enquiries without telling users it is not a person. A customer later complains. Under syllabus 8.4, what is the core problem?",
 "opts": [
   "Users should be told when they are interacting with an AI system, because non-disclosure misleads them about who they are dealing with",
   "The chatbot gave incorrect information, which is the only real issue",
   "Chatbots are not permitted in customer service roles",
   "The problem is purely technical and can be resolved by improving the chatbot's accuracy"
 ],
 "ans": 0,
 "exp": "Disclosure is required where AI use would otherwise mislead. A person who believes they are speaking to a human is misled about the nature of the interaction, regardless of whether the information given was accurate.",
 "why": [
   "Correct. The failure is the misleading impression of human contact, which is exactly what 8.4 addresses.",
   "Wrong. Accuracy is a separate issue and is not the complaint here. A perfectly accurate chatbot can still breach disclosure expectations.",
   "Wrong. The syllabus does not prohibit chatbots. It requires appropriate disclosure of their nature.",
   "Wrong. Framing a disclosure duty as a technical accuracy problem misses the point entirely. The customer was not told what they were dealing with."
 ]
},
{
 "q": "Which of the following is the clearest case where AI use should be disclosed?",
 "opts": [
   "A published report was substantially generated by an AI tool",
   "An employee used a spell-checker to correct typing errors",
   "A member of staff used a search engine to look up a reference",
   "A team used a calculator to check a total"
 ],
 "ans": 0,
 "exp": "The syllabus ties disclosure to where it is required, where AI substantially generated the content, or where non-disclosure would mislead. Substantial generation of a published report is the clear case. Assistive tools that do not alter meaning are not the same thing.",
 "why": [
   "Correct. Substantial AI generation of published content triggers disclosure.",
   "Wrong. A spelling correction is an assistive edit that does not alter the substance or meaning of the content.",
   "Wrong. Using a search engine to locate a source is a research action, not the generation of content.",
   "Wrong. Checking arithmetic with a calculator is routine assistance and does not meet the disclosure threshold."
 ]
},
{
 "q": "A team uses AI to draft the bulk of an external policy document, then a senior manager reviews, edits and approves it. What does the syllabus suggest about disclosure?",
 "opts": [
   "Disclosure should be considered where AI substantially generated the content, and non-disclosure would mislead if readers assumed it was entirely human-authored",
   "Disclosure is never needed once a human has reviewed and approved the document",
   "Disclosure is required only if the document contains errors",
   "Disclosure is required for all documents of any kind produced with any AI assistance"
 ],
 "ans": 0,
 "exp": "Substantial AI generation is a disclosure trigger in its own right. The question to ask is whether omitting disclosure would mislead the audience. Human review and approval is good practice and may affect the judgment, but it does not automatically remove the trigger.",
 "why": [
   "Correct. Substantial generation plus a misleading impression is the trigger. Human review informs the judgment but does not erase it.",
   "Wrong. Review and approval is important and can affect the assessment, but it does not automatically settle the disclosure question.",
   "Wrong. Disclosure is about transparency regarding how content was produced, not about whether the content happens to be correct.",
   "Wrong. Too broad. Ordinary assistive uses that do not substantially generate the content are not disclosure triggers."
 ]
},

# ---------------- 8.5 Policy & Governance ----------------
{
 "q": "What is the primary purpose of an organisational AI policy?",
 "opts": [
   "To set out how AI may be used, who is accountable, and how use is reviewed",
   "To guarantee that the organisation will never experience an AI-related incident",
   "To prevent employees from learning about AI tools",
   "To satisfy a single regulator in one jurisdiction"
 ],
 "ans": 0,
 "exp": "A policy provides the framework: permitted use, accountability, and review. Its purpose is to make responsible use the default and to make responsibilities clear, not to promise that nothing will ever go wrong.",
 "why": [
   "Correct. Policy defines permitted use, assigns accountability and establishes review. These are the governance essentials.",
   "Wrong. No policy can guarantee the absence of incidents. Its value is in guiding behaviour and enabling response.",
   "Wrong. Policy is not about restricting knowledge. It is about directing use. Restricting awareness would also undermine the AI literacy obligations elsewhere in the framework.",
   "Wrong. Organisations commonly operate across multiple jurisdictions. A policy written to satisfy a single regulator is incomplete."
 ]
},
{
 "q": "An employee wants to use a new AI tool that is not on the organisation's approved list. What is the appropriate course of action according to syllabus 7.3 and 8.5?",
 "opts": [
   "Seek approval through the organisation's process, and treat a gap in policy as a reason to escalate rather than to proceed",
   "Use the tool for non-confidential work only, since the risk is limited",
   "Use the tool but avoid mentioning it, to prevent unnecessary delay",
   "Use the tool freely, because unapproved tools are only a concern for the IT department"
 ],
 "ans": 0,
 "exp": "The syllabus is explicit: use approved tools and seek approval for new ones. Where policy is silent, that is a reason to escalate, not a licence to proceed on personal judgement.",
 "why": [
   "Correct. Escalation is the syllabus position. A policy gap is a governance question for the organisation, not a decision for the individual.",
   "Wrong. Deciding unilaterally that the risk is limited is exactly the judgement the approval process exists to make. 'Non-confidential' is easy to get wrong.",
   "Wrong. Concealing unapproved use is the definition of shadow AI and is expressly contrary to the syllabus.",
   "Wrong. Responsibility for governance is not confined to one department. Every user has obligations, and the organisation carries the consequences."
 ]
},
{
 "q": "Which of the following best describes the regulatory picture as the syllabus presents it at Foundation level?",
 "opts": [
   "A high-level, risk-based landscape, in which obligations scale with the risk of the use",
   "A single worldwide AI law with uniform requirements that must be learned in detail",
   "A purely voluntary set of guidelines with no legal effect anywhere",
   "A matter for specialist legal interpretation and therefore outside this certification"
 ],
 "ans": 0,
 "exp": "The syllabus tests the regulatory picture at awareness level: a high-level, risk-based landscape. Obligations increase with the risk of the use. Detailed legal interpretation is explicitly outside the scope of this certification.",
 "why": [
   "Correct. Risk-based and high-level is the syllabus framing, with the regulatory picture marked as awareness.",
   "Wrong. There is no single worldwide AI law. Treating the landscape as one uniform regime is a factual error and beyond what is required here.",
   "Wrong. Regulatory frameworks are not purely voluntary, and describing them as having no legal effect is inaccurate.",
   "Wrong. The syllabus deliberately excludes legal interpretation, but that does not place the regulatory picture outside the certification. It is tested at awareness level."
 ]
},

# ---------------- 8.6 Professional Decision Framework ----------------
{
 "q": "The professional decision framework in syllabus 8.6 consists of which set of options?",
 "opts": [
   "Use / use with verification / escalate / do not use",
   "Use / delegate / automate / disclose",
   "Draft / review / publish / archive",
   "Ask / accept / record / move on"
 ],
 "ans": 0,
 "exp": "The syllabus framework has four outcomes: use, use with verification, escalate, and do not use. The final clause of 8.6 adds the direction that when unsure, be more cautious.",
 "why": [
   "Correct. These are the four options named in the syllabus.",
   "Wrong. These terms belong to other domains. Delegation and automation are not the framework's options.",
   "Wrong. This describes a document workflow, not a decision framework for AI use.",
   "Wrong. This is not the syllabus framework and omits the 'do not use' outcome entirely."
 ]
},
{
 "q": "A member of staff is unsure whether an AI tool may be used for a particular task, and the relevant policy does not clearly cover the situation. According to the syllabus, what should guide the decision?",
 "opts": [
   "Being more cautious when unsure, escalating the question rather than assuming permission",
   "Proceeding, because the absence of a prohibition implies permission",
   "Proceeding, because uncertainty is resolved by the individual's judgement",
   "Stopping all AI use across the organisation until a new policy is written"
 ],
 "ans": 0,
 "exp": "Syllabus 8.6 states that the framework is applied with greater caution when unsure. Combined with the escalation principle in 7.3, the correct response to an unclear situation is to ask.",
 "why": [
   "Correct. Caution and escalation are exactly what the syllabus prescribes when the position is unclear.",
   "Wrong. Silence in a policy is not permission. A gap is a reason to escalate.",
   "Wrong. The framework exists to constrain individual judgement in exactly these cases, not to rely on it.",
   "Wrong. Overcorrects. The obligation is to escalate the unclear case, not to halt all use across the organisation."
 ]
},
{
 "q": "Which statement best expresses the central principle that syllabus 8.6 requires candidates to demonstrate?",
 "opts": [
   "AI can assist with professional work, but humans remain accountable for the outcome",
   "AI should be avoided in professional work wherever it is possible to do so",
   "AI can be held accountable for outcomes where its recommendations were followed",
   "Accountability is transferred to the AI provider once a system is purchased"
 ],
 "ans": 0,
 "exp": "The central principle is that AI assists while humans remain accountable. This runs through 8.2, 8.3 and 8.6 and is the anchor for the whole domain.",
 "why": [
   "Correct. Assistance with retained human accountability is the syllabus's central principle.",
   "Wrong. The syllabus is not anti-AI. It requires responsible, accountable use, not avoidance.",
   "Wrong. Directly contradicts 8.2. 'The AI did it' is not a defence and AI cannot hold accountability.",
   "Wrong. Procuring a system does not transfer accountability away from the deploying organisation."
 ]
},

# ---------------- Applied / scenario synthesis ----------------
{
 "q": "A hospital plans to use an AI tool to help triage patients. Which combination of actions best reflects the syllabus across Domains 6, 7 and 8?",
 "opts": [
   "Keep a clinician in the loop for every decision, treat all output as requiring verification given the stakes, and use only an approved tool under organisational policy",
   "Use the tool as the primary decision-maker because it processes cases faster than staff",
   "Rely on the tool because medical software is regulated and therefore cannot be wrong",
   "Avoid recording that AI was used, to protect patient confidentiality"
 ],
 "ans": 0,
 "exp": "Medical contexts are named in syllabus 6.5 as mandatory-verification settings. Oversight (8.3) and approval (7.3) also apply. The correct combination keeps the clinician accountable, verifies the output, and uses the approved tool.",
 "why": [
   "Correct. High stakes require verification, human oversight and approved tooling, all of which the syllabus requires.",
   "Wrong. This inverts 8.3. AI proposes while a person decides, and 6.5 names medical contexts as requiring verification.",
   "Wrong. Regulation of a product does not make its outputs correct in every case, and it does not remove the operator's duty of care.",
   "Wrong. Concealing AI use is the opposite of the disclosure duty in 8.4 and conflicts with governance and audit requirements."
 ]
},
{
 "q": "A financial services firm uses AI to produce a creditworthiness score. An applicant is declined and asks why. Which response best meets the syllabus standard?",
 "opts": [
   "Provide a meaningful account of the basis for the decision, with a route to human review",
   "State that the decision was automated and therefore cannot be explained",
   "Provide the model's internal numerical weights so the applicant can assess them",
   "Decline to respond, on the basis that the model is commercially confidential"
 ],
 "ans": 0,
 "exp": "Credit scoring affects people's opportunities and is a high-stakes use. The syllabus requires transparency and explainability at Foundation level, plus human oversight. A meaningful account with a route to review satisfies all three.",
 "why": [
   "Correct. Explainability plus human oversight is precisely what 8.2 and 8.3 require in a people-affecting decision.",
   "Wrong. Contradicts 8.2. Automation does not extinguish accountability, and explainability is still required.",
   "Wrong. Internal weights are far beyond Foundation level and would not give the applicant a meaningful account in professional terms.",
   "Wrong. Commercial confidentiality does not remove the duty to account for a decision that affects a person."
 ]
},
{
 "q": "Which of the following best describes why 'the AI did it' fails as a professional defence?",
 "opts": [
   "Because accountability requires a party that can answer for the outcome, and an AI system has no standing to do so",
   "Because AI systems deliberately conceal their reasoning from users",
   "Because AI systems are owned by their providers, who become liable",
   "Because automated decisions are unlawful in professional contexts"
 ],
 "ans": 0,
 "exp": "The defence fails because accountability needs a subject that can answer for the outcome. An AI system cannot be answerable, so responsibility remains with the human and the organisation that chose to deploy it.",
 "why": [
   "Correct. Accountability requires a party capable of answering for the outcome. A system cannot be that party.",
   "Wrong. This attributes intent to a system that has none, and it misdescribes the basis of the principle.",
   "Wrong. Provider liability is a separate commercial and regulatory question. It does not remove the deploying organisation's own accountability.",
   "Wrong. Automated decisions are not unlawful as such. They carry oversight, transparency and accountability obligations."
 ]
},
{
 "q": "An organisation wants to introduce an AI tool that summarises employee performance reviews to inform promotion decisions. Which set of considerations from Domain 8 is most directly engaged?",
 "opts": [
   "Bias assessment, human oversight of people-affecting decisions, and disclosure to those affected",
   "Only the technical accuracy of the summarisation model",
   "Only the cost of the tool compared with manual summarisation",
   "Only the data retention terms of the supplier agreement"
 ],
 "ans": 0,
 "exp": "Performance summaries feeding promotion decisions are a people-affecting use. Bias assessment (8.1), human oversight (8.3) and disclosure (8.4) are all engaged, and the stakes are high because careers are affected.",
 "why": [
   "Correct. This use engages bias, oversight and disclosure together, which is the point of the domain.",
   "Wrong. Accuracy alone is insufficient. A technically accurate summary can still embed unfair patterns and be applied without proper oversight.",
   "Wrong. Cost is a business consideration, not the dominant ethical consideration in a people-affecting use.",
   "Wrong. Data terms matter under Domain 7, but they are not the most direct Domain 8 considerations for a promotion decision."
 ]
},
{
 "q": "A team wants to publish an article written largely by generative AI. The team lead says 'we do not need to say anything, because the facts have all been checked.' How should this be assessed?",
 "opts": [
   "Accuracy checking and disclosure are separate obligations; disclosure may still be required where AI substantially generated the content",
   "The assessment is correct, because verified content needs no disclosure",
   "Disclosure is only required if the article contains a factual error",
   "Disclosure is never required for text, only for images and video"
 ],
 "ans": 0,
 "exp": "Fact-checking addresses whether the content is correct. Disclosure addresses how the content was produced. They are distinct obligations under 8.4 and 6.3, and satisfying one does not discharge the other.",
 "why": [
   "Correct. Verification and disclosure are separate duties. Doing one does not remove the other.",
   "Wrong. This conflates two distinct obligations. Verified content can still require disclosure.",
   "Wrong. This makes disclosure depend on error, which inverts the purpose of transparency.",
   "Wrong. The syllabus disclosure principle is not limited to images and video. Substantial AI generation of text can trigger it, particularly where readers would be misled."
 ]
},
{
 "q": "Which of the following best illustrates the syllabus statement that bias is a duty in people-affecting uses rather than a purely technical concern?",
 "opts": [
   "A team documents how a screening tool was tested for differential outcomes before deployment and records the results for review",
   "A developer increases the model's accuracy score by two percentage points",
   "A manager confirms the tool runs within its expected response time",
   "A supplier confirms the tool meets its own published benchmarks"
 ],
 "ans": 0,
 "exp": "Treating bias as a duty means actively testing for differential impact in the uses that affect people, and documenting the results so the decision can be reviewed. Accuracy, latency and supplier benchmarks are not assessments of fairness.",
 "why": [
   "Correct. Outcome testing plus a documented record is what discharging the duty looks like in practice.",
   "Wrong. Overall accuracy can improve while differential outcomes stay the same or worsen. It is not a fairness measure.",
   "Wrong. Response time is a performance measure and says nothing about differential impact on groups.",
   "Wrong. Supplier benchmarks may be relevant evidence, but they are not the deployer's assessment of its own use and its own affected population."
 ]
},
{
 "q": "A junior employee is asked to send an AI-drafted response to a client complaint. Which action best demonstrates the professional decision framework from 8.6?",
 "opts": [
   "Review and verify the draft against the case record, correct it where needed, and take ownership of the final message",
   "Send the draft unchanged because the AI drafted it accurately",
   "Send the draft but add a line stating that AI produced it",
   "Refuse the task because AI should not be used in client communication"
 ],
 "ans": 0,
 "exp": "The framework's 'use with verification' outcome applies: check the draft against the real record, correct it, and own the result. This combines the verification habit (5.5) with the accountability principle (8.2).",
 "why": [
   "Correct. Use with verification plus personal ownership is exactly the framework's expected behaviour.",
   "Wrong. This ignores 5.5 and 8.6. Uncritical use of a draft is the behaviour the framework is designed to prevent.",
   "Wrong. A disclosure line is not a substitute for verification and may be unnecessary in a routine internal reply. The work of checking still has to be done.",
   "Wrong. Overcorrects. The syllabus does not prohibit AI use in client communication. It requires responsible, verified use."
 ]
},
{
 "q": "Which of the following most accurately states the relationship between the four ethical pillars described in Domain 8 and the wider syllabus?",
 "opts": [
   "Accountability, transparency, oversight and responsible use are interconnected, so weakness in one undermines the others",
   "Each pillar operates independently, so an organisation need only satisfy the one most relevant to its sector",
   "Only accountability carries any practical weight, because the others are aspirational",
   "The pillars apply only to organisations that develop their own AI models"
 ],
 "ans": 0,
 "exp": "The pillars reinforce one another. Oversight without transparency cannot be meaningful, and accountability without disclosure cannot be demonstrated. Weakness in one undermines the rest.",
 "why": [
   "Correct. The pillars are interdependent, which is why the syllabus presents them as a framework rather than a checklist.",
   "Wrong. Treating them as independent invites gaps. An organisation that satisfies only one has not achieved responsible use.",
   "Wrong. All four carry practical weight and appear in the decision framework and governance material.",
   "Wrong. The obligations fall on deployers and users, not only on model developers. Most organisations are deployers."
 ]
},
{
 "q": "An organisation adopts a policy requiring that AI-generated content intended for external publication be reviewed by a named individual before release. Which governance purpose does this serve?",
 "opts": [
   "It assigns clear accountability and inserts a human decision point where errors could cause public harm",
   "It transfers liability to the reviewing individual and away from the organisation",
   "It removes the need for any disclosure of AI use",
   "It guarantees that published content will contain no errors"
 ],
 "ans": 0,
 "exp": "Naming a responsible reviewer creates an accountable human decision point before externally visible release, which is precisely what governance is for. It does not shift organisational liability, remove disclosure duties, or guarantee accuracy.",
 "why": [
   "Correct. Clear accountability plus a human gate at the highest-risk moment is the core purpose of the control.",
   "Wrong. Naming a reviewer does not transfer liability away from the organisation, which remains accountable for its systems and processes.",
   "Wrong. Review and disclosure are separate obligations. Reviewing content does not remove the duty to disclose where required.",
   "Wrong. Review reduces risk. It cannot guarantee the absence of errors."
 ]
},
{
 "q": "Which statement correctly distinguishes a Foundation-level understanding of responsible AI from a specialist one?",
 "opts": [
   "Foundation level requires understanding and applying responsible-use principles in professional work, not legal or technical specialisation",
   "Foundation level requires the ability to interpret AI regulation in detail",
   "Foundation level requires the ability to build and audit a machine learning model",
   "Foundation level requires only awareness that AI exists and carries risks"
 ],
 "ans": 0,
 "exp": "The syllabus states that all content is tested at Foundation level: candidates understand and apply concepts rather than engineer, implement or specialise. Legal interpretation and model building are explicitly excluded.",
 "why": [
   "Correct. Understand and apply is the Foundation standard. The exclusions are explicit in the syllabus scope statement.",
   "Wrong. Legal and regulatory interpretation is expressly excluded from the syllabus.",
   "Wrong. Model building and technical implementation are excluded. Awareness of how models work is not the same as being able to build one.",
   "Wrong. Too low a standard. Foundation level requires application and judgement, not passive recognition, other than for the items marked awareness."
 ]
},
{
 "q": "An organisation's AI policy is two years old and predates the tools its staff now use daily. What does the syllabus suggest about the governance response?",
 "opts": [
   "The policy should be reviewed and updated, because governance requires ongoing review as practice and the field change",
   "The policy remains valid indefinitely because it was formally approved",
   "Staff should be trusted to interpret an out-of-date policy as they see fit",
   "The policy should be withdrawn entirely rather than updated"
 ],
 "ans": 0,
 "exp": "Syllabus 8.5 describes governance as including oversight, accountability and review. A policy that no longer reflects how AI is actually used cannot guide behaviour or assign responsibility, so it needs periodic review rather than permanent validity.",
 "why": [
   "Correct. Review is a named element of governance, and a policy that lags actual practice has stopped doing its job.",
   "Wrong. Formal approval at a point in time does not make a policy fit for purpose as tools and practice change.",
   "Wrong. Leaving interpretation to individuals removes the accountability structure that policy exists to provide, and encourages shadow AI.",
   "Wrong. Overcorrects. The remedy for an out-of-date policy is to update it, not to remove the governance framework altogether."
 ]
},
]

#!/usr/bin/env python3
"""
Final examination question banks for Domains 1, 2, 3, 5, 7.
Written to the exact examination weightings in SYL_AIF v1.0:
  D1 = 14, D2 = 17, D3 = 14, D5 = 15, D7 = 12
Each question: 4 options, ans (0-3), exp, why[4]. Foundation level, vendor-neutral.
"""

# ============================ DOMAIN 1 (14 questions, 12%) ============================
Q1 = [
{
 "q": "Which statement best describes what most modern artificial intelligence actually does?",
 "opts": [
   "It learns patterns from data in order to make predictions, generate content or take actions",
   "It stores a large database of verified facts and looks up the correct answer",
   "It reasons from first principles in the way a human expert does",
   "It follows a fixed set of written rules that programmers supply in advance"
 ],
 "ans": 0,
 "exp": "Most modern AI learns patterns from data and then uses those patterns to make predictions, generate content or take actions. This is the syllabus definition and the foundation for everything else in Domain 1.",
 "why": [
   "Correct. Learning patterns from data to produce predictions, content or actions is the syllabus definition.",
   "Wrong. This describes a database lookup. A learning system derives answers from learned patterns rather than retrieving stored ones.",
   "Wrong. Reasoning from first principles is not how these systems work. They generalise from statistical patterns.",
   "Wrong. This describes rule-based systems, which the syllabus separately identifies as a distinct and older approach."
 ]
},
{
 "q": "A colleague says an AI tool 'knows' the answer because it is intelligent in the human sense. How should this be corrected?",
 "opts": [
   "The tool produces likely outputs from patterns in its training data; it is not conscious and is not infallible",
   "The tool is conscious but its consciousness is not observable to users",
   "The tool does know the answer, because it was trained on a very large amount of text",
   "The tool has no relationship to its training data and produces answers at random"
 ],
 "ans": 0,
 "exp": "Syllabus 1.1 states plainly what AI is not: not conscious, not infallible, not magic. Fluency in output is a property of pattern-based generation, not evidence of understanding.",
 "why": [
   "Correct. Pattern-based generation without consciousness or guaranteed accuracy is the syllabus position.",
   "Wrong. Suggesting an unobservable consciousness is not a correction and is not supported by the syllabus.",
   "Wrong. Large training data improves fluency and coverage but does not confer knowledge in the human sense, nor accuracy.",
   "Wrong. Overcorrects. The outputs are derived from training data; they are not random, which is precisely what makes them persuasive."
 ]
},
{
 "q": "Which of the following best illustrates that a simple explanation of AI can still be accurate?",
 "opts": [
   "Describing a language model as producing likely continuations of text, which is a simplification but not a falsehood",
   "Stating that AI is magic because the internal process is too complex to describe",
   "Claiming that AI has feelings because it responds sympathetically",
   "Saying that AI cannot be explained at all and should simply be trusted"
 ],
 "ans": 0,
 "exp": "Syllabus 1.1 notes that some systems are rule-based rather than learning systems and that 'simple does not equal wrong'. A simplified but truthful description is accurate; a false description dressed up as simplicity is not.",
 "why": [
   "Correct. Simplified-but-true is the syllabus standard. It is a legitimate description of the mechanism.",
   "Wrong. Magic is a false explanation, not a simple one, and the syllabus explicitly rejects it.",
   "Wrong. This attributes a capacity the system does not have. Sympathetic phrasing is generated, not felt.",
   "Wrong. This conflates complexity with inexplicability and encourages uncritical trust."
 ]
},
{
 "q": "Which of the following is an example of a rule-based system rather than a learning system?",
 "opts": [
   "A system that checks an invoice against a fixed set of validation conditions",
   "A system that groups customers by reviewing past purchasing behaviour",
   "A system that generates a written summary of a long document",
   "A system that predicts which email users are most likely to open"
 ],
 "ans": 0,
 "exp": "Syllabus 1.1 notes that some systems are rule-based rather than learning systems. Fixed validation conditions apply explicit rules; the other options derive behaviour from data.",
 "why": [
   "Correct. Fixed validation conditions are rules applied directly, with no learning from data.",
   "Wrong. Grouping customers from past behaviour is learning from data, which is a learning system.",
   "Wrong. Generating a summary requires a trained model, not a fixed rule set.",
   "Wrong. Predicting which emails users open is derived from historical patterns, so it is a learning system."
 ]
},
{
 "q": "Which sequence correctly shows how the terms nest, from broadest to narrowest?",
 "opts": [
   "Artificial intelligence contains machine learning, which contains deep learning, which contains generative AI",
   "Machine learning contains artificial intelligence, which contains generative AI, which contains deep learning",
   "Generative AI contains deep learning, which contains machine learning, which contains artificial intelligence",
   "Artificial intelligence, machine learning, deep learning and generative AI are all separate and unrelated fields"
 ],
 "ans": 0,
 "exp": "Syllabus 1.2 requires candidates to state the nesting: AI contains machine learning, which contains deep learning, which contains generative AI and large language models.",
 "why": [
   "Correct. This is the exact nesting described in the syllabus.",
   "Wrong. This inverts the relationship. Machine learning is a subset of AI, not the other way round.",
   "Wrong. This reverses the order entirely. Generative AI is the narrowest category, not the broadest.",
   "Wrong. The terms are nested, not separate. Treating them as unrelated is the error the syllabus asks candidates to avoid."
 ]
},
{
 "q": "A software vendor advertises that its product 'uses AI' when it is in fact a machine learning model performing classification. How should a professional respond?",
 "opts": [
   "Recognise that the claim is imprecise and that precision matters when reading tool claims and marketing",
   "Accept the claim, because machine learning is a form of artificial intelligence and the statement is therefore false",
   "Reject the product, because vendors who use broad terms cannot be trusted",
   "Ignore the terminology, because the distinction has no practical consequence"
 ],
 "ans": 0,
 "exp": "Syllabus 1.2 explains that precision matters when reading tool claims, vendor marketing and media coverage. Machine learning is a subset of AI, so the claim is technically defensible but vague rather than false. Precision lets a professional ask what the system actually does.",
 "why": [
   "Correct. The issue is imprecision, and the syllabus specifically says precision matters in marketing claims.",
   "Wrong. A machine learning model is a form of AI, so the statement is not false. It is imprecise, which is a different problem.",
   "Wrong. Rejecting a product on terminology alone is an overreaction and is not what the syllabus asks for.",
   "Wrong. The distinction has practical consequences, because it determines what questions to ask about capability and limits."
 ]
},
{
 "q": "Which of the following correctly distinguishes machine learning from deep learning?",
 "opts": [
   "Deep learning uses neural networks with many layers, and sits within the broader category of machine learning",
   "Deep learning is a broader category that contains all of machine learning",
   "Machine learning requires no data, whereas deep learning requires data",
   "The two terms are exact synonyms and may be used interchangeably"
 ],
 "ans": 0,
 "exp": "The syllabus requires the nesting to be understood: machine learning contains deep learning, which uses multi-layered neural networks. They are not synonyms.",
 "why": [
   "Correct. Deep learning is a subset of machine learning characterised by multi-layered neural networks.",
   "Wrong. This reverses the nesting. Deep learning sits inside machine learning, not outside it.",
   "Wrong. Both approaches learn from data. The claim that machine learning requires no data is false.",
   "Wrong. The syllabus specifically identifies treating these terms as synonyms as an error to avoid."
 ]
},
{
 "q": "Which statement best defines artificial general intelligence (AGI)?",
 "opts": [
   "A hypothetical system able to perform any intellectual task a human can, and a research goal rather than a current product",
   "A large language model that performs well on a wide range of benchmarks",
   "Any AI system capable of performing more than one task",
   "A general-purpose AI system available to the public without a licence"
 ],
 "ans": 0,
 "exp": "Syllabus 1.3 defines AGI as a hypothetical system able to perform any intellectual task a human can, and states it is a research goal and not a current product.",
 "why": [
   "Correct. This is the syllabus definition, including its status as a hypothesis rather than a shipping product.",
   "Wrong. Strong benchmark performance is evidence of broad capability within narrow tasks, not general intelligence.",
   "Wrong. Narrow AI routinely handles many tasks. Multi-task ability is not the AGI threshold.",
   "Wrong. Public availability and licensing have nothing to do with the AGI definition."
 ]
},
{
 "q": "A news article claims a new model 'has achieved general intelligence'. What is the most reliable test to apply?",
 "opts": [
   "Ask whether it can perform any intellectual task a human can, or whether it is a system designed for specific tasks and limited outside them",
   "Ask whether the model was trained on a very large dataset",
   "Ask whether the model is available to the public",
   "Ask whether the model can pass a single difficult examination"
 ],
 "ans": 0,
 "exp": "Syllabus 1.3 requires candidates to apply the 'narrow or general?' test to dramatic claims. Narrow systems are capable within their domain and limited outside it. All commercial AI today is narrow.",
 "why": [
   "Correct. This is the narrow-versus-general test the syllabus asks candidates to apply.",
   "Wrong. Dataset size affects capability within a domain. It does not establish general intelligence.",
   "Wrong. Availability is a distribution question, not a capability question.",
   "Wrong. Excelling on one examination demonstrates narrow capability in that area, not general intelligence."
 ]
},
{
 "q": "Which of the following is the most accurate statement about narrow AI?",
 "opts": [
   "It is designed for specific tasks, is capable within its domain and is limited outside it",
   "It is a temporary stage that all current systems have already moved beyond",
   "It can only perform a single task and nothing else under any circumstances",
   "It refers to AI systems with deliberately limited training data"
 ],
 "ans": 0,
 "exp": "Syllabus 1.3 defines narrow AI as systems designed for specific tasks, capable within their domain but limited outside it. All commercial AI today is narrow.",
 "why": [
   "Correct. This is the syllabus definition of narrow AI.",
   "Wrong. Narrow AI is the current state of all commercial AI, not a stage that has been passed.",
   "Wrong. Slightly overstates it. Narrow systems can handle several related tasks; the limitation is breadth of domain.",
   "Wrong. The term refers to scope of capability, not the size of the training dataset."
 ]
},
{
 "q": "Which of the following is the clearest example of narrow AI already embedded in everyday tools?",
 "opts": [
   "Email spam filtering that classifies incoming messages",
   "A system that can perform any intellectual task a human can",
   "A chatbot that is conscious of the conversation",
   "A tool that has replaced the need for human judgement in all decisions"
 ],
 "ans": 0,
 "exp": "Syllabus 1.4 asks candidates to recognise narrow AI already embedded in routine tools such as spam filtering, search ranking, navigation and recommendations.",
 "why": [
   "Correct. Spam filtering is a named syllabus example of everyday narrow AI.",
   "Wrong. This describes AGI, which the syllabus states is hypothetical and not a current product.",
   "Wrong. Chat systems are not conscious. This invokes a misconception the syllabus explicitly addresses.",
   "Wrong. No system has replaced human judgement, and the syllabus requires humans to remain accountable."
 ]
},
{
 "q": "Why does syllabus 1.4 state that most professionals are already daily AI users?",
 "opts": [
   "Because narrow AI is embedded in routine tools such as search ranking, navigation and recommendations that people use without thinking of them as AI",
   "Because everyone has now attended formal AI training",
   "Because all workplace software now contains generative AI",
   "Because using a computer is itself a form of AI use"
 ],
 "ans": 0,
 "exp": "The syllabus point is that AI is already embedded in routine tools and used daily, often without the user identifying it as AI. This matters because it means AI literacy is not an optional future concern.",
 "why": [
   "Correct. Embedded narrow AI in everyday tools is the reason the syllabus gives.",
   "Wrong. The claim is about tool use, not training. Most users have had no formal AI training at all.",
   "Wrong. Too strong. Generative AI is one form of AI and is not present in all workplace software.",
   "Wrong. Using a computer is not the same as using AI. The claim is specific to AI-enabled features."
 ]
},
{
 "q": "A manager claims her team does not use AI at all. Which response is most consistent with the syllabus?",
 "opts": [
   "Most professionals already use some form of narrow AI daily, so the useful question is which tools use it and how they should be governed",
   "She is correct if her team only uses standard office software",
   "She is correct because AI only counts as AI when it is generative",
   "She should be advised to avoid all AI use to keep the position accurate"
 ],
 "ans": 0,
 "exp": "Syllabus 1.4 makes the practical point that most professionals are already daily AI users. The valuable move is to recognise where AI is in use and govern it accordingly, not to debate the label.",
 "why": [
   "Correct. Recognising embedded AI and governing it is the professionally useful response.",
   "Wrong. Standard office software increasingly includes AI-enabled features such as ranking, suggestions and prediction, so the claim is unlikely to hold.",
   "Wrong. Narrow non-generative AI such as ranking and classification is still AI.",
   "Wrong. Avoidance is not the syllabus position. Responsible, accountable use is."
 ]
},
{
 "q": "Which of the following statements about all commercial AI available today is correct?",
 "opts": [
   "It is narrow AI, designed for specific tasks and limited outside its domain",
   "It is general AI, because modern models handle many different tasks",
   "It is a mixture, with several general AI systems in commercial use",
   "It is rule-based and contains no machine learning"
 ],
 "ans": 0,
 "exp": "Syllabus 1.3 states explicitly that all commercial AI today is narrow. Handling multiple tasks within a broad domain does not make a system general.",
 "why": [
   "Correct. All commercial AI today is narrow, per the syllabus.",
   "Wrong. Handling many tasks is not the same as being able to perform any intellectual task a human can.",
   "Wrong. There are no commercially deployed general AI systems. AGI remains a research goal.",
   "Wrong. Modern commercial AI is predominantly learning-based, not purely rule-based."
 ]
},
]

# ============================ DOMAIN 3 (14 questions, 12%) ============================
Q3 = [
{
 "q": "What does 'generative' mean in relation to AI?",
 "opts": [
   "The system produces new content rather than classifying or labelling existing content",
   "The system produces content that has never existed anywhere in any form, from no source at all",
   "The system generates revenue by automating tasks",
   "The system generates explanations of its own reasoning on request"
 ],
 "ans": 0,
 "exp": "Syllabus 3.1 defines generative as producing new content, as distinct from classifying or labelling. The output is generated from learned patterns rather than selected from a fixed list of labels.",
 "why": [
   "Correct. Producing new content, contrasted with classification, is the syllabus definition.",
   "Wrong. Overstated. Generated content derives from patterns in training data. It is new in composition, not conjured from nothing.",
   "Wrong. This is a commercial meaning of 'generate' and is unrelated to the technical sense.",
   "Wrong. Producing explanations is one possible output, not the definition of generative AI."
 ]
},
{
 "q": "Which of the following is NOT one of the major generative AI output types identified in the syllabus?",
 "opts": [
   "Financial advice",
   "Text",
   "Audio and voice",
   "Video and code"
 ],
 "ans": 0,
 "exp": "Syllabus 3.1 lists the major output types as text, image, audio/voice, video and code. 'Financial advice' is a professional service and a regulated activity, not an output type.",
 "why": [
   "Correct. Financial advice is not an output type. It is a regulated professional activity, which is a useful reminder that generated content can touch regulated territory.",
   "Wrong. Text is one of the listed output types.",
   "Wrong. Audio and voice is one of the listed output types.",
   "Wrong. Video and code are both listed output types."
 ]
},
{
 "q": "What is a foundation model?",
 "opts": [
   "A large, general-purpose model that can be adapted to many different tasks, at awareness level",
   "The first model a company ever trains, on which later models are built",
   "A model that has been formally certified as the basis for a product",
   "A small, specialised model used only for a single narrow task"
 ],
 "ans": 0,
 "exp": "Syllabus 3.2 tests foundation models at awareness level as large, general-purpose models adapted to many tasks.",
 "why": [
   "Correct. Large, general-purpose and adaptable to many tasks is the syllabus description.",
   "Wrong. This is chronological, not definitional. The term describes scale and generality, not development order.",
   "Wrong. Certification is a regulatory concept and is not part of the definition.",
   "Wrong. This describes the opposite of a foundation model, which is large and general rather than small and specialised."
 ]
},
{
 "q": "Which of the following best describes multimodal AI?",
 "opts": [
   "A system that handles more than one type of input or output, such as text and images together",
   "A system that can be used by many people at the same time",
   "A system deployed across many different departments",
   "A system that produces several alternative answers to one question"
 ],
 "ans": 0,
 "exp": "Syllabus 3.2 tests multimodal AI at awareness level as handling more than one type of input or output.",
 "why": [
   "Correct. Multiple modalities of input or output is the syllabus definition.",
   "Wrong. Concurrent users is a scale question about serving, not about modalities.",
   "Wrong. Departmental spread is an organisational question, not a technical one about modalities.",
   "Wrong. Offering alternatives is a sampling behaviour, not multimodality."
 ]
},
{
 "q": "What problem does retrieval-augmented generation (RAG) primarily address?",
 "opts": [
   "The grounding problem: the model answers from its own frozen parameters with no reference to current or specific source material",
   "The cost of training a model from scratch",
   "The speed at which a model produces its output",
   "The need to disclose when AI has been used"
 ],
 "ans": 0,
 "exp": "Syllabus 3.3 identifies the grounding problem and describes RAG as retrieving relevant sources and then generating an answer grounded in them.",
 "why": [
   "Correct. RAG retrieves sources so the answer can be grounded in them rather than drawn only from the model's own parameters.",
   "Wrong. Training cost is a separate concern. RAG operates at inference time and does not retrain the model.",
   "Wrong. Response speed is not the problem RAG is designed to solve, and retrieval can add latency.",
   "Wrong. Disclosure is a governance requirement, addressed in Domain 8, not the purpose of RAG."
 ]
},
{
 "q": "Which statement about RAG is most accurate?",
 "opts": [
   "RAG improves freshness and grounding but reduces rather than removes error",
   "RAG eliminates hallucination because answers come from retrieved sources",
   "RAG removes the need for the user to verify anything",
   "RAG makes a model's knowledge permanently current"
 ],
 "ans": 0,
 "exp": "Syllabus 3.3 states directly that RAG improves freshness and grounding but reduces rather than removes error. This distinction is tested, and it is the reason verification remains necessary.",
 "why": [
   "Correct. This is the exact syllabus formulation, and it is why verification cannot be dropped.",
   "Wrong. This is the tempting error. Retrieval improves grounding but does not eliminate error. Tools marketed as hallucination-free have been shown to fail.",
   "Wrong. Verification remains essential. RAG changes how answers are produced, not the user's accountability for them.",
   "Wrong. Knowledge is current only insofar as the retrieved sources are current. A stale or partial index still yields weak grounding."
 ]
},
{
 "q": "What distinguishes an AI agent from a single-turn assistant?",
 "opts": [
   "An agent pursues a goal across multiple steps, using tools, rather than responding once to one prompt",
   "An agent is any assistant that remembers the conversation",
   "An agent is a system with a larger model behind it",
   "An agent is an assistant that has been approved for enterprise use"
 ],
 "ans": 0,
 "exp": "Syllabus 3.4 defines agents as multi-step, tool-using systems that pursue a goal, distinct from a single-turn assistant.",
 "why": [
   "Correct. Multi-step goal pursuit with tool use is the distinguishing characteristic.",
   "Wrong. Conversation memory is a feature of a session, not what makes a system agentic.",
   "Wrong. Model size is not the distinction. A larger model in a single-turn setting is still single-turn.",
   "Wrong. Approval is an organisational status and has nothing to do with the definition."
 ]
},
{
 "q": "Why does the syllabus state that agents taking actions require greater human oversight?",
 "opts": [
   "Because an agent can take consequential actions across several steps, so errors can compound and effects can be harder to reverse",
   "Because agents are inherently less accurate than single-turn assistants",
   "Because agents cannot use tools safely under any circumstances",
   "Because agents are not permitted in professional environments"
 ],
 "ans": 0,
 "exp": "Syllabus 3.4 marks this point at awareness level. The concern is that multi-step action-taking amplifies both the reach of errors and the difficulty of reversing them, so oversight must be stronger.",
 "why": [
   "Correct. Compounding errors and harder reversal are why oversight needs to be greater.",
   "Wrong. Accuracy is not the essential difference. The scope of action is.",
   "Wrong. Tool use is the point of an agent. The requirement is oversight, not prohibition.",
   "Wrong. Agents are used professionally. The syllabus requires greater oversight, not exclusion."
 ]
},
{
 "q": "Which correctly distinguishes a model, an application and an AI-enabled service?",
 "opts": [
   "The model is the engine, the application is the interface built around it, and the service is the offering delivered to users",
   "The model is the interface, the application is the engine, and the service is the training data",
   "All three terms refer to the same thing and are interchangeable",
   "The service is the model, and the application is the hardware it runs on"
 ],
 "ans": 0,
 "exp": "Syllabus 3.5 requires this distinction: the model is the engine, the application is the interface, and the service is what is delivered. The distinction matters because obligations and risks attach to different layers.",
 "why": [
   "Correct. Engine, interface and delivered offering is the syllabus distinction.",
   "Wrong. This misassigns every layer and invents a role for training data that the syllabus does not describe.",
   "Wrong. The syllabus specifically asks candidates to distinguish them, so they are not interchangeable.",
   "Wrong. This conflates the model with the service and misdescribes the application as hardware."
 ]
},
{
 "q": "An organisation wants maximum control over data residency and model behaviour. Which option and trade-off does the syllabus describe?",
 "opts": [
   "Open-weight or self-hosted deployment gives more control but requires more setup and maintenance",
   "Open-weight deployment gives more control and requires no additional effort",
   "Hosted services always give more control over data residency",
   "Data residency is unrelated to the choice between self-hosted and hosted services"
 ],
 "ans": 0,
 "exp": "Syllabus 3.5 marks this at awareness level: open-weight and self-hosted options trade control and data residency against setup and maintenance effort.",
 "why": [
   "Correct. Control and residency improve, but setup and maintenance effort rises.",
   "Wrong. Self-hosting requires infrastructure, updates and expertise. The effort is real.",
   "Wrong. Hosted services generally give less control over where data resides and how it is handled.",
   "Wrong. Data residency is a central consideration in this choice, which is why the syllabus names it."
 ]
},
{
 "q": "When selecting an appropriate category of AI tool, which set of factors does syllabus 3.6 identify?",
 "opts": [
   "Capability, cost, data sensitivity and organisational approval",
   "Brand recognition, market share and user reviews",
   "Model parameter count, release date and benchmark score",
   "Speed of output, number of features and subscription tier"
 ],
 "ans": 0,
 "exp": "Syllabus 3.6 identifies capability, cost, data sensitivity and organisational approval as the factors for choosing a category of tool.",
 "why": [
   "Correct. These are the four factors named in the syllabus.",
   "Wrong. Brand and popularity are not the syllabus criteria and can conflict with the exam's vendor-neutral stance.",
   "Wrong. Technical benchmarks are not the Foundation-level basis for tool selection and are not vendor-neutral in practice.",
   "Wrong. These are feature comparisons rather than the syllabus's professional selection criteria."
 ]
},
{
 "q": "Why does the syllabus emphasise choosing a 'category' of tool rather than a specific product?",
 "opts": [
   "Because the certification is vendor-neutral, so the testable skill is recognising what kind of tool is appropriate",
   "Because specific products are too expensive for most organisations",
   "Because product names change too quickly to be memorised",
   "Because only categories of tool can be approved by an organisation"
 ],
 "ans": 0,
 "exp": "The syllabus excludes knowledge of any specific commercial product. The transferable skill is selecting a category based on capability, cost, data sensitivity and approval.",
 "why": [
   "Correct. Vendor neutrality is a stated property of the certification, so the skill is category selection.",
   "Wrong. Cost is one selection factor, but it is not the reason for the category-level framing.",
   "Wrong. Rate of change is a supporting reason at best. The stated reason is vendor neutrality.",
   "Wrong. Organisations approve specific products. The syllabus distinction is about what is tested, not what is procured."
 ]
},
{
 "q": "A team needs to summarise a very large set of current internal documents and has an approved vector-store pipeline available. Which approach is most appropriate?",
 "opts": [
   "Retrieval-augmented generation, so answers are grounded in the organisation's own current sources",
   "Asking the base model from memory, because it has seen similar documents in training",
   "Fine-tuning the model on the documents before every query",
   "Pasting all documents into a single prompt regardless of length"
 ],
 "ans": 0,
 "exp": "RAG is designed for exactly this case: retrieving relevant sources from a corpus and grounding the answer in them. The base model has no access to internal documents and a training cut-off besides.",
 "why": [
   "Correct. RAG grounds answers in the organisation's own current sources, which is its purpose.",
   "Wrong. The base model has no access to internal documents and cannot answer from them reliably.",
   "Wrong. Fine-tuning before every query is not a practical or proportionate response, and RAG addresses the need directly.",
   "Wrong. Exceeding the context window causes earlier detail to be lost, which the syllabus identifies as a specific failure."
 ]
},
{
 "q": "Which statement best captures the relationship between generative AI and classification systems?",
 "opts": [
   "Generative systems produce new content, whereas classification systems assign existing content to categories or labels",
   "Generative systems assign labels, whereas classification systems produce new content",
   "Both terms describe the same operation performed at different speeds",
   "Classification systems are a more advanced form of generative AI"
 ],
 "ans": 0,
 "exp": "Syllabus 3.1 contrasts generative AI, which produces new content, with classifying or labelling, which assigns existing content to categories.",
 "why": [
   "Correct. Producing new content versus assigning labels is the distinction the syllabus draws.",
   "Wrong. This reverses the two definitions.",
   "Wrong. They perform fundamentally different operations, not the same one faster.",
   "Wrong. Classification is not an advanced form of generation. They are different tasks."
 ]
},
]

# ============================ DOMAIN 5 (15 questions, 12%) ============================
Q5 = [
{
 "q": "A professional uses AI to produce a first draft of a report. What does the syllabus say should happen next?",
 "opts": [
   "The draft should be reviewed and personalised rather than used unchanged",
   "The draft should be sent as produced, to save time",
   "The draft should be discarded, because AI output cannot be used professionally",
   "The draft should be published with a note that AI produced it and no further review"
 ],
 "ans": 0,
 "exp": "Syllabus 5.1 requires that AI output be reviewed and personalised rather than used unchanged. The draft is a starting point that the professional owns once they adopt it.",
 "why": [
   "Correct. Review and personalisation is the syllabus requirement for drafting with AI.",
   "Wrong. Using the draft unchanged is the behaviour the syllabus warns against.",
   "Wrong. Overcorrects. The syllabus supports drafting with AI, subject to review.",
   "Wrong. Disclosure and review are separate obligations. A disclosure note does not substitute for reviewing the work."
 ]
},
{
 "q": "Which of the following is an example of reshaping existing content with AI, as described in syllabus 5.1?",
 "opts": [
   "Shortening a long report and re-levelling it for a non-specialist audience",
   "Asking the model to invent supporting statistics for a report",
   "Requesting a list of sources the model is confident about",
   "Asking the model to confirm that a document is legally accurate"
 ],
 "ans": 0,
 "exp": "Syllabus 5.1 lists shortening, re-levelling for an audience, and changing tone or format as reshaping tasks.",
 "why": [
   "Correct. Shortening and re-levelling for a different audience is exactly the reshaping use described.",
   "Wrong. Inventing statistics is fabrication, not reshaping, and is the highest-risk behaviour addressed in Domain 6.",
   "Wrong. Confidence is not a reliable indicator of accuracy, and sourcing requires verification at the original source.",
   "Wrong. Legal accuracy requires qualified human expertise. AI cannot confirm it, and legal interpretation is outside the syllabus."
 ]
},
{
 "q": "What limitation of AI summarising does the syllabus specifically identify?",
 "opts": [
   "Summaries can omit critical detail, so the original must be read for high-stakes documents",
   "Summaries are always longer than the original",
   "Summaries cannot be produced for technical documents",
   "Summaries are only accurate if the document is under one page"
 ],
 "ans": 0,
 "exp": "Syllabus 5.2 identifies the limitation that summaries can omit critical detail and requires reading the original for high-stakes documents.",
 "why": [
   "Correct. Omission of critical detail is the named limitation and the reason high-stakes documents must be read in full.",
   "Wrong. A summary is by definition shorter. This is not a limitation the syllabus identifies.",
   "Wrong. Summarisation works across document types, though quality varies.",
   "Wrong. Length alone does not determine summary reliability."
 ]
},
{
 "q": "A team is preparing a summary of a contract for a board decision. What does the syllabus require?",
 "opts": [
   "The original should be read, because this is a high-stakes document where omitted detail could matter",
   "The AI summary can be relied upon if it is well written",
   "The AI summary can be relied upon if the model was given the whole document",
   "The summary should be produced by two different AI tools and compared"
 ],
 "ans": 0,
 "exp": "Syllabus 5.2 requires the original to be read for high-stakes documents. Provision of the whole document improves grounding but does not remove the risk that critical detail is omitted from the summary. Comparing two AI outputs is specifically rejected as verification under 6.4.",
 "why": [
   "Correct. High stakes plus the risk of omitted detail means the original must be read.",
   "Wrong. Writing quality is a fluency signal, not an accuracy signal, and it does not protect against omission.",
   "Wrong. Full-document input improves grounding but does not guarantee that nothing critical was dropped.",
   "Wrong. Cross-checking against another AI is explicitly not verification under syllabus 6.4."
 ]
},
{
 "q": "Which of the following best describes using AI as a thinking partner for ideation and planning?",
 "opts": [
   "Generating and testing ideas with AI while retaining human ownership of the result",
   "Delegating the decision to AI because it can consider more options",
   "Using AI output as the final plan without further consideration",
   "Avoiding AI in planning because ideas must be original"
 ],
 "ans": 0,
 "exp": "Syllabus 5.3 supports AI as a thinking partner for ideas and planning, with human ownership of the result.",
 "why": [
   "Correct. AI assists with idea generation and testing; the human owns the outcome.",
   "Wrong. Delegating the decision contradicts the ownership requirement.",
   "Wrong. This treats a draft as a final decision and removes human judgement from the process.",
   "Wrong. Overcorrects. The syllabus supports ideation with AI, subject to ownership of the result."
 ]
},
{
 "q": "How does the syllabus characterise AI research assistance?",
 "opts": [
   "As a starting point to verify, not an authoritative source",
   "As an authoritative source when the model is well regarded",
   "As a complete substitute for primary research",
   "As unsuitable for any professional research purpose"
 ],
 "ans": 0,
 "exp": "Syllabus 5.3 states that research assistance should be treated as a starting point to verify, not as an authoritative source.",
 "why": [
   "Correct. A starting point requiring verification is the syllabus position.",
   "Wrong. Model reputation does not confer authority. Authority comes from the original source.",
   "Wrong. AI assistance complements research. It does not replace primary sources.",
   "Wrong. Overcorrects. The syllabus supports AI research assistance, subject to verification."
 ]
},
{
 "q": "What determines whether AI is appropriate for a given task according to syllabus 5.4?",
 "opts": [
   "The nature of the task and the stakes involved, which together indicate when human expertise or authoritative sources should lead",
   "Whether the task can be completed quickly with AI",
   "Whether the team has been trained on the specific tool",
   "Whether the organisation has a licence for the tool"
 ],
 "ans": 0,
 "exp": "Syllabus 5.4 requires determining when AI is suitable and when human expertise, conventional tools or authoritative sources should lead, based on task and stakes.",
 "why": [
   "Correct. Task type and stakes determine whether AI, human expertise or an authoritative source should lead.",
   "Wrong. Speed is an efficiency consideration and does not settle appropriateness.",
   "Wrong. Training is a readiness factor, not the determinant of appropriateness.",
   "Wrong. Licensing is a commercial and compliance matter, not the basis for appropriateness."
 ]
},
{
 "q": "A junior employee is asked to provide a legal opinion on a contract clause. Which action is most consistent with syllabus 5.4?",
 "opts": [
   "Escalate to qualified human expertise, because the task requires expertise the AI cannot supply",
   "Produce the opinion with AI and note that AI assisted",
   "Produce the opinion with AI and have a colleague read it",
   "Produce the opinion with AI, since the clause is short and self-contained"
 ],
 "ans": 0,
 "exp": "Legal interpretation requires qualified human expertise and is explicitly outside the syllabus scope. Where human expertise should lead, the appropriate action is to escalate.",
 "why": [
   "Correct. Where qualified expertise is required, the task should go to that expertise.",
   "Wrong. Disclosure does not supply the missing qualification.",
   "Wrong. Peer review by an unqualified colleague does not provide the required expertise.",
   "Wrong. Clause length is irrelevant. The nature of the task is what requires expertise."
 ]
},
{
 "q": "Which of the following should always be verified before AI output is acted on or shared?",
 "opts": [
   "Facts, figures, dates, names, quotes and citations",
   "Only the spelling and grammar",
   "Only the sections the reader is most likely to check",
   "Nothing, provided the output reads fluently"
 ],
 "ans": 0,
 "exp": "Syllabus 5.5 names facts, figures, dates, names, quotes and citations as the elements to verify. Fluency is not evidence of accuracy.",
 "why": [
   "Correct. These are the specific high-risk elements named in the syllabus.",
   "Wrong. Presentation checks do not address factual accuracy at all.",
   "Wrong. Verification cannot be limited to what an audience might happen to check.",
   "Wrong. Fluency is precisely what makes unverified output dangerous, because it discourages checking."
 ]
},
{
 "q": "Who remains accountable for AI-assisted work according to syllabus 5.5?",
 "opts": [
   "The user, not the AI",
   "The AI system, because it produced the output",
   "The tool vendor, because it supplied the system",
   "No one, because AI output is provisional by nature"
 ],
 "ans": 0,
 "exp": "Syllabus 5.5 states that the user, not the AI, remains accountable. This principle recurs in Domain 8.2 and 8.6.",
 "why": [
   "Correct. The user remains accountable, and this is stated explicitly.",
   "Wrong. An AI system cannot bear accountability. This is the recurring error the syllabus guards against.",
   "Wrong. Vendor liability is a commercial matter and does not transfer the user's professional accountability.",
   "Wrong. Provisional outputs still require a responsible human. Accountability is not dissolved by the nature of the tool."
 ]
},
{
 "q": "What is the purpose of maintaining a personal prompt library, as described in syllabus 5.6?",
 "opts": [
   "To save and organise reusable prompts and templates for recurring tasks, at awareness level",
   "To record every prompt ever used for audit purposes",
   "To share prompts publicly for professional recognition",
   "To prevent colleagues from using the same prompts"
 ],
 "ans": 0,
 "exp": "Syllabus 5.6 tests at awareness level the purpose of saving and organising reusable prompts and templates for recurring tasks.",
 "why": [
   "Correct. Reusable prompts and templates for recurring tasks is the stated purpose.",
   "Wrong. A prompt library is a working aid, not an audit log. Audit requirements are a governance matter under Domain 8.",
   "Wrong. Public sharing is not the stated purpose and raises separate data considerations.",
   "Wrong. Exclusivity is not the purpose. The library is a personal efficiency aid."
 ]
},
{
 "q": "A team members' AI-generated client email contains a specific figure that the model supplied without any source. What is the correct action?",
 "opts": [
   "Verify the figure against the authoritative source before sending",
   "Send it, because the model is generally reliable with numbers",
   "Send it with a caveat that the figure is unverified",
   "Remove the figure and send the email without it"
 ],
 "ans": 0,
 "exp": "Figures are named in syllabus 5.5 as elements requiring verification, and invented statistics are identified in 6.2 as a specific fabrication risk. Verification against the primary source is the correct action.",
 "why": [
   "Correct. Unsupported figures are a named high-risk element and must be verified at source.",
   "Wrong. Sourced or not, a figure from a model carries no authority. Reliability in general is not evidence for this figure.",
   "Wrong. A caveat shifts risk to the client rather than resolving it, and an unverified figure should not be sent at all.",
   "Wrong. Removing the figure may be acceptable in some cases, but the syllabus requirement is to verify. The figure may well be correct and necessary."
 ]
},
{
 "q": "Which of the following best describes the relationship between drafting with AI and professional authorship?",
 "opts": [
   "The professional remains the author of the work and takes responsibility for the final content",
   "The AI is the author because it produced the words",
   "Authorship is shared equally between the professional and the AI",
   "Authorship is determined by who last edited the text"
 ],
 "ans": 0,
 "exp": "Syllabus 5.1 requires review and personalisation, and 5.5 places accountability on the user. The professional who adopts and issues the work is its author and is responsible for it.",
 "why": [
   "Correct. Adopting the work makes the professional responsible for it as its author.",
   "Wrong. A system cannot be an author or hold responsibility.",
   "Wrong. Accountability cannot be shared with an entity that cannot bear it.",
   "Wrong. Editing order does not determine authorship or responsibility."
 ]
},
{
 "q": "An analyst uses AI to help plan a project and then follows the plan without checking whether it accounts for a known regulatory constraint. What is the primary failure?",
 "opts": [
   "Treating AI output as a finished decision rather than a draft to be assessed against known constraints",
   "Using AI for planning, which the syllabus does not permit",
   "Failing to disclose the use of AI in the planning process",
   "Failing to use a second AI tool to check the plan"
 ],
 "ans": 0,
 "exp": "Syllabus 5.3 requires human ownership of the result. A plan that ignores a known constraint has not been owned. Using AI for planning is permitted, and cross-checking with another AI is not a valid verification method.",
 "why": [
   "Correct. The failure is adopting a draft as a decision without applying known constraints and judgement.",
   "Wrong. The syllabus supports AI use for planning, with human ownership.",
   "Wrong. Disclosure is a separate question and not the primary failure here.",
   "Wrong. Cross-checking against another AI is explicitly not verification under syllabus 6.4."
 ]
},
{
 "q": "Which task is LEAST appropriate to delegate to AI without substantial human involvement?",
 "opts": [
   "Deciding whether an employee should be dismissed for misconduct",
   "Shortening a public-facing document for a general audience",
   "Generating alternative phrasings of a sentence",
   "Drafting a first version of a routine internal update"
 ],
 "ans": 0,
 "exp": "Dismissal decisions are people-affecting, high-stakes and governed by process and law. The syllabus places these firmly in the category where human expertise must lead (5.4) and where oversight is essential (8.3). The other options are routine assistance tasks.",
 "why": [
   "Correct. A people-affecting decision with legal consequences requires human expertise to lead.",
   "Wrong. Shortening a document for an audience is a named reshaping task in syllabus 5.1, subject to review.",
   "Wrong. Generating alternative phrasings is routine assistance with low stakes.",
   "Wrong. Drafting a routine internal update is a standard assisted-drafting task."
 ]
},
]

# ============================ DOMAIN 7 (12 questions, 10%) ============================
Q7 = [
{
 "q": "Which of the following must NOT be entered into a public or unapproved AI tool?",
 "opts": [
   "Personal data, confidential and commercially sensitive information, credentials and confidential documents",
   "Publicly available marketing content",
   "Published research papers",
   "General questions about a topic with no specific details"
 ],
 "ans": 0,
 "exp": "Syllabus 7.1 names the categories that must not be entered into public or unapproved tools: personal data, confidential and commercially sensitive information, credentials and confidential documents.",
 "why": [
   "Correct. These categories are named explicitly in the syllabus.",
   "Wrong. Publicly available marketing material is already in the public domain and contains no confidential detail.",
   "Wrong. Published papers are public documents.",
   "Wrong. A general question with no identifying or confidential detail carries no disclosure risk."
 ]
},
{
 "q": "What is the default rule the syllabus gives for handling information in AI tools?",
 "opts": [
   "When in doubt, leave it out",
   "When in doubt, ask a colleague",
   "When in doubt, remove the person's name and proceed",
   "When in doubt, use an approved tool instead"
 ],
 "ans": 0,
 "exp": "Syllabus 7.1 gives the default rule directly: 'when in doubt, leave it out.' It is a conservative default that resolves uncertainty in favour of protection.",
 "why": [
   "Correct. This is the syllabus rule and it is deliberately conservative.",
   "Wrong. Consulting a colleague may be sensible, but the syllabus default is a decision rule about the data itself.",
   "Wrong. Removing a name does not necessarily remove identifiability, and other confidential detail may remain.",
   "Wrong. Using an approved tool may address part of the concern, but the default rule is about whether the information belongs in a prompt at all."
 ]
},
{
 "q": "What should a professional understand about how a third-party AI service handles inputs?",
 "opts": [
   "The service may transmit, store or use inputs according to its terms, so organisational policy governs what may be entered",
   "Inputs are deleted immediately and are never transmitted",
   "Inputs are always confidential by default",
   "Inputs are only stored if the user explicitly opts in"
 ],
 "ans": 0,
 "exp": "Syllabus 7.2 states that third-party services may transmit, store or use inputs according to their terms, and that organisational policy governs use.",
 "why": [
   "Correct. Handling follows the provider's terms, and organisational policy governs what may be submitted.",
   "Wrong. Immediate deletion is not a safe default assumption and is not true of all services.",
   "Wrong. Confidentiality is not automatic. It depends on the terms of the specific service.",
   "Wrong. Retention behaviour varies by service and tier. Assuming opt-in storage is unsafe."
 ]
},
{
 "q": "What do the concepts of data retention and residency refer to in relation to AI services?",
 "opts": [
   "How long inputs and outputs are kept, and where they are stored or processed geographically",
   "How quickly the model responds, and how many users it supports",
   "How much the service costs, and how the cost is calculated",
   "How the model was trained, and which data was used"
 ],
 "ans": 0,
 "exp": "Syllabus 7.2 requires basic awareness of data retention and residency: how long data is kept and where it is held or processed.",
 "why": [
   "Correct. Duration of storage and geographic location are the two concepts.",
   "Wrong. These are performance and capacity characteristics, not retention and residency.",
   "Wrong. Cost is a commercial matter unrelated to these terms.",
   "Wrong. Training provenance is a separate concern, though related to transparency."
 ]
},
{
 "q": "What is shadow AI?",
 "opts": [
   "Unapproved AI use outside organisational oversight, which creates data and compliance risks the organisation cannot see",
   "AI used by employees working remotely",
   "AI that operates without a user interface",
   "AI used for security testing purposes"
 ],
 "ans": 0,
 "exp": "Syllabus 7.3 defines shadow AI as unapproved AI use outside organisational oversight and identifies the risks it creates.",
 "why": [
   "Correct. Unapproved use outside oversight is the definition.",
   "Wrong. Remote work is a location, not the defining characteristic. Approved remote AI use is not shadow AI.",
   "Wrong. Interface type is irrelevant. Approval and oversight are what matter.",
   "Wrong. Security testing is a specific authorised activity, not the definition of shadow AI."
 ]
},
{
 "q": "An employee finds that the organisation has no policy covering the AI tool they want to use. What should they do according to syllabus 7.3?",
 "opts": [
   "Treat the policy gap as a reason to escalate for approval rather than proceeding on personal judgement",
   "Proceed, because absence of a policy means the use is permitted",
   "Proceed but keep a personal record of what they entered",
   "Ask a colleague whether they think it is acceptable"
 ],
 "ans": 0,
 "exp": "Syllabus 7.3 states that a policy gap is a reason to escalate. Proceeding without approval is the shadow AI behaviour the syllabus warns against.",
 "why": [
   "Correct. Escalation is the syllabus position on a policy gap.",
   "Wrong. This is the reasoning that produces shadow AI.",
   "Wrong. A personal record does not provide authorisation or oversight.",
   "Wrong. A colleague's opinion does not substitute for organisational approval."
 ]
},
{
 "q": "Which of the following best describes AI-enabled threats named in syllabus 7.4?",
 "opts": [
   "Deepfakes, impersonation and AI-assisted phishing and social engineering that can be highly convincing",
   "Only attacks carried out by AI systems acting alone",
   "Attacks that exclusively target AI systems",
   "Threats that are easily recognised because they contain errors"
 ],
 "ans": 0,
 "exp": "Syllabus 7.4 names deepfakes, impersonation and AI-assisted phishing and social engineering, tested at awareness level.",
 "why": [
   "Correct. These are the named threat categories.",
   "Wrong. The threats are AI-enabled, meaning humans use AI to make attacks more effective.",
   "Wrong. Targets are people and organisations, not only AI systems.",
   "Wrong. This is precisely the danger. AI-assisted attacks can be fluent and convincing rather than error-ridden."
 ]
},
{
 "q": "You receive an urgent message from an executive, apparently in their voice, asking for an immediate payment. What is the correct response?",
 "opts": [
   "Verify the request through a separate, trusted channel before acting",
   "Comply, because the request came from a senior person",
   "Reply to the message asking for confirmation",
   "Forward the message to a colleague for a second opinion"
 ],
 "ans": 0,
 "exp": "Syllabus 7.4 requires verification of unexpected or urgent requests through a separate, trusted channel. Replying through the same channel does not verify identity, since the same attacker controls it.",
 "why": [
   "Correct. A separate trusted channel is the syllabus requirement, and it defeats impersonation of the original channel.",
   "Wrong. Seniority is exactly what makes the request attractive to an attacker.",
   "Wrong. Replying within the same channel does not verify identity. The attacker receives the reply.",
   "Wrong. A second opinion through the same channel does not establish authenticity."
 ]
},
{
 "q": "What is prompt injection?",
 "opts": [
   "Malicious instructions hidden in content the AI processes, which the model may follow as if they came from the user",
   "An error in a prompt that causes the model to produce a wrong answer",
   "A technique for inserting structured data into a prompt",
   "An attempt to overload the model's context window"
 ],
 "ans": 0,
 "exp": "Syllabus 7.5, tested at awareness level, defines prompt injection as malicious instructions hidden in content the AI processes.",
 "why": [
   "Correct. Hidden malicious instructions in processed content is the definition.",
   "Wrong. A mistake in a prompt is a user error, not an injection.",
   "Wrong. Structured data insertion is a legitimate prompting technique.",
   "Wrong. Overloading the context window is a different failure mode, addressed in Domain 2 and 6."
 ]
},
{
 "q": "An AI assistant is asked to summarise a document supplied by an external party. Why is caution warranted?",
 "opts": [
   "The document may contain hidden instructions aimed at the AI, so untrusted content should be handled with caution and AI actions kept under oversight",
   "Because external documents are always longer than expected",
   "Because summarising requires approval from the document's author",
   "Because summarisation is not a supported task for AI"
 ],
 "ans": 0,
 "exp": "Syllabus 7.5 requires caution with untrusted content and oversight of AI actions, because hidden instructions in processed content can redirect the model.",
 "why": [
   "Correct. Untrusted content is the injection vector, so caution and oversight are required.",
   "Wrong. Length is a context-window concern, not the reason for caution here.",
   "Wrong. Permission from an author is a separate matter, and the summary may be fully legitimate.",
   "Wrong. Summarisation is a supported task. The issue is the trustworthiness of the content."
 ]
},
{
 "q": "Which combination best reflects the handling of information when using AI at work?",
 "opts": [
   "Use approved tools, enter no confidential or personal data into unapproved ones, and follow organisational policy",
   "Use any tool that is free, since cost indicates low risk",
   "Use any tool, provided the data is deleted afterwards on the user's device",
   "Use only tools recommended by colleagues, since peer experience reduces risk"
 ],
 "ans": 0,
 "exp": "Syllabus 7.1 to 7.3 together require approved tooling, protection of information and adherence to organisational policy. The other options substitute assumptions for governance.",
 "why": [
   "Correct. Approved tools, protected information and policy compliance are the three requirements combined.",
   "Wrong. Cost to the user has no bearing on the risk of data handling.",
   "Wrong. Local deletion does not affect what has already been transmitted or stored by the service.",
   "Wrong. Peer recommendation is not approval, and it provides no oversight."
 ]
},
{
 "q": "Why does the syllabus treat a policy gap as a matter for escalation rather than individual discretion?",
 "opts": [
   "Because the organisation carries the consequences of unapproved AI use and is the body able to assess and approve the risk",
   "Because individuals are not permitted to make any decisions at work",
   "Because escalation delays use until the tool is no longer needed",
   "Because policy gaps always indicate that use is prohibited"
 ],
 "ans": 0,
 "exp": "Unapproved use creates organisational risk in data protection and compliance, and the organisation is responsible for assessing and accepting that risk. That is why the decision belongs with the organisation, not the individual.",
 "why": [
   "Correct. Risk acceptance belongs to the organisation, which bears the consequences.",
   "Wrong. Overstated. Individuals make many decisions, but risk acceptance for unapproved tooling is not one of them.",
   "Wrong. Escalation is intended to reach a decision, not to stall indefinitely.",
   "Wrong. A gap is not a prohibition. It is an unanswered question that should be answered before use."
 ]
},
]

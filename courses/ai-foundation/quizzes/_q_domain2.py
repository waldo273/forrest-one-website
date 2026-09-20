#!/usr/bin/env python3
"""Domain 2 — How AI Works (Without the Maths). 17 questions, 14% weighting."""

Q2 = [
{
 "q": "Which statement best describes what an AI model is at a conceptual level?",
 "opts": [
   "A set of learned values, known as parameters, produced by training on data",
   "A database of stored answers that the model looks up",
   "A set of instructions written by a programmer that the model follows",
   "A copy of the data it was trained on, held in compressed form"
 ],
 "ans": 0,
 "exp": "Syllabus 2.1 describes a model as a set of learned values (parameters), not a database of stored answers. This distinction explains why a model can be fluent yet wrong, and why it cannot cite a stored record.",
 "why": [
   "Correct. Learned parameters, not stored answers, is the syllabus description.",
   "Wrong. A database retrieves stored records. A model derives outputs from learned values.",
   "Wrong. Programmed instructions describe rule-based software, which is a different approach.",
   "Wrong. The model does not retain a compressed copy of its training data. It holds learned values derived from it."
 ]
},
{
 "q": "What is the difference between training and inference?",
 "opts": [
   "Training is the process of learning the model from data; inference is using the trained model to produce an output",
   "Training happens on the user's device; inference happens in the cloud",
   "Training produces the interface; inference produces the parameters",
   "Training and inference are two names for the same process"
 ],
 "ans": 0,
 "exp": "Syllabus 2.1 requires the distinction between training (learning the model) and inference (using it to produce an output). Parameters are adjusted during training and are effectively fixed during inference.",
 "why": [
   "Correct. Learning versus using is the distinction the syllabus requires.",
   "Wrong. Location is not the distinction. Inference commonly runs in the cloud as well.",
   "Wrong. This inverts the two. Parameters are produced by training, not inference.",
   "Wrong. They are distinct stages with different purposes and different computational behaviour."
 ]
},
{
 "q": "At Foundation level, what are parameters?",
 "opts": [
   "The adjustable values that a model learns during training",
   "The settings a user chooses in an application menu",
   "The maximum length of a prompt the model accepts",
   "The list of tasks the model is permitted to perform"
 ],
 "ans": 0,
 "exp": "Syllabus 2.1 defines parameters at Foundation level as the adjustable values learned during training.",
 "why": [
   "Correct. Learned, adjustable values is the Foundation-level definition.",
   "Wrong. User-facing settings are application controls, not model parameters.",
   "Wrong. Prompt length relates to the context window, which is a different concept.",
   "Wrong. Permissions are a policy matter, not a property of the model's parameters."
 ]
},
{
 "q": "What role do datasets play in producing a model?",
 "opts": [
   "They supply the material from which the model learns its patterns during training",
   "They store the model's answers for later retrieval",
   "They set the price of using the model",
   "They determine the model's maximum output length"
 ],
 "ans": 0,
 "exp": "Syllabus 2.1 identifies the role of datasets as the material the model learns from. This is why the qualities and limitations of training data carry through into model behaviour, including bias (8.1).",
 "why": [
   "Correct. Datasets are the material from which patterns are learned.",
   "Wrong. This describes a database, which the syllabus explicitly distinguishes from a model.",
   "Wrong. Pricing is commercial and unrelated to training data.",
   "Wrong. Output length is a configuration limit, not a property of the dataset."
 ]
},
{
 "q": "How does a language model generate text?",
 "opts": [
   "By predicting likely next tokens based on the prompt and the text produced so far",
   "By retrieving the most relevant passage from a stored library of documents",
   "By copying sentences it has seen verbatim into a new arrangement",
   "By applying grammatical rules written by its developers"
 ],
 "ans": 0,
 "exp": "Syllabus 2.2 describes next-token prediction: producing likely continuations from the prompt and the text so far.",
 "why": [
   "Correct. Next-token prediction from the prompt and prior output is the syllabus explanation.",
   "Wrong. Retrieval from a document library describes RAG, not the base generation mechanism.",
   "Wrong. Verbatim copying is not how generation works and would not explain novel phrasing.",
   "Wrong. Written grammatical rules describe rule-based systems, not learned language models."
 ]
},
{
 "q": "Why does fluent AI output not guarantee accurate output?",
 "opts": [
   "Because the model optimises for plausible continuations, and there is no built-in fact-checker",
   "Because the model deliberately mixes true and false statements",
   "Because fluency and accuracy are unrelated in principle but always coincide in practice",
   "Because the model has no training data to draw on"
 ],
 "ans": 0,
 "exp": "Syllabus 2.2 states that output is generated, not retrieved, and that fluency does not guarantee accuracy, because the mechanism has no built-in fact-checker.",
 "why": [
   "Correct. Plausibility is optimised; accuracy is not checked. The absence of a fact-checker is the syllabus point.",
   "Wrong. The model does not intend to deceive. It has no intent and no knowledge of truth in the relevant sense.",
   "Wrong. The claim that they always coincide is false and contradicts the syllabus.",
   "Wrong. The model has extensive training data. The issue is that it does not verify against it at generation time."
 ]
},
{
 "q": "Which statement best characterises the mechanism behind language models?",
 "opts": [
   "It is more sophisticated than simple autocomplete, but it has no built-in fact-checker",
   "It is exactly simple autocomplete and nothing more",
   "It is a search engine that returns the most popular answer",
   "It is a reasoning engine that verifies each claim before producing it"
 ],
 "ans": 0,
 "exp": "Syllabus 2.2 makes this precise point: the mechanism is more sophisticated than simple autocomplete, yet it has no built-in fact-checker. Over-simplifying or over-claiming both mislead.",
 "why": [
   "Correct. Sophisticated continuation without verification is the syllabus formulation.",
   "Wrong. Understates it. Characterising it as simple autocomplete hides the scale and capability of the mechanism.",
   "Wrong. Popularity of an answer is not the basis for generation.",
   "Wrong. Overstates it. Verification is precisely what the mechanism lacks."
 ]
},
{
 "q": "What is a token?",
 "opts": [
   "The basic unit of text that a model reads and writes",
   "A single word, always separated by spaces",
   "A security credential used to access an AI service",
   "A measure of the model's accuracy"
 ],
 "ans": 0,
 "exp": "Syllabus 2.3 defines tokens as the basic unit of text a model reads and writes. Tokens are not identical to words, which matters for estimating how much text fits in the context window.",
 "why": [
   "Correct. The basic unit of text is the syllabus definition.",
   "Wrong. Tokens often correspond to parts of words and do not map cleanly onto whitespace-separated words.",
   "Wrong. This is an unrelated meaning of the word 'token' in the security domain.",
   "Wrong. Tokens are units of text, not measures of accuracy."
 ]
},
{
 "q": "What is the context window best described as?",
 "opts": [
   "The model's short-term working memory, holding the text it can currently take into account",
   "A settings panel where users configure the model",
   "The maximum length of a single sentence the model can generate",
   "The total size of the model's training data"
 ],
 "ans": 0,
 "exp": "Syllabus 2.3 describes the context window as short-term working memory.",
 "why": [
   "Correct. Short-term working memory is the syllabus description.",
   "Wrong. The context window is a technical limit, not a user interface element.",
   "Wrong. It governs the total text in play, not one sentence.",
   "Wrong. Training data is a separate and much larger body of material."
 ]
},
{
 "q": "What happens when a conversation exceeds the context window?",
 "opts": [
   "Earlier detail may effectively be forgotten, and large pastes can crowd out the instructions that matter",
   "The model automatically retrains on the new conversation",
   "The conversation is permanently deleted without warning",
   "The model becomes more accurate because it has more information"
 ],
 "ans": 0,
 "exp": "Syllabus 2.3 identifies the effects of exceeding the window: earlier detail is forgotten and large pastes crowd out instructions.",
 "why": [
   "Correct. Loss of earlier detail and displacement of instructions are the named effects.",
   "Wrong. The model does not learn or retrain during inference.",
   "Wrong. The practical effect is that content falls out of scope, not necessarily permanent deletion.",
   "Wrong. More input beyond the limit does not improve accuracy. It displaces what was there."
 ]
},
{
 "q": "Which of the following is a practical technique for working within the context window?",
 "opts": [
   "Keeping prompts concise, placing key instructions first or last, and chunking large material",
   "Repeating the same instructions many times throughout the prompt",
   "Pasting the entire document collection to be certain nothing is missed",
   "Using the longest possible prompts to give the model more to work with"
 ],
 "ans": 0,
 "exp": "Syllabus 2.3 lists practical techniques: concise prompts, key instructions placed first or last, and chunking.",
 "why": [
   "Correct. These three techniques are named in the syllabus.",
   "Wrong. Repetition consumes the window and displaces other content without improving adherence.",
   "Wrong. Pasting everything risks exceeding the window and losing the very detail that mattered.",
   "Wrong. Longer prompts are the problem, not the solution, once the window is a constraint."
 ]
},
{
 "q": "Why does placing key instructions at the beginning or end of a prompt help?",
 "opts": [
   "Because attention is strongest at the start and end of the input, so the middle is more easily overlooked",
   "Because the model only reads the first and last lines",
   "Because instructions outside those positions are automatically rejected",
   "Because the model sorts prompts by length before processing them"
 ],
 "ans": 0,
 "exp": "Syllabus 2.3 identifies this as a practical technique for working within the window, and Domain 6 describes the underlying 'lost in the middle' effect where the model over-indexes the start and end of its input.",
 "why": [
   "Correct. The start and end of the input receive the strongest attention, so important instructions are safest there.",
   "Wrong. The model does read the whole input. The issue is the strength of attention, not outright omission.",
   "Wrong. Instructions in the middle are not rejected. They are simply more likely to be under-weighted.",
   "Wrong. Prompt ordering is not affected by any sorting behaviour."
 ]
},
{
 "q": "What is a knowledge cut-off?",
 "opts": [
   "The point after which a base model has no knowledge, because its training data ended at that date",
   "The maximum number of questions a user may ask in one session",
   "The point at which a model is retired from service",
   "The limit on how long output may be"
 ],
 "ans": 0,
 "exp": "Syllabus 2.4 defines the knowledge cut-off as the point after which a base model has no knowledge, because its training data ended at that date.",
 "why": [
   "Correct. The end date of the training data is the knowledge cut-off.",
   "Wrong. Session question limits are a service policy, not a knowledge cut-off.",
   "Wrong. Retirement is a lifecycle decision, unrelated to the training data date.",
   "Wrong. Output length relates to generation limits, not to knowledge."
 ]
},
{
 "q": "Why are time-sensitive questions unreliable when put to a base model alone?",
 "opts": [
   "Because the model has no knowledge of events after its training date and may answer confidently anyway",
   "Because the model refuses to answer questions about current events",
   "Because time-sensitive questions are always too long for the context window",
   "Because the model deliberately gives out-of-date answers"
 ],
 "ans": 0,
 "exp": "Syllabus 2.4 states that a base model has no knowledge of events after its training date, and the risk compounds because it may still answer fluently rather than indicating uncertainty.",
 "why": [
   "Correct. Absent knowledge plus fluent answering is the risk the syllabus identifies.",
   "Wrong. Refusal is not the problem. The model often answers anyway.",
   "Wrong. Length is unrelated to time sensitivity.",
   "Wrong. The model has no intent. It simply lacks post-cut-off knowledge."
 ]
},
{
 "q": "An application provides live web search alongside a model. How should this be understood?",
 "opts": [
   "The application adds current information, but the base model itself remains frozen at its training date",
   "The base model has been updated and now has current knowledge",
   "Live search removes any need to verify information",
   "The model retrains itself each time search is used"
 ],
 "ans": 0,
 "exp": "Syllabus 2.4 states that some applications add live search, but the base model itself remains frozen. This is an important distinction between the model and the application built around it (also syllabus 2.5 and 3.5).",
 "why": [
   "Correct. Search extends the application, not the model's own knowledge.",
   "Wrong. The model's parameters are unchanged. Current information comes from retrieval, not from the model.",
   "Wrong. Retrieved content still requires verification, and RAG reduces rather than removes error (3.3).",
   "Wrong. The model does not learn during inference."
 ]
},
{
 "q": "Why can the same prompt produce different answers on separate occasions?",
 "opts": [
   "Because the model samples from a range of plausible continuations, influenced by settings such as temperature",
   "Because the model is malfunctioning",
   "Because the model's training data changes between requests",
   "Because the interface rewrites the prompt each time"
 ],
 "ans": 0,
 "exp": "Syllabus 2.5 explains that identical prompts can produce different answers because of sampling and settings such as temperature. This variability is why verification and review are essential.",
 "why": [
   "Correct. Sampling behaviour, including the temperature setting, is the syllabus explanation.",
   "Wrong. Variability is a property of the design, not a fault.",
   "Wrong. Training data is fixed after training. It does not change between requests.",
   "Wrong. Inconsistent output stems from the generation mechanism, not from prompt rewriting."
 ]
},
{
 "q": "Which distinction does syllabus 2.5 require candidates to make?",
 "opts": [
   "The distinction between a model and the application built around it",
   "The distinction between hardware and software",
   "The distinction between open-source and proprietary licences",
   "The distinction between text and image outputs"
 ],
 "ans": 0,
 "exp": "Syllabus 2.5 requires the distinction between a model and the application built around it. Many features users attribute to the model, such as live search or saved context, are properties of the application layer.",
 "why": [
   "Correct. Model versus application is the required distinction.",
   "Wrong. This is a general computing distinction, not the one the syllabus specifies here.",
   "Wrong. Licensing is a commercial and legal matter, addressed elsewhere if at all.",
   "Wrong. Output modality is a separate concern, addressed under multimodal AI in 3.2."
 ]
},
{
 "q": "What are embeddings, at the awareness level required by the syllabus?",
 "opts": [
   "Numerical representations of meaning, in which related items sit close together",
   "Compressed copies of the original documents",
   "Encrypted versions of user prompts",
   "Lists of keywords extracted from a text"
 ],
 "ans": 0,
 "exp": "Syllabus 2.5 tests embeddings at awareness level as the representation of meaning as numbers, so that related items sit close together. This is what makes semantic search and retrieval possible.",
 "why": [
   "Correct. Meaning represented numerically, with related items close together, is the awareness-level description.",
   "Wrong. Embeddings represent meaning rather than storing the source document.",
   "Wrong. Encryption protects data in transit or at rest. It is unrelated to embeddings.",
   "Wrong. Keyword lists are a different and older technique, not embeddings."
 ]
},
]

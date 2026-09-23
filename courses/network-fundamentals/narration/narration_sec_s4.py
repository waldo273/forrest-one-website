# narration_sec_s4.py — Security+ SY0-701 (revised), Session 4
# "Fundamental Security Concepts"
# One-video-per-lesson format. Each frame: (template, payload, narration).
# Narration is read ALOUD IN FULL by ElevenLabs (Billy's voice) — short
# sentences that stand alone without the visual. Abbreviations are written
# so the engine reads them the way they are spoken in the classroom.
# USER RULES: no "good morning" (use "good day"); no courseware timing
# references — only the video's own length may be mentioned.

DECK = 'Fundamental Security Concepts'
SESSION = 'Session 4 · Security+ SY0-701 (revised)'

# Course palette (matches site + decks)
NAVY      = (0, 43, 92)
NAVY_MID  = (13, 67, 128)
NAVY_SOFT = (58, 90, 128)
STEEL     = (106, 138, 170)
LINE      = (208, 220, 232)
PANEL     = (247, 250, 253)
PANEL2    = (238, 243, 249)
WHITE     = (255, 255, 255)
GREEN, GREEN_BG = (46, 125, 50),  (232, 245, 233)
RED,   RED_BG   = (198, 40, 40),  (251, 233, 231)
AMBER, AMBER_BG = (184, 134, 11), (255, 248, 225)

FRAMES = [('chapter',
  {'num': 1,
   'of': 5,
   'title': 'The CIA Triad & Non-Repudiation',
   'blurb': 'The three pillars of security and the fourth property'},
  'Good day, and welcome to Session Four of the combined Network Fundamentals and CompTIA '
    'Security+ course. This session lays the foundation that every later session builds on: the '
    'principles of information security. Confidentiality, integrity and availability, or C-I-A. '
    'The authentication, authorisation and accounting framework, or triple A. Security controls. '
    'Frameworks and roles. Get these right, and the rest of the course fits into place. We begin '
    'with the three pillars that anchor almost every security decision you will ever make.'),
 ('statement',
  {'kick': 'The Journey',
   'title': 'The Shape of the Course',
   'body': 'Network foundation first, then the security core, then architecture, then operations '
           'and governance. Every later session assumes you can name the principles that protect '
           'data.'},
  'Here is the shape of the course. Sessions one to three are the network foundation — models, '
  'addressing, switching, services. Sessions four to seven are the security core — fundamental '
  'concepts, threats, cryptography, identity. Sessions eight and nine are security architecture — '
  'network, endpoint, application, cloud. Sessions ten to twelve are operations and governance — '
  'vulnerability management, incident response, and compliance. This session is the first of the '
  'security core, and it sets the vocabulary the whole course depends on.'),
 ('bullets',
  {'kick': 'The Journey',
   'title': 'Session Objectives',
   'items': ['Define the CIA triad — confidentiality, integrity, availability',
             'Explain non-repudiation and why it matters',
             'Describe the AAA framework — identification, authentication, authorisation, '
             'accounting',
             'Classify security controls by category and functional type',
             'Apply the NIST Cybersecurity Framework',
             'Name the key roles and their responsibilities'],
   'note': 'Six objectives — the quiz at the end tests every one.'},
  'By the end of this session you will be able to do nine things. One: define confidentiality, '
    'integrity and availability, or C-I-A, and give a real-world example control for each. Two: '
    'explain non-repudiation, and how digital signatures and logs provide it. Three: describe the '
    'authentication, authorisation and accounting framework, or triple A — identification, '
    'authentication, authorisation and accounting. Four: classify security controls by category — '
    'managerial, operational, technical and physical. Five: classify security controls by '
    'functional type — preventive, detective, corrective, directive, deterrent and compensating. '
    'Six: describe the National Institute of Standards and Technology Cybersecurity Framework, or '
    'N-I-S-T C-S-F, and its five functions. Seven: explain what a gap analysis measures, and why '
    'it is valuable. Eight: name the key security roles and their responsibilities. And nine: '
    'explain defence in depth, least privilege, separation of duties, and zero trust. Nine '
    'objectives, and the quiz at the end tests every one of them.'),
 ('bullets',
  {'kick': 'Security Concepts',
   'title': 'The CIA Triad',
   'items': ['Confidentiality — protects information from unauthorised access and disclosure',
             'Integrity — data is stored and transferred as intended; any modification is '
             'authorised',
             'Availability — information is accessible to those authorised to view or modify it',
             'The balance — controls protect all three, usually at some cost to convenience',
             'The anchor — most security decisions trace back to one of the three pillars'],
   'note': 'CIA is the anchor of the whole course.'},
  'Everything in security starts here. Confidentiality: information should only be read by '
  'authorised persons. Integrity: data is stored and transferred as intended, and any modification '
  'is authorised. Availability: information is accessible to those authorised to view or modify '
  'it. Three pillars, and most security work is protecting them — usually at some cost to '
  'convenience, which is why security is a balance, not an absolute. Most security decisions trace '
  'back to one of the three pillars.'),
 ('table',
  {'kick': 'Security Concepts',
   'title': 'CIA in Practice',
   'headers': ['Pillar', 'Threat to it', 'Example control'],
   'rows': [['Confidentiality', 'Data theft, interception', 'Encryption, access controls'],
            ['Integrity', 'Unauthorised changes', 'Hashing, digital signatures'],
            ['Availability', 'Outages, DoS attacks', 'Redundancy, backups, failover']]},
  'Make the triad concrete. Confidentiality is threatened by data theft and interception — the '
  'control is encryption and access controls. Integrity is threatened by unauthorised changes — '
  'the control is hashing and digital signatures. Availability is threatened by outages and '
  'denial-of-service — the control is redundancy, backups and failover. When you meet a control in '
  'this course, ask which pillar it protects.'),
 ('bullets',
  {'kick': 'Security Concepts',
   'title': 'Non-Repudiation',
   'items': ['Definition — persons cannot deny creating or modifying data',
             'Proof of origin — the sender cannot deny sending',
             'Proof of action — the actor cannot deny the action they performed',
             "Digital signatures — hash encrypted with the sender's private key",
             'Audit logs — chronological record of who did what, with timestamps',
             'The exam line — non-repudiation is proof, not merely logging'],
   'note': 'Signatures and logs make denial fail.'},
  'The fourth property the exam expects is non-repudiation. It means persons cannot deny creating '
  'or modifying data. It provides proof of origin — the sender cannot deny sending — and proof of '
  'action — the actor cannot deny what they did. The mechanisms matter. A digital signature hashes '
  "the message, encrypts that hash with the sender's private key, and the recipient verifies it "
  "with the public key, so only the sender's key could have produced it. Audit logs record who did "
  'what and when, with timestamps. If a system logs who did what, and a signature proves who sent '
  'what, denial fails. Non-repudiation is not merely logging; it is proof.'),
 ('bullets',
  {'kick': 'Security Concepts',
   'title': 'Access Control: The AAA Framework',
   'items': ['Identification — the user claims an identity; an account is created',
             'Authentication — the user proves the claim with a credential',
             'Authorisation — permissions are checked for each action',
             'Accounting — usage is logged and audited; the user cannot prevent this',
             'Auth factors — something you know, have, or are — combine for MFA'],
   'note': 'Identification, authentication, authorisation, accounting — AAA.'},
  'How does access actually work? Four steps. Identification: the user claims an identity — an '
    'account is created to represent them. Authentication: the user proves the claim with a '
    'credential. Authorisation: for each action, a permission list is checked to allow or deny. And '
    'accounting: usage is logged and audited — the user cannot prevent this auditing. Together '
    'these four steps are the triple A framework. Behind authentication lie three factors: '
    'something you know, a password or personal identification number, or pin; something you have, '
    'a token or smart card; and something you are, a biometric. Multifactor authentication, or '
    'M-F-A, combines two or more of these, so a compromised password alone is not enough.'),
 ('callout',
  {'kind': 'info',
   'label': 'Discussion',
   'title': 'Which pillar fails first in a typical data breach?',
   'body': 'Stolen credentials hit confidentiality first, then integrity, then availability. Real '
           'incidents chain across pillars.'},
  'Here is a question worth working through. Which pillar of the confidentiality, integrity and '
  'availability triad fails first in a typical data breach? Stolen credentials hit confidentiality '
  'first — data is read. Then integrity — data is altered. Then availability — systems are locked '
  'or destroyed. Real incidents chain across pillars; that is why the triad is a triad, not three '
  'separate problems.'),
 ('chapter',
  {'num': 2,
   'of': 5,
   'title': 'Security Controls',
   'blurb': 'Categories and the six functional types'},
  'Now we move from the principles to the controls that protect them. Chapter two is security '
  'controls. Every control sits on two axes: a category that says who or what it is, and a '
  'functional type that says when and how it acts. Learn both axes, and you can classify any '
  'control the exam throws at you.'),
 ('table',
  {'kick': 'Security Controls',
   'title': 'Control Categories',
   'headers': ['Category', 'What it is', 'Example'],
   'rows': [['Managerial',
             'Policies and oversight of risk',
             'Risk assessments, training programmes'],
            ['Operational', 'Depends on a person to implement', 'Guard patrols, incident response'],
            ['Technical',
             'Implemented in systems and software',
             'Firewalls, ACLs, encryption, IDS'],
            ['Physical',
             'Mediates access to premises and hardware',
             'Locks, fences, cameras, mantraps']]},
  'First, the category. Managerial: oversight of systems and risk — policies and risk assessments. '
  'Operational: depends on a person to implement — training and guard patrols. Technical: '
  'implemented in systems and software — firewalls, antivirus and encryption. Physical: mediates '
  'access to premises and hardware — locks, fences and cameras. Four categories.'),
 ('bullets',
  {'kick': 'Security Controls',
   'title': 'Functional Types: The First Three',
   'items': ['Preventive — blocks an incident before it occurs — e.g. firewalls, access controls',
             'Detective — identifies intrusions during or after — e.g. IDS, log monitoring',
             'Corrective — remediates damage after — e.g. patching, restore from backup'],
   'note': 'Preventive before, detective during, corrective after.'},
  'Second axis: the functional type — what the control does. Preventive: physically or logically '
    'restricts unauthorised access; it operates before an attack — a firewall blocking ports. '
    'Detective: identifies attempted or successful intrusions; it operates during an attack — an '
    'intrusion detection system, or I-D-S. Corrective: responds to and fixes an incident; it '
    'operates after an attack — restoring from backup after ransomware.'),
 ('bullets',
  {'kick': 'Security Controls',
   'title': 'Functional Types: The Next Three',
   'items': ['Directive — guides user behaviour — e.g. policies, acceptable use rules',
             'Deterrent — discourages intrusions psychologically — e.g. warning banners, visible '
             'cameras',
             'Compensating — substitutes when a primary control is not feasible',
             'The exam trick — controls sit on two axes — category and functional type'],
   'note': 'Six types; the exam loves asking you to tell them apart.'},
  'The other three types. Directive: guides user behaviour — a security policy or acceptable use '
  'rule that says what staff must do. Deterrent: psychologically discourages intrusions — warning '
  'banners, visible cameras, the presence of guards. And compensating: substitutes for a principal '
  'control that cannot be implemented — if a legacy system cannot support encryption, '
  'network-level encryption or enhanced logging compensates. Six types, and the exam loves asking '
  'you to tell them apart. Remember the trick: every control sits on two axes — a category and a '
  'functional type.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Activity',
   'title': 'Classify the controls',
   'body': 'A firewall blocking ports — technical and preventive. A camera over the server room '
           'door — physical and deterrent. An IDS watching traffic — technical and detective. '
           'Backup-and-restore after ransomware — operational and corrective.'},
  'Let us classify a few controls together. A firewall blocking unauthorised ports — technical and '
    'preventive. A security camera over the server room door — physical and deterrent. An I-D-S '
    'watching traffic — technical and detective. A backup-and-restore plan after ransomware — '
    'operational and corrective. Category first, then type — two axes every time.'),
 ('chapter',
  {'num': 3,
   'of': 5,
   'title': 'Frameworks & Gap Analysis',
   'blurb': 'The NIST CSF and measuring where you stand'},
  'Chapter three is frameworks and gap analysis. Frameworks give security a common map — a shared '
    'language for the whole programme. The N-I-S-T Cybersecurity Framework is the one the exam '
    'expects, and gap analysis is how you measure where you stand against it.'),
 ('bullets',
  {'kick': 'Frameworks',
   'title': 'The NIST Cybersecurity Framework',
   'items': ['Identify — know your assets, systems and risks',
             'Protect — implement safeguards for critical services',
             'Detect — find security events quickly',
             'Respond — contain and mitigate incidents',
             'Recover — restore capabilities and learn',
             'Purpose — a common language and map for the whole security programme'],
   'note': 'Identify, protect, detect, respond, recover — the lifecycle of security.'},
  'The N-I-S-T Cybersecurity Framework has five functions. Identify: know your assets, systems '
    'and risks. Protect: implement safeguards for critical services. Detect: find security events '
    'quickly. Respond: contain and mitigate incidents. And Recover: restore capabilities and learn. '
    'Identify, protect, detect, respond, recover — the lifecycle of security. The framework gives '
    'the whole programme a common language and a map.'),
 ('bullets',
  {'kick': 'Frameworks',
   'title': 'Gap Analysis',
   'items': ['Definition — comparing current security posture against a target framework',
             'What it finds — missing controls, weak areas, unmeasured functions',
             'Output — a scored view — e.g. 50% maturity in a function',
             'The value — prioritised, evidence-based improvement',
             'The distinction — a scan finds technical holes; gap analysis measures the programme'],
   'note': 'The scan finds cracks in the wall; the gap analysis checks the wall is where it should '
           'be.'},
  'How do you know where you stand? Gap analysis compares your current security posture against a '
  'target framework. It finds missing controls, weak areas and unmeasured functions. The output is '
  'a scored view — say, fifty percent maturity in a function. The value is prioritised, '
  'evidence-based improvement: you know what to fix first, and you can measure progress. And here '
  'is the distinction the exam tests: a vulnerability scan finds technical holes in systems, while '
  'a gap analysis measures the whole programme against a framework — policies, processes, '
  'coverage, maturity. The scan finds cracks in the wall; the gap analysis checks the wall is '
  'where it should be. You need both.'),
 ('callout',
  {'kind': 'info',
   'label': 'Discussion',
   'title': 'What does a gap analysis tell you that a scan does not?',
   'body': 'A scan finds technical holes; a gap analysis measures the whole programme against a '
           'framework — policies, processes, coverage, maturity.'},
  'Here is the discussion question. What does a gap analysis tell you that a vulnerability scan '
  'does not? A scan finds technical holes in systems. A gap analysis measures the whole programme '
  'against a framework — policies, processes, coverage, maturity. The scan finds cracks in the '
  'wall; the gap analysis checks the wall is where it should be. You need both.'),
 ('chapter',
  {'num': 4,
   'of': 5,
   'title': 'Roles, Responsibilities & Principles',
   'blurb': 'Who does what, and the principles that shape secure design'},
  'Chapter four is the people and the principles. Security is a team sport, and knowing who is '
  'accountable for what is a classic exam distinction. Then we meet the four principles that shape '
  'secure design — defence in depth, least privilege, separation of duties, and zero trust.'),
 ('table',
  {'kick': 'Roles & Responsibilities',
   'title': 'Who Does What',
   'headers': ['Role', 'Responsibility'],
   'rows': [['CISO / CSO', 'Executive ownership of security strategy and risk'],
            ['ISSO', 'Day-to-day management of security systems and compliance'],
            ['Data owner', "Accountable for a data set's classification and protection"],
            ['Data custodian', 'Implements the controls that protect the data'],
            ['Security analyst', 'Monitoring, triage and incident response'],
            ['Auditor', 'Independent review of controls and compliance']]},
  'Security is a team sport. The Chief Information Security Officer, or C-I-S-O, owns security '
    'strategy and risk at executive level. Some organisations call this role the Chief Security '
    'Officer, or C-S-O. The Information Systems Security Officer, or I-S-S-O, manages day-to-day '
    'security systems and compliance. The data owner is accountable for a data set\'s '
    'classification and protection. The data custodian implements the controls that protect it. '
    'The security analyst monitors, triages and responds. The auditor reviews controls '
    'independently. Notice the pattern: owners are accountable; custodians implement; auditors '
    'verify.'),
 ('bullets',
  {'kick': 'Roles & Responsibilities',
   'title': 'Core Security Principles',
   'items': ['Defence in depth — layered controls, no single point of failure',
             'Least privilege — users get only the access they need; review regularly',
             'Separation of duties — no one person controls a critical process alone',
             'Zero trust — never trust implicitly; verify every request',
             'The thread — each principle limits the blast radius of one failure'],
   'note': 'These four reappear in almost every session of this course.'},
  'Four principles shape secure design. Defence in depth: layered controls, so no single point of '
  'failure — one layer failing does not mean the asset falls. Least privilege: users get only the '
  'access they need, nothing more, and you review it regularly. Separation of duties: no one '
  'person controls a critical process alone. And zero trust: never trust implicitly — verify every '
  'request. Each principle limits the blast radius of a single failure. These four will reappear '
  'in almost every session of this course.'),
 ('bullets',
  {'kick': 'Roles & Responsibilities',
   'title': 'Zero Trust in One Slide',
   'items': ['The old model — trust inside the perimeter, distrust outside',
             'The problem — perimeters leak — insiders, breaches, cloud',
             'The model — verify every request, whatever its origin',
             'Microsegmentation — split the network to limit lateral movement',
             'Continuous verification — re-check identity and device, not once but always',
             'The exam line — zero trust is a design principle, not a product'],
   'note': 'Never trust, always verify.'},
  'Zero trust is the modern security model. The old model trusted everything inside the perimeter '
  'and distrusted everything outside. The problem: perimeters leak — insiders, breaches, cloud. '
  'The zero-trust model verifies every request, whatever its origin — a laptop on the corporate '
  'network gets no more trust than one in a coffee shop. Two supporting ideas: microsegmentation '
  'splits the network so a breach cannot move sideways, and continuous verification re-checks '
  'identity and device rather than trusting once at login. And the exam line: zero trust is a '
  'design principle, not a product you buy.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Activity',
   'title': 'Defence in depth',
   'body': 'Name the layers protecting a server: firewall, OS hardening, AV/EDR, patch management, '
           'backups. Layers fail independently — that is the point.'},
  'Let us build defence in depth around a server. Name the layers: a firewall, operating system '
    'hardening, antivirus, or A-V, and endpoint detection and response, or E-D-R, patch management, '
    'and backups. Map each layer to the confidentiality, integrity and availability pillar it '
    'primarily protects. Which layer catches a zero-day exploit? Endpoint detection and behaviour '
    'monitoring — signatures miss unknown threats. Which layer survives one? Backups — recovery. '
    'Layers fail independently; that is the point of defence in depth.'),
 ('chapter',
  {'num': 5, 'of': 5, 'title': 'Consolidation', 'blurb': 'Key takeaways and what to revise'},
  'Chapter five is consolidation. We bring the session together into the key takeaways you should '
  'carry forward, and the revision checklist that turns this session into long-term recall.'),
 ('recap',
  {'title': 'Key Takeaways',
   'items': ['CIA is the foundation — confidentiality, integrity, availability, plus '
             'non-repudiation',
             'AAA governs access — identification, authentication, authorisation, accounting',
             'Controls have two axes — category and functional type',
             'The CSF is the map — identify, protect, detect, respond, recover — and gap analysis '
             'shows where you are',
             'Principles protect the design — defence in depth, least privilege, separation of '
             'duties, zero trust']},
  'Five takeaways. One: C-I-A is the foundation — confidentiality, integrity and availability, '
    'plus non-repudiation. Two: triple A governs access — identification, authentication, '
    'authorisation and accounting. Three: controls have two axes — category and functional type. '
    'Four: the C-S-F is the map — identify, protect, detect, respond, recover — and gap analysis '
    'shows where you are. Five: principles protect the design — defence in depth, least privilege, '
    'separation of duties, zero trust.'),
 ('bullets',
  {'kick': 'Consolidation',
   'title': 'Revision Checklist',
   'items': ['Retake the session quiz until you score well without guessing',
             'Map your workplace — one control for each category and type',
             'Practise the triad — classify five recent incidents by pillar',
             'Read ahead to Session 5 — threat types, threat actors and attack vectors'],
   'note': 'This video is one revision pass — the quiz is the recall test.'},
  'Before you move on, make the learning stick. Retake the session quiz until you score well '
  'without guessing. Map your workplace — one control for each category and each type. Practise '
  'the triad — classify five recent incidents by pillar. And read ahead to Session 5, where we '
  'meet the bad guys: threat types, threat actors and attack vectors. This video is one revision '
  'pass — the quiz is where you prove you can recall it.'),
 ('statement',
  {'kick': 'Next',
   'title': 'Session 5 — Threats, Attack Types & Threat Actors',
   'body': 'Compare threat actor types and motivations, explain threat vectors and attack '
           'surfaces, and understand the vulnerability-threat-risk relationship.'},
  'That closes Session Four. You can now explain the C-I-A triad and non-repudiation, the triple A '
    'framework, security controls by category and functional type, the N-I-S-T Cybersecurity '
    'Framework, and the roles that make security governance work. Retake the session quiz until you '
    'score seventy percent without guessing. These are the concepts behind every control you will '
    'meet for the rest of the course.')]

if __name__ == "__main__":
    total = sum(len(f[2].split()) for f in FRAMES)
    print("Session 4 narration: %d frames, %d words (~~%d min at 163 wpm)"
          % (len(FRAMES), total, round(total / 163)))

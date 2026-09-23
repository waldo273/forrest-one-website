# narration_sec_s5.py — Security+ SY0-701 (revised), Session 5
# "Threats, Attack Types & Threat Actors"
# One-video-per-lesson format. Each frame: (template, payload, narration).
# Narration is read ALOUD IN FULL by ElevenLabs (Billy's voice) — short
# sentences that stand alone without the visual. Abbreviations are written
# so the engine reads them the way they are spoken in the classroom.
# USER RULES: no "good morning" (use "good day"); no courseware timing
# references — only the video's own length may be mentioned.

DECK = 'Threats, Attack Types & Threat Actors'
SESSION = 'Session 5 · Security+ SY0-701 (revised)'

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
   'title': 'Know the Adversary',
   'blurb': 'Vulnerability, threat, risk and the actors who attack'},
  'Good day, and welcome to Session Five of the combined Network Fundamentals and CompTIA '
  'Security+ course. Session Four built the foundations: the confidentiality, integrity and '
  'availability triad, controls and frameworks. In this video we study the adversary. Who attacks '
  'organisations, why they do it, and the paths they take. The exam frames most of this area as '
  'scenarios, so this session gives you the vocabulary to name the actor, the vector and the '
  'motivation, and to defend accordingly. You cannot defend against a threat you cannot name.'),
 ('statement',
  {'kick': 'The Adversary',
   'title': 'Where We Are',
   'body': 'Session 4 set the CIA triad, controls and frameworks. Today: the adversary — who '
           'attacks, why, and how. A vulnerability plus a threat equals risk.'},
  'Here is where we are in the course. Session Four established the fundamentals. In this video we '
  'take the threat side of the equation. Hold on to the relationship that frames everything: a '
  'vulnerability plus a threat equals risk. A weakness on its own is not risk; a weakness someone '
  'is willing to exploit is. The outcome of this video is simple: you will classify actors and map '
  'attack surfaces, and the attributes framework we meet in a moment is the tool you will use '
  'throughout.'),
 ('bullets',
  {'kick': 'The Adversary',
   'title': 'Session Objectives',
   'items': ['Define vulnerability, threat and risk, and the relationship that joins them',
             'Compare threat actors by behaviour, source, sophistication, resources and funding',
             'Classify actor types — lone hackers, hacktivists, nation-state, organised crime, '
             'insiders',
             'Explain the attack surface — the points reachable by an attacker',
             'Map common vectors — direct, remote, lure-based, vulnerable software, supply chain'],
   'note': 'Five objectives — the quiz at the end tests every one.'},
  'By the end of this video you will be able to do seven things. First, define vulnerability, '
  'threat and risk, and explain how they combine. Second, describe the attributes of threat '
  'actors — behaviour, source, sophistication, resources and funding. Third, compare the threat '
  'actor types: lone hackers, unskilled attackers, hacker teams and hacktivists, nation-state '
  'actors and advanced persistent threats, the A-P-Ts, plus organised crime, competitors and '
  'internal actors. Fourth, explain threat actor motivations — financial, political, strategic '
  'and '
  'personal. Fifth, define the attack surface and the factors that expand it. Sixth, explain '
  'the threat vectors — direct access, remote access, wireless and cloud, lure-based, vulnerable '
  'software and supply chain. And seventh, describe the attack chain — reconnaissance, vector, '
  'exploit, act. Seven objectives, and the quiz at the end tests every one.'),
 ('bullets',
  {'kick': 'Threat Actors',
   'title': 'Vulnerability, Threat and Risk',
   'items': ['Vulnerability — a weakness in a system, process or design',
             'Threat — a person, tool or method that could exploit it',
             'Risk — the likelihood and impact of that exploitation',
             'The formula — a threat that exploits a vulnerability creates risk',
             'The lesson — a weakness alone is not risk; add an adversary and it is'],
   'note': 'Think risk as weakness plus adversary.'},
  'Three terms, one relationship. A vulnerability is a weakness in a system, a process or a '
  'design. A threat is something that could exploit that weakness — whether a person, a tool or a '
  'method. Risk is the likelihood and impact of that exploitation happening. The formula: a threat '
  'that exploits a vulnerability creates risk. When you hear the word risk in this course, think '
  'weakness plus adversary. A weakness documented in a report is not risk; the moment someone is '
  'willing to exploit it, you have risk.'),
 ('table',
  {'kick': 'Threat Actors',
   'title': 'Attributes of Threat Actors',
   'headers': ['Attribute', 'What it tells you'],
   'rows': [['Behaviour', 'Targeted or opportunistic; malicious or accidental'],
            ['Source', 'Internal with authorised access, or external'],
            ['Sophistication', 'Commodity tools up to custom zero-day attacks'],
            ['Resources & funding', 'Individual, criminal group, or nation-state backing'],
            ['Motivation & intent', 'The reason to act and the outcome sought']]},
  'How do we compare threat actors? The framework rests on five attributes. Behaviour: targeted or '
  'opportunistic, malicious or accidental. Source: internal, with authorised access, or external. '
  'Sophistication: from commodity tools up to custom zero-day attacks. Resources and funding: an '
  'individual, a criminal group, or a nation-state. And motivation with intent: the reason to act '
  'and the outcome sought. These five attributes let you classify any actor you meet in a '
  'scenario.'),
 ('bullets',
  {'kick': 'Threat Actors',
   'title': 'Motivations',
   'items': ['Financial — blackmail, extortion, fraud, ransomware, card theft',
             'Political / ideological — hacktivism, disinformation, state objectives',
             'Strategic — espionage, exfiltration, competitive advantage',
             'Personal — curiosity, challenge, revenge, grievance',
             'The predictor — motivation decides the target and the method'],
   'note': 'The financially motivated go where the money is.'},
  'Why do they attack? Financial: blackmail, extortion, fraud, ransomware, card theft. Political '
  'or ideological: hacktivism, disinformation, nation-state objectives. Strategic: espionage, '
  'exfiltration, competitive advantage. Personal: curiosity, challenge, revenge, grievance. '
  'Motivation matters because it predicts targets. The financially motivated go where the money '
  'is; the politically motivated go where the message lands.'),
 ('table',
  {'kick': 'Threat Actors',
   'title': 'Hackers and Hacktivists',
   'headers': ['Type', 'Profile', 'Typical motivation'],
   'rows': [['Lone hacker',
             'Independent; ethical white hat to malicious black hat',
             'Curiosity, challenge, gain'],
            ['Unskilled attacker',
             'Script kiddie using pre-written tools on easy targets',
             'Notoriety, low effort'],
            ['Hacker team / hacktivist',
             'Organised groups promoting a political or social cause',
             'Ideology, disruption'],
            ['Insider',
             'Employee, contractor or partner with authorised access',
             'Sabotage, gain, grievance']]},
  'The cast of characters. The lone hacker: independent, ranging from the ethical white hat to the '
  'malicious black hat, often driven by curiosity or challenge. The unskilled attacker: the script '
  'kiddie, using pre-written tools without deep understanding, and typically chasing easy targets '
  'with weak passwords or outdated software. The hacker team and the hacktivist: organised groups '
  'using cyber means to promote a political or social cause, often through defacement, data leaks '
  'or denial-of-service. And the insider: an employee, contractor or partner with authorised '
  'access, which makes them hard to detect. Remember that many insider incidents are accidents, '
  'not malice.'),
 ('bullets',
  {'kick': 'Threat Actors',
   'title': 'Nation-State Actors & APTs',
   'items': ['State-sponsored — tied to military or intelligence services',
             'High capability — substantial resources, skilled personnel, persistence',
             'APT — advanced persistent threat, long-term and strategic',
             'Objectives — espionage, IP theft, critical infrastructure disruption',
             'Deniability — complex obfuscation and false-flag operations'],
   'note': 'The APT is the most tested actor type.'},
  'The heavyweight class. Nation-state actors are attached to military or intelligence services, '
  'with substantial resources, access to advanced technology and the ability to recruit skilled '
  'personnel. The A-P-T is their signature: long-term, targeted '
  'attacks that stay undetected while pursuing strategic objectives such as espionage, '
  'intellectual property theft and disruption of critical infrastructure. Their methods include '
  'zero-day exploits, custom malware and careful social engineering. They work hard on '
  'deniability, using complex obfuscation and false-flag operations that make attribution '
  'extremely difficult.'),
 ('bullets',
  {'kick': 'Threat Actors',
   'title': 'Organised Crime and Competitors',
   'items': ['Organised crime — profit-driven, structured like legitimate businesses',
             'Methods — ransomware, banking trojans, card theft, BEC scams',
             'Crime-as-a-service — tools and skills rented out to lower the entry bar',
             'Cross-jurisdiction — operate across borders, hard to prosecute',
             'Competitors — espionage for IP and trade secrets, disinformation'],
   'note': 'Crime wants your money; competitors want your edge.'},
  'Two more classes. Organised crime is profit-driven, structured like legitimate businesses with '
  'specialisation and hierarchy, and running ransomware campaigns, banking trojans, credit card '
  'theft and business email compromise. A thriving underground economy and crime-as-a-service let '
  'the less skilled rent tools and skills, lowering the entry bar for new criminals. Groups '
  'operate across jurisdictions, which makes prosecution difficult. Competitors engage in cyber '
  'espionage to steal intellectual property and trade secrets, and may run disinformation to '
  'damage reputation. Crime wants your money; competitors want your edge.'),
 ('callout',
  {'kind': 'info',
   'label': "Analyst's Lens",
   'title': 'Attribution drives defence',
   'body': 'The insider has authorised access; organised crime brings ransomware; the nation-state '
           'brings espionage; the hacktivist brings disruption. Know who most values what you '
           'hold.'},
  'Which threat actor type worries your organisation most, and why? Walk each type. The insider '
  'has authorised access. Organised crime brings ransomware. The nation-state brings espionage. '
  'The hacktivist brings disruption. The answer depends on what your organisation holds, and that '
  'is exactly how attribution should drive defence. Know who is most likely to value what you '
  'have, and you know where to spend your effort.'),
 ('bullets',
  {'kick': 'Threat Actors',
   'title': 'Match the Actor',
   'items': ['A group defaces a government website to protest a policy — hacktivist, political',
             'An employee steals customer data to sell — insider, financial',
             'A state-sponsored team exfiltrates defence research over a year — APT, strategic',
             'A lone developer finds a bug and reports it responsibly — white hat, ethical'],
   'note': 'Type plus motivation together — the exam asks for the pair.'},
  'Let us match the actor. A group defaces a government website to protest a policy — hacktivists, '
  'political motivation. An employee steals customer data to sell — insider, financial. A '
  'state-sponsored team quietly exfiltrates defence research over a year — A-P-T, strategic. A '
  'lone developer finds a bug and reports it responsibly — white hat, ethical. Type plus '
  'motivation together, always both, because the exam will ask for the pair.'),
 ('chapter',
  {'num': 2,
   'of': 5,
   'title': 'The Attack Surface',
   'blurb': 'Every point an attacker can reach, and the vectors that reach it'},
  'Now we move from the actors to the ground they attack on. Chapter two is the attack surface and '
  'the threat vectors that reach it. You will learn what the surface includes, how it grows, and '
  'the paths an attacker can take — from direct access to the lure-based vectors that work on the '
  'human. Every one of these is a door; the surface is how many doors exist.'),
 ('bullets',
  {'kick': 'Attack Surface',
   'title': 'The Attack Surface',
   'items': ['Definition — every point where an attacker can enter or extract data',
             'Scope — hardware, software, networks, processes, human factors',
             'Scale — from a whole organisation down to a single system',
             'Growth — cloud, mobile and IoT devices add entry points',
             'The rule — the larger the surface, the more opportunities for breach'],
   'note': 'From the server room to the reception desk.'},
  'The attack surface is the set of points where an attacker can enter or extract data. It '
  'encompasses hardware, software, networks, processes and human factors, spanning everything from '
  'the server room to the reception desk. Its scope ranges from an entire organisation down to a '
  'single system. And the surface grows: every cloud service, mobile device and internet-connected '
  'thing adds new entry points. The rule is simple: the larger the surface, the more opportunities '
  'for breach.'),
 ('bullets',
  {'kick': 'Attack Surface',
   'title': 'Threat Vectors',
   'items': ['Definition — the paths or methods used to gain access or deliver a payload',
             'Direct access — USB ports, console access, wired connections',
             'Remote access — VPN, RDP, SSH, the remote administration tools',
             'Wireless & cloud — Wi-Fi, Bluetooth, misconfigured cloud services',
             'Open ports — unnecessary TCP and UDP services exposed to attackers'],
   'note': 'Vectors are the paths; the surface is how many doors exist.'},
  'Vectors are the paths. Direct access: universal serial bus, or U-S-B ports, console access '
  'and wired connections. Remote access: virtual private network, or V-P-N, Remote Desktop '
  'Protocol, or R-D-P, and secure shell — the remote administration tools. Wireless and cloud: '
  'Wi-Fi, Bluetooth and misconfigured cloud services. And '
  'open ports: unnecessary transmission control protocol, or T-C-P, and user datagram protocol, '
  'or U-D-P, services exposed to attackers. The reference text adds the human and file-based '
  'vectors too, such as '
  'malicious documents and infected executables. Every one of these is a door; the surface is how '
  'many doors exist.'),
 ('bullets',
  {'kick': 'Attack Surface',
   'title': 'Lure-Based Vectors',
   'items': ['Trojan horse — malware concealed inside a benign-looking program',
             'Malicious documents — macro and scripting payloads hidden in files',
             'Phishing — deceptive messages delivering links or attachments',
             'Spear phishing & whaling — targeted, personalised against named people',
             'Smishing & vishing — deception by text message and by phone',
             'Watering holes — compromising sites the target regularly visits'],
   'note': 'These bypass the technical perimeter by targeting the person.'},
  'Some vectors work on the human. The Trojan horse: malware concealed inside a benign-looking '
  'program. Malicious documents: macro and scripting payloads hidden in files. Phishing: deceptive '
  'messages delivering links or attachments, with spear phishing aimed at a named individual and '
  'whaling at an executive. Smishing and vishing do the same by text message and by phone. '
  'Watering holes compromise sites the target regularly visits. These vectors bypass the technical '
  'perimeter by targeting the person at the keyboard.'),
 ('bullets',
  {'kick': 'Attack Surface',
   'title': 'Vulnerable Software Vectors',
   'items': ['Unpatched systems — known flaws left open between disclosure and fix',
             'Misconfigurations — open ports, weak firewalls, exposed cloud storage',
             'Zero-day flaws — unknown vulnerabilities with no vendor patch',
             'Unsupported systems — end-of-life software with no patches at all',
             'Default credentials — unchanged factory passwords on devices'],
   'note': 'Vulnerable software is the most common vector of all.'},
  'And some vectors are simply weaknesses you left open. Unpatched systems: known flaws left '
  'exposed between disclosure and fix, as WannaCry exploited a Microsoft flaw that had already '
  'been patched, so the unpatched were hit. Misconfigurations: open ports, weak firewalls and '
  'exposed cloud storage. Zero-day flaws: vulnerabilities unknown to the vendor, with no patch '
  'available. Unsupported systems: end-of-life software with no patches at all. And default '
  'credentials: unchanged factory passwords on routers, switches and devices. Vulnerable software '
  'is the most common vector of all, because it is the most common mistake.'),
 ('bullets',
  {'kick': 'Attack Surface',
   'title': 'The Supply Chain Vector',
   'items': ['Definition — attacks that target vendors, suppliers and dependencies',
             'Software supply chain — malicious code injected into trusted products and updates',
             'Vendor credentials — stolen access to a supplier used to reach the target',
             'Hardware supply chain — compromised devices or components',
             'The lesson — you inherit risk from everything you procure'],
   'note': 'Your security is only as strong as the weakest vendor you trust.'},
  'The last vector is the one you inherit. Supply chain attacks target vendors, suppliers and '
  'dependencies, exploiting the trust between an organisation and its third-party partners. The '
  'software supply chain: malicious code injected into trusted products and updates, as with the '
  'NotPetya attack that rode in through a compromised software update. The attacker may also steal '
  "a vendor's credentials and use them to reach the larger target. The hardware supply chain: "
  'compromised devices or components. The lesson is uncomfortable: you inherit risk from '
  'everything you procure. Your security is only as strong as the weakest vendor you trust.'),
 ('chapter',
  {'num': 3,
   'of': 5,
   'title': 'The Attack Chain',
   'blurb': 'How vectors, vulnerabilities and actors combine into real attacks'},
  "Chapter three puts it all together. Attacks follow a pattern, and the reference text's A-P-T "
  'lifecycle shows it on a grand scale. You will learn the four steps of the attack chain — '
  'reconnaissance, vector, exploit, act — and why every defence you will learn in this course '
  'interrupts one of those steps.'),
 ('bullets',
  {'kick': 'Attack Chain',
   'title': 'Putting It Together',
   'items': ['Recon — the attacker maps the surface and finds a weakness',
             'Vector — a path is chosen: email, port, USB, web',
             'Exploit — a vulnerability is triggered to run the payload',
             'Act — access gained, data taken or operations disrupted'],
   'note': 'Four steps, from the single strike to the year-long campaign.'},
  'Attacks follow a pattern. Recon: the attacker maps the surface and finds a weakness. Vector: a '
  'path is chosen, whether email, an open port, a U-S-B stick or the web. Exploit: a vulnerability is '
  'triggered to run the payload. Act: access is gained, data is taken or operations are disrupted. '
  'Four steps, from the single strike to the year-long espionage campaign. Every defence you will '
  'learn in this course interrupts one of these steps, which is why knowing the chain matters.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Activity',
   'title': 'Map the Vectors',
   'body': 'List every way data could leave your building — physical. Then every way it could '
           'leave your network — technical. Then every way a person could be tricked — human. Rank '
           'the three lists by likelihood.'},
  'Now make the surface personal. List every way data could leave your building, physical vectors '
  'first. Then every way data could leave your network, technical vectors. Then every way a person '
  'could be tricked, human vectors. Rank the three lists by likelihood for your organisation. '
  'Attack surfaces are physical, technical and human, and defence in depth covers all three.'),
 ('chapter',
  {'num': 4,
   'of': 5,
   'title': 'Exam Alignment',
   'blurb': 'How this session maps to the CompTIA objectives'},
  'Chapter four is exam alignment. We map everything in this video to the CompTIA objectives, so '
  'you know exactly what the paper will test and how the questions are framed. The questions are '
  'scenario-based: you will be handed an attack and asked to label the actor, the vector or the '
  'motivation — often both.'),
 ('table',
  {'kick': 'Exam Alignment',
   'title': 'What This Maps To',
   'headers': ['Objective', 'What the exam tests'],
   'rows': [['2.1 Threat actors & motivations', 'Compare actor types; attributes; motivations'],
            ['2.2 Threat vectors & attack surfaces',
             'Vectors and attack surface; vulnerable software; supply chain'],
            ['2.4 Indicators of compromise', 'Malware types, phishing and credential abuse'],
            ['Cross-domain', 'Vulnerability, threat and risk terminology throughout']]},
  'Quick alignment with the paper. Objective 2.1: compare threat actors and their motivations, '
  'across attributes, types and A-P-Ts. Objective 2.2: explain threat vectors and attack surfaces, '
  'including vulnerable software and the supply chain. Objective 2.4 on indicators of compromise '
  'touches the malware, phishing and credential abuse behind many of these actors. And the '
  'vulnerability-threat-risk terminology runs through the whole exam. The questions are '
  'scenario-based: you will be handed an attack and asked to label the actor, the vector or the '
  'motivation, often both.'),
 ('bullets',
  {'kick': 'Exam Alignment',
   'title': 'Check Your Understanding',
   'items': ['Open the session quiz in your browser',
             'Twenty questions, immediate feedback, exam-objective tag on every question',
             'Read each explanation — the distractors teach as much as the answer',
             'Score seventy percent or better before moving on'],
   'note': 'Every question maps to a CompTIA exam objective.'},
  'Now check your understanding. Open the session quiz. Twenty questions, immediate feedback, and '
  'every question is tagged with the exam objective it tests, so you will see the tag, like 2.1 '
  'Threat Actors, above each question. Read every explanation; the distractors teach as much as '
  'the answers. Aim for seventy percent or better before moving on.'),
 ('chapter',
  {'num': 5, 'of': 5, 'title': 'Consolidation', 'blurb': 'Key takeaways and what to revise'},
  'Chapter five is consolidation. We bring the session together into the key takeaways you should '
  'carry forward, and the revision checklist that turns this video into long-term recall.'),
 ('recap',
  {'title': 'Key Takeaways',
   'items': ['Risk = threat × vulnerability — weaknesses plus someone willing to exploit them',
             'Actors have profiles — origin, sophistication, resources and motivation',
             'Motivations vary — financial, political, strategic, personal; attribution shapes '
             'defence',
             'The surface is everywhere — physical, network, human and supply chain',
             'Vectors are paths — direct, remote, wireless, lure-based, vulnerable software']},
  'Five takeaways. One: risk equals threat times vulnerability — weaknesses plus someone willing '
  'to exploit them. Two: actors have profiles — origin, sophistication, resources and motivation. '
  'Three: motivations vary across financial, political, strategic and personal, and attribution '
  'shapes defence. Four: the surface is everywhere — physical, network, human and supply chain. '
  'Five: vectors are paths — direct, remote, wireless, lure-based and vulnerable software.'),
 ('bullets',
  {'kick': 'Consolidation',
   'title': 'Revision Checklist',
   'items': ['Retake the quiz until you score seventy percent without guessing',
             'Profile one real threat group and classify it by the five attributes',
             'Map your surface — five physical, five technical, five human vectors',
             'Read ahead to Session 6: cryptography and public key infrastructure'],
   'note': 'This video is one revision pass — the quiz is the recall test.'},
  'Before you move on, make the learning stick. Retake the quiz until you score seventy percent '
  'without guessing. Profile one real threat group and classify it using the five attributes. Map '
  'your surface — five physical, five technical and five human vectors. And read ahead to Session '
  '6, where we learn the art of cryptography and public key infrastructure. This video is one '
  'revision pass — the quiz is where you prove you can recall it.'),
 ('statement',
  {'kick': 'Next',
   'title': 'Session 6 — Cryptography & Public Key Infrastructure',
   'body': 'Symmetric and asymmetric encryption, hashing, digital signatures, PKI and '
           'certificates.'},
  'That closes Session Five. You can now compare threat actor types and their motivations, explain '
  'threat vectors and attack surfaces, and understand the relationship between vulnerability, '
  'threat and risk. Retake the session quiz until you score seventy percent without guessing. You '
  'have now put faces to the threats behind every control you have learned.')]

if __name__ == "__main__":
    total = sum(len(f[2].split()) for f in FRAMES)
    print("Session 5 narration: %d frames, %d words (~~%d min at 163 wpm)"
          % (len(FRAMES), total, round(total / 163)))

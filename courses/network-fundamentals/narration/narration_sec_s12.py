# narration_sec_s12.py — Security+ SY0-701 (revised), Session 12
# "Governance, Risk, Compliance & Exam Consolidation"
# One-video-per-lesson format. Each frame: (template, payload, narration).
# Narration is read ALOUD IN FULL by ElevenLabs (Billy's voice) — short
# sentences that stand alone without the visual. Abbreviations are written
# so the engine reads them the way they are spoken in the classroom.
# USER RULES: no "good morning" (use "good day"); no courseware timing
# references — only the video's own length may be mentioned.

DECK = 'Governance, Risk, Compliance & Exam Consolidation'
SESSION = 'Session 12 · Security+ SY0-701 (revised)'

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
   'title': 'The Governance Stack',
   'blurb': 'Policy, standard, procedure, guideline — and compliance'},
  'Good day, and welcome to Session Twelve, the final session of the combined Network Fundamentals '
  'and CompTIA Security+ course. This session has eleven objectives. They cover governance, risk, '
  'compliance, and data protection. First, we explain the governance stack: policy, standard, '
  'procedure, and guideline. We describe the common security policies, and regulatory and industry '
  'compliance. Then we cover the risk management process, qualitative and quantitative risk '
  'assessment, the four risk responses, and vendor risk. After that, we explain data classification, '
  'the data lifecycle, and the data roles. Finally, we explain privacy law and data sovereignty. '
  'Eleven sessions built the technical estate. This session builds the layer above it: the policies '
  'that direct people, the risk decisions that direct money, and the law that directs both. It turns '
  'security into organisational behaviour. We begin with the governance stack.'),
 ('statement',
  {'kick': 'The Governance Stack',
   'title': 'Four Layers in a Hierarchy',
   'body': 'Policy: high-level intent. Standard: mandatory requirements. Procedure: step-by-step '
           'instructions. Guideline: recommended practice. Each lower layer adds the detail the '
           'layer above leaves open.'},
  'The governance stack has four layers, in a hierarchy. Policy is high-level intent: what must be '
  'achieved. That is the strategic direction. A standard is specific mandatory requirements: how to '
  'comply, the criteria and benchmarks. A procedure is step-by-step instructions for a task, '
  'including the tools and the data. And a guideline is recommended practice: flexible, and not '
  'mandatory. Policy says why. Standard says how well. Procedure says exactly how. Guideline says '
  'consider. Each lower layer adds the detail that the layer above leaves open.'),
 ('bullets',
  {'kick': 'The Governance Stack',
   'title': 'The Policy Set',
   'items': ['Security policy, password policy, data retention policy',
             'Acceptable use, privacy policy',
             'Audience: everyone — policies are organisational behaviour',
             'Lifecycle: develop, approve, distribute, review'],
   'note': 'Policies are mandatory; guidelines are recommended.'},
  'The policy set includes the security policy, the password policy, the data retention policy, '
  'acceptable use, and the privacy policy. The audience is everyone. Policies are organisational '
  'behaviour, not reading for the security team alone. And the force differs: policies are '
  'mandatory, while guidelines are recommended. Policies also have a lifecycle: develop, approve, '
  'distribute, and review. That keeps them current with new threats and new regulations. The exam '
  'line to hold onto: policy sets intent, standard sets the bar, procedure sets the steps.'),
 ('table',
  {'kick': 'The Governance Stack',
   'title': 'Compliance — Which Rules Apply',
   'headers': ['Type', 'Examples', 'Source'],
   'rows': [['Regulatory', 'GDPR, PCI DSS, HIPAA, SOX', 'Required by law'],
            ['Industry', 'ISO 27001, Cyber Essentials', 'Sector practice'],
            ['Organisational', 'Internal policy, standards', 'The business itself']]},
  'Compliance is about which rules apply to you. Regulatory compliance is required by law. The '
  'General Data Protection Regulation, or GDPR, protects personal data. The Payment Card Industry '
  'Data Security Standard, or PCI DSS, governs card payments. The Health Insurance Portability and '
  'Accountability Act, or HIPAA, applies in healthcare. And the Sarbanes-Oxley Act, or SOX, covers '
  'financial reporting. Industry compliance is required by sector practice, such as International '
  'Organisation for Standardisation 27001, or ISO 27001, or Cyber Essentials. The question is always '
  'the same: which of these apply to this organisation? Judge by its industry, its geography, and '
  'the data it handles. Remember: compliance sets a baseline. Security must go beyond it for '
  'emerging threats. And the cost of getting it wrong is fines, lost trust, and lost business.'),
 ('callout',
  {'kind': 'info',
   'label': 'Standards vs Guidelines',
   'title': 'The difference in force',
   'body': 'A standard is mandatory — audits measure against it. A guideline is recommended — '
           'departures are acceptable if justified. Standards are measured; guidelines are '
           'advisory.'},
  'Here is the difference in force, and it is a scored distinction. A password standard that says '
  'twelve characters minimum is mandatory. Audits measure against it. A guideline that suggests '
  'passphrases is recommended. Departures are acceptable if they are justified. Standards are '
  'measured. Guidelines are advisory. Get that pair exact, and the scenario questions answer '
  'themselves.'),
 ('chapter',
  {'num': 2,
   'of': 5,
   'title': 'Risk Management',
   'blurb': 'Identify, assess, respond, monitor — and vendor risk'},
  'Now we move from governance to risk. Risk management is a loop, and it is the daily work of '
  'security. We will walk the process, the two ways of expressing risk, the four responses, and '
  'the risk that vendors bring with them.'),
 ('bullets',
  {'kick': 'Risk Management',
   'title': 'The Risk Management Loop',
   'items': ['Identify: assets, threats, vulnerabilities',
             'Assess: likelihood and impact',
             'Respond: avoid, transfer, mitigate, accept',
             'Monitor: review and re-assess continuously'],
   'note': 'Log every risk in a risk register with an owner and a treatment status.'},
  'Risk management is a loop with four stages. Identify: assets, threats, and vulnerabilities. Use '
  'asset inventories, threat modelling, and vulnerability assessments. Assess: the likelihood and '
  'the impact. Respond: avoid, transfer, mitigate, or accept. And monitor: review and re-assess '
  'continuously. Risk is not a one-time exercise. It moves as the business moves. Log every risk in '
  'a risk register, with an owner and a treatment status. And review it regularly.'),
 ('table',
  {'kick': 'Risk Management',
   'title': 'Qualitative vs Quantitative',
   'headers': ['Approach', 'Basis', 'Strength'],
   'rows': [['Qualitative', 'Ratings and judgement — high, medium, low', 'Fast, no hard numbers'],
            ['Quantitative', 'Monetary values — SLE, ALE', 'Precise, data-hungry']]},
  'There are two ways to express risk. Qualitative uses ratings and judgement: high, medium, low. '
  'It is fast, and needs no hard numbers. Quantitative uses monetary values. Single Loss Expectancy, '
  'or SLE, is the asset value times the exposure factor. Annualised Loss Expectancy, or ALE, is SLE '
  'times the Annual Rate of Occurrence, or ARO. The maths is precise, but hungry for reliable data. '
  'Many organisations use a hybrid of both. Use qualitative for speed. Use quantitative for '
  'board-level money decisions. And expect to be handed numbers and asked for the ALE.'),
 ('bullets',
  {'kick': 'Risk Management',
   'title': 'The Four Risk Responses',
   'items': ['Avoid: eliminate the activity — no activity, no risk',
             'Transfer: shift the risk — insurance, outsourcing',
             'Mitigate: reduce likelihood or impact — controls',
             'Accept: tolerate, with management sign-off'],
   'note': 'Acceptance is a decision, not an accident — it must be documented.'},
  'There are four risk responses. Avoid means eliminate the activity. No activity, no risk, though '
  'avoidance can cost opportunity. Transfer means shift the risk, through insurance or '
  'outsourcing. Mitigate means reduce the likelihood or the impact, with controls. That is the '
  'daily work. Accept means tolerate the risk, with management sign-off. Avoid and accept are the '
  'poles. Transfer and mitigate sit between them. Acceptance is a decision, not an accident. It '
  'must be documented, with the owner and the reasoning.'),
 ('callout',
  {'kind': 'warn',
   'label': 'Vendor Risk',
   'title': 'Vendors extend your risk',
   'body': "You inherit the vendor's weaknesses — their breaches become your breaches. Assess "
           'before contract, monitor during, exit cleanly at the end. Contracts set security '
           'requirements, incident notification and audit rights.'},
  "Never forget that vendors extend your risk. Third-party risk means you inherit the vendor's "
  'weaknesses. Their breaches become your breaches. The tools are security questionnaires, '
  'documentation review, on-site assessments, and references. Also check financial stability and '
  'certifications, through due diligence. The depth is risk-based: vendors handling sensitive data, '
  'or holding deep access, warrant deeper scrutiny. The lifecycle is assess before contract, monitor '
  'during, and exit cleanly at the end. And the agreements matter: contracts set security '
  'requirements, incident notification, and audit rights. Vendor risk is risk. Manage it like any '
  'other.'),
 ('chapter',
  {'num': 3,
   'of': 5,
   'title': 'Data Classification',
   'blurb': 'Labels, states, roles, and the lifecycle'},
  'Now we turn to the data itself. Data needs a label. It exists in three states. It is owned by '
  'three roles. And it has a lifecycle. Get these four ideas straight, and data protection falls '
  'into place.'),
 ('table',
  {'kick': 'Data Classification',
   'title': 'The Four Classes',
   'headers': ['Class', 'Meaning', 'Example'],
   'rows': [['Public', 'No restriction', 'Brochures, press releases'],
            ['Internal', 'Internal use only', 'Procedures, plans'],
            ['Confidential', 'Restricted', 'HR records, contracts'],
            ['Restricted', 'Most sensitive', 'Trade secrets, health data']]},
  'Data needs a label, and there are four classes. Public means no restriction: brochures, press '
  'releases. Internal means internal use only: procedures, plans. Confidential means restricted: '
  'human resources records and contracts. And restricted is the most sensitive class: trade '
  'secrets, health data. Classification drives controls. The higher the class, the stronger the '
  'protection. And the data owner decides the class.'),
 ('bullets',
  {'kick': 'Data Classification',
   'title': 'Data States and Roles',
   'items': ['Three states: at rest, in transit, in use — each needs controls',
             'Data owner: accountable for classification, access, protection',
             'Data steward: quality and governance day to day',
             'Data custodian: implements the technical controls'],
   'note': 'Accountable, governed, implemented — three different jobs.'},
  'Data exists in three states: at rest, in transit, and in use. Each state needs its own '
  'controls. And there are three roles. The data owner is accountable for classification, access, '
  'and protection. The data steward ensures quality and governance, day to day. The data custodian '
  'implements the technical controls: encryption, access controls, backups. Accountable, governed, '
  'implemented: three different jobs. And the exam expects you never to swap the owner and the '
  'custodian.'),
 ('bullets',
  {'kick': 'Data Classification',
   'title': 'Lifecycle and Retention',
   'items': ['Lifecycle: collect, store, use, share, archive, destroy',
             'Retention policy answers how long — and why',
             'Failure mode: keep everything forever — a breach waiting to happen',
             'Destroy at the end of retention, securely'],
   'note': 'Retention is about the right amount of data, not the maximum.'},
  'Data has a lifecycle: collect, store, use, share, archive, and destroy. The retention policy '
  'answers how long, and why, driven by legal and business needs. The failure mode is keeping '
  'everything forever. That is a data breach waiting to happen. The discipline is to destroy data '
  'at the end of its retention, securely, by wiping or by physical destruction of the media. '
  'Retention is about the right amount of data, not the maximum.'),
 ('chapter',
  {'num': 4, 'of': 5, 'title': 'Privacy Law & Sovereignty', 'blurb': 'The law above the policy'},
  'Now the law above the policy. Privacy is not optional. It is law, and the penalties are severe. '
  'We will cover the GDPR principles and rights, and the idea of data sovereignty.'),
 ('bullets',
  {'kick': 'Privacy Law',
   'title': 'GDPR and UK GDPR',
   'items': ['Principles: lawful, transparent, minimised, accurate, secure',
             'Rights: access, rectification, erasure, portability, restriction',
             'Consent: informed, specific, freely given',
             'Breach duty: notify the regulator within 72 hours where required'],
   'note': 'Penalties up to four percent of annual global turnover.'},
  'The GDPR and the UK GDPR are the European Union and United Kingdom data protection frameworks. '
  'The principles are lawful, transparent, minimised, accurate, and secure. The rights are access, '
  'rectification, erasure, portability, and restriction. Individuals can exercise them. Consent '
  'must be informed, specific, and freely given. And there is a breach duty: notify the regulator '
  'within seventy-two hours where required. Privacy is not optional. It is law, and the penalties '
  'are severe: up to four percent of annual global turnover.'),
 ('statement',
  {'kick': 'Privacy Law',
   'title': 'Data Sovereignty',
   'body': 'Data is subject to the laws of the jurisdiction where it resides. Cloud regions matter '
           '— legal jurisdiction follows the data. Regulations apply by the location of the data '
           'subject, not merely where your servers sit.'},
  'Where data lives matters. Data sovereignty means data is subject to the laws of the '
  'jurisdiction where it resides. The implication: cloud regions matter, because legal '
  'jurisdiction follows the data. Choose regions that match your compliance needs. Geography '
  'matters too: regulations such as GDPR apply by the location of the data subject, not merely '
  'where your servers sit. The exam line: sovereignty is jurisdiction, not geography for its own '
  'sake.'),
 ('chapter',
  {'num': 5, 'of': 5, 'title': 'Exam Consolidation', 'blurb': 'Five domains, complete'},
  'And so we reach the end of the course. This final part consolidates the whole journey: the five '
  'domains, the key takeaways, and the checklist that leaves you exam-ready.'),
 ('bullets',
  {'kick': 'Exam Consolidation',
   'title': 'The Five-Domain Map',
   'items': ['General Security Concepts — sessions one and two',
             'Threats, Vulnerabilities and Mitigations — three to five',
             'Security Architecture — six and seven',
             'Security Operations — eight to eleven',
             'Security Program Management — this session'],
   'note': 'Twelve sessions, five domains, complete.'},
  'Here is the whole map. General Security Concepts, in sessions one and two. Threats, '
  'Vulnerabilities and Mitigations, in sessions three to five. Security Architecture, in sessions '
  'six and seven. Security Operations, in sessions eight to eleven. And Security Program '
  'Management, in this session. Twelve sessions, five domains, complete. Every block built on the '
  'last.'),
 ('recap',
  {'title': 'Key Takeaways',
   'items': ['Governance directs behaviour — policy, standard, procedure',
             'Risk drives decisions — identify, assess, respond, monitor',
             'Vendors extend risk — assess, contract, monitor',
             'Data needs classification and a disciplined lifecycle',
             'Privacy is law — GDPR principles, rights, breach duty']},
  'Five takeaways to carry with you. One: governance directs behaviour. Policy sets intent, '
  'standards set the bar, procedures set the steps. Two: risk drives decisions. Identify, assess, '
  'respond, monitor. Three: vendors extend risk. Assess, contract, monitor. Four: data needs '
  'classification and a disciplined lifecycle. Five: privacy is law. The GDPR principles, the '
  'rights, and the seventy-two hour breach duty.'),
 ('statement',
  {'kick': 'Exam Consolidation',
   'title': 'You Are Exam-Ready',
   'body': 'Revise the five domains, practise performance-based items, and book the exam: ninety '
           'questions, ninety minutes, pass mark seven hundred and fifty. The certification is the '
           'start, not the destination.'},
  'That closes Session Twelve, and with it the whole course. You can now build the governance '
  'stack, run risk management, manage vendor risk, classify and protect data, apply privacy law, '
  'and understand sovereignty. Revise the five domains. Re-take the earlier session quizzes as a '
  'full sweep. Then book the exam: ninety questions, ninety minutes, pass mark seven hundred and '
  'fifty. You are ready. Good luck in the exam, and stay curious. The certification is the start, '
  'not the destination.')]

if __name__ == "__main__":
    total = sum(len(f[2].split()) for f in FRAMES)
    print("Session 12 narration: %d frames, %d words (~~%d min at 163 wpm)"
          % (len(FRAMES), total, round(total / 163)))

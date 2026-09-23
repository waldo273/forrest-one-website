# narration_sec_s11.py — Security+ SY0-701 (revised), Session 11
# "Security Operations: Monitoring, Incident Response & Forensics"
# One-video-per-lesson format. Each frame: (template, payload, narration).
# Narration is read ALOUD IN FULL by ElevenLabs (Billy's voice) — short
# sentences that stand alone without the visual. Abbreviations are written
# so the engine reads them the way they are spoken in the classroom.
# USER RULES: no "good morning" (use "good day"); no courseware timing
# references — only the video's own length may be mentioned.

DECK = 'Security Operations: Monitoring, Incident Response & Forensics'
SESSION = 'Session 11 · Security+ SY0-701 (revised)'

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
   'title': 'Monitoring & the IR Lifecycle',
   'blurb': 'Data sources, alerting, and the six phases of response'},
  'Good day, and welcome to Session Eleven of the combined Network Fundamentals and CompTIA '
  'Security+ course. This session is Security Operations: monitoring, incident response, and '
  'forensics. Sessions one to ten prevented, detected, and hardened. This is the moment something '
  'gets through. Three skills carry the whole session: monitoring that alerts, response that '
  'contains the damage, and forensics that proves what happened. This is Domain Four, the largest '
  'domain on the exam, so the weight here is real. We begin with monitoring and the incident '
  'response lifecycle.'),
 ('statement',
  {'kick': 'The Alarm',
   'title': 'The Shape of the Session',
   'body': 'Monitor, respond, investigate, recognise. The exam rewards sequencing — phases and '
           'steps in the right order.'},
  'Here is the shape of the session. Monitor first, respond second, investigate third, and '
  'recognise indicators throughout. The exam rewards sequencing — phases and steps in the right '
  'order. Monitoring is only as good as its sources, response only as good as its lifecycle, and '
  'forensics only as good as its evidence handling. Hold that sequence in your head, because each '
  'block builds on the last.'),
 ('bullets',
  {'kick': 'The Alarm',
   'title': 'Session Objectives',
   'items': ['Design monitoring — data sources, baselines, thresholds',
             'Avoid alert fatigue — tune alerting to signal',
             'Run the IR lifecycle — preparation to lessons learned',
             'Handle evidence — chain of custody, order of volatility',
             'Apply forensic techniques — imaging, hashing, carving',
             'Read indicators — malware, network, application, behaviour'],
   'note': 'Six objectives — the quiz at the end tests every one.'},
  'By the end of this session you will be able to do twelve things. You will describe monitoring '
    'data sources — logs, flow data, packet capture, sensors, and the security information and event '
    'management, or SIEM, that aggregates and correlates them. You will explain alerting: baselines, '
    'thresholds, alert fatigue, and real-time alerting versus trend analysis. You will describe the '
    'incident response lifecycle, from preparation through detection, containment, eradication, '
    'recovery, and lessons learned. You will classify incidents and assign severity to drive response '
    'urgency, and explain containment strategy and its evidence trade-offs. You will describe digital '
    'forensics basics — evidence types, admissibility, write blockers, and the preservation-first '
    'mindset. You will explain chain of custody and why breaking it makes evidence inadmissible, and '
    'the order of volatility, including memory forensics. You will describe preservation — imaging, '
    'hashing, legal hold, and log retention — and apply forensic techniques like file carving, '
    'timeline analysis, hash analysis, and metadata analysis. You will explain after-action review '
    'and root cause analysis to prevent recurrence. And you will recognise indicators of malicious '
    'activity across malware, network, application, and behaviour. Twelve objectives, and the quiz at '
    'the end tests every one of them.'),
 ('bullets',
  {'kick': 'Monitoring',
   'title': 'Data Sources for Monitoring',
   'items': ['Logs — security, system, application, network device, firewall',
             'Flow data — NetFlow, sFlow: conversation summaries, who spoke to whom',
             'Packet capture — full payloads when depth and evidence are required',
             'Sensors — IDS/IPS, EDR, endpoint telemetry',
             'SIEM — aggregates and correlates all sources into one view'],
   'note': 'Layer the sources — summaries for trend, captures for evidence.'},
  'Monitoring is only as good as its sources. Logs: security, system, and application events, plus '
  'firewall and network device logs. Flow data — NetFlow and sFlow — gives conversation summaries: '
  'who talked to whom, how much, and for how long. Packet capture gives full payloads when you '
  'need depth and evidence. Sensors: intrusion detection and prevention systems, endpoint '
  'detection and response, and endpoint telemetry. And the sim aggregates and correlates all of '
  'these into a single view. Layer the sources — summaries for trend, captures for evidence.'),
 ('bullets',
  {'kick': 'Monitoring',
   'title': 'Alerting That Works',
   'items': ["Baselines — know what 'normal' looks like first",
             'Thresholds — alert on meaningful deviations, not noise',
             'Alert fatigue — too many alarms, real ones get ignored',
             'Real-time vs trend — immediate alerts and long-term analysis',
             'Alert tuning — reduce false positives',
             'The tuning loop — review, refine, retest'],
   'note': 'Monitoring is alive, not a one-time setup.'},
  'Alerting fails when it screams constantly. Baselines: know what normal looks like first — you '
  'cannot detect abnormal without one. Thresholds: alert on meaningful deviations, not noise. '
  'Alert fatigue: too many alarms, and the real ones get ignored — that is how breaches go '
  'unnoticed for months. Pair real-time alerting with long-term trend analysis: one catches the '
  'active threat, the other reveals a coordinated attack building over weeks. Tune your alerts to '
  'cut false positives, then run the tuning loop — review, refine, retest. Monitoring is alive, '
  'not a one-time setup.'),
 ('bullets',
  {'kick': 'Incident Response',
   'title': 'The IR Lifecycle',
   'items': ['Preparation — plans, tools, trained people, before the incident',
             'Detection & analysis — confirm it, scope it, classify it, grade severity',
             'Containment — stop the spread: isolate, segment',
             'Eradication — remove the cause from the environment',
             'Recovery — restore validated systems to normal operation',
             'Lessons learned — fix the process, not just the symptom'],
   'note': 'Preparation first — that is the order the exam expects.'},
  'The incident response lifecycle has six phases. Preparation: plans, tools, and trained people — '
  'before the incident, always. Detection and analysis: confirm it, scope it, classify it, and '
  'grade its severity. Containment: stop the spread — isolate and segment. Eradication: remove the '
  'cause from the environment. Recovery: restore validated systems to normal operation. Lessons '
  'learned: the post-incident review that fixes the process, not just the symptom. Preparation '
  'comes first — that is the order the exam expects.'),
 ('bullets',
  {'kick': 'Incident Response',
   'title': 'Containment and Eradication',
   'items': ['Containment strategy — short-term isolation then long-term control',
             'The trade-off — containment preserves evidence but alerts the adversary',
             'Eradication — remove malware, revoke credentials, close the hole',
             'Classification — unauthorised access, malware, DoS, data breach',
             'Severity — low to critical, grades the urgency of response'],
   'note': 'Containment stops the bleeding; eradication stops the cause.'},
  'Containment and eradication are different jobs. Containment strategy: short-term isolation '
  'first, then long-term control — the network segment pulled, then the systems rebuilt. The '
  'trade-off: containment preserves evidence but can alert the adversary, who may accelerate or '
  'cover their tracks. Eradication: remove malware, revoke credentials, and close the hole. Every '
  'incident is classified — unauthorised access, malware, denial of service, data breach — and '
  'graded low to critical. That classification and severity set how urgently you respond. The exam '
  'line: containment stops the bleeding; eradication stops the cause.'),
 ('bullets',
  {'kick': 'Incident Response',
   'title': 'Recovery and Lessons Learned',
   'items': ['Recovery — restore from validated backups, verify integrity',
             'Monitoring — intensified post-incident, watch for re-infection',
             'After-action review — what worked, what failed, what changes',
             'Root cause analysis — find the underlying source',
             'Lessons learned — update the plan, train again, close the gaps',
             'The report — timeline, root cause, actions taken, improvements'],
   'note': 'The incident is not over until the process is fixed.'},
  'Recovery is more than pressing the power button. Restore from validated backups and verify '
  'integrity — a restored system that still carries the malware is not recovered. Intensify '
  'monitoring afterwards, watching for re-infection. Then the after-action review with all '
  'stakeholders: what worked, what failed, what changes. Use root cause analysis to find the '
  'underlying source so the incident cannot recur — patching the hole matters more than treating '
  'the symptom. Update the plan, train again, close the gaps. And write the report: timeline, root '
  'cause, actions taken, improvements. The incident is not over until the process is fixed.'),
 ('callout',
  {'kind': 'info',
   'label': 'Discussion',
   'title': 'When is an incident actually over?',
   'body': 'Restoration of service is not the end — verification, intensified monitoring and '
           'lessons learned are what close the incident.'},
  'Here is the question worth pausing on: when is an incident actually over? Restoration of '
  'service is not the end. Verification, intensified monitoring, and lessons learned are what '
  'close the incident. Recovery ends when the process is fixed, not when the screens are back. '
  'That distinction — between service restored and incident closed — is exactly the kind of '
  'sequencing the exam tests.'),
 ('chapter',
  {'num': 2,
   'of': 5,
   'title': 'Digital Forensics',
   'blurb': 'Evidence, chain of custody, volatility, and preservation'},
  'Now we move from response to investigation. Chapter two is digital forensics — the discipline '
  'that answers the question that comes after response: what actually happened? You will learn the '
  'basics of evidence, the chain of custody that keeps it admissible, the order of volatility that '
  'decides what you capture first, and the preservation techniques that protect the original. '
  'These are the two favourite exam concepts — chain of custody and order of volatility — so give '
  'them your full attention.'),
 ('bullets',
  {'kick': 'Forensics',
   'title': 'Digital Forensics Basics',
   'items': ['The goal — collect, preserve and analyse evidence defensibly',
             'Evidence types — disk, memory, network, logs, filesystem artefacts',
             'The standard — evidence must be admissible, handle it lawfully',
             'Write blockers — prevent any change to the original data',
             'Authorization — search warrant or consent before collection',
             'The mindset — preserve first, analyse second'],
   'note': 'Handle it lawfully, or it counts for nothing.'},
  'Forensics answers the question that comes after response: what actually happened? The goal: '
  'collect, preserve, and analyse evidence defensibly. Evidence types: disk, memory, network, '
  'logs, and filesystem artefacts. The standard: evidence must be admissible — handle it lawfully, '
  'or it counts for nothing. Use write blockers so nothing touches the original data. And '
  'collection needs authorisation — a warrant or consent — before it starts. Above all, the '
  'mindset: preserve first, analyse second.'),
 ('bullets',
  {'kick': 'Forensics',
   'title': 'Chain of Custody',
   'items': ['The record — who handled the evidence, when, and what changed',
             'Every handover — documented, signed, and tracked',
             'The purpose — prove the evidence is what it claims to be',
             'Break the chain — and the evidence becomes inadmissible'],
   'note': 'The case fails on process, not facts.'},
  "The chain of custody is the evidence's biography. The record: who handled the evidence, when, "
  'and what changed. Every handover: documented, signed, and tracked. The purpose: prove the '
  'evidence is what it claims to be — that it was not swapped, altered, or contaminated. Break the '
  'chain, and the evidence becomes inadmissible. The case fails on process, not on facts. That is '
  'why the record matters as much as the evidence itself.'),
 ('bullets',
  {'kick': 'Forensics',
   'title': 'Order of Volatility',
   'items': ['The rule — capture the most volatile data first',
             'Registers/cache — nanoseconds, gone in an instant',
             'RAM — seconds: process memory, network connections',
             'Disk — minutes to hours, survives reboot',
             'Memory forensics — running processes and open connections',
             'The order — memory before disk, live before offline'],
   'note': 'Capture the perishable evidence before the workstation arrives.'},
  'Not all evidence waits for you. Order of volatility: capture the most volatile data first. '
  'registers and cache: gone in nanoseconds. Random Access Memory, or RAM: seconds — process '
    'memory, open network connections, running processes. Disk: minutes to hours — it survives a '
    'reboot. And remember memory forensics: running processes and open connections often hold the '
    'story that the disk never recorded. The order: memory before disk, live before offline. '
    'Capture the perishable evidence before the forensic workstation even arrives.'),
 ('bullets',
  {'kick': 'Forensics',
   'title': 'Preservation',
   'items': ['Imaging — bit-for-bit copies, never analyse the original',
             'Deleted data — a forensic image captures deleted and hidden files',
             'Hashing — integrity verification, prove nothing changed',
             'Legal hold — preserve records relevant to litigation',
             'Log retention — retain logs for compliance and investigation',
             'The rule — analyse the copy, archive the original'],
   'note': 'You cannot investigate what you never kept.'},
  'Preservation is the discipline. Imaging: bit-for-bit copies — you never analyse the original. A '
  'forensic image captures deleted and hidden files that a normal copy would miss. Hashing: '
  'integrity verification — the hash proves nothing changed between capture and court. Legal hold: '
  'preserve records relevant to litigation — deletion stops when the hold is issued. And retain '
  'logs to meet compliance and investigation needs — you cannot investigate what you never kept. '
  'The rule: analyse the copy, archive the original.'),
 ('bullets',
  {'kick': 'Forensics',
   'title': 'Forensic Techniques',
   'items': ['File carving — recovering files from raw disk without the filesystem',
             'Timeline analysis — reconstructing events in order',
             'Hash analysis — matching known-good and known-bad files',
             'Metadata analysis — creation dates, authorship, modification history',
             'The output — a defensible story of what happened'],
   'note': 'Evidence, ordered and verified.'},
  'The techniques. File carving: recovering files from raw disk without the filesystem — deleted '
  'files, hidden data. Timeline analysis: reconstructing events in order — what happened, when. '
  'Hash analysis: matching known-good and known-bad files against databases. And metadata '
  'analysis: creation dates, authorship, and modification history — the context behind the file. '
  'The output is a defensible story of what happened — evidence, ordered and verified.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Activity',
   'title': 'Handle the evidence',
   'body': 'Volatile first — RAM and connections. Image and hash before analysing. Document every '
           'handover — break the chain and it is inadmissible.'},
  'Let us put it together with a scenario. A compromised server is found. What do you capture '
  'first? The volatile data — ram and network connections. Before any analysis, '
  'image the disk and hash it. Two investigators handle the disk — every handover documented and '
  'signed. And what breaks the case in court? A broken chain of custody — the evidence becomes '
  'inadmissible. Volatile first, image and hash before analysing, and document every handover.'),
 ('chapter',
  {'num': 3,
   'of': 5,
   'title': 'Indicators of Malicious Activity',
   'blurb': 'Malware, network, application and behavioural IoCs'},
  'Chapter three is the indicators — the fingerprints of malicious activity. You will learn to '
  'read the four families: malware, network, application, and behavioural. These are scenario '
  'material on the exam, so the skill is reading a pattern and naming the indicator. The lesson '
  'throughout: indicators combine into a story, and your monitoring layers decide which one you '
  'catch first.'),
 ('table',
  {'kick': 'Indicators',
   'title': 'Malware Indicators',
   'headers': ['Indicator', 'What it looks like'],
   'rows': [['Virus / worm', 'Self-replicating code; spreading files, scanning activity'],
            ['Trojan', 'Benign-looking software doing malicious work'],
            ['Ransomware', 'Encrypted files, ransom notes, mass renames'],
            ['Spyware / keylogger', 'Silent exfiltration of credentials and data'],
            ['Rootkit', 'Hidden presence — privileges maintained stealthily'],
            ['Botnet', 'Command-and-control traffic, coordinated activity']]},
  'The malware indicators — the fingerprints. Viruses and worms self-replicate and spread — you '
  'see spreading files and scanning activity. Trojans look benign and act malicious. Ransomware '
  'encrypts files and leaves notes, with mass renames. Spyware and keyloggers exfiltrate '
  'credentials and data silently. Rootkits hide deep and maintain privileges stealthily. And '
  'botnets show command-and-control, or C two, traffic and coordinated activity. Know each '
  'signature '
  'behaviour.'),
 ('bullets',
  {'kick': 'Indicators',
   'title': 'Network Indicators',
   'items': ['Port scanning — rapid probes across ports and hosts, reconnaissance',
             'Unusual traffic — odd volumes, protocols, destinations',
             'Data exfiltration — sudden outbound spikes when data leaves',
             'C2 beacons — regular small connections to suspicious hosts',
             'The lesson — traffic anomalies are often the first signal'],
   'note': 'The heartbeat of a compromised system.'},
  'The network tells stories. Port scanning: rapid probes across ports and hosts — reconnaissance. '
  'Unusual traffic: odd volumes, protocols, and destinations. Data exfiltration: sudden outbound '
  'spikes when data leaves the network. C two beacons: regular, small connections to suspicious '
  'hosts '
  '— the heartbeat of a compromised system. The lesson: traffic anomalies are often the first '
  'signal of a breach — which is why monitoring matters.'),
 ('bullets',
  {'kick': 'Indicators',
   'title': 'Application and Behavioural Indicators',
   'items': ['Web logs — injection probes, scanning paths, abnormal errors',
             'Email — phishing patterns, spoofed senders, malicious attachments',
             'Privilege escalation — accounts gaining rights they should not have',
             'Privilege usage — elevated accounts acting at unusual hours',
             'Authentication — repeated failed logins, brute force or stuffing',
             'Behaviour — unusual times, impossible travel, data volume spikes'],
   'note': 'Indicators combine into a story.'},
  'The application and human layers. Web logs: injection probes, scanning paths, and abnormal '
  'error rates. Email: phishing patterns, spoofed senders, and malicious attachments. Privilege '
  'escalation: accounts gaining rights they should not have. Privilege usage: elevated accounts '
  'acting at unusual hours or on sensitive data. Authentication: repeated failed logins point to '
  'brute force or credential stuffing. And behaviour: unusual login times, impossible travel — a '
  'login from London and Sydney ten minutes apart — and spikes in data volume. Indicators combine '
  'into a story.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Activity',
   'title': 'Read the indicators',
   'body': 'A C2 beacon, impossible travel, ransomware — monitoring layers catch different ones.'},
  'Let us read some patterns. A server sends one megabyte every ten minutes to an unknown internet '
  'protocol — that is a C two beacon. A user logs in from London and Sydney in ten minutes — '
  'impossible travel. Files renamed with a dot-locked extension and a note — ransomware. Which '
  'indicator would you have caught first? That depends on your monitoring layers — and that is the '
  'point. Different layers catch different indicators.'),
 ('chapter',
  {'num': 4, 'of': 5, 'title': 'Exam Alignment', 'blurb': 'How the session maps to the paper'},
  'Chapter four is exam alignment. We map everything you have just learned onto the paper, so you '
  'know exactly what each objective tests. Domain Four is scenario-heavy, and the exam rewards '
  'order-of-operations thinking. Knowing which objective each concept belongs to makes your '
  'revision traceable.'),
 ('table',
  {'kick': 'Exam',
   'title': 'What This Maps To',
   'headers': ['Objective', 'What the exam tests'],
   'rows': [['11.1 Monitoring & alerting', 'Data sources; baselines; thresholds; alert fatigue'],
            ['11.2 Incident response', 'Lifecycle phases; containment; eradication; recovery'],
            ['11.3 Forensics', 'Chain of custody; order of volatility; imaging; techniques'],
            ['11.4 Indicators', 'Malware, network, application and behavioural IoCs']]},
  'Here is the alignment. Objective eleven point one, monitoring and alerting: data sources, '
  'baselines, thresholds, and alert fatigue. Objective eleven point two, incident response: '
  'lifecycle phases, containment, eradication, and recovery. Objective eleven point three, '
  'forensics: chain of custody, order of volatility, imaging, and techniques. Objective eleven '
  'point four, indicators: malware, network, application, and behavioural. Sequencing scenarios '
  'run throughout — which phase, which evidence step, which indicator.'),
 ('bullets',
  {'kick': 'Exam',
   'title': 'Check Your Understanding',
   'items': ['Open the session quiz in your browser',
             'Twenty questions, immediate feedback, exam-objective tag on every question',
             'Read each explanation — the distractors teach as much as the answer',
             'Score seventy percent or better before moving on'],
   'note': 'Every question maps to a CompTIA exam objective.'},
  'Now check your understanding. Open the session quiz in your browser. Twenty questions, '
  'immediate feedback, and every question is tagged with the exam objective it tests — you will '
  'see the tag above each question. Read every explanation — the distractors teach as much as the '
  'answer. And aim for seventy percent or better before you move on. Every question maps to a '
  'CompTIA exam objective, so the quiz is your fastest route to Domain Four marks.'),
 ('chapter',
  {'num': 5, 'of': 5, 'title': 'Consolidation', 'blurb': 'Key takeaways and what to revise'},
  'Chapter five is consolidation. We bring the session together into the key takeaways you should '
  'carry forward, and the revision checklist that turns this session into long-term recall.'),
 ('recap',
  {'title': 'Key Takeaways',
   'items': ['Monitoring needs tuning — baselines, thresholds, and protection from alert fatigue',
             'IR is a lifecycle — prepare, detect, contain, eradicate, recover, learn',
             'Evidence is fragile — chain of custody and order of volatility protect it',
             'Preserve before analysing — image, hash, then work on the copy',
             'Indicators tell the story — malware, network, application and behaviour, read '
             'together']},
  'Five takeaways. One: monitoring needs tuning — baselines, thresholds, and protection from alert '
  'fatigue. Two: incident response is a lifecycle — prepare, detect, contain, eradicate, recover, '
  'learn. Three: evidence is fragile — chain of custody and order of volatility protect it. Four: '
  'preserve before analysing — image, hash, then work on the copy. Five: indicators tell the story '
  '— malware, network, application, and behaviour, read together.'),
 ('bullets',
  {'kick': 'Consolidation',
   'title': 'Revision Checklist',
   'items': ['Retake the session quiz until you score well without guessing',
             'Know your IR plan — who leads, what tools, when to escalate',
             'Practise volatility — list your own systems in capture order',
             'Read ahead to Session 12: governance, risk, compliance and data protection'],
   'note': 'This video is one revision pass — the quiz is the recall test.'},
  'Before you move on, make the learning stick. Retake the session quiz until you score well '
  'without guessing. Know your incident response plan — who leads, what tools, and when to '
  'escalate. Practise volatility — list your own systems in capture order. And read ahead to '
  'Session 12, the final session: governance, risk, compliance, and data protection. This video is '
  'one revision pass — the quiz is where you prove you can recall it.'),
 ('statement',
  {'kick': 'Next',
   'title': 'Session 12 — Governance, Risk, Compliance & Data Protection',
   'body': 'Policies and standards, risk management processes, compliance and privacy — the layer '
           'that turns security from technical work into organisational behaviour.'},
  'That closes Session Eleven. You can now watch with monitoring, alerting and log analysis, '
  'respond through the incident response lifecycle, and prove with forensics, evidence, chain of '
  'custody and timelines. Retake the session quiz until you score seventy percent without '
  'guessing. This is the operational core that investigates what the earlier controls fail to '
  'stop.')]

if __name__ == "__main__":
    total = sum(len(f[2].split()) for f in FRAMES)
    print("Session 11 narration: %d frames, %d words (~~%d min at 163 wpm)"
          % (len(FRAMES), total, round(total / 163)))

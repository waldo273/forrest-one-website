# narration_sec_s10.py — Security+ SY0-701 (revised), Session 10
# "Vulnerability Management, Resiliency & Asset Protection"
# One-video-per-lesson format. Each frame: (template, payload, narration).
# Narration is read ALOUD IN FULL by ElevenLabs (Billy's voice) — short
# sentences that stand alone without the visual. Abbreviations are written
# so the engine reads them the way they are spoken in the classroom.
# USER RULES: no "good morning" (use "good day"); no courseware timing
# references — only the video's own length may be mentioned.

DECK = 'Vulnerability Management, Resiliency & Asset Protection'
SESSION = 'Session 10 · Security+ SY0-701 (revised)'

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
   'title': 'The Hunt & the Safety Net',
   'blurb': 'Finding weaknesses, then surviving what gets through'},
  'Good day, and welcome to Session Ten of the combined Network Fundamentals and CompTIA Security+ '
  'course. This session is about two sides of the same coin. Sessions eight and nine built the '
  'defences. Now we do two things: find the holes before the attackers do, and survive what gets '
  'through. The hunt, and the safety net. We begin with how vulnerabilities are found, then how '
  'they are assessed, remediated and disclosed, and finally how resiliency, backups and the '
  'physical side of security keep the business running.'),
 ('statement',
  {'kick': 'The Loop',
   'title': 'The Continuous Hunt & the Safety Net',
   'body': 'The hunt: identify, assess, remediate, disclose — the vulnerability loop. The safety '
           'net: resiliency, backups, physical and environmental controls. The loop never stops, '
           'because the attack surface never stops changing.'},
  'Here is the shape of the session. The hunt is the vulnerability loop: identify, assess, '
  'remediate, disclose. The safety net is resiliency, backups, and the physical and environmental '
  'controls that protect the site. The loop never stops, because the attack surface never stops '
  'changing. Every time you close one hole, the environment shifts and a new one appears. That is '
  'why this is a continuous process, not a one-off project.'),
 ('bullets',
  {'kick': 'The Loop',
   'title': 'Session Objectives',
   'items': ['Explain vulnerability identification — scanners, agents, sources',
             'Assess and prioritise with CVSS and context',
             'Remediate and disclose — patching, compensating controls',
             'Design resiliency with RTO and RPO',
             'Secure the site with physical and environmental controls',
             'Manage assets from acquisition to destruction'],
   'note': 'Six objectives — the quiz at the end tests every one.'},
  'By the end of this session you will be able to explain how vulnerabilities are found: network '
    'scanners, host agents and vulnerability sources. You will compare scanner-based and agent-based '
    'approaches, including their strengths and weaknesses. You will assess findings using the '
    'Common Vulnerability Scoring System, or CVSS, along with exploitability, exposure and asset '
    'criticality. You will prioritise remediation based on risk, not score alone. You will describe '
    'remediation strategies: patching, compensating controls and documented risk acceptance. You '
    'will explain patch management in practice: testing, change control, exceptions and re-scan '
    'verification. You will describe vulnerability reporting and responsible disclosure, including '
    'service level agreements, or SLAs. You will explain penetration testing and rules of '
    'engagement. You will design resiliency: redundancy, high-availability clusters, backup types '
    'and the three-two-one rule. You will explain the recovery time objective, or RTO, and the '
    'recovery point objective, or RPO, and the trade-offs between them. You will describe physical '
    'and environmental controls. And you will explain data destruction and asset management across '
    'the asset lifecycle. Twelve objectives, and the quiz at the end tests every one of them.'),
 ('bullets',
  {'kick': '10A · Identification',
   'title': 'How Vulnerabilities Are Found',
   'items': ['Scanners — network, host and application assessments',
             'Agents — on-host visibility of installed software',
             'Credentialed scans — see missing patches and misconfiguration',
             'Sources — CVE identifiers, NVD and vendor advisories',
             'The limitation — scans find technical holes, not design flaws'],
   'note': 'Three sources: scanners, agents, and the vulnerability feeds.'},
  'Vulnerabilities are found through three sources. Network scanners assess routers, switches, '
  'servers and applications for open ports, insecure protocols and outdated versions. Host agents '
  'see what is installed on the machine itself. And the feeds keep your tooling current: '
  'identifiers from Common Vulnerabilities and Exposures, or CVE; the National Vulnerability '
  'Database, or NVD; and vendor advisories. Two scan modes matter. Non-credentialed scans see '
  'only what an outsider can. Credentialed scans log in and reveal missing patches and '
  'misconfiguration. And the limitation: scans find technical holes, but they do not see design '
  'flaws or policy gaps.'),
 ('table',
  {'kick': '10A · Identification',
   'title': 'Scanner or Agent?',
   'headers': ['Approach', 'Strengths', 'Weaknesses'],
   'rows': [['Network scanner',
             'No install; sees the attack surface',
             'Misses encrypted or internal detail'],
            ['Host agent',
             'Deep visibility of installed software',
             'Must be deployed and maintained'],
            ['Credentialed scan',
             'Sees internal state and missing patches',
             'Needs valid credentials to run'],
            ['Combined', 'Attack surface plus host truth', 'More moving parts to manage']]},
  'The comparison table. A network scanner needs no installation and sees the attack surface as an '
  'attacker would, but it misses what is encrypted or hidden from the outside. A host agent sees '
  'the installed software in depth, but it must be deployed and maintained on every host. A '
  'credentialed scan sits between them: it uses valid credentials to reveal internal state, such '
  'as missing patches and misconfigured settings. Combined, you get the attack surface plus the '
  'host truth, at the cost of more moving parts to manage.'),
 ('bullets',
  {'kick': '10B · Assessment',
   'title': 'Making Sense of Findings',
   'items': ['CVSS — scores severity using base, temporal and environmental metrics',
             'Risk = likelihood × impact × exposure',
             'The question — is this vulnerability reachable and critical?',
             'False positives — validate by manual test or log review',
             'The trap — a high score on an unreachable asset is not a risk'],
   'note': 'Severity is not risk.'},
  'The findings arrive. Now what? CVSS scores severity from three '
  'metric groups. Base metrics describe the intrinsic nature of the flaw. Temporal metrics capture '
  'the current exploit state. Environmental metrics reflect the value of the asset in your '
  'organisation. But severity is not risk. Risk is likelihood times impact times exposure. The '
  'question for every finding: is this vulnerability reachable, and does it touch something '
  'critical? And validate false positives by manual test or log review before you spend time on '
  'them.'),
 ('bullets',
  {'kick': '10B · Assessment',
   'title': 'Prioritisation',
   'items': ['Exploitability — is there exploit code, and is it used in the wild?',
             'Exposure — is the asset internet-facing or well connected?',
             'Criticality — does it support a critical function or hold crown-jewel data?',
             'Scale — categorise thousands of findings to find the urgent few',
             'The trap — fixing by score alone ignores context'],
   'note': 'Three factors layer on top of the score.'},
  'Three factors decide priority, layered on top of the score. Exploitability: is there working '
  'exploit code, and is it being used in the wild? Exposure: is the asset internet-facing or '
  'heavily connected? Criticality: does it support a critical function or hold crown-jewel data? '
  'Organisations often juggle thousands of findings, so categorise by score, criticality and '
  'exposure to surface the urgent few. The trap: fixing by score alone ignores context. A critical '
  'internal tool with no exploit and low exposure is not your top risk.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Activity',
   'title': 'Prioritise the findings',
   'body': 'An internet-facing critical CVSS with a working exploit — remediate now. An internal '
           'tool with a high score but no exploit — lower priority. A false positive — verify '
           'before acting. Exposure and exploitability trump the raw score.'},
  'Let us apply that. An internet-facing web server with a critical CVSS '
  'and a working exploit: remediate now. An internal tool with a critical score but no '
  'exploit and low exposure: lower priority. A scan flags a false positive: verify by manual test '
  'or log review before acting. Which factor outweighs the score? Exposure and exploitability. '
  'They trump the raw number every time.'),
 ('chapter',
  {'num': 2,
   'of': 5,
   'title': 'Remediation & Disclosure',
   'blurb': 'Fixing the holes, then reporting and disclosing them'},
  'Now we move from finding and assessing weaknesses to fixing them. Chapter two is remediation '
  'and disclosure. You will learn the four remediation strategies, how patch management works in '
  'practice, how to report findings to the right audience, and the rules that keep penetration '
  'testing legal. These are the decisions that turn a scan report into a safer environment.'),
 ('bullets',
  {'kick': '10C · Remediation',
   'title': 'Remediation Strategies',
   'items': ['Patch — update software to fix known vulnerabilities',
             'Configuration change — disable services, tighten defaults, reduce surface',
             'Compensating control — monitor, log and detect where patching is impossible',
             'Risk acceptance — documented decision when cost of fix exceeds impact',
             'The rule — every unpatched hole needs a reason and a date'],
   'note': 'Four strategies, in order.'},
  'Four remediation strategies, in order. Patch: update the software to fix the known '
  'vulnerability; this is the first choice. Configuration change: disable unused services, change '
  'default settings and reduce the attack surface where no patch applies. Compensating control: '
  'monitor, log and detect where a direct fix is impossible. Risk acceptance: a documented '
  'decision when the cost of remediation outweighs the impact, reviewed regularly. The rule: every '
  'unpatched hole needs a reason and a date.'),
 ('bullets',
  {'kick': '10C · Remediation',
   'title': 'Patch Management in Practice',
   'items': ['Test before deploy — a patch that breaks you is a new incident',
             'Change control — scheduled, approved, rolled back if needed',
             'Exceptions — documented with owners, risk and expiry dates',
             'Validate by rescanning — confirm patches applied and no residual flaws',
             'Automate — reduce human error across a large estate'],
   'note': 'Patching is a process, not an event.'},
  'Patching is a process, not an event. Test before you deploy; a patch that breaks you is a new '
  'incident. Change control: scheduled, approved, rolled back if needed. Exceptions: when a '
  'vulnerability cannot be patched promptly, document the reason, apply temporary compensating '
  'controls, set a target date, and review the exception regularly. And validate by rescanning '
  'after remediation, to confirm the patch applied and no residual flaw remains. Automation '
  'reduces human error across a large estate.'),
 ('bullets',
  {'kick': '10D · Reporting & Disclosure',
   'title': 'Vulnerability Reporting',
   'items': ['The report — findings, evidence, risk, recommendations and metrics',
             'Metrics — counts by severity, average time to patch',
             'Trends — spot recurring weaknesses and improvement over time',
             'The audience — executives want risk, engineers want detail',
             'The SLA — fix by severity within agreed timescales',
             'Disclosure — responsible: vendor gets time before public'],
   'note': 'Know your audience.'},
  'The report carries findings, evidence, risk and recommendations. Add metrics to track the '
  'programme: counts of vulnerabilities by severity, average time to patch, and the percentage of '
  'systems patched. Use trends to spot recurring weaknesses and measure improvement over time. '
  'Know your audience: executives want risk in business terms, engineers want technical detail. '
  'An SLA sets fix timescales by severity. And disclosure should be responsible: the vendor gets time '
  'to fix before the public knows.'),
 ('bullets',
  {'kick': '10D · Reporting & Disclosure',
   'title': 'Penetration Testing & Rules of Engagement',
   'items': ['Pentest — authorised simulated attack on live systems',
             'Scope — what is in and out: systems, times, techniques',
             'Rules of engagement — written authorisation, no surprises, no collateral',
             'The boundary — testing without permission is the crime'],
   'note': 'Authorisation is mandatory.'},
  'A penetration test is an authorised simulated attack on live systems. Scope defines what is in '
  'and out: systems, times, techniques. Rules of engagement are the written authorisation: no '
  'surprises, no collateral damage. And the boundary: testing without permission is a crime, '
  'whatever the intent. Authorisation is not optional; it is what makes the test legal.'),
 ('callout',
  {'kind': 'info',
   'label': 'Discussion',
   'title': 'A critical vulnerability with no patch',
   'body': 'Compensating controls, segmentation, enhanced monitoring, or documented risk '
           'acceptance — each with an owner and a review date. Unpatchable is not unmanageable.'},
  'Here is the discussion. A critical vulnerability has no patch yet. What are your options? '
  'Compensating controls, segmentation, enhanced monitoring, or documented risk acceptance, each '
  'with an owner and a review date. Unpatchable is not unmanageable, but it must be managed '
  'deliberately, and revisited when the threat changes. The plan is what matters, not the absence '
  'of a patch.'),
 ('chapter',
  {'num': 3,
   'of': 5,
   'title': 'Resiliency & Availability',
   'blurb': 'Redundancy, backups, and the RTO/RPO design'},
  'Chapter three is resiliency and availability. The hunt finds the holes, but some attacks will '
  'still get through. Resiliency is how you survive them. You will learn how redundancy removes '
  'single points of failure, the backup types and the three-two-one rule, and the two numbers that '
    'drive every recovery design: RTO and RPO.'),
 ('bullets',
  {'kick': '10E · Resiliency',
   'title': 'Resiliency & Availability',
   'items': ['Availability — a CIA pillar, measured as uptime and MTBF',
             'Redundancy — RAID storage, NIC teaming, dual power supplies',
             'Load balancing — distribute traffic across healthy servers',
             'Failover — automatic switch to standby on failure',
             'HA clusters — linked servers that share the workload',
             'The goal — no single point of failure and minimal interruption'],
   'note': 'Availability is a business contract.'},
  'Availability is a confidentiality, integrity and availability pillar and a business contract, '
  'measured as uptime percentage and mean time between failures. A system at ninety-nine point '
  'nine percent uptime is down about eight point seven six hours a year. Redundancy removes single '
  'points of failure: redundant array of independent disks storage, network interface card teaming '
  'and dual power supplies. Load balancing spreads traffic across healthy servers, and automatic '
  'failover switches to a standby on failure. High-availability clusters keep the service up '
  'through failures, not just recover after them. The goal: no single point of failure and minimal '
  'interruption.'),
 ('table',
  {'kick': '10E · Resiliency',
   'title': 'Backup Types & Strategy',
   'headers': ['Backup', 'What it stores', 'Trade-off'],
   'rows': [['Full', 'Everything, every time', 'Slowest to take, simplest to restore'],
            ['Incremental', 'Changes since the last backup', 'Fast backups, slow restore chain'],
            ['Differential', 'Changes since the last full', 'Faster restore than incremental'],
            ['3-2-1 rule', '3 copies, 2 media, 1 off-site', 'Survives site loss']]},
  'The backup table. Full: everything, every time, slowest to take but simplest to restore. '
  'Incremental: changes since the last backup, fast backups but a slow restore chain that must '
  'apply the last full and every subsequent incremental. Differential: changes since the last '
  'full, faster to restore than incremental because it needs only the last full and the most '
  'recent differential. And the three-two-one rule: three copies, two media, one off-site. That '
  'last copy survives site loss, which is what makes it count.'),
 ('bullets',
  {'kick': '10E · Resiliency',
   'title': 'RTO and RPO',
   'items': ['RTO — recovery time objective: maximum acceptable downtime',
             'RPO — recovery point objective: maximum acceptable data loss',
             'Shorter RTO — needs real-time replication or redundant systems',
             'Shorter RPO — needs more frequent backups, such as hourly',
             'The tension — tighter targets cost more in storage and capacity',
             'The exam line — RPO is data; RTO is time'],
   'note': 'Two numbers drive the design.'},
  'Two numbers drive the design. RTO, the recovery time objective, is the maximum acceptable '
  'downtime: how fast must we be back? A short RTO demands redundant systems or real-time '
  'replication. RPO, the recovery point objective, is the maximum acceptable data loss: how '
  'much can we afford to lose? A short RPO demands frequent backups, perhaps hourly. The '
  'tension: tighter targets cost more in storage, capacity and replication. The exam line: RPO '
  'is data; RTO is time.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Activity',
   'title': 'Design the backup plan',
   'body': 'A database that cannot lose more than 15 minutes of data — RPO 15 minutes, so frequent '
           'transaction logs. A branch back online in 4 hours — RTO 4 hours, so a warm standby. A '
           'full backup restores fastest. Off-site copies survive site loss.'},
  'Let us design a backup plan. A database that cannot lose more than fifteen minutes of data: '
  'an RPO of fifteen minutes, so frequent transaction logs. A branch that must be '
  'back online in four hours: an RTO of four hours, so a warm standby rather than a '
  'cold site you must rebuild. Which backup restores fastest? A full, because it needs no restore '
  'chain. What survives a fire in the server room? The off-site copy, which is the third of the '
  'three-two-one rule.'),
 ('chapter',
  {'num': 4,
   'of': 5,
   'title': 'Site Security & Assets',
   'blurb': 'Physical, environmental, and the asset lifecycle'},
  'Chapter four is site security and asset management. All the logical controls in the world mean '
  'nothing if the rack walks out the door. You will learn the physical controls that protect the '
  'perimeter, the environmental controls that keep the room survivable, and the data destruction '
  'and inventory discipline that close the asset lifecycle.'),
 ('bullets',
  {'kick': '10F · Site Security',
   'title': 'Physical Security — the First Line',
   'items': ['Perimeter — fences, gates, vehicle barriers',
             'Doors — locks, mantraps, badge readers, biometric access',
             'Monitoring — surveillance cameras and on-site response',
             'The rule — defence in depth applies to buildings too',
             'The gap — logical controls mean nothing if the rack walks out'],
   'note': 'Physical is the first line, not the last.'},
  'Physical security is the first line, not the last. Perimeter: fences, gates and vehicle '
  'barriers. Doors: locks, mantraps, badge readers and biometric access. Monitoring: surveillance '
  'cameras and on-site response keep an eye on the whole perimeter. The rule: defence in depth '
  'applies to buildings too, with multiple layers rather than one locked door. The gap: all your '
  'logical controls mean nothing if the rack walks out the door.'),
 ('bullets',
  {'kick': '10F · Site Security',
   'title': 'Environmental Controls',
   'items': ['Fire — suppression: gas systems such as FM-200, not just water',
             'Climate — cooling and humidity control keep hardware in spec',
             'Power — UPS for short gaps, generators for long outages',
             'Managed power — distribution monitors usage and flags failures',
             'The goal — the room survives what the building throws at it'],
   'note': 'Each is an availability control with a physical body.'},
  'The room must survive what the building throws at it. Fire suppression: gas systems such as '
  'FM-200 or inert gas protect electronics where water would destroy them. Climate: cooling and '
  'humidity management keep hardware within specification, preventing overheating, static and '
  'condensation. Power: an uninterruptible power supply bridges short gaps with battery power, and '
  'generators take over for long outages. Managed power distribution monitors usage and flags '
  'failures. Each is an availability control with a physical body.'),
 ('bullets',
  {'kick': '10F · Site Security',
   'title': 'Data Destruction & Asset Management',
   'items': ['Destruction — overwrite, degauss, shred or cryptoshred',
             'Verify — confirm data cannot be recovered after disposal',
             'Inventory — know every asset, its location and its owner',
             'Lifecycle — acquire, assign, track, retire, destroy',
             'Chain of custody — records of transfer and disposal',
             'The leak — a discarded drive is a data breach waiting'],
   'note': 'The end of the lifecycle matters as much as the start.'},
  'The end of the lifecycle matters as much as the start. Destruction: overwrite the data, degauss '
  'magnetic media, shred or crush the device, or cryptoshred the keys, so the data is gone and not '
  'just the label. Then verify the data cannot be recovered, and keep chain of custody records of '
  'transfer and disposal for compliance. Inventory: know every asset, its location and its owner. '
  'Lifecycle: acquire, assign, track, retire, destroy. The leak: a discarded drive is a data '
  'breach waiting to happen.'),
 ('chapter',
  {'num': 5, 'of': 5, 'title': 'Consolidation', 'blurb': 'Key takeaways and what to revise'},
  'Chapter five is consolidation. We bring the session together into the key takeaways you should '
  'carry forward, and the revision checklist that turns this session into long-term recall.'),
 ('recap',
  {'title': 'Key Takeaways',
   'items': ['Scan, assess, remediate, verify — the vulnerability loop never stops',
             'Severity is not risk — exposure and exploitability decide priority',
             'Unpatched needs a plan — compensate, accept with an owner, or fix',
             'Resiliency is availability — RTO, RPO, backups, redundancy',
             'Physical is security — site, environment, destruction, inventory']},
  'Five takeaways. One: scan, assess, remediate, verify; the loop never stops. Two: severity is '
  'not risk; exposure and exploitability decide priority. Three: unpatched needs a plan; '
  'compensate, accept with an owner, or fix. Four: resiliency is availability; RTO, '
  'RPO, backups, redundancy. Five: physical is security; site, '
  'environment, destruction, inventory.'),
 ('bullets',
  {'kick': 'Consolidation',
   'title': 'Revision Checklist',
   'items': ['Retake the session quiz until you score well without guessing',
             'Map your RTO and RPO for one critical service you depend on',
             'Audit a backup and test a restore — untested backups are hopes',
             'Read ahead to Session 11: security operations, monitoring and incident response'],
   'note': 'This video is one revision pass — the quiz is the recall test.'},
  'Before you move on, make the learning stick. Retake the session quiz until you score well '
  'without guessing. Map your RTO and RPO for one '
  'critical service you depend on. Audit a backup and test a restore, because untested backups are '
  'hopes, not plans. And read ahead to Session 11: security operations, monitoring and incident '
  'response. This video is one revision pass — the quiz is where you prove you can recall it.'),
 ('statement',
  {'kick': 'Next',
   'title': 'Session 11 — Security Operations: Monitoring, Incident Response & Forensics',
   'body': 'Watching, responding and proving — the operational core. Monitoring and alerting, the '
           'incident response lifecycle, and forensics: evidence, chain of custody and timelines.'},
  'That closes Session Ten. You can now find the holes with scanning, CVSS '
  'and prioritisation, fix them with patching and compensating controls, and survive what '
  'gets through with backups, redundancy and site security. Retake the session quiz until you '
  'score seventy percent without guessing. Resiliency is what keeps the business standing when a '
  'control fails.')]

if __name__ == "__main__":
    total = sum(len(f[2].split()) for f in FRAMES)
    print("Session 10 narration: %d frames, %d words (~~%d min at 163 wpm)"
          % (len(FRAMES), total, round(total / 163)))

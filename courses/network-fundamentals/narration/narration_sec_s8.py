# narration_sec_s8.py — Security+ SY0-701 (revised), Session 8
# "Enterprise Network Security: Firewalls, IDS, IPS, VPNs & Secure Protocols"
# One-video-per-lesson format. Each frame: (template, payload, narration).
# Narration is read ALOUD IN FULL by ElevenLabs (Billy's voice) — short
# sentences that stand alone without the visual. Abbreviations are written
# so the engine reads them the way they are spoken in the classroom.
# USER RULES: no "good morning" (use "good day"); no courseware timing
# references — only the video's own length may be mentioned.

DECK = 'Enterprise Network Security: Firewalls, IDS, IPS, VPNs & Secure Protocols'
SESSION = 'Session 8 · Security+ SY0-701 (revised)'

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
   'of': 4,
   'title': 'Architecture & Segmentation',
   'blurb': 'Tiered, spine-leaf, VLANs, DMZ and the appliance stack'},
  'Good day, and welcome to Session Eight of the combined Network Fundamentals and CompTIA '
  'Security+ course. This session is Enterprise Network Security. Sessions one to three gave you '
  'the network foundation — addressing, switching, services. Sessions four to seven gave you the '
  'security core — concepts, threats, cryptography, identity. Now we put it all together: the '
  'appliances and protocols that defend an enterprise network. Keep the scenario mindset, because '
  'the exam describes a situation and asks you to pick the control. We begin with architecture and '
  'segmentation.'),
 ('statement',
  {'kick': 'The Journey',
   'title': 'The Shape of the Session',
   'body': 'Architecture and segmentation first, then the appliance stack — firewalls, IDS/IPS, '
           'proxies, WAF, NAC — then secure remote access with VPN and ZTNA, and the secure '
           'protocol toolkit that carries traffic safely.'},
    'Here is the shape of the session. We start with architecture and segmentation — how the network is built and how it is divided into zones. Then the appliance stack: firewalls, intrusion detection and prevention, proxies, web application firewalls, and network access control. Then secure remote access — the virtual private network types, zero trust network access, and how to make remote desktop safe. And finally, the secure protocol toolkit: transport layer security, secure shell, internet protocol security, and the rest. Defence in depth runs through all of it. No single layer carries the whole burden.'),
 ('bullets',
  {'kick': 'The Journey',
   'title': 'Session Objectives',
   'items': ['Describe tiered, spine-leaf and SMB architectures',
             'Explain VLANs, DMZ and microsegmentation as containment',
             'Classify firewalls, IDS/IPS, proxy, WAF, load balancer, NAC',
             'Compare IDS and IPS — detect versus prevent',
             'Explain VPN types, ZTNA and RDP security',
             'Pick the right secure protocol for the job'],
   'note': 'Scenario questions reward exactly this: pick the appliance and the protocol.'},
  'By the end of this session you will be able to do ten things. First, describe the architectures — '
    'tiered, spine-leaf, and the small business model. Second, explain virtual local area networks, '
    'the demilitarised zone, and microsegmentation as containment controls. Third, classify the '
    'appliances — firewalls, intrusion detection and prevention, proxies, web application firewalls, '
    'load balancers, and network access control. Fourth, compare intrusion detection with intrusion '
    'prevention. Fifth, explain network access control posture checking. Sixth, describe the virtual '
    'private network types. Seventh, explain zero trust network access and secure access service edge. '
    'Eighth, describe transport layer security versions, cipher suites, perfect forward secrecy, and '
    'certificate validation. Ninth, state the jobs of the secure protocols. And tenth, explain remote '
    'desktop risk and the controls that make remote access safe. The quiz tests every one of these.'),
 ('bullets',
  {'kick': 'Architecture',
   'title': 'Campus Network Architecture',
   'items': ['Tiered: core (fast transport) → distribution (policy) → access (endpoints)',
             'Spine-leaf: data-centre fabric — every leaf to every spine, low latency',
             'SMB: flat, single-layer — fewer devices, simpler policy',
             'Redundancy: duplicate paths and devices — no single point of failure',
             'The choice: scale, budget, reliability and control drive the model'],
   'note': 'Redundancy is the companion to reliability.'},
  'Architecture first. The tiered model has three layers. The core provides fast transport. The '
  'distribution layer applies policy. The access layer connects the endpoints. Spine-leaf is the '
  'data-centre fabric, where every leaf connects to every spine for low latency. The small '
  'business model is flat and single-layer — fewer devices, simpler policy. Redundancy matters '
  'too: duplicate paths and devices, so a single failure does not bring the network down. The '
  'choice of model is driven by scale, budget, reliability and control needs.'),
 ('bullets',
  {'kick': 'Architecture',
   'title': 'Segmentation',
   'items': ['VLANs: logical separation within a switch — zones with rules',
             'DMZ: a buffer zone — twin firewalls shield internal from public services',
             'Microsegmentation: fine-grained isolation, even within a workload',
             'Least connectivity: only necessary connections between segments',
             'The benefit: a compromise in one segment does not spread'],
   'note': 'Segmentation is containment.'},
    'Segmentation is containment. Virtual local area networks — vlans for short — separate traffic logically within a switch. Different zones, different rules. The demilitarised zone, or D M Z, is a buffer zone between the internet and the internal network, ringed by two firewalls. An external one guards the demilitarised zone itself. An internal one shields the local area network from anything that breaks in. Microsegmentation goes further, isolating even within a single workload. And least connectivity means you allow only the connections you actually need. The benefit: a compromise in one segment does not spread everywhere.'),
 ('table',
  {'kick': 'Appliances',
   'title': 'Appliances at a Glance',
   'headers': ['Appliance', 'Role'],
   'rows': [['Firewall', 'Filters traffic by rules; stateless, stateful or NGFW'],
            ['IDS / IPS', 'Detects suspicious traffic; IPS actively blocks inline'],
            ['Proxy', 'Intermediary — forwards requests; filters, caches, hides topology'],
            ['WAF', 'Protects web apps from application-layer attacks (SQLi, XSS)'],
            ['Load balancer', 'Distributes traffic across servers; health checks; redundancy']]},
    'The appliance table is your anchor. Firewalls filter traffic by rules — stateless, stateful, or next-generation. Intrusion detection and intrusion prevention — I D S and I P S for short — detect suspicious traffic, and the prevention system actively blocks it inline. Proxies sit in the middle, forwarding requests, filtering, caching, and hiding the internal topology. The web application firewall, or W A F, protects web applications from application-layer attacks like structured query language injection and cross-site scripting. And load balancers spread traffic across servers with health checks, giving you redundancy.'),
 ('bullets',
  {'kick': 'Appliances',
   'title': 'Firewalls in Depth',
   'items': ['Stateless: packet filtering by IP, port, protocol — fast, no context',
             'Stateful: state table tracks connections — allows established flows',
             'NGFW: application awareness, deep packet inspection, IPS, threat intel',
             'UTM: unified threat management — one box for SMBs',
             'Rule management: change control and regular review keep rules tight'],
   'note': 'They differ by how much they remember and inspect.'},
    'Four firewall flavours, and they differ by how much they remember and inspect. Stateless packet filtering checks each packet alone — source, destination, port, protocol. It is fast, but it has no context. Stateful inspection keeps a state table and tracks each connection, so established flows are allowed through sensibly. The next-generation firewall, or N G F W, adds application awareness and deep packet inspection, plus intrusion prevention and threat intelligence. It understands what an application is doing, not just which port it uses. And unified threat management — U T M — bundles all of it into one box for small and medium businesses. Keep firewall rules tight too. Change control and regular review stop an old rule from becoming a back door.'),
 ('bullets',
  {'kick': 'Appliances',
   'title': 'IDS vs IPS',
   'items': ['IDS: watches, alerts, logs — passive, no direct action',
             'IPS: watches AND blocks inline — drops packets, resets sessions',
             'Detection: signature (known) and anomaly (deviation) and behavioural',
             'Deployment: network-based (gateway) or host-based (per device)',
             'Tuning: balance sensitivity against false positives',
             'Placement: IPS inline; IDS can be inline or port-mirrored'],
   'note': 'Detection tells you what happened; prevention stops it happening.'},
    'Here is the exam distinction. Intrusion detection — the I D S — watches, alerts, and logs. It is passive, and takes no direct action. Intrusion prevention — the I P S — watches and blocks inline. It is active, and can drop malicious packets, block an offending address, or reset a session. On detection methods: signature-based catches known attack patterns, but misses new ones. Anomaly-based builds a baseline and flags deviations, so it can find the unknown, at the cost of more false positives. Both deploy network-based at the gateway, or host-based on individual devices. Tuning matters too. Set sensitivity too high, and alerts overwhelm you. Set it too low, and genuine threats slip past. And placement: the I P S must be inline, while the I D S can be inline, or fed by port mirroring. Detection tells you what happened. Prevention stops it happening.'),
 ('statement',
  {'kick': 'Appliances',
   'title': 'Activity: Place the Appliance',
   'body': 'Which appliance inspects application-layer web attacks? The WAF. Which blocks '
           'malicious traffic inline? The IPS. Which should not be a single point of failure? The '
           'load balancer. Which hides the internal topology? The proxy.'},
    'Let us place the appliances. Which appliance inspects application-layer web attacks? The W A F. Which blocks malicious traffic inline? The I P S. Which should not be a single point of failure? The load balancer, which needs its own redundancy. Which hides the internal topology? The proxy. And the deeper question: what happens when each of these fails? That is exactly how exam scenarios are written.'),
 ('callout',
  {'kind': 'info',
   'label': "Analyst's Lens",
   'title': 'Place the appliance by the job',
   'body': 'Web application attacks → WAF. Malicious traffic to block inline → IPS. Never a single '
           'point of failure → load balancer. Hide the internal topology → proxy.'},
    'How do you place the appliance? Match it to the job. Application-layer web attacks — the W A F. Malicious traffic you need to block inline — the I P S. Something that must never be a single point of failure — the load balancer, which needs its own redundancy. Hiding the internal topology — the proxy. When you can name what each appliance does, when it acts, and where it sits, you can answer the scenario questions.'),
 ('bullets',
  {'kick': 'Appliances',
   'title': 'Network Access Control',
   'items': ['The idea: endpoints prove posture before joining',
             'Checks: antivirus status, OS patches, encryption, user credentials',
             'Outcomes: allow, quarantine to a restricted segment, or deny',
             'Guest access: portal-based onboarding for unknown devices',
             'The exam line: only compliant devices reach sensitive resources'],
   'note': 'Prove you are healthy before I trust you.'},
    'Network access control — N A C for short, pronounced nack — is the posture gate. Endpoints must prove their health before joining the network. The controller assesses antivirus status, operating system updates, encryption, and user credentials. The outcomes: allow, quarantine to a restricted segment until the device complies, or deny outright. Guest access is handled through portal-based onboarding for unknown devices. The network asks: prove you are healthy before I trust you. And only compliant devices reach sensitive resources.'),
 ('callout',
  {'kind': 'warn',
   'label': 'Security Lens',
   'title': 'Segment by trust, not by convenience',
   'body': 'Smart building sensors have weak patching, default credentials and no authentication. '
           'Compromised, they become pivot points into the whole LAN. IoT is untrusted by '
           'default.'},
    'Why do smart building sensors belong on their own vlan? Because they have weak patching, default credentials, and no authentication. If they are compromised, they become pivot points into the whole local area network. Segment by trust, not by convenience. Internet of things devices are untrusted by default, so they get their own segment. A compromise there stays there.'),
 ('chapter',
  {'num': 2,
   'of': 4,
   'title': 'Secure Remote Access',
   'blurb': 'VPN types, RDP controls, ZTNA and SASE'},
    'Now we move from the inside of the network to getting in from the outside. Chapter two is secure remote access. Remote access is a target, so every path in needs authentication, encryption, and monitoring. You will learn the virtual private network flavours, how to lock down remote desktop, and the modern shift to zero trust network access.'),
 ('bullets',
  {'kick': 'Remote Access',
   'title': 'Remote Access Essentials',
   'items': ['VPN: encrypted tunnel over an untrusted network',
             'RDP: powerful and frequently attacked — secure it or disable it',
             'The rule: every remote path needs authentication, encryption, monitoring',
             'Jump servers: controlled entry points, heavily monitored and hardened',
             'Bastion hosts: internet-exposed hosts designed to withstand attack'],
   'note': 'Sensitive systems are never directly reachable.'},
    'Remote access is a target. The virtual private network is an encrypted tunnel over an untrusted network. Remote desktop protocol — R D P for short — is powerful and frequently attacked. Secure it, or disable it. The rule: every remote path needs authentication, encryption, and monitoring. And think about how administrators get in. Jump servers provide a controlled, heavily monitored entry point into the network. Bastion hosts sit exposed to the internet, hardened and designed to withstand attack. The result: sensitive systems are never directly reachable.'),
 ('table',
  {'kick': 'Remote Access',
   'title': 'VPN Flavours',
   'headers': ['Type', 'What it is'],
   'rows': [['Site-to-site', 'Connects whole networks — branch to HQ, often IPsec tunnel mode'],
            ['Remote access', 'Connects individual users to the network'],
            ['Client-based', 'Software on the user device (often IPsec)'],
            ['SSL VPN', 'Browser-based or TLS — no client install'],
            ['Split tunnel', 'Only some traffic goes through the tunnel; the rest is direct']]},
    'Five virtual private network flavours in the table. Site-to-site connects whole networks — branch to headquarters — and often runs internet protocol security, or I P sec, in tunnel mode, wrapping the whole packet. Remote access connects individual users to the network. Client-based runs software on the user device, again often I P sec. The Secure Sockets Layer virtual private network — the SSL V P N — is browser-based, or runs over transport layer security. No client install, which makes it ideal for contractors. And split tunnel sends only some traffic through the tunnel; the rest goes direct. That is convenient, but it does not protect everything.'),
 ('bullets',
  {'kick': 'Remote Access',
   'title': 'Zero Trust Network Access',
   'items': ['ZTNA: per-request verification — no implicit network trust',
             'SASE: ZTNA + SD-WAN delivered as a service',
             'The shift: from location-based to identity- and posture-based access',
             'The outcome: the network becomes irrelevant to trust decisions'],
   'note': 'Trust follows the user and the device, not the IP.'},
    'Zero trust network access, or Z T N A, is per-request verification, with no implicit network trust. Secure access service edge — SASE, pronounced sassy — delivers zero trust network access, plus a software-defined wide area network, or SD wide area network, as a service. The shift is from location-based access to identity-based and posture-based access. The outcome: the network becomes irrelevant to trust decisions. Trust follows the user and the device, not the internet protocol address.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Lockdown Activity',
   'title': 'Secure the remote path',
   'body': 'RDP that must stay enabled: add MFA, firewall allowlists, patching and monitoring. '
           'Branch users: site-to-site VPN. Browser-only contractor: SSL VPN. The non-negotiable '
           'control is MFA.'},
    'Let us lock down remote access. If remote desktop protocol must stay enabled for one administrator, add multi-factor authentication, or M F A, plus firewall allowlists, patching, and monitoring. Branch users who need the headquarters systems get a site-to-site V P N. A contractor who needs browser-only access gets an SSL V P N. And the non-negotiable control across all of them is M F A.'),
 ('chapter',
  {'num': 3,
   'of': 4,
   'title': 'The Secure Protocol Toolkit',
   'blurb': 'TLS, HTTPS, SSH, IPsec, S/MIME and DNSSEC'},
    'Chapter three is the secure protocol toolkit. These are the protocols that protect data in transit. The workhorse is transport layer security — T L S for short — which carries web, email, and file transfer. You will learn how the handshake works, how certificates defeat man-in-the-middle attacks, and how to match each protocol to its job.'),
 ('bullets',
  {'kick': 'Protocols',
   'title': 'TLS in Depth',
   'items': ['The handshake: authenticate the server, agree keys and algorithms, then encrypt',
             'Cipher suites: the negotiated algorithm bundle — strength matters',
             'Versions: TLS 1.2/1.3 current; SSL and TLS 1.0/1.1 are dead',
             'PFS: ephemeral keys — past traffic stays secret',
             'Coverage: web, email, and file transfer all ride on TLS'],
   'note': 'When you see HTTPS, FTPS or SMTPS, you are seeing TLS underneath.'},
    'T L S is the workhorse that protects data in transit across the web, email, and file transfer. The handshake authenticates the server, agrees the encryption keys and algorithms, and then encrypts. Cipher suites are the negotiated algorithm bundle, and strength matters. Versions: T L S one point two and one point three are current, while SSL, T L S one point zero, and T L S one point one are dead. Perfect forward secrecy uses ephemeral keys, so past traffic stays secret even if a key leaks. When you see hypertext transfer protocol secure, or H T T P S, file transfer protocol secure, or F T P S, or simple mail transfer protocol secure, or S M T P S, you are seeing T L S underneath.'),
 ('bullets',
  {'kick': 'Protocols',
   'title': 'HTTPS and Certificates',
   'items': ['HTTPS: HTTP over TLS — the non-negotiable default',
             'Validation: chain, hostname, expiry, revocation — against a trusted CA',
             'The aim: defeat man-in-the-middle by confirming who you really speak to',
             'HSTS: tells browsers to refuse plaintext connections',
             'The exam line: no HTTPS, no trust'],
   'note': 'Certificate validation is what defeats the impostor.'},
    'H T T P S is hypertext transfer protocol over T L S — the non-negotiable default. Certificate validation checks the chain of trust, the hostname, the expiry, and the revocation status, against a trusted certificate authority. That validation is what defeats a man-in-the-middle attack. It confirms you are speaking to the server you think you are, not an impostor. Hypertext transfer protocol strict transport security, or H S T S, tells browsers to refuse plaintext connections entirely. The exam line: no H T T P S, no trust.'),
 ('table',
  {'kick': 'Protocols',
   'title': 'The Secure Protocol Toolkit',
   'headers': ['Protocol', 'Job'],
   'rows': [['TLS / HTTPS', 'Transport encryption for web and APIs'],
            ['SSH / SFTP', 'Secure remote administration and file transfer'],
            ['IPsec', 'Network-layer encryption for VPNs (tunnel mode)'],
            ['S/MIME', 'Email signing and encryption'],
            ['DNSSEC', 'DNS response integrity'],
            ['FTPS', 'FTP wrapped in TLS for secure transfers']]},
    'Match the protocol to the job. T L S and H T T P S: transport encryption for web and APIs. Secure shell, or S S H, and secure file transfer protocol, or S F T P: secure remote administration and file transfer. I P sec: network-layer encryption for virtual private networks, in tunnel mode for whole networks. Secure multipurpose internet mail extensions, or S MIME: email signing and encryption. Domain name system security extensions, or D N S E C: domain name system response integrity. And F T P S wraps file transfer protocol in T L S for secure transfers. When a scenario says web traffic, you say T L S. Remote administration, S S H. Virtual private network, I P sec. Email, S MIME.'),
 ('chapter',
  {'num': 4, 'of': 4, 'title': 'Consolidation', 'blurb': 'Key takeaways and what to revise'},
  'Chapter four is consolidation. We bring the session together into the key takeaways you should '
  'carry forward, and the revision checklist that turns this session into long-term recall.'),
 ('recap',
  {'title': 'Key Takeaways',
   'items': ['Architecture shapes defence — tiered and spine-leaf define where policy lives',
             'Segmentation contains breaches — VLANs, DMZ and microsegmentation stop lateral '
             'spread',
             'Appliances inspect and block — firewalls, IDS/IPS, proxies, WAF, load balancers',
             'NAC enforces posture — endpoints prove health before they join',
             'Remote access is a target — VPN, ZTNA and SASE, always authenticated, encrypted, '
             'monitored']},
    'Five takeaways. One: architecture shapes defence — tiered and spine-leaf define where policy lives. Two: segmentation contains breaches — vlans, the D M Z, and microsegmentation stop lateral spread. Three: appliances inspect and block — firewalls, I D S and I P S, proxies, W A F s, and load balancers. Four: nack enforces posture — endpoints prove their health before they join. Five: remote access is a target — V P N, zero trust network access, and sassy — always authenticated, encrypted, and monitored.'),
 ('bullets',
  {'kick': 'Consolidation',
   'title': 'Revision Checklist',
   'items': ['Retake the session quiz until you score well without guessing',
             'Draw a zone diagram — DMZ, internal, management — for a network you know',
             'Match the protocols — TLS, SSH, IPsec, S/MIME, DNSSEC — to their jobs',
             'Read ahead to Session 9: endpoint, application, cloud and virtualisation'],
   'note': 'This video is one revision pass — the quiz is the recall test.'},
    'Before you move on, make the learning stick. Retake the session quiz until you score well without guessing. Draw a zone diagram — D M Z, internal, management — for a network you know. Match the protocols — T L S, S S H, I P sec, S MIME, D N S E C — to their jobs. And read ahead to Session 9, where we cover endpoint, application, cloud, and virtualisation security. This video is one revision pass. The quiz is where you prove you can recall it.'),
 ('statement',
  {'kick': 'Next',
   'title': 'Session 9 — Endpoint, Application, Cloud & Virtualisation Security',
   'body': 'Harden the hosts — OS, EDR, mobile. Secure the code — the SDLC and application '
           'attacks. Move to the cloud — service models, shared responsibility and the '
           'hypervisor.'},
  'That closes Session Eight. You can now explain on-premises architecture models and '
  'segmentation, switching, routing and security appliances, network access control, and secure '
  'remote access and tunnelling. Retake the session quiz until you score seventy percent without '
  'guessing. This is where the identity you have learned to manage meets the network that carries '
  'it.')]

if __name__ == "__main__":
    total = sum(len(f[2].split()) for f in FRAMES)
    print("Session 8 narration: %d frames, %d words (~~%d min at 163 wpm)"
          % (len(FRAMES), total, round(total / 163)))

# narration_sec_s9.py — Security+ SY0-701 (revised), Session 9
# "Endpoint, Application, Cloud & Virtualisation Security"
# One-video-per-lesson format. Each frame: (template, payload, narration).
# Narration is read ALOUD IN FULL by ElevenLabs (Billy's voice) — short
# sentences that stand alone without the visual. Abbreviations are written
# so the engine reads them the way they are spoken in the classroom.
# USER RULES: no "good morning" (use "good day"); no courseware timing
# references — only the video's own length may be mentioned.

DECK = 'Endpoint, Application, Cloud & Virtualisation Security'
SESSION = 'Session 9 · Security+ SY0-701 (revised)'

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
   'title': 'Endpoint Security',
   'blurb': 'Protection stack, hardening, app control, mobile management'},
  'Good day, and welcome to Session Nine of the combined Network Fundamentals and CompTIA '
  'Security+ course. Session Eight secured the network boundary. In this video we defend the '
  'assets themselves: the hosts, the code they run, and the cloud and virtualised estate that '
  'hosts so much of it. The thread that runs through everything is asset first: for every asset, '
  'name the control. We begin with the endpoint, the device that touches your network.'),
 ('statement',
  {'kick': 'The Journey',
   'title': 'Defence beyond the network',
   'body': 'Session 8 secured the boundary. Today: the hosts, the code and the cloud. Every layer '
           'carries its own controls, none trusted alone.'},
  'Here is the shape of this video. Session Eight gave us the appliances and protocols at the '
  'boundary. Now we cover endpoint protection and management, the application lifecycle and secure '
  'coding, application-layer attacks, and cloud and virtualisation security. The thread: every '
  'layer needs its own controls, and none is trusted alone. And the exam line: pick the control '
  'for the asset, not the product.'),
 ('bullets',
  {'kick': 'The Journey',
   'title': 'Session Objectives',
   'items': ['Explain endpoint protection — hardening, EDR, app control',
             'Describe mobile management — MDM, BYOD and mobile threats',
             'Secure the SDLC — DevSecOps and secure coding',
             'Describe app attacks — injection, XSS, CSRF',
             'Explain cloud security — models, shared responsibility',
             'Secure virtualisation — hypervisors, containers'],
   'note': 'Six objectives — the quiz at the end tests every one.'},
  'By the end of this video you will be able to tackle eleven objectives. One: describe the '
  'endpoint protection stack — antivirus and endpoint detection and response, hardening, '
  'patching, and application control. Two: explain allowlisting versus blocklisting, and why '
  'allowlisting wins. Three: describe mobile device management, bring your own device models, '
  'and mobile threats, including remote wipe and containerisation. Four: explain operating '
  'system security controls — least privilege, secure boot, and full disk encryption. Five: '
  'describe security in the software development lifecycle — shift left, threat modelling, code '
  'review, and static and dynamic application security testing. Six: explain DevSecOps and the '
  'continuous integration, continuous delivery security pipeline. Seven: describe the '
  'application attacks — injection, cross-site scripting, cross-site request forgery, buffer '
  'overflow, directory traversal, and race conditions — and their fixes. Eight: explain the '
  'cloud deployment and service models: infrastructure, platform, and software as a service, '
  'and public, private, and hybrid. Nine: explain the shared responsibility model, and where '
  'the line falls for each service model. Ten: describe cloud risks, especially '
  'misconfiguration, and the tools that manage them. Eleven: explain virtualisation security — '
  'hypervisor attacks, virtual machine escape, and container isolation. Eleven objectives, and '
  'the quiz at the end tests every one of them.'),
 ('bullets',
  {'kick': 'Topic 9A',
   'title': 'Endpoint Protection',
   'items': ['The endpoint — any device that touches the network',
             'Antivirus and EDR — signature detection plus behaviour monitoring',
             'The gap — signatures miss unknown threats, behaviour catches them',
             'The stack — AV/EDR, host firewall, hardening, patching, app control'],
   'note': 'Detection is a stack, not a single product.'},
  'The endpoint is any device that touches the network, whatever its role: laptop, phone, '
  'server, or sensor. The protection stack has five parts. First, antivirus and endpoint '
  'detection and response — EDR — signature detection plus behaviour monitoring. Then a host '
  'firewall, hardening, patching, and application control. Here is the gap: signatures only '
  'name what they have already seen, so unknown threats slip through. Behaviour monitoring '
  'watches what a process does, not what it is called, and that catches what signatures cannot '
  'name.'),
 ('bullets',
  {'kick': 'Topic 9A',
   'title': 'Hardening the Endpoint',
   'items': ['Baseline — a documented secure configuration from a known state',
             'Sources — CIS benchmarks and vendor hardening guides',
             'Patch management — close the known holes first, then verify',
             'Disable what you do not use — services, ports, default accounts',
             'The test — would a default install fail your policy?'],
   'note': 'Reduce the attack surface, then prove it.'},
  'Hardening starts with a baseline: a documented secure configuration that puts the system in '
  'a known secure state. You can build that baseline from Center for Internet Security '
  'benchmarks and vendor hardening guides. Patch management closes the known holes first, then '
  'you verify the fix. Disable what you do not use — services, ports, and default accounts — '
  'which all reduce the attack surface. And the test: would a default install fail your '
  'policy? If it would pass, you are not hardened.'),
 ('bullets',
  {'kick': 'Topic 9A',
   'title': 'Application Control',
   'items': ['Allowlisting — only pre-approved software runs',
             'Blocklisting — known bad software is denied',
             'Code signing — verify origin and integrity before execution',
             'The modern choice — allowlisting wins, blocklists miss unknowns',
             'The benefit — malware cannot execute if it is not approved'],
   'note': 'Allowlisting beats blocklisting for unknown threats.'},
  'Two approaches to controlling what runs. Allowlisting: only pre-approved software runs. '
  'Blocklisting: known bad software is denied. A supporting control is code signing, which '
  'verifies the origin and integrity of software before it executes, so a tampered binary is '
  'rejected. The modern choice is allowlisting, because blocklists miss the unknowns. Malware '
  'cannot execute if it is not approved in the first place.'),
 ('bullets',
  {'kick': 'Topic 9A',
   'title': 'Mobile Device Management',
   'items': ['MDM — enrol, configure, enforce, wipe centrally',
             'BYOD — personal devices carrying corporate data',
             'Application vetting — assess, comply and check reputation before install',
             'Containers — separate work and personal data on the device',
             'The controls — remote wipe, encryption, jailbreak detection'],
   'note': 'The device is managed, never blindly trusted.'},
  'Mobile device management — MDM — enrols, configures, enforces, and can centrally wipe '
  'devices. Bring Your Own Device, or BYOD, brings personal devices carrying corporate data. '
  'So you vet the applications before they install, and you answer with containers: work and '
  'personal data separated on the device. The controls are remote wipe, encryption, and '
  'jailbreak detection. The device is managed, never blindly trusted. Weigh BYOD against '
  'corporate-owned devices; the latter give you more control over configuration and compliance.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Activity',
   'title': 'Secure the fleet',
   'body': "A laptop runs an unknown executable: allowlisting stops it. A manager's phone holds "
           'corporate mail: MDM with containers fits BYOD. Guest and IoT devices stay off the '
           'domain. Patching is the baseline every endpoint needs.'},
  'Let us apply this to a fleet. A laptop runs an unknown executable — allowlisting stops it. A '
  "manager's phone holds corporate mail — MDM with containers fits BYOD. Which device should "
  'never join the domain? Guest and Internet of Things devices stay off. And the one control '
  'every endpoint needs is patching, the baseline. The exam angle: the question about which '
  'control stops an unknown executable tests allowlisting, not signature updates.'),
 ('bullets',
  {'kick': 'Topic 9A',
   'title': 'Operating System Security',
   'items': ['User accounts — least privilege, no admin by default',
             'Secure boot — verified boot chain blocks tampered firmware',
             'Full disk encryption — protects data at rest on lost media',
             'Firmware updates — close hardware-level vulnerabilities',
             'The habit — update, reboot, verify'],
   'note': 'The OS layer sits below every application.'},
  'Now the operating system layer. User accounts: least privilege, no admin by default. Secure '
  'boot: a verified boot chain that blocks tampered firmware from loading at startup. Full disk '
  'encryption: data at rest stays unreadable if the drive walks away. Firmware updates close '
  'vulnerabilities below the operating system, which candidates often overlook. And the habit: '
  'update, reboot, verify.'),
 ('callout',
  {'kind': 'warn',
   'label': 'Discussion',
   'title': 'Your AV never fired',
   'body': 'A workstation was compromised and the antivirus stayed silent. Signatures miss '
           'zero-days. Behaviour monitoring, allowlisting and patching would have caught or '
           'prevented it.'},
  'Here is the discussion. Your antivirus never fired, yet a workstation was compromised. What '
  'went wrong? Signatures miss unknown threats. Behaviour monitoring, allowlisting and patching '
  'would have caught it or prevented it. Detection is a stack, not a single product, so you layer '
  'the controls. And ask the deeper question: which data state — at rest, in transit, or in use — '
  'went unprotected on that workstation?'),
 ('chapter',
  {'num': 2,
   'of': 5,
   'title': 'The Application Lifecycle',
   'blurb': 'Security in the SDLC and DevSecOps'},
  'Now we move from the host to the code that runs on it. Chapter two is the application '
  'lifecycle: how security moves into the software development lifecycle — the SDLC — and how '
  'DevSecOps makes it part of the pipeline, rather than a gate at the end. The theme is shift '
  'left: find the flaw early, when it costs the least.'),
 ('bullets',
  {'kick': 'Topic 9B',
   'title': 'Security in the SDLC',
   'items': ['Shift left — security from the first design, not the last test',
             'Threat modelling — find the attack surface before code exists',
             'Code review — human and automated checks at every change',
             'Testing — SAST for source, DAST for running apps',
             'Input validation — whitelisting, sanitisation and boundary checks'],
   'note': 'The later you find a flaw, the more it costs.'},
  'Shift left: security from the first design, not the last test. Threat modelling finds the '
  'attack surface before the code exists. Code review, human and automated, happens at every '
  'change. Secure coding adds least privilege for the code itself, error handling that leaks '
  'nothing, and input validation using whitelisting, sanitisation and boundary checks. And '
  'testing: static application security testing — SAST — for the source, and dynamic '
  'application security testing — DAST — for the running application. The later you find a '
  'flaw, the more it costs.'),
 ('bullets',
  {'kick': 'Topic 9B',
   'title': 'DevSecOps',
   'items': ['The idea — security is part of the pipeline, not a gate',
             'CI/CD — every build is scanned and tested automatically',
             'Infrastructure as code — scan templates, manage secrets centrally',
             'The failure mode — security bolted on at the end',
             'The outcome — secure code ships as fast as insecure code'],
   'note': 'The checks run continuously, so nothing waits at release.'},
  'DevSecOps makes security part of the pipeline, not a gate at the end. In Continuous '
  'Integration and Continuous Delivery — CI/CD — every build is scanned and tested '
  'automatically. Infrastructure as Code — IaC — is in scope too: scan your templates and '
  'manage secrets centrally, rather than leaving keys in configuration files. The failure '
  'mode is security bolted on at release. The outcome: secure code ships as fast as insecure '
  'code, because the checks run continuously.'),
 ('chapter',
  {'num': 3,
   'of': 5,
   'title': 'Application Attacks',
   'blurb': 'Injection, XSS, CSRF and the pattern behind them'},
  'Chapter three is where the code meets the attacker. We cover the classic application '
  'attacks: Structured Query Language injection — SQL, pronounced sequel — cross-site '
  'scripting, or XSS, and cross-site request forgery, or CSRF, pronounced c-surf. Then the '
  'supporting cast: buffer overflow, directory traversal, and race conditions. And we close '
  'with the pattern that defends against most of them: input validation and least privilege.'),
 ('bullets',
  {'kick': 'Topic 9C',
   'title': 'SQL Injection',
   'items': ['The flaw — user input treated as part of the query',
             'The impact — read, modify or delete database data',
             'The classic fix — parameterised queries, input is data not code',
             'Input validation — whitelist, sanitise and bound every field',
             'The test — any input field is a potential injection point'],
   'note': 'Input is data, never code.'},
  'The classic application attack. The flaw: user input is treated as part of the query. The '
  'impact: an attacker reads, modifies or deletes database data. The classic fix: parameterised '
  'queries, so input is data and never code. Back that with input validation on every field: '
  'whitelist, sanitise and bound the input. And the test mindset: any input field is a potential '
  'injection point.'),
 ('bullets',
  {'kick': 'Topic 9C',
   'title': 'XSS and CSRF',
   'items': ["XSS — attacker script runs in another user's browser",
             "CSRF — forged request rides a victim's session",
             'The fixes — output encoding, same-site cookies, tokens',
             'Defence — a WAF filters and monitors web traffic',
             'The difference — XSS hijacks the browser; CSRF hijacks the action'],
   'note': 'Two attacks, two targets.'},
  "Two attacks, two targets. XSS: attacker script runs in another user's browser. CSRF, "
  "pronounced c-surf: a forged request rides a victim's session. The fixes: output encoding, "
  'same-site cookies, and tokens. A web application firewall — WAF — adds defence by filtering '
  'and monitoring web traffic. And the difference: XSS hijacks the browser, while c-surf '
  'hijacks the action.'),
 ('bullets',
  {'kick': 'Topic 9C',
   'title': 'More Application Attacks',
   'items': ['Buffer overflow — excess input overwrites memory',
             'Directory traversal — dot dot slash escapes the web root',
             'Race condition — timing gap between check and use',
             'Sandboxing — isolate risky code to contain any compromise',
             'The pattern — input validation and least privilege'],
   'note': 'Contain the compromise, then fix the input.'},
  'Three more. Buffer overflow: excess input overwrites memory. Directory traversal: dot dot slash '
  'escapes the web root. Race condition: a timing gap between check and use. Add sandboxing: '
  'isolate risky code so a compromise is contained rather than reaching the whole system. And the '
  'pattern across all of them: input validation and least privilege.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Activity',
   'title': 'Find the flaw',
   'body': "A login field accepts ' OR 1=1: SQL injection. A script tag in another user's browser: "
           'XSS. A forged form submission on a logged-in session: CSRF. Two fixes cover most: '
           'parameterised queries and output encoding.'},
  'Let us classify the flaws. A login field accepts quote, space, OR, one equals one: that is '
  "sequel injection. A script tag appears in another user's browser: that is XSS. A forged "
  'form submission uses a logged-in session: that is c-surf. And the two fixes that cover most '
  'of these are parameterised queries and output encoding. The exam may present the symptom '
  'and ask for the fix, so match the attack to the countermeasure.'),
 ('chapter',
  {'num': 4,
   'of': 5,
   'title': 'Cloud & Virtualisation',
   'blurb': 'Service models, shared responsibility, and the virtual estate'},
  'Chapter four takes the same asset-first thinking into the cloud and the virtualised estate. You '
  'will learn the service and deployment models, the shared responsibility line that the exam '
  'loves, the number one cloud risk of misconfiguration, and how to secure the hypervisor and the '
  'containers that run on it.'),
 ('table',
  {'kick': 'Topic 9D',
   'title': 'Cloud Deployment & Service Models',
   'headers': ['Model', 'What it means'],
   'rows': [['IaaS', 'VMs, storage, network. You secure everything above the hypervisor'],
            ['PaaS', 'Platform provided. You secure the app and its data'],
            ['SaaS', 'Software delivered. The vendor secures nearly everything'],
            ['Public / private / hybrid', 'Who owns and operates the infrastructure'],
            ['Community cloud', 'Shared by organisations with common needs']]},
  'The cloud models. Infrastructure as a Service — IaaS: virtual machines, storage, and '
  'network, so you secure everything above the hypervisor. Platform as a Service — PaaS: the '
  'platform is provided, so you secure the application and its data. Software as a Service — '
  'SaaS: the software is delivered, so the vendor secures nearly everything. Then the '
  'deployment models: public, private, hybrid, and community. They tell you who owns and '
  'operates the infrastructure, and each shifts the shared responsibility line in a slightly '
  'different way.'),
 ('bullets',
  {'kick': 'Topic 9D',
   'title': 'Shared Responsibility',
   'items': ['The vendor — secures the cloud, the infrastructure underneath',
             'The customer — secures what is in the cloud, config, data, access',
             'The line moves — IaaS you secure the guest; SaaS the vendor does more',
             'Community cloud — responsibilities shared across members and provider',
             'The exam line — misunderstanding the line is a failing answer'],
   'note': 'You secure what is in the cloud, never assume.'},
  'This is the exam core. The vendor secures the cloud, the infrastructure underneath. The '
  'customer secures what is in the cloud: configuration, data, access. The line moves: with IaaS '
  'you secure the guest, with SaaS the vendor does more. Deployment models matter too — in a '
  'community cloud, responsibilities are shared among the member organisations and the provider. '
  'Misunderstanding the line is a failing answer, so know where it falls for each model.'),
 ('bullets',
  {'kick': 'Topic 9D',
   'title': 'Misconfiguration is the Number One Cloud Risk',
   'items': ['The cause — defaults, open buckets, permissive policies',
             'The exposure — data leaks reachable from the internet',
             'The tooling — CASB, posture management, policy as code',
             'IaC guardrails — scan templates and check compliance automatically',
             'The habit — assume misconfiguration until proven otherwise'],
   'note': 'Not exotic attacks — misconfiguration.'},
  'The number one cloud risk is not an exotic attack — it is misconfiguration. Defaults left '
  'in place, storage buckets left open, policies too permissive. The exposure: data leaks '
  'reachable from the internet. The tooling: a cloud access security broker — CASB — cloud '
  'security posture management, and policy as code. With IaC, scan your templates and check '
  'compliance automatically before anything is deployed. And the habit: assume misconfiguration '
  'until proven otherwise.'),
 ('bullets',
  {'kick': 'Topic 9D',
   'title': 'Securing the Virtual Estate',
   'items': ['Hypervisor — separates the VMs, attack it and you own all',
             'Type 1 vs Type 2 — bare metal is smaller and safer than hosted',
             'VM escape — breaking out of the guest into the host',
             'Containers — share the kernel, isolate with namespaces and seccomp',
             'The controls — patch the hypervisor, least privilege, network isolation'],
   'note': 'The hypervisor is the crown jewel.'},
  'Virtualisation changes the attack surface. The hypervisor separates the virtual machines — '
  'the VMs — so attack it, and you own everything on it. Hypervisor types matter: a '
  'bare-metal Type 1 hypervisor has a smaller attack surface than a hosted Type 2 that '
  'depends on an operating system. VM escape: breaking out of the guest into the host. '
  'Containers share the kernel, so isolation needs namespaces and seccomp. The controls: patch '
  'the hypervisor, apply least privilege, and isolate the network.'),
 ('chapter',
  {'num': 5, 'of': 5, 'title': 'Consolidation', 'blurb': 'Key takeaways and what to revise'},
  'Chapter five is consolidation. We bring the session together into the key takeaways you should '
  'carry forward, and the revision checklist that turns this video into long-term recall.'),
 ('recap',
  {'title': 'Key Takeaways',
   'items': ['Endpoints need a stack — AV/EDR, hardening, patching, app control',
             'Mobile is managed, not trusted — MDM, containers and remote wipe',
             'Secure code shifts left — threat modelling, review, SAST/DAST in the pipeline',
             'Injection is input as code — parameterised queries and output encoding',
             'Cloud is shared responsibility — you secure what is in the cloud, never assume']},
  'Five takeaways. One: endpoints need a stack — antivirus and EDR, hardening, patching, and '
  'app control. Two: mobile is managed, not trusted — MDM, containers, and remote wipe. Three: '
  'secure code shifts left — threat modelling, review, and SAST and DAST in the pipeline. '
  'Four: injection is input as code — parameterised queries and output encoding. Five: cloud '
  'is shared responsibility — you secure what is in the cloud, and you never assume.'),
 ('bullets',
  {'kick': 'Consolidation',
   'title': 'Revision Checklist',
   'items': ['Retake the quiz until you score 70% without guessing',
             'Audit an app — find one input field and its validation',
             'Map the responsibility line for a SaaS and an IaaS you use',
             'Classify the data — label a sample by type and state',
             'Read ahead to Session 10: vulnerability management'],
   'note': 'This video is one revision pass — the quiz is the recall test.'},
  'Before you move on, make the learning stick. Retake the quiz until you score seventy percent '
  'without guessing. Audit an application: find one input field and its validation. Map the '
  'responsibility line for a SaaS and an IaaS you use. Classify the data: label a sample by type '
  'and state. And read ahead to Session Ten, vulnerability management, resiliency and asset '
  'protection. This video is one revision pass — the quiz is where you prove you can recall it.'),
 ('statement',
  {'kick': 'Next',
   'title': 'Session 10 — Vulnerability Management, Resiliency & Asset Protection',
   'body': 'We find the holes: scanning, CVSS, prioritisation. We fix them: patching, compensating '
           'controls, disclosure. And we survive what gets through: backups, redundancy and site '
           'security.'},
  'That closes Session Nine. You can now harden hosts, secure the code through the SDLC, and '
  'move to the cloud with service models, shared responsibility, and the hypervisor. Retake '
  'the session quiz until you score seventy percent without guessing. Endpoint, application, '
  'cloud, and virtualisation are where the controls you have learned are actually deployed.')]

if __name__ == "__main__":
    total = sum(len(f[2].split()) for f in FRAMES)
    print("Session 9 narration: %d frames, %d words (~~%d min at 163 wpm)"
          % (len(FRAMES), total, round(total / 163)))

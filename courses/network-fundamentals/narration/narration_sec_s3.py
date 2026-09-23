# narration_sec_s3.py — Security+ SY0-701 (revised), Session 3
# "Network Services & the Attack Surface"
# One-video-per-lesson format. Each frame: (template, payload, narration).
# Narration is read ALOUD IN FULL by ElevenLabs (Billy's voice) — short
# sentences that stand alone without the visual. Abbreviations are written
# so the engine reads them the way they are spoken in the classroom.
# USER RULES: no "good morning" (use "good day"); no courseware timing
# references — only the video's own length may be mentioned.

DECK = 'Network Services & the Attack Surface'
SESSION = 'Session 3 · Security+ SY0-701 (revised)'

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
   'title': 'The Services & the Attack Surface',
   'blurb': 'DNS, DHCP, NTP and SSH — and how each becomes a way in'},
  'Good day, and welcome to Session Three of the combined Network Fundamentals and CompTIA '
  'Security+ course. Sessions one and two built the map and the roads — models, addressing, '
  'switching. This session completes the network foundation. We meet the services that make '
  'networks usable: the Domain Name System, or DNS; the Dynamic Host Configuration Protocol, or '
  'DHCP; the Network Time Protocol, or NTP; and Secure Shell, or SSH — and the attacks that target '
  'each one. Keep one pattern in your head for the whole video: every service has a purpose, an '
  'attack, and a command that verifies it.'),
 ('statement',
  {'kick': 'The Foundation',
   'title': 'The Foundation Is Complete',
   'body': 'Session 1: models and IP addressing. Session 2: switching, VLANs and architectures. '
           'Session 3: the services that run on top of it all. Every service is also an attack '
           'surface.'},
  'Here is where we stand. Session one covered models and Internet Protocol, or IP, addressing. '
  'Session two covered switching, Virtual Local Area Networks, or VLANs, and architectures. This session covers the '
  'services that run on top of all of it — and that closes the network-foundation strand. From '
  'here onward, we study security itself. And the pattern for this video: every service is also an '
  'attack surface. An attack surface is the sum of entry points an attacker can use to enter or '
  'extract data. Every service you run adds to it.'),
 ('bullets',
  {'kick': 'The Foundation',
   'title': 'Session Objectives',
   'items': ['Explain DNS — hierarchy, records and resolution',
             'Describe DNS attacks — poisoning, tunnelling, amplification',
             'Explain DHCP — the DORA process and lease timers',
             'Describe DHCP attacks — rogue servers and starvation',
             'Explain NTP and SSH — time integrity and secure access',
             'Verify services on Kali — dig, ntpq, ss, journalctl'],
   'note': 'Six objectives — the quiz at the end tests every one.'},
  'By the end of this video you will be able to explain the DNS hierarchy — root, top-level '
  'domains, authoritative servers and recursive resolvers — and name the common record types and '
  'their purposes. You will describe DNS cache poisoning, tunnelling and amplification, and the '
  'role of Domain Name System Security Extensions, or DNSSEC. You will explain the DHCP DORA '
  'process — Discover, Offer, Request, Acknowledge — and the T one and T two lease timers, '
  'and describe rogue servers and starvation and how DHCP snooping counters them. You will explain '
  'NTP\'s stratum hierarchy and why accurate time matters to forensics, and describe NTP '
  'amplification and spoofing and their mitigations. You will explain SSH connection establishment '
  'and key-based authentication, and list the core hardening settings. And you will use dig, ntpq, '
  'ss and journalctl to verify services and read evidence on Kali, and explain how closing unused '
  'services and hardening reduce the attack surface. Eleven objectives, and the quiz at the end '
  'tests every one of them.'),
 ('statement',
  {'kick': 'The Foundation',
   'title': 'The Attack Surface',
   'body': 'The sum of entry points an attacker can use to enter or extract data. Every service '
           'you run adds to it — and every service is also a way in.'},
  'Before we meet the services, hold the central idea. An attack surface is the sum of entry '
  'points an attacker can use to enter or extract data from your environment. Every service you '
  'run adds to it. And every service is also a way in — a path an attacker can reach. So the '
  "analyst's job is not just to run services, but to know what each one exposes, and to close what "
  'is not needed. That is the lens for the rest of this video.'),
 ('chapter',
  {'num': 2,
   'of': 5,
   'title': "DNS — the Internet's Directory",
   'blurb': 'Hierarchy, record types, and the attacks that poison the trust anchor'},
  "Chapter two is the Domain Name System, or DNS — the internet's directory. It "
  'translates human-readable names into addresses, and almost everything depends on it: web '
  'browsing, email, software updates. You will learn the hierarchy, the record types, and the '
  'attacks that turn this trusted directory against you.'),
 ('bullets',
  {'kick': 'Topic 3A · DNS',
   'title': "DNS: the Internet's Directory",
   'items': ['Purpose — translate names to addresses',
             'Dependency — browsing, email, updates all use it',
             'Hierarchy — root, TLD, authoritative, recursive',
             'The catch — everyone trusts the answer, until it is poisoned',
             'DNS spoofing — an on-path attacker forges a reply mid conversation',
             'Threat vector — DNS outbound is almost never blocked'],
   'note': 'DNS is the trust anchor of the internet.'},
  'DNS translates names into addresses. The hierarchy runs from the root, down to the top-level '
  'domains, then to the authoritative servers that own each domain, and finally to the recursive '
  'resolvers that query on your behalf. And here is the catch: everyone trusts the answer — until '
  'it is poisoned. DNS spoofing is an on-path attacker forging a reply mid-conversation. And the '
  'threat vector matters: DNS outbound is almost never blocked, so it carries attacks out of your '
  'network.'),
 ('table',
  {'kick': 'Topic 3A · DNS',
   'title': 'DNS Record Types',
   'headers': ['Type', 'Purpose'],
   'rows': [['A', 'Name to IPv4 address'],
            ['AAAA', 'Name to IPv6 address'],
            ['CNAME', 'Alias for another name'],
            ['MX', 'Mail exchange server'],
            ['NS', 'Authoritative name server'],
            ['TXT', 'SPF, DKIM, DMARC text records'],
            ['PTR', 'Reverse lookup — IP to name']]},
  'The record types are the vocabulary of DNS. A maps a name to an IP version four address. Quad A '
  'maps a name to an IP version six address. C name is an alias for another name. M X is the mail '
  'exchange server. N S names the authoritative name server. T X T carries Sender Policy '
  'Framework, or SPF; DomainKeys Identified Mail, or DKIM; and Domain-based Message Authentication, '
  'Reporting and Conformance, or DMARC, text records. And P T R does the reverse — IP back to '
  'name. You will meet all of these again in mail security and in logs.'),
 ('bullets',
  {'kick': 'Topic 3A · DNS',
   'title': 'DNS Attacks',
   'items': ['Cache poisoning — forged responses redirect users',
             'DNS tunnelling — data exfiltrated inside queries',
             'Amplification — small queries, huge responses, DDoS',
             'DNSSEC — cryptographic signing stops the forgery',
             'Attack surface — open recursive resolvers are free amplifiers',
             'The fix — close resolvers, DNSSEC validation, log queries'],
   'note': 'Spoofing forges one reply; poisoning plants it in the cache for everyone.'},
  "Three attacks dominate. Cache poisoning: forged responses are inserted into a resolver's cache, "
  'redirecting every user who asks — the highest-impact scenario, because one poisoned cache '
  'serves many victims. DNS tunnelling: data is encoded inside queries to exfiltrate it past '
  'firewalls that allow DNS out. Amplification: tiny queries with spoofed sources draw huge '
  'responses — a DDoS engine powered by open resolvers, which is why you never run an open '
  'recursive resolver. And the defence: Domain Name System Security Extensions, or DNSSEC, '
  'cryptographically signs the answers so forgery fails. Remember the exam distinction: '
  'spoofing forges a single reply; poisoning puts that forgery into the cache for everyone.'),
 ('callout',
  {'kind': 'info',
   'label': "Analyst's Lens",
   'title': 'Which DNS attack shows up first in your logs?',
   'body': 'Poisoning — users redirected to unexpected IPs. Tunnelling — many tiny queries to one '
           'name from one host. Amplification — a flood of large responses from a single server.'},
  'Which DNS attack would you spot first in your logs? Poisoning shows as users redirected to '
  "unexpected IPs — check the resolver's cache against known answers. Tunnelling shows as many "
  'tiny queries to one name from one host. Amplification shows as a flood of large responses from '
  'a single server. DNS is the trust anchor of the internet — poisoning it redirects everyone who '
  'asks.'),
 ('chapter',
  {'num': 3,
   'of': 5,
   'title': 'DHCP — Automatic Addressing',
   'blurb': 'The DORA process, lease timers, and the rogue server on your LAN'},
  'Chapter three is the Dynamic Host Configuration Protocol, or DHCP — the service that automates '
  'address assignment. You will learn the DORA process — Discover, Offer, Request, Acknowledge — '
  'the lease timers, and the two attacks that turn this convenience into a way in: the rogue '
  'server and starvation.'),
 ('bullets',
  {'kick': 'Topic 3B · DHCP',
   'title': 'DHCP: Automatic Addressing',
   'items': ['Purpose — assign IP, mask, gateway, DNS automatically',
             'DORA — Discover, Offer, Request, Ack',
             'Lease timers — T1 at 50%, T2 at 87.5%, then renewal',
             'Scope design — exclusions reserve servers and routers',
             'The trust problem — clients accept the first offer they receive',
             'Attack surface — an unauthorised server on the LAN wins the race'],
   'note': 'A client trusts the first offer it receives.'},
  'DHCP automates address assignment. The DORA process: Discover — the client broadcasts for an '
  'address. Offer — a server offers one. Request — the client accepts. Acknowledge — the server '
  'confirms the lease. Then the timers: T one at fifty percent of the lease, when the client tries '
  'to renew; T two at eighty-seven point five percent, when it broadcasts for any server. And '
  'scope design: exclusions reserve addresses for servers, routers and printers. Now the security '
  'catch, and it matters: a client trusts the first offer it receives. So an unauthorised server '
  'on the LAN wins the race and becomes your gateway.'),
 ('bullets',
  {'kick': 'Topic 3B · DHCP',
   'title': 'DHCP Attacks',
   'items': ['Rogue server — assigns a malicious gateway or DNS',
             'Starvation — spoofed MACs exhaust the address pool',
             'DHCP snooping — switch filters, trusts only known ports',
             'The result — man-in-the-middle or denial of service',
             'The chain — a rogue gateway enables interception of all traffic',
             'The defence — snooping plus port security restrict the LAN'],
   'note': 'A rogue gateway sits on every conversation.'},
  'Two attacks and one defence. The rogue server: an attacker on the network answers Discover with '
  'a malicious gateway or DNS server — a man-in-the-middle setup. Follow the chain: a rogue gateway '
  'does not just assign addresses, it sits on every conversation, so all traffic can be '
  'intercepted or altered. Starvation: spoofed MAC addresses exhaust the address pool — a denial '
  'of service. And the defence: DHCP snooping on the switch, which trusts only authorised ports '
  'and builds a MAC-to-IP-to-port binding table that also blocks spoofing. Pair it with port '
  'security and segmentation, so a rogue server is contained to one segment instead of the whole '
  'LAN.'),
 ('callout',
  {'kind': 'warn',
   'label': 'Security Lens',
   'title': 'The rogue gateway is a man-in-the-middle',
   'body': 'It does not just assign addresses — it sits on every conversation, so all traffic can '
           'be intercepted or altered. DHCP snooping plus port security contain it to one '
           'segment.'},
  'Why does the rogue server matter so much? Because a rogue gateway is a man-in-the-middle. It '
  'does not just assign addresses — it sits on every conversation, so all traffic can be '
  'intercepted or altered. That is why the defence is layered: DHCP snooping on the switch trusts '
  'only authorised ports, and port security plus segmentation contain a rogue server to one '
  'segment instead of the whole LAN.'),
 ('chapter',
  {'num': 4,
   'of': 5,
   'title': 'NTP & SSH — Time and the Doorway',
   'blurb': 'The clock everyone trusts, and the secure management channel'},
  'Chapter four covers two services that matter more than they look: the Network Time Protocol, or '
  'NTP, the clock everyone trusts, and Secure Shell, or SSH, the secure management channel. One '
  'keeps evidence honest; the other is the doorway into your systems.'),
 ('bullets',
  {'kick': 'Topic 3C · NTP',
   'title': 'NTP: the Clock Everyone Trusts',
   'items': ['Purpose — synchronise clocks to UTC',
             "UDP 123 — the protocol's well-known port",
             'Stratum — 0 atomic, 1 direct, 2 onward',
             'Forensics — logs, tokens and timelines need accurate time',
             'The dependency — Kerberos tickets expire against wrong clocks',
             'The exam line — an unknown clock offset corrupts evidence'],
   'note': 'Accurate time is infrastructure, not a convenience.'},
  'NTP synchronises clocks to Coordinated Universal Time, or UTC, over UDP port one two three. The '
  'hierarchy runs in strata: stratum zero is the atomic clock or GPS source; stratum one servers '
  'sync directly to it; stratum two syncs to stratum one, and so on. And the forensic angle: '
  'authentication tokens, certificate validation, log correlation and timeline reconstruction all '
  'depend on accurate time. A clock that drifts corrupts evidence. Add the operational angle too: '
  'Kerberos tickets and many authentication systems reject requests when the clock is wrong, so a '
  'badly drifted server quietly breaks logins. Accurate time is infrastructure, not a '
  'convenience.'),
 ('bullets',
  {'kick': 'Topic 3C · NTP',
   'title': 'NTP Attacks and Verification',
   'items': ['Amplification — monlist requests fuel DDoS attacks',
             'Spoofing — shifted time corrupts logs and tokens',
             'The fix — authenticated NTP, restricted access',
             'Verify on Kali — ntpq -p, timedatectl, journalctl'],
   'note': 'A small monlist request can draw a response a hundred times larger.'},
  'Two attacks. Amplification: a small monlist request with a spoofed source draws a response up '
  'to a hundred times larger — fuel for DDoS, and it powered some of the largest on record. '
  'Spoofing: if an attacker shifts system time, tokens expire, logs misalign, timelines break. The '
  'fixes: authenticated NTP and restricted server access. And verification on '
  'Kali: ntpq -p shows peers and offset; timedatectl shows the clock; journalctl reads the NTP '
  'events.'),
 ('bullets',
  {'kick': 'Topic 3D · SSH',
   'title': 'SSH: the Secure Management Channel',
   'items': ['Purpose — encrypted remote access, replaces Telnet',
             'TCP 22 — the well-known port',
             'Key exchange — Diffie-Hellman derives the session key',
             'Authentication — password or public key, keys win',
             'The threat — exposed port 22 draws constant brute force',
             'The answer — keys, restricted users, strict logging'],
   'note': 'Keys are never transmitted and resist brute force.'},
  'SSH provides encrypted remote access, replacing Telnet, rlogin and clear-text File Transfer '
  'Protocol, or FTP. It runs on TCP port twenty-two. Connection establishment: TCP handshake, '
  'version exchange, key exchange — Diffie-Hellman derives a shared session key without sending '
  'it — then host key verification, and authentication by password or public key. Keys win: they are never transmitted and resist '
  'brute force. And the threat: an exposed port twenty-two draws constant brute force, so the '
  'answer is keys, restricted users and strict logging.'),
 ('table',
  {'kick': 'Topic 3D · SSH',
   'title': 'SSH Hardening',
   'headers': ['Setting', 'Value', 'Why'],
   'rows': [['PermitRootLogin', 'no', 'Stop root brute force'],
            ['PasswordAuthentication', 'no', 'Force key-based auth'],
            ['LogLevel', 'VERBOSE', 'Capture key and session detail'],
            ['AllowUsers', 'admin analyst', 'Restrict who may connect'],
            ['ClientAliveInterval', '300', 'Kill idle sessions']]},
  'The hardening table is directly examinable. PermitRootLogin no — stop root brute force. '
  'PasswordAuthentication no — force key-based auth. LogLevel verbose — capture key and session '
  'detail. AllowUsers admin analyst — restrict who may connect. ClientAliveInterval three hundred '
  '— kill idle sessions. Five settings that turn SSH from a doorway into a guarded gate. Notice '
  'the pattern: each setting shrinks the attack surface. Removing password auth denies brute force '
  'entirely; restricting users denies everyone else. The exam loves presenting an SSH config and '
  'asking which line stops password guessing — it is PasswordAuthentication no.'),
 ('callout',
  {'kind': 'ok',
   'label': "Analyst's Lens",
   'title': 'Hardening shrinks the attack surface',
   'body': 'Removing password auth denies brute force entirely; restricting users denies everyone '
           'else. Each setting closes a class of attack before it starts.'},
  'Notice the pattern across all five settings: each one shrinks the attack surface. Removing '
  'password authentication denies brute force entirely — there is nothing to guess. Restricting '
  'users denies everyone else before they even try. And verbose logging means that when someone '
  'does connect, you capture the key and session detail. Hardening is not a list of chores — it is '
  'closing whole classes of attack before they start.'),
 ('chapter',
  {'num': 5,
   'of': 5,
   'title': 'Verification & Consolidation',
   'blurb': "Reading the services' truth on Kali, and the key takeaways"},
  'Chapter five is where the theory becomes practice. We verify every service on Kali Linux, read '
  'the evidence the logs produce, and then bring the whole session together into the key takeaways '
  'you should carry forward.'),
 ('bullets',
  {'kick': 'Kali Linux · Verification',
   'title': 'Verifying Services on Kali',
   'items': ['DNS — dig bbc.co.uk +short, cat /etc/resolv.conf',
             'DHCP — cat /var/lib/dhcp/dhclient.leases',
             'NTP — ntpq -p, timedatectl, journalctl -u ntp',
             'SSH — ss -tnp | grep :22, grep sshd /var/log/auth.log',
             'Services — ss -tuln shows what is listening',
             'The audit — explain every listener or you have a gap'],
   'note': 'An analyst should be able to explain every listener on the box.'},
  'Here are the commands that verify each service. DNS: dig bbc.co.uk plus short, and cat '
  '/etc/resolv.conf. DHCP: cat /var/lib/dhcp/dhclient.leases shows the lease history. NTP: ntpq '
  '-p, timedatectl, and journalctl -u ntp. SSH: ss -tnp with grep for port twenty-two, and grep '
  'sshd in /var/log/auth.log. And the master command: ss -tuln shows '
  'everything listening. An analyst should be able to explain every listener on the box — if you '
  'cannot, that is a gap.'),
 ('bullets',
  {'kick': 'Kali Linux · Forensics',
   'title': 'Reading the Evidence',
   'items': ["Failed passwords — grep 'Failed password' /var/log/auth.log | wc -l",
             'Accepted logins — grep Accepted /var/log/auth.log',
             "SSH sessions — ss -tunap | grep -E ':(22|53|123)'",
             'The analyst habit — correlate SSH and xrdp times, users, flows',
             'The red flag — an unexpected listening port is compromise'],
   'note': 'Every exposed service widens the attack surface.'},
  'Now the forensic commands. The failed password count: grep Failed password in '
  '/var/log/auth.log, piped to wc -l — that is the brute-force volume. Accepted logins: grep '
  'Accepted in the same log. Active sessions: ss -tunap with grep for ports twenty-two, '
  'fifty-three and one two three. The analyst habit: correlate SSH and xrdp session times with '
  'user accounts and network flows for a complete picture. And the red flag: an unexpected '
  'service listening on a high port is an indicator of compromise. Every exposed service widens '
  'the attack surface, and the logs tell you who is knocking.'),
 ('recap',
  {'title': 'Key Takeaways',
   'items': ['DNS is the trust anchor — poisoning redirects everyone; DNSSEC signs the answers',
             'DHCP must be controlled — rogue servers and starvation, and snooping filters both',
             'Time is forensic — NTP amplification and spoofing corrupt evidence',
             'SSH is the doorway — keys over passwords, VERBOSE logging, restrict users',
             "Kali verifies — dig, ntpq, ss and journalctl read the services' truth"]},
  'Five takeaways. One: DNS is the trust anchor — poisoning redirects everyone, and DNSSEC signs '
  'the answers. Two: DHCP must be controlled — rogue servers and starvation, and snooping filters '
  'both. Three: time is forensic — NTP amplification and spoofing corrupt evidence. Four: SSH is '
  'the doorway — keys over passwords, verbose logging, restricted users. Five: Kali verifies — '
  "dig, ntpq, ss and journalctl read the services' truth."),
 ('bullets',
  {'kick': 'Consolidation',
   'title': 'Revision Checklist',
   'items': ['Retake the quiz until you score 70%+ without guessing',
             'Run the commands — dig, ntpq, ss on any Linux box',
             'Audit an SSH config against the hardening table',
             'Read ahead — Session 4: fundamental security concepts'],
   'note': 'This video is one revision pass — the quiz is the recall test.'},
  'Before you move on, make the learning stick. Retake the quiz until you score seventy percent or '
  'better without guessing. Run the commands — dig, ntpq, ss — on any Linux box you can reach. '
  'Audit an SSH config against the hardening table. And read ahead to Session 4, where the '
  'Security+ core begins: fundamental security concepts. This video is one revision pass — the '
  'quiz is where you prove you can recall it.'),
 ('statement',
  {'kick': 'Next',
   'title': 'Session 4 — Fundamental Security Concepts',
   'body': 'The Security+ core begins: the CIA triad, non-repudiation, the AAA framework, security '
           'controls, and the NIST Cybersecurity Framework.'},
  'That closes Session Three, and with it the network-foundation strand. You can now explain the '
  'services that carry traffic, the attacks that target them, and how every service you run adds '
  'to your attack surface. Retake the session quiz until you score seventy percent without '
  'guessing. From here, the course turns to security itself, and the ground you have built is what '
  'that study stands on.')]

if __name__ == "__main__":
    total = sum(len(f[2].split()) for f in FRAMES)
    print("Session 3 narration: %d frames, %d words (~~%d min at 163 wpm)"
          % (len(FRAMES), total, round(total / 163)))

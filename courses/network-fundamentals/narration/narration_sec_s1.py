# narration_sec_s1.py — Security+ SY0-701 (revised), Session 1
# "Network Foundations: Networking Models & IP Addressing"
# One-video-per-lesson format. Each frame: (template, payload, narration).
# Narration is read ALOUD IN FULL by ElevenLabs (Billy's voice) — short
# sentences that stand alone without the visual. Abbreviations are written
# so the engine reads them the way they are spoken in the classroom.
# USER RULES: no "good morning" (use "good day"); no courseware timing
# references — only the video's own length may be mentioned.

DECK = 'Network Foundations: Networking Models & IP Addressing'
SESSION = 'Session 1 · Security+ SY0-701 (revised)'

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
   'title': 'Models & the Journey of Data',
   'blurb': 'OSI, TCP/IP, encapsulation and addressing at each layer'},
  'Good day, and welcome to Session One of the combined Network Fundamentals and CompTIA Security+ '
  'course. The first three sessions build your network foundation: how data moves, how devices are '
  'addressed, and which services carry the traffic. Everything after that — threats, cryptography, '
  'network security, operations — assumes you can read a network like a map. This session is where '
  'you learn to read the map. We begin with the models that organise how data travels, and the '
  'addressing that gives every layer its own identity.'),
 ('statement',
  {'kick': 'The Journey',
   'title': 'The Shape of the Course',
   'body': 'Network foundation first, then the security core, then architecture, then operations '
           'and governance. Every later session assumes you can read a network like a map.'},
  'Here is the shape of the course. Sessions one to three are the network foundation — models, '
  'addressing, switching, services. Sessions four to seven are the security core — fundamental '
  'concepts, threats, cryptography, identity. Sessions eight and nine are security architecture — '
  'network, endpoint, application, cloud. Sessions ten to twelve are operations and governance — '
  'vulnerability management, incident response, and compliance. Hold that map in your head, '
  'because each block builds on the last.'),
 ('bullets',
  {'kick': 'The Journey',
   'title': 'Session Objectives',
   'items': ['Explain the OSI model and map TCP/IP onto it',
             'Describe encapsulation and the packet at each layer',
             'Calculate subnet boundaries with CIDR and VLSM',
             'Explain how subnets become security zones',
             'Describe IPv6 and the risk of running both stacks'],
   'note': 'Seven objectives — the quiz at the end tests every one.'},
  'By the end of this session you will be able to name the seven layers of the open systems '
  'interconnection model — the OSI model — and state the role and a representative protocol for '
  'each. You will map the four-layer transmission control protocol over internet protocol stack — '
  'TCP/IP — onto that model. You will describe encapsulation, and name the protocol data unit — '
  'the PDU — at each layer: the segment, the packet, and the frame. You will state the purpose of '
  'port, internet protocol and media access control — MAC — addressing, and where each is used. '
  'You will explain internet protocol version four — IP version four — address structure, '
  'including the network and host split and subnet masks. You will describe classful addressing, '
  'and why classless inter-domain routing — CIDR, pronounced cedar — replaced it. You will '
  'calculate subnet counts and usable hosts using the two formulas. You will design a variable '
  'length subnet masking — VLSM — scheme, allocating the largest requirements first without '
  'overlap. You will explain how subnet segmentation acts as a security control, limiting the '
  'attack surface and lateral movement. You will write and shorten internet protocol version six — '
  'IP version six — addresses using the two shorthand rules, and distinguish the four address '
  'types. And you will explain the security risk of running both stacks at once. Twelve '
  'objectives, and the quiz at the end tests every one of them.'),
 ('bullets',
  {'kick': 'Models',
   'title': 'The OSI Model — Seven Layers',
   'items': ['7 Application — HTTP, DNS, SSH',
             '6 Presentation — encoding, encryption',
             '5 Session — dialog control',
             '4 Transport — end-to-end delivery, ports',
             '3 Network — logical addressing, routing',
             '2 Data link — frames, MAC addresses, switching',
             '1 Physical — bits, cables, signals'],
   'note': 'OSI is the map; TCP/IP is the road you actually drive.'},
  'The OSI model organises networking into seven layers. Layer seven, application — the services '
  'your software uses, such as hypertext transfer protocol, or HTTP; domain name system, or DNS; '
  'and secure shell, or SSH. Layer six, presentation — encoding and encryption. Layer five, session '
  '— dialog control between hosts. Layer four, transport — end-to-end delivery and ports. Layer '
  'three, network — logical addressing and routing. Layer two, data link — frames, MAC addresses '
  'and switching. Layer one, physical — bits, cables and signals. OSI is the map. The road you '
  'actually drive is the TCP/IP stack.'),
 ('table',
  {'kick': 'Models',
   'title': 'The TCP/IP Stack — Four Layers',
   'headers': ['TCP/IP', 'OSI', 'Examples'],
   'rows': [['Application', '5–7', 'HTTP, DNS, SSH, SMTP'],
            ['Transport', '4', 'TCP, UDP'],
            ['Internet', '3', 'IP, ICMP, ARP'],
            ['Network Access', '1–2', 'Ethernet, Wi-Fi']]},
  'The model you will actually meet in systems is the TCP/IP stack, with four layers. Application '
  'maps to OSI layers five to seven — HTTP, DNS, SSH, and simple mail transfer protocol, or SMTP. '
  'Transport maps to layer four — transmission control protocol, or TCP, and user datagram '
  'protocol, or UDP. Internet maps to layer three — internet protocol, or IP; internet control '
  'message protocol, or ICMP; and address resolution protocol, or ARP. Network Access maps to '
  'layers one and two — Ethernet and Wi-Fi. CompTIA questions usually name OSI layer numbers, so '
  'keep both maps in your head at once.'),
 ('bullets',
  {'kick': 'Models',
   'title': 'Encapsulation — Building the Packet',
   'items': ['Application creates the data',
             'Transport adds a TCP/UDP header with the port — a segment',
             'Internet adds an IP header with addresses — a packet',
             'Network Access adds an Ethernet header with MACs — a frame'],
   'note': 'Each layer adds its header on the way out, strips it on the way in.'},
  'Encapsulation is how data travels. The application creates the data. The transport layer adds a '
  'TCP or UDP header with the port — that makes the segment. The internet layer adds an IP header '
  'with source and destination addresses — that makes the packet. The network access layer adds an '
  'Ethernet header with MAC addresses — that makes the frame. So the protocol data unit grows as '
  'data moves down: segment, then packet, then frame. Each layer adds its header on the way out, '
  'and strips its own header on the way in. That is the journey of a single piece of data across '
  'a network.'),
 ('table',
  {'kick': 'Models',
   'title': 'Addressing at Each Layer',
   'headers': ['Layer', 'Address', 'Example'],
   'rows': [['Transport', 'Port', '443 HTTPS, 53 DNS'],
            ['Network', 'IP', '192.168.1.10 / 2001:db8::1'],
            ['Data link', 'MAC', '00:1A:2B:3C:4D:5E']]},
  'Each layer has its own address. Transport uses ports — 443 for hypertext transfer protocol '
  'secure, or HTTPS, and 53 for DNS. Network uses IP addresses — 192.168.1.10, or 2001 colon db 8 '
  'colon colon one for IP version six. Data link uses MAC addresses — six hex pairs, like zero '
  'zero colon one A colon two B. And here is the security link. Firewall rules match on IP '
  'addresses and ports, while switches and wireless filters match on MAC addresses. Know which '
  'layer each control reads, and you know which control to pick.'),
 ('callout',
  {'kind': 'info',
   'label': "Analyst's Lens",
   'title': 'Identify the layer before choosing a control',
   'body': 'A web attack arrives at layer 7 — use a web application firewall. A spoofed packet '
           'arrives at layer 3 — filter at the router. A rogue switch or ARP-poisoned MAC appears '
           'at layer 2 — use MAC filtering and port security.'},
  'Why must an analyst identify the layer before choosing a control? Because each layer has its '
  'own attack and its own defence. A web attack arrives at layer seven — the control is a web '
  'application firewall, or WAF. A spoofed packet arrives at layer three — the control is IP '
  'filtering at the router. A rogue switch, or an ARP-poisoned MAC mapping, appears at layer two — '
  'the control is MAC filtering and port security. Match the control to the layer, and you fix '
  'the right problem.'),
 ('chapter',
  {'num': 2,
   'of': 5,
   'title': 'IPv4 Addressing & Subnetting',
   'blurb': 'Structure, classes, CIDR and the two formulas'},
  'Now we move from the models to the numbers. Chapter two is IP version four addressing and '
  'subnetting — the geometry of the network. You will learn how an IP version four address is '
  'structured, how classless inter-domain routing — cedar — replaces the old class system, and '
  'the two formulas that carry the whole of subnetting. These are the calculations you will do '
  'by hand in the exam, and the zones your firewalls defend.'),
 ('bullets',
  {'kick': 'IPv4',
   'title': 'IPv4 Address Structure',
   'items': ['32 bits — four octets of 8 bits',
             'Written dotted-decimal, each octet 0–255',
             'Two parts: network portion + host portion',
             'Subnet mask marks the boundary'],
   'note': '192.168.1.10 / 255.255.255.0 — change the mask, change the boundary.'},
  'An IP version four address is thirty-two bits: four octets of eight bits, written '
  'dotted-decimal, each octet zero to two hundred and fifty-five. Every address has two parts — '
  'the network portion and the host portion — and the subnet mask marks the boundary. Take '
  '192.168.1.10 with mask 255.255.255.0. The first three octets are the network; the last is the '
  'host. Change the mask, and you change the boundary.'),
 ('bullets',
  {'kick': 'IPv4',
   'title': 'Classful Addressing — History',
   'items': ['Class A: 1–126, /8, ~16 million hosts',
             'Class B: 128–191, /16, 65,000 hosts',
             'Class C: 192–223, /24, 254 hosts',
             'Classes D and E: multicast and reserved'],
   'note': 'Classful addressing survives only as history.'},
  'Historically, addresses came in classes. Class A, first octet one to one hundred and '
  'twenty-six, default mask slash eight — sixteen million hosts. Class B, one hundred and '
  'twenty-eight to one hundred and ninety-one, slash sixteen — sixty-five thousand hosts. Class C, '
  'one hundred and ninety-two to two hundred and twenty-three, slash twenty-four — two hundred and '
  'fifty-four hosts. Classes D and E are multicast and reserved. Classful addressing survives only '
  'as history — cedar replaced it.'),
 ('bullets',
  {'kick': 'IPv4',
   'title': 'CIDR — Classless Inter-Domain Routing',
   'items': ['The /n count states the network bits',
             '/25 = 255.255.255.128 — splits a /24 into two',
             '/26 = 255.255.255.192 — splits it into four',
             '/30 = 255.255.255.252 — two usable hosts, point-to-point'],
   'note': 'The boundary can fall at any bit position.'},
  'Cedar lets the boundary fall at any bit position. The slash-n count states how many bits belong '
  'to the network. Slash twenty-five is 255.255.255.128 and splits a slash twenty-four into two. '
  'Slash twenty-six is 255.255.255.192 and splits it into four. Slash thirty is 255.255.255.252 — '
  'two usable hosts, the classic point-to-point link mask. Classes survive only as history.'),
 ('statement',
  {'kick': 'Subnetting',
   'title': 'The Two Formulas',
   'body': 'Subnets created = 2^n (n = bits borrowed). Usable hosts per subnet = 2^h − 2 (h = '
           'remaining host bits). Minus two: the network ID and the broadcast.'},
  'Two formulas carry the whole of subnetting. The number of subnets created is two to the power '
  'of n, where n is the bits borrowed from the host portion. The number of usable hosts per subnet '
  'is two to the power of h minus two, where h is the remaining host bits. Why minus two? One '
  'address is the network identifier, one is the broadcast. A slash twenty-six has six host bits: '
  'sixty-four minus two — sixty-two usable hosts.'),
 ('bullets',
  {'kick': 'Subnetting',
   'title': 'Subnetting Walkthrough',
   'items': ['Start: 10.0.0.0/24, need four equal subnets',
             'Borrow 2 bits → /26 mask (255.255.255.192)',
             '2² = 4 subnets; 2⁶ − 2 = 62 usable hosts each',
             'Ranges: .0–.63, .64–.127, .128–.191, .192–.255'],
   'note': 'First address is the network, last is the broadcast — never assign them.'},
  'Let us work one through. Start with ten dot zero dot zero dot zero, slash twenty-four, and we '
  'need four equal subnets. Borrow two bits — that makes a slash twenty-six mask, 255.255.255.192. '
  'Two squared is four subnets, and two to the sixth minus two is sixty-two usable hosts per '
  'subnet. The ranges: ten dot zero dot zero dot zero to point sixty-three, then point sixty-four '
  'to one twenty-seven, then one twenty-eight to one ninety-one, then one ninety-two to two '
  'fifty-five. In every range the first address is the network and the last is the broadcast — '
  'never assign them.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Quick Arithmetic',
   'title': 'Five fast checks',
   'body': '192.168.10.50/28 → network .48. A /29 has 6 usable hosts. 255.255.255.240 is /28. '
           'Borrow 2 from a /24 → 4 subnets of 62. Block size = 256 − mask octet.'},
  'Five quick calculations to anchor the skill. The network address of 192.168.10.50 with a slash '
  'twenty-eight — block size sixteen, fifty falls in the point forty-eight to point sixty-three '
  'range, so the network is 192.168.10.48. A slash twenty-nine has three host bits: eight minus '
  'two, six usable hosts. Mask 255.255.255.240 is slash twenty-eight. Borrow two bits from a slash '
  'twenty-four: four subnets of sixty-two hosts each. And the block size is always two hundred and '
  'fifty-six minus the mask octet. Practise these until they are instant.'),
 ('chapter',
  {'num': 3,
   'of': 5,
   'title': 'VLSM & Security Zones',
   'blurb': 'Variable-length masks and the zones they create'},
  'Chapter three is variable length subnet masking — VLSM — and the security story behind it. Real '
  'networks rarely need equal-sized subnets, and the design rule is largest first. Then we turn '
  'the same skill into security: those subnets become zones that contain a breach and block '
  'lateral movement.'),
 ('bullets',
  {'kick': 'VLSM',
   'title': 'Variable-Length Subnet Masks',
   'items': ['Different masks inside the same major network',
             'Finance might need 50 addresses; a link needs 2',
             'One rule governs: allocate the largest requirement first',
             'Start small and you fragment the space'],
   'note': 'Waste as little address space as possible.'},
  'Real networks rarely need equal-sized subnets. The finance team might need fifty addresses, '
  'while a point-to-point link needs two. VLSM lets you use different masks inside the same major '
  'network, so you waste as little address space as possible. One rule governs the whole design: '
  'allocate the largest requirement first. Start small and you fragment the space, and the big '
  'block no longer fits.'),
 ('table',
  {'kick': 'VLSM',
   'title': 'VLSM Design — Office Network',
   'headers': ['Requirement', 'Mask', 'Range'],
   'rows': [['Engineering 50', '/26', '.0–.63'],
            ['Sales 25', '/27', '.64–.95'],
            ['Management 10', '/28', '.96–.111'],
            ['Link A 2', '/30', '.112–.115'],
            ['Link B 2', '/30', '.116–.119']]},
  'Here is a real design. We have 192.168.1.0, slash twenty-four, and five requirements. '
  'Engineering needs fifty hosts — two to the sixth minus two is sixty-two, so slash twenty-six, '
  'range point zero to point sixty-three. Sales needs twenty-five — slash twenty-seven, point '
  'sixty-four to point ninety-five. Management needs ten — slash twenty-eight, point ninety-six to '
  'one eleven. Link A needs two — slash thirty, one twelve to one fifteen. Link B, also two — '
  'slash thirty, one sixteen to one nineteen. Largest first, no overlap, and every requirement '
  'fits.'),
 ('table',
  {'kick': 'VLSM',
   'title': 'VLSM for Security Segments',
   'headers': ['Zone', 'Hosts', 'Mask', 'Range'],
   'rows': [['Workstations', '100', '/25', '.0–.127'],
            ['Internal servers', '30', '/27', '.128–.159'],
            ['DMZ', '14', '/28', '.160–.175'],
            ['Management', '6', '/29', '.176–.183'],
            ['Two WAN links', '2', '/30', '.184–.191']]},
  'Now the security version of the same skill. Ten-ten-ten-zero, slash twenty-four, cut into six '
  'segments. Workstations, one hundred hosts — slash twenty-five, point zero to point one '
  'twenty-seven. Internal servers, thirty — slash twenty-seven, one twenty-eight to one '
  'fifty-nine. The demilitarised zone — the DMZ — runs fourteen hosts on slash twenty-eight, one '
  'sixty to one seventy-five. Management, six — slash twenty-nine, one seventy-six to one '
  'eighty-three. And two wide area network — WAN — links, slash thirty each. Notice the security '
  'story: these are zones, not just ranges. The DMZ is a buffer between your network and the '
  'outside world.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Security Lens',
   'title': 'Subnet design is a security control',
   'body': 'A compromised workstation can reach only its own segment if the firewall denies the '
           'other ranges. Segmentation contains the breach — the blast radius is the size of the '
           'subnet it lands in.'},
  'How does subnet design become a security control? A compromised workstation can reach only its '
  'own segment if the firewall denies the other ranges. Segmentation contains the breach: the '
  'attacker cannot move laterally to servers or the management zone. The blast radius of a breach '
  'is the size of the subnet it lands in, and every isolated zone shrinks that radius. That is the '
  'security value of everything you just calculated.'),
 ('chapter',
  {'num': 4,
   'of': 5,
   'title': 'IPv6 Addressing',
   'blurb': 'Why it exists, the shorthand, and the address types'},
  'Chapter four is IP version six. IP version four ran out of addresses, and IP version six is the '
  'successor with a vastly larger space. You will learn why it exists, the two shorthand rules '
  'that shorten an address, and the four address types you need to recognise. Then the security '
  'angle: running both stacks at once doubles your attack surface.'),
 ('bullets',
  {'kick': 'IPv6',
   'title': 'Why IPv6 Exists',
   'items': ['IPv4 ran out — 4.3 billion was never enough',
             'IPv6 uses 128-bit addresses',
             '340 undecillion addresses — ~665 quadrillion per mm² of Earth',
             'Notation: eight groups of four hex digits, colon-separated'],
   'note': '2001:0db8:85a3:0000:0000:8a2e:0370:7334'},
  'IP version four ran out. Four point three billion addresses were never enough for a connected '
  'planet. IP version six uses one hundred and twenty-eight-bit addresses — three hundred and '
  'forty undecillion of them, roughly six hundred and sixty-five quadrillion per square millimetre '
  'of the Earth\'s surface. Notation: eight groups of four hex digits, separated by colons — two '
  'thousand one, zero db 8, eight five a 3, and so on.'),
 ('bullets',
  {'kick': 'IPv6',
   'title': 'IPv6 Shorthand Rules',
   'items': ['Drop leading zeros in each group — 0db8 → db8',
             'One contiguous run of zero groups → double colon (once only)',
             '2001:0db8:85a3::8a2e:370:7334',
             'Two double colons would be ambiguous'],
   'note': 'Shorter to read, shorter to type — the form you see in logs.'},
  'Two rules shorten that address. First, drop leading zeros in each group — zero db 8 becomes db '
  '8, zero three seven zero becomes three seven zero. Second, one contiguous run of zero groups '
  'may be replaced by a double colon — and only once, because two double colons would be '
  'ambiguous. The example becomes two thousand one colon db 8 colon eight five a 3, double colon, '
  'eight a 2 e, three seven zero, seven three three four. Shorter to read, shorter to type, and it '
  'is the form you will see in logs.'),
 ('table',
  {'kick': 'IPv6',
   'title': 'IPv6 Address Types',
   'headers': ['Type', 'Prefix', 'Use'],
   'rows': [['Global unicast', '2000::/3', 'Routable on the public internet'],
            ['Link-local', 'fe80::/10', 'Auto-assigned, never leaves its subnet'],
            ['Unique local', 'fc00::/7', 'IPv6 private range, like RFC 1918'],
            ['Multicast', 'ff00::/8', 'One-to-many']]},
  'Four types to know. Global unicast — prefix two thousand double colon slash three — routable on '
  'the public internet. Link-local — fe 80 double colon slash ten — automatically assigned, and it '
  'never leaves its subnet. Unique local — fc 00 double colon slash seven — the IP version six '
  'private range, like request for comments 1918, or RFC 1918, in IP version four. Multicast — '
  'ff 00 double colon slash eight — one-to-many. And the exam line: IP version six has no '
  'broadcast addresses — multicast takes that role.'),
 ('callout',
  {'kind': 'warn',
   'label': 'Security Risk',
   'title': 'Dual-stack doubles the attack surface',
   'body': 'IPv6 traffic can bypass IPv4-only ACLs. A firewall filtering only IPv4 leaves a quiet '
           'door open over IPv6. Filter both, or disable the stack you do not use.'},
  'The transition has been running for years, and most networks run dual-stack — both protocols '
  'at once. That doubles the attack surface. An attack surface is every point where an '
  'unauthorised user could enter, or extract data from, your environment — and running two '
  'address families doubles those points. The risk: IP version six traffic can bypass IP version '
  'four-only access control lists — ACLs. A firewall filtering only IP version four leaves a '
  'quiet door open over IP version six. Filter both stacks, or disable the one you do not use.'),
 ('chapter',
  {'num': 5, 'of': 5, 'title': 'Consolidation', 'blurb': 'Key takeaways and what to revise'},
  'Chapter five is consolidation. We bring the session together into the key takeaways you should '
  'carry forward, and the revision checklist that turns this session into long-term recall.'),
 ('recap',
  {'title': 'Key Takeaways',
   'items': ['Models organise the layers — OSI seven, TCP/IP four, know both and the mapping',
             'Encapsulation builds the packet — each layer adds a header, from data to frame',
             'Addressing is the geometry — CIDR and VLSM define the zones your firewalls defend',
             'VLSM goes largest first',
             'Segmentation is a control — zones limit the attack surface and block lateral '
             'movement',
             'Dual-stack doubles the attack surface — filter or disable what you do not use']},
  'Six takeaways. One: models organise the layers — OSI seven, TCP/IP four — know both and the '
  'mapping. Two: encapsulation builds the packet — each layer adds a header, from data to frame. '
  'Three: addressing is the geometry — cedar and VLSM define the zones your firewalls defend. '
  'Four: VLSM goes largest first. Five: segmentation is a control — zones limit the attack '
  'surface and block lateral movement. Six: dual-stack doubles the attack surface — filter both, '
  'or disable what you do not use.'),
 ('bullets',
  {'kick': 'Consolidation',
   'title': 'Revision Checklist',
   'items': ['Retake the session quiz until you score well without guessing',
             'Practise subnetting — ten /24 to /30 calculations by hand',
             "Draw a VLSM table for your own network's segments",
             'Read ahead to Session 2: switching, VLANs and spanning tree'],
   'note': 'This video is one revision pass — the quiz is the recall test.'},
  'Before you move on, make the learning stick. Retake the session quiz until you score well '
  'without guessing. Practise subnetting — ten slash twenty-four to slash thirty calculations by '
  'hand. Draw a VLSM table for your own network\'s segments. And read ahead to Session 2, where we '
  'build the layer two picture: switching, virtual local area networks — VLANs — and spanning '
  'tree protocol. This video is one revision pass — the quiz is where you prove you can recall '
  'it.'),
 ('statement',
  {'kick': 'Next',
   'title': 'Session 2 — Switching, VLANs & Network Architectures',
   'body': 'Follow frames through switches, split the network into VLANs with 802.1Q trunking, and '
           'meet Spanning Tree Protocol — the loop-prevention safety net.'},
  'That closes Session One. You can now explain the OSI model, and map the TCP/IP stack onto it. '
  'You can describe encapsulation and the packet at each layer. You can calculate subnet '
  'boundaries with cedar and VLSM, and explain how those subnets become security zones that limit '
  'the attack surface. Retake the session quiz until you score seventy percent without guessing, '
  'and practise ten subnet calculations by hand. The network foundation you have built here is '
  'the legend every later session reads.')]

if __name__ == "__main__":
    total = sum(len(f[2].split()) for f in FRAMES)
    print("Session 1 narration: %d frames, %d words (~~%d min at 163 wpm)"
          % (len(FRAMES), total, round(total / 163)))
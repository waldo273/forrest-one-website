# narration_sec_s2.py — Security+ SY0-701 (revised), Session 2
# "Switching, VLANs & Network Architectures"
# One-video-per-lesson format. Each frame: (template, payload, narration).
# Narration is read ALOUD IN FULL by ElevenLabs (Billy's voice) — short
# sentences that stand alone without the visual. Abbreviations are written
# so the engine reads them the way they are spoken in the classroom.
# USER RULES: no "good morning" (use "good day"); no courseware timing
# references — only the video's own length may be mentioned.

DECK = 'Switching, VLANs & Network Architectures'
SESSION = 'Session 2 · Security+ SY0-701 (revised)'

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
   'title': 'Layer 2 Switching',
   'blurb': 'Frames, MAC addresses and the forwarding table'},
  'Good day, and welcome to Session Two of the combined Network Fundamentals and CompTIA Security+ '
  'course. Session one gave you the models and the addressing. In this video we follow the '
  'traffic: how frames travel inside a network, how switches learn, how virtual local area '
  'networks, or vlans, keep segments apart, and how Spanning Tree keeps redundancy from '
  'destroying you. Every mechanism here is also a security control. We begin with layer two '
  'switching — the machinery that actually moves frames between devices.'),
 ('statement',
  {'kick': 'The Journey',
   'title': 'From Addressing to Forwarding',
   'body': 'Session 1 was the map — models and addresses. This session is the journey: how frames '
           'actually move. Every segment is a containment boundary.'},
  'Here is the arc of this session. Session one was the map — the models and the addresses. This '
  'session is the journey: how frames actually move inside a network. We will trace switch '
  'forwarding, then vlans, then Spanning Tree, then the architectures that put zones where '
  'traffic should not cross. Hold one thread through all of it: every segment is a containment '
  'boundary.'),
 ('bullets',
  {'kick': 'The Journey',
   'title': 'Session Objectives',
   'items': ['Explain switch forwarding — learn, look up, forward',
             'Describe VLANs and 802.1Q trunking',
             'Explain Spanning Tree root election and port states',
             'Describe the STP attacks and the guard features',
             'Map architectures into zones, DMZ and segmentation'],
   'note': 'Five objectives — the quiz at the end tests every one.'},
  'This session has ten objectives. One: explain why switches forward frames rather than '
  'packets, and name the layer two protocol data unit, or PDU. Two: describe the structure of a '
  'media access control, or MAC, address, including the organisationally unique identifier — '
  'the OUI — and its forensic value. Three: explain the learn, look up, forward and flood '
  'behaviour of the switch forwarding table. Four: describe vlans and their security purposes — '
  'guest isolation, blast-radius containment, and limiting lateral movement. Five: explain '
  'eight-oh-two-point-one-Q tagging, trunk ports and access ports, and the vlan hopping attacks '
  'that target native vlan misconfiguration. Six: explain the native vlan risk and the '
  'mitigations — move vlan one, prune unused vlans, restrict trunk allowed lists. Seven: '
  'describe the switching-loop problem, and how Spanning Tree solves it. Eight: explain root '
  'bridge election, root ports and spanning tree port states. Nine: describe spanning tree '
  'attacks, and the defensive features — bridge protocol data unit Guard, Root Guard and port '
  'security. Ten: map network segments to security zones, including the demilitarised zone, or '
  'DMZ, with external and internal firewalls, and explain microsegmentation. Ten objectives — '
  'and the quiz at the end tests every one of them.'),
 ('bullets',
  {'kick': 'Layer 2',
   'title': 'Switches Forward Frames, Not Packets',
   'items': ['Switches connect devices within a broadcast domain',
             'Layer 2 decision — based on MAC addresses, not IP',
             'Frame — the layer 2 PDU with Ethernet headers',
             'Forensic value — MACs in a capture show direct neighbours'],
   'note': 'A switch never reads an IP address.'},
  'Here is the key distinction of this session. A switch operates at layer two, and makes its '
  'decisions on MAC addresses — never on internet protocol, or IP, addresses. It forwards '
  'frames — the layer two PDU — not packets. And there is forensic value in that. When you see '
  'a frame in a capture, the source and destination MAC addresses tell you which directly '
  'connected devices spoke, even if the traffic later crossed a router.'),
 ('bullets',
  {'kick': 'Layer 2',
   'title': 'MAC Addresses',
   'items': ['48-bit identifier burned into the interface',
             'Written as six pairs of hex, e.g. 00:1A:2B:3C:4D:5E',
             'OUI — first three octets identify the manufacturer',
             'Last three octets are device-specific'],
   'note': 'The OUI lets you identify a vendor from a capture alone.'},
  'Every network interface carries a MAC address — a forty-eight-bit identifier, burned in by '
  'the manufacturer and written as six pairs of hexadecimal digits, like zero-zero colon one-A '
  'colon two-B. The first three octets are the OUI, and they name the manufacturer. The last '
  'three are unique to the device. And that OUI is how you can often identify the vendor of a '
  'device just from a capture.'),
 ('bullets',
  {'kick': 'Layer 2',
   'title': 'The Switch Forwarding Table',
   'items': ['Learn — record the source MAC and its port',
             'Look up — find the destination MAC in the table',
             'Forward — to the matching port if known',
             'Flood — unknown unicast goes to all ports but the source',
             'Broadcasts — always flooded, they reach every host'],
   'note': 'Learn, look up, forward, flood — the classic sequence.'},
  'When a switch receives a frame it does three things. Learn: record the source MAC address and '
  'the port it arrived on. Look up: find the destination MAC address in the table. Forward: '
  'send the frame to the matching port if the address is known. If the destination is unknown, '
  'it floods the frame to every port except the source — that is unknown unicast flooding. And '
  'broadcasts are always flooded, because they are meant to reach every host.'),
 ('bullets',
  {'kick': 'Layer 2',
   'title': 'Frame Switching Walkthrough',
   'items': ['Host A sends to B — the table is empty',
             'The switch learns A is on port 1',
             'Look up fails — B is unknown, so flood to all but port 1',
             'B replies — the switch learns B on port 2',
             'Next time, frames between A and B go straight to the port'],
   'note': 'Once learned, the path never floods again.'},
  'Let us trace it. Host A sends to Host B — the switch table is empty. The switch learns that '
  'A is on port one. The lookup for B fails, so the frame floods to every port except port one. '
  'B receives it on port two, and replies. The switch learns B on port two. The lookup for A '
  'succeeds, so the reply goes straight to port one. From then on, frames between A and B never '
  'flood again — the switch has learned the path.'),
 ('callout',
  {'kind': 'warn',
   'label': "Analyst's Lens",
   'title': 'A flood of unknown-unicast frames is a warning',
   'body': 'It could be a stale ARP cache or a misconfigured switch — or an attacker flooding the '
           'CAM table until the switch degrades into hub mode and every frame is visible.'},
  'What does a flood of unknown-unicast frames in a capture tell you? It could be a stale '
  'address resolution protocol, or ARP, cache, or a misconfigured switch. Or it could be an '
  'attacker flooding the content-addressable memory, or cam, table until the switch degrades '
  'into hub mode, and every frame is visible. That is the MAC flooding attack, and it is '
  'dangerous precisely because it undoes segmentation at the port. If your capture shows a '
  'suspicious flood, check the rate and the source MAC addresses before you blame the network.'),
 ('chapter',
  {'num': 2,
   'of': 4,
   'title': 'VLANs & Trunking',
   'blurb': 'Segmentation, 802.1Q tags and the native VLAN risk'},
  'Now we move from forwarding to segmentation. Chapter two is vlans and trunking. A vlan '
  'splits one physical switch into logical broadcast domains — and that is the core containment '
  'control of the whole course. You will learn how eight-oh-two-point-one-Q tags carry frames '
  'between switches, how access and trunk ports differ, and the native vlan risk that every '
  'exam scenario returns to.'),
 ('bullets',
  {'kick': 'VLANs',
   'title': 'VLANs Segment the Broadcast Domain',
   'items': ['A VLAN splits one switch into logical broadcast domains',
             'Without VLANs, every device shares one domain',
             'Security purpose — separate servers, DMZ and workstations',
             'Guest traffic is isolated from the corporate network',
             'A breach cannot cross VLAN boundaries freely'],
   'note': 'Each VLAN shrinks the attack surface an attacker can roam.'},
  'A vlan splits one physical switch into multiple logical broadcast domains. Without vlans, '
  'every device on the switch shares one broadcast domain. With vlans, broadcast traffic stays '
  'inside its own vlan. The security purposes: separate sensitive systems from user '
  'workstations, isolate guest wireless from corporate, and contain the blast radius of a '
  'broadcast storm or an ARP spoofing attack. And beyond that, vlans are a lateral movement '
  'control. If a workstation is compromised, segmentation stops the attacker stepping sideways '
  'into the server vlan. Each vlan shrinks the attack surface the attacker can roam.'),
 ('bullets',
  {'kick': 'VLANs',
   'title': '802.1Q Trunking',
   'items': ['Trunk port — carries many VLANs between switches',
             'The tag — a 4-byte 802.1Q header inserted in the frame',
             'VID — a 12-bit VLAN ID, 4094 usable VLANs',
             'Access port — carries one untagged VLAN to an endpoint'],
   'note': 'Trunks are the highways; access ports are the driveways.'},
  'When a frame must travel between switches and stay in its vlan, the switch inserts a '
  'four-byte eight-oh-two-point-one-Q tag into the Ethernet header. The tag carries the '
  'twelve-bit vlan ID — vlans one to four thousand and ninety-four. A trunk port carries many '
  'tagged vlans between switches. An access port carries one untagged vlan to an endpoint. '
  'Trunks are the highways; access ports are the driveways. And because trunks are the '
  'highways, they need the most protection: restrict which vlans a trunk is allowed to carry, '
  'and never leave the native vlan on its default.'),
 ('table',
  {'kick': 'VLANs',
   'title': 'A Practical VLAN Design',
   'headers': ['VLAN', 'Name', 'Purpose'],
   'rows': [['10', 'MANAGEMENT', 'Switch and infrastructure management'],
            ['20', 'SERVERS', 'Internal servers'],
            ['30', 'WORKSTATIONS', 'User workstations'],
            ['40', 'DMZ', 'Public-facing services'],
            ['999', 'BLACKHOLE', 'Unused quarantine VLAN']]},
  'Here is a real design. vlan ten, management — switch and infrastructure administration. '
  'vlan twenty, servers. vlan thirty, workstations. vlan forty, the DMZ — public-facing '
  'services. vlan nine-nine-nine, the blackhole — an unused quarantine vlan that swallows '
  'traffic from ports nothing should use. And the key rule: vlan one is the default native vlan '
  'on trunks, and it is a known attack surface. Move it to an unused ID, prune the vlans you do '
  'not need, and restrict trunks to an explicit allowed list.'),
 ('callout',
  {'kind': 'warn',
   'label': 'Security Risk',
   'title': 'The native VLAN and VLAN hopping',
   'body': 'VLAN 1 is the default native VLAN — a known attack surface. VLAN hopping crosses '
           'boundaries by switch spoofing or double tagging. Move VLAN 1, prune unused VLANs, '
           'restrict trunk allowed lists.'},
  'Why does the native vlan matter so much? Because vlan one is the default native vlan on '
  'trunks, and it is a known attack surface. vlan hopping crosses vlan boundaries in two ways. '
  'Switch spoofing — the attacker negotiates a trunk port to reach many vlans. Double tagging — '
  'the attacker spoofs the native vlan to carry a frame into another vlan. The mitigations are '
  'the same: move vlan one to an unused ID, prune the vlans you do not need, and restrict trunks '
  'to an explicit allowed list. That is what blunts vlan hopping.'),
 ('bullets',
  {'kick': 'VLANs',
   'title': 'Design the Segmentation',
   'items': ['The public web server lives in the DMZ',
             'The blackhole never carries user traffic',
             'Management is isolated from workstations',
             'The native VLAN risk is VLAN hopping',
             'Segmentation prevents hopping and broadcast storms'],
   'note': 'Think microsegmentation — isolate the sensitive workloads.'},
  'Let us fix the design reasoning. Which vlan hosts the public web server? The DMZ. Which '
  'never carries user traffic? The blackhole. Why isolate management? Management should never '
  'share a broadcast domain with users — a compromise there controls the switches. What does '
  'the default native vlan risk? vlan hopping through double tagging. And two attacks '
  'segmentation prevents: vlan hopping, and the spread of broadcast storms. And think '
  'microsegmentation — isolate the sensitive workloads, not just whole departments.'),
 ('chapter',
  {'num': 3,
   'of': 4,
   'title': 'Spanning Tree',
   'blurb': 'Loops, root election, port states and the guards'},
  'Chapter three is Spanning Tree — the availability story. Redundancy is essential, but '
  'redundant links create loops, and loops kill networks. Spanning Tree Protocol, or STP, keeps '
  'a redundant topology loop-free, by blocking the ports that would cause a loop. You will '
  'learn the problem, the root election, the port states, and the guard features that stop an '
  'attacker from hijacking the whole process.'),
 ('bullets',
  {'kick': 'STP',
   'title': 'The Problem: Switching Loops',
   'items': ['Redundancy — two links between switches create a loop',
             'Broadcast storm — frames circulate forever',
             'The cause — broadcasts are always flooded back out',
             'The cost — CPU pegged, network collapse'],
   'note': 'Redundancy is essential — but loops are fatal.'},
  'Redundancy is essential for availability — but two links between switches create a loop. A '
  'broadcast frame enters switch A, which forwards it to switch B over link one. B sees a '
  'broadcast and forwards it back to A over link two. A forwards it again. The frame never '
  'dies. That is a broadcast storm, and it consumes bandwidth and central processing unit until '
  'the network collapses. The cause is simple: broadcasts are always flooded back out, so a '
  'loop keeps them alive forever.'),
 ('bullets',
  {'kick': 'STP',
   'title': 'STP: A Loop-Free Logical Topology',
   'items': ['STP — IEEE 802.1D — blocks redundant ports',
             'Root bridge — lowest bridge ID (priority + MAC) wins',
             "Root port — each non-root switch's best path to root",
             'Blocking — neither root nor designated ports block'],
   'note': 'One logical path, no loops.'},
  'STP — the Institute of Electrical and Electronics Engineers standard, eight-oh-two-point-'
  'one-D — creates a loop-free logical topology by blocking redundant ports. It elects a root '
  'bridge: the lowest bridge ID wins, where the bridge ID is the priority plus the MAC address. '
  'Every non-root switch then picks its root port — the lowest-cost path to the root. Ports '
  'that are neither root nor designated go into blocking state. The result is one logical path, '
  'and no loops.'),
 ('table',
  {'kick': 'STP',
   'title': 'STP Port States',
   'headers': ['State', 'Forwards?', 'Role'],
   'rows': [['Blocking', 'No', 'Listens for BPDUs only'],
            ['Listening', 'No', 'Transitional — still learning topology'],
            ['Learning', 'No', 'Builds the MAC table'],
            ['Forwarding', 'Yes', 'Normal operation'],
            ['Disabled', 'No', 'Administratively down']]},
  'There are five port states. Blocking: no forwarding, listening for BPDUs only. Listening: '
  'transitional, still learning the topology. Learning: building the MAC table, but not '
  'forwarding. Forwarding: normal operation. Disabled: administratively down. And the '
  'convergence note: traditional STP takes thirty to fifty seconds to converge after a topology '
  'change. Rapid Spanning Tree — eight-oh-two-point-one-W — does it in seconds.'),
 ('table',
  {'kick': 'STP',
   'title': 'STP Attacks and the Guard Features',
   'headers': ['Threat', 'Feature', 'Effect'],
   'rows': [['Attacker becomes root bridge', 'Root Guard', 'Port cannot become a root port'],
            ['BPDUs on an access port', 'BPDU Guard', 'Port shuts down on receipt'],
            ['Rogue switch insertion', 'Port security', 'Limits MACs per port']]},
  'STP can be attacked. A rogue switch sending superior BPDUs can become the root bridge — and '
  "then all traffic traverses the attacker's switch, an invisible interception. Three defences. "
  'Root Guard: a port protected by it cannot become a root port, so it neutralises a rogue '
  'root. BPDU Guard: an access port that receives a BPDU shuts down, stopping a rogue switch '
  'being plugged in at all. Port security: limits the MAC addresses allowed per port, which '
  'also blunts MAC flooding. The stakes are real — a rogue root silently reroutes your '
  'traffic.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Worked Election',
   'title': 'Two switches, equal priority',
   'body': 'The lower MAC becomes root. The gigabit link (cost 4) forwards; the 100 Mbps link '
           '(cost 19) blocks until failure.'},
  'Let us work an election. Two switches, equal priority — which becomes root, and what '
  'converges? Equal priority, so the tiebreaker is the MAC address: the lower MAC roots. On the '
  'non-root switch, the root port is the lowest-cost path — the gigabit link at cost four '
  'forwards. The hundred-megabit link at cost nineteen blocks. If the gigabit link fails, the '
  'blocked port transitions, and the network reconverges — thirty to fifty seconds on '
  'traditional STP, seconds on Rapid Spanning Tree.'),
 ('chapter',
  {'num': 4,
   'of': 4,
   'title': 'Architectures & Consolidation',
   'blurb': 'Zones, DMZ, campus layers and the takeaways'},
  'Chapter four is the architecture view. We take everything you have learned — forwarding, '
  'vlans, Spanning Tree — and turn it into security zones. Segmentation becomes zoning. The DMZ '
  'brackets public services, and the campus layers show where traffic is filtered. Then we '
  'consolidate the session into the takeaways you should carry forward.'),
 ('bullets',
  {'kick': 'Architectures',
   'title': 'From Segments to Security Zones',
   'items': ['Segmentation — VLANs and subnets become zones',
             'DMZ — public services isolated from internal',
             'DMZ firewalls — external and internal, with proxy between',
             'Blast radius — compromise stays inside its segment',
             'Lateral movement — zones block east-west spread'],
   'note': 'Architecture is a control, not plumbing.'},
  'Now the architecture view. Segmentation — vlans and subnets — becomes security zoning. The '
  'DMZ hosts public services, isolated from the internal network and bracketed by an external '
  'firewall and an internal firewall, often with a proxy between them. Blast radius: a '
  'compromise stays inside its segment. Lateral movement: zones block east-west spread, so an '
  'attacker who lands on one workstation cannot roam the whole campus. And the exam line: '
  'architecture is a control, not plumbing. When a question asks how to contain a breach, the '
  'answer is often segmentation.'),
 ('bullets',
  {'kick': 'Architectures',
   'title': 'Campus Architecture in One Slide',
   'items': ['Access layer — endpoints connect, switchports and Wi-Fi',
             'Distribution layer — VLAN routing, policy enforcement',
             'Core layer — high-speed backbone, no endpoint policy',
             'Zones — DMZ, internal, management, guest',
             'IoT isolation — separate segment for unmanaged devices'],
   'note': 'Traffic moves up to be filtered, across only where zones allow.'},
  'A classic campus has three layers. Access: where endpoints connect — switchports and Wi-Fi. '
  'Distribution: where vlan routing and policy enforcement happen. Core: the high-speed '
  'backbone, with no endpoint policy. Across it all, the zones: DMZ, internal, management, '
  'guest. And a modern addition — the Internet of Things, or I-O-T. Unmanaged I-O-T devices are '
  'a high-risk endpoint, so they get their own segment, isolated from everything sensitive. '
  'Traffic moves up to be filtered, and across only where the zones allow.'),
 ('recap',
  {'title': 'Key Takeaways',
   'items': ['Switches learn and forward — source MAC in, destination MAC out, flood when unknown',
             'VLANs are containment — segmentation limits broadcast, blast radius and lateral '
             'movement',
             '802.1Q tags the trunk — 12-bit VID; native VLAN 1 is a risk to move and prune',
             'STP blocks loops — root by lowest ID; the guards stop hijacking',
             'Architecture is security — zones, DMZ firewalls and IoT isolation define where '
             'traffic may flow']},
  'Five takeaways. One: switches learn and forward — source MAC in, destination MAC out, flood '
  'when unknown. Two: vlans are containment — segmentation limits broadcast and blast radius. '
  'Three: eight-oh-two-point-one-Q tags the trunk — a twelve-bit vlan ID, and native vlan one '
  'is a risk to move. Four: STP blocks loops — root by lowest ID, and the guards stop '
  'hijacking. Five: architecture is security — zones and the DMZ define where traffic may '
  'flow.'),
 ('bullets',
  {'kick': 'Consolidation',
   'title': 'Revision Checklist',
   'items': ['Retake the session quiz until you score well without guessing',
             'Draw a VLAN table for a small campus you know',
             'Trace an STP election — two switches, two links, pick root and blocked port',
             'Read ahead to Session 3 — DNS, DHCP, NTP and SSH'],
   'note': 'This video is one revision pass — the quiz is the recall test.'},
  'Before you move on, make the learning stick. Retake the session quiz until you score well '
  'without guessing. Draw a vlan table for a small campus you know. Trace an STP election — two '
  'switches, two links, pick the root and the blocked port. And read ahead to Session Three, '
  'where we meet the services every network runs: domain name system, dynamic host '
  'configuration protocol, network time protocol and secure shell. This video is one revision '
  'pass — the quiz is where you prove you can recall it.'),
 ('statement',
  {'kick': 'Next',
   'title': 'Session 3 — Network Services & the Attack Surface',
   'body': 'DNS, DHCP, NTP and SSH — the services every network runs, and how each can be turned '
           'against you.'},
  'That closes Session Two. You can now follow frames through switches, split a network into '
  'vlans with eight-oh-two-point-one-Q trunking, and explain how Spanning Tree Protocol '
  'prevents loops from collapsing a layer two network. Retake the session quiz until you score '
  'seventy percent without guessing. The layer two picture you have built here carries '
  'everything you learned about addressing in Session One.')]

if __name__ == "__main__":
    total = sum(len(f[2].split()) for f in FRAMES)
    print("Session 2 narration: %d frames, %d words (~~%d min at 163 wpm)"
          % (len(FRAMES), total, round(total / 163)))
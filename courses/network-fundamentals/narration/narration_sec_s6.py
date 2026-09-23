# narration_sec_s6.py — Security+ SY0-701 (revised), Session 6
# "Cryptography & Public Key Infrastructure"
# One-video-per-lesson format. Each frame: (template, payload, narration).
# Narration is read ALOUD IN FULL by ElevenLabs (Billy's voice) — short
# sentences that stand alone without the visual. Abbreviations are written
# so the engine reads them the way they are spoken in the classroom.
# USER RULES: no "good morning" (use "good day"); no courseware timing
# references — only the video's own length may be mentioned.

DECK = 'Cryptography & Public Key Infrastructure'
SESSION = 'Session 6 · Security+ SY0-701 (revised)'

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
   'title': 'The Lock and Key of the Digital World',
   'blurb': 'Symmetric, asymmetric, hashing and signatures — the three jobs'},
  'Good day, and welcome to Session Six of the combined Network Fundamentals and CompTIA Security+ '
  'course. This session is cryptography and public key infrastructure — the art of securing data. '
  'Sessions one and two established the principles and the adversaries. In this session we learn '
  'the mechanisms that protect data: encryption for confidentiality, hashing for integrity, and '
  'digital signatures for identity. No mathematics — just the right tool for the right job.'),
 ('statement',
  {'kick': 'The Three Jobs',
   'title': 'The Shape of the Session',
   'body': 'Encrypt for confidentiality. Hash for integrity. Sign for identity. Every mechanism in '
           'this session fits one of those three jobs, and the exam rewards knowing which.'},
  'Cryptography is the lock and key of the digital world, and it has exactly three jobs. Encrypt '
  'for confidentiality. Hash for integrity. Sign for identity. Hold that map, because every '
  'cryptographic mechanism in this session fits into one of those three jobs. The exam rewards '
  'knowing which tool fits which job, so keep the three-job map in your head throughout.'),
 ('bullets',
  {'kick': 'The Three Jobs',
   'title': 'Session Objectives',
   'items': ['Explain symmetric encryption — one key, fast, key distribution problem',
             'Explain asymmetric encryption — key pairs, slower, solves distribution',
             'Describe hashing — one-way digests for integrity',
             'Explain digital signatures — hashing plus private key',
             'Describe PKI — certificates, CAs, revocation, key management',
             'Match solutions to data states — at rest, in transit, in use'],
   'note': 'Six objectives — the quiz at the end tests every one.'},
  'By the end of this session you will be able to explain symmetric encryption — one key, fast, '
    'with a key distribution problem. You will explain asymmetric encryption — key pairs, slower, '
    'which solves that distribution problem. You will explain key length and keyspace, and why '
    'longer keys resist brute force. You will describe hashing — one-way digests for integrity. '
    'You will explain digital signatures — hashing combined with a private key. You will describe '
    'the public key infrastructure — certificates, authorities, revocation and key management. '
    'You will explain the certificate signing request flow and subject name attributes. You will '
    'describe certificate revocation and the certificate lifecycle. You will describe key '
    'management, including cryptoprocessors and key escrow. You will match cryptographic solutions '
    'to data at rest, in transit and in use. And you will explain salting, key stretching, perfect '
    'forward secrecy, blockchain and obfuscation. Eleven objectives, and the quiz tests every one.'),
 ('bullets',
  {'kick': 'Algorithms',
   'title': 'Symmetric Encryption',
   'items': ['One key — the same secret key encrypts and decrypts',
             'Fast — ideal for bulk encryption of large data',
             'AES — the Advanced Encryption Standard, 128, 192 or 256-bit keys',
             'Confidentiality only — sender and recipient share the same key',
             'The problem — secure key storage and distribution',
             'In action — BitLocker, FileVault, VPNs and secure messaging'],
   'note': 'The algorithm is fine; the key is the challenge.'},
  'Symmetric encryption uses one key: the same secret key encrypts and decrypts. It is fast, which '
  'makes it ideal for bulk encryption of large amounts of data. The Advanced Encryption Standard, '
  'advanced encryption standard, is the symmetric algorithm you will meet — it supports key sizes '
  'of 128, 192 or 256 bits, and larger keys mean greater security. It provides confidentiality '
  'only — the sender and recipient must both hold the same key. And that is its problem: storing '
  'and distributing the key securely. The algorithm is fine; the key is the challenge. You will '
  'see advanced encryption standard at work in BitLocker, FileVault and virtual private networks.'),
 ('bullets',
  {'kick': 'Algorithms',
   'title': 'Key Length Matters',
   'items': ['Keyspace — the range of possible key values',
             'Longer = stronger — a 256-bit key is exponentially stronger than 128-bit',
             'The effect — each added bit doubles the work required',
             'Brute force — larger keyspaces defeat exhaustive search',
             'The cost — longer keys use more CPU, memory and power'],
   'note': 'Strength and resources trade off.'},
  'Why do we talk about key lengths? The key ensures the ciphertext remains protected even when '
  'the algorithm is known. The range of possible key values is the keyspace, and a longer key bit '
  'length means a larger keyspace. Add one bit and you double the keyspace — a 256-bit key is '
  'exponentially stronger than a 128-bit key. Longer keys protect against brute-force '
  'cryptanalysis. The cost: larger keys use more central processing unit, memory and power. '
  'Strength and resources trade off.'),
 ('bullets',
  {'kick': 'Algorithms',
   'title': 'Asymmetric Encryption',
   'items': ['Key pair — a public key and a private key',
             'The rule — if the public key encrypts, only the private key decrypts',
             'RSA — relies on the difficulty of factoring large primes',
             'ECC — similar security with smaller keys, ideal for mobile and IoT',
             'Distribution solved — the public key is easy to share',
             'Slower — used for keys, signatures and handshakes, not bulk payloads'],
   'note': 'The private key cannot be derived from the public key.'},
  'Asymmetric encryption solves the distribution problem with a key pair. If the public key '
  'encrypts, only the private key can decrypt. The private key cannot be derived from the public '
  'key, and it must be kept secret. The public key is easy to distribute — anyone can have it. Two '
  'algorithms matter. rivest shamir adleman relies on the mathematical difficulty of factoring '
  'large prime numbers, and it is widely used for data transmission and signatures. elliptic curve '
  'cryptography, elliptic curve cryptography, reaches similar security with smaller keys, which '
  'makes it faster and lighter — a good fit for mobile and IoT devices. The trade-off: asymmetric '
  'is slower, so it is used for small amounts of data — keys, signatures, handshakes — not bulk '
  'payloads.'),
 ('bullets',
  {'kick': 'Algorithms',
   'title': 'Hashing — Integrity, Not Secrecy',
   'items': ['One-way — the plaintext cannot be recovered from the digest',
             'Fixed length — any input yields a same-sized digest',
             'Avalanche effect — one changed bit transforms the whole digest',
             'Anti-collision — no two plaintexts are likely to share a digest',
             'The standards — SHA-256 or better; MD5 and SHA-1 are broken',
             'Uses — password storage, checksums, integrity verification'],
   'note': 'Hashing is integrity, not secrecy.'},
  'Hashing is a different job. A hash produces a fixed-length digest from a variable-length '
  'string, with cryptographic properties. It is one-way — the plaintext cannot be recovered from '
  'the digest. It is anti-collision — no two plaintexts are likely to produce the same digest. It '
  'also has the avalanche effect — change a single bit of the input and the whole digest changes, '
  'so even a tiny alteration is caught. secure hash algorithm-256, from the secure hash '
  'algorithm-2 family, produces a 256-bit digest and is secure for most modern use. MD5 and secure '
  'hash algorithm-1 are no longer considered secure against collision attacks. Hashing is used for '
  'password storage and checksums — integrity, not secrecy.'),
 ('bullets',
  {'kick': 'Algorithms',
   'title': 'Digital Signatures',
   'items': ['The recipe — hash the message, encrypt the hash with the private key',
             'Verification — decrypt with the public key and compare hashes',
             'Provides — integrity, authentication, non-repudiation',
             'In the wild — software signing and document verification',
             'The exam line — sign with private, verify with public'],
   'note': 'Only your private key could have created the signature.'},
  'Digital signatures combine hashing with public key cryptography. The recipe: hash the message, '
  'then encrypt that hash with your private key. To verify, the recipient decrypts with your '
  'public key and compares hashes. If they match, the message is intact and it came from you — '
  'because only your private key could have created the signature. A signature provides integrity, '
  'authentication and non-repudiation. You see this in the wild whenever software is signed: '
  'operating systems and app stores check the signature before they allow installation, protecting '
  'you from tampered code. The exam line: sign with private, verify with public.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Activity',
   'title': 'Which tool for which job?',
   'body': 'Bulk backup → symmetric. Contract integrity → hashing. Sender authentication → '
           'signature. Key exchange → asymmetric. Name the job before you name the tool.'},
  'Let us test the three-job map. Encrypting a large database backup — symmetric, for speed. '
  'Proving a contract was not altered — hashing, for integrity. Authenticating a sender beyond '
  'doubt — a digital signature. Exchanging a session key over an untrusted network — asymmetric. '
  'Name the job before you name the tool, and the answer falls out.'),
 ('chapter',
  {'num': 2,
   'of': 5,
   'title': 'Public Key Infrastructure',
   'blurb': 'Certificates, authorities, root of trust and revocation'},
  'Now we move from the algorithms to the infrastructure that makes them trustworthy. Chapter two '
  'is the public key infrastructure — the certificates, the authorities, the root of trust, and '
  'the way bad keys are revoked. This is how a public key is bound to an identity, and how you can '
  'trust that binding.'),
 ('bullets',
  {'kick': 'PKI',
   'title': 'Certificates and Certificate Authorities',
   'items': ['PKI — proves the identity of a public key holder',
             'Certificate authority (CA) — issues certificates to verified subjects',
             'Registration authority (RA) — verifies identities before the CA issues',
             'Third-party CA — an entity with widespread trust in its issuance policies',
             'The certificate — binds a public key to an identity'],
   'note': 'That binding is the whole point of PKI.'},
  'Public key infrastructure — public key infrastructure — proves the identity of a public key '
  'holder. The certificate authority, the certificate authority, is the repository of certificates '
  'and public keys issued to verified subjects. Working alongside it, the registration authority, '
  'the registration authority, acts as the intermediary — it handles the initial registration and '
  'identity checks before the certificate authority issues. A third-party certificate authority is '
  'an entity whose policies and procedures have earned widespread trust. The certificate itself '
  'binds a public key to an identity — and that binding is the whole point of public key '
  'infrastructure.'),
 ('bullets',
  {'kick': 'PKI',
   'title': 'Digital Certificates',
   'items': ["Contents — the subject's public key, identity, usage and validity",
             'Also carries — the issuing CA and its digital signature',
             'Standard — X.509, the certificate format',
             'Common Name (CN) — legacy FQDN field, deprecated but still used',
             'Subject Alternative Name (SAN) — modern field, multiple hosts, wildcards'],
   'note': 'CN vs SAN is a favourite exam distinction.'},
  "What is inside a certificate? The subject's public key, information identifying the subject, "
  'usage and validity — plus the identity of the issuing certificate authority and its digital '
  'signature, which is how the binding is vouched for. The standard is X.509. Two subject name '
  'attributes matter for the exam. Common Name, common name: the legacy way of recording the fully '
  'qualified domain name — deprecated by standards but still used. Subject Alternative Name, '
  'subject alternative name: the modern field — structured identifiers, multiple hosts and '
  'subdomains, and wildcard support.'),
 ('bullets',
  {'kick': 'PKI',
   'title': 'Root of Trust',
   'items': ["Root certificate — self-signed, trust in the CA's procedures is implicit",
             'Chain of trust — root CA → intermediate CAs → leaf certificates',
             'Subordinate CAs — certified by the root, scaling the hierarchy',
             'The model — you trust the root, which vouches for the intermediates',
             'No PKI — certificates can exist, but provide no root of trust'],
   'note': 'Trust has to start somewhere.'},
  'Trust has to start somewhere. The root certificate is self-signed — users must trust in the '
  "certificate authority's security procedures directly. The model is hierarchical: a root "
  'certificate authority issues certificates to intermediate certificate authorities, which issue '
  'leaf certificates to subjects. Subordinate certificate authorities are certified by the root or '
  'by another subordinate, which lets the hierarchy scale. You trust the root, and the root '
  'vouches for the whole chain below it. Without public key infrastructure you can still have '
  'certificates — but there is no root of trust to make them meaningful.'),
 ('bullets',
  {'kick': 'PKI',
   'title': 'The Certificate Signing Request',
   'items': ['Generate — the subject creates a key pair',
             'Send — the public key goes to the CA with a CSR, never the private key',
             'Verify — the CA or an RA performs identity checks',
             'Issue — the CA signs the certificate and publishes it',
             'Renew — re-verification before the validity period ends'],
   'note': 'Generate, send, verify, issue — and renew on time.'},
  'How does a certificate get issued? Generate: the subject creates a key pair. Send: the public '
  'key goes to the certificate authority with a certificate signing request — the certificate '
  'signing request. Note the critical rule: the subject never sends the private key; it stays with '
  'the subject. Verify: the certificate authority, or an registration authority on its behalf, '
  'performs identity checks. Issue: the certificate authority signs the certificate and publishes '
  'it. And because certificates expire, renewal re-verifies the holder before a new certificate is '
  'issued. Generate, send, verify, issue — and renew on time.'),
 ('bullets',
  {'kick': 'PKI',
   'title': 'Certificate Revocation',
   'items': ['Revocation vs suspension — permanent removal vs temporary hold',
             'CRL — certificate revocation list, checked by browsers and clients',
             'OCSP — online certificate status protocol, real-time per-certificate queries',
             'Why revoke — compromised keys, changed details, expired trust',
             'The lifecycle — issuance, renewal, revocation, expiration'],
   'note': 'A bad key must stop being trusted quickly.'},
  'Certificates can be revoked — and there are two mechanisms. Revocation means permanent removal; '
  'suspension is a temporary hold. The Certificate Revocation List, certificate revocation list, '
  'is a list of revoked and suspended certificates that browsers and clients check. The Online '
  'Certificate Status Protocol, online certificate status protocol, queries a single certificate '
  'in real time. Why revoke? Compromised keys, changed details, expired trust. Revocation is one '
  'stage in the certificate lifecycle — issuance, renewal, revocation, expiration — and it exists '
  'so that a bad key stops being trusted quickly.'),
 ('table',
  {'kick': 'PKI',
   'title': 'Key Management and Cryptoprocessors',
   'headers': ['Mechanism', 'What it is'],
   'rows': [['TPM',
             'Trusted Platform Module — cryptoprocessor on the motherboard; tamper-evident key '
             'storage and entropy for key generation'],
            ['HSM',
             'Hardware Security Module — dedicated or removable cryptoprocessor for key management '
             'at scale; reduced attack surface'],
            ['Key escrow',
             'Backup of keys with a trusted third party; M-of-N control splits recovery so no one '
             'agent acts alone'],
            ['Key lifecycle', 'Generation, storage, revocation, expiration, renewal']]},
  'Keys need secure handling. The trusted platform module — Trusted Platform Module — is a '
  'cryptoprocessor implemented on the central processing unit or motherboard, providing '
  'tamper-evident storage and entropy for key generation. The hardware security module — Hardware '
  'Security Module — is a dedicated or removable cryptoprocessor, or virtual appliance, managing '
  'keys at scale with a reduced attack surface. Key escrow backs up keys with a trusted third '
  'party — and M-of-N control splits recovery across multiple agents so no one person holds all '
  'the power. And the key lifecycle runs from generation through storage, revocation, expiration '
  'and renewal.'),
 ('callout',
  {'kind': 'info',
   'label': 'Discussion',
   'title': 'What does a website certificate actually prove?',
   'body': 'It proves the public key belongs to the named domain — not that the site is safe or '
           'legitimate. Trust in the CA chain is what makes the binding meaningful.'},
  'Here is a question worth pausing on. What does a website certificate actually prove? It proves '
  'the public key belongs to the named domain — nothing more. It does not prove the site is safe '
  'or legitimate. The chain of trust to a certificate authority is what makes the binding '
  'meaningful. Certificates prove identity and key binding; they do not vouch for content.'),
 ('chapter',
  {'num': 3,
   'of': 5,
   'title': 'Cryptographic Solutions',
   'blurb': 'Data at rest, in transit and in use'},
  'Chapter three is where cryptography is applied. We organise the solutions by data state — at '
  'rest, in transit and in use. Each state needs an appropriate control, and the exam expects you '
  'to match them. This is the practical half of the session.'),
 ('bullets',
  {'kick': 'Solutions',
   'title': 'Data States',
   'items': ['Data at rest — stored data, disks, databases, backups, files',
             'Data in transit — moving across a network, transport encryption',
             'Data in use — being processed in memory, the hardest to protect',
             'The rule — every state needs an appropriate control',
             'The exam — scenario questions match a state to a tool'],
   'note': 'State first, then tool — always.'},
  'Cryptography is applied by data state. Data at rest: stored — disks, databases, backups, files. '
  'Data in transit: moving across a network — protected by transport encryption. Data in use: '
  'being processed in memory — the hardest state to protect. The rule is simple: every state needs '
  'an appropriate control, and the exam expects you to match them. State first, then tool — '
  'always.'),
 ('bullets',
  {'kick': 'Solutions',
   'title': 'Disk and File Encryption',
   'items': ['Full disk / partition — encrypt the whole volume, often OS or firmware driven',
             'File and volume encryption — encrypt selected files or containers',
             'Self-encrypting drives — encryption performed by the drive firmware',
             'The benefit — a stolen drive yields nothing without the key',
             'At scale — BitLocker and FileVault protect at-rest data'],
   'note': 'A stolen drive yields nothing without the key.'},
  'Start with data at rest. Full disk and partition encryption encrypt the whole disk or partition '
  '— often performed by the operating system or software. Volume and file encryption protect '
  'selected files or containers. Self-encrypting drives perform encryption in the drive firmware. '
  'The benefit is simple: a stolen drive yields nothing without the key. At scale, BitLocker and '
  'FileVault protect at-rest data across an organisation.'),
 ('bullets',
  {'kick': 'Solutions',
   'title': 'Database Encryption',
   'items': ['Levels — database-level, table/column-level, cell/record-level',
             'Fine-grained access — column and record encryption enforce precise control',
             'DBMS support — the database management system decrypts as data moves to memory',
             'Compliance — supports privacy and security requirements',
             'The trade-off — fine granularity adds complexity and overhead'],
   'note': 'Structured data adds finer controls.'},
  'Structured data adds finer controls. Database-level encryption protects the whole database; '
  'table, column and cell-level encryption protect individual structures — pages, columns or '
  'records. The database management system decrypts as data moves from disk to memory, enforcing '
  'fine-grained access. This granularity supports compliance requirements for privacy and '
  'security. The trade-off: fine granularity adds complexity and overhead.'),
 ('bullets',
  {'kick': 'Solutions',
   'title': 'Transport Encryption and Perfect Forward Secrecy',
   'items': ['Transport encryption — protects data in transit, TLS, VPN tunnels',
             'Key exchange — asymmetric crypto exchanges symmetric session keys',
             'How TLS works — asymmetric handshake, then fast symmetric bulk encryption',
             'Perfect forward secrecy — session keys are ephemeral',
             'The result — recorded traffic stays encrypted even if keys leak later'],
   'note': 'PFS is a modern requirement, not a luxury.'},
  'For data in transit: transport encryption — transport layer security, virtual private network '
  'tunnels. transport layer security shows symmetric and asymmetric working together. In the '
  'handshake, asymmetric encryption securely exchanges a symmetric session key — the client '
  "encrypts it with the server's public key, the server decrypts with its private key — and then "
  'both sides switch to fast symmetric encryption for the session. And perfect forward secrecy '
  'matters: session keys are ephemeral, so even if one key is compromised later, it cannot decrypt '
  'past traffic. Recorded sessions stay secret. That is why perfect forward secrecy is a modern '
  'requirement, not a luxury.'),
 ('bullets',
  {'kick': 'Solutions',
   'title': 'Salting and Key Stretching',
   'items': ['The problem — passwords are low-entropy, brute force finds them',
             'Salting — add a random value per password before hashing, defeats pre-computed '
             'tables',
             'Key stretching — extra hashing rounds make each guess expensive',
             'Together — slower attacks, safer stored passwords',
             'Never plain — store only salted, stretched hashes'],
   'note': 'Salt plus stretch: slower attacks, safer storage.'},
  'Passwords need special treatment. The problem: user-generated passwords are low entropy, so '
  'brute force finds them. Salting adds a random value to each password before hashing — which '
  'defeats pre-computed hash tables, because every salted hash is unique. Key stretching adds '
  'extra hashing rounds, making each guess expensive for the attacker. Salt plus stretch: slower '
  'attacks, safer storage. And never store a password plain — store only salted, stretched '
  'hashes.'),
 ('bullets',
  {'kick': 'Solutions',
   'title': 'Blockchain and Obfuscation',
   'items': ['Blockchain — linked blocks of records, each hashed and chained, tamper-evident',
             'Steganography — concealing a message inside a cover file, often image LSBs',
             'Tokenisation — substituting sensitive data with tokens, reversible via the token '
             'server',
             'Data masking — redacting or obfuscating fields for display',
             'Code obfuscation — making code hard to understand, resisting reverse engineering'],
   'note': 'Recognition items — know what each does.'},
  'Two final technique areas. Blockchain: an expanding list of transactional records — blocks — '
  'each holding a list of transactions, a timestamp and a hash of the previous block. Alter one '
  'block and every subsequent hash changes, making tampering impractical. And obfuscation. '
  'Steganography conceals a message within a cover file — often hidden in the least significant '
  'bits of an image so the change is invisible to the eye. Tokenisation substitutes sensitive data '
  'with tokens, reversible only via the token server — think of a credit card number replaced by a '
  'stored token. Data masking replaces fields with realistic-looking values for display and '
  'testing. And code obfuscation makes software hard to understand, resisting reverse engineering. '
  'These are recognition items — know what each does.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Activity',
   'title': 'Match the technique',
   'body': 'Backup tape stolen → disk/file encryption. Web session must survive key compromise → '
           'perfect forward secrecy. Storing passwords → salt and stretch. Message hidden in a '
           'photo → steganography.'},
  'Let us consolidate with a quick activity. A backup tape is stolen — disk and file encryption '
  'protects data at rest. A web session must survive key compromise — perfect forward secrecy. '
  'Storing passwords — salting and key stretching. Hiding a message inside a photo — '
  'steganography. State first, then tool — always.'),
 ('chapter',
  {'num': 4, 'of': 5, 'title': 'Exam Alignment', 'blurb': 'How this session maps to the paper'},
  'Chapter four is exam alignment. We map everything you have learned onto the objectives of the '
  'paper, so you know exactly what the exam will test and how. Scenario questions throughout — '
  'which tool fits which job.'),
 ('table',
  {'kick': 'Exam Alignment',
   'title': 'What This Maps To',
   'headers': ['Objective', 'What the exam tests'],
   'rows': [['3.1 Cryptographic algorithms',
             'Symmetric, asymmetric, hashing; key length; digital signatures'],
            ['3.2 PKI & certificates',
             'CAs, X.509, root of trust, CSR, revocation, key management'],
            ['3.3 Cryptographic solutions',
             'Data states, disk/database/transport encryption, salting, PFS, obfuscation']]},
  'Here is the alignment with the paper. Objective 3.1, cryptographic algorithms — symmetric, '
  'asymmetric, hashing, key length, signatures; recognise advanced encryption standard for '
  'symmetric work, and rivest shamir adleman and elliptic curve cryptography for asymmetric. '
  'Objective 3.2, public key infrastructure — certificate authorities, X.509, root of trust, '
  'certificate signing request, revocation, key management. Objective 3.3, cryptographic solutions '
  '— data states, disk and database encryption, transport and perfect forward secrecy, salting, '
  'obfuscation. Scenario questions throughout: which tool fits which job.'),
 ('bullets',
  {'kick': 'Exam Alignment',
   'title': 'Check Your Understanding',
   'items': ['Open the session quiz in your browser',
             'Twenty questions, immediate feedback, exam-objective tag on every question',
             'Read each explanation — the distractors teach as much as the answer',
             'Score seventy percent or better before moving on'],
   'note': 'Every question maps to a CompTIA exam objective.'},
  'Now check your understanding. Open the session quiz in your browser. Twenty questions, '
  'immediate feedback, and every question is tagged with the exam objective it tests — you will '
  'see the tag, like 3.1 Cryptographic Algorithms, above each question. Read every explanation — '
  'the distractors teach as much as the answer. And aim for seventy percent or better before you '
  'move on.'),
 ('chapter',
  {'num': 5, 'of': 5, 'title': 'Consolidation', 'blurb': 'Key takeaways and what to revise'},
  'Chapter five is consolidation. We bring the session together into the key takeaways you should '
  'carry forward, and the revision checklist that turns this session into long-term recall.'),
 ('recap',
  {'title': 'Key Takeaways',
   'items': ['Symmetric for bulk, asymmetric for keys — one key is fast but hard to share; pairs '
             'solve distribution',
             'Hash for integrity, sign for identity — one-way digests; sign with private, verify '
             'with public',
             'Certificates bind keys to identities — X.509, CA chains, root of trust, CRL and OCSP',
             'Protect every data state — at rest (disk/file), in transit (TLS + PFS), in use',
             'Salt and stretch passwords — random salt plus extra rounds defeat brute force']},
  'Five takeaways. One: symmetric for bulk, asymmetric for keys — one key is fast but hard to '
  'share; pairs solve distribution. Two: hash for integrity, sign for identity — one-way digests; '
  'sign with private, verify with public. Three: certificates bind keys to identities — X.509, '
  'certificate authority chains, root of trust, certificate revocation list and online certificate '
  'status protocol. Four: protect every data state — at rest with disk and file encryption, in '
  'transit with transport layer security and perfect forward secrecy, and in use. Five: salt and '
  'stretch passwords — random salt plus extra rounds defeat brute force.'),
 ('bullets',
  {'kick': 'Consolidation',
   'title': 'Revision Checklist',
   'items': ['Retake the quiz until you score seventy percent without guessing',
             'Practise the jobs — for five data types, name the right crypto tool',
             "Inspect certificates — look at a browser certificate's SAN and chain",
             'Read ahead to Session 7 — identity and access management'],
   'note': 'This video is one revision pass — the quiz is the recall test.'},
  'Before you move on, make the learning stick. Retake the quiz until you score seventy percent '
  'without guessing. Practise the jobs — for five data types, name the right cryptographic tool. '
  "Inspect certificates — look at a browser certificate's subject alternative name and chain of "
  'trust. And read ahead to Session 7, where we control access: identity and access management. '
  'This video is one revision pass — the quiz is where you prove you can recall it.'),
 ('statement',
  {'kick': 'Next',
   'title': 'Session 7 — Identity & Access Management',
   'body': 'Authentication factors, password concepts, MFA, biometrics, tokens and federation. '
           'Cryptography gave us the tools; IAM decides who gets in.'},
  'That closes Session Six. You can now explain symmetric and asymmetric encryption and when to '
  'use each, hashing for integrity, digital signatures for authentication and non-repudiation, and '
  'the whole public key infrastructure world of certificates, certificate authorities, revocation '
  'and key management. Retake the session quiz until you score seventy percent without guessing. '
  'Cryptography has given you the tools; the next part of the course decides who gets in.')]

if __name__ == "__main__":
    total = sum(len(f[2].split()) for f in FRAMES)
    print("Session 6 narration: %d frames, %d words (~~%d min at 163 wpm)"
          % (len(FRAMES), total, round(total / 163)))

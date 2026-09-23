# narration_sec_s7.py — Security+ SY0-701 (revised), Session 7
# "Identity & Access Management"
# One-video-per-lesson format. Each frame: (template, payload, narration).
# Narration is read ALOUD IN FULL by ElevenLabs (Billy's voice) — short
# sentences that stand alone without the visual. Abbreviations are written
# so the engine reads them the way they are spoken in the classroom.
# USER RULES: no "good morning" (use "good day"); no courseware timing
# references — only the video's own length may be mentioned.

DECK = 'Identity & Access Management'
SESSION = 'Session 7 · Security+ SY0-701 (revised)'

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
   'title': 'Authentication & the Factors',
   'blurb': 'Who gets in, how they prove it, and the password layer'},
  'Good day, and welcome to Session Seven of the combined Network Fundamentals and CompTIA '
  'Security+ course. This session is Identity and Access Management — the layer every other '
  'control depends on. Session six gave us the cryptographic mechanisms. Now we put them to work '
  'at the gate: proving who you are, and limiting what you can do. Authentication establishes '
  'identity; authorisation limits action. Get this layer right, and the rest of the enterprise '
  'stands on solid ground.'),
 ('statement',
  {'kick': 'The Gatekeeper',
   'title': 'The Shape of the Session',
   'body': 'Authentication factors first, then password concepts and managers, then MFA and '
           'biometrics, then tokens. After that: account policies and authorisation, and finally '
           'single sign-on with federated identity.'},
  'Here is the shape of the session. We begin with the authentication factors — the building '
  'blocks of proving identity. Then password concepts, and password managers. Then multifactor '
  'authentication, and biometrics. Then hard and soft tokens. From there, account policies, and '
  'the authorisation models that limit what a proven identity may do. And we close with single '
  'sign-on and federated identity — the protocols that connect identity systems across '
  'organisations. Hold that map in mind, because each block builds on the last.'),
 ('bullets',
  {'kick': 'The Gatekeeper',
   'title': 'Session Objectives',
   'items': ['Name the authentication factors — know, have, are or do, somewhere',
             'Describe password concepts and managers',
             'Explain MFA and why two of the same factor is not MFA',
             'Compare hard and soft tokens, and biometrics',
             'Apply account policies and authorisation models',
             'Explain SSO and federation, and the protocols behind them'],
   'note': 'Six objectives — the quiz at the end tests every one.'},
  'By the end of this session you will be able to name the authentication factors — something you '
    'know, something you have, something you are or do, and somewhere you are. You will describe '
    'password concepts, and explain password managers. You will define multifactor authentication, '
    'and the trap of combining two factors of the same type. You will describe biometric '
    'authentication, including the false acceptance and false rejection rates. You will compare '
    'hard and soft tokens, and passwordless authentication. You will describe account types and '
    'account policies. You will explain the authorisation models. You will explain single sign-on '
    'and its concentration risk. And you will explain federated identity and the protocols behind '
    'it. Ten objectives, and the quiz at the end tests every one.'),
 ('bullets',
  {'kick': 'Authentication',
   'title': 'The Four Factors',
   'items': ['Something you know — password, PIN — the knowledge factor',
             'Something you have — token, smart card, phone — the ownership factor',
             'Something you are or do — fingerprint, face, voice — the biometric factor',
             'Somewhere you are — geolocation, IP or network location'],
   'note': 'The categories matter — MFA depends on them.'},
  'Authentication factors are the building blocks. Something you know: a password or a personal '
  'identification number — the knowledge factor. Something you have: a token, a smart card, or a '
  'phone — the ownership factor. Something you are or do: a fingerprint, a face, or a voice — the '
  'biometric factor. And somewhere you are: geolocation, an internet protocol address, or a '
  'network location. Four categories — and the categories matter, as we will see when we reach '
  'multifactor authentication, or M F A.'),
 ('bullets',
  {'kick': 'Authentication',
   'title': 'Password Concepts',
   'items': ['Length and complexity — long passphrases beat short complex ones',
             'Aging and history — rotation policies and reuse prevention',
             'NIST guidance — favour length, avoid forced periodic expiry, ban common passwords',
             'Password hints — a vector, avoid them entirely'],
   'note': 'The knowledge factor is the most common and the weakest.'},
  'Password policy is more nuanced than it used to be. Consider length and complexity. Long '
  'passphrases beat short, complex ones. Aging and history cover rotation policies, and reuse '
  'prevention. The National Institute of Standards and Technology — N I S T — now favours length '
  'over forced periodic expiry, and bans common passwords. And password hints? Treat them as a '
  'vector, and avoid them entirely. The knowledge factor is the most common. It is also the '
  'weakest, because phishing and data breaches harvest it easily. Which is exactly why we add '
  'other factors.'),
 ('bullets',
  {'kick': 'Authentication',
   'title': 'Password Managers',
   'items': ['Vault — one master password unlocks the store',
             'Generation — a unique, strong password per site',
             'Secure filling — credentials entered automatically, no typing, no keylogging',
             'Form factors — built-in OS or browser, or third-party cloud'],
   'note': 'One master password, unique everywhere else.'},
  'Password managers solve the reuse problem. A vault, protected by one master password, stores '
  'all your credentials. The manager generates a unique, strong password for every site. Secure '
  'filling enters the credentials automatically. No typing, and no keylogging. And consider the '
  'form factors. Built-in operating system and browser managers, or third-party cloud and '
  'plug-in tools. One master password, and unique everywhere else.'),
 ('bullets',
  {'kick': 'Authentication',
   'title': 'Multifactor Authentication',
   'items': ['The rule — MFA combines factors of different types',
             'Know plus have — a password and a token, that is MFA',
             'Know plus know — a password and a PIN is NOT MFA, same factor',
             'The exam trap — two factors must come from different categories'],
   'note': 'Same category twice is still one factor.'},
  'M F A has one rule that the exam loves. The factors must come from different categories. '
  'Something you know plus something you have — a password and a token — that is true M F A. '
  'Something you know plus something else you know — a password and a pin — is not M F A, however '
  'many items you add. Same category, twice, is still one factor. The exam trap is exactly this: '
  'two factors must come from different categories.'),
 ('bullets',
  {'kick': 'Authentication',
   'title': 'Biometric Authentication',
   'items': ['Enrollment — the sensor captures and extracts features',
             'False Rejection Rate (FRR) — Type I error, a genuine user is rejected',
             'False Acceptance Rate (FAR) — Type II error, an impostor is accepted',
             'The trade-off — tighten FAR and FRR rises; balance by context',
             'The strength — unique to the user and hard to replicate'],
   'note': 'A vault door can tolerate more friction than a phone unlock.'},
  'Biometrics authenticate by who you are. Enrollment captures the feature through sensors. Two '
  'error rates matter. The false rejection rate, or F R R, is a Type One error. It rejects a '
  'genuine user. The false acceptance rate, or F A R, is a Type Two error. It accepts an '
  'impostor. The two trade off. Tighten F A R, and F R R rises. The right balance depends on '
  'context. A vault door can tolerate more friction than a phone unlock. Their strength is that '
  'they are unique to the user, and difficult to replicate. Which is why they now sit in phones '
  'and secure facilities alike.'),
 ('table',
  {'kick': 'Authentication',
   'title': 'Hard Authentication Tokens',
   'headers': ['Token', 'What it is'],
   'rows': [['Smart card', 'Certificate-based credential requiring a reader'],
            ['OTP token', 'One-time password generator, hardware fob'],
            ['FIDO / U2F key', 'Security key; a presence gesture proves the user'],
            ['TOTP', 'Time-based one-time passwords from a shared secret']]},
  'Hard tokens are physical credentials. The smart card is a certificate-based credential that '
  'requires a reader. The one-time password token — O T P — is a hardware fob that generates '
  'one-time passwords. Then there is the Fast Identity Online and Universal Second Factor security '
  'key — FIDO, pronounced fido, and U two F. A presence gesture proves the user is there. And '
  'TOTP, or T O T P, generates time-based one-time passwords from a shared secret. Hard tokens '
  'are phishing-resistant, because the secret never leaves the device.'),
 ('bullets',
  {'kick': 'Authentication',
   'title': 'Soft Tokens and Passwordless',
   'items': ['Out-of-band — SMS, email, phone call, push — subject to interception',
             'Authenticator app — a software OTP generator on the device',
             'Passwordless — the authenticator holds the private key; biometric or PIN proves '
             'presence',
             'The direction — phishing-resistant methods over shared secrets'],
   'note': 'SMS is out-of-band but interceptable — prefer apps and FIDO.'},
  'Soft tokens live in software. Out-of-band channels — short message service, or S M S, email, '
  'phone call, and push notification — transmit codes, but they are subject to interception. '
  'Authenticator apps generate O T P codes on the device itself. Passwordless authentication '
  'relies on the authenticator holding a private key, with a biometric or a pin proving presence. '
  'The direction of travel is clear. Phishing-resistant methods, over shared secrets.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Quick Check',
   'title': 'Classify the factor',
   'body': 'A password plus a PIN — one factor, both knowledge. A smart card plus a fingerprint — '
           'two factors, possession and biometric. A push notification plus a password — two '
           'factors. Different categories, different factors.'},
  'Let us classify a few combinations. A password plus a pin. That is one factor, because both '
  'are knowledge. A smart card plus a fingerprint. That is two factors: possession and biometric. '
  'A push notification plus a password. That is two factors. The rule holds every time. '
  'Different categories mean different factors, and the same category twice is not M F A.'),
 ('chapter',
  {'num': 2,
   'of': 5,
   'title': 'Account Policies & Authorisation',
   'blurb': 'The lifecycle, the models, and guarding privileged access'},
  'Now we move from proving identity to managing it. Chapter two is account policies and '
  'authorisation. You will learn the account types, and the lifecycle that keeps them honest. The '
  'authorisation models decide what a proven identity may do. And we look at how privileged access '
  'is guarded. These are the policies that turn identity into controlled action.'),
 ('bullets',
  {'kick': 'Account Policies',
   'title': 'Account Types and Policies',
   'items': ['Account types — user, privileged or admin, service, shared, guest',
             'Provisioning — create, modify and remove accounts as roles change',
             'Lockout policies — thresholds and durations defeat password guessing',
             'Time-of-day restrictions — limit when accounts may be used',
             'Auditing — every account action is logged and reviewable'],
   'note': 'A dormant account is an open door — offboard promptly.'},
  'Now the policies around accounts, and the lifecycle that keeps them honest. Account types: '
  'user, privileged or admin, service, shared, and guest. Provisioning creates, modifies and '
  'removes accounts as people join, change role, and leave. Prompt offboarding is essential, '
  'because a dormant account is an open door. Lockout policies set thresholds and durations that '
  'defeat password guessing. Time-of-day restrictions limit when accounts may be used. And '
  'auditing logs every action. That is the accounting step of authentication, authorisation and '
  'accounting — often called triple A — and it is reviewable after the fact.'),
 ('bullets',
  {'kick': 'Authorisation',
   'title': 'Authorisation Models',
   'items': ['Permissions — every action checked against an allow or deny list',
             'Least privilege — the minimum access the role requires',
             'RBAC — role-based access, permissions to roles, users to roles',
             'ABAC — attribute-based, decisions use user, resource and environment attributes',
             'PAM — privileged access management guards admin accounts',
             'JIT access — elevated rights granted only when needed, then revoked'],
   'note': 'Roles for structure; attributes for granularity.'},
  'Authorisation decides what a proven identity may do. Permissions: every action is checked '
  'against an allow or deny list. Least privilege: grant the minimum the role requires. '
  'Role-based access control, or R B A C, attaches permissions to roles, and places users in '
  'roles. Attribute-based access control, or A B A C, makes decisions using attributes of the '
  'user, the resource, and the environment. Roles for structure. Attributes for granularity. And '
  'privileged accounts carry the greatest risk. So we guard them with privileged access '
  'management — P A M — using just-in-time access, password vaulting, and session recording.'),
 ('callout',
  {'kind': 'ok',
   'label': 'Quick Check',
   'title': 'Least privilege in practice',
   'body': 'A new analyst needs read access to three systems — grant exactly that. A contractor '
           'leaves next week — revoke today. A service account runs backups — no admin rights.'},
  'Let us apply least privilege. A new analyst needs read access to three systems. Grant exactly '
  'that, nothing more. A contractor leaves next week. Revoke access today, not at the end of the '
  'week. A service account runs backups. It should have no admin rights at all. When least '
  'privilege is ignored, one compromised account becomes a master key. Remember: least privilege '
  'is a process, not a setting.'),
 ('chapter',
  {'num': 3,
   'of': 5,
   'title': 'Single Sign-On & Federation',
   'blurb': 'One identity, many systems, and the protocols that connect them'},
  'Chapter three is single sign-on, and federated identity. Single sign-on lets one authentication '
  'open many applications. Federation extends that trust across organisational boundaries. And '
  'beneath both sit the protocols — security assertion markup language, OAuth, OpenID Connect, '
  'lightweight directory access protocol, and Kerberos — that connect identity systems together. '
  'This is where identity becomes an enterprise service.'),
 ('bullets',
  {'kick': 'SSO',
   'title': 'Single Sign-On',
   'items': ['The idea — one authentication grants access to many applications',
             'The benefit — fewer credentials, fewer resets, one logout',
             'Fighting fatigue — fewer passwords reduces poor password habits',
             'The risk — the SSO credential becomes a single point of failure',
             'The requirement — protect it with MFA and monitoring'],
   'note': 'SSO trades convenience for concentration — the protection effort must match.'},
  'Single sign-on, or S S O, lets one authentication grant access to many applications. The '
  'benefits: fewer credentials, fewer password resets, and one logout. It is also a real answer '
  'to password fatigue, where too many passwords drive people to reuse and weak choices. The risk '
  'is concentration. The single sign-on credential becomes a single point of failure, because '
  'compromising it opens every connected system. The requirement follows. Protect the S S O '
  'account with M F A and monitoring, and revoke it rapidly on compromise.'),
 ('bullets',
  {'kick': 'Federation',
   'title': 'Federated Identity',
   'items': ["The idea — trust relationships between organisations' identity systems",
             'Identity provider (IdP) — authenticates the user and issues a token',
             "Service provider (SP) — accepts the IdP's assertion",
             'Directory services — central stores, the source of truth',
             'The result — one identity works across organisational boundaries',
             'Identity governance — access reviews, policy enforcement and audit'],
   'note': 'Sign in once with your home organisation; partner systems trust it.'},
  'Federation extends identity across organisational boundaries. Trust relationships link '
  'identity systems. The identity provider, or I D P, authenticates the user, and issues a '
  'token. The service provider, or S P, accepts that assertion of identity. Directory services '
  '— Active Directory, lightweight directory access protocol, and Azure A D — are the central '
  'stores. The single source of truth for who users are. The result: one identity works across '
  'organisations. You sign in once with your home organisation, and partner systems trust it. '
  'Identity governance then reviews that access, enforces policy, and audits it.'),
 ('table',
  {'kick': 'Federation',
   'title': 'Protocols Behind the Curtain',
   'headers': ['Protocol', 'Role'],
   'rows': [['SAML', 'XML-based authentication and authorisation assertions for web SSO'],
            ['OAuth 2.0', 'Authorisation framework — delegated access to resources'],
            ['OpenID Connect (OIDC)', 'Identity layer built on OAuth 2.0 — user identity'],
            ['LDAP / Kerberos', 'Directory services and ticket-based authentication']]},
  'The protocols, at recognition level. Security assertion markup language, or S A M L, uses '
  'extensible markup language based assertions for web single sign-on. Authentication and '
  'authorisation. OAuth two point zero is the authorisation framework. It delegates access to '
  'resources, without sharing passwords. OpenID Connect, or O I D C, is the identity layer built '
  'on OAuth two point zero. It answers who the user is. Lightweight directory access protocol, '
  'or L D A P, provides directory services. Kerberos provides ticket-based authentication. Know '
  'which protocol does which job.'),
 ('callout',
  {'kind': 'warn',
   'label': "Analyst's Lens",
   'title': 'The concentration risk',
   'body': 'One credential, many systems — the blast radius of compromise is the whole estate. '
           'Mitigate with MFA, conditional access, monitoring, and rapid revocation.'},
  'What is the single biggest risk of an S S O deployment? It is the concentration risk. One '
  'credential, many systems. The blast radius of a compromise is the whole estate. The '
  'mitigations: M F A on the single sign-on account, conditional access, monitoring for unusual '
  'sign-ins, and rapid revocation. S S O trades convenience for concentration, and the '
  'protection effort must match the risk.'),
 ('chapter',
  {'num': 4, 'of': 5, 'title': 'Exam Alignment', 'blurb': 'What this session maps to in the paper'},
  'Chapter four is exam alignment. Identity and access management — I A M — is consistently '
  'examined, and the questions appear across multiple domains. Let us map what you have learned '
  'to the objectives the exam actually tests, so you know exactly where this session pays off.'),
 ('table',
  {'kick': 'Exam Alignment',
   'title': 'What This Maps To',
   'headers': ['Objective', 'What the exam tests'],
   'rows': [['4.1 Authentication',
             'Factors; password concepts; MFA; biometrics; tokens; passwordless'],
            ['4.2 Account policies & authorisation',
             'Account types; provisioning; lockout; least privilege; RBAC or ABAC; PAM'],
            ['4.3 SSO & federation',
             'SSO; IdP and SP; directory services; SAML, OAuth, OIDC, LDAP, Kerberos']]},
  'Here is the alignment. Objective four point one, authentication: factors, password concepts, '
  'M F A, biometrics, tokens, and passwordless. Objective four point two, account policies and '
  'authorisation: account types, provisioning, lockout, least privilege, R B A C and A B A C, and '
  'P A M. Objective four point three, single sign-on and federation: S S O, the identity provider '
  'and service provider, directory services, and the protocols — S A M L, OAuth, O I D C, '
  'L D A P, and Kerberos. I A M questions appear across multiple domains, so this session pays '
  'off repeatedly.'),
 ('bullets',
  {'kick': 'Exam Alignment',
   'title': 'The Exam Style',
   'items': ['Scenario questions — which factor, which policy, which protocol',
             'The MFA rule — different categories, not just two items',
             'RBAC versus ABAC — roles versus attributes',
             'Recognition level — know which protocol does which job'],
   'note': 'The quiz tags every question to its exam objective.'},
  'The exam style is scenario-based. It asks which factor, which policy, which protocol. The '
  'most tested concept is the M F A rule. Different categories, not just two items. R B A C '
  'versus A B A C is a favourite distinction. Roles versus attributes. And the protocols are '
  'recognition level. You need to know which protocol does which job. Every quiz question is '
  'tagged with the objective it tests, so you can trace your revision.'),
 ('chapter',
  {'num': 5, 'of': 5, 'title': 'Consolidation', 'blurb': 'Key takeaways and what to revise'},
  'Chapter five is consolidation. We bring the session together into the key takeaways you should '
  'carry forward, and the revision checklist that turns this session into long-term recall.'),
 ('recap',
  {'title': 'Key Takeaways',
   'items': ['Factors differ — know, have, are or do, somewhere — and MFA needs different '
             'categories',
             'Passwords need management — length over complexity, managers, no hints',
             'Tokens come in two flavours — hard and soft',
             'Authorisation limits access — least privilege, RBAC and ABAC, with lockout and time '
             'controls',
             'Privileged access is guarded — PAM, just-in-time rights and password vaulting',
             'SSO concentrates risk — federation extends identity across organisations, so protect '
             'the IdP']},
  'Six takeaways. One: factors differ — know, have, are or do, and somewhere — and M F A needs '
  'different categories. Two: passwords need management. Length over complexity, managers, and no '
  'hints. Three: tokens come in two flavours. Hard and soft. Four: authorisation limits access. '
  'Least privilege, R B A C and A B A C, with lockout and time controls. Five: privileged access '
  'is guarded. P A M, just-in-time rights, and password vaulting protect admins. Six: S S O '
  'concentrates risk. Federation extends identity across organisations, so protect the I D P.'),
 ('bullets',
  {'kick': 'Consolidation',
   'title': 'Revision Checklist',
   'items': ['Retake the session quiz until you score well without guessing',
             'Audit your MFA — which of your accounts use true multifactor?',
             'Map the models — find one RBAC and one ABAC example at work',
             'Read ahead to Session 8 — enterprise network and campus security'],
   'note': 'This video is one revision pass — the quiz is the recall test.'},
  'Before you move on, make the learning stick. Retake the session quiz until you score well '
  'without guessing. Audit your M F A. Which of your accounts use true multifactor? Map the '
  'models. Find one R B A C and one A B A C example at work. And read ahead to Session 8, where '
  'identity meets the network: enterprise network and campus security. This video is one '
  'revision pass. The quiz is where you prove you can recall it.'),
 ('statement',
  {'kick': 'Next',
   'title': 'Session 8 — Enterprise Network & Campus Security',
   'body': 'Architecture models and segmentation, switching and routing appliances, network access '
           'control, and secure remote access and tunnelling.'},
  'That closes Session Seven. You can now explain the authentication factors, password concepts '
  'and passwordless authentication. M F A and biometrics. Account policies, and S S O and '
  'federated identity. Retake the session quiz until you score seventy percent without guessing. '
  'Identity is the gatekeeper that decides who gets in.')]

if __name__ == "__main__":
    total = sum(len(f[2].split()) for f in FRAMES)
    print("Session 7 narration: %d frames, %d words (~~%d min at 163 wpm)"
          % (len(FRAMES), total, round(total / 163)))

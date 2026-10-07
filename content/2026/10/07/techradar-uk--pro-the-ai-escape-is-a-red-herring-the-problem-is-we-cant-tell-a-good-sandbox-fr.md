---
title: The AI escape is a red herring. The real problem is we can't tell a good sandbox
  from a bad one
source_url: https://www.techradar.com/pro/the-ai-escape-is-a-red-herring-the-problem-is-we-cant-tell-a-good-sandbox-from-a-bad-one
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-07T13:17:20Z'
published: '2026-10-07T00:00:00Z'
description: Scoring agent sandbox containment after the OpenAI escape
image: https://cdn.mos.cms.futurecdn.net/F8GmZXNJTQZttVhvkvgpp9-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- Hugging Face
- U.S
organisations:
- AI Risk Management Framework
- Cloud Security Alliance
- Coder
- Future plc
- Hugging Face
- Institute of Nuclear Power Operations
- L5
- MITRE ATLAS
- NIST
- OWASP
- OpenAI
- TechRadar Pro
- TechRadarPro
---

![Hacking red and blue digital binary code matrix 01 background.](https://cdn.mos.cms.futurecdn.net/F8GmZXNJTQZttVhvkvgpp9-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Not all sandboxes are created equal, and until recently there was no way to say so precisely. There is now.

Two OpenAI models escaped an evaluation sandbox, breached Hugging Face's production infrastructure and used the answer key to their own benchmark. The attack was novel and creative in how the models passed notes back and forth, complex multi-step escalations throughout. It's fair to conclude from this incident that frontier models are proficient at hacking and can be dangerous.

CEO of Coder.

But the breaking-out-of-the-sandbox notion is a red herring. If a sandbox is poorly constructed, as so many are, it’s easy to break out of. They don’t have the locked-down environments common at the network level such as access controls and separated privileges. This incident would have unfolded very differently with a properly configured sandbox.

If only some sandboxes are properly configured, how can you tell them apart? Let’s explore if anyone has come up with a real, testable definition of ‘sandboxed’.

## The landscape, briefly

Almost nothing written about agent security is a scoring standard for a single sandbox's containment architecture specifically.

OWASP's Agentic AI Top 10 and its Agent Security Cheat Sheet catalogue threats and mitigations at a high level, useful as a checklist, not built to produce a comparable score. NIST's AI Risk Management Framework operates a level above this entirely, more organizational risk governance, rather than a technical grading rubric for a runtime boundary.

MITRE ATLAS catalogues adversarial techniques against AI systems, closer to a threat library than a containment measure. The Cloud Security Alliance has several overlapping efforts, MAESTRO, an AI Controls Matrix, and an Agentic Trust Framework that scores autonomy on a four-stage ladder from Intern to Principal, the closest thing I found to one specific slice of what I was after, how much an agent can do without a human, but it isn't scoped to sandboxing as a whole.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

RAND's Securing AI Model Weights defines five security levels, but for weight theft and exfiltration risk at a lab, not for whether a given agent's runtime sandbox holds under an adversarial task. None of those take a single agent sandbox, break it into independent parts, score each part, and produce something you could compare across products.

Let’s look further.

## The agent sandbox taxonomy

Published in March 2026 and still under active community review, it organizes itself around a memorable ‘7-7-3’ (seven defense layers, seven threat categories, three evaluation dimensions). The layers are numbered bottom-up, because the lower ones are foundational:

· L1 Compute isolation

o What separates the agent's execution from the host?

· L2 Resource limits

o Can it exhaust CPU, memory, disk or time?

· L3 Filesystem boundary

o What can it read, write or delete?

· L4 Network boundary

o What can it communicate with?

· L5 Credential and secret management

o Can it see, use or exfiltrate credentials?

· L6 Action governance

o Can it perform destructive or unauthorized operations?

· L7 Observability and audit

o Can you see what it did, when, and why?

Each layer gets scored on Strength, 0 to 4, and Granularity, 0 to 3, plus a flat set of Portability tags for OS and infrastructure dependencies. The Strength scale is the part I like the most.

0 is no enforcement. 1 is cooperative enforcement; the sandboxed process can simply ignore or route around, as well as proxy environment variables and an opt-in convention. 2 is software-enforced by something the process can't bypass internally but an operator could reconfigure. 3 is kernel-enforced and irreversible once applied, namespaces, Landlock, seccomp-BPF. 4 is structural, the protected resource just doesn't exist inside the sandbox at all, a microVM, a credential proxy, no network device.

That scale is how we can properly distinguish locked-down environments. Every product gets a fingerprint, a CVSS-style vector showing strength at each layer in order. The taxonomy also maps its seven threats back onto specific layer combinations with explicit thresholds.

That means something like data exfiltration is addressed systematically, and not as a judgment call. It's a mechanical check against whether L3, L4 and L5 all clear a score of 2 or better. And critically, it comes with a composition framework. No single product covers all seven layers well, so the practical guidance is to stack products and take the maximum score at each layer rather than pretend one tool solves everything.

The project ships 26 real products scored, a verification probe you can run against an actual sandbox to check the claims, and an interactive explorer for comparing fingerprints side by side.

## The good, and the missing

Let’s return to the Hugging Face incident. The way the agent “escaped” its sandbox was to route around a proxy. That’s a service running in the sandbox. It is a fundamentally weaker guarantee than a boundary enforced below the application layer.

The Agent Sandbox Taxonomy gives that distinction a name and a number instead of leaving it as vibes. It's honest about its own limits; the project says outright which product scores are unverified. And the composition framework's core finding is the most useful thing in it for anyone assembling a stack. It shows that combining products both builds a better box and controls what's inside that box. Almost nobody does both.

Two blind spots stood out. The first is that there's no layer for what happens after containment fails. No kill switch, no automatic credential rotation on trigger, no forensic rollback runbook. It tells you whether an agent could plausibly be contained, not what happens in the window after it isn't. That window is exactly where the Hugging Face incident lived.

A kill switch is not a bad idea in principle. We need to be able to block frontier models that have proven they can escape and cause harm. The hard question is who initiates it, and how fast. It took two of the most advanced organizations in the world, OpenAI and Hugging Face, weeks to comb through the forensics of this attack. A centralized agency without frontier talent would take considerably longer.

We should take our lead from industry. In the U.S. the Institute of Nuclear Power Operations’ first line of defense is an automated control at the reactor core, the second is an onsite operator, and only the third is a centralized regulator whose job is primarily to audit the first two.

Agent infrastructure needs the same shape. Automated kill switches built into the model infrastructure, because nothing else moves fast enough. Safety officers at each lab empowered to take further action or initiate a manual shutdown. Standards set and audited above both.

The second blind spot is related. L7 scores whether logging exists and how tamper-evident it is, but not how fast an anomaly actually reaches a human. A system can score well on L7 and still take days to notice something. That appears to have happened here. Neither blind spot is a knock on the project. They're reasonable scoping choices for a v1, but they're the two places I'd want the standard to grow next.

## Running the incident

Here's the actual exercise: can I fingerprint that eval environment using public disclosures alone? Mostly no. That tells me that responsible disclosure is mature for something like a CVE, but not for a sandbox jailbreak.

Compute isolation was described only as ‘highly isolated,’ with no mechanism named. Resource limits and the filesystem boundary weren't addressed in the public writeup at all. The network boundary looks like a 2 and it didn't hold. A single proxy chokepoint was the sanctioned exit and a zero-day in it gave code execution, exactly the failure mode the S:2 tier warns is reconfigurable but not kernel-irreversible.

Credentials look like 0 or 1. Stolen credentials enabled lateral movement into Hugging Face's production systems, consistent with ambient, reachable credentials rather than a proxy or ephemeral tokens. Action governance was 0 or 1 by design. Guardrails were deliberately stripped for this evaluation to measure maximum capability. Observability was partial, logging existed and Hugging Face detected the intrusion independently, but nobody connected it to OpenAI's own telemetry quickly.

Run that through the taxonomy's own threat rules and data exfiltration can't be marked addressed with what's public, because the inputs were never disclosed. That's the value of the exercise. It lets you say precisely which of seven specific, falsifiable claims about a containment architecture were available and a way to request those that weren’t.

That tells me there is a standard definition of ‘sandboxed’, or at least close enough. But reading a fingerprint format is one thing and trusting it is another, especially when nearly every entry in the taxonomy's own dataset was inferred from documentation rather than hands-on testing. Next up is using the probe for verified scores.

None of which gets any individual organization off the hook while the standard matures. Determine your risk appetite. Put sensible auditing and controls into your own infrastructure. Be prepared with your own version of a kill switch.

And if your own agent's sandbox had to be fingerprinted against these seven layers in public, how would it score? Hopefully better than the one OpenAI used in this incident.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

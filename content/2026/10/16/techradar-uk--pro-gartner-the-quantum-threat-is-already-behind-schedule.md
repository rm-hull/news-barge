---
title: 'Gartner: The quantum threat is already behind schedule'
source_url: https://www.techradar.com/pro/gartner-the-quantum-threat-is-already-behind-schedule
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-16T11:17:28Z'
published: '2026-10-16T00:00:00Z'
description: Why post-quantum cryptography requires action now
image: https://cdn.mos.cms.futurecdn.net/d4oN2QTeNf8QYJDmjZnAKE-1920-80.jpg
categories:
- Technology & Software
- Science
people: []
locations: []
organisations:
- Amazon
- CIOs
- CISO
- Future plc
- Gartner
- Google
- IBM
- IT
- ITL
- TLS
- TechRadar Pro
- TechRadarPro
- Transport Layer Security
---

![Quantum computing](https://cdn.mos.cms.futurecdn.net/d4oN2QTeNf8QYJDmjZnAKE-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

For years, quantum computing lived in a strange place in the cybersecurity conversation: important enough to worry about, but sufficiently distant to leave for another day. When we asked CISO what's keeping them up at night, quantum computing rarely made the top five. It still feels distant, theoretical, someone else's problem for 2030-something.

That calculation is starting to look wrong.

Director Analyst within the ITL Application and Data Security research team at Gartner.

Gartner predicts that by 2030, advances in quantum computing will make conventional asymmetric cryptography unsafe to use. Four years away sounds like breathing room. It isn't. Replacing the cryptography embedded across a modern technology estate isn't a patch cycle. It's a multi-year transformation touching applications, infrastructure, identity systems, suppliers and developers all at once.

The clock is already running. Most organizations just haven't noticed it started or don’t appreciate how little time they really have.

## This was never really a technology question

Quantum innovation is moving at pace with IBM, Amazon and Google publishing roadmaps or breakthroughs on error correction and qubit stability. Taken together, they tell a consistent story: the timeline to a cryptographically relevant quantum computer is shrinking, not stretching.

But for the average enterprise, that's not the most useful question to be asking right now. The more useful question is far more uncomfortable: how much cryptography do we actually have, do we know where it lives, and could we change it if we had to?

Cryptography isn't a product category you can point to. It's woven into everything, buried in vendor software, embedded in Transport Layer Security (TLS) handshakes, quietly doing the work inside identity and access management systems nobody thinks about. Gartner's research puts a number on the blind spot: 61% of organizations lack full visibility into their own cryptographic systems.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

CIOs and IT leaders cannot migrate away from a risk they cannot see. That single statistic is arguably the real concern than the quantum breakthrough itself.

## The attack has already started

Here's the unnerving part. You don't need a working quantum computer today for the threat to be live today. Adversaries, particularly well-resourced state actors are already engaged in what the industry calls "harvest now, decrypt later": hoovering up encrypted data now, sitting on it, and waiting for the day decryption becomes trivial.

For anything with a long shelf life such as government records, medical files, IP, legal contracts, identity documents, a five-year-away breakthrough is still a today problem, because the theft happens now.

Encrypted securely today doesn't mean secure for the data's whole useful life. That's the sentence every chief information security leader should be testing their current strategy against.

## Crypto-agility is the actual prize

There's a temptation for CIOs and IT leaders to treat post-quantum cryptography as a swap: rip out an old algorithm, drop in a quantum-resistant one, done. It doesn't work that way. New algorithms aren't drop-in replacements.

Larger key sizes strain memory on older systems, signing operations run at different speeds, and performance assumptions baked into legacy applications quietly break. Moreover, additional standards are still being developed meaning today’s replacement might be tomorrow’s cryptographic debt.

Which is why the capability that actually matters isn't any specific algorithm. It's crypto-agility - the ability to change cryptographic algorithms, keys and protocols quickly, without re-engineering the business around them. And organizations are starting to focus on building it, alongside prototyping or evaluating post-quantum algorithms outright.

Build crypto-agility properly and you're not just preparing for quantum. You're fixing something older: cryptographic technical debt that would have caused pain at the next major algorithm weakness regardless of what triggered it. Quantum is the deadline. Technical debt is the disease.

Additionally, hybrid cryptography which blends classical and post-quantum mechanisms during the transition buys some breathing room. Treat that as scaffolding, not a destination. Classical methods have a shelf life measured in single-digit years.

## Why now, when nobody can predict the exact date

There's an understandable instinct to wait for certainty, to see exactly when a cryptographically relevant quantum computer arrives before committing budget. That instinct is the wrong strategy for a transformation measured in years, not sprints.

Organizations don't need to know the date. They need to start building visibility and flexibility now, so they can act when required. The unglamorous first step: build an inventory. Scan the estate, catalogue every cryptographic component, feed the findings into whatever technical-debt dashboard has executive attention. It surfaces expired algorithms, outdated TLS versions and vendor dependencies — and gives the migration a factual basis instead of a guess.

Then prioritize. A marketing database that's stale in eighteen months carries a very different risk profile to a decade-long government contract or an identity credential meant to last a generation. Ask which information still needs protecting after 2030. That list moves to the top. Then ask which use cases could disable the business and tackle those next.

## This cannot be handed to the security team

A mistake is treating post-quantum migration as a security project with a security owner. It isn't. Developers need to understand how algorithm changes hit application performance. Cloud and network teams inherit protocol changes. Identity teams own the authentication dependencies.

Procurement needs to interrogate vendors on their own timelines, because a huge share of enterprise cryptography arrives bundled inside third-party software nobody directly controls.

Equally, pushing this down to individual system owners without central coordination is a guaranteed way to fail, leading to inconsistent decisions, no organization-wide picture of progress, and gaps precisely where attackers look first.

A cross-functional Cryptographic Centre of Excellence, pulling IT, development and data security under one roof, isn't governance theatre. It's what keeps the response from fragmenting into a patchwork.

## The real question isn't about quantum at all

Strip away the acronyms and this stops being a story about qubits. It becomes a test of how resilient an organization's architecture actually is, whether it knows where its cryptography sits, understands which data needs long-term protection, and can change cryptographic mechanisms without rebuilding from scratch.

The organizations most exposed won't be the ones with the weakest algorithms. They'll be the ones still treating quantum as a distant technology story rather than a resilience problem sitting on today's books. By the time the threat is obvious to everyone, the hard part—untangling years of cryptographic dependencies—will already be behind schedule.

The quantum era is still approaching. The migration effort isn't.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

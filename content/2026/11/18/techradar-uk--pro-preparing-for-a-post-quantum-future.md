---
title: Preparing for a post-quantum future
source_url: https://www.techradar.com/pro/preparing-for-a-post-quantum-future
source_site: TechRadar UK
source_slug: techradar-uk
description: '"Q-day" is a very real approaching reality'
image: https://cdn.mos.cms.futurecdn.net/d4oN2QTeNf8QYJDmjZnAKE-1920-80.jpg
published: '2026-11-18T00:00:00Z'
scraped_at: '2026-11-18T11:32:57Z'
categories:
- Technology & Software
people: []
locations:
- Willow
organisations:
- AI
- AWS
- CISOs
- CTO
- Future plc
- Google
- NCSC
- NHS
- National Cyber Security Centre
- OSWAP
- RSA
- Roke
- TechRadar Pro
- TechRadarPro
- US Department of War
---

![Quantum computing](https://cdn.mos.cms.futurecdn.net/d4oN2QTeNf8QYJDmjZnAKE-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Quantum computing is one of the most significant technological leaps in human history. Although it has the potential to revolutionize drug discovery, climate modelling, and material science, there also lies an uncomfortable reality in this powerful technology: the undeniable risk that it could be weaponized to break the digital locks protecting our most sensitive data.

CTO at defense and national security company Roke.

Security experts have coined this breaking point “Q-Day“ and, according to recent research, new estimates suggest that some crypto-secure systems may be vulnerable to quantum-powered break-ins far sooner than we initially expected. While general-purpose quantum machines may still be five to ten years away, nation states and cybercriminals are already stockpiling data now, with plans to decrypt it later.

So, the threat is very real even in 2026. In recent weeks, the US Department of War has reportedly been searching for interim software-only cryptographic solutions as part of its transition to post-quantum cryptography.

However, this threat is not on the radar of many CEOs, and certainly not a high priority if it is. Given the risks at stake here, becoming educated on the threats posed by quantum hackers and understanding how sensitive data could one day be at risk is essential for future-proofing businesses against this threat. Acting now will help to protect against potentially huge security and brand reputation risks further down the line.

## Why does quantum create new threats and how will cybercriminals get access?

Quantum computers differ from existing, classical computers in their ability to solve computational problems in a fraction of the time, including cracking some types of encryptions. For example, Google’s Willow chip, developed in 2024, could take five minutes to complete a task that would take the fastest supercomputers 10 septillion years to complete (written out, that’s 10,000,000,000,000,000,000,000,000 years).

However, it’s worth noting that was a benchmark with no specific practical application. To understand the scale of this threat, we must first consider how current digital security works. RSA asymmetric encryption, one of the foundations of internet security, works because it is easy to multiply two large prime numbers together but more difficult to identify these later, if only given the result of the multiplication. Other common algorithms are based on the ‘discrete logarithm’ problem.

While, classical computers would need thousands of years to factor a large composite number into its prime components, a quantum algorithm exists with the potential to solve this problem in only hours or days. Willow has around 105 qubits; breaking RSA-2048 would need a far larger machine.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

But this leads us to the question – how will cybercriminals get hold of this information? The simple answer is through economics. We saw this play out with the advent of AI. Originally, there was a select group of people working on specific Graphics Processing Units (GPUs). But these weren’t scalable. Fast forward to today and businesses can buy an AWS cloud service that creates GPUs almost instantly.

We can extrapolate this to quantum computing. Quantum hardware is already sold by the hour through cloud services. As machines mature, expect the same model to put powerful ones within reach of anyone who can pay. That is how criminals will get access.

## Why is this a problem for today?

Anything that relies on vulnerable asymmetric cryptographic algorithms, like the one described above, will quickly become easy to compromise. Just a few examples of these include diplomatic cables that shape international relations, NHS health records, the banking infrastructure underpinning our financial system, intellectual property, and state secrets.

Meaning all of these vital parts of society could be exposed by a quantum hacker. And it doesn’t end with decryption, RSA is used to sign the digital certificates that computers use to prove their identity. This means that breaking RSA would allow a hacker to forge digital certificates, undermining online trust.

## The ‘harvest now, decrypt later’ strategy

So, if working quantum computers are on the horizon but not yet here, why does the risk need to be on the C-suite agenda right now? To put it simply, adversaries don’t need working quantum computers to pose a danger today. This is because they’re already implementing ‘harvest now, decrypt later’ strategies.

Right now, sophisticated nation-state actors and high-end contractors are stockpiling encrypted data. To do this, they’re intercepting communications, stealing encrypted databases, and hoarding digital assets they can’t yet decrypt. But they’re playing the long game, because the data being stolen today will still be sensitive, valuable, and damaging when quantum computers become available to them.

## How can businesses protect against quantum attacks?

Despite the quantum threat being a topic of discussion for years, not all businesses are planning for a post-quantum future. Quantum risk assessments regularly reveal that both CEOs and CISOs are more focused on immediate concerns such as ransomware, data breaches, and regulatory compliance. These are issues that demand attention now and need to remain at the front of a CISO’s mind. But the quantum threat adds a new challenge to how we think about and manage data security.

Becoming quantum-safe is a complex, multi-year effort that businesses must begin now. It requires careful planning, testing, and integration across an entire technology stack. Last year, the National Cyber Security Centre (NCSC) issued guidance recommending that large companies, including energy and transport providers, introduce postquantum cryptography (PQC) measures, as they “will be a key part of defense in the coming years”.

These are encryption methods designed to resist attacks from both classic and quantum computers, but PQC integration is not a trivial task.

## Preparing for quantum safety

The NCSC’s strategy highlights the importance of early preparation and sector-specific plans to ensure a smooth PQC transition. This is a big technology transition, involving business-wide management and affecting supply chains. Getting this transition wrong risks introducing new vulnerabilities as unwanted side-effects.

We must not forget that in 2021 OSWAP designated ‘cryptographic failures’ as the second biggest security concern. Implementing cryptography is hard, and a major transition of cryptography is something to plan, deliver, and assure with care.

As a first step, every organization must understand which parts of its operations rely on quantum-vulnerable encryption and therefore which assets need protection. This is essential for businesses and governments to build the right defenses.

By 2028, every organization should have completed discovery and have a migration plan, with priority systems moved by 2031 and everything by 2035. This involves identifying priorities and setting clear goals within timelines. This should not be static but continually updated to ensure a thorough and effective transition.

Cross-industry partnerships will also be crucial to accelerate readiness. Sharing best practices, threat intelligence, and technical solutions will help to prepare against the quantum threat.

“Q-day” is not a distant theoretical concept but a very real approaching reality that demands an immediate strategic response from businesses and government for our protection. Proper preparation, strategic thinking, and commitment to strict timelines will allow businesses to be confident that they are quantum safe.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

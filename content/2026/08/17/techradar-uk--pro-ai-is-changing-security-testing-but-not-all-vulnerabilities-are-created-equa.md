---
title: AI is changing security testing, but not all vulnerabilities are created equal
source_url: https://www.techradar.com/pro/ai-is-changing-security-testing-but-not-all-vulnerabilities-are-created-equal
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-17T16:40:53Z'
published: '2026-08-17T00:00:00Z'
description: AI accelerates security testing, but hardware vulnerabilities still demand
  specialist expertise
image: https://cdn.mos.cms.futurecdn.net/5rDPr5xYvLwnkP7ZvpR2w3-2122-80.jpg
---

![Caution sign data unlocking hackers. Malicious software, virus and cybercrime, System warning hacked alert, cyberattack on online network, data breach, risk of website](https://cdn.mos.cms.futurecdn.net/5rDPr5xYvLwnkP7ZvpR2w3.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Artificial intelligence is rapidly reshaping cybersecurity. Much of the conversation has focused on how large language models are helping developers write code, but a more significant shift may be occurring elsewhere: security testing.

AI systems are becoming remarkably effective at identifying vulnerabilities, forcing organizations to rethink how they evaluate the security of both software and hardware products.

Vice President of Product Security & Innovation at PQShield.

The reason lies in the nature of modern software. Large codebases are sprawling ecosystems of interconnected modules, third-party dependencies, legacy components, and undocumented assumptions.

Security flaws often emerge not from a single defective function, but from subtle interactions between components that may be separated by hundreds of files or years of development history. Human reviewers excel at deep analysis, but they are constrained by time and cognitive bandwidth.

AI systems, by contrast, can rapidly traverse vast amounts of code, correlate information across repositories, and identify patterns associated with known vulnerability classes.

## Common software weaknesses

This capability is particularly powerful for common software weaknesses such as memory-safety issues, race conditions, authentication flaws, insecure API usage, and privilege-escalation paths. In many cases, AI is acting as an amplifier for established security techniques rather than inventing new ones. Yet the result is still significant: vulnerabilities that previously required substantial manual effort to uncover can now be identified at a much greater scale and speed.

The implications for product security are profound. Organizations can no longer assume that obscure vulnerabilities will remain undiscovered because finding them is too expensive. The cost of vulnerability discovery is falling, and it is falling for defenders and attackers alike. Security testing therefore becomes less about achieving a point-in-time assessment and more about maintaining continuous assurance throughout the development lifecycle.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

However, it would be a mistake to assume that all areas of cybersecurity will be transformed equally by AI. Hardware security, particularly side-channel analysis of cryptographic implementations, presents a very different challenge.

Unlike general-purpose software systems, cryptographic implementations operate within a comparatively narrow and mathematically defined problem space. Side-channel attacks do not typically exploit unexpected program behavior or complex interactions between software components. Instead, they target subtle information leakage through physical phenomena such as execution timing, power consumption, or electromagnetic emissions.

The challenge is not understanding millions of lines of source code; it is extracting meaningful signals from carefully collected measurements and applying sophisticated statistical techniques to reveal hidden secrets.

## Side-channel analysis

This distinction matters because many of the strengths that make large language models effective in software security are less relevant in side-channel analysis. LLMs excel at connecting information across large bodies of text and code, identifying relationships that humans may overlook.

Side-channel research, by contrast, already relies heavily on structured datasets, statistical processing, signal analysis, and deep domain expertise. AI can certainly accelerate parts of the workflow—from automating experimentation to assisting with data interpretation—but the advantage is typically more incremental than transformational.

That does not make hardware security less important. If anything, it highlights the need for specialized testing approaches. As AI lowers the barriers to software vulnerability discovery, organizations may be tempted to assume that automated tools alone can provide comprehensive assurance.

The reality is that different classes of vulnerabilities require different forms of expertise. An AI-assisted code review may uncover a memory corruption bug, but it is unlikely to replace the specialist knowledge required to evaluate whether a cryptographic implementation leaks secrets through power analysis.

The broader lesson is that security testing is becoming more important, not less. AI is increasing the speed at which vulnerabilities can be found, but it is not eliminating the need for expert analysis. Instead, it is changing where that expertise delivers the most value.

Organizations that combine AI-assisted testing with rigorous human-led security evaluation will be best positioned to address the evolving threat landscape—whether the target is a cloud application, an embedded device, or the cryptographic hardware that underpins digital trust.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

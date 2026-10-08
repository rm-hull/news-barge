---
title: The most dangerous attacker of the past year looked completely ordinary
source_url: https://www.techradar.com/pro/the-most-dangerous-attacker-of-the-past-year-looked-completely-ordinary
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-08T10:32:03Z'
published: '2026-10-08T00:00:00Z'
description: AI cyberattacks demand behavioral detection beyond traditional indicators
image: https://cdn.mos.cms.futurecdn.net/U76sZeRd6fS2fKt5RqBYPL-2560-80.jpg
categories:
- Technology & Software
people:
- David Bianco
locations:
- AI
organisations:
- AI
- APEX
- Anthropic
- Cribl
- Future plc
- IOC
- MITRE ATT&CK
- Pyramid of Pain
- TechRadar Pro
- TechRadarPro
---

![Big letters AI in pink in front of pink and blue strands of light suggesting a digital explosion](https://cdn.mos.cms.futurecdn.net/U76sZeRd6fS2fKt5RqBYPL-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

When Anthropic's threat intelligence team ranked a year of AI-enabled cyberattacks, the most dangerous operation in the dataset didn't stand out by the measure the security industry has relied on for years.

Mapped against MITRE ATT&CK, the state-sponsored espionage campaign Anthropic disrupted in November 2025 used 30 techniques across 13 tactics, comparable to many medium-risk actors in the same dataset. Against Anthropic's own risk methodology, the same campaign scored the maximum of 100.

Senior Director, Security Engineering & Operations at Cribl.

The fact that the highest-risk actor looked unremarkable by technique count exposes a weakness in conventional detection thinking. Technique breadth alone tells defenders relatively little about risk. More useful insight comes from understanding how techniques are combined, sequenced and executed over time.

## The indicator was always the fragile part

Security operations spent two decades getting very good at recognizing evidence an attacker had already used. Malware hashes, malicious IP addresses and suspicious domains gave teams a practical way to identify known threats and block repeat attacks. Once an attacker exposed part of their infrastructure, thousands of organizations could benefit.

David Bianco's Pyramid of Pain outlined this weakness in 2013. The indicators defenders find easiest to consume are also the cheapest for attackers to discard. A hash can change when you modify a file, while an IP address can simply be replaced. The techniques and procedures an attacker relies on to reach an objective are far harder to change.

Generative AI has made indicator-based detection more vulnerable by driving down the cost of variation. Code-generation tools can produce new malware variants quickly, phishing content can be created at scale, and offensive tooling can be assembled with far less specialist effort. Defenders increasingly work with indicators whose useful life may be shorter than the process required to identify, publish, and act on them.

None of which retires the IOC feed. It remains valuable for blocking known-bad in volume, enriching investigations and hunting retrospectively once a campaign becomes public. What it can no longer do is carry the weight of the detection program.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Individual techniques are weak signals

Anthropic’s study examined 832 accounts banned for malicious cyber activity between March 2025 and March 2026, mapping 13,873 observed actions across 482 techniques and all 14 ATT&CK tactics. The accounts represent a subset of total bans with enough detail for thorough assessment.

There was little correlation between an actor's skill and the number of techniques they used: the least capable actors in the dataset averaged around 16 distinct techniques, the most capable around 20. The platform an attacker worked through made no difference either.

That tracks with how enterprise environments actually behave. Account discovery appears in attacks, and also in legitimate administration. Remote services enable lateral movement and routine infrastructure management alike. Almost every individual technique requires interpretation before it supports a conclusion.

The information appears when activities connect. Account discovery, followed by credential access, followed by movement into another system and data staging within a compressed window, describes something the same activities spread across several days of routine work do not. Sequence becomes part of the detection logic, along with the identity involved, the systems touched, and what happened immediately afterwards.

## AI is moving deeper into the attack

AI introduces another consideration: the speed at which an attack unfolds. Automation can compress the time between actions, changing how otherwise familiar activity should be interpreted.

Human-led attacks have always used some degree of automation, but an operator still has to interpret results and decide what to do next. As AI systems take on more of that decision-making, the time between stages of an attack can shrink considerably. That makes the speed and sequence of activity useful information in its own right.

Anthropic's data shows where this pressure is being applied. Across the study period, AI use shifted away from gaining access and toward what happens after. Use of AI tools for account discovery inside compromised environments rose 8.9 percent while AI-assisted phishing fell 8.6 percent. Post-compromise techniques that once demanded real expertise are being performed on behalf of less capable actors.

The proportion of actors Anthropic classified as medium risk or higher rose from 33 percent in the first half of the study to 56 percent in the second, roughly a 1.7-fold increase in twelve months.

Speed alone proves nothing. A sequence plausible over several hours from an administrator carries different weight when the same actions cross multiple systems in minutes. Time belongs in the detection model alongside the activity.

This is the thinking behind APEX, or Adversarial Pattern Extraction and Correlation, a behavioral detection framework developed around the Anthropic findings. Rather than treating an individual ATT&CK technique as the unit of detection, APEX looks at combinations of techniques, the order in which they occur, the time between them and the entities involved.

The premise is that these behavioral chains provide a more durable basis for detection than the individual indicators or techniques attackers can change more easily.

## The frameworks have not caught up either

Anthropic's research also exposes a limitation in the frameworks used to describe attacker behavior. MITRE ATT&CK can map the individual techniques used during an intrusion, but it does not currently capture the agentic orchestration that links those techniques together.

An AI system that interprets results, selects its next action and moves through multiple stages of an attack with limited human involvement is therefore difficult to represent within the existing framework. Anthropic is now working with MITRE on how that behavior could be incorporated.

For security leaders, the practical consequence arrives sooner than any framework revision. Recognizing a behavioral chain means correlating evidence across endpoints, identities, networks and cloud platforms, each producing telemetry in a different shape.

That is a substantially harder data problem than checking a value against a list, and it is worth asking whether the telemetry required to see those chains is available, correlated and timely, rather than assuming volume will suffice.

## What attackers cannot change

AI makes an attack's observable features easier to change, but the underlying operational requirements remain relatively stable. An attacker seeking to steal data still needs to gain access, understand the environment, obtain sufficient privileges and move information out. The tools and infrastructure may vary, but those requirements are much harder to eliminate.

Bianco pointed to the industry at the top of the pyramid more than a decade ago, and the principle has held. Frameworks such as APEX are now attempting to turn that principle into practical detection logic by focusing on the sequence, timing and context of attacker behavior. AI has made that work considerably more urgent.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

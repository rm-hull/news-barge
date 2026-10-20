---
title: Chinese hacker hits over 100 company websites using AI agents — Deere and SharkNinja
  among top brands affected in attack
source_url: https://www.techradar.com/pro/security/chinese-hacker-hits-over-100-company-websites-using-ai-agents-deere-and-sharkninja-among-top-brands-affected-in-attack
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-20T14:22:37Z'
published: '2026-10-20T00:00:00Z'
description: It seems the goal was to establish persistence
image: https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg-1376-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Cairn
- Claude Code
- Fageraland
- SharkNinja
- Snorre Fagerland
locations:
- AI
- Australia
- Canada
- Japan
- NorForge
- United States
organisations:
- AI
- Cairn
- Cummins
- Cybersecurity News
- Deere
- Reuters
- SharkNinja
- TechRadar Pro
---

![an ai agent sat at a laptop](https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg-1376-80.jpg)

* **A hacker used AI agents to target more than 1,200 websites, compromising over 100 in under a month**
* **Autonomous agents tested vulnerabilities, adapted tactics, and established access with minimal human input**
* **Researchers warn AI-powered attacks are making large-scale website compromise faster and cheaper**

In less than a month, a single Chinese hacker managed to break into more than 100 company websites, while doing almost none of the work himself. Instead, he tasked AI agents to do it for him and paid them around $5,000 in tokens for the job.

The campaign was spotted by cybersecurity researcher Snorre Fagerland from NorForge, who was looking for exposed Cairn installations when he found approximately two dozen being used for malicious purposes. These gave him first-hand insight into an active cybercriminal operation.

Cairn is described as an open source, general-purpose AI problem-solving engine, designed to help autonomous agents find solutions to complex tasks. Instead of focusing on a single application, Cairn provides a framework that defines goals, explores different approaches, and then executes actions to try and solve the problem. According to numerous media outlets, Cairn is quite popular in the cybercriminal community (although it’s not malicious by design).

## When security becomes a problem needing solving

In this case, the “problem” Cairn was trying to solve for the attacker was how to run code on a website without signing in. They were trying out SQL injection, file uploads, as well as unsafe handling of stored objects. The goal, according to the researcher, was to establish persistent access to shopping and payment systems which could later be used to steal money.

Fagerland said the attacker used a combination of models, likely Claude Code with a DeepSeek model, although it is very difficult to determine. The instructions themselves were very brief, generally fewer than 100 Chinese characters, and in less than a month, the agents tried to break into more than 1,200 sites.

On average, the agents poke around a website for a day (23 hours), before either breaking in or moving on. With some 100 successful break-ins, Fagerland says the hacker paid $50 for tokens on average, per breach. This, however, is an estimate and not a confirmed billing.

The analyst did not name the victims. In its report, Cybersecurity News said the victims were mainly online stores in the United States, Canada, Australia and Japan, and Reuters managed to confirm some targets by “independently reviewing the hacker's Cairn activity”: including Deere (farm equipment maker), SharkNinja (home appliance ​company), and Cummins (engine manufacturer). It added that two “smaller businesses” also acknowledged being compromised but did not reply to the agency’s inquiries.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Impressive technique

Deere told *Reuters* it took “necessary remediation actions” and added that there was “no indication that sensitive information was accessed.” SharkNinja said the breach hit a standalone site carrying product support information only, and that the threat had been remediated. Cummins just said it was looking into reports.

So far, no one knows if the attacker managed to steal any sensitive data from his victims, and if so - how many. The researcher apparently found “hundreds” of exposed secrets in the open panels and was working with Reuters to let the victims know.

Fageraland told Reuters he was “impressed” by some of the techniques the agents used while compromising their victims. Apparently, after hitting a dead end against one of the targets, the AI agents scanned digital records in search of associated infrastructure. When they found a public-facing control panel, they discovered a “subtle weakness” in how it processed data. It took “hours of trial and error” before finally being able to execute a malicious command on the website’s server.

"It's ⁠not straightforward to come up with solutions like that," Fagerland said. "It's not script kiddie stuff."

AI attackers are the new normal, it seems. Business owners are advised to patch public-facing applications, restrict access to admin panels, and keep an eye on unexpected files in web directories.

*Via* * Tom's Hardware*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

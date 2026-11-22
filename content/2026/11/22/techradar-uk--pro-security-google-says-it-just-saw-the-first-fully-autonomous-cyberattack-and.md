---
title: Google says autonomous AI tools can now exploit fresh patches in minutes
source_url: https://www.techradar.com/pro/security/google-says-it-just-saw-the-first-fully-autonomous-cyberattack-and-says-a-significant-threshold-has-been-crossed-in-terms-of-cybersecurity
source_site: TechRadar UK
source_slug: techradar-uk
description: Hackers are hijacking cloud AI accounts to rack up $100,000 daily bills
  and resell stolen tokens on the dark web 'LLM Mixers.'
image: https://cdn.mos.cms.futurecdn.net/5rDPr5xYvLwnkP7ZvpR2w3-2122-80.jpg
published: '2026-11-22T00:00:00Z'
scraped_at: '2026-11-22T19:30:22Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Mandiant
locations: []
organisations:
- APIMart
- ARTEX
- CAIRN
- Claude Code
- CyberStrikeAI
- Google Threat Intelligence Group
- Greynoise
- HexStrike AI
- MIDNIGHT NEPTUNE
- Mandiant
- PentAGI
- TechRadar Pro
---

![Caution sign data unlocking hackers. Malicious software, virus and cybercrime, System warning hacked alert, cyberattack on online network, data breach, risk of website](https://cdn.mos.cms.futurecdn.net/5rDPr5xYvLwnkP7ZvpR2w3-1920-80.jpg)

* **Google uncovered an AI system finding flaws and launching exploits autonomously**
* **Cybercriminals are moving from chatbot assistance toward independently operated attack systems**
* **An exposed server revealed software designed to automate vulnerability research and exploitation**

Google researchers have reported that cybercriminals have moved past supervised chatbots and now run software that discovers, builds, and runs exploits autonomously.

The Google Threat Intelligence Group and Mandiant call this change a significant threshold, saying machine-speed intrusions create a fresh challenge for security teams.

Investigators found an unsecured staging server that hosts a system called exploit\_agent, which links to several advanced cloud-based and locally run language models.

## How the automated pipeline operates

The framework examines software code on both sides of each patch announcement, identifies differences related to flaws, writes working exploits, and launches them automatically.

Scripts on the machine also handled later steps, including mapping internal networks, guessing passwords, planting webshells, and deleting webshells installed by rival attackers.

Victim data suggests the operator cared about French media, entertainment, and education websites, but comments in the configuration file were written in Russian.

In August 2026, attackers exploited two PaperCut print server flaws, CVE-2026-81578 and CVE-2026-82078, that, when chained, let outsiders run commands remotely without logging in.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

According to Greynoise, a cybersecurity company that monitors internet-wide scanning and attack traffic, a campaign launched four days after disclosure hit hundreds of organizations through those same flaws.

The attacker likely used AI tools to build and test exploits and assemble a target list, then expanded an initial foothold to domain administrator within minutes.

## Autonomous attacks will increase

Google tracks open source attack frameworks including ARTEX, CAIRN, PentAGI, CyberStrikeAI, and HexStrike AI, and has confirmed CAIRN and PentAGI were used against live targets.

The company claims that from August through early October 2026, one actor ran a customized PentAGI platform that probed many Asian organizations for weaknesses.

“While these frameworks are capable of significantly compressing attack timelines to machine speed and achieving operational objectives, they currently trade stealth for velocity,” the team said in its report.

“We anticipate not only reduced human involvement in these operations but also increased stealth and sophistication of the activity.”

Google recorded at least 8 zero-day exploits per month in 2025 and 11 per month in 2026, with August reaching 22 and overall exploits nearly doubling.

Hundreds of claimed but broken exploit demonstrations, likely AI-made, appeared after PHP patches arrived on October 21, 2026, burdening defenders with verification work.

In 2026, Mandiant responded to several LLMJacking incidents in which criminals drained victims' cloud computing and model quotas, with daily fraudulent bills above $100,000.

In the worst cases, losses reached $1 million before cleanup, and stolen access was resold through underground storefronts called LLM Mixers.

Advertised rates ran between $0.10 and $25 for every million tokens, while APIMart applied a 5x surcharge once prompts passed 100,000 tokens.

Google also found a contractor building a platform managing over 100,000 accounts, using virtual phones and automated agents to run thousands of fake personas.

At cryptocurrency firms across two continents, suspected MIDNIGHT NEPTUNE actors edited Claude Code configuration files so that launching the tool downloaded a backdoor.

Google acknowledges that hallucinated details and noisy tool behavior can hurt reliability, so stealthy espionage groups are expected to use these systems selectively.

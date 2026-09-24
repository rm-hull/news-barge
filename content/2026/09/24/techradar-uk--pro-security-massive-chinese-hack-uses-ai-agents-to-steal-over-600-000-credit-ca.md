---
title: Massive Chinese hack uses AI agents to steal over 600,000 credit cards and
  hit hundreds of sites with malware
source_url: https://www.techradar.com/pro/security/massive-chinese-hack-uses-ai-agents-to-steal-over-600-000-credit-cards-and-hit-hundreds-of-sites-with-malware
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-24T13:31:16Z'
published: '2026-09-24T00:00:00Z'
description: It only cost them around $25 per target
categories:
- Technology & Software
- Business & Entrepreneurship
- Personal Finance & Investing
image: https://cdn.mos.cms.futurecdn.net/AvZcjmUMtehpuha5oJLcTB-2560-80.jpg
---

![Who will win the AI race?](https://cdn.mos.cms.futurecdn.net/AvZcjmUMtehpuha5oJLcTB.jpg)

* **Gambit researchers uncovered ongoing AI‑driven skimming campaign stealing 600,000+ payment records since July 2026**
* **Attackers used three autonomous harnesses (Strix, Cairn, Hermes) to compromise dozens of retail sites cheaply**
* **Victims include major US firms; campaign shows AI enables faster, persistent, low‑cost cyberattacks at scale**

In July 2026, a hacker tasked autonomous AI agents to attack retail organizations around the world, deploy credit card skimmers, and steal payment data.

Since then, the bots launched hundreds of attack projects, compromised dozens of organizations, and stole at least 600,000 payment records - and to make matters worse, the campaign is still live, attacking and breaking into websites as we speak.

All of this was reported by security researchers Gambit, who said they managed to recover the operator’s staging server and through it - reconstruct the ongoing campaign. They also saw the skimmers live on victim websites, and sifted through logs and AI claims found on the attacker’s server. In just five days, between September 10 and 15, the agents made 105 attack waves and compromised 27 organizations “to varying degrees.”

Among the victims are a Fortune 500 hospitality company, a “major” US airline, a large private US industrial supplies distributor, and a US online fashion retailer. One of the AI tools would use a website ranking service to produce a list of potential targets, focusing primarily on those running custom-built software.

## A fistful of dollars

But the victims are not the “interesting” part of this story - the attackers are. Gambit believes they are financially motivated Chinese threat actors. They are using three AI “harnesses” (frameworks, essentially), which can run almost the entire attack chain autonomously, striking around 10 companies a day, for a handful of dollars per company.

In four weeks, the attackers spent around $7,000, meaning that their entire cost for the operation so far was no more than $18,000. Breaking it down, it means that the attacker spent around $25 per target.

“Spread over the companies attacked, this is a marginal cost of a few US dollars to a few tens of US dollars for each targeted company,” Gambit’s researchers said. “The operator’s own cost review gives a similar figure, a mean of $25.46 over 101 completed scans, from $3.13 for the cheapest target to $79.31 for the most expensive.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“Where access was achieved, it usually took less than a day, and in many cases just a few hours. We also detected instructions in the attacker’s playbook that could disrupt the operations of a company as a result of data deletion or cleanup procedures run by the agent - and this has indeed happened in some of the breaches,” Gambit said.

## The three harnesses

The three harnesses are called Strix, Cairn, and Hermes.

Gambit describes Hermes as an open source autonomous AI agent with a persistent memory, skills that the agent wrote and edited itself, a searchable archive of past sessions, scheduled jobs, and a web console. On the staging server the researchers analyzed, it loaded a Chinese system persona called “SOUL - Red Team Operator”, which contained 121 skills (78 attack skills).

“Hermes is the operator’s console for orchestrating the activity and for direct hacking activities,” Gambit explained. “It used Anthropic’s opus-4.6 (after newer models refused its requests), with 1,951 prompts typed by the human across 260 sessions - only a few prompts per target. The human prompts are short instructions in Chinese, usually launching an attack, tasking the agent with a general next step, or what to do next after achieving access.”

Strix is an open-source AI pentest tool, while Cairn is an autonomous pentest engine. It receives target domains and an objective, such as to get a shell or admin access, then runs for hours until it achieves the objective, times out, or is stopped. Cairn used DeepSeek v4.1 Flash, it was said.

Gambit’s researchers seem to be rather impressed with the campaign. They described it as very low cost, with a level of patience, persistence, and creativity that most human attackers would be “unlikely to sustain”, managing to achieve “far greater results, far faster.”

They have also called to arms, urging organizations to “adapt to a reality where attacks are significantly faster and more comprehensive.” To do that, they must adopt a resilience-first mentality and deploy a security stack that can match the AI on speed.

Many of the affected organizations were notified, and the skimmers were removed, they said.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

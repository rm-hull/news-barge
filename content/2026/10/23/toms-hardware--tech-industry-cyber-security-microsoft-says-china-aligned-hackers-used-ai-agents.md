---
title: China-aligned hackers deploy AI agents in massive ConnectWise supply chain
  attack — agents attempted sign-ins at more than 2,250 Microsoft 365 tenants, with
  some of the group's attacks reaching privileged access in under three hours
source_url: https://www.tomshardware.com/tech-industry/cyber-security/microsoft-says-china-aligned-hackers-used-ai-agents-in-connectwise-supply-chain-attack-agents-attempted-sign-ins-at-more-than-2-250-microsoft-365-tenants-with-some-of-the-groups-attacks-reaching-privileged-access-in-under-three-hours
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-23T11:34:19Z'
published: '2026-10-23T00:00:00Z'
description: Automated password guessing failed, but stolen app credentials needed
  no user sign-in at all.
image: https://cdn.mos.cms.futurecdn.net/wA2Noe6WhknviBc6VQJqFo-992-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Shane Downing
- Tom
locations:
- China
organisations:
- AI
- ARTEX
- Autumn-27
- Cloud Backup
- ConnectWise
- CrowdStrike
- Get Tom's Hardware
- GitHub
- Google News
- Huntress
- Microsoft Defender
- Reuters
- SaaS Security and Cloud Management
- Shane Downing
- SkyKick
- Storm-0940
- Tom’s Hardware
---

![Microsoft Threat Intelligence illustration for its Storm category of developing threat actors: a green hexagon around a spiral on a dark navy panel](https://cdn.mos.cms.futurecdn.net/wA2Noe6WhknviBc6VQJqFo-992-80.jpg)

China-state-aligned actor Storm-0940 used ARTEX, an open-source agentic AI penetration testing framework, in its large-scale ConnectWise supply chain attack, Microsoft wrote in its Security blog. After unauthorized access to the multi-tenant application, the group attempted sign-ins at more than 2,250 Microsoft 365 tenants, with stolen ConnectWise app credentials that authenticated as the apps with no interactive user sign-in. Some of the group’s attacks reached privileged access less than three hours after initial targeting.

Automated password guessing, or password spraying, also targeted 327 accounts across eight organizations with more than 151,000 failed logons and no successes. The use of ARTEX, “a system of LLM-driven agents that run an autonomous penetration test,” sped up scanning and reconnaissance, password spraying, and OAuth application abuse. The agents can work around the clock “with little needed human interaction,” at a pace that “leaves defenders with little time to detect and respond.” It’s uncertain how the ConnectWise credentials were stolen or how many tenants were actually compromised.

Storm-0940, active since 2021, is a “China-state aligned actor” with “no known industry aliases,” and its name follows the convention for a developing actor. Industries targeted this time include aerospace and defense, semiconductor, government, and think tanks, with 14 listed in total. The activity “did not result from a compromise of or a vulnerability” in Microsoft’s systems, products, or services.

At its peak on Oct. 11, the password spray engaged in 2,900 attempts, all failures, per minute, at more than 111,000 for that day, with 48 accounts logging more than 1,000 failures each. Almost 98% of this activity was locked out. However, with control of the identities of multiple ConnectWise cloud apps, the attacking AI agents signed in to customer tenants from the same IP range using those apps’ credentials, with more than 200 sign-ins in under four minutes using four application credentials. Operations taken within some tenants include Graph and directory operations, reconnaissance, app credential changes, plus changes to identities, groups, and privileged roles.

In one tenant on Oct. 15, Huntress, a security firm, saw an app add itself to the top administrator role, the behavior behind the Microsoft Defender alert “Application self-assigned Global Administrator role.” Actions included planting new secrets set to expire in 2028. It confirmed unauthorized sign-ins for 162 tenants by Oct. 16 and, a day later, almost 1,000 Entra tenants with sign-in activity from the attacking IP, with more than 300 succeeding. The attack’s sweep through tenants in sorted order, a few seconds apart, indicated “a script working from a target list.”

What differs from many traditional attacks is the use of the open-source pentest framework that, Microsoft says, can use any AI model. Threat actors in multiple regions are using the technology, and public reporting this month tied it to breaches at South Korean financial institutions. CrowdStrike said the suspect in those separate attacks was likely based in China and allegedly used ARTEX with Anthropic’s Claude Code. ARTEX’s developer, who goes by the handle “Autumn-27,” said on GitHub that the ARTEX project “will no longer be updated” and would become closed source, *Reuters* reported.

ConnectWise noted the unauthorized access and suspended Cloud Backup (formerly SkyKick) as well as SaaS Security and Cloud Management as a precaution. It has started a phased restoration with recovery expected to take several days and has no indicators to date that partner backup data was compromised. Microsoft notes that an affected app, or even a successful sign-in, doesn’t necessarily mean data was accessed or taken, and advises customers to keep affected app connections disabled until formal restoration instructions are issued, and to review activity from this month where logs allow.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

---
title: Microsoft says Chinese and North Korean hacking groups are now actively using
  ARTEX in their attacks
source_url: https://www.techradar.com/pro/security/microsoft-says-chinese-and-north-korean-hacking-groups-are-now-actively-using-artex-in-their-attacks
source_site: TechRadar UK
source_slug: techradar-uk
description: Microsoft reveals the first confirmed names of ARTEX users
image: https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW-1920-80.jpg
published: '2026-11-26T00:00:00Z'
scraped_at: '2026-11-26T16:51:05Z'
categories:
- Technology & Software
- Business & Entrepreneurship
- Arts & Culture
people:
- Anne Neuberger
- Crystal Typhoon
locations:
- Azure Key
- Salt Typhoon
- US
- then-White House
organisations:
- AI
- ARTEX
- Artex
- CIA
- Crystal Typhoon
- European Commission
- GitHub
- Microsoft
- National Geospatial-Intelligence Agency
- Office of the Director of National Intelligence
- Onyx Sleet
- Pearl Sleet
- Salt Typhoon
- Storm-0940
- Storm-3358
- TechRadar Pro
---

![Concept art representing cybersecurity principles](https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW-1920-80.jpg)

* **Microsoft says Chinese and North Korean threat groups have adopted the AI-powered ARTEX platform for reconnaissance, credential attacks, and exploitation**
* **Researchers linked ARTEX activity to state-sponsored espionage campaigns as well as financially motivated cybercriminal operations**
* **Defenders are urged to monitor for high-volume automated activity, strengthen identity protections, and deploy deception technologies to detect AI-driven attacks**

Chinese and North Korean state-sponsored threat actors are among the ones now using ARTEX in cyberattacks, new research from Microsoft has claimed.

ARTEX, an AI-powered pentesting tool, first emerged in the summer of 2025, and while it was originally intended as a white hat tool, it was almost instantaneously hijacked by different hacking collectives. The developer, apparently Chinese, distanced themselves from the illicit activity and even shut down the project, but it was already too late.

Thousands of archived copies, translations, and different rebrands were left circulating on the web, and security researchers started spotting traces of ARTEX in different breaches. Recently, three US spy agencies - the CIA, National Geospatial-Intelligence Agency, and the Office of the Director of National Intelligence - suffered cyberattacks and data theft by unidentified attackers who apparently used ARTEX as part of their tech stack.

The European Commission had to shut down two apps - human resources platform Sysper, and a medical reimbursement system called MyPMO, due to an ARTEX-powered assault, and before that, researchers saw threat actors using AntiFox (an ARTEX clone) to steal login credentials and access people’s AWS environments.

## Salt Typhoon and friends

In an in-depth report, Microsoft argued that at least two state-sponsored groups - Crystal Typhoon and Salt Typhoon, are now using ARTEX as part of their arsenal, for “network reconnaissance, credential attacks, and web application exploitation.”

“In the past few weeks, we’ve reported several distinct campaigns that abused Artex to search public repositories for exposed secrets, enable supply chain compromise, and scan internet-facing systems for exploitation,” Microsoft said in its report.

Salt Typhoon has been around for almost a decade, and is best known for targeting telecommunications providers, government, healthcare, and hospitality firms. Its usual modus operandi includes exploiting flaws in network infrastructure (primarily routers) to establish persistent access and intercept communications. Its goal is to harvest actionable intelligence on behalf of the Chinese government.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

In December 2024, then-White House Deputy National Security Adviser Anne Neuberger confirmed Salt Typhoon compromised at least eight US telecom carriers, in a campaign that’s apparently been active for more than two years at the time.

Crystal Typhoon, on the other hand, is a newer addition to the team. First seen in late 2023, it targets government networks and critical infrastructure worldwide, focusing on edge devices and firewalls. Its modus operandi involves exploiting vulnerabilities in network appliances and deploying custom backdoors to maintain access, conduct reconnaissance, capture network traffic, and potentially move laterally through compromised environments.

## An extremely fast tool

The researchers also named a handful of other threat actors: Storm-0940, Storm-3358, Onyx Sleet, and Pearl Sleet. They said ARTEX has attracted both state-sponsored and financially motivated hacking groups, and that the appeal extends way beyond government-backed cyber-espionage campaigns.

One of the reasons for ARTEX’s mass appeal is the speed at which it operates. Microsoft described a case in which an AI agent went from searching GitHub for exposed application secrets to accessing data in Azure Key vault in just five minutes.

In a separate Storm-0940 campaign, Microsoft recorded more than 151,000 failed sign-in attempts, with activity peaking at 2,900 attempts per minute, and in other intrusions, attackers gained privileged access in less than three hours after initially targeting their victims. This is the speed no human can match, and without AI assistance, ARTEX is essentially unstoppable.

But it isn’t entirely unstoppable. When defending against ARTEX, IT teams should not rely solely on classic signature-based detection, Microsoft warns. Although the tool sometimes uses easy-to-recognize user-agent strings such as “artex-enrich”, threat actors can tweak these to evade detection. Instead, the researchers said the easiest way to spot ARTEX is by observing bursts of machine speed activity and the “characteristically large volume of anomalous traffic from a single source in a short time.” Microsoft also recommends using honeypots and decoy systems to divert autonomous attacks away from legitimate infrastructure.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

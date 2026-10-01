---
title: '''It is possible that threat actors are finding it more accessible or efficient
  to use LLMs and AI tools'': Google warns that AI explosion will lead to more dangerous
  and advanced security threats'
source_url: https://www.techradar.com/pro/security/it-is-possible-that-threat-actors-are-finding-it-more-accessible-or-efficient-to-use-llms-and-ai-tools-google-warns-that-ai-explosion-will-lead-to-more-dangerous-and-advanced-security-threats
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-01T20:24:23Z'
published: '2026-10-01T00:00:00Z'
description: It's not about zero-days, at all
image: https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-2560-80.jpg
categories:
- Technology & Software
people: []
locations: []
organisations:
- AI
- GTIG
- Google Threat Intelligence Group
- TechRadar Pro
---

![A hand about to touch a phone. Superimposed on top of it is a pink triangle with exclamation mark inside it. Behind it is a computer display with code on it](https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-1920-80.jpg)

* **AI is accelerating exploitation of known vulnerabilities more than zero-day discovery**
* **Google observed sharp rises in disclosed flaws and real-world exploitation**
* **Defenders must prioritize intelligence-led patching as n-day weaponization speeds up**

Artificial Intelligence (AI) is helping cybercriminals find and exploit software bugs faster, more easily, and with greater consequences, a new report from the Google Threat Intelligence Group (GTIG) has claimed. However, it’s not in the way you’d expect - there’s very little focus on zero-day vulnerabilities.

GTIG's Vulnerability Discovery and Exploitation Trends in the AI Era paper outlines how AI is already having a “measurable impact” on the vulnerability landscape, not just in the speed at which new flaws are discovered, but also in the nature of the vulnerabilities themselves. Researchers found that the number of flaws discovered in 2026 doubled throughout the year, and the number of those exploited in the wild rose significantly, as well.

GTIG says that the number of bugs found each month this year rose from 5,045 in January to 10,740 in August 2026. During the same period, the average number of flaws exploited in the wild rose from 10.5 a month in 2025, to 18 a month.

## Speeding up n-day exploitation

But it seems AI’s ace in the sleeve is not finding zero-days, as Mythos would have you think. Google’s researchers found only a marginal increase in zero-day exploitation (from 8 a month in 2025, to 11 a month this year). Instead, GTIG argues that the bigger threat is the rapid weaponization of n-day flaws:

"It is possible that threat actors are finding it more accessible or efficient to use LLMs and AI tools to automate analysis of differences between product versions, patches, vulnerability disclosure announcements, and Proof-of-Concept (POC) code to rapidly weaponize n-days, rather than to discover new zero-days," the report states.

In other words, the exploitation growth recorded this year was mostly within previously known vulnerabilities, not zero-days. The number of exploited high-risk flaws doubled year-on-year, Google said.

## Finding high-impact flaws

But AI is also helping defenders, especially when it comes to filtering out less impactful flaws and focusing on the most dangerous ones. Looking just at vulnerabilities discovered with the help of AI, Google says there are proportionally fewer low-risk ones, and significantly more medium and high-risk ones. In fact, 50% of AI-discovered vulnerabilities resulted in remote code execution (RCE), compared to 26% across the broader vulnerability ecosystem.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

GTIG says the security community is using AI primarily for high-level flaws in critical infrastructure, privilege boundaries, core libraries, and runtime environments where they’re more likely to be found.

Google highlighted at least one example where an AI-discovered vulnerability quickly attracted the attention of threat actors. The company cited CVE-2026-1731, a command-injection vulnerability in BeyondTrust products that was discovered by a third-party AI research agent. GTIG said threat actors began exploiting the flaw within days of public disclosure, using it in campaigns that included privilege escalation, data theft, and malware deployment.

In the near future, both vulnerability discovery and exploitation rates are expected to grow, Google says. Threat actors are increasingly experimenting with AI to build exploits, as well as various vulnerability discovery tools.

The defenders, on the other hand, need to focus on n-days even more, and understand that crooks will be able to weaponize them at unprecedented speed.

As a result, organizations will need to move away from broad, unprioritized patching programs and toward intelligence-driven vulnerability management capable of keeping pace with increasingly automated adversaries.

“GTIG expects that vulnerability discovery and exploitation will continue to grow in the short to medium term,” Google said. “To counter the increased risk from rapid vulnerability discovery and exploitation, organizations must transition from unprioritized mass-patching to threat-intelligence-driven triage, combining targeted edge-defense with automated, agentic remediation.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

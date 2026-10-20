---
title: Russia drafted plans for AI that could block 95% of VPNs — but the idea has
  quietly vanished from its national roadmap
source_url: https://www.techradar.com/pro/security/russia-drafted-plans-for-ai-that-could-block-95-percent-of-vpns-but-the-idea-has-quietly-vanished-from-its-national-roadmap
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-20T19:13:40Z'
published: '2026-10-20T00:00:00Z'
description: The machine-learning filter it would have relied on is funded separately
image: https://cdn.mos.cms.futurecdn.net/4egzBLcxERGb2K5oHqyi6g-1920-80.jpg
categories:
- Technology & Software
people:
- Alexey Kozlyuk
- Maria Kolomychenko
- Pavel Durov
- Sarkis Darbinyan
locations:
- Kuznyechik
- Russia
organisations:
- AI
- Amnezia VPN
- Digital Development Ministry
- Forbes Russia
- GRChTs
- Kommersant
- Main Radio Frequency Center
- Meduza
- RBC
- RKS Global
- Roskomnadzor
- State Duma
- Supervision of Communications, Information Technology and Mass Media
- TechRadar Pro
- VPN Guild
- VPNs
- Verstka
- Windscribe
---

![VPN encrypting a flow of data](https://cdn.mos.cms.futurecdn.net/4egzBLcxERGb2K5oHqyi6g-1920-80.jpg)

* **A draft of Russia's national AI plan proposed using AI to analyze 70% of blocked VPN services and lift blocking effectiveness to 95%**
* **The Digital Development Ministry says the measure is absent from the current draft, but Roskomnadzor's separately budgeted and arguably crucial ML filtering project remains**
* **The 95% is an effectiveness target, not accuracy, and sources expect AI to raise false positives, with corporate VPN, cloud and voice traffic most exposed**

Russia's Digital Development Ministry considered using artificial intelligence to push the effectiveness of its VPN blocking to 95%, according to a front-page report in Kommersant.

The measure appeared in a draft of the country's national plan for implementing AI through 2030; the ministry now says it is not in the current version.

This isn't the first time such a move has been reported, but some earlier coverage might have been overzealous, to say the least, when it reported that "Russia Eyes AI-Powered VPN Crackdown With 95% Blocking Accuracy." The problem with that headline is that not only was that proposal dropped, but the 95% accuracy figure was never actually in play.

## A draft that proposed AI use

None of the above reporting should reassure an estimated 57 million Russians who rely on circumvention tools.

Roskomnadzor (the Federal agency tasked with "Supervision of Communications, Information Technology and Mass Media") has its own machine-learning filtering project budgeted outside the national AI plan, and the money for Russia's blocking infrastructure is set to double next year.

Kommersant, which reviewed the draft, reports that the ministry wanted AI to analyze the characteristics of 70% of all the VPN services Russia blocks. The drafters reckoned that would lift blocking effectiveness to 95%.

Asked about it, the ministry said the current draft of the plan "contains no such information," in Meduza's translation. A source familiar with the discussions told Kommersant that agencies had pitched a range of measures for the plan, some of which may never be implemented, and that the traffic-analysis algorithms already in service are a form of intelligent analysis but do not count as AI.

An AI layer would behave fundamentally differently; rather than matching known signatures, models would weigh packet sizes and timing, session length, and the balance of inbound to outbound traffic, then flag likely VPN servers from indirect clues: how a node behaves, which host it sits on, and what its neighboring IP addresses look like. The payoff is speed, catching new servers before they reach any blocklist.

Kommersant uses the word effectiveness, and the distinction matters: a blocking-effectiveness figure describes how much targeted traffic it stops. It says nothing about how much legitimate traffic gets stopped with it, and that is what the catch is; the solution proposed does not account for any mistakes, just how effective it would be at its job of blocking out VPN traffic.

The 95% target is also less of a leap than some headlines suggest, because Russia already has 92% on paper, at least by its own estimates. A Roskomnadzor subsidy decision for its Main Radio Frequency Center (GRChTs), dated January 2025 and surfaced in May 2026 by journalist Maria Kolomychenko, sets an "average level of effectiveness" of 92% for restricting VPNs via signatures by the end of 2030. Verstka reports that the AI proposal was meant to lift that same indicator to 95%.

The more consequential point is that striking a line from a draft strategy does not strike the capability. *Forbes Russia* reported in January 2026 that Roskomnadzor planned to spend 2.27 billion rubles (around $29 million) in 2026 on a machine-learning-based traffic-filtering mechanism, a project we flagged when Windscribe saw a roughly 90% drop in its Russian traffic that same month.

The false-positive risk is not hypothetical in Russia, because the government has already learned how hard it is to separate good VPNs from bad ones. When the ministry ordered major platforms in April to block users with VPNs switched on, its guidance promised a whitelist for corporate VPNs.

Telegram founder Pavel Durov claimed the crackdown had "triggered a massive banking failure," and outage-tracking data showed bank disruptions on April 3 2026. A source told RBC at the time that no reliable technical method existed to tell permitted corporate VPN traffic from the rest.

For now the picture on the ground is unchanged: blocking is intensifying with or without an AI mandate. At least 10 VPN providers reported tighter restrictions in the week after September's State Duma elections, and VPN Guild chairman Alexey Kozlyuk described it to Meduza as "a continuation and gradual intensification" of a campaign that began in August.

The Kommersant report also landed a day after RBC revealed a draft ministry order requiring phones on Russia's 5G networks to support the FSB-developed Kuznyechik cipher from March 1, 2032.

Providers keep adapting. "In Russia, VPNs face pressure almost every month; it is a new norm," an Amnezia VPN spokeswoman told TechRadar Pro. But Sarkis Darbinyan of RKS Global and the VPN Guild warned TechRadar that for users, the end result is "an ever-shrinking number of services that actually work."

The 95% target may be gone from one document. The infrastructure, the money, and the intent behind it are not.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

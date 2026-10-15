---
title: Malicious Russian disinformation bot traffic barely flinches after Ukraine
  strikes Yandex data centers and auto-migration kicks in — Cloudflare tracks 170
  million automated attacks shifting to alternate cloud hosts
source_url: https://www.tomshardware.com/service-providers/network-providers/malicious-russian-disinformation-bot-traffic-barely-flinches-after-ukraine-strikes-yandex-data-centers-and-auto-migration-kicks-in-cloudflare-tracks-170-million-automated-attacks-shifting-to-alternate-cloud-hosts
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-15T17:02:27Z'
published: '2026-10-15T00:00:00Z'
description: Taking out malicious bots is a game of whack-a-mole.
image: https://cdn.mos.cms.futurecdn.net/cvrKM8CEZVoo8iapjUyEPZ-1920-80.png
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Cloudflare
- Jowi Morales
- Tom
locations:
- Abu Dhabi
- Cloudflare
- Russia
- Ukraine
organisations:
- AWS Bahrain
- Amazon
- Cloudflare
- Google News
- Jowi Morales
- Radist
- Selectel
- Yandex Search
- Yandex.Cloud
---

![bots working on virtual computers](https://cdn.mos.cms.futurecdn.net/cvrKM8CEZVoo8iapjUyEPZ-1920-80.png)

Russian bot traffic showed signs of slowing down after Ukraine bombed some of Yandex’s biggest data centers. Unfortunately, while the attacks have slowed down overall bot traffic from Russia, Cloudflare reports that malicious bots appeared to have simply transferred to other hosting ASNs like Radist and Selectel. Overall traffic on Yandex Search and Yandex.Cloud continues to stay at 10% to 15% of normal traffic levels, meaning the network remains disrupted. Cloudflare noted that traffic from the former is composed mostly of verified search crawlers indexing websites, meaning traffic from this service is mostly legitimate. On the other hand, the latter experienced a drop in malicious activities such as vulnerability scanning and probing after the data center bombings, but Cloudflare says that “high-volume automation did not vanish — it simply migrated to other hosting providers.”

This was evident with one Cloudflare customer in the gambling sector: it saw malicious bot requests from Yandex.Cloud drop to zero but started seeing the same activity being routed through other networks. “Overall, Russian bot traffic targeting gambling accounts remained essentially flat over the week, moving from 167.7 million to 170.1 million requests (+1.4%),” the company wrote in its analysis. “The automation never stopped running; the operators simply migrated their workloads to alternate cloud providers once Yandex.Cloud became unavailable.”

The company also looked at social media traffic and found a similar result — traffic from Russian-origin IPs only dropped by 0.6% in the same period while Russian bot traffic hitting “post,” “reply,” and “like” on one platform only decreased by 5.7%. Because of this, Cloudflare debunked the theory that Ukrainian strikes have caused a drop in social media manipulation, although it also noted that the scope of its analysis is limited to traffic that passed through Cloudflare services.

Since cloud-based workloads can easily be transferred between data centers, taking a few out will not necessarily end the services running out of them. Instead, owners and operators could simply migrate to another data center, which is exactly what Amazon advised its clients who have been affected by Iranian strikes on AWS Bahrain and AWS Abu Dhabi.

Cloudflare pointed out that this is why it’s difficult to defend against automated threats like bot networks — even though an IP prefix gets blocked or the physical infrastructure behind them gets annihilated, their operators could simply move their operations to another provider in a matter of hours and quickly return to normal traffic levels.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK-140-80.jpg)

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.

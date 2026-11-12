---
title: Hackers are more excited for Black Friday than UK shoppers — but not for the
  same reasons
source_url: https://www.techradar.com/pro/security/hackers-are-more-excited-for-black-friday-than-uk-shoppers-but-not-for-the-same-reasons
source_site: TechRadar UK
source_slug: techradar-uk
description: Some hunt for bargains, and others for sensitive customer data
image: https://cdn.mos.cms.futurecdn.net/XhzxqrxHR5MerGpUeEvDo9-2560-80.jpg
published: '2026-11-12T00:00:00Z'
scraped_at: '2026-11-12T19:55:46Z'
categories:
- Technology & Software
- Sports
people:
- Log4Shell
- SonicWall
- Spencer Starkey
locations:
- Log4Shell
- UK
organisations:
- EMEA
- Log4Shell
- RCE
- SonicWall
- TechRadar Pro
---

![small business security](https://cdn.mos.cms.futurecdn.net/XhzxqrxHR5MerGpUeEvDo9-1920-80.jpg)

* **UK retailers face a surge in cyberattacks ahead of Black Friday and Christmas, with intrusion attempts up sharply year-over-year**
* **Most attacks target web applications, using techniques such as directory traversal, remote code execution, and cross-site scripting**
* **Researchers warn stolen customer data from retail breaches often fuels phishing, fraud, and follow-on cyberattacks**

Black Friday, Christmas, and the New Year are not just a busy time for UK shoppers, they’re the busiest time of the year for cybercriminals, as well, experts have warned.

A new report from SonicWall notes that cybercriminals have been preparing all year long to compromise as many ecommerce companies and online stores as possible, in order to steal their data and possibly - money.

Between January and September 2026, SonicWall recorded 23.3 million events that could be described as high- and medium-priority intrusion attempts. In the same timeframe, the company recorded almost 400,000 malware attacks.

Most of this came during the peak trading quarter - with roughly half of entire 2025's attack volume was recorded in that timeframe, and on a yearly basis, intrusion attempts against UK retailers are up 169% year-on-year.

## Directory traversal and other travesties

“The busiest weeks for shoppers are also the busiest for attackers hitting retailers,” the company said.

Almost all of those attacks (97%) targeted web applications, SonicWall stressed, adding that the criminals are broadly mapping the sector’s customer-facing infrastructure as they look for a way to grab the data stored inside.

The most popular technique seems to be directory traversal, recorded 10.5 million times (roughly half of the company’s entire Intrusion Prevention System volume).

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

With directory traversal, threat actors try to trick a web server into granting access to data such as configuration files and stored records, where different passwords are often stored. Sometimes, that includes credentials for databases containing people’s names, addresses, and order histories.

Directory traversal might be popular, but it’s hardly the only technique used. Two in five of SonicWall’s sensors recorded attempts to exploit a React Server Components remote code execution (RCE) flaw.

The company did not say which flaw that was, or share the CVE, but claims it “affects the modern web frameworks behind many new storefronts and shopping apps” and warns that a successful attack can hand criminals control of the server running the site.

Cross-site scripting is also quite popular with 1.6 million hits, but perhaps the biggest surprise is the resilience of Log4Shell.

For those with a shorter memory span, here’s a quick rundown: Apache builds and maintains Log4j, an open-source Java logging framework that developers use to record events their apps generate, including errors, user activity, or system events. In 2021, a critical RCE flaw was discovered, which is now tracked as CVE-2021-44228. Dubbed “Log4Shell”, the flaw allowed threat actors to take control of vulnerable servers by submitting a specially crafted string to applications that used it. That way, they were able to steal credentials or even deploy malware and ransomware.

## Log4Shell refuses to die

Roughly half a decade later, it seems Log4Shell is still in play, since SonicWall recorded at least 263,000 hits.

“Criminals are mapping the retail sector’s web estate ahead of peak trading, seeking any gap that could lead to stolen customer data, payment fraud, or a site outage at the worst possible moment,” the company warned.

Commenting on the findings, executive vice president, EMEA at SonicWall, Spencer Starkey, said the criminals all want the same thing - personally identifiable data ecommerce companies generate on their customers.

“In the Golden Quarter, nobody wants to take a checkout offline to patch it," he noted, "Criminals know that. When a breach happens, it's the customer who pays the price in fraud, phishing scams and lost trust.”

The company also warns that a breach at an e-commerce site is often just the first step, as the data found there is later used for wire fraud, social engineering, and stage-two attacks against other organizations.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

---
title: Buggy microcontrollers making up some of the world's most important servers
  can be easily backdoored
source_url: https://www.techradar.com/pro/security/buggy-microcontrollers-making-up-some-of-the-worlds-most-important-servers-can-be-easily-backdoored
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-06T14:32:22Z'
published: '2026-08-06T00:00:00Z'
description: Researchers found more than a dozen new flaws
image: https://cdn.mos.cms.futurecdn.net/Dtd9CSn6K6jfEdpnzch4zj-2121-80.jpg
---

![Security padlock and circuit board to protect data](https://cdn.mos.cms.futurecdn.net/Dtd9CSn6K6jfEdpnzch4zj.jpg) 

- **runZero disclosed 12+ new flaws in BMCs from HPE, Supermicro, Dell, Lenovo, Huawei, and others at Black Hat**
- **Scans found 86k internet‑exposed BMCs and 120k internal devices**
- **Researchers warn BMCs form a widespread, under‑patched parallel attack surface**

Security researchers have discovered more than a dozen new vulnerabilities in Baseboard management controllers (BMC), hardware components found in thousands of the world’s most popular enterprise servers.

BMCs are specialized chips built into servers that allow administrators to remotely monitor and manage hardware regardless of the operating system, and even when the hardware is turned off. They provide out-of-band management capabilities such as remote console access, firmware updates, hardware health monitoring, and power control, and have been a pivotal component since their introduction in the late 1990s.

Earlier this week, during the Black Hat security conference in Las Vegas, security expert HD Moore of runZero disclosed finding more than a dozen flaws in BMCs sold by HPE, Supermicro, Avocent, Huawei, Lenovo, Dell, and others - and to make matters worse, some of the flaws disclosed in the past remain active even today.

## Parallel attack surface

“The end result is a pervasive, under-monitored, under-patched parallel attack surface that is both Internet-exposed and widespread inside corporate networks, and is much more exploitable than many folks realize,” Moore told the publication.

To assess the associated risks, Moore ran two scans - one looking at internet-connected BMCs in general, and another internally surveying devices in corporate networks. The first one found 86,000 exposed BMCs, more than half of which (54%) carried at least one of the flaws he found.

The internal scan, counting more than 120,000 BMCs, found almost a third (29%) carrying at least one critical vulnerability.

Details about the flaws will remain under lock and key until the manufacturers address them, Moore explained, saying that many of them cannot be exploited without prior authentication. However, for many (well-equipped) threat actors, that often isn’t a problem, since a number of smaller pre-authentication flaws exist as well, which could be abused.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

*Via**Ars Technica*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

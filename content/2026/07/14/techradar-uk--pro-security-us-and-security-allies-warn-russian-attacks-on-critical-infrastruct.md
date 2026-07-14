---
title: US and security allies warn Russian attacks on critical infrastructure are
  ramping up
source_url: https://www.techradar.com/pro/security/us-and-security-allies-warn-russian-attacks-on-critical-infrastructure-are-ramping-up-against-poorly-configured-and-vulnerable-networking-devices-worldwide
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-14T17:24:42Z'
published: '2026-07-14T00:00:00Z'
description: Russians are targeting misconfigured routers running in critical infrastructure
  firms.
image: https://cdn.mos.cms.futurecdn.net/kqDd8hw4VtrskmqGDY5fKa-1980-80.png
---

![A person plugging an Ethernet cable into a router](https://cdn.mos.cms.futurecdn.net/kqDd8hw4VtrskmqGDY5fKa.png) 

- **NSA, FBI, CISA, and 15 allied agencies warn Russia’s FSB Center 16 is exploiting weak/default credentials and old Cisco flaws to compromise critical infrastructure devices**
- **Advisory highlights CVE‑2018‑0171 (Smart Install DoS/RCE) and CVE‑2008‑412813 (CSRF in Cisco IOS 12.4) as examples of vulnerabilities still being abused**
- **TTPs overlap with Chinese groups but attribution points to Russian actors like Berserk Bear and Energetic Bear; full IoCs and mitigations were published in the joint advisory**

Russian state-sponsored threat actors are continuously targeting broken and poorly configured networking devices belonging to critical infrastructure providers all around the world, a joint security advisory published by the US National Security Agency (NSA) and more than a dozen other agencies has warned.

As per the advisory, hackers working for the Russian Federal Security Service (FSB) Center 16 are constantly scanning for routers and other internet-connected devices that can be accessed with “common or default” login credentials.

Once found, these devices are instructed to copy device configuration files and later exfiltrate them via the Trivial File Transfer Protocol to servers under their control.

## Berserk Bear and Salt Typhoon

In cases where default or weak credentials don’t work, the threat actors also try to exploit vulnerabilities. In the advisory, the agencies specifically mentioned two flaws in Cisco devices - CVE-2018-0171 and CVE-2008-412813. The former is an eight-year-old bug in the Smart Install feature of Cisco IOS Software and Cisco IOS XE Software that allows an unauthenticated, remote attacker to cause a denial of service (DoS) condition, or to execute arbitrary code.

The latter is an even older (18 years old) set of multiple cross-site request forgery (CSRF) vulnerabilities in the HTTP Administration component in Cisco IOS 12.4 on the 871 Integrated Services Router that allows remote attackers to execute arbitrary commands.

Even though many of these tactics, techniques, and procedures (TTP) overlap with Chinese hackers Salt Typhoon, the agencies suggested they are primarily focusing on Russian hackers known as Berserk Bear, Energetic Bear, Crouching Yeti, Dragonfly, Ghost Blizzard, or Static Tundra.

The joint advisory is co-authored by the NSA, FBI, and CISA, as well as 15 other agencies from Australia, the United Kingdom, Canada, New Zealand, Estonia, Finland, France, and Italy.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

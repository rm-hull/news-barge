---
title: Microsoft nemesis returns with another zero-day PoC — but is 'LegacyHive' as
  nasty as expected?
source_url: https://www.techradar.com/pro/security/microsoft-nemesis-returns-with-another-zero-day-poc-but-is-legacyhive-as-nasty-as-expected
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-16T17:36:59Z'
published: '2026-07-16T00:00:00Z'
description: Chaotic Eclipse is back with a new Windows 11 zero-day called LegacyHive.
image: https://cdn.mos.cms.futurecdn.net/HCMx4u3U8KVpNCqssJps2J-2560-80.jpg
---

![A laptop with the Windows 11 desktop on screen, glowing, while on a work desk](https://cdn.mos.cms.futurecdn.net/HCMx4u3U8KVpNCqssJps2J.jpg) 

- **Researcher “Chaotic Eclipse” releases new Windows 11 zero‑day dubbed**-** LegacyHive**-**, a local privilege escalation bug targeting user registry hives**
- **Exploit could let attackers elevate low‑privileged accounts, but requires prior device access; no CVE or full PoC was published**
- **Experts caution that skilled actors could weaponize it quickly, urging intelligence teams to prepare mitigations despite lower perceived impact than earlier releases**

Chaotic Eclipse, the infamous security researcher with a Microsoft grudge, did as they previously promised and released yet another zero-day vulnerability for fully patched Windows 11 devices.

However, other researchers don’t see it as dangerous as some of their previous releases.

Chaotic Eclipse disclosed a zero-day called LegacyHive, which is a local privilege escalation (LPE) bug targeting Windows’ user hives.

## Escalating privileges

A few months ago, a hacker/researcher with the alias Chaotic Eclipse started publishing functioning exploits for fully patched Windows 11 systems, all with PoCs, claiming that Microsoft acted against them in ill faith and argued that the company does not treat researchers with the respect they deserve.

They released a total of seven exploits, some more damning than others, and promised to release a “bone-shattering” one on July 14 2026. In the meantime, Microsoft first criticized the researcher for not “responsibly” disclosing the flaws, and at one point even threatening possible legal action. However, it did not sue the researcher and later backed away from the threat entirely, partly as a result of strong public backlash.

In Windows, user hives are registry files that store configuration settings specific to an individual user account. These include desktop preferences, user-specific application settings, network drive mappings, user-specific security and privacy settings, and more.

With LegacyHive, threat actors could, in theory, gain privileged read-write access targeting other users’ hives. Or, in other words, they could turn low-privileged accounts into high-privileged ones. However, they would first need to have any access to the device, which is one of the reasons why some security researchers don’t see it as disastrous as Chaotic Eclipse’s previous work.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

What also makes LegacyHive different from some other releases is that this one was not released with a CVE identifier or a fully functioning Proof of Concept (PoC).

Still, security experts are urging intelligence teams to work fast, because skilled threat actors can fill the gaps with relative ease, and turn LegacyHive into a potent weapon.

*Via**The Register*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

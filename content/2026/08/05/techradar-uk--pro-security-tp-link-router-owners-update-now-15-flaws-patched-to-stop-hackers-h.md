---
title: TP-Link router owners update now — 15 flaws patched to stop hackers hijacking
  your devices
source_url: https://www.techradar.com/pro/security/tp-link-router-owners-update-now-15-flaws-patched-to-stop-hackers-hijacking-your-devices
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-05T14:30:03Z'
published: '2026-08-05T00:00:00Z'
description: Omada platform was found to be vulnerable in several ways
image: https://cdn.mos.cms.futurecdn.net/xiF2oa9QT4q5sePeRdA8Af-1920-80.jpg
---

![cables going into the back of a broadband router on white background](https://cdn.mos.cms.futurecdn.net/xiF2oa9QT4q5sePeRdA8Af.jpg) 

- **Forescout’s Vedere Labs found 15 flaws in TP‑Link Omada business networking gear, exploitable for RCE when chained with prior CVEs**
- **Weak trust shortcuts in zero‑touch provisioning exposed devices to client‑side code execution, hijacking, spoofing, and encrypted comms compromise**
- **TP‑Link released firmware updates; admins should patch immediately, with 1,800+ Omada controllers exposed online**

TP-Link has patched more than a dozen vulnerabilities across multiple business networking products which could have been chained to achieve remote code execution (RCE).

Security researchers at Vedere Labs from Forescout found the flaws and published an in-depth report on the issues, which particularly affect TP-Link Omada, the company’s business networking platform for centrally managing enterprise and small-business network infrastructure.

It includes cloud-managed Wi-Fi access points, routers, switches, gateways, and controllers, all of which can be monitored and configured from a single interface.

## Enabling "concrete attacks"

These support zero-touch provisioning (ZTP), a mechanism that allows IT managers to deploy and maintain devices without needing to configure each one manually and on site.

However, ZTP has to establish trust between a factory-fresh device, and a controller with no human involved, so TP-Link used different shortcuts: from hard-coded keys and certificates shared across multiple devices, to default credentials, and from guessable serial numbers as “identity”, to weak session-key randomness.

Now, Forescout says 15 vulnerabilities its researchers discovered all allow for different ways of exploiting these shortcuts, meaning a flaw anywhere in the onboarding chain can compromise every device that goes through it. These bugs would need to be combined with two previously disclosed command-injection flaws, though.

“The vulnerabilities fall into four impact categories: client-side code execution, information disclosure, device hijacking and spoofing, and compromise of encrypted communications,” Forescout said. “Combined with two previously disclosed CVEs (CVE-2025-7850 and CVE-2025-7851), these flaws enable concrete attacks that let attackers infiltrate networks through controllers and client devices.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Out of the 15 discovered flaws, 11 received CVE identifiers, and the rest did not receive a tracking number.

Forescout said there are more than 1,800 Omada controllers accessible from the wider internet. If you are using any of the devices from the platform, you should head over to TP-Link’s download portal and grab the latest firmware for your device model.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

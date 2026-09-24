---
title: These cheap Skullcandy earbuds have a worrying Bluetooth flaw that could let
  anyone connect to your device
source_url: https://www.techradar.com/pro/security/these-cheap-skullcandy-earbuds-have-a-worrying-bluetooth-flaw-that-could-let-anyone-connect-to-your-device
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-15T04:45:53Z'
published: '2026-09-14T00:00:00Z'
description: Apple can push a firmware fix to earbuds already in your pocket - but
  Skullcandy cannot reach yours at all for now
image: https://cdn.mos.cms.futurecdn.net/G3oxprCVAwUWdyxSFfSoQL-1619-80.jpeg
categories:
- Technology & Software
- Business & Entrepreneurship
locations:
- Airoha
- Heidelberg
- Taiwan
people:
- Bob Kemerer
- Dennis Heinze
- Frieder Steinmetz
- Jacob Nowak
- Rahim Amir
organisations:
- Airoha
- Apple
- CERT Coordination Center
- CERT/CC
- CISA
- Carnegie Mellon University
- Dime 3
- ERNW
- Google News
- MediaTek
- PC
- PCs
- RGB
- SFF
- Skullcandy
- TROOPERS
- TechRadar Pro
- Tom's Guide
---

![Person listening to music](https://cdn.mos.cms.futurecdn.net/G3oxprCVAwUWdyxSFfSoQL.jpeg) 

- **Researchers warn Skullcandy Dime 3 earbuds on older firmware accept Bluetooth pairing from unknown devices with no user interaction required**
- **When leveraged, it can be used to interrupt the owner's connections, hijack playback, and even capture live microphone audio**
- **The vulnerability has been patched in a newer firmware update available only on newer units, does not seem to be addressable for existing earbuds**

Carnegie Mellon University's CERT Coordination Center has warned Skullcandy's Dime 3 wireless earbuds will accept a Bluetooth pairing request from a stranger's device without the owner doing anything.

The resulting bond is permanent, and the only sign the owner gets is a spoken "new device paired" notification delivered after it has already happened, with zero user interaction to confirm the request.

The advisory covering the Dime 3 was written by CERT/CC's Bob Kemerer and credits independent researcher Jacob Nowak, who had posted his findings to the Full Disclosure mailing list in early August after testing it on hardware he owned.

## A fix deployed that covers virtually no existing users

What makes this worse is that, ironically, while Skullcandy was swift in addressing the issue affecting earbuds running firmware version 1.0.0.28 by rolling out a patched version 1.0.0.30, it seems to address the issue only in newly made units.

CERT notes that there seem to be no "consumer-accessible" methods to upgrade existing units to the newest firmware because it reportedly has no support via the companion app, as a Tom's Guide review indicates.

A product without an update path that is user-accessible essentially means that its software flaws, or in this case, security issues, are here to stay for users who have had the bad luck of buying an earlier unit.

The underlying vulnerability, CVE-2025-20701, is not new and is not of Skullcandy's making. It is one of three vulnerabilities that Dennis Heinze and Frieder Steinmetz of the German firm ERNW disclosed in June 2025 at the TROOPERS conference in Heidelberg, affecting Bluetooth systems-on-chip from Taiwan's Airoha.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The Dime 3's Bluetooth identifier names Airoha as its chipset vendor, and while Airoha shipped a fixed SDK to its customers in June 2025 and published its bulletin that August, owners of the earbuds are in a unique situation, to say the least.

The vulnerability's severity is disputed: MediaTek (which owns Airoha) assigned it a relatively low 6.7 rating, while CISA's vulnerability enrichment program later assigned it an 8.8 with a 'high' categorization.

A potential attacker is limited to what the earbuds can access, since the vulnerability is essentially limited to the earbuds, but one could still wreak havoc with that alone. It should allow for more than just disrupting a person's routine by 'hijacking' one's earbuds by essentially using their microphones on them to record conversations or, in an extreme theoretical case (requiring chaining with other exploits), impersonate the headset and pull contacts, call history, and even pass hands-free commands to a paired smartphone. The latter, however, would require a high technical skill set, being within a few meters of a victim, and a Bluetooth connection turned on on the paired smartphone.

For now, a vulnerability exists that Skullcandy should have been able to patch, exactly as Apple recently did for its Beats Studio Buds, but a lack of support for any third party apps on the budget earbuds is somewhat annoyingly resulting in an unpatchable vulnerability for existing users.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png) 

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

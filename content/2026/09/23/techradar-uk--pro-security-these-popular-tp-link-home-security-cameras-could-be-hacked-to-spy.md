---
title: These popular TP-Link home security cameras could be hacked to spy on you while
  you sleep, experts warn
source_url: https://www.techradar.com/pro/security/these-popular-tp-link-home-security-cameras-could-be-hacked-to-spy-on-you-while-you-sleep-experts-warn
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-23T19:39:16Z'
published: '2026-09-23T00:00:00Z'
description: A fix is already available to download, so act now
categories:
- Technology & Software
image: https://cdn.mos.cms.futurecdn.net/8AQ6mNEWbxZfbYjrKfsCkF-1280-80.jpg
locations:
- Amazon
people:
- Khoi Tran
- Rahim Amir
- Thai Do
organisations:
- Google News
- OPSWAT
- PC
- PCs
- RGB
- SFF
- SKUs
- TP-Link
- Tapo C120
- TechRadar Pro
---

![Privacy](https://cdn.mos.cms.futurecdn.net/8AQ6mNEWbxZfbYjrKfsCkF.jpg)

* **Cybersecurity company OPSWAT found a login bypass and a crash bug in TP-Link's Tapo C200 cameras**
* **TP-Link has extended that to include its C120 offering too**
* **Anyone on the same network could get admin access, live video, and recordings without requiring the owner's credentials**

Security researchers at OPSWAT have detailed two high-severity flaws in TP-Link's Tapo C200, a pan-and-tilt indoor camera listed on Amazon for $26.99 and sold as a baby monitor and pet camera.

The more serious issue is that someone on the same network can log in as the camera's administrator without the password, accessing the live feed and stored recordings.

At least one other bug, which OPSWAT rates as critical in the same disclosure but does not detail, has not been published.

## A localized login that requires no authentication

![The TP-Link Tapo C200 camera](https://cdn.mos.cms.futurecdn.net/sXT4pLeU6CuMN5RuzCofpY.png)

The TP-Link Tapo C200, as we noted in previous coverage of the incident, isn't just another security camera that happens to be vulnerable; it is one of the most popular models on the market, clocking in at over 3,000 sales on Amazon alone.

The Tapo C120, in its current iteration, sells over 5,000 units monthly, even as the advisory notes that its V1 hardware version is currently compromised until users update the firmware on their devices.

Both SKUs have received firmware updates that patch the vulnerabilities (CVE-2026-15315 & CVE-2026-15316), which are assigned 'high' scores of 8.7 and 7.1, respectively. However, according to TP-Link, CVE-2026-15316 does not affect the C120 camera.

However, the former vulnerability is the more pressing of the two and, according to OPSWAT, is particularly problematic for users because of how the C120 and C200 cameras function.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Both run a local management interface over HTTPS and use a challenge-response login designed to prove a client knows the owner's password. Khoi Tran, a graduate fellow at OPSWAT, and his mentor, Thai Do of the company's Unit 515 team, found a second verification path in which, under certain conditions, a value the camera hands out during login can be sent back and accepted as a valid authentication response.

The result is an administrator session after a small number of requests, with no password, no existing session, and no requirements for the new 'owner'. As a result, access includes live video, stored footage, and configuration changes.

OPSWAT's researchers pointed out that a C200 used as a baby monitor would expose "live video, night vision, crying detection and two-way audio."

The second flaw, CVE-2026-15316, affects only the C200 and sits in its Wi-Fi onboarding code. Sending the camera an oversized chunk of encrypted Wi-Fi credential data can crash its HTTPS service or restart the device outright, cutting the owner off from management and monitoring until it recovers.

The attacks are somewhat limited in scope: users aiming to exploit such vulnerabilities would need to be on the same Wi-Fi network, or within a certain trusted ecosystem, to begin with.

For now, users upgrading to TP-Link's newest firmware, issued for both models, rectifies both issues, but there might already be another security patch in the works: OPSWAT also found "a critical vulnerability that could allow an attacker to fully compromise the camera," which could then serve as a foothold inside the network.

It is currently holding off on publishing any details about the vulnerability as it waits for TP-Link to issue a patch that rectifies the situation. Neither OPSWAT nor TP-Link, however, has provided a timeline for when the patch will be available to end users.

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

***Follow TechRadar on Google News***and** add us as a preferred source** * to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

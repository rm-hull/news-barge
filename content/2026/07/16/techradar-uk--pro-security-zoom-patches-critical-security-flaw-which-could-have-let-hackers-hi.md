---
title: Zoom patches critical security flaw which could have let hackers hijack accounts
source_url: https://www.techradar.com/pro/security/zoom-patches-critical-security-flaw-which-could-have-let-hackers-hijack-accounts
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-16T17:36:38Z'
published: '2026-07-16T00:00:00Z'
description: Zoom spots improper input validation bug which could have led to disaster
image: https://cdn.mos.cms.futurecdn.net/oQs6iUSDCYDEV6yP7Pj9Gh-1651-80.png
---

![Zoom Verified on LinkedIn Example](https://cdn.mos.cms.futurecdn.net/oQs6iUSDCYDEV6yP7Pj9Gh.png) 

- **Zoom patches critical improper input validation flaw in multiple Windows clients and SDKs that allowed remote account takeover**
- **Additional high‑severity bugs fixed include CVE‑2026‑53410 (TOCTOU race condition), CVE‑2026‑53409 (privilege management flaw), and CVE‑2026‑53411 (input validation issue)**
- **All vulnerabilities were found internally, with no evidence of exploitation; users are urged to update Zoom Workplace and related products to the latest versions**

Zoom has patched a critical-level vulnerability in multiple products that allowed threat actors to take over people’s accounts remotely.

In a security advisory, Zoom said it fixed an Improper Input Validation bug plaguing Zoom Desktop Client for Windows (before version 7.0.0), Zoom VDI Client for Windows (before versions 7.0.10, 6.6.15, and 6.5.18), and Zoom Meeting SDK for Windows (before version 7.0.0). It did not go into more details on how the flaw works.

The bug is now tracked as CVE-2026-53412, and was given a severity score of 9.8/10 (critical). To fix it, users are advised to update their software to the newest version.

## More vulnerabilities

While certainly the most dangerous one, this is not the only bug Zoom recently addressed. The company also fixed a handful of less severe vulnerabilities, including a time-of-check to time-of-use (TOCTOU) race condition bug affecting Zoom Workplace for Windows before 7.0.5, Zoom Workplace VDI Client and VDI Plugin before 6.5.17/6.6.14, Zoom Rooms for Windows before 7.0.5, and Remote Control for Zoom Contact Center before 7.0.0. This bug is tracked as CVE-2026-53410 and was given a “high” severity score of 7/10.

Other notable mentions include CVE-2026-53409 (a high-severity improper privilege management flaw in Zoom Rooms for Windows before version 7.1.0), and

CVE-2026-53411 (a high-severity improper input validation flaw affecting the Zoom Workplace VDI Plugin for Windows before version 6.6.14).

Zoom found all of these vulnerabilities in-house and says there is no evidence that any of these were abused in real-life attacks in the past.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Zoom Workplace (the company’s all-in-one collaboration platform) offers video meetings, team chat, phone, email, calendar, scheduling, whiteboards, and other productivity tools. It is an evolution of the original Zoom Meetings app which now competes with platforms such as Microsoft 365 and Google Workspace.

*Via**BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

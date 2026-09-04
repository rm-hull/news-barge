---
title: Cisco patches three critical vulnerabilities as part of 'comprehensive internal
  security review'
source_url: https://www.techradar.com/pro/security/cisco-patches-three-critical-vulnerabilities-as-part-of-comprehensive-internal-security-review
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-04T18:59:27Z'
published: '2026-09-04T00:00:00Z'
description: A total of eight flaws were fixed
image: https://cdn.mos.cms.futurecdn.net/4vPx4qpVwRADJoMvv3gttX-970-80.jpg
---

![Cisco](https://cdn.mos.cms.futurecdn.net/4vPx4qpVwRADJoMvv3gttX.jpg) 

- **Cisco patched eight IOS XR flaws, including three critical (CVE‑2026‑20274, CVE‑2026‑20279, CVE‑2026‑20212)**
- **Vulnerabilities allow unauthenticated exploitation, improper access control, and crafted input execution**
- **No abuse reported; patches urged, with iACL workarounds for Nexus 9000 devices using Silicon One ASIC**

Cisco patched eight vulnerabilities affecting its IOS XR operating system, including three critical-severity ones. It urged its customers to apply the patches as soon as possible, even though it stressed that there is no evidence any of these were abused in the wild.

The company detailed its findings in two advisories published on the same day - September 2.

In the first one, it disclosed seven vulnerabilities, including two critical-severity ones: CVE-2026-20274 and CVE-2026-20279. Both carry a severity rating of 9.8/10 (critical). The former is an improper control of a resource during its lifetime flaw - a network-based, low complexity, vulnerability that requires no authentication or user interaction to be exploited. The latter is described as an improper access control vulnerability that can lead to the same consequences.

## Fixes and mitigations

These flaws, along with five others, affect all releases of Cisco IOS XR Software, including Cisco IOS XR7 (LNT) Software, regardless of device configuration, the company explained. There are no available workarounds, and installing the provided patch is the only way to mitigate the risk.

The third flaw, disclosed in a separate advisory, is tracked as CVE-2026-20212. Successfully exploiting this one allows attackers to connect to an affected device and send crafted input that could be executed as code, without root privileges. “The exploitation of this vulnerability could also cause the S1HAL process to crash, which could cause the device to reload,” Cisco explained.

This bug affects Cisco Nexus 9000 Series Switches if they include a Silicon One ASIC, the company stressed. A possible workaround is to use infrastructure access control lists (iACLs) to allow only required management and control plane traffic that is destined to the affected device. There is also the option of iACLs only being used to explicitly deny all TCP packets that are destined to a locally configured IP address with a destination port of 43210 or 43211.

*Via**The Register*

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: Cisco routers are being turned into surveillance vantage points to hoover up
  data on trusted networks — and it's all thanks to this new malware
source_url: https://www.techradar.com/pro/security/cisco-routers-are-being-turned-into-surveillance-vantage-points-to-hoover-up-data-on-trusted-networks-and-its-all-thanks-to-this-new-malware
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-01T19:23:51Z'
published: '2026-09-01T00:00:00Z'
description: Fire Ant is now targeting routers, authentication servers, and Linux
  management hosts
image: https://cdn.mos.cms.futurecdn.net/EEXAxCUDKAq3frELz3rVYY-1920-80.jpg
---

![A group of 7 hackers, 6 slightly blurred in the background and one in the foreground, all wearing black with hoods pulled up over their heads. You cannot see their faces.](https://cdn.mos.cms.futurecdn.net/EEXAxCUDKAq3frELz3rVYY.jpg) 

- **Sygnia reports China‑linked Fire Ant expanding beyond virtualization to routers, TACACS, and Linux hosts**
- **Compromised routers act as operational platforms**
- **Campaign aims at “target behind the target,” leveraging trust relationships for broader espionage reach**

Fire Ant, a China-nexus cyberespionage group, is no longer targeting just virtualization platforms, it’s also going for routers, authentication systems, and Linux management hosts. This is according to cybersecurity researchers Sygnia, who recently saw the group target Cisco IOS XR Routers.

Once they compromise a router, they don’t just use it to move around the network, the researchers explained. Instead, they turn them into full-blown operational platforms, collecting traffic, establishing connections, manipulating command output, and even suppressing logging so that they fly under the defenders’ radars.

For authentication systems, Fire Ant was seen taking aim at TACACS servers. Admins use them to authenticate when accessing network hardware, and crooks use them to harvest valuable credentials and weaken the reliability of audit logs, as well. Finally, Sygnia says Fire Ant also targets Linux management hosts. The researchers saw multiple persistent implants and backdoors, including a custom SSH backdoor and a piece of malware spoofing legitimate software.

## Target behind the target

The goal of the campaign seems to be to establish a foothold that allows crooks to reach other environments. Sygnia describes it as a “target behind the target” scenario:

“This reinforces the “target behind the target” concept introduced earlier in this report. Fire Ant’s interest in the compromised organization should be understood not only as an attempt to compromise a single environment, but as an effort to control infrastructure that may enable visibility, collection, and potential access beyond the immediate victim. The strategic value lies in the trust relationships the organization maintains with connected environments,” Sygnia explained.

Very little is known about Fire Ant, besides the fact that it was first observed in 2025. Some researchers claim it has significant overlaps with a threat actor tracked as UNC3886, a Chinese espionage group previously observed by Google. However, there are also significant differences which make attribution inconclusive.

*Via**BleepingComputer*

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

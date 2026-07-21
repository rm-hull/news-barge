---
title: Watch out - that Microsoft Calendar invite dated 2050 could be hiding stolen
  files and worse
source_url: https://www.techradar.com/pro/security/watch-out-that-microsoft-calendar-invite-dated-2050-could-be-hiding-stolen-files-and-worse
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-21T17:40:40Z'
published: '2026-07-21T00:00:00Z'
description: Check your calendars for entries far into the future
image: https://cdn.mos.cms.futurecdn.net/NK6WMQwJZAmbq9SfRREf2f-2560-80.jpg
---

![Top view of woman holding smartphone and tablet with calendar on desk](https://cdn.mos.cms.futurecdn.net/NK6WMQwJZAmbq9SfRREf2f.jpg) 

- **Group‑IB discovers HollowGraph malware targeting Israeli entities, exfiltrating files via Microsoft Graph API**
- **Operators hide instructions in future calendar entries, then attach encrypted stolen data to events**
- **At least 12 systems were compromised; overlaps with Lyceum noted but attribution remains low‑confidence**

Cybercriminals have found a way to communicate with the malware installed on victim devices through compromised Microsoft Calendar apps, experts have warned.

Security researchers at Group-IB have detailed a newly discovered piece of malware called HollowGraph designed to exfiltrate sensitive files from compromised devices.

What makes the malware stand out is the way it communicates with its operators. The best way to spot hidden malware is to monitor the traffic flowing in and out of a device, which is why cybercriminals try their best to hide this traffic, or blend it with another, legitimate one. In that respect, HollowGraph is unique because it abuses Microsoft Graph API and a compromised Microsoft 365 mailbox calendar.

## A dozen victims

After landing on a device and compromising the Microsoft 365 account, HollowGraph uses that account’s permissions to access Microsoft Graph. Operators create calendar entries containing instructions and place them far into the future (in the year 2050) to avoid being spotted. After acting on the instructions and harvesting valuable information, the malware exfiltrates it through the same channel.

Instead of uploading files to a suspicious server, HollowGraph attaches encrypted stolen data to calendar events and sends it through Microsoft Graph. For defenders, all of this traffic seems legitimate and usually flies under their radars.

So far, all of the victims are Israeli entities, Group-IB said. The researchers identified at least 12 compromised systems, three of which were still actively communicating with the attackers’ infrastructure during the investigation.

The researchers did not attribute the attack to any known threat actor, but hinted at a potential. They identified technical similarities in command structures and plugin mechanisms between HollowGraph’s framework, Cavern, and a .NET backdoor used by Lyceum (an Iranian-nexus threat actor associated with OilRig). However, Group-IB explicitly emphasizes that these overlaps are not distinct enough, so they assess this link with low confidence.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

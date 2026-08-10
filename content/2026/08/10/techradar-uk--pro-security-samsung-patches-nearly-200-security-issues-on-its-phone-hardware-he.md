---
title: Samsung patches nearly 200 security issues on its phone hardware - here's what
  you need to know
source_url: https://www.techradar.com/pro/security/samsung-patches-nearly-200-security-issues-on-its-phone-hardware-heres-what-you-need-to-know
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-10T17:05:02Z'
published: '2026-08-10T00:00:00Z'
description: Samsung's bloatware carried dangerous flaws
image: https://cdn.mos.cms.futurecdn.net/BBM4XfubmWGFTaMhYGgJKX-2000-80.jpg
---

![Samsung Galaxy S23 Ultra review angled tea](https://cdn.mos.cms.futurecdn.net/BBM4XfubmWGFTaMhYGgJKX.jpg) 

- **Oversecured found 176 vulnerabilities across Samsung’s preinstalled mobile apps**
- **Flaws enabled account takeover, code execution, and traffic hijacking via bloatware**
- **Samsung patched all reported issues, affecting hundreds of millions of devices**

Security researchers from Oversecured have given “bloatware” an entirely new meaning, revealing that they uncovered 176 vulnerabilities - including some rather worrying ones - in Samsung’s mobile apps.

For the last three years, the team analyzed Samsung’s preinstalled system applications and found vulnerabilities that could cause some serious harm. Some of the bugs granted camera and microphone access, while others allowed for remote Samsung Account takeover with nothing more than a single click.

Some flaws allowed for network traffic hijacking via DNS manipulation, and others granted arbitrary code execution via an image. In theory, a malicious actor could craft and send a JPEG image which, when the victim opens, copies and loads attacker-controlled native libraries from the SD card. Finally, Oversecured found path traversal vulnerabilities allowing writing arbitrary files to the file system without proper path validation.

## Arbitrary code execution

The researchers disclosed their findings to Samsung which, according to their report, fixed all of the reported issues - the full list can be found on __GitHub__.

Most Android smartphone manufacturers preload their devices with proprietary apps - think Bixby, Samsung Free, or AR Zone. These apps - which cannot be uninstalled or removed from the devices - aren’t necessary to their operations and are often not wanted by the users in the first place.

This 'bloatware' is also one of the key selling propositions of Google Pixel devices, since these are considered “stock Android”, or bloatware-free.

Out of context, these bugs are nothing extraordinary. Single-click account takeover flaws and traffic hijacking bugs pop up every now and then and get fixed rather quickly. The context here is that these are Samsung’s proprietary apps that don’t fall under the protection of Google’s Play Protect. Users might think they’re safe because they’ve not downloaded apps from risky places, or enabled dangerous permissions, when in reality, they’re not safe at all:

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“Preinstalled system applications run with extra privileges than normal apps, cannot be removed by users, and operate outside Google Play Protect,” the researchers warned. “A single vulnerability affects hundreds of millions of devices globally through one vendor's distribution channel.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

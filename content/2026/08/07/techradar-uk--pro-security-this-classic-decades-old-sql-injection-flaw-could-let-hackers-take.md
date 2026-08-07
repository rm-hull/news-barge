---
title: This 'classic' decades-old SQL injection flaw could let hackers take over entire
  Windows servers, thanks to a nifty database trick
source_url: https://www.techradar.com/pro/security/this-classic-decades-old-sql-injection-flaw-could-let-hackers-take-over-entire-windows-servers-thanks-to-a-nifty-database-trick
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-07T17:03:57Z'
published: '2026-08-07T00:00:00Z'
description: Huntress spotted a white whale
image: https://cdn.mos.cms.futurecdn.net/vEiXHZbWKMMSpkbbmnWVwP-1920-80.jpg
---

![database](https://cdn.mos.cms.futurecdn.net/vEiXHZbWKMMSpkbbmnWVwP.jpg) 

- **Huntress saw Oracle SQLi used to deploy rare khunt toolkit**
- **Khunt enabled OS commands, credential theft, and registry hive exfiltration**
- **Defense includes input sanitation and more**

Someone managed to pair the classic SQL Injection (SQLi) attack with a nifty database trick to take over the underlying system entirely.

Security researchers Huntress, who were called in to investigate the incident, said the investigation first showed a classic, decades-old technique called an SQL injection attack: a public-facing application with an Oracle backend accepted and executed SQL commands input into a form without checking whether that input was valid or not.

This granted the attackers the ability to upload a database-resident, posts-exploitation toolkit named khunt. This technique is something of a cyber-white whale: it’s been widely discussed but rarely seen in the wild.

## How to defend

“What happened next, however, raised our eyebrows,” Huntress said. “After performing SQL injection, the threat actor managed to upload a database-resident, post-exploitation toolkit named khunt. This is a technique that's previously been discussed and described over the years, including via a technique described as oraexec – however, the use of the technique in the wild has rarely been documented.”

As a toolkit, khunt granted the attackers multiple capabilities, including loading cmd.exe on the system and running arbitrary OS commands, steal usernames and passwords, listing, reading, searching, and checking file sizes (essentially looking around the compromised system), unzipping files, and more.

Of all the things they could have done, the attackers opted to run a PowerShell command and invoke the Windows Registry tool, copying the SAM, SECURITY and SYSTEM registry hives. They can later use the copies to extract and decode password hashes for local accounts on the system, the researchers explained.

To defend against such attacks, Huntress recommends making sure the forms aren’t injectable. “Practice proper input sanitization and query parameterization for any inputs,” they warned. “It's also important to ensure that users with the ability to execute queries aren't overprovisioned.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Even if someone manages to pull off SQL injection, user accounts should not be capable of authoring Java sources or running stored procedures.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: These popular Tenda routers have an unpatched security backdoor which could
  give hackers access
source_url: https://www.techradar.com/pro/security/these-popular-tenda-routers-have-an-unpatched-security-backdoor-which-could-give-hackers-access
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-09T18:07:41Z'
published: '2026-07-09T00:00:00Z'
description: CERT/CC finds a critical flaw in multiple Tenda routers, warning users
  to be careful.
image: https://cdn.mos.cms.futurecdn.net/xiF2oa9QT4q5sePeRdA8Af-1920-80.jpg
---

![cables going into the back of a broadband router on white background](https://cdn.mos.cms.futurecdn.net/xiF2oa9QT4q5sePeRdA8Af.jpg) 

- **CERT/CC discloses CVE‑2026‑11405, a critical 9.8/10 flaw in multiple Tenda router families caused by a hardcoded backdoor credential**
- **Attackers can bypass normal login checks and gain full admin access with the hidden password, regardless of configured username or password**
- **Tenda has not responded; CERT/CC advises disabling remote web management and limiting local exposure, though these are only partial mitigations**

Multiple Tenda router families carry a critical vulnerability that allows malicious actors to log in with admin privileges without knowing the credentials, experts have found.

The CERT Coordination Center disclosed a vulnerability in Tenda routers which it described as an undocumented authentication backdoor caused by a hardcoded credential.

The flaw is tracked as CVE-2026-11405 and was assigned a severity score of 9.8/10 (critical). CERT/CC allegedly tried reaching out to the manufacturer, to no avail.

## How the vulnerability works

Explaining how it works, CERT/CC says that the attacker would first try to log into the router’s web management interface normally. Even if the credentials are wrong, the firmware would not automatically reject them, but would rather check a second, hidden password, stored internally. If the attacker knows the hidden credential, they get full admin access, regardless of the configured admin password or username.

The username doesn’t even matter, as long as the password is supplied. Obviously, CERT/CC did not say what the password was, but with a little reverse-engineering of the firmware, it can be exposed either on the dark web, or to the general public.

Tenda is a Chinese company building budget networking gear, popular mostly in India and adjacent markets, where its products are popular in homes and among small businesses.

The flaw thus still affects multiple firmware versions, including FH1201, W15E, AC10, AC5, and AC6 router families. To make matters worse, CERT/CC added that the full list of affected models is probably even bigger.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Tenda is yet to comment on the findings. In the meantime, CERT/CC recommended users disable remote web management, if possible, to make sure the vulnerability cannot be exploited remotely, at least. The organization also suggests limiting local network exposure, but stresses that this is not an entirely bulletproof solution.

*Via**Tom's Hardware*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: A cheap Temu device allows attackers to execute instructions remotely.
source_url: https://www.techradar.com/pro/expert-finds-this-gbp3-temu-wi-fi-extender-is-full-of-security-issues-and-definitely-not-the-bargain-youd-hoped-for
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-13T13:18:28Z'
published: '2026-09-13T00:00:00Z'
description: This six-antenna £3 Wi-Fi extender came with a secret password shared
  across every unit running its firmware
image: https://cdn.mos.cms.futurecdn.net/q8rXV4rnByXw28AGiSLWQg-1920-80.png
categories:
- Technology & Software
- Business & Entrepreneurship
---

![Temu Wi-Fi Extender](https://cdn.mos.cms.futurecdn.net/q8rXV4rnByXw28AGiSLWQg.png) 

- **A £3 Wi-Fi extender carried hidden administrator access beyond ordinary user controls**
- **Every device running the firmware shared the same concealed administrator password**
- **Changing the visible administrator password could not disable the secret account**

A £3 Wi-Fi extender bought through Temu has exposed security problems that challenge the idea of cheap connected devices being simple bargains.

Security researcher Keiran Smith examined the device and discovered hidden access features that ordinary users would never see during normal operation.

Smith, who holds a penetration-testing certification, picked up the six-antenna extender after seeing it promoted through a targeted ad on the shopping app.

## The cheap extender contained access users could not control

The examination began with the hardware, where he identified a MediaTek MT7620 processor commonly used in low-cost networking products.

After extracting the firmware stored inside the device, Smith found a hidden administrator account with complete control over its functions.

The account used a fixed password embedded inside the software, meaning every unit using that firmware carried the same credentials.

Changing the normal administrator password through the device settings would not remove this separate hidden access.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Smith also found a remote login service that accepted the concealed credentials without requiring physical access to the extender itself.

“It’s worth being precise about what makes this as bad as it is, because ‘hardcoded password’ covers a wide range of sins,” Smith said

The researcher said this case was more serious because the password remained identical across devices rather than being generated individually.

“A default credential is something the owner can see, is told about and can change,” he said. “What we have here is the opposite on every count.”

“This one is a compile-time constant rather than something derived from the MAC address or serial number, so it is identical on every unit ever sold.”

The combination of hidden access, unchanged credentials, and remote availability creates a security concern for ordinary owners.

Even if technically skilled users discovered the account, Smith found that changes could disappear after restarting the extender.

## Additional flaws raise questions about cheap connected hardware

The investigation also uncovered a command injection weakness that could allow attackers to execute unauthorized instructions through the device.

Smith found that the extender lacked strong protection around software updates, creating possible opportunities for tampered firmware installation.

He admitted that these issues did not prove that manufacturers intentionally created unsafe features for malicious purposes.

They could have originated from factory testing processes and remained active accidentally before consumer sales.

This Temu extender shows how extremely cheap smart devices can create security challenges beyond their purchase price.

Consumers may focus on immediate savings while having little visibility into the software decisions built inside connected equipment.

The findings do not mean every inexpensive networking device contains similar weaknesses, though they show why basic security checks matter.

As more homes add connected products, hidden software features could become a larger concern for users and manufacturers.

Via CyberNews

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png) 

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

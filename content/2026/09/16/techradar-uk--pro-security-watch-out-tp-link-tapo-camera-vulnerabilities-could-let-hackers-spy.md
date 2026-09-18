---
title: Watch out — TP-Link Tapo Camera vulnerabilities could let hackers spy inside
  homes, so patch now
source_url: https://www.techradar.com/pro/security/watch-out-tp-link-tapo-camera-vulnerabilities-could-let-hackers-spy-inside-homes-so-patch-now
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-16T19:32:18Z'
published: '2026-09-16T00:00:00Z'
description: Researchers find two flaws in highly popular cameras
image: https://cdn.mos.cms.futurecdn.net/JoaAAvDK3PPAJUwTSBoEM7-1920-80.jpg
categories:
- Technology & Software
---

![TP-Link C200](https://cdn.mos.cms.futurecdn.net/JoaAAvDK3PPAJUwTSBoEM7.jpg) 

- **Opswat found two flaws in TP‑Link Tapo C200 cameras: auth bypass (CVE‑2026‑15315) and DoS (CVE‑2026‑15316)**
- **Bugs let attackers hijack admin sessions or crash devices; millions of users potentially exposed**
- **TP‑Link patched with firmware V5_1.4.6 on Aug 18, 2026; users urged to update immediately**

Security researchers found a pair of vulnerabilities in popular smart cameras, which could allow threat actors to peep into people’s homes and businesses.

Earlier this week, Opswat disclosed finding two bugs in the TP-Link Tapo C200 smart security camera - an authentication bypass flaw, and a denial-of-service vulnerability. The former is tracked as CVE-2026-15315 and was given a severity score of 8.7/10 (high). Opswat says the bug allows unauthenticated attackers to obtain valid admin sessions without having a password, which would allow them to manage the device and even watch the stream.

The latter is tracked as CVE-2026-15316. With a severity score of 7.1/10 (high), this bug allows threat actors to send oversized crypted ciphertext values that may trigger exception handling failures and cause the affected device to crash or restart. “Successful exploitation may temporarily disrupt HTTPS management and monitoring functionality, resulting in a denial-of-service (DoS) condition until the service recovers,” according to the NVD.

## Patching the bugs

The C200 is a mass-market product, advertised as a security camera, a baby monitor, or a pet camera, with motion detection, 1080p video, 2-way audio, night vision, cloud & SD card storage, and integrations with both Alexa and Google Home.

Opswat disclosed their findings to TP-Link in mid-April this year, which started working on a fix in early July this year. On August 18, 2026, TP-Link released firmware version V5_1.4.6, which addressed both flaws. Users are advised to install the fix as soon as possible.

The researchers did not discuss if the flaws were being abused in the wild, or to what extent. We do know that TP-Link Tapo cameras are rather popular, with the C200 model being relatively widely sold. According to TP-Link, the Tapo app has more than 13 million users, while the Google Play Store shows 10+ million downloads.

On Amazon, the C200 specifically is listed as the #1 top rated product in its category, with more than 3,000 purchases this month alone.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

"Camera bugs always get attention because of the "spy factor," but they usually sound cooler and scarier than they actually are," said Dahvid Schloss, OSCP, Chief Operating Officer at Suzu Labs. "The main reason not to "worry" about this one is that running this exploit requires local network access, so a threat actor has to be on your Wi-Fi or already own a device that is.

"If someone's made it that far into your network, they're not after the baby monitor. Now, if the camera was port-forwarded to the internet, that's a bigger design issue and probably should be a concern, but not a common setup for the everyday home user. Either way, I'd still patch the camera, but it's pretty low on the totem pole of what a cybercriminal wants."

"I'm quite curious about the undisclosed vulnerability that reportedly allows full compromise and a foothold to pivot from," Schloss added. "Based on what was reported, I would guess the exploit would be a command injection or a memory-safety bug in the same management service, chained behind that auth bypass to get code execution as root, where they then dropped a static binary to return a shell on the device whose firmware ships with almost no tooling. That attack chain isn't uncommon on cheap, older consumer IoT devices where security wasn't top of mind, but if that's the case here, seeing it hold up on a modern TP-Link device would be a bit of a blast from the past.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: IT helpdesk impersonation hits Microsoft Teams once again, with the hackers
  hiding their activity within legitimate tools
source_url: https://www.techradar.com/pro/security/it-helpdesk-impersonation-hits-microsoft-teams-once-again-with-the-hackers-hiding-their-activity-within-legitimate-tools
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-03T19:16:55Z'
published: '2026-09-03T00:00:00Z'
description: Microsoft is warning about an ongoing scam campaign
image: https://cdn.mos.cms.futurecdn.net/D4YBMfcEsNT7BhaNJJgm2A-2560-80.jpg
---

![Collaboration in an office.](https://cdn.mos.cms.futurecdn.net/D4YBMfcEsNT7BhaNJJgm2A.jpg) 

- **Microsoft warns of Teams‑based campaign where attackers impersonate IT staff**
- **Victims tricked into granting remote access, leading to malware, lateral movement, and ransomware**
- **Defenses: verify support contacts, train staff, harden Teams, and use Defender Safe Links/ZAP**

Microsoft is warning about an ongoing hacking campaign that starts with a Teams message and ends with a ransomware infection and data theft.

In a new in-depth report published on the Microsoft blog, it was said that unnamed threat actors were reaching out to their targets at various enterprises via a Teams chat, while impersonating IT staff.

They were coercing their victims into granting remote access via screen sharing or remote monitoring and management tools and once received, used their access to install malware loaders and various other implants.

## How to defend against Teams-borne phishing

The malware was just the first stage of the attack. Subsequent stages include host reconnaissance, security-product and virtualization discovery, and “periodic desktop screen capture”. In other words - mapping out the landscape and conducting espionage.

The crooks would then enumerate domain accounts, servers, and users, through native tools and Active Directory Service Interfaces (ADSI) queries and begin moving laterally.

The final step includes identifying and extracting valuable data, followed by a ransomware infection.

Microsoft does not name the perpetrators, and mostly refers to them as “threat actors”. It makes sense, since the “fake IT support via Teams” technique is being used by multiple groups at this moment. Russia’s Cozy Bear, FIN7, and Storm-1811 are probably the most obvious examples.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The world’s biggest extortionists - ShinyHunters - are also known to use Teams to trick victims into granting access, but this group rarely deploys an encryptor and instead just focuses on data exfiltration.

Whoever the attackers are, and whoever they’re after, one thing is for certain - the risk in the enterprise environment has never been greater.

That is why Microsoft advises reinforcing user education by establishing internal helpdesk authentication phrases, and by training employees to recognize external-tenant indicators.

The company also urges enterprises to verify unsolicited support contact, and to harden Microsoft Teams and email against social engineering. “Use Microsoft Defender for Office 365 with Safe Links and Zero-hour auto purge (ZAP) so malicious messages and URLs are neutralized at time of click and removed after delivery,” Microsoft urges.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

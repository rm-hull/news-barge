---
title: Microsoft 365 users hit by phishing scheme posing as RingCentral emails
source_url: https://www.techradar.com/pro/security/microsoft-365-users-hit-by-phishing-scheme-posing-as-ringcentral-emails
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-05T14:29:01Z'
published: '2026-08-05T00:00:00Z'
description: Greatness PhaaS are going after Microsoft 365 accounts
image: https://cdn.mos.cms.futurecdn.net/rsstAB5QjUqoXwXYPEgT7d-1920-80.jpg
---

![Phishing](https://cdn.mos.cms.futurecdn.net/rsstAB5QjUqoXwXYPEgT7d.jpg) 

- **ZeroBEC observes Greatness PhaaS evolving to bypass MFA and phish Microsoft 365, iCloud, Yahoo, and Google Workspace accounts**
- **Attackers spoofed RingCentral emails post‑ShinyHunters breach, luring victims to fake Microsoft 365 logins that capture authentication tokens**
- **Greatness is sold on Telegram for $289/month, enabling access to Outlook, Teams, SharePoint, OneDrive, and more across multiple regions**

Microsoft 365 users have been getting phishing emails spoofing RingCentral, designed to steal their accounts even if they were protected by multi-factor authentication (MFA), experts have warned.

Security researchers ZeroBEC claim to have observed a phishing-as-a-service (PhaaS) platform called Greatness evolve to also target MFA accounts, as well.

Greatness used to be a simple credential phishing platform. However, in recent times, it evolved to target not just Microsoft 365 accounts, but also those of iCloud, Yahoo, and Google Workspace.

## Grabbing MFA-approved authentication tokens

ZeroBEC notes that RingCentral recently suffered a data breach at the hands of the infamous ShinyHunters hackers, meaning there is a good chance (although not confirmed) that the threat actors exfiltrated a list of emails belonging to RingCentral customers from that attack, and used it in this attack.

Now, RingCentral customers have been getting emails that look as if they are coming from the company itself, despite being mailed from an unknown mail server, and despite failing SPF and DMARC checks. The emails are the standard fake voicemail and performance-review notifications which, if clicked, redirect the victim to attacker-owned infrastructure spoofing the Microsoft 365 login page.

Through this malicious landing page, Greatness operators are able to capture MFA-approved authentication tokens, bypassing the login process entirely and moving straight into victim accounts.

From there, they would enumerate Outlook mailboxes, Teams conversations, and SharePoint sites. They would also access OneDrive files, contacts, calendars, and registered applications through Microsoft Graph.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The number of victims is unknown at the time, but ZeroBEC says Greatness has been active for at least four years now, targeting users in the US, UK, Australia, Canada, and South Africa.

According to *BleepingComputer*, the platform is being advertised for sale on Telegram channels with “thousands of subscribers”, and is currently being offered for a monthly fee of $289.

*Via**BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

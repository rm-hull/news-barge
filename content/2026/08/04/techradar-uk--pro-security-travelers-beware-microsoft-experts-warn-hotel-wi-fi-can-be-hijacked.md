---
title: Travelers beware — Microsoft experts warn hotel Wi-Fi can be hijacked to infect
  your devices with dangerous malware
source_url: https://www.techradar.com/pro/security/travelers-beware-microsoft-experts-warn-hotel-wi-fi-can-be-hijacked-to-infect-your-devices-with-dangerous-malware
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-04T14:36:52Z'
published: '2026-08-04T00:00:00Z'
description: Russian hackers are targeting hotel Wi-Fi networks with captive portals
image: https://cdn.mos.cms.futurecdn.net/euoWA3SymQA2cKKjmF37W4-1920-80.jpg
---

![Wi-Fi](https://cdn.mos.cms.futurecdn.net/euoWA3SymQA2cKKjmF37W4.jpg) 

- **Microsoft reports Russian APT29 (Midnight Blizzard) hijacking captive portals in hotels and conference centers**
- **Victims redirected to fake Microsoft 365 logins or bogus update pages, spreading CornFlake and CocoShell malware**
- **CornFlake steals files, credentials, and device data; CocoShell targets browser cookies, passwords, and Microsoft tokens**

Threat actors are taking over Wi-Fi networks in hotels and conference centers and using the log-in portals to steal credentials and deploy information-stealing malware, experts have claimed.

Researchers from Microsoft have published a new report outlining how they spotted Russian state-sponsored actors, known as Midnight Blizzard or APT29, attacking captive portal equipment - networking hardware and software that manages the login page users see before accessing public Wi-Fi.

When connecting to a hotel network, users are often redirected to a page where they must enter their room number, accept the terms of service, and click “Connect” - that redirection is handled by the captive portal.

## CornFlake and CocoShell

Microsoft did not explain exactly how this gear is attacked. However, when users try to log in on compromised networks, they may be redirected to a fake Microsoft 365 login portal that steals their credentials.

They may also be redirected to device code phishing pages abusing Microsoft Entra ID authentication flows. Finally, the researchers also saw the captive portals being used to display fake browser and OS update pages that trick victims into downloading infostealers.

So far, MIcrosoft found two malware variants being distributed: CornFlake, and CocoShell.

CornFlake acts as an infostealer capable of grabbing keystrokes and clipboard, running remote shell access, grabbing screenshots, using the microphone and the webcam, stealing browser credentials and cookies, exfiltrating files, and more. It presents itself as a “Cloud Sync Service” while using multiple persistence mechanisms.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

CocoShell, on the other hand, is an in-memory PowerShell credential stealer targeting browser cookies, saved passwords, Microsoft 365 and Azure AD tokens, and Wi-Fi credentials.

APT29 is one of the most documented state-sponsored threat actors out there. It’s been active for years and is well-known for its links to Russia’s Foreign Intelligence Service and notable attacks on high-ranking western targets, such as US and German Government officials, as well as SolarWinds and Microsoft.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

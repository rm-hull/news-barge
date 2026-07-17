---
title: '''macOS users may face real, sophisticated threats that require neither exploits
  nor any elevated access to succeed'': ClickLock Stealer tries to trick Apple users
  into revealing their passwords'
source_url: https://www.techradar.com/pro/security/macos-users-may-face-real-sophisticated-threats-that-require-neither-exploits-nor-any-elevated-access-to-succeed-clicklock-stealer-tries-to-trick-apple-users-into-revealing-their-passwords
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-17T17:21:20Z'
published: '2026-07-17T00:00:00Z'
description: ClickLock bores its victims into complying
image: https://cdn.mos.cms.futurecdn.net/VGPtSi99Vy7pCWeNLEcT5c-2560-80.jpg
---

![hacker hands at work with interface around](https://cdn.mos.cms.futurecdn.net/VGPtSi99Vy7pCWeNLEcT5c.jpg) 

- **Group‑IB uncovers ClickLock, a new macOS‑focused infostealer using aggressive social engineering by spamming password prompts and terminating key apps every 210ms until victims comply**
- **Once credentials are obtained, it exfiltrates browser data, crypto wallets, password manager entries, FTP configs, and device info via Telegram Bot API**
- **Active since May 2026, spotted in 33 countries (mostly Europe), distributed via ClickFix campaigns, and initially undetected by security vendors until recently**

Security researchers from Group-IB have uncovered a new infostealer targeting primarily macOS users in Europe.

Dubbed ClickLock, it is more of an annoying social engineering mechanism rather than a full-blown malware variant, constantly popping up a login prompt on the victim’s device, until they finally comply and share the credentials.

Every 210 milliseconds it terminates key apps on the device (Finder, Dock, TErminal, etc.), essentially making it useless. At the same time, it keeps prompting a password dialog on the screen, making sure the victim can do nothing but provide the credentials.

## Targeting Europeans

The loop is set to continue for more than three straight days, or until the victim folds.

After getting the keys to the kingdom, the malware gets to work and starts exfiltrating valuable information.

This includes data from key browsers (Chrome, Firefox, Brave, and others), saved logins, cookies, autofill data, and other browser information, data linked to cryptocurrency wallets and extensions, encrypted wallet vault material that can be cracked off-site, data from password managers, cached cryptocurrency addresses across EVM, Bitcoin, Solana, TRON, TON, and Stacks, shell histories, FileZilla FTP configuration and recent-server data, and basic device information.Everything is then packaged into a .ZIP archive and exfiltrated via a Telegram Bot API.

Group-IB says the campaign has been active since at least May 2026, so it’s been active for a few months now. A researcher submitted a variant to VirusTotal in early June, but it remained undetected by all security vendors until recently, Group-IB says.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

So far, it has been spotted in 33 countries, more than half of which are in Europe, it was also added. The malware is most likely being distributed via a ClickFix social engineering campaign, and has not been tied to any particular threat actor.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

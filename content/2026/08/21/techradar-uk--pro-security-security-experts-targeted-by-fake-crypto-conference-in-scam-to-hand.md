---
title: Security experts targeted by fake crypto conference in scam to hand over details
source_url: https://www.techradar.com/pro/security/security-experts-targeted-by-fake-crypto-conference-in-scam-to-hand-over-details
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-21T16:48:25Z'
published: '2026-08-21T00:00:00Z'
description: Huntress discovers a new twist to the ClickFix tale
image: https://cdn.mos.cms.futurecdn.net/y7GLevUTEjLYdujEYsv668-2560-80.jpg
---

![Back view of hooded internet criminal hacking laptop in the dark, stealing credit card details](https://cdn.mos.cms.futurecdn.net/y7GLevUTEjLYdujEYsv668.jpg) 

- **Huntress spotted a ClickFix campaign targeting security pros via fake conference invites** 
- **Victims tricked into pasting code that installs AMOS infostealer on macOS** 
- **If lured, isolate systems, reset credentials, rotate secrets, and review cryptocurrency wallets**

Cybercriminals are targeting security professionals with a highly tailored ClickFix campaign in an attempt to get their computers infected with infostealer malware, experts have warned.

An active campaign against people who have attended, or have a history of attending, various cybersecurity conferences such as Black Hat, or DEF CON has been detetced by security researchers Huntress, who were targets themselves.

The attack starts on X, where the threat actor uses a fake account to interact with people visiting and sharing content from these conferences. After establishing rapport, they move into DMs, claiming they’re organizing a conference of their own, and sharing a Google Docs file containing “more info” with the victim.

## Follow-up attack

Here is where the attackersy go for the ClickFix attack. The document comes with a vertical sidebar, apparently as a security feature that keeps the contents of the file encrypted. The victim is given a decryption code to enter, but it returns an error and offers a solution - to bring up the Terminal and copy/paste a piece of code.

From here, it’s the usual ClickFix practice: the victim ends up downloading and running AMOS, a notorious Mac infostealer capable of grabbing browser information, cookies, keychain data, cryptocurrency wallet information, Telegram files, and more. The Windows variant did not work when Huntress tried to analyze it, but it’s safe to assume the end goal is the same.

Huntress also found that this is not where the attack ends. If the victim does not install the infostealer, the threat actor will follow up with a different document, this time pretending to be for Dropbox and working only with the desktop app. Of course, the download button leads straight back to the infostealer.

The researchers shared a full list of Indicators of Compromise (IoC) which can be found on this link. They also advised anyone who interacted with this kind of lure to isolate the system from the network, collect relevant forensic evidence, and “consider reimaging the system”.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“Assume that credentials on the system have been compromised”, they said. “Revoke active sessions, reset passwords, and rotate API keys or any other secrets that may reside on the system. Review cryptocurrency wallets as well, if present.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

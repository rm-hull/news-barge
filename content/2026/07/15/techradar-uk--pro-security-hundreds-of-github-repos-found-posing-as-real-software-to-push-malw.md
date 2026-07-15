---
title: Hundreds of GitHub repos found posing as real software to push malware
source_url: https://www.techradar.com/pro/security/hundreds-of-github-repos-found-posing-as-real-software-to-push-malware
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-15T17:35:02Z'
published: '2026-07-15T00:00:00Z'
description: Russian hackers are trying to sneak infostealers onto people's devices
image: https://cdn.mos.cms.futurecdn.net/YQaVTQE6JAfu6bvPgwmd5U-2560-80.jpg
---

![Phone malware](https://cdn.mos.cms.futurecdn.net/YQaVTQE6JAfu6bvPgwmd5U.jpg) 

- **ArcticWolf uncovered 292 malicious GitHub repositories spoofing legitimate tools and products, delivering a new BoryptGrab infostealer variant**
- **Malware steals from 19 browsers, 32 crypto wallets, messaging apps, Steam, and Windows Credential Manager, and uniquely bypasses Chrome’s App‑Bound Encryption via code injection**
- **Most repos have been removed, but some remain active; GitHub’s popularity makes it a prime target, underscoring the need to vet code before use**

Russian actors have reportedly created hundreds of malicious GitHub repositories masquerading as legitimate software but acting as a dangerous infostealer.

Cybersecurity researchers ArcticWolf discovered the campaign after finding their own products spoofed as part of the attack.

In total, the researchers found 292 fake repositories, spoofing things like security products, developer tools, macOS utilities, games, and more. Each repository contained a README file with the download URL.

## Obviously malicious

Victims who download the program get a variant of the BoryptGrab infostealer family that grabs data from 19 browsers (passwords, cookies, payment information), 32 cryptocurrency wallets, Telegram, Discord, and Steam sessions, credentials for Meta’s Max, data from Windows Credential Manager, and more. It can also exfiltrate files from Desktop and Documents, and grab screenshots.

While most of the features can be found in other BoryptGrab variants, this one is unique in a sense that it can bypass Chrome’s App-Bound Encryption through direct code injection into the browser process.

While it hasn’t been specifically said that the threat actors are Russian, the compressed data is later sent to a Russia-based command-and-control (C2) infrastructure.

What’s also worth mentioning is that the malware is not designed to last. It has no anti-analysis layer, and doesn’t even try to hide itself in any specific manner. It does not establish persistence and simply tries to grab as much sensitive data as it can on the first attempt.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The attack, which seems to have started in the final days of June, is almost thwarted now, since most of the malicious repositories have been removed from GitHub. Citing “researchers”, *BleepingComputer* reported that several dozen still remain active, though.

Because of its importance and popularity in the open-source community, GitHub is currently one of the most targeted platforms on the internet, which is why it’s important to double-check and vet every piece of code before it’s applied to a project.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

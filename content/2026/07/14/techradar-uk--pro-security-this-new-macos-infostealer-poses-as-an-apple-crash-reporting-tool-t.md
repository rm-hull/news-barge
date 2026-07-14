---
title: This new macOS infostealer poses as an Apple crash reporting tool to try and
  steal all your valuable data
source_url: https://www.techradar.com/pro/security/this-new-macos-infostealer-poses-as-an-apple-crash-reporting-tool-to-try-and-steal-all-your-valuable-data
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-14T14:08:07Z'
published: '2026-07-14T00:00:00Z'
description: Researchers found a new piece of macOS malware
image: https://cdn.mos.cms.futurecdn.net/ctJuqMRzZN6mdeA4UPgdTd-1920-80.jpg
---

![The menu bar running in macOS.](https://cdn.mos.cms.futurecdn.net/ctJuqMRzZN6mdeA4UPgdTd.jpg) 

- **Jamf researchers uncover “CrashStealer,” a notarized macOS infostealer disguised as Apple’s CrashReporter**
- **Distributed via a fake site called “Werkbit Setup”, it bypasses Gatekeeper, installs a LaunchAgent**
- **It then uses a fake password prompt to unlock Keychain, exfiltrating credentials, cookies, files, and data from 80 crypto wallets and 14 password managers**

A new macOS infostealer has been spotted in the wild, masquerading as an Apple crash reporting tool, experts have warned.

Called CrashStealer, this C++ infostealer was designed to nab login credentials, keychain information, as well as data related to more than 80 cryptocurrency wallets.

Cybersecurity researchers Jamf published an in-depth report on the malware, noting CrashStealer is most likely distributed via a fake software site that was only registered recently.

## Unlocking Keychain

Victims who land on the site (either via a social media recommendation or search engine results) need to know the PIN code before initiating the download. This was most likely done to avoid analyst scrutiny, as well as to increase perceived credibility and a sense of exclusivity.

Usually, apps downloaded from third-party sources are scanned by Gatekeeper, Apple’s built-in security system. However, Jamf says that this payload is delivered via a signed and Apple-notarized installer and distributed as a disk image named “Werkbit Setup”, which allowed it to bypass Gatekeeper without any warnings.

Those that download and run the program will get a binary named ‘CrashReporter.app’, which will create a LaunchAgent (‘com.apple.crashreporter.helper’), and will see a fake macOS password prompt.

That prompt unlocks the user’s Keychain where most of their secrets are stored (passwords, private cryptographic keys, and more) and then exfiltrates all information to a third-party server.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Besides Keychain data, the CrashReporter malware also pulls browser credentials and cookies from most browsers, data from 80 cryptocurrency wallet extensions, 14 password managers, locally stored files, and more.

Jamf said CrashReporter overlaps, to some extent, with other known infostealers (AMOS, for example), but is still unique enough given its client-side encryption mechanism, as well as the native C++ implementation.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

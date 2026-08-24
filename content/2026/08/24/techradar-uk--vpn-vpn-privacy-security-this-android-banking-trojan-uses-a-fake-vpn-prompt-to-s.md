---
title: This Android banking trojan uses a fake VPN prompt to silence Google's defenses
source_url: https://www.techradar.com/vpn/vpn-privacy-security/this-android-banking-trojan-uses-a-fake-vpn-prompt-to-silence-googles-defenses
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-24T16:52:13Z'
published: '2026-08-24T00:00:00Z'
description: The upgraded ToxicPanda malware disguises a network takeover as a routine
  VPN request, then cuts off Google's on-device protections
image: https://cdn.mos.cms.futurecdn.net/tEhgdM2MKoCYRwV4Ch3awa-2048-80.jpg
---

![malware](https://cdn.mos.cms.futurecdn.net/tEhgdM2MKoCYRwV4Ch3awa.jpg) 

- **Researchers found banking malware requests VPN permissions to block Google Play and Play Protect on infected Android phones**
- **ToxicPanda 2.0 bypasses security to install hidden payloads, targeting 349 banking and crypto apps across 16 countries** 
- **The malware can even seize shell-level control of a device**

Security researchers have flagged a new twist in Android banking malware: a trojan that turns your phone's own VPN feature against you.

A report from mobile security firm Zimperium details how ToxicPanda 2.0 abuses VPN permissions to shut down Google's built-in protections before it strikes.

The tactic is effective because it hides in plain sight. Plenty of legitimate apps ask for VPN access, and even the best VPN apps rely on the same underlying permission to route your traffic. ToxicPanda copies that request, but uses the access to cut your phone off from Google Play instead.

Once Google Play Protect can no longer reach the device, the malware has a clear runway to install its payload and begin harvesting your data.

## How ToxicPanda uses VPN permissions to blind Google Play

ToxicPanda operates as a "dropper," an app that smuggles in a second, hidden program. According to Zimperium researchers, the malware first shows a fake installation screen and prompts the victim to grant VPN permissions. That request looks routine, so many users tap "allow" without a second thought.

Granting it lets ToxicPanda create a local network interface that sits between the phone and the internet, giving the malware control over all traffic passing through the device. It immediately uses that control to block communication with Google Play and Google Play Services.

Cutting off this connection lets the malware interfere with app verifications, updates, and Play Protect, the security layer that would normally flag or remove a harmful app. With Google effectively blindfolded, ToxicPanda decrypts a payload hidden in its own files, installs it, and then asks for Accessibility Service permissions to dig deeper.

 ![Screenshots from a malware app](https://cdn.mos.cms.futurecdn.net/8Ne52JFZZ7mzAM8PtByEdh.png) 


This release is a major escalation from the previous ToxicPanda iteration.

As Zimperium says, ToxicPanda 2.0 now supports 167 remote commands. It can also overlay fake login screens on 349 banking, e-wallet, and crypto apps across 16 countries, up from just 16 apps previously. A separate module harvests PINs from more than 140 financial apps using invisible overlays that capture your taps.

The trojan can also spoof your Android lock screen to steal your PIN, pattern, or password, and it abuses Android's Wireless Debugging (ADB) feature to gain shell-level access and grant itself permissions without prompts.

ToxicPanda first appeared in 2024, targeting European banks. Other similar malware such as Rokarolla, has also hit hundreds of banking and crypto apps in recent months.

## How to stay safe

The strongest defense is to keep the malware off your phone in the first place.

Only install apps from the official Google Play Store, and avoid sideloading APK files from links, ads, or third-party sites. Be aware that dangerous VPN links have even slipped into official app stores, so treat any surprise VPN prompt with suspicion.

A legitimate VPN remains a valuable privacy tool, but this campaign is a reminder that the permission itself is powerful, so grant it only to apps you genuinely trust.

***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds. Make sure to click the Follow button!*

![Monica J. White](https://cdn.mos.cms.futurecdn.net/6AQ4y5nzk8kQ47Yp69GERj.jpg)

Monica is a tech journalist with over a decade of experience. She writes about the latest developments in computing, which means anything from computer chips made out of paper to cutting-edge desktop processors.

GPUs are her main area of interest, and nothing thrills her quite like that time every couple of years when new graphics cards hit the market.

She built her first PC nearly 20 years ago, and dozens of builds later, she’s always planning out her next build (or helping her friends with theirs). During her career, Monica has written for many tech-centric outlets, including Digital Trends, SlashGear, WePC, and Tom’s Hardware.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

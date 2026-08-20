---
title: Android users beware — if you own one of these budget smartphones, your device
  could be hacked with a simple video call
source_url: https://www.techradar.com/pro/security/android-users-beware-if-you-own-one-of-these-budget-smartphones-your-device-could-be-hacked-with-a-simple-video-call
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-20T20:40:51Z'
published: '2026-08-20T00:00:00Z'
description: Exploitable Improper Isolation
image: https://cdn.mos.cms.futurecdn.net/sMMYYw2WasgE4m4saLhZ9M-2560-80.jpg
---

![A man looking frustrated at his mobile phone](https://cdn.mos.cms.futurecdn.net/sMMYYw2WasgE4m4saLhZ9M.jpg) 

- **Unisoc system-on-chip (SoC) devices – usually budget smartphones – are vulnerable to a video call-based exploit**
- **Any smartphone can be used to place the call, with malicious code sent in call setup messages**
- **Despite attempts, Unisoc did not respond to the disclosure**

Security researchers have demonstrated a weakness in several Unisoc SoC-based devices that makes them vulnerable to an exploit sent during a video call. The exploit can deliver root access of the target device to the attacker, placing them in full control of the handset.

The vulnerability is in the firmware running on several Unisoc SoCs, each of which are used in budget smartphones, including models from Xiaomi, Motorola, and Realme.

A successful attack can be used to alter an Android device’s operating system, but the proof-of-concept was tested on a controlled network rather than a carrier network. Additionally, the devices involved were rooted. Consequently, the attack may not have real-world implications.

## Which phones are affected?

While you may not know the name Unisoc, it is a big player in the chip business, sitting fourth behind MediaTek, Qualcomm, and Apple. Its chips appear in IoT and smart home devices, as well as mobile technology, typically for well-known companies including Samsung and Motorola.

The researcher who uncovered the vulnerability is known only by the alias 0x50594d.

They tested the exploit on three models:

• Realme C33

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

• Xiaomi Redmi A5 (with security patch level 2026-01-01)

• Motorola E13 (running security patch level 2025-02-01)

In addition, the phones were installed with the July 2025 Android security update.

The advisory indicates that the flaw is in the modem firmware of four Unisoc SoCs. These are the T612, T616, T606, and T7250, which means any phone using those SoCs is potentially at risk.

However, it is important to note that the vulnerability was exploited in specific conditions.

## Improper Isolation

The phones used in testing the exploit were all rooted, a process that makes devices prone to malware. In the majority of cases, these phones would not normally be rooted. In addition, the exploit was tested across a closed VoLTE network, rather than across a carrier network.

Finally, as noted, the phones were running older security patches. So, the conditions for the exploit are very specific, but nevertheless concerning.

0x50594d’s research was published on the SSD Secure Disclosure website, which summarized it as an “exploitable Improper Isolation of Shared Resources on System-on-a-Chip. A critical vulnerability has been identified in the Unisoc modem firmware that allows arbitrary code execution with kernel privileges from the modem context.”

“An attacker who gains the ability to execute code on the modem can read from and write to the entire memory space by disabling protections on the first Memory Protection Unit (MPU) region (region ID 0).”

It is should be noted that Unisoc has so far failed to respond to the security disclosure.

*Via**Cybernews*

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Christian Cawley](https://cdn.mos.cms.futurecdn.net/zBDYnjPnB2XPvhKbYX9Kuc.png)

Christian Cawley has extensive experience as a writer and editor in consumer electronics, IT and entertainment media. He has contributed to TechRadar since 2017 and has been published in Computer Weekly, Linux Format, ComputerActive, and other publications.

He currently heads up the team at smart home website Matter Alpha, and writes about retro gaming at Gaming Retro.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

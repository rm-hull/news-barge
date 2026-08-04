---
title: A potentially dangerous macOS security flaw went unreported due to Apple being
  deluged by AI slop bug reports
source_url: https://www.techradar.com/pro/security/a-potentially-dangerous-macos-security-flaw-went-unreported-due-to-apple-being-deluged-by-ai-slop-bug-reports
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-04T14:36:06Z'
published: '2026-08-04T00:00:00Z'
description: Security researchers found high-severity RCE flaw in macOS
image: https://cdn.mos.cms.futurecdn.net/gth8FZBY7MR8cmk3vbbJ6N-1920-80.jpg
---

![The Apple M5 Pro and M5 Max chips against a black background.](https://cdn.mos.cms.futurecdn.net/gth8FZBY7MR8cmk3vbbJ6N.jpg) 

- **Bynario disclosed CVE‑2026‑43760, a macOS RCE flaw allowing root file creation via legacy VNC password option**
- **Apple patched it July 27, 2026 in macOS Tahoe 26.6 and Sonoma 14.8.8; unpatched users should disable Screen Sharing/Remote Management or the legacy VNC setting**
- **Reporting was delayed as Apple limited submissions due to AI‑generated bug report overload, but the company reached out directly to fix this issue**

Apple has fixed a high-severity vulnerability that allowed threat actors to execute malicious code remotely (RCE), as root, on certain macOS devices - and would have probably fixed the issue even sooner; had it not been flooded with AI slop vulnerability reports.

Security researchers Bynario published an in-depth report discussing finding an RCE flaw on macOS 26.5.2 devices running on Apple Silicon M4 and M5 systems, with System Integrity Protection (SIP) enabled.

According to Bynario, the vulnerability affects Mac devices with Screen Sharing or Remote Management enabled, and with the legacy "VNC viewers may control screen with password" option turned on. For those devices, should a threat actor obtain the VNC password and authenticate to the Mac (no macOS account compromise is required, only the VNC password), they would be able to perform file-transfer operations, with root permissions, due to a logic flaw.

![NordStellar Threat Exposure Platform NordStellar Threat Exposure Platform](https://cdn.mos.cms.futurecdn.net/UkssaJUuTjbMsQ9NN4ejH7-200-80.jpg.webp)

NordStellar provides businesses of all sizes with a comprehensive threat exposure management platform to bolster your cybersecurity. NordStellar actively monitors for data breaches and exposed credentials to prevent hackers gaining easy access, while simultaneously implementing a range of cybersecurity tools to keep employees and company data safe.

Use coupon code **TECHRADAR10** for an additional 10% off.

## Drowning in the AI flood

The attacker would then be able to create new files owned by root anywhere the system allows.

In the report, the researchers demonstrated creating a valid file inside /private/etc/sudoers.d, granting passwordless sudo privileges, and once that policy was in place, they were able to run commands as root.

In a separate report, the researchers said Apple was forced to limit the number of active bug reports individual researchers can keep open at one time, due to its security teams being flooded with AI slop reports.

Since they already hit that threshold by submitting more than 50 bugs in three weeks, the researchers were unable to report this RCE flaw sooner. However, they explained that Apple reached out to Bynario directly to review, and later patch, the flaw.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The bug is now tracked as CVE-2026-43760 and was given a severity score of 8.6/10 (high).

Apple released the updates on July 27, 2026, addressing the bug on macOS Tahoe 26.6 and macOS Sonoma 14.8.8.

Those who cannot patch should disable the legacy "VNC viewers may control screen with password" option or disable Screen Sharing and Remote Management entirely.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

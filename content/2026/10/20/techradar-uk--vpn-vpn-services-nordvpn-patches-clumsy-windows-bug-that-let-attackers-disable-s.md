---
title: NordVPN patches "clumsy" Windows bug that let attackers disable system services
source_url: https://www.techradar.com/vpn/vpn-services/nordvpn-patches-clumsy-windows-bug-that-let-attackers-disable-system-services
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-20T14:22:11Z'
published: '2026-10-20T00:00:00Z'
description: The vulnerability allowed low-privileged local attackers to disable unprotected
  Windows services, but critical antivirus defenses remained completely safe.
image: https://cdn.mos.cms.futurecdn.net/kEn3wXDv34dPV6X2rbZfFW-1945-80.jpg
categories:
- Technology & Software
people:
- Mallory
- Marcin Ressel
- Mike Williams
locations: []
organisations:
- CERT Polska
- IT Security
- LinkedIn
- Nord Security
- NordVPN
- TechRadar
- VPN
---

![NordVPN](https://cdn.mos.cms.futurecdn.net/kEn3wXDv34dPV6X2rbZfFW-1920-80.jpg)

* **A vulnerability in NordVPN's Windows app allowed local attackers to stop unprotected system services.**
* **The flaw, officially tracked as CVE-2026-106030, does not affect NordVPN version 8.12.0.0 or later**
* **Experts label the bug "clumsy," but the actual impact on users is minimal, requiring a device to already be compromised by malware.**

Nord Security has rolled out an important security update for its Windows application to address a vulnerability that could allow a hacker to stop unprotected Windows services.

The flaw allowed a local, low-privileged attacker to act as a trusted process. From there, they could potentially stop unprotected Windows services or change their startup types to manual, leading to a denial of service for those specific applications.

When a top-tier provider, frequently ranked as the best VPN on the market, flags a security patch of this nature, it naturally turns heads. However, cybersecurity experts stress that while the coding error shouldn't have happened, the real-world danger to users is incredibly low.

The issue, officially tracked as CVE-2026-106030, was responsibly reported to CERT Polska by IT Security Expert Marcin Ressel. NordVPN appears to have fixed the vulnerability in version 8.12.0.0, and users are simply advised to ensure their app is fully up to date.

## How the vulnerability works

![NordVPN Windows](https://cdn.mos.cms.futurecdn.net/DNLsiQgDNuZzEN5z5KNdPk-1200-80.jpg)

To understand the bug, you have to look at how Windows applications talk to each other using a feature called "named pipes."

According to an intelligence brief published by Mallory, the vulnerability allowed an attacker to connect to a specific NordVPN named pipe and invoke methods to stop services or change their start types without proper authorization.

Mike Williams, Technical Editor at TechRadar, explains the core of the issue: "Named pipes are a common means for Windows processes to communicate with each other. One process might send a message to another asking it to carry out some task."

Because this communication channel is incredibly powerful, it is a frequent target for threat actors. "Because named pipes are so sensitive, hackers often try to abuse them, to run these tasks without permission," Williams notes. "That means it's important to secure them, and make sure that only messages from legitimate processes are accepted. Any good developer knows this: it's a fundamental aspect of using named pipes."

Unfortunately, the NordVPN Windows app, specifically versions earlier than 8.12, fell short of this standard. "NordVPN has failed to do that, which makes this a clumsy bug. It should never have happened," Williams adds.

## Why the real-world impact is minimal

While the technical details of the flaw, which carries a CVSS v4 base severity score of 6.8, sound alarming, the practical implications for the average user are far less dramatic.

In a LinkedIn post, the researcher who discovered the flaw, Marcin Ressel, described it as "a local privilege escalation with limited impact" that he found while "playing around with NordVPN for Windows."

Crucially, this exploit can't shut down critical, system-protected security services. Built-in defenses like Windows Defender and processes guarded by Windows Tamper Protection are entirely immune to this specific attack.

> "There's no impact on the VPN itself, and you would have to have malware running on your PC to even cause the issue"
>
> Mike Williams, Technical Editor

"But the impact of the bug is very small," Williams clarifies. "All an attacker can do is change the status of non-critical Windows services. That is, it can't turn off Windows Defender, but maybe it could disable something related to media playback. But even if it did that, it's only flipped a Windows setting, and once you understood the cause, you could just flip it back."

Furthermore, this vulnerability cannot be triggered remotely over the internet. An attacker would already need to have a local foothold on your machine to exploit it. There has also been no active exploitation of this flaw reported in the wild.

"In other words, there's no impact on the VPN itself, and you would have to have malware running on your PC to even cause the issue," Williams concludes. "(And if there's malware running on your device then you've much bigger problems than this.)"

If you are running NordVPN on Windows, your best defense is simple: open the app and confirm you are running version 8.12.0.0 or later.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

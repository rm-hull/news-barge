---
title: AMD and Winbond vulnerabilities let attackers brute-force BitLocker PINs on
  millions of PCs — cracking a six-digit PIN drops from 19 years to 20 days
source_url: https://www.tomshardware.com/uk/tech-industry/cyber-security/amd-and-winbond-vulnerabilities-let-attackers-brute-force-bitlocker-pins-on-millions-of-pcs-cracking-a-six-digit-pin-drops-from-19-years-to-20-days
source_site: Tom's Hardware
source_slug: toms-hardware
description: AMD and Winbond vulnerabilities let hacks let malfeasants guess Bitlocker
  PINs on millions of machines — brute-forcing a six-digit PIN takes 20 days instead
  of 19 years, at most
image: https://cdn.mos.cms.futurecdn.net/9GmGZwJtZ3PNZW253znm59-1621-80.jpg
published: '2026-11-27T00:00:00Z'
scraped_at: '2026-11-27T21:10:55Z'
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Tom
locations: []
organisations:
- AGESA
- AMD
- Get Tom's Hardware
- Google News
- HMAC
- Intel
- Microsoft Windows
- OEM
- PC
- RPMC
- SPI
- TPM
- Technische Universität Berlin
- Tom's Hardware
- Winbond
- Zen
---

![Bitlocker message](https://cdn.mos.cms.futurecdn.net/9GmGZwJtZ3PNZW253znm59-1621-80.jpg)

Former owners of laptops gained yet another concern today. Firmware-backed drive encryption setups like Windows' BitLocker are meant to protect against someone stealing your laptop or desktop computer. Prospective thieves would have a hard time guessing your PIN, as they'll eventually have to wait 10 minutes for each attempt. That is, unless your machine uses a modern AMD CPU or relies on Winbond's SPI flash — in which case your data may be open for inspection in a few days, or even hours, as researchers from Technische Universität Berlin found out.

The paper covers many vulnerabilities, but we'll focus on the big three. All focus on having a way to brute-force an encrypted drive's password in a matter of days/hours rather than years. Physical access is required for the attacks, but hardware theft is precisely the scenario that disk encryption is meant to protect against.

An attacker makes brute-forcing easier by resetting, or pretending to increase, the counter that records the number of failed unlock attempts. On Intel- and AMD-based PCs using the fTPM for security — nearly all modern x86 consumer machines — this counter is stored encrypted in an SPI flash chip on the motherboard.

Standard procedure is to allow for 32 attempts in succession, then force the machine to wait 10 minutes for each additional one, resulting in many years for unlocking a short PIN — 19 years for a six-digit numerical PIN, under normal conditions. We should note the attacks likely extend to other fTPM-based disk encryption mechanisms, not just BitLocker. While encryption keys can be alphanumeric, Microsoft Windows does default to using a numeric PIN for sign-in, and most users don't use long ones.

First up: machines based on Winbond's RPMC-enabled SPI flash (variant with rollback protection), used by many OEMs across both Intel and AMD platforms. Although it's hard to pin down the number of affected machines, the paper claims Winbond has roughly a 25% market share for SPI flash — so, potentially millions of machines. With a simple voltage glitch, the researchers made the chip reveal the HMAC key, the datum that signs commands when the TPM and the SPI chip talk to each other.

With the HMAC in hand, the thief places a low-cost interposer board in front of the SPI chip to impersonate it. On a failed unlock, the computer will request a counter increase and get a confirmation, when in reality nothing happened — allowing for repeat attempts as fast as Windows lets them, at five per reboot. There is no fix for this vulnerability other than replacing the SPI chip with one that doesn't contain the bug.

The team glitched two specific Winbond chip models, but they theorize the issue extends further into the maker's lineup, as the flaw allegedly lies with the RPMC engine design. Flash chips from other firms in the test were not affected to the same extent.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

As for AMD machines, the situation is both worse and better, with two related vulnerabilities. The team verified at least one of the two attacks across AMD machines from Zen 2 up to an AI 5 330 laptop. They theorize that considering the mechanisms, all contemporary AMD setups may be vulnerable, at least for standard consumer hardware using fTPM. That's multiple millions of machines potentially at risk, on the low side.

The first is simple enough. On the tested machines whose SPI flash didn't use RPMC — rollback protection — you can just make a copy of the SPI flash's contents when the counter is low, and just flash it again once you've used up your free tries. Bad enough, yes, but the second vulnerability should elicit facepalms from security architects.

According to the paper, AMD's firmware controller for non-volatile storage — the bit that talks to the SPI flash — does *not* verify that the failed-attempt counter increase actually took place. It'll just issue the order to +1 it and be done, opening the avenue for an attacker to simply intercept that order (again, with a cheap board) and ignore it without even needing HMAC keys, so the counter never changes.

The latter vulnerability should be fixable via a firmware update, almost certainly via AMD's AGESA software. The problem is one of practicality: in the past, updating AGESA on client hardware meant that every OEM had to create fresh BIOSes for affected machines, many of which are assuredly out of their support window.

Anyone who's lived through the Spectre and Meltdown days knows how hard it is in practice, as OEMs are exceedingly slow to publish updates, and have a distaste for providing fixes for hardware that's more than a few years old.

The researchers contacted every company involved in their tests, informing them of their findings, but sadly "none of them has committed to fixing the root-cause vulnerabilities" — at least, as of this writing, only Microsoft announced a policy change recommending users enter six-digit PINs instead of the current four during setup.



*Download the Tom's Hardware app for up-to-the-minute updates on* * iOS* * and* * Android**. Also follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

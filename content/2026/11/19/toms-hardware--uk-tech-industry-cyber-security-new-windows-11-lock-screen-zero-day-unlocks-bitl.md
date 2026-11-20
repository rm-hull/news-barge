---
title: New Windows 11 lock screen zero-day unlocks BitLocker-protected PCs with just
  a few keystrokes — Win+U keyboard trick lets physical attackers run USB payloads
  or create new admin accounts
source_url: https://www.tomshardware.com/uk/tech-industry/cyber-security/new-windows-11-lock-screen-zero-day-unlocks-bitlocker-protected-pcs-with-just-a-few-keystrokes-win-u-keyboard-trick-lets-physical-attackers-run-usb-payloads-or-create-new-admin-accounts
source_site: Tom's Hardware
source_slug: toms-hardware
description: Windows 0-day lets attackers run software by partially bypass the lock.
  screen with just some keystrokes — even BitLocker-protected machines are seemingly
  vulnerable
image: https://cdn.mos.cms.futurecdn.net/sR3wn4pbkQv44DiMtCfRCY-2048-80.jpg
published: '2026-11-19T00:00:00Z'
scraped_at: '2026-11-20T02:17:18Z'
categories:
- Technology & Software
- Hardware
people:
- Abdelhamid Naceri
- Bruno Ferreira
- Reddit
- Tom
locations:
- Narrator
organisations:
- Google News
- Microsoft
- PC
- Tom's Hardware
---

![Security vulnerability](https://cdn.mos.cms.futurecdn.net/sR3wn4pbkQv44DiMtCfRCY-1920-80.jpg)

Considering the current status of the cybersecurity landscape, some may well say that "0-day" has lost its meaning, The latest high-stakes vulnerability pertains to a bug in Windows 11 (and possibly 10), wherein an attacker can partially bypass the lock screen and run software as the logged-in user, and seemingly access their data. If true, the vulnerability means even BitLocker won't help keep users' files protected.

Unsurprisingly, the bug was discovered by Abdelhamid Naceri, the prolific Windows hacker known to the world as Nightmare Eclipse, and is responsible for about a dozen zero-day findings in Microsoft's operating system. The exploit requires physical access to the machine, but that's precisely the scenario that lock screens and/or BitLocker are supposed to protect against.

To trigger the vulnerability, all you need is a keyboard. In the Windows 11 lock screen, click "Forgot my PIN," then hit Win+U to bring up the voice narrator. The window will be hidden behind the lock screen, which, for practical purposes, is just a veneer, but you can interact with it using the keyboard if you hold down the Caps Lock key and use the arrows and Enter.

After some brief navigation through Narrator, you'll actually be in Settings, and then have multiple avenues for further shenanigans. One obvious one is going into Bluetooth and Devices and setting Autoplay to show a USB stick's files and folders, then plugging in your own with your software of choice to run. Additionally, on a personal machine, the user is bound to have administrator permissions, so you can just create your own account.

This bug is quite fresh, so there isn't widespread reporting or testing. The author claims "the vulnerability seems to be extremely consistent in every machine I tested it in." We did encounter a sysadmin on Reddit, danrhodes1987, who claims they've tested it on machines they manage, and sure enough, it works, though only on their InTune-enrolled devices. He says that "you can launch anything you want in the context of the user logged onto the device."

Additionally, they found it possible to invisibly navigate whichever programs the user had open before they locked their screen, which all but guarantees that the victim's entire data and programs will be fully accessible. As a Windows sysadmin friend of mine remarked, Windows' lock screen implementation always felt like a kludge, and he posits this won't be the last hack found for it.



*Download the Tom's Hardware app for up-to-the-minute updates on* * iOS* * and* * Android**. Also follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

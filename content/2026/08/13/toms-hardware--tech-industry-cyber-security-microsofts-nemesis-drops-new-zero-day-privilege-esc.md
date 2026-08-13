---
title: Microsoft's nemesis drops new zero-day privilege escalation vulnerability —
  attack grants system-level privileges, but it could already be patched
source_url: https://www.tomshardware.com/tech-industry/cyber-security/microsofts-nemesis-drops-new-zero-day-privilege-escalation-vulnerability-attack-grants-system-level-privileges-but-it-could-already-be-patched
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-13T20:56:32Z'
published: '2026-08-13T00:00:00Z'
description: The researcher's vendetta against Microsoft continues apace, but it seems
  like the company could be keeping up this time around
image: https://cdn.mos.cms.futurecdn.net/CrscyWC2mg69wBbrK9dcpa-2176-80.jpg
---

![Software bug](https://cdn.mos.cms.futurecdn.net/CrscyWC2mg69wBbrK9dcpa.jpg) 

Prolific hacker and Microsoft nemesis 'Nightmare Eclipse' has just published ShieldBreak, yet another Windows zero-day vulnerability that ought to get you SYSTEM-level privileges just by running some code as a regular user. Although Eclipse has generally kept ahead of Microsoft, it seems the company may be catching up, as our own quick testing found this exploit is already detected by Defender and might even be patched as of last Tuesday.

As described by the author, ShieldBreak is essentially a continuation of the previously reported RoguePlanet vulnerability in Windows Defender's subsystems. Eclipse claims that Microsoft failed to properly patch RoguePlanet, and that ShieldBreak in theory bypasses the recently added protection.

The proof-of-concept code for the new exploit is supposed to bring up a super-elevated command prompt with SYSTEM privileges (higher than Administrator). The author claims the vulnerability is present in the "latest" versions of Windows 11, Windows Server 2025, and Windows 10, though the proof-of-concept is limited to the former two operating systems.

Although researchers like Kevin Beaumont and Will Dormann say they've successfully reproduced the exploit, our informal testing in a Windows 11 virtual machine didn't yield any results. Said VM was just updated yesterday with the latest Windows 11 patches and currently sits at version 10.0.**26200.9168**. Given that Microsoft just published a giga-patch last Tuesday, there's a solid chance it plugged whichever hole ShieldBreak was getting through.

The sample screenshot in the ShieldBreak repository shows the exploit working under version 10.0.**26100.33296**, lending some credence to this theory.* A sample size of one does not research make*, so we advise caution and remind everyone to run their own testing before assuming the bug has truly been fixed.

Microsoft appears to have already published a Defender detection for it. We found it when double-checking our results, with just a 20-minute window between both tests, as shown in the screenshot below.

 ![ShieldBreak vulnerability detected by Defender](https://cdn.mos.cms.futurecdn.net/iA84GombBvogaz5XrSKteB.png) 


Even if the issue is fixed, not every user updates their machines as soon as patches are available, and perhaps more importantly, corporations tend to hold back on patches until they know they don't bring in any new issues. That means that a good portion of the world's machines may still be vulnerable to ShieldBreak.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Little is known about Nightmare Eclipse, other than that they *really* don't like Microsoft and claim the company has ruined their lives. Some cybersecurity experts like Brian Krebs and Kevin Beaumont have offered up the theory that Eclipse is a disgruntled Microsoft ex-employee.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

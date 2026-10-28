---
title: Most data centers and servers on the planet could be vulnerable to dangerous
  UEFI firmware flaw — here's what we know
source_url: https://www.techradar.com/pro/security/most-data-centers-and-servers-on-the-planet-could-be-vulnerable-to-dangerous-uefi-firmware-flaw-heres-what-we-know
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-28T19:22:18Z'
published: '2026-10-28T00:00:00Z'
description: A critical buffer overflow vulnerability was found in EDK II, with patch
  code already available
image: https://cdn.mos.cms.futurecdn.net/QXcBRNeHkzXC6am5m3TXYf-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
- Science
people:
- Alex Matrosov
- Dan Goodin
- Dan Holmes
locations: []
organisations:
- AMI
- Anthropic
- Ars Technica
- EDK II
- Google
- NVD
- National Vulnerability Database
- TechRadar Pro
- TianoCore Project
- UEFI
---

![Computer programming code. Programming code abstract technology background of software developer and Computer script. ](https://cdn.mos.cms.futurecdn.net/QXcBRNeHkzXC6am5m3TXYf-1920-80.jpg)

* **Researchers uncover critical UEFI firmware flaw that could enable remote code execution on servers**
* **Public release of patch code may accelerate exploit development before many vendors deploy updates**
* **Delayed firmware patching across hardware ecosystems leaves organizations exposed despite available fixes**

Cybersecurity researchers from Anthropic and Google have discovered a critical-severity vulnerability in boot-time firmware used by practically every server in existence today.

A patch is available, but given the fragmented market of UEFI manufacturers, it could take months before most of the servers are secured. In the meantime, patch code was made publicly available, which means cybercriminals will have their work laid out for them.

## Discovering the bug

Virtually all modern servers today run UEFI (Unified Extensible Firmware Interface), software built into the server’s motherboard that helps start the device and load the operating system. It includes security features like Secure Boot, which helps stop unauthorized programs from running when the machine starts.

The free, open source toolkit developers use to build this firmware is called TianoCore EDK II - it serves as a common foundation for creating UEFI firmware for different types of hardware.

Alex Matrosov of Anthropic and Dan Holmes of Google recently found that EDK II contained a critical buffer overflow vulnerability. The National Vulnerability Database (NVD) describes it as a bug in BIOS “where a user may cause “Out-of-bounds Write”, Classic Buffer Overflow, and “Incorrect Calculation of Buffer Size” by remote access.” “Successful exploitation of this flaw can result in remote arbitrary code execution, " it added.

Just like other UEFI vulnerability exploits, this one would be difficult to remediate in the wild. Deploying malicious code before security solutions, or even the operating system for that matter, means that whatever anti-malware or endpoint protection solutions are installed won’t be able to spot, or remove it. Reinstalling the operating system won’t help, and neither would replacing the hard drive.

The bug is now tracked as CVE-2026-97631, and was given a severity score of 9.5/10 (critical). Luckily enough, it doesn’t seem to have been exploited in the wild. However, that might change very soon, given that the security community botched the disclosure efforts.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Multiple companies and hardware manufacturers develop their own UEFI, and many rely on shared codebases such as EDK II. When a vulnerability is discovered in the code, fixing it upstream (in the codebase) is only half the work - each affected firmware vendor must patch their own product and then distribute the new firmware to their customers. This process can take time, leaving a window between the availability of the fix and its deployment across affected systems.

## Discretion is advised

That is why discretion is paramount, and some participants seem to have dropped the ball, with *Ars Technica* claiming the two researchers who found the bug arranged for it to stay private until a coordinated disclosure that was planned for January 2027.

However, AMI - one of the manufacturers building motherboards - apparently published a pull request last month that not only detailed the vulnerability but also included a fix for the code.

Since the cat was out of the bag, TianoCore Project members then published a public advisory about the flaws, as well.

“With publicly available patch code, it will be trivial for advanced hackers to learn how the vulnerability is triggered and to build working exploits,” Ars Technica’s Dan Goodin writes. “Further compounding the urgency, patching UEFI code vulnerabilities in millions of end devices sold and used by thousands of hardware makers and cloud providers is cumbersome and time-consuming.”

Exploiting this flaw is not that easy, though. Threat actors need to have some level of access to the target device beforehand, meaning that the bug will be mostly used by state-sponsored threat actors, and large, highly organized hacking collectives.

It really is turning out to be Black October - especially since the PHP2Shell flaws were inadvertently disclosed to the public in similar fashion.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

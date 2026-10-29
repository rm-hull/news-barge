---
title: Fake PS5 emulators are being used to steal gamers' passwords — two well-known
  GitHub repos, including popular AnyPS5, get hit, infecting gamers' computers with
  password-scraping malware
source_url: https://www.tomshardware.com/tech-industry/cyber-security/fake-ps5-emulators-are-being-used-to-infect-gamers-computers-with-password-scraping-malware-two-well-known-github-repos-including-anyps5-hit
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-29T18:33:42Z'
published: '2026-10-29T00:00:00Z'
description: Emulators downloaded via GitHub may be stealing your passwords, with
  two well-known projects being exploited.
image: https://cdn.mos.cms.futurecdn.net/hvR9HQGsb9khuSd3sSJxCY-2000-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Oliver Haslam
- Tom
locations: []
organisations:
- Get Tom's Hardware
- GitHub
- Google News
- Microsoft Defender
- NordVPN
- Oliver Haslam
- PS5
- Threat Intelligence
---

![PS5](https://cdn.mos.cms.futurecdn.net/hvR9HQGsb9khuSd3sSJxCY-1920-80.jpg)

Malicious GitHub repositories masquerading as two well-known and legitimate PS5 game emulation tools have been identified as spreading malware that steals gamers' passwords. The malware uses self-signed certificates, created using fake company names and on the same day the malware was built — suggesting that the malware campaign may be automated. Just two minutes after infection, a cleanup script scrubs the affected computer of the malware's files, leaving no trace that it was ever present, according to a report shared with *Tom's Hardware* by NordVPN's Threat Intelligence research team.

The campaign trades on the back of the popularity of two projects that have become popular within the PS5 emulation community. AnyPS5 is a portability layer that allows PS5 games to run as native applications on both Windows and Linux. Kyttyps5 is an emulator for running PS5 games on PCs, and both projects are freely available for download via their respective GitHub repositories. However, users who visit one of the malicious repositories posing as these tools are directed to download a zip file containing a Windows executable. Notably, the GitHub repositories used as part of the malware campaign rapidly rotate, and it's possible that GitHub is not the only source.

The malicious executable unpacks a hidden application before launching its own multi-stage loader. It first checks whether the PC is a legitimate machine or a security researcher's sandbox by checking if less than 2GB of RAM is available, if it's a virtual machine, if it's running on a cloud-based server, or if it doesn't have a physical GPU installed. If any of those criteria are met, the loader exits silently. If the machine is deemed to be a legitimate target, the malware adds exclusion rules to Microsoft Defender to ensure that it will never be scanned and identified during an antivirus scan. Finally, the payload is decrypted and executed.

That payload, we're told, is an executable protected by a commercial packer that is believed to be an infostealer — a type of malware whose job it is to steal passwords as well as any other sensitive data that it comes across.

While this appears to be a relatively new malware attack, there are some steps that you can take to avoid falling foul of it. If you're trying to download tools like AnyPS5 and Kyttyps5, it's vital to ensure that the repository belongs to the official project team. Double-check the owner of the project, look for download links that use third-party destinations, and check metadata like the project and files' creation dates.

If you do find yourself in a position where you have accessed a suspected malicious download, disconnect your computer from the internet and run a full antivirus scan. It's also recommended that you change your passwords from a separate device where possible.

PS5 emulation is likely to become more popular than ever once GTA 6 is released on November 19, 2026. The game will be a console exclusive at launch, with a PC version expected to arrive in early 2027.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Oliver Haslam](https://cdn.mos.cms.futurecdn.net/3XaHYJa7vPsa7PG8i5U8F5-140-80.jpg)

Oliver Haslam has written about technology of all shapes and sizes for over 15 years, both online and in print. He's fascinated by how personal computing continues to change as tower PCs give way to foldable phones and beyond.

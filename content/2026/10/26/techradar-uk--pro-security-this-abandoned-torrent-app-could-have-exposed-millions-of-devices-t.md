---
title: This abandoned torrent app could have exposed millions of devices to cyberattack
source_url: https://www.techradar.com/pro/security/this-abandoned-torrent-app-could-have-exposed-millions-of-devices-to-cyberattack
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-26T20:27:39Z'
published: '2026-10-26T00:00:00Z'
description: Time4Popcorn continued to ping for updates, despite being abandoned years
  ago
image: https://cdn.mos.cms.futurecdn.net/RqKVi2WSCc5sZaXEPWu5aX-998-80.jpg
categories:
- Technology & Software
people: []
locations: []
organisations:
- Eye Security
- Netflix
- TechRadar Pro
- The Shadowserver Foundation
---

![The best free torrent client](https://cdn.mos.cms.futurecdn.net/RqKVi2WSCc5sZaXEPWu5aX-998-80.jpg)

* **Researchers say an abandoned Popcorn Time app could have enabled malware delivery to millions of devices through insecure updates**
* **The flaw let anyone controlling a defunct update domain push executable code to connected systems**
* **Security researchers safely disabled the updater, preventing potential compromise of millions of Windows and macOS devices**

Security researchers recently discovered an abandoned torrent app which could have been used to deploy malware to millions of devices around the world rather easily.

Luckily enough, it seems that no threat actors discovered this vulnerability, and the researchers were able to legally close it and keep the devices safe.

## Popcorn Time

A “torrent” is a popular way of downloading large files fast - instead of hosting the files on a single server and risking slow download speeds and downtime, hosting is split across numerous nodes in a network. Then, a small torrent file is created (.torrent) (usually around 100kb), which contains information about where the large file is hosted.

Users can then download and run it through a specialized torrent client (a computer program, basically). The client then connects to as many nodes as it can, downloading small chunks of the large file at the same time, significantly speeding up the download time.

Torrenting became hugely popular among cybercriminals and people looking to pirate copyrighted content (movies, commercial software, games). However for many people - especially those who weren’t tech savvy - the process was rather cumbersome. Downloading a client, finding a torrent file, then downloading the actual file and running it in a separate app was too much for many, which resulted in the creation of Popcorn Time.

This app looked and felt like Netflix, but instead of streaming from the company’s servers, it streamed movies directly from torrents. It became hugely popular roughly 10 years ago because it made watching pirated content remarkably easy. However, it was soon shut down, after legal pressure from the film industry. But since it was open-source, many spin-offs soon emerged, including Time4Popcorn.

## Critical flaw

Eventually, this one was abandoned, but many people keep it installed on their computers, and that’s where trouble starts.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

These clients, installed on millions of computers, came with an updater that tried to connect to the app’s abandoned domain ‘popcorntimeupd.xyz’ over unencrypted HTTP, and accepted any executable found there without verifying the digital signature. This is a vulnerability that’s now tracked as CVE-2026-30612, with a severity score of 9.8/10 (critical).

In theory, a threat actor could have obtained the domain and used it to push a malicious update to anyone who still had the app installed on their device. In practice, this was done by security researchers Eye Security. They registered the defunct domain and saw up to 3 million Windows and 350,000 macOS client connections to Time4Popcorn - residential ISPs, government and military networks, corporate devices. All of these had the app installed but apparently did not use it. Eye Security believes it was installed at one point and simply forgotten.

“If we were able to send an update, we could potentially get code execution on millions of systems,” Eye Security said, stressing that “the impact would be severe if this were to fall into the wrong hands.”

But instead of deploying malware, Eye Security wrote and pushed code that stopped and disabled the updater. It did not delete the app from people’s computers, nor did it collect host data or telemetry - it just instructed the app not to look for updates anymore.

It took the researchers from November 2025 to March 2026 to push the update to almost all computers and now, requests to the update domain are down by 98%. The remaining 2% seem to fall on Android devices, who apparently continue to be at risk.

Eye Security considered the remediation operation a success, after which it transferred the ownership of the domain (as well as 14 others it acquired) to The Shadowserver Foundation. It urged everyone to uninstall the app from their devices immediately, since it poses a major security risk.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

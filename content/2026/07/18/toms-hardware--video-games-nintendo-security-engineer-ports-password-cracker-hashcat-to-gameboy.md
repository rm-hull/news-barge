---
title: Security engineer ports password cracker hashcat to Gameboy Advance — 16.8
  MHz chip can perform a meager 727 hashes a second, 30 million times slower than
  a modern rig
source_url: https://www.tomshardware.com/video-games/nintendo/security-engineer-ports-password-cracker-hashcat-to-gameboy-advance-16-8-mhz-chip-can-perform-a-meager-727-hashes-a-second-30-million-times-slower-than-a-modern-rig
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-18T13:43:23Z'
published: '2026-07-18T00:00:00Z'
description: Hey, it's better than nothing in this day and age.
image: https://cdn.mos.cms.futurecdn.net/aiBCowjyWCCrB3e6d6uFFi-1655-80.jpg
---

![Gameboy Advance](https://cdn.mos.cms.futurecdn.net/aiBCowjyWCCrB3e6d6uFFi.jpg) 

In the modern age, password cracking is an activity that generally begets quite powerful hardware, usually high-powered GPUs. Hashing algorithms have gotten trickier, and brute-forcing them has become computationally expensive. It's only natural, then, that a new software project has come up to port the common hashcat cracking utility to the mighty... Gameboy Advance (GBA).

I "ported" @hashcat to the GBA, the ultimate password cracking rig ever (my dumbest project yet).The monstrously powerful 16.78 MHz ARM7TDMI chip does an astronomical 727 SHA256 hashes per second!! which is about thirty million times slower than a modern cracking rig. 350 days… pic.twitter.com/kWDD2B27KMJuly 17, 2026


The gba-hashcat software is the brainchild of security engineer solstICE (Ice), to whom the question of "why" is seemingly answered with "why not." Running on an original GBA, the app can power through SHA256 hashes at 727 h/s. At that rate, the author estimates that one year's worth of gba-hashcat would be equivalent to one second of a modern GPU-accelerated rig.

The GBA's main processor is an ARM7TDMI chip, a 32-bit RISC affair clocked at all of 16.8 MHz. It connected to most of its data buses and memory on a 16-bit bus, though, and the machine only carried 288 KB of RAM, plus 98 KB of VRAM. Most password-cracking software makes use of precomputed tables to help speed the repeated attempts along, but given that standard GBA cartridges are limited to 32 MB in size, all that Ice could include was the ignis-1M (one million) word list that rings in at 8 MB.

The software itself is quite small, given that Ice made good use of the Butano engine, a library that allows developers to easily write GBA games using plain C++ code. The gba-hashcat user interface is quite sparse, showing only an intro screen, progress statistics, and the current password attempt. It's not like you need much more for this application, save perhaps for a "please be patient" message.

In the GitHub commit, Ice calls gba-hashcat "[their] dumbest app of all time." That's quite the statement, but X commenters were quick to request networking support so they could make a cluster of password-cracking Gameboys, an idea that may have merit considering the price of graphics cards these days. At any rate, joke all you want, but for the one really important password retrieval I was once tasked with — recovering access to an Excel payroll sheet — even the original Gameboy would have sufficed. The password was "123".

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

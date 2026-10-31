---
title: Veteran Microsoft engineer makes his own RAM from scratch using AI — custom
  FPGA board dodges extreme 1970s PDP-11 memory prices
source_url: https://www.tomshardware.com/pc-components/ram/veteran-microsoft-engineer-makes-his-own-ram-from-scratch-using-ai-attempts-to-build-4mb-of-1970s-pdp-11-ram-from-scratch
source_site: Tom's Hardware
source_slug: toms-hardware
description: The times are hard for us all.
image: https://cdn.mos.cms.futurecdn.net/ZcWNV2jNQTywTDrpaAsqbL-2048-80.png
published: '2026-10-31T00:00:00Z'
scraped_at: '2026-10-31T12:19:08Z'
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Dave Plummer
- Tom
locations: []
organisations:
- CPU
- EasyEDA
- FPGA
- Get Tom's Hardware
- Google News
- M8190
- Microsoft
- PC
- PDP
- Q-Bus
- RAM
- Raspberry Pi
- TMOG
- Task Manager
- Tom's Hardware
- Windows Pinball
---

![PDP-11 memory](https://cdn.mos.cms.futurecdn.net/ZcWNV2jNQTywTDrpaAsqbL-1920-80.png)

Dave Plummer, former Microsoft engineer and wizard of Task Manager, Windows Pinball, and now TMOG, has an interesting project in his hands once again. After seeing exactly how many zeros were in the price tag for a megabyte of memory for his vintage PDP-11, he decided to take matters into his own hands and conjure up a new RAM board.

The PDP-11 is from 1970, and later models could fit in as much as four *megabytes* of memory. Plummer enlisted the help of ChatGPT and the EasyEDA online circuit simulator, though he notes that he hadn't done complicated projects like this before. As several PDP-11 models used Q-Bus boards for main system components, he designed this RAM as a standalone card, then tested it on a backplane alongside another board containing the system's M8190 CPU.

Atop it, he placed a Lattice MachXO2 FPGA serving as a memory controller (model 2000HC, if you're wondering), connected to four ISSI 1 MB memory chips. After adding a U2S I/O chip, a bank of DIP switches, comm ports, and sprinkling a handful of capacitors, he had a complete circuit. The M8190 board design has a 22-bit bus and reserves the top 256 KB for I/O and ROM.

However, it wasn't a first-time-lucky project. Plummer encountered a few abortive starts, as he'd never flash-programmed an FPGA chip before. He fixed that after a few attempts, but then he fell into what appears to be a classic PDP-11 trap.

The machine's memory bus design means it can only access entire words (two bytes) at once, and treats the lowest bit in a memory address as a "lane" selector that picks between the low or high byte in the word.

When reading, the CPU will pick out the right byte itself, but Plummer's "memory controller" still needs to return two. Similarly, on writes, the bit selector must be read and then the proper byte selected so that only that will be updated, as the bus lines will still carry an entire word that could otherwise write invalid data.

Plummer seemingly wasn't aware of this before, and one commenter joked that he'd "built 4MB of memory that turned out to be 2MB", to which he replied that the memory "only returns every second word," matching the aforementioned design pattern. Although there are no further updates, since more commenters pointed this out, we assume that he implemented an easy fix in his FPGA code.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

One person suggested that he sidestep the entire problem and implement his memory in software via a Raspberry Pi instead, wired directly to the PDP bus. Plummer replied that he'd basically done that already last week with a modern QBone DEC interface board, which in turn contains a Beaglebone Black atop it (similar to a Raspberry Pi).



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

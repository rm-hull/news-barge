---
title: Dev ports Linux to Atari's notorious Jaguar console from 1993 — the first 64-bit
  console features 2MB of RAM, 13.3 MHz CPU, and Tom and Jerry co-processors; the
  Jag was notoriously difficult to program and flopped
source_url: https://www.tomshardware.com/software/linux/dev-ports-linux-to-ataris-notorious-jaguar-console-from-1993-the-first-64-bit-console-features-2mb-of-ram-13-3-mhz-cpu-and-tom-and-jerry-co-processors-the-jag-was-notoriously-difficult-to-program-and-flopped
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-07T15:10:11Z'
published: '2026-07-07T00:00:00Z'
description: The ill-fated Jag featured a Motorola 68000 CPU, augmented by Tom & Jerry
  co-processors, with 2MB RAM, and up to 6MB ROM.
image: https://cdn.mos.cms.futurecdn.net/zeu6pJbvfG7KKf3TpxXUQ8-1920-80.jpg
---

![Atari Jaguar](https://cdn.mos.cms.futurecdn.net/zeu6pJbvfG7KKf3TpxXUQ8.jpg) 

A Spanish systems software developer has ported Linux to the Atari Jaguar console. To succeed at the task, cakehonolulu had to overcome severe memory limits, the lack of a memory management unit (MMU), and face off against a handful of unusual hardware quirks. A blog post from the dev tells us about the work to port Linux to this ill-fated 1993-launched flop, and happily ends in evidence that a working Linux kernel and BusyBox command line shell can be booted on the old Jag. Now Linux runs on both your cherished real hardware via cartridge, or in a Jaguar emulator.

 ![Atari Jaguar](https://cdn.mos.cms.futurecdn.net/Sqm8c5GWMTvtqP6HYHrhT8.jpg) 


Anyone wishing to port Linux to the Atari Jaguar would face numerous constraints due to the hardware. One of the first hurdles successfully leaped by cakehonolulu was the CPU used. Atari’s system designers architected the Jag using a Motorola 68000 CPU, which was already pretty old at the time, but a moderately fast 13.3 MHz version was selected. Though the gaming prowess of the console was lifted by custom co-processors dubbed Tom & Jerry, some games didn’t make much use of this graphics and DSP acceleration, as it was notoriously difficult to tap into.

For this Linux port, the general CPU capabilities of the M68000 would also be targeted to run the OS. With that in mind, and knowing that the CPU lacked an MMU, cakehonolulu was lucky to find that classic Motorola 68k processors are still supported by Linux, and also the uClinux project, which allows Linux to run on MMU‑less systems like the Jaguar.

While these prior works were helpful, it wasn’t long until the linux_jag developer needed to battle with other Atari Jaguar constraints. The console comes with just 2MB of RAM and up to 6MB of ROM, which is incredibly miserly compared to even the cheapest microcontrollers and SBCs nowadays. Much RAM and storage optimization later, cakehonolulu tripped over a few issues getting Linux to boot on the Jaguar, and ended up implementing a console driver for Tom so the OS would work on real hardware.

 ![Atari Jaguar Linux](https://cdn.mos.cms.futurecdn.net/HR8dcwDG3r3MGQGcGwwGQ8.jpg) 


## A brief Atari Jaguar history

Atari’s Jaguar was released with great pride by the iconic video game company in 1993. It was controversially claimed to be the world’s first 64-bit console, but it still never managed to push aside incumbent previous-gen machines from Sega (Genesis / Mega Drive) or Nintendo (Super NES).

The mass market had enough patience to largely ignore the first wave of ‘early fifth-generation consoles’ like this, the 3DO, and the Amiga CD32. They were rewarded handsomely with the launch of the true accelerated 3D gaming next-gen wave, led by the Sega Saturn (which also used an M68000 CPU, alongside co-processors), Sony’s first PlayStation, and the Nintendo 64.

History can be a little unfair to the Atari, though, as it did have some eye-popping for the time original games and ports. I owned the original console with *Alien vs. Predator***(1994), and it was quite a stunning, tense, and scary game. Others thought the Jag’s* Tempest 2000* was a killer app. In addition, there were strong* Doom***and * Wolfenstein 3D*FPS ports from the PC.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

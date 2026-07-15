---
title: Developer successfully ports Linux to 1994 Sega 32X — Genesis and MegaDrive
  expansion runs open-source OS on paltry 23MHz processors and 256KB of RAM
source_url: https://www.tomshardware.com/software/linux/developer-successfully-ports-linux-to-1994-sega-32x-genesis-and-megadrive-expansion-runs-open-source-os-on-paltry-23mhz-processors-and-256kb-of-ram
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-15T10:12:17Z'
published: '2026-07-15T00:00:00Z'
description: In today’s employment market, the dev reckons this port and their earlier
  Linux for Atari Jaguar effort will help improve their job hunting prospects.
image: https://cdn.mos.cms.futurecdn.net/NNRFxXJVxqtHxtSeA5GFu6-1920-80.jpg
---

![Linux is now available for the Sega 32X](https://cdn.mos.cms.futurecdn.net/NNRFxXJVxqtHxtSeA5GFu6.jpg) 

The adventurous developer who recently released Linux for the Atari Jaguar (1993) has brewed up a version of the open-source OS for the Sega 32X (1994). If you can’t remember the 32X, it was Sega’s mid-gen answer to early fifth-generation challengers like the Jaguar, 3DO, and Amiga CD32. Sega’s solution added some potent processing power to a mushroom-like slot in an expansion to its popular Mega Drive/Genesis. Now cakehonolulu has got it running Linux, despite facing several major hurdles.

Compared to its Genesis host, the Sega 32X was incredibly muscular. The Genesis had relied on the capable but long-in-the-tooth Motorola 68000 (7 MHz) for years, but the 32X add-on boosted that with a pair of Hitachi SuperH SH2s (SH7604) CPUs (23 MHz). It also ramped up system RAM from the base 64KB by adding 256KB of its own. Sega’s expansion offered more than just speed; the console’s color palette was ramped up from 64 to 32,000 simultaneous colors on screen, and it was powerful enough to introduce hitherto unachievable 3D graphics elements to mainstream console gaming.

As with cakehonolulu’s tale of Linux wrangling on the old Jag, the above-linked blog talks through a long list of hurdles that needed to be leapt to get the Linux kernel booted and running BusyBox. This time around, particularly steely roadblocks included: the even more constrained RAM situation, the lack of hardware synchronization primitives, the desire to get SMP working across the pair of SH2 CPUs, no direct UART access from the 32X, and scheduler bugs, among other things.

On the positive side, smoothing the development process along were access to Chilly Willy’s 32X devkit, the linuxmd project, the Krikzz FPGA-based flash cart with ROM – RAM mapping tools, and existing SH2 documentation and sample projects. Please check through the linked blog for far more technical details from cakehonolulu.

 ![Linux now available for the Sega 32X](https://cdn.mos.cms.futurecdn.net/Rqx2UUYEWCX5Sw8yagtgt6.jpg) 


As you can see, cakehonolulu was successful again. So, what’s the next stop for this adventurous dev – the Sega Saturn? Whatever the project may be, it was interesting to read that works like this are basically forming a portfolio for the Spanish dev, which they hope will help them with job hunting.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

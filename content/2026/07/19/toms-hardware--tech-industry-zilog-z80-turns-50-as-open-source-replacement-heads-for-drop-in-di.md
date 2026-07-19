---
title: Zilog Z80 turns 50 as an open-source replacement heads to drop-in DIP40 silicon
  — iconic 8-bit CPU launched in July 1976 and was discontinued in 2024
source_url: https://www.tomshardware.com/tech-industry/zilog-z80-turns-50-as-open-source-replacement-heads-for-drop-in-dip40-silicon
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-19T17:11:23Z'
published: '2026-07-19T00:00:00Z'
description: The Z80 powered many retro favorites like the ZX Spectrum, TRS-80, MSX,
  Game Boy, Master System, Pac-Man arcade cabinet, and many more
image: https://cdn.mos.cms.futurecdn.net/e73bN7kT5wtLF7GJZMRYLP-1920-80.jpg
---

![The Z80 CPU is nearing its End of Life, but one developer hopes to resurrect it with a clone.](https://cdn.mos.cms.futurecdn.net/e73bN7kT5wtLF7GJZMRYLP.jpg) 

The Zilog Z80 has just turned 50 years old. This iconic 8-bit processor first went on sale in July 1976 and stayed in production for 48 years until Zilog, now a Littelfuse subsidiary, stopped accepting orders in June 2024. However, there’s an open-source replacement closer than ever to shipping in the chip’s original 40-pin DIP package thanks to community-funded fabrication.

The original Z80 packed 8,500 transistors on a 4μm process and typically ran at 2.5 MHz, with later CMOS variants reaching 20 MHz. Binary compatibility with the Intel 8080 let it absorb the existing CP/M software base, with an on-die DRAM refresh counter that cut the number of support chips a system needed. Development of working prototypes cost roughly $400,000 against $500,000 in funding from Exxon, per the Computer History Museum.

The chip powered the ZX Spectrum, TRS-80, MSX machines, Nintendo's Game Boy, Sega's Master System, the Pac-Man arcade cabinet, and Texas Instruments' graphing calculators, then shipped in industrial controllers for decades after home computing moved on to more powerful successors. Zilog's end-of-life notice, dated April 15, 2024, told customers its wafer foundry was discontinuing support for the Z84C00 family, and last-time-buy orders closed that June.

However, Renaldas Zioma's FOSS Z80 project, launched shortly after the end-of-life notice, now has working silicon. The first version, fabbed on SkyWater's 130nm node through Tiny Tapeout 7 on a die of just 0.064mm2, has been confirmed as functional via the project’s GitHub repository. A QFN64 version with all 40 pins exposed followed on the Efabless CI2406 shuttle, two further runs then went through IHP's 130nm process, and the current run targets the classic DIP40 form factor using chip-on-board assembly on GlobalFoundries' 180nm GF180MCU node via Wafer.Space. The end goal here is to fab a drop-in replacement for machines like the ZX Spectrum and RC2014 kits.

The design is built around Guy Hutchison's TV80 Verilog core, and the project's Tiny Tapeout page says the 130nm CMOS implementation should support clocks up to 50 MHz, against 4 MHz for the original NMOS part.

Zilog is trimming the Z80's official successor line as well. A product change notification from last October put the eZ80L92, along with several Z8F-series microcontrollers, on end-of-life, citing "little to no demand." Last-time-buy orders closed on January 20 this year, with shipments scheduled through April 20, on non-cancelable, non-returnable terms. The eZ80L92 is the only eZ80 part named in the notice; the pipelined eZ80 architecture, introduced in 2001 and still inside TI's current TI-84 Plus CE calculators, otherwise remains in Zilog's catalog.

Hobbyists keep finding work for the original chip regardless. For example, earlier this year, a developer ran a tiny conversational AI on a Z80 with 64KB of RAM.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.

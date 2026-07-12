---
title: Sega Dreamcast driver fixes appear in Linux 7.2-rc3 — fabled console remains
  in favor while iconic computing architectures like i486 fall by the wayside
source_url: https://www.tomshardware.com/software/linux/sega-dreamcast-driver-fixes-appear-in-linux-7-2-rc3-fabled-console-remains-in-favor-while-iconic-computing-architectures-like-i486-fall-by-the-wayside
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-12T17:13:08Z'
published: '2026-07-12T00:00:00Z'
description: Dreamcast driver crashes get patched with keyboard, mouse and joystick
  input now more reliable.
image: https://cdn.mos.cms.futurecdn.net/mQuCtTLZ9td5xEUSFCTd9M-2034-80.png
---

![Sega Dreamcast](https://cdn.mos.cms.futurecdn.net/mQuCtTLZ9td5xEUSFCTd9M.png) 

A set of updates for Sega Dreamcast hardware has been merged into the Linux 7.2-rc3 kernel this weekend. Dmitry Torokhov submitted updates addressing the legendary console’s input subsystem and Linus Torvalds merged them on Saturday. The updates even surprised Linux-focused site Phoronix, That’s probably due to context: the Dreamcast continues to enjoy support while admittedly older but real computing hardware like the i486, PowerPC 40x chips, DEC Alpha, and Itanium / IA‑64, have all been sidelined in recent times.

In brief, the updates should mean new versions of Linux will come with more stable mouse, keyboard, and joystick drivers for Dreamcast stalwarts. If you are one of the Dreamcast faithful, still satisfying your computing (and gaming) needs on the final original consumer gaming hardware from Sega, this is good news.

Reading the pull request we can see some details about the new drivers for the Dreamcast’s Maple‑bus peripherals (mouse, keyboard, controller). Specifically, there’s a “fix for a crash in Sega Dreamcast (Maple) mouse driver when opening the device, caused by missing driver data,” as well as “Fixes for Maple drivers (keyboard, mouse, joystick) to properly order setting driver data and device registration to avoid races.” In this context*races* refers to things happening in the wrong order to result in crashes: it’s a timing bug that’s now been quashed.

Dreamcast hangers-on will now be able to craft specialized Linux builds on CD-R for their machines. The maplemouse driver has had the now-fixed crash-inducing bug since 2017.

Phoronix also comments that Linux kernel fixes for the GD-ROM driver used by the Dreamcast and a proposal for the VMUFAT file-system driver were also seen this year.

The Sega Dreamcast launched at the end of 1998 (in Japan, and the following year in the U.S.). So, in some ways it isn’t that surprising that it is still getting Linux kernel updates when the Intel i486 (1989) has been retired from mainline support. But one might have expected stronger demand for supported Linux distributions among i486 desktop and laptop users.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

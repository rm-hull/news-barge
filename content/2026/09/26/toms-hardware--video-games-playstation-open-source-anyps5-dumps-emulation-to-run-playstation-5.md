---
title: Open-source AnyPS5 dumps emulation to run PlayStation 5 console games natively
  on PC — AMD Zen 2 architecture enables Proton-like binary translation for Windows
  and Linux
source_url: https://www.tomshardware.com/video-games/playstation/open-source-anyps5-dumps-emulation-to-run-playstation-5-console-games-natively-on-pc-amd-zen-2-architecture-enables-proton-like-binary-translation-for-windows-and-linux
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-26T15:49:32Z'
published: '2026-09-26T00:00:00Z'
description: Going beyond emulation.
image: https://cdn.mos.cms.futurecdn.net/S86fJafmzvVuMLhTj6vipT-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Kunal Khullar
- Tom
locations:
- Vulkan
organisations:
- AMD
- AnyPS5
- GitHub
- Google News
- KytyPS5
- PS5
- Proton
- Sony
- Tom’s Hardware
---

![Sony PlayStation 5](https://cdn.mos.cms.futurecdn.net/S86fJafmzvVuMLhTj6vipT.jpg)

PlayStation 5 emulation has witnessed massive growth ever since Sony confirmed its plans to end PC ports for its first-party, narrative-driven single-player games. The latest name joining the list is the open source project AnyPS5, which is claimed to run PS5 games natively on PC *without* requiring any emulation. The official GitHub page describes it as a tool for automatically porting executables to Linux and Windows.

Since the PS5 is powered by AMD’s Zen 2 hardware, it uses the x86-64 architecture, thus allowing AnyPS5 to work as a compatibility translation layer somewhat similar to Proton or Wine. It takes the original PS5 executable files and converts them into Windows and Linux formats, while the shaders are recompiled into SPIR-V for Vulkan. By avoiding emulation altogether, AnyPS5 can potentially eliminate some of the computational overhead, resulting in a smoother experience.

That said, development is still in the early stages, with test builds reportedly managing to boot select games as far as the main menu, with some even reaching gameplay with audio. However, the tool still requires a lot of work, particularly when it comes to system libraries and proprietary APIs unique to the PlayStation 5’s operating system. While the project is currently active on GitHub, a working public build is yet to be released.

PS5 emulation is still far from being practical, but if you are interested or have been following the topic, make sure to check out KytyPS5, one of the most prominent and popular PlayStation 5 emulators in active development. It recently managed to run the PS5 version of *Grand Theft Auto V* as high as 40 to 60 FPS using high-end PC hardware. Unfortunately, this one is also in an early experimental phase and is not stable enough to maintain playable frame rates.

There is also SharpEmu, which focuses on accuracy and the underlying infrastructure needed to improve compatibility with PS5 games. The project has managed to successfully run *Astro’s Playroom* on a Steam Deck and was shown booting on the handheld at around 0.5 to 1 FPS. The game remains unplayable at those frame rates and does not progress beyond the introductory sequence, but getting PS5 emulation to run on the Steam Deck represents a major step forward for the project.

*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*



Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Kunal Khullar](https://cdn.mos.cms.futurecdn.net/NDK3ae3zDxAx2BJnMXxBJV.jpg)

Kunal Khullar is a contributing writer at Tom’s Hardware. He is a long time technology journalist and reviewer specializing in PC components and peripherals, and welcomes any and every question around building a PC.

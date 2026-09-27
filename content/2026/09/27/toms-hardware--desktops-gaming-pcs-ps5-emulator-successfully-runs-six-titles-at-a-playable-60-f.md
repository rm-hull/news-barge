---
title: PS5 emulator successfully runs six titles at a playable 60 FPS — PS5 emulation
  continues to gather momentum as developers improve shader translation and Vulkan
  support
source_url: https://www.tomshardware.com/desktops/gaming-pcs/ps5-emulator-successfully-runs-six-titles-at-a-playable-60-fps-ps5-emulation-continues-to-gather-momentum-as-developers-improve-shader-translation-and-vulkan-support
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-27T17:00:06Z'
published: '2026-09-27T00:00:00Z'
description: 12 of 55 tested titles tested could be played, but only six achieved
  a playable 60 FPS.
image: https://cdn.mos.cms.futurecdn.net/6WLzZkYnGEZSXr5wsUrafQ-1280-80.png
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Etiido Uko
- SharpEmu
- Tom
locations: []
organisations:
- AGC
- Caveman Ninja
- Etiido Uko
- GTA V
- Google News
- KytyPS5
- New Joe & Mac
- PC
- SharpEmu PS5
- Sony
- Tetris Forever
- Tom's Hardware
- Void Terrarium
- Vulkan
---

![Sony](https://cdn.mos.cms.futurecdn.net/6WLzZkYnGEZSXr5wsUrafQ.png)

Developers of SharpEmu — an experimental, open-source PS5 emulator — have successfully run PS5 games at a playable 60 FPS on the emulator. According to an X post on September 25, the developers reached this milestone for six of 55 titles tested, with 12 — including the six playable — reaching gameplay. According to the developer, the six games are yet to be tested from start to finish; the “playable” designation means the games currently run without issues, although minor graphical or audio issues may persist in some.

The six 60 FPS titles are *Dreaming Sarah, Void Terrarium, New Joe & Mac: Caveman Ninja, Tetris Forever, Hoa,* and*Tomb Raider IV-VI Remastered*. The breakthrough was achieved with SharpEmu v0.0.4-release.2, the emulator’s latest public build released on September 25. According to developers, the build includes upgrades such as improved SPIR-V shader translation and updated Vulkan API support.

Developed in C#, the SharpEmu PS5 emulator supports Windows, Linux, and macOS and uses Vulkan and MoltenVK for graphics API calls. PlayStation 5 relies on an AMD Zen 2 x86-64 CPU architecture; therefore, SharpEmu can execute the console's CPU instructions natively on a standard PC rather than translating them from an unfamiliar instruction set. The emulator focuses on loading a game's eboot.bin executable and required system modules, partially handling kernel functions, and processing the game's shader, resource, and AGC graphics submissions.

For now, SharpEmu is still far from handling demanding 3D titles, with only 12 of 55 tested titles reaching a game ready state. Of those 12, only six performed cleanly enough to be designated as “playable” at a full 60 FPS. The developers stress that SharpEmu is still in its early stages, noting that “SharpEmu is an experimental emulator intended for research and educational purposes. This project does not contain any copyrighted system firmware, game data, or proprietary PlayStation assets.” Meanwhile, another emulator, KytyPS5, recently ran the PS5 version of GTA V at roughly 40 to 60 FPS on a high-end Ryzen 9 9950X3D and Radeon RX 7900 XT system, crashing after the game's opening mission.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.

* AI may accelerate the emulator improvement pace. Consoles are fast becoming locked-down PCs anyway. If you want the games to be around and playable for the long haul, getting them emulated is a good way to do that.Reply

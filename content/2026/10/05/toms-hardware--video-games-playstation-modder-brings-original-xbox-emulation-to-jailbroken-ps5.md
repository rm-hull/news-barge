---
title: Modder brings original Xbox emulation to jailbroken PS5 — XPSemu plays Halo
  2 and Forza as PS5 emulators outnumber its 15 exclusives
source_url: https://www.tomshardware.com/video-games/playstation/modder-brings-original-xbox-emulation-to-jailbroken-ps5-xpsemu-plays-halo-2-and-forza-as-ps5-emulators-outnumber-its-15-exclusives
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-05T14:38:30Z'
published: '2026-10-05T00:00:00Z'
description: Developer claims Halo 2 runs at 60fps.
image: https://cdn.mos.cms.futurecdn.net/p6RKS3uArE9EvG6rNBgPYb-970-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Jhet Borja
- Tom
- ZiZc3
locations: []
organisations:
- AMD GPU
- FSR
- Forza Motorsport
- Get Tom's Hardware
- Google News
- Halo
- ISO
- Nintendo Switch
- PS5
- QEMU
- RADV Vulkan
- Reddit
- RetroArch
- TCG JIT
- Wii U
- XPSemu
- Xemu
- Yzenxam
- ZiZc3
---

![One Year of Xbox Series X and PS5](https://cdn.mos.cms.futurecdn.net/p6RKS3uArE9EvG6rNBgPYb-970-80.jpg)

Popular Xbox emulator Xemu has just been ported to jailbroken Sony PlayStation 5 consoles. Reddit user u/Yzenxam posted a video of their PS5 running the emulator with three games installed: *Forza Motorsport, Halo 2,* and*Crash Bandicoot*. The port, playfully named XPSemu, is on their GitHub page: ZiZc3.

The modder has stated that XPSemu is Xemu and is nothing different; all they did was allow it to be opened on the PS5 as an application. Xemu uses QEMU’s TCG JIT to translate the Xbox CPU to the PS5 CPU in realtime, allowing for fast performance compared to interpretation-based translation.

Xemu has its own translation for the Xbox’ NV2A GPU and uses a Vulkan renderer to work with modern GPUs; thanks to the modder behind PS5\_Vulkan, Xemu can talk to the PS5’s AMD GPU through the open-source RADV Vulkan driver — allowing the porter to run Xemu as a native PS5 application.

ZiZc3 also added their own touches as explained in their GitHub repository:  
"On top of the port, XPSemu adds its own controller-friendly dashboard, per-game settings, cover art, play time, game patches, a performance overlay, a per-game log and a set of CPU optimizations made for the PS5's Zen 2 processor."

While QEMU's TCG JIT is relatively fast, it still leaves plenty to be desired. ZiZc3 explains that the emulated Xbox CPU is the bottleneck, loaded at 85-97% while the PS5 GPU remains mostly idle. As a consequence, the resolution multiplier up to 3-4x barely affects performance, and upscaling with FSR does not add performance.

The developer further explains that the PS5's Zen 2 cores are slower per core than a fast PC, and CPU-heavy games suffer from this. In terms of performance, ZiZc3 has provided a table of their experience and performance of the games on XPSemu:

|  |  |  |
| --- | --- | --- |
| XPSemu performance as stated by developer |  |  |
| Halo 2 | ✅ Good | 30 FPS stock. With the Halo 2 60 FPS patch: 51-60 FPS in the opening, 36-50 in gameplay.. |
| Forza Motorsport | ⚠️ In-game | 30 FPS (its cap) in menus and intro, 15-21 FPS while racing. |
| Fable: The Lost Chapters | ⚠️ In-game | 22-30 FPS in many areas (30 is its cap), 10-20 FPS in heavy areas. |
| Crash Bandicoot: The Wrath of Cortex | ✅ Great | Runs smoothly. |

As of writing, there are fewer than 15 fully PS5-exclusive games, while the number of emulators the PS5 can run is increasing by the week. On X, users BrinoTk and Mihawk9\_9 (the same person behind PS5\_Vulkan) announced their Xbox 360 and PS5 Proton projects on the same day, with the Xbox 360 emulator already available for testing.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

> The emulator is now available for testing. Please keep in mind that I cannot guarantee that every game will work properly right away. Some games may not run very well, some may not run at all, and others may have graphical glitches or other issues. This is still a testing phase, and I’ll continue adjusting, fixing, and improving things over time. New features will also be added as development progresses. I’ll also be opening a Discord server so everyone can talk, share feedback, and report any bugs or issues they find directly to me. For now, I have only tested games in folder format, but I’ll also be testing ISO files soon. Everything will continue to improve over time, so feedback from testing will be very helpful. [https://t.co/GeSLyKQSwd](https://t.co/GeSLyKQSwd) [https://t.co/5a1vYcXbBdOctober](https://t.co/5a1vYcXbBdOctober) 3, 2026

The PS5 already has emulators for PS1-3, with PS4 emulation technically built in. Non-PlayStation emulators besides the XPSemu include the Nintendo Switch, Wii U, 3DS, and of course the myriad of emulators available on RetroArch as well. On the other side of the coin, the PS5 itself has also been emulated on PC and the Xbox Series X — at this point, the lines are blurring faster than owners know what to do with their jailbroken PS5.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jhet Borja](https://cdn.mos.cms.futurecdn.net/niBNJTDN6c99Ri7HD5zNZ8-140-80.png)

Jhet Borja is a serial hobbyist who was taking apart toys from childhood and sketching inventions. He now loves doing DIY projects ranging from designing custom 3D-printed parts, building PCs and keyboards, all the way to woodworking. If he's not getting his hands dirty, he's probably brainstorming his next project.

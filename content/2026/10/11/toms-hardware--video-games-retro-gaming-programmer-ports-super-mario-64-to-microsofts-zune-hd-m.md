---
title: Programmer ports Super Mario 64 to Microsoft’s Zune HD media player — the 2009
  iPod rival runs the game natively on its Nvidia Tegra chip, with touchscreen controls
  and saves
source_url: https://www.tomshardware.com/video-games/retro-gaming/programmer-ports-super-mario-64-to-microsofts-zune-hd-media-player-the-2009-ipod-rival-runs-the-game-natively-on-its-nvidia-tegra-chip-with-touchscreen-controls-and-saves
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-11T12:46:21Z'
published: '2026-10-11T00:00:00Z'
description: It plays mostly at full speed if you bring the ROM.
image: https://cdn.mos.cms.futurecdn.net/Fc5e3hgKxF7RAEEoVG3mfL-1280-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Mario
locations: []
organisations:
- 3DS
- ARM
- Apple
- DSi
- Docker
- FPS
- GPU
- Get Tom's Hardware
- Google News
- Hackaday
- Microsoft
- Nintendo
- Nvidia
- OpenZDK
- PC
- PS Vita
- PS2
- ROM
- Shane Downing
- Tegra
- Tom’s Hardware
- Video Games Chronicle
- Wii U
- XNA
- Zune HD
- iPod
---

![Hands holding a Zune HD sideways with Super Mario 64 running on its screen, Mario inside the castle and touch buttons overlaid on the right](https://cdn.mos.cms.futurecdn.net/Fc5e3hgKxF7RAEEoVG3mfL-1280-80.jpg)

The Nintendo 64 game *Super Mario 64* has come to the Microsoft Zune HD,*Hackaday* reports, through a project that runs natively on the device’s hardware through the unofficial OpenZDK kit, per the repo’s README. A touchscreen controller overlay is drawn over the game’s video, and the game “plays (mostly) at full speed with sound, touch controls and saves,” from the rsheldiii repo, although no ROM is included and one dumped from your own cartridge is required. The Zune HD, a 2009-era media player that rivaled Apple’s iPod, has Nvidia Tegra hardware inside, and the project is built on sm64ex, a fork of the unofficial, decompiled*Super Mario 64* PC port.

The Zune HD, part of our 2009 gift guide, was marketed as having a “3.3-inch glass screen” using OLED and touchscreen technology, from Microsoft’s media alert at the time, with Tegra providing the “multimedia muscle,” according to an Nvidia release. The unit was originally priced between $219.99 and $289.99, depending on capacity, and uses the Nvidia Tegra APX 2600 chip. The operating system is Windows CE-based, with third-party games going through Microsoft’s XNA. The Zune was short-lived, with Microsoft halting production in 2011, but an exploit led to OpenZDK coming out that allowed for homebrew.

The implementation depends on native ARM code on top of the Zune HD’s OS, using OpenZDK. The device’s firmware is not modified, but the port, according to the developer, should only be used “at your own risk,” a standard disclaimer. It leverages an OpenGL ES 2 renderer derived from Fast3D with prebuilt shader variants, using Nvidia’s cgc and shaderfix tools, because the Zune’s graphics driver can’t compile OpenGL Shading Language (GLSL) shaders. Blending is compiled into the fragment shaders as well, since the GPU lacks fixed-function blending hardware. These workarounds are what make the project interesting.

The game’s logic runs at 30 ticks a second, but some lag is present when the Zune is unable to keep up. There is also no official FPS number. The game renders at 480x272 in landscape, with the device rotated to match. The audio synthesis runs on its own thread at a higher priority than the game, so it is not impacted by a slower frame rate. The touch control overlay provides a facsimile analog stick as well as the A, B, Z, R, four C, and Start buttons, with customizability for button style and opacity.

The project itself relies on a *Super Mario 64* decompilation effort completed by fans in 2019, with a C source that rebuilds a matching ROM. The decompilation doesn’t include all of the game’s assets, and extraction requires a copy of the game. The ROM is read on the PC during the build, and the finished game can later be moved over to the device through USB. The build runs on Docker in Linux, so no Windows PC is required. The repo has no releases, and the port, which applies 14 patches to a pinned version of sm64ex, has only been tested on firmware 4.5.

The full PC port arrived in May 2020, of which sm64ex is a fork with extra features, such as mouse look and a cheats menu. Nintendo’s legal representatives responded quickly, targeting “sites hosting the compiled version of the Mario 64 PC port” and at least one gameplay video, *Video Games Chronicle* reported. However, a number of ports have found their way out for the 3DS, Wii U, PS2, PlayStation and PS Vita, Dreamcast, Nintendo DS and DSi, the web, and now the Zune HD.

The project shows what could have been on the Zune HD had Microsoft been less restrictive with development. Ports are nothing new, but the number has been increasing lately, potentially due to the wider availability of powerful AI tools; the repo’s first commit ends “Co-Authored-By: Claude Opus 5.5,” so AI was used at least in part. An example of something different is a decent *Doom* port to an $8,000 Hasselblad X2D camera, born from firmware research, showing there are multiple pathways to the same goal.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom’s Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

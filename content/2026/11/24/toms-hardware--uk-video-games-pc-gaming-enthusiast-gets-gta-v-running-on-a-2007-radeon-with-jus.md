---
title: Enthusiast gets GTA V running on a 2007 Radeon with just 64MB of VRAM — config
  edits, Windows 8, and an overclock lift it from 1 FPS to 20 FPS, but most cars stop
  rendering
source_url: https://www.tomshardware.com/uk/video-games/pc-gaming/enthusiast-gets-gta-v-running-on-a-2007-radeon-with-just-64mb-of-vram-config-edits-windows-8-and-an-overclock-lift-it-from-1-fps-to-20-fps-but-most-cars-stop-rendering
source_site: Tom's Hardware
source_slug: toms-hardware
description: Budget-Builds Official ran GTA V on a 2007 ATI Radeon HD 2350 with 64MB
  of DDR2 VRAM at 13 to 20 FPS.
image: https://cdn.mos.cms.futurecdn.net/ZXzjJjNmQJ8n7qfRxMHy8C-2398-80.jpg
published: '2026-11-24T00:00:00Z'
scraped_at: '2026-11-24T13:38:59Z'
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Shane Downing
- Tom
locations:
- Unigine Valley
organisations:
- 1FPS
- Budget-Builds Official
- GPU
- GTA V
- GTA VI
- Get Tom's Hardware
- Google News
- Grand Theft Auto V
- MSI Afterburner
- Minecraft
- OS
- Radeon
- Shane Downing
- Tom’s Hardware
- YouTube
---

![An ATI Radeon HD 2350 graphics card with a small fan bearing the ATI logo, held in two hands above a wooden desk](https://cdn.mos.cms.futurecdn.net/ZXzjJjNmQJ8n7qfRxMHy8C-1920-80.jpg)

YouTube channel Budget-Builds Official has done the unthinkable, getting Grand Theft Auto V to run on a Radeon graphics card from 2007 with just 64MB of VRAM. The game is almost downright playable, too, with config edits, a move to Windows 8, and an overclock getting its speed up from just 1 FPS into the 13 to 20 FPS range, sans most cars, that is.

![GTA V on 64MB of VRAM! - YouTube](https://img.youtube.com/vi/dr3F_rqGZ24/maxresdefault.jpg)

The channel detailed the feat, which targets a GPU with just a sixteenth of the video memory that’s usually required to play the game. GTA V Legacy lists, as its minimum, an Nvidia 9800 GT or AMD HD 4870, both cards with DirectX 10 support and 1GB of VRAM. The Enhanced version, released in 2025, needs 4GB, from a GTX 1630 or RX 6400 as specified.

![A GTA V shootout in a snowy yard rendered on a 64MB graphics card, with two robbers in cover in the foreground and rows of white dots across the scene](https://cdn.mos.cms.futurecdn.net/QEWfeAHYiHeg4ei5JqwKom-1200-80.jpg)

In fact, the chosen card, an ATI Radeon HD 2350, is potentially the worst card that can launch GTA V, at least by the tester’s claim, even though its DDR2 memory is probably one of the few types not in short supply at the moment. Notably, this approach doesn’t involve using a unified or shared system memory AMD APU workaround; this is dedicated VRAM. It’s also not the first attempt at something like this, as the channel has an earlier run with 8MB of VRAM on games like Half-Life 2 and Minecraft.

Reaching the final settings took “the best part of half a day” of tweaking, after which it was possible to complete the prologue and the first mission. In some respects, the end result “genuinely does look like a PS2 game,” which probably wouldn’t actually faze fans of the series. However, for this specific title, the modder believes that “this is as low as you can actually go with GTA V.” Going any lower would likely mean reimagining the game in some way.

The game’s first launch with the card, on Windows 10 and the Catalyst 13.1 driver, led to a start screen hang of about 10 minutes. The game was expecting the previous HD 6900-series card, and a settings deletion plus relaunch got things back into action. One of the video’s chapter titles, “We are in GAME... at 1FPS,” summarizes the experience pretty well.

The plan was to use the lowest in-menu settings, of course, and then the config file from the channel’s earlier 256MB run with various settings: no shadows, no reflections, and a resolution around 240p. This got things to 3 FPS, a significant improvement, but far from good enough. Changes to level-of-detail values to their lowest levels got things up to 10 FPS. However, it wasn’t yet time to give up.

Downgrading to Windows 8 and Catalyst 12.6, “the original display drivers for Windows 8,” as well as an older build of the game, paved the pathway forward. Importantly, the OS exposed overclocking that wasn’t available in Windows 10, so a second fan went onto the card first, and the GPU’s core was pushable from 400MHz to 520MHz with the assistance of MSI Afterburner. Pushing the memory from 400MHz to 475MHz led to a black screen, and the video doesn’t say what the memory ended up at, though the card survived.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The Windows 8 setup reached 14 FPS, and further engine-file edits, to visual settings.dat and to level-of-detail options through OpenIV, put gameplay in the 13 to 20 FPS range.

Ignore the dots on the screen during gameplay; the tester says these are from being out of memory, verified by an artifact-free Unigine Valley run.

The game ended up playable, although, aside from the dots, it had many other visual issues: gaps between vertices in the world, and side characters had far fewer textures than the main ones. Additionally, most cars didn’t render, since keeping them loaded crashed the game with out-of-memory errors. This makes police “hover” into scenes and, hilariously, pop out of invisible cars. Likewise, the train in the prologue never actually loads. First-person driving, at least, works. All of this plays within that range, although busier city streets can drop from 15 down to 11 or 12 FPS.

The creator says the full gameplay will likely go up as its own video on a second channel, in “lossless quality.” The video is timely, acting as a send-off just before GTA VI’s release on Nov. 19, although not yet on PC, with a PC version reportedly due next year.



Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

---
title: Modder injects leaked DLSS 5 4x Multipass on 1996 Quake — post-process AI upscale
  looks far worse than engine-level RTX mods
source_url: https://www.tomshardware.com/video-games/pc-gaming/modder-put-dlss-5-4x-multipass-on-1996-quake-looks-worse-than-rtx-modded-quake
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-14T11:51:56Z'
published: '2026-10-14T00:00:00Z'
description: At least it tried to emulate how a dungeon lit by torches would look.
image: https://cdn.mos.cms.futurecdn.net/W4vRfzZhTSPzsD8hRLvzdf-1894-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Jhet Borja
- Tom
- Valery Kryzhanovsky
locations: []
organisations:
- Google News
- Nvidia
- RTX
- Real DLSS
- Sultim Tsyrendashiev
---

![Quake 1996 with DLSS 5](https://cdn.mos.cms.futurecdn.net/W4vRfzZhTSPzsD8hRLvzdf-1894-80.jpg)

A Ukrainian DLSS 5 experimenter is back at it again, this time testing the original *Quake* game. It’s running as a post-process, not natively integrated into the game engine, using 4x Multipass to enhance the effect, but it doesn’t look so good.

Valery Kryzhanovsky has posted multiple videos running DLSS 5 on games it was never meant to be used for, nor were the games built with AI upscaling and image enhancements in mind. We previously covered a few of Valery’s projects, running DLSS 5 on 2D games like *Duke Nukem* and*Pac-Man*, resulting in weird and cursed images.

![Quake (Software Rendering) with Real DLSS 5 Multipass x4 — All Four Modes - YouTube](https://img.youtube.com/vi/OpefTaXpIMI/maxresdefault.jpg)

However, this time Valery uploaded a video of it on the 1996 Quake, considered to be the very first true 3D FPS in history. Valery explains in the description that the game is not running the leaked DLSS 5 build natively, but as a post-process using ReShade through RenoDX to play with the parameters and settings and inject the effect on DOSBox’s rendered frame. So it’s an emulated version of Quake with basically an AI filter with the DLSS 5 algorithm over it four times, except it’s running in real time on a game. This is similar to how others have experimented with DLSS 5 on videos, applying the effect on top, like JackSpace’s video to “fix” bad CGI in old movies with DLSS 5.

Before DLSS’ popularity, Nvidia released an RTX demo running Quake II with ray tracing in the game engine to improve the lighting. That demo looked stunning, with realistic lighting and reflections, but DLSS is not ray tracing/RTX; it’s an upscaling technology that runs well on RTX cores. And on top of that, DLSS 5 is not even integrated into Quake’s engine, explaining the terrible results. However, this is a very early build of DLSS 5, and Valery says in his blog that the leaked build is undertrained. I honestly thought it would do better, considering there are more obvious 3D elements for the upscaler to work with compared to the 2D games Valery has experimented with. It seems that it darkens everything so much, possibly because of the sparse distribution of torches and highlights.

![Quake II RTX: Official Announce Trailer - YouTube](https://img.youtube.com/vi/unGtBbhaPeU/maxresdefault.jpg)

This might fare better if DLSS 5 were integrated into the engine, like how Sultim Tsyrendashiev modded ray tracing into Quake's engine, similar to Nvidia's Quake II demo.

Earlier this week, Nvidia announced that it had improved the performance of its DLSS 5 model by 2x, while shrinking its footprint by 24%. The result should be higher FPS while using less VRAM, drastically increasing performance.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jhet Borja](https://cdn.mos.cms.futurecdn.net/niBNJTDN6c99Ri7HD5zNZ8-140-80.png)

Jhet Borja is a serial hobbyist who was taking apart toys from childhood and sketching inventions. He now loves doing DIY projects ranging from designing custom 3D-printed parts, building PCs and keyboards, all the way to woodworking. If he's not getting his hands dirty, he's probably brainstorming his next project.

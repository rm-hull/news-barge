---
title: PlayStation 3 emulator adds support for ATI Radeon HD 2000, 3000, and 4000
  series graphics cards on Linux — 20-year-old HD 2600 crumbles, can only run Portal
  at 13 fps in 273p
source_url: https://www.tomshardware.com/video-games/retro-gaming/playstation-3-emulator-adds-support-for-ati-radeon-hd-2000-3000-and-4000-series-graphics-cards-on-linux-20-year-old-hd-2600-crumbles-can-only-run-portal-at-13-fps-in-273p
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-22T14:19:28Z'
published: '2026-07-22T00:00:00Z'
description: ATI TeraScale GPUs from 2007-2009 can now be used for some RPCS3 fun.
image: https://cdn.mos.cms.futurecdn.net/hPxrCnciuXxmjC3PZZ3p95-1920-80.jpg
---

![PlayStation 3 emulator adds support for ATI Radeon HD 2000, 3000, and 4000 series graphics cards](https://cdn.mos.cms.futurecdn.net/hPxrCnciuXxmjC3PZZ3p95.jpg) 

The developers of RPCS3 have announced that their PlayStation 3 emulator’s minimum system requirements have been adjusted to include a crop of even older Radeon graphics cards. This well-regarded application already supported ATI Terascale 2 GPUs from the Radeon HD 5000 and 6000 series, but now gamers still cradling Radeon HD 2000, 3000, and 4000 series can join in the fun. Some of these GPUs date back nearly 20 years. Please note that while RPCS3 is available for a range of platforms, this extended ATI architecture support is only for Linux users.

## Fine wine on Terascale 2

Back in 2021, the RPCS3 devs lowered the emulator’s system requirements to embrace Radeon HD 5000 and HD 6000 (Terascale 2) series graphics cards. In the subsequent five years, the emulator has been tuned to improve performance on hardware from these generations. An example provided asserts that when using Persona 5 as a benchmark, performance in Kamoshida’s Castle went from 35 to 49 FPS between 2021 and today (on a PC system with an ATI Radeon HD 5850, AMD FX-8350 CPU, and 8GB of RAM).

## Inspired Terascale 1 experiments

Success spurred the devs to investigate TeraScale 1 performance and compatibility. Some OpenGL wrangling ensued due to TeraScale 1 GPUs only reporting OpenGL 3.3 and GLSL 3.30 support, but getting these old and unloved ATI cards to work with the RPCS3 OpenGL renderer was surprisingly simple. It was done by overriding the reported OpenGL levels to 4.3 and 4.40.

Initial tests made use of a system packing an ATI Radeon HD 4890 with 1GB of VRAM – the most powerful Terascale 1 GPU ever sold. According to the RPCS3 blog, this card has a more powerful GPU than the PS3, but the emulator’s complex shader code is not optimal for older architectures like this. Nevertheless, “Simpler games work perfectly fine, with playable performance,” notes the blog, “while games that have more complex graphics are GPU bottlenecked with subpar performance.” Screenshots show Metal Gear Solid HD Collection and Outrun Online Arcade with frame rates close to 60 FPS.

 ![PlayStation 3 emulator adds support for ATI Radeon HD 2000, 3000, and 4000 series graphics cards](https://cdn.mos.cms.futurecdn.net/QQeYLWLmDgcr4wvnAwS3E5.jpg) 


Moving down the stack and further back in time, GPUs like the ATI Radeon HD 3870 are “still able to render very simple games with playable performance in RPCS,” assert the devs. To achieve playability, you will want to dial in PSP-like resolutions, though. Specifically, 273p was mentioned.

What about the weakest TeraScale 1 GPUs? The ATI Radeon HD 2600 XT with a measly 256MB of VRAM even performs poorly at 273p. Screenshots from RPCS3 tests show it only managing 8 FPS in Outrun Online Arcade and 13 FPS in Portal.

With RPCS3’s progress over the last half decade, these performance numbers could also improve. In fact, the blog states that “future optimization should improve performance by quite a bit on these old GPUs.”

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

It looks like a good time to dust off your retro PC and try a few old PS3 classics on your ATI TeraScale 1 GPU-accelerated rig. Remember this extended graphics card support requires a Linux distro with the Mesa driver r600. Then you need to launch RCPS3 with the following environment variables: MESA_GL_VERSION_OVERRIDE=4.3 MESA_GLSL_VERSION_OVERRIDE=440 ./rpcs3.AppImage

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

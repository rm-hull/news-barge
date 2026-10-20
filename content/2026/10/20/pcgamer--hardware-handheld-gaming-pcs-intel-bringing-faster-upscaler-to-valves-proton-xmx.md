---
title: Intel bringing faster XeSS upscaler to Valve's Proton
source_url: https://www.pcgamer.com/hardware/handheld-gaming-pcs/intel-bringing-faster-upscaler-to-valves-proton-xmx-accelerated-xess-could-come-to-steamos-in-boost-to-future-intel-powered-handheld-gaming-pcs/
source_site: PC Gamer
source_slug: pcgamer
scraped_at: '2026-10-20T14:25:30Z'
published: '2026-10-20T00:00:00Z'
description: Intel giving SteamOS a little more love?
image: https://cdn.mos.cms.futurecdn.net/9MJHAQihCEJpovFPTVxFoR-2560-80.jpg
categories:
- Technology & Software
people:
- Damian Tomczak
locations: []
organisations:
- AMD
- Intel XeSS
- Linux XeSS
- MSI
- Microsoft
- Phoronix
- Proton
- SteamOS
- Valve
- Vulkan
- XMX
---

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/9MJHAQihCEJpovFPTVxFoR-1920-80.jpg)

Intel has opened requests to add Intel XeSS support to Valve's Proton, signalling a renewed interest in getting its mobile gaming chips up to speed on the Linux operating system.

Some of the best handheld gaming PCs right now are powered by Intel processors, namely the Intel Arc G3 Extreme. That can be found in the formidable MSI Claw 8 EX AI+. Though this is resolutely a Windows machine—Intel chips are built with Microsoft in mind, but more importantly, Valve has historically only supported AMD chips with SteamOS.

That's changing as time goes on. As spotted by Phoronix, Intel has opened pull requests for Intel XeSS support in Proton, specifically to utilise dedicated XMX cores in Intel's own GPUs for better performance.

Proton is the compatibility layer that allows games programmed for Windows to run on Linux machines, and has been crucial to the success of the Steam Deck and SteamOS as a whole. XeSS is Intel's upscaling technology, which works one of two ways, either using DP4a for wide support across various vendor's GPUs, or XMX on Intel's own GPUs. The XMX option is preferred.

"Adds a builtin libxess.dll which forwards the XeSS D3D12 calls to the Linux XeSS library (libxess.so)," says Intel engineer Damian Tomczak in the request, "so XeSS can use XMX (the fast upscaler) under Proton instead of the slower fallback path. D3D12 objects are converted to Vulkan through vkd3d-proton's interop interface."

The dream here is that, further to future support being added to Proton and SteamOS, we can happily switch our Windows-based handheld gaming PCs over to the Linux operating system without any hitches or performance drops. The good news is that this is already happening. Valve has this year "improved compatibility" with both AMD *and* Intel's recent platforms with recent SteamOS releases, and broader support for SteamOS goes beyond handhelds into plucky homemade Steam Machines, too.

![An Asus ROG Xbox Ally X handheld gaming PC.](https://cdn.mos.cms.futurecdn.net/d8uRQPMCepL5Hc6cMkvNEc-140-80.png)

The PC Gamer Circuit Breaker newsletter breaks down the latest PC gaming tech, and finds you the best deals on the best products

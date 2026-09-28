---
title: Modders bring Nvidia’s DLSS 5 Neural Rendering to AMD Radeon GPUs — latest
  build delivers 74% performance boost in just 24 hours, new launcher automates install
  process
source_url: https://www.tomshardware.com/pc-components/gpus/modders-bring-nvidias-dlss-5-neural-rendering-to-amd-radeon-gpus-latest-build-delivers-74-percent-performance-boost-in-just-24-hours-new-launcher-automates-install-process
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-28T13:51:01Z'
published: '2026-09-28T00:00:00Z'
description: No more manually copying and replacing DLL files for each game.
image: https://cdn.mos.cms.futurecdn.net/MzcBQaXhbvuzF57fSvYf3h-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Kunal Khullar
- Tom
locations: []
organisations:
- AMD
- AMDNR
- Ancient Gameplays
- DLSS 5
- DLSS-NR-on-AMD
- FSR
- GPU
- GTA
- GitHub
- Google News
- Nvidia
- RTX
- Tom’s Hardware
- YouTube
---

![A screenshot of Cyberpunk 2077 running on an AMD Radeon 9070 XT with an unofficial DLSS 5 mod](https://cdn.mos.cms.futurecdn.net/MzcBQaXhbvuzF57fSvYf3h.jpg)

Nvidia officially rolled out DLSS 5 earlier this month, bringing its new Neural Rendering technology to supported games for RTX 50-series GPU owners. While early testing has shown improvements in image quality and rendering, the technology is very resource-intensive, resulting in significant drops in frame rate. That, however, has not stopped modders from experimenting with DLSS 5 and attempting to bring the technology to AMD Radeon GPUs.

A GitHub project called DLSS-NR-on-AMD, designed to run DLSS 5 Neural Rendering on AMD's Radeon RX 9000 and RX 7000 series GPUs, is already seeing a rapid improvement in performance. It uses a ground-up, full reimplementation of the neural network runtime for AMD GPU architectures. As per the developer, the project currently works with DirectX 12 games that use FSR, with Cyberpunk 2077 and GTA V Enhanced among the tested titles.

Testing done by YouTube channel Ancient Gameplays shows Cyberpunk 2077 running at over 80 FPS on a Radeon RX 9070 XT without DLSS 5 Neural Rendering. Enabling the unofficial implementation, however, caused performance to drop around 11-12 FPS. Not only is that unplayable, but it also highlights just how much optimization was still needed to make the technology practical on AMD hardware.

![HUGE UPDATE for DLSS 5 on AMD Cards!! FPS & Quality Improvements!! - YouTube](https://img.youtube.com/vi/qyRaA4wLYXI/maxresdefault.jpg)

Development has been rather quick, as an Alpha 0.3.3 version was released with a claimed 23% performance improvement, followed shortly by Alpha 0.4.0, which reportedly added another 42% improvement over version 0.3.3. The changes essentially amount to roughly a 74% performance improvement in just 24 hours. The project has also become easier to install thanks to the AMDNR launcher that can automate much of the setup process, meaning that users no longer need to manually copy and replace DLL files for each game. The launcher also supports different runtimes and provides additional options through the OptiScaler interface.

Ancient Gameplays tested the latest Alpha 0.4.0 build in Cyberpunk 2077 at 3440 x 1440 resolution and found the Radeon GPU reaching around 50 FPS. That is a substantial improvement over the roughly 30 FPS achieved with the earlier build, although it remains well below the performance of the game without Neural Rendering enabled.

There is still a long way to go before DLSS 5 on AMD hardware can be considered a practical alternative to native implementation. The project remains in alpha, which means performance and compatibility can vary considerably depending on the game and GPU. That said, the developer has informed Ancient Gameplays that they are working on another major update, which should bring a substantial performance boost on Radeon GPUs.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Kunal Khullar](https://cdn.mos.cms.futurecdn.net/NDK3ae3zDxAx2BJnMXxBJV.jpg)

Kunal Khullar is a contributing writer at Tom’s Hardware. He is a long time technology journalist and reviewer specializing in PC components and peripherals, and welcomes any and every question around building a PC.

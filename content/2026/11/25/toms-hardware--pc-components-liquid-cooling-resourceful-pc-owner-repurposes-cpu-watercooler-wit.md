---
title: Resourceful PC owner repurposes CPU watercooler with dead pump as standalone
  LCD hardware monitor, vibecodes new software for module — NZXT Kraken’s LCD and
  controller board combined with 3D-printed stand for second chance at life
source_url: https://www.tomshardware.com/pc-components/liquid-cooling/resourceful-pc-owner-repurposes-cpu-watercooler-with-dead-pump-as-standalone-lcd-hardware-monitor-vibecodes-new-software-for-module-nzxt-krakens-lcd-and-controller-board-combined-with-3d-printed-stand-for-second-chance-at-life
source_site: Tom's Hardware
source_slug: toms-hardware
description: The Redditor salvaged the LCD and controller board, 3D-printed a stand,
  and used AI to develop a custom software to turn the screen into a standalone PC
  monitoring display.
image: https://cdn.mos.cms.futurecdn.net/PhywGimNE7gbWBVp7vRDoj-1920-80.jpg
published: '2026-11-25T00:00:00Z'
scraped_at: '2026-11-26T03:32:27Z'
categories:
- Technology & Software
- Hardware
people:
- BodeeHav
- Kunal Khullar
- Tom
locations: []
organisations:
- AI
- Aorus
- BodeeHav
- GitHub
- Google News
- LCD
- NZXT CAM
- PC
- Reddit
- STL
- Tom’s Hardware
---

![The LCD from an NZXT Kraken Elite AIO liquid cooler repurposed into a standalone display to monitor the system](https://cdn.mos.cms.futurecdn.net/PhywGimNE7gbWBVp7vRDoj-1920-80.jpg)

AIO liquid coolers are notorious for shorter lifespans due to pump failure or leaks, which usually results in having to replace the entire unit. However, one enthusiast decided to salvage theirs uniquely, at least a part of it. Sharing their DIY project on Reddit, u/BodeeHav repurposed the LCD screen from a dead NZXT Kraken AIO into a standalone desktop monitor that displays live CPU and GPU temperatures and utilization after vibecoding entirely new software.

According to the post, the pump on their NZXT Kraken AIO stopped working around a month ago. Rather than discarding a perfectly usable screen, they decided to dismantle the block and remove the LCD and its main board. They used the original black outer housing and 3D printed a stand to hold the LCD in place. To keep things tidy, they stripped the connector down to just its SATA power and USB pins. The display connects directly to the motherboard, presumably using the internal 9-pin USB header, although BodeeHav says they plan to adapt it for external USB.

Getting the display working properly required more than just pulling it out of the pump block. BodeeHav initially used NZXT’s CAM software; however, he kept running into issues whenever the PC entered sleep or standby. To overcome this hurdle, they turned to AI and vibe coded an entirely new software as a replacement that offers full control of the LCD with various customization options.

BodeeHav has graciously made his entire project available on GitHub, where you can access the DesktopKraken software and an STL file for the stand. According to the official GitHub page, the software is a standalone Windows application that communicates with compatible NZXT Kraken Elite LCDs over USB without requiring NZXT CAM.

The software currently only offers support for the 2023 Kraken Elite and 2024 Kraken Elite V2, which use circular LCDs with a 640x640 resolution. Apart from CPU and GPU temperatures and utilization, it can also display clock speeds, power consumption, memory usage, and VRAM information. Additionally, the software can be used for brightness control, screen orientation, sensor logging, and it even offers support for custom images, animated GIFs, thermal warning gauges, and automatic recovery after Windows sleep or a USB disconnect.

While it may cater to a very niche audience, the project is a great example of how a little ingenuity can give failed components a second life.



*Download the Tom's Hardware app for up-to-the-minute updates on* * iOS* * and* * Android**. Also follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Kunal Khullar](https://cdn.mos.cms.futurecdn.net/NDK3ae3zDxAx2BJnMXxBJV-140-80.jpg)

Kunal Khullar is a contributing writer at Tom’s Hardware. He is a long time technology journalist and reviewer specializing in PC components and peripherals, and welcomes any and every question around building a PC.

* Wow, nice way of up-cycling. Wish there was a way of just turning on the LEDs on my dead Aorus x370 Gaming K5 I mounted on a plaque in my work room. Got other motherboards that may still work, but that Aorus has a dead 12v rail and will not come back to life.Reply

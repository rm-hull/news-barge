---
title: The best iGPUs around now have proper hardware upscaling support in Linux
source_url: https://www.pcgamer.com/hardware/handheld-gaming-pcs/experimental-project-beats-intel-in-bringing-real-intel-xess-super-resolution-to-steamos-and-proton-games-on-linux/
source_site: PC Gamer
source_slug: pcgamer
description: Intel has promised to do it itself, but Linux devs are an impatient bunch.
image: https://cdn.mos.cms.futurecdn.net/xqNYPKPfuhqvZCqbXacdTR-2560-80.jpg
published: '2026-11-05T00:00:00Z'
scraped_at: '2026-11-05T17:24:55Z'
categories:
- Technology & Software
people: []
locations:
- GameSir
- Proton
organisations:
- DP4a
- Elgato Facecam
- Flatpak Steam
- GPU
- Intel
- PC Gamer Circuit Breaker
- Proton
- Razer BlackShark V34
- Razer Viper
- Secretlab Magnus Pro XL3
- Secretlab Titan Evo2
- Shure
- Valve
- Wireless5
- XMX
---

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/xqNYPKPfuhqvZCqbXacdTR-1920-80.jpg)

Intel has already committed to bringing its XMX-powered upscaling and frame generation tech to Linux via Valve's Proton compatibility layer, but one enterprising developer is clearly not willing to wait for the chip behemoth to get it working and has released an experimental version on Github (via Phoronix).

This new release promises "real Intel XeSS super resolution and XeSS Frame Generation inside Proton games, running on the GPU's XMX (matrix) units instead of the DP4a fallback that stock Wine/Proton gets." It was built on a OneXPlayer 3 handheld running the same Intel G3 Extreme chip that ships in the latest MSI Claw and the new Acer Predator Atlas 8, but has also been tested on a discrete Arc B580 GPU, too.

And it's already delivering a 29% performance boost in Cyberpunk just from the switch to XMX processing of upscaling, and when you throw in XeSS Frame Generation you're looking at a 145% performance boost. That is just one game, however, and the only other benchmark they note is for Forza Horizon 6 where the performance boosts are not quite so great, with a 16% bump from the XMX implementation. Though again you are looking at a healthy frame rate increase from 3x frame generation.

The installation seems surprisingly straightforward; you just unpack the release archive somewhere safe and run the install command. Then every game will run with the patched drivers without the need for any special launch options.

The one note is that you must be running the native Steam client to support the XMX switch in Proton, with the Flatpak Steam client not being currently supported.

It's great to see this being picked up and running with Intel's Arc GPUs right now. The ideal would be to have Intel get the official release out and available for anyone running SteamOS, or any other Linux distro, with their Arc-based graphics silicon, but given how straightforward this implementation seems to be, it's a great stop gap measure.

![Intel Arc B580 graphics card](https://cdn.mos.cms.futurecdn.net/xGyYPnGX2u6BMLVR6c75nV-1200-80.jpg)

And it's worth noting that while graphics card prices have become an apocalyptic nightmare, where you might have to barter a kidney or two just for the privilege of potentially buying an RTX 5060, the two Intel Battlemage cards are still *relatively* affordable. The Arc B580 is around $330 and the Arc B570 is a shade over $300 today. That makes them solid 'budget' cards, and now they're becoming great options for that little Linux gaming tower you always wanted to build, too.

The PC Gamer Circuit Breaker newsletter breaks down the latest PC gaming tech, and finds you the best deals on the best products

Now, if only those excellent G3 Extreme handhelds weren't so damned expensive…

![Secretlab Titan Evo gaming chair in Royal colouring, on a white background](https://cdn.mos.cms.futurecdn.net/7rTxS5WgHWFPDRsqLd28vh-140-80.png)

**1. Best gaming chair: Secretlab Titan Evo2. Best gaming desk: Secretlab Magnus Pro XL3. Best gaming headset: Razer BlackShark V34. Best gaming keyboard: Asus ROG Strix Scope II 96 Wireless5. Best gaming mouse: Razer Viper V4 Pro6. Best PC controller: GameSir G7 Pro7. Best steering wheel: Logitech G Pro Racing Wheel8. Best microphone: Shure MV6 USB Gaming Microphone9. Best webcam: Elgato Facecam MK.2**

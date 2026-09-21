---
title: PlayStation 3 emulation devs work around an Nvidia bug for up to 37% faster
  performance — open-source coders reach out to Nvidia to over uncovered bug
source_url: https://www.tomshardware.com/pc-components/gpu-drivers/playstation-3-emulation-devs-work-around-an-nvidia-bug-for-up-to-37-percent-faster-performance-open-source-coders-reach-out-to-nvidia-to-over-uncovered-bug
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-21T15:04:44Z'
published: '2026-09-21T00:00:00Z'
description: AMD users aren’t affected by the bug, so don’t need the workaround.
categories:
- Technology & Software
- Hardware
image: https://cdn.mos.cms.futurecdn.net/DTyif5tMyL37FaiLreQSkS-1920-80.jpg
---

![Gran Turismo 5 ran 37% faster, used far less VRAM](https://cdn.mos.cms.futurecdn.net/DTyif5tMyL37FaiLreQSkS.jpg)

The developers of the open-source PlayStation 3 emulator RPCS3 are celebrating finding a workaround for an Nvidia driver bug. The social media celebration stems from their testing showing that some PC configurations with Nvidia GPUs can enjoy up to 37% faster gaming performance. That’s more than a small wrinkle that’s been ironed out.

![Asus RTX 5080 Noctua Edition](https://cdn.mos.cms.futurecdn.net/Wh9EZgD8NG9yUioNNgPB3d.png)

> More RPCS3 performance on NVIDIA GPUs!Yahfz found a workaround for an @NVIDIA driver bug that was bottlenecking performance.In this boat test scenario:13900K + RTX 3080: +20% FPS9800X3D + RTX 5090: +25% FPSAMD GPU drivers do not have this bug, thus seeing no change. pic.twitter.com/BRad9AyesfSeptember 16, 2026

We don’t know the exact nature of the Nvidia driver bug here, but the RPCS3 devs say that it bottlenecks the performance of their PS3 emulator. The first example cited provides two PC configurations running Red Dead Redemption in a scene featuring a paddle steamer. This is a popular ‘benchmarking’ scene focused on the Blackwater docks in the game, featuring relatively consistent camera paths and water effects.

| RDR boat test | Configuration | Performance uplift |
| --- | --- | --- |
| **System 1** | 13900K + RTX 3080 | 20% FPS |
| **System 2** | 9800X3D + RTX 5090 | 25% FPS |

Those are very gratifying performance uplifts resulting from a driver bug workaround. Plenty of readers are probably more interested if the purported bug might also be bottlenecking native PC gaming performance. If it were, that would be a hugely significant find/workaround from the RPCS3 team, specifically ‘Yahfz.’ Please note that “AMD GPU drivers do not have this bug, thus seeing no change,” say the emulator developers.

## Gran Turismo 5 ran 37% faster, used far less VRAM

Follow-up social media postings underline that RDR isn’t an outlier, and “most games are impacted” by the bottleneck in the Nvidia driver. Great frame rate improvements can also be seen when using lower-end GPUs, too. The open sourcerers tested Gran Turismo 5 and saw frame rates climb by an incredible 37%, while VRAM usage dropped from 7.1 to 4.8GB. Meanwhile, playing Saints Row IV on a more mainstream GTX 1060 saw a 20% improvement in performance.

Sadly, RPCS3 dev reach-outs to Nvidia are falling on deaf ears. Another follow-up tweet states that “We tried using the developer forums in the past to no avail and gave up.” It then asks @Nvidia to establish a direct communication channel to receive driver bug reports. Nvidia Software QA boss Manuel Guzman has now replied directly, so we will see what happens in due course.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

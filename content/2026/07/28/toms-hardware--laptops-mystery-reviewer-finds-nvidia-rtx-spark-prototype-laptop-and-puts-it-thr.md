---
title: Mystery reviewer 'finds' Nvidia RTX Spark prototype laptop and puts it through
  its paces — Microsoft Surface Laptop Ultra with Nvidia N1X chip shows promise, though
  prototype warts are still quite visible
source_url: https://www.tomshardware.com/laptops/mystery-reviewer-finds-nvidia-rtx-spark-prototype-laptop-and-puts-it-through-its-paces-microsoft-surface-laptop-ultra-with-nvidia-n1x-chip-shows-promise-though-prototype-warts-are-still-quite-visible
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-28T17:43:46Z'
published: '2026-07-28T00:00:00Z'
description: The machine displays potential, but it definitely needs to be in the
  oven a good while longer.
image: https://cdn.mos.cms.futurecdn.net/pFTYguUbejMTf2HZpGAU7a-2148-80.png
---

![Surface Laptop Ultra](https://cdn.mos.cms.futurecdn.net/pFTYguUbejMTf2HZpGAU7a.png) 

Everyone loves previews of pre-release hardware that just happened to fall off the back of a truck — particularly when it's a piece of kit that's been lighting up news headlines. Fouquin, a TechPowerUp reader, "accidentally" stumbled upon a Microsoft Surface Laptop Ultra prototype that ensconces an Nvidia RTX Spark N1X SoC.

As a quick recap, the N1X is supposed to herald a generation of "AI laptops", meaning it's an alternative to the RTX Spark desktop, Mac Studio, Ryzen AI Max machines, and the Macbook Pro. This is due to the fact that they're all designs with large pools of unified memory and competent GPUs, making them suitable for non-datacenter AI work. The N1X packs 10 MediaTek-designed ARM CPU cores in a 5p5e configuration with multi-threading for 20 threads total, plus a GPU purportedly equivalent to a desktop RTX 4070 or a mobile RTX 5070. It can be wired up to 128 GB of LPDDR5X onboard in a unified pool, though the tested machine only has 24 GB.

Fouquin notes the limitations of their "review" and notes they're not an AI person, though they tried running the Phoronix AI test suite nonetheless. This yielded a mixed bag of results, as very few tests would reliably work, seemingly due to pre-production drivers. Some Vulkan tests did run properly, and the reported performance appears to be indeed in the ballpark of an RTX 4070, though there are two very important caveats.

First, this system and its drivers appear to be very buggy and unoptimized, particularly around power management. Fouquin says the system came with ancient 591.33 drivers from November 2025, eventually upgraded to 616.00 preview drivers with CUDA and Vulkan support. Apart from that, the tester found the machine's TDP spends and power plans behaving erratically, and none of the Phoronix CUDA tests produced results.

Second, head-to-head benchmarks are hard to come by, as RTX-series desktop cards have limited pools of VRAM compared to the 24 GB on the test machine. All told, there's a fair chance that final hardware might perform better, especially considering this pre-production machine displayed many outstanding issues with the LCD display, idle current draw, and that plugging it in or running it from battery didn't make any difference. Interestingly, despite the 616.00 drivers adding features, performance actually took a significant turn for the worse.

The Cinebench 2024 multi-threaded CPU test produced a result of 1386 points, trailing the 12-core Macbook M4 Pro, while Cinebench 2026 yielded 5771, a fair bit behind the Apple M4 Max. Fouquin did run some GPU tests, and the best results in 3DMark were with the older drivers. Port Royal showed 26-31 FPS on older drivers, while Nomad got 20-21 FPS. Meanwhile, Unigine Superposition actually improved with the 616.00 software, netting a maximum of 56-58 FPS.

Compared to desktop cards, those results would roughly match RTX 3060 or RTX 3060 Ti, once again underscoring the pre-release nature of the Nvidia drivers and related software. As if more illustration was needed, the Balanced power plan almost always produced the best results.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The story isn't much different in gaming, as Fouquin says that while most of their library of games ran fine, the performance was very sluggish, with multiple-second stutters and with GPU clock speed "bouncing all over the place." *Helldivers 2* would outright crash the system, as did the GPGPU integer tests. Fouquoin believes these are all issues specific to this particular implementation of the N1X rather than a problem with the platform altogether. It's worth adding that presumably the games ran under the ARM emulation layer, which can introduce its own set of issues.

N1X chip and fixable warts aside, Fouquin actually liked the machine, remarking on the high build quality, the keyboard feel, touchpad input, and display quality. Given there were previous claims the machine would be serviceable, Fouquin put those to the test and opened it, finding that while that claim is technically true, "many snap-on thin aluminum sheet panels covering all the primary components (even encasing the SSD) means actually attempting to service the laptop will lead to much bending and/or breaking." Here's to hoping that this too is fixed before final release.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

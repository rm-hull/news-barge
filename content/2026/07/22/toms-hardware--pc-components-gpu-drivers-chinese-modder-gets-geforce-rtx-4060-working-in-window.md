---
title: Chinese modder gets GeForce RTX 4060 working in Windows 11 on Huawei Arm workstation
  — uses modified driver borrowed from an Nvidia RTX Spark
source_url: https://www.tomshardware.com/pc-components/gpu-drivers/chinese-modder-gets-geforce-rtx-4060-working-in-windows-11-on-huawei-arm-workstation-uses-modified-driver-borrowed-from-an-nvidia-rtx-spark
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-22T14:18:45Z'
published: '2026-07-22T00:00:00Z'
description: A janky first attempt at using an RTX GPU with Windows on Arm
image: https://cdn.mos.cms.futurecdn.net/qKdt8UASX2B4463bDnpbmT-1920-80.jpg
---

![Nvidia GeForce RTX 4060 review charts](https://cdn.mos.cms.futurecdn.net/qKdt8UASX2B4463bDnpbmT.jpg) 

When Microsoft and Qualcomm launched the first Copilot+ PCs sporting Snapdragon X Elite processors, the CPU performance was beyond reproach, but whether due to immature software or underwhelming integrated hardware, the GPU horsepower left a lot to be desired. The easiest way to solve that is to hook up a discrete GPU, of course, but nobody's managed that yet. Instead, an enterprising hacker in China has become the first person to publicly get an Nvidia GeForce RTX GPU running on an Arm-based platform using Windows 11, but it's not Snapdragon, and it's not an Nvidia CPU, either, *WindowsLatest* reports.

We knew that the Nvidia RTX Spark processors used an integrated GPU directly derived from Nvidia's Blackwell technology, and we also knew that those machines would run Arm Windows 11, so this was bound to happen sooner or later, because that necessarily means that there is an Nvidia client graphics driver for Arm-based Windows 11 out there. That's exactly what "VoidTech" on BiliBili used for his experiment, though the experiment wasn't without some pitfalls.

 ![A Chinese-language screenshot of a Windows 11 desktop, showing the GeForce RTX 4060 working on the Arm system.](https://cdn.mos.cms.futurecdn.net/x6yCxSamb5MrEaDHd2i8zY.jpg) 


Specifically, VoidTech got an Nvidia GeForce RTX 4060 8GB graphics card working in a Huawei Qingyun W510 workstation. This machine does not have a Snapdragon processor, of course; Huawei makes its own CPUs, and indeed this chip is the Kunpeng 920, created by Huawei's HiSilicon division. This chip was considered a major milestone when it was introduced in 2019, as it's a 7nm server CPU with up to 80 cores, although the specific implementation in the Qingyun W510 has "only" 24 cores.

All those cores don't help it much in gaming. As PC gamers will be well aware, CPU gaming performance is basically down to single-threaded CPU performance and system memory latency. The custom TaiShan v110 cores in the Kunpeng 920 only offer up around a sixth of the single-core performance of something like a Ryzen 9 9700X, at least going by Passmark, with the usual caveats that apply to Passmark. Combined with relatively small caches and a DDR4 memory interface that's clearly tuned for throughput, not latency, and you have a recipe for middling gaming performance. That's before we even start talking about x86 emulation penalties.

| Benchmark Comparison | Qingyun W510 + GeForce RTX 4060 8GB | Ryzen 7 5800X + GeForce RTX 4060 8GB | 
| Passmark ST / MT | 733 / 9496 | 3448 / 27671 | 
| Genshin Impact 1080p High | ~25 FPS | = 60 FPS (cap) | 
| Black Myth Wukong 1080p Medium | 21 FPS | 83 FPS | 
| 3DMark Speed Way | 2252 | 2682 | 
| 3DMark Time Spy Graphics | 6369 | 10939 | 
| 3DMark Time Spy CPU | 3402 | 10775 | 
| 3DMark Night Raid GPU | 43530 | 61080 | 
| 3DMark Solar Bay | 32373 | 49435 | 

So did it work? Well, more or less. Actually, the GeForce RTX 4060 did about half of its job flawlessly, running advanced games like the Unreal Engine 5-based *Black Myth Wukong* and slightly less advanced games (*Genshin Impact*), as well as various 3DMark tests. Most software seemed to work without any issues aside from overall weak performance due to the slow Kunpeng 920 CPU; the* Wukong*benchmark finished at 21 FPS, while* Genshin Impact*struggled to break 25 FPS and stuttered frequently. However,* Arknights: Endfield* refused to launch, likely due to an incompatibility between its restrictive "Anti-Cheat Expert" package and the Prism translation layer required to run the x86 Windows games on Arm Windows.

 ![A Genshin Impact screenshot showing poor performance on a 2019 Arm server with a GeForce RTX 4060 installed.](https://cdn.mos.cms.futurecdn.net/244vGKMwbRhxeU3ctkY8K8.jpg) 


The half of its job that the RTX 4060 *didn't* do was that VoidTech wasn't actually able to get a video signal out of the graphics card. He notes that the graphics card was recognized, and the monitor was picked up, too. He simply couldn't get the system to properly push pixels to the monitor. This likely comes down to the Nvidia Arm driver being built specifically for the RTX Spark and thus missing the necessary code to support the HDMI and DisplayPort encoders on desktop graphics cards. To get around this issue, VoidTech used the Sunshine game streaming server and the Moonlight game streaming client (on another system) to run the Huawei machine headlessly. A janky solution to be sure, but it does seem to have worked.

 ![A screenshot from the VoidTech video showing that the Chinese workstation, designed for Linux, doesn't have Windows drivers for many things.](https://cdn.mos.cms.futurecdn.net/pKu328GZEkP8Wa85ssppLj.jpg) 


There's a bit more to the video, including how VoidTech had a hard time getting Windows 11 to boot on the machine at all due to broken ACPI tables, some frustration with missing Windows 11 drivers for the HiSilicon Network Subsystem (HNS), a bit where he runs a Blender Cycles render on the GeForce RTX 4060, and a couple of Nvidia RTX demos including the Star Wars "Reflections" demo that was shown with the introduction of the RTX 20 Series "Turing" GPUs. It's an interesting saga of making hardware that was never meant to work together run on an operating system that none of it supports.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

This does somewhat bode well for RTX Spark. While you probably shouldn't expect the Cortex-X925 CPU cores in the RTX Spark to outpace the latest AMD or Intel CPUs due to still being forced to pay the Prism penalty, they're going to be a damn sight faster than this seven-year-old workstation chip. Since the drivers seem to be in good shape, the consumer laptops should indeed offer capable gaming performance when they arrive later this year—at least, as long as your game doesn't have kernel-level anti-cheat

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi.jpg)

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

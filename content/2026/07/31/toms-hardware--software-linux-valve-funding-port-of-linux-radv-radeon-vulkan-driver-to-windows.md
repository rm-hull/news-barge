---
title: Valve funding port of Linux RADV Radeon Vulkan driver to Windows — cross-platform
  effort already runs 'Counter-Strike 2'
source_url: https://www.tomshardware.com/software/linux/valve-funding-port-of-linux-radv-radeon-vulkan-driver-to-windows-cross-platform-effort-already-runs-counter-strike-2
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-31T14:29:24Z'
published: '2026-07-31T00:00:00Z'
description: Long-term effort can eventually pay off big dividends.
image: https://cdn.mos.cms.futurecdn.net/d9sMHtzKwoKRrKJSznzoAT-2121-80.jpg
---

![PCB under red light](https://cdn.mos.cms.futurecdn.net/d9sMHtzKwoKRrKJSznzoAT.jpg) 

The Steam Machine helped grow the popularity of Linux gaming, including installations of Bazzite and other gaming-oriented Linux distributions. Valve seemingly doesn't want to stop its open-source development efforts anytime soon, and is now working on a port of the Mesa Radeon Vulkan driver (RADV) to Windows; It's already running *Counter-Strike 2*, according to developers at Collabora.

As cross-platform development is rather tricky, Valve opted to get a port of RADV to Windows going by way of sponsoring contractors at Collabora. In its blog post, Collabora explained the several hoops it had to jump through to accomplish this task.

With Windows 10 and WDDM 2.0, Microsoft improved the split between graphics drivers' userspace code (the vast majority of the driver itself) and the kernel-level portion that actually talks to the graphics card. This presented the opportunity to hook RADV to the AMD kernel card driver. That's easier said than done, however, as communication between those parts often carries non-standardized data that RADV needs to understand. And to understand the "conversation," it needs to be recorded and analyzed.

An earlier 2024 effort by Faith Ekstrand yielded a basic-but-valuable utility for logging WDDM 2.0 calls and reverse-engineering them to produce a basic RADV implementation. Out of both debugging necessity and as a development tool, Collabora built and expanded upon Ekstrand's work, improving the logger to the point where it can now fully analyze any Vulkan application that runs with AMD's official driver and dump all the data passing to the kernel.

After a lot of work getting to grips with how the AMD driver interacts with the kernel driver, including but not limited to reverse-engineering obscure data structures, the team made progress, and Windows RADV is now able to run some games, including *Counter-Strike 2*.

Despite the ongoing effort, Collabora explains that since user- and kernel-space driver are a matched pair, changes to those aren't guaranteed to be backwards-compatible, meaning that even a fully functional RADV could break at any point. For that reason, Collobora is requesting that AMD, Microsoft, or both provide a documented interface to the kernel driver or an intermediary compatibility layer.

AMD graphics driver development on Linux has coalesced around the Mesa Vulkan stack, with both company and community devs contributing to the RADV project. Over in the Windows world, the only option is AMD's proprietary driver, which can cause a lot of headaches when developing cross-platform games and applications.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

AMD's Vulkan driver for Windows has developed a reputation for instability. Meanwhile, Linux RADV is generally praised for its stability and performance, sometimes running faster than the AMD Windows driver, especially on older cards. With a rapid development schedule, it also generally sees fixes and speed upticks often.

If at some point using RADV on Windows becomes viable, you'd be getting an arguably more stable, mature driver with active development. Games' graphical issues could become far easier to debug and patch thanks to the open nature of RADV, and studios developing with Linux in mind can target the one platform instead of two with different behaviors. Any developer or company can contribute to the project, too.

Furthermore, this lets Valve improve Windows compatibility layers, and any optimizations can be carried over to both operating systems. All told, this is likely one of the several moving parts to improve Linux — thus the Steam Deck, Steam Machine, and upcoming hardware — as a viable gaming platform. Even a future notion of gamers installing RADV on Windows to get a performance or stability boost isn't too far-fetched.

Additionally, RADV on Windows would also help keep discontinued cards usable, and given pricing right now, that certainly would be a good thing.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

---
title: Linux enthusiasts see 10-second kernel compilation times on the horizon — AI-assisted
  patches cut build times by nearly a third without a RAMdisk
source_url: https://www.tomshardware.com/software/linux/linux-enthusiasts-see-10-second-kernel-compilation-times-on-the-horizon-ai-assisted-patches-cut-build-times-by-nearly-a-third-without-a-ramdisk
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-27T16:56:26Z'
published: '2026-09-27T00:00:00Z'
description: Upcoming advances like Zen 6, PCIe Gen6 storage are expected to help
  get us into single figures.
image: https://cdn.mos.cms.futurecdn.net/j3i4k4NSzmSB3zYSzK3mEE-1920-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Lorenzo
- Mark Tyson
- Michael Larabel
- Tom
locations:
- Nova Lake
organisations:
- AI/LLMs
- AMD
- Get Tom's Hardware
- Google News
- Hammer Lake
- Lorenzo Stoakes
- Phoronix
- Samsung
- Tom's Hardware
---

![Benchmarking](https://cdn.mos.cms.futurecdn.net/j3i4k4NSzmSB3zYSzK3mEE.jpg)

It won’t be long until Linux enthusiasts will be able to complete a clean kernel build in under 10 seconds. Linux expert and Phoronix head honcho Michael Larabel said that “the coffee window is closing” in recent commentary that weighs computer processor advances and human / AI optimizations of the Kbuild code. What once used to be a computer processing task that provided a decent excuse for a coffee break now only allows enough time for a measured sip.

The source site’s determined Linux focus has meant that OS kernel compilation times have become a signature benchmark over the last two decades. Larabel notes that this once time-consuming process “can be done in now roughly 15 seconds.” It isn’t just advances in hardware and core counts pushing the envelope; compiling a defconfig x86-64 Linux kernel build has had many bottlenecks removed thanks to the work of Linux MM developer Lorenzo Stoakes and the assistance of AI/LLMs recently. Even modest processors have seen their compile times cut dramatically thanks to this work.

Larabel went hands-on with the latest v4 kernel patches from Lorenzo, and armed with his very powerful EPYC workstation, achieved “a 15-second kernel build!” Before the latest patches, the same system took over 22 seconds for the same compilation task.

The test system is extremely potent, though. Your home PC or laptop might still let you have enough time to go brew some coffee, as Larabel’s test rig features the following components:

* 2x AMD EPYC 9575F 64-core processors (so, 128 cores / 256 threads)
* 24 x 64GB DDR5-6400 memory modules
* Samsung PM1743 3.84TB PCIe Gen 5.0 NVMe SSD storage
* Stock Ubuntu 26.04 LTS

It is noted that the code compilation benchmarking didn’t employ a RAMdisk to aggressively tune the compile times

All the above timings mentioned are for the minimal default kernel compilation for x86-64 systems. The Phoronix chief also timed the compilation of a Linux kernel with ‘allmodconfig’ with thousands of drivers and subsystems enabled. This precipitates far longer compile times. On the above beefy system, though, the latest Lorenzo patches drove the time down from 169 seconds to 134 seconds. So, this other milestone is approaching the two-minute mark.

Phoronix is now taking bets on AMD (Zen 6) EPYC 9686F systems, with MRDIMMs and PCIe Gen6 storage pushing defconfig x86-64 Linux kernel compilation times under the 10-second mark.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

* Saw this earlier.Reply  
    
  There are a lot of caveats, like the test system having 128 cores, but Zen 6 and Nova Lake are going to bring big multi-threaded increases to consumer sockets. And if you're sitting the generation out because of high DDR5 prices, Zen 7 should bring another +33% to core counts, and Hammer Lake should bring back SMT.

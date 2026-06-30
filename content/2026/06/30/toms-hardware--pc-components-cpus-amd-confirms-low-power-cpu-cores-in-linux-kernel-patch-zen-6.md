---
title: AMD confirms low-power CPU cores in Linux kernel patch — Zen 6 chips could
  follow in Intel's footsteps with new core type for background tasks
source_url: https://www.tomshardware.com/pc-components/cpus/amd-confirms-low-power-cpu-cores-in-linux-kernel-patch-zen-6-chips-could-follow-in-intels-footsteps-with-new-core-type-for-background-tasks
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-06-30T18:09:16Z'
published: '2026-06-30T00:00:00Z'
description: Zen 6LP incoming?
image: https://cdn.mos.cms.futurecdn.net/b6AWuqaDHTv9ZS4ZpfqZNV-1280-80.png
---

![AMD](https://cdn.mos.cms.futurecdn.net/b6AWuqaDHTv9ZS4ZpfqZNV.png) 

AMD has submitted Linux kernel patches including support for its new low-power CPU cores that will likely emerge in its future heterogeneous processors. The new patch clearly distinguishes between high-performance cores, efficiency cores, and low-power cores, so it is safe to say that AMD's upcoming CPU platforms will use three types of cores, with the low-power one serving light workloads, reports *Phoronix*.

 ![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB.jpg) 


AMD's heterogeneous processors identify CPU types using CPUID Function 0x80000026 (Extended CPU Topology), as EBX bits [31:28] carry the core classification. Up until recently, AMD only classified its cores as Performance and Efficiency, while the latest patch adds Low-Power cores. The patch enables Linux to distinguish between Performance, Efficiency, and Low-Power cores efficiently, and the latter are also correctly supported by AMD's performance management.

According to AMD engineer Vishal Badole, these cores are designed specifically for background and idle tasks where reducing energy consumption is more important than offering high performance.

In recent years, both AMD and Intel released heterogeneous processors featuring both high-performance and energy-efficient types of cores in a bid to wed performance and low power consumption. With its latest CPU platforms, Intel introduced its low-power cores located in the SoC tile to offload light tasks and prolong the battery life of laptops. As it turns out, AMD is going the same route. Although AMD uses two different core types, the underlying architecture is the same. It offers a "dense" core offering that's optimized for space, while Intel uses entirely different microarchitectures.

Beyond the description of the Linux patch, AMD disclosed little about the low-power cores. The company only described them as being optimized for the lowest possible power consumption during background processing and idle operation, but did not reveal how they differ architecturally from today's dense Zen 5c cores. In addition, the kernel patches introduce no new scheduling policies or optimization logic beyond identifying the additional CPU category.

AMD also did not reveal whether these cores are based on the Zen 5, Zen 6, or other future microarchitecture. It should indeed be noted that AMD has traditionally preferred to use the same microarchitecture within one CPU, albeit with different optimizations when it comes to die size (or rather floorplan) and clocks. Such an approach greatly simplifies software development and performance management, but at the cost of higher power consumption compared to what a simplified microarchitecture would have offered.

  


*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

- 
I've argued about the Zen 6 LP cores here back when they were a leak. Desktops should get them, and they can lower idle/low-intensity power consumption and save everybody (small amounts of) money. Governments and businesses will appreciate lowering power across millions of x86 machines.Reply
 
 The E-cores/C-cores are there to maximize multi-threading performance per die area for the most part. LPE-cores and LP cores will be truly efficiency focused, especially if they can turn off the compute die(s) completely when they aren't needed.
 
 Having more of them could prevent tasks from spilling over to compute die(s). Every Nova Lake-S SKU will have 4c/4t of these. I think they should move up to 8c/8t in a future generation.
 
 Your operating system could have a super power saving mode to manually disable CCDs and run everything on LPs. For example, if you're trying to run a mini PC off a battery pack, are working in a hot environment, etc.
 
 Zen 6 mobile APUs will definitely get LP cores. Zen 6 Olympic Ridge desktop CPUs are still uncertain, and we've recently heard they may not include an iGPU, but will include a big NPU. If they do include Zen 6 LP cores, it will be 2c/4t. If they make the final cut, I suspect they may include a tiny amount of dedicated L3 cache, e.g. 4 MiB.

---
title: '16 cores, 5.2 GHz, and 55 TOPS: Minisforum''s newest AI workstation is mostly
  a massive upgrade to 192GB of memory - and that is not necessarily a bad thing'
source_url: https://www.techradar.com/pro/16-cores-5-2-ghz-and-55-tops-minisforums-newest-ai-workstation-is-mostly-a-massive-upgrade-to-192gb-of-memory-and-that-is-not-necessarily-a-bad-thing
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-14T04:49:50Z'
published: '2026-10-14T00:00:00Z'
description: Minisforum's $7,399 MS-S1 MAX-P495 leads with 16 cores and 55 TOPS
image: https://cdn.mos.cms.futurecdn.net/LEbuAknSz7pCmnKQQf47aQ-1600-80.webp
categories:
- Technology & Software
people: []
locations: []
organisations:
- AMD
- APU
- CPU
- GPU
- LPDDR5X
- Minisforum
- MoE
- NPU
- Nvidia
- Qwen3.5-397B
- RAM
- TechRadar Pro
---

![The Minisforum MS-S1 MAX-P495 pictured](https://cdn.mos.cms.futurecdn.net/LEbuAknSz7pCmnKQQf47aQ-1600-80.webp)

* **Minisforum's MS-S1 MAX-P495 is on pre-order at $7,399 with 192GB of unified memory and a 2TB SSD**
* **CPU and NPU specs are similar to previous iterations: 16 cores, 32 threads with a boost in clock speeds of 100 MHz, in addition to increased NPU performance by 10% to 55 TOPS**
* **The real upgrade is memory: 192GB total, 160GB for the GPU, and about 7% more bandwidth, enough to fit a 284B-parameter MoE model on one box**

Minisforum has opened orders for the MS-S1 MAX-P495, a 3.5-liter workstation built around AMD's Ryzen AI Max+ PRO 495, and its launch announcement leads with the processor: 16 Zen 5 cores and 32 threads, clocks of up to 5.2 GHz, and an NPU rated at up to 55 TOPS within a platform total of 131 TOPS.

The single configuration pairs 192GB of unified memory with a 2TB SSD, sells for $7,399 on pre-order, and is expected to begin shipping in mid-October 2026.

Those processor figures match AMD's own specification page; however, they are also the least consequential change in the machine: what actually separates the P495 from the MS-S1 MAX that Minisforum launched a year ago is the memory.

## Similar cores, much larger memory pool

AMD introduced the Ryzen AI Max PRO 400 series in May 2026 as a refresh of the Strix Halo silicon in the 300 series, and the CPU side barely improves in performance. The PRO 495 keeps the 16-core, 32-thread Zen 5 layout of the Ryzen AI Max+ 395 that powered the original MS-S1 MAX. Its boost clock rises by 100 MHz, from the 5.1 GHz listed on Minisforum's spec sheet for the earlier model to 5.2 GHz.

The Radeon 8065S graphics keep 40 RDNA 3.5 compute units and gain 100 MHz to reach 3.0 GHz, and the NPU goes from 50 to 55 TOPS, a 10% uplift that nudges the platform rating from 126 TOPS to 131 TOPS.

All of these upgrades are mild compared to where AMD does the real work: the memory controller. The 400 series supports up to 192GB of LPDDR5X across a 256-bit interface, with up to 160GB assignable to the GPU, against 128GB and 96GB on the last-generation chip it replaces. Rated memory speed also rises from 8,000 to 8,533 MT/s, a roughly 7% increase that will probably matter more here than the clock-speed bumps on display.

Minisforum's own test results show where the extra capacity pays off: the company says a single unit ran DeepSeek V4 Flash, a 284-billion-parameter model, at Q4 quantization at about 12 tokens per second. Two units linked together ran Qwen3.5-397B at roughly 16 tokens per second, and a four-system cluster loaded the 380GB Q4\_0 build of DeepSeek-R1 671B, though it gives no speed for that last result.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

These parameter counts are larger, however, than the actual work involved. Both models use a mixture-of-experts (MoE) design, which lets them load only specific "experts" into memory when needed. DeepSeek V4 Flash activates about 13 billion of its 284 billion parameters for each token, per Nvidia's catalog entry, and Qwen3.5-397B activates about 17 billion, per its model card.

Memory capacity decides whether a model fits at all, while active parameters and bandwidth decide how fast it runs, which is how a box with roughly 273 GB/s of bandwidth manages double-digit speeds on models this large. That is also why the 192GB of RAM in play matters far more than the modest performance upgrade the MS-S1 MAX-P495's APU offers.

The $7,399 price it currently goes for is presented as 20% off a list price of $9,249 that nobody has paid yet, with the unit going on sale even in the preorder stage. This makes the standard MS-S1 MAX with 128GB arguably a better value for all but the most ardent of local AI users who can justify twice the cost for a 50% increase in memory.

The rest of the machine (sans the APU and memory) is identical to the original MS-S1 MAX, including the 320W internal power supply, the six-heat-pipe, dual-blower cooler, dual 10GbE, two 80Gbps USB4 v2 ports, and 2U rack support.

What changes here is that a single compact box can now hold models that previously needed two, and for developers and small teams that need 200-to-300-billion-parameter mixture-of-experts models kept on premises for privacy or latency, that is a meaningful shift. For anyone drawn in by the 16 cores and 55 TOPS that Minisforum chooses to headline with, the cheaper MS-S1 MAX delivers nearly the same power for about half the price.

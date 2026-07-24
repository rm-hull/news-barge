---
title: Nvidia reveals deep dive into what makes Vera CPU tick — with the super-powered
  Olympus core promising huge performance increases and more
source_url: https://www.techradar.com/pro/nvidia-reveals-deep-dive-into-what-makes-vera-cpu-tick-with-the-super-powered-olympus-core-promising-huge-performance-increases-and-more
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-24T21:17:36Z'
published: '2026-07-24T00:00:00Z'
description: A different kind of AI data center CPU
image: https://cdn.mos.cms.futurecdn.net/MLH2WqUBs2jRD6pZ52Gdn6-1462-80.jpg
---

![Nvidia Vera CPU](https://cdn.mos.cms.futurecdn.net/MLH2WqUBs2jRD6pZ52Gdn6.jpg) 

- **Nvidia's Olympus core architecture prioritizes single-thread IPC over frequency, using a 10-wide decode front end, deep out-of-order mid-core, and a graph prefetcher tuned for agentic AI's branch-heavy, pointer-heavy workloads**
- **Vera trades chiplet-style core density for a monolithic 88-core die and single-NUMA-per-socket design, a deliberate bet on agentic AI workloads that Nvidia's own engineers admit comes at the expense of legacy workload performance**
- **Self-reported SPEC CPU 2026 results by Nvidia paint a per-core advantage figure of anywhere between 70% and 80% versus AMD's EPYC 9755 server CPU**

Nvidia's Vera CPU has a lot to prove, representing the company's first real attempt at the AI server CPU market, where traditional vendors Intel and AMD, along with third-party Arm-based providers, are all gunning for a piece of an increasingly lucrative data center pie.

To that end, Nvidia has published its most detailed technical account yet of the chip, promising substantial performance gains over the competition. Vera is the company's first server processor built around a fully in-house core design, a departure from the stock Arm cores that powered its Grace predecessor.

As Vera heads toward general availability in the second half of 2026, Nvidia is making its case on a specific front: not raw core count, but sustained per-core performance under load, the metric it argues matters most for agentic AI.

## What's actually under the hood of Nvidia's Vera CPU?

At the core of every Vera CPU is Olympus, Nvidia's first custom server core, built to the Armv9.2 instruction set but designed in-house rather than derived from Arm's stock Neoverse designs, as its predecessor, Grace, was.

Nvidia's second-generation data center CPU is a completely reworked design built around a single goal: to lead in agentic workload performance.

Rather than following Intel and AMD down the chiplet route, Nvidia packs all 88 cores (176 threads) onto a single monolithic die, with a dual-socket configuration delivering 176 cores and 352 threads in one system.

Nvidia has detailed the core design extensively, and several publications have since dug into the microarchitecture. The front end runs a 10-wide decode engine paired with a neural branch predictor that can resolve up to two taken branches per cycle, designed to handle the large instruction footprints and irregular control flow of interpreters, compilers, and agent runtimes.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

 ![Nvidia GPUs](https://cdn.mos.cms.futurecdn.net/zqz2HRcSyyaU7RCQ6HodRU.jpg) 


The mid core combines a wide rename-and-allocation engine with a large reorder buffer and dependency-breaking techniques including memory renaming and value prediction.

The execution engine schedules dynamically across integer, vector, floating-point, cryptographic, load, and store resources, while the cache subsystem adds a graph prefetcher targeting the pointer-chasing access patterns that defeat conventional streaming prefetchers.

That design has not gone unanswered. AMD has countered with estimated figures for its 256-core Zen 6 "Venice" part, claiming a 3.3x rack-level advantage over Vera, though those numbers are extrapolated rather than measured.

AMD responding first isn't surprising. Within x86, it continues taking ground from Intel, reaching 33.2% of x86 server CPU shipments in Q1 2026 per Mercury Research, up from 27.2% a year prior.

With Arm reporting that its architecture now accounts for roughly 50% of CPU compute among top hyperscalers, competition is building from several directions at once. Vera may well set a new bar for agentic AI.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

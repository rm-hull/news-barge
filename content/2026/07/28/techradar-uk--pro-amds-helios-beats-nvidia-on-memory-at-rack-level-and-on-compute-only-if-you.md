---
title: AMD's Helios beats Nvidia on memory at rack level and on compute — only if
  you count it at the GPU level
source_url: https://www.techradar.com/pro/amds-helios-beats-nvidia-on-memory-at-rack-level-and-on-compute-only-if-you-count-it-at-the-gpu-level
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-28T17:43:35Z'
published: '2026-07-28T00:00:00Z'
description: A GPU-level win that does not scale linearly
image: https://cdn.mos.cms.futurecdn.net/JDsz8h7QFekhAxGx6aXjTT-1200-80.jpg
---

![A render of the AMD Helios server rack from 2025](https://cdn.mos.cms.futurecdn.net/JDsz8h7QFekhAxGx6aXjTT.jpg) 

- **AMD's Helios beats Vera Rubin NVL72 on memory at rack level, with 31TB of HBM4 against roughly 20.7TB**
- **AMD also claims it beats the competition by 15% on FP4 compute on a 'per-GPU' basis even as Nvidia comes out ahead on published 'per-rack' figures**
- **AMD claims Helios also offers 30% more tokens per dollar spent versus the competition**

AMD has launched its Helios rackscale offering, outlining five comparisons in which it claims wins over what it calls "the leading competitive solution."

While the company skipped naming Nvidia, the market leader's Vera Rubin-based NVL72 rack-scale solution is the only real competitor to Helios and the one it continues to compare itself against.

While its memory claims hold, its GPU FP4 claim might fall short when comparing rack to rack, and many of its calculations are based on peak performance rather than Nvidia's published numbers, making Helios an interesting "win" but one that does encourage potential adopters to look more closely.

## A numbers game that continues to grow complex even as AMD ekes out some wins

While AMD claims a 15% win versus Nvidia's Rubin on a per-GPU basis for FP4 compute, its 72-GPU rack-scale solution falls short of Nvidia's published rack-level numbers: 2.9 exaflops versus 3.6. AMD does not specify whether it is counting Nvidia's individual dies or its two-die packages, and the distinction matters: against dies the gap runs in AMD's favor by far more than 15%, while against packages AMD trails.

The two figures also use different formats, AMD's MXFP4 against Nvidia's NVFP4, so they are not measuring identical arithmetic.

This might, however, be indicative of a very real situation that hampers both vendors' headline numbers: real-world FP4 workloads rarely reach hardware peak ratings due to memory movement constraints, scheduling overheads, and software kernel efficiency. AMD conceded as much at its own event, putting measured FP4 throughput at roughly half its peak rating.

Nvidia may sustain more of its peak thanks to its custom Vera CPU, a mature NVLink 6 software stack and a larger pool of what it calls fast memory, 75 TB per rack once 54 TB of LPDDR5X is counted alongside 20.7 TB of HBM4. AMD's 31 TB is all HBM, which is better suited to models that must be held entirely in high-bandwidth memory, and Helios offers higher capacity and bandwidth per accelerator at 432 GB and 23.3 TB/s.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

On raw scale-up fabric, the two are level, both delivering 3.6 TB/s per accelerator and 260 TB/s per rack.

Despite this, Helios is an exceptionally strong product on paper, and it may be the first time AMD has produced a credible rack-scale answer to Nvidia since the AI race began. Seventy-two MI455X accelerators, 18 EPYC Venice CPUs, 31 TB of HBM4, UALink over Ethernet inside the rack and Ultra Ethernet out, on an OCP Open Rack Wide chassis with merchant Broadcom switch silicon, is a serious response to a company that had a two-year head start on the form factor.

More importantly, its fabric specifications are publicly available, enabling hyperscalers to build customized variants that meet their requirements. Nvidia's platform offers no equivalent latitude.

AMD frames openness as the platform's central advantage, with Vamsi Boppana, senior vice president of AI at AMD, saying that Helios "brings together leadership compute, high-performance networking and open software in a unified rackscale platform."

The more important question for AMD, however, might be memory supply. Nvidia has had Vera Rubin in full production since Q1 with partner availability this half, while AMD's first Helios deployments are not due until Q4. AMD may be further gated by HBM4 supply, much of which is reported to be already committed to hyperscalers, which could keep its deployment volumes well below Nvidia's this year.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

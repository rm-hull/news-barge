---
title: Intel reportedly cans 12Xe option for Nova Lake-S desktop — gaming APU design
  said to resurface with Razor Lake
source_url: https://www.tomshardware.com/pc-components/cpus/intel-reportedly-cans-12xe-option-for-nova-lake-s-desktop-gaming-apu-design-said-to-resurface-with-razor-lake
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-15T19:41:23Z'
published: '2026-09-15T00:00:00Z'
description: Intel's gaming APU won't show up in the next generation, apparently.
image: https://cdn.mos.cms.futurecdn.net/6dhScSyVh9hBM75rUoJ4qN-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
---

![Intel 12th Generation Alder Lake CPU](https://cdn.mos.cms.futurecdn.net/6dhScSyVh9hBM75rUoJ4qN.jpg) 

Intel won't launch a Nova Lake-S SKU with 12 Xe3P graphics cores, according to tipster Jaykihn, who originally flagged a beefed-up APU design with the Nova Lake architecture. The original SKU was said to come with 4 P-cores, 8 E-cores, and 4 LPE-cores, along with the 12 Xe3P cores, presumably offering an inexpensive onramp to a gaming desktop without a discrete GPU. Now, the leaker says that design is cancelled, and Intel intends to pick it back up with Razor Lake, the generation that will follow Nova Lake.

Originally, Intel's 12 Xe3P Nova Lake SKU was said to require 65W of dedicated power to drive the iGPU, necessitating the use of two VCCGT phases on the motherboard for integrated graphics. Intel's Arc B390 GPU, which is the 12 Xe3-core model available in Panther Lake and Arc G-series processors, has a thermal design that can sustain up to 80W. However, it's currently being used in Panther Lake machines and handhelds like MSI Claw 8 EX AI+ that have lower power targets.

The Xe3P architecture is slotted for use in Intel's Crescent Island AI accelerator, but it hasn't been announced for any other products yet. Xe3P supports a wide deployment of Xe cores (up to 32), a deeper XMX engine with support for low-precision data types like FP8 and FP4, an increased 512KB L1 cache per Xe core, and a new unified L2 cache (32MB on Crescent Island).

Even by desktop APU standards, an 80W iGPU is a beefy accelerator to have on the same package. In addition, Intel's Nova Lake stack is said to extend up to a 175W TDP with the rumored top-end 52-core SKU, meaning the full 12 Xe3P iGPU would likely only be possible lower down the stack (and maybe only in the 4 + 8 + 4 + 12 Xe design originally suggested).

Earlier in the year, rumors suggested Intel was working on a mobile APU to counter AMD's Strix/Gorgon Halo products, featuring a large pool of unified memory and a large iGPU, dubbed Nova Lake AX. Now, the rumor mill suggests Intel will recycle the Nova Lake CPU cores for Razor Lake AX on mobile while pushing a larger iGPU.

| Nova Lake-S rumored specifications |  |  |  | 
|---|---|---|---|
| SKU*| Core Config (P+E+LPE)* | bLLC*| TDP (Unlocked/Locked)* | 
|---|---|---|---|
| 52 Cores (dual-tile) | (8+16)+(8+16)+4 | 288MB | 175W | 
| 44 Cores (dual-tile) | (8+12)+(8+12)+4 | 264MB | 175W | 
| 28 Cores | 8+16+4 | 144MB | 125W | 
| 28 Cores | 8+16+4 | - | 125W / 65W | 
| 24 Cores | 8+12+4 | 132MB | 125W | 
| 24 Cores | 8+12+4 | - | 125W / 65W | 
| 22 Cores | 6+12+4 | 108MB | 125W / 65W | 
| 22 Cores | 6+12+4 | - | 125W / 65W | 
| 16 Cores | 4+8+4 | - | 65W / 35W | 
| 12 Cores | 4+4+4 | - | 65W / 35W | 
| 8 Cores | 4+0+4 | - | 65W / 35W | 
| 6 Cores | 2+0+4 | - | 65W / 35W | 

**Specs rumored, unconfirmed by Intel*

Intel has told us that Nova Lake is one of the most important desktop CPU launches for the company ever, following on the heels of the mediocre Arrow Lake rollout. Perhaps the biggest addition to the lineup is rumored to be bLLC, or big last-level cache, which is said to show up on select SKUs to counter AMD's X3D assault among the best CPUs for gaming. The company has yet to confirm that bLLC is even possible with its current packaging capabilities, though enthusiast channel VP Robert Hallock hinted to *Tom's Hardware* that Intel has plans to address X3D in the next generation.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The main stack is rumored to climb up to 28 cores, with two additional dual-tile SKUs that can go as high as 52 cores. The dual-tile models look like a bid for HEDT, perhaps competing with AMD's Threadripper CPUs, though it's not clear how Intel will position its dual-tile models yet.

Earlier this month, a leaked slide gave us a glimpse into Intel's launch plans for Nova Lake. The slide suggested Intel will announce the main stack (up to 28 cores) in Q4 of this year, with the chips arriving in Q1 2027. Intel will apparently follow up later in the year with the 52-core model. This aligns with what we've heard from our sources about Intel's Nova Lake rollout.

Alongside Nova Lake, Intel will introduce the new LGA1954 socket, along with the flagship Z990 chipset. We've already seen multiple Z990 motherboards in the flesh, suggesting Intel is preparing for a Nova Lake release in short order.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg) 

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

- 
Disappointing, but it's in line with the Nova Lake-AX (different APU) cancellation rumors.Reply
 
 I don't think the gap between Nova and Razor is supposed to be that long either, guess we'll see how that plays out.
 
AMD gets to reign supreme with its half-hearted desktop APUs for a little longer.
- 
Reply
This was actually my take on reading the news: RZL is likely on time for a proper release whereas NVL is releasing over the first half of the year. Another thing to keep in mind is that RZL-AX is still using Coyote Cove so this would fit with that as well.usertests said:I don't think the gap between Nova and Razor is supposed to be that long either, guess we'll see how that plays out.

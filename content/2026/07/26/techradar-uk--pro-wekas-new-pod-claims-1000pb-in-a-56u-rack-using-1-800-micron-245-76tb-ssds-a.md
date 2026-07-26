---
title: WEKApod 3 reaches the exabyte milestone using 1,800 Micron SSDs
source_url: https://www.techradar.com/pro/wekas-new-pod-claims-1000pb-in-a-56u-rack-using-1-800-micron-245-76tb-ssds-and-a-decades-old-compression-trick
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-26T21:09:01Z'
published: '2026-07-26T00:00:00Z'
description: WEKA squeezes claimed 1.1 exabytes into one rack, though compression
  does much of the heavy lifting behind the headline
image: https://cdn.mos.cms.futurecdn.net/GcrTCnpBmQ3XdHYts8Cref-1920-80.png
---

![WEKAPod 3](https://cdn.mos.cms.futurecdn.net/GcrTCnpBmQ3XdHYts8Cref.png) 

- **WEKApod 3 reaches exabyte capacity through software alongside dense Micron storage**
- **NeuralMesh 6 turns 441.5PB of flash into claimed exabyte-scale storage capacity**
- **WEKApod 3 relies on compression to exceed raw storage hardware limits**

WEKA has launched WEKApod 3, a storage appliance line built specifically to run its new NeuralMesh 6 software at rack-scale density.

The flagship Prime Max configuration claims 1.1 exabytes of effective capacity within a single 56U rack, positioning it as the first system to cross that threshold.

Using Micron's 245.76 TB 6600 ION SSDs across roughly 1,800 drives per rack yields only 441.5 PB of raw hardware capacity, well under half an exabyte.

## Software tiering closes the capacity gap

This means that the advertised exabyte-scale capacity depends heavily on data reduction technologies rather than installed flash alone.

That configuration packs 70 NVMe drives into a compact two-rack-unit, two-node chassis for maximum density.

Fingerprinting, similarity hashing, deduplication, and compression run by default across every deployment, with write overhead kept below 5%.

WEKA claims up to 6x capacity savings specifically on AI training data, backed by a contractual guarantee covering both reduction ratio and performance.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

This is where NeuralMesh 6 and WEKApod 3 genuinely function as one integrated product rather than separate announcements.

AlloyFlash tiering automatically routes latency-sensitive operations to TLC flash while sending bulk-capacity data to QLC drives, which run roughly 30 to 40% cheaper per terabyte.

Per-rack throughput reaches 10.2 TB/s with 210 million IOPS, figures WEKA says beat the next-best publicly available alternative by 114% in throughput density.

Jeremy Werner, senior vice president at Micron's Core Data Center Business Unit, said the architecture paired with Micron's 245TB SSDs delivers 15.8 petabytes within a single 2U footprint.

Steve McDowell, chief analyst at NAND Research, argued that inference workloads at production scale demand different metrics than training, pointing to tokens per rack and cost per inference as the numbers buyers should now track.

## Constraints force storage vendors to rethink hardware entirely

WEKA points to several structural pressures behind this hardware approach, starting with a documented drop in US data center construction in 2025.

Grid connection queues in major markets now stretch four to seven years before new capacity comes online.

Morgan Stanley has forecast a 49-gigawatt power shortfall across the United States extending through 2028, compounding existing NAND supply constraints.

WEKA argues that inefficient storage directly competes with GPUs for the same limited rack space and power budget.

By managing its own hardware supply chain instead of relying on third-party OEM channels, the company says it can offer more predictable pricing and delivery timelines.

NeuralMesh 6 will hit the shelves in the second half of 2026, with existing customers upgrading at no additional cost.

WEKApod Nitro, Prime, and Prime Max are already orderable through WEKA's distributor network, with deliveries beginning in fall 2026.

Via Storage Review

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

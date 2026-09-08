---
title: Arm debuts next-gen semi-custom Neoverse CSS N4 ‘Ranger’ platform — compute
  subsystem packs up to 128 cores per die on TSMC N3P
source_url: https://www.tomshardware.com/pc-components/cpus/arm-debuts-next-gen-semi-custom-neoverse-css-n4-ranger-platform-compute-subsystem-packs-up-to-128-cores-per-die-on-tsmc-n3p
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-08T04:26:20Z'
published: '2026-09-08T00:00:00Z'
description: Putting a little pep in Neoverse N-series’ step.
image: https://cdn.mos.cms.futurecdn.net/bAKg8h7YbSj7xEQNjC7EXi-1600-80.jpg
---

![An Arm CPU in a motherboard.](https://cdn.mos.cms.futurecdn.net/bAKg8h7YbSj7xEQNjC7EXi.jpg) 

Arm is bringing its next-gen Neoverse CSS N4 platforms to the cloud, sporting up to 128 cores per die, built on TSMC’s N3P process. Arm’s Compute Subsystem, or CSS, is a semi-custom program that allows customers to design a chip based on Arm’s IP, configuring components like core count, cache size, I/O, and connectivity to fit their specific needs. It’s the same platform we’ve seen at work everywhere from CPUs at Azure and Google Cloud to DPUs at Nvidia and Intel.

Arm says Neoverse CSS N4 supports between eight and 128 Neoverse N4 cores, running up to 3.8 GHz. Presumably, the clocks drop as the core count rises; Arm didn’t clarify the maximum clocks for each possible configuration. At a system level, Neoverse CSS N4 can scale beyond 128 cores, with support for multi-chiplet and multi-socket designs, and with support for UCIe through chip-to-chip interconnects, as well as “partner-specific PNYs.”

The platform supports either DDR5 or LPDDR6, and features up to 256 MB of L3 cache per die. For local cache, Arm includes up to 2 MB of L2 per core, as well as 64 KB of L1 instruction cache and 64 KB of L1 data cache per core. For I/O, Arm supports up to 128 lanes of PCIe 7/6 and CXL 4.0.

It’s a significant upgrade over the Neoverse CSS N2 platform, which topped out at just 64 cores, 1 MB of L2 cache per core, and 64 MB of L3 cache, paired with either DDR5 or LPDDR5 and 64 PCIe 5.0/CXL lanes.

 ![Arm Neoverse CSS N4 platform.](https://cdn.mos.cms.futurecdn.net/Mqh37KJZubEeuTqMwhzft6.jpg) 


With 128 cores running at 3GHz and 2MB of L2 cache per core, Arm says Neoverse CSS N4 delivers twice the socket performance of Neoverse N3, 1.25x performance per watt, and 1.75x the memory bandwidth.

Arm’s N-series cores are optimized for performance per watt, while its V-series cores are targeting maximum performance. For instance, Arm used the Neoverse CSS V3 building blocks for its own AGI CPU, and Nvidia used Neoverse V2 for its last-gen Grace CPU (the __Vera CPU uses a custom core__). AWS has also used Neoverse V-series cores for its own Graviton chips, as does __Google Cloud for Axion__.

N-series cores aren’t usually deployed in high-performance CPUs. Rather, they fit into less-performant accelerators, such as Intel’s IPU Adapter E2100, which is built on Neoverse N1 cores. We’ve also seen it deployed in less-demanding, cloud-based workloads, such as through Microsoft’s Azure Cobalt 100, which is built on Neoverse N2. Cobalt 200 moved onto Neoverse V3.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

We don’t know much about the Neoverse N4 cores, codenamed Dionysus. Arm’s 2024 roadmap indicated we’ll see Arm Neoverse CSS V4, as well, codenamed Vega.

Unlike a traditional announcement from Intel, AMD, or the various partners that build on Arm, we won’t see Neoverse N4 cores in the wild for a while. The announcement Arm is making is for those who are building on the CSS platform, leveraging Arm’s validated building blocks to create semi-custom silicon quickly. Arm has yet to announce any partners, though traditionally, only a few large CSS contracts are needed.

## Additional Arm AGI CPU deployments

 ![Arm AGI CPU deployments](https://cdn.mos.cms.futurecdn.net/SbeseATtzoYi2jqrvY5uDm.jpg) 


Alongside the announcement of Arm Neoverse CSS N4, the company revealed additional deployments of __its own AGI chip__, which is built with Neoverse V3 cores. The company revealed that Oracle and ByteDance will deploy AGI chips, alongside previously announced deployments at Meta, Lenovo, SAP, OpenAI, Cloudflare, and others.

Although Arm has talked a lot about AGI, including __a deep dive into the chip’s architecture at Hot Chips__, we’ve yet to see real-world performance numbers. That’s not uncommon, especially among more recent Arm-based chips. For instance, we only have gen-on-gen __comparisons for Microsoft’s Azure Cobalt 200__ and AWS’ Graviton5. Arm has vaguely referenced performance by saying AGI offers “more than 2x the performance per rack compared to the latest x86 systems,” though those claims are based on internal estimates, not real benchmarks.

AGI is a dual-die CPU with up to 136 Neoverse V3 cores and up to 272 MB of L3 cache that can clock up to 3.7 GHz. It has the specs to match any high-end x86 design currently on the market, built on a 3nm node and packing up to 6TB of memory capacity per chip, running at up to DDR5-8800. Perhaps the biggest difference compared to AMD and Intel was Arm’s decision to include the memory and I/O on the same die as compute, which it says leads to sub-100ns memory latency.

It’s Arm’s first attempt at its own production silicon, though it’s also been positioned so far as a vehicle for the broader applications of Arm in the data center. Microsoft, Nvidia, Meta, Google Cloud, and others build custom chips based on Arm IP, which still seems to be the primary goal, even with AGI in the mix.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg) 

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

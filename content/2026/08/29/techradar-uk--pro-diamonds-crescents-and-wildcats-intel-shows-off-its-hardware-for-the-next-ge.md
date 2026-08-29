---
title: 'Diamonds, Crescents and Wildcats: Intel shows off its hardware for the next
  generation of agentic AI workloads'
source_url: https://www.techradar.com/pro/diamonds-crescents-and-wildcats-intel-shows-off-its-hardware-for-the-next-generation-of-agentic-ai-workloads
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-29T06:59:48Z'
published: '2026-08-29T00:00:00Z'
description: Intel wants to power the next iteration of AI
image: https://cdn.mos.cms.futurecdn.net/ec3PDmnghmiiwaebiAjh83-970-80.jpg
---

![Intel](https://cdn.mos.cms.futurecdn.net/ec3PDmnghmiiwaebiAjh83.jpg) 

- **Intel shows three agentic AI architectures at Hot Chips 2026: the 256-core Diamond Rapids Xeon, the Crescent Island inference GPU, and the already-shipping Wildcat Lake client SoC**
- **Diamond Rapids matches AMD's EPYC Venice on cores and bandwidth but arrives in 2027 with half the threads, while Wildcat Lake's 17 TOPS NPU falls short of Copilot+'s 40+ TOPS certification**
- **Intel's Crescent Island will support up to 480 GB via third-party partner cards, but the Intel-branded variant will be limited to 160 GB, even as it currently does not publish the memory bandwidth that determines its token economics.**

Intel used its slot at Hot Chips 2026 to lay out three architectures it says will carry agentic AI from the rack to the laptop.

The already-shipping Wildcat Lake Core Series 3 SoC is for mainstream client and edge machines, Crescent Island is an inference-optimized data center GPU, and Diamond Rapids is its next-generation enterprise-class data center CPU that can be configured with up to 256 cores.

Pushkar Ranade, Intel's chief technology officer, said in a statement accompanying the announcement that agentic AI is changing how the company designs computing from the transistor upward.

## Plenty of compute promises, sans some GPU numbers

Intel's Diamond Rapids, which it plans to brand as Xeon 7, is where the chipmaker provides the most information, unsurprisingly, in an industry that plans purchases and upgrades years in advance.

Its flagship offering can encompass as many as 256 cores, backed by 1.28G of fast last-level cache, 16 memory channels, 128 PCIe 6 lanes, and CXL 3.0. ServeTheHome reported that the maximum configuration uses 16-core chiplets, built on Intel's 18A-P process node.

Rival chipmaker AMD also offers a 256-core trim: the EPYC 9996, built on TSMC's 2nm node, keeps hyperthreading in play, effectively doubling its thread count versus Intel's flagship.

Its Crescent Island GPU is arguably the most interesting design of the three, but the least detailed: a 350W air-cooled PCIe card built on its Xe3P GPU architecture, with 32 cores feeding 256 third-generation XMX engines and 32 MB of unified L2 cache. It surprisingly uses LPDDR5X rather than HBM, but the choice seems rationalized to offer capacity at a power and cost profile that lets Intel compete meaningfully with Nvidia and AMD.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Interestingly, the 480GB figure Intel touts in its press release isn't what it will ship; Intel-branded cards cap at 160GB, and 480GB is a ceiling available to ODM partners building their own configurations. Intel also remains mum on memory bandwidth specifics and told Chips and Cheese it won't disclose the figure; this is crucial for many AI applications, as memory bandwidth determines decode throughput, and decode throughput essentially determines token economics.

Of the three architectures that Intel talked about, Wildcat Lake is the only one you can pick up off a shelf (as a miniPC or laptop) today; it launched as Intel's Core Series 3. Intel stated that it replaced the Foveros packaging used in Panther Lake with an organic multi-chip package, eliminating the base die and, with it, assembly cost and yield loss. Compute die area fell by 38 percent, and I/O tile area by 15 percent.

The 17 TOPS NPU available to such CPUs sits well below the 40 TOPS Microsoft requires for Copilot+ certification. The 40 TOPS Intel cites is a platform total across CPU, GPU, and NPU, which arguably can be met elsewhere, but it's a sticking point for the chipmaker's AI push, which has otherwise been concentrated on capturing enterprise and hyperscale customers.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

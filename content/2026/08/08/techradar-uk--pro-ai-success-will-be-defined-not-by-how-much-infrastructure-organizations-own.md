---
title: '''AI success will be defined not by how much infrastructure organizations
  own, but by how productively they use it'': Nvidia lays out its thoughts on how
  storage has become the next frontier of AI'
source_url: https://www.techradar.com/pro/ai-success-will-be-defined-not-by-how-much-infrastructure-organizations-own-but-by-how-productively-they-use-it-nvidia-lays-out-its-thoughts-on-how-storage-has-become-the-next-frontier-of-ai
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-08T16:48:41Z'
published: '2026-08-08T00:00:00Z'
description: Storage is the new frontier for AI
image: https://cdn.mos.cms.futurecdn.net/Nhzgg9xAiHAHtrAZnwyfqD-1920-80.jpg
---

![Nvidia logo on a dark background](https://cdn.mos.cms.futurecdn.net/Nhzgg9xAiHAHtrAZnwyfqD.jpg) 

- **Nvidia open sources its cuFile APIs and storage stack into a new GitHub organization with Google, Intel, and Meta as founding maintainers, and formally launched Storage-Next with 40-plus flash and storage vendors**
- **Nvidia's key unveiling is its SCADA framework, which moves the storage control path onto the GPU, allowing parallel GPUs to pull data directly from storage**
- **The driver is KV cache economics: inference fetches data in a few hundred bytes at a time, while SSD controllers tuned for 4KB spend the same effort on either size**

Following the recent Future of Memory and Storage conference, Nvidia has argued that the next leap in AI rests as much on the storage feeding accelerated computing as on the silicon doing the computing.

The company open sourced its cuFile APIs and the storage stack beneath them, and formally launched an industry initiative called Storage-Next with more than 40 flash and storage vendors.

It also put a name to SCADA, the framework that lets GPUs pull data from drives without the CPU brokering every request.

## A 512-byte problem that comes into focus as storage becomes key

Nvidia's approach here is not new. cuFile was introduced in 2019 as the interface component of GPUDirect Storage and has shipped since 2021; its role is to take the CPU out of the data path. Bytes move by Direct Memory Access (DMA) straight between the drive and GPU memory, with no bounce buffer in host RAM. What stayed on the CPU was the control path: host software still decided what to fetch and issued every request, with the GPU as the DMA target rather than the initiator.

That split is invisible at large transfer sizes. A one-megabyte read essentially amortizes the per-request cost. At 512 bytes, the ratio inverts, the fixed cost dominates, and the CPU saturates long before the drives do. SCADA is the piece that moves the control path onto the GPU, letting it construct and complete its own storage requests and absorb per-operation latency, just as it already absorbs memory latency by keeping hundreds of thousands of operations in flight. The two are complementary rather than successive: cuFile for bulk transfers, SCADA for high volumes of small random reads.

The problem it solves is one that enterprise SSDs exhibit, having been tuned around 4KB random reads for nearly a decade to match virtualization and databases. As a result, most controllers do the same amount of work to serve 512 bytes of data as they would a 4KB read request.

AI inference access patterns are considerably smaller than that: embeddings run a few hundred bytes, and the KV cache blocks sit well under a kilobyte. Serving them from 4K-tuned drives imposes something like eightfold read amplification, and at tens of terabytes of small objects, that amplification decides whether flash works as a memory tier at all.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The KV cache, essentially the attention state for every token already processed, grows with context length, and agentic deployments run thousands of concurrent conversations. It quickly outgrows GPU memory, and recomputing evicted entries costs more GPU time than reading them back, so the standard design spills from GPU memory to system memory and flash, and refills through high volumes of small random reads.

Serving that from flash rather than DRAM increases the context length and the concurrent user count each GPU can support, which in turn affects the per-user cost of serving a model. This also explains why Nvidia is focusing on 512-byte IOPS rather than raw bandwidth, since inference performance depends heavily on the former.

Opening up cuFile is a departure; this layer has historically lived inside CUDA, and the logic is not charity. A GPU-initiated storage interface only pays off if drive, controller and array vendors build to it, and vendors do not build to a proprietary interface owned by the company whose GPUs they are feeding.

Publishing the interface, open-sourcing the implementation, and convening 40-plus vendors to standardize the underlying hardware behavior is how Nvidia aims to make GPU-initiated storage the industry default. It also stands to benefit the most from that outcome, since it sells most of the GPUs in question.

*StorageReview* notes Intel's participation as a significant development; a leading supplier of the x86 silicon currently sitting in storage controllers has signed on to maintain software designed to remove that silicon from the I/O path. Google and Meta co-maintaining a layer that standardizes how accelerators reach storage, while building their own accelerators, points in the same direction.

Nvidia's take is a coherent, well-argued push at a real bottleneck, with unusually credible partners attached. Partner systems from DDN, Dell, HPE, IBM, VAST Data and WEKA are due in the second half of 2026. Kioxia's XL-Flash drives built for 512-byte access are in development under Storage-Next.

Nvidia's roadmap calls for Gen7 SSDs sustaining 100 million IOPS each, which is a target controller vendors are designing toward rather than a product anyone can buy. Storage-Next itself has been discussed publicly since GTC 2025; this week, it acquired both a membership number and a framework to build against.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: Nvidia unveils custom high-bandwidth memory promising higher bandwidth and
  lower power use - but who will actually get to use it?
source_url: https://www.techradar.com/pro/nvidia-unveils-custom-high-bandwidth-memory-promising-higher-bandwidth-and-lower-power-use-but-who-will-actually-get-to-use-it
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-04T22:20:33Z'
published: '2026-09-04T00:00:00Z'
description: Nvidia just announced custom high-bandwidth memory that almost nobody
  is allowed to buy, and the one named customer has not specified which chip will
  use it
image: https://cdn.mos.cms.futurecdn.net/THrQgcJizbtksGzNr9f3qb-1920-80.jpg
---

![Nvidia Blackwell GPU](https://cdn.mos.cms.futurecdn.net/THrQgcJizbtksGzNr9f3qb.jpg) 

- **Nvidia's NVHBM moves the memory controller off the accelerator die and into the HBM stack's base die, allowing it to claim a potential 30% more bandwidth, 15% lower HBM power, and 25% more compute area versus standard HBM4E**
- **Nvidia's NVHBM performance comparisons are linked to HBM4E, which is still in the sampling stage, with a launch expected sometime in 2027**
- **Access to the custom solution is gated behind NVLink Fusion; Amazon's Annapurna Labs is the only named partner so far and has not said which GPU uses that memory**

On August 26, Nvidia extended its NVLink Fusion program with NVHBM, a custom high-bandwidth memory architecture that the company says delivers up to 30% more memory bandwidth per stack, 15% lower HBM power consumption, and up to 25% more usable area on the accelerator die.

The performance was measured against standard HBM4E samples even as the memory is expected to ship in volume some time in 2027.

Amazon's Annapurna Labs is the first named partner for Nvidia's memory advance which aims to address growing performance limitations for frontier-level AI models centering around limited bandwidth.

## What makes NVHBM tick?

Nvidia's approach doesn't reinvent how memory is handled; it reimagines where it is managed. Conventional HBM approaches split this between two companies: the memory vendor supplies the DRAM stack and its base die, and the accelerator designer puts the memory controller and physical interface on its own compute die.

JEDEC standardizes the connection between the two at the cost of a very wide, comparatively slow parallel bus. NVHBM dissolves the seam altogether by moving Nvidia's memory controller into the base die of the 3D stack, replacing the standard bus with a narrower, serialized die-to-die link that Nvidia designs and memory makers can build.

Nvidia's technical blog puts the resulting reduction in interface and support area at up to 67% against the JEDEC HBM4E standard, even as it improves key power consumption, memory bandwidth, and usable area.

The underlying tech is not completely new, however: Marvell announced the same basic idea in December 2024, naming Micron, Samsung, and SK hynix as collaborators while claiming up to 25% more compute area, 33% greater memory capacity, and a 70% reduction in memory interface power, figures that come close to what Nvidia is currently projecting. Counterpoint Research analyst Neil Shah put it plainly: "The technology is not new. The distribution is."

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Even as HBM4E remains elusive, as it is not in mass production just yet, with Samsung shipping the first HBM4E samples in late May 2026 and SK hynix pulling its own sampling forward to around June, NVHBM is even more elusive. It is a building block gated behind NVLink Fusion, Nvidia's program for connecting third-party accelerators to its rack-scale platform, and access runs through that program's partner list.

Amazon's Annapurna Labs is the first named participant, with Nvidia's blog saying Annapurna will support NVLink Fusion with Trainium4 without explicitly mentioning NVHBM.

For now, NVHBM might be the future, but it may arrive well after HBM4E is already being deployed en masse. Nvidia's own technical blog describes NVHBM as built on the same technology the company will use for future GPUs, without specifying the first generation that would support it natively.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png) 

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

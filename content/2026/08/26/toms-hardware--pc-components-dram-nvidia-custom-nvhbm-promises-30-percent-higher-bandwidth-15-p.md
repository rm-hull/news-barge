---
title: Nvidia custom 'NVHBM' promises 30% higher bandwidth, 15% lower power than commodity
  HBM4e — custom base die and PHY will be available to NVLink Fusion partners
source_url: https://www.tomshardware.com/pc-components/dram/nvidia-custom-nvhbm-promises-30-percent-higher-bandwidth-15-percent-lower-power-than-commodity-hbm4e-custom-base-die-and-phy-will-be-available-to-nvlink-fusion-partners
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-26T23:23:45Z'
published: '2026-08-26T00:00:00Z'
description: Not a replacement for commodity HBM, though.
image: https://cdn.mos.cms.futurecdn.net/TaGTq85mNPD8CGfDe72ByP-1208-80.jpg
---

![An illustrative NVHBM implementation](https://cdn.mos.cms.futurecdn.net/TaGTq85mNPD8CGfDe72ByP.jpg) 

Nvidia's NVLink Fusion program gives the company's partners the building blocks necessary to connect custom chips with the NVLink scale-up domain used to join many separate processors into a single coherent system like the Vera Rubin NVL72 rack-scale accelerator. Today, Nvidia is adding a new building block to that toolkit: NVHBM, a custom implementation of the high-bandwidth memory that underpins practically every AI accelerator in use today.

 ![HBM3E vs HBM4](https://cdn.mos.cms.futurecdn.net/xi79WuWDZXzix4Fc7sXNMn.png) 


As Nvidia describes it, NVHBM is a custom HBM base die that promises higher bandwidth, lower power usage, and a smaller on-die footprint than traditional HBM4e. Nvidia says it's designed and validated with "leading memory vendors," so it promises custom silicon developers faster time-to-market than implementing commodity HBM from the ground up. But it's worth re-emphasizing that this isn't an HBM replacement. Instead, it's a new building block that Nvidia is only offering to its custom silicon partners.

Memory bandwidth is everything for AI accelerators, and NVHBM promises up to 30% higher bandwidth per stack than standard HBM4e. For memory-bandwidth-bound AI workloads, that higher bandwidth translates into higher throughput, such as a higher tokens-per-second rate for AI inference.

The custom NVHBM base die also reduces the footprint of memory-related circuitry on the main custom accelerator die. Traditionally, the HBM memory controller has been incorporated into the primary silicon die on the package. NVHBM instead moves the memory controller into the base die of the HBM stack and provides a smaller custom PHY that NVLink Fusion customers can then integrate into their designs.

 ![NVHBM package area advantage](https://cdn.mos.cms.futurecdn.net/vv9jRtQErFtRUZwFJZPEEU.jpg) 


Nvidia says this approach frees up precious package real estate that can then be used for additional compute die area — up to 30% more compute on the primary silicon die. NVHBM further promises to simplify the interposer routing used to join multiple chips together for designs using advanced packaging techniques.

NVHBM also provides power savings versus off-the-shelf HBM4e stacks. As Nvidia has continuously hammered home in the Vera Rubin roll-out, every watt that isn't going into token production is a watt wasted. Nvidia says NVHBM uses 15% less power than commodity HBM4e, and that power savings can be banked for performance-per-watt improvements, reallocated into more functional units for a custom accelerator design, or translated into higher sustained performance within the same power budget.

Higher bandwidth at lower power is a huge win for AI accelerators that are moving massive data structures like model weights and KV caches around, especially when those savings are multiplied across many thousands of chips. The energy saved on data movement can be plowed back into higher performance from the accelerator itself or reallocated to support larger numbers of accelerators within the same fixed power envelope.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

But these are, as of now, reasons for Nvidia's prospective partners to consider incorporating NVLink Fusion and NVHBM into their custom designs, not benefits that will materialize in the Rubin rack-scale systems already in production.

Along with NVHBM itself, Nvidia announced that Amazon's Annapurna Labs will be its first partner on NVHBM. , and Annapurna VP Nafea Bshara says: “We look forward to this technology collaboration to benefit future AWS infrastructure designs.” Annapurna's next-generation Trainium 4 AI chips will already support the NVLink Fusion scale-up interface, so it seems likely that follow-on chips will support NVHBM, too.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jeffrey Kampman](https://cdn.mos.cms.futurecdn.net/8JCjGs5yVZds2YdKmzjUDE.jpg)

As the Senior Analyst, Graphics at Tom's Hardware, Jeff Kampman covers everything that has to do with graphics cards, gaming performance, and more. From integrated graphics processors to discrete graphics cards to the hyperscale installations powering our AI future, if it's got a GPU in it, Jeff is on it.

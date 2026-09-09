---
title: Nvidia's unreleased RTX 3070 Ti 16GB comes to life thanks to a modder's crazy
  GDDR6 swap — Frankenstein card combines RTX 3070 PCB and new VRAM with RTX 3070
  Ti GPU
source_url: https://www.tomshardware.com/pc-components/gpus/nvidias-unreleased-rtx-3070-ti-16gb-comes-to-life-thanks-to-a-modders-crazy-gddr6-swap-frankenstein-card-combines-rtx-3070-pcb-and-new-vram-with-rtx-3070-ti-gpu
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-09T12:56:44Z'
published: '2026-09-09T00:00:00Z'
description: Doing what Nvidia wouldn't.
image: https://cdn.mos.cms.futurecdn.net/yEM7zXwVHypT7nAhDBVMek-2560-80.png
---

![A VRAM-modded RTX 3070 Ti with 16GB of GDDR6 memory](https://cdn.mos.cms.futurecdn.net/yEM7zXwVHypT7nAhDBVMek.png) 

A few years ago, Nvidia was expected to release the RTX 3070 Ti with as much as 16GB of VRAM instead of the 8GB we actually ended up getting. Only database listings ultimately indicated its existence until a physical prototype showed up, but we never really got to see it working. Fast forward to today, however, and Brazilian YouTuber fmklab, aka Fabian, has recreated the card on his own. Using an RTX 3070 PCB with a transplanted 3070 Ti core and GDDR6 chips from Samsung, fmklab broughall those parts together to achieve a 16GB memory pool.

![Criei a PRIMEIRA RTX 3070 Ti 16 GB GDDR6 do MUNDO? - YouTube](https://img.youtube.com/vi/X3hgaii6FNo/maxresdefault.jpg) 

The card was stripped down to its PCB, and the RTX 3070 GPU was removed and replaced with a 3070 Ti chip. The reason for the swap is that the RTX 3070 uses GDDR6 instead of the GDDR6X the retail version of the RTX 3070 Ti is equipped with, which presented an interesting challenge.

 ![A VRAM-modded RTX 3070 Ti with 16GB of GDDR6 memory](https://cdn.mos.cms.futurecdn.net/fvYnp8oNo735ingoY6tm5m.png) 


Fabian could've put all 16GB of GDDR6X memory on a 3070 Ti card, but it would've been far too expensive, so he swapped the Samsung-made HC14 (8Gb) GDDR6 chips that were already on the board with HC16 (16Gb) chips. That changed the VRAM capacity from 8GB to 16GB, but when the card booted, GPU-Z only recognized 8GB. The PCB's memory straps needed to be reconfigured in order for it to use the entire memory pool.

 ![A VRAM-modded RTX 3070 Ti with 16GB of GDDR6 memory](https://cdn.mos.cms.futurecdn.net/5ukUiH3mbAcJVSbN5HFMzm.png) 


Using the Nvidia BIOS Reader tool, Fabian figured out exactly what straps to adjust and went ahead with the soldering process. Afterward, MATS properly recognized the full 16GB VRAM capacity with no errors. GPU-Z also showed the RTX 3070 Ti equipped with 16GB of GDDR6 memory, similar to the prototype that popped up years ago. But verifying that the card recognized the additional VRAM was just the first step.

To actually test his creation's performance, Fabian ran a local LLM on the GPU to see if it would allocate more than 8GB and found that it used nearly the entire 16GB pool. *Call of Duty: Warzone* ate more than 13GB of VRAM while paired with a Ryzen 7 9800X3D, exhibiting no signs of instability.

Fabian even linked a Unigine Superposition benchmark in the video's description as proof of the card's existence, where he scored 5,367 points, which is actually lower than most real 3070 Ti runs. That's probably because of the decreased memory bandwidth of GDDR6 versus that chip's stock GDDR6X, which is the biggest tradeoff for the higher capacity.

 ![A VRAM-modded RTX 3070 Ti with 16GB of GDDR6 memory](https://cdn.mos.cms.futurecdn.net/Tix85o5yruL97dEya89tdn.png) 


Overall, this was a successful experiment and possibly the only working 3070 Ti 16GB in the world, but there comes a point of diminishing returns. A 3070 Ti is still a powerful card, but it gets smoked by current-gen Blackwell options even with less memory. It would be much more reasonable to buy, say, an RTX 5060 Ti 16GB if you actually need better performance with some future proofing today, not to mention the superior efficiency, feature set, and after-sales support you'd get from a new Blackwell card.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg) 

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

- 
Replyn RTX 5060 Ti 16GB if you actually need better performance with some future proofing today 
 sorry but thats not a futureproofing GPU...
 
 it can barely run many modern games native 60 fps w/o dlss/fg....and that will get worse in future games.
 
60 sku from nvidia has been a 50 sku marked as a 60sku for past 2 gens.

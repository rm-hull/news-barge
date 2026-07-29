---
title: GPU repair service will upgrade the 11GB of VRAM on your RTX 2080 Ti to 22GB
  — mod involves physically adjusting the strap resistors on the PCB to support a
  new BIOS
source_url: https://www.tomshardware.com/pc-components/gpus/gpu-repair-service-will-upgrade-the-11gb-of-vram-on-your-rtx-2080-ti-to-22gb-mod-involves-physically-adjusting-the-strap-resistors-on-the-pcb-to-support-a-new-bios
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-29T14:29:49Z'
published: '2026-07-29T00:00:00Z'
description: Plug-and-play convenience for an advanced mod.
image: https://cdn.mos.cms.futurecdn.net/MmqRv6C4cxpsk7GWCfvm88-1282-80.jpg
---

![GeForce RTX 2080 Ti Founders Edition](https://cdn.mos.cms.futurecdn.net/MmqRv6C4cxpsk7GWCfvm88.jpg) 

Limits on the amount of VRAM on Nvidia's consumer GPUs have forced the modding community to take matters into their own hands. Time and again we've seen various DIY memory upgrades being performed, and it's even offered as a proper repair service in underground markets, but rarely is it done openly. As such, we've just spotted a vendor that will upgrade the 11GB of VRAM on an RTX 2080 Ti to 22GB and provide the BIOS for it upfront — no shady back-alley deals required.

 ![Asus RTX 5080 Noctua Edition](https://cdn.mos.cms.futurecdn.net/Wh9EZgD8NG9yUioNNgPB3d.png) 


The name of the shop is *GPU Solutions*(very creative, we know), and it's based in the UAE, though they say they serve customers around the world. On their website, you can select the "Graphics Card Memory Upgrade" service for both the RTX 2080 Ti and the RTX 3070, though the former has more details. These guys also have a YouTube channel where they've already performed the upgrade on an Asus Strix variant before.

The upgrade works just like any other you might've already seen. The card is disassembled to reach the PCB and remove the preexisting VRAM modules. The RTX 2080 Ti uses 11x 1GB GDDR6 chips, so replacing them with the same amount of 2GB GDDR6 doubles the memory capacity instantly. This is a rather straightforward way of going about a VRAM upgrade, because oftentimes it actually requires a custom PCB.

![Asus RTX 2080 Ti 11GB to 22GB VRAM Upgrade | Memory Replacement Guide - YouTube](https://img.youtube.com/vi/-dWSWDOj6Ag/maxresdefault.jpg) 

Once the hardware part of the job is done, the VBIOS is then manually edited to support the new memory pool. This can either be an easy tweak or a lot of work just to get the BIOS to recognize the card, depending on how that specific GPU was built by the manufacturer. For instance, Nvidia was once said to include 16GB of memory with the RTX 3070, but it ended up shipping with 8GB instead, so customizing the BIOS is as simple as unlocking its full potential.

In this case, there wasn't any software tweaking; the core supports multiple memory configs, so the repairperson physically modified the memory strap resistors on the PCB. The original config for the 11GB modules was set to *low*,* low*,* low*. They desoldered and moved the resistors to a new configuration:* high*,* high*, and* low*, which made the GPU recognize and report 22GB of VRAM inside GPU-Z.

 ![RTX 2080 Ti VRAM upgrade service](https://cdn.mos.cms.futurecdn.net/jaCj5TsSdYUofvZyUAkCnK.png) 


The fact that you get not only double the VRAM on your RTX 2080 Ti but a working, stable BIOS out of the box adds to the overall package significantly. These kinds of mods are usually very hands-on, which means limited to just enthusiasts and tinkerers, but the factory-like service GPU Solution is providing means pretty much anyone can get it done without a hassle.

Their website doesn't mention the charges for an upgrade like this, but considering the ongoing component crisis, the memory modules won't be cheap. They also clarify that the upgrade can only be performed on a card with "compatible PCB layouts." If yours qualifies, they'll also replace the thermal pads and thermal paste accordingly, plus provide substantial benchmarking data to prove the modded card is stable.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Doubling the VRAM should allow you to squeeze a lot more performance out of your 2080 Ti in AI workloads and creative applications such as video editing. It's also helpful in gaming but not to a significant degree since the GPU itself isn't as powerful as modern offerings that are otherwise bottlenecked by memory capacity. Ultimately, this remains a pretty reasonable upgrade because the true, full potential of this GPU was achieved three years ago when someone modded it with an insane 44GB of VRAM.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

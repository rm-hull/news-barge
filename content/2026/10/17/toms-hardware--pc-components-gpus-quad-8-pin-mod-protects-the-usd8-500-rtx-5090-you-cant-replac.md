---
title: Quad 8-pin mod protects the $8,500 RTX 5090 you can’t replace from melting
  — modder’s custom power solution claims to fix Nvidia 16-pin GPU meltdowns
source_url: https://www.tomshardware.com/pc-components/gpus/quad-8-pin-mod-protects-the-usd8-500-rtx-5090-you-cant-replace-from-melting-modders-custom-power-solution-claims-to-fix-nvidia-16-pin-gpu-meltdowns
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-17T20:32:13Z'
published: '2026-10-17T00:00:00Z'
description: RTX 5090 production halts make protecting your GPU from meltdowns critical
image: https://cdn.mos.cms.futurecdn.net/Jb5jmGv4igA8EhyHvpgbcV-2560-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Tom
locations: []
organisations:
- Amazon
- DallasGrave
- Get Tom's Hardware
- Google News
- Nvidia
- PCB
- PCI-SIG
- Reddit
- Redditor
- Tom’s Hardware
---

![GeForce RTX 5090](https://cdn.mos.cms.futurecdn.net/Jb5jmGv4igA8EhyHvpgbcV-1920-80.jpg)

Nvidia’s GeForce RTX 5090, undeniably one of the best graphics cards of our time, vanished overnight without a trace and is now selling for $8,500 on Amazon. In a recent development, Reddit user DallasGrave showcased a custom quad 8-pin power conversion kit designed for the notorious melting 16-pin (12VHPWR) power connector and the later 12V-2x6 revision. This invention, an upgrade over a previous mod, could reduce the risk of power-related meltdowns.

![Asus RTX 5080 Noctua Edition](https://cdn.mos.cms.futurecdn.net/Wh9EZgD8NG9yUioNNgPB3d-1200-80.png)

Unlike the endless stream of aftermarket adapters designed solely to prevent 16-pin power meltdowns, DallasGrave's iteration is more like a power-conversion kit. The direct-mount kit sits above the graphics card and uses a custom harness soldered to the graphics card’s PCB power rails. The quad 8-pin power conversion kit bypasses the 16-pin connection and redistributes the massive power draw more evenly across four conventional 8-pin PCIe power connectors.

Each 8-pin PCIe power connector can deliver up to 150W, so all four combined in this custom configuration match the 16-pin connector’s maximum capacity of 600W. However, this configuration addresses concerns with the 16-pin power connector, which channels 50A through a small, tightly packed set of pins. The power-conversion kit instead spreads the load across four 8-pin PCIe power connectors, which are physically larger and allow a wider pin pitch.

While 8-pin PCIe power connectors are not entirely immune to melting or other power-related failures, such incidents are far less common than issues with 16-pin power connectors. The 16-pin power connector is significantly more compact than a single 8-pin power connector and carries 4X the wattage, so it is more prone to higher current density and heat buildup.

According to PCI-SIG specifications, each of the six power pins inside the 16-pin power connector is rated for a maximum current of 9.5A. This means that, in theory, the power connector's total capacity reaches up to 684W or 57A. For example, 600W (50A) requires each power pin to carry about 8.33A, which is already close to the recommended safety limits.

By contrast, a standard 8-pin PCIe power connector contains three power pins. Combining four of these connectors in tandem provides 12 power pins. When distributing a 50A load across 12 pins, each pin carries just 4.17 amps, about half the current per pin of the 16-pin power connector design. This lower current per pin dramatically reduces wire and terminal temperatures and lowers the risk of heat-related damage.

The quad 8-pin power conversion kit tricks the sense pins on the 16-pin power connection into recognizing the full 600W. However, the Redditor claims they have tested the kit for up to 800W with a shunt mod. The beauty of the kit is that users can use it as a standalone power source or alongside the native 16-pin power connector, essentially acting as a parallel load spreader.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

DallasGrave is developing a custom backplate that will enhance the power conversion kit's visual appeal. Notably, it is not limited to the GeForce RTX 5090 or any specific brand. According to the Redditor, they are preparing a range of models for production that cover nearly every variant on the market, including Nvidia’s Founders Edition. However, the creator has not yet revealed key details such as the official release date, pricing, or installation logistics.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your* * feeds**.*

![Zhiye Liu](https://cdn.mos.cms.futurecdn.net/HhmwL5w9ggUtLCPfqGjTi4-140-80.jpg)

Zhiye Liu is a news editor, memory reviewer, and SSD tester at Tom’s Hardware. Although he loves everything that’s hardware, he has a soft spot for CPUs, GPUs, and RAM.

* I have an idea, let's try a cable standard that has been tried, tested, and true for 10+ years now, and see if that fixes the melting....  
    
  ....Oh wow, imagine that, no melting. Color me shocked :openmouth: Lol  
    
  While we're at it, maybe we can try and diagnose with the 3090Ti never melted, but the 4090 did even though they both have the same power draw and same connector.... hashtag currentbalancing  
    
  I begin to wonder if the melting problem was all a part of the plan the whole time. It wouldn't surprise me tbh Reply
* If you are going to mod – use EPS connector. Two should be enough for the same 600W.  
  PCI-E connector is far from the best: not all wires actually can carry power, different number of power/ground wires. Reply

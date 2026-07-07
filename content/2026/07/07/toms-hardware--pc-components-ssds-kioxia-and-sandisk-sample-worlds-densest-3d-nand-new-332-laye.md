---
title: Kioxia and Sandisk sample world's densest 3D NAND — new 332-Layer beats Samsung’s
  400-Layer NAND
source_url: https://www.tomshardware.com/pc-components/ssds/kioxia-and-sandisk-sample-worlds-densest-3d-nand-new-332-layer-beats-samsungs-400-layer-nand
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-07T11:19:33Z'
published: '2026-07-07T00:00:00Z'
description: Over 29 Gb/mm2 areal density.
image: https://cdn.mos.cms.futurecdn.net/EEMnmsxmaVz4zeSMzUtib3-1600-80.jpg
---

![Kioxia](https://cdn.mos.cms.futurecdn.net/EEMnmsxmaVz4zeSMzUtib3.jpg) 

Kioxia and Sandisk last week said they had started sampling of their latest 3D NAND memory with 332 active layers that features a combination of the industry's leading areal density and performance. The new 10th Generation BiCS 3D TLC NAND is set to address density and performance-sensitive data center applications, as well as promises to surpass Samsung’s latest V10-class 3D NAND in terms of storage density.

Unlike the previous generations, 10th Generation BiCS (BiCS10) is explicitly aimed at data center-grade storage, where bit density and performance are more important than cost. Indeed, the new type of memory features a 332-layer active layer architecture, greater than 29 Gb/mm2 density, and a 4,800 MT/s data transfer rate to enable extreme performance for data center solid-state drives featuring PCIe 5.0 and 6.0 interfaces. Kioxia and Sandisk plan to offer BiCS9 NAND specifically for client applications.

| Header Cell - Column 0 | Kioxia/Sandisk | Kioxia/Sandisk | Samsung | Samsung | Micron | SK hynix | YMTC | YMTC | 
|---|---|---|---|---|---|---|---|---|
| Generation | BiCS 10 | BiCS 8 | V10 | V9 | Gen 9 (G9) | Gen 9 | ? | Xtacking 3.0/Gen 4 | 
| Layers | 332-Layer | 218-Layer | 4xx-Layer | 290-Layer (?) | 276-Layer | 321-Layer | 232-Layer | 232-Layer | 
| Density | >29 Gb/mm^2 | 22.9 Gb mm^2 (?) | 28 Gb mm^2 | 17 Gb mm^2 | 21.0 Gb mm^2 | 20 mm^2 | >20 Gb mm^2 | 19.8 Gb mm^2 | 
| Architecture | TLC | QLC | TLC | TLC | TLC | TLC | TLC | QLC | 
| Die Capacity | 1 Tb | 2 Tb | 1 Tb | 1 Tb | 1 Tb | 1 Tb | 1 Tb | 1 Tb | 
| I/O Speed | Up to 4800 MT/s | Up to 3600 MT/s | Up to 5600 MT/s | Up to 3200 MT/s | Up to 3600 MT/s | ? | ? | ? | 

When we normally describe 3D NAND memory, we usually mention all possible applications, which include high-end consumer SSDs (after all, we are Tom's Hardware, we are hardware enthusiasts!) and data center drives. We did not mention consumer applications for BiCS10 for a very specific reason: Kioxia does not position this generation for client devices and only targets data center-grade drives. Whether or not to expect BiCS10 on a high-performance SSD near you probably depends on supply and demand, given the current market circumstances.

While the BiCS10 332-layer 3D NAND boosts bit density by 59% all the way to over 29 Gb/mm², it also promises to deliver meaningful performance and efficiency gains specifically for enterprise applications. Kioxia claims read latency drops by around 4 microseconds (about 10%), while read energy consumption is reduced by 25%, from roughly 100 mJ/GB to approximately 75 mJ/GB.

According to Kioxia, these improvements stem from a redesigned read scheme that changes how unselected word lines behave during consecutive read operations. In a 332-layer NAND stack, a significant portion of read latency and power consumption is associated with repeatedly charging long word lines from ground (VSS) to the read voltage (VREAD).

Normally, NAND memory discharges its wordlines to ground (VSS) after every read, which is a general-purpose approach that works regardless of what the next operation is. However, there is no need to discharge at all times. Therefore, during continuous read operations, the word lines are not fully discharged in the case of BiCS10. Instead, they are lowered to an intermediate voltage and then raised back to VREAD for the next read, which makes a lot of sense for read-heavy applications (most cloud applications are).

After the initial read, the circuitry reduces the word-line voltage only to an intermediate level instead of completely discharging it to VSS. Before the next access, the voltage is restored to VREAD from that intermediate level rather than from ground. Since the voltage excursion is considerably smaller, the word lines recharge more quickly and require less current, which improves both read latency and energy efficiency. The approach is particularly beneficial for very tall 3D NAND stacks, where long word lines amplify charging delays and power losses during sustained sequential read workloads.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

It is interesting to note that Kioxia and Sandisk plan to manufacture their BiCS9 and BiCS10 3D NAND products at different production sites. The newest Fab 2 facility in Kitakami, Iwate Prefecture, will handle production of the flagship 332-layer BiCS10 memory, while the long-established Yokkaichi complex in Mie Prefecture will continue manufacturing the 218-layer BiCS9 generation.

This manufacturing split makes a lot of sense. Fab 2 is equipped with Kioxia’s most advanced production tools, so it is better suited to manufacture the highest-density NAND from Kioxia and Sandisk. Meanwhile, the mature Yokkaichi fabs are well-suited for client-oriented BiCS9 production. The manufacturing facility has largely been depreciated, which enables the company to manufacture mainstream NAND at lower cost and reserve its newest capacity in Kitakami for leading-edge products.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

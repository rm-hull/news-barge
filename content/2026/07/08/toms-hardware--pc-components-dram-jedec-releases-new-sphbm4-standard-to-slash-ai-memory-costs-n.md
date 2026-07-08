---
title: JEDEC releases new SPHBM4 standard to slash AI memory costs — Narrow 512-bit
  interface enables dropping expensive interposers for organic substrates
source_url: https://www.tomshardware.com/pc-components/dram/jedec-releases-new-sphbm4-standard-to-slash-ai-memory-costs-narrow-512-bit-interface-enables-dropping-expensive-interposers-for-organic-substrates
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-08T17:50:07Z'
published: '2026-07-08T00:00:00Z'
description: Cheaper HBM-class memory.
image: https://cdn.mos.cms.futurecdn.net/vnqdtRupVqWHAik43ZWctH-1920-80.jpg
---

![Micron](https://cdn.mos.cms.futurecdn.net/vnqdtRupVqWHAik43ZWctH.jpg) 

JEDEC has released its new specification that aims to push down the pricing of the ultra-expensive HBM that powers the fastest AI processors. While the new standard will not help relieve the DRAM shortage as it uses large HBM4 DRAM devices, it can make high-bandwidth memory a bit cheaper as it enables attaching SPHBM4 memory stacks without advanced packaging and using inexpensive organic substrates.

The standard's body published the specification of SPHBM4, Standard Package High Bandwidth Memory (JESD330-4), that combines HBM4 DRAM ICs with standard packaging and a fast 'narrow' 512-bit interface. Here are the details.

## HBM4 performance with a 512-bit wide interface

Although 1024-bit and 2048-bit interfaces used by HBM3 and HBM4 memory deliver unbeatable performance, their wide interfaces consume significant silicon area inside processors, they require expensive interposers, and advanced packaging technologies with limited capacity, such as TSMC’s CoWoS, for integration with host processors. The upcoming SPHBM4 memory continues to use the same HBM4 DRAM stacks as JESD270-4, but swaps the conventional HBM base die for a new SPHBM4 PHY/buffer die featuring a narrower 512-bit interface that enables mounting on standard organic substrates without using sophisticated packaging methods for integration. To offset the effect of the narrower interface, SPHBM4 supports considerably higher data transfer rates ranging from 22.4 GT/s to 46.0 GT/s.

Instead of connecting to the host processor using a 2048-bit memory interface like HBM4, SPHBM4 uses 32 independent 16-bit DDR channels organized into eight Quad Channels. Since 'Quad Channel' is a new term, let us explain how things work. Internally, an HBM4 stack contains 32 memory channels, each 64 bits wide, for a total external interface width of 2048 bits. SPHBM4 needs to 'convert' the 2048-bit internal I/O onto a 512-bit external interface, which is why it groups every four HBM4 channels into a Quad Channel. As a result, externally, a Quad Channel exposes 64 data pins (4 × 16 bits), which replace the 256 data pins (4 × 64 bits) that those four HBM4 channels would normally require. To preserve bandwidth, these 64 pins operate at four times the data rate of the original HBM4 interface.

While SPHBM4 dramatically increases I/O bandwidth, it does not make the DRAM array itself faster. The HBM4 memory core retains the same fundamental architecture and timings, including core frequency, row activation, precharge, and refresh operations, though the additional PHY is expected to introduce some latency. For example, the DRAM core runs at only one-quarter of the external interface frequency, which means 2 GHz in the case of SPHBM4 with a 32 GT/s speed bin.

The major change is the new base die, which implements a high-speed SerDes-like PHY that maps each 16-bit external channel to four conventional 64-bit HBM4 channels. As a result, SPHBM4 introduces equalization, lane training, BER requirements, and other high-speed signaling features that are unnecessary in HBM4’s slower, wide parallel interface. To support transfer rates of up to 46.0 GT/s/s per pin, each Quad Channel uses a shared command/address interface protected by forward error correction (FEC), while data transfers rely on dedicated differential write (WCK) and read (RCK) clocks, as well as ECC and error-reporting signals.

When it comes to capacity, SPHBM4 can use stacks containing 4, 8, 12, or 16 DRAM dies featuring 24 Gb or 32 Gb densities, so the largest standardized SPHBM4 configuration is a 64 GB memory stack built from sixteen 32 Gb DRAM dies, identical to the maximum capacity supported by HBM4E.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

## Cheap HBM at last?

The standard supports bump pitches greater than 90 µm and channel reaches up to 20 mm, which are two features that enable dropping the expensive interposer and using less-expensive organic substrate routing. However, getting rid of the interposer and CoWoS (or similar) packaging does not automatically make SPHBM4 inexpensive. SPHBM4 still requires massive HBM4 DRAM ICs, 2.5D packaging, a complex base die (which is likely costlier than the one used by conventional HBM4), and advanced package assembly with through-silicon vias. In addition, SPHBM4's narrow interface consumes significantly less die perimeter and silicon area inside processors, which makes it more attractive to companies that strive to install more compute capability and/or intend to install more memory stacks around their processors. However, we are still talking about a niche high-performance memory technology that will address select applications and will barely rival HBM4 directly.

When it comes to maximum performance, HBM4 moves the data at 8 GT/s (though most controllers and chips support higher data rates), so one HBM4 stack can offer bandwidth of 2 TB/s. HBM4E is set to up data transfer rate to 12 – 12.8 GT/s, therefore increasing peak bandwidth to 3 – 3.3 TB/s per stack. By contrast, one SPHBM4 with a 46 GT/s interface can hit 2.944 TB/s, though do not expect the initial versions of SPHBM4 to hit the maximum speed. Therefore, it is likely that HBM4, HBM4E, and C-HBM4E will maintain a performance lead in terms of bandwidth over SPHBM4 in the foreseeable future.

HBM4 latency will still probably have an edge over SPHBM4. HBM4 essentially connects to its host processor almost directly through a very simple interface. By contrast, SPHBM4 inserts a much more sophisticated PHY that performs serialization/deserialization, lane training, FEC handling, and other operations that can add a few nanoseconds of latency. This may not be a big problem for some applications, but inference benefits a lot from low latencies.

When it comes to power and voltages, HBM4 and SPHBM4 share the same DRAM core voltage because SPHBM4 reuses standard HBM4 DRAM stacks. However, I/O is different: HBM4 leaves the interface voltage up to memory vendors and allows implementations at 0.7V, 0.75V, 0.8V, or 0.9V, depending on the desired balance between power, speed, and signal integrity. By contrast, SPHBM4 standardizes the external I/O at 0.75V.

Also, HBM4 moves data over a very wide interface with many slow parallel links that tend to be very energy efficient. By contrast, SPHBM4 moves the same amount of data through one-quarter as many wires, which run roughly four times faster. High-speed data transfer tends to be less energy efficient than 'slow' data transfers over a wide interface. Keeping in mind SPHBM4's rather sophisticated PHY that converts a wide interface into a narrow interface, which is likely a power-hungry process. Nonetheless, the 4X lower number of drivers and receivers could tangibly reduce the power consumption of SPHBM4. That said, without implementation details from DRAM makers or a processor developer, it is impossible to conclude which memory type has lower power consumption.


Last but not least, SPHBM4 essentially trades manufacturing challenges that arise from using silicon interposers for an engineering challenge of developing an extremely sophisticated base die/PHY. Developing and manufacturing such a base die should not be a problem for foundries. However, it remains to be seen whether DRAM makers can design and produce SPHBM4 with decent power efficiency. After all, both Micron and SK hynix work with TSMC to build C-HBM4E and HBM4E base dies, whereas Samsung's memory division uses base dies produced by Samsung Foundry.

## China factor

One interesting aspect of SPHBM4 is whether Chinese developers of AI accelerators can benefit from this technology. In theory, Chinese developers like Biren, Huawei, Moore Threads, and other blacklisted companies that cannot use TSMC's chip manufacturing or packaging services could become one of the biggest beneficiaries of SPHBM4, perhaps even more so than the U.S.

First up, a smaller shoreline directly benefits chips that are made using trailing nodes, as it enables packing more compute capability into them without sacrificing memory bandwidth or capacity. Secondly, Chinese OSATs currently do not offer CoWoS-like technologies, so eliminating the interposer and using advanced organic substrates is a benefit.

However, SPHBM4 still requires HBM4 DRAM stacks, and today, Samsung, SK hynix, and Micron are the only companies capable of producing them, while China-based CXMT can barely make HBM2E. Furthermore, building a 46 GT/s PHY is very hard and will likely be challenging for Chinese IC developers.

Nonetheless, assembling SPHBM4 packages on organic substrates is arguably more aligned with China's existing manufacturing base, so if local DRAM makers eventually develop competitive HBM4-class memory, SPHBM4 could substantially reduce one of the country's remaining infrastructure gaps.

## Summary

JEDEC's SPHBM4 looks like a promising standard that can potentially address a broader range of applications than HBM4 itself due to lower integration cost. Still, HBM4, HBM4E, and C-HBM4E will maintain performance leadership, which will make them a preferable choice for flagship AI accelerators in the coming years.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

---
title: Intel's new space-grade Starfire chip is a Panther Lake SoC that puts an 18A
  CPU into orbit — chip designed for the US government leverages Intel 3 for the GPU
source_url: https://www.tomshardware.com/tech-industry/semiconductors/intel-shows-off-starfire-space-grade-chip
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-13T18:04:27Z'
published: '2026-07-13T00:00:00Z'
description: The two-SKU part tops out at 75 TOPS.
image: https://cdn.mos.cms.futurecdn.net/KZGW5q9Sg3zZFPPZqNGYh8-1920-80.png
---

![Intel shows off Starfire, a space-grade chip that pairs 18A CPU tiles with an Intel 3 GPU](https://cdn.mos.cms.futurecdn.net/KZGW5q9Sg3zZFPPZqNGYh8.png) 

Intel has unveiled Starfire, a space-grade system-on-chip designed for the U.S. government that pairs eight CPU cores and a three-tile NPU built on its Intel 18A node with an Intel 3 graphics tile, all in one Foveros package. Intel published the Starfire sell sheet, listing two versions that draw 10 W and 35 W and reach up to 45 and 75 TOPS, respectively, rated to run between -55 and 125 Celsius.

Both SKUs share the same layout of four Intel 18A P-cores, four low-power efficiency cores, a three-tile NPU also on 18A, and a four-core Xe GPU with 64 execution units built on Intel 3. The Low Power part runs its P-cores at 1.0 GHz, efficiency cores at 850 MHz, and the GPU between 800 MHz and 1.0 GHz. The Performance part clocks the P-cores to 3.1 GHz, efficiency cores to 2.1 GHz, and the GPU to 2.0 GHz. Both carry 12 PCIe Gen4 lanes, support LPDDR5 or DDR5, and are rated for a 10-plus year lifetime.

Intel builds the CPU and NPU on 18A and the GPU on the older Intel 3, the same node division it used for Clearwater Forest, the 288-core Xeon that stacks 18A compute tiles on Intel 3 base tiles. Smaller transistors hold less charge per stored bit, which makes leading-edge silicon more prone to radiation-induced bit flips, so committing 18A to orbit leans on RibbonFET and design-level hardening rather than a mature, inherently more tolerant node.

The market Starfire is targeting has run on BAE Systems' RAD750 for two decades. That radiation-hardened PowerPC part clocks 110 to 200 MHz, carries 10.4 million transistors, and is built on 150nm or 250nm lithography, per public specifications, and it flies on the Mars rovers, Kepler, and Fermi, among more than 150 spacecraft. BAE's multi-core RAD5545 and the Microchip-built processor NASA is developing to reach 100 times the throughput of current spaceflight chips are the more recent step up. Starfire's up to 75 TOPS and dedicated NPU put it in a different bracket, built for on-orbit AI inference rather than telemetry and control.

Intel lists the radiation data, covering total ionizing dose, single-event latch-up, and single-event effects, as characterization in process, so the part isn't radiation-qualified yet, and it notes the specs are subject to change. Intel Government Technologies is handling Starfire, with samples in Q3 2026 and a pitch of market-competitive pricing and domestic manufacturing. Intel Foundry is the only U.S.-based maker of leading-edge logic, holds Trusted Foundry status, and has tied its 18A and packaging roadmap to Pentagon programs including RAMP-C and SHIP, though 18A yields aren't expected to reach industry-standard levels until 2027.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.

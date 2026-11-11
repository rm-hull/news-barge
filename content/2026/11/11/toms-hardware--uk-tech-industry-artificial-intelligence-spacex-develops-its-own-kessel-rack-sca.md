---
title: SpaceX develops its own ‘Kessel’ rack-scale system featuring 72 Nvidia Rubin
  GPUs for data centers in space, report claims — replaces conventional NVLink cable
  assemblies with a massive 84-layer printed circuit board
source_url: https://www.tomshardware.com/uk/tech-industry/artificial-intelligence/spacex-develops-its-own-kessel-rack-scale-system-featuring-72-nvidia-rubin-gpus-for-data-centers-in-space-report-claims-replaces-conventional-nvlink-cable-assemblies-with-a-massive-84-layer-printed-circuit-board
source_site: Tom's Hardware
source_slug: toms-hardware
description: SpaceX is reportedly developing a 'Kessel' rack-scale system design with
  72 Nvidia Rubin GPUs that relies on a massive 84-layer PCB midplane.
image: https://cdn.mos.cms.futurecdn.net/H9AoDYcDEGHaWVoTNcrLHK-2560-80.png
published: '2026-11-11T00:00:00Z'
scraped_at: '2026-11-11T19:36:21Z'
categories:
- Technology & Software
- Hardware
- Science
people:
- Anton Shilov
- Kessel
- Nvidia Vera Rubin
- Tom
- Vera Rubin
locations: []
organisations:
- AI GPU
- Elon Musk
- Google News
- Kessel
- Nvidia
- PCB
- Rubin GPUs
- SpaceX
- Tom’s Hardware
- xAI
---

![Nvidia Vera Rubin, CES 2026](https://cdn.mos.cms.futurecdn.net/H9AoDYcDEGHaWVoTNcrLHK-1920-80.png)

SpaceX/xAI is developing a custom version of Nvidia's Vera Rubin NVL72 rack-scale AI system that replaces conventional NVLink cable assemblies with a massive 84-layer printed circuit board (PCB), in part for use in orbital data centers, reports SemiAnalysis. The system is codenamed Kessel and retains 36 Vera CPUs, 72 Rubin GPUs, and nine NVLink switch trays, but introduces a different solid-state interconnect architecture. While SpaceX/xAI will continue to buy Nvidia hardware directly from the company, Elon Musk's company will source other components independently, which could give it greater control over its hardware supply chain.

![Asus RTX 5080 Noctua Edition](https://cdn.mos.cms.futurecdn.net/Wh9EZgD8NG9yUioNNgPB3d-1200-80.png)

The Kessel system retains the fundamental configuration of Nvidia's Vera Rubin NVL72 platform, which comprises 72 GPU packages distributed across 18 compute trays and nine NVLink switch trays. However, instead of Nvidia's conventional arrangement with internal NVLink cable cartridges, SpaceX plans to position compute and switch trays back-to-back around a passive PCB midplane. The architecture resembles a smaller version of Nvidia's Kyber design with 576 AI GPUs (albeit in 144 packages), which also relies on a PCB-based interconnect rather than conventional cable assemblies, *SemiAnalysis* notes. Interestingly, the design is aimed at both terrestrial and orbital deployments, according to the analysts.

Arguably the most distinctive feature of Kessel is its 84-layer PCB midplane, which uses ultra-low-loss M10 copper-clad laminates (CCLs). By contrast, Nvidia's Kyber architecture relied on a backplane based on a considerably more complex 156-layer PCB featuring M9 CCLs. The reduction in layer count by nearly half could substantially improve manufacturability and production yields, but the more advanced copper-clad laminate will almost certainly increase material costs. In any case, an 84-layer PCB is a device that is exceptionally hard to build.

The move to a PCB midplane could simplify system assembly by eliminating numerous high-speed cable connections, but it would not necessarily reduce manufacturing costs. An 84-layer PCB that relies on ultra-low-loss M10 laminate is an exceptionally expensive component that requires sophisticated manufacturing processes and precise quality control. To put an 84-layer PCB number into context, modern high-end server motherboards use 15 – 20 layers, whereas server development boards use more than 20 layers to virtually eliminate any electrical issues with the board itself. Furthermore, manufacturing yields of an 84-layer PCB could become a major obstacle, as defects in internal layers may render an entire board unusable. Consequently, the economic viability of Kessel will depend on whether savings from cable elimination and independent component procurement can offset the cost of its complex midplane.

Perhaps more importantly, Kessel represents a departure from Nvidia's conventional system-level procurement model. Instead of purchasing Nvidia's assembled L6 compute boards or even L10 trays that Nvidia plans to sell with its Vera Rubin generation, SpaceX reportedly plans to acquire AI accelerators, CPUs, switches, and networking components directly from Nvidia and procure other components from third-party suppliers (one can wonder how easy it will be for SpaceX/xAI to procure memory amid today's shortages). This would enable SpaceX to select its own PCB manufacturers, component vendors, and manufacturing partners, optimize its hardware for its infrastructure (which will be important for orbital deployments), and perhaps reduce intermediary costs. Meanwhile, the company would assume greater responsibility for system design, validation, manufacturing quality, and supply-chain management, which is something that most hyperscalers have been doing in recent years.

For Nvidia, the implications are less straightforward. Although direct sales of CPU and AI GPU packages could reduce the company's revenue from complete compute-board assemblies, the arrangement could also encourage other large customers to develop their own Nvidia-based systems and eventually deploy more Nvidia-based machines, something that may be important in a world where custom silicon developed by hyperscalers is rapidly gaining traction. However, to make this happen, Kessel must be a smashing success that will offer clear advantages over systems designed by Nvidia.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV-140-80.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

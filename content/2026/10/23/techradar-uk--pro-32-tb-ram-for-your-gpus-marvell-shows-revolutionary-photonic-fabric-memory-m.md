---
title: '32 TB RAM for your GPUs: Marvell shows revolutionary Photonic Fabric Memory
  Module that uses light to link up to 16 GPUs and slash CAPEX — but Nvidia won''t
  stick around doing nothing'
source_url: https://www.techradar.com/pro/32-tb-ram-for-your-gpus-marvell-shows-revolutionary-photonic-fabric-memory-module-that-uses-light-to-link-up-to-16-gpus-and-slash-capex-but-nvidia-wont-stick-around-doing-nothing
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-24T04:29:52Z'
published: '2026-10-23T00:00:00Z'
description: Marvell wants to stop GPUs acting as "the world's most expensive memory
  controller"
image: https://cdn.mos.cms.futurecdn.net/UgtKFmktsVFP6sZJXur5gG-2560-80.jpg
categories:
- Technology & Software
- Film & TV
people:
- Dave Lazovsky
- Jensen Huang
- Marvell
- Ravi Mahatme
- Will Chu
locations:
- AI
- Marvell Campus
- US
organisations:
- Celestial AI
- Coherent
- Custom Cloud Solutions
- Enfabrica
- FMS
- GPU
- HBM
- Hot Interconnects
- Lumentum
- Marvell
- NVLink Fusion
- Nvidia
- Photonic Fabric
- TechRadar Pro
---

![Marvell Campus](https://cdn.mos.cms.futurecdn.net/UgtKFmktsVFP6sZJXur5gG-1920-80.jpg)

* **Marvell reveals Photonic Fabric Memory Module, the building block of a 16-module appliance sharing 32TB of DDR5 and 1,152GB of HBM3e across 16 hosts over fiber**
* **The design dates back to Celestial AI's 2025 presentations, currently remains pre-silicon, and is targeting customer sampling by 2027**
* **Nvidia is already hedging with a $2 billion Marvell stake in addition to its own BlueField-4 STX context memory, Enfabrica's pooling tech, and a co-packaged optics roadmap**

Marvell has put physical hardware behind one of the more ambitious ideas in AI infrastructure.

In a video posted to X, and earlier in a theCUBE interview recorded around its October 6 Investor Day, the company showed off its Photonic Fabric Memory Module, which it bills as the "first optically interconnected high-capacity, high-bandwidth memory."

The pitch is simple: use light instead of copper so that dozens of terabytes of memory can sit in a separate box, racks away, and be shared by many processors at once, something that could effectively birth the widespread use of communal or shared memory across multiple AI servers.

## Two terabytes at a time

Some clarity, however, is warranted: the 32TB figure belongs not to the module but to the Photonic Fabric Memory Appliance, which gangs 16 modules together and shares the pool across up to 16 hosts.

Those hosts can be whole servers or individual accelerators, so 16 GPUs might understate the potential reach in one sense and at the same time, overstate the bandwidth any single GPU will see in another. Nothing is shipping just yet, either: Marvell is targeting customer sampling in 2027.

Each module pairs 72GB of HBM3e with slots for up to eight DDR5 DIMMs, a Photonic Fabric ASIC, and 7.2Tbps of optical I/O, according to Marvell's August 2026 Hot Interconnects presentation.

Hitting 2TB per module means filling all eight slots with 256GB RDIMMs and sixteen modules, joined by a passive all-to-all fiber shuffle rather than an electrical switch, yields 32TB of DDR5 plus 1,152GB of HBM3e, which Marvell rounds to about 1TB and runs as a faster write-through cache in front of the DRAM.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Marvell is going after the economics of today's accelerators. HBM sits roughly 1.5 millimeters from the processor inside the same package, so the only way to buy more of it is to buy more processors. This is increasingly expensive because HBM is extremely costly, and it also means a GPU essentially acts as "the world's most expensive memory controller," as per Dave Lazovsky.

The target workload is the KV cache, the working memory a large language model keeps for each conversation, which balloons with long contexts and agentic sessions. Once it outgrows local HBM and host DRAM, servers either evict it and recompute, or fetch it from much slower storage. This has significant performance implications, and Marvell plans to mitigate it differently.

Ravi Mahatme, who leads product management for the Photonic Fabric unit, said the biggest payoff of a shared tier is "a cross-node KV cache," letting one accelerator reuse context another has already computed. Will Chu, Marvell's EVP of Custom Cloud Solutions, made the broader case in the company's FMS announcement: "As AI scales, memory must scale more independently of compute."

The CAPEX argument is rooted in this: If operators can buy memory separately from accelerators, they no longer need to buy GPUs just to get capacity. This makes sense, but Marvell has yet to put a number to it, even as a May 2026 company blog talks about lower memory cost per gigabyte and lower inference costs without figures, and Celestial AI's 2025 conference slides promised benefits beyond TCO reduction with no supporting numbers.

The timing also isn't ideal for harnessing cheap memory: the approach's 128 DIMM slots draw on the same DDR5 caught up in the current memory crunch, where server RDIMM prices have climbed faster than consumer memory, now around 5.5 times their pre-crisis price in the US.

The appliance design is not entirely new either; Celestial AI presented the same architecture, 16 modules holding 32TB of DDR and about 1TB of HBM, at Hot Interconnects in August 2025, and TechRadar has covered its DDR5-plus-HBM approach back in 2024. What has changed is the Marvell badge, a physical module, and a sampling date.

## Nvidia is already hedging, both as an investor and a pioneer

The idea that Nvidia won't sit idle is more than an assumption, because it has been moving for more than a year, including taking a stake in Marvell itself. In March 2026, Nvidia invested $2 billion in Marvell in a deal covering NVLink Fusion and silicon photonics, with Jensen Huang declaring that "The inference inflection has arrived."

It is also important to understand that every NVLink Fusion platform must include at least one Nvidia product, so Nvidia gets paid even when custom silicon wins the socket, but that doesn't mean it doesn't want a piece of that pie anyway.

It is bringing its own answers to the same memory problem in multiple ways; A single Vera Rubin NVL72 rack carries 54TB of LPDDR5X, more than Marvell's entire appliance.

At Nvidia GTC 2026, the company launched BlueField-4 STX, a flash-based context memory tier built for KV cache, claiming up to five times the token throughput of CPU-based storage, with Huang saying reasoning AI needs "a new class of storage." Partner systems are due in the second half of 2026. Back in 2025, Nvidia reportedly spent more than $900 million on Enfabrica, whose EMFASYS system pooled up to 18TB of memory for GPU clusters.

On optics, Nvidia has put $4 billion into Lumentum and Coherent, unveiled photonics switches at GTC 2025, and will offer co-packaged optics as an NVLink option in Feynman-generation systems due in 2028. On the choice between copper and optical scale-up, Huang has said: "We're going to do both."

Marvell still has a long way to go: working silicon, a named customer, a memory partner, and measured throughput on real hardware rather than simulated curves all need to play out exactly as planned.

Until then, the appliance is a well-argued blueprint, and the CAPEX savings remain an argument rather than a number. The irony is hard to miss: the company whose GPUs Lazovsky casts as the world's priciest memory controller owns a $2 billion slice of Marvell, and through NVLink Fusion, stands to earn on the racks either way.

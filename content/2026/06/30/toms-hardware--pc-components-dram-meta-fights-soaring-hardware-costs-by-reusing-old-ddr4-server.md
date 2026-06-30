---
title: Meta fights soaring hardware costs by reusing old DDR4 server memory in new
  DDR5-only servers — custom CXL 2.0 chip marries legacy DDR4-2400 with cutting-edge
  DDR5-6400
source_url: https://www.tomshardware.com/pc-components/dram/meta-fights-soaring-hardware-costs-by-reusing-old-ddr4-server-memory-in-new-ddr5-only-servers-custom-cxl-2-0-chip-marries-legacy-ddr4-2400-with-cutting-edge-ddr5-6400
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-06-30T14:40:53Z'
published: '2026-06-30T00:00:00Z'
description: CXL memory expanders give new life to DDR4 memory.
image: https://cdn.mos.cms.futurecdn.net/Q3NJwvq4G77cCgLH8yDqyb-1920-80.png
---

![72 32GB HPE DDR4-2666 ECC RDIMMs](https://cdn.mos.cms.futurecdn.net/Q3NJwvq4G77cCgLH8yDqyb.png) 

The price of DDR5 memory is setting new highs these days as demand badly outstrips supply. In a bid to save money, Meta is recovering legacy DDR4 memory from used servers and is installing it into new machines using its in-house developed Vistara ASIC that enables it to connect old memory modules to its latest servers running AMD EPYC 'Turin' processors that only support DDR5 memory.

Interestingly, Meta is not the only company developing such a solution. Panmnesia, a startup from South Korea, has developed an off-the-shelf CXL controller and switch that enables servers to attach considerably larger memory pools without extending latency, which differentiates Panmnesia’s solution from competing CXL offerings.

## Custom ASIC enables DDR4 memory to work with new servers

Vistara is Meta’s first-gen custom CXL memory expander ASIC designed to attach outdated DDR4 memory to modern servers. The chip implements a CXL 2.0 Type-3 memory expander over a PCIe 5.0 x16 interface and bridges standard DDR4 RDIMMs to host processors. Each ASIC supports two independent 72-bit DDR4 memory channels and can provide up to 256 GB of capacity using 64 GB DIMMs. At present, Meta deploys 128 GB per ASIC using 32 GB DDR4 modules recovered from decommissioned servers.

 ![Meta](https://cdn.mos.cms.futurecdn.net/ApDXyg7GGYX5G4nDXEVpUg.png) 


Meta deploys Vistara in its MemServer platform, where two ASICs connect to a single 158-core AMD Turin processor over PCIe 5.0 x8 links. Each server combines 768 GB of DDR5-6400 local memory with 256 GB of CXL-attached DDR4-2400, which expands memory capacity to 1 TB. The software stack transparently exposes CXL memory as a separate NUMA node and enables Linux to migrate cold pages to the slower DDR4 tier (with 76 GB/s of bandwidth) and retain frequently accessed data in local DDR5 (with 614 GB/s of bandwidth).

 ![Meta](https://cdn.mos.cms.futurecdn.net/6sJrEcDcy3Z6h2tMA5p4Vg.png) 


The ASIC is based on three RISC-V processor cores for secure boot, device initialization, firmware management, and health monitoring. Meta claims it has optimized its CXL controller and memory pipeline to reduce protocol overhead, minimize queuing delays, and lower idle round-trip latency to around 50ns. The chip also incorporates advanced reliability features, including Reed-Solomon two-symbol error correction and x4 chip-kill support.

 ![Meta](https://cdn.mos.cms.futurecdn.net/FtyXGeB3FnwTutMtxU6PTg.png) 


## Not only Meta's Vistara

Meta is not the only company that wants to attach legacy DDR4 memory to newer servers that rely on DDR5 memory and save some money. While Vistara is available exclusively to Meta, there is a new CXL expander solution from Panmnesia that will be available to other companies.

"There has been a perception that putting a switch between the CPU and devices makes it hard to meet the memory-access latency these systems expect, so directly attached multi-headed devices (MHDs) stayed the norm even though they were harder to scale," said Myoungsoo Jung, chief executive of Panmnesia. "Our work shows this is not an inherent limit of CXL or CXL switches — it is a trait of early-stage CXL, and one that fades as the standard and the products around it mature. With a fabric switch that carries our next-stage CXL controller, scalability, low latency, and stable performance can come together."

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

CXL is a protocol that sits on top of the PCIe physical interface. As a result of this, many early CXL implementations were built by modifying existing PCIe IP, which is why such implementations inherited architectural characteristics optimized for PCIe rather than for memory-semantic communications, which added substantial latency, according to Panmnesia. By contrast, its new CXL controller IP features a redesigned data path that replaces separate per-layer buffers with shared buffers to eliminate much of the synchronization overhead. In addition, it features additional latency optimizations throughout the protocol stack that offset the additional hop introduced by the switch.

The accompanying CXL fabric switch introduces Port-Based Routing (PBR), which removes the tree-topology limitations of conventional Hierarchy-Based Routing (HBR) used by PCIe and early CXL implementations. The fabric switch still supports both PBR and HBR to enable flexible system topologies, optimized traffic routing, and stable performance. In practice, it enables companies like Meta to install more DDR4 memory into their modern servers without major performance degradation because of high latency.

Panmnesia claims that while early CXL deployments could connect only a handful of compute nodes to shared memory pools, its fabric scales to up to 64 nodes, which means greater flexibility for hyperscalers that tend to run thousands of servers, but which now have to rationalize usage of expensive DRAM.

Panmnesia says its next-generation CXL technologies are progressing toward commercialization. The company has pre-release silicon for its PCIe 6.4/CXL 3.2 Fusion Switch and has completed development of its PCIe 7.0/CXL 4.0 Combo IP, which supports the latest features introduced by the CXL 4.0 specification.

  


*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

- 
Reply
 No, this is a true memory expansion. It does not appear to the system as a drive (NVMe or otherwise).edzieba said:Somehow, RAMdisk returned.
 
 That said, the approach of relying on page migration does presume certain access patterns and requires the direct-attached memory to be large enough to hold the working set (i.e. if you want to achieve good efficiency). I think those are very achievable hurdles.
 
 The article said:The software stack transparently exposes CXL memory as a separate NUMA node and enables Linux to migrate cold pages to the slower DDR4 tier (with 76 GB/s of bandwidth) and retain frequently accessed data in local DDR5 (with 614 GB/s of bandwidth).
 Back in the bad old days of DOS, there were memory-expander cards that I think worked in a fashion that more resembles VGA video memory addressing.
 [https://en.wikipedia.org/wiki/Expanded_memory#Expansion_boards](https://en.wikipedia.org/wiki/Expanded_memory#Expansion_boards)
 Here's an example:
 [https://www.ebay.com/itm/307031071607](https://www.ebay.com/itm/307031071607)

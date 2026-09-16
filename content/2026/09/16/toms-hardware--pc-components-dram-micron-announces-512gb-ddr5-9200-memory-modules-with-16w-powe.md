---
title: Micron announces 512GB DDR5-9200 memory modules with 16W power draw — up to
  12TB per server, claims 60% less energy-intensive than four 128GB modules
source_url: https://www.tomshardware.com/pc-components/dram/micron-announces-512gb-ddr5-9200-memory-modules-with-16w-power-draw-up-to-12tb-per-server-claims-60-percent-less-energy-intensive-than-four-128gb-modules
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-16T19:32:57Z'
published: '2026-09-16T00:00:00Z'
description: Already tested by AMD and Intel, but supply will depend on demand.
image: https://cdn.mos.cms.futurecdn.net/piUuHtgGMF6aJLG24RchXg-1280-80.png
---

![Micron](https://cdn.mos.cms.futurecdn.net/piUuHtgGMF6aJLG24RchXg.png) 

Micron this week introduced its first 512GB DDR5-9200 memory module that is designed for servers used for applications that demand a lot of memory. The new modules — which are currently being validated by AMD and Intel with their next-generation server platforms — will enable server makers to build machines with up to 12TB of fast memory. What remains to be seen is the price of such modules and servers.

 ![HBM3E vs HBM4](https://cdn.mos.cms.futurecdn.net/xi79WuWDZXzix4Fc7sXNMn.png) 


To build its 512GB DDR5 RDIMM, Micron uses advanced packaging that stacks multiple DRAM dies vertically and connects them using through-silicon vias (TSVs). The company does not disclose which memory devices and how many of them it uses, but claims that a single 512GB RDIMM consumes over 60% less operating power than four 128GB modules — based on 16.0W for one 512GB module compared with the 44.2W total for four 128GB modules — which suggests that we are dealing with fairly advanced ICs.

Micron's 512GB module is not the industry's first 512GB DDR5 RDIMM — that achievement belongs to Samsung — but it is certainly the industry's first 512GB module certified to operate with a 9200 MT/s data transfer rate with standard 1.1V voltage (which implies on usage of Micron's 16Gb DDR5-9200 devices made on its 1γ (1-gamma) fabrication process that uses EUV lithography and consumes 20% less power than predecessors, though we are speculating).

Truth to be told, 512GB DDR5 memory modules are rather niche products, which is perhaps why Samsung's 512GB RDIMMs formally introduced in 2021 have not become widespread even after AMD and Intel introduced processors with over 100 cores. Micron positions its 512GB DDR5 RDIMM primarily for servers running analytics, in-memory databases, simulations, virtualization, agentic AI, and other workloads demanding high-core-count processors and plenty of memory. As processors with 200 or more cores emerge, 512GB modules may become more relevant as 12TB of memory in a server running two 256-core CPUs means 24GB per core, which no longer looks particularly excessive for applications like in-memory databases, analytics, or caching.

Micron claims that in memory-constrained Spark Support Vector Machine (SVM) analytics workloads, systems featuring 512GB memory modules can provide up to 1.4 times the performance of configurations equipped with 256GB DDR5 modules, though the company does not disclose how much memory in total these systems use. Micron also says the higher-capacity memory can increase throughput and concurrency for memory-intensive database and caching applications such as RocksDB and Redis.

AMD and Intel are working with Micron to qualify the new modules for their upcoming server platforms. Micron plans to begin volume production of its 512GB DDR5 RDIMMs sometime in the second half of 2027 and intends to align the schedule with customer requirements.

One of the more pressing questions about Micron's 512GB DDR5-9200 memory modules is their price. A 256GB DDR5-6400 RDIMM currently retails for around $19,000. Given the unique proposition that 512GB modules have for memory-constrained applications, such modules can cost significantly more than 256GB memory sticks, which will not help their broad adoption.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png) 

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

- 
Reply
 Wow, who even uses SVMs, any more? Neural networks started outperforming them likeThe article said:Micron claims that in memory-constrained Spark Support Vector Machine (SVM) analytics workloads*entire decades* ago, and you don't even need a very big or costly ones to do it.
 
 BTW, I always find it interesting to look at the ratio of system memory capacity to bandwidth. Essentially, it tells you how many seconds it takes to actually read or write all of that memory. I have a theory that, when it exceeds a certain point, the performance benefit of adding more RAM vs. swapping to fast SSDs loses to the cost-savings of the SSDs.
 
The transition point should vary by application, but I expect that even in-memory databases struggle to justify more RAM, beyond a certain point. At the high end of the curve, you end up in mainframe territory, because you need lots of uptime just to fill the RAM, let alone actually get the benefits of reading it vs. NAND.

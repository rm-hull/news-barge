---
title: AMD’s 256-core Epyc 9996 ‘Venice’ claims up to a 3.4x jump over Intel Xeon
  competition, 20% over Nvidia Vera – Zen 6 comes with up to 1024MB of L3, 16-channel
  memory, and 5GHz+ clock speeds
source_url: https://www.tomshardware.com/pc-components/cpus/amds-256-core-epyc-9996-venice-claims-up-to-a-3-4x-jump-over-intel-xeon-competition-20-percent-over-nvidia-vera-zen-6-comes-with-up-to-1024mb-of-l3-16-channel-memory-and-5ghz-clock-speeds
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-23T17:42:42Z'
published: '2026-07-23T00:00:00Z'
description: That’s a big chip.
image: https://cdn.mos.cms.futurecdn.net/fqE7uiQeMahN3tCxTd8qRV-1999-80.jpg
---

![AMD Venice](https://cdn.mos.cms.futurecdn.net/fqE7uiQeMahN3tCxTd8qRV.jpg) 

AMD is finally providing some details on its first Zen 6 CPU, which it has been teasing for over a year. The Epyc 9996 is a 256-core / 512-thread chip, packing AMD’s new Zen 6 architecture, and it’s the first to launch in what AMD describes as a “broad portfolio” for Venice. In addition to claiming significant performance advantages over the impending Nvidia Vera and Intel’s Xeon 6, AMD says it will continue to build out the Venice range with bespoke designs over the next year.

“It’s not just a single processor,” said AMD’s Ravi Kuppuswany, corporate VP of compute and enterprise solutions.q “It’s a portfolio.” AMD says it has purpose-built solutions, splitting its offerings depending on the application, not dissimilar to how Intel has split its Xeon ranges over the past few generations (nor how AMD has softly segmented its Epyc offerings). The roadmap starts with the main Venice lineup on the SP7 socket, which is what AMD has been teasing for so long. It scales up to 256 cores and 512 threads, 1.6 TB/s of memory bandwidth with fast MRDIMMs, and 128 PCIe 6 lanes in 1P configuration (160 lanes in 2P).

![AMD Venice](https://cdn.mos.cms.futurecdn.net/XCGh2YjJn47yiVU448a63M-1200-80.jpg) 

![AMD Venice](https://cdn.mos.cms.futurecdn.net/6dsfSPhYZJCmdUanzSJayL-1200-80.jpg) 

![AMD Venice](https://cdn.mos.cms.futurecdn.net/2kfRCSFRkRW4PTSRjj8u2M-1200-80.jpg) 

![AMD Venice](https://cdn.mos.cms.futurecdn.net/9Z7WN7gu89jYF5jJntzkzL-1200-80.jpg) 

![AMD Venice](https://cdn.mos.cms.futurecdn.net/XCGh2YjJn47yiVU448a63M-1280-80.jpg) 

![AMD Venice](https://cdn.mos.cms.futurecdn.net/6dsfSPhYZJCmdUanzSJayL-1280-80.jpg) 

![AMD Venice](https://cdn.mos.cms.futurecdn.net/2kfRCSFRkRW4PTSRjj8u2M-1280-80.jpg) 

![AMD Venice](https://cdn.mos.cms.futurecdn.net/9Z7WN7gu89jYF5jJntzkzL-1280-80.jpg) 

**Note:** When scaling up to 256 cores, AMD uses its Zen 6c “dense” design. With a standard Zen 6 design, AMD says Venice scales up to 128 cores and 256 threads, while high-frequency variations top out at 96 cores.

In the first half of next year, AMD plans to launch Venice on its SP8 socket, offering as few as eight cores and up to 128, focused on smaller deployments. These chips support eight-channel memory with two DIMMs per channel, and the same 128 PCIe 6 lanes.

Venice-X is expected in the second half of 2027, on the SP7 socket. We didn’t see Turin-X, but the last, last-gen Genoa-X came with 96 cores and up to 1152 MB of stacked L3 cache. Those specs haven’t changed (short of the Zen 6 microarchitecture), but AMD says it's able to clock Venice-X up to 5.15 GHz.

Finally, Verano should arrive in the second half of next year on the SP8 socket, and it looks like the most direct competitor to Vera (AMD’s Kuppuswamy had some fun with calling it “Vera-No”). It’s optimized to be an AI host node, says AMD, packing up to 72 cores and 5 GHz peak clocks. Critically, it comes with a 24-channel LPDDR5X memory system, leveraging SOCAMM2 modules.

 ![AMD Venice](https://cdn.mos.cms.futurecdn.net/BYCGbv4Zs5iPj2MFostnUV.jpg) 


One of the advantages __Nvidia claims with its Vera chip__ is lots of memory bandwidth through the LPDDR5X system. AMD’s approach is different with Venice SP7. It’s scaling up to 16-channel memory with Venice SP7, with support for MRDIMMs running at 12,800 MT/s, or standard DDR5 RDIMMs running at 8000 MT/s.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

It’s a significant jump over Turin, which uses 12-channel memory, with support for RDIMMs running at 6400 MT/s. AMD claims per-socket bandwidth of 1.6 TB/s, significantly higher than the 1.2 TB/s available on Vera, and nearly triple the 576 GB/s per-socket bandwidth of Turin. Intel recently enabled 8000 MT/s RDIMMs on select Granite Rapids and Clearwater Forest SKUs, and it says support for MRDIMMs with speeds up to 8800 MT/s is coming in Q1 2027.

AMD didn’t provide a list of SKUs or detailed specs for Venice. We really only know about the Epyc 9996, the dense 256-core design, and even then there are a lot of holes. We learned a few critical details about Venice more broadly, however, confirming previous rumors and reports.

Zen 6 is built on TSMC’s N2 (this has been previously confirmed). AMD confirmed that there are 32 cores on a CCD, along with two IODs. Keep in mind that the 32-core CCD is using Zen 6c, not full Zen 6. There has been plenty of speculation about 32-core CCDs in consumer Zen 6 CPUs, but that seems unlikely.

The 256-core configuration comes with a massive 1,024 MB of L3, nearly triple the amount of the Epyc 9965. This isn’t stacked cache, either; that will come with Venice-X. Each CCD has access to 128 MB or L3, or 4 MB per core, double what was available on Turin.

Although AMD has focused a lot of its teases on the 256-core Venice, the initial SP7 offerings will also hold a 96-core, high-frequency model that can clock up to 5 GHz.

## AMD shares first 256-core Epyc ‘Venice’ benchmarks

![Venice AAI Performance](https://cdn.mos.cms.futurecdn.net/AW7WBmW58kD97YYY8VMvPQ-1200-80.jpg) 

![Venice AAI Performance](https://cdn.mos.cms.futurecdn.net/nCY9XHWEL9gPeTwB7vJQMQ-1200-80.jpg) 

![Venice AAI Performance](https://cdn.mos.cms.futurecdn.net/ftBc8o6LGnks4Dkk27vfPQ-1200-80.jpg) 

![Venice AAI Performance](https://cdn.mos.cms.futurecdn.net/poh7h38fDAmEDUG6nH3ZPQ-1200-80.jpg) 

![Venice AAI Performance](https://cdn.mos.cms.futurecdn.net/rc7Ctucd2M9YpQicYYo8PQ-1200-80.jpg) 

![Venice AAI Performance](https://cdn.mos.cms.futurecdn.net/HrxH4bgxxiRKHDyS9Ta8NQ-1200-80.jpg) 

![Venice AAI Performance](https://cdn.mos.cms.futurecdn.net/AW7WBmW58kD97YYY8VMvPQ-1280-80.jpg) 

![Venice AAI Performance](https://cdn.mos.cms.futurecdn.net/nCY9XHWEL9gPeTwB7vJQMQ-1280-80.jpg) 

![Venice AAI Performance](https://cdn.mos.cms.futurecdn.net/ftBc8o6LGnks4Dkk27vfPQ-1280-80.jpg) 

![Venice AAI Performance](https://cdn.mos.cms.futurecdn.net/poh7h38fDAmEDUG6nH3ZPQ-1280-80.jpg) 

![Venice AAI Performance](https://cdn.mos.cms.futurecdn.net/rc7Ctucd2M9YpQicYYo8PQ-1280-80.jpg) 

![Venice AAI Performance](https://cdn.mos.cms.futurecdn.net/HrxH4bgxxiRKHDyS9Ta8NQ-1280-80.jpg) 

Unlike the __extrapolated performance AMD shared__ a few weeks back, we have some concrete benchmarks for the Epyc 9996 now. AMD has, unsurprisingly, focused the workloads around agentic AI. However, many of the workloads applicable for agentic AI are applicable elsewhere, as well, including high-concurrency networking tasks, code compilation, and media processing.

Note that AMD includes just the Epyc 9965 as a gen-on-gen comparison point in the charts above. This is a “dense” Zen 5 design with 192 cores. Results for the 128-core 9755 are included in the tables below.

Starting with front-end operations, AMD claims a 1.2x gen-on-gen improvement and a 2.8x improvement compared to Intel Xeon 6980P, with an NGINX web server using the WRK load generator. Unlike most of these competitive performance figures, AMD included the actual numbers for the benchmarks it ran in the footnotes, which you can see in the table below.

| 
 | 
 | 
| Intel Xeon 6980P | 10,162,179 | 
| AWS Graviton5 | 15,331,108 | 
| AMD Epyc 9755 | 17,906,196 | 
| AMD Epyc 9965 | 24,320,476 | 
| AMD Epyc 9996 | 28,789,170 | 

In data-heavy workloads that are common among AI agents, AMD claims a 1.7x improvement over Turn, and a massive 3.4x over the Xeon 6980P. AMD used the __TPCx-AI benchmark__ to gather these results. The primary metric for this test is AI use cases per minute (AIUCpm), for which AMD shared the median result2. If you’re interested in more about the reporting of this benchmark, __Dell has published an extensive breakdown__.

| 
 | 
 | 
| Intel Xeon 6980P | 1,750.36 | 
| AWS Graviton5 | 2,444.8 | 
| AMD Epyc 9755 | 2,704.19 | 
| AMD Epyc 9965 | 3,458.79 | 
| AMD Epyc 9996 | 5,982.91 | 

In vectorized workloads, AMD claims a 1.6x gen-on-gen improvement and 2.3x improvement compared to the Xeon 6980P. For this test, AMD used Meta’s open-source FAISS (Facebook AI Similarity Search) library to search for similar vectors in the siftm1 dataset. The metric here is QPS, or queries processed per second, looking at overall query throughput.

| 
 | 
 | 
| Intel Xeon 6980P | 316,069 | 
| AWS Graviton5 | 119,179 | 
| AMD Epyc 9755 | 369,252 | 
| AMD Epyc 9965 | 472,079 | 
| AMD Epyc 9996 | 751,453 | 

For its “enterprise tools” benchmarks, AMD ran several tests, including TPC-H, TPC-C, and Redis, and it reports the results as “geomean throughput.” We have actual numbers here, but they’re a geomean representing several different tests rather than a single benchmark. Broadly, however, AMD claims a 1.6x gen-on-gen improvement in these workloads, and a 2.6x improvement compared to Intel.

| 
 | 
 | 
| Intel Xeon 6980P | 2,284,701 | 
| AWS Graviton5 | 2,982,203 | 
| AMD Epyc 9755 | 2,546,290 | 
| AMD Epyc 9965 | 3,867,149 | 
| AMD Epyc 9996 | 6,054,748 | 

A lot of agentic workloads are applicable outside of agents, but AMD also tested a few agents directly. It replayed five different agent personas across the chips and, once again, gathered a throughput geomean. We don’t have the metrics here, nor for the previous benchmark, so it’s possible there’s an angle of performance that we’re not seeing with the data provided by AMD.

Regardless, the company claims a 1.5x gen-on-gen improvement in this test, and a 2.5x improvement compared to the 6980P.

| 
 | 
 | 
| Intel Xeon 6980P | 1.779 | 
| AWS Graviton5 | 2.505 | 
| AMD Epyc 9755 | 2.317 | 
| AMD Epyc 9965 | 2.97 | 
| AMD Epyc 9996 | 4.451 | 

AMD ran these tests earlier in the month. But just a few days ago, Nvidia published its __first SPEC CPU 2026 results for Vera__. AMD ran some tests of its own using the same compiler for a comparison between Vera and Venice. AMD’s Kuppuswamy says, “everything is apples-to-apples comparison, same compiler.” That’s GNU 15.2, if you’re curious.

 ![AMD Venice](https://cdn.mos.cms.futurecdn.net/Nd9udWC5rPBo6kVkbVyGrV.jpg) 


In throughput, AMD claims a 2.2x improvement in the SPECrate integer suite, compared to Vera using the dense Venice design with 256 Zen 6c cores. More importantly, AMD claims a 1.2x improvement in per-core performance when comparing Vera to a 96-core “High Frequency” Venice chip. AMD says it used Nvidia’s results as the basis for comparison. With both Venice designs, AMD used a 600W TDP.

 ![AMD Venice](https://cdn.mos.cms.futurecdn.net/VbVU6ByWdAB22L3gVxyXTV.jpg) 


In SPEC CPU 2017 (again using SPECrate with integer workloads), AMD has data comparing Venice to Intel’s 6980P and __Arm’s new AGI__, showing 2x throughput compared to Intel, and 1.3x per-core performance. Note the core counts here for AMD. SPECrate is a throughput test, and AMD stepping down to a 128-core model suggests that performance will likely drop off as the core count increases.

![Venice legacy workloads](https://cdn.mos.cms.futurecdn.net/FtipThANHsMS5km9WXnn2Z-1200-80.jpg) 

![Venice legacy workloads](https://cdn.mos.cms.futurecdn.net/2itPBFKNyskKzLzfDXX8yY-1200-80.jpg) 

![Venice legacy workloads](https://cdn.mos.cms.futurecdn.net/FtipThANHsMS5km9WXnn2Z-1280-80.jpg) 

![Venice legacy workloads](https://cdn.mos.cms.futurecdn.net/2itPBFKNyskKzLzfDXX8yY-1280-80.jpg) 

Although AMD wants to focus Venice performance on agentic workloads, it shared a range of what are now being called “legacy” workloads across the cloud and HPC. Some of the results are repeated from the earlier slides, such as Redis and NGINX, but there are some additional data points, including NAMD and SQL. The performance improvements here are large, though not surprising. You can see that across these tests, even Turin beats the competition from Intel and AWS.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

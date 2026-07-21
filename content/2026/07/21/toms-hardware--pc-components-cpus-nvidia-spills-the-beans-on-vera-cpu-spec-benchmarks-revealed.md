---
title: Nvidia deep dives Vera CPU for AI data centers — SPEC CPU 2026 benchmarks revealed,
  Olympus architecture specifics, and more
source_url: https://www.tomshardware.com/pc-components/cpus/nvidia-spills-the-beans-on-vera-cpu-spec-benchmarks-revealed-olympus-architecture-detailed-and-more
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-21T17:40:26Z'
published: '2026-07-21T00:00:00Z'
description: Setting the stage for a Vera / Venice showdown.
image: https://cdn.mos.cms.futurecdn.net/tAXNckhbwBFZknaHqvpJe7-1920-80.jpg
---

![Nvidia Vera CPU](https://cdn.mos.cms.futurecdn.net/tAXNckhbwBFZknaHqvpJe7.jpg) 

Nvidia’s Vera CPU is its first bid to become a key player in the data center CPU market. Although Grace has seen some success (most notably with Grace standalone deployments at Meta), Vera is Nvidia’s first CPU with a custom core design. It’s arriving at an ideal time, as well, with the server CPU market exploding in the last few months on the back of agentic AI demand.

Vera isn’t a chip built to chip away at the market share of AMD and Intel in the cloud. It’s built to grab market share in an expanding market, as hyperscalers look to widen AI infrastructure beyond legacy clouds. As such, it’s designed in a much different way than Nvidia’s x86 competitors, and it even holds some unique architectural design points compared to the swath of Arm-based designs.

Nvidia has slowly revealed more details about Vera as it ramps into general availability, which is on track for the back half of this year. Now, we have a full picture of the chip. Nvidia shared its Vera white paper, along with unofficial SPEC CPU 2026 results comparing Vera to AMD’s Turin-based Epyc 9755.

We’re going to break down the white paper here, including all of the details about the Olympus core and a look at the benchmarks Nvidia ran. At the end of this piece, we’ll also take a brief look at the larger context of Vera and how it fits into Nvidia’s wider AI ecosystem compared to standalone deployments.

But plenty of ink has been spilled about Vera’s technical capabilities and Nvidia’s next-gen AI infrastructure vision. Let’s start with the important thing: the benchmarks.

## Nvidia Vera CPU benchmarks

We’ve seen Vera in action before, though only through a series of __selected benchmarks ran at Nvidia HQ by Phoronix__. In the Vera white paper, Nvidia shared benchmarks for SPEC CPU 2026, specifically the integer suite from SPECrate, against AMD’s Epyc 9755, with both chips running in a dual-socket configuration. Before getting into the results, there are some important notes about how SPEC runs work, and the reporting criteria for them.

Nvidia’s run here isn’t official, as Vera was tested in a reference system due to the fact that it’s not broadly available yet. It’s ramping for general availability in the second half of the year. Due to that, Nvidia is unable to report its results. That’s why you see “estimated” in some of the charts below. Nvidia ran SPEC CPU 2026; it’s not extrapolating expected performance __like we’ve seen from AMD so far__ with its upcoming Venice chips.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

SPEC CPU 2026 is split into four suites, but Nvidia tested the SPECrate integer suite, which is focused on system throughput with integer-based workloads. The “rate” result is looking at how much work is completed within a certain amount of time. Here, each thread in the system has a copy of the workload. The score is how much time it takes for those workloads to complete, regardless of thread count, naturally giving chips with more cores an advantage.

If you want more detail on the benchmarks included in the suite, make sure to read our __original coverage of SPEC CPU 2026__. Here are the overall results:

| 
 | 
 | 
 | 
| 706.stockfish_r | 324 | 1370 | 
| 707.ntest_r | 251 | 830 | 
| 708.sqlite_r | 250 | 744 | 
| 710.omnetpp_r | 203 | 842 | 
| 714.cpython_r | 136 | 1240 | 
| 721.gcc_r | 296 | 817 | 
| 723.llvm_r | 196 | 909 | 
| 727.cppcheck_r | 142 | 890 | 
| 729.abc_r | 196 | 823 | 
| 734.vpr_r | 199 | 815 | 
| 735.gem5_r | 131 | 1300 | 
| 750.sealcrypto_r | 231 | 816 | 
| 753.ns3_r | 129 | 1670 | 
| 777.zstd_r | 469 | 483 | 
| 
 | Row 15 - Cell 1 | 
 | 

Nvidia didn’t share the exact results for the 9755 it tested, short of the overall score of 898. Taking that overall score into account, Vera is 3% ahead of the 9755. It’s worth noting that Vera is ahead here despite a large thread disadvantage. An overall score of 898 for a dual-socket Epyc 9755 system isn’t unreasonable compared to publicly-submitted SPEC CPU 2026 runs, though higher results have been published. SPEC CPU ships as source code, which the tester must compile with their compiler of choice, and that can heavily influence results (particularly with vendor-specific compilers). Nvidia used GNU 15.2 with both systems.

 ![Nvidia Vera CPU](https://cdn.mos.cms.futurecdn.net/rcRrMvi7TMFtUaXGwYUCh7.jpg) 


Above, you can see Vera’s results stacked up against the 9755, but these aren’t comparing the numbers directly. Nvidia has normalized the per-core performance, which isn’t how SPECrate results are normally shared. According to the overall numbers, Vera is still completing more work within the same amount of time, despite a thread disadvantage, but the margins aren’t in the range of a 70% or 80% advantage as the above chart suggests.

We asked Nvidia about the results given that they're obfuscated by comparison; we could not reverse-engineer the Epyc 9755's scores with the information Nvidia has provided. Here's the response it gave: "Per-core performance under a fully loaded socket is important because agentic AI and RL run many sandboxes concurrently, while each agent step remains sequential and latency-sensitive. It measures how much performance each core sustains amid contention for shared power, memory, cache, and fabric. We therefore normalize by physical core, with SMT enabled on both systems."

The “agentic” workloads Nvidia has highlighted here are code compilation and interpretation workloads, which is something an agent is often doing, querying repos for dependencies and building source code. Below are data science workloads (or Exploratory Data Analysis), and below that are data processing workloads like SQLite database management. The results here align with Nvidia’s overall messaging of Vera, that it’s highly competent at data-rich, backend operations.

Although Nvidia is sharing per-thread results, it argues that SPECrate is still the correct benchmark to run. The per-thread results here are in the context of a fully-loaded socket. Here’s the justification from the white paper: “This metric is non-trivial for agentic AI and RL systems, where many sandboxes, tools, and environments run concurrently rather than as isolated single-thread tests. Fully loaded per-core performance captures how well each core sustains throughput while sharing socket-level power, memory bandwidth, cache, and fabric resources.”

![Nvidia Vera IPC](https://cdn.mos.cms.futurecdn.net/bKCCSdCPe95huZbfp52aJg-757-80.jpg) 

![Nvidia Vera IPC](https://cdn.mos.cms.futurecdn.net/3hAZpX73UiAwdrs3FVGaKg-783-80.jpg) 

![Nvidia Vera IPC](https://cdn.mos.cms.futurecdn.net/vwLjX9HBTd9MTG5S9iKjKg-792-80.jpg) 

![Nvidia Vera IPC](https://cdn.mos.cms.futurecdn.net/z6gDePRf8RhWf36G9woiKg-793-80.jpg) 

![Nvidia Vera IPC](https://cdn.mos.cms.futurecdn.net/H2sAzWoGEJF2SZDPyKjFLg-787-80.jpg) 

![Nvidia Vera IPC](https://cdn.mos.cms.futurecdn.net/bKCCSdCPe95huZbfp52aJg-757-80.jpg) 

![Nvidia Vera IPC](https://cdn.mos.cms.futurecdn.net/3hAZpX73UiAwdrs3FVGaKg-783-80.jpg) 

![Nvidia Vera IPC](https://cdn.mos.cms.futurecdn.net/vwLjX9HBTd9MTG5S9iKjKg-792-80.jpg) 

![Nvidia Vera IPC](https://cdn.mos.cms.futurecdn.net/z6gDePRf8RhWf36G9woiKg-793-80.jpg) 

![Nvidia Vera IPC](https://cdn.mos.cms.futurecdn.net/H2sAzWoGEJF2SZDPyKjFLg-787-80.jpg) 

In addition to running the workloads, Nvidia analyzed the code execution for architectural benchmarks, which you can see in the gallery above. Nvidia claims an overall IPC gain of up to 1.9x compared to Turin, up to 2.3x more branch predictions and 3.5x taken branches per cycle, and up to 2.4x higher instruction fetch operations per cycle.

![Nvidia Vera Pagerank](https://cdn.mos.cms.futurecdn.net/ZqwYuSuHpqxBT8v7PdznGE-737-80.jpg) 

![Nvidia Vera Pagerank](https://cdn.mos.cms.futurecdn.net/L6RuUKxf65J6gPiEv9WcHE-787-80.jpg) 

![Nvidia Vera Pagerank](https://cdn.mos.cms.futurecdn.net/ZqwYuSuHpqxBT8v7PdznGE-737-80.jpg) 

![Nvidia Vera Pagerank](https://cdn.mos.cms.futurecdn.net/L6RuUKxf65J6gPiEv9WcHE-787-80.jpg) 

Outside of SPEC, Nvidia shared a few benchmarks highlighting the capabilities of the Olympus core. First up is PageRank, an algorithm developed by Google to originally rank web pages, which highlights Olympus’ prefetch engine. Nvidia scaled this workload to higher core counts, showing Vera maintaining much of its single-core performance up to 32 cores, while the Turin chip hits a wall around 20 cores.

In addition to the above results, Nvidia shared some tests of the Vera memory system compared to Turin. These microbenchmarks are good for validating Nvidia’s specifications, but they’re looking at architectural performance, not application performance. An architectural advantage translates into a performance advantage, but not always in a linear, expected fashion.

Nvidia used internally-developed tools for the memory tests, though they're available on GitHub for anyone to run.

 ![Nvidia Vera CPU](https://cdn.mos.cms.futurecdn.net/94LUPccLfy8TKEx2QvBMF7.jpg) 


First is loaded memory latency, stressing the memory subsystem as bandwidth usage increases. Vera has much higher bandwidth overall, but you can see the Turin chip hit a latency wall below its maximum, which Nvidia attributes to Non-Uniform Memory Access (NUMA) domain traversal and CCD-to-CCD latency.

 ![Nvidia Vera CPU](https://cdn.mos.cms.futurecdn.net/TtkR22Fu7Fi3BJjRpT6hC7.jpg) 


Looking at per-core bandwidth, Nvidia claims Vera provides more than four times the bandwidth of AMD’s 9755. The suggestion here is that “real-world” per-core bandwidth is even better than Nvidia’s specs lead on (or perhaps worse than AMD’s).

 ![Nvidia Vera CPU](https://cdn.mos.cms.futurecdn.net/9N3K4rNCtv822nwhUz4j48.jpg) 


Maybe the most consequential of these tests is the one you can see above, looking at core-to-core latency. It’s no secret that crossing the CCD on AMD’s chiplet-based architecture incurs a big latency penalty. You can see that in action even in our __Ryzen 9 9950X3D2 review__, and the penalties compound as you scale up the number of CCDs.

In fairness to AMD here, chiplet-based designs aren’t built for this type of cross-CCD traversal, preferring to keep workloads localized and optimizing for core density. Vera’s design goal is clearly to keep latencies consistent across the entire die and sacrificing core density in the process. Nvidia’s Ian Buck told us that this design trade-off “will come at the cost of the legacy workload,” when we recently visited Nvidia HQ.

That’s important context. Nvidia isn’t gunning to steal existing market share from AMD and Intel as much as it’s trying to grab market share in an expanding market before AMD and Intel can. Some financial institutions (including Morgan Stanley and Bank of America) suggest the server CPU market could double in size (or grow even larger) by 2030. That context is important because there will be a continuing demand for CPUs that can handle workloads Vera is not optimized for, and it’ll be interesting to see how AMD and Intel tackle that dynamic with future products, trying to keep a legacy base of customers while pushing ahead into the expanded market.

Nvidia clearly has a vision of how that expanded market looks, and to that end, hasn’t shared SPEC CPU floating point results. Presumably, this is due to the fact that SPEC’s vectorized suite is focused primarily on HPC workloads, whereas Nvidia focused on what it believes are critical agentic workloads that are integer-based. Vera has a vector engine complete with SVE, but that doesn’t seem like Nvidia’s focus.

In an end-to-end Nvidia system, those vectorized workloads would be offloaded to a Rubin GPU. Still, we don’t have any vector results for Vera yet. Up to this point, we’ve only seen integer results, which is strange given the memory system at play in Vera.

Current page: Nvidia Vera CPU

Next Page Nvidia Vera CPU architecture -— A closer look at the Olympus core![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

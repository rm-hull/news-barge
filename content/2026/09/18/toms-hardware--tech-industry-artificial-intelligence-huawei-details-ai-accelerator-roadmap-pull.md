---
title: Huawei details AI accelerator roadmap, pulls in next-generation Ascend NPUs
  by several quarters — FP4 performance of the Ascend 960PR doubles expectations
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-details-ai-accelerator-roadmap-pulls-in-next-generation-ascend-npus-by-quarters-fp4-performance-of-the-ascend-960pr-doubles-expectations
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-18T13:00:47Z'
published: '2026-09-18T00:00:00Z'
description: Huawei accelerates AI roadmap.
image: https://cdn.mos.cms.futurecdn.net/GgPdYEHgr4MXhF4VFT3HtR-2560-80.png
categories:
- Technology & Software
- Hardware
locations: []
people:
- Anton Shilov
- David Wang
- Tom
organisations:
- Ascend
- Board
- Chinese AI
- Get Tom's Hardware
- Google News
- Huawei
- NPU
- Nvidia
- Peerium
- Rotating
- SuperPod
- Tom’s Hardware
- UnifiedBus
---

![Huawei Ascend](https://cdn.mos.cms.futurecdn.net/GgPdYEHgr4MXhF4VFT3HtR.png) 

Huawei has updated its AI hardware roadmap by adding new accelerators and supporting processors and pulling in next-generation Ascend 960 accelerators at its annual Huawei Connect event. Specifically, the company accelerated its Ascend 960 roadmap, disclosed Ascend 970 and 980 specifications, introduced its Peerium architecture based on the UnifiedBus, and expanded its vertically integrated AI infrastructure portfolio.

Huawei is currently in the middle of transitioning from its SIMD architectures that it has used for almost a decade with its Ascend accelerators (or neural processing units, how the company prefers to call them) to its all-new SIMD+SIMT architectures that bring together vector-based processing and thread-level parallelism to improve hardware utilization and performance across a variety of AI workloads (SIMD for data parallel operations and SIMT for branch-heavy workloads).

 ![Huawei Ascend AI chip](https://cdn.mos.cms.futurecdn.net/ANu9aBzADbe49opeKu4gnP.jpg) 


The first Ascend NPUs to adopt Huawei's new architecture are Ascend 950PR for prefill and recommendation, as well as Ascend 950DT for decoding and training. Huawei said at the event that its Ascend 950 platform is gaining traction as the Atlas 950 SuperPoD systems are already in large-scale commercial use, though it did not elaborate. The company said tests of its training-oriented Ascend 950DT have produced 'good results' and expects numerous Chinese AI developers to begin training models on 950DT-based systems next year. Meanwhile, Huawei acknowledged that its production capacity remains insufficient to satisfy domestic demand.

Indeed, in September 2025, Huawei announced the maximum Atlas 950 SuperPoD configuration as 2,048 Kungpeng 950 CPUs, 8,192 Ascend 950DT NPUs, 160 cabinets (128 compute + 32 communications), 8 FP8 EFLOPS, 16 FP4 EFLOPS, and 16 PB/s of aggregate interconnect bandwidth. However, in July 2026 Huawei publicly showed a real Atlas 950 SuperPoD implementation with 256 CPUs as well as 1,024 accelerator cards, which is well below the maximum configuration. While the company still describes the architecture as scaling up to 8,192 NPUs, it is not listed on its website, so we can only wonder which systems are now in large-scale commercial use.

For now, the adoption of the Atlas 950 SuperPod does not seem to be proceeding rapidly, perhaps because of insufficient supply, or maybe because of the all-new architecture that requires major redesign of software. In any case, the Atlas 950 SuperPod will in many ways be a pipecleaner for the company to clear the road for more capable Ascend 960-series accelerators and their successors.

Speaking of the Ascend 960, this family will start with the Ascend 960DT in Q1 2027, when it is set to be formally available, three quarters earlier than previously planned.

 ![Huawei Ascend](https://cdn.mos.cms.futurecdn.net/GgPdYEHgr4MXhF4VFT3HtR.png) 


The Ascend 960DT accelerator is expected to deliver 2 FP8 PFLOPS and 4 FP4 PFLOPS, carries 288 GB of presumably HiZQ memory with 9.6 TB/s bandwidth, and features a 2.2-TB/s interconnect.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The Ascend 960PR NPU follows in Q3 2027, one quarter earlier than originally planned, with 2 FP8 PFLOPS for training, but 8 FP4 PFLOPS for inference (2X higher than Huawei announced last year). The unit carries 192 GB of memory providing 2.4 TB/s of bandwidth and retains the 2.2-TB/s interconnect. For comparison: Nvidia's VR200 GPU due in Q4 2026 can deliver 35 NVFP4 PFLOPS for training and 50 NVFP4 PFLOPS for inference while carrying 288 GB of HBM4 memory.

"We are evolving our Ascend chip series on a one-generation-a-year cycle," said David Wang, the Deputy Chairman of the Board and Rotating Chairman at Huawei, in his keynote. "In 2028 and 2029, we will roll out the Ascend 970 and 980 chips, respectively. Thanks to the Tau (τ) Scaling Law, not only will their compute specifications continue to double, but you can also expect to see huge improvements across the board in terms of memory bandwidth, memory capacity, interconnect bandwidth, and more."

| Huawei Ascend roadmap |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|
| **NPU**|** Targeted Release**|** Architecture**|** FP8 Performance**|** FP4 Perf**|** Memory**|** Memory Bandwidth**|** Interconnect Bandwidth**|** Supported Formats**  | 
| Ascend 910C | 2025 Q1 | SIMD | – | – | 128 GB | 3.2 TB/s | 784 GB/s | FP32, HF32, FP16, BF16, INT8 | 
| Ascend 950PR | 2026 Q1 | SIMD + SIMT | 1 PFLOPS | 2 PFLOPS | 128 GB of HiBL 1.0 | 1.6 TB/s | 2.0 TB/s | FP32, HF32, FP16, BF16, FP8, MXFP8, HiF8, MXFP4 | 
| Ascend 950DT | 2026 Q4 | SIMD + SIMT | 1 PFLOPS | 2 PFLOPS | 144 GB of HiZQ 2.0 | 4.0 TB/s | 2.0 TB/s | FP32, HF32, FP16, BF16, FP8, MXFP8, HiF8, MXFP4 | 
| Ascend 960DT | 2027 Q1 | SIMD + SIMT | 2 PFLOPS | 4 PFLOPS | 288 GB | 9.6 TB/s | 2.2 TB/s | FP32, HF32, FP16, BF16, FP8, MXFP8, HiF8, MXFP4, HiF4 | 
| Ascend 960PR | 2027 Q3 | SIMD + SIMT | 2 PFLOPS | 8 PFLOPS | 192 GB | 2.4 TB/s | 2.2 TB/s | FP32, HF32, FP16, BF16, FP8, MXFP8, HiF8, MXFP4, HiF4 | 
| Ascend 970 | 2028 | SIMD + SIMT | 3.6 PFLOPS | 14 PFLOPS | 288 GB | 14.4 TB/s | 4.4 TB/s | FP32, HF32, FP16, BF16, FP8, MXFP8, HiF8, MXFP4, HiF4 | 
| Ascend 980 | 2029 | SIMD + SIMT | 7.2 PFLOPS*| 28 PFLOPS* | 384 GB | 38.4 TB/s*| 8 TB/s* | FP32, HF32, FP16, BF16, FP8, MXFP8, HiF8, MXFP4, HiF4* | 

Starting with the Ascend 960-series and onwards, Huawei plans to maintain a one-generation-per-year cadence for its AI accelerators. Pulling in the Ascend 960DT by several quarters is, without any doubt, a remarkable achievement. However, what is even more extraordinary is that Huawei has managed to increase FP4 performance of the Ascend 960PR by two times compared to original expectations, which likely means that the company has substantially reworked the processor's low-precision compute capabilities rather than merely adjusted its memory subsystem or clock speeds. In fact, four-fold higher FP4 performance compared to FP8 is set to be a distinctive feature of Ascend 970 and 980.

The Ascend 970 is due in 2028 with 3.6 FP8 PFLOPS, 14 FP4 PFLOPS, 288 GB of memory providing 14.4 TB/s, and 4.4 TB/s of interconnect bandwidth. Ascend 980 follows in 2029 with 7.2 FP8 PFLOPS and 28 FP4 PFLOPS, along with 384 GB of memory reaching 38.4 TB/s and an 8-TB/s interconnect. Huawei marks the Ascend 980 figures as preliminary.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png) 

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

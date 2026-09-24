---
title: Huawei shelves global AI chip rollout as China's own demand outstrips supply
  — 15,488-chip Atlas clusters leverage optical networking to counter Nvidia, scales
  to 120 EFLOPS
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-shelves-global-ai-chip-rollout-as-chinas-own-demand-outstrips-supply-15-488-chip-atlas-clusters-leverage-optical-networking-to-counter-nvidia-scales-to-120-eflops
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-21T20:26:13Z'
published: '2026-09-21T00:00:00Z'
description: AMD and Nvidia no longer have to worry.
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
- Science
image: https://cdn.mos.cms.futurecdn.net/ANu9aBzADbe49opeKu4gnP-1786-80.jpg
locations:
- China
people:
- Anton Shilov
- Eric Xu
- Tom
organisations:
- AMD
- CANN
- Get Tom's Hardware
- Google News
- Huawei Connect
- NPO
- NPUs
- Nvidia AI
- Reuters
- SMIC
- SuperClusters
- Tom’s Hardware
---

![Huawei Ascend AI chip](https://cdn.mos.cms.futurecdn.net/ANu9aBzADbe49opeKu4gnP.jpg)

Huawei's impressive next-generation Ascend 900-series AI accelerators will be offered only in China, not internationally, as the company struggles to meet domestic demand amid capacity constraints, the company announced this week. While the upcoming Ascend 960-series neural processing units (NPUs) could rival some of AMD's and Nvidia's existing AI GPUs, demand for these units outside of China was not guaranteed anyway.

![Nvidia](https://cdn.mos.cms.futurecdn.net/z53fPgXjpKHTpeGv3RHpqj.png)

"Since we do not have enough capacity to even satisfy the ​demand in China, we do not have a plan to expand into the international market in a fully-fledged way," said Eric Xu, rotating chairman of Huawei, on the sidelines of the company's Huawei Connect conference, Reuters reports. He added that Huawei supplies limited volumes to 'some countries where demand is particularly strong,' though he did not elaborate.

Huawei this week unveiled its latest AI accelerator roadmap, revealing major training and inference performance gains for its next-generation Ascend 960, 970, and 980 NPUs over the existing Ascend 910C and Ascend 950-series. The Ascend 960DT and 960PR are set to increase their FP8 training performance to 2 PFLOPS and their FP4 inference performance to 4 PFLOPS and 8 PFLOPS, respectively, in 2027. Meanwhile, their successors, Ascend 970 and Ascend 980, are projected to increase their FP4 performance to 14 PFLOPS and 28 PFLOPS, respectively, in the coming years.

## Huawei Ascend vs Nvidia AI GPUs

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **NPU**|** FP8 Performance**|** FP4 Perf**|** Memory**|** Memory Bandwidth**|** Interconnect Bandwidth**|** Targeted Release** |
| Nvidia H200 | 4 PFLOPS | - | 141 GB HBM3E | 4.8 TB/s | 900 GB/s | 2023 Q4 |
| Nvidia B300 | 10 PFLOPS | 15/20 S/D PFLOPS | 279 GB HBM3E | 8 TB/s | 1.8 TB/s | 2025 Q4 |
| Ascend 950PR | 1 PFLOPS | 2 PFLOPS | 128 GB of HiBL 1.0 | 1.6 TB/s | 2 TB/s | 2026 Q1 |
| Ascend 950DT | 1 PFLOPS | 2 PFLOPS | 144 GB of HiZQ 2.0 | 4.0 TB/s | 2 TB/s | 2026 Q4 |
| Nvidia R200 | 17.5 PFLOPS | 35/50 T/I PFLOPS | 288 GB HBM4 | 19.2 TB/s | 3 TB/s | 2026 Q4 |
| Ascend 960DT | 2 PFLOPS | 4 PFLOPS | 288 GB | 9.6 TB/s | 2.2 TB/s | 2027 Q1 |
| Ascend 960PR | 2 PFLOPS | 8 PFLOPS | 192 GB | 2.4 TB/s | 2.2 TB/s | 2027 Q3 |
| Ascend 970 | 3.6 PFLOPS | 14 PFLOPS | 288 GB | 14.4 TB/s | 4.4 TB/s | 2028 |
| Ascend 980 | 7.2 PFLOPS\*| 28 PFLOPS\* | 384 GB | 38.4 TB/s\* | 8 TB/s | 2029 |

\*Preliminary data  
S/D - Sparse and Dense  
T/I - Training and Inference

But while the upcoming Ascend NPUs will be considerably faster than their predecessors, particularly for inference, they will remain well behind Nvidia's previous- and current-generation accelerators, at least in raw compute performance. Huawei's 2027 Ascend 960DT is projected to deliver 2 FP8 TFLOPS for training, compared with Nvidia's 4 FP8 TFLOPS for the H200, released in 2023. The Ascend 960PR is expected to offer 8 FP4 PFLOPS for training, which is far behind Nvidia's B300, which delivers 15–20 NVFP4 PFLOPS. Even the Ascend 980, targeted for 2029, is projected to reach 7.2 FP8 PFLOPS and 28 FP4 PFLOPS, well below Nvidia's R200, which is on track to deliver 17.5 FP8 PFLOPS and 35/50 FP4 PFLOPS this year.

Such a massive performance difference with leading AI hardware will reinforce Huawei's reliance on massive system-level scaling rather than chip-for-chip performance to compete with Nvidia. But massive system-level scaling comes with massive power consumption, which will make Huawei's next-generation Atlas SuperPoDs and SuperClusters considerably less competitive in markets that can access hardware from AMD or Nvidia.

Huawei is in an interesting paradoxical situation. On the one hand, its integration efforts like near-package optics (NPO) clearly free up capacity on 'older' nodes that can be used for other components of AI platforms. But on the other hand, SMIC's inability to ramp production on 7nm and 6nm-class nodes limits Huawei's ability to supply its AI hardware anyway, which is why it can barely meet demand.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Then again, while Huawei's Atlas SuperPoDs with up to 15,488 Ascend 960 NPUs can deliver up to 30 FP8 EFLOPS and 120 FP4 EFLOPS performance by far exceeding the capabilities of Nvidia's NVL72 clusters with a 72-GPU scale-up world size, their performance-per-watt is poised to be dramatically lower compared to Nvidia's architectures, which means that demand for such hardware outside of China will be limited at best. That said, a global AI hardware push doesn't make much sense for Huawei right now. What perhaps does make sense is offering cloud access to its hardware to various academic and research customers to popularize its CANN software stack.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

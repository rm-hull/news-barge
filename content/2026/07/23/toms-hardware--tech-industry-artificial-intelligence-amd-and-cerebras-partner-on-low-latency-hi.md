---
title: AMD and Cerebras partner on low-latency, high-throughput AI inference — EPYC
  processors in Helios rack-scale infrastructure paired with Cerebras' Wafer-Scale
  Engine (WSE) solutions
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-and-cerebras-partner-on-low-latency-high-throughput-ai-inference-epyc-processors-in-helios-rack-scale-infrastructure-paired-with-cerebras-wafer-scale-engine-wse-solutions
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-23T21:07:25Z'
published: '2026-07-23T00:00:00Z'
description: Like Groq, but different.
image: https://cdn.mos.cms.futurecdn.net/QDGHobTS56GF94GsXHu2PV-2500-80.jpg
---

![Cerebras Andromeda](https://cdn.mos.cms.futurecdn.net/QDGHobTS56GF94GsXHu2PV.jpg) 

AMD and Cerebras Systems on Thursday announced plans to develop a platform that would combine AMD's EPYC processors in Helios rack-scale infrastructure with Cerebras' Wafer-Scale Engine (WSE) solutions. Together, the new systems promise to combine low latency of AMD's CPUs and Instinct GPUs with high throughput of Cerebras's Wafer Scale Engines (WSE) processors.

AMD and Cerebras expect the new inter-rack-scale platform — based on AMD Helios rack with EPYC CPUs and Instinct MI400-series accelerators inside — to be responsible for prompt processing and large context windows, whereas Cerebras' WSE will take care of the memory-bandwidth-intensive token-generation stage.

AMD and Cerebras expect their disaggregated inference platform to deliver up to 5X higher tokens per second per watt (T/s/W) by assigning different portions of an inference workload to architectures optimized for them. Therefore, AMD Helios provides rack-scale compute capacity and large volumes of complex requests, whereas the Cerebras WSE handles latency-sensitive token generation. The two compute platforms will operate within a single inference workflow, although the companies have not disclosed additional performance data or explained how the systems will be interconnected.

The underlying idea of the AMD + Cerebras platform is essentially the same as Nvidia's CPX concept, but AMD and Cerebras assign the specialized hardware to the opposite inference stage.

Nvidia's disaggregated design separates inference into context/prefill and generation/decode. The cancelled Rubin CPX GPU with GDDR7 was optimized specifically for the compute-heavy context/prefill stage, while the regular HBM-equipped Rubin GPUs handle the memory-bandwidth-bound generation stage.

By contrast, the AMD and Cerebras platform follows the same disaggregation principle, but the specialization is inverted: AMD's Helios platform with Instinct GPUs handles the prefill stage and processes prompts and large context windows, while the Cerebras WSE takes over the decode stage and handles latency-sensitive token generation.

Cerebras plans to install AMD Helios systems in its own data centers and integrate them with its WSE racks. The combined offering is scheduled to become available initially through Cerebras Cloud in the second half of 2026, according to the two companies.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

- 
ReplyCerebras plans to install AMD Helios systems in its own data centers and integrate them with its WSE racks. The combined offering is scheduled to become available initially through Cerebras Cloud in the second half of 2026, according to the two companies. They couldn't find enough customers willing to buy Wafer Scale Engines, eh? I think Cerebras might crash and burn. Impressive technology though.

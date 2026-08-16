---
title: Google reportedly taps AMD to design next-generation TPU — hybrid AI ASIC could
  integrate on-package CPU cores for reinforcement learning
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reportedly-taps-amd-to-design-next-generation-tpu-hybrid-ai-asic-could-integrate-on-package-cpu-cores-for-reinforcement-learning
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-16T12:57:15Z'
published: '2026-08-16T00:00:00Z'
description: A custom TPU for agentic and RL workloads?
image: https://cdn.mos.cms.futurecdn.net/9yjpJGx28XVepArU3M5vBD-2144-80.jpg
---

![Google](https://cdn.mos.cms.futurecdn.net/9yjpJGx28XVepArU3M5vBD.jpg) 

Google has teamed up with AMD to develop one of its 10th-generation TPUs, according to a note by SemiAnalysis (via Sean). Analysts at SemiAnalysis believe Google may be interested in AMD's CPU cores for CPU-heavy workloads. If accurate, the collaboration would mark AMD's first major involvement in a custom AI ASIC project and could indicate that Google is exploring a new kind of TPU that combines its proprietary accelerator technology with on-board general-purpose cores for CPU-heavy workloads.

 ![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB.jpg) 


"Market chatter suggests [Google] is working with AMD on a TPU project in the v10 generation," a SemiAnalysis note for clients cited by Sean reads. "AMD's involvement would be the first real involvement in a custom AI ASIC project, despite having a custom silicon team. AMD has strong IP, especially in advanced packaging and SoIC. Additionally, CPU IP could also be a draw given Google and its customers are pushing for TPUs with on-package CPU cores for RL workloads."

Having developed nine generations of its proprietary AI accelerators (with Broadcom acting as actual silicon designer) and possessing extensive expertise in accelerator architecture, Google hardly needs AMD to design a conventional TPU. Hence, chances that AMD will implement Google's TPU v10i for inference or V10t for training are low. Hence, Google might need something only a CPU maker like AMD could provide, including CPU IP, programmable logic, interconnects, or certain advanced packaging know-how.

Of these, the CPU angle is particularly noteworthy. SemiAnalysis claims that Google and its customers are pushing for TPUs with on-package CPU cores for reinforcement learning and potentially other CPU-heavy workloads. While conventional LLM training remains overwhelmingly accelerator-heavy, reinforcement learning for reasoning and agentic models can require considerably more general-purpose compute around accelerator operations.

Google has already begun to increase CPU resources around its latest inference-oriented TPUs. Its TPU 8i systems, designed for inference, reasoning, and RL workloads, feature one Google Axion CPU for every two TPUs. By contrast, servers running Google's 7th Generation TPUs used one Xeon 'Emerald Rapid' processor for every four TPUs. Furthermore, we are hearing that in some cases a 1:1 ratio of CPUs to accelerators is optimal, so the future of AI may be way more CPU-heavy than we think.

Meanwhile, bringing CPU cores directly into the TPU package could be a logical next step, as reducing the distance between general-purpose and tensor compute can improve performance and reduce power consumption. This is where AMD comes into play, as it already has experience developing a data center-grade design — the Instinct MI300A — that packs both x86 and accelerator chiplets. A hypothetical Google design could therefore combine Google-developed TPU compute chiplets with AMD CPU and HBM in a tightly integrated package built by AMD. Perhaps, Intel would appear as another potential candidate given that Google and Intel have multiple strategic collaborations. Yet Intel has no experience building hybrid x86+accelerator data center designs.

Note that for now we are speculating and our analysis may be inaccurate. For now, the nature of AMD's alleged involvement remains unclear. Yet, if the report is indeed accurate, the important development may not be that AMD is helping Google build another TPU. Instead, what matters is that Google is considering a new CPU-heavy member of its TPU v10 family, optimized specifically for RL and agentic workloads, and is using AMD as a provider of some of the building blocks needed to create it.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

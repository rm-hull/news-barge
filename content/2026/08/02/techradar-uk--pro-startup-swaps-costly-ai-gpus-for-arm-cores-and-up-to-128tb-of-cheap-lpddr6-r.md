---
title: Israeli startup takes direct aim at Nvidia with Arm-powered AI server
source_url: https://www.techradar.com/pro/startup-swaps-costly-ai-gpus-for-arm-cores-and-up-to-128tb-of-cheap-lpddr6-ram-instead-of-expensive-hbm-to-smash-through-the-memory-wall
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-02T03:46:54Z'
published: '2026-08-02T00:00:00Z'
description: Startup claims a 128TB LPDDR6 server could outgun Nvidia GPUs while cutting
  AI costs and smashing the memory wall completely
image: https://cdn.mos.cms.futurecdn.net/hmq3Uw9iuC4HBqYDdUzT5a-1920-80.png
---

![Majestic Labs founders and server](https://cdn.mos.cms.futurecdn.net/hmq3Uw9iuC4HBqYDdUzT5a.png) 

- **Startup replaces Nvidia GPUs with custom Arm-powered AI processing hardware**
- **Prometheus packs up to 128TB of unified LPDDR6 memory onboard**
- **New server promises 1,000× more memory available per processor**

Majestic Labs, a startup founded in 2023 by former Google and Meta engineers, has unveiled a server built to rival Nvidia's GPU and HBM combination.

The Tel Aviv-based company argues that pairing costly graphics processors with high-bandwidth memory has become a fundamentally memory-bound and dead-end approach for AI inference.

Its answer is the Prometheus server, which swaps GPUs for Ignite AI Processing Units combining Arm cores with RISC-V vector and tensor engines.

## A different way to scale memory

Each Prometheus server can house up to 12 AIUs, sharing between 8 TB and 128 TB of LPDDR6 memory across one contiguous, coherent pool.

That memory pool is accessed through custom memory aggregation chiplets linked by copper cables up to one metre long instead of memory attached directly to GPU packages.

A standard 40U rack can hold four such servers, drawing 120 kW total and cooled through cold-plate liquid systems rather than air.

By comparison, an Nvidia DGX B300 system with eight Blackwell GPUs offers 2.3 TB of HBM3e plus up to 4 TB of DDR5 system memory.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Majestic claims its architecture therefore delivers over 50 times more fast memory than that rival configuration, alongside 1.7 times its interconnect bandwidth.

“One Majestic rack holds the fast memory capacity of 25 Nvidia NVL72 Vera Rubin racks at a fraction of the power,” Majestic Lab said.

“Organizations that could never justify hyperscaler infrastructure can now run any workload. In fact, there can be up to “1000× more memory per processor.”

## Performance claims await broader testing

Majestic Labs says the Prometheus server could cost between 10 and 50 times less than a GPU system of equivalent performance once it ships next year, while consuming less electricity per rack.

The server is designed to be OCP-compliant and will support PyTorch, vLLM and OpenAI's Triton frameworks, letting existing AI models run without modification.

Founded by CEO Ofer Shacham, President Sha Rabii and COO Masumi Reynders, the company employs around 40 people across Tel Aviv and Los Angeles and raised $100 million in an A-round late in 2025.

It claims to have already received significant orders from large enterprises, neoclouds and hyperscalers.

Yet several details remain unclear, including how many memory aggregation chiplets a single server actually requires.

If a 128 TB configuration relies on widely available 2 GB LPDDR6 dies, it would need roughly 64,000 of them, implying well over a hundred aggregation chiplets per server.

The numbers Majestic Labs presents are striking, but they remain the startup's own projections ahead of any independent benchmarking or shipped hardware.

Enterprise buyers considering a shift away from established GPU vendors may have to wait for independent validation to verify Majestic's claims.

Via *Blocks and Files*

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: AI enthusiast adds Nvidia Tesla V100 as loud as a lawnmower to gaming PC for
  $266 — 32GB of VRAM rig can run 27 billion parameter model at 32 tokens per second
source_url: https://www.tomshardware.com/pc-components/gpus/ai-enthusiast-adds-nvidia-tesla-v100-as-loud-as-a-lawnmower-to-gaming-pc-for-usd266-32gb-of-vram-rig-can-run-27-billion-parameter-model-at-32-tokens-per-second
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-26T13:50:05Z'
published: '2026-07-26T00:00:00Z'
description: Now they have a total 32GB VRAM system on a budget, for local LLM inference.
image: https://cdn.mos.cms.futurecdn.net/E3s43avFuEmiCykzqRLmGM-1200-80.jpg
---

![Tesla V100](https://cdn.mos.cms.futurecdn.net/E3s43avFuEmiCykzqRLmGM.jpg) 

A computing enthusiast has repurposed a very noisy and largely obsolete enterprise GPU (with lots of VRAM) for local LLM inference purposes. They are now enjoying a system that has doubled its total VRAM quota to 32GB for just a $266 (£200) outlay. That’s a good result, especially in the midst of a RAMpocalypse.

Oscar Molnar explains that a cheap Tesla V100 SXM2 with 16GB HBM2 was sourced, as was an SXM2-to-PCIe adapter, and a PWM mod for the loud-as-a-lawnmower cooler, to complete this VRAM expansion for the hefty local LLMs project. Indeed, these GPUs do look cheap right now, as I can see them listed on eBay US for under $140 each, if you don’t mind buying from China.

As mentioned above, you can’t just get one of these Tesla V100 SXM2 cards with abundant VRAM and plug it into your PC. Molnar says they spent about $66 on an SXM2-to-PCIe adapter, also on eBay.

You might think that was enough. However, the PC and local LLMs enthusiast baulked at the noise of “the fan from hell,” which came as standard with the Tesla V100 SXM2. That shrieking cooler was measured outputting 82dB of noise. Molnar described it as “somewhere between a garbage disposal and a lawnmower.” This may be the most complicated tweak yet, but basically the existing fan wires just needed rerouting and plugging into the motherboard PWM fan header. You could also simply purchase a “2.54mm male to PH2.0 female jumper cable” for the task. Apparently, the fan only needs to run at 10% to keep the Tesla V100 under 50C at full load.

 ![Nvidia Tesla V100](https://cdn.mos.cms.futurecdn.net/5UhZUv7mNhAoDYNYbE8BJf.jpg) 


## 27 billion parameter LLM runs at 32 tokens per second

With the hardware all now fitted and finessed, Molnar had a 32GB VRAM system at their disposal – that’s a PC with RTX 4080: 16GB VRAM, Ada architecture and Tesla V100: 16GB VRAM, Volta architecture. They note you can get Tesla V100s with 32GB of VRAM, but they are double the price.

Getting the system to make use of this 32GB of total VRAM for LLMs wasn’t tricky, says the DIYer. They used NixOS with a legacy Nvidia driver that overlapped support for both Volta and Ada architectures. Testing a local LLM, they got a 27 billion parameter model running at 32 tokens per second, which they say is “fast enough for interactive use” and faster than most cloud API alternatives.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

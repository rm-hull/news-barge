---
title: Nvidia paid $20 billion for SRAM decode - AMD just partnered for it instead
source_url: https://www.techradar.com/pro/nvidia-paid-usd20-billion-for-sram-decode-amd-just-partnered-for-it-instead
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-29T03:31:24Z'
published: '2026-07-29T00:00:00Z'
description: A partnership to split inference
image: https://cdn.mos.cms.futurecdn.net/oN8C2XnJkqZJEi4ecAeBgE-1920-80.jpg
---

![Cerebras CS-3 AI Chip](https://cdn.mos.cms.futurecdn.net/oN8C2XnJkqZJEi4ecAeBgE.jpg) 

- **AMD and Cerebras will split inference across two machines, with Helios racks handling prompt processing and the Wafer-Scale Engine generating tokens, available through Cerebras Cloud in H2 2026**
- **Nvidia is also doing something similar by licensing AI chip startup Groq's SRAM decode technology for $20 billion**
- **The move sees AMD and Cerebras claim 5x higher tokens per watt versus a standalone Cerebras WSE configuration**

AMD and Cerebras Systems have announced a technical partnership which pairs the former's Helios rackscale system with the latter's Wafer-Scale Engine in what both companies call a disaggregated inference solution.

The move has enabled a combined AMD Helios and Cerebras WSE configuration to deliver up to five times the tokens per second per watt (TPS/W) in internal testing by both chip designers.

The move aims to address a Cerebras WSE efficiency challenge by offloading prompt processing to AMD's rackscale offering.

## An efficiency gains-centric play?

Both AMD and Cerebras Systems are painting the news as a win, and it very well might be, given the latter's efficiency gains in play and the former's ability to get access to SRAM decode technology without spending the $20 billion Nvidia shelled out at the end of last year for a non-exclusive deal.

It must, however, be noted that the efficiency claims of 5 tokens per second per watt are compared against an existing Cerebras WSE (Wafer-Scale Engine) as the baseline, while running the open-source Kimi 2.6 1T model, making them impressive, but without a direct comparison to figures for an Nvidia rackscale offering, one that lacks context, especially when efficiency is the metric.

The idea itself is sound and well established in the industry, with WSE known to struggle with the 'prefill' part of the equation while handling the 'decode' segment relatively well, essentially substituting AMD's hardware where Cerebras' equipment falls short.

The choice of Kimi 2.6, however, deserves a second look. Moonshot AI's model, released on 20 April 2026, is a mixture-of-experts design with one trillion total parameters but only 32 billion active per token, and it ships natively in INT4. At INT4, the full weight set runs to roughly 500 GB. A single Cerebras wafer holds 44 GB. Even before KV cache, a Cerebras-only deployment needs somewhere north of a dozen wafers just to hold the model, while one Helios rack could hold it around sixty times over.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

That asymmetry means the five-times figure is measured on a model that is close to the least favorable for a WSE-only configuration. A dense model small enough to sit resident on a handful of wafers could flatter Cerebras considerably more. None of this makes the number wrong, but it does make the case for additional testing to demonstrate both its strengths and weaknesses for different models.

## A partnership without numbers, for now

More importantly, the absence of any financial information might very well be a future story, especially at a time when there are increasing concerns about 'circular financing' in an industry where Nvidia's recent move to backstop OpenAI's data center purchases was seen as a net negative by Wall St, which is already concerned about AI spend and the sustainability of such transactions.

AMD has also, in the past (and more recently with Anthropic), linked purchases of its own hardware to investments or stakes it would take in AI companies, moves that the market welcomed earlier but might view with a bit more hostility lately.

The announcement comes at a time when Cerebras might need it more than AMD: Cerebras listed on Nasdaq in May, priced at $185, opened at $350, and closed its first day at $311.07 before falling back to around $227 by late June 2026.

AMD stock, on the other hand, is up 121.48% year-to-date (YTD) as investors continue to bet heavily on its new Instinct AI processors, and the Cerebras partnership allows it to further consolidate its gains, as this might be seen as another vote of confidence in its current direction by one of its prospective customers.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

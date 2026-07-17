---
title: China's 2.8-trillion-parameter Kimi K3 beats Claude Fable 5 in Frontend Code
  Arena benchmark— Moonshot AI delivers largest open-weight AI model ever, as China
  works around U.S. compute limits
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-17T13:58:40Z'
published: '2026-07-17T00:00:00Z'
description: Moonshot's own disclosures point to export-grade Nvidia silicon and an
  unnamed alternative GPU vendor.
image: https://cdn.mos.cms.futurecdn.net/Bf3cosvjPduc22JVWXLHJE-1920-80.png
---

![Moonshot releases 2.8 trillion parameter Kimi K3](https://cdn.mos.cms.futurecdn.net/Bf3cosvjPduc22JVWXLHJE.png) 

Beijing-based Moonshot AI has released Kimi K3, a 2.8 trillion parameter model that the company describes in its technical blog as the world's first open 3T-class system and the largest open-weight AI model to date. Moonshot said K3 still sits behind Anthropic's Claude Fable 5 and OpenAI's GPT 5.6 Sol on overall performance, but it outperformed every other model in the company's evaluation suite, including Claude Opus 4.8 and GPT 5.5, across coding and agentic benchmarks. The model has a 1 million token context window, native vision, and activates just 16 of its 896 experts per token, roughly 1.8% of the pool. Full weights are due by July 27.

 ![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7.jpg) 


Arena ranked K3 first in its Frontend Code evaluation at 1,679 points, ahead of Fable 5, in blind developer testing. API pricing is $0.30 per million cache-hit input tokens, $3 per million on cache misses, and $15 per million output tokens. Kimi K2 launched a year ago at $0.60 per million input tokens, so uncached K3 input costs five times as much.

Big news: Kimi-K3 by @Kimi_Moonshot is now #1 in the Frontend Code Arena with 1679 pts, surpassing Claude Fable 5.This is a 17-place jump from Kimi-k2.6 (#18 -> #1).In Frontend, Kimi-K3 ranked #1 in 6 of 7 domains: Brand & Marketing, Reference-Based Design, Data & Analytics,… [https://t.co/YDN3BufGkC](https://t.co/YDN3BufGkC) pic.twitter.com/Oa6teaQnWpJuly 16, 2026


Moonshot claims roughly a 2.5x improvement in scaling efficiency over Kimi K2, attributed to two architectural changes: Kimi Delta Attention, a hybrid linear attention scheme, and Attention Residuals, which change how information moves between layers. Quantization-aware training starts at the supervised fine-tuning stage, using MXFP4 weights and MXFP8 activations, a combination Moonshot says it chose for broad hardware compatibility. Bank of America analysts led by Alex Liu said in a note cited by *CNBC***that K3 shows large-scale pre-training plus architectural work can still deliver step-change gains for flagship Chinese models despite compute constraints.

Moonshot's kernel optimization benchmark ran on Nvidia's H200, and what the blog identifies only as a "GPGPU from an alternative vendor," which the company didn't name. MiniTriton, a Triton-like compiler K3 built from scratch, is charted against Triton on an Nvidia L20, the cut-down Ada-based card sold into China under U.S. export rules. Moonshot recommends serving K3 on supernodes of 64 or more accelerators, keeping expert-parallel traffic inside one high-bandwidth domain. The blog doesn't say where the H200 hardware is; Congress passed a bill in January to close the offshore cloud rental loophole that gave Chinese firms remote access to restricted accelerators.

In one case study, K3 spent a single 48-hour autonomous run designing a simulated inference chip for a nano model built on its own architecture, using open-source EDA tools and the Nangate 45nm library. The design closed timing at 100 MHz within 4mm squared, packed 1.46 million standard cells and an INT4 MAC array, and sustained more than 8,700 tokens per second of simulated decode.

At the moment, every published K3 number is a claim made by Moonshot-reported or drawn from API access and can’t be verified until the weights are made public on July 27. Anthropic accused Moonshot in February of using 3.4 million Claude exchanges to train its models through distillation, and K3 now benchmarks within a few points of the models named in that complaint.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.

- 
Truth hurts sometimes.Reply
 You'll see hurt people lash out statements of disbelief when presented with proof.
 
 Clearly things are changing, but some people prefer to think that the US doesn't have a serious contender.
 
 Sadly Europe is nowhere to be found.
- 
Reply
 The problem is the proof is sometimes not as awesome as it seems. Benchmarking AI can be a cat and mouse game as its possible to train AI on a particular benchmark without noticeably improving real world results. Qwen36 looks like it should beat Gemma4, and for a while I was regularly switching between them, but now I find myself sticking with Gemma4 because it produces usable results more often. YMMV.heffeque said:Truth hurts sometimes.
 You'll see hurt people lash out statements of disbelief when presented with proof.
 
 Clearly things are changing, but some people prefer to think that the US doesn't have a serious contender.
 
 Sadly Europe is nowhere to be found.
 
 That's not to take anything away from Chinese models as they are producing some good things. Just cautioning against getting over excited about 1st party benchmarks that have yet to be verified.

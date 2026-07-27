---
title: Moonshot AI releases weights for Kimi-K3, firing a shot across the bow of OpenAI
  and Anthropic — open-weight model performs almost as well as frontier models while
  being 2-3x easier to run
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-ai-releases-weights-for-kimi-k3-firing-a-shot-across-the-bow-of-openai-and-anthropic-open-weight-model-performs-almost-as-well-as-frontier-models-while-being-2-3x-easier-to-run
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-27T21:20:59Z'
published: '2026-07-27T00:00:00Z'
description: Cached prompts can reach a 10x inference cost gain versus Anthropic and
  OpenAI's offerings
image: https://cdn.mos.cms.futurecdn.net/ZAD3iv3s8sBSmZNAoBfxGj-1104-80.png
---

![Kimi K3](https://cdn.mos.cms.futurecdn.net/ZAD3iv3s8sBSmZNAoBfxGj.png) 

Well, the artificially intelligent cat is out of the bag. After publishing a blog post and API documentation for the minty-fresh Kimi K3, Chinese outfit Moonshot AI delivered on its promise to release the model's weights for free, meaning that most anyone with a contemporary rack of AI GPUs can run it and charge for it, with few restrictions.

 ![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7.jpg) 


This is quite the shot across the bow of the big AI players, namely but not only Anthropic and OpenAI. Those companies' latest models are Claude Fable and GPT-5.6 Sol, respectively, and it happens that Kimi K3's capabilities outright beat previous generations of Claude and GPT in Moonshot's benchmarks, and closely trail Fable and Sol— all while seemingly being around 2-3x cheaper to run, up to 10x if a particular query lands in the cache. Moonshot's technical write-up seemingly backs up the benchmarks published last week, as the company reveals which exact software was used for testing.

For its inference cost comparisons, Moonshot says that its costs "are measured internally" versus the publicly available token pricing for other companies, but the figures are quite impressive. For input, Moonshot charges $3 per million tokens for Kimi K3. Meanwhile, Fable costs $10/1M, while Sol goes for $5/1M. That figure is standard non-cached input and is already pretty good-looking, but Kimi K3's caching structure seemingly has a 90% hit ratio for coding tasks, turning those $3 into $0.30/1M if your use case hits the cache a lot. The story is pretty similar for output tokens.

One of the likely reasons why Kimi K3 is so efficient is that it uses a mix of MXFP4 for weights and MXFP8 for input activation, both data types with relatively low precision and thus amenable to running on far less VRAM. Out of Kimi's 2.8 trillion parameters, only 104.2 billion are activated at a time, too.

Interestingly, Moonshot's write-up only mentions Nvidia's H20 being used for running Kimi for some coding tests, a fairly low-end chip by today's standards. That GPU doesn't have native support for MX floating-point types, unlike the export-controlled Blackwell B-series chips.

In turn, this can mean that Kimi K3's optimizations make it particularly amenable to run on lower-end hardware, but it's an equally reasonable guess that running it on something like Nvidia Blackwell or other MXFP-native silicon could make it even more cost-effective than in the presented benchmarks. We'll have to wait for more official figures to confirm this speculation.

Additionally, Kimi K3 doesn't use a conventional ever-expanding key-value (KV) store, instead relying on a fixed-size state handler called Kimi Delta Attention, again theoretically saving both on VRAM and execution time. Its mixture-of-experts (MoE) is particularly sparse with only 16 activated at each time out of 896, further contributing to inference cost reductions. Broadly speaking, Moonshot went for optimization at every layer of inference to avoid unnecessary overhead and bring inference cost down.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

This is could be bad news for OpenAI and Anthropic, given that most anyone with decent AI GPUs can now become their direct competitor, and the fact that Kimi K3 is open-weight also gives off the impression that "free" software is nearly as good, and far cheaper to run, than its proprietary competitors. It's worth noting that open-weight does not mean open-source; the training process and dataset are still Moonshot's special secret sauce.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

---
title: AI developer runs 28.9-million-parameter model on $10 ESP32-S3 microcontroller
  — uses Google's Per-Layer Embeddings technique, stores table on 16MB Flash memory
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-developer-runs-28-9-million-parameter-model-on-usd10-esp32-s3-microcontroller-uses-googles-per-layer-embeddings-technique-stores-table-on-16mb-flash-memory
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-27T15:08:42Z'
published: '2026-07-27T00:00:00Z'
description: Local model running on a sub-$10 microcontroller is impressive despite
  its obvious limitations.
image: https://cdn.mos.cms.futurecdn.net/rJLKQc9rokgCtsp5sxcjs-1920-80.jpg
---

![A photo of an ESP32 microcontroller wired up to a small screen showing AI benchmark results.](https://cdn.mos.cms.futurecdn.net/rJLKQc9rokgCtsp5sxcjs.jpg) 

When we talk about running local AI these days, the conversation usually either revolves around mini-PCs like the RTX Spark or drifts into wistful thinking about home servers and ludicrously expensive professional GPUs. Well, I reckon the most impressive AI hardware trick in a good while just happened on a piece of silicon that costs less than a decent burger. Last week, a Ukrainian developer named Slava S, who simply goes by 'slvDev' on GitHub, dropped a project called ESP32-AI. It's exactly what you think: he got a 28.9-million-parameter language model running locally, entirely on-device, on an ESP32-S3 microcontroller.

If you haven't read any of our previous coverage of this tiny chip, ESP32-S3 boards offer about the best bang for buck in the whole computing world. You can snag one online with a protective case for under $20 here in the States, and bare boards are readily available for under $10 around most of the world. As you'd expect from a chip so cheap, it's not powerful. On this variant, the S3, you get exactly 512KB of SRAM, 8MB of PSRAM, and 16MB of flash memory, which is not very much memory at all. So how exactly do you cram a nearly 30-million parameter model onto a chip with less primary storage than a single raw photo from your smartphone?

Usually, to run an LLM, the entire model has to sit in your system's fast memory because the processor needs to constantly do math against every parameter to generate the next word. If you try to run a 29M parameter model normally on an ESP32, you run out of fast RAM instantly. The previous record for a chip like this was around 260,000 parameters by one Mr. Dave Bennett, as pointed out by Slava himself on X.

 ![A diagram showing that the same architecture from big Google AI models can be used on a low-end machine.](https://cdn.mos.cms.futurecdn.net/B9WA3ApFaaSCqf7RT7WgSm.png) 


Our clever hacker got around this bottleneck by borrowing a brilliant architectural trick from Google's Gemma called Per-Layer Embeddings. He quantized the model down to 4-bit (making the total file size just 14.9 MB) and changed where the data lives; instead of trying to stuff the whole thing into the tiny 512KB SRAM or the only slightly-less-tiny 8MB PSRAM, he dumped the 25-million-parameter embedding table into the relatively-slow 16MB Flash memory. Because this specific model architecture only needs to pull a few rows from this table per token, the inherent slowness of the Flash memory doesn't choke the processor, and so the 512KB of fast SRAM is kept clear for just the "thinking core", the actual reasoning weights.

Now, let's pump the brakes for a second, because I know someone out there is already wondering if they can replace their server with an $8 chip. The model he used was trained on the TinyStories dataset, and it's really more of a Small Language Model (SLM), or honestly, a "micro LM." Due to the way it was created, it's only capable of writing short, simple, fictional stories. It will not answer questions, it will not follow instructions, it won't write your Python code, and it possesses exactly zero factual knowledge about the real world.

29M model won't chat with you or write your code. that's fine, that was never the point.point it at one narrow thing and it gets genuinely useful.imagine a coffee machine that actually knows about coffee, every bean, grind, ratio, water temp. offline, no app.when the model… [https://t.co/pWmzBRJTTPJuly](https://t.co/pWmzBRJTTPJuly) 24, 2026


Focusing on that limitation completely misses the magic of what's happening here in this proof-of-concept, though. The achievement is fitting a structurally quite large model onto a computer with practically no resources. It proves that with clever architecture, you can run genuine neural networks on dirt-cheap embedded hardware, and there are useful applications for a model this size. Slava imagines the idea of a coffee machine that actually knows about coffee: every bean, grind, ratio, water temperature, all offline, no app required.

Truthfully, when we're talking about "AI", it all comes down to what you are trying to accomplish. To put it plainly, asking how much hardware you need for local AI without specifying the workload is like asking what vehicle you need without saying what the goal is. A bicycle, a sedan, a pickup truck, a semi-trailer, and a train all "get you from A to B," but they're built for radically different jobs. AI is the exact same way; it's what you're doing with it that determines how much hardware you need.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

 ![Screenshots of Dragon Warrior and Final Fantasy for the 8-bit NES showing character names generated by AI.](https://cdn.mos.cms.futurecdn.net/SV4hzTVfeDn8pqEHDRYcM6.png) 


*Dragon Warrior*(left) and

*Final Fantasy*(right) were AI-generated directly on the NES. (Image credit: erodola / GitHub)

To illustrate the point, last year another developer published a project cramming an AI language model (a bigram name generator) into the original *Dragon Warrior* and*Final Fantasy* games on the NES. Yes, the Nintendo Entertainment System. Developer Emanuele Rodolà managed to fit the entire model weight table (729 bytes) and the inference code (~140 bytes of hand-written assembly) into the original game ROM to generate new character names on the fly. That's real AI, running on a MOS 6502 processor, a piece of silicon that dates back to 1975.

The ultimate takeaway from slvDev's project is that Per-Layer Embeddings scale far further down than most people would have imagined, and it lends credence to the recent enthusiasm surrounding High-Bandwidth Flash as a tiered storage medium for AI servers. That's exciting not because it means an ESP32 will replace your desktop GPU, but because it suggests the same architectural ideas could make AI dramatically more practical across the entire spectrum of hardware, from tiny embedded devices all the way up to datacenter accelerators.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi.jpg)

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

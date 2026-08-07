---
title: The next age of LLMs? Dev gets a small LLM running at 10 tokens a second locally
  on a $10 microcontroller
source_url: https://www.techradar.com/pro/the-next-age-of-llms-dev-gets-a-small-llm-running-at-10-tokens-a-second-locally-on-a-usd10-microcontroller
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-07T20:54:28Z'
published: '2026-08-07T00:00:00Z'
description: 28.9M-parameter model runs on a microcontroller costing less than $10
image: https://cdn.mos.cms.futurecdn.net/XJxYihidzczXcGX9g2rsNn-1920-80.jpg
---

![AI chip on a lit circuit board](https://cdn.mos.cms.futurecdn.net/XJxYihidzczXcGX9g2rsNn.jpg) 

- **A developer has a 28.9-million-parameter model generating TinyStories-style text at 9.88 tokens per second, fully offline, on a $10 microcontroller**
- **It was achieved by fitting a language model on a chip with 512KB of RAM by leaving most of it in flash storage**
- **The project is available on GitHub under an MIT license**

A developer going by slvDev has a 28.9-million-parameter language model generating text on an ESP32-S3, a microcontroller built for sensor nodes and smart plugs, at 9.88 tokens per second, with nothing leaving the chip.

The project, esp32-ai, went up on GitHub under an MIT license in late July 2026, was showcased on the Better Stack YouTube channel, and has since collected over 3,600 stars and has more than 470 forks of the underlying code.

Given the underlying hardware's limitations, the attempt meant the model, which was trained on the TinyStories dataset by Microsoft Research, had to be scaled down.

## Still a capable LLM despite the loss in accuracy

The arithmetic involved here is brutally unforgiving; weights typically need one to four bytes per parameter just to sit in memory, so 28.9 million parameters at 16-bit precision still require nearly 60 MB of RAM. An ESP32-S3 offers 512 KB of SRAM and 8 MB of PSRAM that is woefully inadequate at first glance.

Quantization closes the first part of the gap: dropping the weights to four-bit precision trades a little accuracy for a 75% reduction, bringing 60MB down to 14.9MB.

The second step is where the project earns most of its attention: most of a language model's parameters sit in embedding tables that the model reads from rather than computes against, and something you only read can live somewhere slow.

Borrowing Per-Layer Embeddings from Google's Gemma 3n, slvDev moved about 25 million parameters (roughly 12 MB at four-bit) into the board's 16 MB of flash, pulling around 6 rows, about 450 bytes, per token.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

What remains in working memory is closer to 2 MB: the dense core and output head in PSRAM, and activations and norm weights in SRAM. Each tier stores whatever is read at its own frequency, and the chip's memory hierarchy serves as the architecture that enables the LLM.

Offloading weights to storage is not new; it is how people coax frontier-class models onto hardware that has no business running them, but it usually destroys throughput, turning tokens per second into seconds or minutes per token.

The PLE approach avoids that because the offloaded weights are accessed sparingly, so flash bandwidth never becomes the bottleneck. The resulting performance, 9.88 tokens per second, is faster than most people read.

The LLM has its limitations, however: the model writes short, mostly coherent stories and will not answer questions, follow instructions, write code, or know facts. The developer says the limit stems from the small part of the model that performs the reasoning (~4M parameters) and that the memory trick does not change its capabilities. His repository also ships a second model, Barista, which expressly answers espresso questions only *(pun intended)*.

In short, the approach doesn't make small models smarter, but it does allow them to offload data within the board onto chips they could not previously run on, making it an interesting choice, though one with limited practical uses in its current iteration.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

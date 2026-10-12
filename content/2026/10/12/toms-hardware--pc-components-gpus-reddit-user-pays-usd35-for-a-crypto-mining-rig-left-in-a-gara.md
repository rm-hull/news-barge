---
title: 'Reddit user pays $35 for a crypto mining rig left in a garage and gets 54GB
  of VRAM at 65 cents per GB — the first test for 2017-era GPUs: a 35B-parameter AI
  model running locally at over 30 tokens per second'
source_url: https://www.tomshardware.com/pc-components/gpus/reddit-user-pays-usd35-for-a-crypto-mining-rig-left-in-a-garage-and-gets-54gb-of-vram-at-65-cents-per-gb-the-first-test-for-2017-era-gpus-a-35b-parameter-ai-model-running-locally-at-over-30-tokens-per-second
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-12T10:44:32Z'
published: '2026-10-12T00:00:00Z'
description: A rusty rig and a refused test, but all nine cards worked.
image: https://cdn.mos.cms.futurecdn.net/QDZdfYqJbKd5P6QKeMwVEk-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Personal Finance & Investing
people: []
locations:
- Ollama
- Russia
organisations:
- Avito
- CUDA
- GPUs
- GTX
- Get Tom's Hardware
- Google News
- MoE
- Nvidia
- OP
- PCIe
- RAM
- Shane Downing
- Tom’s Hardware
- WiredEntrepreneur
---

![Rows of open-frame cryptocurrency mining rigs packed with graphics cards, their fans glowing green, in a dimly lit room](https://cdn.mos.cms.futurecdn.net/QDZdfYqJbKd5P6QKeMwVEk-1920-80.jpg)

A Reddit post by user markpronkin (“OP”), titled “54gb vram for 35$,” says the user purchased an old crypto mining rig, originally discovered in a garage, for a negotiated 3,000 rubles, or about $35. The rig was rusty, and the buyer “had zero idea if it works, so did the seller,” with a pre-purchase test request refused. However, on the first try, all nine Nvidia P106-100 GPUs, with 54GB of VRAM between them, worked. The initial test: a successful local run with the 35-billion-parameter model Qwen3.6-35B-A3B in Ollama, which operated at over 30 tokens per second.

The rig was discovered in a “damp garage” the seller had purchased years earlier, then listed on Avito, a Russian classifieds site. The OP had concerns about whether or not the rig would work and offered to test it and pay more if it functioned, but the seller refused, and the price was negotiated down without a test. The cost was low enough to take the risk, the buyer said. Even in the case the rig worked, performance was imbalanced, as the main system has a weak Celeron CPU with very little system memory.

The setup was originally intended for crypto mining with specialized Nvidia P106-100 GPUs, Pascal-generation cards with 6GB of GDDR5 each that OP calls “basically gtx 1060 6gb.” Gigabyte’s P106-100, for reference, has 8,008 MHz memory with a 192-bit bus width for about 192 GB/s per card. The hardware was originally introduced around the middle of 2017. The cards are no longer entirely supported as CUDA 13.0 removed offline compilation for GPUs below compute capability 7.5, which includes Pascal GPUs, and driver branch 580 is “the final [one] that supports GPUs before CC 7.5,” Nvidia says on its developer blog. Security updates are supported through October 2028, however.

The first test was a mixture-of-experts model using Alibaba’s Qwen with “35B [parameters] in total and 3B activated,” per Qwen’s model card on Hugging Face; it’s roughly a 24GB download. The initial test had it at “30+ tokens a second” in Ollama but it can probably operate faster “with mtp and some optimizations,” OP says, referring to multi-token prediction.

Another user stated that such performance was possible on a CPU alone, to which OP replied, “On a 35$ device without any optimizations?” A dense, non-MoE model such as Qwen3.8-27B is unlikely to run as well, but “It should run any MoE model that fits entirely into VRAM decently well.” Performance is also expected to be limited by the PCIe 2.0 x1 motherboard slots.

The system is capable but would have some limitations due to the sizes of some popular models. Qwen3.6-35B-A3B at 8-bit should fit at 36.9GB, as should Llama 3.3 70B at 4-bit, at 42.5GB; at 5-bit, just below 50GB, it would leave little room for context. Larger models are probably not workable, and even the 70B 4-bit Llama would hit a ceiling around 4.5 tokens per second before hitting other bottlenecks, since each token reads all 42.5GB, card by card, at about 192 GB/s. The performance the buyer achieved is in spite of the rig, and the MoE model was the best choice for that type of result.

The buyer still got a good deal, as the price comes out to about 65 cents per GB of VRAM. For comparison, an RTX 5090 with 32GB of VRAM and 1,792 GB/s of memory bandwidth launched at $1,999 in early 2025. The rig has 1.7 times the VRAM for less than 2% of that price, but each of its cards has about a ninth of the bandwidth. According to OP, the mostly compute-only P106 cards sell for about 50% of their GTX counterparts.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

One important caveat here is electricity costs, with the GPUs having a combined 1,080W TDP as estimated by one commenter, but OP says their power is free and generally inexpensive in Russia as a whole.

With the rig securely in hand, the OP’s next move is to transfer the hardware to a better case that supports up to an i7-7700K CPU and 32GB of RAM. The new case allows for 12 GPUs, so buying three more of the same adds up to 72GB of VRAM total. The solution is attractive because of “unlimited usage and actual privacy,” the buyer said to WiredEntrepreneur. Repurposing used hardware for a self-hosted AI solution with appropriately sized MoE models is a viable, useful project for enthusiasts who want freedom. From the OP’s perspective, more VRAM means more freedom.



*Follow* * Tom’s Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

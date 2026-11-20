---
title: OpenAI says it redesigned an AMD GPU, doing a year’s worth of optimisation
  in 5 months
source_url: https://www.pcgamer.com/hardware/openai-says-it-redesigned-an-amd-gpu-and-amd-is-using-some-of-those-tweaks-for-use-in-future-products/
source_site: PC Gamer
source_slug: pcgamer
description: And AMD is putting some of those optimisations into 'future products'.
image: https://cdn.mos.cms.futurecdn.net/LosgWX2VGL8NLmymLz7zmi-2560-80.jpg
published: '2026-11-20T00:00:00Z'
scraped_at: '2026-11-20T20:06:52Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- Jalapeño
organisations:
- AI
- AMD
- BigGo Finance
- GPT-6.1 Sol
- GPT-6.2 Astra
- GPU
- OpenAI
- PC Gamer Circuit Breaker
---

![Photo of an AMD Ryzen 9 9950X3D processor](https://cdn.mos.cms.futurecdn.net/LosgWX2VGL8NLmymLz7zmi-1920-80.jpg)

OpenAI has recently reported that its frontier models attempted to rewrite AMD circuits and received an up-to 14% PPA (Power, Performance and Area) boost. OpenAI says these rewrites are "production-viable" too (via BigGo Finance).

The claim is not that humans couldn't make these same optimisations, but instead that it did around a year's worth of design optimisations in less than 5 months, an optimisation of optimisation, if you will. (Okay, I'll stop writing optimisation now.)

Apparently, AMD has even incorporated some of these findings into chip designs that have recently gone to manufacturing. The model worked on an in-house "Jalapeño" chip, as well as an AMD "flagship GPU IP" and "AMD next-gen flagship CPU key modules." Each one of these saw different gains.

For the Jalapeño vector compute unit, the model's changes managed to reduce cell area by around 13%, and this was observed when powering on the hardware. The Jalapeño compute unit saw the standard cell area reduced by around 10%, with the multiplier area alone reduced by around 15 % and latency cut from two clock cycles to one.

It's the AMD flagship GPU that saw the 14% PPA improvement, and AMD has reportedly verified a 'single-digit' PPA improvement on the next-gen CPU.

![Asus Prime RX 9070 XT graphics card](https://cdn.mos.cms.futurecdn.net/7crxcVBLebepY7bD2jrRNB-1200-80.jpg)

Using a budget of around 112,000 tokens, all models in the report (GPT-6.2 Astra, GPT-6 Astra, GPT-6.1 Sol, and GPT-5.6 Sol) performed better when asked to design a RISC-V core from scratch, rather than optimising one given to them. That being said, OpenAI does note that models asked to entirely redesign rather than optimise could omit features in the original design, which can become its own problem.

Generative AI is a bit of a double-edged sword in the PC hardware space. Before mentioning the memory crisis the AI global buildout is responsible for, generative AI's ability to work constantly and fast can be a boon for development, but it can also be a slog to work through. Linux engineers are currently struggling to get on top of the thousands of bugs AI is finding, which is a real monkey's paw element of the tech. And it's a sign that AI itself needs to be maintained and monitored, even if it genuinely does seem to produce favourable results in engineering.

The PC Gamer Circuit Breaker newsletter breaks down the latest PC gaming tech, and finds you the best deals on the best products

One can only hope that not being able to afford memory is worth it when we get to the next generation of chips and their proposed performance boost. That or one can hope that the whole memory crisis thing cools down soon. Both preferably.

![Razer Blade 16 gaming laptop](https://cdn.mos.cms.futurecdn.net/YwnnY4PZ7TcCYKRYDho7VW-140-80.jpg)

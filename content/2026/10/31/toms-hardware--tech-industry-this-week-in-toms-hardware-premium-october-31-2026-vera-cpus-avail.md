---
title: 'This week in Tom''s Hardware Premium: October 31, 2026 — Vera CPUs available
  on Oracle clusters, building an agentic CPU benchmark and a primer to LLMs'
source_url: https://www.tomshardware.com/tech-industry/this-week-in-toms-hardware-premium-october-31-2026-vera-cpus-available-on-oracle-clusters-building-an-agentic-cpu-benchmark-and-a-primer-to-llms
source_site: Tom's Hardware
source_slug: toms-hardware
description: Catch up on everything we published this week.
image: https://cdn.mos.cms.futurecdn.net/eRuBmbo6Lk5aDxn4D79nAE-1920-80.jpg
published: '2026-10-31T00:00:00Z'
scraped_at: '2026-10-31T17:42:20Z'
categories:
- Technology & Software
- Hardware
people:
- Jake Roach
- Sayem Ahmed
- Tom
- Vera
locations:
- U.S
organisations:
- ABF
- Agentic AI
- Ajinomoto Build-up Film
- Anthropic
- Bench
- CPU
- Cadence
- Dexerto
- EDA
- FCC
- GPU
- Gamespot
- Get Tom's Hardware
- Ghidra
- IGN
- IPO
- Ibiden
- LLM
- LLMs
- Maestro
- Nvidia Vera
- OCI
- Oracle
- PC
- PsiQuantum
- TP-Link
- Tom's Hardware
- Vera CPUs
- Wi-Fi 8
---

![THP logo on a blurred background](https://cdn.mos.cms.futurecdn.net/eRuBmbo6Lk5aDxn4D79nAE-1920-80.jpg)

In case you're not yet subscribed to our *Tom's Hardware Premium* subscription service, here's what you've been missing out on this week. We detail our thoughts on Anthropic's filings pre-IPO, Cadence's new suite of LLMs to power its EDA tools, how Nvidia is securing its entire supply chain to serve AI data center demand, how Vera CPUs are landing in the cloud, an update to the ongoing TP-Link saga, and more. Remember, to access any of the articles listed here, you'll need to arm yourself with a subscription.

We've been hard at work behind the scenes to determine exactly how locally-run AI models and workloads stress consumer-level components. While throughput and tokens per second are indeed important factors, our resident CPU expert Jake Roach has begun laying out his vision for how Agentic workloads tax CPUs, and how we're building benchmarks in this newfangled AI world that the PC hardware space finds itself increasingly entrenched in. It's not often that readers get the chance to look at our behind-the-scenes work, and this piece offers a look at some of the foundational exploration we're doing around how to define what an agentic AI CPU benchmark might look like in the future.

![A DGX Spark sitting on top of a graphics card.](https://cdn.mos.cms.futurecdn.net/QLzVeqtnQBaChuCMvquA7A-1200-80.jpg)

As the rise of Artificial Intelligence increasingly becomes attached to powerful, locally-run hardware, you might encounter terminology and nomenclature that you may otherwise not be familiar with. So, we've published a primer on all of the basic terminology that you need to know moving forward. Currently, you get breakdowns of how inference works, details on quantization, context, KV cache, and more. We're striving to update this page as our exploration with local AI grows, to serve as a handy bookmark. It's not a mere dictionary either, as we contextualize how each of these things relates to the larger overall model, how it might be served, or where you might encounter it when trying to run an AI model of your own.

Nvidia's Vera CPUs were a salient part of a swath of Oracle announcements this week. The chip, usually found alongside Nvidia's NVL72 rack, is now generally available, but curiously, standalone Vera instances are also available on OCI superclusters. The CPU is specifically designed with Agentic AI workloads in mind, and it just so happens that we've benchmarked an Nvidia Vera server just this week to highlight the efficacy of how well Vera might perform under certain workloads.

Last week, we covered TP-Link's proposal to allow the router manufacturer to sell its Wi-Fi 8 products in the U.S. Now, according to a new report, it's alleged by the FCC that TP-Link's own reports contain "false or incorrect information in its applications" related to equipment authorizations for four different models of Wi-Fi 8 routers that the company hopes to sell stateside. As the saga continues to develop, we attained a statement from TP-Link on the subject, as the situation continues to develop.

Anthropic's large and sprawling S1 filing made headlines this week as the company prepares for an IPO. Within the document, it details many (but not all) of the numbers driving one of the world's foremost AI labs. Once you get past the mind-bogglingly high $800 billion in GPU and TPU contracts, the company has shown that most of its compute capacity isn't actually served to customers, and is instead dedicated to R&D for new models, features, and testing. There's a huge amount of information to sink your teeth into here, and despite what many might believe, the company's revenue per compute dollar spent is actually in Anthropic's favor, shattering the myth that tokens cost more in compute than they do for a user.

As neoclouds and hyperscalers (who rent compute out to companies like Anthropic) scale up and scale out, domains become exceedingly important. With copper materials coming up to their natural limits, eyes have turned to the photonic domain to alleviate bandwidth bottlenecks. Now, PsiQuantum has entered the domain, showcasing a prototype photonic switch that loses less light than other devices on the market, and the company expects to develop and mature its solution and is likely to enter the photonic switch market.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Cadence diagram of AgentStack over five AI Super Agents, with the new Maestro AI models layer, the JedAI data and AI platform, and cloud or on-premises compute beneath.](https://cdn.mos.cms.futurecdn.net/P8XPrtLpMc8eqkqoGb66Vo-1200-80.png)

Cadence has revealed Maestro, a suite of tuned LLM's, designed specifically to work in EDA flows using the company's in-house suite of agentic tools. We've covered the rise of agentic EDA tools closely, and Cadence's Maestro suite appears to be the company's own shot across the bow in helping its customers automate elements of their own chip designs. In initial results compared with general-purpose AI models, Cadence claims up to a 30% improvement in the quality of results and that Maestro effectively uses fewer tokens for the same task, with up to 5x the token efficiency compared to off-the-shelf AI models.

But all of those new AI chips have to come from somewhere. With the ongoing, ceaseless AI buildout, firms are looking to secure their supply chains, with Nvidia one of the chief companies among them. As demand continues to soar, the very real limitation of fabs is particularly highlighted in the realm of the substrates used to create PCBs. Ajinomoto Build-up Film, or ABF, is one of the hottest commodities in the chipmaking industry as a result, and Nvidia has announced plans to secure the material from Ibiden, in addition to other critical materials used in chip packaging, testing, and more. Of course, Nvidia isn't doing this out of the goodness of its own heart; it's doing it in exchange for reserved production capacity.

The ramifications of AI are still being felt across the globe, but if you've been on social media over the past several weeks, you may have found that there's one particular trend: Decompilation and recompilation of video games, recompiled to work natively on PCs. We detail how additional software tools like Reverse Engineer Anything and Ghidra are powering the boom.

![Tom's Hardware Premium Subcription]([https://cdn.mos.cms.futurecdn.net/RZiWuzR4HNRoJJYAbkWDRX-200-80.png.webp](https://cdn.mos.cms.futurecdn.net/RZiWuzR4HNRoJJYAbkWDRX-200-80.png.webp) "Tom's Hardware Premium Subcription")

Don’t miss out on this Tom’s Hardware Premium. Get a full year of access for just $29, or from $7 per-month. Get daily news analysis, deep dives into specialist topics in the semiconductor industry, as well as access to Bench, the largest benchmarking database around.

To read any of the articles we mention above, as well as unlock Bench, you'll need to purchase a *Tom's Hardware Premium* subscription. Your support goes a long way in helping us to publish deeper, more insightful articles that might not otherwise be covered.

![Sayem Ahmed](https://cdn.mos.cms.futurecdn.net/xsPCakGobuUWmyECbrEM2T-140-80.jpg)

Sayem Ahmed is the Subscription Editor at Tom's Hardware. He covers a broad range of deep dives into hardware, both new and old, including the CPUs, GPUs, and everything else that uses a semiconductor. He has worked as a professional tech journalist since 2015 and has written for Gamespot, IGN, and Dexerto.

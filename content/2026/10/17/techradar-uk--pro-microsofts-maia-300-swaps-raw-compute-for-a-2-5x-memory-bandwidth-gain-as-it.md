---
title: Microsoft's Maia 300 swaps raw compute for a 2.5x memory bandwidth gain as
  it moves to make in-house silicon its main AI engine while claiming a 40% efficiency
  bump — could going the Google route be the pin that pops the Nvidia AI bubble?
source_url: https://www.techradar.com/pro/microsofts-maia-300-swaps-raw-compute-for-a-2-5x-memory-bandwidth-gain-as-it-moves-to-make-in-house-silicon-its-main-ai-engine-while-claiming-a-40-percent-efficiency-bump-could-going-the-google-route-be-the-pin-that-pops-the-nvidia-ai-bubble
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-17T20:32:37Z'
published: '2026-10-17T00:00:00Z'
description: Can in-house chips pop the AI bubble?
image: https://cdn.mos.cms.futurecdn.net/gn2pVK4F4zf9ZvW3ypaFod-1920-80.jpg
categories:
- Technology & Software
people:
- Anat Ashkenazi
- Andy Jassy
- Colette Kress
- Hock Tan
- Jensen Huang
- Maia
- Rani Borkar
- Satya Nadella
- Saurabh Dighe
- Scott Guthrie
- Sundar Pichai
- Vera Rubin
locations:
- AI
- Amazon
organisations:
- AI
- AMD
- Alphabet
- Amazon
- Anthropic
- Azure Hardware Systems and Infrastructure
- Azure Maia
- Broadcom
- CNBC
- Cloud
- European Commission
- GPU
- Gartner
- Google
- Graviton
- Groq
- ISI
- Meta
- Microsoft Blog
- NVIDIA
- Nitro
- Nvidia
- OpenAI
- StorageReview
- TPU
- TPUs
- TSMC
- TechRadar Pro
- Trainium
---

![Maia 300](https://cdn.mos.cms.futurecdn.net/gn2pVK4F4zf9ZvW3ypaFod-1920-80.jpg)

* **Microsoft will make Maia its main inference engine at multi-gigawatt scale, following Google and Amazon into in-house silicon**
* **Microsoft's upcoming Maia 300 trades a modest 36% compute gain for 2.5x Maia 200's memory bandwidth, betting on memory-bound decode, with production in 2027**
* **Hyperscalers supply just over half of Nvidia's data center revenue at a 75% gross margin, so each move to in-house chips affects not only its pricing power but the chip industry's sustainability as a whole**

In 2024, Microsoft told the European Commission that Google was the only company vertically integrated at every AI layer, from chips to a mobile app store, and that "everybody else must rely on partnerships to innovate and compete."

Now, it has revealed plans to follow the same route without breaking a sweat.

In an Official Microsoft Blog post, Scott Guthrie, executive vice president of Cloud + AI, said Microsoft will scale its Azure Maia accelerators to multi-gigawatt deployments starting in 2027 and make Maia the primary inference system for Microsoft's products and services.

The vehicle of its choice is Maia 300, which Rani Borkar, president of Azure Hardware Systems and Infrastructure, and Saurabh Dighe, corporate vice president of systems planning and architecture, detail in an architecture deep dive.

## Feeding the beast, not growing it, as it takes the Google route

The move is a pointed statement from one of Nvidia's biggest customers, and it lands as bubble worries grow louder. Gartner forecast this week that AI providers will spend nearly $1 trillion on infrastructure in 2026 alone, and that AI revenue won't cover the build-out profitably until at least 2032.

If the largest buyers of AI hardware stop paying Nvidia's margins for the work they do most, the most richly valued part of that build-out starts to look exposed. Whether Maia 300 is the final catalyst for such a move, though, is a harder case to make.

Maia 300 moves from Maia 200's single die to a multi-chiplet package, with compute on TSMC's N2P process and memory-controller and I/O functions split onto separate dies. Eight HBM4 stacks deliver 288GB at 18TB/s per accelerator, against 216GB at 7.1TB/s for Maia 200, according to StorageReview's breakdown of Microsoft's spec sheet.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Microsoft hasn't abandoned compute so much as rebalanced around memory. In decode, the token-by-token phase that dominates long reasoning chains and agent loops, accelerators spend much of their time waiting on data rather than doing arithmetic.

The Maia 300 tries to close that gap by keeping data near the compute that uses it, through a non-uniform memory layout across chiplets, software-managed on-die SRAM, and narrower number formats, including an enhanced MXFP4 and sub-3-bit storage formats, with hardware conversion between them. The Maia 300 announces something the rest of the industry already knew, albeit more subtly: Custom silicon is no longer a side project for hyperscalers.

Google, the company Microsoft singled out two years ago, began recognizing revenue from TPU system sales delivered to customer data centers in the second quarter, CFO Anat Ashkenazi said on Alphabet's July earnings call, while CEO Sundar Pichai said the company is "seeing strong demand for TPUs as standalone systems from other customers."

It isn't the only one either; Anthropic has lined up 3.5GW of TPU capacity through Broadcom for 2027, on top of an earlier deal for up to a million TPUs, and Meta was reported in 2025 to be in talks to rent-cum-purchase them. Amazon has gone the same way. CEO Andy Jassy said in April 2026 that Amazon's chip business, spanning Trainium, Graviton and Nitro, had passed a $20 billion annual revenue run rate and was now "one of the top three data center chip businesses in the world." OpenAI, meanwhile, has lifted the lid on its own Jalapeño accelerator.

## Nvidia's margins: the AI holy grail?

The incentive is plain from Nvidia's own results. In the quarter to July 2026, the company reported $96.2 billion in revenue, $89 billion of it from data centers, at a 75% gross margin. CFO Colette Kress put hyperscale revenue at $49 billion on the earnings call, meaning a little over half of Nvidia's data center business comes from a small group of buyers, the biggest of which now design their own accelerators.

Every inference workload that moves in-house is one where that buyer pays closer to manufacturing cost instead of Nvidia's margin. Microsoft told investors in July that Maia 200 was up to 40% cheaper to operate than Nvidia's latest chips on OpenAI and Microsoft models.

It did, however, fail to name a particular GPU it called a "leading GPU-based system," an important distinction given Nvidia's focus on efficiency via Vera Rubin, which OpenAI even refused to compare against outright.

The reveal didn't move stocks much; on Monday, Nvidia shares closed down 1.29% after the reveal, while Microsoft's rose 1.14%, and Microsoft's opaqueness about efficiency gains may be one reason.

The other reason is equally important: Evercore ISI analysts estimate Maia will account for only about 10% of Microsoft's AI chip spending by the first quarter of 2027, CNBC reported, and Nvidia has guided to $108 billion in revenue for the current quarter.

Scale is arguably an ongoing constraint, however; at 167 kW per rack, a gigawatt of rack power is roughly 6,000 Maia 300 racks, or about 575,000 accelerators, before cooling and facility overheads.

Going the Google route hasn't stopped anyone buying from Nvidia either. Amazon, with its "top three" chip business, is still set to take more than 3 million Nvidia GPUs by mid-2028.

Alphabet, which now sells its own TPUs, raised its 2026 capex guidance to between $195 billion and $205 billion in July, lists Vera Rubin alongside its own TPUs, and Ashkenazi said it is "still in a supply constraint environment."

Microsoft keeps Nvidia and AMD for training, and Satya Nadella said earlier in 2026 that "because we can vertically integrate doesn't mean we just only vertically integrate."

Jensen Huang's answer to the custom silicon question on Nvidia's August call could have been written about Maia: "Whereas many of these XPUs are inference-specific chips for one cloud or one service, NVIDIA is a platform." Microsoft's counter-bet is somewhat different: one cloud is big enough.

The deeper problem for the pin theory is that custom silicon changes who collects the margin, not how much gets spent. Gartner warns that the industry needs about $8.5 trillion in revenue between 2026 and 2030 to earn a reasonable return on its build-out, versus no more than $3.6 trillion it expects AI to generate. Microsoft isn't responding by building less; it is planning gigawatts more, and cheaper tokens arguably help close that revenue gap rather than widen it.

Some of what Microsoft saves will also flow elsewhere in the supply chain. Maia 300's pitch rests on HBM4, the same constrained memory Nvidia's Rubin uses at the same 288GB per package, and its compute dies come from TSMC, which supplies everyone.

Google's TPUs are developed and supplied under a long-term agreement with Broadcom, whose CEO Hock Tan said that "many investors in AI don't understand what they're putting their money into," and who expects chip shortages to ease only around 2028 or 2029. Nvidia isn't sitting idle either; it already paid $20 billion to license Groq's SRAM decode technology, a sign it sees the same inference threat coming.

Until production silicon ships and someone outside Microsoft can measure it, Maia 300 is a well-argued design whose most important numbers are ones that only Microsoft has seen, and a reminder that the biggest threat to Nvidia's margins may be its best customers rather than its rivals.

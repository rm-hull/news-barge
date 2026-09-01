---
title: OpenAI lifts the lid on its in-house Jalapeño chip - with benchmarks claiming
  it beats Nvidia's GB300
source_url: https://www.techradar.com/pro/openai-lifts-the-lid-on-its-in-house-jalapeno-chip-with-benchmarks-claiming-it-beats-nvidias-gb300
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-01T19:22:45Z'
published: '2026-09-01T00:00:00Z'
description: A custom ASIC to rule AI efficiency domestically?
image: https://cdn.mos.cms.futurecdn.net/UgCf3tNYvSJsCa9pAqzrvL-1920-80.webp
---

![A render of OpenAI's first generation Jalapeño chip](https://cdn.mos.cms.futurecdn.net/UgCf3tNYvSJsCa9pAqzrvL.webp) 

- **OpenAI published the first Jalapeño benchmarks at Hot Chips, claiming 1.5 to 1.9x more throughput per kilowatt and up to 3.6x lower latency than Nvidia's GB200 and GB300 rack systems**
- **The chip's purported gains are at a reported 700W power draw and center around efficiency, with Nvidia's GB300 still leading on absolute throughput per package by 20-25 percent.**
- **The numbers are currently self-reported, and volume production of the chip is not expected to ramp up until 2027**

OpenAI took the stage at Hot Chips on August 25 with the first published performance figures for Jalapeño, the inference accelerator it co-developed with Broadcom, and the numbers are designed to be read the way it flatters the former: efficiency.

The company reported 1.5 to 1.9 times more throughput per kilowatt and 1.7 to 3.6 times lower end-to-end latency across three open models than the Nvidia rack systems it tested against.

OpenAI's Jalapeño is currently rated at 700W, versus comparable Nvidia silicon that was rated for 1200W and 1400W, a key differentiator in a benchmark that already has limited information available to researchers looking to pick a clear winner.

## AI efficiency takes center stage?

OpenAI's Jalapeño is an ASIC, or an Application-specific integrated circuit, which essentially means that it focuses primarily on and is great for very specific AI workloads; in this case, OpenAI's inference needs, which allow it to run multiple models with significant efficiency gains in tow.

Richard Ho, who runs OpenAI's hardware program, told reporters on a press call that the results show "a very, very significant performance advance over state-of-the-art."

OpenAI ran SemiAnalysis's public InferenceX suite on GPT-OSS 120B, DeepSeek R1 670B, and Moonshot AI's trillion-parameter Kimi K2.5, at a nominal 8,000-token input and 1,000-token output. It scored a 1.9x efficiency win vs. GB200 on its own GPT-OSS model, and 1.7x and 1.5x on DeepSeek and Moonshot's offerings against a GB300 system. Interestingly, the figures for GPT-OSS 120B running on a GB300 compared to OpenAI's Jalapeño are not published.

It is important to point out here that there is a certain degree of cherry-picking to flatter OpenAI's own results: by choosing to compare ratios on a per-kilowatt basis versus a per-chip basis, while efficiency remains consistent, it does paint Jalapeño as potentially a much more potent competitor to Nvidia's last-generation offerings than it actually is.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Nvidia's GB300 might not have an efficiency win versus Jalapeño, but it remains a much more powerful chip in all tests, at a time when Nvidia is already rolling out Vera Rubin. Curiously, OpenAI has not published any information about how its chip stacks up against an HBM4-touting Vera Rubin, which Nvidia has presented as an efficiency juggernaut.

It is important to point out that Jalapeño's results also use single-token prediction throughout, with no speculative decoding and no prefill-decode disaggregation. Nvidia's production deployments commonly use multi-token prediction, and when OpenAI pits Jalapeño against a GB300 configured that way, the peak efficiency lead drops to roughly 1.5x.

OpenAI says it built the chip to keep model state local, writing that it "designed Jalapeño to minimize data movement and communication delays." Cores and HBM are divided into slices, each core slice holding a low-latency view of its own memory, with synchronization pushed onto a dedicated collective network. Each package pairs a compute die with six HBM4 stacks for 216 GiB at 15.4 TB/s, which is less capacity than the GB300's 288GB of HBM3E but considerably more bandwidth, and roughly 50 percent more memory per watt of rated power.

Every number published currently comes from A0 silicon, also known as the initial, first-run version of the chip. A more efficient B0 stepping is already in the fab with roughly 25 percent better performance per watt, and production is scheduled to ramp gradually across 2027.

Although it may not hold a candle to Nvidia's Vera Rubin, it might not have to; Alexander Harrowell of Omdia told CNBC that "this is the biggest competitive threat to NVIDIA," noting that roughly half of AI infrastructure capital spending comes from firms that already run custom chip programs or could. Yole Group's Adrien Sanchez framed it as pressure on Nvidia's inference margins specifically, the fastest-growing part of the business.

The timing of this announcement is both awkward and potentially suspect at a time when Nvidia just agreed to backstop $105 billion in financing for OpenAI's upcoming Ohio facility, even as Richard Ho told Bloomberg that the company continues to need a lot of Nvidia's chips, with the latter being "a really good partner." This is hardly surprising, given Jalapeño's limitations as an ASIC useful mainly for inference, while Nvidia's chips are key to training new AI models.

From Nvidia's perspective, this can be seen as a blow to its plans for a high-margin inference industry where one of the two major buyers of inference hardware is not only looking for a homegrown alternative, but is already well on its way to getting the job done.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png) 

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

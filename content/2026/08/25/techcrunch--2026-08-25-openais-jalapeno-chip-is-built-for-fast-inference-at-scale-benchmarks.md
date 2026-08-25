---
title: OpenAI’s Jalapeño chip is built for fast inference at scale, benchmarks show
  | TechCrunch
source_url: https://techcrunch.com/2026/08/25/openais-jalapeno-chip-is-built-for-fast-inference-at-scale-benchmarks-show/
source_site: TechCrunch
source_slug: techcrunch
scraped_at: '2026-08-25T16:50:51Z'
published: '2026-08-25T00:00:00Z'
description: Tested on SemiAnalysis’ InferenceX benchmark, Jalapeño registered both
  more tokens per user and more throughput per kilowatt than the currently available
  state-of-the art.
image: https://techcrunch.com/wp-content/uploads/2026/08/Jalapeno-chip-final.jpeg?resize=1200,900
---

At the Hot Chips conference on Tuesday, OpenAI shared a more detailed look at Jalapeño, including the first batch of benchmark results for the new system. Tested on SemiAnalysis’ InferenceX benchmark, Jalapeño registered both more tokens per user and more throughput per kilowatt than the currently available state-of-the-art inference processors.

“The bottom line is that the results show a very, very significant performance advance over state of the art,” said Richard Ho, OpenAI’s head of hardware, in a press call. “Jalapeño can serve more AI work per unit of power, while also returning responses more quickly. It’s very efficient to serve a lot of customers, but it can also be very low latency.”

Notably, that comparison is against an Nvidia Blackwell system — but by the time Jalapeño reaches full deployment, the competition may have advanced significantly. Ho estimated that Jalapeño would deploy at the end of 2026 “in very small volumes,” with more significant deployment coming in 2027.

First announced last October, Jalapeño was developed by OpenAI in close collaboration with Broadcom, with OpenAI’s own models assisting in the development process. The company plans to make Jalapeño a multigenerational platform, allowing AI products, models, chips, and memory all developed in concert.

Because of that full-stack approach, OpenAI was able to address specific phases in the inference process that often cause friction during inference processing. In particular, Jalapeño is designed to minimize delays during the prefill and communication phases of processing, which OpenAI says often act as bottlenecks.

“We designed Jalapeño to minimize data movement and communication delays,” the company said in a blog post presenting the results. “This means that model state, including the KV cache used while generating a response, can be explicitly placed and kept local while the system activates the right combination of compute, memory, and networking for each inference phase.”

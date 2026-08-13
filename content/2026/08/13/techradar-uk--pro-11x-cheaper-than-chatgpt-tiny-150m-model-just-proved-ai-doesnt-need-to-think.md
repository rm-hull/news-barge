---
title: Pathway says architecture can matter as much as model scale
source_url: https://www.techradar.com/pro/11x-cheaper-than-chatgpt-tiny-150m-model-just-proved-ai-doesnt-need-to-think-out-loud-to-be-smart
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-13T02:41:15Z'
published: '2026-08-13T00:00:00Z'
description: This tiny 150M AI model just challenged the idea that better reasoning
  requires bigger models and longer thinking traces
image: https://cdn.mos.cms.futurecdn.net/qP76MS2BAb7kSuWrvJXXYL-2560-80.jpg
---

![Hands typing on a tablet with AI superimposed in text in front](https://cdn.mos.cms.futurecdn.net/qP76MS2BAb7kSuWrvJXXYL.jpg) 

- **A 150M model reached 29.5% while costing just $0.0007 per task**
- **ChatGPT scored higher, yet its comparable reasoning runs cost substantially more**
- **BDH-CQ performs reasoning internally instead of generating lengthy intermediate text**

Pathway, an AI lab focused on building Post-Transformer architectures, has released new benchmark results for its BDH-CQ reasoning model.

According to the researchers, their 150M-parameter model scored 29.5% pass@2 on the public ARC-AGI-1 evaluation set.

It achieved this at a computed inference cost of $0.0007 per task, roughly eleven times cheaper than ChatGPT's underlying GPT 5.6 Luna (Low) model.

## A cheaper way to reason

Today, many AI tools waste computing power because of how they are designed, not because deep reasoning demands it.

"Today's AI pays a steep token cost for reasoning, but that cost is imposed by architecture, not by any law of intelligence," said Zuzanna Stamirowska, CEO and co-founder of Pathway.

“We show that a different architecture changes the game and opens up a whole new space in terms of how much intelligence per dollar.”

Amazon Web Services believes that BDH-CQ’s result is a promising step toward using advanced AI reasoning in real products more affordably.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

"Customers are increasingly exploring how to move advanced reasoning from experimentation into production, where performance, efficiency, and scalability all matter," said Nicolas Tarducci of AWS.

ARC-AGI-1, a widely used reasoning benchmark for AI systems, checks whether a system can infer an underlying rule from limited examples and apply it correctly to new inputs.

In this test, OpenAI's Luna model scored only slightly higher at 34.2%, yet running it still costs significantly more ($0.008 per task).

That price gap already includes OpenAI's recent 80% price cut on Luna, which began on July 30th of this year.

Further up the chart, Claude Opus 5 and Gemini 3.1 Pro reach 97–98% but cost around $0.5 – $0.6 per task, meaning the frontier's very top costs close to a thousand times more than BDH-CQ for the highest scores.

On the cheap end, Qwen3 235B costs over three times more than BDH-CQ while scoring worse than even its Low variant, so it isn't a real competitor on either price or performance.

"Pathway shows that model architecture, not just scale, can drive the next leap in AI reasoning," said Łukasz Kaiser, co-author of the original 2017 Transformer paper.

## Why it costs so much less

The efficiency gap stems mainly from a structural difference in how each system actually performs reasoning during inference computations.

Many reasoning AI systems generate intermediate text, adding one token after another before producing their final answers.

The longer that written reasoning becomes, the more it costs to run and the slower the AI responds to each request.

BDH-CQ works quite differently, quietly solving problems inside its own memory instead of writing everything down first as visible text.

Pathway also confirmed that early experiments already follow standard Transformer-like scaling laws across model sizes from 1B to 600B parameters.

The company also plans to extend this approach toward harder benchmarks, including mathematical reasoning, ARC-AGI-2, and eventually full ARC-AGI-3 evaluations.

If these efficiency gains hold across larger and more difficult tasks, cost rather than raw capability could increasingly separate rival reasoning systems.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

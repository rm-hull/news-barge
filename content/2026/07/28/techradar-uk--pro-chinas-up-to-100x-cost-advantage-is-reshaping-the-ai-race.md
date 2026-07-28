---
title: China's up to 100x cost advantage is reshaping the AI race
source_url: https://www.techradar.com/pro/chinas-up-to-100x-cost-advantage-is-reshaping-the-ai-race
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-28T10:44:26Z'
published: '2026-07-28T00:00:00Z'
description: China is catching up to the West when it comes to AI - what will this
  mean for the market?
image: https://cdn.mos.cms.futurecdn.net/8PUxwC4hX4bc3YwLSGjQcY-1920-80.jpg
---

![AI human interface](https://cdn.mos.cms.futurecdn.net/8PUxwC4hX4bc3YwLSGjQcY.jpg) 

Western labs still build the highest-scoring AI models. But the strongest Chinese alternatives now sit only a few benchmark points behind, while costing up to 100 times less, depending on the model and deployment scenario.

That changes the competitive question. The winner of the AI race may not be the company with the single smartest model, but the ecosystem that makes advanced AI affordable enough to deploy everywhere. That conclusion comes out of an analysis of 33 models from 15 providers, comparing reasoning performance, cost, and deployment control across the current market.

## A Six-Point Gap: The Top of the Leaderboard Has Nearly Closed

On GPQA Diamond, a demanding science reasoning benchmark, the leading models remain American,but Chinese labs are no longer a step behind in a separate tier.

They're inside the same competitive band as the leaders. Claude Mythos 5 leads at 94.4%, followed by Gemini 3.1 Pro at 94.3% and Claude Fable 5 at 94%.

But Qwen 3.7 Max already reaches 92.4%, while GLM-5.2 and DeepSeek V4 Pro score 91.2% and 90.1%.

The benchmark scores still favor the West. What they no longer do is fully explain the business decision.

## The Number That Matters More: Up to 100x Cheaper

A lower inference cost doesn't just save money on the same workload - it changes what companies can afford to build.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Lower inference costs mean more queries for the same budget, AI deployed across dozens of internal processes rather than a single premium use case, and cheaper support, analysis, and automation. They also make advanced models accessible to startups and mid-market companies that cannot justify frontier pricing.

Part of that price gap reflects a different safety model. Chinese open-weight systems generally come with lighter default guardrails than Western frontier models, so more responsibility for testing, misuse prevention, and compliance moves to the company deploying them.

A model that is slightly weaker but ten or fifty times cheaper can be commercially more competitive than the benchmark leader, because most business applications don't need the last few points of reasoning - they need a cost structure that scales.

This is a binary choice. The market has already split into two layers, and each follows its own logic.

At the bottom is the mass-market layer: classification, support, content generation, and routine business tasks. Here, “good enough” has already won, because users simply do not notice a difference of a few benchmark points, while every CFO notices a price difference of tenfold or more. Chinese open-source models are already taking this layer. Over the past year, the share of American models in OpenRouter traffic fell from roughly 74% to 20%, while Chinese models grew to almost half. By token volume, this is already their market.

At the top is the frontier: complex agentic tasks, coding, and everything where a model performs dozens of steps in a row without human intervention. Here, a small difference in quality compounds with every step, and over a sequence of 50 steps, a couple of percentage points in error rate can become the difference between completing the task and failing. That is why money behaves in the opposite way to traffic: enterprise budgets are concentrating around a few top models. Anthropic now accounts for around 40% of enterprise API spending, largely because of coding and agents. Tokens flow to the cheap models, while dollars flow to the best ones.

So there will not be a classic winner-takes-all outcome like in search. Models do not have a network effect, switching to another one costs almost nothing, and routing between several models is already a standard production architecture. In the end, we will have an oligopoly of a few frontier labs capturing most of the value at the top, and an ocean of cheap commodity models at the bottom capturing most of the volume. And that boundary will keep moving downward: what is frontier today will be commodity a year from now. That is why the value is not in any specific model, but in the speed of iteration and distribution.

And this brings us back to the original idea about regulation. If the West over regulates its own models, it will hand the entire lower layer to China, because for most business tasks, “good enough” is already enough. This is not a hypothesis. It is already visible in the numbers.

That's the real threat facing Western AI companies. The biggest risk is not that China immediately takes the top benchmark spot. It is that the market decides the top spot is no longer worth the premium.

## Beyond Price: Open Weights as a Second Advantage

Several of the strongest Chinese models: GLM-5.2, DeepSeek V4 Pro, and Qwen3.5 397B among them are released as open weights, meaning companies can run them on their own infrastructure rather than renting access through an API.

That gives businesses more control over their own data, less dependence on a single vendor's pricing or policy changes, and the ability to adapt a model's behavior to their own needs.

Chinese labs are not only offering cheaper versions of Western products. They are competing with a different model of adoption, built around lower cost, openness, and control — one that appeals directly to companies wary of vendor lock-in.

That debate has now moved into Washington. In a recent open letter, leaders including Satya Nadella and Jensen Huang argued against restrictions on open AI models, warning that limiting their development could weaken US competitiveness.

When the heads of the world’s most valuable companies all defend something at the same time, the first question is always about money. Open models benefit Nvidia because it sells the hardware to everyone who runs them. It is telling that OpenAI and Anthropic, whose businesses depend on closed models, did not sign the letter at first, and OpenAI joined only after its absence became the main story. Everyone here is defending their own business model, and that is normal. It just should not be confused with concern for humanity.

But on the substance, the signatories are right. This is the same story as open source. Giving software away for free once seemed irrational, and then Linux became the foundation of the entire internet. Closed and open models will coexist, each in its own segment. The more open models there are, the more competition there is, the cheaper the technology becomes, and the faster the entire industry moves.

The real context of this letter is not philosophy, but Washington’s attempt to restrict Chinese open models that have moved close to the frontier.

## Why This Pressures Western Labs

None of this means OpenAI, Anthropic, or Google are losing the AI race. Their models still lead on raw capability.

But that lead is becoming harder to monetize across every workload. As cheaper alternatives get close enough for routine business use, Western labs will face more pressure to defend premium pricing task by task rather than relying on benchmark leadership alone.

## Six Topics Chinese Models Won't Touch the Same Way

But the same models that offer more economic and technical freedom come with a different kind of constraint. Technical openness doesn't mean political neutrality.

Chinese models can offer more infrastructure control while remaining more politically constrained on China-related topics: Tiananmen Square and 1989, Taiwan's status, Xinjiang and the treatment of Uyghurs, the Hong Kong protests, criticism of Xi Jinping, and even politically sensitive references such as Winnie the Pooh.

Responses may be refused, redirected, or framed in line with the official Chinese position. This operates on two levels: a live filter on the hosted API, and a deeper alignment trained into the model itself, which survives even when a company runs the model on its own servers.

Enkrypt AI found that roughly 91% of DeepSeek R1's responses on China-related controversies still leaned pro-Beijing after standard jailbreak attempts. Self-hosting can provide data sovereignty, but it does not automatically create political neutrality.

## What Decides the Next Phase

The West still leads on maximum capability. The next phase of the AI race will not be decided by a few benchmark points alone. It will be decided by which ecosystem can turn advanced intelligence into affordable, scalable infrastructure for the wider market.

China has built a serious advantage on cost and control, but companies adopting that infrastructure will also need to account for its political constraints.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

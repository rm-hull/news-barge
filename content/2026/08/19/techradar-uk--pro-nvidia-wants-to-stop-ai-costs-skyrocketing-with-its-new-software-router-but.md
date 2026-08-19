---
title: Nvidia wants to stop AI costs skyrocketing with its new software router — but
  will it really make a difference?
source_url: https://www.techradar.com/pro/nvidia-wants-to-stop-ai-costs-skyrocketing-with-its-new-software-router-but-will-it-really-make-a-difference
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-19T01:49:38Z'
published: '2026-08-19T00:00:00Z'
description: Routing to the ideal AI agent to save compute
image: https://cdn.mos.cms.futurecdn.net/TwTNQ2vfXDVQryv6YuEVjU-2560-80.jpg
---

![Nvidia's Computex keynote pictured](https://cdn.mos.cms.futurecdn.net/TwTNQ2vfXDVQryv6YuEVjU.jpg) 

- **Nvidia's open source NeMo Switchyard 'smartly' routes each agent request to the cheapest model that can handle it**
- **The approach allows it to claim a 74% cost cut against a frontier-only model in return for a 6% reduction in accuracy**
- **NeMo Switchyard joins an increasingly well-established territory that already sees players such as RouteLLM, LiteLLM, and OpenRouter, in addition to in-house efforts at OpenAI and AT&T to save costs**

Nvidia has released NeMo Switchyard, an open source model router that sits between an application and a pool of language models and decides, per request or per turn, which model should handle a particular task.

The aim is to maximize efficiency by picking the right model for the right task: pushing frontier-level models to do simple tasks that much smaller or cheaper models could handle is not only inefficient, but also costly for enterprise customers.

This comes at a time when enterprise customers are already grappling with rising costs that can quickly spiral out of control as they increasingly adopt AI.

## An open-source addition to a growing chorus of AI routers

The problem Nvidia is trying to solve isn't new, and industry giants are already attracting a lot of attention. The emerging field itself is potentially lucrative, even if it focuses on cutting costs, and major players are looking to get in on the action; Stripe's upcoming $7+ billion acquisition of OpenRouter, underscores this.

Switchyard is no different from its peers; it is essentially a proxy that uses a routing algorithm to decide which AI model to send queries to, while delivering an answer in the format that the calling application or user requires.

It accepts OpenAI, Anthropic, and Responses API requests, translates between them, and documents the selected model, decision rationale, token usage, and latency for each call, enabling transparency and letting it tweak or tune its approach over time.

This makes sense compared with a one-size-fits-all approach that would otherwise be prevalent in a world with limited frontier-level AI compute, as LLMs continue to grow larger and more demanding. One example is what Nvidia points to: Nemotron Parse, a one-billion-parameter model primarily designed to extract structure from PDFs.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The question remains, however, whether such an approach is always feasible. Leveraging such a routing tool comes at a cost; LangChain's test of Nemotron 3.5 Lightning found that its judge model, which determines whether the agent is still on track after each turn, consumed up to 21.2% of total cost, second only to what it spent on Claude's Opus 4.8.

Running a more optimized judge model could therefore yield greater savings or lower overhead, but it could also hinder cases where users need a more basic AI model, and the judge model increases costs by reading or checking output at every turn.

A secondary concern would be variance: while costs are noticeably lower than running just Opus 4.8 in testing, it does swing from anywhere between $2.16 and $3.61, a mammoth 67% movement essentially guided by when it escalated queries to a bigger or smarter model. This tradeoff makes cost hard to predict: while routing lowers average spend, it widens the distribution around it.

LangChain also says users should not use Switchyard if their workloads are short or latency-sensitive; it estimates it adds about 700ms of latency because the judge model has to read all output.

Nvidia's take here is simple: it is pushing a packaged, open-source solution that offers a broad set of integrations in what is essentially a relatively fragmented space. Routing work to smaller open-weight models pushes inference toward hardware enterprises own, which Nvidia sells.

At the same time, cheaper inference per task has historically meant more inference, not less, which is the outcome a company selling accelerators would choose to woo enterprises, many of which are still on the fence when it comes to directly investing in the hardware that powers it all.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

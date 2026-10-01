---
title: Don’t follow the herd on AI cost optimization – control compute this way
source_url: https://www.techradar.com/pro/dont-follow-the-herd-on-ai-cost-optimization-control-compute-this-way
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-01T13:26:49Z'
published: '2026-10-01T00:00:00Z'
description: Cut AI costs with business logic, not cheaper models
image: https://cdn.mos.cms.futurecdn.net/rNZmVCrdHzszaDCyTrBWmj-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations: []
organisations:
- AI
- Alteryx
- Future plc
- Kimi K3
- LLM
- LLMs
- TechRadar Pro
- TechRadarPro
- Uber
---

![A representative abstraction of artificial intelligence](https://cdn.mos.cms.futurecdn.net/rNZmVCrdHzszaDCyTrBWmj-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Remember Tokenmaxxing? Just some months ago, reports of tech companies tracking and gamifying token usage as a measure of employees as AI ‘power users’ caught global attention. There’s been an 180-degree turn since. The gradual pivot from experimentation to at-scale deployment of AI agents comes with a bigger bill. Uber bemoaned blowing its entire AI budget for 2026 in four months.

Chief Product Officer at Alteryx.

This has led many to talk up the idea of model routing and leveraging open source models to optimize AI spending. Excitement around new Chinese models, like Kimi K3, offering cut-price access to near-frontier capabilities has fueled the enthusiasm.

Targeting which models are used for which work is a legitimate way to optimize AI costs. But it’s narrow-focused when used in isolation. Organizations lacking the discipline to define when an LLM should be used, and where running data processing makes sense elsewhere, are guaranteed unnecessary token consumption and inflated costs.

Recognizing this is a welcome opportunity to look beyond reducing the cost of tokens as the single route to optimize AI costs.

## The folly of running LLMs as an analytics engine

LLMs are undoubtedly transformational, and people like using them. But there’s value in scrutinizing how exactly they’re being used. File reconciliation, applying business rules, compliance checks, interpretation of source documents. LLMs might be able to get the job done but not cost-efficiently.

That’s because LLMs constantly rebuild context to formulate answers to such problems. Standalone, LLMs aren’t tapping into the organizational knowledge that gets to the bottom of solutions quickly without blowing through tokens as models verbally reason through the best approach to land on a final answer that satisfies an individual business’s definitions, policies and context.

The other issue is that many problems put to LLMs are repeatable. It’s unnecessary to have models fire up from square one to answer the same problem time and time again, across user conversations and over time.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

This gets to the root of the limits of a narrow focus on model selection. Because asking models to rediscover information at every corner – overlooking the revenue calculation, margin and compliance know-how that already exists internally – is wasteful no matter the model. Limiting unnecessary token usage must be part of the equation.

## The cheapest token is the one you never generate

If it wasn’t clear already, a key bottleneck driving AI costs is that many AI systems aren’t connected to business logic. They’re missing a business logic layer, where analytics workflows for repeatable tasks, factoring in organization-specific rules and definitions, live. Such layers are also where compliance guardrails can be set and applied to analytics output generally.

When integrated with a business logic layer, LLMs have a better option at their disposal to answer certain kinds of user queries. Imagine an employee asking an LLM to calculate their team’s current margin performance.

Standalone, a model could pull data from a wide range of relevant sources, blow up a massive context window in the process and still get the answer wrong if it fails to factor in internal definitions for concepts like margin. A business logic layer, on the other hand, offers models pre-built workflows calculating core margin variables daily. The model works with the output.

Repeatable workflows, drawing on analytics workflows and business context that already exists, help to optimize AI costs. Business logic layers also have the benefit of integrating with cloud data platforms as well as LLMs, to act as a connective tissue that averts potential duplication of compute cost.

For example, compute happens in a cloud data platform; the outcome is carried over into an analytics workflow which an LLM can draw on. The need for intensive LLM compute to make sense of data from the cloud data platform is limited.

## The critical need to be right

Putting granular cost management aside, there’s also something to be said for the long-term cost benefits of injecting sturdy business logic into AI inputs and outputs. A lack of business logic limits confidence in AI tools and, therefore, slows the rollout that delivers ROI.

This is quite simple. When it comes to queries around business domains like tax, compliance and finance – we see deterministic questions that require deterministic answers. It’s business logic, and its mobilization, that holds the key to those answers.

This is going to become harder to ignore as the rollout of agents picks up pace in workplaces. Agents move quickly and can do so in the wrong direction without being rooted in the right rules and logic. In an enterprise setting, 1,000 agents across a workforce can’t produce 1,000 different answers to every question and be a force for good. A source of business truth, via a business context layer, keeps things in check.

## A new angle for cost optimization

Model selection as a means to optimize AI costs is limited without limiting unnecessary token consumption. In the process, organizations get better outcomes from the rollout of AI – just as rollouts of agents take off. Ultimately, organizations that combine trusted workflows, governed business logic and targeted use cases will see the best returns from the technology.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

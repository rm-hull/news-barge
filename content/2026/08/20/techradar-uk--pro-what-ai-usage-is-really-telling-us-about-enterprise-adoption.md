---
title: What AI usage is really telling us about enterprise adoption
source_url: https://www.techradar.com/pro/what-ai-usage-is-really-telling-us-about-enterprise-adoption
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-20T16:47:23Z'
published: '2026-08-20T00:00:00Z'
description: For business adoption, AI usage should matter more than model rankings
image: https://cdn.mos.cms.futurecdn.net/qP76MS2BAb7kSuWrvJXXYL-2560-80.jpg
---

![Hands typing on a tablet with AI superimposed in text in front](https://cdn.mos.cms.futurecdn.net/qP76MS2BAb7kSuWrvJXXYL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Many public AI conversations still revolve around leaderboards: which model ranks highest, which provider is 'winning', and which benchmark score matters most. But for organizations building AI in production, those questions are becoming less useful than understanding how AI is actually being used.

One reason is the growing debate around "tokenmaxxing" - the practice of maximizing AI usage, often driven by internal adoption targets, incentives or leaderboard-style competitions.

But focusing on token consumption can encourage activity for activity's sake, rather than measuring the business value AI actually delivers.

CTO at Vercel.

Recent examples, including Amazon reportedly shutting down an internal AI leaderboard and Uber capping employee AI spending after rapidly exhausting its annual budget, highlight the risks of treating usage as the primary success metric.

Yet the latest data suggests something more nuanced is happening. According to Vercel's July AI Gateway data, token volume grew by 29% in June while spend increased by 27%, with the average price per token remaining flat. Rather than simply consuming more AI, organizations are becoming deliberate about where they deploy different models and how they balance cost with performance.

The teams building real AI systems are increasingly routing tasks dynamically across multiple models depending on cost, reliability and reasoning. For example, a low cost model may be useful for handling summarization, while a premium reasoning model is reserved for high stakes decisions.

In practice, AI is more about orchestrating layers across many models than building systems around a single provider.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The latest AI Gateway data shows organizations distributing workloads across different classes of models rather than relying on a single provider. Open-weight models now process 29% of gateway tokens while accounting for less than 4% of spend, while frontier models continue to dominate higher-value reasoning workloads.

Rather than taking a one-size-fits-all approach, organizations are selecting different models according to the task at hand.

## Beyond the leaderboards

In the early stages of enterprise AI adoption, teams were encouraged to experiment aggressively, push models further and explore new use cases. This helped accelerate adoption, but it also created a simplistic assumption: that more AI automatically meant more value.

Token volume and spend both grew by nearly 30% in June, yet the average price per token remained flat. Organizations are continuing to invest heavily in AI, but they're becoming strategic about how workloads are distributed across lower-cost and premium models.

That pattern mirrors previous changes in technology, such as the early cloud computing era, when businesses expanded aggressively before refining efficiency. AI adoption is following a similar trajectory, but moving at a much faster pace.

For AI teams, the most useful measure of AI is not cost, but outcome. A workflow that automates weeks of engineering effort may be far more efficient than a lower-cost workflow that produces unreliable outputs and creates downstream operational costs that outweigh the initial savings.

The question is not how little AI a team can use. It is how effectively AI can be deployed to solve meaningful problems.

## AI is changing workloads

Traditional chatbot workflows are relatively straightforward: prompt in, answer out. Agentic systems behave very differently.

AI agents reason, call tools, execute code, retrieve information, question databases and iterate across multiple steps before completing a task. Every one of those actions consumes tokens.

As a result, AI workloads are becoming increasingly agent-led. A single request may now involve chains of tool calls, validation loops and provider switches happening behind the scenes, which changes the economics entirely.

Back-office agents are the most expensive workload per token on the gateway, accounting for 5% of total tokens but 14% of total spend. More complex, business-critical workloads need greater reasoning capability than simpler AI tasks.

That means rising usage is not always a symptom of inefficiency. In many cases, it reflects the growing complexity and capability of AI systems themselves.

## Infrastructure as the differentiator

As organizations adopt more models and providers, reliability becomes harder to manage.

Reasoning tasks, multi-agent workflows and complex orchestration chains can cause significant strain on model providers. If one model fails midway through execution, an entire workflow can break.

As a result, fallback routing is becoming essential infrastructure for production AI. Vercel’s AI Gateway report in May found around 3.5% of requests require rerouting due to failure, timeout or rate limiting issues.

Without dynamic routing between providers, those requests would simply fail. For end users, provider instability is invisible as they do not care where the issue originated; they only experience whether the application continues working.

So as AI systems become more agentic, resilience and orchestration become just as important as model capability itself.

## The end of the single-model era

Single-provider strategies are becoming difficult to maintain. New models are launching constantly, pricing is changing quickly, and performance leadership is shifting from workload to workload.

A model that is best for coding today, may not be best for retrieval, customer support or reasoning workflows tomorrow.

None of this is really about picking a winner. It is about building AI systems that can adapt and absorb whichever model is best this week, because that answer changes fast and will keep changing.

The teams that treat multi-model orchestration as infrastructure are the ones that won’t need to rebuild when the next model ships.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

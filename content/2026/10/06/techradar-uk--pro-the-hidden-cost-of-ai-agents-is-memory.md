---
title: The hidden cost of AI agents is memory
source_url: https://www.techradar.com/pro/the-hidden-cost-of-ai-agents-is-memory
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-06T15:55:05Z'
published: '2026-10-06T00:00:00Z'
description: Agentic AI's real cost lies in memory management
image: https://cdn.mos.cms.futurecdn.net/PAztEScphfxGJfYno5NjrL-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
- Personal Finance & Investing
people: []
locations:
- AI
organisations:
- AI
- AWS
- Anthropic
- Future plc
- SurrealDB
- TechRadar Pro
- TechRadarPro
---

![A robot standing thoughtfully in front of a giant digital display with code on it](https://cdn.mos.cms.futurecdn.net/PAztEScphfxGJfYno5NjrL-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

The first generation of enterprise AI projects taught businesses how to retrieve information. A user asks a question, the system finds relevant context, and a model turns it into an answer.

CEO & Co-Founder of SurrealDB.

AI agents change that equation because they retrieve information dynamically and adjust their own state in the process. As tasks evolve they juggle everything from plan development, and outbound tool calls, to updating records, and recording results.

Multiply that activity across hundreds or thousands of agents and the data layer starts behaving very differently - with significant implications for both cost and accuracy. These implications are becoming major considerations when moving agentic AI projects from pilot to production.

## Why pilots can hide the real cost

## Memory becomes an operational system

Early pilots tend to be narrow by design. Typically, there’s one team working with a limited dataset and relatively simple, short-lived interactions. Take as an example requesting a summary of a document. The model completes a request and that task is done. Here, model access, tokens, and context retrieval appear to account for most of the bill.

When shifting from passive chatbots to multi-agent systems, however, the economics flip. Traditional generative AI costs scale linearly with users, whilst the cost of running multi-agent deployments tends to escalate with task complexity. Proof-of-concept expenditure typically multiplies as tasks become more complex.

For example, AWS puts a text-based proof of concept handling about 100 interactions a day at around $40 a month. Its estimate for an agent-based proof of concept using a knowledge base and guardrails at roughly the same volume is around $840 a month. Anthropic's write-up on its multi-agent research supports this finding.

The data shows multi-agent systems use 15x more tokens than chat interactions and that economic viability requires the value of the task to be high enough to justify the expense.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

In multi-agent systems, therefore, it’s easy to see why costs accrue. Agents use dynamic loops, tool calls, retries, and context transfers to complete a task. But there’s another important dimension - agents need to remember and reason across increasing volumes of data.

Agents have longer operational lives than a typical chatbot session. They have to remember yesterday's actions, preserve the evidence behind a decision, and make that information available to other agents in the fleet. Every completed task becomes a new state.

As the agent fleet grows, the business is paying not only for the next answer but also for the expanding operational provenance required to operate efficiently, and safely.

Early generative AI systems often treated memory as context - retrieved when required. Persistent agents create a different requirement. Memory becomes a live operational system that is constantly updated.

That matters for both performance and cost. A narrow write path can create contention as more agents update records. Separate copies of the same context increase storage and synchronization work, and keeping every historical record on the fastest storage tier makes rarely used information unnecessarily expensive.

When designing the data layer to support agentic fleets, the service level dictates how memory is accessed and managed. Leaders should establish how quickly each kind of memory must be available, who can update it, which agents should share it, and how long must it remain immediately accessible.

## Designing memory for a fleet of agents

Three main principles will become increasingly important as the variety and complexity of agent deployments grows.

The first is concurrency. Leaders should ask whether write capacity can grow as the number of agents grows. Infrastructure designed mainly for read-heavy applications may behave very differently once large numbers of autonomous processes start updating state at the same time.

The second is shared memory. If several agents are working on the same customer, asset, or process, creating separate copies of the same context can introduce cost and inconsistency. A common source of state can make collaboration easier, provided access controls and provenance remain clear.

The third is separating active memory from historical memory. An agent may need the last few minutes of a workflow immediately, while records from six months ago might only be required for an audit or an unusual query. Treating those two categories identically is an expensive default.

Frequently accessed state can remain close to the compute layer, while older information moves to lower-cost durable storage. Compute can then scale according to current activity rather than the total memory accumulated since the system was launched.

How historical changes are stored poses a similar question. Saving every full version of a record makes retrieval straightforward but consumes more capacity. Saving only incremental changes uses less space, but reconstructing an old state can take longer. Periodic snapshots combined with smaller changes between them can offer a useful middle ground.

## What to establish before scaling

These read like technical considerations, but they set the economic model for the deployment, and they are cheaper to resolve before an agent fleet expands than after.

Once it is accepted that agents create information as well as consume it, earlier design choices become measurable rather than abstract. For example, how much state each agent writes and how often; how many agents may update the same customer, asset, or workflow at once; how much memory needs immediate access versus cheaper durable storage after a day, a week, or a month; and whether context can be shared safely rather than copied per agent.

Each of these steps carries a cost, and together they determine the figure that decides viability at scale - the cost per task is both the number of agents and the volume of retained memory.

Resolving these considerations before expansion changes the design of the pilot. A team can test the write load, retention rules, and the expected sharing model in production while the system is still small, which is the point at which hidden costs are both visible and cheap to fix.

## AI economics start below the model

Even if model prices continue to fall and inference becomes more efficient, large-scale agent deployments will still create a growing stream of operational data that has to be written, shared, protected, retrieved, and retained.

The cost of that activity will depend heavily on the architecture underneath the model, but companies planning the next stage of AI adoption should measure the whole lifecycle of an agent task, including the memory it leaves behind. Doing that before a pilot becomes a fleet gives technology leaders a much clearer view of whether an AI system will remain economical when it reaches production scale.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

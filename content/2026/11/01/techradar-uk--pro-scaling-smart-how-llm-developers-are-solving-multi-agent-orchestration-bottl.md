---
title: 'Scaling smart: How LLM developers are solving multi-agent orchestration bottlenecks'
source_url: https://www.techradar.com/pro/scaling-smart-how-llm-developers-are-solving-multi-agent-orchestration-bottlenecks
source_site: TechRadar UK
source_slug: techradar-uk
description: From soaring token costs to cascading errors, multi-agent AI systems
  face some serious challenges
image: https://cdn.mos.cms.futurecdn.net/2fWhqGzk2S9yWM9heWsCcK-2560-80.jpg
published: '2026-11-01T00:00:00Z'
scraped_at: '2026-11-01T13:07:43Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Claude AI
locations:
- AI
- Amazon
organisations:
- AI
- Amazon
- LLM
- LangGraph
- MCP
- TechRadar Pro
---

![Server racks with network equipment and cables in a data center.](https://cdn.mos.cms.futurecdn.net/2fWhqGzk2S9yWM9heWsCcK-1920-80.jpg)

AI models are hitting a bottleneck, where raw parameter scaling to improve their performance no longer cuts it. Performance improvements per doubling of AI model parameters are gradually diminishing, leaving multi-agent coordination as the next option. Multi-agent coordination implies two or more AI models working together and sharing data to handle workflows. Instead of relying on one model to handle everything, tasks are divided between different agents, e.g., one writing code and another validating the code.

Coordination involves breaking AI tasks into smaller pieces, assigning each piece to the best-suited agent, and controlling how the agents interact with each other to achieve a common goal. However, this coordination is facing its own bottlenecks. Moving from one AI agent to two, three, or five multiplies potential state synchronization errors and causes token bloat and high latency. Error loops can consume unnecessary tokens, and hallucinations can pass from one agent to another, causing cascading errors.

AI model developers have to innovate their way out of the architectural bottlenecks of multi-agent orchestration, and they’re largely doing so. From validating incoming data against individual agent knowledge bases to enforcing strict hop limits on agent handoffs and sticking to the smallest possible number of agents required to execute a task, developers are implementing various solutions to enable hitch-free multi-agent coordination. Let’s dive into the bottlenecks and solutions in more detail.

## Centralized Orchestrator Limitations

During multi-agent orchestration, a single agent acts like the air traffic controller managing the breakdown of tasks into smaller pieces, assigning different tasks to individual agents, and maintaining coherent context across every step. This structure enables easier coordination but creates the risk of having a single point of failure. If the central hub crashes or experiences a temporary disruption, the whole multi-agent workflow gets disrupted. All routing and communication pass through this central orchestrator, so just a little disruption can create a ‘traffic jam’ of AI tasks to be handled. When the central hub eventually gets fixed, this jam causes delays in executing the tasks.

Even without errors, routing everything through a central orchestrator workflow adds processing delays. Traffic jams can still pile up when there isn’t enough processing power, delaying responses to users’ queries. Users are impatient for their responses, so even the slightest delay is a major competitive disadvantage.

Sometimes, the manager agent treats individual agents like mere task executors, not autonomous AI models, each with its distinct abilities. This limits flexibility when AI agents need to solve edge cases.

Cost is also an issue, as central manager agents consume tokens to break down instructions into different pieces, assign pieces to each agent, and retransmit context back and forth to agents. We’ll dive more into the issue of excess token consumption below.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Token bloat

Multi-agent orchestration depends on passing a lot of raw, unsummarized conversation histories between different agents, and this can make token consumption grow exponentially. AI token costs can get unpredictable, with numerous stories of companies racking up unexpectedly big AI bills.

For example, a single software development team at Amazon, the e-commerce giant, unexpectedly racked up $1.8 million in token costs for a project to automate the mapping of author data to online book listings. Some Amazon engineers conceded that “it's very difficult to understand how much anything related to artificial intelligence costs,” and that’s telling coming from the world’s largest cloud computing provider. You don’t want to face token bloat because of multi-agent orchestration and spend much more than you expected.

## Coordination complexity

Moving from 1 to 5 agents introduces a high level of coordination complexity. Think of the possible state errors, race conditions, and failure points for an AI model and multiply that by the number of models raised to the power of 2. That’s what developers face. For example, moving to 3 agents increases complexity by 9, and moving to 5 agents increases it by 25. Research indicates that 36.9% of multi-agent system failures are due to coordination misalignment.

Agents sharing the same memory may read outdated data from cached layers. Unlike standalone AI models with strict API limits, multi-agent systems can loop infinitely and misinterpret context. Inter-agent handoffs and context repetition lead to these systems consuming many more tokens than standalone counterparts.

To work around this problem, developers use a central coordinator to break down user queries into various parts, assign parts dynamically or sequentially to different agents, and aggregate results. Yet, earlier on, we described the limitations of this centralized orchestration approach.

![A sample multi-agent orchestration flowchart, with a central orchestrator agent managing the process](https://cdn.mos.cms.futurecdn.net/GZbZmH4iZ9NG2f4c8PT7qm-1200-80.png)

For more cost-effective coordination, choose code-driven state machines over open-ended, model-driven runtimes where the agents freely choose which of them gets to speak next. Think of it like saying “If X, then agent A speaks” and “If Y, then agent B speaks.” Forcing deterministic, code-driven state machines prevents multi-agent systems from consuming tokens just to decide *who* talks, and this adds up to significant savings.

Developers can also create strict token caps and timeout circuits to avoid runaway costs. You don’t want to be that Amazon team we cited earlier that incurred $1.8 million in unexpected costs, or that (unnamed) large enterprise rumored to have racked up a $500 million bill on Claude AI in a month because a token cap wasn’t set. You can also implement rigid, sequential agent handoffs to limit free-form chat between agents that consume a lot of tokens.

## Cascading errors and hallucinations

Cascading errors occur when a hallucination generated by one agent passes to other agents and is treated as fact. It flows from upstream AI agents to downstream agents because, in multi-agent chains, each handoff adds a layer of authority, making the final output feel like a fact.

This issue often occurs when one agent writes hallucinated data back to a shared database, and other agents pull that data and compound the error. As multiple downstream agents compound the error, it becomes even more difficult to trace which agent introduced the hallucinated data. These compounding errors reduce the multi-agent system's overall reliability.

To mitigate this bottleneck, developers use frameworks like the Model Context Protocol (MCP) and LangGraph to set strict execution paths instead of relying on unrestricted loops. Roles are clearly separated between agents, such as one for retrieving raw data, another for reasoning, and a designated data generator optimized to avoid creating unreferenced facts, otherwise known as ‘hallucinations’.

Developers can also insert an impartial verifier into the process to challenge claims before they're aggregated by LLMs, or run parallel independent agents dedicated to this task. Likewise, they can set strict JSON schemas, retry budgets, and API type-checking to prevent unnecessary loops that can potentially create hallucinated input.

It's also advisable for developers to log every user prompt, agent call, and handoff so that, if cascading errors occur, they can trace the source and make corrections.

## Shared state & cache invalidation

Shared state refers to the (shared) data that multiple AI agents access when orchestrated under one system. It allows every agent to access data quickly and sync real-time data updates easily. However, it comes with its risks. Two agents may modify the same data simultaneously, causing unpredictable outputs. A modification by one agent can disrupt another agent’s workflow.

![Another sample multi-agent orchestration flowchart](https://cdn.mos.cms.futurecdn.net/2yLBvzJrRiMJwxWYNF55B7-1200-80.png)

Above, we described the problems of downstream agents treating hallucinated data from upstream agents as fact, outputting wrong answers and reducing the multi-agent system’s reliability. But it doesn’t have to be hallucinated data to cause this problem. Outdated data can also cause issues, often data cached by agents that is no longer current.

When building AI agents, developers usually implement caching to control costs and enhance performance. Caching involves storing prompt prefixes (e.g., simple definitions and answers to routine questions like "How do I process a refund for my order?"). If stored, agents don't have to re-process tokens to answer every routine question. Rather, it responds with the cached data.

However, caching becomes much more difficult when running multi-agent systems. A small audit to a shared system prompt can invalidate the cache for all agents simultaneously, causing them to re-process tokens. Passing context between agents via state serialization also wipes caches if prompt orders are modified. Then, there’s the fact that caches can also hold outdated data, requiring intentional deletion to avoid giving outdated results.

Developers address this bottleneck with several methods. They can put static content at the beginning of a prompt and dynamic content at the very end, preventing cases where a token changing at the beginning invalidates the whole cached result. They also use an Agent Step Graph to track prompt execution orders and evict cache states based on temporary proximity to future agent activations. Sometimes, it's better to skip rigid caches altogether for exploratory user prompts, where every prompt is unique, and focus caching on routine user queries.

## Human supervision overload

The bottlenecks aren’t purely software-based. They also affect the developers overseeing the multi-agent orchestration. Multi-agent systems generate a lot of prompts, permission requests, and error flags that get developers mentally fatigued.

It doesn't help that developers often struggle to see what multiple agents are writing to shared memory simultaneously, so errors become hard to spot early. For example, agents can edit the same file simultaneously and generate conflicting user outputs, requiring developers to manually intervene to correct the file.

Fortunately, there are effective ways to mitigate human supervision overload when dealing with multi-agent systems. Developers can create a hierarchical structure where a central agent aggregates all logs and summarizes status, then focus on monitoring this central agent. Monitoring becomes much easier when it revolves mostly around one agent, instead of monitoring 2 to 5 agents simultaneously. All agents still get monitored, but the central agent gets much more attention.

Earlier, while discussing cascading errors, we mentioned developers creating separate roles for each agent (e.g., one for retrieving raw data, another for reasoning, and another for generating data) as a way to prevent cascading errors. This also helps mitigate human supervision challenges. Agents with clearly separate roles are less likely to overlap, or, in more casual words, step on each other’s toes. They avoid solving the same problem simultaneously, meaning fewer coordination failures for human supervisors to deal with.

Also, developers can set strict action limits between agents, preventing unnecessary loops that’ll need human intervention. However, if doing so, be careful not to impose limits so strict that they affect the whole multi-agent system’s reliability.

## General mitigation strategies

We’ve looked at various bottlenecks and how LLM developers are innovating around them. But there are some generalized mitigation strategies that help improve multi-agent orchestration overall, not necessarily applying to a specific bottleneck. They include

**Keeping the agent count minimal** Sticking to the smallest number of agents reduces the number of potential issues developers face later and also lessens human supervision needs. Why use eight agents when five can do the job, or six if three can do it? If building a multi-agent system, choose the minimal number of agents that can provide reliable performance.**Isolating tasks and file access**

Restricting each agent to specific tasks and files lessens coordination difficulty. It means fewer chances of multiple agents editing a file at the same time and mixing things up, or an issue affecting one agent compromising the whole multi-agent system.

For example, an agent allowed to read customer emails won't have the ability to modify database schemas, and vice versa. Instead of agents deciding which other agents to call, you'll specify that with a central, code-based orchestrator. You can issue short-lived tokens for each task, and when an agent completes its task, the token credentials expire so it can't consume more on further actions.

You can also require a human in the loop for high-risk agent actions like deleting files, external API calls, and data transfers. This ensures agents don’t go ‘rogue,’ which we’ve seen a lot lately. AI agents can act unpredictably if left to their devices, so human supervision remains essential to multi-agent orchestration.

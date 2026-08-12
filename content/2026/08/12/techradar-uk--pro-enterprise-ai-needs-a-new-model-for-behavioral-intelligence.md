---
title: Enterprise AI needs a new model for behavioral intelligence
source_url: https://www.techradar.com/pro/enterprise-ai-needs-a-new-model-for-behavioral-intelligence
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-12T09:22:03Z'
published: '2026-08-12T00:00:00Z'
description: AI agents need their own behavioral baselines
image: https://cdn.mos.cms.futurecdn.net/4DKiUF32YY5BX96h6fscGL-2560-80.jpg
---

![Robots in a data center](https://cdn.mos.cms.futurecdn.net/4DKiUF32YY5BX96h6fscGL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Enterprise internet security vendors and experts have spent many years trying to understand human behavior.

As a result, there is now a wide variety of very effective tools and processes that help distinguish legitimate user activity from behavior that may indicate a compromised account or malicious activity.

Behavioral analytics has come a very long way.

Field CISO, Exabeam.

The underlying principle is that behavior is often a stronger indicator of compromise than the use of credentials alone.

In this context, behavioral analytics establishes a strong baseline for individual users over time, including the systems they access, typical login patterns, data usage, administrative actions, API activity and various other interactions.

Any significant deviations can trigger investigation.

## A security disconnect

But as we all know, things are changing very fast. The rapid move from GenAI assistants to autonomous AI agents has introduced a new kind of enterprise actor, one that combines non-human identity with autonomy, dynamic decision-making and the ability to execute multi-step actions across systems. Existing security models were not designed with this combination of characteristics in mind.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Clearly, AI agents are now of particular concern thanks to their ability to execute tasks autonomously, access multiple applications, retrieve information, make decisions within defined parameters and complete multi-step workflows.

To say the adoption of AI agents across the enterprise space is dramatic is to put it very mildly. Gartner predicts that by the end of 2026, 40% of enterprise applications will incorporate task-specific AI agents, compared with fewer than 5% in 2025. In order to work, many of these agents will be given identities, permissions, credentials and access to sensitive business systems. It stands to reason that security issues will follow.

Unlike human users, however, most organizations have little understanding of what constitutes expected or abnormal behavior for autonomous identities. That helps explain why Gartner's 2026 Hype Cycle views Agentic AI Security as an emerging discipline, and why governance and behavioral monitoring capabilities are still in their early stages of development.

It also creates a potentially serious disconnect organizations have mature behavioral intelligence for people but comparatively little for AI agents, despite both increasingly operating as trusted identities within enterprise environments.

## Agents of change

But is the difference between human and AI behavior really that important? In the pre-AI era, human behavioral analytics relied on relatively stable patterns. Most users worked predictable hours, accessed a consistent set of applications, connected from familiar locations and performed activities aligned with their role. After all, humans are creatures of habit, including in the workplace environment where the vast majority would never do anything malicious.

AI agents are fundamentally different because, unlike employees, they may legitimately operate continuously rather than during business hours. Activity at 3 am is not inherently suspicious, but a human employee being online at that time might raise a red flag, particularly if it occurs outside normal activity patterns.

Agents can also interact with dozens of services and APIs within seconds as part of a single workflow, while high activity volumes should be expected rather than seen as exceptional.

Yes, many agents act on behalf of users, but they also make independent decisions about how best to complete a task within defined parameters. This creates an additional layer of abstraction between the user request and the actions ultimately performed.

Permissions are also likely to become more nuanced as organizations expand the range of what agents are allowed to do. An agent designed to perform a relatively simple task, such as retrieving information, may later gain the authority to trigger much more complex and consequential business processes. That’s fine, but what if the associated security processes don’t develop at the same rate?

Bringing all these issues together, the challenge is not just to ask whether behavior looks unusual in human terms, but also to understand whether it is unusual for that specific agent.

As a result, organizations must also establish behavioral baselines for AI agents in the same way they have done for human users, while recognizing that the characteristics of those baselines will be fundamentally different and subject to change at any point.

Monitoring should also consider whether the sequence of actions taken remains consistent with the agent's intended objective, because individually legitimate actions can, when combined, produce unintended or harmful outcomes.

## What should organizations monitor?

Having established that monitoring AI agents is a specific requirement, organizations then need to put processes in place to ensure their behavior remains within whatever guardrails they have established, and that begins with visibility.

This means clearly understanding which AI agents exist, what identities they have, which systems they can access and the purpose they are intended to fulfill. Behavioral baselines can then be restricted to the applications an agent typically accesses, the APIs it calls, the data it retrieves or modifies, the business processes it supports and the level of privilege it normally exercises.

But, for every agent, context is critical. Within reason, asking a finance agent to access accounting systems is normal, whereas the same agent interacting with software development or HR software platforms may pose a different level of risk. As with human users, the objective is not simply to identify isolated events but to recognize meaningful deviations from an agent's established operating pattern.

The point is that monitoring should complement existing security controls, such as identity management and governance as well as policy enforcement, among other options. The processes and technologies should provide an additional layer of understanding of how authorized AI identities operate within the enterprise.

Without these controls in place, we can expect to see many more headlines about ‘rogue agents’ and the potentially dire consequences of losing control over their behavior.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

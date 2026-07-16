---
title: Most enterprise AI governance is already out of date
source_url: https://www.techradar.com/pro/most-enterprise-ai-governance-is-already-out-of-date
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-16T10:20:53Z'
published: '2026-07-16T00:00:00Z'
description: Governance that can't keep up with the technology isn't governing anything
image: https://cdn.mos.cms.futurecdn.net/4DKiUF32YY5BX96h6fscGL-2560-80.jpg
---

![Robots in a data center](https://cdn.mos.cms.futurecdn.net/4DKiUF32YY5BX96h6fscGL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

When organizations first started formalizing AI policies, the problem they were solving for was narrow: keep employees from sharing sensitive data with a public model. A clear, manageable risk with a clear, manageable response.

Chief People & AI Transformation Officer at Zapier.

What those policies didn't account for was how quickly AI would evolve, or how far the organizational guardrails would fall behind it.

Most companies are still running governance frameworks written for that original moment, applied to a technology that looks nothing like it did then.

## What happens when outdated governance meets AI agents

The governance frameworks most organizations are running were designed to manage exposure, not enable work—and that design shows.

Organizations are running agents that autonomously query databases, update records, and trigger downstream workflows, across connected systems, at a pace no approval cycle was designed to match.

Those agents can be governed, but vague policies won't cut it. The governance has to be specific enough to translate into actual system-level constraints, like which systems the agent can access and under what conditions.

Governance that can't keep up with the technology it covers isn't governing anything. It's just documentation.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## 4 questions to audit your AI governance framework

**1. Can your employees find out right now what AI can access on their behalf?**

When someone deploys an AI tool or agent at work, that tool is often connected to real systems (email, CRM, databases, and calendars) on behalf of the person using it. Without a governance framework that clearly outlines what those connections look like or what the tool is authorized to do within them, your organization doesn't have a reliable way to assess what's actually exposed.

To make this clear, build and maintain a permissions inventory: a living record of which AI tools are approved, which systems each tool can connect to, what actions it's authorized to take, and which team or individual owns each integration. If your organization uses an AI governance platform, much of this can be tracked and managed there rather than maintained manually.

Either way, it doesn't need to be overly sophisticated out the gate. But it does need to be current discoverable.

**2. If an AI agent takes a wrong action, how quickly can you revoke it?**

Agents take actions, sometimes sequences of them, across connected systems. When something goes wrong, the ability to stop it quickly depends entirely on how access was set up in the first place. If credentials are scattered across sessions, scripts, and individual tool configurations, revoking access to one system means tracking down every place that credential was used.

Consolidating agent credentials under a centralized auth system changes that. Each agent operates under a defined identity with explicit, scoped permissions, so removing access is a single action with a clear audit trail and no cleanup exercise required.

Standards like the Model Context Protocol (MCP) are designed specifically for this. MCP can give agents a structured, auditable channel to access external systems through OAuth rather than credentials embedded in prompts or scripts. For organizations evaluating how to centralize agent access, it's worth understanding what's possible when the connection layer itself is built with governance in mind.

**3. Does your governance policy describe what's permitted, or only what's prohibited?**

A policy built around prohibitions tells employees what they can't do, but it doesn't tell them what they can. For humans, that leaves a gray zone they have to interpret. For agents, the problem is more concrete: an agent given a prohibition list and no permitted-use definition has no reliable boundary for what falls inside or outside its scope.

The fix is to define use cases affirmatively: approved tools, permitted system connections, and authorized actions. That gives both employees and the agents they deploy a clear framework to operate within, and it makes the governed path the default one.

**4. Does your governance framework specify what your AI agents can access and act on, at the system level?**

A framework that addresses AI in general terms (for example, responsible use and acceptable outputs) gives humans enough to make informed decisions about how they use AI.

Agents require something more specific. When you deploy an agent, it operates based on two things: the instructions and context it's been given, and the systems it's been granted access to. If your governance framework isn't precise enough to be included in that context, then it isn't governing the agent. Governance that actually covers agents defines access at the system level: which systems, which actions, and under what conditions.

In practice, that looks like provisioning agent access through an identity and access management system, assigning each agent a defined role with scoped permissions, and logging every action it takes against those permissions.

## Build for what's next, not just what's now

AI capabilities are moving fast enough that some of what's true today about how agents operate will look different in a year. Governance frameworks that are current now will need to be revisited.

Getting the fundamentals right today matters precisely because the landscape keeps shifting. That means treating governance as an ongoing operational practice: reviewing access definitions when new tools are deployed, auditing permissions when agent capabilities expand, and updating permitted-use frameworks when the technology changes scope.

The cadence matters as much as the content.

The principle that holds, regardless of what AI looks like next year, is this: governance that can't keep pace with the technology it's supposed to cover isn't governing anything. Building governance that's designed to evolve is the work.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: Why 'never trust, always verify - repeatably' security strategy for AI Agents,
  starts after login
source_url: https://www.techradar.com/pro/why-never-trust-always-verify-repeatably-security-strategy-for-ai-agents-starts-after-login
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-28T12:46:58Z'
published: '2026-10-28T00:00:00Z'
description: Securing AI agents requires continuous verification of actions after
  login
image: https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej-2000-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations: []
organisations:
- AI Agents
- Agentic AI
- Cato Networks
- Conversational AI Agents
- Fully Autonomous Agents
- Future plc
- GenAI
- MCP
- Semi/Full Human Guardrails
- TechRadar Pro
- TechRadarPro
---

![A robot hand touching a locked digital shield blocking a human from accessing data](https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Modern digital security frameworks were originally built to correct a flawed historical assumption: the belief that if a user or system was inside the company network, they could be trusted implicitly. Over the past decade, the rapid rise of cloud storage, subscription-based business software, and remote working destroyed that network boundary.

In response, our security models shifted focus. We began verifying the identity of the person trying to log in, inspecting the hygiene of their computer, requiring multiple verification steps during login, and continuously checking that they were who they claimed to be.

Chief Information Officer and Global Chief Information Security Officer at Cato Networks.

This model works well when a human is logging in to perform a task. But with the rise of autonomous AI agents, the real security risk no centralized at the login screen. It starts after access has been granted.

An AI agent does not behave like a standard piece of software. It reads a human instruction, pulls context from company databases, utilizes multiple sets of tools, chooses its own digital tools, connects to external software communication links, and triggers complex automated workflows.

Verifying the initial login simply tells you that the agent is officially recognized by your system. It tells you absolutely nothing about whether the next action the agent plans to take is safe, ethical, or correct, focus has shifted to context.

## The evolution of the machine identity problem

IT teams have already experienced a simpler, quieter version of this challenge with non-human identities. For years, companies have used automated service accounts, security tokens, and digital certificates to allow different software programs to talk to one another.

Most security leaders are all too familiar with the risks these credentials present: accounts are created for a temporary project, granted permanent access to database files, and then completely forgotten long after the project has ended. They become silent, unmonitored backdoors into the network.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

However, AI agents complicate this familiar problem by introducing the element of independent judgment.

A traditional service account follows strict, pre-written code. By contrast, an AI agent interprets a high-level goal, analyses real-time context, selects its own tools, and actively decides how to proceed.

As a result, security policies can no longer stop at the front door. We must protect every internal data or compute asset the agent can reach and monitor every single decision it makes.

## Matching autonomy with executive control

To manage this risk, security leaders must separate two distinct concepts: how much independence an AI agent has, and what level of file access it holds.

The combination of these two factors dictates the level of control required. For example, a basic agent that merely summarizes long documents only needs limited reading rights and clear activity logs. However, an agent designed to update sensitive, production databases, access code repos, write new types of code, or alter business workflows requires mandatory human approval steps, strict operational boundaries, and a clear path to reverse any mistakes.

We can categorize these digital workers into 3 distinct levels of independence, applying tighter security controls as their autonomy increases:

1. First, there are Conversational AI Agents (GenAI), productivity agents usually built and managed by employees & teams as part of their productivity (e.g. managed agents, self hosted chat bots). When driving security, we must enable proper RBAC authorization, associated with the employee and team, ensuring access to non-sensitive or production-related data, enabling logging, and validating the response to ensure proper integrity.

2. Second, there are Agents Acting with Semi/Full Human Guardrails (AI Agents), such as customer support tools that draft emails or prepare database updates for review. Here, security teams must validate the parameters of the tools being used and require a human to approve any actions involving writing, deleting, spending money, or sending information externally. All above controls apply

3. Finally, there are Fully Autonomous Agents (Agentic AI), which reset passwords or trigger complex workflows on their own. These require the strictest boundaries, from visibility (agent architecture, tool usage, and more) and focus on active set of controls. The controls include strict rate limits, continuous real-time policy checks, network access restrictions, run time security controls (Public/Private Cloud) continuous identity and minimal authorization verification, and finally complete, unalterable audit trails.

The industry is leaning toward autonomous agents seeking human approval upon abnormal behavior, can that be triggered in your agent?

## The need for real-time inspection

To enforce these policies, security teams need a dedicated vantage point within the network. They must be able to inspect the human prompt, the agent's response, the digital tools being used, and the movement of data while the work is actually happening.

This requires an architecture that can discover all active agent activity across the business, govern how those agents use internal tools, and maintain complete visibility over data flows and automated workflows.

The true value of this approach lies in context. When the behavior of an AI agent is viewed alongside network traffic, user activity, and cloud database logs, security teams can investigate incidents with clear evidence. They can instantly see which agent ran, who in the organization owns it, what data was moved, and which automated tool was called.

For business leaders, this means cleaner, more consistent governance across human users, software applications, and digital agents alike.

## How to begin: Start with a single workflow

Securing this new landscape does not require a complete overhaul of your entire security department overnight.

Start by picking a single AI workflow that is currently in use or close to being launched. Map out its digital identity, its level of independence, the files it can access, the tools it uses, the points where a human must approve an action, and how you would undo a mistake.

This simple mapping exercise will quickly highlight where your security gaps lie. If you cannot see the agent's actions in real-time, approve its decisions, block its access, or explain its behavior after the fact, your security controls are simply too far away.

From there, build a baseline on how your secure your coding agents, AI harness (or AI orchestrator) up to utilizing of tools/skills/MCP and moving forward to data assets access and utilization of identity that will allow you to set the correct foundations and guard rails.

The core principle of a "never trust, always verify" security model must follow the agent into its daily work. The most meaningful decision is no longer who is logging in, but whether their next action should be allowed to happen, under these exact conditions, right now.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

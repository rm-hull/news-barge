---
title: Why AI coding agents keep stalling before production and the governance controls
  that fix it
source_url: https://www.techradar.com/pro/why-ai-coding-agents-keep-stalling-before-production-and-the-governance-controls-that-fix-it
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-13T14:55:59Z'
published: '2026-07-13T00:00:00Z'
description: AI agents need governance controls before reaching production
image: https://cdn.mos.cms.futurecdn.net/qP76MS2BAb7kSuWrvJXXYL-2560-80.jpg
---

![Hands typing on a tablet with AI superimposed in text in front](https://cdn.mos.cms.futurecdn.net/qP76MS2BAb7kSuWrvJXXYL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Across 100 engineering organizations, 61% already run AI agents. Yet almost none trust them enough to bring them into production.

There are a few reasons for this. Firstly, agents are prone to making mistakes that humans know to avoid through experience. They move at a much faster pace, and by their nature operate autonomously. If something goes wrong, there’s often no audit trail or visibility into what they are doing across the organisation.

This is problematic when a rogue agent inevitably leaks credentials, hits unauthorized repositories, or burns through cloud budget before anyone notices.

This unreliability is why most organizations keep agents away from anything that matters.

CEO of Coder.

However, the real problem is not the agents. It’s the absence of governance around using them. The controls already exist, and have for a long time.

They are the same principles that have been applied to human engineers for years: minimal privileges, audit logging, identity management, and scoped access. Though familiar, companies struggle to apply these fundamental rules.

To ensure organizations get off to a good start with deploying AI agents, they should implement three simple governance controls: isolate, scope, and approve.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Isolate by default

Start with isolated, ephemeral workspaces. Every task that is spun up from a clean template should be erased the moment it is completed. No shared state or bleeds between runs. This means that should something go wrong, the damage will be confined to that task, and nothing beyond it.

Then from that workspace, all agents should have zero outbound access by default. Not limited. Zero. An explicit ‘allowlist’ then defines exactly which domains, methods, and paths an agent can touch. Everything else gets blocked. And even with narrow access, sensitive systems such as GitHub or Salesforce should get read-only access also.

Your agent is in an isolated workspace. Network connectivity is limited. Now it’s time to control tool calls. Model context protocol (MCP), for instance, is how agents invoke external tools, including file systems, databases, and APIs. Without airtight guardrails, an agent can reach any MCP server available to it.

The danger is that this is a significant and largely invisible attack surface. Proxies that sit in front of those tools allow administrators to define an approved list, filter at the per-tool level, and log anything that tries to reach outside the boundary.

## Scope permissions and real-time monitoring

Even a well-isolated agent can cause problems if it’s running with more permissions than it needs. Agents should never inherit a user’s full credentials. API keys should only carry the permissions required for that specific task, and nothing more.

In addition to scoped identities, there must be clear visibility. Streaming every request through real-time monitoring and alerting teams when an agent makes 10x its typical API calls, contacts a new domain, or starts burning tokens unusually fast will provide timely, and actionable signals.

Identity-aware LLM routing ties it all together. Authenticating users through existing SSO, and routing all model requests through centrally managed keys solves the problem of API key sprawl. Without this measure of control, hundreds of loose keys with no attribution or clear revocation path quietly accumulate.

## Approve agentic tasks with a human in the loop

Think of an agent as a talented junior employee. High output, eager to help, but not yet trusted to push to production unsupervised. AI agents should generate output but not decide what ships. This is where human approval gates, backed by existing role-based access controls, come in. Humans must be held mutually accountable for their agent’s output. This is as much a mindset as a technical control.

However, there is one area where you should assist human oversight: model selection. Not every task should go to the same model. For example, regulated data has different requirements than content generation. Routing by policy ensures that compliance requirements are met without relying on individual developers to make the correct call every time.

Full audit trails make the whole lot accountable. Every prompt, every tool call, every model interaction should be mapped to an authenticated identity and exportable to whatever observability stack is already in place. It should always be clear which authenticated user sent which prompt to which model, and why.

## Embed governance in your infrastructure, not your apps

Overall, the goal is to empower organizations with the confidence to deploy their AI agents safely without slowing down their developers, agents or the business. Ensure this happens by laying down a governance layer to make AI agent adoption sustainable. But there’s a catch. Implement governance at the infrastructure layer. There are two reasons why.

Firstly, it avoids duplicating policy for every AI stack you deploy. Secondly, it ensures a consistent governance across a very fast-changing world where agents, models, and harnesses will leapfrog each other monthly. You do not want to rewrite governance policies at the pace of AI change.

Done right, infrastructure-lever governance makes AI production ready. Security teams with visibility over what agents are doing will be more inclined to approve more, compliance teams with clear audit trails will sign off faster, and developers who trust the guardrails will be able to push further.

Those enterprises that build in governance now will not just have better security posture, they’ll outpace competitors waiting for sign-off to run their first pilot.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

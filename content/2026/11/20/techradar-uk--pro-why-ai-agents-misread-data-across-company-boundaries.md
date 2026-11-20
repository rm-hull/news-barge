---
title: Why AI agents misread data across company boundaries
source_url: https://www.techradar.com/pro/why-ai-agents-misread-data-across-company-boundaries
source_site: TechRadar UK
source_slug: techradar-uk
description: 'Cross-environment context for AI agents: anarchitectural perspective'
image: https://cdn.mos.cms.futurecdn.net/wZAaq2s2qH4tHBJTEBNZXM-2560-80.jpg
published: '2026-11-20T00:00:00Z'
scraped_at: '2026-11-20T11:33:34Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- Jira
organisations:
- AI
- Challenge Organizations
- Exalate
- Future plc
- Jira
- SLA
- ServiceNow
- TechRadar Pro
- TechRadarPro
---

![An abstract pattern of blue lines and orange-yellow dots on a dark blue background, to represent a digital environment](https://cdn.mos.cms.futurecdn.net/wZAaq2s2qH4tHBJTEBNZXM-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

AI agents can connect and act on data in systems like Jira and ServiceNow. However, sometimes misinterpretations can lead to unreliable output.

One such agent assumes “Priority” means the same thing in both systems, draws inferences, and syncs accordingly. If these inferences reach a customer ticket, a Priority 1 incident misses SLA, and the impacted teams are unaware, because the agent indicated it was being handled. The output was plausible.

Co-founder and CEO of Exalate.

When AI agents misconstrue their own results, they often lack “context,” and a common approach is to give them more permissions.

## AI Agents and Cross-Company Context: The Challenge

Organizations associate more permissions with data volume. They believe AI agents get more “context” if their scope is broad, i.e., read more fields or records.

The real problem is interpretation, i.e., what data in one system contextually means in the other, how each field corresponds to its counterpart, or how workflow states map with each other.

This information lives in the relationships between connected systems and differs for every environment.

An AI model trained on enterprise tooling understands how Jira and ServiceNow work, but lacks the knowledge of how each environment is operationally built.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

For instance, it may not have the context of a custom field: “Customer Escalation," or understand that a “Pending” status in one system is the same as “Waiting on external” in another, and can draw incorrect inferences.

The damage an incorrect AI inference causes in a single organization is limited.

The same inference in a cross-company environment, with broader access levels, creates a bigger impact.

Here, the AI agent needs knowledge of the most current information, system precedence when conflicts occur, and the relevant mapping on the other side.

In a single organization, an internal authority can provide this information and ensure the agent receives it. This authority approves field mappings, enforces their definitions, maintains central catalogues and audit trails, and defines data ownership frameworks.

This authority is absent across organizational boundaries, and the agent cannot derive this information alone. Plus, companies do not formally agree on field naming or discuss visibility into how the other side configures its environment. Data structures and naming conventions are not formally documented, only assumed, and subject to either party changing terms independently. This makes the job of an AI agent even more difficult.

## Configuration Changes Make Matters Worse

Consider a support team connecting their Jira to an engineering team using ServiceNow in different organizations.

It involves defining what syncs, what passes over, and what is strictly restricted. This is set during implementation but can change over time.

New field mappings can be added, but they are generally inert and do not break existing processes.

The real risk lies in removal. For instance, if the support team removes a dropdown in Jira for operational reasons, the original data is no longer reflected in ServiceNow. Since no errors are generated, the ServiceNow team remains unaware of this change.

From the support team’s perspective, the change was internal and didn’t need external communication.

In a single organization, the agent with access to both sides can detect this field change and flag it for a human review.

In a cross-company setup, the agent on the affected side has no visibility into the changed configuration, so even the first step is unavailable. What it requires is to determine whether a change on one side has broken a dependency the other side relies on. That is a meaningful capability to have.

## The Architecture Models for Cross-Company Context

A system’s native AI capability has complete context of its own configuration but none outside. When using this model to connect systems, cross-company context remains essential but, as discussed, is difficult to achieve.

A centralized intermediary can, in theory, understand both systems but holds credentials in a third-party location. Enterprises accept this arrangement within their own perimeters but refuse it beyond their boundaries. They might also face some resistance from their legal and compliance teams.

A third decentralized approach keeps each organization fully in control of its setup, running its own independent piece of software and credentials that never leave the system. Only derived context, which includes structured descriptions of field mappings, configurations, and their relationships, crosses boundaries.

Out of the three, only this approach preserves organizational autonomy without storing credentials in a third location.

## What a Solution Must Do For Cross-Company Context

System credentials must remain local to the environment they belong to. Only defined, agreed-upon, shared context crosses the boundary: field definitions, status mappings, and data transformation rules, not credentials or system access.

The agent scope must also be strictly limited to configuration metadata: what fields exist in the system and how they are defined within it. The business semantics are also important, i.e., what the field is used for.

It should not have access to sensitive data like customer records or information under data protection obligations. The solution should support this architecturally. The AI agent must be able to differentiate between something that doesn’t exist (absence) and something it’s not allowed to view (non-visibility).

If an agent not permitted to access a field reports that the field does not exist, it decides on a false pretext.

Consider an agent accessing a field “Escalation Owner” and receiving no response. It treats this “no response” as confirmation that the field does not exist and proceeds. It’s possible that the field exists, but the agent isn’t permitted to access it. The agent needs to notify this correctly.

A system returning “field not found” and one returning “access not permitted” are communicating two entirely different scopes. The solution must be able to distinguish between them correctly.

Change detection must operate at the right level of detail. A modified field can be a simple log entry, but a change breaking a dependency on the other side needs action. Most solutions deliver the former but leave the latter out ambiguously.

## Conclusion

Cross-company context is valuable not because it oversees both systems but because it knows the limits of what it can see and reports them accurately.

In this setup, an AI agent stating it cannot verify an answer is more reliable than the one that always answers.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

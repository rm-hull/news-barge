---
title: Why "I approve" can become the most dangerous button in enterprise AI
source_url: https://www.techradar.com/pro/why-i-approve-can-become-the-most-dangerous-button-in-enterprise-ai
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-24T11:48:48Z'
published: '2026-08-24T00:00:00Z'
description: Why human oversight alone fails in agentic AI
image: https://cdn.mos.cms.futurecdn.net/wZAaq2s2qH4tHBJTEBNZXM-2560-80.jpg
---

![An abstract pattern of blue lines and orange-yellow dots on a dark blue background, to represent a digital environment](https://cdn.mos.cms.futurecdn.net/wZAaq2s2qH4tHBJTEBNZXM.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

At 2 a.m., an automated remediation agent detects a problem on the network, traces it to a misconfigured policy, validates through the harness that the proposed fix operates within the given policy boundaries and fixes it. The network stabilizes. Nobody’s notified.

In the morning, a human reviews the agent's daily insights: a summary of all the changes executed, with links to the logs, audit trails, reasoning and root cause behind them, confirms everything has been properly resolved and moves on. That is what Human-on-the-Loop looks like.

At another organization, at 4 a.m., a DIY-built, vibe-coded remediation agent detects a problem on the network, traces it to a misconfigured policy, and fixes it. The network stabilizes. Nobody’s notified. In the morning, a human reviews the logs, assumes the issue has been resolved, and moves on.

Where's the difference?

CTO EMEA and Head of AI Engineering, Extreme Networks.

The difference is that, in the DIY scenario, the logs only tell part of the story. They don't show that the agent made three other changes to get there, which were broader than intended, and the decisions behind those changes weren’t flagged because nothing in its constraints required them to be.

This is what the move toward Human-on-the-Loop can look like without the right controls in place. No dramatic handover. Just a series of small, reasonable delegations that gradually build into something nobody explicitly signed off on.

And it's happening faster than most leaders realize. According to recent research, 57% of IT leaders expect to remove humans from the loop within a year or less, and 79% already treat AI agents as "users" who require their own identity management and governance controls.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The shift to agentic AI is happening faster than most organizations are prepared for, both in terms of governance and the ability to evaluate autonomous systems.

## The illusion of "I approve"

The answer to autonomous AI has long been quite simple: keep a human in the loop. Somebody who reviews the output, hits approve, preserving accountability. Except it isn't, not really. Reviewing every action doesn't automatically create accountability, and it also prevents organizations from realizing the full benefits of autonomy.

Rather than reviewing every individual action, humans should be focused on evaluating outcomes, ensuring the system operated within its intended boundaries, and providing feedback that improves its performance over time.

Approval can become a ritual without meaning. As systems prove reliable and the number of alerts multiply, humans sometimes start to treat intervention as something that isn’t often needed.

The approval can become more of a click than a considered choice. And when something goes wrong (for example, a misconfigured policy, an automated remediation that turns into an outage), the question of who was responsible is difficult to answer.

It also reinforces a broader shift: one of the most important human capabilities becomes critical thinking and the validation of hypotheses, rather than the execution of tasks.

And something else is happening. Humans are transitioning from doing to reading before approving – a fundamental change in the day-to-day work of most of us.

Also, attribution isn't the same as provenance. A log that records what an agent did tells you almost nothing about why, or what shaped that decision. When things go wrong, those are the things you need to know.

## Non-human identities and the new network population

When AI agents act on your network, querying systems or making configuration changes or routing traffic, they are effectively users. They need credentials, policies, guardrails, explainability, and audit trails just like human operators.

Most organizations haven't caught up with this. Identity frameworks were built for people, and applying AI agents to them as a kind of afterthought creates exactly the sort of shadow access that security teams spend their lives trying to eliminate.

The near-80% of leaders who already treat agents as governed identities are ahead of the curve. The rest are collecting risk they can't quantify, until it crystallizes into an incident.

To get this right you have to treat each agent as a principal with bounded permissions, time-limited access and a clear revocation path, along with a complete record; not just of what it did, but of what it was allowed to do and why.

## Autonomy isn't given, it's earned

Network and security teams already know how to do this. Every enterprise has access control frameworks that govern what humans can reach and when. A junior engineer doesn't walk in on their first day with total production access. They gradually earn it, and this same logic needs to apply to AI agents.

We're not quite there yet. Too often, autonomy is treated as all-or-nothing. That isn’t the right model. Trust when it comes to humans doesn’t work like that, and it shouldn’t with AI either. Start agents in suggestion mode and let them prove themselves within clearly defined limits before expanding what they can do. And make sure every decision leaves a trail that explains not just what happened but the reasoning behind it.

As the use of autonomous AI grows, organizations will need to balance human oversight with systemic governance. People remain responsible for reviewing not only the outcomes AI produces, but, where necessary, the actions it takes and the reasoning behind them.

However, as the volume and complexity of autonomous decisions increase, this oversight should be complemented by infrastructure that embeds identity, policy enforcement, observability and accountability. Together, these controls help ensure AI actions remain transparent, traceable and aligned with organizational intent.

## Building multi-agent systems that hold up under pressure

The more capable these systems become, the more organizations will move toward multi-agent architectures. This is where specialized agents each own a piece of a workflow and hand off context as they go. That's where things get complicated.

A single agent misbehaving is traceable. A chain of agents, each acting on the outputs of the last, is much harder to untangle when something goes wrong unless the right architecture and governance are in place. You need to know what each agent knew, not just what it did.

## Do the boring part

Two organisations deploy the same AI-powered networking agent. One of them has done the unglamorous work: setting up tight permissions, proper identity controls and audit trails that actually answer questions. The other one hasn't.

You won't know the difference until something breaks.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

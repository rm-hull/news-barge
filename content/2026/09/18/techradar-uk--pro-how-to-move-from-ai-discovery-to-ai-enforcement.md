---
title: How to move from AI discovery to AI enforcement
source_url: https://www.techradar.com/pro/how-to-move-from-ai-discovery-to-ai-enforcement
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-18T13:00:12Z'
published: '2026-09-18T00:00:00Z'
description: Discovery found the AI. Enforcement has to stop it.
image: https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej-2000-80.jpg
categories:
- Technology & Software
- Science
locations: []
people:
- Run
organisations:
- AI Enforcement
- AIUC-1
- Blocking AI
- Future plc
- IDE
- MCP
- Microsoft
- TechRadar Pro
- TechRadarPro
---

![A robot hand touching a locked digital shield blocking a human from accessing data](https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Most enterprise shadow AI programs have completed step one. They ran discovery, found more AI in the building than expected, and built a spreadsheet. Then the program stalled.

This pattern is nearly universal. Discovery is genuinely useful, and it's also where the easy work ends. Knowing that 37 agents are running, roughly the enterprise average per Microsoft's February 2026 Cyber Pulse research, doesn't change the fact that more than half operate with no security oversight or logging.

An inventory tells you what happened. Enforcement decides what happens.

CMO of Morphisec.

## What enforcement means for AI

Enforcement is the ability to change the outcome of an AI action while it's occurring, not report on it afterward. For an agent, that means one of four interventions: block the tool from running, scope down what it can reach, gate a specific action behind approval, or terminate the process mid-execution.

These aren't interchangeable: choosing between them is most of the work. Blocking is blunt and generates the most complaints. Scoping is the most durable and hardest to configure. Gating works until the approval queue becomes a formality people click through. Termination is the last resort; it needs to land before the action completes.

## Why network blocking keeps failing

Blocking AI domains at the network edge was the first control most organizations reached for. It's easy to deploy and explain to a board, and it stops a shrinking share of the actual risk. AI stopped being a website.

Local models make no outbound call to inspect. Embedded copilots run inside licensed applications, so their traffic looks like the vendor you approved. IDE and command-line agents, and MCP servers on localhost, never cross a network boundary you control. Personal devices remain the oldest gap, worse now that AI tools are free and everywhere.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## The permissions problem underneath

Here's what makes AI enforcement harder than the access control problems before it: an agent acts using a human's identity and entitlements. The log shows the employee read the file, or the credential belongs to a person or service account provisioned for something else. Existing identity controls just ask whether that principal is allowed to perform the operation, and the answer is usually yes.

The question identity infrastructure was never built to answer is whether this action, taken by software on the human's behalf, is one the human would have sanctioned. That's why emerging standards like AIUC-1 treat unauthorized agent actions, access privilege enforcement, and unsafe tool calls as separate controls, not folded into general access management. That separation is the right instinct.

## Where enforcement has to sit

Enforcement has to sit at the point where an action executes, the only place the decision is deterministic. Controls at the instruction layer, input filtering and prompt guardrails, evaluate text before it reaches a model. They're worth deploying and they reduce volume, but they're probabilistic, and separating instructions from data inside a language model is still not solved.

So build for the case where the instruction gets through. If the agent's tool call is scoped, gated, or stopped at the moment it fires, the origin of the instruction stops mattering. A malicious prompt, a poisoned document, and an honest mistake all produce the same blocked action. That's the property you want: an outcome that doesn't depend on correctly classifying intent.

It's also why endpoint and runtime placement keeps winning the architecture argument: nearly every AI interaction eventually becomes a process on a device, where a local model, an embedded copilot, and a browser tab all look like what they are: code executing.

## How to start without breaking anything

Enforcement projects fail loudly, so sequence them to fail quietly:

1. Pick one category, not the whole inventory: a small group of prohibited tools with an obvious sanctioned replacement.
2. Run in monitor mode for two weeks. You'll find the legitimate workflow nobody told you about. There's always one.
3. Name an owner for every agent before enforcing against it. An unowned agent can't be exempted or fixed, and that turns a block into an incident.
4. Turn on blocking for the smallest viable scope, then measure the complaint rate before expanding.
5. Wire the enforcement log into your evidence pipeline from day one; retrofitting is harder than building it in.

## What to tell leadership

Lead with a number they won't like: the count of AI agents running with no owner, no logging, and no control. It's usually large enough to fund the program by itself. Then commit to a second number: enforcement actions taken in the first quarter, broken out into blocks and approvals. A control that never stops anything isn't a control. It's a report with better branding.

Discovery is a list. Enforcement is a decision.

The inventory was worth building. It's just not the deliverable. An AI agent moves faster than any human in your approval chain, and it doesn't wait for the quarterly review. The organizations that come out of this era in good shape will be those that can stop an action before it completes, and prove afterward exactly which rule stopped it. Find them, then be able to stop them.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

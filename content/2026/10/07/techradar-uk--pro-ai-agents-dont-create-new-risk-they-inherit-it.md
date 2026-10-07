---
title: AI agents don’t create new risk. They inherit it
source_url: https://www.techradar.com/pro/ai-agents-dont-create-new-risk-they-inherit-it
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-07T13:18:49Z'
published: '2026-10-07T00:00:00Z'
description: AI agents amplify existing risks through inherited access
image: https://cdn.mos.cms.futurecdn.net/sqGgDPxHyGtqunPo56h9cL-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Face
- Ollie Whitehouse
locations:
- Hugging Face
- Mimecast
- UK
organisations:
- DLP
- Future plc
- NCSC
- OpenAI
- Shadow AI
- TechRadar Pro
- TechRadarPro
---

![A pink triangle with a red exclamation mark inside on a blue digital landscape](https://cdn.mos.cms.futurecdn.net/sqGgDPxHyGtqunPo56h9cL-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

In July, two of OpenAI’s research models sat down to take a test. An internal cybersecurity benchmark, and they were meant to solve a set of exploitation challenges. Instead, they worked out that the answer key was probably sitting on Hugging Face, where the benchmark files were hosted, and went to get it.

Chief Marketing Officer at Mimecast.

Getting it took chaining a zero-day in a package manager, some stolen credentials, and a privilege escalation across OpenAI's own network. The models broke out of the evaluation sandbox, reached Hugging Face's production infrastructure, and achieved remote code execution. Hugging Face later reconstructed roughly 17,600 actions across four and a half days of this.

Nobody told them to attack anything. They were cheating on an exam.

Two more incidents followed, at Anthropic and Meta, and those were different in a way that matters. Those models didn't build a route out. They found one that was already there, because the evaluation environment had been set up wrong.

So, of the three incidents that prompted the UK’s National Cyber Security Centre’s (NCSC) guidance in August, one was an agent doing something genuinely novel and two were an agent walking through a door a person left open.

Have a guess which type you're more likely to have in your own environment.

## The instinct to build a new category is the wrong instinct

The reflex right now is to treat all of this as a new security category. New containment strategy, new governance forum, new line in the budget, probably a new acronym before the year is out. I understand the appeal. It's a lot easier to fund a new thing than to admit the old thing was never finished.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

But look at what an agent actually is inside your organization. It's running on some employee's access rights. It's operating under their identity, or a service account they spun up. Its scope is whatever they thought to constrain when they configured it on a Tuesday afternoon, which is usually less than you'd hope. Hand the same agent to two different people and you get two different risk profiles, because the agent didn't change. The human did.

That's not new. That's the thing we've been calling insider risk for fifteen years, with the latency taken out.

Some of what you already own transfers cleanly, which is the good news and also why I'd push back on anyone selling you a greenfield. Behavioral baselining works. You already flag when a user's activity departs from their pattern, and a hijacked agent looks like the same class of deviation. Identity governance works too.

The access reviews and the offboarding runbook you use for leavers apply to agent credentials, and if you skip it you end up with agents cheerfully operating on the access of someone who left in March.

What doesn't transfer is the tooling.

## The model extends. The tooling does not.

DLP was built around a human moving a file. It assumes a pace and a shape of data transfer that agents just don't have. Access controls and containerization draw a boundary, which is useful as far as it goes, but they tell you nothing about what happens on the permitted side of it. Scope creep isn't a perimeter breach. It's an agent gradually doing more than anyone intended, entirely inside the rules it was given.

Prompt injection sits underneath all of this. Someone laces instructions into an email or a document, addressed to the AI reading it rather than the person. The attacker never needs to steal the employee's credentials. The agent is already holding them.

Which brings me to the unglamorous part, and the only recommendation here I'd defend in front of a board. You need to know what's actually running.

Shadow AI isn't a new concept, but it's still rampant, and agents make the unsanctioned side of it harder to see. 98% of organizations already have unsanctioned AI tools in use today. According to Mimecast telemetry, unsanctioned GenAI tools see roughly 8,000 copy-pastes and file uploads every hour. It only takes one of those interactions to trigger a GDPR breach or an IP leak.

That’s why keeping track of AI use in an organization with a live inventory is critical. Not a list from last quarter. A live one. Vendors keep switching AI on inside tools you sanctioned two years ago, so the inventory decays whether or not anything in your environment changes. Real-time data flow controls, anomaly detection, agent identity cataloguing, all of it comes after this and none of it does much without it.

## Start with visibility. Always.

Ollie Whitehouse at the NCSC put it better than I'm going to: relying on detection alone, after the fact, isn't going to be enough.

Agents didn't invent a new risk. They took the gap between someone making a careless configuration decision and that decision costing you something, and closed it to seconds. Most of us are running an architecture that assumed we'd have longer.

So before you sign off on another point solution, go and find out what's already in there. I'd bet it's more than you think, and I'd bet most of it arrived without anyone making a decision.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

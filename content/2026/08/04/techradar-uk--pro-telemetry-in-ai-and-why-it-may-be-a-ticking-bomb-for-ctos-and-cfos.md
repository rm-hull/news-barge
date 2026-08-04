---
title: Telemetry in AI and why it may be a ticking bomb for CTOs and CFOs
source_url: https://www.techradar.com/pro/telemetry-in-ai-and-why-it-may-be-a-ticking-bomb-for-ctos-and-cfos
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-04T14:36:41Z'
published: '2026-08-04T00:00:00Z'
description: Governing telemetry before it governs you
image: https://cdn.mos.cms.futurecdn.net/U76sZeRd6fS2fKt5RqBYPL-2560-80.jpg
---

![Big letters AI in pink in front of pink and blue strands of light suggesting a digital explosion](https://cdn.mos.cms.futurecdn.net/U76sZeRd6fS2fKt5RqBYPL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

As telemetry becomes central to how modern platforms are built, trained, and automated, its perceived future utility has driven a dramatic increase in collection and retention. A recent study shows telemetry volumes tripling in many enterprises over the past year, with agentic AI expected to drive nearly 10x more growth expected within the next two years.

Co-founder and CEO of Countly.

Clearly, telemetry is starting to look less like infrastructure and more like capital. The mistake is treating it as a pure asset and overlooking the other side of the ledger. Exploding log volumes and rising costs are the most tangible inconveniences, and often the first triggers for concern, but they are merely symptoms.

The bigger problem is that telemetry gradually becomes a system of knowledge that exceeds an organization’s ability to understand, govern, or explain it and, therefore, to reliably bound its cost, risk, and downstream use.

## When AI systems both produce telemetry and consume it

Traditional telemetry was largely retrospective. It described what happened. In AI, it starts feeding back into the system. A session log captured to troubleshoot a crash today may become training data tomorrow, evolve into a model feature later, and eventually drive automated decisions without human supervision.

In essence, the same data serves multiple functions throughout its lifecycle, many of which have little to do with why it was collected in the first place.

This sets a loop in motion. The system produces telemetry, the AI consumes it, which produces new signals and predictions, and those create an appetite for still more telemetry. As a result, the value organizations place on data keeps growing, often ahead of any clear understanding of how it will be used.

Once telemetry becomes a form of organizational memory over time, you are past just discussing observability. You are now dealing with governance, cost, and control.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Telemetry retention is fundamentally biased by asymmetry

It’s easy to justify the seemingly “small cost” of storing another terabyte when weighed against the hypothetical cost of discarding it, which can seem enormous, because someone can always argue that the data you threw away might have been a golden ticket.

The prospect of regretting its deletion feels potentially irreversible. Could it have solved a problem? Could it have trained a model or shown you an opportunity you missed? Caving to uncertainty, most organizations just keep everything.

The flaw in this reasoning is a myopic focus on the asset that ignores its liabilities. Every retained dataset carries ongoing storage and governance costs, security and compliance obligations, and discovery risk if you ever land in litigation. Each new dataset can also be combined with existing ones, amplifying its informational value in ways that were never foreseen.

Is there a guarantee that organizations will never regret a deletion? No, but there can be a clear rationale. You knowingly forgo some option value because the expected benefits of keeping the data do not outweigh the costs and risks of holding it. That is a decision you can stand behind later, even if it turns out the data might have been useful.

Asking whether something could be useful someday is not helpful, because almost anything clears that bar. It’s better to ask what specific capability you are keeping it for. If you have a clear answer, retain the data and govern it accordingly.

## For CTOs, the blind spot is treating telemetry growth as a scaling problem

As important as ingestion pipelines, storage, query speed, and tooling are, what often catches people off guard is that telemetry turns into a body of knowledge that no single person in the company actually understands. While most teams can tell you where their data lives, far fewer can explain what it reveals once you start putting it together.

The math here is quite unforgiving because exposure does not grow one stream at a time. Every new source can be matched against every source you already have, so the number of possible combinations spirals into something no longer tractable.

Consider clicks, session length, support tickets, device IDs, login records, or approximate location – on their own, none of it is sensitive, and nobody thinks much of collecting any of it. But put them together, and you can reconstruct someone’s daily routine, flag changes in their financial behavior, or predict upcoming life events.

The sensitivity is not attributed to any single stream but is born out of correlation across streams. In reality, most organizations have never fully explored what those correlations could actually enable.

For a CTO, the thing to worry about is not the size of the data, but whether you can still explain what your organization knows and where that knowledge came from. Give every stream an owner, a stated purpose, and a date it expires. If a stream cannot answer what it improves, then it has no business being retained indefinitely. A rule like that will do more to reduce risk than any amount of clever storage engineering.

## For CFOs, the blind spot is filing telemetry under infrastructure cost

What makes telemetry different from other infrastructure is that it compounds. More telemetry produces more analysis, which creates new use cases, which extend retention and increase demand for more storage, processing, tooling, and oversight. Before long, what started as a small storage expense has become an ongoing commitment.

The next year’s cloud bill may seem like the thing you should brace for, but at least you can put a number on it. What’s more concerning is that telemetry can become an ever-growing liability with unpredictable cost, risk, and duration. Unglamorous as it may be, the fix is down to the same thing – focus on the bounded business outcomes it produces.

Can you take any category of telemetry you hold and say plainly why it exists, what value it earns, how long it should live, and what happens to it when it stops being useful?

## What would a bounded telemetry architecture look like in an AI-driven world?

It starts by overturning the most basic assumption that you have to collect and keep everything until it turns out to be absolutely impractical. Instead, assume most things should not be collected and that nothing stays forever unless there is a reason for it to.

The effect is a change in default behavior. When every stream is set up with a clear purpose, owner, retention policy, and expected outcome, data starts following a lifecycle instead of piling up. Raw events might exist briefly at full detail, collapse into aggregates after that, and, once they are no longer useful for decisions, eventually disappear.

Thinking in lifecycle terms reframes data as something that interacts across systems rather than existing as isolated stores. That’s why the boundary you draw is not around a single database, but around what the combined system is allowed to infer and act on. What you collect should be based on the decisions you want to improve.

The complication in an AI setting is that these systems do need substantial telemetry to work, so it is not as simple as collecting less. The challenge is to collect enough while still keeping control over what the system learns from and what it ultimately produces.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

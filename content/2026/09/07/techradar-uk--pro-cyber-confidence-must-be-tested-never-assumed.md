---
title: Cyber confidence must be tested, never assumed
source_url: https://www.techradar.com/pro/cyber-confidence-must-be-tested-never-assumed
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-07T14:13:30Z'
published: '2026-09-07T00:00:00Z'
description: Continuous validation turns cyber confidence into proven resilience
image: https://cdn.mos.cms.futurecdn.net/wV66hEbpJdAc4iPB7RwtkK-2560-80.jpg
---

![An exclamation mark inside a red warning triangle, surrounded by email symbols, superimposed on someone typing on a laptop](https://cdn.mos.cms.futurecdn.net/wV66hEbpJdAc4iPB7RwtkK.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Internet security teams are not short of information. Threat intelligence feeds run around the clock, vulnerability scanners flag thousands of issues a month, and high-profile CVEs dominate the news cycle before most teams have finished their morning coffee.

What is far harder to come by is proof. Raw data is one thing, but what about evidence that the controls sitting in your environment actually detect and respond to the way real attackers behave, in your specific network, today?

Senior Director of Solutions Engineering, Rapid7.

That gap is what purple teaming exists to close, and it is where the surprises tend to show up. Running these exercises with organizations that have invested heavily in their security stack, I have repeatedly seen gaps nobody expected, missing telemetry, misfiring detections, and attack paths nobody was watching.

The problem was never simply being under attack. It is being under-validated, and mistaking spend for assurance.

## Why so many programs that look mature on paper still fail

Here's a pattern I keep running into with otherwise well-resourced organizations: every control on their books checks out, reports are signed off, tooling is deployed, leadership reassured. None of that holds up once a real attack runs through the environment. The cracks show almost immediately.

Ask where the actual gaps sit, and a familiar list comes back. Some systems feed logs in real time, others barely at all, leaving the SOC with a patchier picture than the dashboard implies. Detection rules are tuned to a generic attacker, not the one likely to show up here. And when something does trigger, it can sit unactioned for hours, since no one owns it.

None of this is exotic, just the ordinary, unglamorous consequence of tools and processes configured once and assumed still to work. With luck, those gaps surface in a simulated exercise before a real attacker finds them.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Part of the problem is what gets measured in the first place. Running standard techniques against a host already flagged as compromised only confirms which rules switch on. That's coverage, nothing more. It won't tell you whether the excess permissions, trust relationships, or misconfigurations in your real environment are exploitable, since that activity looks like normal use and was never built to trigger an alert.

Real validation looks different. It starts with the organization's own risk profile, not a generic library of techniques, and treats configuration and permissions as the real cause, not something a new detection rule can patch over. Only testing your own environment tells you which gap you're actually facing.

## What's worth measuring, and the case for continuous validation

Treating validation as an ongoing discipline rather than a one-off exercise also changes the output you’re looking for.

You don’t want another report that sits in a folder until next year's audit; you want to create a living, prioritized backlog. This is a running list of gaps that have been proven to matter, ranked against the paths an attacker could realistically use, not against theoretical severity scores.

It’s an important distinction because a CVE rated critical in isolation may be unreachable in your environment, while a modest misconfiguration sitting on a well-trodden attack path can be far more urgent.

The most valuable information a security team can generate is not a longer list of vulnerabilities, but evidence of which exposures are actually exploitable, mapped against real behavior, and prioritized against genuine business impact.

This is why it is critical to avoid relying purely on agent-based validation. Because an agent is already embedded within the network or on an endpoint, it inherently shortcuts a lot of attack paths and bypasses defensive controls. It assumes the attacker has already achieved a foothold at that specific location, giving you an artificial view of your actual perimeter and lateral resilience.

Alongside the process itself, cadence is another important factor here. An annual or ad hoc test captures a single snapshot, and environments do not stand still between engagements: new services get deployed, configurations drift, staff change. Shifting from ad hoc testing towards an operationalized, continuous cycle of testing, validating, remediating, and retesting is what keeps that backlog tied to the environment as it is right now, not as it was assessed to be six months ago.

The ability to close a validated gap before it can be exploited as an attack path enables the organization to shift from reactive footing to a more proactive stance.

## Breaking down the walls between red, blue, and the business

None of this works if validation happens in a silo. The most consistent driver of a strong outcome I have seen is not a tool; it is collaboration between people who are technically on the same side but often operate as if they are not.

Red and blue teams that only meet at the end of an engagement, via a report, tend to treat findings as a scorecard, something to defend or dispute rather than act on. An open-book approach changes that dynamic entirely. When offensive and defensive teams compare notes on what they are seeing, what they expected to see, and why, as the exercise unfolds, gaps get identified and understood together.

If a defensive team cannot follow a technique or lacks the telemetry to see it, that is not a failing to hide; it is the exact information the exercise exists to surface.

Clear ownership matters just as much as clear findings. An alert with no defined owner is functionally the same as no alert at all, so part of building this collaboration is agreeing, in advance, on who acts on what.

That communication cannot stop at the SOC door, either. Validation findings need to travel outward too, translated into terms a business audience can act on: which risks are real, which are theoretical, and where investment will actually reduce exposure. Security teams that build this bridge consistently get faster remediation and fewer arguments about priority, because everyone is working from the same evidence rather than competing assumptions.

Moving towards more coordinated action is another step towards preempting risk, delivering smoother and more effective operations than an isolated response where fixes happen team by team.

## Resilience is proven, not assumed

None of this is an argument against investment in tools or people. Rather, it’s an argument for asking a different question that identifies risk. It's time to stop asking, "Are we safe?", because no environment stays safe indefinitely. The question that matters is whether you're resilient enough to validate an exposure and respond before it turns into a breach.

Confidence built on assumptions collapses the moment a real adversary tests it. Confidence built on shared, ongoing validation does not, because it has already been tested, refined, and proven against the way attackers actually behave in your environment.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

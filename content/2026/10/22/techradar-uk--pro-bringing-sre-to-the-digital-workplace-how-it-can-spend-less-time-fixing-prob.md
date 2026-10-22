---
title: 'Bringing SRE to the digital workplace: How IT can spend less time fixing problems'
source_url: https://www.techradar.com/pro/bringing-sre-to-the-digital-workplace-how-it-can-spend-less-time-fixing-problems
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-22T17:16:59Z'
published: '2026-10-22T00:00:00Z'
description: How Site Reliability Engineering can stop recurring IT problems
image: https://cdn.mos.cms.futurecdn.net/ywSwn3oGxXv4PfcRPZmTrc-2560-80.jpg
categories:
- Technology & Software
- Careers & Productivity
people: []
locations: []
organisations:
- AI
- CIOs
- Future plc
- Google
- IT
- Lakeside Software
- PIMCO
- SLO
- SLOs
- SRE
- Site Reliability Engineering
- TechRadar Pro
- TechRadarPro
---

![ Man coding programmer, software developer working on digital tablet with binary, html computer code on virtual screen](https://cdn.mos.cms.futurecdn.net/ywSwn3oGxXv4PfcRPZmTrc-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Real-time has become something of a benchmark in IT. Teams see a problem, diagnose it quickly and, ideally, remediate it before the employee has time to raise a ticket.

Clearly, that's better than waiting for an employee to report a problem to the service desk. But real-time isn't necessarily preventative - if an issue occurs and we respond in milliseconds, we have still reacted to an issue.

Chief Product Officer and AI Officer at Lakeside Software.

And if the same thing happens again tomorrow? An automated remediation may mean the employee barely notices and an engineer never gets involved, which is valuable. But we're still fixing something we've fixed before.

Recurring problems carry a cost even when IT becomes very efficient at dealing with them. The cost shows up on both sides: employees lose time when technology doesn't work as expected, while IT spends time investigating and remediating familiar conditions. This is where Site Reliability Engineering (SRE) offers a way to break that cycle.

## Bringing SRE to the endpoint

SRE came out of Google's approach to running large-scale production systems, applying software engineering principles to operational problems. At its simplest, it means defining the reliability a service needs, measuring it and reducing the repetitive work involved in keeping it there.

A Service Level Objective (SLO) puts a measurable target around that reliability, while error budgets recognize that no service will be perfect all of the time. These are established ideas in software and infrastructure, but they translate increasingly well to the digital employee experience.

The device, applications and services an employee relies on are now part of how the organization operates, and their reliability has a direct bearing on whether people can get work done.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

A recent conversation with a partner put the challenge neatly. They said: “Tell me about emerging risk whilst it’s still at 0–2% and give me the evidence to prioritize. At 5–10% beyond baseline, the service desk will have already lit up.”

They were talking about deviation from their normal baseline, not the percentage of employees affected. They wanted enough evidence to spot deterioration early and decide whether it warranted attention before the consequences showed up in support demand. A millisecond reaction is good, but prevention is always better.

That depends on being able to see problems before they become obvious. Digital employee experience data can expose issues that conventional operational measures miss, giving IT evidence of what is happening before the service desk becomes the signal.

At a large Fortune 100 insurance organization, for example, the team discovered that approximately 25% of call-center downtime was effectively invisible to IT. By combining endpoint telemetry with proactive automation, the organization reduced ticket volume by 35% in a year and avoided more than 45,000 tickets through a single self-service automation.

## Learn from what keeps coming back

Anyone who has worked in IT operations knows how much time can disappear into familiar problems. A large hospital network found that a small number of recurring issues were generating a disproportionate amount of service desk activity. They included problems with file synchronization, security services, CPU utilization, network services and collaboration tools.

By using endpoint data to identify and address those recurring causes, the organization reduced annual ticket volume by roughly 50,000 incidents and estimated savings of approximately $1.6 million.

This is where the SRE idea of toil maps particularly well to workplace IT. Toil is the repetitive operational work involved in keeping a service running, and automation can take a lot of that work away from engineers. But if the same remediation keeps being required, that pattern is worth paying attention to.

Sometimes automation will remain the sensible answer. Not every repeated condition needs an engineering project behind it. In other cases, the evidence may point towards an application, configuration, update, or another underlying problem that can be tackled more permanently.

Global investment management firm PIMCO provides another example of what changes when teams have better evidence to work with. Its infrastructure team used endpoint evidence and change correlation to reduce root-cause investigations that had previously taken days to minutes.

That speed matters, but so does what the team can do with the evidence: understand what changed, isolate the cause and get closer to eliminating a recurring issue rather than repeatedly treating its symptoms.

## Knowing what happened after the fix

We have plenty of evidence that tells us an IT action happened. A script completed, an update installed, a device restarted or a workflow reached its final step. What matters next is whether it worked. Did the issue disappear? Did the affected experience return to its expected range? Was the improvement still there a day or a week later?

Subsequent telemetry can provide that answer. Without it, IT knows an intervention took place but has less evidence of the outcome or whether the improvement lasted. SLOs help by giving teams an expected level of reliability against which to assess recovery. A completed action is one data point, while the state of the service afterward is another.

AI makes this feedback increasingly important because more diagnosis and remediation will happen without an engineer examining every signal or action individually. If AI identifies a problem and initiates a response, IT still needs evidence of the outcome.

The workflow from insight to outcome matters here. As more of it becomes autonomous, validation and accountability need to remain part of it. Otherwise, IT could automate more activity without necessarily making the environment more reliable.

None of this argues against real-time observability, automation or an efficient service desk. We need them. How quickly IT reacts still matters, as does how much manual work automation removes.

For CIOs, the bigger gain comes when those capabilities lead to fewer problems requiring attention in the first place. That means spotting deterioration earlier, learning from recurring issues and checking whether interventions have actually held. We've become very good at fixing problems quickly, and now SRE gives us a chance to spend less time fixing the ones we've seen before.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

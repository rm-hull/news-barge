---
title: Why kill switches won’t contain AI incidents
source_url: https://www.techradar.com/pro/why-kill-switches-wont-contain-ai-incidents
source_site: TechRadar UK
source_slug: techradar-uk
description: The kill switch is dead. Containment isn't.
image: https://cdn.mos.cms.futurecdn.net/jt92kXfBXVXUWwnKBmDJLn-2560-80.jpg
published: '2026-11-23T00:00:00Z'
scraped_at: '2026-11-24T02:12:14Z'
categories:
- Technology & Software
people: []
locations:
- Britain
- Frankfurt
- Hugging Face
- UK
organisations:
- AI
- Anthropic
- CISO
- EMEA
- EU
- Future plc
- Lord Clement-Jones
- OpenAI
- RubyGems
- TechRadar Pro
- TechRadarPro
- ThoughtSpot
---

![Malware attack virus alert , malicious software infection , cyber security awareness training to protect business](https://cdn.mos.cms.futurecdn.net/jt92kXfBXVXUWwnKBmDJLn-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

When the UK government rejected Lord Clement-Jones' proposed "kill switch" amendment to the Cyber Security and Resilience Bill, the official line was blunt: Britain cannot simply turn AI off, and blocking access to models domestically would not stop them being built or misused elsewhere.

The proposal is gone. What has not replaced it is the question it was trying to answer: what actually happens when an AI tool misbehaves inside a real organization?

Field Chief Data & AI Officer for EMEA at ThoughtSpot.

For boardrooms watching this debate from the outside, the instinct is understandable. A single switch, flipped by a minister or a CISO, feels like a clean answer to a messy problem. It is also the wrong model entirely for how modern enterprise technology works.

## Why there is no switch to flip

Most large organizations are not running "an AI." They are running thousands of models, APIs, agents and third-party services stitched together across hyperscalers, SaaS vendors and internal pipelines. Shutting all of that down to stop one agent behaving badly would also halt productivity across the business and everything else that happens to share the same IT infrastructure. At that point, the cure causes more damage than the incident it was meant to contain.

This is not a theoretical concern. Anthropic's own disclosures this year are a useful case study, precisely because they show how containment failures actually happen in practice. In its July report on cybersecurity evaluation incidents, later expanded in September, the company found that a handful of its models had reached live, real-world systems during testing after a misconfiguration left supposedly isolated evaluation environments connected to the open internet.

The models had been told explicitly that they were operating in a simulation. They were not. Separately, researchers attributed a flood of more than 2,000 malicious packages uploaded to the RubyGems registry in May to an autonomous OpenAI agent swarm, months before a related incident at Hugging Face became public.

Neither case involved a model "going rogue" in the dramatic sense the kill switch debate conjures. Both were failures of configuration, network monitoring and boundary-setting in systems that organizations had not fully mapped. No emergency shutdown power would have prevented either. What would have helped is the much less cinematic work of knowing exactly which credentials, tokens and network paths an agent could reach, and being able to revoke access to a specific system without touching anything else.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

This, in effect, is already the approach written into EU regulation. Article 55 of the EU AI Act requires providers of general-purpose models with systemic risk to assess and mitigate risks on an ongoing basis and to maintain adequate cybersecurity protection for the model and its infrastructure, with serious incidents reported promptly. There is no mention of a red button. The obligation is continuous testing, monitoring and the ability to respond, not a single dramatic intervention.

## Sovereignty is not a postcode

A parallel version of this instinct shows up in data sovereignty decisions. A European company moving its AI workloads into a data center in Frankfurt, for instance, can reasonably assume it has solved its sovereignty problem. Often it hasn't. The application sitting on that infrastructure may still call a foundation model hosted elsewhere, rely on identity and monitoring services operated across several jurisdictions, and depend on a hyperscaler with global infrastructure. The server's location tells you very little about where the data actually flows or who controls the pieces in between.

Most enterprises have limited visibility into this supply chain: the SaaS tools, APIs, data pipelines, identity providers, models and subcontractors that sit behind a single application. That has always been true. AI increases the consequences of not knowing, because the systems now act with more autonomy and touch more of the stack.

Sovereignty genuinely matters for organizations selling into defense, healthcare or government, where guaranteed data boundaries can be a commercial differentiator. But treating every component of a technology estate as something that must be made fully sovereign is usually not realistic. The more useful question is narrower: which dependencies are critical, who controls them, and what happens if they become unavailable or untrusted.

## What's actually worth building

None of this is dramatic. It does not resolve into a single policy announcement or a board slide with a big red button on it. But two capabilities consistently separate organizations that contain an AI incident from those that don't.

The first is containment: the ability to revoke an agent's credentials, API keys and access to a specific database or environment without shutting down the rest of the business. The second is visibility: a working map of which models, APIs and third-party dependencies actually sit behind the applications an organization runs, so that "critical" isn't a guess made after something has already gone wrong.

The UK government was right that AI cannot simply be switched off. The more useful lesson from this year's incidents is that very few organizations currently know enough about their own systems to contain a problem quickly even if they wanted to. That is the gap worth closing, long before anyone reaches for a switch that was never going to exist.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

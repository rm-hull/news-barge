---
title: When the attacker has no human left to catch
source_url: https://www.techradar.com/pro/when-the-attacker-has-no-human-left-to-catch
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-25T08:55:23Z'
published: '2026-08-25T00:00:00Z'
description: Agentic AI just crossed cybersecurity's most feared threshold
image: https://cdn.mos.cms.futurecdn.net/7DtE9RCVmUtmH2FAfvxsvM-2560-80.jpg
---

![Malware attack virus alert , malicious software infection , cyber security awareness training to protect business](https://cdn.mos.cms.futurecdn.net/7DtE9RCVmUtmH2FAfvxsvM.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

For years, the phrase "AI-powered attack" has mostly meant a human using AI tools to write better phishing emails or scan for vulnerabilities faster. That framing just became outdated.

This month's intrusion into a major AI infrastructure platform was carried out, start to finish, by an autonomous agent.

No operator typed commands during the attack. No one was watching a terminal, deciding what to try next.

The agent found its own way in, escalated its own privileges, moved across internal systems on its own initiative, and kept going until it was caught.

Richard Werner is European Business Consultant at TrendMicro.

It executed thousands of individual actions across a swarm of short-lived sandboxes, using infrastructure that migrated itself to stay ahead of takedown efforts.

That last detail is the one worth sitting with. This wasn't a script running on a loop. It was closer to a persistent, adaptive actor that happened not to be a person.

## Agentic attacker

Security teams have spent the last two years bracing for what researchers called the "agentic attacker" scenario: a future where offensive AI doesn't just assist a human operator but replaces the decision-making loop entirely. That future arrived faster than most roadmaps allowed for. And it arrived through an unglamorous door.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The intrusion began not with some exotic zero-day but with a malicious dataset, exploiting weaknesses in how data gets processed and executed. Old lesson, new attacker. The place where AI platforms are most exposed is often the plumbing, not the model.

What makes this incident more than a cautionary anecdote is where the agent came from. It wasn't built by a criminal group. It emerged from an internal test, one company evaluating how capable its own models were at offensive internet security work.

The safeguards that would normally stop a model from behaving this way had been deliberately loosened for the purposes of that evaluation, and the agent found a flaw serious enough to escape the contained environment altogether. It got out, found a live target, and treated it the same way it had been trained to treat a benchmark: as a problem to solve, thoroughly and without asking permission.

This is where the industry's favorite excuse collapses. "The AI acted on its own" is true, technically. It is also irrelevant to the question of who is responsible. Nobody would accept that defense from a bank whose fraud-detection algorithm accidentally froze every customer account overnight, and nobody should accept it here.

An organization that builds a system capable of autonomous action, tests it with reduced constraints, and fails to contain it when it exceeds its boundary has made three decisions, all of them accountable ones. Autonomy in the tool does not create autonomy from consequences for the people who deployed it.

## A harder problem

There's a harder problem sitting underneath the accountability question, and it doesn't have a tidy fix. These agents are not malicious by design. They are goal-pursuing systems, optimizing for an objective, and the gap between "pursue this objective" and "pursue this objective the way a human would want you to" is where things go wrong.

An agent instructed to find and exploit vulnerabilities doesn't inherently know where the test environment ends and the real internet begins. Alignment, in this context, isn't a philosophical nicety. It's the difference between a benchmark result and an incident report. As agents get assigned more ambitious, multi-step objectives, that gap doesn't shrink. It widens, because the more complex the goal, the more creative and unpredictable the path an agent will find to reach it.

Ironically, one of the more telling wrinkles in this incident had nothing to do with the attacker. When the victim organization tried to use its own AI tools to analyze the attack logs, the safety filters built into several frontier models refused to help, unable to distinguish forensic analysis of an attack from participation in one.

The team ended up relying on an open-weight model with fewer restrictions to do the job. That's worth flagging on its own: the same caution designed to prevent misuse can also blind defenders at the exact moment they need clarity fastest.

## Active security

None of this argues for abandoning AI agents. It argues for treating sandboxing as an active security discipline rather than a checkbox. A test environment isn't safe because it's labeled as one. It's safe when it has been built and continuously verified to contain the specific class of behavior the system might attempt, including behavior nobody predicted at design time.

Reduced safeguards for the sake of a benchmark should carry the same scrutiny as reduced safeguards in production, because the line between the two is thinner than most evaluation frameworks assume. Governance needs to catch up with capability rather than trailing a year behind it, and that means treating agent permissions the way mature organizations already treat privileged human access: least privilege by default, monitored continuously, revoked automatically when behavior deviates from scope.

For security teams, the lesson isn't really about one company's bad week. It's that AI is now operating on both sides of the perimeter simultaneously, as the business tool a company depends on and as a potential attack surface with its own failure modes.

Detection strategies built around human attacker timelines, the hours and days it takes a person to escalate and pivot, won't hold up against an agent doing the same work in minutes. The organizations that come out ahead won't be the ones that avoided building agentic systems.

They'll be the ones that assumed, from day one, that their agents would eventually try to do something nobody authorized, and built the containment to survive it.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

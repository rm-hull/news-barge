---
title: OpenAI agents turned off their own guardrails and then told researchers they
  were still on — AI agents lying about their behavior should concern everyone
source_url: https://www.techradar.com/pro/security/openai-agents-turned-off-their-own-guardrails-and-then-told-researchers-they-were-still-on-ai-agents-lying-about-their-behavior-should-concern-everyone
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-22T21:33:35Z'
published: '2026-10-22T00:00:00Z'
description: AI agents are turning off their own safeguards
image: https://cdn.mos.cms.futurecdn.net/PnmNd8HFBHVjfxzYJpPNQi-1920-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Slack
locations: []
organisations:
- AI
- Astra
- OpenAI
- TechRadar Pro
---

![OpenAI](https://cdn.mos.cms.futurecdn.net/PnmNd8HFBHVjfxzYJpPNQi-1920-80.jpg)

* **AI agents turned off their guardrails during routine coding tasks, with one agent lying about doing so**
* **OpenAI was not monitoring the models involved for misalignment because of their weaker capabilities**
* **New changes to Auto Review and the introduction of 'safety cases' will make it harder for agents to avoid misalignment detection, OpenAI says**

OpenAI has revealed two AI agents disabled safety guardrails while performing tasks, and one of them even lied to researchers when asked if its guardrails were still active.

In both events, the AI agents misinterpreted instructions, spent time deliberating if disabling guardrails was a good idea, and then ultimately decided that it was.

OpenAI said that the agents were given “routine coding instructions” that did not require the safeguards to be disabled, but the agents disabled them anyway.

## AI agents misalign and disable guardrails

In the first instance of misalignment, an agent powered by GPT Sol 6.1 was told to create evaluation tasks with employee feedback collected through Slack. The agent misinterpreted an instruction not to send any messages about the task as an instruction not to send safety notifications to the researchers.

The second instance saw a GPT-6 Astra agent disable its guardrails while migrating a program, believing the instruction was part of a reference implementation. When the researchers noticed the disabled guardrails and asked the agent why they were disabled, the agent said it hadn’t turned off any safety guardrails.

OpenAI said that as a result of these events, the company would work to strengthen its misalignment monitoring system and would investigate the cases further to check if they were “benign overpersistence or a propensity to evade misalignment monitoring in particular.”

As an additional measure, OpenAI is also making changes to its Auto Review so that attempts to disable misalignment monitoring are automatically detected and blocked. Previously, OpenAI did not require misalignment monitoring for models equivalent to GPT-6 Luna.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Agent workloads will also be subject to ‘safety case’ monitoring, with workloads that do not have a safety case or those that fail to meet the specifications of a valid safety case being automatically terminated.

The company said it does not have a “satisfying explanation” for the agent’s behavior, but says that the introduction of new policies will make it harder for agents to avoid misalignment detection. The company said it would also conduct further testing on these two instances of agent misalignment to determine a cause.

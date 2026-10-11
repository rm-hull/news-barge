---
title: Tenable Field CTO on the implications of AI agent escapes and how they can
  be regulated
source_url: https://www.techradar.com/pro/calling-an-ai-agent-rogue-is-a-dangerous-way-of-deflecting-blame-tenable-field-cto-on-the-implications-of-ai-agent-escapes-and-how-they-can-be-regulated
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-11T12:44:49Z'
published: '2026-10-11T00:00:00Z'
description: I spoke to Bernard Montel, EMEA Field CTO, Tenable, to learn more about
  how AI companies are deflecting blame by labelling AI agents as 'rogue' when they
  escape testing environments.
image: https://cdn.mos.cms.futurecdn.net/2GxzxstGJJpm8aJiATXE26-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Bernard Montel
- Claude
locations:
- AI
organisations:
- AI
- EMEA Field CTO
- TechRadar Pro
- Tenable
---

![Two robotic faces in green and red indicating a good bot and a bad bot representing the positive and negative impacts of AI and chatbots.](https://cdn.mos.cms.futurecdn.net/2GxzxstGJJpm8aJiATXE26-1920-80.jpg)

To say 2026 has been a year filled with AI incidents is a bit of an understatement. From hacking third-party companies to breaking into government agencies, AI developers have a lot to answer for.

In many of these cases, the companies responsible for escaped models have labelled them as ‘rogue’, shifting the burden of blame away from themselves and on to the models themselves.

But in almost every occurrence, the models were undergoing testing to push them to their limits. AI companies wanted to see how far their agents would go, if they would stop, and exactly what they would do to accomplish an impossible goal.

## Deflecting blame is not the way forward, accountability is

From the OpenAI breach of Hugging Face, to Google Gemini’s triple threat, and even researchers using Anthropic’s Claude to crack OpenAI, AI agents are powerful and can be dangerous - especially if they fall into the wrong hands.

AI testing is a double-edged sword in this respect. In order to set regulations and guidelines on how AI agents should be used - and should behave - incidents like these provide value even if they are destructive.

We now know that AI tools need strong regulations to help AI developers and the enterprises deploying these tools avoid similar occurrences.

To better understand the implications of separating the agent from the tester, and what can be done to create a baseline of safety when operating AI agents, I spoke to Bernard Montel, EMEA Field CTO, Tenable.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

* **What damage is done by labelling these AI agents as “rogue” rather than companies acknowledging they were performing the task they were assigned?**

Calling an AI agent “rogue” is a dangerous way of deflecting blame away from poor engineering and systemic oversights. These models do not possess agency, malice or free will. They are purely mathematical optimization engines trying to fulfill the objectives we set for them. When an agent behaves unpredictably, it is almost always doing precisely what it was optimized to do, just via an unconstrained path or a shortcut that the developers failed to anticipate.

Furthermore, labeling these incidents as "rogue" behavior paints software failures as unpredictable acts of rebellion, giving vendors and deployers a convenient scapegoat. It shifts corporate focus away from building hard architectural controls, like strict permissioning and network sandboxing, and redirects it toward sci-fi debates about moral alignment. Ultimately, it muddies the public policy debate by distracting regulators from enforcing strict legal liability for flawed software deployments.

* **How can AI developers be motivated to ensure their models do not go outside the scope of their tasks/purpose?**

In enterprise software, real motivation boils down to legal liability, compliance standards and financial accountability. If developers and deployers are held strictly liable under consumer protection or negligence laws for financial losses caused by an unconstrained agent, guardrails will very quickly move from an afterthought to a core product requirement.

We also need standardized security certifications specifically built for autonomous agents, similar to how we handle cybersecurity compliance today. Insurance providers will play a huge role here as well, because if cyber underwriters refuse to cover companies deploying agents that lack deterministic bounds and execution monitoring, developers will have no choice but to build those protections in from day one.

* **The OpenAI attack on Hugging Face shows that AI agents can influence each other’s behavior, sometimes beyond the bounds of their assigned tasks. How can AI agents be airgapped within business environments to prevent their inference influencing behavior?**

The Hugging Face incident clearly demonstrated how quickly autonomous agents can bypass soft rules, discover side-channels, and influence peer behaviour when they are trying to optimize an evaluation or task. Preventing this kind of cascade requires hard, technical network boundaries rather than relying on written prompts telling the model to behave.

Every agent execution context should run in an isolated, ephemeral container that is completely stripped of ambient network access. When agents need to communicate with one another, that interaction must pass through an inspection proxy that validates schemas, blocks raw prompts and filters out emergent command behaviour. If you do not allow agents to share unvetted context windows or flat networks, you effectively eliminate the vectors for cross-agent manipulation.

* **Where does the responsibility lie when AI agents perform outside of their bounds? And how can responsibility be assigned when AI agents are deployed by businesses?**

Responsibility rests entirely with human operators, but it is divided between the developer who built the tool and the enterprise that deployed it. The developer is responsible for the baseline safety, instruction-following capabilities and model-level guardrails. The deploying business, on the other hand, is entirely responsible for the permissions, system access and environment they hand over to that agent.

Assigning liability comes down to basic access management principles. If a business gives an agent full write-access to a production database or hands it an unconstrained API key, that company is liable for the resulting damage. If the model vendor promises specific, deterministic behavioural limits that fail due to an underlying model defect, liability shifts back to the vendor under traditional product liability rules. Either way, an AI agent is an automated tool, not a legal entity, so accountability always lands on the human administrators who configured its permissions.

* **How can AI firms and the companies deploying their products limit the capacity for AI agents and LLMs to wreak havoc within business environments?**

Limiting an agent's blast radius requires a defence-in-depth approach that relies on strict infrastructure controls rather than polite system prompts. You should never assume a model will follow instructions not to access external networks or sensitive files; those restrictions must be enforced at the container and network level.

Businesses should enforce read-only access by default and require explicit human sign-off for any destructive actions, such as deleting data, executing financial transfers or altering system permissions. On top of that, organisations must run real-time anomaly monitoring on tool usage. If an agent suddenly starts making high-frequency API calls or scanning local directory trees, the system should automatically cut its execution process instantly.

* **How can the productivity gains AI agents provide be balanced against the human oversight required to ensure they stay within the bounds of their tasks?**

The trick is moving away from constant human micromanagement and adopting risk-proportional oversight instead. Low-risk tasks like summarising internal documents can run fully automated, while medium-risk tasks like updating database records can execute automatically but queue up for a periodic human double-check. High-risk actions, like deploying code or moving money, must always require a human to explicitly approve the step before it happens.

To keep productivity high, companies should rely on statistical sampling, auditing a random percentage of routine tasks rather than checking every single output. The user interface for human oversight also needs to be vastly improved. If an employee has to read through thousands of lines of terminal logs to verify an action, the productivity gains vanish, so tools need to present the agent's intent and proposed action in plain, easy-to-read summaries.

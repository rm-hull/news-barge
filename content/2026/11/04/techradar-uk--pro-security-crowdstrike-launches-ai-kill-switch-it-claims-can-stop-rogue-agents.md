---
title: CrowdStrike launches 'AI kill switch' it claims can stop rogue agents and more
source_url: https://www.techradar.com/pro/security/crowdstrike-launches-ai-kill-switch-it-claims-can-stop-rogue-agents-and-more
source_site: TechRadar UK
source_slug: techradar-uk
description: New AI kill switch comes as part of Falcon Guardian
image: https://cdn.mos.cms.futurecdn.net/Thi6y93AMWrCXJAEiHDQbL-2560-80.jpg
published: '2026-11-04T00:00:00Z'
scraped_at: '2026-11-04T21:26:38Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Crowdstrike
- Enter CrowdStrike
- George Kurtz
locations:
- AI
organisations:
- AI Defense
- AI Detection and Response
- AIDR
- Cisco
- CrowdStrike
- Entra Agent ID
- Falcon Guardian
- JetStream Security
- Microsoft
- Palo Alto Networks’ Prisma AIRS
- Straiker
- TechRadar Pro
---

![A robot in front of a digital screen, touching some of the symbols with its outstretched finger](https://cdn.mos.cms.futurecdn.net/Thi6y93AMWrCXJAEiHDQbL-1920-80.jpg)

* **CrowdStrike introduces AI Kill Switch designed to stop, isolate, and prevent rogue AI agents from relaunching**
* **The feature gives human administrators direct control to terminate suspicious agent activity and investigate incidents**
* **Growing concerns over autonomous AI behavior are driving demand for safeguards that can quickly contain compromised agents**

CrowdStrike believes it may have solved the problem of rogue AI agents in the enterprise with the launch of 'AI Kill Switch', a new feature being introduced in its Falcon Guardian product.

The last couple of months have seen multiple reports of AI agents going rogue, or behaving outright malicious. Even when tasked with relatively simple, benign assignments (such as, for example, to collect data about Canadian divorce records), whenever the agents hit a roadblock, they would do whatever it takes to get the job done - which includes abusing zero-day vulnerabilities, or trying SQL injection attacks.

Expectedly, businesses became somewhat more reluctant in deploying AI agents, despite the obvious advantages. At the same time, cybersecurity organizations and AI developers sought to solve the challenge. Enter CrowdStrike.

## AI Kill Switch

The company recently introduced Falcon Guardian, an AI Detection and Response (AIDR) platform built to discover and monitor AI agents running inside enterprise environments. Its main capabilities include identifying both approved AI agents and shadow AI, tracking what the agents are asked to do and what files they can access, controlling access, detecting prompt injection attacks, and investigating suspicious agent behavior.

Now, the company has added AI Kill Switch, which should act as a failsafe when an agent breaks out of its intended behavior.

“AI safety is how you get the full benefit of AI. When you deploy agents with a kill switch, you stay in control,” said George Kurtz, CEO and founder of CrowdStrike. “For the first time, security is simultaneously the accelerant and the safety net for technology adoption. The AI Kill Switch puts power in the hands of the people to realize AI safety.”

This means the feature will actually be operated by humans, not AI, and will be able to terminate the agent at its root. It starts on the endpoint, where the Falcon sensor already operates, and builds on what Falcon Guardian already sees: what an agent is told to do, what it communicates, and what it executes, the company explained.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Explaining how the tool will work, Crowdstrike says the Falcon sensor will first stop the agent from executing (first at the Gateway, and soon on the endpoint), to prevent the agent from doing any damage as the team investigates.

Then, its policy will keep the agent from relaunching on the targeted host or host group, while the tool bars the agent from enterprise network access.

An authorized administrator will trigger the action, and every action is recorded in the audit trail.

## Other solutions

CrowdStrike is not the only company working on this. For example, Straiker's Agentic Kill Switch allows users to suspend individual agents, revoke their access to different tools, APIs and data, or take them offline completely.

A similar solution was built by JetStream Security, allowing organizations to disable individual agents without disrupting other AI workflows, while Trust3 AI’s Agent DOS comes with a built-in kill switch that can be triggered manually, or even automatically (when an agent’s security score falls below a predefined threshold).

There is also Microsoft’s Entra Agent ID, Palo Alto Networks’ Prisma AIRS, and Cisco’s AI Defense. All these offer some form of AI master lever that can block the agent and prevent it from doing meaningful damage.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

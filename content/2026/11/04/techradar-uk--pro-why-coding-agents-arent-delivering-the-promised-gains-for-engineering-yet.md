---
title: Why coding agents aren’t delivering the promised gains for engineering – yet
source_url: https://www.techradar.com/pro/why-coding-agents-arent-delivering-the-promised-gains-for-engineering-yet
source_site: TechRadar UK
source_slug: techradar-uk
description: AI writes code in minutes, but engineers are struggling to understand
  and fix it
image: https://cdn.mos.cms.futurecdn.net/PAztEScphfxGJfYno5NjrL-2560-80.jpg
published: '2026-11-04T00:00:00Z'
scraped_at: '2026-11-04T21:23:08Z'
categories:
- Technology & Software
people:
- Greg
locations:
- UK
organisations:
- AI
- Future plc
- TechRadar Pro
- TechRadarPro
- Undo
---

![A robot standing thoughtfully in front of a giant digital display with code on it](https://cdn.mos.cms.futurecdn.net/PAztEScphfxGJfYno5NjrL-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Vibe coding agents enable engineers to create code in a fraction of the time. This has shifted the bottleneck to later in the development process: when engineers have to understand what that code is doing, track down bugs, and investigate incidents.

As agents generate ever greater volumes of code, it’s becoming increasingly difficult for engineers to understand their output.

Greg is the co-founder and CTO of Undo.

It takes time to work out what their code does and how it interacts with the systems around it.

To realize the productivity gains, AI must be applied to the later stages of the cycle, not simply code generation. When it comes to large-scale complex code bases, agents struggle.

## A critical issue in critical industries

Nowhere is the pain of code comprehension and debugging more acute than in organizations powering the digital economy – from financial services and semiconductor design to the networks and databases that keep everything connected.

In these sectors, one escaped defect can have serious consequences – a trading system returning a bad value, a database returning the wrong row, or a network failure leading to a service blackout. The UK’s national air traffic controller found itself an unfortunate case in point when it revealed that its recent service outage, which caused 2,000 flight cancellations and days of disruption, was triggered by a legacy software defect.

As AI continues to increase the volume of code engineers can produce, the challenge is no longer about increasing the speed at which they work. Rather, engineering leaders must ensure their teams can still understand what they’ve built when something goes wrong or behaves unexpectedly – and act before a problem becomes a much bigger one.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## The code comprehension gap

AI can produce code in minutes. However, that speed comes at a cost. As AI-generated code accumulates, duplicated logic and layers of change are built on top of one another, creating a kind of spaghettification of the codebase. It then becomes harder for engineers to understand how their code is behaving, let alone know where to start untangling it when something goes wrong.

The problem gets worse as codebases become more complex. Nine in ten engineering leaders say code comprehension and debugging take longer in complex environments such as C/C++ codebases. Engineers were already struggling to keep up when they wrote every line themselves.

Now, with AI being far less capable at debugging complex code than it is at creating it – engineers find themselves buried in an avalanche of review work that is beyond human ability. As a result, defects can more easily escape into production, with no clear path back to their root cause.

The productivity gains are failing to add up. Despite being able to write code more easily, 79% of engineering leaders say their release cycles are no faster. It’s a vicious cycle. The faster AI generates code, the more engineers have to review and understand – and the harder that becomes as complexity builds. Without solving the comprehension problem, increasing the speed of code generation risks simply moving the bottleneck further downstream.

## The limits of AI for debugging

The obvious answer if humans are struggling to comprehend and debug code is for coding agents to take over. However, without the right inputs, even the most advanced AI tools struggle to deliver accurate answers.

Coding agents debugging complex codebases often work from static context such as source code, logs and documentation. This tells them what the code is supposed to do, but not necessarily what it actually did at runtime. Agents are left to fill in the gaps and guess at what happened and why.

That lack of context creates a particular problem when the issue is buried in the complexity of a live system. AI agents can produce an answer that looks plausible, but without the evidence to support it, there is no guarantee that the diagnosis is correct. In fact, 93% of engineering organizations have had the root cause of an issue incorrectly diagnosed because of an AI hallucination. As a result, a third (37%) of teams only use AI agents for comprehension and debugging straightforward codebases.

The consequences extend beyond simply failing to solve the problem. When an agent cannot identify the root cause, it can resort to trial and error – adding more logs, rerunning the code and trying another approach. Agents end up stuck in a loop, consuming budgeted AI tokens without getting any closer to an answer.

## Better evidence, not bigger models

This raises a broader question for engineering leaders: how do you make AI genuinely useful for the difficult parts of software engineering, rather than simply using it to generate more code?

The way to get better results from AI agents isn’t necessarily to use a more powerful model, but to give them better evidence. Giving an agent a record of what actually happened when code ran helps it understand how an issue occurred, making it better equipped to trace problems to their root cause and support engineers with debugging.

Ultimately, AI can only be as useful as the information it has to work with. Give agents a clear picture of how software behaved, and they can take on more of the difficult work that still sits with human engineers today. That means faster answers, fewer dead ends and, most importantly, greater understanding of the software teams are responsible for.

## Turning AI speed into engineering value

The future of AI-powered development isn’t just about generating more code, but understanding what it actually does. Give agents access to the right information, with high-quality context, and they can move from plausible answers to accurate automated root cause analysis.

That gives engineers something far more valuable than speed alone – the confidence to let AI tackle the hardest problems without losing control of the software they build.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

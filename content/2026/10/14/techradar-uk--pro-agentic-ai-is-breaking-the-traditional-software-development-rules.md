---
title: Agentic AI is breaking the traditional software development rules
source_url: https://www.techradar.com/pro/agentic-ai-is-breaking-the-traditional-software-development-rules
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-14T11:51:39Z'
published: '2026-10-14T00:00:00Z'
description: The Agent Development Lifecycle – where AI agents are managed, not coded
image: https://cdn.mos.cms.futurecdn.net/rNZmVCrdHzszaDCyTrBWmj-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations: []
organisations:
- ADLC
- AI
- Future plc
- MCP
- Solace
- TechRadar Pro
- TechRadarPro
---

![A representative abstraction of artificial intelligence](https://cdn.mos.cms.futurecdn.net/rNZmVCrdHzszaDCyTrBWmj-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

AI Agents are unlike any software development witnessed before. Traditionally, trustworthy software systems have followed a structured approach to being built and developed. One that plans, builds, tests, and maintains software to ensure its reliability and scalability. This created the Software Development LifeCycle (SDLC) (1) framework.

But AI agents are different: they are a team of autonomous, probabilistic actors that work most effectively in a real-time, event-driven environment, enabling the agents to coordinate with real-time data to develop, learn, and work.

Director of AI and industry solutions at Solace.

To scale an enterprise workforce of AI agents, organizations need to combine the principles of employee management with software development rigor. These agents are not static software that can be coded and developed, due to probabilistic language models. They are built, evaluated, and governed differently.

This requires organizations to move from traditional SDLC to an Agent Development LifeCycle (ADLC) (2), which utilizes the structure and repeatable process of the SDLC framework and combines it with the development and management of AI agents.

## A helping hand from HR

Since AI agents perform roles within an enterprise, the ADLC should draw on lessons from the human employee lifecycle.

When an organization brings on a new team member, there is a deliberate process: their role is defined; they’re given access to the systems they need; they are trained; and they are integrated into a team. Once they are empowered and put to work, a manager oversees their activity, monitoring and developing their performance over time.

As autonomous actors operating within a system of governance, AI agents deserve and require that same treatment.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

AI agents need a similar structured approach to onboard and integrate them into a business and deliver the efficiency benefits they’re designed for – that means they need real-time contextual data to do their jobs!

## Treat AI agents like humans at the hiring stage

Picture an organization where every employee is a generalist, there’s no hierarchy or structure, and all communication happens via synchronous one–to–one phone calls. No email. No Slack. No shared systems.

The organization can’t scale. Information doesn’t flow. People drown in data from every direction, with no real understanding of what’s going on or what to do. There are no accountability structures, no access controls, no coordination mechanisms beyond individual conversations.

You wouldn’t drop a new human hire into this chaos. Effective organizations look different, counting on people who are specialized and organized hierarchically, so coordination happens in parallel and communication is premised on asynchronous channels that let information flow without requiring everyone to be online at the same time. The same goes for onboarding AI agents.

## AI agents and employees are no different in the eye of an agent mesh

Most early agentic AI deployments work as complex monolithic agents tasked with doing everything, accessing all data, communicating synchronously, and trying to maintain very large context or working synchronously with sub-agents. The result? A system that’s brittle, expensive, inconsistent, and completely unable to handle real enterprise complexity.

This is where an agent mesh can act as a development and runtime platform, helping build AI agents that actually work for a real-time enterprise, specialized for particular functions, organized hierarchically, and orchestrated by a development and runtime platform that specializes in delegating tasks to appropriate agents.

Communications between agents are asynchronous and event–driven, and access to data and systems is governed by role-based access controls, giving agents exactly the permissions they need and nothing more.

So, let’s look at how agents can be “onboarded” through an ADLC much like a new employee joining the organization:

## 1. Treat agent setup like drafting a job description

Before a human employee starts, you write the job description. You define what role they’ll fill, what they’re responsible for, what behaviors you expect, and what boundaries they operate within.

An agent mesh’s agent builder can use an internal AI agent to provide a guided interface for defining an agent’s purpose, scope, and configuration. You set up the instructions and system prompts that shape the agent’s persona and behavioral parameters. And you configure guardrails – hard constraints on what the agent can and cannot do – that prevent it from going off–script or taking unsafe actions.

## 2. Get the agent up to speed with tool and system access

A new employee’s first weeks are spent getting access to tools, systems, and data. Agent onboarding is the same.

An agent mesh should include a number of data connectors – pre-built integrations to enterprise databases, data warehouses, data lakes, enterprise application APIs, and MCP servers. This enables agents to access real-time data from day one.

Access is provisioned through role-based access controls (RBAC), enforcing least-privilege principles so agents only see what they need to see. It can also define skills that go with internal tools so agents know best how to use them.

## 3. Passing the probation period – stress-test agents before deployment

After getting access to systems, human employees undergo training. This is where general ability becomes company and job-specific skills. You wouldn’t put a new hire in front of customers without first verifying they know what they are doing. The same logic applies here.

An agent mesh can provide an Eval function that uses AI to suggest tests for agents, allows you to add more and then run them against your agents. This empowers the organization to validate agent competence against defined success criteria during development. This supports both initial testing and regression tests as you make changes.

## 4. Keep humans in control – validate AI actions in real-time

Even the most capable employee gets close oversight when they are new to a role. Supervision isn’t micromanagement; it’s the safety net that ensures quality, builds trust, and catches errors before they compound.

An agent mesh with human-in-the-loop architecture would support routing of specific agent actions or decisions to human reviewers for approval before execution. This is important in agentic systems because LLMs are non-deterministic, they make mistakes so when the impact of agents being wrong is too risky, humans can validate their actions, responses or conclusions.

## 5. Teamwork makes the AI agent dream work

The most transformative phase of the employee lifecycle is when individuals become part of high-performing teams, where collective capability exceeds the sum of its parts. For AI agents, this is where things get really interesting.

An agent mesh would support workflows that define repeatable processes, such as the steps involved in approving a loan, providing an insurance quote or opening an account. Dynamic orchestration is where the mesh comes alive: orchestrator agents route work to the right specialists, in sequence or in parallel, adapting in real time when the input is fluid and the path forward must be reasoned through.

The result is a multi–agent mesh topology – hierarchical agent organizations coordinating specialist agents across various functions that mirror the structure of an effective human organization.

## 6. Continuous AI improvement – catch performance drift early

Effective organizations don’t deploy employees and forget about them. They monitor performance, provide feedback, and create mechanisms for continuous improvement.

An agent mesh’s visualizer would give a real-time graphical interface for tracing agent interactions, tool and LLM calls, and decision pathways, so you can see exactly what your agents are doing and why. Ongoing evaluations detect performance drift or emerging failure modes via online evals that run in the background, monitoring production execution.

Further, Open Telemetry instrumentation can surface performance trends over time, giving you the data to make informed decisions about when and how to tune your agents.

## Turning AI agents into mission-critical assets requires a new deployment approach

To turn AI agents from simple experiments into high-performance operational tools requires a whole new mindset for building and developing them. Traditional SDLCs work for predictable code, but AI agents act on their own! As a result, they require clearly defined roles, secure tool access, strict testing, human oversight, and constant monitoring.

To successfully deploy, manage, and scale a workforce of AI agents with confidence, organizations must deploy an ADLC on a real-time and event-driven platform.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

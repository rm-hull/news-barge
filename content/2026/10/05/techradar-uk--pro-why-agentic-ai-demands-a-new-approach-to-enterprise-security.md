---
title: Why agentic AI demands a new approach to enterprise security
source_url: https://www.techradar.com/pro/why-agentic-ai-demands-a-new-approach-to-enterprise-security
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-05T14:32:38Z'
published: '2026-10-05T00:00:00Z'
description: AI autonomy introduces new risks organizations must learn to govern.
image: https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej-2000-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Matt Cooke
locations: []
organisations:
- Agentic AI
- CRM
- EMEA
- Future plc
- Proofpoint
- TechRadar Pro
- TechRadarPro
- Zendesk
---

![A robot hand touching a locked digital shield blocking a human from accessing data](https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Artificial intelligence is moving beyond the chatbot. Across enterprises, AI now does more than summarize documents, draft emails or answer questions. Organizations are increasingly piloting autonomous AI agents that read communications, retrieve information from business systems, update customer records, trigger workflows and execute operational actions with limited human oversight.

That autonomy creates a new kind of exposure. Our research finds 76% of organizations are piloting or rolling out autonomous AI agents, and 42% have already had a confirmed or suspected AI-related incident. Agentic AI is already inside the workplace; the real test is whether organizations can govern it without strangling the productivity gains it delivers.

Matt Cooke is Cybersecurity Strategist for EMEA at Proofpoint.

Unlike traditional generative AI, which responds to a question and stops, agentic AI pursues an objective. It interprets a request, selects tools, accesses data and acts across connected business environments. A conventional assistant might summarize an email chain. An autonomous agent could read it, pull details from a CRM, draft a response, update a Zendesk ticket and schedule a follow-up call.

Each stage may look legitimate on its own, yet the end result could still be wrong, excessive or manipulated. Blocking AI tools outright isn't practical. It just pushes employees toward unapproved services where activity and data flows are harder to see. Leaders need to treat AI agents as a new category of digital worker, with clear boundaries, oversight and accountability.

## Moving beyond traditional access control

Securing autonomous AI agents means moving from access control to behavior-aware governance. Permission to act matters less than whether that action fits the original request, the data it touches, and the consequences it could trigger.

Traditional enterprise security assumes a person makes the decision and a system executes it. Agentic AI compresses that chain. A human writes the prompt, the AI interprets it, pulls in connected tools, and triggers the action itself, often without a checkpoint between decision and execution.

That works fine for low-risk, repetitive, reversible tasks. But once an agent can send external communications, modify sensitive records, approve transactions or change permissions, a misunderstood instruction, or a malicious one, turns into an immediate consequence.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Security teams must assess what an agent is doing, why it is doing it, and whether its actions remain aligned with organizational policy and human intent. Governance has to cover the full chain of activity, from the original request through to the outcome inside a business system.

## The risk of semantic privilege escalation

One emerging concern is semantic privilege escalation, where an agent stays fully within its access rights but stretches them further than the user intended.

An employee asks an agent to "organize customer communications." With access to a CRM, an email platform and a customer database, the agent could read that instruction broadly enough to email confidential pricing details to the wrong contact, message an entire distribution list instead of one recipient, or push through a change that should have needed a manager's sign-off.

The agent stays within its authorization the entire time; the mismatch is between its behavior and human intent. Static permissions can't catch that gap. Organizations need controls that weigh an action's purpose, context and likely impact before it completes, not just its permission level.

## Human risk and data protection

AI agents are directed by prompts, shaped by whatever information they receive, and trusted by employees who assume the output is correct. Three failure points follow from that: what data goes in, how the agent interprets it, and how much employees trust what it produces.

Employees paste sensitive data into prompts or upload confidential files without thinking twice. An agent can misread a request, or get steered by hidden instructions buried in an email, document, chat message or webpage. And employees often wave AI-generated recommendations through without the scrutiny they'd give a colleague's advice.

Prompt injection is the clearest example: attackers hide instructions inside content they know an AI agent will process. If the agent treats that content as trustworthy, it can ignore policy, leak data, alter a workflow or act on an instruction no human ever approved. Against a chatbot, that produces an embarrassing wrong answer. Against an agent with direct access to tools and systems, it produces an executed action.

Data leakage compounds this. Agents typically need broad access to enterprise data, which means sensitive information can travel through prompts, uploads, generated responses, logs and retrieval workflows. Data loss prevention has to extend into these AI environments, flagging sensitive content before it reaches an AI tool, and controlling where that tool can send it.

Email and collaboration platforms deserve particular attention. They sit at the intersection of people, data and autonomous workflows, while also serving as common routes for phishing, malicious links, manipulated files and prompt injection. Among organizations reporting an AI-related incident, 67% saw threat activity in email, 57% in SaaS or cloud applications, and 53% in AI assistants or agents.

Requiring human approval for every automated action would defeat the purpose of deploying agents in the first place. Targeted human-in-the-loop controls work better, reserved for high-impact, irreversible or sensitive decisions such as financial transfers, external communications, permission changes and regulated data sharing.

Lower-risk actions can run autonomously within clear boundaries. Higher-risk actions should pause for human confirmation, require step-up authentication or face additional policy checks.

Agentic AI security rests on four pillars: visibility into human-AI interactions, controls on sensitive data, governance over agent behavior, and audit trails that hold up under scrutiny. These agents are becoming digital colleagues with real system access and real authority to act. They warrant the same scrutiny organizations already apply to privileged users, critical applications and high-risk business processes.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

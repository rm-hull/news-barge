---
title: AI agents can now face an explicit security verdict before acting
source_url: https://www.techradar.com/pro/phone-communications/the-agent-itself-has-become-its-own-entity-to-secure-bitdefenders-new-free-mac-tool-goes-after-flaws-that-let-attackers-fool-ai-models
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-04T17:09:04Z'
published: '2026-10-04T00:00:00Z'
description: AI agents can be manipulated to carry out dangerous actions — Bitdefender's
  AI Guardian is built to stop them
image: https://cdn.mos.cms.futurecdn.net/2BaNK5XKNiUsUgc3MA8WBC-970-80.jpg
categories:
- Technology & Software
people:
- Ciprian Istrate
- Claude Code
locations:
- AI
organisations:
- AI Guardian
- AI Guardian Research
- Bitdefender
- Consumer Solutions Group
- MCP
- TechRadar Pro
---

![AI security](https://cdn.mos.cms.futurecdn.net/2BaNK5XKNiUsUgc3MA8WBC-970-80.jpg)

* **Bitdefender's new software checks AI agent actions before they happen**
* **AI Guardian blocks unauthorized actions from autonomous software agents**
* **AI Guardian records agent decisions so users can examine individual operations**

AI agents increasingly receive access to software tools, private files, and credentials while performing technical tasks for their users every day.

That access creates another security problem because malicious instructions can influence what automated systems attempt to execute without authorization.

Bitdefender has released a public beta of AI Guardian, a macOS security tool that checks what autonomous software agents do before those actions take effect.

## A security checkpoint for autonomous software

AI Guardian is a standalone application that initially supports Claude Code 2.1.121 and OpenClaw 2026.6.6.

The software operates quietly in the background and compares requested operations against rules established by users before allowing them.

Each request receives an allowed, flagged or blocked outcome, while decisions remain recorded for later examination and auditing.

Prompt processing takes place locally, although selected services such as website reputation checks can use Bitdefender's cloud infrastructure.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The system can identify attempts to manipulate agents through hidden instructions and prevent resulting operations from proceeding without approval.

It also examines Model Context Protocol tools, stopping suspicious or altered components before an agent can invoke them.

The software checks supported agent skills before execution, while exposed API credentials can trigger restrictions around protected resources.

It can also block an agent from accessing sensitive resources such as SSH keys and system credentials without authorization.

These controls are intended for developers, technical practitioners, and others who rely on agents for coding or operational tasks.

The company says every decision can be reviewed through an auditable record showing how individual requests were handled.

The security process establishes permitted resources first, then checks individual requests before returning an outcome for each operation.

## Why the need for AI Guardian

Research cited by Bitdefender tested 20 AI agents against more than 1,300 tool poisoning attempts, with attacks succeeding 36.5% of the time.

One model in that testing was manipulated in 72.8% of attempts, illustrating risks that agent capabilities can introduce beyond ordinary chatbot interactions.

Another study reported more than 1.2 million exposed AI service secrets during 2025, representing an 81% annual increase.

That analysis also identified more than 24,000 credentials exposed through publicly available MCP configurations during the same period.

“AI agents are becoming a direct extension of the users who rely on them, inheriting the same security risks that come with that role,” said Ciprian Istrate, senior vice president of operations, Consumer Solutions Group at Bitdefender.

“This rapid shift means security can no longer stop at protecting the human alone; the agent itself has become its own entity to secure…”

AI Guardian is currently free during its public beta period, with the first release limited to English and macOS users.

The company says AI Guardian will eventually roll out for other operating systems, and its agent security lineup already includes two other products.

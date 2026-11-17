---
title: 5 Things That Break When AI Agents Start Acting on Their Own
source_url: https://www.kdnuggets.com/2026/11/collibra/5-things-that-break-when-ai-agents-start-acting-on-their-own
source_site: KDnuggets
source_slug: kdnuggets
description: Five governance problems emerge when AI agents begin taking real-world
  actions, from unmanaged access and identity sprawl to approval bottlenecks and manual
  oversight.
image: https://www.kdnuggets.com/wp-content/uploads/Collibra-Agentic-Control-Ebook-Social-1.png
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-17T03:47:24Z'
categories:
- Technology & Software
- Science
- Business & Entrepreneurship
people: []
locations:
- AI
- Okta
- US
organisations:
- CISOs
- CRM
- Collibra AI Command Center
- Harris Poll
---

# 5 Things That Break When AI Agents Start Acting on Their Own

Five governance problems emerge when AI agents begin taking real-world actions, from unmanaged access and identity sprawl to approval bottlenecks and manual oversight.

![5 Things That Break When AI Agents Start Acting on Their Own](https://www.kdnuggets.com/wp-content/uploads/Collibra-Agentic-Control-Ebook-Social-1.png)

An agent is asked to investigate a data quality issue. It traces the pipeline and finds the root cause. Then it exports 1,800 sensitive customer records to a shared workspace “so the team can verify.” Nobody asked it to, and by its own measure it succeeded.

That scenario is illustrative, but agents do write to production systems now. Five problems follow.

## 1. The Models Are Good Enough. Rollouts Are Stuck.

Task completion on the OSWorld benchmark went from about 12% in 2024 to 66% in 2026. Yet no more than 10% of enterprises are scaling agents in any single function. Most teams can’t say what their agents are allowed to touch.

## 2. Most of the Damage Starts Inside.

80% of organizations report risky agent behavior such as improper data exposure. Few of those cases involve an attacker. A sales team clones a quoting agent and edits the prompt. The copy keeps applying discount rules legal retired a quarter ago.

## 3. Your Agent Inventory Is Wrong.

There are about 45 nonhuman identities for every human. Fewer than half of CISOs know where their agents are or what they can access.1 A developer wires an agent into the CRM over a weekend and quits in March. The agent keeps running on their credentials. Every agent needs its own identity and an owner who still works there.

## 4. Per-Agent Approval Is a Dead End.

If your process ends with a committee signing off on each new agent, drop it. That works at ten agents. It collapses at a hundred, now that agents ship inside software you already pay for. Machine-readable agent contracts hold up better: one baseline every agent inherits, plus narrower rules by risk and domain.

## 5. Manual Review Is Already Eating Your Team.

A Harris Poll surveyed 306 US data, privacy and AI decision makers. 87% said their teams spend hours re-verifying the context their agents rely on. Guardian agents check each action against its contract while it runs, then flag, redirect, or block it. People see only what crossed a line. Everything else just runs.

## Where to Go Next

* Download the playbook for the Scan, Set, Supervise framework and a 10-step action plan.
* Take the AI Trust Score assessment to see which problem to fix first.
* Request a demo of Collibra AI Command Center.

1 Source: Global CISO Insights 2026: Identity security in the age of AI, Okta.

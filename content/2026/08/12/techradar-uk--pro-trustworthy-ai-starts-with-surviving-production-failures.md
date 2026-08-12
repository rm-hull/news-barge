---
title: Trustworthy AI starts with surviving production failures
source_url: https://www.techradar.com/pro/trustworthy-ai-starts-with-surviving-production-failures
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-12T13:38:06Z'
published: '2026-08-12T00:00:00Z'
description: 'Designing AI for the 30% case: rare failures, huge consequences'
image: https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-2560-80.jpg
---

![A hand about to touch a phone. Superimposed on top of it is a pink triangle with exclamation mark inside it. Behind it is a computer display with code on it](https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Evaluating AI agents in production tends to focus only on positive results. Did the agent complete the task? Was the output accurate? Did the demo go well?

The answers to those questions matter, but they miss the case that determines whether an enterprise can actually trust agents with real work: what happens in the 30% of instances where something goes wrong?

Co-founder and CTO of Diagrid.

In financial services, for example, an autonomous agent that mishandles a money-movement workflow doesn't turn into an innocuous support ticket. It creates legal liability that can extend across an entire business.

In healthcare, unchecked data access calls can compromise patient safety and lead to HIPAA violations. Highly regulated industries can’t treat failure as a minor inconvenience. And when the stakes are categorically higher than in most other sectors, it changes what "production-ready" means.

The problem? Most popular agent frameworks were built by teams focused on connecting large language models to reasoning loops and evaluation. While valuable, it's not the same discipline as distributed systems engineering.

Few of these frameworks were built by people who spend their careers thinking about recovery, consistency and fault isolation. Many give little thought to what happens when an agent fails mid-flight, and that gap can be very expensive once agents are handling real-world transactions.

## Replaying From Scratch Doesn't Work

When a sales agent moves through a 10-step workflow and fails at step nine, the naive recovery approach is to start the entire flow over from step one. That sounds harmless until you account for what each step actually costs. Every restart means re-running every LLM call that already succeeded, burning through token spend for work that was already done correctly. At scale, that inefficiency turns a single bug into a real financial problem.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

It also produces a worse experience for the people and systems downstream. In a regulated workflow, it’s sloppy work that becomes a compliance and audit problem waiting to surface.

The fix is durable execution: checkpointing that captures progress at each meaningful step, so recovery means resuming from step nine, not replaying the whole sequence. This has become standard practice in distributed systems, and agent orchestration needs to follow suit.

When you’re evaluating agent frameworks, here’s the question you should ask: if an agent fails partway through a long-running task, does the system resume from where it left off, or does it start over? The answer will tell you the difference between frameworks built for production and those built for demos.

## There’s an Access Problem Nobody Talks About

Security in agentic systems presents its own version of this challenge, and it starts with a question that sounds basic but that most organizations can't seem to answer: can you prove exactly who or what did what, and when?

That question is harder to answer as agents act on behalf of other agents, which act on behalf of humans. Each layer of delegation adds ambiguity about accountability. And when you add MCP servers into the mix, the exposure compounds. MCP gives language models access to company records, patient data and internal systems. The vast majority of MCP servers in production today connect to some kind of database, and the common mistake is granting broad access to that entire data store rather than narrowly scoping what each server can see.

That distinction matters when something goes wrong. If a system with broad access suffers a breach or a supply chain compromise, the attacker gains access to the entire environment. Scoped access, where an MCP server or agent can only reach the specific data it needs for the task at hand, is one of the most overlooked design decisions in agentic architecture right now. It's also a relatively cheap problem to fix before deployment, yet one of the most expensive to fix after a breach.

Identity adds another layer. Many organizations still use traditional authentication protocols that were made for human users logging into applications, not for autonomous systems that act at machine speed and scale. Without verifiable identities for each agent and each component, malicious code can impersonate a legitimate part of the system and operate undetected.

What’s needed here is what’s known as cryptographic attestation: a tamper-proof record of everything that happened in the system tied to the specific identity that did it. That record lets you replay the system's state after the fact and determine with certainty that a specific piece of code accessed a specific system at a specific moment. Why? Because that identity was managed and enforced in real time. It's the difference between a policy that says a component “should” be trusted and a system that can prove what it actually did.

## Design to Limit the Blast Radius, Not Just Patch the Damage

There's also a problem with how most organizations think about vulnerabilities. The industry's attention is almost entirely on patching known CVEs, and that's necessary. But at the same time, it misses something important: a vulnerability only becomes a known CVE after a breach has already occurred. Patch management is inherently reactive and does nothing while a system is actively compromised, by which point malicious code is already trying to move laterally through the network.

This is why runtime enforcement deserves far more attention. The goal isn't just prevention; it's containment. If a system is compromised, can you detect that a component is behaving abnormally and immediately restrict its access, even before you’ve identified or patched the underlying flaw? Limiting the blast radius in real time, rather than relying solely on detection after the fact, is what separates a contained incident from a full-scale breach.

Zero trust principles should be applied specifically to AI workloads, not just inherited from traditional cloud-native security protocols. That means strict authentication and authorization for every agent and MCP server, clear policies on what each component is allowed to access, and controls that stop compromised components from sending data outside the organization.

## You Need to Prove Safety, Not Just Function

This isn’t pessimism toward AI agents; it's about engineering maturity. Every distributed system that has matured into something enterprises trust with critical workloads, from databases to cloud infrastructure, went through this same evolution. They go from optimizing for common cases to designing explicitly for the rare, expensive failure.

Agentic AI is now at that point. The organizations that get it right will be able to sit down with an auditor or a regulator and demonstrate, with evidence, exactly how their systems behave when something breaks:

- Durable recovery that doesn't waste a single completed step.

- Access that's scoped to the task, not the whole database.

- Identity that can be cryptographically verified, not just assumed.

- Containment that activates in real time, not after the fact.

These are the bars that enterprises serious about deploying AI agents at scale need to meet.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

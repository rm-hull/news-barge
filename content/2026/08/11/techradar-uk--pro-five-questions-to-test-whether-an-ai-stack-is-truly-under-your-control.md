---
title: Five questions to test whether an AI stack is truly under your control
source_url: https://www.techradar.com/pro/five-questions-to-test-whether-an-ai-stack-is-truly-under-your-control
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-11T17:09:29Z'
published: '2026-08-11T00:00:00Z'
description: Five tests for genuine enterprise AI control
image: https://cdn.mos.cms.futurecdn.net/Y9gz3ntBvZYTntd8XpFxfL-2560-80.jpg
---

![A blue digital cloud containing lots of symbols on a dark blue background](https://cdn.mos.cms.futurecdn.net/Y9gz3ntBvZYTntd8XpFxfL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Control is one of the easiest words in enterprise AI to misuse.

A business may download a model, run it in its own cloud and negotiate favorable terms, and yet still remain dependent at the points that matter.

Access can create useful freedom. It does not, by itself, prove operating control.

Founder, and CEO/CTO of NEUVIOR.

I have learned to treat sovereignty as an operating discipline, not a nationality badge.

If an organization cannot prove what it is running, who can change it, what it depends on and how it can be retired, its control is largely assumed.

These five questions turn an ambiguous claim into a practical test for procurement, security and leadership teams.

## 1. Can you prove exactly what you are running?

A model name and version number on an architecture diagram are not provenance. Teams need a traceable origin, an artefact identifier, a cryptographic hash or signature, the approved configuration and a record of every material change. That record should include fine-tunes, safety layers, prompt templates, retrieval sources and any post-deployment adjustments that affect behavior.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The harder question is operational: who approved the change, who can make the next one and how quickly can the previous state be restored? If a supplier can alter behavior without the customer seeing the change, or rollback depends on goodwill, control is borrowed. The evidence should be simple enough to inspect during an incident, not buried in a quarterly assurance exercise.

## 2. Can you verify the weights and every critical dependency?

Model weights matter, but they are only one layer of an AI system. The inference engine, libraries, drivers, orchestration tools, safety filters, retrieval components, monitoring services and update channels all shape how it operates. Open weights may remove one dependency while introducing several others.

Every critical component therefore needs an owner, a known version, a license, an update route, a vulnerability response and a credible substitute. Integrity checks should run when the system is built, when it is deployed and after a suspected incident. A bill of materials is useful only when it connects inventory to verification and action. A long list of components with no decision rights is documentation, not control.

## 3. Who controls the infrastructure and operating conditions?

Location is not the same as control. A model can sit in a domestic data center whilst essential decisions remain elsewhere. Teams should map who operates the compute, network, identity system, encryption keys, logs and administrative tools. They should know which party can pause, patch, throttle, inspect or revoke the service, and under what conditions.

Owning the building is not enough if a supplier retains remote administration, a proprietary control plane or the only route to scarce accelerators. Backups and telemetry matter too: where they go, who can read them and how long they persist. The strongest test is a degraded-mode exercise. When capacity disappears, credentials are compromised or a provider becomes unavailable, can the organization continue safely and make its own decisions?

## 4. Which law, license and contract governs the stack?

Technical architecture and legal architecture form the same control map. The relevant questions cover the law, license and contract governing the weights, hosted services, support, telemetry and any fine-tuned assets. They also cover subcontractors, audit rights, incident notification, unilateral changes, export constraints, and the rights available at exit.

Data residency does not settle jurisdiction, and a familiar supplier name does not settle enforceability. Legal, procurement, and security teams should be able to answer from the same evidence set. Contradictions between the contract and the system design are not paperwork problems; they are design defects. The useful test is not whether a supplier appears trustworthy today, but which rights survive a dispute, acquisition, service withdrawal or regulatory change.

## 5. Can you switch, stop and dispose safely?

No AI strategy is controlled until its exit has been tested. Could the organization move to another model, runtime, or provider without rebuilding the entire service? Can it export configurations, evaluation sets, prompts, logs, and fine-tuning artefacts in usable formats? Can it revoke identities and tokens, remove deployed copies, clear checkpoints and caches, and still retain the evidence required for audit or investigation?

Safe stopping deserves the same attention as fast starting. The exit plan should name triggers, owners, sequence, time limits, and recovery targets, then be rehearsed before dependence becomes difficult to unwind. If switching exists only in a contract slide, it is not a credible option. Disposal is the final proof that control includes ending a dependency without creating a new operational or security risk.

## Control must be evidenced, not declared

The answer to these questions will rarely be a clean yes or no. Control has degrees, and different workloads justify different dependencies. What matters is that each answer is evidenced, assigned to an owner and tested again as the stack changes.

Open access, local infrastructure and strong contracts can all reduce risk. None substitutes for the ability to prove what is running, verify its dependencies, identify who can intervene, understand which rules bind it and leave safely.

That is less glamorous than a sovereignty label, but it is the difference between an AI architecture an organization can use and a stack it can genuinely govern.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

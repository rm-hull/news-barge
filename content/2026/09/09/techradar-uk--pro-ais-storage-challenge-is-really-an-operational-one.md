---
title: AI’s storage challenge is really an operational one
source_url: https://www.techradar.com/pro/ais-storage-challenge-is-really-an-operational-one
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-09T12:56:48Z'
published: '2026-09-09T00:00:00Z'
description: Why AI needs autonomous data infrastructure
image: https://cdn.mos.cms.futurecdn.net/9WT9t3hZhDVD84bF8rSypL-2560-80.jpg
---

![A line of robots typing at computers](https://cdn.mos.cms.futurecdn.net/9WT9t3hZhDVD84bF8rSypL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Enterprise infrastructure has always adapted as scale increased. Virtualization tackled server sprawl, cloud computing reduced the need to provision physical resources for every application, and automation made increasingly complex environments manageable. Artificial intelligence presents a different kind of scaling problem.

The discussion around enterprise AI has largely centered on models, GPUs, and inference performance, but those technologies represent only a fraction of what organizations must operate. Every production AI deployment creates a continuous flow of data that must be ingested, protected, moved, analyzed, retained, governed, and eventually archived.

Those activities place demands on infrastructure that are very different from the workloads storage systems were originally designed to support.

Director of Product Marketing at Scality.

This is becoming increasingly apparent as organizations move beyond pilot projects. AI is no longer a single workload running on isolated infrastructure. A single application may include high-speed storage for model training, object storage for inference data, lower-cost capacity for operational datasets, immutable storage for cyber resilience, and long-term archives to satisfy regulatory requirements.

Traditionally, those functions have been handled by separate products with separate management tools, security policies, and operational teams. That architecture worked reasonably well when data moved slowly and applications followed predictable lifecycles. AI changes both assumptions.

Training datasets expand continuously. New models are introduced far more frequently than traditional enterprise applications. Inference workloads fluctuate as demand changes. The same dataset may move repeatedly between active processing, backup, compliance, and archival over its lifetime.

Each transition introduces another operational task, another opportunity for inconsistency, and another point where administrators must intervene. Before long, the effort required to manage the infrastructure begins to rival the effort required to build the AI applications themselves.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Complexity becomes the real infrastructure challenge

For years, the answer to operational complexity was automation. Administrators automated provisioning, scripted maintenance, and orchestrated repetitive tasks. Those capabilities remain valuable, but they were designed to execute predefined actions under predefined conditions.

AI environments are considerably less predictable. Infrastructure must continually adapt to changing workloads, shifting performance requirements, evolving security policies, and rapidly growing data volumes, often without the benefit of stable operating patterns.

That is where autonomous data infrastructure represents something more substantial than another automation framework. Rather than treating storage as a collection of independent systems, it starts with the assumption that the platform itself should continuously optimize how data is managed throughout its lifecycle. Capacity, performance, protection, and cost become policy decisions rather than infrastructure projects.

Data moves between performance tiers automatically according to business requirements instead of being exported, migrated, and re-imported into separate platforms. A single namespace spans workloads that historically required multiple storage systems, allowing infrastructure to evolve without repeatedly forcing administrators to redesign the environment.

That architectural change may ultimately prove more important than the automation itself. Many organizations underestimate how much operational complexity accumulates simply from running multiple storage platforms. Every environment has its own authentication model, monitoring tools, lifecycle policies, upgrade schedules, recovery procedures, and performance characteristics.

As AI expands across the enterprise, those management layers multiply alongside the data. Reducing the number of operational boundaries often creates greater long-term value than introducing another layer of orchestration.

The same principle applies to cyber resilience. AI has increased the value of enterprise data far beyond traditional business records. Training datasets, model checkpoints, vector indexes, and inference pipelines have become strategic assets in their own right. Protecting them requires more than backup software. It requires infrastructure that assumes failures and attacks will occur and is designed to recover without depending on manual intervention.

## Governance becomes part of the data lifecycle

The conversation also extends beyond security to control. As AI initiatives become more strategic, organizations are under growing pressure to understand where data resides, who can access it, and which legal and regulatory frameworks govern it.

That is especially true for enterprises operating across multiple countries or in highly regulated industries, where data residency requirements, digital sovereignty initiatives, and industry-specific compliance obligations increasingly influence infrastructure decisions.

Rather than treating these as separate governance exercises, modern infrastructure must make location, retention, and access policies part of the data lifecycle itself, enabling organizations to meet regulatory requirements without introducing additional operational complexity.

One of the more significant design decisions behind autonomous data infrastructure is that immutability exists within the storage engine itself rather than being implemented solely through administrative policy. Instead of modifying existing data in place, new versions are written separately while previous versions remain intact.

Combined with distributed self-healing that rebuilds only affected objects instead of entire disks, this creates a fundamentally different operational model for resilience. Recovery becomes part of normal system behavior instead of an exceptional event requiring administrators to coordinate lengthy repair efforts.

## Infrastructure operators become infrastructure architects

Perhaps the most interesting implication has little to do with storage technology itself. Infrastructure teams are already responsible for environments that are growing faster than headcount, and AI is accelerating that imbalance. The objective is not to remove people from operations, but to reduce the amount of time highly skilled engineers spend on repetitive maintenance that adds little strategic value.

As more routine activities become policy-driven and continuously optimized, infrastructure professionals can devote more attention to architecture, governance, capacity planning, and aligning technology decisions with business priorities.

That evolution mirrors what is happening across software engineering, networking, and cybersecurity. AI is steadily shifting human expertise away from repetitive execution and toward system design, governance, and strategic decision-making. Autonomous data infrastructure reflects the same progression.

Rather than asking administrators to manage an ever-growing collection of storage products, it treats the infrastructure as an adaptive system that operates within policies established by the people responsible for it. The most effective approach is not to take humans out of the loop, but to keep them in control of the decisions that shape security, compliance, and business outcomes while allowing the platform to execute routine operational tasks autonomously.

Viewed from that perspective, autonomous data infrastructure is less about storage than it is about preparing enterprise IT for the next decade. AI has exposed the limitations of architectures built around isolated products, manual coordination, and steadily increasing operational overhead.

Organizations will continue investing in faster GPUs and more capable models, but those investments will deliver their greatest value only if the infrastructure beneath them becomes equally capable of managing complexity. The next generation of enterprise infrastructure will not simply store data more efficiently. It will actively participate in operating the environments that modern AI depends upon.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

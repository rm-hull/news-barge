---
title: 'AI Storagemaxxing: Your GPUs are optimized, what about your data?'
source_url: https://www.techradar.com/pro/ai-storagemaxxing-your-gpus-are-optimized-what-about-your-data
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-15T11:29:13Z'
published: '2026-10-15T00:00:00Z'
description: AI data storage is just as important as compute
image: https://cdn.mos.cms.futurecdn.net/M6fvPLRyP9CRCBwfYj7mxL-2560-80.jpg
categories:
- Technology & Software
people: []
locations: []
organisations:
- AI
- Cloud Strategy
- Future plc
- TechRadar Pro
- TechRadarPro
- Wasabi
---

![Digital representations of phones and cards in slots](https://cdn.mos.cms.futurecdn.net/M6fvPLRyP9CRCBwfYj7mxL-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Enterprise investment in artificial intelligence has, understandably, been concentrated on compute. Access to GPUs, model performance and the cost of inference have become central considerations as organizations move AI workloads from experimentation towards production.

Vice President of Cloud Strategy at Wasabi.

However, an increasing proportion of the economic and operational challenge sits elsewhere in the infrastructure stack. AI depends on data at every stage of its lifecycle: datasets must be collected and prepared, training data must be made available to compute, checkpoints and model artefacts must be retained and information may need to move between infrastructure providers as workloads and commercial priorities change.

As these workloads scale, the storage layer is becoming a strategic component of AI infrastructure with significant implications for the economics of enterprise AI.

## AI is changing the role of storage

Traditional storage strategies have generally been built around considerations such as capacity, availability, performance and retention. AI introduces another dimension: the relationship between storage and the changing requirements of the wider infrastructure environment.

Different stages of an AI workflow have different storage requirements. Data being actively processed may require high-performance infrastructure, while historical datasets, checkpoints and model artefacts may place greater emphasis on durability, security, accessibility and cost. Applying the same storage approach across the entire lifecycle can therefore result in inefficient infrastructure utilization.

The challenge is particularly significant because AI data volumes can be substantial and continue to expand as organizations generate additional training data, model versions and associated artefacts.

The objective should not be to minimize storage expenditure in isolation. It should be to ensure that data is held on infrastructure appropriate to its role, while maintaining the performance, security and accessibility required by the business.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

This is the foundation of what can be described as AI storagemaxxing: the systematic optimization of storage across the AI lifecycle to ensure that infrastructure investment is aligned with business and workload requirements.

## Data mobility is becoming an infrastructure requirement

Organizations are adopting a broader range of infrastructure providers, including hyperscalers, specialized GPU providers and emerging cloud platforms known as neoclouds. The economics and availability of these environments can change rapidly, creating incentives to move workloads between providers. Compute can be relatively straightforward to reallocate. The associated data is considerably less mobile.

Large training datasets and model artefacts can be expensive and operationally complex to transfer. Where significant charges are associated with moving or retrieving data, organizations may find themselves constrained by infrastructure decisions that were made at an earlier stage of their AI program, creating a form of unintended dependency.

The ability to move data should therefore be considered when designing AI infrastructure, rather than treated as a contingency for a future migration. Open standards and interoperable storage can provide an important degree of separation between data and compute, allowing organizations to adapt their infrastructure strategy as market conditions change.

For technology leaders, this creates a broader consideration than simply assessing the cost of storage capacity. The relevant question is the total economic and strategic cost of retaining data within a particular environment.

## Storage optimization must include security

Training datasets, proprietary information and model artefacts can represent significant commercial value. At the same time, the number of applications and automated systems interacting with enterprise data is increasing. Storage resilience must therefore form part of the AI security strategy.

Immutable copies, appropriate access controls and robust recovery processes can help organizations protect critical data from ransomware, accidental deletion and unauthorized modification. These capabilities are particularly important for datasets that would be difficult or expensive to recreate.

Security should consequently be considered alongside performance and cost when determining where AI data resides. A storage environment that reduces expenditure but creates unacceptable recovery or security risks does not represent effective optimization.

## Predictable economics will become increasingly important

Storage costs can include capacity, access, retrieval and data transfer. Where these costs are difficult to predict, they can complicate infrastructure planning and influence architectural decisions. This becomes particularly problematic when organizations need to move large datasets between storage and compute environments.

Predictable storage economics allow organizations to make infrastructure decisions based on workload requirements rather than uncertainty over the cost of accessing or moving their data. This distinction will become increasingly important as AI workloads mature. During experimentation, infrastructure decisions can be relatively temporary.

Production workloads, by contrast, may persist for years and generate substantial quantities of associated data, so the storage strategy needs to account for the full lifecycle of that data, rather than the requirements of a single workload or infrastructure deployment.

## The strategic role of the data layer

The next phase of enterprise AI adoption will require organisations to look beyond compute optimisation. GPUs will remain critical. Model efficiency will remain important. However, neither can be optimized effectively without considering the data on which AI workloads depend.

AI storagemaxxing provides a useful framework for applying the principle: storage should be treated as part of the AI operating model. Assess storage according to several strategic criteria: whether it is appropriate for the workload, does it provide adequate protection and recovery, are the economics predictable, and could data be moved without friction as infrastructure requirements evolve.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

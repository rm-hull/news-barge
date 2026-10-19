---
title: Arm fits up to 23 AGI CPU servers into a 24 kW rack
source_url: https://www.techradar.com/pro/arm-agi-cpu-crushes-amd-in-new-agentic-ai-benchmark-but-what-does-its-2x-rack-level-performance-advantage-mean-for-the-future-of-x86-data-centers
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-19T04:34:31Z'
published: '2026-10-19T00:00:00Z'
description: AMD and Intel face a new challenge as Arm’s agentic AI benchmark points
  to higher rack-level computing capacity
image: https://cdn.mos.cms.futurecdn.net/LJiLEMa769tLHbMg8ahzT5-1600-80.jpg
categories:
- Technology & Software
people:
- Mohamed Awad
locations: []
organisations:
- AGI CPU
- AMD
- Arm
- Arm’s
- Cloud AI
- Fujitsu
- Intel
- Meta
- OpenAI
- Signal65
- TechRadar Pro
---

![ARM](https://cdn.mos.cms.futurecdn.net/LJiLEMa769tLHbMg8ahzT5-1600-80.jpg)

* **Arm’s AGI CPU nearly doubles AMD’s modelled rack-level performance across seven workloads**
* **A 24-kW rack accommodates up to 23 Arm servers under the assessment’s assumptions**
* **Arm’s rack-level advantage reaches 3.19x in the strongest individual workload**

Arm’s AGI CPU has recorded nearly twice the modelled rack-level performance of AMD’s EPYC 9755 across seven workloads designed to evaluate agentic artificial intelligence.

The assessment, conducted by Signal65 with Arm’s cooperation, compared measured processor results before estimating performance across racks operating within a fixed power budget.

The findings rely partly on power-based modelling, while testing on final production hardware remains outstanding.

## Rack density gives Arm a substantial advantage

The assessment examined workloads involving software tools, autonomous task execution, information retrieval, and support for AI model serving, including Terminal-Bench 2 and SWE-bench.

Across the seven tests, Arm’s processor achieved an average performance ratio of 1.99x, with individual results ranging from 1.43x to 3.19x compared with AMD’s EPYC 9755.

The modelled advantage partly comes from differences in server power consumption, allowing more Arm systems within the same electricity allocation.

A 24 kW rack could accommodate 21 to 23 AGI CPU servers, compared with 13 dual-socket EPYC 9755 systems.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

That configuration provides between 5,712 and 5,888 physical cores for Arm, compared with 3,328 for AMD, although the comparison depends on the rated power assumptions.

Individual server power ranges from 950 to 1,050 watts for Arm’s systems, while AMD’s dual-socket configurations carry a rated consumption of 1,700 watts.

Across workload categories, Arm recorded modelled rack-level advantages averaging 1.7x for tooling, 2.0x for agentic workflows and 2.2x for reasoning and planning.

The report also estimated that database and vector-search operations could require 30% to 35% fewer racks for equivalent processing workloads.

## Faster sandbox creation and the x86 challenge

Separate testing compared Arm’s processor against AMD’s EPYC 9965 using Sandbench, which measures the time required to establish isolated execution environments.

Arm completed cold starts 45% faster, warm starts 27% faster, and its worst-case scenario under fourfold oversubscription 41% faster.

These improvements matter because AI agents frequently create execution environments while accessing services, running code, and processing information.

Faster setup can reduce delays, although the results do not demonstrate equivalent gains across all applications or complete data center deployments.

Arm executive vice president for Cloud AI Mohamed Awad said, “The industry needs to measure how well systems handle the work agents actually complete,” describing the need for workload-specific performance evaluation.

The company developed its evaluation framework with support from Fujitsu, Meta and OpenAI, while Signal65 independently verified the reported processor results.

Arm also acknowledged that further testing on final production systems would cover additional workloads and competitive comparisons.

For AMD and Intel, the findings suggest that Arm-based servers could challenge x86 infrastructure in agentic AI deployments where rack power limits constrain computing capacity.

Higher rack-level performance could let operators accommodate more AI workloads within existing power allocations.

However, the benchmark does not establish that Arm will outperform x86 across general-purpose computing or justify replacing existing servers across entire data centers.

Software compatibility, deployment costs and real-world operating conditions will influence whether the modelled advantage translates into wider adoption.

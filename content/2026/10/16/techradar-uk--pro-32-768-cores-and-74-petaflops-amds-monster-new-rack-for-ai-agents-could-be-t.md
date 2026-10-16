---
title: AMD is preparing a massive overhaul of the data center rack for the AI age
source_url: https://www.techradar.com/pro/32-768-cores-and-74-petaflops-amds-monster-new-rack-for-ai-agents-could-be-too-much-for-traditional-data-centers
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-16T21:03:45Z'
published: '2026-10-16T00:00:00Z'
description: The AI agent boom is demanding new hardware — AMD’s answer is a radical
  rack with up to 32,768 cores and 16 GPUs
image: https://cdn.mos.cms.futurecdn.net/9tasRtXoH4yfhJmxkE4z9k-1920-80.png
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- Venice
organisations:
- AI
- AMD
- Open Compute Project
- TechRadar Pro
---

![AMD rack-scale computing system](https://cdn.mos.cms.futurecdn.net/9tasRtXoH4yfhJmxkE4z9k-1920-80.png)

* **AMD's proposed rack combines 32,768 CPU cores with 16 AI accelerators**
* **Traditional data centers may need new power and cooling infrastructure**
* **AMD divides agent workloads into personal, enterprise, and technical computing categories**

AMD is developing a rack-scale computing system for artificial intelligence agents, with configurations designed for personal, enterprise, and technical workloads.

Dubbed Helion Agentic AI Rack, it supports up to 32,768 Zen 6 x86 CPU cores, 16 Instinct MI350P accelerators, and 74 petaflops of FP4 computing performance.

The proposed platform also supports 102 Tbps of networking bandwidth and uses modular hardware designed for different agent computing requirements.

## A rack built around three kinds of AI agents

AMD groups agent workloads into three categories: personal assistants, enterprise applications, and technical computing, each with different processing requirements.

Personal agents need dense, energy-efficient servers; enterprise applications require a balance between agent capacity and performance; while technical workloads prioritize processing speed.

AMD allows operators to customize CPU core density, processing performance, and power consumption according to their workloads.

The hyperscale configuration uses CPU-only infrastructure, while the enterprise version combines processors and graphics accelerators within an integrated rack.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

For personal agents, the system uses 256-core Venice processors operating at 400W, prioritizing processing density and power efficiency.

Enterprise workloads use the 256-core Venice processors rated at 600W, while technical computing uses 96-core, high-frequency Venice processors.

The enterprise configuration separates agent execution, inference, and general-purpose computing into distinct server nodes.

CPU sandbox nodes handle agent execution, Instinct MI350P accelerators support inference, and general-purpose servers accommodate databases, storage, and technical computing.

AMD also includes an integrated token router for directing agent model requests across frontier and open-source models.

The rack supports programmable networking, an open-source software ecosystem, and ORv3 44OU hardware compliant with Open Compute Project specifications.

## Why traditional data centers may need substantial changes

Traditional data centers are built for standard cloud or legacy enterprise computing, not racks packing up to 32,768 Zen 6 CPU cores alongside heavy GPU configurations.

Therefore, facilities built around existing server arrangements may lack the appropriate combination of power delivery, cooling capacity and network infrastructure for these configurations.

Workload diversity creates another challenge because personal agents, enterprise applications and technical computing require different processing characteristics.

AMD's proposed rack mixes dense 256-core processors with 96-core high-frequency systems, requiring infrastructure that can accommodate different server types and operating requirements.

This creates a planning challenge for data centers, which must allocate rack space, power, and cooling to different server configurations instead of deploying identical systems.

Operators may need to modify existing infrastructure if it cannot support the selected combination of high-core-count and high-frequency servers.

Networking introduces an additional consideration because the rack supports up to 102 Tbps of bandwidth and integrates a programmable token router.

Existing facilities may need compatible networking equipment and software to support this throughput and route model requests across different AI systems.

The Helion Agentic AI Rack is scheduled for availability in November 2026, but AMD has not disclosed complete facility upgrade costs or cooling requirements.

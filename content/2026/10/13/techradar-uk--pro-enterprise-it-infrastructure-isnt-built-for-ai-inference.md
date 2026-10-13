---
title: Enterprise IT infrastructure isn’t built for AI inference
source_url: https://www.techradar.com/pro/enterprise-it-infrastructure-isnt-built-for-ai-inference
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-13T16:58:20Z'
published: '2026-10-13T00:00:00Z'
description: AI inference requires fundamentally new, distributed enterprise infrastructure
image: https://cdn.mos.cms.futurecdn.net/h8ZQHernNUVpnGYX7QnxVM-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations: []
organisations:
- API
- Autonomous AI
- Deloitte
- Future plc
- GPU
- Gartner
- IDC
- IT
- McKinsey
- Megaport
- TechRadar Pro
- TechRadarPro
- WANs
---

![The letters AI in a box in the middle of a vast digital room divided by beams of line](https://cdn.mos.cms.futurecdn.net/h8ZQHernNUVpnGYX7QnxVM-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

As global AI investment continues to climb — it surpassed $300 billion in 2025, according to IDC — enterprise IT remains primarily focused on supporting the development of training models, with architecture such as large GPU clusters and high-density compute taking center stage.

But now AI inference is becoming the dominant workload, and the architecture that supports models in production, at scale, and to real users and systems has quickly become the future of AI.

The demand for AI inference is there — according to Deloitte, inference already accounts for roughly two-thirds of compute, while McKinsey projects that it will represent between 30% and 40% of total data center demand by 2030 — however, the dedicated infrastructure is not.

CEO of Megaport.

## Inference is more than a scaled-down training environment

What training and inference require from an IT point of view are very nearly polar opposites. Enterprises have facilitated AI training via data centers with massive, centralized data GPU clusters for extreme power density and specialized, high-speed interconnects meant to maximize communication within a single room.

Inference, on the other hand, is defined by a continuous flow of information and unpredictable user demand as opposed to a pre-defined workload. Once the prompts start coming in, you need geographically distributed compute that responds to and scales with real-time demands.

Because inference runs 24/7 and requires millisecond-fast responses for end users, it relies on commodity ethernet, geographically distributed edge sites, and low-latency network connections rather than isolated throughput within a single data center. The very design choices that make an enterprise data center optimal for training actively work against running inference at scale.

The cost structure is entirely different, too. Training is a one-time capital event — once a model is built, that cost is already sunk. Organizations that continue to optimize their spending for training are now being hit with the reality that they have the wrong foundation.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Inference, meanwhile, is a recurring operational cost that scales with every user, query, agent interaction, and more. It’s more like a living, breathing organism which needs to grow alongside the kind of workload that is going to determine the future of AI economics.

## Agents are creating new strain on architecture

Autonomous AI agents are also compounding the infrastructure deficit. Agents don’t generate a single response and then stop; they plan, execute across multiple steps, call external tools, coordinate other agents, and pass outputs between systems. The ripple effect of an agentic workload multiplies the data traffic flowing through a network. As demand for agentic solutions grows, so will the demand for supporting infrastructure.

That growth is already consequential. Gartner predicts that by the end of 2026, 40% of enterprise applications will be integrated with task-specific agents, while IDC projects that agent usage will surge tenfold by 2027, with token and API call volumes multiplying by a factor of thousands.

Inference is also acting as a north-south traffic multiplier in ways that traditional WAN and data center network architectures aren’t designed to handle. McKinsey found that most enterprise WANs are currently unable to support AI data traffic patterns, and must evolve as AI now ranks as the second-highest infrastructure investment priority.

Burst traffic is another issue impacting architecture strain. Agentic workloads aren’t a steady flow, they’re a torrential downpour that comes and goes. A single orchestration event can trigger dozens of downstream API calls simultaneously.

This causes networks that are sized for average loads to hit capacity ceilings when agents coordinate at scale, creating the same latency and reliability problems that lead enterprise AI pilots to crash before reaching production. To thrive in the AI era, enterprises must build the proper infrastructure from the ground-up.

## Inference is now the critical CPU use case

Building inference-forward architecture starts at the most basic layer: hardware. CPUs are critical for planning, scheduling, tool-call coordination, and the multi-step reasoning loops that define agentic workloads.

However, the industry’s heavy focus on the GPU market during the AI training boom has directed attention away from the necessity for CPUs in AI inference workloads. As inference workloads increase in scale, CPUs move from a supporting role to a critical one, acting as the main filter to the orchestration layer.

When viewed through a purely agentic lens, high-core-count server CPUs can handle the workload more economically than GPU accelerators. But it’s important to understand that one cannot function without the other. Inference still demands GPU function; it’s simply that CPU capacity is the bottleneck that most organizations aren’t accounting for.

## Aligning compute, network, and storage is key

The reality is that AI use cases are generating abysmal ROI in most cases. Gartner’s most recent survey of infrastructure and operations leaders found that only 28% of AI use cases fully succeed and meet ROI projections, while 20% fail outright. The leading cause of failure was expecting too much, too fast from infrastructure that was incapable of supporting the workload.

How can enterprises avoid that trap? Take the time to set up their underlying infrastructure before diving headfirst into building systems they can’t support. Putting real effort into building dedicated compute, network, and storage that function as individually managed resources is the key.

Inference at production scale requires all three to work in tandem, with compute handling model execution, storage determining how quickly context, embeddings, and retrieval data are available, and network defining whether compute and storage can communicate externally with the appropriate latency

The organizations that can make this distinction early will be better prepared for the next phase of AI, and will spend less time managing infrastructure failures during production, and more time actually focusing on generating value through AI inference.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

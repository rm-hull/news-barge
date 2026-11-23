---
title: Uncovering the operational blind spots driving GPU overspend
source_url: https://www.techradar.com/pro/uncovering-the-operational-blind-spots-driving-gpu-overspend
source_site: TechRadar UK
source_slug: techradar-uk
description: Poor GPU utilization is driving up AI infrastructure spending
image: https://cdn.mos.cms.futurecdn.net/ywSwn3oGxXv4PfcRPZmTrc-2560-80.jpg
published: '2026-11-23T00:00:00Z'
scraped_at: '2026-11-23T12:20:26Z'
categories:
- Technology & Software
people: []
locations:
- AI
- Europe
organisations:
- CPU
- Datadog
- FinOps FinOps
- Future plc
- GPU
- TechRadar Pro
- TechRadarPro
- VP EMEA
---

![ Man coding programmer, software developer working on digital tablet with binary, html computer code on virtual screen](https://cdn.mos.cms.futurecdn.net/ywSwn3oGxXv4PfcRPZmTrc-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

As AI moves from experimentation to a more operational phase, the pressure to deliver faster, support more workloads and secure additional compute is understandable. But the cost of the underlying technology is harder to ignore, and few resources illustrate this more clearly than GPUs.

While GPUs provide the computing power modern AI applications require, investing in more capacity without understanding how existing resources are being used risks scaling the waste alongside the ambition.

VP EMEA at Datadog.

Recent research found just 37% of IT leaders in Europe actively optimize their AI spend. Without a clear view of what they are getting from their investments, organizations risk paying for more compute while leaving existing resources underused.

Leaders, therefore, need to understand whether additional spending will improve performance or simply accommodate existing inefficiencies. So, before approving the next investment, leaders should ask: do we need more capacity or are we failing to get enough value from what we already have?

## The hidden sources of GPU waste

GPU waste doesn't necessarily mean a device is completely idle. A workload can reserve several GPUs even when much of its processing happens on the CPU, leaving some accelerator capacity underused. Other workloads may consume GPU resources without using them effectively, while zombie processes can continue to hold capacity and waste GPU spend. These inefficiencies can quickly accumulate as deployments scale.

The distinction matters because each problem requires a different response. A workload constrained by the CPU will not necessarily run faster with more GPUs. An abandoned process needs to be removed. An inefficient workload needs to be tuned before its resource allocation grows. Buying additional capacity without identifying the cause can increase spending without resolving the performance problem.

## The growing complexity of GPU management

Hybrid environments make this more difficult. GPUs may be running on-premises, across public clouds, or through GPU-as-a-Service platforms. Each environment can expose different telemetry, while teams often rely on separate tools to monitor infrastructure, Kubernetes, applications, model workloads, and cloud costs. The result is fragmented information, making it harder to connect infrastructure costs with the workloads responsible.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Technology leaders are in the process of shifting from securing enough compute to managing it effectively. With AI workloads spread across on-prem systems, public clouds and specialist GPU providers, capacity, performance and spending are increasingly hard to assess.

GPU decisions now affect applications teams, finance and long-term planning, often requiring investment before workloads are fully understood. As organizations expand GPU use, it's becoming critical to know what value that infrastructure is actually delivering.

## Putting GPU costs into context for FinOps

FinOps teams require more than a static view of infrastructure costs to understand AI expenditure. They need to connect cost to capacity, utilization and workload behavior. This means bringing information from the GPU, server, workload and application layers into a single view, with cost linked to the resources and workloads that generate it.

Costs can then be broken down by services, namespaces, training jobs, clusters or owners, helping teams prioritize areas for optimization. An unexpected increase in spending becomes something teams can investigate: which workload changed, why is it consuming more resources and who can act on it?

This gives FinOps, platform and machine learning teams a shared source of truth for investigation and optimization. Platform engineers can identify inefficient workloads, while machine learning teams can examine how those workloads use GPU resources and adjust them as needed.

Instead of switching between separate views of infrastructure, workload performance, and cost, teams can investigate and address inefficiencies in the same operational context.

It also creates accountability. A cost attributed to a specific workload, with a team responsible for it, is far more actionable than an unexplained increase in infrastructure budget.

## Looking beyond utilization with GPU monitoring

Effective GPU observability shouldn’t stop at measuring utilization percentages. Engineers need to see across the AI stack, from the workload using a GPU to the host running it and the specific accelerator involved.

Low utilization can stem from different causes. CPU saturation, resource contention, and workloads that do not make effective use of GPUs can all reduce the value gained from available capacity. Understanding those causes helps teams decide whether to tune a workload, resolve an infrastructure bottleneck or reclaim resources.

Equally, a busy GPU is not proof of a productive workload. Teams should judge efficiency by whether a workload delivers its intended result at an acceptable cost and speed. Pursuing higher utilization for its own sake can obscure that question, while spare capacity may be necessary to handle peaks or maintain resilience.

The practical value of monitoring is the decision it enables. When a training run repeatedly stalls or fails, teams need to identify the cause before committing more resources to another unsuccessful attempt.

## Moving from monitoring to optimization

GPU efficiency should be part of daily operations rather than a periodic cost review. Capacity planning should use real utilization data; underused devices should be reclaimed, stalled or abandoned workloads removed, inefficient workloads tuned, and hardware health monitored alongside workload performance.

As AI infrastructure expands across on-premises systems, public clouds and specialized GPU providers, consistent monitoring becomes more important. That insight gives organizations a clearer basis for deciding when to optimize existing infrastructure and when to invest in additional resources.

Before approving more capacity, technology and finance teams should share an understanding of the demand it will serve, the constraint it will address and how success will be measured. Teams that can answer those questions have a stronger case for investment and a better chance of directing it where it will make a difference.

For companies operating AI tools at scale, GPU spend is becoming a resource-allocation question as much as an infrastructure one. The decisions made around capacity today will shape both the cost and flexibility of future AI deployments.

More GPUs may be the right answer to support and scale your AI strategy. But the next purchase should address a demonstrated need, rather than compensate for an inefficiency that has yet to be investigated.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

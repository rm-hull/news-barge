---
title: Data movement is the new performance battleground in semiconductor design
source_url: https://www.techradar.com/pro/data-movement-is-the-new-performance-battleground-in-semiconductor-design
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-11T13:13:21Z'
published: '2026-08-11T00:00:00Z'
description: The next breakthrough in AI starts with moving data faster
image: https://cdn.mos.cms.futurecdn.net/YoQ7bF6XQjs33SMa72NcwK-2560-80.jpg
---

![Light blue folders from a computer operating system on a dark blue background](https://cdn.mos.cms.futurecdn.net/YoQ7bF6XQjs33SMa72NcwK.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

For much of the semiconductor industry’s history, performance debates have centered on compute throughput and memory capacity. Faster processors, wider vectors, and larger caches have been the primary levers for system architects, often treating the movement of data between them as a secondary concern.

Today, a different constraint is asserting itself as AI data center workloads proliferate, architectures diversify, and systems extend beyond traditional computing into the physical world. Data movement, rather than processing or storage, is increasingly defining the limits of performance, power efficiency, predictability, determinism, and scalability.

VP of Product Management and Marketing at Arteris.

This shift around data movement is already visible. Across applications like advanced SoCs, AI accelerators, chiplet-based systems, and now in physical AI applications such as robotics, industrial automation, and intelligent vehicles, it has become clear that transporting the vast quantities of data required by such workloads is more demanding than processing them.

Physical AI does not introduce a new problem so much as it exposes an existing one: when systems must perceive, decide, and act in closed loops under real-time and safety constraints, inefficient or unpredictable data movement quickly becomes the dominant bottleneck.

The implications for both AI in the data center and physical AI extend far beyond any single market. As data center demand increases exponentially and the industry pushes toward increasingly complex, heterogeneous systems in anything from vehicles to industrial systems, data movement has become the primary performance battleground.

## Performance limits are increasingly defined by data movement

Modern semiconductor systems integrate an unprecedented number of processing elements, including general-purpose CPUs, AI accelerators, GPUs, DSPs, sensor processors, and domain-specific engines. Still, simply adding compute resources rarely delivers proportional gains. In many advanced designs, performance plateaus long before compute capacity is exhausted.

Compute units are left sitting idle not because they lack capability, but because data cannot reach them efficiently or predictably. Late-stage analysis of high-performance SoCs often reveals that throughput shortfalls stem from contention, imbalanced bandwidth allocation, or inefficient routing within the communication fabric, rather than from compute limitations.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

This is especially visible in physical AI systems, where delays introduced by data movement propagate directly into system behavior in closed-loop architectures. Latency or contention in the transport fabric can destabilize control algorithms, reduce accuracy, and even force over-provisioning of compute to compensate for the absence of bounded latency and guaranteed behavior.

While physical AI makes data movement constraints more immediately visible, the same forces are amplified dramatically in the data center. To push enormous volumes of data through extremely wide interfaces, processors increasingly contain hundreds of compute and accelerator instances, press against reticle-scale integration limits, use chiplet-based designs, and interface with multiple stacks of high-bandwidth memory (HBM).

As designs scale, the combined costs of moving data grow rapidly. In this environment, abundant compute and memory bandwidth offer little benefit without a data movement architecture capable of managing data at scale. What is a tight constraint in physical AI becomes an overwhelming one in the data center.

In both the AI data center and physical AI, performance is inseparable from the behavior of the data paths that connect perception, decision, and actuation. As a result, interconnect design can no longer be a back-end integration task. It has become a central architectural decision, on equal footing with compute and memory selection.

## On-chip data movement is fundamentally different

Data movement inside a chip operates under constraints that differ radically from those of off-chip networking or board-level interconnect. On-chip transfers are extremely frequent, tightly synchronized with execution, and subject to stringent latency and power budgets.

Traffic is also inherently heterogeneous. A single system may need to carry high-bandwidth AI data streams, cache and coherency traffic, latency-critical control messages, and safety-related signaling, often simultaneously. These flows have very different requirements and cannot be treated uniformly.

Traditional best-effort arbitration models break down quickly under these conditions. Bursty accelerator traffic can interfere with control-plane and real-time data paths, leading to unpredictable system behavior. In mission and safety-critical or physical AI applications, such interference is unacceptable.

As a result, quality of service (QoS), traffic isolation, bounded latency, and determinism are now architectural requirements, not just optional optimizations. The interconnect fabric increasingly functions as an active system component, enforcing policy and guaranteeing behavior, rather than as a passive conduit for bits.

## AI, heterogeneity, and physical intelligence magnify the challenge

AI workloads fundamentally change the character of data movement. They generate massive data volumes, irregular access patterns, and asymmetric traffic flows. At the same time, heterogeneous architectures distribute computation across many specialized engines, eliminating any single “center” of the system.

In both data center and edge contexts, this decentralization increases coordination costs. Data replication, synchronization overhead, and inefficient sharing can consume significant power and latency, eroding the benefits of specialized compute. Rather than compute placement, the challenge designers face now lies in how to efficiently orchestrate data movement between diverse compute elements.

Physical AI places additional pressure on these architectures. Unlike batch or best-effort inference workloads, physical systems operate continuously in real time. Sensor data must be ingested, processed, and acted upon within strict deadlines. Feedback loops amplify even small inefficiencies in data movement.

Together, these demands reinforce the broader lesson that heterogeneity without a deliberate data movement architecture leads to complexity and inefficiency, not scalability.

## Chiplets turn data movement into a system-level design problem

Chiplet-based multi-die architectures promise yield advantages, faster innovation cycles, and importantly, flexibility. But they also elevate data movement challenges beyond a single piece of silicon.

Cross-die communication introduces higher energy per bit, tighter physical and architectural constraints, and more extra latency than on-die data movement. Interfaces that were trivial within a single die become critical bottlenecks once they must traverse package boundaries.

Successful chiplet systems, therefore, require system-level planning of data movement, encompassing topology, hierarchy, coherency and protocol selection, and physical constraints. Partitioning functionality without an integrated strategy for how data flows between partitions often increases, rather than reduces, overall system complexity.

Control and safety domains may span multiple dies, and failures or delays in inter-die communication directly affect system behavior. Chiplets demand not only modular compute but also modular, predictable connectivity.

## Deliberate data movement is a strategic differentiator

Across markets, a clear divide is emerging. Teams that treat data movement as an incidental consequence of integration struggle with rising complexity, unpredictable performance, and costly late-stage redesigns. Those who deliberately architect data movement gain sustained advantages.

Deliberate data movement architecture enables a host of benefits. Bottlenecks in latency, bandwidth, and power can be identified early; system architectures can be made easily repeatable across product generations; and architectural intent, software behavior and physical implementation can be correlated much more closely and reliably.

Additionally, it better enables teams to explore the tradeoffs between alternative floorplans and interconnect topologies (as well as logical & physical partitioning of multi-die products) well before physical constraints harden.

Achieving this at scale increasingly requires automation that is physically aware, yet architect controlled. Modern approaches synthesize interconnect structures directly from connectivity, traffic, and layout constraints, while allowing designers to intervene and iterate rapidly. The goal is not to hide complexity, but to make it tractable.

Equally important is the generation of consistent architectural, software, verification, and implementation views from a unified system description. This top-down correlation reduces mismatch between intent and realization, helping to minimize risk and accelerate time to market.

## The new battleground

As systems extend into the physical world, while architectures grow more complex to keep pace with expanding AI workloads the semiconductor industry is entering a new phase. Performance, power, safety, and scalability are no longer determined primarily by how fast data can be processed, but by how intelligently, efficiently, and predictably it can be moved.

Physical AI makes this reality impossible to ignore, but the lesson applies broadly, from data centers to embedded systems. The invisible highways inside chips have become the decisive terrain on which competitive advantage is won or lost. In this environment, data movement is no longer simple plumbing. It is the battleground where the next generation of semiconductor systems will succeed - or fail.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

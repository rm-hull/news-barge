---
title: Long-distance CXL could change how AI servers communicate
source_url: https://www.techradar.com/pro/meta-enlists-tiny-korean-startup-to-build-one-chip-like-datacenter-cxl-architecture-introduced-by-facebooks-parent-company-and-panmnesia-can-handle-almost-1000-ai-gpus-per-domain
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-14T04:48:31Z'
published: '2026-09-13T00:00:00Z'
description: Meta's new CXL design could cut cross-rack AI latency from microseconds
  to only several hundred nanoseconds
image: https://cdn.mos.cms.futurecdn.net/pVdxPdmrrXkVxR4MfZxiTV-1920-80.png
---

![Meta and Panmnesia chip](https://cdn.mos.cms.futurecdn.net/pVdxPdmrrXkVxR4MfZxiTV.png) 

- **Meta wants nearly 1,000 AI GPUs operating inside one coherent data center domain**
- **Panmnesia's CXL design connects CPUs, accelerators, and memory across multiple racks**
- **The architecture increases accelerator coordination from two devices to sixteen per CPU**

Meta is working with Panmnesia on an artificial intelligence data center design intended to make thousands of processors operate within one coherent environment.

The proposal uses Compute Express Link, or CXL, to connect CPUs, accelerators and memory across multiple racks without conventional network links.

The architecture could bring as many as 960 AI accelerators into one coherence domain, putting its capacity at almost 1,000 GPUs working as one system.

## CXL architecture extends accelerator connectivity

The design addresses a problem that becomes increasingly difficult as AI training systems combine hundreds or thousands of accelerators processing enormous data.

Every accelerator must progress through repeated computational stages, meaning one delayed component can force other devices to wait before continuing their work.

The researchers therefore focus on reducing unpredictable communication delays between racks, where Ethernet or InfiniBand networks normally handle connections beyond individual systems.

Those networks require packet processing and software coordination, which can introduce greater latency variation as workloads spread across additional servers.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

CXL instead provides a shared coherence mechanism, allowing processors, accelerators and memory to participate within one connected resource environment.

The proposed architecture adds dedicated hardware intended to keep communication paths and processing behaviour more consistent across the larger fabric.

Panmnesia's design uses a high-fan-out switch, a link acceleration unit and a fabric controller to manage traffic across the system.

These components are organized into trays, pods and a fabric, borrowing organizational principles normally associated with arranging functional blocks inside semiconductor chips.

The company says its fabric controller and link acceleration unit have completed silicon validation, while its switch has already been fabricated.

Its switch has also been fabricated, while pre-release silicon is reportedly being supplied as development continues toward commercial products.

## Up to 960 accelerators in one coherence domain

The review compares the proposed arrangement with NVIDIA's GB200 NVL72, where one CPU directly coordinates two accelerators through NVLink-C2C.

Under Panmnesia's architecture, one CPU could coordinate 16 accelerators, representing an eightfold increase over that reference configuration.

According to the published design, around 60 such groups could then form a coherence domain containing approximately 960 accelerators.

Cross-rack access could also fall from microsecond-level timing to several hundred nanoseconds, representing roughly an order-of-magnitude reduction.

The architecture would allow individual failed devices to be replaced without taking an entire server out of service.

That separation could reduce the amount of functioning hardware removed during failures, although actual operational benefits would depend on implementation.

During the announcement, Myoungsoo Jung, CEO of Panmnesia, said, “CXL enables the entire datacenter to operate as a single computing system.”

The architecture still faces physical limits because electrical CXL signalling reaches only about seven meters at 128 GT/s with two retimers.

Panmnesia therefore proposes optical CXL links for longer distances, and says it has already completed hardware proof-of-concept validation for that approach.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png) 

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: AMD opens up its new Lux supercomputer, powering everything from nuclear fusion
  to weather predictions
source_url: https://www.techradar.com/pro/amd-opens-up-its-new-lux-supercomputer-powering-everything-from-nuclear-fusion-to-weather-predictions
source_site: TechRadar UK
source_slug: techradar-uk
description: The first Genesis Mission supercomputer is live
image: https://cdn.mos.cms.futurecdn.net/MsYA6juw5nnzkw2YnMJYRJ-1920-80.jpg
published: '2026-11-20T00:00:00Z'
scraped_at: '2026-11-21T10:56:03Z'
categories:
- Technology & Software
- Science
people:
- Thomas Zacharia
locations:
- Tennessee Valley Authority
- US
organisations:
- AMD
- DOE
- Discovery
- EPYC CPUs
- El Capitan
- Frontier
- Genesis Mission
- HPE Juniper Networking QFX
- HPL
- Instinct MI355X GPUs
- Instinct MI430X GPUs
- Lux
- No. 14
- OLCF
- ORNL
- Oak Ridge
- Oak Ridge Leadership Computing Facility
- Oak Ridge National Laboratory
- SI
- TechRadar Pro
- Trump
- US Department of Energy
---

![AMD Lux supercomputer](https://cdn.mos.cms.futurecdn.net/MsYA6juw5nnzkw2YnMJYRJ-1920-80.jpg)

* **Lux, the HPE-built AI supercomputer with 4,000+ AMD MI355X GPUs at Oak Ridge, opens to scientific users**
* **It debuted at No. 14 on the TOP500 with 220.79 petaflops, about a sixth of Frontier, as it focuses primarily on low-precision AI math**
* **Half its 3.5 million annual node-hours go to Genesis Mission work such as fusion plant design and river forecasting; the rest are up for sale**

Lux, the AI-focused supercomputer AMD and the US Department of Energy agreed to build at Oak Ridge National Laboratory (ORNL) a little over a year ago, is now open to scientific users.

The system debuted at No. 14 on the November 2026 TOP500 list and is billed as the first dedicated "AI Factory" for the DOE's Genesis Mission.

ORNL's Oak Ridge Leadership Computing Facility (OLCF) operates the system, and AMD supplies nearly everything inside: EPYC CPUs, Instinct MI355X GPUs, Pensando networking, and the ROCm software stack, along with a share of the funding under what ORNL describes as a co-investment model.

## What's inside an AI machine with a supercomputer ranking?

HPE's announcement says Lux runs on direct liquid-cooled HPE ProLiant Compute XD685 servers, linked by HPE Juniper Networking QFX switches running 800G Ethernet.

Neither HPE nor AMD gives a GPU count, but the OLCF's Lux resource page fills in most of the gaps: more than 500 nodes, more than 4,000 MI355X GPUs with 288GB of HBM3E each, roughly 1.1PB of HBM across the system, over 24TB of local NVMe per node, and a 400G NIC per GPU. Users also get access to Orion, the Lustre file system with more than 600PB of capacity that was originally built alongside Frontier.

The same page lists peak figures of 40 exaflops at FP4, 20 exaflops at FP8 and 317 petaflops at FP64. That last number makes a useful cross-check. AMD rates each MI355X at 78.6 teraflops of FP64 on its product brochure, so dividing one figure by the other gives roughly 4,030 GPUs, or about 504 eight-GPU nodes. The FP8 and FP4 totals line up with the same count, so ORNL's spec table is consistent in its claimed performance based on AMD's own spec sheet.

On the High Performance Linpack (HPL) benchmark that decides the TOP500, Lux posted 220.79 petaflops. Set against ORNL's 317-petaflop FP64 peak, that works out to roughly 70% efficiency, a respectable figure when you consider that competitors on the November 2026 list, El Capitan and Frontier, convert about 64% and 66% of their theoretical peaks, respectively.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

AMD names three Genesis Mission projects allocated time on Lux. The fusion work is FADO, the Fusion Agentic Design Orchestrator, an agentic AI workflow meant to fold design simulation, robotics and maintenance planning into fusion pilot plant design. ORNL argues that reliability, availability, maintainability, and inspectability shape whether a first-of-a-kind plant can ever be economic, and that high-fidelity modeling has tended to leave them out.

The second is a foundation model factory for materials and advanced manufacturing, which produces custom models for problems such as designing the microstructures of 3D-printed alloys.

The third is a project centered on weather forecasting using an approach ORNL calls long-range water prediction: forecasting water availability, streamflow, and river temperature weeks to years ahead to support hydropower and thermoelectric plants in the Tennessee Valley Authority region.

All three sit under the Genesis Mission, the AI-for-science program the Trump administration launched by executive order in November 2025, which now spans a first-year cohort of 297 projects. That program also explains why AMD calls Lux an "SI + HPC" machine. The DOE has begun framing Genesis in terms of Super Intelligence (SI) for science, a label that describes an aspiration rather than anything Lux has yet demonstrated.

## Half for science, half for sale

Lux's business model may be its most unusual feature. The OLCF says the machine delivers 3.5 million node-hours a year. Half go to the Genesis Mission, and the other half are sold for proprietary use at the DOE user facility rate, with a minimum commitment of 175,000 node-hours per six months and projects running from six months to five years.

AMD will use part of that paid share for development and testing and plans to offer some of its reserved time to new partners. HPE contributed a $37 million in-kind investment, according to *StorageReview*.

That arrangement is how the DOE got a top-15 machine roughly a year after it was first announced as part of a $1 billion deal covering both Lux and its successor, Discovery. It also means a national lab system doubles as a commercial AI cloud, with its chip supplier as one of its tenants, a trade-off worth watching as Genesis Mission demand grows.

Lux was meant to arrive sooner. ORNL's launch announcement put deployment in early 2026, but AMD was still describing the system as under construction months later, and it only opened to users in mid-November. For a machine of this size, a slip of a few months is hardly unusual, but it's happening at a time when AI compute-related deals and their timelines are being scrutinized particularly heavily in the US by regulators, political entities, and investors alike.

One could argue that the upcoming Discovery supercomputer is the bigger prize here. It will pair AMD's EPYC "Venice" CPUs with Instinct MI430X GPUs on HPE's Cray GX5000 platform, with delivery expected in 2028.

AMD's Thomas Zacharia says Lux "shows what is possible when national laboratories, government and industry work together." On delivery, that holds up very well: a co-funded system built, ranked and opened in just over a year.

What it has not yet shown is science. The fusion, materials, and water projects are only now getting started, and the benchmark that will matter is whether they produce results that could not have come from Frontier next door, a machine that has already trained trillion-parameter models on its older AMD GPUs.

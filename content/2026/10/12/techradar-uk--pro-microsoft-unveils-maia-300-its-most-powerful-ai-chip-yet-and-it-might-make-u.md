---
title: Microsoft unveils Maia 300, its most powerful AI chip yet - and it might make
  using Teams, Copilot and Cowork much better at last
source_url: https://www.techradar.com/pro/microsoft-unveils-maia-300-its-most-powerful-ai-chip-yet-and-it-might-make-using-teams-copilot-and-cowork-much-better-at-last
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-12T18:59:10Z'
published: '2026-10-12T00:00:00Z'
description: More AI is coming to Microsoft services
image: https://cdn.mos.cms.futurecdn.net/8ydm6cbAA5GBz9y3joy9uH-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- GitHub
organisations:
- Cowork
- GPU
- GitHub Copilot
- HBM
- Microsoft AI
- Microsoft Foundry
- Microsoft Teams
- TSMC
- TechRadar Pro
---

![Microsoft Maia 300](https://cdn.mos.cms.futurecdn.net/8ydm6cbAA5GBz9y3joy9uH-1920-80.jpg)

* **Microsoft reveals Maia 300, its latest AI chip**
* **Designed for "inference-first", Maia 300 offers huge improvements in efficiency and power**
* **Maia 300 will begin deploying in 2027**

Microsoft has revealed Maia 300, the next generation of its Azure hardware as it prepares to scale up its in-house AI infrastructure to multi-gigawatt deployments.

The company says Maia 300, set to begin deployment in 2027, will deliver 40% more tokens per megawatt than other leading GPU-based system - designed primarily for inference, the new release targets long-context reasoning, responsive conversational AI and sustained, multi-step agent tasks.

Microsoft says a rack containing 96 Maia 300 accelerators will provide up to seven times the rack-scale token throughput of a Maia 200 rack.

## Inference-first

Interestingly Microsoft says it expects Maia 300 to help support a new generation of AI across its products and services, from agentic coding in GitHub to large-scale model serving through Microsoft Foundry.

But it also expects improved inference and data generation for its Microsoft AI team, and improvements in the likes of Copilot and Cowork, as well as individual products such as Microsoft Teams.

Designed with what Microsoft says is an "inference-first architecture", Maia 300 is built to improve performance by reducing data movement and making more efficient use of computing, memory and networking resources, Microsoft says, with its software-defined dataflow architecture, combined with AI-assisted kernel optimization, designed to keep data close to the parts of the system that need it.

![Maia 300](https://cdn.mos.cms.futurecdn.net/gn2pVK4F4zf9ZvW3ypaFod-1200-80.jpg)

Unsurprisingly, memory is central to the design, as Maia 300 will use a huge eight stacks of HBM4, with a claimed peak bandwidth of 18TB/s within a 950W thermal design power. Microsoft says specialized software can use on-chip SRAM as a scratchpad, easing pressure on HBM during demanding workloads.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The accelerator also introduces a multi-chiplet architecture that separates compute, memory-controller and input/output functions. Its compute chiplets will be built using TSMC’s N2P process. Microsoft says support for low-precision formats, including an enhanced MXFP4, will reduce memory and bandwidth demands, helping the system run larger context windows and increase throughput within the same power envelope.

Networking is designed to operate as part of the system’s dataflow rather than as a separate layer. Maia 300 will use high-bandwidth connections between accelerators for tensor parallelism, alongside a custom AI transport based on Ethernet infrastructure. Microsoft says this approach can scale from a single rack to data-center deployments.

A Maia 300 rack will contain 96 accelerators within a 167kW power envelope, with 27.6TB of HBM capacity and 1.7 petabytes per second of aggregate HBM bandwidth. Microsoft says that density will let it serve more simultaneous AI interactions and larger workloads from each rack.

The launch builds on Maia 200, which Microsoft says is already running production workloads including Microsoft 365 Copilot and models developed by its Microsoft AI team.

The company says Maia 200 delivers up to 1.7 times more tokens per watt than leading GPU infrastructure for built-in AI features in Teams, Copilot and Cowork. GitHub Copilot and Microsoft Foundry are expected to follow by the end of this year.

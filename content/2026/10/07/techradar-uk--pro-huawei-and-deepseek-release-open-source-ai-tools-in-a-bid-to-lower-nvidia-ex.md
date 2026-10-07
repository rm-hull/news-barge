---
title: Huawei and DeepSeek release open source AI tools in a bid to lower Nvidia exposure
  — but will programmers make the switch?
source_url: https://www.techradar.com/pro/huawei-and-deepseek-release-open-source-ai-tools-in-a-bid-to-lower-nvidia-exposure-but-will-programmers-make-the-switch
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-07T20:36:17Z'
published: '2026-10-07T00:00:00Z'
description: DeepSeek just open sourced its Ascend kernel stack
image: https://cdn.mos.cms.futurecdn.net/FMwRmCw7wxB7F6AQgqzqnX-1920-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Bloomberg
locations:
- China
- US
organisations:
- Baidu
- Bloomberg
- CANN
- CUDA
- ChinaTalk
- DeepEP-Ascend
- DeepGEMM-Ascend
- DeepSeek
- Epoch AI
- Financial Times
- FourWeekMBA
- GitHub
- Huawei Ascend
- Nvidia
- Reuters
- TechRadar Pro
- Tencent
- TileLang
---

![DeepSeek](https://cdn.mos.cms.futurecdn.net/FMwRmCw7wxB7F6AQgqzqnX-1920-80.jpg)

* **DeepSeek open sourced Ascend ports of its production kernel and communication libraries with Huawei's support in tow**
* **Published benchmarks ran on a proof-of-concept hardware kit DeepSeek says is not a publicly distributed release**
* **Two repositories are genuinely new and have received hundreds of GitHub stars versus Nvidia's thousands; the other announced components are updates to existing tools**

DeepSeek has revealed it is open sourcing a set of infrastructure components for Huawei's Ascend accelerators.

DeepSeek published two completely new repositories, DeepGEMM-Ascend for matrix multiplication and DeepEP-Ascend for the all-to-all communication that mixture-of-experts models depend on.

The other components named in the announcement were upgrades: TileKernels, DeepSelect, and FlashMLA are existing projects that received Ascend-targeted updates, a distinction FourWeekMBA established from the GitHub creation dates.

## An open source offering with limited use cases?

*Reuters* framed it as two Chinese firms deepening ties in search of an alternative to Nvidia, with*Bloomberg* called the centerpiece a programming language named TileLang, China's answer to CUDA.

The question is whether any of this matters when engineers are still on the fence about using these tools and access to Chinese compute remains, at best, elusive.

The biggest piece, as Bloomberg puts it, TileLang itself is neither new nor DeepSeek's own offering. It was open-sourced in January 2025, and its Huawei Ascend adapters were published in an external repository, tilelang-ascend, on September 29, 2025, a full year before the recent announcement.

While TileLang supports Nvidia's CUDA backend, it also supports Huawei's Ascend as an ecosystem backend, classified and maintained in a separate repository. One could therefore argue that TileLang is less a weapon aimed at Nvidia than a shared abstraction layer that half a dozen Chinese accelerator vendors are quietly standardizing on, with Huawei as the largest of several tenants rather than the landlord.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The new software has limitations: DeepGEMM-Ascend requires the Ascend 950 series and CANN 9.20. DeepEP-Ascend requires Ascend 950 silicon with UBMEM connectivity, so it targets a narrow audience beyond Huawei's own engineers and limited Chinese AI labs with access to that silicon.

Despite this, at a time when Nvidia chips are unlikely to be generously exported by the US or allowed in by China, Huawei's Ascend silicon has a large task on its shoulders: DeepGEMM-Ascend keeps the same Python package name and API shape as its CUDA sibling, and DeepEP-Ascend aligns its public buffer interfaces with the Nvidia version.

That is because the goal isn't a performance claim, but switching-cost reduction, and switching costs are precisely what Nvidia's moat is made of: it costs far too much for most developers to abandon CUDA or code their own alternative currently.

Public signals show this remains an uphill task; at the time of writing, DeepGEMM-Ascend has 515 stars and 39 forks, compared with DeepGEMM, which has a comfortable lead at 8,522 stars and 1,359 forks, for example. The story is similar for DeepEP-Ascend and DeepEP, with the latter surpassing 10,200 stars versus DeepEP-Ascend's 224.

The reputational problem Huawei faces here predates the repositories. ChinaTalk, citing the *Financial Times*, quotes a Huawei researcher describing CANN as making Ascend chips difficult and unstable to use, and a Chinese developer characterizing work on the 910B as a road full of pitfalls.

Epoch AI has reported that Huawei dispatches engineering teams to major customers such as Baidu and Tencent to help port CUDA training code and keep deployments running.

A frontier lab publishing its own production kernels partially answers that complaint, because it replaces vendor documentation with code that has survived contact with a model and can be optimized further. It is also, however, code that runs on one chip family, under one toolkit version, on firmware the rest of the world cannot download or even potentially access.

---
title: DeepSeek and Huawei release open-source Ascend AI programming tools to reduce
  reliance on Nvidia CUDA ecosystem — tools include compute and communication libraries,
  as well as Ascend support for TileLang
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseek-and-huawei-release-open-source-ascend-ai-programming-tools-to-reduce-reliance-on-nvidia-ecosystem-tools-include-compute-and-communication-libraries-as-well-as-ascend-support-for-tilelang
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-01T20:25:56Z'
published: '2026-10-01T00:00:00Z'
description: The tools build on Huawei's existing CANN software platform.
image: https://cdn.mos.cms.futurecdn.net/XshNMmxdYaq78TYvcLQQRL-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Etiido Uko
- Tom
locations: []
organisations:
- Ascend AI
- CANN
- CUDA
- Chinese AI
- DeepEP-Ascend
- DeepGEMM-Ascend
- DeepSeek
- Etiido Uko
- Google News
- Huawei
- Nvidia
- PC
- Reuters
- TileLang
- Tom's Hardware
---

![Deepseek logo](https://cdn.mos.cms.futurecdn.net/XshNMmxdYaq78TYvcLQQRL-1920-80.jpg)

Chinese AI company DeepSeek has released open-source programming tools developed in partnership with Huawei, for the company's Ascend AI chips, as part of efforts to reduce reliance on Nvidia's software and hardware ecosystem. According to a September 30 Reuters report, the release includes open-source libraries for AI computation and chip-to-chip communication, as well as Ascend support for the high-level programming language TileLang.

DeepSeek says the tools — for which Huawei provided full support during development — are intended to simplify programming while enabling developers to fully leverage the hardware's performance. The two companies also worked together to optimize computation and communication on a supernode system built around 128 Ascend 950 chips. The work addresses two requirements for running large AI workloads across multiple accelerators: performing calculations efficiently on each chip and moving data quickly enough between them to keep the processors occupied.

The released libraries include DeepGEMM-Ascend, which handles matrix multiplication and other calculations used in DeepSeek's models. It supports BF16, FP8, and FP4 operations and uses the same programming interfaces as DeepSeek's existing DeepGEMM library, allowing developers to retain familiar APIs when moving to Ascend. Meanwhile, DeepEP-Ascend handles communication for training and inference, including routing data to the different experts in mixture-of-experts models and combining their outputs. Both libraries were developed and tested on Ascend 950 hardware.

TileLang provides the higher-level programming layer for writing optimized kernels. DeepSeek described it as offering “a simpler programming model” than Nvidia's CUDA, with the aim of improving development efficiency and simplifying code. The language already supported Nvidia and other hardware, with earlier adapters available for Huawei's Ascend processors. The September 30 update adds native support for Ascend 950, including code generation, automatic scheduling, and synchronization.

The tools build on Huawei's existing CANN software platform, which provides the underlying infrastructure for running AI workloads on Ascend. Nvidia's CUDA platform has long supplied developers with a mature programming environment and libraries optimized for its GPUs, making the software ecosystem a major part of the company's advantage in AI computing. While DeepSeek's release provides developers with additional tools to optimize workloads on Huawei hardware, TileLang's support for multiple platforms ensures the language remains useful for Nvidia GPUs.

The announcement comes two weeks after Huawei unveiled its next generation of AI processors and supernode systems. Huawei said it expected its AI systems to be widely used for model training in 2027. The companies had already collaborated on DeepSeek's V4 model, released in preview form in April, with support for Huawei's Ascend chips. Huawei said its Ascend 950 supernodes fully supported the V4 models and that its chips had been used for part of the lighter V4-Flash model's training.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD-140-80.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.

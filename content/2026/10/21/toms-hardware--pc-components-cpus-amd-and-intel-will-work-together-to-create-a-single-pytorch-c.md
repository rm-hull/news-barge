---
title: AMD and Intel will work together to create a single PyTorch code path for AI
  inference on CPUs — x86 rivals fold AMD ZenDNN library into Intel oneDNN to make
  CPU AI simpler
source_url: https://www.tomshardware.com/pc-components/cpus/amd-and-intel-will-work-together-to-create-a-single-pytorch-code-path-for-ai-inference-on-cpus-amd-zendnn-library-gets-folded-into-intel-onednn-to-make-cpu-ai-simpler
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-21T17:12:03Z'
published: '2026-10-21T00:00:00Z'
description: AMD has also joined the UXL Foundation as a steering member.
image: https://cdn.mos.cms.futurecdn.net/rYe5kJq2zmKffyrHqBDYkE-2560-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Jake Roach
- Tom
locations:
- Mount Pleasant
- Wisconsin
organisations:
- ACE
- AMD
- Arm
- EAG
- Google Cloud
- Google News
- Intel
- Microsoft
- PyTorch
- Qualcomm
- Tom’s Hardware
- UXL Foundation
- ZenDNN
- oneDNN
- x86 Ecosystem Advisory Group
---

![AMD at Advancing AI.](https://cdn.mos.cms.futurecdn.net/rYe5kJq2zmKffyrHqBDYkE-1920-80.jpg)

Intel and AMD are integrating their CPU optimizations for PyTorch into a unified library, offering tuning for both AMD and Intel chips through the oneDNN library. AMD has maintained a downstream version of oneDNN called ZenDNN, which is now moving into the open-source oneDNN, published by the UXL Foundation and driven by Intel. AMD also announced it's joining the UXL Foundation as a "steering member," which "influences the future of the UXL Foundation" in exchange for a contribution of $20,000 per year.

![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7-1200-80.jpg)

AMD says the move to unify these efforts under oneDNN was recommended by the x86 Ecosystem Advisory Group (EAG), which is a joint initiative that primarily exists between Intel and AMD and was established in 2024. The two companies have collaborated through the EAG previously, such as with the ACE extensions for x86 that we learned about earlier this year.

The oneDNN backend is used for CPU inference, and it's built to accelerate that workload for the latest Intel (and now AMD) chips in frameworks like PyTorch. When oneDNN was added to PyTorch as a backend in late 2023, it showed a 1.24x improvement with the Float32 data type, and 2.21x for the BFloat16 data type.

From the oneDNN GitHub, the library "detects hardware features at runtime" to generate optimized kernels for the platform, as well as provides low-precision data types. It also features optimized instructions for common AI and machine learning operations, such as matrix multiplication and convolution.

For developers, the move simplifies working with PyTorch across different systems, ensuring a single backend provides the proper optimizations for whatever hardware you're running. Although the news here is focused on the x86 guard, oneDNN is a cross-platform library that works on Arm and RISC-V architectures as well.

Intel originally developed oneDNN, built on top of previously deep learning libraries, before it was folded into the UXL Foundation. Intel was among the founding members of the UXL Foundation, alongside Arm, Qualcomm, Google Cloud, and others.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi-140-80.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

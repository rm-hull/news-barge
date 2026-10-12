---
title: Intel's Crescent Island AI accelerator officially powers new GPU D-Series products
  — chip delivers 1.3 peak PFLOPS of FP8 compute and 1.5 TB/s of memory bandwidth
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/intels-crescent-island-ai-accelerator-officially-powers-new-gpu-d-series-products-chip-delivers-1-3-peak-pflops-of-fp8-compute-and-1-5-tb-s-of-memory-bandwidth
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-12T21:16:45Z'
published: '2026-10-12T00:00:00Z'
description: Crescent Island gets official performance and bandwidth specs at OCP
  2026.
image: https://cdn.mos.cms.futurecdn.net/rhHcYjk8r2a28j68LDnQ88-1920-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Jeff Kampman
- Jeffrey Kampman
- Rubin
- Tom
locations:
- Crescent Island
organisations:
- Data Center GPU Max
- Get Tom's Hardware
- Google News
- Intel GPU
- Nvidia
- Ponte Vecchio
- Tom's Hardware
- Xe
---

![Intel GPU D-Series](https://cdn.mos.cms.futurecdn.net/rhHcYjk8r2a28j68LDnQ88-1920-80.jpg)

At OCP 2026 today, Intel has given Crescent Island a proper name: the Intel GPU D-Series. For the first time, the company also shared a theoretical peak performance target for the chip: 1.3 PFLOPS of FP8. It also disclosed the final memory bandwidth to expect from these AI inference accelerators: 1.5 TB/s. This new information adds to the slow drip of disclosures Intel has made about Crescent Island throughout 2026.

We already knew that Crescent Island is the first chip to be built on Intel's Xe3P graphics architecture (or massively parallel computing architecture, really, as the chip lacks most or all of the graphics-specific functional units that would characterize a true GPU). Intel will release GPU D-Series products in an air-cooled PCIe form factor with a TDP of 350W and up to 480GB of LPDDR5X memory.

For reference, each of the 72 Rubin GPUs in Nvidia's Vera Rubin NVL72 rack-scale system can push a theoretical 17.5 PFLOPS of FP8 throughput, but each of those chips requires liquid cooling and likely has a TGP measured in kilowatts. In any event, it should be clear that the GPU D-Series is targeting an entirely different performance envelope and infrastructure requirements than Rubin.

Intel GPU D-Series products, in contrast, are meant to be deployed in traditional air-cooled rack servers scaling up to eight GPUs, like Nvidia's HGX systems. In such a configuration, Intel says that GPU D-Series chips could power inference on models spanning more than one trillion parameters. Intel also highlights the chip’s suitability for “large language models, long-context inference, and concurrent inference services," creating a foundation for "multi-tenant AI services, robotics, and other latency-sensitive workloads."

In order for that kind of distributed inference deployment to work, in which multiple GPUs will presumably act as one, Intel will also need a robust software stack. The company is highlighting the “common Xe software foundation” it’s already built for AI across its Xe Cores in iGPUs and discrete GPU products.

To bring Xe accelerators into the data center, Intel says it’s working with “a broad ecosystem of OEMs, ODMs, neoclouds, independent software vendors, appliance providers, and AI-native companies.” To that end, Intel says customer sampling of GPU D-Series products is in progress, although it didn’t provide any details of a broad launch.

It’ll remain to be seen whether the Intel GPU D-Series is the product that finally gives Intel an AI accelerator toehold after the failure of the Data Center GPU Max family (code-named Ponte Vecchio) and its mothballed follow-ons, as well as a series of silicon acquisitions that failed to coalesce into a coherent AI strategy.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

But in a world that’s hungry for every compute cycle for inference, a product with a proven architectural shape that’s targeted specifically at that workload in an accessible thermal and electrical envelope might be just the recipe Intel needs to start getting traction as AI models keep advancing in intelligence and agentic workflows assume ever-greater importance in the computing vision of the future.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jeffrey Kampman](https://cdn.mos.cms.futurecdn.net/8JCjGs5yVZds2YdKmzjUDE-140-80.jpg)

As the Senior Analyst, Graphics at Tom's Hardware, Jeff Kampman covers everything that has to do with graphics cards, gaming performance, and more. From integrated graphics processors to discrete graphics cards to the hyperscale installations powering our AI future, if it's got a GPU in it, Jeff is on it.

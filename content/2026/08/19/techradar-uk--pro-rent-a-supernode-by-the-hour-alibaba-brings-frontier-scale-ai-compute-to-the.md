---
title: Rent a supernode by the hour - Alibaba brings frontier-scale AI compute to
  the public cloud, but only if you live in this remote Chinese province
source_url: https://www.techradar.com/pro/rent-a-supernode-by-the-hour-alibaba-brings-frontier-scale-ai-compute-to-the-public-cloud-in-china
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-19T01:49:41Z'
published: '2026-08-19T00:00:00Z'
description: A homegrown AI supernode for hire, for domestic users only, for now
image: https://cdn.mos.cms.futurecdn.net/zwBWPNAfpJdnNkfJY3wUKM-2560-80.jpg
---

![A data center in a blue light](https://cdn.mos.cms.futurecdn.net/zwBWPNAfpJdnNkfJY3wUKM.jpg) 

- **Alibaba Cloud's Lingjun Zhenwu M890 supernode instance is now on commercial sale**
- **It offers rentable 64-card computing units built entirely on in-house silicon**
- **It marks the first time Alibaba has directly sold supernode compute through the public cloud, however availability is limited to the Ulanqab region in Inner Mongolia**

Alibaba Cloud has begun commercial sales of its Lingjun Zhenwu M890 supernode instance, letting customers rent a 64-card, high-speed interconnected computing unit without building their own data center.

The launch makes it the only Chinese-origin supernode that users can effectively use online without entering a purchase agreement or using a preconfigured AI model instance, an impressive enterprise-centric addition.

There is a caveat for enthusiasts looking to test it outside China: it is currently limited to users in North China's Inner Mongolia Autonomous Region only.

## What is Alibaba offering to enterprise consumers?

A supernode is a set of accelerators wired together tightly enough that software treats them as one very large chip rather than a network of separate ones. This approach is often necessary; a model too big to fit on a single card would otherwise have to shovel data across comparatively slow networking, and that overhead can determine whether trillion-parameter models are practical to serve.

One of the best examples is Nvidia's GB200 NVL72, which leverages 72 of its Blackwell GPUs in a single configuration, or AMD's 72-GPU Helios configuration, which offers its own Instinct MI455X GPUs with more memory per GPU in tow.

Alibaba's offering is not faster than either example, and both are among the fastest options available to consumers worldwide, but it offers a mix of advantages to domestic Chinese consumers that would not otherwise be in play: Chinese Silicon, a Chinese cloud, and lower latency.

## A domestic supernode built around a mixture of state restrictions and sanctions

As Beijing restricts Chinese cloud providers from accessing the latest Nvidia and AMD chips they can buy in a tit-for-tat move for the White House's increasing heavy-handedness, the best options for enterprise customers and AI startups have become increasingly domestic, and Alibaba Cloud's homegrown silicon is a key example of how that policy has shaped its offerings.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The underlying Zhenwu M890 processor debuted at the Alibaba Cloud Summit in May 2026, where the company also disclosed a detailed chip roadmap through 2028. comes from T-Head, the group's chip design unit, and carries 144GB of HBM memory with inter-chip bandwidth up to 800 GB/s. The interconnect fabric uses an in-house ICNSwitch 1.0 chip, which lifts the scale-up domain from 16 cards on the previous-generation Zhenwu 810E to 64, with bandwidth up from 700 GB/s.

The company says that the configuration is, on paper, capable of handling a Mixture of Experts (MoE) AI configuration of up to 10 trillion parameters, while emphasizing that this is the first supernode-form architecture in China to successfully run large language models exceeding 2 trillion parameters; Alibaba says the current instance is already powering commercial services for Kimi K3 and Qwen3.8-Max.

Alibaba's roadmap continues past the M890. T-Head has said the Zhenwu V900 arrives in the third quarter of 2027 with three times the M890's performance, 216GB of memory, and 1,200 GB/s of inter-chip bandwidth, followed by the Zhenwu J900 in the third quarter of 2028.

There is no public pricing for the instance, and information on its power consumption is nonexistent; benchmarks comparing it to mainstream options are scant at best. Despite the limited information and geographic limits, the move underscores both China's growing self-reliance in the AI industry and its ambitions, which could see the supernode offered to a wider range of consumers, both domestic and international, in the near future.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: '''It''s a beast, but not at everything'' — RTX Spark-powered Microsoft Surface
  Laptop Ultra lives up to expectations, but you need to be a big fan of local AI'
source_url: https://www.techradar.com/pro/its-a-beast-but-not-at-everything-rtx-spark-powered-microsoft-surface-laptop-ultra-lives-up-to-expectations-but-you-need-to-be-a-big-fan-of-local-ai
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-20T08:30:12Z'
published: '2026-10-20T00:00:00Z'
description: Is the Surface Laptop Ultra price tag justified? This depends on what
  you need
image: https://cdn.mos.cms.futurecdn.net/vsSgqJ4vKjLh2Rtb79f7rN-2160-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Zac Bowden
locations: []
organisations:
- AMD
- Apple
- Blackwell GPU
- Hermes Agent
- Intel
- LLVM
- Microsoft
- N1X
- NVIDIA
- Nvidia
- RTX Spark
- Surface Laptop Ultra
- TechRadar Pro
- Tom's Hardware
---

![Microsoft Surface Laptop Ultra laptop open, being held by a person in very shadowed lighting](https://cdn.mos.cms.futurecdn.net/vsSgqJ4vKjLh2Rtb79f7rN-1920-80.jpg)

Nvidia's RTX Spark laptops hit the shelves last week, led by Microsoft's Surface Laptop Ultra, and the chip supports up to 128GB of memory.

This laptop starts at $2,599.99, but does its performance justify the price tag?

I took a look at some of the earliest in-depth reviews of the Microsoft Surface Laptop Ultra to ascertain what this device offers and whether it is worth every penny.

## What reviews say

The prowess of the RTX Spark laptop was acknowledged, but all the reviews agreed on one thing: it’s not foolproof and has some downsides.

“It's a beast, but not at everything,” said Zac Bowden of *Windows Central**,* while*Tom's Guide* went further, calling it “not a MacBook Pro killer but something much weirder and wildly powerful.”

The praise is concentrated in one area: local AI models. Every outlet that tested them put the Surface ahead of Apple's M5 Max and AMD's Ryzen AI Max+ 395, the most powerful mobile chips for laptops.

Its gaming performance, however, did not exactly get much praise – while some said it is just okay, others think it’s a weak spot.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Price

> Most people would be better served getting an Intel or AMD laptop with a dedicated NVIDIA GPU instead, as these often cost less than the cheapest RTX Spark laptops right now

Cost is the sticking point for RTX Spark. Microsoft's Surface Laptop Ultra starts at $2,599.99 for the 18-core model with 24GB of memory and 512GB of storage.

The 20-core, 128GB, 1TB configuration tops out at $5,899.99, and the lead times on this model already stretch to late December.

The jump is steepest where the platform is strongest. The 64GB to 96GB of GPU-accessible memory that lets 35B-parameter models run well only comes with the 128GB build, and a 32GB or 48GB Surface won't fit the same models.

*Tom’s Hardware* warns that “sky-high DRAM and NAND price hikes” will be a headwind for the platform in the near term. That is a lot to spend, and you need a local AI workload to justify it.

The biggest challenge is the “eye-watering price tags,” since that money still buys “a lot” of cloud tokens from OpenAI and Anthropic, as *Tom's Hardware* puts it.

As *Windows Central* notes, comparable devices offer just enough and cost less.

## CPU

> The RTX Spark...is the strongest multi-threaded CPU we have ever seen in a notebook

Multi-core speed is the strength, and single-core speed is the weakness.

The 20-core N1X pairs 10 performance cores with 10 efficiency cores, targeting heavy multi-threaded work.

In single-core tests, it was found to “edge” the Dell Pro Precision 5 16S, scoring 558.5 against 534.8 in Cinebench 2026.

But across the wider suite, single-thread results, *StorageReview* says it “sit 15 to 30 percent behind the x64 field,” which is “just okay.”

Moving to multi-core, the Surface is an absolute "beast", finishing “34 percent ahead of the Razer Blade 16.”

Compared with Apple, however, it “simply doesn’t compete with Apple’s latest Max chips,” consistently trailing the M4 Max and M3 Ultra.

Under a heavy all-core CPU workload (an OpenBLAS double-precision solve), this device lost power repeatedly, though most buyers will never run anything like it.

On real-world work, it “won nearly every multi-threaded CPU test,” compiling LLVM in 206 seconds against 327 for the next-fastest system.

But there are weak spots: its Arm64 SVT-AV1 encoding managed about “a fifth” of what the x64 systems produced, and memory latency of 251 ns was the “worst in the group.”

That’s not to say it’s slow. Day-to-day use “feels fine,” and even emulated apps feel native. But for single-threaded, browser-bound work, “the x64 field is likely the better buy.”

|  |  |  |
| --- | --- | --- |
| RTX Spark 20-core CPU benchmark results |  |  |
| **Outlet**|** Benchmark**|** Score** |
| *Windows Central* | Cinebench 2026 (Multi-Core) | 6,885 |
| *StorageReview* | Cinebench 2026 (Multi-Core) | 6,963 |
| *Windows Central* | Cinebench 2026 (Single-Core) | 558 |
| *StorageReview* | Cinebench 2026 (Single-Core) | 558.5 |
| *Windows Central* | Geekbench 7.1 (Multi-Core) | 23,571 |

## GPU

The 6,144-core Blackwell GPU is the real engine of the chip, with 5th-generation Tensor Cores built for AI workloads and up to 96GB of memory to draw on.

In local AI tests, it was “the fastest overall” at agentic tasks, finishing about 25% quicker than the M5 Max MacBook Pro.

In Stable Diffusion 1.5 INT8, it scored 11,294 and “substantially outperformed” the RTX 5080, 5070 Ti and 5060.

However, for models that fit in 24GB, the Razer Blade 16’s RTX 5090 generates tokens “2.3x faster,” and video rendering trails even the RTX 5060.

Gaming is a secondary strength. Performance is “similar to an RTX 4070 or 5060,” and Cyberpunk 2077 held 60fps at 1440p with frame generation.

But shared memory bandwidth and input latency are limited. Its shared memory bandwidth hit 300GB/s, below the 384GB/s on a mobile RTX 5060.

Gears of War: E-Day averaged 77.7 fps with 1% lows of 39.9 fps and 83.5 ms of latency. Control Resonant reached 109.2 fps, but only with 3X frame generation.

If AI is not your thing and you need low latency and top performance, “a separate gaming laptop with a dedicated RTX 50-series GPU will still provide a superior experience.”

## AI

> The RTX Spark is one of the better choices in the Windows space right now

Nothing else in a laptop gives a GPU this much room to work with. The RTX Spark pairs its Blackwell GPU with up to 128GB of unified memory, and 64GB of it, adjustable up to 96GB, can go straight to the GPU.

That is “more than any NVIDIA laptop GPU before it,” and it is what lets 35B-parameter models run at up to 89 tokens per second. Models up to 120B parameters can fit entirely on the GPU.

In agentic tests it was “the fastest overall,” finishing about 25% quicker than the M5 Max MacBook Pro and in roughly half the time of the Ryzen AI Max+ 395.

Quantized models are where it truly leads, with Stable Diffusion 1.5 INT8 scoring 11,294 and “substantially outperforming” the RTX 5080, 5070 Ti and 5060.

It also makes local agents practical. Hermes Agent organized a cluttered downloads folder and built a website without sending any data to the cloud, so “you are no longer constrained by usage limits.”

That’s not to say it beats everything. For models that fit in 24GB, the Razer Blade 16’s RTX 5090 generates tokens “2.3x faster.”

Still, for those running models locally all day, it is “king”.

This, then, is a machine for the local AI believer, built for privacy, offline use and tinkering.

## Who should buy it

Nvidia has built a compelling workstation for certain AI workloads, although conventional laptop buyers have several reasons to remain cautious.

Developers and analysts running 20B to 35B models locally are the clear audience.

Gamers, browser-heavy users, and anyone whose models fit in 24GB are better served by a laptop with a dedicated GPU.

## Verdict

**The good**

· Strong multi-threaded CPU

· Up to 96GB of GPU memory runs 35B models at up to 89 tokens per second

· Fastest in agentic AI tests

**The bad**

· Expensive, from $2,599.99 to $5,899.99

· Weak single-thread speed and high memory latency

· Gaming is only decent, with high input latency

**The verdict**

Grab it if local models above 24GB are your daily work. Opt for a dedicated-GPU laptop for everything else. Avoid it if gaming is your focus.

|  |  |  |
| --- | --- | --- |
| NVIDIA RTX Spark N1X specs |  |  |
|  | **18-core version**|** 20-core version** |
| **CPU** | 9x Cortex-X925 + 9x Cortex-A725 | 10x Cortex-X925 + 10x Cortex-A725 |
| **GPU** | 5,120 CUDA cores | 6,144 CUDA cores |
| **Memory** | LPDDR5X, up to 64GB | LPDDR5X, up to 128GB |
| **Memory speed** | 9,400MT/s | 9,400MT/s |
| **Bandwidth** | Up to 300GB/s | Up to 300GB/s |
| **Laptop TDP** | 45W to 80W | 45W to 80W |
| **Process** | TSMC 3nm | TSMC 3nm |

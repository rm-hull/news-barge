---
title: Tiny's new AI workstation is anything but — packing in 16 TB SSD array and
  128 GB GPU memory, but with an eye-watering price tag to boot
source_url: https://www.techradar.com/pro/tinys-new-ai-workstation-is-anything-but-packing-in-16-tb-ssd-array-and-128-gb-gpu-memory-but-with-an-eye-watering-price-tag-to-boot
source_site: TechRadar UK
source_slug: techradar-uk
description: Tiny Corp's new $30,000 tinybox swaps DRAM for sixteen SSDs
image: https://cdn.mos.cms.futurecdn.net/UXUoBz2xYzpVLMMrg7S6Te-1920-80.jpg
published: '2026-11-05T00:00:00Z'
scraped_at: '2026-11-05T06:36:14Z'
categories:
- Technology & Software
people:
- Kimi K3
locations:
- BaM
organisations:
- AMD GPUs
- Apple
- CPU
- DGX Station
- Hyperstack
- Kimi K3
- M5 Ultra
- MXFP4
- Macworld
- Moonshot AI
- Nvidia
- Red Kimi
- Red Kimi's
- TechRadar Pro
- Threadripper Halo Station
- Tiny Corp
- Tiny's
- University of Illinois
---

![The Tinybox workstation pictured](https://cdn.mos.cms.futurecdn.net/UXUoBz2xYzpVLMMrg7S6Te-1920-80.jpg)

* **Tiny Corp's $30,000 tinybox Red Kimi pairs four Radeon AI Pro R9700 GPUs (128 GB GDDR6) with sixteen 1 TB NVMe SSDs**
* **A tinygrad driver lets the GPUs read the 238.4 GB/s SSD array directly to run Moonshot's 2.8-trillion-parameter Kimi K3**
* **Tiny claims 40 tokens per second, but the math involves caching nearly all of each token's weights in VRAM**

There is nothing tiny about Tiny Corp's latest tinybox, the tinybox Red Kimi: It costs a mammoth $30,000 and pairs four AMD Radeon AI Pro R9700 graphics cards with sixteen 1 TB NVMe SSDs, all with one goal in mind: running Moonshot AI's 2.8-trillion-parameter Kimi K3 on a desk rather than in a data center.

Each R9700 carries 32 GB of GDDR6 at 640 GB/s, giving the four cards 128 GB of GPU memory and 2,560 GB/s of aggregate bandwidth to go with a system built on Tiny Corp's G5 platform, with a 32-core AMD Epyc Genoa processor whose exact model the tinybox configurator doesn't name, and a modest 32 GB of DDR5 system memory in tow.

Tiny Corp claims the machine can run Kimi K3 at 40 tokens per second, a figure nobody outside the company has tested yet.

## Sixteen drives, four GPUs and an AMD EPYC CPU rule the roost

The storage in play is the unique selling point for Tiny Corp's behemoth: its 16 drives form a RAID array rated at 238.4 GB/s, and Tiny Corp says its tinygrad software now includes a driver that lets the AMD GPUs control the NVMe drives directly, rather than routing every read through the CPU.

Sharing the system's topology on X, the company pitched the result as "frontier models at home at usable speeds for a good price."

The rationale comes down to capacity. Moonshot's model card shows Kimi K3 ships with native MXFP4 weights, and Hyperstack measured the published checkpoint at roughly 1.56 TB. The four GPUs can hold about 8% of that, so the rest has to live somewhere, and Tiny Corp has picked considerably cheaper flash over DRAM.

The concept isn't entirely new: Researchers from Nvidia and the University of Illinois presented GPU-initiated SSD access in the BaM system architecture at ASPLOS 2023, treating storage as another tier of accelerator memory. Tiny Corp's offering, however, is a working version on AMD workstation cards, inside a box you can actually order.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The configurator's own code estimates the Red Kimi's installed weight at around 56 pounds, in a chassis 12 inches wide, 19.25 inches tall, and 18 inches deep. It also raises the noise rating from under 50 dB to under 60 dB for R9700 builds, warning that the cards' blower fans are "audible".

Kimi K3 is a mixture-of-experts model that activates 16 of its 896 routed experts, plus two shared experts, for 104 billion active parameters per token. At MXFP4's effective 4.25 bits per weight, that means reading at least 55 GB of weights for every token generated.

If every one of those bytes were read from the SSDs, the array would manage only about four tokens per second. Reaching 40 tokens per second means moving roughly 2.2 TB/s of weights, about 86% of the four GPUs' combined memory bandwidth, while the SSDs could contribute at most about 6 GB per token, or around 11% of what each one needs.

In a nutshell, the claim only works if the GPUs' 128 GB already contains nearly everything each token touches, even though it fits less than a tenth of the model. That is achievable if expert selection is predictable enough to cache well, or if Tiny Corp is running a lower-precision quantization than Moonshot's native format, speculative decoding, or a mix of the three.

Tiny Corp hasn't published the precision, context length, batch size, or method behind its number, and it would be prudent to treat it as a manufacturer claim at best. The aggregate bandwidth figure also assumes the workload is split evenly across four cards that communicate over PCIe.

## A pricey proposition that goes neck and neck with Apple's Mac Studio

At $30,000, the Red Kimi is a lot of money for a desktop computer, but the alternatives for running a 2.8-trillion-parameter model locally aren't cheaper. Apple's Mac Studio with M5 Ultra and 512 GB of unified memory starts at $22,299 and reaches $29,799 with a 16 TB SSD, Macworld reports, just $201 shy of Tiny's box. It offers four times the fast memory at 1.2 TB/s, according to Apple, but 512 GB still can't hold K3's native checkpoint.

Nvidia's GB300-based DGX Station went on sale for almost $91,100 with 748 GB of memory, which also falls short. AMD's Threadripper Halo Station, with up to 2.6 TB of combined memory, would fit the model comfortably, but it isn't due until 2027, and industry estimates put a full system at around $150,000.

Against such prolific (and pricey) competition, the Red Kimi is the cheapest way to maintain Kimi K3's native precision on a single desk. The catch is that it gets there by asking flash to do the job of memory, and every token per second it delivers depends on how well that bet pays off. Until someone outside Tiny Corp runs the numbers, "usable speeds" is a promise rather than a result.

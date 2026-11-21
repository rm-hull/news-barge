---
title: Homelabber’s second-gen Optane build uses two RTX 3090s to run 2.8-trillion-parameter
  Kimi AI model at 3.11 tokens per second — moving nearly half the model into a RAM
  drive boosted performance by 41%
source_url: https://www.tomshardware.com/uk/tech-industry/artificial-intelligence/homelabbers-second-gen-optane-build-runs-2-8-trillion-parameter-kimi-k3-at-3-11-tokens-per-second-after-adding-two-rtx-3090s-moving-nearly-half-the-model-into-a-ram-drive-boosted-performance-by-41-percent
source_site: Tom's Hardware
source_slug: toms-hardware
description: A Reddit homelabber’s Optane PMem 200 server now runs Moonshot AI’s Kimi
  K3 at 3.11 tokens/s with two RTX 3090s and a RAM drive.
image: https://cdn.mos.cms.futurecdn.net/RSZf8MCxnNZcbAmBJQ8uxD-1072-80.jpg
published: '2026-11-21T00:00:00Z'
scraped_at: '2026-11-21T19:07:44Z'
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Nick Mermiges
- Shane Downing
- Tom
locations:
- Optane
organisations:
- CPU
- GPU
- Get Tom's Hardware
- Google News
- Moonshot
- Optane AI
- PSU
- Reddit
- Shane Downing
- Tom’s Hardware
---

![Open white PC case with a large CPU cooler, two GeForce RTX graphics cards and two black blower fans aimed at a row of memory modules](https://cdn.mos.cms.futurecdn.net/RSZf8MCxnNZcbAmBJQ8uxD-1072-80.jpg)

A homelabber detailed improvements to the second-gen Optane AI build in a follow-up post on Reddit, showing the addition of two RTX 3090s to run the 2.8-trillion-parameter Moonshot Kimi K3 model at 3.11 tokens per second. Transferring almost half the model onto a RAM drive added a significant 41% to generation speed and 26% to prompt evaluation. The extra fans are still needed, though, as the persistent Optane memory gets very hot.

That speed is not the most impressive, but it comes with 16.8 tokens per second for prompt evaluation, with 45 of 94 shards, or 414 GB out of 865 GB, living on a RAM drive. Such an arrangement is not new to enthusiasts who would set aside system memory for extra-fast performance in a pseudo-non-volatile manner — it’s still volatile, but appears like a disk — although not everyone has that much RAM sitting around free these days. With both GPUs but no RAM drive, the build ran at 2.20 tokens per second for generation and 13.3 for prompt evaluation.

|  |  |  |  |
| --- | --- | --- | --- |
| Kimi K3 Q2\_K with two RTX 3090s: model in Optane vs. partly in a RAM drive |  |  |  |
| Configuration | Where the model is stored | Generation (tokens/s) | Prompt evaluation (tokens/s) |
| Optane only | All 94 shards in Optane | 2.20 | 13.3 |
| RAM drive + Optane | 45 of 94 shards (414 GB of 865 GB) in a tmpfs RAM drive, the rest in Optane | 3.11 | 16.8 |
| Change | — | About 41% faster | About 26% faster |

*Builder’s measurements; llama.cpp, DAX on for the Optane portion.*

Even a quick read of the details makes it clear that the GPUs aren’t holding the model: two RTX 3090s, at 24 GB apiece, only have a total of 48 GB of VRAM, which is about 5.5% of the 865 GB model file. That said, the model is a mixture-of-experts (MoE) type, where its weights are split into multiple “experts” with only a few run per token. Any given token will have “routed” experts selected for it, while “shared” experts run on every token.

For this model, with 896 experts, 16 are chosen per token, with two shared, with an active 104B parameters out of its 2.8T. All 2.8T parameters would take about 5.6 TB at 16-bit precision. Moonshot’s own release, which uses the 4-bit MXFP4 format, comes to about 1.56 TB, and the Q2\_K file used here shrinks that to 865 GB, an average of under 3 bits per parameter. The 865 GB figure is likely in gibibytes (GiB), but for clarity we’re using the GB values as written by the homelabber.

The configuration here has the routed-expert tensors stay on the CPU side, originally in Optane, and now in Optane plus the RAM drive. The RTX 3090s handle attention, or how each token weighs the rest of the context, and the dense feed-forward network layer that isn’t split into experts, where every token passes through it. They also manage the shared experts, other active-dense components, the KV cache, and the stored context of the current conversation, with the GPU compute buffers. Basically, the parts on the GPUs are “used on every token,” and the improvements there come from the high level of GPU compute and memory bandwidth.

DRAM is a lot slower than VRAM, but it’s still capable of giving a decent speedup. The new build involves using Linux’s tmpfs, which, per the kernel documentation, “is a file system which keeps all of its files in virtual memory.” Those shards now live in memory, which admittedly is not ideal when the original build was designed to save money by using Optane instead. With those shards in DRAM, which the builder has said is faster than Optane, that part of the model no longer has to be read from the slower memory; the workload is decidedly distributed.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The speed that came with the GPUs is within the range of what the builder expected, guessing “somewhere between 2 and 4 tokens per second” in a prediction from the original build thread. The GPU install had to wait, in part, for modifications to the case, which required cutting out some of the metal and relocating the PSU to make room for the GPUs and their cooling. Cooling remains a huge issue, with “the improved throughput [not changing] the original thermal warning,” and the two 12W blower fans for the Optane DIMMs are kept in place. Add in dual 350W-class GPUs, and the changes are understandable.

Things won’t stop here, as more optimizations are possible, including “customized quantization,” which may be similar to the techniques used by lawyer Nick Mermiges. Quantization selected per tensor or layer, or by where the data lives, might reduce bandwidth and capacity pressures for the slower tiers; the setup “might be faster yet.” Speed, or tokens per second alone, is not enough, and output quality must be taken into consideration in any future plan.



Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

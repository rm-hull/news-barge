---
title: Modders halve FSR 4 render times on AMD’s PS5-derived BC-250 mining APU — portable
  FidelityFX DLL cuts 1440p upscaling time from 11.51 ms to 5.92 ms
source_url: https://www.tomshardware.com/pc-components/modders-halve-fsr-4-render-times-on-amds-ps5-derived-bc-250-mining-apu-portable-fidelityfx-dll-cuts-1440p-upscaling-time-from-11-51-ms-to-5-92-ms
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-14T14:59:29Z'
published: '2026-09-14T00:00:00Z'
description: Byte-identical output at half the GPU cost
image: https://cdn.mos.cms.futurecdn.net/4nd24gYgXdAhsopXnQWWf-1999-80.jpg
categories:
- Technology & Software
- Hardware
---

![The BC 250 board in-hand](https://cdn.mos.cms.futurecdn.net/4nd24gYgXdAhsopXnQWWf.jpg) 

Modders have slashed the cost of running FSR 4 on AMD’s RDNA 2-powered BC-250 by nearly half, with a new implementation cutting the upscaler’s processing time from 11.51 ms to 5.92 ms at 1440p. Detailed in a VideoCardz post, the latest work builds on the community’s ongoing effort to turn AMD’s unusual PlayStation 5-derived crypto-mining board into a capable Linux gaming machine, while moving the FSR 4 optimizations from a custom Mesa modification into a portable FidelityFX DLL.

According to testing shared by the developer, FSR 4.1.1 running at 2560 x 1440 with a 1706 x 960 Quality input required 11.51 ms using the original shaders, compared with 5.92 ms using the latest v4.0.0-rc9 release. At 4K, processing time reportedly dropped from 25.72 ms to 12.08 ms, while 1080p fell from 7.13 ms to 3.93 ms. The developer also reports that the optimized implementation produced byte-identical images to the original shaders in controlled testing, suggesting that the performance improvement comes from executing the same workload more efficiently, and not reducing image quality.

The BC-250 is particularly interesting in this context because it is based on much older RDNA 2 graphics hardware. FSR 4 relies heavily on machine-learning workloads and accelerated low-precision integer operations that are far better suited to newer AMD architectures. On the BC-250, those operations have to be handled through alternative instruction paths.

Earlier community work tackled the problem in Mesa, optimizing the INT8 dot-product operations used by FSR 4. Instead of relying on a much more expensive fallback sequence, the modified implementation used a more efficient mathematical path based around signed 24-bit integer operations. One representative shader reportedly fell from 64,269 instructions to 37,613.

The latest fork takes that work a step further by shifting the optimizations into a FidelityFX DLL. This removes the requirement to run a specially modified Mesa build, potentially making the optimized path easier to use with an existing OptiScaler installation or games with compatible native FidelityFX implementations.

Native Windows support, other GPUs, and frame generation have not yet been qualified, as the developer tested the BC-250 on Linux using standard Mesa and GE-Proton. The practical upper target for the board is roughly 1440p, as FSR 4 still consumes 12.08 ms at 4K even after the optimization.

The achievement is the latest chapter in the BC-250's unusual story. ASRock built the board for cryptocurrency mining systems around PlayStation 5-class AMD silicon, with six Zen 2 CPU cores and 24 RDNA 2 compute units enabled by default. With the mining market's collapse, individual boards began filtering onto the second-hand market for well under $150, and enthusiasts have since assembled a mature Linux gaming ecosystem around them, complete with custom firmware, GPU governors, CU unlock tools, cases, cooling solutions, and distro-specific fixes.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

We recently put the BC-250 through its paces and found that community-developed tools can unlock all 40 physical RDNA 2 compute units on compatible boards, up from 24 enabled by default, while separate firmware work can restore the two disabled Zen 2 CPU cores and take the chip from six cores to eight.

The ecosystem still comes with limitations. In our testing, the BC-250’s aging Zen 2 CPU became a substantial bottleneck at 1080p and 1440p in some games, even with the GPU fully unlocked. The board also has only 16GB of shared GDDR6 memory, which caused some titles to crash due to memory issues at 4K and made frame generation harder at higher resolutions. While FSR 4 will not erase those limitations, halving the upscaler's per-frame cost gives a once-discarded mining board significantly more headroom to spend elsewhere.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg) 

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.

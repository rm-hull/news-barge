---
title: AMD attempts to get ahead of expected RTX Spark launch with Gorgon Halo AI
  benchmarks — company says it has shipped 'over half a million agentic PCs' to date
source_url: https://www.tomshardware.com/pc-components/cpus/amd-attempts-to-get-ahead-of-expected-rtx-spark-launch-with-gorgon-halo-ai-benchmarks-company-says-it-has-shipped-over-half-a-million-agentic-pcs-to-date
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-05T22:03:02Z'
published: '2026-10-05T00:00:00Z'
description: AMD would like to remind you that it makes a big SoC for agentic PCs,
  too.
image: https://cdn.mos.cms.futurecdn.net/Kb7ipLjAkMtvShGfbBHACf-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Meh
- Neilbob
- Yuve
locations:
- Panther Lake
organisations:
- AMD
- Apple
- ComfyUI
- GLM
- Get Tom's Hardware
- Google News
- Gorgon Halo
- Intel
- Microsoft
- Nvidia
- Panther Lake
- RTX Spark
- Strix
- Tom’s Hardware
- Unsloth
---

![AMD Strix Halo Ryzen AI Max](https://cdn.mos.cms.futurecdn.net/Kb7ipLjAkMtvShGfbBHACf-1920-80.jpg)

Nvidia is expected to launch RTX Spark devices later this week, following a not-so-subtle tease at the end of last week (and the chip’s announced fall release). Ahead of Microsoft’s event on Wednesday, October 7 (where the launch is expected) AMD has shared some benchmarks for its new Gorgon Halo chips — the range that will directly compete with RTX Spark devices. The extra insight comes a matter of days after the first Gorgon Halo devices launched, some of which cost upwards of $7,099.

![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB-1200-80.jpg)

Short of a few questionable Geekbench leaks, we haven’t seen any performance results for the RTX Spark yet, so AMD isn’t using it as a comparison point. Rather, it’s comparing the Ryzen AI Max+ Pro 495 to Intel’s Core Ultra X9 388H. These chips aren’t in the same class of device, though AMD would argue that it’s comparing its top-of-stack part to Intel’s top-of-stack part.

AMD used ComfyUI to measure generative AI performance. AMD averaged multiple runs of various models, comparing total throughput to Intel’s competition. AMD used its top-spec 192GB configuration of the Ryzen AI Max+ Pro 495 and compared it to the Core Ultra X9 388H in a system with 64GB of memory (Panther Lake supports up to 128GB).

The performance advantage ranges from 1.1x up to 32.2x, though the end point is a clear outlier. We searched for Yuve on Hugging Face and didn’t find any results. It’s possible this delta comes down to an optimization issue, or that it’s simply too big to run on the Panther Lake machine.

![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/97PWMs5ECyz3nqhLh2Cuu6-1200-80.jpg)

We don’t have gaming or general application performance, but we don’t expect a major swing compared to last-gen Strix Halo chips. Gorgon Halo is largely a refresh of that range.

Gorgon Halo isn’t getting into the ring with Panther Lake, however. It’s going mainly against the RTX Spark, and to a lesser extent, Apple’s larger M-series SoCs. This category of agentic PCs, as AMD calls it, is seemingly expanding, though it’s still far smaller than some of the hype around the RTX Spark would have you believe. AMD bragged in a prebriefing with the press about shipping “10s of millions” of AI PCs (read: laptops) before clarifying that it had slipped “over half a million” agentic PCs. Presumably, those are numbers for Strix/Gorgon Halo devices.

The matchup between Gorgon Halo and the RTX Spark has, up to this point, focused mainly on memory capacity. RTX Spark devices top out at 128GB of unified memory, same as the GB10 in the DGX Spark (the two chips are nearly identical). AMD, on the other hand, supports up to 192GB with Gorgon Halo. Higher capacity means running larger models locally, though at a lower performance level.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/TfERuQxfCy3TJQtzSazPN6-1200-80.jpg)

In the GLM 5.3 Flash with 320 billion parameters, AMD saw peak throughput of 20 tokens per second, though using Unsloth's UD-IQ4\_XS mixed-quantization format. For context, we clocked peak token throughput on the DGX Spark running GPT-OSS 120B with 4-bit quantization at 64 tokens per second, and the last-gen Ryzen AI MAx+ 395 at 56 tokens per second.

Note that although GLM 5.3 Flash has 320 billion total parameters, only 18 billion are activated for each token. Similarly, GPT-OSS 120B is another mixture-of-experts model with 120 billion total parameters, though only around 5 billion are active per token.

![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/W7wxx4TYAxfjMws47a2NN6-1200-80.jpg)

AMD also shared Qwen 3.8 Flash Next performance, a multimodal MoE model with 125 billion main parameters, 51 billion embedding parameters, and about 4 billion parameters for multi-token prediction (MTP), with 5 billion parameters active per token. AMD says the Ryzen AI Max+ Pro 495 achieves up to 42 tokens per second with this model, once again using Unsloth’s dynamic 4-bit quantization and MTP.

That’s solid performance, but in both cases, “up to” carries a lot on its shoulders. The story of token throughput is told as the context length increases, showcasing what happens when someone actually runs these models locally, not just boots them up cold. Performance drops at higher context lengths, naturally, which could pose some issues for the larger models. If GLM 5.3 Flash provides up to 20 tokens per second, it could very easily decline into unusable territory as the context length increases.

We largely know what performance to expect out of the Ryzen AI Max+ Pro 495, and Gorgon Halo more broadly. It’s a refresh of Strix Halo, with notable spec changes being the bump up to 192GB of unified memory from 128GB, as well as a 100 MHz jump on boost clocks for the 495. Otherwise, the range is using identical core counts and microarchitectures as previous-gen Strix Halo chips.

With these proxies — Strix Halo for Gorgon Halo, and GB10 for RTX Spark — we can already get a good idea about how these parts will stack up. As you can see in our Ryzen AI Halo review (packing the Ryzen AI Max+ 395), AMD’s part universally underperformed compared to the DGX Spark in both time to first token and tokens per second across three models. More unified memory will allow you to run larger models, but that doesn’t mean those models will run *faster*.

The first Gorgon Halo devices are available for sale now, such as the Minisforum MS-S1 Max-P495. For the top-line configuration, prices sit around $7,000 right now, though we expect a broad range of prices once different devices are available, likely driving above that $7,000 mark.

## Full presentation

![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/Q8zF24EEDRZVKq3XxzeRd5-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/sqaqNxjWWDDhjxnzou4or5-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/n6U4mjn7zQoJXsu8QjWLD7-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/Q7kJDQRfF2bmV5pY2UXR67-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/VwqzkuZ7mSS2bh2fGaBG36-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/E4jBukQZgd9GG9EWzL5oc6-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/YMm8yrEP4q9P4zZrs8Bj67-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/Y6R45SHrAy7WHJsDrK3q97-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/3SK9babXoYJrXveRDyXE26-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/xaJUBXhs42Vq3HrsGrgs67-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/HZoyTff93MhqQF3arffdC7-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/4d4pCtVPFbkyWr4aDEBhM6-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/Cw5i8NYj9FNKBAK7EP2jC7-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/TfERuQxfCy3TJQtzSazPN6-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/W7wxx4TYAxfjMws47a2NN6-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/UpqAMuKBXVUAi7BSLbZ3Y7-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/97PWMs5ECyz3nqhLh2Cuu6-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/Qenh5gvVYhef5hDVMxDk76-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/LqaN5rDQBC7NTcvWkj8386-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/7KoHNhqyQHDMXXNvR6W5c7-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/af7UJFRj87TajLpgVDRWA7-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/dVyiKQuR5ckveygDKks9E7-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/RmdrwvGYUcvvkmVeuXpuC7-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/nrMYJRycXAq4KiWZYVVgE7-1200-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/Q8zF24EEDRZVKq3XxzeRd5-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/sqaqNxjWWDDhjxnzou4or5-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/n6U4mjn7zQoJXsu8QjWLD7-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/Q7kJDQRfF2bmV5pY2UXR67-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/VwqzkuZ7mSS2bh2fGaBG36-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/E4jBukQZgd9GG9EWzL5oc6-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/YMm8yrEP4q9P4zZrs8Bj67-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/Y6R45SHrAy7WHJsDrK3q97-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/3SK9babXoYJrXveRDyXE26-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/xaJUBXhs42Vq3HrsGrgs67-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/HZoyTff93MhqQF3arffdC7-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/4d4pCtVPFbkyWr4aDEBhM6-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/Cw5i8NYj9FNKBAK7EP2jC7-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/TfERuQxfCy3TJQtzSazPN6-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/W7wxx4TYAxfjMws47a2NN6-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/UpqAMuKBXVUAi7BSLbZ3Y7-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/97PWMs5ECyz3nqhLh2Cuu6-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/Qenh5gvVYhef5hDVMxDk76-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/LqaN5rDQBC7NTcvWkj8386-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/7KoHNhqyQHDMXXNvR6W5c7-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/af7UJFRj87TajLpgVDRWA7-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/dVyiKQuR5ckveygDKks9E7-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/RmdrwvGYUcvvkmVeuXpuC7-2000-80.jpg)
![AMD agentic PC presentation.](https://cdn.mos.cms.futurecdn.net/nrMYJRycXAq4KiWZYVVgE7-2000-80.jpg)



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi-140-80.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

* Neilbob said:Meh, whatever.  
    
  More importantly, the messed up font substitution issue we've seen before on AMD slides makes my bum hurt.But not your eyes? I question exactly what it is that you are doing when you are on the internet lol  
    
  [https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSX1T4Jkmw-AmKbWg\_vCG5LCO7TB1rxBHsPdiuAvqruyHt1zx1T9RSHCrY&s=10](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSX1T4Jkmw-AmKbWg\_vCG5LCO7TB1rxBHsPdiuAvqruyHt1zx1T9RSHCrY&s=10) Reply

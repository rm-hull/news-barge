---
title: Three 'e-waste' Nvidia V100s hit 100 tokens per second on Qwen 3.6 35B in a
  $1,042 homelab rig — decommissioned GPUs outpace a $5,399 M5 Max Mac Studio at long
  contexts
source_url: https://www.tomshardware.com/uk/tech-industry/artificial-intelligence/three-e-waste-nvidia-v100s-hit-100-tokens-per-second-on-qwen-3-6-35b-in-a-usd1-042-homelab-rig-decommissioned-gpus-outpace-a-usd5-399-m5-max-mac-studio-at-long-contexts
source_site: Tom's Hardware
source_slug: toms-hardware
description: A homelab builder runs Qwen 3.6 35B on three used Nvidia Tesla V100 GPUs
  at about 100 tokens per second, in a $1,042 build.
image: https://cdn.mos.cms.futurecdn.net/Mmy36NYLic3BaS5bAHCZZ7-2560-80.jpg
published: '2026-11-19T00:00:00Z'
scraped_at: '2026-11-19T20:30:39Z'
categories:
- Technology & Software
- Hardware
people:
- Arkitekt78
- Dav\_Daddy
- Guy
- Humm
- Kleybrink
- Qwen
- Shane Downing
- Spark
- Tom
locations:
- Qwen
organisations:
- GPU
- Get Tom's Hardware
- Google News
- K80's
- Mac
- MoE Gemma
- PSU
- Parasail
- Reddit
- Shane Downing
- Supermicro X10DRG-Q
- Tom’s Hardware
- eBay
---

![Three Nvidia Tesla V100 graphics cards side by side, each fitted with a black 3D-printed blower fan duct](https://cdn.mos.cms.futurecdn.net/Mmy36NYLic3BaS5bAHCZZ7-1920-80.jpg)

A homelab builder benchmarked three used Nvidia V100s on Qwen 3.6 35B, achieving about 100 tokens per second in a custom setup costing $1,042 with just “e-waste” GPUs. The smaller, dense Qwen 3.6 27B manages about 24 tokens per second on the same platform, and the V100s use about half the energy of the same number of P100s for a given job.

The blog post, “Scaling ‘E-Waste’: LLMs on Multiple Decommissioned GPUs,” compares nine different builds — one to three K80s, P100s, or V100-16GB cards — on a single Supermicro dual-Xeon board. The test uses llama.cpp and covers more than 130 LLM tests, including Qwen 2.5, Gemma 4, and, of course, Qwen 3.6, at Q4/Q8/F16 precisions and from 4K to 128K context sizes. GPU energy per run is also recorded. The builder is “daily driving Qwen 3.6 35B” on the V100s and notes that scaling decommissioned GPUs will only get you so far.

“E-waste,” in this case, refers to decommissioned enterprise GPUs, which are a popular but somewhat underpowered option when compared to very expensive modern alternatives. The Nvidia Tesla V100s in question are tested as a follow-up to a July round which tested 15 “e-waste” GPUs, and this time the board and CPUs stay the same for every build — the Supermicro X10DRG-Q with two Intel Xeon E5-2687W 12-core CPUs, powered by the Corsair HX1500i PSU.

Performance is judged based on what is considered “realtime interaction” which, here, is 70 tokens per second. As to why the number of GPUs is three: Qwen 3.6 35B, the primary tested model, fails on just one or two at Q8, or 8-bit quantization.

Here are the given prices, with the note that they aren’t “100% reflective of what you could find on eBay today,” although the totals count only one of the two CPUs and omit RAM, storage, the case, and any cooling.

|  |  |  |  |
| --- | --- | --- | --- |
| What the builder paid for each three-card build |  |  |  |
| Part | 3x K80 | 3x P100 | 3x V100-16GB |
| Three GPUs | $270 ($90 each) | $403.50 ($134.50 each) | $655.16 ($436.77 per pair) |
| Board | $211 | $211 | $211 |
| PSU | $147.70 | $147.70 | $147.70 |
| One CPU | $28.20 | $28.20 | $28.20 |
| Builder’s total | $657 | $790 | $1,042 |
| With 2nd CPU | $685 | $819 | $1,070 |

The older cards are relatively inexpensive because they “run hot and ship without cooling,” which required the builder to 3D print one blower duct per card and has led to the development of a standalone cooler.

The bench itself involves 10 runs of 512 generated tokens per test with context pre-filled to 4K, 32K, 64K, or 128K. Qwen 3.6 35B is a mixture-of-experts (MoE) model, which only activates about 3 billion out of its 35 billion total parameters per token. The numbers that immediately follow are at Q8.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The token goal was easily reached…when the context window was small, or 4K. The 100.8 tokens per second there fell to 72.7 at 128K, still usable by the 70 tokens per second goal. The 27B model, which is not MoE, fared much worse, at 24.3 at 4K, 21.6 at 32K, 18.7 at 64K, and just 14.2 at 128K. The MoE ends up about four to five times faster, depending on the context size.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Qwen 3.6 35B generation speed by context length (tokens per second) |  |  |  |  |
| Setup | 4K | 32K | 64K | 128K |
| 3x V100, Q8 | 100.8 | 89.4 | 83.5 | 72.7 |
| 2x V100, Q4 | 105.4 | 96.2 | 89.5 | 77.1 |
| 3x P100, Q8 | 55.2 | 50.9 | 47.5 | 40.2 |
| M5 Max Mac, 8-bit | 105.5 | 91.1 | 78.5 | 61.3 |

Also tested were other dense models of about 30B parameters. At 4K, Gemma 4 31B achieved 20.9 and Qwen 2.5 32B 21.0, while the MoE Gemma 4 26B cleared the 70 tokens per second bar with just two V100s at Q8. If you move down to Q4, or 4-bit quantization, two V100s can run Qwen 3.6 35B at 77.1 to 105.4 tokens per second, between 128K and 4K context size. This is where it’s claimed that adding more cards gives you more memory, which enables larger models to be run, but not speed.

![Bar chart showing Qwen 3.6 35B running about four to five times faster than Qwen 3.6 27B on three Tesla V100 cards at every context length](https://cdn.mos.cms.futurecdn.net/A6SeePQLEXNDjF65NZGeNf-1200-80.png)

The P100s, for comparison, only hit 40.2–55.2 tokens per second in the same context range with Q8 Qwen 3.6 35B, and the target 70 only with Qwen 2.5 3B. If we compare to more modern hardware — the Nvidia DGX Spark, MSRP $4,700, and the M5 Max Mac Studio, which starts at $2,499 but costs $5,399 with the tested 40-core GPU, 128GB of memory, and a 1TB SSD — the 3x V100 build holds its own, using sourced data.

The Mac comparison comes from the oMLX benchmark page for the M5 Max with 40 GPU cores and 128GB of unified memory, and that hits 43.9 tokens per second with a ~195K-token prompt on the Qwen 3.6 35B model. The Mac is slightly ahead at 4K and 32K, while the V100s pull ahead at 64K and 128K, by 19% at the longest context. These numbers have to be taken loosely, as the machines use different runtimes.

The Spark run came from Kleybrink’s dgx-spark-bench, using Ollama in thinking mode with short prompts. Its 45.8 tokens per second is less than half the V100s’ 4K figure.

Going further to modern GPUs, which “destroy our decommissioned equivalents,” as the builder puts it, you get about 315 tokens per second on two H100s and about 455 on one B200 at 128K, the B200 roughly six times the V100 box, even though the hosted cards ran the full 16-bit model against the V100s’ 8-bit. Parasail, an inference provider, sponsored that comparison with dedicated H100 and B200 deployments.

As for energy, the V100 setup came out to about 0.02 kWh for a 128K 35B run, with the P100s taking twice that much and two or three K80s as much as 0.35 to 0.45 kWh. The V100-16GB simply “[puts] up better scores while consuming less energy,” in comparison to the P100s. These numbers are for the GPUs and not from the wall.

There’s more to come. The builder wants a benchmark that “maps to ‘software factory’ performance,” a term for models being prompted constantly, around the clock, where instant speed matters less. Then there’s the cooler, which is “almost ready for release,” with beta testers to be recruited from the mailing list, although no date has been given. From the Reddit thread, the builder mentions the intention to compare inference backends and use speculative decoding to improve performance.



Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

* So it can do 86,400 tokens per day... Congrats, your rig is useless in the first 5mins of my work!  
    
  but lets do the math, this rig is worth $1042, you would need 96 of these rigs to sustain my daily (8-hour) load, bringing the total to $100,032 per DAY, vs my roughly $5K per month I pay now.  
    
  Youre right, this rig is e-waste, aka garbage! Reply
* Rand0m\_Guy said:So it can do 86,400 tokens per day... Congrats, your rig is useless in the first 5mins of my work!  
    
  but lets do the math, this rig is worth $1042, you would need 96 of these rigs to sustain my daily (8-hour) load, bringing the total to $100,032 per DAY, vs my roughly $5K per month I pay now.  
    
  Youre right, this rig is e-waste, aka garbage!Humm, now I know why you use a lot o IA:  
  e-waste rig -100 token/sec\*86400 sec/day = 8.640.000 tokens/day.  
  You are wasting $4000 by month...  
  your brain is already shrinking Reply
* Arkitekt78 said:Its almost as if if these engineers knew what they were doing, they wouldn't have to be spending billions of $ on "the best" and we wouldn't be in a RAM/storage/GPU crisis. Huh.The problem was, and continues to be, density and supply, not money. Because that was the issue, large companies would not have seeked out older tech that takes up 5 times the space for the same speed at 1/5th the efficiency to fill their needs. Money was never the constraint. Reply
* Where are the numbers for the K80's? I was thinking about grabbing a couple of them while they are still cheap but was afraid they'd be too slow.  
    
  Assuming you're a single user and you are just using them for chat/coding anything much above 35 tok/sec is unnecessary. Sure generating a response takes a few seconds but on the bright side you can monitor the thing and stop it if it gets into a loop or something. Reply
* mangaba said:Humm, now I know why you use a lot o IA:  
  e-waste rig -100 token/sec\*86400 sec/day = 8.640.000 tokens/day.  
  You are wasting $4000 by month...  
  your brain is already shrinkingHey, maybe you saved them 4k a month after they get an older 1000-2000 dollar system for their work 'needs.' Reply
* Dav\_Daddy said:Where are the numbers for the K80's? I was thinking about grabbing a couple of them while they are still cheap but was afraid they'd be too slow.  
    
  Assuming you're a single user and you are just using them for chat/coding anything much above 35 tok/sec is unnecessary. Sure generating a response takes a few seconds but on the bright side you can monitor the thing and stop it if it gets into a loop or something.I asked AI how many tokens a K80 would get with Qwen 3.6 with 35B parameters, and it said the following regarding K80s, "...getting Qwen 3.6 running at these speeds requires custom/patched engines or sm\_37 builds, and splitting layers across dies or host RAM adds PCIe/bridge overhead." It also estimated that one of them would do between 10-30 tokens a second depending upon parameters, context length, quant, and speculative decoding with Qwen. K80's also have two GPUs and each one has only half the cards 24gb of memory available to it. Reply

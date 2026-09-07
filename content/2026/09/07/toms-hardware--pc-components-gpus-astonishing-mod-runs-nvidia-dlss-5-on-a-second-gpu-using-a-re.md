---
title: Astonishing mod runs DLSS 5 on a second GPU to boost neural-rendered FPS up
  to 127% — game renders on one card, neural post-processing runs on the other, much
  like dedicated PhysX GPUs
source_url: https://www.tomshardware.com/pc-components/gpus/astonishing-mod-runs-nvidia-dlss-5-on-a-second-gpu-using-a-reshade-add-on-to-reduce-performance-impact-boosts-neural-rendered-fps-up-to-127-percent-game-renders-on-one-card-neural-post-processing-runs-on-the-other-much-like-dedicated-physx-gpus
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-07T14:13:22Z'
published: '2026-09-07T00:00:00Z'
description: Harkening back to the days of PhysX.
image: https://cdn.mos.cms.futurecdn.net/4ZFtovYiMpEBjjieRS5K5j-1263-80.jpg
---

![Cyberpunk DLSS overlay](https://cdn.mos.cms.futurecdn.net/4ZFtovYiMpEBjjieRS5K5j.jpg) 

Nvidia's DLSS 5 Neural Rendering technology has taken the PC gaming world by storm since its recent leak and then official rollout in recent days. In what might be one of the most impressive technical applications and mods of the feature yet, one developer has showcased DLSS 5 running on a second GPU to share the processing load, rendering the game on the first GPU before applying Neural rendering at the end of the frame, thus boosting the performance of neural-rendered frames.

Marcelo Guibout shared the demonstration online, with videos showing the process running on a cinematic video from *The Blood of Dawnwalker,* as well as*Cyberpunk 2077.* Guibout was quick to clarify that the videos are technical showcases, not benchmarks. However, they did share some performance figures. More exciting still, you can download the project from GitHub and try it for yourself. However, the technique does require a second display and doubles the display latency.

![Cyberpunk 2077 with DLSS 5 Neural Rendering Offloaded to a Second GPU — Dual RTX 5060 Ti - YouTube](https://img.youtube.com/vi/XWv5jw90yHc/maxresdefault.jpg) 

The above demonstration features a Ryzen 7 7800X3D, 32GB DDR5 setup with two Nvidia RTX 5060 Ti 16GB GPUs, with both cards using PCIe 5.0 x8, and a display attached to each card. The ReShade add-on, dubbed MGPU Bridge, reads each finished frame before applying Nvidia's Neural rendering. "Neural rendering happens at the end of the frame: it takes a finished frame and hands a finished frame back," they explain. "That is what makes it possible to pick it up and run it somewhere else. The add-on creates its own D3D12 device on your second GPU, sends each finished frame across to it, runs DLSS-NR there, and displays the result on that card's own monitor — so nothing has to come back. The render GPU does no neural work at all and runs cooler for the same reason."

In the TBOD demo at 1080p, they shared the following performance numbers:

| DLSS mode | DLSS 5 off | DLSS 5 on the render card | DLSS 5 on the second card | 
|---|---|---|---|
| DLAA | 67-70 | 44 | 67-70 | 
| Quality | 98-99 | 54-55 | 91 | 
| Performance | 127-131 | 59 | 106-107 | 
| Ultra Performance | 172 | 69-71 | 157 | 

Guibout clarified that DLSS super-resolution is running in every column of the test, with the rows showing each mode tested. The game rendered at the same internal resolution in all three columns, with the first column giving figures with DLSS 5's neural rendering switched off, representing the ceiling for performance. As you can see, running DLSS 5 on the second card in this dual-GPU setup drastically increases performance in every mode.

"The frame rates are not the finding. The slope is: what you gain by going from DLAA down to Ultra Performance, and how much of that available gain each arm keeps," Guibout explains. "Neural post-processing saturates whatever device it runs on, and it always runs at *output* resolution. Its cost barely falls as you drop the DLSS mode, while the render work collapses. On the render card it therefore eats a larger and larger share of every frame, and upscaling stops paying for itself: you keep about a third of what the machine actually had to give. Move it to the second card and you keep 86% of it."

Other benefits include temperature reductions on the rendering card, with the first GPU running 21 degrees cooler without the neural load.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Guibout is cautious to note this isn't a return to Nvidia's SLI technology, which would split the workload of frame rendering between two GPUs. They also noted plainly this is not Nvidia's vision for DLSS 5 and lacks the native integration of official DLSS 5 support.

You can see the original demo for TBOD below:

![Multi-GPU DLSS Neural Rendering — Dual RTX 5060 Ti (Dawnwalker, Cinematic) - YouTube](https://img.youtube.com/vi/yoEsuZyltFc/maxresdefault.jpg) 

As commenters online have noted, the method seems more akin to using Nvidia's dedicated PhysX cards, with plenty of potential for gamers who have the capacity to run a dual GPU setup. The second demo features a Ryzen 5 5600 on a DDR4 system, so top-of-the-line hardware isn't required to make it happen.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Stephen Warwick](https://cdn.mos.cms.futurecdn.net/uWwzwaway8BM4BERLmtuNE.jpg) 

Stephen is Tom's Hardware's News Editor with almost a decade of industry experience covering technology, having worked at TechRadar, iMore, and even Apple over the years. He has covered the world of consumer tech from nearly every angle, including supply chain rumors, patents, and litigation, and more. When he's not at work, he loves reading about history and playing video games.

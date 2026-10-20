---
title: Mods can almost double DLSS 5 performance through Foveation, reducing resolution
  at the edges of frames — technique makes DLSS 5 possible on high-resolution ultrawide
  monitors
source_url: https://www.tomshardware.com/pc-components/gpus/mods-can-almost-double-dlss-5-performance-through-foveation-reducing-resolution-at-the-edges-of-frames-technique-makes-dlss-5-possible-on-high-resolution-ultrawide-monitors
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-20T14:18:22Z'
published: '2026-10-20T00:00:00Z'
description: This might actually make DLSS 5 more accessible.
image: https://cdn.mos.cms.futurecdn.net/Axh3XNQ6DqK4KMfxtoMRBU-2560-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Jhet Borja
- Tom
locations: []
organisations:
- Foveated DLSS5
- GPU
- Google News
- Maximed
- Maximedgoulet
- Reddit
- VR
---

![Nvidia GeForce RTX 5090](https://cdn.mos.cms.futurecdn.net/Axh3XNQ6DqK4KMfxtoMRBU-1920-80.jpg)

Popular graphics post-processing injector software ReShade, commonly used to mod DLSS 5 into unsupported games, now has a foveated imaging add-on, including another standalone project that doesn't need precursor software, allowing DLSS 5 to affect only what's in view, reducing GPU load and increasing FPS.

Foveated imaging is nothing new; it's a technique that's been used in VR to increase performance. It works by only rendering what's in view, often increasing the resolution in the center and reducing it at the edges. Our eyes work in a similar way, with the clearest image in a small area in the center of your vision, blurring on the edges. With foveated rendering, you barely notice the lower-resolution edges as the peripheral vision is less concerned with fine details.

Instead of varying the resolution of the image, however, it varies the level of detail in DLSS 5 Neural Rendering. DLSS NR loads a whole AI model into your GPU and renders images in real time, making it a resource-intensive task; but the task is minimized greatly when most of the detail is only asked for in the middle of the image. That's what projects like maximedgoulet’s Foveated DLSS5 and ClarkCheekyKent’s CheekyFoveatedDLSS aim to do; with Foveated DLSS being a ReShade add-on and CheekyFoveatedDLSS capable of being a standalone integration.

Both implementations allow you to adjust the size of the center area with the highest rendering quality, with independent width and height adjustments to suit your personal situation, as some people have a larger focus area than others or have a different monitor distance. You can also adjust the render fall-off rate, so the image quality lessens more quickly or slowly past the focus area.

As Maximedgoulet's implementation is an add-on for an injector, the pipeline is quite long compared to the standalone integration of CheekyFoveatedDLSS, which Reddit comments claim is more convenient and more polished. Though both show a big improvement in performance, Maximed's Reddit post on Foveated DLSS5 claims an improvement from 48 to 80FPS in The Witcher 3 with 2x Multipass at ultrawide 7680x2160p on an RTX 4090. Considering Maximedgoulet’s 4090 could not handle DLSS-NR on an ultrawide, this implementation might genuinely be feasible to make Neural Rendering more playable.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jhet Borja](https://cdn.mos.cms.futurecdn.net/niBNJTDN6c99Ri7HD5zNZ8-140-80.png)

Jhet Borja is a serial hobbyist who was taking apart toys from childhood and sketching inventions. He now loves doing DIY projects ranging from designing custom 3D-printed parts, building PCs and keyboards, all the way to woodworking. If he's not getting his hands dirty, he's probably brainstorming his next project.

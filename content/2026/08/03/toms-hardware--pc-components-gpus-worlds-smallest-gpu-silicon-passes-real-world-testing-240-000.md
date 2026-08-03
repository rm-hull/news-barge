---
title: World’s smallest GPU silicon passes real-world testing — 240,000-transistor
  TinyGPU v2.0 renders 3D graphics at up to 15 FPS while v3.0 prepares for 2026 release
source_url: https://www.tomshardware.com/pc-components/gpus/worlds-smallest-gpu-silicon-passes-real-world-testing-240-000-transistor-tinygpu-v2-0-renders-3d-graphics-at-up-to-15-fps-while-v3-0-prepares-for-2026-release
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-03T11:39:40Z'
published: '2026-08-03T00:00:00Z'
description: TinyGPU v3.0 will feature a programmable pixel shader.
image: https://cdn.mos.cms.futurecdn.net/XGMRs2DoMrY7PMM2eekx3k-1920-80.jpg
---

![TinyGPU v2.0](https://cdn.mos.cms.futurecdn.net/XGMRs2DoMrY7PMM2eekx3k.jpg) 

We wrote about the world’s tiniest GPU heading to production last November. Its developer, Pongsagon Vichit, has now received the finished silicon back from the Tiny Tapeout community, where it was part of the SKY 25b shuttle. “ASIC TinyGPU v2.0 is alive and working!!!” cheered the amateur ASIC/FPGA designer on social media. That’s definitely worth celebrating, and we are also happy to hear that TinyGPU v3.0 will arrive towards the end of this year.

ASIC TinyGPU v2.0 is alive and working!!!Huge thanks to the #TinyTapeout community for all the support.Check out the fully open-source design here:[https://t.co/ClhiKS89st](https://t.co/ClhiKS89st) P.S. TinyGPU v3.0 is coming this December! Stay tuned.#OpenHardware #FPGA #ASIC pic.twitter.com/vgfg2ZehAuJuly 31, 2026


Above you can see the TinyGPU v2.0 SKY 25d “standalone GPU” silicon in action. At the beginning of the embedded video, Vichit has a rather low-polygon model on screen that is being manipulated by a game controller in real time. The second demo, showing a colorful zooming and rotating globe representing the Earth, is more impressive.

According to the TinyGPU v2.0 GitHub, this GPU can perform transformation & lighting plus rasterization with a maximum of 1,000 triangles on screen. It also features one dynamic directional light, flat shading, backface culling, and affine texture mapping. This finished sliver of silicon, packing around 240,000 transistors, also offers a 4-bit double buffer and an 8-bit depth buffer stored on QSPI RAM, according to its designer.

In our earlier reporting, we noted that TinyGPU v2.0 was tested using a Basys3 FPGA host. This test only managed frame rates in the demo of between 7.5 and 15 FPS. The Tiny Tapeout silicon won’t run any faster than the FPGA, Vichit previously indicated, and indeed, the on-screen action doesn’t look any more fluid.

## TinyGPU v3.0 ASIC details and delivery schedule

No sooner has TinyGPU v2.0 materialized than the excitement over TinyGPU v3.0 begins to build. The next-gen TinyGPU had already been submitted to Tiny Tapeout’s upcoming run before TinyGPU v2.0 was actually received and tested by Vichit. “But we all know that GPU is a cut-throat business — must release new models fast,” joked the enthusiast.

New and significant in TinyGPU v3.0 is the programmable pixel shader. In other social media posts about this upcoming GPU, Vichit reveals that it will boast the following pixel shader specs:

- Lightweight DirectX 8 PS 1.1–inspired design
- SIMD (4 pixels in parallel)
- 31 instructions per shader (tweaking)
- 26-op instruction set
- Branching via masked execution
- 4x 8-bit temp registers

With the new pixel shader in parallel with Z-buffer access, and near/far plane culling plus guard band clipping, big fidelity gains are teased. A far more detailed, textured, and animated model should be the result with little to no performance impact.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

TinyGPU v3.0 is coming with a programmable Pixel Shader!! Tested on FPGA and submitted to the #TinyTapeout May shuttle (~290k transistors). This Chameleon demo is a tribute to the #GeForce 3, the first programmable GPU released 25 years ago. [https://t.co/GCy7tmGfUA](https://t.co/GCy7tmGfUA) pic.twitter.com/ijr0DGzuR9April 22, 2026


One of the earliest TinyGPU v3 demos featured a chameleon to pay tribute to the Nvidia GeForce 3, reputed to be the first programmable shader GPU for consumers. That milestone was achieved in a PC graphics card that launched a quarter of a century ago (Feb 2001).

The latest information about TinyGPU v3 mentions that the finished ASIC should be delivered in December 2026 or January 2027.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

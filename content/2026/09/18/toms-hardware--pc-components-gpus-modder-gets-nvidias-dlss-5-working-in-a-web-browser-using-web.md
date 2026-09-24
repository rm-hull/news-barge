---
title: Modder gets Nvidia's DLSS 5 working in a web browser using WebGPU — 147MB browser
  port runs on non-Nvidia GPUs and macOS but takes two seconds per render
source_url: https://www.tomshardware.com/pc-components/gpus/modder-gets-nvidias-dlss-5-working-in-a-web-browser-using-webgpu-147mb-browser-port-runs-on-non-nvidia-gpus-and-macos-but-takes-two-seconds-per-render
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-18T13:00:14Z'
published: '2026-09-18T00:00:00Z'
description: Neural rendering in a browser tab, no game install needed
image: https://cdn.mos.cms.futurecdn.net/peEtJE98WLRCbHo2PH4CQF-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
locations:
- NBA
- WebGPU
people:
- Shane Downing
- Tom
organisations:
- Cloudflare Workers
- DLSS 5
- GPU
- GeForce NOW
- Google News
- MAAN
- MAAN's X
- Nvidia
- Shane Downing
- Tom’s Hardware US
- Vulkan
- WebGPU
- __*VideoCardz*__
---

![NBA 2K27 gameplay](https://cdn.mos.cms.futurecdn.net/peEtJE98WLRCbHo2PH4CQF.jpg) 

A modder by the name of MAAN has reportedly gotten Nvidia DLSS 5 working in a browser window with an interactive demo, according to a report by __*VideoCardz*__. The developer said the technique also works on macOS. The demo is hosted on Cloudflare Workers with some default scenes, starting with "Cowboy Gramps," with a variety of adjustable settings and a comparison view.

DLSS 5 running in the browser with #webgpu And yes it works on MacOS too. Try the the live demo here [https://t.co/frqdwHzeDv](https://t.co/frqdwHzeDv) You can also try it with your own models #WebDev #AI #threejsSeptember 16, 2026


DLSS 5 is Nvidia's neural rendering feature used to improve graphical quality using AI. Nvidia __launched it earlier this month__ for NBA 2K27, the first game with official support for the technology. DLSS 5 is officially RTX 50-series only, aside from GeForce NOW. The DLSS 5 DLL file has since been pushed onto __RTX 40-__ and __RTX 30-series__, and even __AMD hardware__. There is also a mod to unlock it for __RTX 20-series__ hardware.

According to MAAN, the demo uses model weights extracted from a leaked DLSS 5 library file. They did not know whether this file differs from the official one. Normally, Nvidia offers DLSS through its NGX interface or the Streamline SDK on DirectX and Vulkan. The documentation does not list WebGL or WebGPU, the outlet noted. MAAN plans to publish the source code on GitHub this weekend.

In our quick test of the demo on an RTX 40-series desktop, the 3D viewer was smooth to rotate, but each DLSS 5 render took a second or two and was notably slow in live mode.

MAAN said that the demo is DLSS 5's neural network reimplemented using WebGPU compute shaders. The weights are around 147MB, with a JavaScript runtime of around 1MB compressed. WebGPU has no trouble running on macOS, so the only surprise here is the DLSS part. Normally this needs an RTX GPU and Nvidia's driver, but a WebGPU implementation would not inherently require Nvidia hardware.

The outlet suggested the approach could suit architecture, 3D model previews, and other work where real-time speed matters less. MAAN's X post said users "can try it with your own models" and the demo's page accepts common 3D formats by file or drag-and-drop. Due to the technology's current restrictions, a browser demo is a way for more people to see the effect on a model without owning the game or appropriate hardware. Nvidia has said __official RTX 40-series support__ is coming.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69.png) 

Shane Downing is a Freelance Reviewer for Tom’s Hardware US, covering consumer storage hardware.

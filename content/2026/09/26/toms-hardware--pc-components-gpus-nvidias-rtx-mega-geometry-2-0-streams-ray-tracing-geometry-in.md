---
title: Nvidia’s RTX Mega Geometry 2.0 streams ray-tracing geometry into VRAM on demand
  — Nanite-inspired design drops detail instead of dropping out
source_url: https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-mega-geometry-2-0-streams-ray-tracing-geometry-into-vram-on-demand-nanite-inspired-design-drops-detail-instead-of-dropping-out
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-26T15:46:32Z'
published: '2026-09-26T00:00:00Z'
description: Nvidia's new ray-tracing sample handles a 1.6-billion-triangle scene
  with just 2GB of VRAM dedicated to geometry.
image: https://cdn.mos.cms.futurecdn.net/f5mw94jS8GbvM99nu2SUWa-2560-80.png
categories:
- Technology & Software
- Hardware
- Film & TV
people:
- Alan Wake
- Tom
locations:
- GitHub
- Zorah
organisations:
- Agility SDK
- Get Tom's Hardware
- Google News
- Microsoft
- NTC
- Nvidia
- RTX Kit
- Shane Downing
- Tensor Core
- Tom’s Hardware
- VRAM
- Vulkan
- Zorah
---

![Path-traced view into the carved dome of Nvidia&#039;s Zorah sample scene](https://cdn.mos.cms.futurecdn.net/f5mw94jS8GbvM99nu2SUWa.png)

Nvidia has updated its RTX Mega Geometry SDK to 2.0, adding streaming support for “continuous level-of-detail clusters” to handle high-density meshes, according to the developer blog post. Nvidia says it works even for scenes too big for the VRAM budget. The technology is in addition to its RTX Kit, arriving alongside RTX Kit 2026.3. The announcement comes close to the release of Gears of War: E-Day, which makes use of RTX Mega Geometry technology. Nvidia has not explicitly said what version of Mega Geometry the game uses.

![Asus RTX 5080 Noctua Edition](https://cdn.mos.cms.futurecdn.net/Wh9EZgD8NG9yUioNNgPB3d.png)

Mega Geometry “organizes detailed meshes into clusters so ray-traced scenes can adapt geometric detail efficiently,” according to Nvidia. The SDK appeared at version 0.9.0 beta in 2025 and found its way into Alan Wake 2’s title update 1.2.8 early that same year. Our test on an RTX 4090 found about 1GB of VRAM saved with a performance boost of 13%, at native 4K and with DLSS Quality. On an 8GB graphics card, that 1GB is an eighth of the memory.

The SDK is at version 2.0.0 on GitHub as of this week. The technology makes dense scenes less expensive to ray trace, with 2.0 specifically targeting geometry that doesn’t fit in VRAM. This means that “a scene’s source geometry no longer has to fit in VRAM [with detail] bounded by a memory budget rather than by mesh count,” according to Nvidia’s changelog.

When a scene goes over budget, it settles at lower detail instead of constantly swapping geometry in and out of VRAM. By default, this is based on 2GB of VRAM for streamed geometry, another 2GB for ray-tracing acceleration structures, and 4GB of material textures, but these are adjustable. The existing tessellation path remains.

In the case of Nvidia’s sample Zorah, there are 1.6 billion unique triangles in a 70GB download, with a first load that can require up to 64GB of RAM at peak. Zorah uses 31GB of mesh data, but the courtyard sample view only has 1.5GB of mesh data in VRAM, using an RTX 5090 at 4K with DLSS Quality.

![Nvidia&#039;s path-traced Zorah sample scene courtyard](https://cdn.mos.cms.futurecdn.net/d5DHfWRfqvqn9dbRijNRMf-1200-80.png)
![Nvidia&#039;s Zorah courtyard in Mega Geometry&#039;s level-of-detail view](https://cdn.mos.cms.futurecdn.net/eUQBtktfpjC5yrUSC5gaWf-1200-80.png)
![Nvidia&#039;s path-traced Zorah sample scene courtyard](https://cdn.mos.cms.futurecdn.net/d5DHfWRfqvqn9dbRijNRMf-1280-80.png)
![Nvidia&#039;s Zorah courtyard in Mega Geometry&#039;s level-of-detail view](https://cdn.mos.cms.futurecdn.net/eUQBtktfpjC5yrUSC5gaWf-1280-80.png)

The sample requires an RTX GPU with 10GB of VRAM or more, a Game Ready driver 570 or later, Microsoft’s DXR 1.1 or later, and Windows 10 at a minimum. For now, this looks more like a tool for developers than players. It’s an SDK with a reference sample, and currently no game has been confirmed to use it.

The rest of RTX Kit 2026.3 includes RTX Character Rendering 1.4, RTX Dynamic Illumination 3.1, RTX Neural Texture Compression (NTC) 0.10 beta, RTX Neural Shading 1.4, and RTX Texture Filtering 1.3. NTC has been at v0.10.0 beta on GitHub since Aug. 4, with the DX12 LinAlg path only for testing purposes. The DX12 LinAlg path requires preview driver 620.12, the preview Agility SDK, and Windows Developer Mode. That leaves Vulkan as the only way for released games to use NTC with Tensor Core acceleration today.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

An existing problem, Nvidia said in August, is that under ray tracing, Nanite elements “switch to a single, static low-detail mesh” because it’s “prohibitively expensive” to build acceleration structures for them with “existing DXR 1.2 and Vulkan APIs.” It has taken six years of research and development to pioneer the new technology, with the innovations debuting with Gears of War: E-Day on Oct. 6. These will later be part of Microsoft’s DirectX Raytracing 2.0 standard, according to Nvidia.

On Sept. 22, in a Game Ready driver post, Nvidia stated that Mega Geometry enables “accurate ray tracing of Nanite geometry for the very first time.” Nvidia’s Game Ready driver 617.14 for the game is already out. Early access on Oct. 1 is the first chance for players to see Nvidia’s Nanite ray tracing technology in action.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

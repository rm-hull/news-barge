---
title: Open source project renders your Windows 11 desktop using the NPU rather than
  the GPU — ‘npu-driver’ can only run at 2 to 3 Hz, targets 30 Hz performance
source_url: https://www.tomshardware.com/pc-components/gpu-drivers/open-source-project-renders-your-windows-11-desktop-using-the-npu-rather-than-the-gpu-npu-driver-can-only-run-at-2-to-3-hz-targets-30-hz-performance
source_site: Tom's Hardware
source_slug: toms-hardware
description: Developer is aiming for 30 Hz performance on Intel Panther Lake NPUs
  but the current version of this research driver is only achieving 2 to 3 Hz.
image: https://cdn.mos.cms.futurecdn.net/Ro4sQLyJUnVjqu8DK7qu85-1920-80.jpg
published: '2026-11-04T00:00:00Z'
scraped_at: '2026-11-04T14:26:53Z'
categories:
- Technology & Software
- Hardware
people:
- Mark Tyson
- Tom
locations:
- Panther Lake
organisations:
- Copilot
- GPU
- GitHub
- Google News
- Intel Panther Lake
- Microsoft
- NPU
- Reddit
- Tom's Hardware
---

![NPU rendering](https://cdn.mos.cms.futurecdn.net/Ro4sQLyJUnVjqu8DK7qu85-1920-80.jpg)

A developer group by the name of labscommunity has released a prototype driver for Windows 11 that renders the desktop using an NPU instead of the system’s (i)GPU. The new driver is called npu-driver, and the open-source (Apache 2.0) code is available on GitHub. It has been tested on Intel Panther Lake systems, and while it isn’t hitting its 30 Hz performance target yet, it is clever enough to fall back to GPU on request or on any fault.

![NPU rendering](https://cdn.mos.cms.futurecdn.net/txdq2hBQbjznvs5cjc28E5.gif)

The reasoning behind the development of this driver may strike a chord with those observing the 2020s processor landscape. “Every new laptop ships an NPU that sits idle while the GPU composes the desktop, runs the browser and, increasingly, runs local models,” notes the npu-driver readme file. “The question this project asks is narrow and testable: can the NPU take over desktop composition, end-to-end, without the applications or the compositor knowing?”

![NPU is lazy](https://cdn.mos.cms.futurecdn.net/dhR3fbhSxMaMD2VYWpUZ65-1200-80.jpg)

Thankfully, the answer to the question about whether the NPU can render the Windows 11 desktop - and apps like Notepad and Edge windows - is a yes. The npu-driver functions as intended and as demonstrated. Moreover, it seamlessly switches back to GPU rendering if/when it needs to.

The developer admits that this driver is strictly “a research prototype, not a product” at this stage, and the main issue currently is performance. The GitHub readme notes that the target 30 Hz performance isn’t very close right now, with actual screen refresh speeds of around 2 to 3 Hz. npu-driver is being developed on a Panther Lake laptop, and all these Intel processors feature NPU 5 architecture silicon with performance spanning 45-50 TOPS.

A Reddit post that appears to be penned by one of the labscommunity crew says that this project might render Windows 11 visuals rather slowly, but it can “bring 3D GPU usage down from 3.4% to 0.6%,” thus freeing up the GPU for other tasks, like inference.

Having a(nother) useful task for the system NPU to do is a welcome development, even if it seems of rather niche appeal for now. There are no signs consumer processors will abandon NPU integration, and these accelerators will likely remain alongside other now-essentials like hardware for video (de)coding, DSPs, and so on, even if the Copilot+ PC branding exercise has been abandoned by Microsoft and its partners.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR-140-80.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

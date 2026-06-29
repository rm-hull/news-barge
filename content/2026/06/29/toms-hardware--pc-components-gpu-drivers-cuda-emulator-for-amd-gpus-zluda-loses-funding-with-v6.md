---
title: CUDA emulator for AMD GPUs Zluda loses funding with v6 release — embattled
  project goes back to hobby status but now includes 32-bit PhysX support
source_url: https://www.tomshardware.com/pc-components/gpu-drivers/cuda-emulator-for-amd-gpus-zluda-loses-funding-with-v6-release-embattled-project-goes-back-to-hobby-status-but-now-includes-32-bit-physx-support
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-06-29T21:57:42Z'
published: '2026-06-29T00:00:00Z'
description: The latest release will be welcome news for retro gaming fans.
image: https://cdn.mos.cms.futurecdn.net/XCxGXQPUTqQ7sr5bD4otmL-2048-80.png
---

![Graphics card installed in PC](https://cdn.mos.cms.futurecdn.net/XCxGXQPUTqQ7sr5bD4otmL.png) 

There's bittersweet news from the shore of the open-source Zluda project, a long-running effort to create a CUDA emulator for AMD GPUs. The project's latest blog post for version 6 shows off the fresh 32-bit PhysX support and improved Windows support. Additionally, there are a number of PyTorch-driven fixes. Unfortunately, the project has again lost commercial funding, and it's now back to being a hobby for developer Andrez Janik.

 ![Asus RTX 5080 Noctua Edition](https://cdn.mos.cms.futurecdn.net/Wh9EZgD8NG9yUioNNgPB3d.png) 


Zluda 6's 32-bit PhysX support is still in a pre-alpha stage, but the results are promising. Janik showed off multiple cloth and deformation demos running at speed, and even a screenshot showing a 3x performance uplift of 2010's *Mafia II* running with PhysX effects turned on. Given the pre-alpha nature, Janik notes that "fluid simulations can be glitchy, and the current method of loading ZLUDA into Steam games is poor." One of his goals is to have better support for Windows, and v6 includes a refreshed zluda.exe loader that now loads required performance libraries automatically.

Last but by no means least, Zluda v6 includes a host of PyTorch-driven enhancements, composed of compiler fixes and improvements to performance libraries. As a silver lining of sorts, Janik notes that since there's now no funding, the priorities for the project have shifted to things "[he] finds the most entertaining," justifying the addition of PhysX and the revamped Windows loader.

The project was initially started in 2020 to get CUDA running on Intel hardware, but has since then turned to AMD cards. After being abandoned in 2021, it was brought back from the dead around 2022 thanks to AMD pulling out the checkbook to make it happen — presumably because one of the main obstacles (if not the primary one) is that most all the AI software ecosystem revolves around Nvidia's GPUs.

Unfortunately, AMD also cut the funding to Zluda in 2024, and in August even forced Janik to rebuild the code the company paid for. He thankfully found an undisclosed sponsor in late 2024; likely an AI company to whom the translation layer would be valuable, letting them run CUDA AI workloads on Instinct cards. Said funding is now sadly gone once again, and Janik says Zluda is back to being a "weekend project."

For end users, it's nice to have a fully open-source drop-in replacement for CUDA binaries. As for large-scale conversion for AI usage, though, there are a number of alternative projects that look to accomplish the same end results via different means. These include AMD's HIP source code porting, Spectral Compute's Scale, and MooreThreads' Musify toolkit, to name a few.

  


*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

- 
Reply
 Not quite yet, but that is likely the future, but more likely with human direction, supervision and involvement. Grok is also a good fit for at least some parts of this project as it has unique skills at optimizing some things this project uses. It will probably be quite some time before AI can completely replace humans on large complex projects like this and even then humans will most likely have unique skills at pushing projects to the maturity that other humans expect.Scott_Tx said:Claude Fable, write me a cuda replacement that runs on AMD cards and make it snappy!
 
 Open source and Linux as a whole has gained more momentum and as the user base grows so does the pool of people needed to support it. That and when AI replaces developers they won't have anything better to do than help develop free software because they can't afford to buy it anymore. The last part is a joke, I hope. ;)
- 
Reply
 Linux has actually lost market share this quarter lol. It's a pain to setup, one wrong update can ruin everything. Windows isn't going anywhereZaranthos said:Not quite yet, but that is likely the future, but more likely with human direction, supervision and involvement. Grok is also a good fit for at least some parts of this project as it has unique skills at optimizing some things this project uses. It will probably be quite some time before AI can completely replace humans on large complex projects like this and even then humans will most likely have unique skills at pushing projects to the maturity that other humans expect.
 
 Open source and Linux as a whole has gained more momentum and as the user base grows so does the pool of people needed to support it. That and when AI replaces developers they won't have anything better to do than help develop free software because they can't afford to buy it anymore. The last part is a joke, I hope. ;)
- 
Reply
 Windows can also brick computers and generally make things worse with updates.upsetkiller said:Linux has actually lost market share this quarter lol. It's a pain to setup, one wrong update can ruin everything. Windows isn't going anywhere
 
 I think you're alluding to Linux dependency hell and other packaging related problems though.

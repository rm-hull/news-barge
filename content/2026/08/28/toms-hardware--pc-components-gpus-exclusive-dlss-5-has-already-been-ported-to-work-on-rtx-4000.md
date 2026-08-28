---
title: DLSS 5 has already been ported to work on RTX 4000 Series graphics cards —
  incompatible CUDA instructions get patched to work on previous-gen hardware
source_url: https://www.tomshardware.com/pc-components/gpus/exclusive-dlss-5-has-already-been-ported-to-work-on-rtx-4000-series-graphics-cards-incompatible-cuda-instructions-get-patched-to-work-on-previous-gen-hardware
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-28T22:14:52Z'
published: '2026-08-28T00:00:00Z'
description: DLSS 5 support broadens thanks to modder.
image: https://cdn.mos.cms.futurecdn.net/XWFApR3UjpmFwiQ2t7DdNV-2560-80.png
---

![Control Running DLSS 5 on RTX 4080 Super](https://cdn.mos.cms.futurecdn.net/XWFApR3UjpmFwiQ2t7DdNV.png) 

*Tom's Hardware* has verified that modders have managed to get DLSS 5 up and running on RTX 4000 series graphics cards, following the leaked release of the DLSS 5 nvngx_dlssnr.dll yesterday, which saw modders flock to integrate it into other titles outside of Remedy Entertainment's Control.

Yesterday, modders managed to get Nvidia's DLSS 5 running inside Control, and now in other titles. The early access version of NBA 2K27 contained a new file enabling the Neural Rendering technique, and has since been ported to other games.

The RenoDX Discord server has been the center of action for all of the development of getting this early version of Neural Rendering to function on other pieces of software. The modification leverages both ReShade and RenoDX to essentially activate the additional files.

![Nvidia Dlss 5 NR Ada Lovelace patch - YouTube](https://img.youtube.com/vi/HxRFihnFQ4A/maxresdefault.jpg) 

While it's clearly an early look at the technology, one limitation of the current binary available has been that it only works with RTX 5000 Series Blackwell GPUs. This is even though the AI model contained within the DLL runs on FP8, which can be read and executed on previous-gen Ada Lovelace hardware. The reason behind the incompatibility (as *TechPowerUp* explained) is that certain CUDA binaries can only be read by Blackwell GPUs.

However, intrepid RTX Remix modder "Uncle Burrito" has since patched the DLL file to get things working on Ada Lovelace hardware. "All I had to do was look into it to see what binaries it's actually using. Find the ones that aren't compatible with Ada, and then patch in fresh ones myself," the modder told *Tom's Hardware*. They continued to share that, since the nvngx_dlssnr.dll for NBA 2K27 was likely an early development build, Ada-equivalent binaries had likely not been built for it.

*Tom's Hardware* has verified that Uncle Burrito's patch works when using an Nvidia RTX 4080, and that multiple versions of such a patch are in the works from other developers within the RenoDX Discord server.

Currently, official DLSS 5 support on non-Blackwell hardware remains a question mark, though after seeing the work that modders have done to get things up and running on previous-generation hardware, Nvidia may choose to release it for previous-generation GPUs. Support for Ampere GPUs and older may pose a significant challenge, however, as the hardware does not have native FP8 support.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Sayem Ahmed](https://cdn.mos.cms.futurecdn.net/xsPCakGobuUWmyECbrEM2T.jpg)

Sayem Ahmed is the Subscription Editor at Tom's Hardware. He covers a broad range of deep dives into hardware, both new and old, including the CPUs, GPUs, and everything else that uses a semiconductor. He has worked as a professional tech journalist since 2015 and has written for Gamespot, IGN, and Dexerto.

- 
Reply
Exactly because that would go counter to their engineered obsolescence.thisisaname said:Just because it can be made to run on a RTX 4000 does not mean Nvidia will make any effort to support it on a TRX 4000 GPU.

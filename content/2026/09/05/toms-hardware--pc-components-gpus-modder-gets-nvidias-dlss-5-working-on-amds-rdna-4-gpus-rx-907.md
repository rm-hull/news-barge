---
title: Modder gets Nvidia's DLSS 5 working on AMD's RDNA 4 GPUs — RX 9070 XT only
  manages 30 FPS at 1080p right now, but 5070 Ti-level performance is the eventual
  goal
source_url: https://www.tomshardware.com/pc-components/gpus/modder-gets-nvidias-dlss-5-working-on-amds-rdna-4-gpus-rx-9070-xt-only-manages-30-fps-at-1080p-right-now-but-5070-ti-level-performance-is-the-eventual-goal
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-05T15:06:57Z'
published: '2026-09-05T00:00:00Z'
description: The game must already support FSR.
image: https://cdn.mos.cms.futurecdn.net/A5B8BfAZTyVWEpy5TRr3UY-2560-80.jpg
---

![Nvidia DLSS 5](https://cdn.mos.cms.futurecdn.net/A5B8BfAZTyVWEpy5TRr3UY.jpg) 

DLSS 5 officially debuted inside NBA 2K27 yesterday with more games to follow down the line, along with RTX 40-series support planned for the future. However, if you don't own a GPU from either of those families, the modding community has once again stepped up to offer a workaround. Developer *danielblnc* has figured out a way to make DLSS 5 work on AMD's RDNA 4 GPUs (RX 9000 series). As long as you're playing a DirectX 12 game with FSR support, "DLSS-NR-on-AMD" can inject DLSS 5 inside it.

The project is closed-source, so we don't know exactly how it works but we can make a few educated guesses. The mod is likely using a dynamic wrapper to intercept NGX API calls and fool the DLSS 5 DLL into loading on an AMD GPU. Once loaded, it extracts the AI model and Tensor data inside that DLL and converts those calculations into math AMD's matrix accelerators can understand via the HIP RT backend (rather than translating CUDA).

It then hooks into the game's FSR pipeline to run that frame data through the neural model and produce the same quality results you would get on an actual RTX 50-series GPU, just without any of the Tensor cores. DLSS-NR-on-AMD doesn't work on any game requiring anti-cheat. Even in single-player titles the performance is not great, especially since the RX 9070 XT is the top-end RDNA 4 GPU available.

Initially, Cyberpunk 2077 was running at 28 FPS at 1080p on the 9070 XT with DLSS 5 on, but a patch has been released that improves the frame rate by 12% to a stable 30 FPS. Another update has added a 2% boost but that's likely negligible. Performance reports from users online are a bit less optimistic. The ultimate goal is to get performance similar to an RTX 5070 Ti, which is not far-fetched since both GPUs are matched in raster and very close in ray tracing.

 ![Cyberpunk 2077 running with DLSS 5 on an AMD RX 9070 XT](https://cdn.mos.cms.futurecdn.net/wKRC28bDz997jEGRsGUZSd.png) 


If you want to try it yourself, just head on over to the GitHub page and grab the latest release (it's an executable). Inside, you won't find the DLSS 5 DLL; you have to provide a "legally-obtained" copy yourself, as the repo points out. Currently, only NBA 2K27 natively supports DLSS 5 and that's where the DLL was originally leaked from. Anyways, once you have it, move the DLL and the executable inside the game's bin folder. Follow the on-screen instructions to finish installation.

Open the game, select FSR 3 or 4 from the in-game graphics settings, and press the End key to bring up the custom menu. This menu allows you to adjust individual parameters like structure and tone, similar to how the ReShade mod works in other games. You see the changes in real-time and it looks just as "good" as the non-intercepted DLSS 5. Don't expect any miracles because DLSS 5 is already very compute heavy and you're adding extra overhead by running it on non-compatible hardware.

Sure, both the RTX 50-series and the RX 9000 series support FP8 formats but DLSS 5 is meant to run on Tensor cores; not AMD's dual-issue AI accelerators. However, since the RTX 40-series also has Tensor cores and native FP8 support, Nvidia has confirmed that DLSS 5 will eventually make its way onto last-gen silicon as well. As for DLSS-NR-on-AMD, users have been able to get it running on RX 7000 series, but performance is once again abysmal because of the lack of FP8 support.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The GitHub repo does mention RDNA 3 support being explored but there are no plans for it at the moment. There is a lot of work to be done just to get the RX 9070 XT performance on the level of the 5070 Ti first. Ultimately, the ambition of the modding community never fails to impress because this is the slowest DLSS 5 on RDNA 4 will ever be. Nvidia's efforts to optimize DLSS 5 on its own hardware will, inadvertently, improve this mod as well as time goes on.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg) 

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

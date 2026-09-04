---
title: Nvidia app update fails to block unofficial DLSS multi-frame generation mod
  on RTX 40 series gaming GPUs — modders restore support across multiple games within
  hours
source_url: https://www.tomshardware.com/video-games/pc-gaming/nvidia-app-update-fails-to-block-unofficial-dlss-multi-frame-generation-on-rtx-40-series-modders-restore-support-across-multiple-games-within-hours
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-04T18:58:50Z'
published: '2026-09-04T00:00:00Z'
description: Enterprising game modders have found ways to enable NVIDIA's own DLSS-G
  pipeline intended for Blackwell on Ada Lovelace.
image: https://cdn.mos.cms.futurecdn.net/uWtej5aJNqQwbgnjf5BLDM-1920-80.jpg
---

![An NVIDIA slide showing the benefits of DLSS 4 multi frame generation.](https://cdn.mos.cms.futurecdn.net/uWtej5aJNqQwbgnjf5BLDM.jpg) 

When NVIDIA launched the GeForce RTX 50 series, a major part of the hype surrounding the new GPU family was its support for DLSS Multi-Frame Generation. This feature was officially locked to the new RTX 50 "Blackwell" GPUs, but modders have been working on unlocking it for RTX 40-series cards for a while now. NVIDIA is clearly aware of these efforts, as it recently pushed an over-the-air update via the NVIDIA App that seemed targeted at blocking them due to its odd changes. Yet, as pointed out by Sebastian Castellanos on X, enterprising hackers had already found a workaround just hours later.

At the launch of Blackwell, NVIDIA explained that bringing Multi-Frame Generation to previous-generation RTX 40-series cards wasn't possible because those GPUs relied on a hardware optical flow generator incapable of producing multiple interpolated frames per rendered frame. Instead, Blackwell introduced a software-based optical flow method executed directly on the GPU shader cores without requiring the hardware unit. To tech-savvy gamers, the obvious question arose: why not use that same software method on Ada Lovelace GPUs and bypass their hardware optical flow units? NVIDIA showed no interest in enabling this, leading many to assume it was technically impossible.

I uploaded a video on how to enable DLSS Multi-Frame Generation on my RTX 4060 GPU.I tested RE9 and Forza Horizon 6. To be honest apart from the oblivious latency increase, it works extremely well!Thanks to @Sebasti66855537 for notifying me about this mod!Video linked below pic.twitter.com/Tldr9JZIxJSeptember 4, 2026


Put simply, it's possible. There are apparently various roadblocks within NVIDIA's software, but the strength of the PC platform lies in its openness; users can freely modify software running on their own hardware. And so, at least three distinct mods have emerged to unlock DLSS Multi-Frame Generation across multiple titles. It began with a *Cyberpunk 2077* mod by creator "dashdogy" that relied on game-specific modding frameworks, but the technique has since been adapted into a broader ReShade plugin applicable to almost any game, and that's just one of at least three different multi-game unlock mods I found.

It's obviously in the company's best interest to protect its marketing narrative, and the narrative is that Multi-Frame Generation doesn't work on GeForce RTX 40 series graphics cards. However, user reports across X and Reddit tell a different story. Users report that the mods not only work, but also deliver surprisingly smooth frame pacing. NVIDIA had previously warned that Blackwell's specialized hardware flip metering was mandatory for proper frame pacing with multi-frame generation, but dashdogy noted that his mod backports "Blackwell-specific frame timing instructions to allow Ada to place the frames in the correct positions," suggesting that MFG's purported hardware dependency was greatly exaggerated.

 ![A screenshot of the MFGAdaUnlock-RenoDx GitHub project showing the patch notes for Release 0.4.](https://cdn.mos.cms.futurecdn.net/CntksbppNk6RFaVQwVJ6vM.png) 


Earlier attempts to enable multi-frame generation on Ada Lovelace relied on GPU spoofing or hybrid solutions, like combining standard 2x DLSS Frame Generation with AMD's FSR 3 or Lossless Scaling's software frame generation. Those workarounds were significantly clunkier than native game mods that utilize NVIDIA's own DLSS-G framework. While I couldn't get this latest mod working in the limited time before publication, community developers have not only bypassed the latest roadblocks thrown up by Mean Green, but in fact, they've released at least two more updates for the mod in the last ten hours since Castellanos' X post.

All of this coincides rather neatly with the contentious rollout of DLSS 5 "Neural Rendering," which is another technology originally pitched as an RTX 50-series exclusive before NVIDIA made a last-minute reversal to promise it for RTX 40-series cards as well. That shift may well have been driven by hackers porting DLSS 5 Neural Rendering not just to older NVIDIA architectures, but even to AMD Radeon GPUs. Once it became common knowledge that DLSS 5 runs on non-Blackwell hardware, continuing to claim hardware exclusivity risked a major loss of consumer trust. It'll be fascinating to see if NVIDIA will pivot on DLSS Multi-Frame Generation in the same way. While it would be a nice bone to throw the company's loyal previous-generation customers, we wouldn't bet on it.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi.jpg) 

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

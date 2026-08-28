---
title: Modders get leaked DLSS 5 running in Control — early Blackwell test drops RTX
  5070 Ti from 71 to 35 FPS at 4K
source_url: https://www.tomshardware.com/pc-components/gpus/modders-get-leaked-dlss-5-running-in-control-early-blackwell-test-drops-rtx-5070-ti-from-71-to-35-fps-at-4k
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-28T11:16:03Z'
published: '2026-08-28T00:00:00Z'
description: There she blows.
image: https://cdn.mos.cms.futurecdn.net/aRSiWBgcRxFsTpt9SXgjRd-1429-80.jpg
---

![Nvidia DLSS 5](https://cdn.mos.cms.futurecdn.net/aRSiWBgcRxFsTpt9SXgjRd.jpg) 

DLSS 5 has apparently leaked, originating from inside a new game. This week, Renan Maniero discovered that NBA 2K27, which has entered early access, contains a new Nvidia library called nvngx_dlssnr.dll. The file, named Nvidia DLSSNR, appears to be associated with Nvidia’s DLSS 5 neural rendering technology, suggesting that NBA 2K27 will be among the first games to support it. Developers were quickly able to get DLSS 5 running in Control.

DLSS 5 is Nvidia’s upcoming neural rendering technology, first introduced in March of this year, which received a mixed reception from the gaming community. Nvidia announced that the technology would launch this fall, meaning its release is now fast approaching.

Eita, o acesso antecipado do jogo NBA 2K27 veio com uma DLL nova do DLSS. DLSS-NR (Neural Rendering) 👀 pic.twitter.com/X15fYO92RUAugust 26, 2026


One of the developers behind RenoDX, a popular toolset for modding games, has been working to get DLSS 5 running in an actual game using the aforementioned DLSS 5 library. The developer successfully got the technology working in Control and applied it to the game's character models.

🚨DLSS 5 Running On Control with renodxso one of the renodx guys has dlss 5 neural rendering (ai filter) running on control. This was using the dlss nr dll found in nba 2k27. They have it working on character models only so far. Theres 7 different styles, the video clip… pic.twitter.com/YlEFVCIPJCAugust 27, 2026


You can expand the tweet above to see DLSS 5 in action, with seven sliders controlling parameters such as style, intensity, tone, and structure strength.

According to the developer on the RenoDX Discord server, DLSS 5 currently runs only on Blackwell GPUs. On an RTX 5070 Ti at 4K, enabling the technology reportedly reduced performance from 71 FPS to 35 FPS. However, the developer did not specify the DLSS 5 settings or the internal rendering resolution used for the test, so it is not yet clear how representative this performance impact is.

It is important to remember that this is an early implementation of DLSS 5 injected into a game by modders. Therefore, it should not be taken as confirmation that Blackwell GPUs will be the only hardware supported at launch, nor should the performance shown here be considered representative of the final release.

That said, the performance impact is not entirely unexpected. When Nvidia first demonstrated DLSS 5 in March, the demo was running on two RTX 5090s. Since then, the model has been distilled into a smaller and more efficient version capable of running on a single GPU, according to Nvidia’s presentation at SIGGRAPH 2026. Nvidia may still have additional optimizations to implement ahead of the official launch, but we still expect DLSS 5 to be demanding to run in practice.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

In terms of image quality, a user provided a couple of comparisons in the RenoDX Discord server we linked to previously.

In Nvidia’s initial reveal in March, many of the comparison shots demonstrated substantial improvements to effects such as subsurface scattering, contact shadows, light transmission through hair and foliage, and overall lighting. However, there were occasional instances where the neural rendering model deviated significantly from the intended artistic direction. At SIGGRAPH 2026, this no longer appeared to be an issue. The same appears to be true in the Control screenshots, where improved shadows and light transmission through the characters’ hair and skin make the scenes appear more photorealistic without altering the underlying geometry or the game's overall look.

DLSS 5 is set to launch soon, and while what we have seen today is only an early glimpse of the technology, it has certainly left us intrigued. Even in this early implementation, the improvements in lighting, shadows, and material rendering are impressive, particularly given that they can enhance a scene's visual fidelity without altering its underlying geometry or artistic style. Of course, the real test will come with the official release, where we will get a better idea of its image quality, performance requirements, and hardware compatibility. For now, however, DLSS 5 is shaping up to be a fascinating addition to Nvidia’s suite of neural rendering technologies.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Dan Mateescu](https://cdn.mos.cms.futurecdn.net/ExmVPaYL2qmyNWzwnGHxKQ.jpg)

Dan Mateescu is a PC enthusiast with many years of experience benchmarking PC hardware. In 2021, he started his own YouTube channel called 'Compusemble' where he benchmarks hardware in video games and the latest tech demos.

- 
I'm thinking that despite the initial anger, it's here to stay. So now AMD needs their own slop filter.Reply
 
 The uncanniness of it depends on the settings and what it has to work with.
 
The performance drop is not always so dramatic. Someone on VideoCardz got it working with Cyberpunk and only reported a 25% drop (from 200+ FPS to 150+ FPS on 5090).

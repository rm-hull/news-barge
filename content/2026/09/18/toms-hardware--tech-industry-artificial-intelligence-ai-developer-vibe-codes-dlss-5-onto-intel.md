---
title: AI developer vibe codes DLSS 5 onto Intel CPU's integrated graphics — Intel
  Arc 140T runs neural rendering in 360p at 10 frames per second
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-developer-vibe-codes-dlss-5-onto-intel-arc-140t-integrated-graphics-run-neural-rendering-in-360p-at-10-frames-per-second
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-18T19:01:20Z'
published: '2026-09-18T00:00:00Z'
description: You won't be playing any games with DLSS 5 on integrated GPUs, but it
  might be fun to use with photo modes.
image: https://cdn.mos.cms.futurecdn.net/jyBsQv3HMAD6GKyN3aksrV-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
---

![A before/after comparison of Tekken 7's Sergei Dragunov with DLSS 5 Neural Rendering.](https://cdn.mos.cms.futurecdn.net/jyBsQv3HMAD6GKyN3aksrV.jpg) 

A new project on GitHub, simply titled "dlss-nr-on-intel", purports to provide exactly that: a port of NVIDIA's DLSS 5 Neural Rendering to Intel's Xe architecture. Specifically, the author (who goes by "Uzbekunknown") focused on porting the technology to the Intel Arc 140V graphics in his Lunar Lake system, and they seem to have succeeded, at least insofar as he's getting outputs that look reasonably like those of DLSS 5 on other hardware.

AI is at the center of this project, beyond the DLSS 5 neural rendering technique itself. Uzbekunknown credits Anthropic's Claude as well as OpenAI's GPT-6 Astra with the code and says that they "supplied the machine, the binary, and the direction, and made the decisions", while the AI agents did everything else. Amusingly, they note that "the wrong turns are in the notes, too, deliberately," including a hallucinated driver bug that does not exist and shaped three phases of development.

The end result, rather than being a wrapper around the DLSS 5 DLL as many other hacks have been, fully reimplements the 71-block U-Net that DLSS 5 uses and then runs it on the Intel Xe XMX units through a Vulkan extension called VK_KHR_cooperative_matrix. It's entirely run in FP16 with FP32 accumulate, because Xe2 doesn't support FP8. You can run the model on anything presenting its output through Vulkan, and the user presents proof-of-concept results from three fighting games: *Dead or Alive 5 Last Round*,* Tekken 7*, and* Mortal Kombat 1*.

 ![A before/after comparison of DLSS 5 on Dead or Alive 5 Last Round.](https://cdn.mos.cms.futurecdn.net/u9jrC5UXjs8W28UHFsxpH.jpg) 


It's not fast. Running the ten-year-old *Tekken 7* in 640x360 resolution (1/9 of FHD) should be a trivial task for the potent Intel Arc 140V graphics, yet it apparently struggles at around 10.5 FPS with this model loaded. Note (as the author does) that the performance of DLSS 5 depends almost entirely on the game's output resolution, so running in hilariously low resolutions is required to try and achieve anything approaching a real-time frame rate on this limited hardware with this inefficient approach; apparently the DLSS 5 pass by itself takes some 412 milliseconds in full HD on the Arc 140V, which means that even if your game renders instantaneously, your maximum frame rate would still be around 2.4 FPS.

Still, it does appear to work, and that's the impressive part. I'm not sure I completely agree with the author's analysis of the effects on the three games he tested; he says that *Mortal Kombat 1* loses detail in the DLSS 5 output, and while that may be statistically true, visually it does look more detailed to my eye. The DLSS 5 NR model is known to be specifically trained to produce a photorealistic look, and this has good effects on*Mortal Kombat* and*Tekken*, but not as much on* Dead or Alive*, which is more stylized to give an anime look; the model instead makes the character look older and less appealing.

 ![Two screenshot comparisons of Mortal Kombat 1 characters with DLSS 5 on/off.](https://cdn.mos.cms.futurecdn.net/9XgGoQnKk7su7tCYbhkCKB.jpg) 


As the author notes, this is more of a proof of concept than something you would actually want to use. However, there are efforts to get the work ported to both discrete Arc GPUs as well as AMD cards. AMD's RDNA 4 graphics already supports FP8, so you'd want to use the original model there, but this could allow RDNA 3 and Xe2 graphics cards to use DLSS 5. While it would almost assuredly be too slow for gameplay, it might be interesting for photo modes since you can toggle the function with a keystroke.

The project currently requires Linux, which is going to invalidate it for the majority of our audience, but as a user on Reddit, /u/arielcasari, says that they intend to "adapt it to run on Windows" and that they will post the results on the /r/IntelArc subreddit. If you're interested in fooling around with it yourself, head over to the developer's GitHub and make sure to read over the Readme.MD, as the project exposes all of Nvidia's own DLSS 5 controls, and you'll need to be familiar with them to get anything approaching decent results.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi.jpg) 

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

- 
When journalists embed opinions into reporting and sell them as facts (such as saying "it also changes her look considerably, clashing with the visual style of the game" under the image), it really devalues the piece and erodes trust in the publication, as well as helps feed the cycle of sensationalized misinformation. A good journalist reports facts, and let's the readers form their own opinions.Reply
 
 Just a thought.
 
Otherwise, interesting article.

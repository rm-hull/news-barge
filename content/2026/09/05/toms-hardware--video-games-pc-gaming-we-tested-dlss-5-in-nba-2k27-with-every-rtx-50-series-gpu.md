---
title: We tested DLSS 5 in NBA 2K27 with every RTX 50-series GPU — first official
  release comes with a big performance hit, but almost every Blackwell card can run
  it at 1080p
source_url: https://www.tomshardware.com/video-games/pc-gaming/we-tested-dlss-5-in-nba-2k27-with-every-rtx-50-series-gpu-first-official-release-comes-with-a-big-performance-hit-but-almost-every-blackwell-card-can-run-it-at-1080p
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-05T11:49:35Z'
published: '2026-09-05T00:00:00Z'
description: Once you see it, you won't want to turn it off, even with the frame rate
  hit.
image: https://cdn.mos.cms.futurecdn.net/peEtJE98WLRCbHo2PH4CQF-1920-80.jpg
---

![NBA 2K27 gameplay](https://cdn.mos.cms.futurecdn.net/peEtJE98WLRCbHo2PH4CQF.jpg) 

Nvidia's DLSS 5 has arrived in *NBA 2K27*, and we've been up since midnight testing it across every RTX 50-series graphics card to see what the first official implementation of this tech can do and how it compares to the community-implemented mods that have been circulating over the past couple weeks.

Before we discuss the performance cost of DLSS 5, many will ask whether this tech is even worth getting excited about, given the intense controversy that it's sparked ever since Nvidia revealed it earlier this year.

In short: yes, absolutely.

This first-party implementation of DLSS 5, tuned under the full control of 2K Games' art directors and artists, looks incredible, full stop. If you see it running, you will want to leave it on. It doesn't look like "slop" or a cheap filter. It just looks *correct*, or at least more correct.

![NBA 2K27 DLSS 5](https://cdn.mos.cms.futurecdn.net/D5d2hZEJj32qFQNHzmqTvf-1200-80.jpg) 

![NBA 2K27 DLSS 5](https://cdn.mos.cms.futurecdn.net/5hJeDM2KvgdkP88oUtS9uf-1200-80.jpg) 

![NBA 2K27 DLSS 5](https://cdn.mos.cms.futurecdn.net/D5d2hZEJj32qFQNHzmqTvf-1280-80.jpg) 

![NBA 2K27 DLSS 5](https://cdn.mos.cms.futurecdn.net/5hJeDM2KvgdkP88oUtS9uf-1280-80.jpg) 

For just a couple of examples, without DLSS 5, even at ultra settings and with RT, the game has a slightly "plastic" or "flat" look. Faces can have a waxy uniformity that immediately indicates that you're looking at a video game, not a live broadcast. Hair looks totally and unnaturally flat. The whites of eyes can be unnaturally bright, giving a sort of googly-eye or doll-like effect that immediately broke my sense of immersion. I didn't think any of this would be a big deal for a sports game, but it all stands out.

![NBA 2K27 DLSS 5 comparisons](https://cdn.mos.cms.futurecdn.net/r4bbvZqKoQ6CyDjadTX6Mo-1200-80.jpg) 

![NBA 2K27 DLSS 5 comparisons](https://cdn.mos.cms.futurecdn.net/gn2zFMMSYEYN8NR6M4eYKo-1200-80.jpg) 

![NBA 2K27 DLSS 5 comparisons](https://cdn.mos.cms.futurecdn.net/r4bbvZqKoQ6CyDjadTX6Mo-1280-80.jpg) 

![NBA 2K27 DLSS 5 comparisons](https://cdn.mos.cms.futurecdn.net/gn2zFMMSYEYN8NR6M4eYKo-1280-80.jpg) 

DLSS 5 breathes incredible life into *NBA 2K27*. Skin looks like real flesh and blood. Eyes are rendered with the proper tones, depth, and sparkle. Hair looks a billion times more realistic. Every human on screen just looks more* alive.* You won't entirely forget that you're looking at a game, but it becomes much easier to suspend disbelief and get lost in the action.

My experience slapping DLSS 5 mods into games has produced promising but sometimes mixed results. If the polished experience that *NBA 2K25* delivers is any indication, I can't wait for more studios to get their hands on it and integrate it into their games under the care of the same artists that created them.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

### Our testing methods

We did our best to deliver clean test numbers in the short time we've had with *NBA 2K27.* Performance in this can be tricky to measure. Benchmarking in the hub worlds or cutscenes will deliver lower performance than on the court, and even then, in-game events like fouls and time-outs will also result in skewed numbers if you're not careful. We picked a repeatable match-up from the game's career mode and sampled 60 seconds of continuous gameplay with DLSS 5 on and off, making sure to restart if we ran into any of the scripted events above.

We used *NBA 2K27*'s maximum graphics settings as our baseline, including RT. We tested at native resolutions without upscaling, and we didn't test with Multi Frame Generation enabled. We view MFG as a cherry on top of an already solid baseline experience, not a baseline in itself.

Our test system is built with the following components:

| Tom's Hardware 2026 GPU Test System |  | 
|---|---|
| **CPU** | AMD Ryzen 7 9800X3D | 
| **CPU Cooler** | Thermalright Phantom Spirit 120SE | 
| **Memory** | 32GB (2x16GB) G.Skill Trident Z5 Neo DDR5-6000 CL30 | 
| **Motherboard**  | Asus TUF Gaming X670E-Plus Wifi | 
| **Storage** | Inland Performance Plus 4TB PCIe 4.0 NVMe SSD | 
| **Power supply** | MSI MPG Ai1600TS 1600W | 
| **Operating system** | Windows 11 Pro | 
| **Graphics driver version** | GeForce Game Ready 616.64 | 

All of our performance results are captured using Nvidia's FrameView 2.0 utility. We measure graphics card power consumption directly with Nvidia's PCAT hardware power logging tool.

If you have any questions about our testing methods, let us know in the comments and we'll do our best to answer them. On to the numbers.

### NBA 2K27 1080p performance

 ![DLSS 5 performance](https://cdn.mos.cms.futurecdn.net/PrQfmkMLYvzdJZzEWonXtQ.png) 


At 1080p, everything from the RTX 5070 on up is CPU-bound without DLSS 5 enabled, even with maxed-out settings and RT on. Turn on DLSS 5, though, and the differences in Tensor Core compute across the cards quickly becomes obvious. But even the RTX 5060 can manage nearly 60 FPS on average with DLSS 5 enabled at 1080p, so almost anybody with a Blackwell card can at least try out the feature.

Given these results, you might think to enable DLSS Super Resolution (aka upscaling). But because the amount of time needed to run the DLSS 5 model has a fixed cost per output frame that scales with your target resolution and largely dominates the total frame time, especially on lower-end hardware, you may find that enabling DLSS SR doesn't have as much of an effect on performance as we've come to expect. The game still has to wait for that final generative step to occur, even if DLSS SR cuts down some of the total frame time.

As noted, we didn't use MFG for these tests, simply because there's no need for us to make the numbers on these charts artifically large. If you do want to enable it, the multiplier you want will be determined by your monitor's refresh rate and your own personal tastes.

 ![DLSS 5 performance](https://cdn.mos.cms.futurecdn.net/9pMQGeNCtC6Vt8ec2DA3mQ.png) 


We did chart PC latency as estimated by FrameView, so you can get a sense of whether there's enough of a latency budget to enable MFG at all. At 1080p, every card is a solid candidate for enabling MFG without adding unreasonable amounts of input latency, although the RTX 5050 is in a borderline position. And all three of the 8GB cards might have trouble fitting the MFG model into their VRAM with these maxed-out settings and DLSS 5 enabled, so you might need to turn off RT at a minimum to use MFG on these lower-end GPUs.

 ![DLSS 5 performance](https://cdn.mos.cms.futurecdn.net/p8qG5KZz5MnbMu5BHrSinQ.png) 


As we already saw in early testing of the leaked DLSS 5 builds circulating in the community, enabling the model has a large impact on power consumption, likely due to the intense Tensor Core load required to run the DLSS 5 model.

### NBA 2K27 1440p performance

 ![DLSS 5 performance](https://cdn.mos.cms.futurecdn.net/LSB8znYC8PL6NE2nGp79sQ.png) 


Moving up to 1440p separates our cards some more. The RTX 5080 and RTX 5090 are still CPU-limited without DLSS 5. The RTX 5060 Ti 8GB, RTX 5060, and RTX 5050 all get a "Low VRAM" warning with these settings, so if you're trying to push this higher resolution with those cards, you might want to start tuning your DLSS upscaling settings to relieve VRAM pressure, even if it doesn't result in additional performance with DLSS 5.

 ![DLSS 5 performance](https://cdn.mos.cms.futurecdn.net/Ci43NR3iasnUq2apkjWmoQ.png) 


But you really want an RTX 5060 Ti at a minimum here to get acceptable input latency with DLSS 5 enabled, and the RTX 5070 is the true baseline for a good experience. At the higher end, the RTX 5070 Ti and RTX 5080 both provide fluid frame rates even without MFG, and you have the latency budget to enable framegen without worry on anything from the RTX 5070 on up.

 ![DLSS 5 performance](https://cdn.mos.cms.futurecdn.net/iU67wQ6qVGMQGLzK2hhtpQ.png) 


DLSS 5's power consumption on all these cards (except the chugging RTX 5050) rises as expected with the higher-resolution output frame we're asking it to generate. Everything from the RTX 5060 up to the RTX 5070 Ti ends up running at its power limit, while the RTX 5080 and RTX 5090 still have room to stretch out. The unconstrained MSI RTX 5090 Lighting Z sucks down a ton of power to deliver its scorching performance.

### NBA 2K27 4K performance

 ![DLSS 5 performance](https://cdn.mos.cms.futurecdn.net/88aLgvB7kSPViJgV6Ja3sQ.png) 


Running *NBA 2K27* at 4K with DLSS 5 is extremely demanding, since the model has to generate an output frame with more than twice as many pixels than at 1440p. Even the RTX 5070 Ti is straining here, as its input latency with DLSS 5 is potentially too high to enable MFG while still delivering a responsive gameplay experience.

 ![DLSS 5 performance](https://cdn.mos.cms.futurecdn.net/5UM7nLmarUh9DDx5AzQFrQ.png) 


You can see why Nvidia only recommends the RTX 5080 and RTX 5090 for a 4K DLSS 5 experience in this title, as they're the only two cards that deliver high enough baseline performance with low enough input latencies to make MFG practical. And even then, the RTX 5080 is on the edge of what we'd consider an acceptable input latency before enabling MFG.

 ![DLSS 5 performance](https://cdn.mos.cms.futurecdn.net/hN3y2mQNGK5Lh9LFYoEdrQ.png) 


Our power consumption chart at 4K is a bit of a mess at the low end since the RTX 5050 and RTX 5060 are crushed by the demands of DLSS 5 and end up chugging. Really, though, we're here to see how the RTX 5080 and RTX 5090s handle this incredibly Tensor Core-intensive work. Both cards end up running at their power limits.

The MSI RTX 5090 Lightning Z shows how much power scaling the GB202 GPU has left in it once you remove the constraint of a single 12V-2x6 connector. We were wondering whether the power numbers we saw from a modded version of *Control* were a fluke, but DLSS 5 in*NBA 2K27* goes even harder and pushes the RTX 5090 Lightning Z to nearly 850W on average in this test. For 48% more power than the RTX 5090 Founders Edition, you get 22% higher performance.

On a big 4K screen like an OLED TV, a fluid 90 FPS at a native 4K resolution with the level of detail and realism that DLSS 5 adds is an astounding gaming experience. You really haven't seen anything like it. But mere mortals with single-plug 5090s will probably want to enable MFG 2X at a minimum.

### Bottom line

It's early days for DLSS 5 performance, and in its first official showing in *NBA 2K27*, it certainly has a large performance cost—sometimes well over 50% on lower-end hardware. But the generational leap in realism it provides for every human on screen is well worth it to my eye, at least. Now that I've seen a first-party, developer-driven implementation of DLSS 5, I want it in every game where its photorealistic enhancements would make sense, without question.

And as it's implemented in *NBA 2K27*, our performance results show that the tech is accessible enough that almost anybody with an RTX 50-series graphics card can try it out and still enjoy a fluid and responsive experience, even without Multi Frame Generation. Most of us aren't playing on 4K monitors, and at 1080p and 1440p, the Blackwell card you may already have is probably up to the task of running DLSS 5 with acceptable baseline performance.

DLSS 5 does upend some intuitions we've developed around the interactions of upscaling and frame rate. The large fixed frame-time cost that's required to generate the DLSS 5 output frame is entirely dependent on your target *output* resolution, making the lowered*input* resolution of DLSS 4.5 upscaling far less of a performance multiplier than it might otherwise be.

Given those realities, DLSS MFG can still make for a more fluid experience alongside DLSS 5 with a couple of clicks in a menu—at least assuming you have enough VRAM to hold the game assets, the DLSS 5 model, *and* the MFG model all at once. On 8GB graphics cards, this may require some tweaking to get working.

Nvidia has promised to continue improving the fundamental performance of the DLSS 5 model with time, and the fact that it's moved from requiring a dedicated RTX 5090 to run in the demos we saw at GTC to running on an RTX 5060 today is a sign that such promises do bear fruit.

Boosting the fundamental performance of the DLSS 5 model is vital, because as we all well know, prices for most Blackwell cards have spiked across the board to the point that former midrange options like the RTX 5060 Ti 16GB and RTX 5070 are many hundreds of dollars more expensive than their MSRPs and well out of whack with their former performance-per-dollar propositions. A hardware upgrade to get better performance is no longer a no-brainer for many PC builders, and that problem is going to get even worse as the AI boom continues unabated.

Those elevated prices are also why Nvidia's post-launch pledge to bring the DLSS 5 model to RTX 40-series cards later this year is a welcome development. In our limited experience with community mods, Ada GPUs run the current DLSS 5 model about as well as Blackwell cards do, and gamers who haven't already upgraded from their 40-series cards certainly won't be raring to move off that hardware any time soon. Locking DLSS 5 to new GPUs that are prohibitively expensive to buy for non-technical reasons isn't a winning strategy for goodwill or broad adoption, and it's good to see Nvidia acknowledge that reality.

For all that, we shouldn't lose sight of the fact that DLSS 5 is a huge, exciting leap forward in the never-ending pursuit of photorealism in real-time graphics. When you toggle it on and off in *NBA 2K27*, it feels like a generational improvement in rendering technology at the press of a button. Now that I've seen it in action, I don't want to play* NBA 2K27* without it, and I hope to see more first-party integrations of it soon.

![Jeffrey Kampman](https://cdn.mos.cms.futurecdn.net/8JCjGs5yVZds2YdKmzjUDE.jpg) 

As the Senior Analyst, Graphics at Tom's Hardware, Jeff Kampman covers everything that has to do with graphics cards, gaming performance, and more. From integrated graphics processors to discrete graphics cards to the hyperscale installations powering our AI future, if it's got a GPU in it, Jeff is on it.

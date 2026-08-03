---
title: Gaming on the 4GB Radeon RX 6500 XT and GTX 1650 Super in 2026 — upscaling
  makes low-end GPUs viable for esports and internet cafes
source_url: https://www.tomshardware.com/pc-components/gpus/gaming-on-the-4gb-radeon-rx-6500-xt-and-gtx-1650-super-in-2026
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-03T15:11:30Z'
published: '2026-08-03T00:00:00Z'
description: Does just 4GB of VRAM equal an instant performance cliff?
image: https://cdn.mos.cms.futurecdn.net/JNwrD3iHC3CDUsVzkDayMo-1920-80.jpg
---

![Gaming on the 4GB Radeon RX 6500 XT and GTX 1650 Super in 2026](https://cdn.mos.cms.futurecdn.net/JNwrD3iHC3CDUsVzkDayMo.jpg) 

As memory supplies get tighter and tighter and graphics card prices continue to rise, things are getting weirder and weirder in the discrete GPU market. The latest sign of the times is AMD's launch of the RX 9050 4GB, an OEM-only and region-specific variant of the already limited-release RX 9050 8GB. If 4GB GPUs are coming back, we wanted to see how much gamers should expect to suffer by attempting to play the latest games on graphics cards with such small memory pools.

For reference, the last time AMD launched a new 4GB product was all the way back in 2022 with the RX 6500 XT and the RX 6400. And at least for discrete GPUs, Nvidia got off the 4GB train years earlier, after the launch of the GTX 1650 Super back in 2019. At a minimum, most every discrete GPU since has had 6GB or 8GB of VRAM.

AMD says the existing RX 9050 8GB is meant for 1080p medium gameplay with no further details about settings or upscaling, so the bar is already low for that product before the 9050 4GB cuts both bus width and memory bandwidth in half. Despite its cutting-edge RDNA 4 GPU architecture, the 9050 4GB has a meager 64-bit memory bus and a mere 144 GB/s of memory bandwidth, specs that would have been low-end even 10 years ago.

But the RX 9050 brings support for FSR 4 to even this lowest rung of the discrete graphics ladder, and its more advanced machine-learning-powered upscaling model should deliver a massive leap in image quality compared to the temporal approach of FSR 3 and earlier generations. Upscaling is likely going to be key to achieving playable performance in all but the most lightweight games on 4GB graphics cards.

So, is it totally insane for AMD to release a 4GB graphics card in 2026? Does that tiny VRAM pool make a graphics card useless for gaming? We don't have an RX 9050 4GB at hand, but we do happen to have both an RX 6500 XT and a GTX 1650 Super in the TH GPU library, so we fired up a few popular titles on these cards to see what kind of experience gamers can expect if they’re stuck with just 4GB.

To track GPU memory usage, we used HWiNFO64 and logged both its “GPU D3D Dedicated” and “GPU D3D Dynamic” parameters. If a GPU reports a large dynamic memory allocation, it’s a good sign of spilling out of VRAM, but that’s not an immediate sign that performance is going to fall off a cliff. Different games handle this kind of spillover in different ways, so it’s worth knowing about but not necessarily cause for alarm.

## Fortnite

We started our testing with *Fortnite*, which needs no introduction as one of the most popular PC games out there. While it may have a reputation as a potato game, it can just as easily showcase the most advanced features of Unreal Engine 5.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

*Fortnite* recently started using hardware RT acceleration to enable UE5's flagship Lumen effects, so the RT-Core-less GTX 1650 simply can't run the game with the visual richness we've taken for granted on most every other graphics card we've tested this year.

As a fully DirectX 12 Ultimate-compatible graphics card with RT support, the RX 6500 XT would seem to have an advantage here. And you can certainly run the game with Lumen enabled at medium settings and with XeSS Quality upscaling on the RX 6500 XT despite reported memory usage totaling well over 4GB.

But even though those delivered frame rates might seem acceptable, input latency is not, even with Radeon Anti-Lag enabled. Nvidia’s FrameView utility estimates input latency of 63.9 ms with Lumen on, and that’s too much for a competitive shooter like this. To get input latency down, you have to disable Lumen, and since that makes for an apples-to-apples comparison anyway, that’s how we continued our testing.

 ![Gaming on the 4GB Radeon RX 6500 XT and GTX 1650 Super in 2026](https://cdn.mos.cms.futurecdn.net/xqb43rHzFUNfQwXy6KrLtC.png) 


| Row 0 - Cell 0 | 
 | 
 | 
 | 
| Dedicated | 3917 | 3852 | 3713 | 
| Dynamic | 1254 | 533 | 545 | 
| Total | 5171 | 4385 | 4258 | 

Between medium settings and XeSS Quality upscaling, *Fortnite* ends up being perfectly playable, and reported VRAM usage on both cards hovers just over the 4GB mark.

We have to wonder whether the RX 9050 might be able to run *Fortnite* with Lumen enabled while delivering lower input latency thanks to its more powerful RT accelerators and more modern architecture generally.

## Apex Legends

*Apex Legends* struggled on both the GTX 1650 and RX 6500 XT out of the gate with our usual maxed-out test settings. Dropping back to High reduced the VRAM footprint and resulted in playable frame rates.

 ![Gaming on the 4GB Radeon RX 6500 XT and GTX 1650 Super in 2026](https://cdn.mos.cms.futurecdn.net/rnKHdsBc5HnWszLGLEEguC.png) 


| Row 0 - Cell 0 | RX 6500 XT | GTX 1650 Super | 
| Dedicated | 3465 | 3547 | 
| Dynamic | 299 | 450 | 
| Total | 3764 | 3997 | 

*Apex* doesn’t have any kind of upscaling support, so you’re entirely dependent on its quality settings to boost performance. But we were happy to see that we didn’t have to dial them back much to achieve playability on these cards.

## Cyberpunk 2077

We also called up *Cyberpunk 2077* as an example of a triple-A title that gamers with entry-level PCs might want to run in 2026. We chose 1080p medium settings out of the gate for this game and immediately enabled XeSS 2.0 Balanced upscaling, as even with that dialed-back preset, VRAM usage was already well over 4GB for both cards.

 ![Gaming on the 4GB Radeon RX 6500 XT and GTX 1650 Super in 2026](https://cdn.mos.cms.futurecdn.net/BbPwUQjEW7TdZawmvzXNuC.png) 


| Row 0 - Cell 0 | RX 6500 XT | GTX 1650 Super | 
| Dedicated | 3453 | 3457 | 
| Dynamic | 2439 | 2249 | 
| Total | 5892 | 5706 | 

But even with that massive indicated VRAM spillover, *Cyberpunk*’s performance remained perfectly playable, if not entirely smooth. The crowd density setting had the biggest effect on the immersiveness of the gameplay experience compared to our usual maxed-out test settings. With low crowd density, the sprawling streets of Night City are practically empty. Cranking it back up to High restored the bustle that makes it feel like a lived-in world without totally devastating performance.

## Counter-Strike 2

*Counter-Strike 2* showed the greatest divergence between cards for memory allocation, at least according to the tools we have available. The GTX 1650 reported a total of 3.5 GB of memory used, and the RX 6500 XT showed 4.6 GB.

 ![Gaming on the 4GB Radeon RX 6500 XT and GTX 1650 Super in 2026](https://cdn.mos.cms.futurecdn.net/bp9rGUTNZaT8r8BDFg8ovC.png) 


| Row 0 - Cell 0 | RX 6500 XT | GTX 1650 Super | 
| Dedicated | 3936 | 3266 | 
| Dynamic | 696 | 240 | 
| Total | 4632 | 3506 | 

But that apparent spillover once again doesn’t equal poor performance, as the Radeon handily beats out the 1650 Super here.

## Bottom line

Across the handful of titles we tested, gaming with just 4GB of VRAM isn't the instant performance cliff you might expect in 2026, but it also requires careful finessing of quality and upscaling settings to achieve not just playable performance, but also tolerable input latency. Once you’ve done that, though, it’s possible to have a perfectly fun time on hardware that would make most people turn up their noses at first glance.

Judging by our experience with the RX 6500 XT and GTX 1650 Super, upscaling will be key for the best experience with the RX 9050 4GB, and its support for FSR 4 will be a huge image quality improvement for low-end PCs.

The 9050 also brings much higher RT performance to the table compared to RDNA 2 and RDNA 3 products, and if games as widely played as *Fortnite* are finally starting to lean on RT acceleration to enable their most advanced lighting effects, that’s another useful technical upgrade for enabling the best experience, even on low-end products.

We’re sure that some modern AAA games would be truly unplayable on these 4GB cards, but that’s not the reason they exist. For low-end PCs that are built to run the most popular esports and free-to-play titles, 4GB is still fine, and for markets outside of the United States, especially, products like this are important—just not to enthusiast PC builders.

In that light, the just-released RX 9050 4GB and the higher-end 8GB version are best understood as a much-needed technical update for entry-level OEM systems, much like how we described the RTX 5050 when we reviewed that card last year. If you have the luxury of spending more on a graphics card, you certainly should, but for those renting time in internet cafes and esports centers outside of the USA, low-cost products like the 9050 are an important bridge to the wider world of PC gaming.

![Jeffrey Kampman](https://cdn.mos.cms.futurecdn.net/8JCjGs5yVZds2YdKmzjUDE.jpg)

As the Senior Analyst, Graphics at Tom's Hardware, Jeff Kampman covers everything that has to do with graphics cards, gaming performance, and more. From integrated graphics processors to discrete graphics cards to the hyperscale installations powering our AI future, if it's got a GPU in it, Jeff is on it.

- 
4 GB should also be enough for most PS4-era games. Many great games.Reply
 
 The 9050 also brings much higher RT performance to the table compared to RDNA 2 and RDNA 3 products Is that even true with only 16 ray accelerators?

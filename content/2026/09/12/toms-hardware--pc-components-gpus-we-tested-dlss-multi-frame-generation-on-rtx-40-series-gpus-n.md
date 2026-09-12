---
title: We tested unofficial DLSS Multi Frame Generation support on RTX 40-series GPUs
  — new mod brings RTX 50-series exclusive feature to older cards, and it really works
source_url: https://www.tomshardware.com/pc-components/gpus/we-tested-dlss-multi-frame-generation-on-rtx-40-series-gpus-new-mod-brings-rtx-50-series-exclusive-feature-to-older-cards-and-it-really-works
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-12T15:01:54Z'
published: '2026-09-12T00:00:00Z'
description: But as with any mod, there are caveats
image: https://cdn.mos.cms.futurecdn.net/Fo7xNWht4SGgq8HghfUkRB-2560-80.jpg
---

![Nvidia GeForce RTX 4090](https://cdn.mos.cms.futurecdn.net/Fo7xNWht4SGgq8HghfUkRB.jpg) 

![](https://cdn.mos.cms.futurecdn.net/fsmmX34yhrKZwE44QQk7Qg-200-100.png) 

It’s been a heck of a time lately for PC gamers willing to get their hands dirty with mods. Hot on the heels of the discovery of the DLSS 5 DLL in a prerelease version of NBA 2K27, __modder dashdogy__ found a way to bring Multi Frame Generation, one of the crown jewels of GeForce RTX 50-series graphics cards, to RTX 40-series (and earlier) products.

As already elevated graphics card prices seem set to continue rising, and hardware upgrades get further and further out of reach of the average PC gamer, more and more folks are going to want to hold on to the RTX 40-series hardware they have for as long as they can, especially if smoothness-boosting features like MFG are just a few clicks away on those older cards.

So we had to see MFG working on Ada for ourselves—assuming it works at all. We grabbed the mod files and got to playing with them in *Cyberpunk 2077*, since it’s likely in many TH readers’ Steam libraries already and has a healthy modding community. You can find the latest instructions for enabling MFG on Ada through __dashdogy’s GitHub page__.

Before spending a ton of time testing, we verified that the mod works at all. While spinning the camera at a high, constant speed, we could indeed see that increasing MFG multipliers beyond the officially supported 2X factor on Ada cards does greatly increase perceived smoothness or fluidity of motion in *Cyberpunk 2077,* as you would expect.

Another tell is that the same visual artifacts are visible in certain regions of the screen on both RTX 40-series and RTX 50-series graphics cards as you add more generated frames. MFG 4X and above, especially, tend to add some visual “junk” at the bottom of the frame that appears regardless of the game, and we could see that artifacting on Ada.

At least in *Cyberpunk 2077*, then, we’re confident that MFG is really doing its thing on RTX 40-series cards with this mod.

We also didn’t see any perceptible issues with frame pacing or frame delivery, although playing on a high-refresh-rate, G-Sync-Compatible monitor like our test bench’s ROG Strix XG27UCS smooths out all but the worst such issues. If you don’t have a high-resolution or high-refresh-rate monitor to begin with, the utility of MFG will be seriously limited for you anyway.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

## The latency question

So is this a free lunch? Is Nvidia soft-locking MFG to Blackwell purely for marketing reasons? That’s where performance testing comes in, since it has the potential to reveal whether there’s a catch in running MFG on Ada. The question is not so much whether MFG juices output frame rates, but whether it runs on Ada within acceptable latency thresholds.

__As we’ve long emphasized__, when you have essentially arbitrary control over output frame rates like MFG allows, input lag becomes the final barrier to a playable experience. So in the performance results that follow, we’ll certainly present output frame rates as you would expect. But you should view those in the context of your own monitor’s refresh rate. As long as the delivered frame rates we recorded exceed your display’s peak refresh rate, you have headroom to play with to keep your monitor at or near that number during gameplay.

The real issue, then, is whether both RTX 40-series and 50-series cards deliver an acceptable input latency under our test conditions. In our past testing, we’ve determined that a roughly 60ms average latency threshold, as indicated by Nvidia’s FrameView app, is the point at which player inputs and displayed frames start to become noticeably decoupled in AAA single-player experiences like *Cyberpunk.* 

If you’re only slightly on the wrong side of this threshold, a game might still be playable, but if you totally blow past it, you’re likely to notice laggy inputs and increasingly distracting visual artifacts as the MFG model struggles to fill in the gaps between sparser and sparser input data.

## Testing methods and notes

As one of the biggest technical showcases of the current PC gaming era, *Cyberpunk* 2077 lets us enable all the modern rendering features we’d want for Nvidia cards. It implements not only ray tracing and path tracing, but DLSS Super Resolution, Ray Reconstruction, and Multi Frame Generation. The number of AI-generated pixels per frame can be quite high in this title.

We enabled all those features to expose the full potential complexity of running all of their associated AI models in a modern rendering pipeline. If RTX 40-series cards are going to stumble for some reason with modded MFG enabled, we want to put as many obstacles in their way as possible.

And because benchmarking the performance of an unofficial mod is venturing into the Wild West anyway, we also added a DLSS 5 mod to the mix to see whether Blackwell GPUs have a distinct edge in the neural rendering future that the arrival of that feature promises to usher in. DLSS 5 is supposed to come to RTX 40-series cards later this year, so we think it’s good to understand where performance sits today, even if it’s subject to the same disclaimers as this MFG mod.

For reference, then, we tested *Cyberpunk* with maxed-out raster settings, path tracing, and MFG 4X at three resolutions: 1080p with DLSS Balanced, 2560x1440 with DLSS Performance, and 4K with DLSS Ultra Performance upscaling enabled.

We only tested cards ranging from the RTX 4090 down to the RTX 4070 for these experiments, both because of time and *Cyberpunk*’s VRAM requirements. We didn’t want to deal with potential performance pitfalls due to running out of VRAM, so the 12GB RTX 4070 is where we’re drawing the line for now.

## Modded Cyberpunk 2077 1080p performance

 ![MFG on Ada](https://cdn.mos.cms.futurecdn.net/o9Mk5eCEAxkB2PoCziUcT9.png) 


At 1080p, *Cyberpunk 2077* with MFG 4X scales fine on Ada, but it’s clearly scaling better on Blackwell. The RTX 4090 lands between the RTX 5070 Ti and RTX 5089. Introducing DLSS 5 to the mix doesn’t change any relative standings, although it does create some larger gaps between average frame rates and 1% lows than we might like on the RTX 4070 Ti Super, RTX 4070 Ti, RTX 4070 Super, and RTX 4070. The RTX 5070 has no such trouble.

 ![MFG on Ada](https://cdn.mos.cms.futurecdn.net/HmvoG94QKyFZZN2KaXLnR9.png) 


But again, the real story is in our latency results. Here, we can see that every card we tested falls under our 60ms threshold with MFG 4X alone. But Blackwell hardware has a clear advantage in the standings, as even the RTX 5070 delivers a lower input latency than the RTX 4090 with our DLSS 5 mod off and a comparable input latency with it enabled. All the other Ada cards shake out as you would expect from there. But in absolute terms, even with DLSS 5 enabled, only the RTX 4070 Super and RTX 4070 are far beyond our acceptable latency thresholds.

Blackwell might have a latency edge with MFG enabled and a smoothness edge with a modded version of DLSS 5 on top, but at least with the RTX 4070 on up, there’s certainly enough headroom to use the feature on Ada.

And as we went to press, a version of the RTX 40-series MFG mod came out that removes the need for ReShade. That more streamlined approach might cut down latency, but we couldn’t test it because it currently crashes *Cyberpunk 2077*. Again, this is the Wild West, not a validated, bulletproof solution from Nvidia like you get with RTX 50-series products.

## Modded Cyberpunk 2077 2560x1440 performance

 ![MFG on Ada](https://cdn.mos.cms.futurecdn.net/kgBMsxPaUjNJyNFyRYaqT9.png) 


At 2560x1440, generational performance standings and scaling between cards remains much the same as we saw at 1080p. The RTX 4090 still falls short of the RTX 5080, and the RTX 4080 duo falls behind the RTX 5070 Ti.

We also still see the wide gap between average frame rates and 1% lows rear its head on more Ada cards with our DLSS 5 mod enabled, though to be fair, these lows are still being smoothed over by MFG to the point that you’re unlikely to notice them with a high-refresh-rate, variable-refresh-rate monitor like we’re using.

 ![MFG on Ada](https://cdn.mos.cms.futurecdn.net/HLnHBr5iikUSgmSrFb6ES9.png) 


On the latency side, all of the Ada cards except the RTX 4070 still run our modded MFG 4X with acceptable input latency. But enable the DLSS 5 mod we’re using, and input latency climbs past 60ms for all Ada cards except the RTX 4090. The RTX 4080 Super and RTX 4080 still provide acceptable performance under this full load, as they’re only slightly over our latency threshold. But for any less powerful RTX 40-series cards, you’d need to start choosing between DLSS 5 and other eye candy, like lighter RT settings instead of path tracing or no RT or PT at all.

## Modded Cyberpunk 2077 4K performance

 ![MFG on Ada](https://cdn.mos.cms.futurecdn.net/h3eyeCYJFyX77MtbDQBAU9.png) 


Our modded performance results at 4K with DLSS Ultra Performance demonstrate why it’s so important to discuss MFG-boosted frame rates in the context of input latency. If you’re not mentally dividing by four, everything on our output frame rate might look playable.

At this high output resolution, the RTX 4090 finally takes the lead over the RTX 5080, both with plain MFG 4X and with our DLSS 5 mod on top. The 16GB of VRAM of the RTX 4070 Ti Super would seem to be giving it an edge over the RTX 4070 Ti and RTX 5070, and the RTX 4080 duo would seem to beat out the RTX 5070 Ti.

 ![MFG on Ada](https://cdn.mos.cms.futurecdn.net/yjNmAPeDfp64nKLpzaPuH9.png) 


Our latency chart for MFG 4X shows a weird, but entirely reproducible result: input latencies at 4K with DLSS Ultra Performance are actually much lower than they are at 2560x1440 for most Ada cards, despite the fact that both of these output resolution targets share the same input resolution.

We’re not sure why Ada cards run into such a latency hump with this MFG mod at 2560x1440 with DLSS Performance, but we double-checked our results, and this behavior is reproducible. Blackwell cards experience the more linear rise in input latency as output resolutions rise that you would expect.

Again, this is the Wild West of modded performance, and we have nobody to blame but ourselves here, but it’s an unfortunate result given the prevalence of 2560x1440 monitors. Perhaps the maintainers of this mod can track down the root cause and fix it, but nothing is guaranteed.

In any event, input latency with MFG 4X alone at 4K with DLSS Ultra Performance isn’t an issue for any card here. You might be pushing your luck with the RTX 4070, but both Blackwell and Ada cards are delivering on the promise of MFG here: smoother output with responsive input.

Add DLSS 5 to the latency picture, though, and as we’ve come to expect, you really want an RTX 5090, RTX 4090, or RTX 5080 for acceptable responsiveness. And you’re pushing it with the RTX 5080. No other cards in this bunch need apply.

## Bottom line

Our experience with the purportedly Blackwell-exclusive Multi Frame Generation on RTX 40-series cards through modding suggests that there isn’t any glaring reason why Nvidia couldn’t enable the feature for Ada Lovelace cards, and that’s kind of wild given how heavily it was touted as a Blackwell-exclusive feature back when those cards launched.

At least as long as Nvidia doesn’t find a persistent way to lock it out, our experience is that MFG generally just works on Ada. Even if input latencies aren’t quite as low on those older cards as they are on comparable Blackwell hardware, all else equal, they’re still perfectly acceptable, even under the combined load of path tracing, DLSS Super Resolution, DLSS Ray Reconstruction, and MFG 4X in *Cyberpunk 2077*.

We only had time to test cards ranging down to the RTX 4070 for this quick look, but for folks looking to extend the useful life of their Ada hardware, the availability of MFG could certainly stretch those cards’ lifespans.

But our experience also shows that MFG on Ada isn’t perfect. It’s still a mod in active development, and the unusual and reproducible input latency behavior we charted at 1440p on RTX 40-series cards is the sort of unexpected pitfall you might expect from an unofficial implementation of the feature. Cross your fingers that it’s an issue that can be fixed by the community.

The fact that MFG works as well as it does on Ada, even in this modded form, also makes us wonder whether Nvidia might just enable official support for it at some point, given the apparently bleak prospects for gaming graphics card pricing and future hardware generations as the AI boom shows no signs of abating. And such a move would provide much broader and more immediate performance relief for gamers than re-introducing ancient silicon like the RTX 3060.

Given that Nvidia is already working on bringing DLSS 5 to RTX 40-series GPUs, maybe this mod will convince it to throw in official MFG support, too. Fingers crossed.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jeffrey Kampman](https://cdn.mos.cms.futurecdn.net/8JCjGs5yVZds2YdKmzjUDE.jpg) 

As the Senior Analyst, Graphics at Tom's Hardware, Jeff Kampman covers everything that has to do with graphics cards, gaming performance, and more. From integrated graphics processors to discrete graphics cards to the hyperscale installations powering our AI future, if it's got a GPU in it, Jeff is on it.

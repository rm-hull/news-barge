---
title: DLSS 5's update sure is faster, but NBA 2K27 isn't going to convince anyone
  to turn it on
source_url: https://www.pcgamer.com/hardware/i-jammed-nvidias-new-dlss-5-october-update-model-into-the-rtx-spark-and-its-25-percent-faster-at-1440p/
source_site: PC Gamer
source_slug: pcgamer
scraped_at: '2026-10-15T16:56:41Z'
published: '2026-10-15T00:00:00Z'
description: We need a better showcase of this tech if Nvidia wants to get gamers
  onside.
image: https://cdn.mos.cms.futurecdn.net/9gFcHJrxmo3sAmPLHpcum6-2560-80.jpg
categories:
- Technology & Software
- Video Gaming
people: []
locations: []
organisations:
- GPU
- NBA
- Nvidia
- OLED
- PC Gamer Circuit Breaker
- VSync
---

![NBA 2K27 with DLSS 5](https://cdn.mos.cms.futurecdn.net/9gFcHJrxmo3sAmPLHpcum6-1920-80.jpg)

Pumpkin month is here and it has brought us bountiful PC tech, too. Along with the launch of the new Nvidia RTX Spark platform—bringing us all-Nvidia powered laptops and mini PCs for a pretty penny—we've also now got the latest update to DLSS 5, or DLSS Neural Rendering, or DLSS NR. I'm still not 100% sure how we should be referring to this, but I'm certainly not convinced by the whole '3D-guided Neural Rendering' moniker.

Whatever, we've got a new model to play with in the one game that has been officially released with the tech inside it: NBA 2K27. And, almost definitely from now on in any of the myriad modding platforms that have baked DLSS 5 into any game you could imagine, on any GPU architecture.

The new model is promising to be half as demanding of your hardware than the previous model—so a nominal 30% hit rather than 60%—and Nvidia says it has done this by refining the training data and reducing the model size itself down to around 118 million parameters, which makes it roughly 24% smaller. In terms of its impact on your GPU's VRAM, Nvidia gives the example of a reduction in VRAM usage at 4K of 20%.

#### NBA 2K27 running on the Nvidia RTX Spark with the DLSS 5 Oct update

Which is all well and good for Nvidia's numbers, but what happens in the real world? I've got hold of a preview version of the .dll files, specifically created for the RTX Spark hardware I'm testing right now (probably so we couldn't drop the files onto a repo somewhere and have the new model leaked early), and have been playing around with NBA 2K27 once more on the Asus ProArt P16.

### DLSS 5 October Update

Testing the new DLSS 5 model in NBA 2K27. Using DLSS Balanced and 4x Multi Frame Gen.

|  |  |
| --- | --- |
| NBA 2K27 (1080p High) Data |  |
| Product | Value |
| DLSS 5 Off | 227 Avg FPS, 93 1% Low FPS, 68 PC Latency (ms) |
| DLSS 5 On (original) | 143 Avg FPS, 63 1% Low FPS, 88 PC Latency (ms) |
| DLSS On (Oct update) | 168 Avg FPS, 61 1% Low FPS, 85 PC Latency (ms) |

|  |  |
| --- | --- |
| NBA 2K27 (1440p High) Data |  |
| Product | Value |
| DLSS 5 Off | 200 Avg FPS, 61 1% Low FPS, 76 PC Latency (ms) |
| DLSS 5 On (original) | 107 Avg FPS, 47 1% Low FPS, 117 PC Latency (ms) |
| DLSS On (Oct update) | 134 Avg FPS, 51 1% Low FPS, 92 PC Latency (ms) |

![PC Gamer Logo](https://cdn.mos.cms.futurecdn.net/bkwSqn4ocKYaQwBeFt2HHb-1200-80.png)

And the results are pretty impressive to be honest. First, that I can get this RTX Spark machine to run at over 200 fps anyways, but also that at 1080p it still sits around the 170 fps mark with DLSS 5 enabled.

Looking at the more intensive 1440p result, you can see what a massive hit the original model delivered to the game when DLSS 5 and Neural Rendering were enabled. Going from a healthy 200 fps down to effectively half that is a brutal performance hit that no-one is going to be happy with.

Especially when, in all honesty, the extra lighting and tonal improvements are only really visible during the game's many cutscenes. When you're zoomed out, actually playing the game, then the extra fidelity doesn't really add a whole lot to the experience, as you can see in the video above.

The PC Gamer Circuit Breaker newsletter breaks down the latest PC gaming tech, and finds you the best deals on the best products

### DLSS 5 October Update

Showing the difference between DLSS 5 off and on with the new October update model.

![After](https://cdn.mos.cms.futurecdn.net/UrCbuUPVrCVNgYvJParokd-1200-80.jpg)
![Before](https://cdn.mos.cms.futurecdn.net/LqVeF2F48rx5mPZi9c7gkd-1200-80.jpg)
![Brand Logo](https://proof.vanilla.tools/media/images/brandLogos/pcgamer.png)
![PC Gamer Logo](https://cdn.mos.cms.futurecdn.net/bkwSqn4ocKYaQwBeFt2HHb-1200-80.png)

It's still quite a hit going from 200 fps down to 134 fps—a 33% drop in performance—but that's in line with what Nvidia has been suggesting would be the case with this updated model. And when you're still getting that sort of frame rate at 1440p on a relatively thin and light laptop (running an Arm CPU, too) then I'll admit I'm impressed with the technical achievements all round here.

Of course we are running all the Nvidia bells and whistly things here, so I've got 4x MFG enabled and DLSS Super Resolution running on Balanced mode, but I'd still say the motion looks grand on the small screen of this Asus ProArt P16 laptop.

Though it really didn't before I disabled VSync. That was enabled by default when I first booted the game, dragging performance down to 60 fps despite the 120 Hz refresh rate of the OLED panel. And, oh boy, the Frame Gen artifacting was nuts. That all went away once I disabled it and the frame rate shot up, but it sure wasn't pretty...

### DLSS 5 October Update

Showing the difference between DLSS 5 off and on with the new October update model.

![After](https://cdn.mos.cms.futurecdn.net/9gFcHJrxmo3sAmPLHpcum6-1200-80.jpg)
![Before](https://cdn.mos.cms.futurecdn.net/t4LkeggvsB6fLkWpQjVRn6-1200-80.jpg)
![Brand Logo](https://proof.vanilla.tools/media/images/brandLogos/pcgamer.png)
![PC Gamer Logo](https://cdn.mos.cms.futurecdn.net/bkwSqn4ocKYaQwBeFt2HHb-1200-80.png)

But while this is *the* showpiece for DLSS Neural Rendering right now, NBA 2K27 is absolutely not the game that's going to show the tech off to its best. Sure, it has a lot of cutscenes, but for the most part you're watching the game from high above where the extra lighting pretties don't matter one jot. So really, why would you turn it on?

At least now, when it appears in new games—and when this updated model goes into the DLSS 5 modding tools—it's not going to have the same sort of performance hit that made it a struggle before. But there does need to be some sort of positive 'wow' moment for the feature.

Fingers crossed they can keep pushing the model further to bring that performance hit down even further, and fingers crossed some engaged devs get on board to make something impressive.

![Asus RX 9070 Prime graphics card](https://cdn.mos.cms.futurecdn.net/cDuR8WTcwKZUDqDb7coa2a-140-80.jpg)

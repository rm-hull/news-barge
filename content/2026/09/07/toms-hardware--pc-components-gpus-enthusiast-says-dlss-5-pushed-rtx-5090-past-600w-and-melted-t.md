---
title: Enthusiast says DLSS 5 pushed RTX 5090 past 600W and melted the 16-pin connector
  — Nvidia's neural rendering tech adds up to 50% more power draw in testing
source_url: https://www.tomshardware.com/pc-components/gpus/enthusiast-says-dlss-5-pushed-rtx-5090-past-600w-and-melted-the-16-pin-connector-nvidias-neural-rendering-tech-adds-up-to-50-percent-more-power-draw-in-testing
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-07T14:13:41Z'
published: '2026-09-07T00:00:00Z'
description: It's in the genetics.
image: https://cdn.mos.cms.futurecdn.net/V3GQ9DBP5BRAWcLwzBwGSL-1920-80.jpg
---

![A post-DLSS 5 RTX 5090 suffering from a genetic disease known as its 16-pin connector melting](https://cdn.mos.cms.futurecdn.net/V3GQ9DBP5BRAWcLwzBwGSL.jpg) 

The RTX 5090 is no stranger to controversy thanks to the incendiary nature of its 16-pin connector. When you add something as taxing as DLSS 5, which comes with a heavy increase in power draw, to an already dangerous mix, you're just cooking up a recipe for disaster. And it seems like this recipe has likely claimed its first victim. HardOCP forum member *Erek* claimed their RTX 5090 fell prey to the woes of the 16-pin connector yesterday, as it melted while testing DLSS 5 in*NBA 2K27*.

The irony is not lost on us that *NBA 2K27* is the only game that officially supports DLSS 5 right now — everything else is modded — yet it still reportedly killed the user's MSI RTX 5090 Gaming Trio OC, which carries a 575W TDP. However, during testing, erek reported his GPU going past 600W, with GPU-Z showing it hovering above 610W consistently, not just as a spike. Before this, the card only consumed around 450W while gaming, implying that DLSS 5 added more than 150W to the power draw.

 ![A post-DLSS 5 RTX 5090 suffering from a genetic disease known as its 16-pin connector melting](https://cdn.mos.cms.futurecdn.net/kUdrywBoX2CceDLLsbiDQL.jpg) 


While the 16-pin connector is capable of carrying up to 600W of power, the PCIe x16 slot the card is plugged into also provides 75W on its own. So, the connector wasn't necessarily drawing over 600W alone. Tragedy struck right after as Erek's RTX 5090 started exhibiting signs of instability and eventually stopped working entirely. The owner smelled something burning and, sure enough, found the 16-pin connector pulling an age-old classic: melting.

The plastic on the connector had melted enough to bond with the cable, making it very difficult to separate the two. Once they did come undone, the damage was clearly visible, with at least five pins on the 16-pin cable scorched; one pin's housing had completely melted away. This was a yellow-tipped cable, too, meant to ensure it was plugged all the way in. Despite the fact that we only got a blurry picture of the connector on the GPU, the little yellow dot of melted plastic almost comically stands out amidst a sea of black and grey.

![A post-DLSS 5 RTX 5090 suffering from a genetic disease known as its 16-pin connector melting](https://cdn.mos.cms.futurecdn.net/JYYPumtYviQ2hNGHivw9WL-1200-80.jpg) 

![A post-DLSS 5 RTX 5090 suffering from a genetic disease known as its 16-pin connector melting](https://cdn.mos.cms.futurecdn.net/WUt5X4puZ52FJBW2HtBtQL-1200-80.jpg) 

![A post-DLSS 5 RTX 5090 suffering from a genetic disease known as its 16-pin connector melting](https://cdn.mos.cms.futurecdn.net/JYYPumtYviQ2hNGHivw9WL-1280-80.jpg) 

![A post-DLSS 5 RTX 5090 suffering from a genetic disease known as its 16-pin connector melting](https://cdn.mos.cms.futurecdn.net/WUt5X4puZ52FJBW2HtBtQL-1280-80.jpg) 

We can't confirm whether DLSS 5 was actually responsible for burning Erek's card. After all, an RTX 5090 meeting its maker is a monthly tradition at this point, and the cause is usually tied to a loose fit between the connector and the cable. However, our own testing does align with how the enthusiast came up with their DLSS 5 hypothesis. We saw the MSI Lightning Z variant of the 5090, which has 2x 16-pin connectors and a 1,000W XOC BIOS, pull 800W in *Control* with DLSS 5 enabled. Without DLSS 5, the same GPU pulled just 691W.

That wasn't even the most egregious difference; in *Hogwarts Legacy*, we went from 480W without DLSS 5 to a whopping 720W with it enabled. That's a 50% increase in power draw for just one feature. The same game made the Founder's Edition of the 5090 pull 417W without the neural rendering tech involved, and 547W with it toggled on. So even in the standard version of the GPU with a single 16-pin connector, there's a 31% jump in power consumption because of DLSS 5.

 ![Hogwarts Legacy DLSS 5 power](https://cdn.mos.cms.futurecdn.net/MNyWN9nULswei8UsZY3EoG.png) 


Considering Erek's 5090 model lands somewhere between those two, and given his own testing showing a severe power budget imbalance, it's not unreasonable to assume DLSS 5 was the culprit. Had the user's GPU been acting weird before they tried the new feature, we might be having a different conversation. But it's clear that Nvidia has a lot of work to do before DLSS 5 makes its way onto the RTX 40-series down the line. Performance improvements aside, the safety concerns stemming from poor efficiency also need to be addressed.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg) 

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

- 
I fail to understand how these higher wattage cards or power supplies don’t have sensors to detect their draw and throttle to keep it below the safety max of their pack in cables. We’ve had something as simple as breakers in electrical for how long now? This is a solved problem. GPU makers need to get it together!Reply
- 
Reply
 Because if the spec was written in a sensible way, you would not need the extra circuitry for a VERY SIMPLE electrical problem which has been solved for nearly a century by now.QuarterSwede said:I fail to understand how these higher wattage cards or power supplies don’t have sensors to detect their draw and throttle to keep it below the safety max of their pack in cables. We’ve had something as simple as breakers in electrical for how long now? This is a solved problem. GPU makers need to get it together!
 
 This is nVidia's pure and sole ego.
 
Regards.

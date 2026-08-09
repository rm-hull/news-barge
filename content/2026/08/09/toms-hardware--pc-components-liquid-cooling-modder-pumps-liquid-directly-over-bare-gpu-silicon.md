---
title: Modder pumps liquid directly over bare GPU silicon via 3D-printed block — drops
  RTX 2060 Super load temps to 28°C despite initial leaks
source_url: https://www.tomshardware.com/pc-components/liquid-cooling/modder-pumps-liquid-directly-over-bare-gpu-silicon-via-3d-printed-block-drops-rtx-2060-super-load-temps-to-28-c-despite-initial-leaks
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-09T16:49:34Z'
published: '2026-08-09T00:00:00Z'
description: Custom 3D printed block was glued to the GPU so water went straight to
  the die.
image: https://cdn.mos.cms.futurecdn.net/u9bBdiUN7DjnuWBbPSTtSC-1920-80.jpg
---

!["Why can't we just pump water directly over the bare silicon?"](https://cdn.mos.cms.futurecdn.net/u9bBdiUN7DjnuWBbPSTtSC.jpg) 

The fearless TrashBench has been testing direct die water cooling of graphics cards. The inevitable twist here is that they removed the metal waterblock from the equation. Despite initial leaky results and much concern of water damage to the expensive parts thrown into the mix, some of the end results are eyebrow-raising in a good way.

![I Pumped Water Directly Onto a Running GPU - YouTube](https://img.youtube.com/vi/W51QlFj95kc/maxresdefault.jpg) 

“In my pursuit of the perfect water block, I realized, why do we need metal at all?” queried the antipodean host of the punk-rock GPU death lab. “Why can't we just pump water directly over the bare silicon? Makes sense to me.”

TrashBench began this project well aware that leaks might be a problem. Thus, a non-working GeForce RTX 3060 was chosen for the initial feasibility tests. It was measured up for a 3D printed water block which would direct the coolant directly over the GPU die. Our hardware adventurer covered any surface-mount components beside the GPU with nail polish to prevent water damage/shorting.

Some tried and trusted plumbing measures were then applied, with the design incorporating washers, gaskets, and hose clamps (worm-screw equipped jubilee clips). Water pipe fittings were melted into the block, which was fastened using the retaining clamp mechanism that the air cooler had previously used.

This initial test sprang a leak, or two, so TrashBench decided to add epoxy adhesive to secure and seal the 3D printed block to the GPU. This worked, but then some water was spotted oozing from the tube fittings, so they got a dose of epoxy too. At last, we had the first non-leaky prototype…

After some live runs using a powered-up GTX 980 were successful, it was time for the main event with fitting, testing, and benchmarking using an RTX 2060 Super. On the way, it was noticed that the choice of 3D print material used on TrashBench’s Bambu Lab 3D printer wasn’t trivial. Some materials leaked from the edges, and others were actually slightly porous. During live power tests, the TechTuber wisely used a PCIe riser cable so any leaks wouldn’t immediately drip onto the motherboard.

## Was it worth it?

If you like to live dangerously, it could be argued that the TrashBench results show some value in this cooling methodology. The headlining technique was compared against the stock cooler and a clamped-on AiO cooling solution.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

| Cooling solution | Observed temperature (°C) | 
|---|---|
| Stock | 70 | 
| AiO | 36 | 
| Direct water | 28 | 

Going by the numbers above, you can see that direct water cooling could be interesting, as long as you can ensure long-term confidence about leakage. In the video, you can also see some interesting extras, like running this system using -28°C coolant. The same trick is also tested using an Intel i5-7600K CPU. That was chosen as “it’s not a particularly hot CPU, but if it dies, I don’t care.”

The eventual conclusion was that chamber size matters (most clearly illustrated by the CPU cooling test), but pumping water directly over silicon can work.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

- 
Another long term concern is whether water will corrode and damage the chip and its connections. There are all kinds of physical effects that can happen, from regular corrosion, to corrosion promoted by electric potential, to also chemical reaction with impurities in water. There could also be damage from hydrogen ions diffusing through the chip and its connections.Reply

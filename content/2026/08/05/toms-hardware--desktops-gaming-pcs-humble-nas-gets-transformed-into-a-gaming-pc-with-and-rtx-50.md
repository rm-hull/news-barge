---
title: Crazed modder turns NAS into a gaming PC with RTX 5060 hanging from the side,
  boosts frame rate by 828% — Frankenstein rig hides dedicated PSU in drive bay, breaks
  Time Spy world record for the onboard CPU
source_url: https://www.tomshardware.com/desktops/gaming-pcs/humble-nas-gets-transformed-into-a-gaming-pc-with-and-rtx-5060-hanging-from-its-side-frankenstein-rig-hides-dedicated-psu-in-drive-bay-to-achieve-vast-performance-increase-over-igpu
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-05T10:45:56Z'
published: '2026-08-05T00:00:00Z'
description: Who needs extra storage anyways?
image: https://cdn.mos.cms.futurecdn.net/3NEvmPuLpnMaWGtcqSAa56-2560-80.png
---

![Putting an RTX 5060 inside a ZimaCube 2 NAS server](https://cdn.mos.cms.futurecdn.net/3NEvmPuLpnMaWGtcqSAa56.png) 

It seems the global component crisis has skyrocketed the prices of storage to the point where some alternative ways of utilizing a NAS have popped up. YouTube PC enthusiast TrashBench recently took a ZimaCube 2 NAS and modded it into a gaming PC, driven by an RTX 5060 graphics card. Despite the low-power laptop CPU inside the server, the results still showed an astronomical improvement in gaming performance across the board, improving frame rates by 828% in some tests and breaking the Time Spy world record for the Intel Core i5-1235U CPU.

![Can a Server Replace a Gaming PC? - YouTube](https://img.youtube.com/vi/YeGX7_m6Utg/maxresdefault.jpg) 

For context, the ZimaCube 2 is powered by an Intel Core i5-1235U CPU, which is an Alder Lake chip featuring just two P-cores and eight E-cores, alongside Iris Xe integrated graphics. The iGPU is weak because that's all that's needed for a server (if it's needed at all). This system was never intended for gaming, but the motherboard inside has a vacant PCIe 4.0 x16 slot, making this NAS the perfect candidate to be liberated by some questionable mods.

At first, the tests showed the iGPU hitting around 18 FPS in *Hitman 3* on 1080p with low settings.*Cyberpunk 2077* was even worse with just 13 FPS, while*Shadow of the Tomb Raider* was the most promising title, achieving 31 FPS. Putting an AMD Radeon Pro WX5100 workstation GPU (a cut-down version of the RX 480) in the board's slot helped raise the numbers a bit, around 40% on average, but the updated performance was still not enough to be classified as playable.

TrashBench proceeded to connect an RTX 5060 to the x16 slot with a riser cable and just let it hang outside the case, since the card was way too big to fit inside. Of course, this wasn't ideal and would restrict airflow quite a bit, so he devised a 3D-printed frame that would hold the GPU in place, while zip-tying the other end to the case directly. The final result might not exactly look polished, but it was firm enough to conduct benchmarks.

 ![Putting an RTX 5060 inside a ZimaCube 2 NAS server](https://cdn.mos.cms.futurecdn.net/i6QRkaz2qDULfGCNWaGz8Q.png) 


Keep in mind that all this jury-rigging was possible due to the ZimaCube's unique design. The chassis has large cutouts across its chassis, allowing the riser cable to easily protrude from the left. To power the RTX 5060, TrashBench removed all the hard drive caddies so that the system's drive bay was left completely empty. He then fit a 750W SFX power supply inside with an extension cable that ran up to the GPU's power connector. The front cover of this NAS is magnetic, so everything was nicely hidden behind it.

 ![Putting an RTX 5060 inside a ZimaCube 2 NAS server](https://cdn.mos.cms.futurecdn.net/mdFhfdo6Ee9cDLTxmZ699D.png) 


 ![Putting an RTX 5060 inside a ZimaCube 2 NAS server](https://cdn.mos.cms.futurecdn.net/qPZadtcEZLHAWGL8kWjyme.png) 


TrashBench's retesting showed *Hitman 3* running at 167 FPS on average, which is an 827% improvement over the stock 18 FPS, or more than nine times faster. Similarly, *Cyberpunk 2077* got a 7x boost, going from 13 FPS to 90 FPS. Framerates in *Shadow of the Tomb Raider* "only" quadrupled, as the RTX 5060 achieved an average of 124 FPS compared to 31 FPS with the iGPU.

TrashBench didn't stop there and, true to his nature, wanted to freeze the CPU to try and see if he could get even better results. The issue was that the chip never throttled to begin with, and the GPU was already bottlenecked, so running an antifreeze loop actually worsened performance. The silicon designed to run a storage server had achieved its maximum potential.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

 ![Putting an RTX 5060 inside a ZimaCube 2 NAS server](https://cdn.mos.cms.futurecdn.net/CfLr4umwCeXkvpTgtBXS6b.png) 


Unfortunately, this variant of the ZimaCube 2 does cost $1,299 to start with so you're much better off just building a regular PC even today. It also doesn't come with Windows, and the BIOS was never configured to run a dedicated GPU, so you have to always have something plugged into the iGPU's display output for the dGPU to display anything. Still, as a wild experiment, we can call this one a success.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

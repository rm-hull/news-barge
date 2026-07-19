---
title: Crazed enthusiast runs PC on 192 AA batteries, successfully boots into Hannah
  Montana Linux — System is stable during stress testing and even plays FreeDoom
source_url: https://www.tomshardware.com/desktops/pc-building/crazed-enthusiast-runs-pc-on-192-aa-batteries-successfully-boots-into-hannah-montana-linux-system-is-stable-during-stress-testing-and-even-plays-freedoom
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-19T13:46:40Z'
published: '2026-07-19T00:00:00Z'
description: The ultimate battery-powered PC?
image: https://cdn.mos.cms.futurecdn.net/eg4Uuo9sB4KAie6rAGTQSP-1920-80.png
---

![Powering a Desktop PC on 400 AA Alkaline Batteries](https://cdn.mos.cms.futurecdn.net/eg4Uuo9sB4KAie6rAGTQSP.png) 

We've seen a few battery-powered PCs around here — after all, what are laptops but small computers running on Lithium-ion cells? When it comes to fueling actual desktop systems, though, the story is always one of compromise, however, this field of cutting-edge shenanigans has hit a new milestone thanks to creator *Uwoslab*. He just built an interconnected power bank out of 192 AA cells, enough to run a modern AM4 system without jeopardizing its performance.

![[LIVE] Powering a Desktop PC on 400 AA Alkaline Batteries to see if it's Possible - YouTube](https://img.youtube.com/vi/NG8r47tdAo4/maxresdefault.jpg) 

The build is rather straightforward and actually started with 400 AA batteries as the creator had bought four separate packs containing 100 cells each. His plan was to wire up 8 cells in parallel, then connect those little banks in series until he had 50 of them. Simple math tells us eight multiplied by fifty is 400, but ultimately, he only ended up wiring 192 batteries together, split across 3 large wooden boxes.

The boxes were used as anchor points to connect the batteries together and provide structural rigidity. They were laser-cut to fit the cells perfectly and were made out of wood. The creator put clips and contact pads at either ends of the apparatus to serve as the negative and positive terminals, respectively, with four cells going into each slot. He then duct-taped the whole thing together to make it even more secure.

![Powering a Desktop PC on 400 AA Alkaline Batteries](https://cdn.mos.cms.futurecdn.net/Ur9mDsrpVnxCh95ShzPkTQ-4080-80.jpg) 

Image credit: Uwoslab

![Powering a Desktop PC on 400 AA Alkaline Batteries](https://cdn.mos.cms.futurecdn.net/5xKncGUPeDsY8XavDgVoaD-1920-80.png) 

Image credit: Uwoslab

Each box held 64 batteries and Uwoslab built three of them, so that's how we get to the 192-count mentioned earlier. This same creator has actually tried to power a PC off of 9V zinc-carbon batteries before, but that experiment failed for the most part since the PC wouldn't stay on for more than a few seconds. His prior experience informed him to switch to Alkaline batteries instead that carry a higher voltage — 1.5V, to be exact.

Since PCs work on 12V, wiring together eight 1.5V cells gets you exactly 12V needed for stable operation, hopefully. Uwoslab was also using "high-drain" Pookell AA Alkaline batteries that trade capacity for higher voltage ratings. If you were to combine 400 of these bad boys in a perfect hypothetical, you'd generate about 160 watts of power for ten straight hours.

Unfortunately, AA batteries are not the most efficient and they drop in voltage over time as they're drained, which makes powering something as (relatively) sensitive as a modern x86 computer a lot more difficult. But it can still be done. The biggest mistake people make at this stage (as if this is a common occurrence) traditional wall-plug power supply attached to a 12V-to-220V inverter. Instead, he ran his parallel battery grid directly into a 12V DC-to-ATX adapter board plugged straight into the motherboard.

 ![Powering a Desktop PC on 400 AA Alkaline Batteries](https://cdn.mos.cms.futurecdn.net/yrF6Nb4NFMVb9qzkmpsNZc.png) 


We don't know much about the PC itself apart from the fact that it's an AM4 system without a dedicated GPU, so it's a G-series chip. There's no storage device either; we're booting straight from a flash drive. And what are we booting into? Hanna Montana Linux. Yes, you're reading that correctly. The popular Linux distro from 2009 based on Disney's teen popstar was recently revived and given a modern makeover.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

IT WORKED! Unlike the 9V attempt, this one ran the desktop for 30 minutes without running dead off of 200 AAs. Given the capacity at the end of the test it will likely run a couple more hours before the power drop becomes too much. we benchmarked with Hannah Montana Linux pic.twitter.com/vKBEkundybJuly 17, 2026


Not only does the battery-powered PC easily boot into Hanna Montana Linux on first try, but it even passed the built-in Linux CPU stress test (stress-ng) with flying colors. The CPU was pegged at 98% usage and dropped down to a stable 11.95V during the testing, while the battery bank was reading out at 13V initially. The experiment was a raging success, perhaps better than any Alkaline-powered PC that came before it.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

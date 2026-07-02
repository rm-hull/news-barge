---
title: Possible AMD RX 7900 XTX engineering sample with red PCB surfaces — prototype
  came with no backplate & custom VBIOS but matches RX 7900 GRE specs
source_url: https://www.tomshardware.com/pc-components/gpus/possible-amd-rx-7900-xtx-engineering-sample-with-red-pcb-surfaces-prototype-came-with-no-backplate-and-custom-vbios-but-matches-rx-7900-gre-specs
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-02T14:27:26Z'
published: '2026-07-02T00:00:00Z'
description: It has 16GB of GDDR6 VRAM.
image: https://cdn.mos.cms.futurecdn.net/VYiyJYZmi5PRuTfy9ycexM-1920-80.png
---

![RX 7900 XTX engineering sample](https://cdn.mos.cms.futurecdn.net/VYiyJYZmi5PRuTfy9ycexM.png) 

It's always interesting to revisit an engineering sample for an older GPU as it allows us to analyze it with the benefit of hindsight. We've come across a card that appears to be an early prototype for AMD's RX 7900 XTX, which was purchased by Tiktoker *Shav Tech*on the secondhand market. The buyer thought they were ordering a regular 7900 XTX, but they got something else that's recognized as such in software but clearly differs at the hardware level.

As you can see above, this card is very red and we've seen AMD's engineering samples come with red-colored PCBs before, which further confirms what we're looking at. The poster said the GPU did not come with a backplate, as you can see from the second image. The third picture gives us a closer look at two extra connectors sticking out from the middle of the PCB that are not found on retail cards. 

The blue connector is composed of I2C, PMBus, and JTAG headers across both rows. JTAG allows engineers to collect diagnostic data directly from the core or memory controller, bypassing all internal circuitry. On the other hand, I2C / PMBus are responsible for monitoring power draw and temps; the testers connect directly to the VRMs and telemetry sensors onboard via specialized USB adapters.

## What's the most impressive launch of 2026 so far?

The shrouded black connector underneath is a logic analyzer meant for checking signal quality. Basically, engineers hook up an oscilloscope or logic analyzer ribbon cables here to capture clean, high-speed signal waves across the PCB trace lines. It helps test the die-to-die communication (since RDNA 3 GPUs employ an MCM design) before chips are sent for final production. 

There are little dip switches at the bottom of the PCB as well that could be used to switch between PCIe generations to test the GPU on older motherboards. It's more likely that these serve as different boot configurations for recovery VBIOSes. Speaking of which, the buyer also confirmed that this unit comes with a custom VBIOS that is identified as "Navi 31" and the card refused to flash an RX 7900 GRE VBIOS entirely.

![RX 7900 XTX engineering sample](https://cdn.mos.cms.futurecdn.net/mhHUobA43j2p2cvw4cDqiM.png)

![RX 7900 XTX engineering sample](https://cdn.mos.cms.futurecdn.net/JL3vknpoFk5AosjJpSCEhM.png)

![RX 7900 XTX engineering sample](https://cdn.mos.cms.futurecdn.net/mcANBF75UsoWW3Uik5XgfM.png)

![RX 7900 XTX engineering sample](https://cdn.mos.cms.futurecdn.net/nGSVzmrK4ZmrFqqpEBGbuM.png)

![RX 7900 XTX engineering sample](https://cdn.mos.cms.futurecdn.net/fvVkGtb77SGFdwZUG8JcsM.png)

![RX 7900 XTX engineering sample](https://cdn.mos.cms.futurecdn.net/rZEpUbijp2XTiURobi5MnM.png)

![RX 7900 XTX engineering sample](https://cdn.mos.cms.futurecdn.net/JrRTMn5gnP9yXPvdhJToAM.png)

The reason the original poster even attempted that was because they thought this was a "spoofed RX 7900 GRE," as in, someone took the PCB from an RX 7900 GRE and just made it look like an RX 7900 XTX in software. GPU-Z screenshots somewhat corroborate this since the card is officially recognized as a 7900 XTX, but the specs don't line up at all. Instead of 24GB of GDRR6X VRAM, this GPU came with 16GB of GDDR6 memory. 

That's exactly the same as an RX 7900 GRE. Moreover, the ROP and TMU count also match the RX 7900 GRE — 160 instead of 192 and 320 instead of 384, respectively. The bus width is marked as 256-bit, which is what the GRE has, while the 7900 XTX comes with a 384-bit wide bus. Other parameters such as the release date, die size, clock speeds indicate it's an RX 7900 XTX, so there's definitely some conflict here.

Realistically, we might be looking at a 7900 XTX prototype that ended up serving as proof-of-concept for a cut-down version of the Navi 31 silicon. This PCB even features 12 memory modules that would otherwise stack up to 24GB, but here it's limited to only 16GB. Not every Navi 31 die is binned perfectly, and some of the leftovers eventually became the RX 7900 GRE in China first, followed by a global release in 2023.

  


*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

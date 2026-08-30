---
title: Modders solder power cables directly to RTX 5090 PCB to eliminate notorious
  melting 16-pin connector — bare-board Galax HOF card pulls 600W under chiller cooling
source_url: https://www.tomshardware.com/pc-components/gpus/modders-solder-power-cables-directly-to-rtx-5090-pcb-to-eliminate-notorious-melting-16-pin-connector-bare-board-galax-hof-card-pulls-600w-under-chiller-cooling
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-30T13:47:56Z'
published: '2026-08-30T00:00:00Z'
description: '''There''s no princess connector here.'''
image: https://cdn.mos.cms.futurecdn.net/35BFzKzoKEL3DVg4G2hTNX-1920-80.png
---

![Soldering power wires directly to the PCB of an RTX 5090](https://cdn.mos.cms.futurecdn.net/35BFzKzoKEL3DVg4G2hTNX.png) 

Ever since the Nvidia GeForce RTX 5090 launched (and the RTX 4090 before it), reports of the card burning down have been commonplace in the community. The culprit behind the GPU's incendiary nature is the 16-pin power connector that's notorious for being unreliable... so what if we got rid of it in the first place? That's what Brazilian YouTuber TecLab did in their latest experiment — stripping an RTX 5090 down and powering it through wires directly soldered to the PCB.

![Aí o cara chora! ... perder 25K por causa de um conector. - YouTube](https://img.youtube.com/vi/D1mIVgYY264/maxresdefault.jpg) 

The GPU used for this test was a very high-end Galax HOF OC LAB XOC variant of the RTX 5090D. Unlike standard RTX 5090s that come with a single 16-pin connector for their 575W TDPs, this bad boy is equipped with twice the firepower (literally) since you can use up to 2,000W OC BIOSes on it. That already sounds like a bad idea, but TecLab went further and removed the heatsink and fans entirely to liquid-cool the core.

The modders took two sets of wires and soldered them right above either power connector on the PCB, linking them to the connectors' traces. They used two adapters to intercept standard 16-pin power cables coming from a PSU and convert them into bare wires that could be soldered easily. From the looks of it, the poor soldering job was only going to put these guys in more danger, but it somehow worked.

 ![Soldering power wires directly to the PCB of an RTX 5090](https://cdn.mos.cms.futurecdn.net/Qqji7GJkLVnUJiotFkGWLX.png) 


The card booted and ran just fine, even benchmarking pretty well. Remember, there was no cooler on the GPU. Instead, it was being tamed by two 120mm fans loosely zip-tied to the PCB and an industrial liquid chiller running ice-cold water across the core. We didn't get any temps, but the card was running at around 600W based on the ~50A reading from the power meter clamped to the 12V rail.

TecLab explained that they'd grown tired of the constant complaints about 16-pin power connectors on RTX 5090s causing problems. They sarcastically presented this "solution" as an answer to people who whine too much about their expensive cards melting, taking matters into their own hands to show Nvidia "how it's done." Even though the experiment was a success, it's safe to say that this is not safe; do not try this at home, kids.

 ![Soldering power wires directly to the PCB of an RTX 5090](https://cdn.mos.cms.futurecdn.net/2HiY7MbVhqT2j3QNw2PkMX.png) 


Regardless of the practicality here, the fact that hastily soldering wires to a 900W GPU is potentially more reliable than Nvidia's factory-developed solution is simply absurd. We've seen so many external monitoring tools purpose-built for saving these 16-pin cards that each new solution just begs the question as to why they haven't been recalled yet. Then again, if you're buying a $5,000 GPU, we suppose a WireView is chump change at that point.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

- 
I wouldn't recommend doing what they did. They used 12 guage wires - which are rated for about 24A continuous (30A peak). 48 amps continuous at 12 volts = 576 watts.Reply
 
Even though the 12VHP connector isn't great, it's certainly "OK" at 290 watts load.. (this board has 2 of them).

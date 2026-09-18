---
title: Proven 8-pin PCIe plugs aren't immune to melting — Thermal Grizzly WireView
  adapter burns out on Radeon RX 7900 XTX
source_url: https://www.tomshardware.com/pc-components/gpus/proven-8-pin-pcie-plugs-arent-immune-to-melting-thermal-grizzly-wireview-adapter-burns-out-on-radeon-rx-7900-xtx
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-14T15:00:55Z'
published: '2026-09-14T00:00:00Z'
description: 8-pin connectors can melt too.
image: https://cdn.mos.cms.futurecdn.net/kmxG3xPY2zgARQU2e6CYcX-1920-80.jpg
categories:
- Technology & Software
- Hardware
---

![Damaged PCIe 8-pin connectors on a Thermal Grizzly WireView adapter](https://cdn.mos.cms.futurecdn.net/kmxG3xPY2zgARQU2e6CYcX.jpg) 

If you believe that the 8-pin PCIe power connector is entirely immune to the problems that have plagued the newer 16-pin connector, think again. A recent incident suggests that even the humble 8-pin is not entirely immune to failure. According to a Radeon RX 7900 XTX owner on Reddit, the 8-pin connectors on a Thermal Grizzly WireView monitoring device suffered overheating damage while connected to the graphics card.

The user said that they experienced frequent freezes and black screens before discovering the damage. The affected connectors were the 8-pin connectors on the GPU side of the monitoring device, with visible signs of burning and melted plastic. The user also confirmed that the connectors were fully inserted, although the exact cause of the failure is still unknown.

WireView is essentially an adapter that sits between a graphics card and the power cables, allowing users to monitor various values like power consumption, voltages, current in amperes, minimum and maximum power consumption, and more. Rather than connecting the PSU cables directly to the GPU, the power passes through the monitoring device, thus adding another set of connectors and electrical contacts to the power delivery path. A poor electrical connection, increased contact resistance, a damaged connector, or an issue with the adapter itself could have caused the overheating damage.

Thermal Grizzly previously pointed to improper seating, backplate interference, or incorrectly aligned or soldered contacts as possible causes of connector damage, although the company is yet to identify the cause of this particular incident. The company has reportedly contacted the affected user and asked them to get in touch with its support team so the company can investigate the damaged WireView adapter. The investigation could potentially help determine whether the failure originated from the adapter, the connectors, the GPU, or a combination of factors.

While we are on the subject of 8-pin power connectors, just days ago we saw a heavily modified RTX 5090 successfully running on traditional 8-pin connectors. The modders replaced the card's original 16-pin connectors with three 8-pin connectors soldered directly to the PCB, using heavy-gauge cables and modified sense pins. The card reportedly pulled as much as 900W and reached 3,400 MHz, demonstrating how capable 8-pin connectors can be when properly implemented. However, this was an extreme hardware modification, not a stock configuration.

*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

  


Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Kunal Khullar](https://cdn.mos.cms.futurecdn.net/NDK3ae3zDxAx2BJnMXxBJV.jpg) 

Kunal Khullar is a contributing writer at Tom’s Hardware. He is a long time technology journalist and reviewer specializing in PC components and peripherals, and welcomes any and every question around building a PC.

- 
Reply
It's just the nature of having multi-pin connectors without balancing, it was always a risk but we just have better visibility now. Adapters with multiple connectors like this make it slightly worse as the spacing and alignment is fixed and doesn't always match the spacing on the card, as soldered.S58_is_the_goat said:Blame the adapter, not the first time this happened with his adapters.
- 
good thing about this is Roman (derbaur) will likely actually investigate the issue, refund the user if its actually the products fault, and then make a YT video about issue and how they plan to fix it.Reply
 
 
also 8pin was never "immune" its just a much more reliable connector with much more in world and yet failure rate is a drop in water vs 12vhighpower
- 
Reply
 I don't think there is a fix for the versions with multiple connectors.hotaru251 said:good thing about this is Roman (derbaur) will likely actually investigate the issue, refund the user if its actually the products fault, and then make a YT video about issue and how they plan to fix it.
 
 
also 8pin was never "immune" its just a much more reliable connector with much more in world and yet failure rate is a drop in water vs 12vhighpower
- 
Ultimately, 12v is not sufficient for a modern high-end machine under load.Reply
 
 The solution is to migrate to 48v. Google and Meta moved datacenter racks to it a decade ago, and PCI-SIG has had a 48v rail and a 48VHPWR connector in the CEM spec since 2022. Nobody has shipped it.
 
 At 48v a 600w card draws 12.5a instead of 50, and this problem goes away. Ideally you’d do this in conjunction with going to a two wire connector of appropriate size so that per-pin imbalances simply don’t exist rather than just reducing them to ‘possible, but generally inconsequential’ with multi-pin connectors.
 
Either way. Anything short of that, when you're dealing with 600w GPUs and CPUs that can exceed 350w, is rearranging deck chairs on the Titanic.
- 
Reply
 Fully agree, I keep calling for an ATX48VO standard.Siorus said:Ultimately, 12v is not sufficient for a modern high-end machine under load.
 
 The solution is to migrate to 48v. Google and Meta moved datacenter racks to it a decade ago, and PCI-SIG has had a 48v rail and a 48VHPWR connector in the CEM spec since 2022. Nobody has shipped it.
 
 At 48v a 600w card draws 12.5a instead of 50, and this problem goes away. Ideally you’d do this in conjunction with going to a two wire connector of appropriate size so that per-pin imbalances simply don’t exist rather than just reducing them to ‘possible, but generally inconsequential’ with multi-pin connectors.
 
Either way. Anything short of that, when you're dealing with 600w GPUs and CPUs that can exceed 350w, is rearranging deck chairs on the Titanic.
- 
Yes, 8-pin standard cables have been known to fail. But the failure rate of a 5090 to all 8-pin GPUs combined is probably 100 to 1. I trust 8-pins a lot more than I would trust the 12-pin. I've started GPU tasks on 8-pin connector cards, went on vacation for two weeks, came back, and everything was perfect. I knew it would be. Ain't no way in hell I'd even leave the room with a 5090 under full load. If someone handed me a 5090 for free on a silver platter, I wouldn't take it. Why? Because I run compute tasks overnight while sleeping. I'm not being woken up by burnt plastic. It's different for a gamer, because they are right there with the PC and can catch it right away. I run overnight tasks while sleeping. Sorry, I'm just not risking it. It really is just not worth the risk. But it shouldn't be this way.Reply
 
 Consumers shouldn't be scared to buy a product due to a fire hazard because of a design flaw. The fact that NVidia puts its consumers in harms way is worse. Our trusty 8-pin has nev.... well I shouldn't say NEVER failed us, but it's pretty rare. If it ain't broke, don't fix it. NVidia needs to own their mistake and fix it.
 
Do you ever notice how the 3090Ti has the same TDP as the 4090, but you never hear of 3090Ti's melting. Now why would this possibly be? They use the same connector. Buildzoid did a video on this. The difference: Current balancing. The 3090Ti does it. The 4090 does not, and NVidia has told all AIBs starting with the 40 series that they are NOT ALLOWED to current balance. That's right ladies. NO FIXING THE PROBLEM!!! YOU AREN'T ALLOWED TO FIX THE PROBLEM. YOU ARE REQUIRED TO LEAVE IT BROKEN!!!!! THATS OUR RULE!!!!!. Pathetic

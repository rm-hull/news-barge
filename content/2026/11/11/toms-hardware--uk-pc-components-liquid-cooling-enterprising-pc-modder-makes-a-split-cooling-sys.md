---
title: Modder routes PC water cooling loop to radiator outside to beat the winter
  heat — winter cold keeps CPU and GPU temperatures below 50C under load
source_url: https://www.tomshardware.com/uk/pc-components/liquid-cooling/enterprising-pc-modder-makes-a-split-cooling-system-to-keep-it-from-overheating-his-room-winter-cold-keeps-cpu-and-gpu-temperatures-below-50-c-under-load
source_site: Tom's Hardware
source_slug: toms-hardware
description: A Reddit PC builder created an automated split cooling system to dump
  heat outside.
image: https://cdn.mos.cms.futurecdn.net/Jt3DBGFEcwnt7xYFibN6f9-2035-80.jpg
published: '2026-11-11T00:00:00Z'
scraped_at: '2026-11-11T10:47:30Z'
categories:
- Technology & Software
- Hardware
people:
- Jhet Borja
- Tom
locations:
- Bykski
organisations:
- CPU
- GPU
- Get Tom's Hardware
- Google News
- Motor\_Attention1865
- PC
- Reddit
---

![PC radiator routed to the outside of a house](https://cdn.mos.cms.futurecdn.net/Jt3DBGFEcwnt7xYFibN6f9-1920-80.jpg)

u/Motor\_Attention1865 on Reddit didn't like how his PC added extra heat to his room in the winter, so he went the extra mile to dump the heat outside in a fashion similar to mini-split air conditioners. The external cooling system is controlled by an Arduino Mega that the PC communicates with when it needs extra cooling. The system opens a three-way valve to route coolant outside and prevents condensation by keeping the coolant temperature above the dew point.

Our intrepid modder's room has heated floors, and the PC was dumping too much heat under the table where his PC sits, even in 25 °F (-4 °C) weather. He grew tired of manually opening a window to regulate the temperature in his space, so he put in much more effort to create a split cooling system that puts another radiator outside in the below-freezing temperatures, cooling down the PC significantly.

Motor\_Attention1865's build itself is impressive enough, with a delidded Core Ultra 7 270K Plus cooled by a Thermal Grizzly 1851 Mycro Pro direct-die water block with Thermal Grizzly Conductonaut Extreme liquid compound. Not only is his RTX 4070 Ti Super also watercooled with a Bykski water block, but the 2x24GB DDR5-8400 G.Skill RAM is also watercooled using Bykski heat spreaders with an IceManCooler two-channel water block. The cooling system within the PC has two radiators: a 120mm in the back and a 360mm in the front, all fed by an EK Kinetic D5 pump-reservoir.

The external cooling system, however, is even more impressive. The 240mm outdoor radiator with two Noctua iPPC-3000 fans isn’t outrageous, but the automated system that makes it useful is what’s interesting. Next to the PC is a box with a Bykski D5 pump and reservoir that pushes water outside, but it doesn’t use the external radiator until the PC needs the extra cooling.

Upon startup, the PC runs a Python script that communicates with an Arduino Mega connected to three temperature probes checking the coolant temperature and three more temperature and humidity sensors that monitor the PC case and the ambient air. The sensors give the Arduino Mega information on where to switch the motorized three-way valve depending on the temperature and humidity.

The problem with extreme cold in any PC is condensation. If coolant gets below the dew point of the environment, condensation forms, potentially shorting out PC components. To prevent this disaster, the Arduino determines the dew point based on the humidity and temperature of the room and in the PC. Motor\_Attention1865 set the Arduino to close off the outside radiator at +10 °C above the dew point, or +5 °C during benchmarking, allowing for low temperatures without risking droplets forming in the PC.

Because of the freezing or below-freezing temperatures at which this external loop is meant to operate, Motor\_Attention1865 also added pure ethylene glycol to the Aquacomputer Double Protect Ultra Clear coolant in the loop, lowering its freezing point from -18 °C to -28 °C.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Thanks to the supplemental cooling system and delidding, the system achieves temperatures below 50 °C under heavy use. According to Motor\_Attention1865, the RTX 4070 Ti sits at 37 °C and the CPU hovers around 45-50 °C while gaming. Temperatures were higher in benchmarks, however — in Cinebench R23, the CPU sat at 52 °C, while in 3DMark Steel Nomad, the GPU was at 48 °C.

Above all, however, Motor\_Attention1865 no longer needs to bother himself with opening a window if their room gets too hot with the PC under load. It's the small things.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jhet Borja](https://cdn.mos.cms.futurecdn.net/niBNJTDN6c99Ri7HD5zNZ8-140-80.png)

Jhet Borja is a serial hobbyist who was taking apart toys from childhood and sketching inventions. He now loves doing DIY projects ranging from designing custom 3D-printed parts, building PCs and keyboards, all the way to woodworking. If he's not getting his hands dirty, he's probably brainstorming his next project.

---
title: This 8-bit computer plans to run flight sim and generates a 'pleasant homely
  aroma' by burning dust off 1950s vacuum tubes — oh, and it can explode at any time
source_url: https://www.techradar.com/pro/this-8-bit-computer-plans-to-run-flight-sim-and-generates-a-pleasant-homely-aroma-by-burning-dust-off-1950s-vacuum-tubes-oh-and-it-can-explode-at-any-time
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-19T04:31:03Z'
published: '2026-09-18T00:00:00Z'
description: 460 tubes, roughly 1 kW of heating power, and a fire extinguisher on
  standby
categories:
- Technology & Software
- Home, Garden & DIY
image: https://cdn.mos.cms.futurecdn.net/dGrnWSuN8rSJLERGqyBSk6-768-80.png
locations:
- Bodet
- UK
- Valve Museum
people:
- Judy
- Mike
- Rahim Amir
organisations:
- ALU
- Apollo Guidance Computer
- Google News
- PC
- PCs
- RGB
- SFF
- TechRadar Pro
---

![A closeup look at The Tube Computer](https://cdn.mos.cms.futurecdn.net/dGrnWSuN8rSJLERGqyBSk6.png)

* **Retired UK hobbyist builds 8-bit computer from 460 recycled tubes, all wired as NOR gates, on a 190 x 130 cm wall panel**
* **The machine is expected to run a flight simulator program once completely finished, but the builder is currently working on the status system that would allow it to do so**
* **Previous versions of the machine have gone 'bang' twice, as noted by the tinkerer, prompting him to keep a fire extinguisher handy for his experiment**

A retired hobbyist in the UK who identifies himself only as Mike has hung an 8-bit computer built from 460 recycled vacuum tubes on a brick wall in his home, and over the past ten days, it has seen widespread press coverage.

The machine is real, the glow is real, the smell is real, and the accompanying documentation is unusually candid and detailed for what is essentially a DIY project.

The tinkerer is currently trying to use the computer to run a flight simulator he has already coded but has yet to get the hardware into a state where it can run.

## Soviet-era tech meets a hobbyist and a computer is born

Mike's technical write-up makes it clear that we have a well-designed, well-researched 8-bit computer that packs 920 triodes into 460 Soviet-designed 6N3P double triodes, each wired as an identical NOR gate.

The registers, counters, 8-bit arithmetic logic unit, ring-oscillator clock, and small tube RAM are all assembled from that single building block, an approach Hackaday traces to the Apollo Guidance Computer.

The tubes sit on 46 ten-tube plug-in boards across five backplanes on a 190 by 130 cm acrylic panel that weighs roughly 20 kg. The instruction set supports 16 operations; the ALU adds, XNOR, increment, NOT, and carry, and a carry register lets the 8-bit machine chain 16-, 32-, 64-, and even 128-bit arithmetic, slowly.

However, there is no pipeline: six fetch cycles, one execute, one unused, and this is intentional, with Mike saying that the timing logic implemented is a bit too complex compared to the rest of the system.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

One design choice matters more than the rest: Mike keeps the high-tension supply below 100 V, well under the 150 V anode rating the Valve Museum datasheet lists for the 6N3P and far below the several hundred volts typical of legacy tube equipment. That is what lets him pack components 2 mm apart under each socket, allowing for a much more 'minimal' look than would otherwise be possible, and it is also why he can describe a wall of hot glass as nearly, but not quite, safe to touch.

About a minute after switch-on, the tubes glow red from the side, and the room fills with the smell of hundreds of double triodes burning off their dust. This gives it its 'pleasant homely aroma,' as the hobbyist puts it.

The machine currently drives a bank of ex-British Rail flip-digit displays, made by Bodet for 1980s station clocks, and is expected to power a rudimentary flight simulator system down the line.

The experiment has had its lows, though, with Mike reporting that it has gone "BANG" at least twice with earlier iterations; the first time he pulled plugs in a panic, and the second time his wife Judy carried on decorating the Christmas tree, later buying him a fire extinguisher as a precaution.

While the flight simulator is a work in progress, the aroma is here to stay, and Mike seems determined to see his project, which encapsulates tech from the previous century, through to completion.

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

***Follow TechRadar on Google News***and** add us as a preferred source** * to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

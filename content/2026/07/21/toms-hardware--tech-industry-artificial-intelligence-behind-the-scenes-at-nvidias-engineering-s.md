---
title: Behind the scenes at Nvidia's Engineering SuperLab — Vera Rubin NVL72 running
  OpenAI workloads, 800VDC demonstrated, and more
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/behind-the-scenes-at-nvidias-engineering-superlab-vera-rubin-nvl72-running-openai-workloads-800vdc-demonstrated-and-more
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-21T17:41:07Z'
published: '2026-07-21T00:00:00Z'
description: Where the sausage is… tested?
image: https://cdn.mos.cms.futurecdn.net/eXLFBd3VeLbbGiDKVLt9D8-1999-80.jpg
---

![Nvidia Vera CPU](https://cdn.mos.cms.futurecdn.net/eXLFBd3VeLbbGiDKVLt9D8.jpg) 

Nvidia invited a group of about a dozen journalists out to the company's HQ to learn more about its Vera CPU, as well as how it fits into the larger Vera Rubin NVL72 rack design at the heart of Nvidia’s next-gen agentic AI platform. Part of that was seeing Vera Rubin in action, not as a disassembled tray on stage or a rack with a few blinking lights at a trade show — real racks running real workloads in a (partially) real data center. And we got to see those racks in action at Nvidia’s Engineering SuperLab.

It’s not a proper data center, or at the very least, it’s a sub-optimal data center. Nvidia was clear that the Engineering SuperLab is built for engineers, allowing them to quickly stand up and swap out racks to see the hardware in action. You could sense a bit of insecurity in the air; if Nvidia were building a proper data center, it wouldn’t look like this. This lab is where the engineers live, and if you’ve ever been around a group of engineers with a lot of hardware to play with, you know that things aren’t always as tidy as you’d expect in a proper data center.

 ![NVL72 Vera Rubin Rack inside Engineering Lab](https://cdn.mos.cms.futurecdn.net/CpCTZFWLUCYjSFzbonFbqF.jpg) 


The SuperLab Nvidia showed us is one of four nondescript locations near Nvidia HQ. These locations haven’t, up to this point, been disclosed. Each of the four locations has popped up over the last two years, giving Nvidia some floor space to play with as it rolls out new hardware.

The hardware in question here is the Vera Rubin NVL72 rack, but we saw a few other demonstrations, as well. Most notably, Nvidia showed us a sidecar running 800VDC power into an NVL72 rack. Nvidia also laid out some parts, demonstrating the assembly process for a Vera Rubin tray, which slides together with various retention arms in a matter of minutes.

This is a look behind the scenes of our tour, how the Engineering SuperLab is set up, and some choice data center eye candy. We’ve published a full breakdown of the Vera CPU and how it fits into Nvidia’s larger AI infrastructure, which goes into the technical details of the platform. Here, we’re mainly giving you a peek behind the curtain.

## Nvidia Vera Rubin NVL72 running in the flesh

 ![An array of NVL72 Trays marked "Rosalind", running the OpenAI model.](https://cdn.mos.cms.futurecdn.net/bkdKuZkSenhzs9jGrMK6UN.jpg) 


Vera Rubin is in full production, and we’ve seen some short videos of racks being stood up in data centers. But this is our first look at a rack running a real workload in the flesh. Nvidia says the racks here are running some workloads for OpenAI, in fact, and as you can see from the image above, it looks like some trays are running OpenAI’s GPT‑Rosalind model.

On the front of each tray here, you can see the ports for the dual ConnectX-9 NICs, along with the Bluefield-4 DPU in the middle. Around the back is Nvidia’s NVLink spine, an almost mediaeval-looking contraption, with sharp pins that connect the various trays together. It houses 5,000 copper cables that measure over two miles in length, delivering up to 3.6 TB/s of bandwidth per GPU and 260 TB/s of scale-up bandwidth per rack, on Nvidia’s sixth-gen NVLink.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![A shot of the Nvidia NVL72 Racks](https://cdn.mos.cms.futurecdn.net/KtNFDPhEwA77Bs9dJascbn-1200-80.jpg) 

![A shot of the Nvidia NVL72 Racks, showing the rear](https://cdn.mos.cms.futurecdn.net/tdLZcL7TJthW3S7pfEKzcn-1200-80.jpg) 

![The NVL72 racks together in a row](https://cdn.mos.cms.futurecdn.net/6cgAnLRbyqBerj5SsqcpCo-1200-80.jpg) 

![The networking interfaces of the NVL72 rack](https://cdn.mos.cms.futurecdn.net/uzjrd7VkWqC7BYGrCE8GDo-1200-80.jpg) 

![A shot of the Nvidia NVL72 Racks](https://cdn.mos.cms.futurecdn.net/KtNFDPhEwA77Bs9dJascbn-1280-80.jpg) 

![A shot of the Nvidia NVL72 Racks, showing the rear](https://cdn.mos.cms.futurecdn.net/tdLZcL7TJthW3S7pfEKzcn-1280-80.jpg) 

![The NVL72 racks together in a row](https://cdn.mos.cms.futurecdn.net/6cgAnLRbyqBerj5SsqcpCo-1280-80.jpg) 

![The networking interfaces of the NVL72 rack](https://cdn.mos.cms.futurecdn.net/uzjrd7VkWqC7BYGrCE8GDo-1280-80.jpg) 

Each Vera Rubin NVL72 rack houses 18 compute trays and 9 NVLink switch trays, the latter of which orchestrate communication between the various trays to function as one large, unified system. Nvidia demonstrated the MGX NVL design for us, which is a single reference rack with 72 Rubin GPUs and 36 Vera CPUs. Nvidia’s MGX ETL design replaces the NVLink spine with either a Spectrum-X Ethernet spine or direct chip-to-chip spine for a scale-out system featuring up to 256 GPUs.

The business-end of things is around the back of the racks, though. Although the back is clear of cabling thanks to the NVLink spine, power and coolant delivery are still a major factor. The organized chaos of the piping and cabling you can see in the images below shows just how much goes into standing up even one rack, let alone dozens or hundreds in a data center.

![A shot of the cooling infrastructure around the NVL72 Vera Rubin setup](https://cdn.mos.cms.futurecdn.net/LLhgqLg62owdGUkBGPz4cX-1200-80.jpg) 

![Two pipes of liquid cooling going to an NVL72 tray](https://cdn.mos.cms.futurecdn.net/L8rDVrRwKgCSMfpugKTxpX-1200-80.jpg) 

![A shot of the cooling infrastructure beneath an NVL72 Vera Rubin tray.](https://cdn.mos.cms.futurecdn.net/5LcMsMkyiBFBCtVqs2SCqX-1200-80.jpg) 

![A shot of the cooling infrastructure around the NVL72 Vera Rubin setup](https://cdn.mos.cms.futurecdn.net/LLhgqLg62owdGUkBGPz4cX-1280-80.jpg) 

![Two pipes of liquid cooling going to an NVL72 tray](https://cdn.mos.cms.futurecdn.net/L8rDVrRwKgCSMfpugKTxpX-1280-80.jpg) 

![A shot of the cooling infrastructure beneath an NVL72 Vera Rubin tray.](https://cdn.mos.cms.futurecdn.net/5LcMsMkyiBFBCtVqs2SCqX-1280-80.jpg) 

Nvidia’s previous-gen GB200 and GB300 NVL72 racks featured hybrid cooling, but Vera Rubin trays are entirely cooled by liquid. There aren’t any fans, which Nvidia says could, eventually, lead to much quieter data centers. That wasn’t the case in the lab here, which still called for eye and ear protection. I didn’t have a decibel meter handy — imagine if I carried one around with me casually — but my guess is that it was somewhere around 80 to 90 decibels inside; louder than an A/C unit, but quieter than a motorcycle. That’s a fairly typical noise level for a data center.

 ![A show of the liquid-cooled portion of a disassembled Vera Rubin NVL72 tray](https://cdn.mos.cms.futurecdn.net/gYM8iWVbYcQd85T2x7qv7h.jpg) 


Regardless, Vera Rubin trays are entirely liquid cooled, with a process called “dry cooling.” Assuming the inlet temperature of the coolant is 45 degrees Celsius or less, Nvidia says it’s able to cool the entire system with a heat exchanger. If true, that would cut costly (in terms of power, space, noise, water consumption, and actual dollars) chillers out of the cooling equation.

Massive piping brings the coolant in (usually antifreeze or deionized water) at the top, and there are outlets at the bottom of the rack to move the warmed coolant out. Along the way are a series of inlet connections that allow trays to automatically hook into the cooling system, leaving just the main connections at the start and end of the loop. Nvidia has standardized everything on a Vera Rubin NVL72 rack with the Open Compute Project (OCP), even as far as shipping specifications. The company says just 47 minutes passes from when the truck pulls up to powering on the rack.

## 800VDC power for next-gen AI infrastructure

 ![A shot of the NVL72 Vera Rubin Sidecar for modern power delivery](https://cdn.mos.cms.futurecdn.net/QNH7b5Vwg4WVu2GkerDk.jpg) 


Nvidia also showed us an 800VDC “sidecar” in action. If you’re unfamiliar, Nvidia (along with other AI infrastructure companies) have been pushing for a new 800VDC power delivery system for modern data centers to reduce AC/DC conversion inefficiencies, as well as deliver the necessary wattage to racks without pushing into current ranges of thousands of amps.

A single Vera Rubin NVL72 rack can easily consume over 200 kW, which is a challenge for traditional power infrastructure in a data center. With current Grace Blackwell racks, power shelves convert the AC power coming into the facility (at 415V or 480V) to 48V/54V Direct Current for distribution within the rack. The problem here is pretty straightforward. If voltage stays constant, and wattage increases, then current also needs to increase. And more current means thicker bus bars, more conversion inefficiencies, and more rack space dedicated to power delivery.

Again, the solution that 800VDC represents is pretty straightforward. If wattage increases and current stays constant, voltage also has to increase. The idea is to convert AC power from the grid to DC power once, and then use a series of DC-to-DC converters within the rack, allowing for denser compute and better power efficiency.

![Populated NVL72 800VDC power ports on the back of the sidecar rack](https://cdn.mos.cms.futurecdn.net/6HkDjfQxWFw4kPYDSXWdAS-1200-80.jpg) 

![NVL72 800VDC power ports on the back of the sidecar rack](https://cdn.mos.cms.futurecdn.net/s9fL9aUYL5tCTXAXFfpGvR-1200-80.jpg) 

![NVL72 800VDC power plugs hanging in the SuperLab room](https://cdn.mos.cms.futurecdn.net/7xt6JbfgQZLohPJyGTkqBS-1200-80.jpg) 

![Populated NVL72 800VDC power ports on the back of the sidecar rack](https://cdn.mos.cms.futurecdn.net/6HkDjfQxWFw4kPYDSXWdAS-1280-80.jpg) 

![NVL72 800VDC power ports on the back of the sidecar rack](https://cdn.mos.cms.futurecdn.net/s9fL9aUYL5tCTXAXFfpGvR-1280-80.jpg) 

![NVL72 800VDC power plugs hanging in the SuperLab room](https://cdn.mos.cms.futurecdn.net/7xt6JbfgQZLohPJyGTkqBS-1280-80.jpg) 

This is not an easy problem to solve, as data centers need to change how power is brought into the facility, not just how it’s converted, stepped down, and moved around. Here, Nvidia showed off a sidecar, which is a rack filled solely with power equipment. This is a “retrofit,” as analyst firm *SemiAnalysis* calls it, representing the first in a series of transition phases to 800VDC. 415V/480VAC is still distributed throughout the facility, but it flows into this sidecar rather than power supplies within the rack. The sidecar rectifies the 415V/480VAC to 800VDC and feeds adjacent racks.

This is all an explanation to show some pretty interesting power infrastructure at play in this lab. Nvidia isn’t the first, nor only, company pushing toward 800VDC infrastructure, and companies like Google, Meta, and Microsoft have contributed to open sidecar designs like the Mt. Diablo spec. Still, it’s interesting to see one of these sidecars in action.

If you haven’t seen a peek behind the back end of a rack, you can see the large red connectors in the gallery above that bring power into the racks. You can also see the massive power cables and connectors at the rear of the 800VDC sidecar.

## Nvidia’s next-gen AI infrastructure laid out

At the front of the facility, Nvidia laid out all of the components of its next-gen AI infrastructure. There’s nothing here we haven’t already seen before, though it's normally seen buried in trade show displays or featured on stage during a keynote.

 ![Partially disassembled NVL72 Vera Rubin trays on a table.](https://cdn.mos.cms.futurecdn.net/Apvum5k2scH8X9HxoyRvAB.jpg) 


First is the Vera Rubin NVL72 tray itself, which you can see above sitting next to a GB300 tray. Both are DGX designs, meaning they’re fully built and integrated by Nvidia, and you can see just how stark of a difference there is in assembly right away. The Vera Rubin NVL72 tray features only two cables, no hoses, and no fans. At the rear where the two Super Chip boards live, Nvidia demonstrated a retention arm that allows the boards to slide in and out in a matter of seconds.

 ![NVL72 Vera Rubin tray retention arm](https://cdn.mos.cms.futurecdn.net/3DE9GjkBz4NVWhndWL7iAJ.jpg) 


The Vera Rubin tray is much cleaner, but it also makes better use of the space. It doesn’t include fans, which you can see take up a significant section in the middle of the tray in the GB300 design. With Vera Rubin, those fans are replaced with the thick midplane you can see above, offering a communication channel between the two ConnectX-9 NICs and Bluefield-4 DPU at the front of the tray.

 ![Communication channel between two ConnectX9-NICs and Bluefield-4 DPU](https://cdn.mos.cms.futurecdn.net/L6gbwuczcUsjhE8So92u5T.jpg) 


Holding one of the two cables inside of a Vera Rubin NVL72 compute tray is the busbar, which handles power routing for the different chips inside the tray.

The Vera Rubin NVL72 tray is, of course, not the only deployment of Nvidia’s next-gen AI hardware. The company also showed us a CPU-only tray with eight Vera chips, offering up to 256 chips within a rack. That gives us a closer look not only at the chip itself, but also the SOCAMM2 LPDDR5X memory system, offering similar density and modularity as traditional RDIMMs at a far lower power cost.

 ![SOCAMM 2 modules spotted on the Vera CPU tray](https://cdn.mos.cms.futurecdn.net/HLdVAsCHvfXFb5ZjVFtz2b.jpg) 


Although most of the modules were unlabeled, we were able to snag the picture you can see above showing where the modules came from. These are 128GB SOCAMM2 modules from Micron running at 6400 MT/s, and as you can see from the photo, the slots aren’t all populated. This is the big advancement with SOCAMM2, offering up modularity for a memory standard that is otherwise soldered.

 ![The NVLink Switches in the NVL72 tray](https://cdn.mos.cms.futurecdn.net/7dWnonXj75WzEpWSkwVddk.jpg) 


Nvidia’s NVLink handles scale-up communications, split across NVLink switches in the rack and the NVLink spine that you can see above. Nvidia describes sixth-gen NVLink as “putting the oven in the car.” Its goal is to get all of the chips in a rack communicating with each other, ensuring critical operations (like baking the pizza) happen as close to the destination as possible.

 ![Spectrum-X CPO Switch Tray](https://cdn.mos.cms.futurecdn.net/MjYKfRTc4u5PxGQsgU7oK7.jpg) 


Scale-out communication, on the other hand, is handled with ConnectX-9 NICs in the tray and the Spectrum-X CPO (co-packaged optics) switch tray. The Spectrum-X switch tray is massive, and it’s a good illustration of just how much physical space is dedicated to communication (over raw compute) in a modern AI data center.

 ![Spectrum-X CPO tray close up](https://cdn.mos.cms.futurecdn.net/w7DdReimihZtKsyzACqtjC.jpg) 


Of course, the size of the switch tray depends on how wide the scale-out infrastructure is. Nvidia also showed a smaller Spectrum-X CPO tray for smaller deployments. That's all we managed to see at Nvidia's AI data center SuperLab. Vera Rubin is in production, and will roll out in the second half of 2026.

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

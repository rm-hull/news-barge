---
title: Micron plans to use wafer bonding and High-NA EUV for next-gen DRAM — company
  also developing vertical high-bandwidth memory and vertical edge inference memory
  integrated directly on top of processors
source_url: https://www.tomshardware.com/pc-components/dram/micron-plans-to-use-wafer-bonding-and-high-na-euv-for-next-gen-dram-company-also-developing-vertical-high-bandwidth-memory-and-vertical-edge-inference-memory-integrated-directly-on-top-of-processors
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-26T20:36:11Z'
published: '2026-10-26T00:00:00Z'
description: Put memory on top of processors too.
image: https://cdn.mos.cms.futurecdn.net/NXXMYUVnvu4xUCtWoHqW48-2560-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Anton Shilov
- Scott DeBoer
- Tom
locations:
- Albany
organisations:
- ASIC
- Albany NanoTech
- CTO
- Get Tom's Hardware
- Google News
- HBM
- HBM4
- Micron
- Tom’s Hardware
- cHBM
- vHBM
- zeta angstrom
---

![Micron](https://cdn.mos.cms.futurecdn.net/NXXMYUVnvu4xUCtWoHqW48-1920-80.jpg)

Having jettisoned 4F2 memory cells from its roadmap, Micron must use different methods to continue scaling its DRAM devices in the coming years to keep up with rivals planning to use smaller DRAM transistors towards the end of the decade. Instead, Micron intends to introduce wafer bonding with its upcoming 1ε DRAM process technology and adopt High-NA EUV lithography for subsequent generations. Meanwhile, the company is developing new types of memory, including vertical high-bandwidth memory (vHBM) and vertical edge inference memory (vEIM), which will be integrated directly on top of processors.

![a snippet from the HBM roadmap article](https://cdn.mos.cms.futurecdn.net/JY32VXJVXoHUR8NRV2Kveb-1200-80.png)

"DRAM is nearing atomic limits at this point," said Scott DeBoer, president and chief technology and products officer at Micron, during the company's event this week. "Although we have confidence in several more planar nodes, we are very focused on making sure that we introduce 3D DRAM at the optimal time from a cost and performance point of view."

## Wafer bonding, High-NA EUV, and new materials

Micron's current 1γ DRAM process is already in high-volume manufacturing, whereas its successor, 1δ, is scheduled to enter volume production in the second half of 2027. The latter promises a mid-20% increase in bit density and is optimized for future AI memory products, including HBM5, vHBM, and vEIM. Beyond 1δ, Micron plans to introduce wafer bonding with its 1ε process, which is currently under development. However, the company has not disclosed how it intends to implement wafer bonding or what improvements it expects from the technology.

![Micron](https://cdn.mos.cms.futurecdn.net/v9TyiXWTXYve2ddGf5X6gP-1200-80.jpg)

For subsequent generations — ζÅ and ηÅ — Micron plans to adopt High-NA EUV lithography (ζÅ, zeta angstrom, Micron's 1st Generation sub-10nm-class DRAM node) and new materials (ηÅ, eta angstrom, Micron's 2nd Generation sub-10nm-class DRAM node) to continue shrinking DRAM cells. For many of its upcoming fabrication technologies that will be used over the next five to 10 years, Micron is also collaborating with Albany NanoTech. Of course, as with all organizations like Albany NanoTech, we are mostly talking about fundamental, or pre-competitive, IP that could be used for DRAM production at some point.

"Albany NanoTech, our announced focus on advanced lithography [is] really driving High-NA EUV roadmap for DRAM," said DeBoer. "In particular at Albany with our team there, focused on the next five to ten years."

![Micron](https://cdn.mos.cms.futurecdn.net/UbtwcKeGtzdNnMfdkrZxfP-1200-80.jpg)

Micron is also developing 3D DRAM technologies and lists two generations — 3D1 and 3D2 — in its roadmap already. However, the company has not disclosed its architectures or launch schedules, as it intends to introduce 3D DRAM only when the technology offers sufficient advantages in manufacturing costs, complexity, and performance over conventional planar DRAM.

"When we look at three 3D DRAM we have that on the roadmap, as I mentioned, and it is shown here in between one zeta and one eta," said Micron's CTO. "But in reality, this is a parallel path, and we will implement it [3D DRAM] in a fashion that is ideal for cost, complexity, and device performance."

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

## Going vertical, becoming critical

Beyond developing new process technologies for its upcoming DRAM products, Micron is also working on all-new types of DRAM products that are tailored for very specific use cases, including vertical HBM (vHBM), vertical edge inference memory (vEIM), and various custom HBM (cHBM) implementations.

![Micron](https://cdn.mos.cms.futurecdn.net/TkDKNMhj6Q6pttJuYkNtZ7-1200-80.jpg)

vHBM will place memory stacks directly on top of processors (such as AI accelerators and AI GPUs) rather than next to them. This approach promises substantially lower latencies and higher bandwidth thanks to shorter connections. However, placing memory above a processor creates significant thermal challenges and limits the number of memory stacks that can be integrated on top of an ASIC. Therefore, Micron expects vHBM to complement conventional HBM, which will continue to provide the bulk of memory capacity in many AI accelerators.

![Micron](https://cdn.mos.cms.futurecdn.net/Q4NcoBESJKUAP5x4PPaxg7-1200-80.jpg)

Another technology under development is vertical edge inference memory (vEIM), which shares architectural and packaging characteristics with vHBM but targets different applications. Whereas vHBM prioritizes maximum bandwidth for high-performance AI accelerators, vEIM is focused on energy efficiency for edge AI processors used in autonomous vehicles, robotics, and other power-constrained devices. Nonetheless, even the 1st Generation vEIM targets formidable 2 TB/s bandwidth at <1pJ/bit energy, which is in line with what HBM4 currently offers (at 8 GT/s over a 2,048-bit interface). Micron intends to optimize these products with customers according to their bandwidth, capacity, and power requirements.

![Micron](https://cdn.mos.cms.futurecdn.net/veCGVZJeuXw3yRGXwR74m7-1200-80.jpg)

Both vertical memory architectures will require advanced packaging technologies, particularly hybrid bonding, which enables much denser connections than conventional microbumps. Thermal management will also be critical, especially for vHBM. To meet cooling requirements, Micron is developing specialized heat-spreading structures to transfer heat from hot regions of memory base dies through the DRAM stacks.

The company has not disclosed when vHBM, vEIM, or cHBM will enter commercial production. What is important about the development of such types of memory is that it indicates that future improvements in memory performance will increasingly depend on advanced packaging and closer integration with processors, which will require collaboration between DRAM makers and logic developers. In turn, this transforms memory from a commodity to a critically important ingredient of an ASIC design.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV-140-80.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

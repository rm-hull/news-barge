---
title: Synopsys validates a PCIe 6.0 PHY inside a face-to-face 3D stack at 64 GT/s
  — says it got there by pulling apart an existing 2D test chip
source_url: https://www.tomshardware.com/tech-industry/semiconductors/synopsys-validates-a-pcie-6-phy-inside-a-face-to-face-3d-stack
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-20T16:48:02Z'
published: '2026-08-20T00:00:00Z'
description: The 5nm test chip routes signals through TSVs to the package.
image: https://cdn.mos.cms.futurecdn.net/7CaVRhQ5giQeWSSo2AjMBF-2000-80.jpg
---

![Synopsys](https://cdn.mos.cms.futurecdn.net/7CaVRhQ5giQeWSSo2AjMBF.jpg) 

Synopsys has published silicon results for what it calls the first 3D PCIe 6.0 test chip, a 5nm PHY built into a face-to-face stacked package that runs 64 GT/s per lane and up to 128 GB/s across an eight-lane link using PAM4 signaling, with receiver eyes clearing the standard's bit error rate requirement. The company says it got there by pulling apart an existing 2D PCIe 6.0 test chip, adding through-silicon vias, and redoing circuit design and signoff against 3D process design kits, according to its blog post.

 ![a snippet from the HBM roadmap article](https://cdn.mos.cms.futurecdn.net/JY32VXJVXoHUR8NRV2Kveb.png) 


In monolithic chips, PCIe PHYs sit at the perimeter of the die, right next to the package I/O connections, helping keep traces to the substrate short so attenuation and reflections remain manageable. A 2.5D package preserves that layout by parking the PHYs along the outer edge of the outermost chiplets. Face-to-face hybrid bonding removes the option. The bottom die is flipped so its redistribution layer meets the redistribution layer of the logic die above it, which leaves the PCIe PHYs facing away from the substrate they need to reach. Instead, the signals travel down through vias cut into the silicon.

Every TSV passes through active silicon and needs a buffer around it, so the vias can't be dropped wherever the PHY happens to sit. "You rarely drill straight down into the package substrate," Manmeet Walia, executive director of product management at Synopsys, said to *Electronic Design*, which reported that routing has to climb to one of the upper metal layers and reverse direction before descending.

Walia told the publication that electromigration and layout rules change substantially in 3D, that via count is a tradeoff between bandwidth and signals corrupting each other, and that customer logic sitting over the PHY's path down to the substrate is a challenge that Synopsys expects to work through iteratively, design by design. PAM4 leaves less room for that kind of error than the NRZ signaling used through PCIe 5.0, since it packs two bits into each symbol.

Fujitsu's Monaka processor takes the opposite approach, instead stacking four N2 compute chiplets carrying 144 Armv9 cores face-to-face on N5 SRAM chiplets using hybrid copper bonding, then putting the memory controllers and the PHYs for its 12 DDR5 channels on a separate and comparatively large I/O die rather than inside the bonded stack.

PCIe generations arrived roughly five to seven years apart for most of the standard's life and now release about every two years, with the Gen 8 specification due in 2028 at 256 GT/s per lane. Walia told *Electronic Design* that a further shift is coming with 3.5D packaging, where the PCIe PHYs get stripped out of the bottom die entirely, replaced with UCIe, and relocated to a side chiplet on the interposer that acts as a multi-protocol hub for Ethernet, PCIe, and CXL. Synopsys hasn't put a date on that. Its blog says leading-edge customers are evaluating angstrom-class process technologies for the top dies in their stacks.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.

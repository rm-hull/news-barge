---
title: Nvidia's Kyber rack for Rubin Ultra reportedly delayed to 2028, stopgap solution
  also axed due to customer pushback — Analyst firm SemiAnalysis says PCB midplane
  problems led to the delay
source_url: https://www.tomshardware.com/pc-components/gpus/nvidias-kyber-rack-for-rubin-ultra-slips-to-2028
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-06T18:20:05Z'
published: '2026-07-06T00:00:00Z'
description: Leaving Nvidia without a proven way to scale Rubin Ultra past its current
  Oberon rack.
image: https://cdn.mos.cms.futurecdn.net/qH9XqmnqHfwSwBhpoXCho6-2560-80.jpg
---

![Nvidia Rubin Ultra with NVL576 Kyber racks and infrastructure](https://cdn.mos.cms.futurecdn.net/qH9XqmnqHfwSwBhpoXCho6.jpg) 

Nvidia reportedly won't ship its Kyber NVL144 rack until 2028, a delay of more than 12 months that pushes the cabinet meant for 2027's Rubin Ultra GPUs into the following year, according to a *SemiAnalysis* thread on X. The holdup is ostensibly being caused by manufacturing challenges with a PCB midplane that connects eight Oberon racks between the NVSwitches, which Nvidia calls the orthogonal backplane. Nvidia is also understood to have killed NVL72x2, a stopgap rack designed to tide customers over, and that no proven alternative is now available to widen Rubin Ultra's scale-up in 2027.

MASSIVE DELAY: Just 3 months after Jensen demoed Kyber NVL144 at GTC, it has faced major setbacks and has been delayed by more than 12 months, pushing it back to 2028. Below, we explain why Kyber has faced massive delays and why NVIDIA’s NVL72x2 back-to-back rack architecture was… pic.twitter.com/VYduxnu01BJuly 5, 2026


The orthogonal backplane sits between Kyber's vertically mounted compute trays and the switch trays behind them, replacing the cable harnesses of earlier racks with a rigid board that carries the all-copper NVLink fabric. Kyber runs liquid cooling by default and stacks 144 Rubin Ultra packages, double the 72 packages in a current Oberon NVL72 rack. Every GPU-to-GPU link inside the cabinet runs through that board, and copper traces lose signal integrity as layer counts increase, alongside power delivery and thermal design challenges. Jensen Huang held up the gray backplane on stage at GTC back in March.

Trade analyses of the board describe three 26-layer sections laminated into one 78-layer stack close to a square meter in area, with trace spacing at or below 25μm and impedance held within a tolerance of 5% to keep 448 Gb/s-class signaling intact. A cabled version of the same interconnect would need upward of 20,000 discrete cables, which is why Nvidia is moving the wiring onto a single passive board.

NVL72x2 would have bolted two Oberon racks back-to-back to reach Kyber-class density over copper NVLink, per *SemiAnalysis*, which said Nvidia abandoned the stopgap after its largest customers balked at running two linked cabinets as a single unit. NVL576, a separate configuration tying eight racks together through co-packaged optics, is likely to slip too or ship in low volume until that optical technology matures.

These cancellations leave Nvidia with "no proven solution to expand the scale-up world size for Rubin Ultra," meaning the largest single Rubin Ultra domain in 2027 could match, but not exceed, what Oberon already delivers.

Nvidia dropped the quad-chiplet Rubin Ultra GPU for a dual-chiplet part last week over manufacturing execution concerns, halving the accelerator's per-package compute. *SemiAnalysis* has also placed a fully production-ready co-packaged optics NVSwitch no earlier than the Feynman generation that follows Rubin, which leaves copper as the only near-term solution for linking Rubin Ultra at rack scale and thereby puts even more weight on the PCB midplane.

The delay only applies only to the Rubin Ultra phase and its Kyber rack. Nvidia's 2026 Rubin GPUs, which reuse the current Oberon rack, aren't part of the reported delay. We've reached out to Nvidia for comment.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.

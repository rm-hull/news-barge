---
title: Modal taps Nvidia Vera CPUs after firm's internal tests show 2x throughput
  over Intel and AMD chips — AI agentic workflows said to favor Arm chips, but firm
  will keep x86 chips deployed in heterogeneous server fleet
source_url: https://www.tomshardware.com/pc-components/cpus/nvidia-vera-cpu-deployed-at-ai-startup-modal-alongside-existing-x86-fleet-internal-testing-showed-2x-throughput-compared-to-amd-and-intel
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-20T14:27:33Z'
published: '2026-10-20T00:00:00Z'
description: Modal plans to use Nvidia's Vera CPUs due to performance advantages,
  but will keep AMD and Intel CPUs in the fleet.
image: https://cdn.mos.cms.futurecdn.net/vnqdtRupVqWHAik43ZWctH-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Anton Shilov
- Erik Bernhardsson
- Modal
- Tom
- Vera
locations: []
organisations:
- AI
- AMD
- Accel
- Google News
- ISA
- Intel
- Modal
- Nvidia
- Olympus
- Reuters
- Tom’s Hardware
- Vera
---

![Micron](https://cdn.mos.cms.futurecdn.net/vnqdtRupVqWHAik43ZWctH-1920-80.jpg)

Nvidia has earned billions selling AI accelerators, but with the emergence of agentic AI, CPUs are going to play a considerably more significant role than before, which creates new opportunities for the company. *Reuters* reports that Nvidia has secured a major design win with its Vera CPUs with AI cloud provider Modal. According to Modal, preliminary evaluations showed that Vera could deliver twice the throughput of its existing AMD and Intel processors, although the company does not intend to cease using CPUs from its current suppliers.

![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB-1200-80.jpg)

Modal provides cloud infrastructure that enables AI developers to deploy AI agents that can perform complex operations autonomously over extended periods. Such workloads require substantial CPU resources for software execution, data processing, and other tasks that cannot be efficiently handled by GPUs. Modal currently relies exclusively on AMD and Intel processors for these operations, but its tests indicate that Nvidia's new Vera CPUs could significantly improve performance in its specific workloads. Of course, since Vera is based on an Arm instruction set architecture, Modal's decision to adopt Vera will require substantial modifications to its software. Nevertheless, Modal believes that the potential performance improvements justify the additional engineering effort.

The reported 2x throughput advantage is particularly interesting because agentic AI workloads can involve numerous independent tasks that compete for CPU cores, cache capacity, and memory bandwidth. However, Modal has not disclosed detailed benchmark configurations it used, specific AMD and Intel processor models, or performance-per-watt figures. Consequently, it remains unclear whether Vera's advantage is enabled by advantages of its Arm v9.2-based Olympus CPU cores that can decode and execute up to 10 instructions per cycle, its memory subsystem with 1.2 TB/s of bandwidth, or other architectural characteristics. Also note that tests compared Vera against currently available AMD and Intel processors rather than their upcoming generations that will compete against Vera in the coming years.

Since Modal cannot port all of its software to Arm ISA overnight, the company will continue using x86 CPUs from AMD and Intel, according to Modal chief executive Erik Bernhardsson. Rather than sticking to one ISA for everything, Modal intends to operate a heterogeneous server fleet and select the most suitable processors for each workload. Naturally, the company intends to evaluate upcoming AMD and Intel processors once they become available to make its choices in the future.

For Nvidia, the agreement represents a major step toward making Vera a standalone server processor that commands a major share of the server market. The company expects Vera sales to generate at least $20 billion during its current fiscal year and estimates the potential total available market for these CPUs is approximately $200 billion. The company is on track to sell at least four million Vera CPUs in fiscal 2026.

The announcement comes shortly after Modal secured $750 million in financing led by Accel, which valued the company at $15.75 billion. Modal expects its annual revenue to reach $1 billion within the next year. The company's service consumption has increased 3X in the last 12 months, while revenue has surged more than 15 times compared with the previous year, *Reuters* reports.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV-140-80.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

---
title: TSMC's A14 1.4nm-class node is ready for chip design — Boost Cells promise
  14% performance uplift or 23% power cut over N2P
source_url: https://www.tomshardware.com/uk/tech-industry/semiconductors/tsmcs-a14-1-4nm-class-node-is-ready-for-chip-design-boost-cells-promise-14-percent-performance-uplift-or-23-percent-power-cut-over-n2p
source_site: Tom's Hardware
source_slug: toms-hardware
description: TSMC announces availability of its version 0.9 process design kit for
  its A14 manufacturing technology. Availability of the v0.9 version of PDK signals
  that the fabrication process is generally ready for design and production.
image: https://cdn.mos.cms.futurecdn.net/YAQU3zRSbuCHbUYm5L4oD4-1920-80.jpg
published: '2026-11-26T00:00:00Z'
scraped_at: '2026-11-26T16:50:59Z'
categories:
- Technology & Software
- Hardware
people:
- Anton Shilov
- Tom
- Wei
locations: []
organisations:
- A13
- A14
- Boost Cells
- Cadence
- Get Tom's Hardware
- Google News
- IP
- Intel
- N2
- N2P
- NanoFlex Pro
- PDK
- Siemens EDA
- Synopsys
- TSMC
- Tom’s Hardware
---

![TSMC](https://cdn.mos.cms.futurecdn.net/YAQU3zRSbuCHbUYm5L4oD4-1920-80.jpg)

TSMC announced at its 2026 Europe OIP Ecosystem Workshop this week that its A14 (1.4nm-class) fabrication technology is ready for customer design work and version 0.9 of its process design kit (PDK) is ready. TSMC also detailed Boost Cells, a way for the new node to deliver 14% higher performance compared to N2P, and how customers can migrate their designs to A13 in the future. Furthermore, Cadence and Synopsys have both completed full design-flow certification on an Arm Cortex-A725 CPU core, which gives chip designers two validated toolchains to build their 14A chips.

"A14 0.9 design ecosystem and the PDK are ready for design in," a TSMC spokesman said on stage at the 2026 Europe OIP Ecosystem Workshop.

## Boost Cells and Low-Power Cells provide further improvements

A14 uses TSMC's 2nd Generation nanosheet transistors and its NanoFlex Pro standard cell architecture, which supports Boost Cells to enable higher performance as well as Low-Power Cells to reduce power consumption. Designers can place compact high-speed Boost Cells on critical paths (which resembles Intel's Turbo Cells supported by its 14A fabrication technology) and use Low-Power Cells with narrower nanosheets for general logic or parts of the chip that do not need high performance.

In general, TSMC promises A14 with NanoFlex Pro optimizations to deliver a 14% speed gain at the same power or a 23% reduction in total power at the same speed compared to N2P with NanoFlex. In a separate comparison against baseline N2P, TSMC put A14 at 50% higher energy efficiency, 22% higher drawn transistor density, and 23% higher logic density.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| TSMC process comparison against baseline N2P |  |  |  |  |  |
| Metric | N2P | N2P NanoFlex | N2U NanoFlex Pro | A14 NanoFlex Pro | A13 NanoFlex Pro |
| Energy efficiency | Baseline | +12% | +23% | +50% | +58% |
| Transistor density (drawn) | Baseline | +11% | +16% | +22% | +22% |
| Logic density (silicon) | Baseline | 0% | +2% | +23% | +30% |

A14 also gives customers a path to A13. The foundry says customers can cut die area by about 6% without changes to their A14 design flow. Furthermore, to take even more advantage of A13 and get 5% higher energy efficiency, all the designers have to do is re-engineer the M0 metal layer, reshape OD, and use VT Flex cells (cells that can use different threshold-voltage options for their NMOS and PMOS transistors).

TSMC expects to start risk production using A14 in the second half of 2027, with mass production following in the second half of 2028. Chief executive C.C. Wei said in October that the company had already seen more customer activity on A14 than on N2 at a comparable stage of development and expects A14 to become a bigger node than its 2nm-class predecessor. A13 is set to reach the high-volume manufacturing stage in the second half of 2029.

## A14 PDK and ecosystem nearly ready

One of the key parts of the TSMC announcement is the readiness of the 0.9 version of the PDK and the electronic design automation (EDA) tools ecosystem. What matters about v0.9 is that the industry considers this revision ready for design work, which means that customers can start designing chips with confidence that they will meet their performance and power goals. Furthermore, TSMC has validated two complete flows — by Cadence and Synopsys for A14, with Siemens EDA's flow coming later.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

"Today, both Cadence and Synopsys have successfully completed full design flow certification for the Cortex-A725," the spokesman said. "This program tests the full chain of implementation and sign-off EDA tools with TSMC foundation IP. We expect it to benefit the entire A14 design community. This table summarizes A14 v0.9 certification for our three major EDA partners, Cadence, Synopsys, and Siemens, across automatic placement and routing, library characterization, timing, power, EM/IR, and other sign-off flows. Siemens is targeting Q4 for transistor-level EM/IR certification. So the A14 v0.9 design ecosystem and the PDK are ready for design-in.

|  |  |  |  |
| --- | --- | --- | --- |
| TSMC A14 v0.9 EDA ecosystem readiness |  |  |  |
| Capability | Cadence | Synopsys | Siemens EDA |
| Automatic placement and routing (APR) | Certified | Certified | — |
| Library characterization | Certified | Certified | — |
| Timing analysis | Certified | Certified | — |
| Power analysis | Certified | Certified | — |
| Electromigration and voltage-drop analysis (EMIR) | Certified | Certified | — |
| Design rule checks (DRC) | Certified | Certified | Certified |
| Dummy fill | Certified | Certified | Certified |
| Layout-versus-schematic checks and layout parasitic extraction (LVS/LPE) | Certified | Certified | Certified |
| Resistance and capacitance extraction (RC) | Certified | Certified | Certified |
| Custom design | Certified | Certified | — |
| Transistor-level EMIR | Certified | Certified | Work in progress |
| Transistor-level timing analysis | — | Certified | — |
| Simulators | Certified | Certified | Certified |
| Certified categories | 12 of 13 | 13 of 13 | 5 of 13 |

As of October 1, Cadence, Synopsys, and Siemens EDA all had A14 v0.9-certified tools for design rule checks, dummy fill, layout-versus-schematic verification and layout parasitic extraction (LVS/LPE), resistance and capacitance extraction, and circuit simulation. Cadence and Synopsys also had certified tools for automatic placement and routing, library characterization, timing and power analysis, custom circuit design, and electromigration and voltage-drop (EM/IR) analysis at both the design and transistor levels.

Synopsys alone had certified transistor-level timing analysis, which gave it coverage across all 13 categories versus 12 for Cadence and five for Siemens EDA. Cadence and Synopsys also completed full-flow certification on an Arm Cortex-A725 design with TSMC foundation IP, from synthesis and physical implementation through electrical, physical, and thermal sign-off. Siemens EDA's transistor-level EM/IR certification is in progress and is due in Q4 2026.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV-140-80.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

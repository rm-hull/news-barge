---
title: Researchers turn HBM on its side to tackle AI memory’s heat wall — Korean V-Die
  and Japanese MOSAIC designs promise higher bandwidth, denser stacks, and cooler
  future GPUs
source_url: https://www.tomshardware.com/tech-industry/semiconductors/researchers-turn-hbm-on-its-side-to-tackle-ai-memorys-heat-wall-korean-v-die-and-japanese-mosaic-designs-promise-higher-bandwidth-denser-stacks-and-cooler-future-gpus
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-10T14:48:36Z'
published: '2026-07-10T00:00:00Z'
description: Technologies not yet proven as viable HBM alternatives
image: https://cdn.mos.cms.futurecdn.net/gkqYGfN48d6aHpbGDsYYvG-826-80.jpg
---

![hbm](https://cdn.mos.cms.futurecdn.net/gkqYGfN48d6aHpbGDsYYvG.jpg) 

Researchers in Korea and Japan have presented two separate memory-integration proposals that aim to increase HBM (High-Bandwidth Memory) capacity and bandwidth without trapping more heat inside ever-taller DRAM (Dynamic Random Access Memory) stacks, one of the most pressing challenges facing future AI accelerators. Presented at the 2026 IEEE/JSAP Symposium on VLSI Technology and Circuits held in June, the two approaches — V-Die from a Korean research collaboration and MOSAIC from a University of Tokyo-led group — both explore the same broad idea of standing DRAM memory dies on their edges instead of stacking the memory dies only upward like conventional HBM.

The Korean proposal, called Vertical-Die (V-Die), was presented by researchers at the Ulsan National Institute of Science and Technology (UNIST). The design rotates custom DRAM dies upright, drops through-silicon vias to free die area for more memory cells, gives each die its own bottom-edge I/O, and runs liquid-cooling channels between adjacent dies. In simulations against an HBM4 system at equal capacity, the V-Die system reportedly achieved 540 tokens per second on a GPT-3-sized workload, compared to 296 tokens per second for HBM4.

 ![HBM3E vs HBM4](https://cdn.mos.cms.futurecdn.net/xi79WuWDZXzix4Fc7sXNMn.png) 


The Japanese project, MOSAIC, takes a similar “sideways stack” idea but focuses on the practical difficulty of connecting so many vertical dies to a GPU or package substrate. Presented by University of Tokyo researchers, the MOSAIC work uses orthogonal die stacking and a contactless die-to-die interface, in which data is transferred through tiny inductive coils rather than requiring every signal pad to land perfectly on a physical contact. The researchers say the prototype interface achieved up to 4 Gbps per channel, while the memory structure could double HBM4-class capacity in a DRAM-on-GPU configuration.

Both projects aim to solve the growing problem of AI chips being held back by memory. Modern accelerators can perform enormous amounts of computation, but large, powerful models depend on moving huge amounts of data between memory and compute. This is why HBM has become one of the defining technologies of modern AI hardware.

The technology addresses the memory wall by stacking multiple DRAM dies vertically on a base die and placing that stack very close to the processor. Nvidia's Blackwell Ultra B300, for instance, carries up to 288GB of HBM3E memory, without which much of the silicon would sit idle waiting for data. The dies are connected via through-silicon vias (TSVs) — tiny vertical channels etched through the silicon and filled with metal.

The stack then communicates with the GPU over an extremely wide interface, often routed through a silicon interposer or an advanced package. This is the core reason HBM can deliver terabytes per second of bandwidth: it uses a very wide, very short data path instead of sending memory traffic across a motherboard, as with conventional DIMMs (Dual In-line Memory Modules), physical sticks of RAM used in computers.

However, that same structure creates several problems. While taller stacks add more capacity, they also make it harder to remove heat. Heat generated in the lower dies and at the high-speed interface must pass through layers of silicon, bonding materials, underfill, and package structures before it reaches a heat spreader. Furthermore, TSVs consume die area that could otherwise be used for memory cells, and as bandwidth rises, more routing and I/O place additional pressure on both signal integrity and packaging costs.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

HBM4, the latest generation of HBM, addresses a number of these challenges. Meanwhile, companies such as SK hynix, Samsung, and Micron are racing to improve speed, capacity, base-die performance, and thermal management. SK hynix has already shown iHBM, which embeds cooling elements into the HBM interface area, and Samsung has shown an HBM5 mockup with Heat Path Block cooling to more directly extract heat from the stack. However, they all retain the same upward stacking structure.

This convention is what V-Die and MOSAIC are challenging. By standing DRAM dies upright, the researchers expose far more silicon surface area to the cooling path. In theory, this turns the memory stack into something closer to a heat-sink fin array, where heat can move laterally and escape more directly instead of being trapped in the middle of a thick vertical pile. It also opens the door to new connection schemes along the bottom or side of each die, rather than forcing every die to communicate through TSVs running vertically through the stack.

For V-Die, the key shift is removing TSVs from the memory dies and replacing them with bottom-edge connections. Each DRAM die gets its own I/O along the bottom edge and connects directly to the substrate, with links reportedly spaced every 20 microns. The team says this layout gives four times as many connections as HBM4 and cuts memory read time by 37%, although some signals must travel farther across the package to reach the processor.

Cooling is the other half of the V-Die argument. The proposal places microfluidic cooling channels between adjacent upright DRAM dies, allowing coolant to dissipate heat closer to its source. According to the researchers, this could keep the stack around 45°C, far below the 80°C-plus range associated with dense HBM systems. In a simulated 16-die stack matched to H100-class hardware on a GPT-3-scale model, V-Die hit 540 tokens per second, compared to HBM4's 296, and cut first-token latency by 32%, or about 24 milliseconds.

MOSAIC, meanwhile, is focused on making the sideways stack manufacturable. Because the dies are assembled flat and then turned on edge, even a few microns of die-thickness variation across dozens of dies can add up to an alignment miss where the signal pads no longer land. The Japanese team’s answer is a contactless interface based on inductive coupling. One side of the memory die carries oblong coils, while a corresponding set of coils sits on the substrate or mating chip. Current in one coil induces a signal in the other, allowing data to cross the small gap without a direct metal-to-metal signal contact. This eliminates the need for precise overlapping, giving the package greater tolerance for assembly variation. Power, which requires fewer, larger connections than data, can still be supplied via physical contacts on the sides of the memory cube.

The VLSI MOSAIC prototype achieved up to 4 Gbps per channel and demonstrated TSV-free 3D integration for a memory-on-GPU layout. The team says the approach can enable twice the memory capacity of HBM4 without significantly increasing peak temperature. A related bump-MOSAIC hardware demonstration at ECTC used 100-micron-pitch microbumps, achieved stacking alignment within 6 microns as verified by X-ray CT, and showed a configuration with three times the thermal conductivity of conventional stacking while adding up to 30% more memory capacity.

While the results look promising, neither V-Die nor MOSAIC is close to replacing commercial HBM. Neither is close to shipping. V-Die is still a proposed architecture, with a prototype in the works to validate its thermal and electrical behavior; MOSAIC has proof-of-principle hardware, but the researchers have yet to show it scales to commercial DRAM capacity, yield, cost, and reliability.

Still, any viable solution to the multifaceted AI memory problem is a welcome development. SoftBank and Intel’s Z-Angle Memory (ZAM) and NEO Semiconductor’s 3D X-DRAM — both still in development — aim to solve the constraints of conventional memory. Meanwhile, the overall market is already feeling the squeeze on price and availability, even as memory makers divert capacity toward the more lucrative AI HBM and server products, driving consumer RAM prices even higher.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.

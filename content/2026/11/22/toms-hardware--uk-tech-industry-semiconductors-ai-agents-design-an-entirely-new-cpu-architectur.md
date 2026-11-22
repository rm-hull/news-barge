---
title: AI agents design an entirely new CPU architecture from scratch, startup claims
  — Frostbite posts 4.59x the performance per watt of an in-order core in pre-silicon
  tests
source_url: https://www.tomshardware.com/uk/tech-industry/semiconductors/ai-agents-design-an-entirely-new-cpu-architecture-from-scratch-startup-claims-frostbite-posts-4-59x-the-performance-per-watt-of-an-in-order-core-in-pre-silicon-tests
source_site: Tom's Hardware
source_slug: toms-hardware
description: Its lead shrinks to 3.83x on the 15 workloads without AI tuning.
image: https://cdn.mos.cms.futurecdn.net/E6ZGdHQ5GTZE5a3yPzPScR-2560-80.jpg
published: '2026-11-22T00:00:00Z'
scraped_at: '2026-11-22T19:32:10Z'
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Fibonacci
- Shane Downing
- Tom
locations:
- Cambridge
- U.K
organisations:
- AI
- ASL
- Architect Labs
- CPU
- Frostbite
- Get Tom's Hardware
- Google News
- PARSEC
- PDF
- Palo Alto
- RTL
- Redwood
- SPEC
- Shane Downing
- TSMC
- Tendrils Compute
- Tom’s Hardware
---

![Stylized render of a chip layout in blue, with red hotspots and connecting lines across a grid of tiles](https://cdn.mos.cms.futurecdn.net/E6ZGdHQ5GTZE5a3yPzPScR-1920-80.jpg)

Architect Labs, a Palo Alto startup, said in a research blog post that its AI systems discovered, designed, and verified Frostbite, a general-purpose CPU with a new instruction set “built from the ground up.” Across 25 workloads, a four-tile Frostbite cluster delivered 4.59 times the performance per watt of a similarly sized “silicon-proven” dual-issue, in-order CPU core. Those numbers come from a simulated 7nm design that has not yet been made in silicon, and the company says it can’t name the comparison core for legal reasons.

Conventional CPUs have hardware that “rediscovers, at runtime, which instructions actually depend on each other.” Multicore designs also need deep cache hierarchies and coherence protocols, which keep every core’s view of shared memory consistent, but scale poorly and cost area and power. Architect Labs’ alternative is what it calls “multithreading for free,” where the program itself exposes the parallel work, without threads, locks, or out-of-order hardware required for that discovery.

Frostbite’s programs are compiled to interaction nets, a model of computation from 1990 in which a program is a graph of nodes and computation happens by rewriting pairs of connected nodes, and the chip is designed around this distinct paradigm. Pairs of nodes being rewritten never overlap, so they can run in any order, or all at once, and arrive at the same result. Every value is also used exactly once, so data can stay in small local memories instead of large shared caches.

An example of the difference given by the team is a 5x5 chess-like board with five queens, placed so none can attack another. A typical program searches for solutions one board at a time. As an interaction net, the same search breaks into 3,183 small operations, and the longest chain that has to run in order is only 262 steps, so on average about 12 operations are ready to run at once at each step. Nothing about the program was rewritten to get there, as the parallel work was already intrinsic.

![Layout of the Frostbite chip, a four-by-four grid of tiles with one two-by-two quad and one L3 node outlined](https://cdn.mos.cms.futurecdn.net/wYRrMnwWqNzDSC95paoPzm-1200-80.jpg)

Each of the chip’s tiles, small identical processing units linked by an on-chip network, has its own small local memory. Four tiles, plus four L3 nodes, form the cluster that’s benchmarked against the conventional core for the performance claims, but the full layout has 16 tiles. The design reached 800 MHz in early synthesis but ended up at 500 MHz in the final layout. The cluster also averaged 8.77 times the comparison core’s performance per area, and the table below shows how its performance per watt varies by workload.

|  |  |
| --- | --- |
| How Frostbite’s efficiency gains vary by workload |  |
| Workloads | Frostbite performance per watt vs. comparison core |
| All 25 (geometric mean) | 4.59x |
| 10 used to tune the design | 6.02x |
| 15 held out until the final evaluation | 3.83x |
| Best: conv2d (held out) | 23.12x |
| Worst: recursive Fibonacci (held out) | 1.15x |

It may come as some surprise that the AI which built Frostbite started with what the company calls “zero architectural priors,” though the team first picked the workloads it had to do well on, and this sort of blank slatism may have its advantages in avoiding bias. Instead, the agents read papers and benchmarks, built Python models, and then selected one concept for focus. The original 141-page PDF output, which contained a programming model, runtime, and high-level blocks, was deleted after the first register-transfer level (RTL) design was generated, because “many of the numbers and estimates were well off what was physically possible.”

That PDF was only ever a starting point. Once the agents picked an architecture, they moved away from English — as it can’t get every detail right or catch every mistake, according to the team — and wrote the spec in the company’s own language, called ASL. ASL translates to Lean, a proof checker, so it can be machine-checked, which the company says stops a large class of bugs and cuts down on agents gaming their objectives. From this, the agents devised Arcmodel, a software model of the whole chip written in ASL, before any circuit design existed.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Simulating the RTL is slow, so the agents tested ideas on the model instead, which ran about 200 times faster. At first, the model’s power estimates were off by up to almost 250%, but an automated loop adjusted it until it matched the circuit design within just 5%.

From there, swarms of agents proposed changes in parallel, and each one was checked against the spec, tried in the fast model, built into the circuit design, and measured for power before being kept or dropped. This led to 58 ideas tried, with 37 kept. Separately, a behavior emerged that “was never specified by any human,” in what is known as work stealing: a tile with nothing to do can pull spare work from a neighbor or, in lieu of anything to do, go idle to save power.

|  |  |  |
| --- | --- | --- |
| Where each chip’s energy goes |  |  |
| Share of energy (one four-tile cluster, mean of 20 workloads, excluding clock distribution) | Comparison core | Frostbite |
| Memory | 57% | 38% |
| Fetching, decoding, and issuing instructions | 27% | 6% |
| On-chip network and scheduler | Not broken out | 26% |
| Clock distribution (share of total energy, left out of the rows above) | 49% | 41% |

This isn’t Architect Labs’ first design, as it showed off Redwood, an AI inference accelerator for robots and drones, in August. In that case, the company says its AI generated the RTL, verification, firmware, drivers, and kernels in under two weeks from a spec written by two human architects. Redwood still runs only on an FPGA and hasn’t been made in silicon, though the company says it is working toward having it built at TSMC.

Tendrils Compute, a possible rival based in Cambridge, U.K., raised funding earlier this month for a processor it says will have “thousands of cores operating in parallel.” It is also developing Vine, the same language Frostbite’s programs are written in.

Architect Labs says more benchmarks are coming, but they’re only part of the plan. It also wants an FPGA-hosted “software playground for anybody to run a program on Frostbite” along with a “preliminary operating system.” Eventually, it plans to release Frostbite’s RTL and instruction set.

In the meantime, the company plans to cover more workloads and compare “a broader set of CPUs,” including larger Frostbite mesh configurations against multicore versions of the comparison core with large caches. It also plans to test against “larger, wider, out-of-order CPUs,” with these comparisons due in the coming months on popular CPU benchmark suites such as SPEC and PARSEC.



Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

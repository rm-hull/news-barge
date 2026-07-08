---
title: Nvidia touts Vera CPU's single-threaded performance as its agentic AI advantage,
  reveals next-gen 'Rigel' Arm CPU cores — frames chip as a 'max single-threaded CPU
  at scale,' not a parallel monster
source_url: https://www.tomshardware.com/pc-components/cpus/nvidia-touts-vera-cpus-single-threaded-performance-as-its-agentic-ai-advantage-frames-chip-as-a-max-single-threaded-cpu-at-scale-not-a-parallel-monster
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-08T14:50:24Z'
published: '2026-07-08T00:00:00Z'
description: AI agents, like humans, demand high single-threaded performance
image: https://cdn.mos.cms.futurecdn.net/JUMzzHeBHtq9q5mBczXBWb-1280-80.jpg
---

![Nvidia Vera CPU](https://cdn.mos.cms.futurecdn.net/JUMzzHeBHtq9q5mBczXBWb.jpg) 

Only a little while back, Phoronix got the chance to test-drive one of Nvidia's upcoming Arm-based Vera CPUs. In certain approved workloads, the chip put up an impressive showing, nipping at the heels of its Xeon and Epyc x86 competitors. In specific single-threaded scenarios, Vera "absolutely dusted the competition" (our words). But AMD had some things to say about the Phoronix test, firing back with its own metrics of a 3.3x performance gain over Vera for the projected output of a 100 kW rack of its hardware.

And Nvidia is already thinking about this future. It revealed that its next-gen Rigel Arm v9.2 CPU core, shipping as part of its Rosa CPU, will deliver even higher per-core performance than Vera's Olympus core within the same silicon footprint via "better instruction delivery," more L2 cache, and better memory handling.

Now, Nvidia is reasserting Vera's advantage for AI work by describing it with a new product category: a "max single-threaded CPU at scale" rather than a parallel-processing beast. Instead of simply maximizing the core count per socket, Nvidia says Vera's monolithic 88-core design is meant to provide strong performance per core under load, enough memory bandwidth per core to keep active cores supplied with data, and predictable latency.

Nvidia describes AI inference workloads as being bound by single-thread speed. For example, a reasoning AI will run the model for one step, and will run the model again as many times as it takes until the answer is generated. Since each step needs the output from the previous one, no amount of parallelism will help — the speed at which one thread can run is most important. The situation is similar in agentic workloads, as agent B can't get its work started without knowing what happened with agent A.

 ![Nvidia Vera performance profile](https://cdn.mos.cms.futurecdn.net/8mT8ibmjuGcQ6tiVpfGaUi.png) 


Vera's design, then, appears to be one aimed at both having and eating the proverbial cake: high single-thread speed with a large number of available threads. Vera is an 88-core design with SMT support for 176 total threads. And to supply each of those cores with adequate bandwidth, Nvidia says Vera talks to LPDDR5X RAM at 1.2 TB/s, and that its monolithic compute die keeps cores well fed and avoids bottlenecks thanks to 3.4 TB/s of core-to-core bandwidth. The company says the latter figure is 3x that of "any other data center CPU."

There are many ways to measure inter-core bandwidth, so direct comparisons are tricky at best, but given the bespoke design of Vera for AI inference tasks, the claim is at least plausible.

The company's latest blog post about the new silicon reiterates this point, claiming its new silicon delivers 1.8x higher performance versus its x86 competition in "loaded CPU workloads that represent agentic execution," 1.5x higher perf in coding workflows, and 3x faster work in database analytics.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The numbers Nvidia touts purportedly come from real-world scenarios, starting with those from Perplexity, whose usage of Vera in coding agent work delivered a claimed 1.5x performance increase over x86, and a 1.9x speedup running concurrent sandboxes.

The claimed speed increases are wider still in database workloads, with Starburst (federated database firm) clocking a 3x uplift in large-scale SQL analytics, while Redpanda's real-time analytics saw a claimed 6x latency drop. According to Nvidia, all this purported performance is delivered by Vera's particular architecture, one that aims to deliver maximal single-thread performance *with* high thread counts.

We should note that vendor-approved benchmarks should always be taken with a bucket of salt, particularly those for hardware in a field that can shuffle trillions of dollars in a single day. The company doesn't say which precise x86 chips it tested Vera against, but it's a fair guess that they're mid- to high-end Intel Xeon and AMD Epyc models.

Nevertheless, in the blog post, Nvidia describes a conundrum that's familiar to most any server administrator: big-iron server chips can pack obscene amounts of cores, making them ideal for processing many tasks at once. However, the more cores you add, the slower they need to be to keep thermal performance and power draw in check. But that scale is an obstacle for tasks that need to be done *now*, parallelization be darned.

And the architectural decisions involved in using chiplets to scale to high core counts aren't free, either. Nvidia calls this "chiplet tax", and it says that scaling using chiplets creates memory access and performance inconsistencies that Vera's monolithic design is specifically meant to avoid.

We've long emphasized the importance of high single-threaded performance for a fast and responsive experience for client PCs, and it seems like AI agents are going to end up placing similar demands on hardware as they do their thing. If that's how the agentic AI future plays out, Nvidia's particular design optimizations for Vera make greater sense than prioritizing core count above all, as it might be for a general-purpose server chip meant to satisfy different economic and customer demands.

We'll have to see if Intel and AMD respond with "max single-threaded CPUs at scale" of their own.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

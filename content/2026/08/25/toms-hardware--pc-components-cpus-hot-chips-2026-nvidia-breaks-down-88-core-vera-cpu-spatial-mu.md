---
title: 'Hot Chips 2026: Nvidia breaks down Vera CPU — spatial multithreading benchmarked,
  agentic workloads detailed, and more'
source_url: https://www.tomshardware.com/pc-components/cpus/hot-chips-2026-nvidia-breaks-down-88-core-vera-cpu-spatial-multithreading-benchmarked-1-2-tb-s-socamm2-memory-agentic-workloads-detailed-and-more
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-25T13:09:01Z'
published: '2026-08-25T00:00:00Z'
description: Nvidia has provided more color on its Vera CPU for agentic data centers
  at Hot Chips 2026, showcasing the benefits of spatial multithreading and power benefits
  of the LPDDR5X memory system.
image: https://cdn.mos.cms.futurecdn.net/nxDGgasmtR5gDDCsVXUGtG-1920-80.jpg
---

![Nvidia Vera CPU](https://cdn.mos.cms.futurecdn.net/nxDGgasmtR5gDDCsVXUGtG.jpg) 

*This Tom's Hardware Premium article is free to read with a Tom's Hardware account; no payment necessary. We're offering free access from August 23 to 26 so you can read all of our reporting from Hot Chips.*

Nvidia has spent the last several months providing key disclosures about its next-gen Vera CPU for agentic data centers, which it continued at Hot Chips 2026. Although we've already learned a lot about Vera, how it compares to AMD's next-gen Venice CPUs, and the inner workings of the Olympus core, Nvidia provided a bit more color at Hot Chips on spatial multithreading, the memory subsystem, and what types of workloads it's targeting with Vera.

As a quick refresher, Vera is the first CPU with a custom Nvidia core, following up on Grace, which used a stock Arm design. It's shipping as a single, 88-core SKU, and it has some key design differences compared to Nvidia's x86 competition, most notably a multi-threading implementation that Nvidia calls spatial multi-threading, an LPDDR5X memory subsystem, and a monolithic compute die rather than using compute chiplets.

Nvidia says it's designed Vera specifically for agentic AI workloads, a category that's still being defined in terms of performance benchmarking. Many CPU-intensive tasks serve as proxies for agentic workloads (i.e., code compilation), though measuring performance across a full agentic chain is complex and inconsistent. Nvidia, in its own slides (see the end of this article), calls agentic AI the "most complex computing workload in history," after all.

Nvidia provided an example of a headless browser to show the benefits of Vera, using optimized code to mimic how an agent would use a browser. Compared to the 96-core EPYC 9655P, Nvidia says Vera runs 24% faster as browser instances scale.

 ![Nvidia Vera agentic headless browser performance.](https://cdn.mos.cms.futurecdn.net/dZQnq8PUubs3HkmxbuTLYT.jpg) 


This slide is a good demonstration of the complexities in measuring traditional workloads and applying that performance to agentic workflows. Agents will often fetch websites for information, but there are several layers where agents can trim back compared to humans; in this case, agents can run through a browsing workflow 4.5x faster by cutting things like GUI rendering, fonts, media decoding, and more.

 ![Nvidia Vera compilation benchmarks.](https://cdn.mos.cms.futurecdn.net/eY4t4f2JxMJZv4enVAKJy5.jpg) 


Another touchstone for agentic performance is code compilation, as agents seek out software to compile on the system. This might be the most direct benchmark of agentic AI performance with current workflows right now. Though, as previously mentioned, agentic chains are long, complex, and involve several different workloads.

Once again, compared to the 96-core EPYC 9655P, Nvidia claims Vera can compile the Linux kernel 22% faster with a native AArch64 target, and 14% faster when cross-compiling for x86.

## Nvidia's big cores for agentic AI — another look at Olympus and how it fits into Vera

Nvidia reiterated the importance of the large cores inside Vera, including the large BPU, neural branch predictor, and 10-wide decode. Nvidia has previously disclosed the Olympus core architecture, which you can read about in our Vera deep dive. Broadly speaking, however, it's a wide core optimized for high single-core throughput.

One of the more interesting design points of Vera is spatial multi-threading, which Nvidia described in more detail during its Hot Chips 2026. In short, Nvidia separates core resources on two pipelines, though data and cache can move between threads as needed. To demonstrate the benefit, Nvidia shared the results from SPEC CPU 2017 intrate that you can see below.

 ![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/VLwm9KpcTTS4YZqwgvcPzf.jpg) 


This shows the "noisy neighbor" effect. Nvidia measured single-core performance and then measured the same workload with another thread active. Nvidia's data shows that Vera is less concerned with the neighboring thread, whereas a "traditional CPU" sees a larger slowdown. Nvidia didn't clarify which CPU it's comparing Vera to here, however.

Nvidia's slide does a good job illustrating, but it's worth noting the difference compared to traditional SMT nonetheless. With traditional SMT, resources are time-sliced between threads, leading to gaps between BP and decode, as illustrated in the slide. With spatial multithreading in Vera, threads are still fighting for resources within the core. However, spatial multithreading allows Nvidia to deal with the demand of neighboring threads in a deterministic way, leading to a more consistent downturn in per-core performance when the second thread is working.

Nvidia's second-gen Scalable Coherency Fabric (SCF) moves data across the die. Nvidia didn't provide any new disclosures around SCF at Hot Chips, but you can see how the fabric is laid out in the slide below. Centralized Coherency Switch Nodes (CSNs) connect the cores to pools of L3 cache totaling 164 MB and the broader memory subsystem.

 ![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/GFvPycJMgQGmWBXEEGmzaB.jpg) 


At a system level, one of the more interesting choices Nvidia made was to use LPDDR5X as opposed to traditional RDIMMs, a choice that it was only able to make due to the serviceable SOCAMM2 design. Nvidia includes eight SOCAMM2 slots per Vera CPU on a board, offering up to 1.5 TB of capacity with 1.2 TB/s of bandwidth.

 ![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/mpRAd7dN2qGMJBiBV8ZSxU.jpg) 


LPDDR5X can deliver transfer rates higher than DDR5 RDIMMs, at least compared to single-rank DIMMs. However, it seems the driving force behind LPDDR5X wasn't performance but rather power consumption. One of the pillars of Vera, according to Nvidia's Hot Chips presentation, was to deliver a CPU for power-limited data centers. Micron says its LPDDR5X consumes about a third of the power compared to a traditional RDIMM.

 ![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/tuWPLbJPhewdufBdsqJXuU.jpg) 


Nvidia demonstrated that point a little differently, using bandwidth per watt as a point of comparison between the LPDDR5X system in Vera and traditional RDIMMs. This illustration does the job, though it could be a bit misleading, measuring power draw against peak bandwidth.

Nvidia tells us that a fully loaded memory system with Vera consumes between 30W and 40W, with 1.5 TB at 9600 MT/s. Power demands for RDIMMs vary wildly depending on capacity, channels, and transfer rate, though power consumption can easily climb over 100W depending on the configuration.

Although Nvidia has deployed Grace in the data center — to the tune of "hundreds of thousands" of standalone servers, apparently — Vera represents Nvidia's first big push to gobble up market share in the expanding agentic CPU market. It's highly targeted, as evidenced by the fact that Nvidia is only delivering a single 88-core SKU, and it's already being put to use in large-scale deployments, with Nvidia announcing yesterday a deployment of Vera at SpaceXAI.

 ![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/T7Am6PBK6q5RC9mwqVFKrU.jpg) 


Nvidia has shared the slide above before, which it once again showed at Hot Chips 2026. It's normalizing per-core performance in SPEC CPU 2026 against the AMD EPYC 9755. The core differences explain the big disparity in numbers; in reality, Vera led in overall score by 3%. Regardless, this is the slide Nvidia is using to pitch Vera, claiming it offers a big improvement in the workloads that are most relevant for agentic AI.

The most formidable opponent for Vera isn't Turin, however. It's Venice, which AMD launched in June, and Diamond Rapids, which Intel detailed just moments after Nvidia left the stage. Vera has a lot of interesting talking points already, but it'll be interesting to watch how Nvidia scales (or doesn't scale) its data center CPU business over the next few generations. Perhaps we'll see the firm double down on these agentic workflows, or maybe concessions and product segmentation to appeal to hyperscalers. Time will tell.

## Full Nvidia Vera Hot Chips 2026 presentation

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/pmmV2js2ZMe5wtYgRb2tvU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/YBfrnXN6HHKBXGuxvyKUpU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/tBg2ErDj8FSGhh8ggujpsU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/7PNoXUZwr3PiNmiTAFhZnU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/qRykFdSScnADP9QbNTy3pU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/rkHg9pvm44dmfhaoRHsFoU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/zaQe97PXT8CEc8bWXKeSrU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/CxSyjTRTpLSXBxnaS6JxvU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/FnsDb5rwRgGQw3Jore87rU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/8UyyeF7uucuWfCMjymHVuU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/mwCo2WB74UnnUnNFK8QtrU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/5YLvPArCBzuaKjB9NasTpU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/yL2eiD4WGANT656yZajCwU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/KMLSpKkYf2287U23zknQpU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/nymo2dhGQKweagjhbP9MtU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/aLiKLbmJPVUzC4Lijx83sU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/T7Am6PBK6q5RC9mwqVFKrU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/zTHH5RHKqWrB2ZpJ4V94qU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/fok8daLnt4Rft5KT7L58wU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/tuWPLbJPhewdufBdsqJXuU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/9irsAsQyjrCvRxXzkveCqU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/pwrzTtfYSkjT83pTFVsRyU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/pwPfj73BbPDMDUBhbUaiuU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/fCoMHrMLgYBZ9ANKXzu6xU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/6buajmxLwWVDEBG5wusUuU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/K3kHB35Wsuq6b73hrzyLsU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/6nRkmvgPzcn7C8eK59fGxU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/mpRAd7dN2qGMJBiBV8ZSxU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/3tXVCu7xUTPmmEi9UhnPvU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/E26MH4FN7MHEDmxqgzPhsU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/jJJ6TFKqGqW8dYJqRpnZuU-1200-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/pmmV2js2ZMe5wtYgRb2tvU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/YBfrnXN6HHKBXGuxvyKUpU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/tBg2ErDj8FSGhh8ggujpsU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/7PNoXUZwr3PiNmiTAFhZnU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/qRykFdSScnADP9QbNTy3pU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/rkHg9pvm44dmfhaoRHsFoU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/zaQe97PXT8CEc8bWXKeSrU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/CxSyjTRTpLSXBxnaS6JxvU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/FnsDb5rwRgGQw3Jore87rU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/8UyyeF7uucuWfCMjymHVuU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/mwCo2WB74UnnUnNFK8QtrU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/5YLvPArCBzuaKjB9NasTpU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/yL2eiD4WGANT656yZajCwU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/KMLSpKkYf2287U23zknQpU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/nymo2dhGQKweagjhbP9MtU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/aLiKLbmJPVUzC4Lijx83sU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/T7Am6PBK6q5RC9mwqVFKrU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/zTHH5RHKqWrB2ZpJ4V94qU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/fok8daLnt4Rft5KT7L58wU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/tuWPLbJPhewdufBdsqJXuU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/9irsAsQyjrCvRxXzkveCqU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/pwrzTtfYSkjT83pTFVsRyU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/pwPfj73BbPDMDUBhbUaiuU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/fCoMHrMLgYBZ9ANKXzu6xU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/6buajmxLwWVDEBG5wusUuU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/K3kHB35Wsuq6b73hrzyLsU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/6nRkmvgPzcn7C8eK59fGxU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/mpRAd7dN2qGMJBiBV8ZSxU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/3tXVCu7xUTPmmEi9UhnPvU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/E26MH4FN7MHEDmxqgzPhsU-1280-80.jpg) 

![Nvidia Hot Chips 2026 presentation.](https://cdn.mos.cms.futurecdn.net/jJJ6TFKqGqW8dYJqRpnZuU-1280-80.jpg) 

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

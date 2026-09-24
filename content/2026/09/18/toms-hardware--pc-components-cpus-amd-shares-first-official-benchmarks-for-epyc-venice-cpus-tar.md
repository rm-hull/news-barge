---
title: AMD shares first official benchmarks for EPYC 'Venice' CPUs, targets Nvidia
  — company claims 256-core chip is more than twice as fast as Nvidia Vera, 96-core
  model 20% faster per-core
source_url: https://www.tomshardware.com/pc-components/cpus/amd-shares-first-official-benchmarks-for-epyc-venice-cpus-targets-nvidia-company-claims-256-core-chip-is-more-than-twice-as-fast-as-nvidia-vera-96-core-model-20-percent-faster-per-core
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-18T22:31:38Z'
published: '2026-09-18T00:00:00Z'
description: Mind the footnotes.
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
image: https://cdn.mos.cms.futurecdn.net/aLSGanWgBzwJhr9LcYMiwb-2048-80.jpg
locations:
- Venice
people:
- Michael Larabel
- Tom
- Vera
organisations:
- AMD
- AWS
- Diamond Rapids
- EPYC
- GCC
- GNU Compiler Collection
- Get Tom's Hardware
- Google News
- HBM
- Intel
- LLVM
- NGINX
- Nvidia
- Phoronix
- SOP
- TPC-C
- TPC-H
- TPCx-AI
- Team Red
- Tom’s Hardware
- Vera
---

![AMD Venice CPU.](https://cdn.mos.cms.futurecdn.net/aLSGanWgBzwJhr9LcYMiwb.jpg) 

Following the launch of AMD's EPYC 'Venice' CPUs in July, AMD extended the performance claims for its upcoming generation of server chips on Friday. The high-level claim hasn't changed. AMD still says a 96-core, high-frequency Venice chip is around 20% faster than Nvidia's 88-core Vera in SPEC CPU 2026's Integer Rate test. However, the company went into far greater detail about the benchmarks in a new white paper.

 ![a snippet from the HBM roadmap article](https://cdn.mos.cms.futurecdn.net/JY32VXJVXoHUR8NRV2Kveb.png) 


There are several configuration differences depending on the benchmark throughout AMD's white paper, and although we'll call out those differences here to the best of our ability, we don't have all of the details. For the Vera comparison, in particular, AMD is mixing data from different sources, and in some cases, using different major releases of the GNU Compiler Collection (GCC). That can have a substantial impact on performance, so keep your salt shaker handy.

 ![Venice benchmarks](https://cdn.mos.cms.futurecdn.net/dcSCvUxLUQTpW4vzdCSXUg.png) 


First up are results in SPEC CPU 2026 with the intrate test, looking at total throughput. These are older numbers, gathered in July with GCC 15.2. The intrate test runs multiple copies of an application on the same CPU, and the SOP is to run one copy per thread. Presumably, that's what AMD did here, but the white paper doesn't clarify, even in the footnotes.

The 256-core 9996 is 2.37x faster than the Intel Xeon 6980P and 2.24x faster than Vera according to the slide. The white paper clarifies the mystery 9006 CPU is the 256-core flagship. Perhaps most impressive is AMD's gen-on-gen comparison. According to these results, the 9996 is around 78% faster than last-gen's 192-core EPYC 9965.

Although the high-level results bring in data from Intel and AWS, much of the white paper focused squarely on the comparison between Venice and Vera. AMD broke down the individual subtests of SPEC CPU 2026 intrate in the white paper, which you can see below.

 ![Venice benchmarks](https://cdn.mos.cms.futurecdn.net/VdJLbU8WZM3wAXsocNoYzS.png) 


The comparison looks good for AMD, naturally, though there are a few wrinkles in the configuration. AMD is testing a down-cored EPYC 9996, dropping from 256 cores to 96 cores. It made no mention of power budget, but when AMD originally shared SPEC numbers, the 96-core model had access to the same 600W as the 256-core model — AMD's 96-core, high-frequency Venice SKU tops out at 500W. More consequential is the compiler, however. AMD is using GCC 16.1 and comparing the results to the ones Nvidia shared in its Vera white paper. Nvidia used GCC 15.2.

Michael Larabel over at *Phoronix* has a nice write-up about the difference between GCC 15 and 16, but the short story is that there are performance differences, not always for the better. GCC 16 takes longer to compile due to better optimizations, hence the lower scores on the GCC and LLVM compilations above. However, that leads to faster binaries. By how much depends on the flags, software, and a whole host of other factors. Regardless, it's not best practice to compare benchmarks using two different compiler versions.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

 ![Venice benchmarks](https://cdn.mos.cms.futurecdn.net/bsTpoyTM7Bksy8kqnkBzrM.png) 


Speaking of *Phoronix,* AMD pulled some data for the publication's initial, controlled testing of Vera. Above, you can see the Stream, an industry-standard benchmark for measuring memory bandwidth. Again, AMD is using a down-cored 9996 from 256 cores to 96, and offering it a 600W power budget. Still, this is an impressive showing, as Vera absolutely clobbered the competition in the publication’s original Stream results. Here, AMD is ahead by about 18%, with per-core performance about 8% ahead.

 ![Venice benchmarks](https://cdn.mos.cms.futurecdn.net/cAypNNupLjhXx8trYSaU7f.png) 


Breaking out of Vera, AMD also showed performance in cloud workloads, including database, Java, and cryptography. Once again, the gen-on-gen comparison stands out, as AMD was already leading in these workloads with its last-gen chips. AMD ran these tests itself, rather than relying on third-party data, though the Graviton5 results came from an AWS cloud instance.

 ![Venice benchmarks.](https://cdn.mos.cms.futurecdn.net/Y3ZTh3bsqYFPHv7BupSPS.png) 


Similarly, in HPC workloads, AMD furthers its lead over Intel's flagship Granite Rapids-AP offering. Intel's next-gen data center CPUs, codenamed Diamond Rapids, are set to be released next year.

 ![Venice benchmarks](https://cdn.mos.cms.futurecdn.net/KrUg73p92NHy9iznKYbe5V.png) 


Finally, we have "agentic AI workload performance," which uses actual benchmarks for comparison, despite what the names in the chart above suggest. From left to right, AMD used NGINX, TPCx-AI kit, FAISS, TPC-H and TPC-C, and a replay of a multi-persona agent. For TPC-H and TPC-C, AMD says it derived workloads from those benchmarks, so the results here aren't comparable to published results.

Although looking at benchmark results is always interesting, it doesn't say much in the context of a server deployment, at least at the scale that AMD is targeting. Peak performance is only one of the major factors that go into server deployments, after all, and even then, performance can vary wildly depending on what software you're running and how it's built.

Still, Venice looks impressive, perhaps more so in the gen-on-gen comparison than any competitive comparison. Hopefully that bodes well for AMD's future Zen 6 rollout on consumer desktops, but we'll have to wait until Team Red has more to share before drawing any conclusions on that front.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg) 

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

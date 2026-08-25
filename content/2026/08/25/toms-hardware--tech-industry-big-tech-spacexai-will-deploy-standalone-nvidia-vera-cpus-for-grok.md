---
title: SpaceXAI will deploy standalone Nvidia Vera CPUs for Grok's agentic workloads
  — will use optimized Vera Rubin NVL72 in space with Starmind satellite
source_url: https://www.tomshardware.com/tech-industry/big-tech/spacexai-will-deploy-standalone-nvidia-vera-cpus-for-groks-agentic-workloads
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-25T13:07:56Z'
published: '2026-08-25T00:00:00Z'
description: SpaceXAI becomes the second announced hyperscale customer for standalone
  Vera after Meta.
image: https://cdn.mos.cms.futurecdn.net/tAXNckhbwBFZknaHqvpJe7-1920-80.jpg
---

![Nvidia Vera CPU](https://cdn.mos.cms.futurecdn.net/tAXNckhbwBFZknaHqvpJe7.jpg) 

Nvidia's 88-core Vera chip will be getting put to work for Elon Musk twice over, first and foremost as the standalone CPU orchestrating Grok's AI agents in SpaceXAI's data centers and, from the fourth quarter of 2027, inside the company's first Starmind satellite. Nvidia announced the deployment yesterday, making SpaceXAI the second hyperscaler after Meta to commit to Vera outside full Vera Rubin racks, with Musk supplying the launch window in a post on X. Nvidia claims the chip completes agentic, reinforcement learning, and data processing tasks up to 1.8 times faster than x86 processors, but that figure hasn't been independently verified.

 ![tsmc](https://cdn.mos.cms.futurecdn.net/p2QqhVFP7dTRWfeVBCYBYV.jpg) 


Agents spend much of their runtime off the GPU. A model that writes code, for example, calls tools, queries databases, and parses results by leaning on the host CPU between every inference pass; idle GPUs waiting on that work are wasted capital. "Vera gives us the CPU performance and memory bandwidth to run enormous amounts of orchestration, code, and data processing while keeping GPUs doing what they do best," Mike Nicolls, president of SpaceXAI, said in the release.

SpaceX, in partnership with Nvidia, has designed a space-optimized Vera Rubin NVL72 system for launch to orbit in Q4 next year, with significant scale in 2028 [https://t.co/qdDq8YBkzlAugust](https://t.co/qdDq8YBkzlAugust) 24, 2026


Meta was the first company to announce a large-scale standalone Vera deployment, confirming in February that it would run Grace-only servers in production with Vera to follow as soon as 2027. Nvidia has since disclosed shipping hundreds of thousands of standalone Grace servers and more than 2.5 million Grace CPUs in total, and the SpaceXAI deal extends that dominance directly into territory held by AMD's EPYC and Intel's Xeon lines.

Vera pairs 88 custom Olympus cores on a monolithic die with spatial multithreading and LPDDR5X memory delivering up to 1.2 TB/s of bandwidth. Nvidia's performance claims for the chip remain contested, and AMD has countered that its 256-core Zen 6 Venice processors beat Vera by 3.3 times in rack-level performance. Neither company disclosed how many Vera CPUs SpaceXAI will deploy, the value of the deal, or when the data center rollout begins; the only date attached to the announcement is the satellite launch window.

Musk said earlier this month that Starmind launches would begin in 2027, and his X post following the press release narrowed that to the fourth quarter, with what he described as significant scale-up following in 2028. The terrestrial NVL72 combines 72 Rubin GPUs and 36 Vera CPUs in a fully liquid-cooled rack, and an orbital version has to be reworked for radiation exposure, heat rejection through radiators rather than facility water loops, launch vibration, and the absence of any hands-on servicing.

SpaceXAI's first-generation AI1 satellite design carries a 120 kW compute payload, peaking at 150 kW, on a craft wider than a Boeing 747. The company has also acknowledged that orbital compute at the scale it's targeting requires significantly more chips than it currently has access to, a constraint the Vera Rubin commitment doesn't itself address.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.

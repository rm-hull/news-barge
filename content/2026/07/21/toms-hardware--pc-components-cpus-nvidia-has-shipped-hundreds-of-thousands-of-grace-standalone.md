---
title: Nvidia has shipped 'hundreds of thousands of Grace standalone servers’ — GPU
  firm pivots messaging as CPUs take center stage in agentic data centers
source_url: https://www.tomshardware.com/pc-components/cpus/nvidia-has-shipped-hundreds-of-thousands-of-grace-standalone-servers-gpu-firm-pivots-messaging-as-cpus-take-center-stage-in-agentic-data-centers
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-21T17:40:39Z'
published: '2026-07-21T00:00:00Z'
description: Nvidia would like you to know that it’s a CPU company, too.
image: https://cdn.mos.cms.futurecdn.net/64zg6rxBUaGx8y7ooex4WA-2560-80.jpg
---

![Nvidia's Vera data center CPU.](https://cdn.mos.cms.futurecdn.net/64zg6rxBUaGx8y7ooex4WA.jpg) 

Nvidia’s Ian Buck, vice president of hyperscale and high-performance computing and the inventor of CUDA, says the company has “shipped... let's put it in the hundreds of thousands of Grace standalone servers.” In May, Nvidia disclosed that it had shipped over 2.5 million Grace CPUs in total, and the company announced a __partnership with Meta to deploy standalone Grace servers__ in February. Buck’s comments suggest the scale of deployment may be even larger, however, as Nvidia tries to compete in a market dominated by other players.

 ![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB.jpg) 


It’s an interesting comment, though not a surprising one. Nvidia has become the dominating force of Silicon Valley as demand for its GPUs skyrocketed during an unprecedented data center buildout for AI inference. Since peaking earlier this year, however, around $1 trillion in Nvidia’s market cap has been wiped away as investors __rally behind CPU makers like Intel__. Evolving agentic AI workloads have changed the hardware balance, shifting away from as many as eight GPUs per CPU, toward a one-to-one ratio in some cases.

Nvidia wants to ride that train with its new Vera CPU, which was architected specifically for those types of workloads. Even before the recent rise of agents, however, Nvidia says it has seen demand for its CPUs for data-hungry workloads. “They weren’t running a web server [with Grace]… or they aren’t being used for, what the cloud uses, of cheap, dollar-per-core,” Buck said. “They were being deployed for the backend, data-rich operations, like the data processing.”

Grace represents an on-ramp for Nvidia into data center CPUs. It uses 72 stock Arm Neoverse V2 cores, but it’s differentiated by Nvidia’s Scalable Coherency Fabric (SCF). Vera uses an updated SCF, but it also features Nvidia’s first custom core design, called Olympus. Grace cracked the door, and Vera represents Nvidia's big entrance into the market against AMD and Intel.

Regardless of where Vera ends up in the battle of next-gen data center CPUs — which is heating up now, as AMD is expected to launch its Zen 6 Venice CPUs this week — the design is vastly different from what we’ve seen out of Intel and AMD. Most notably, Vera is monolithic, placing all of its 88 cores on a single piece of silicon. AMD and Intel, years ago at this point, pivoted away from monolithic dies in favor of chiplets, allowing an extremely high density of cores at the cost of latency and coherency issues. Vera is radically different in that regard, not only being built on a single die, but also dedicating significant die space to the fabric.

“One of the reasons we don’t have 128 cores is because we’ve dedicated so much of the die area toward the fabric,” Buck said. “It’s 3.4 TB/s of bandwidth inside of that CPU that is dedicated toward allowing every core to talk to every cache, every memory [controller] at full speed without any collisions.”

For clarification’s sake, Buck is referencing 3.4 TB/s of core-to-core bandwidth in Vera. There’s up to 1.2 TB/s of aggregate memory bandwidth (14 GB/s per core) through the LPDDR5X interface.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

But just as chiplet-based designs made trade-offs in per-thread performance, Vera will likely make trade-offs for its unique architecture. The majority of data center workloads are still “legacy” tasks that hyperscalers have built for, and even with seemingly insatiable demand for AI infrastructure, that is unlikely to change for several years.

Buck recognizes this trade-off, asking: “Can Intel and others build rich fabrics? Do they have the IP and the ecosystem to do it and connect it all the way through to LP memory? They need to tell you when they’re going to do it… but that trade-off will come at the cost of the legacy workload.” Earlier this year, at GTC in March, Buck was even more clear. “The world is not going to be served by one SKU of CPU, and that is not our intention,” the executive said in a news conference at the time.

Still, it’s clear Nvidia has ambitions with data center CPUs beyond what headlines are floating around on the New York Stock Exchange. Nvidia says CPUs represent a $200 billion TAM (Total Addressable Market) opportunity for the company, a rather rosy forecast compared to the rest of the industry, which sees a TAM of around $120 billion by 2030 (though recent estimates have climbed as high as $170 billion). And agentic AI is expanding that market, with Morgan Stanley in April estimating that agents could add as much as $60 billion to the data center CPU market.

Vera is in full production alongside Nvidia’s next-gen AI infrastructure, including Rubin GPUs, ConnectX-9 NICs, SpectrumX Ethernet switches, and the various components that go into building a Vera Rubin NVL72 rack. The company says there are around 1.3 million components that go into a rack, and it has a list of over 300 partners globally to build them. As part of our visit to Nvidia HQ last week, we saw a Vera Rubin NVL72 rack in action, running workloads for OpenAI.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

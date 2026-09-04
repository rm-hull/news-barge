---
title: AMD unveils Threadripper Halo Station, an AI workstation packing 96 cores and
  dual liquid-cooled MI350P accelerators — 'the most powerful workstation in the world'
  can run trillion-parameter models, says AMD
source_url: https://www.tomshardware.com/pc-components/cpus/amd-unveils-threadripper-halo-station-an-ai-workstation-packing-96-cores-and-dual-liquid-cooled-mi350p-accelerators-the-most-powerful-workstation-in-the-world-can-run-trillion-parameter-models-says-amd
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-04T18:58:37Z'
published: '2026-09-04T00:00:00Z'
description: The machine will likely cost hundreds of thousands of dollars.
image: https://cdn.mos.cms.futurecdn.net/EHns78bnX5ekkg6HfvzEXa-1280-80.png
---

![AMD Threadripper Halo Station at IFA 2026.](https://cdn.mos.cms.futurecdn.net/EHns78bnX5ekkg6HfvzEXa.png) 

AMD announced what it calls "the most powerful workstation in the world" at IFA 2026, dubbed the Threadripper Halo Station. The machine includes a Threadripper Pro 9995WX with 96 Zen 5 cores, dual liquid-cooled Instinct MI350P accelerators "with a path to four," 2TB of DDR5, and 288GB of HBM3E with up to 576GB supported. AMD claims the workstation is capable of running trillion-parameter models.

Taking all of the components together, the street price should come out to over $100,000 with just the core components: memory, CPU, and dual GPUs. Configured higher, and with supporting storage, power, and cooling, the workstation could very easily climb over $150,000.

 ![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB.jpg) 


It's essentially a server tray reconfigured into a tower, with an EPYC host replaced with a 96-core Threadripper. AMD didn't share many details about the machine outside of the specs, though it appears to be a system design that AMD's OEM partners will ultimately build and ship. AMD has yet to announce any partners supporting the machine.

The Threadripper Pro 9995WX at the heart of the machine is a 96-core, 192-thread Zen 5 chip that can boost up to 5.4 GHz. It ships with 384 MB of L3 cache and has a TDP of 350W. It's hard to find Threadripper Pro standalone chips in general, but the 9995WX clocks in at around $11,000 to $12,000.

| **CPU Host** | Threadripper Pro 9995WX, 96 cores, 5.4 GHz boost | 
| **GPU** | 2x Instinct MI350P | 
| **System memory** | 2TB DDR5 | 
| **Cooling** | Liquid-cooled CPU and GPUs | 
| **GPU memory** | 144GB HBM3E per accelerator, up to 576 HBM3E | 
| **CPU TDP** | 350W | 
| **GPU TBP** | 600W (per accelerator) | 

The MI350P accelerators come with 128 CDNA 4 compute units built on TSMC N3. Each accelerator packs 144GB of HBM3E memory, giving the system 288GB of HBM3E. AMD says there's a "path to four," opening up the possibility of two more accelerators bringing 576GB of HBM3E to the system. You'll need plenty of power to feed the GPUs, as each accelerator is rated for up to 600W.

Although AMD says it can support up to four accelerators, the workstation shown off at IFA only has room for two, both of which are liquid-cooled, alongside the Threadripper host. AMD doesn't sell MI350P accelerators on their own in traditional consumer channels, but the estimated price is somewhere around $20,000 per accelerator.

At a system level, the Threadripper Halo Station includes 2TB of DDR5 memory, which is the maximum capacity supported across the eight-channel memory configuration of the Threadripper Pro 9995WX. AMD supports up to DDR5-6400 on the Threadripper, though it made no mention of speed during its IFA presentation. Regardless of speed, 2TB of DDR5 costs about $50,000 right now.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

AMD has yet to set a price or release date for the Threadripper Halo Station, though we'll likely hear more about the design from AMD's partners in the near future. An extremely expensive workstation isn't out of the question. The Lenovo ThinkStation P8, for instance, which uses Threadripper Pro CPUs as a host, clocks in at $334,463 right now, maxed out with 2TB of DDR5 and dual Blackwell accelerators.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg) 

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

- 
Reply
 We'll probably see mainstream 32-core Zen 7 or Zen 8 with the performance of >48 Zen 5 cores. 96-core Zen 5 will be the first component on the list to become "obsolete", although the I/O and memory channels will be lacking on consumer sockets.GenericUser2001 said:Maybe in ten years I will be able to buy one of these on Ebay.
 
 Terabytes of DRAM will become cheaper and more commonplace after 3D DRAM takes off. The GPUs/accelerators of 10 years from now will improve a lot. But to get the memory you want, you might need a future evolution of Strix/Medusa Halo.
 
But yeah, we can dream of the $150k workstation cratering down to $2k. If the MI350P 288 GB accelerators are still holding a lot of value 10 years from now, they could be ripped out of the system and sold separately. The 9995WX + motherboard + 2 TB DDR5 will hopefully be left in the dust by then, if CPUs and memory advance enough.
- 
Reply
 It's Threadripper Pro, and I doubt it lacks much that you would need Epyc to get. Pro has 128 PCIe 5.0 lanes and 8-channel memory, non-Pro has 80 PCIe 5.0 lanes and 4-channel memory.qxp said:Its weird - why settle for Threadripper when the cost is dominated by GPUs and memory? They should have just put Epyc CPUs, more slots, more memory bandwidth.
 
It also clocks higher than Epyc chips, 5.4 GHz vs. 4.5 GHz for a Turin 96-core.

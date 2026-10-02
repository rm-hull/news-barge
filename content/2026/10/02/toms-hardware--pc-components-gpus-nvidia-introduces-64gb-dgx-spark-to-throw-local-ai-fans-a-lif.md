---
title: Nvidia introduces 64GB DGX Spark to throw local AI fans a lifeline amid the
  RAMpocalypse — new GB10 config starts at $4999 for those who can work with less
source_url: https://www.tomshardware.com/pc-components/gpus/nvidia-introduces-64gb-dgx-spark-to-throw-local-ai-fans-a-lifeline-amid-the-rampocalypse-new-gb10-config-starts-at-usd4999-for-those-who-can-work-with-less
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-02T18:02:10Z'
published: '2026-10-02T00:00:00Z'
description: Less memory, lower price, otherwise identical
image: https://cdn.mos.cms.futurecdn.net/D4D8sJFKUe4PFUpqUAPSfB-2560-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Jeff Kampman
- Jeffrey Kampman
- Tom
locations:
- Shenzhen
organisations:
- 64 GB Sparks
- AMD
- Acer
- Apple
- Asus
- CPU
- DGX Spark
- Dell
- GB10
- GPU
- Get Tom's Hardware
- Gigabyte
- Google News
- Gorgon
- HP
- MSI
- MicroCenter
- NIC
- Nvidia Sync Cluster Assistant
- OpenCode
- RAM
- Strix Halo
- Tom's Hardware
---

![DGX Spark](https://cdn.mos.cms.futurecdn.net/D4D8sJFKUe4PFUpqUAPSfB-1920-80.jpg)

Nvidia is tailoring its popular DGX Spark platform and the GB10 SoC to better fit the realities of today's AI models and the broader silicon supply crunch. The company is introducing a 64GB version of the Spark that's meant to be more affordable to local AI trailblazers who just don't need 128GB of RAM.

Back when we first began exploring the capabilities of the DGX Spark and similar systems, the general assumption was that lots of RAM would be necessary to hold the most intelligent models one might want to run, and so unified memory systems built around AMD's Strix Halo, Nvidia's GB10, and Apple's M-series chips could all be configured with 128GB of memory or more.

But the AI field moves fast. Highly intelligent dense models like Qwen 3.8 27B can now fit comfortably within 32GB of RAM (albeit with limited context), so the original Spark's 128GB of memory isn't essential for local inference alone. And skyrocketing RAM prices mean that a chip that’s permanently paired with too much costly LPDDR5X is more of a barrier to entry than an asset. So a more affordable Spark with less RAM makes sense for those who need the capabilities and supporting software stack of Nvidia's GB10 Superchip and can live with less memory.

A "more affordable" DGX Spark is of course relative in today's market. 64GB GB10 systems from Acer, Asus, Dell, Gigabyte, HP, and MSI are slated to start at $4999 when they launch on October 23. Given the ever-shifting prices of memory and storage right now, they might not stay there for long. Assuming you can find a 128GB GB10 system in stock, you can expect to pay roughly $7000 to $9000 for one right now, far above even Nvidia's adjusted MSRP.

Memory capacity change aside, 64 GB Sparks will retain the same ConnectX 7 RDMA NIC as their 128 GB stablemates, meaning that they can still be clustered to boost memory capacity and inference performance if a user does eventually outgrow the bounds of 64GB of RAM. The same 20-core Arm CPU complex from the original Spark carries over unchanged, as does the 273 GB/s of shared memory bandwidth for the CPU and GPU.

To help make use of that ConnectX 7 NIC, Nvidia is also making it easier to join Sparks together with a new software tool, the Nvidia Sync Cluster Assistant, that automates the process of yoking those systems together. (Sync is a remote connectivity and management app for the Spark that allows users to use their Spark’s AI horsepower from other Macs and PCs.)

That tool supplements a variety of community-developed utilities that have sprung up over the past year to make clustering a more seamless process, as we used in our experiments with clustering two Dell GB10 systems together earlier this year.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Nvidia is also adding a feature to Sync called Model Launcher that automatically downloads and starts models like the aforementioned Qwen 3.8 27B across one or more systems and links them to the OpenCode browser-based coding agent so that users can start using their local token factories right away for agentic workflows.

The 128GB DGX Spark and Spark-alikes will remain available for those who need space for larger models and for scaling across clusters, or for more memory-hungry local AI work like model fine-tuning, so there’s basically no downside to this addition to the DGX Spark lineup. In today’s volatile market, it’s good to have options, and a 64 GB Spark gives local AI enthusiasts another choice to better fit their budgets and workflows.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jeffrey Kampman](https://cdn.mos.cms.futurecdn.net/8JCjGs5yVZds2YdKmzjUDE-140-80.jpg)

As the Senior Analyst, Graphics at Tom's Hardware, Jeff Kampman covers everything that has to do with graphics cards, gaming performance, and more. From integrated graphics processors to discrete graphics cards to the hyperscale installations powering our AI future, if it's got a GPU in it, Jeff is on it.

* * * * * * * Reply
              This is your price increase announcement disguised as a product announcement.koga73 said:Total BS when MicroCenter and other retailers still have the 128GB version listed for $4899, now a 64GB version for MORE? $5000. Which will only drive up the 128GB price.
            * Whoa...$5K Spark 64. Guess price went up a little bit hahah.Reply  
                
              So, to recap: DGX Spark 128 launched 10/25 for $4K. Went up to $4.7K on 2/26. Is now $7K-9K street.  
                
              In that context, $5K for 64 is probably inline. Ditto the $6.7K average for Gorgon 192 Shenzhen boxes.  
                
              For a hobbyist--raises hand--you can go either of two ways, go big-but-slow RAM route with unified LPDDR5X, or go small-but-fast with GPUs. The first option was still kinda sorta doable when Strix Halo 128 was around $2K, but it's strictly off-limits now.  
                
              I'd rather spend $6K for four 5080s and jerryrig them together, than paying $5K for lousy LPDDR5X box.  
                
              The clincher is unified LPDDR5X is still butt slow for dense models. Ditto if you want to do image/video generation stuff.
            * Reply
              No both use lpddr6x. And lpddr5x is not faster than ddr5 it has a lower power profile thats why it’s used in laptops and solutions like this to reduce heat and power and cooling requirements in the system. It’s not likely to be as fast as general ddr5 , but neither Mac mini or dgx spark use ddr5. Also, it’s useful in unified mem architectures which both dgx and Mac mini are.kealii123 said:I bet it is. Much faster ram
            * lol "local AI fans" yeah they're called "influencers" bro. No one wants their own slop generator.Reply  
                
              Secondly, halving the RAM and upping the price by $1,000 is not "throwing fans a lifeline". You tech writers kiss more tech bro ass with every passing day.

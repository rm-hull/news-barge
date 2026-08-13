---
title: Elon Musk says xAI will increase data center capacity 7x by 2027 — targeting
  10 gigawatts of compute, up to $500 billion in revenue by the end of next year
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/elon-musk-says-xai-will-increase-data-center-capacity-7x-by-2027-targeting-10-gigawatts-of-compute-up-to-usd500-billion-in-revenue-by-the-end-of-next-year
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-13T13:39:09Z'
published: '2026-08-13T00:00:00Z'
description: $300 billion - $500 billion in revenue by the end of next year too.
image: https://cdn.mos.cms.futurecdn.net/EGD7PmkSMgK6t3rpCaCefg-2000-80.jpg
---

![SpaceX](https://cdn.mos.cms.futurecdn.net/EGD7PmkSMgK6t3rpCaCefg.jpg) 

Elon Musk told employees of SpaceX that the power capacity of the company's xAI data centers will increase by 7x to 10GW by late 2027. If this happens, the company's data centers will bring the company some $300 billion – $500 billion in revenue per year, according to Musk. The claim comes as SpaceX's market capitalization dropped by nearly $570 billion in less than two months. Meanwhile, the combined performance of the cluster will by far outpace not only all supercomputers in the Top 500, but also all AI clusters running today.

 ![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7.jpg) 


"We have already built the most powerful AI training clusters in the world," Musk told SpaceX employees at a meeting. "What we expect to do by the end of next year is about 10 times more than what we have done thus far. […] So, we are aiming to get to 10 GW [of compute] by the end of next year. […] If the value per watt is probably going to be $30 to $50, which means if we bring 10 GW of AI compute online by the end of next year, it will be $300 to $500 billion a year in revenue. Big numbers."

## A lot of power

At present, SpaceX's xAI data centers in Memphis and Southaven have a rated power draw of 1.4 GW. The company plans to increase the electrical capacity of its data centers to 10 GW by the end of 2027, or by around sevenfold in roughly 1.5 years. It should be noted that AI infrastructure with a 'nameplate power draw' of 1.4 GW by far does not offer compute capacity of 1.4 GW.

A large AI data center with a power usage effectiveness (PUE) of roughly 1.2 would have around 1.17 GW available to IT equipment (i.e., 230 MW is used by cooling, pumps, fans, humidification/dehumidification, lighting, power distribution losses, UPS losses, and other facility systems). Not all of that 1.17 GW goes to AI accelerators: CPUs, memory, networking, and storage consume a meaningful share. If perhaps 70% – 80% of IT power ultimately corresponds to accelerators, we might be looking at roughly 0.8 GW – 0.95 GW of accelerator power in the case of a 1.4 GW data center.

## Loads of FLOPS

Compute capacity is not measured in Watts; it is measured in floating-point operations per second (FLOPS). Keeping in mind that currently xAI uses a mix of Hopper- and Blackwell-based accelerators, it is hard to determine how much compute xAI has today. Since xAI seems to be betting primarily at Nvidia's Vera Rubin systems from now on, we can make a more or less educated guess about the company's Rubin-based compute capability the company will have by the end of 2027.

Assuming that all of the new 8.6 GW nameplate power draw will be based on Nvidia's NVL72 VR200 rack-scale systems and the PUE of around 1.2, the IT power budget of the new capacity will be 6.88 GW. Actual Rubin AI accelerators will get between 4.816 GW and 5.504 GW of power depending on how much of the IT power will correspond to these GPUs. Each Rubin GPU is expected to consume 2.3 kW of power in Max-P configuration. As a result, xAI's clusters will house between 2.094 million and 2.393 million Rubin GPUs in Max-P mode, or 29,083 and 33,236 NVL72 VR200 systems.

The performance of the NVL72 VR200 system is well known, so depending on the number of these machines that xAI will deploy by the end of 2027, we are looking at rather formidable numbers. NVFP4 inference performance of the cluster will be between 105 and 120 ExaFLOPS; NVFP4 training performance will range from 73 to 84 ExaFLOPS; FP6/FP8 training capability is projected between 37 and 42 EFLOPS, whereas native FP64 compute will total 70 – 80 EFLOPS. Of course, we are dealing with very rough numbers here as some systems may not work in Max-P configuration.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

To put the numbers into context. The total combined FP64 performance of all systems on the Top 500 list is 18.73 EFLOPS. xAI will have 3.7X – 4.3X more than that if the cluster is deployed. As for AI performance, 105 – 120 NVFP4 EFLOPS inference and 73 – 84 NVFP4 EFLOPS training put this cluster in a whole different league from anything publicly operating right now, meaning that we are talking about dramatically more sophisticated AI models coming. Whether or not the combined xAI compute capability will enable the company to earn $300 billion – $500 billion per year is something that remains to be seen, as SpaceX is not the only company selling compute capacity to AI companies, and the competition will likely be rough.

Yet, it is about time for Musk to make comments like this, as after topping $2.44 trillion in market capitalization on June 20, SpaceX dropped to $1.43 trillion on August 1, but rebounded to $1.87 trillion on August 12.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

- 
Yes. I couldn't be more happy about this. Grok and the Grok ecosystem have quickly become one of my favorite things. Search engines going all the way back to AltaVista and WebCrawler were great tools but AI is quickly making them look like archaic relics of the past. AI is quickly becoming the hottest, coolest technological advancement of my lifetime. Most people have no clue how important AI is going to be or how widespread it's going to be in our daily lives improving all kinds of technologies.Reply
 
There was about zero chance I would have subscribed to X for social media, or news, or the typical social media slop. Now I'm a Premium+ subscriber for the extra Grok access and benefits. I'm hooked, I use it almost daily and it's more useful for me than Google and it beats Google AI in some things already. Let's go, let the AI race continue and hopefully the competition makes them all better. I'm loving it, and it's only just begun to show glimpses of the future potential.

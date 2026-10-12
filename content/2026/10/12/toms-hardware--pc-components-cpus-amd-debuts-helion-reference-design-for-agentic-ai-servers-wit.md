---
title: AMD debuts Helion reference design for agentic AI servers with up to 32,768
  Zen 6 ‘Venice’ cores — rack design ships later this year in CPU-only and all-in-one
  configurations [Updated]
source_url: https://www.tomshardware.com/pc-components/cpus/amd-debuts-helion-reference-design-for-agentic-ai-servers-with-up-to-32-768-zen-6-venice-cores-rack-design-ships-next-year-in-cpu-only-and-all-in-one-configurations
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-12T19:06:14Z'
published: '2026-10-12T00:00:00Z'
description: Helios, meet Helion.
image: https://cdn.mos.cms.futurecdn.net/KwFreiH9LLPrsYZGRWvHU4-802-80.png
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Lisa Su
locations:
- Helion
organisations:
- AMD
- Get Tom's Hardware
- Google News
- Helion
- Helios
- MHS
- Meta’s Muse
- OCP
- OCP’s DC-MHS
- OpenAI Dots
- Tom’s Hardware
---

![AMD Helion rack.](https://cdn.mos.cms.futurecdn.net/KwFreiH9LLPrsYZGRWvHU4-802-80.png)

**Updated 10/12/26 at 12:01pm ET:** * AMD originally said the Helion rack would ship in the first half of 2027, but it has revised the release date to November 2026. We've updated the headline and featured image. We also corrected an error where OpenU trays were marked as 21mm wide instead of 21 inches wide.*

AMD is bringing a new reference rack-scale design to the data center ecosystem with Helion. It’s a standardized, 21-inch rack reference design that will complement the Helios rack AMD revealed at OCP Global Summit last year. This year, we have Helion, which AMD says can house up to 32,768 Zen 6 cores in a CPU-only deployment using the dense 256-core design available with the EPYC ‘Venice’ 9996.

![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB-1200-80.jpg)

The rack design is standardized, based on the Open Compute Project’s ORv4 specification, which is slightly wider and taller than a standard IT rack. Helion is designed to support 44 OpenU trays, which are 21 inches wide and 48mm tall, slightly larger than a standard EA1-310 tray. AMD says the reference design supports both air-cooled and direct liquid-cooled deployments.

The design is also compliant with OCP’s DC-MHS (Data Center Modular Hardware System) standard. MHS is designed to bring “interoperability between key elements of data center, edge, and enterprise infrastructure,” according to OCP.

Although AMD has renders of the design you can see in the presentation below, it won’t actually sell racks. This is a reference design that AMD is contributing to OCP, and OEMs and ODMs will actually bring that design to market. AMD didn’t share partners supporting Helion during a pre-briefing with the press. The company says CEO Lisa Su will announce partners during the lead keynote at the OCP Global Summit later today.

AMD also didn’t share deployment partners, though it suggested that Helios customers will also deploy Helion racks.

Unlike Helios, which is built for AI training and inference, Helion is a more flexible rack solution primarily focused on CPUs. In a CPU-only deployment, the design can hold up to 128 EPYC 9996 CPUs, bringing that impressive 32,768 core count per rack. This configuration would likely look something like an agentic AI sandbox system, which is then connected to an inference system.

This model for personal AI agents is in use today, both in Meta’s Muse and OpenAI Dots. Each user has a sandbox with a slice of compute from the host system, with the backbone of an inference server. Some workloads are handled on those CPU-only servers, such as building software, but the heavy-duty AI inference happens elsewhere.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Presumably, this is the model AMD is aiming at with Helion as hyperscalers build out CPU capacity on the back of agentic AI. However, the design is flexible, supporting up to 16 MI350P GPUs and 102 Tbps of networking, though at the cost of CPU capacity. This hybrid configuration is targeted at enterprises, says AMD, giving them an all-in-one rack for data management, networking, and AI usage.

AMD says the Helion rack will be available starting in the first half of 2027, likely riding the wave of Zen 6 deployments that are expected to start ramping up later this year.

## Full AMD OCP 2026 presentation

![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/qbHXxCUyfD7kTU8WG4nBxf-1200-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/t4R2vWqqwaMMW9bp4n8AKg-1200-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/2932ZFdtxQs7LXf8Xkjs6g-1200-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/VnwDTUtSNDMrihZkqbCELg-1200-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/tZgQQxGBTvdqa8wqAjMg9g-1200-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/zao8dTCw5UkKxGjDAk6RKg-1200-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/8XDHiyeqKsZhuj2o7v38Kg-1200-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/fSuCvgUD8G598vNKuzXk3g-1200-80.jpg)
![AMD Helion rack.](https://cdn.mos.cms.futurecdn.net/KwFreiH9LLPrsYZGRWvHU4-802-80.png)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/qbHXxCUyfD7kTU8WG4nBxf-2000-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/t4R2vWqqwaMMW9bp4n8AKg-2000-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/2932ZFdtxQs7LXf8Xkjs6g-2000-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/VnwDTUtSNDMrihZkqbCELg-2000-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/tZgQQxGBTvdqa8wqAjMg9g-2000-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/zao8dTCw5UkKxGjDAk6RKg-2000-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/8XDHiyeqKsZhuj2o7v38Kg-2000-80.jpg)
![AMD OCP 2026 presentation.](https://cdn.mos.cms.futurecdn.net/fSuCvgUD8G598vNKuzXk3g-2000-80.jpg)
![AMD Helion rack.](https://cdn.mos.cms.futurecdn.net/KwFreiH9LLPrsYZGRWvHU4-802-80.png)



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi-140-80.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

* jp7189 said:"OpenU trays, which are 21mm wide and 48mm tall"  
    
  21mm ? Now that's dense! In reality, those trays are actually 537mmThanks for catching that! Inches, not mm. I've corrected the article. Reply
* jp7189 said:"OpenU trays, which are 21mm wide and 48mm tall"  
    
  21mm ? Now that's dense! In reality, those trays are actually 537mmYeah, ~19 inches is the standard rackmount chassis width. 1.75 inches (44.45 mm) is the height of a standard "rack unit". According to Wikipedia, 23 inches is another popular width.  
    
  I used to have some interest in running old, decommissioned server hardware at home. However, these machines are far too noisy, power-hungry, and expensive (even used!) for me to ever contemplate it. So, I have no personal interest in what rack form factor they use. A lot of them are now requiring liquid cooling, too. Reply

---
title: 'Powering the AI revolution: Inside the grid, thermal, and interconnect challenges
  limiting data center growth'
source_url: https://www.techradar.com/pro/powering-the-ai-revolution-inside-the-grid-thermal-and-interconnect-challenges-limiting-data-center-growth
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-11T19:33:50Z'
published: '2026-10-11T00:00:00Z'
description: The next-gen silicon revolution has met various infrastructure bottlenecks
image: https://cdn.mos.cms.futurecdn.net/PNHHupwLrzuujcF78JCsDN-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- AI
- Memphis
- North America
- Northern Virginia
- Tennessee
organisations:
- AC-DC
- AI GPU
- DC-DC
- Edison Electric
- Elon Musk-led AI
- Microsoft
- Reinhausen
- SMRs
- SSTs
- Siemens
- TechRadar Pro
- xAI
---

![Rows of server racks inside a modern data center](https://cdn.mos.cms.futurecdn.net/PNHHupwLrzuujcF78JCsDN-1920-80.jpg)

The AI boom is quickly reaching the physical limits of grid capacity and thermal dissipation. The electric grid is stretched as ever, causing longer connection waits for AI data centers, and conventional air and liquid cooling systems struggle to meet the demands of rapidly growing facilites.

As they continue growing at a rapid pace, AI data centers now face a mix of challenges, from computing power outpacing GPU interconnects’ data transfer abilities, to volatile load swings stretching grid power factor correction (PFC) systems and rack power density overloading traditional cooling systems.

Let’s break down the major thermal and electrical bottlenecks slowing the AI boom and how companies are innovating their way out.

## The thermal wall (Rack-level friction)

Standard server racks generate a lot of heat, and high-performing GPU clusters generate even more, pushing thermal limits further than ever. Modern GPU racks exceed 50 to 100 kW of power consumption per cabinet, making traditional air and liquid cooling methods insufficient.

Standard cooling systems keep clusters operating between 65 and 85 degrees, but 90 to 100 degrees trigger performance throttling to prevent permanent GPU damage. With GPU racks drawing massive electrical energy, which converts into heat, preventing them from hitting throttling limits has become harder than ever.

Traditional air cooling systems weren’t built for rack densities surpassing 30 to 40 kW, which AI clusters easily surpass, with 100 kW or more becoming the norm. Maintaining airflow at high densities to cool 100 kW+ power racks requires running power-hungry fans at extreme speeds. This saps electrical energy and worsens the Power Usage Effectiveness (PUE) for the data centers. To cool mega AI clusters with air alone, operators would need “hurricane-grade” airflow, which is impractical. Then how about liquid cooling?

Liquid cooling relies on fluid mechanics, where cold plates use microchannels to force turbulent flows directly over chips to keep them cool. Keeping enough volume of fluid flowing through these microchannels requires massive pumping power, an increasing constraint for data center operators. To mitigate this challenge, operators are pivoting to direct-to-chip cold plates mounted directly on the processor, rather than over it, to keep it cool while consuming less pumping power.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

![An illustration of Microsoft&amp;rsquo;s closed-loop liquid cooling system](https://cdn.mos.cms.futurecdn.net/EGQ5BhpZKMGQqWFh6Q39nh-1200-80.png)

Phase-change mechanics are also helping GPU clusters cool more efficiently. Here, the clusters use the latent heat of liquid vaporization or solid-liquid transitions to absorb the massive heat spikes from high-density GPU racks. Specialized dielectric fluid comes in direct contact with the hot GPUs and then boils into vapor to instantly pull away heat. The vapor then rises, reaches a condenser, and converts back into liquid droplets via gravity, then drips back into the pool to repeat the process. This process is known as two-phase immersion cooling, and it reduces cooling energy by up to 40%.

Some data center operators are pivoting to closed-loop liquid cooling systems, where recirculated fluid cools the GPUs with little to no evaporation loss, removing the need for frequent top-ups.

For example, Microsoft, a top-three data center operator by capacity, has implemented a closed-loop system for newer data centers, where water is filled once and circulated to servers to absorb heat, moved to air-chilled coolers to cool down, then recirculated to absorb heat without needing fresh supplies. This system is costly and will take some time to roll out at scale, but it demonstrates how companies are innovating against thermal bottlenecks.

## The interconnect and board-level limits

GPU clusters rely on electrical copper or optical interconnects to share data, memory, and workloads. Electrical copper interconnects have long been the standard, but high GPU workloads have pushed them to the limit.

Electrical signals lose strength over long distances (greater than two meters), with usable reach halving every time bandwidth requirements double, and massive GPU clusters have made the communication distances longer than ever. Closely packed copper interconnects also generate electromagnetic interference that disrupts other signals, requiring complex equalization systems that drain more power.

There’s also the issue of power loss across copper plates on GPU circuit boards (due to resistance). The more current transmitted through copper plates, the more heat is generated, requiring more cooling energy that itself is already a bottleneck.

With electrical interconnects hitting their absolute limits, data center owners have little choice but to pivot to optical interconnects, which convert data into light pulses that travel through fiber optic cables with minimal loss over long distances. These cables are way thinner than copper bundles, creating more airflow paths in dense, heat-generating GPU racks.

Companies are even moving from pluggable fiber optic cables to silicon photonics, or co-packaged optics (CPO), where optical circuits are embedded directly on GPUs to transmit light over long distances. For now, optical interconnects are much costlier than electrical copper, costing up to 7x more in some GPU setups, but there’s little choice but to absorb this cost in the short term because the latter has reached physical limits. On the bright side, as more companies adopt optical interconnects and invest in mass production, the costs will likely reduce.

## The grid & substation crisis

Lastly, electric grid connection is the primary challenge affecting AI data centers. Modern electric grids weren’t designed to handle the rapidly increasing loads of AI data centers, with 30 GW of new capacity added worldwide from 2021 to 2025 alone. Rapidly growing additions have stretched the supply chain for electric grid components and introduced engineering challenges that grid operators must work around.

For instance, high-voltage transformers that ensure safe voltage delivery to GPU clusters are in short supply. Wait times have spiked from 6 to 12 months as of 2020 to two to four years currently, much longer than expensive mega GPU clusters can wait for their operations to get powered.

Existing power factor correction systems on grid networks have become strained by massive load draws from new AI data centers. GPU clusters shift power demand within seconds, with one second of low inference demand drawing stable power from the grid and the next second drawing excessive power because of usage spikes. These fluctuations create complex harmonics that overheat transformers and affect the grid, needing grid operators to invest heavily in mitigation systems.

AI clusters are scaling to gigawatt levels, pushing voltage step-down switchgear to its most tolerable limits. Larger transformers, needed to serve these gigawatt-level clusters, lower electrical impedance, forcing potentially high short-circuit fault currents down a line. If a short circuit ever occurs, magnetic fields exert tough mechanical forces on switchgear busbars, causing them to bend or rip free from their mechanical support. What comes next is a structural failure, which grid operators or isolated data center power networks can’t let happen.

Companies have turned to various solutions to counter these electrical bottlenecks. For one, there has been a major turn to solid-state transformers, which use high-frequency power electronics and semiconductors to step down voltage, not magnetic fields like conventional transformers.

![The efficiency and size of solid-state transformers vs. conventional magnet-based transformers](https://cdn.mos.cms.futurecdn.net/i3RKEaBX87HtsTYxwdr3Yo-1000-80.jpg)

High-frequency electronics enable solid-state transformers to actively regulate voltage and filter harmonics, leading to fewer fluctuations. They are 97 to 99% efficient, compared to 95% to 97% for conventional transformers, and that 1 to 2% difference adds up to a lot in gigawatt-level data centers. Better yet, they are much smaller and lighter than conventional transformers, enabling faster logistics and deployment.

However, SSTs introduce their own challenges. The internal high-frequency components and chips powering them are expensive, often five times or more per kVA than low-frequency alternatives. They also require multiple power conversion stages (AC-DC and DC-AC/DC-DC), and tiny losses compound during these conversions, making it difficult to hit peak efficiency. Internal components generate heat and age faster, requiring more active maintenance than conventional transformers.

Cost is also an issue, as SSTs are currently much more expensive to build and maintain than magnet-based transformers. However, with more investment in mass production, costs will likely reduce over time, allowing AI GPU clusters to adopt them faster. Siemens, the world’s second-largest transformer manufacturer, recently partnered with fellow German tech firm Reinhausen to mass-produce a modular solid-state transformer for AI data centers, and that’s just one example.

Because SSTs can’t be immediately adopted at scale, and conventional transformer shortages have contributed to long wait times for electric grid owners, AI data center owners have been forced to take matters into their own hands. Some have built their behind-the-meter power generation and substation systems to power GPU clusters as they wait to get connected to local grids. xAI, the Elon Musk-led AI company, added 59 portable natural gas turbines, with a combined capacity of over 400 MW, to power its *Colossus* data center in Memphis, Tennessee, while it waits for a grid connection.

Some data center owners are also looking at Small Modular Reactors (SMRs), where compact nuclear fission reactors generate power on-site, but that’s still mostly in the conceptual stage at this point. SMRs face various limitations, particularly very high costs compared to gas turbines or renewables.

Still, many other data centers, both in early and late construction phases or completed, remain in long queues for electrical grid connections. For instance, in Northern Virginia, which hosts the world’s largest cluster of data centers (570 and gradually increasing), new facilities face wait times of up to 14 years for a grid connection.

US-based electrical grid operators have invested massive amounts in upgrades ($208 billion in 2025 alone and $1.1 trillion in planned investments from 2025 to 2030, per Edison Electric) but still struggle to meet exploding data center demand. More investments are needed to address electrical grid bottlenecks, and so are new technologies that can reduce data center energy consumption to help distribution networks keep up.

## The reality of next-generation compute deployment

With technical details, we’ve explained the grid, thermal, and GPU interconnect bottlenecks stretching the next-generation AI compute deployment boom to its limits. These are serious physical and technical challenges that require innovative approaches to address, and fortunately, there’s been no shortage of these approaches.

We’ve outlined examples like electric grid operators turning to solid-state transformers that allow active voltage regulation and harmonic filtering to keep power systems stable, or some GPU cluster operators building their own power generation systems while they wait for local grid connections.

For thermal bottlenecks, GPU cluster operators are leveraging direct-to-chip cold plates mounted directly on GPUs, instead of over them, to stay cool while consuming less energy. Phase-change mechanics also help, where liquid vapor absorbs heat from GPU racks, pulls the heat away, and recondenses back into liquid to repeat the process, reducing energy needs by up to 40%.

Microsoft has tried to reinvent the wheel by implementing a closed-loop liquid cooling system, using liquid coolants continuously recirculated in a sealed pipe network with minimal top-ups.

However, closed-loop cooling systems are more difficult to expand than open-loop systems as GPU needs grow, and they can be louder under heavy loads as pump motors and radiator fans run simultaneously. At a time of growing public backlash against new data centers, environmental noise matters too, not just technical limitations. Closed-loop systems are also more expensive, but costs can reduce over time as more companies adopt them.

For interconnect limits at the circuit board level, companies are switching from electrical copper to fiber optic cables because they transmit data faster and more reliably over long distances, even though they cost more. GPU manufacturers are working on embedding optical circuits directly on chips to transmit light even more efficiently than cables.

Despite these challenges, AI data centers continue to grow at a rapid pace, with 66 GW of new capacity currently under construction in North America alone.

Looking to the future, it's clear a lot is happening in this area, and it’s exciting to watch the various approaches companies have adopted to surmount the electrical, thermal, and interconnect bottlenecks.

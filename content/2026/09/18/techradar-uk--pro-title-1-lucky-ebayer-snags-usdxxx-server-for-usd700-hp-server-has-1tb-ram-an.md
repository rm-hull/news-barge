---
title: An eBay HP C7000 listing crams sixteen blades into one chassis
source_url: https://www.techradar.com/pro/title-1-lucky-ebayer-snags-usdxxx-server-for-usd700-hp-server-has-1tb-ram-and-16-xeon-cpus-worth-more-than-usd4-000
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-18T04:33:40Z'
published: '2026-09-18T00:00:00Z'
description: 16 old Xeon, 1TB of DDR3, and a £500 price tag turn this HP server into
  an unusual find
image: https://cdn.mos.cms.futurecdn.net/Pme4bDE3PmPbWAArkCGpTX-2057-80.png
categories:
- Technology & Software
locations:
- Canberra
- Sandy Bridge-EP
- UK
- United States
people: []
organisations:
- C600
- ECC
- Efosa
- Google News
- HP
- NomadUK
- SK Hynix
- TechRadar Pro
- eBay
---

![HP C7000 enclosure](https://cdn.mos.cms.futurecdn.net/Pme4bDE3PmPbWAArkCGpTX.png) 

- **Sixteen Xeons give this ageing HP C7000 enclosure a surprisingly dense processor count**
- **The 1TB DDR3 memory pool remains the biggest number in the listing**
- **Each blade adds eight cores and sixteen threads to the overall configuration**

A UK seller trading as NomadUK has listed a fully populated HP C7000 blade enclosure for £500 per blade, roughly $700 at current exchange rates.

The bundle includes sixteen BL460c G8 servers, each built around a single Intel Xeon E5-2660 processor with 8 cores, 12 threads, and a 2.20 GHz base clock under the Sandy Bridge-EP architecture.

Multiplied across the chassis, it delivers 128 physical cores and 256 logical threads, backed by 1024GB of DDR3 memory spread across 32 modules of 32GB each, running at speeds up to 1600MHz through registered DIMMs.

## The hardware underneath the headline numbers

The listing shows that each blade uses the Intel C600 series chipset paired with an HP Smart Array P220i controller, supporting RAID 0 and RAID 1 across two small-form-factor drive bays per unit.

Network connectivity runs through an integrated FlexibleLOM slot, typically populated with a 10Gb dual-port adapter capable of Flex-10 partitioning when paired with a Virtual Connect module in the enclosure's interconnect bays.

HP rates the C7000 chassis at 10U, built to house up to 16 half-height blades vertically alongside up to 8 interconnect bays and 6 hot-plug power supplies feeding a shared power backplane.

Each blade also ships with Integrated Lights-Out 4 for out-of-band management, giving remote access to power state, health telemetry, and virtual media independent of the host operating system.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Memory population follows a four-channel design per processor, meaning each blade's DIMM slots must be filled in matched pairs to maintain full bandwidth rather than dropping into single-channel mode.

Combined, the 16 blades, the enclosure, the storage controllers, and 1024GB of registered memory carry an estimated resale value above $4,000.

According to the seller, each blade “has been professionally refurbished and checked for functionality.”

NomadUK carries 3,740 feedback entries with a 99.9% positive rating, though eBay does not independently audit refurbishment claims of this kind.

## Why the economics still work for buyers

A comparable listing surfaced in Canberra during February, where a Dell PowerEdge R820 with four Xeon E5-4650 processors and 1TB of DDR3L memory sold for close to $1,200.

That server used 32 modules of SK Hynix registered ECC memory at 32GB each, working out to roughly $1 per gigabyte at sale price.

Individual sticks of the identical HMT84GR7AMR4A-H9 part number were listed separately near $60 in the United States, meaning the memory alone nearly covered the asking price.

Another UK listing offers 16 32GB DDR3 PC3-10600R registered ECC modules, the same capacity and type used in this bundle, priced at £1,191.45 for 512GB, or roughly $100 per module at today's exchange rates.

Applied across all 32 modules in the HP enclosure, that puts the RAM alone near $3,200, which is what pushes the bundle's total value past the $4,000 mark once the chassis and controllers are factored in.

Equivalent DDR5 registered memory at server-grade capacity costs more than ten times that per-gigabyte rate today, which explains continued demand for DDR3-era enterprise stock despite its age.

However, buyers considering the HP bundle should account for the E5-2660's 95W TDP per socket.

This means that 16 active blades under load draw close to 1.5kW before accounting for chassis fans, interconnects, and shared power supply overhead.

Also, its firmware support for iLO 4 and the C600 chipset ended years ago, leaving buyers dependent on community-maintained tools for BIOS and controller updates.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png) 

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: Nvidia forced to dial back key bandwidth targets on Vera Rubin hardware — tweaks
  will affect target specifications for memory and interconnect fabric
source_url: https://www.techradar.com/pro/nvidia-forced-to-dial-back-key-bandwidth-targets-on-vera-rubin-hardware-tweaks-will-affect-target-specifications-for-memory-and-interconnect-fabric
source_site: TechRadar UK
source_slug: techradar-uk
description: Nvidia quietly edited Vera Rubin's spec sheet
image: https://cdn.mos.cms.futurecdn.net/MLH2WqUBs2jRD6pZ52Gdn6-1462-80.jpg
published: '2026-10-31T00:00:00Z'
scraped_at: '2026-11-01T00:05:19Z'
categories:
- Technology & Software
people:
- Jensen Huang
- Vera Rubin
locations: []
organisations:
- AMD
- AMD's
- Blackwell GPU
- CoreWeave
- FLOPS
- Google Cloud
- HBM
- HBM4
- HGX Rubin NVL8
- Hardware Busters
- Helios
- IT Home
- JEDEC
- Microsoft Azure
- Nvidia
- Rubin GPU
- SK hynix
- Samsung
- SemiAnalysis
- TechRadar Pro
- Tom's Hardware
- TrendForce
- Vera Rubin
- Vera Rubin NVL72
- Wayback Machine
- Wccftech
---

![Nvidia Vera CPU](https://cdn.mos.cms.futurecdn.net/MLH2WqUBs2jRD6pZ52Gdn6-1462-80.jpg)

* **Nvidia has quietly cut Rubin's listed HBM4 bandwidth from 22 TB/s to 19.2 TB/s per GPU and NVLink 6 from 3.6 TB/s to 3 TB/s**
* **The eight-GPU HGX Rubin NVL8 fares worst, losing 26% of its memory bandwidth and dropping from 2.3 TB to 2 TB of HBM4 capacity**
* **On paper, AMD's MI455X now leads on per-GPU memory bandwidth and Helios on scale-up bandwidth, though neither side's figures are benchmarked**

Nvidia has quietly lowered the memory and interconnect bandwidth it publishes for Vera Rubin, cutting per-GPU HBM4 bandwidth by about 13% and NVLink bandwidth by about 17%, without a press release or explanation.

The Vera Rubin NVL72 product page now rates each Rubin GPU at 19.2 TB/s of HBM4 bandwidth, down from 22 TB/s, and 3 TB/s of NVLink 6 bandwidth, down from 3.6 TB/s.

Memory capacity holds at 288 GB, and the headline 50 PFLOPS of sparse NVFP4 inference remains unchanged; however, at rack scale, aggregate memory bandwidth slips from 1,580 TB/s to 1,400 TB/s and the NVLink total from 260 TB/s to 216 TB/s, while the two-GPU Vera Rubin Superchip drops from 44 TB/s to 38.5 TB/s.

## An edit without an announcement?

The revision surfaced in a report from IT Home, which compared Nvidia's October documentation with a copy saved in June 2026. Wccftech then narrowed the window with Wayback Machine snapshots, placing the edit between September 1 and September 11. Nvidia, as Hardware Busters observed, went "the quiet way: by editing the product pages."

The timing matters here: the change landed shortly after Nvidia's August second-quarter results said Vera Rubin racks were already running at partners including CoreWeave, Google Cloud and Microsoft Azure, months after early systems began reaching select customers, and just as the fall production shipments Nvidia promised in May 2026 were due to begin.

This suggests the new figures describe hardware going out the door rather than a distant goal, and the nerfed figures sat on Nvidia's site for at least six weeks before anyone reported them.

The downgrade wasn't completely proportional, though, with some configurations taking a bigger hit.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Most noticeably, the HGX Rubin NVL8, Nvidia's standard eight-GPU server board, fares worst. The HGX page now lists 2 TB of HBM4 at 130 TB/s for the whole system, down from 2.3 TB and 176 TB/s, a 26% bandwidth cut.

NVLink Switch bandwidth falls from 28.8 TB/s to 24 TB/s, and dense training figures slip from 280 to 270 PFLOPS of NVFP4 and from 140 to 130 PFLOPS of FP8. Scale-out networking is the only line that rises, by 12.5% in most configurations, and Nvidia hasn't said why.

## Scaling back to ensure delivery?

Interestingly, the math does not hold completely anymore: its per-GPU table still advertises 288 GB at 22 TB/s with 3.6 TB/s of NVLink, figures that no longer add up to the system totals printed beside them, and Nvidia's July Rubin architecture deep dive still promises 22 TB/s. Split across eight GPUs, the new totals come to about 16.25 TB/s and roughly 250 GB each.

This fits two potential readings: eight smaller HBM4 stacks running at just under 8 Gbps per pin, the industry baseline, or one of the usual eight stacks disabled per GPU, a trick Nvidia used on the 80 GB H100, but Nvidia hasn't said which approach it took.

The retreat makes more sense given the history here: JEDEC's HBM4 standard, published in April 2025, specifies up to 8 Gb/s per pin across a 2,048-bit interface, or 2 TB/s per stack. Nvidia wanted far more, but it might have had to settle for less.

According to a TechPowerUp report from March, Rubin's per-GPU target climbed from 13 TB/s at GTC 2025 to 20.5 TB/s by that September and 22 TB/s at CES 2026, and a SemiAnalysis note it relayed said SK hynix and Samsung were struggling to reach the final figure, with early shipments expected to be nearer 20 TB/s.

TrendForce reported in September 2025 that Nvidia was pressing suppliers for 10 Gbps per pin as AMD readied Helios, and warned that if volumes fell short or costs ballooned, Nvidia "may abandon the upgrade or segment its platform products."

By January, TrendForce said the request had passed 11 Gbps and sent all three HBM makers back to redesign, though an Nvidia spokesperson told Tom's Hardware that "our HBM4 memory partners remain on track for production shipments." SK hynix finished HBM4 development first, and Samsung began shipping in February at 11.7 Gbps, above Nvidia's stated requirement.

More than a year after TrendForce's warning, the revised sheet reads like its fallback scenario: a lower overall ceiling, plus a further-reduced HGX tier, and this seems to be because Nvidia needs to deliver solutions to its customers as a higher priority than chasing an elusive memory bandwidth goal.

## Team Red for the win?

Because of the retreat, perceived or otherwise, the competitive picture shifts considerably, at least on paper. AMD's Instinct MI455X spreads 432 GB across 12 HBM4 stacks for 23.3 TB/s, which needs only about 7.6 Gbps per pin, below the JEDEC baseline. AMD bought its bandwidth with width rather than speed, so it never needed above-standard memory.

When it launched Helios in July 2026, AMD claimed 6% more HBM bandwidth than Vera Rubin NVL72's published figure; against the revised 1,400 TB/s, Helios' 1.67 PB/s is roughly 19% ahead. Scale-up bandwidth, Nvidia's traditional stronghold, was level at 260 TB/s per rack and now favors AMD by about a fifth, while the scale-out increase trims AMD's claimed 50% lead there to about a third.

For buyers running inference, the bandwidth line matters more than the FLOPS line. Nvidia's engineers write in that July deep dive that decode is bound by the memory subsystem, though they argue that what counts is how efficiently kernels use it, and that it is "not about peak bandwidth specs."

The marketing hasn't moved, however: the NVL72 page still promises up to 10x more tokens per megawatt and one-tenth the cost per million tokens versus GB200 NVL72, footnoted as subject to change, and Nvidia hasn't said whether it reran those projections on the lower figures.

None of this makes Rubin slow. At 19.2 TB/s, it still offers about 2.4 times a Blackwell GPU's 8 TB/s, rather than the 2.8x Nvidia's blog still claims. Jensen Huang said in August that "Vera Rubin, now in full production, was built to power exactly this moment." The moment, it turns out, arrived with a little less bandwidth than advertised.

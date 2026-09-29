---
title: AMD drops an EPYC $15,000, 256-core beast — EPYC 9006 Zen 6 'Venice' CPUs get
  full spec and pricing treatment, from $700 up to $14,904
source_url: https://www.tomshardware.com/pc-components/cpus/amd-drops-an-epyc-usd15-000-256-core-bomb-epyc-9006-zen-6-venice-cpus-get-full-spec-and-pricing-treatment-from-usd700-up-to-usd14-904
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-29T12:48:20Z'
published: '2026-09-29T00:00:00Z'
description: Zen 6 is ready to redefine data center performance.
image: https://cdn.mos.cms.futurecdn.net/tJZpPqKeTQpbXuGAQGpNKA-2560-80.png
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Tom
locations:
- Turin
- Venice
organisations:
- AMD
- EPYC
- Get Tom's Hardware
- Google News
- SP7
- SP8
- StorageReview
- TDP
- Tom’s Hardware
- Zhiye Liu
---

![AMD EPYC 9006 (Venice) CPU with Zen 6 cores](https://cdn.mos.cms.futurecdn.net/tJZpPqKeTQpbXuGAQGpNKA-1920-80.png)

After unveiling the EPYC 9006 (codenamed Venice) series in July and previewing a few impressive Zen 6 benchmarks, AMD has now released full pricing for its highly anticipated next-generation server chips. According to the list StorageReview obtained, AMD has big plans for the data center, with a wide range of SKUs from eight to 256 cores and pricing from $700 to $14,904.

![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB-1200-80.jpg)

As a quick refresher, AMD strategically divided the Venice lineup into two distinct segments. The SP7 platform is the flagship offering, delivering maximum memory capacity and throughput. It supports up to 16 memory channels, accommodating both RDIMMs and MDRDIMMs up to DDR5-12800. The platform offers up to 96 PCIe 6.0 lanes and supports Venice chips with TDPs between 400W and 600W.

The Venice parts designed for the SP7 socket offer scalable performance for enterprises. The lineup begins with the 64-core EPYC 9556, priced at $8,008, and extends to the flagship 256-core EPYC 9996, which commands $14,904. In retrospect, the EPYC 9996's price tag does not seem particularly shocking, especially since the previous-generation EPYC 9965 (codenamed Turin) launched at nearly the same price, around $14,800.

As is typical for server processors, the total price increases as the number of cores rises. However, the price per core actually decreases substantially as you move up the core ladder. The pricing dynamic is very notable with Venice. For example, the flagship EPYC 9996, with a massive 256 cores, comes out to just $58.21 per core, whereas the "entry-level" SP7 chip, the 64-core EPYC 9556, costs around $125.12 per core. As a result, higher core-count models are more attractive from a per-core value perspective for data centers, cloud service providers, and enterprises.

## AMD EPYC 9006 SP7 Specifications and Pricing

| Processor | 1Ku Price | Cores / Threads | Base / Boost Clock (GHz) | L3 Cache (MB) | Socket | TDP (W) |
| --- | --- | --- | --- | --- | --- | --- |
| EPYC 9996 | $14,904 | 256 / 512 | 2.55 / 4.10 | 1,024 | 1P / 2P | 600 |
| EPYC 9966 | $14,079 | 192 / 384 | 2.90 / 4.00 | 768 | 1P / 2P | 600 |
| EPYC 9846 | $13,114 | 168 / 336 | 2.85 / 3.70 | 768 | 1P / 2P | 500 |
| EPYC 9756 | $12,498 | 128 / 256 | 3.15 / 4.00 | 512 | 1P / 2P | 500 |
| EPYC 9G76 | $11,622 | 96 / 192 | 3.40 / 4.80 | 384 | 1P / 2P | 500 |
| EPYC 9686F | $11,434 | 96 / 192 | 3.40 / 5.00 | 384 | 1P / 2P | 500 |
| EPYC 9656 | $9,713 | 96 / 192 | 3.05 / 3.70 | 512 | 1P / 2P | 400 |
| EPYC 9586F | $9,701 | 64 / 128 | 3.75 / 5.00 | 384 | 1P / 2P | 500 |
| EPYC 9556 | $8,008 | 64 / 128 | 2.75 / 4.30 | 384 | 1P / 2P | 300 |

The SP7 SKUs support both 1P and 2P socket configurations. The latter, in particular, enables up to 512 Zen 6 cores in one system by pairing two EPYC 9996 chips on a single motherboard. That level of performance logically comes with a substantial investment, since the processors alone would cost $29,808 before factoring in the significant expense of memory today.

Among the nine SP7 SKUs, two models in particular stand out: the EPYC 9686F and EPYC 9586F. The "F" suffix means these chips feature maximum boost clock speeds, in this case, 5 GHz. While both are impressive in their own right, AMD optimized these parts to hit 5 GHz. Naturally, this level of optimization carries a price premium. For example, the 64-core EPYC 9586F costs almost as much as the 96-core EPYC 9656, despite offering 33% fewer cores. The trade-off is also apparent in the thermal envelope. The EPYC 9586F has a TDP that is 100W higher than the EPYC 9656.

## AMD EPYC 9006 SP8 Specifications and Pricing

| Processor | 1Ku Price | Cores / Threads | Base / Boost Clock (GHz) | L3 Cache (MB) | Socket | TDP (W) |
| --- | --- | --- | --- | --- | --- | --- |
| EPYC 9746 | $11,679 | 128 / 256 | 2.90 / 4.00 | 512 | 1P / 2P | 400 |
| EPYC 9736 | $10,639 | 128 / 256 | 2.70 / 3.70 | 256 | 1P / 2P | 360 |
| EPYC 9736P | $9,989 | 128 / 256 | 2.70 / 3.70 | 256 | 1P | 360 |
| EPYC 9676F | $10,116 | 96 / 192 | 3.10 / 5.00 | 384 | 1P / 2P | 400 |
| EPYC 9646 | $8,904 | 96 / 192 | 2.80 / 3.70 | 256 | 1P / 2P | 300 |
| EPYC 9646P | $8,001 | 96 / 192 | 2.80 / 3.70 | 256 | 1P | 300 |
| EPYC 9576F | $9,431 | 64 / 128 | 3.55 / 5.00 | 384 | 1P / 2P | 400 |
| EPYC 9536 | $7,837 | 64 / 128 | 3.25 / 4.00 | 256 | 1P / 2P | 300 |
| EPYC 9526 | $7,123 | 64 / 128 | 2.75 / 3.70 | 256 | 1P / 2P | 220 |
| EPYC 9536P | $6,595 | 64 / 128 | 3.25 / 4.00 | 256 | 1P | 300 |
| EPYC 9476F | $6,695 | 48 / 96 | 3.65 / 5.00 | 192 | 1P / 2P | 330 |
| EPYC 9456 | $5,252 | 48 / 96 | 3.20 / 3.70 | 256 | 1P / 2P | 265 |
| EPYC 9456P | $4,628 | 48 / 96 | 3.20 / 3.70 | 256 | 1P | 265 |
| EPYC 9376F | $4,849 | 32 / 64 | 3.80 / 5.00 | 192 | 1P / 2P | 285 |
| EPYC 9356 | $3,789 | 32 / 64 | 3.60 / 4.50 | 192 | 1P / 2P | 250 |
| EPYC 9336 | $3,320 | 32 / 64 | 3.15 / 3.70 | 128 | 1P / 2P | 195 |
| EPYC 9356P | $2,795 | 32 / 64 | 3.60 / 4.50 | 192 | 1P | 250 |
| EPYC 9276F | $3,512 | 24 / 48 | 3.80 / 5.00 | 96 | 1P / 2P | 230 |
| EPYC 9256 | $2,501 | 24 / 48 | 2.85 / 4.50 | 96 | 1P / 2P | 190 |
| EPYC 9176F | $3,787 | 16 / 32 | 3.90 / 5.00 | 192 | 1P / 2P | 200 |
| EPYC 9116 | $1,200 | 16 / 32 | 2.85 / 4.50 | 48 | 1P / 2P | 160 |
| EPYC 9016 | $700 | 8 / 16 | 3.05 / 4.80 | 48 | 1P / 2P | 130 |

The SP8 platform is a more streamlined and cost-effective counterpart to the SP7 platform for the Venice family. It supports eight-channel memory and does not embrace MRDIMMs. However, the limitation balances out by expansion possibilities, as the SP8 platform offers 128 PCIe 6.0 lanes, 33% more than the SP7 platform. Additionally, the SP7 platform has a lower thermal footprint, as these Zen 6 parts carry TDP ratings between 130W and 400W.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The SP8 platform offers an accessible entry point for organizations, with the octa-core EPYC 9106 priced at just $700. At the other end of the spectrum, the EPYC 9746, which is the top SP8 SKU, offers 128 Zen 6 cores at $11,679.

With the SP8 platform, we also see Zen 6 models with the “P” suffix, which indicates support for single-socket systems only. These variants deliver the same performance as their standard counterparts but at a significantly lower price. For example, the 128-core EPYC 9736P is 6% less expensive than the EPYC 9736. In an even more dramatic case, the 32-core EPYC 9356P retails for 26% less than the EPYC 9356.

One of the more unusual Venice chips is the 16-core EPYC 9176F. Despite its modest core count, it features a massive 192MB of L3 cache, 4X that of the 16-core EPYC 9116, while costing more than 3X as much. This translates to 12MB of L3 cache per core. With its high cache capacity and 5 GHz boost clock, AMD likely designed the EPYC 9176F for organizations seeking to minimize licensing costs for software priced per core.

AMD’s SP7 and SP8 platforms are scheduled to launch in the fourth quarter of this year and the first half of 2027, respectively. However, these Venice prices are not final, as AMD has stated that the list is subject to change. AMD will extend the lineup further later in 2027 with Venice-X chips, which use the company's 3D V-Cache stacking.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zhiye Liu](https://cdn.mos.cms.futurecdn.net/HhmwL5w9ggUtLCPfqGjTi4-140-80.jpg)

Zhiye Liu is a news editor, memory reviewer, and SSD tester at Tom’s Hardware. Although he loves everything that’s hardware, he has a soft spot for CPUs, GPUs, and RAM.

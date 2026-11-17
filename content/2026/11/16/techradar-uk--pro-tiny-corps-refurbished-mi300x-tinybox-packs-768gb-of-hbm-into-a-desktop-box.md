---
title: Tiny Corp's refurbished MI300X tinybox packs 768GB of HBM into a desktop box,
  and the price has already jumped by $29,000
source_url: https://www.techradar.com/pro/tiny-corps-refurbished-mi300x-tinybox-packs-768gb-of-hbm-into-a-desktop-box-and-the-price-has-already-jumped-by-usd29-000
source_site: TechRadar UK
source_slug: techradar-uk
description: Tiny Corp's $60,000 four-MI300X tinybox sold out in three days
image: https://cdn.mos.cms.futurecdn.net/n9QrZ8mixWzcJKcRWrBeY4-1920-80.jpg
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-17T03:47:26Z'
categories:
- Technology & Software
people:
- Hotz
locations:
- Genoa
- San Diego
- Tier 1
- US
organisations:
- AI Quanting
- AMD YOLO
- BMC
- HBM
- MI300X
- Microsoft
- SemiAnalysis
- TechRadar Pro
- Tiny Corp
- eBay
---

![A render of the tinybox red](https://cdn.mos.cms.futurecdn.net/n9QrZ8mixWzcJKcRWrBeY4-1920-80.jpg)

* **Tiny Corp's quad-GPU MI300X tinybox red sold its 25-unit, $60,000 first batch within three days**
* **The cards are refurbished, come without warranties, are capped at 500W, and are linked only over PCIe 5.0**
* **A 50-unit second batch is now on preorder at $89,000, about 48% more, shipping Q1 or Q2 2027**

Tiny Corp has squeezed four of AMD's Instinct MI300X data center accelerators into a box that runs off ordinary wall power.

The first batch sold out within three days, and the second costs nearly 50% more than the former.

The tinybox red 4xMI300X went up for preorder on November 5 2026 at $60,000, with 25 units in the first batch; but a few days later, a breakdown posted by the AI Quanting account on X noted that the store page already showed it as out of stock.

## Data center silicon coming to a pricier desktop near you?

Tiny Corp is now taking preorders for a second batch of 50 units at $89,000, about 48% above the launch price, with delivery penciled in for Q1 or Q2 2027, though Tiny Corp stops just short of committing to either as a firm timeline.

On paper, the numbers are hard to argue with: 768GB of GPU memory, 21.2TB/s of aggregate memory bandwidth and 10.44 PFLOPS of FP8 compute. Those figures are exactly four times AMD's own per-card specifications: 192GB of HBM3, 5.3 TB/s, and 2.61 PFLOPS of dense FP8.

The listing is also more conservative to boot: Tiny Corp quotes the dense figure rather than the 5.22 PFLOPS AMD lists with structured sparsity.

The host itself is a capable 32-core, water-cooled AMD EPYC Genoa platform with 192GB of DDR5 RAM, a 1TB boot drive, four 1TB drives in RAID 0, two 10GbE ports, and an OCP 3.0 slot. Two standard 1,700W ATX power supplies feed the 54V the GPUs need through a converter, so the box runs on one 220V circuit or two 110V circuits. Tiny Corp claims it stays under 50dB, which would make it far quieter than the rack servers MI300X cards normally live in.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Interestingly, these are not the MI300X modules AMD sells to hyperscalers. Tiny Corp refurbishes the cards itself, and they carry no warranty or support from AMD. Each sits on a carrier board Tiny Corp designed, with its own BMC microcontroller, rather than on a standard OAM module.

There are no XGMI links between the GPUs; each gets a dedicated PCIe 5.0 x16 link to the host instead. AMD's reference design gives every MI300X eight Infinity Fabric links at 128GB/s apiece, so in this box all GPU-to-GPU traffic travels a much narrower road. How that impacts performance is not yet known, with Tiny Corp offering no benchmarks.

Power is the other quiet compromise. The cards are capped at 500W via a 600W connector, compared to AMD's 750W board power rating. The 10.44 PFLOPS headline is AMD's peak at full power, so with each card running at two-thirds of that budget, sustained compute should theoretically land below the chipmaker's published figure.s

Tiny Corp hasn't published sustained numbers yet; however, memory bandwidth should suffer less from a power cap, and for single-user inference, that is the figure that matters most.

## A great deal despite tradeoffs?

The company is unusually candid about the tradeoffs. It warns that the software may be rough at first, but insists "none of the issues should be anything a good agent can't handle."

On X, it called the configuration plainly unsupported by AMD, while a companion post offered "huge thanks to AMD for supporting us". The two statements could run in parallel here if you read it as AMD having backed the company, not this particular build.

The listing also promises the cards will have no uncorrectable HBM errors. That guarantee matters more than it might seem: SemiAnalysis has reported that Microsoft walked away from AMD after the MI300X, partly due to unreliable Samsung HBM from 2023. Tiny Corp hasn't said where its refurbished cards came from, so buyers are invoking a lot of trust here.

The MI300X box caps a remarkable reversal. In early 2024, Tiny Corp's first $15,000 tinybox with six Radeon RX 7900 XTX cards drew 583 preorders. Within weeks, the AMD version was put on hold as the company publicly complained that the driver was still very unstable, before it reversed course days later. A year later, Hotz's "AMD YOLO" blog post announced that AMD was shipping the two MI300X systems Tiny Corp had requested.

Tiny Corp also relaunched the tinybox in October around four Radeon RX 9070 XT cards for $11,000, and weeks later its configurator turned AMD-only after a commit titled "rip nvidia".

Despite the price hike, the secondhand market makes the box look cheap: Single used and refurbished MI300X OAM modules listed on eBay, as tracked by GPU Poet, were asking between about $27,550 and $40,300 on November 16, before anyone supplies a baseboard, host, or power. Even at $89,000, the tinybox works out to about $22,250 per GPU with the rest of the computer included, though asking prices on eBay are not sale prices.

Not everyone can buy one, either. The listing says the system is export-controlled and will only ship from San Diego to Tier 1 countries, meaning the US and its close allies. Orders are capped at two per customer, and buyers have 7 days to wire funds before an order is canceled.

A 48% price rise in under a week says plenty about demand for large pools of HBM outside the cloud. But batch two buyers are paying in 2026 for 2027 delivery of warranty-free, refurbished hardware in a configuration AMD doesn't support, and the tokens-per-second figure that would settle the value question has yet to be published officially by the company.

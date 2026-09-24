---
title: Nanya-backed Piecemakers bets edge AI devices will diverge from reliance on
  HBM
source_url: https://www.tomshardware.com/tech-industry/semiconductors/piecemakers-bets-edge-ai-devices-will-diverge-from-reliance-on-hbm-custom-designed-memory-fuses-dram-stack-directly-to-the-processor-using-hybrid-bonding
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-16T19:32:05Z'
published: '2026-09-16T00:00:00Z'
description: Nanya-backed DRAM designer PieceMakers began trading in Taipei on Sept.
  16 on a bet that AI inference memory won’t be HBM.
image: https://cdn.mos.cms.futurecdn.net/wPT2pgJDrMKWtsy78z2WnY-1920-80.jpg
categories:
- Technology & Software
- Hardware
locations:
- China
- France
- Hsinchu
- Israel
- Japan
- San Jose
- Taiwan
- Turkey
people:
- Cristiano Amon
- Groq
- Igor Arsovski
- Jaesik Lee
- Joseph Ting
- Lee Hsiao-wen
- Pei-Ing Lee
- Rubin
- Shane Downing
organisations:
- AI
- Cnyes
- Counterpoint Research
- Emerging Board
- Emerging Stock Board
- Etron Technology
- Formosa Advanced Technologies
- Formosa Plastics Group
- GTC
- Groq 3 LPU
- Groq LPU
- HBM
- HBM3
- HBM4
- Hot Chips
- ISSCC
- Intel
- KGD
- NRE
- Nanya Technology
- Nvidia
- Nvidia’s Rubin CPX
- PieceMakers
- PieceMakers’
- Piecemakers
- Qualcomm
- Rubin GPU
- SK
- SRAM
- Samsung
- Sangwook Han
- Shane Downing
- SoC
- Taipei Exchange
- TechNews
- Tom’s Hardware US
- TrendForce
- UDN
---

![Semiconductor chip](https://cdn.mos.cms.futurecdn.net/wPT2pgJDrMKWtsy78z2WnY.jpg) 

PieceMakers, a Nanya-backed DRAM designer, began trading on Taiwan’s Emerging Stock Board on September 16 at a NT$740 reference price, *Cnyes* reported ahead of the debut. PieceMakers is not an HBM company. Instead, it bets that inference memory diverges from training memory, President Lee Hsiao-wen told C*nyes*, and that DRAM stacked directly on the processor with hybrid bonding can sit between Nvidia’s SRAM-only Groq LPU and HBM. As it stands, design fees, not chips, carry the company's profit, with AI custom-design work accounting for around 40% of the company's revenue in the first half of 2026. Piecemakers Chairman Joseph Ting told* TechNews* that its first volume customer program will not contribute to the company's financials until 2027 at the earliest.

At roughly 60.4 million shares outstanding, that price values the company at around NT$44.7 billion (around $1.4 billion). Taiwan's Emerging Board is the Taipei Exchange's pre-listing market, not a main-board IPO, so shares trade through market makers ahead of any formal listing application. The stock ended its first session at NT$915, 23.6% above the NT$740 reference price, after opening at NT$1,035 and trading as high as NT$1,205.

Nanya Technology is the largest holder of Piecemakers, at 33.96%, after selling 715,000 shares at NT$740 to seed the float, a disposal it disclosed in a Sept. 9 exchange filing reported by *Knews*.

## What PieceMakers sells

PieceMakers was founded in January 2006 in Hsinchu, Taiwan, led by chairman Joseph Ting and president Lee Hsiao-wen. Historically, the company has designed standard SDR/DDR DRAM and known-good-die (KGD) parts through representatives in China, Japan, France, Turkey, and Israel. Now, the company seeks to shift from direct product sales to custom design services, paid as non-recurring engineering (NRE) fees, and then to IP licensing, royalties, and turnkey production from 2027, the company said at its Sept. 7 briefing, *UDN* reported.

Revenue from the AI custom design unit has risen from around 4% in 2024 to almost 40% in the first half of 2026. The products behind that increase are HBLL (High Bandwidth, Low Latency RAM), a 2D die rated at 144 GB/s that was taped out in 2016 for Intel’s HPC line and published at ISSCC in 2017, and HiBaLL, the 3D-stacked version rated at more than 1 TB/s, the company claims.

The company described its customers to *Cnyes* as developers of cloud AI inference accelerators, international semiconductor players, and North American customers, with some programs in design and verification, and none named. Qualcomm CEO Cristiano Amon’s Computex keynote backdrop in June listed PieceMakers among Taiwan ecosystem partners, although neither company has defined the relationship. The takeaway is that the profit is in design fees and not chips. The margin curve matches a pre-royalty Non-Recurring Engineering (NRE) business, rather than a traditional memory vendor.

## Why Nanya is chasing this instead of HBM

Nanya’s AI-memory strategy is custom and edge rather than HBM3E. PieceMakers is the first half of a strategy laid out in 2024. On Aug. 7, 2025, Nanya announced a joint venture with Etron Technology, a Hsinchu-based chip designer, capitalized at NT$500 million, with 80/20 ownership. The venture was envisioned to design custom high-bandwidth memory for edge AI devices rather than for data center accelerators. Nanya president Pei-Ing Lee said earlier in 2025 that the company would not compete in HBM3 or HBM3E, *TrendForce* reported.

Both halves of the strategy rely on Formosa Advanced Technologies, the Formosa Plastics Group’s test and assembly affiliate, for packaging. It is building the through-silicon-via (TSV) and die-stacking processes that both need. The surge in DRAM pricing has made commodity memory Nanya’s real business, which leaves PieceMakers a cheap side bet that has become a windfall. Nanya took advantage of this by selling around 3% of its stake in a move that suggests it is acting more as an investor than a parent building a memory stack.

## The inference gap

Groq is an AI inference startup that Nvidia struck a $20 billion licensing-and-talent deal for on Dec. 24, 2025. Nvidia announced its first chip built from that, the Groq 3 LPU (language processing unit), Nvidia’s SRAM-based inference chip, at GTC, its annual developer conference, in San Jose earlier this year.

There is no HBM or DRAM on the Groq 3 LPU. Instead, it uses 512MB of SRAM on the die to deliver 150 TB/s of bandwidth against 22 TB/s from the 288GB of HBM4 on each Rubin GPU. It’s a decode-only co-processor with Rubin handling the prompt prefill, displacing Nvidia’s Rubin CPX from the roadmap. 

At Hot Chips 2026, Nvidia’s Igor Arsovski, Groq’s former chief architect, said the rack is in production and published the first third-party benchmark: 3,431 tokens per second on a 100K-context, 31B-parameter model, at about four times the next-fastest public endpoint, in a single-request test that we noted isn’t directly comparable to the shared endpoints it was measured against. The cost is capacity: at 512MB per chip, a 256-LPU rack holds 128GB, with the model needing 62 chips at FP8 just to hold the benchmark weights. Nvidia accepted that trade for decode speed, which supports Lee’s point that the market leader’s newest inference product contains no HBM.

At Hot Chips, Samsung’s Sangwook Han laid out a three-phase HBM roadmap that ends in zHBM, which is DRAM stacked directly on top of the processor rather than beside it on an interposer. Samsung projects about 70% less I/O power usage than HBM5 with roughly 2.3x the bandwidth of a four-stack HBM4E system, with zHBM’s stacks limited to about four-high due to heat, at around 100W less. This would require wafer-on-wafer hybrid copper bonding and tight co-design between DRAM and SoC teams. SK hynix’s Jaesik Lee, VP of package engineering, said on Aug. 23 that hybrid bonding won’t be ready for HBM4E, leaving HBM5 as the earliest point. Counterpoint Research expects full-scale HBM production with the technique around 2029–2030.

PieceMakers offers a different version. Instead of the GPU-plus-HBM 2.5D layout, it bonds the DRAM stack directly onto the processor, wafer-on-wafer, with hybrid bonding instead of microbumps. This fits far more connections with the finer pitch, improving bandwidth, and the shorter path reduces both latency and power consumption. The company puts its wafer-on-wafer product at more than 2 TB/s per layer with latency under 20ns, the company figures, but the target is more capacity than SRAM at a lower cost and power than HBM. PieceMakers is not doing the TSV or hybrid bonding itself, as this is handled by the customer’s logic wafer foundry, Ting added. This custom service promises a 2027 date against Samsung's undated roadmap end and SK hynix's HBM5-at-the-earliest timing. Nvidia and Samsung have each, in their own way, settled the architecture question, with the open question being the customer.

## Yield is the product

Lee also said that yield is the biggest hurdle to wafer-on-wafer mass production. The repair architecture has to be designed in, with testing before bonding, after bonding, and then after logic integration. Lee’s own example was 80% yield per layer, at which four layers come out at about 41% and eight at 17%. Our recently-published hybrid bonding state of play covers the process side in more detail.

This better puts into perspective why the company sells repair and known-good-die IP as much as it does bandwidth. It’s also why an IP-and-royalty model fits the strategy — yield IP is portable across customers while a bandwidth number is not.

## What to watch

For PieceMakers, AI revenue remains primarily NRE until there is a first named customer, with the first volume program expected in 2027 at the earliest. Ting said that Nanya’s Q3 2026 results, which come in late October, will gauge the PieceMakers gain and reveal further financial information. SK hynix’s hybrid-bonding timing, which targets HBM5 at the earliest, is the current benchmark, although its 16- and 20-layer memory stacks are a separate problem from a few DRAM layers on a logic wafer. Qualcomm may also describe its relationship with PieceMakers more formally.

PieceMakers is likely to end up as an IP licensor with a small number of accelerator customers and turnkey volume through Nanya and Formosa Advanced Technologies. The technology risk is the foundry’s and the customer’s, which is why PieceMakers’ design-fee model works. PieceMakers is expected to benefit from a 2027–2028 ramp, later than Ting’s 2027. If the largest HBM maker won’t bond its own memory this way before HBM5, PieceMakers’ own 2027 date is the one it must meet.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69.png) 

Shane Downing is a Freelance Reviewer for Tom’s Hardware US, covering consumer storage hardware.

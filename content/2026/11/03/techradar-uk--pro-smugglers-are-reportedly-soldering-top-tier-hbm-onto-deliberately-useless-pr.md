---
title: Smugglers are reportedly soldering top-tier HBM onto deliberately useless processors
  to sneak it into China, and the trick isn't new
source_url: https://www.techradar.com/pro/smugglers-are-reportedly-soldering-top-tier-hbm-onto-deliberately-useless-processors-to-sneak-it-into-china-and-the-trick-isnt-new
source_site: TechRadar UK
source_slug: techradar-uk
description: It's a complex, but old, trick
image: https://cdn.mos.cms.futurecdn.net/Vh7faVPCzVhmG9B8VHujyV-1252-80.png
published: '2026-11-03T00:00:00Z'
scraped_at: '2026-11-03T23:16:25Z'
categories:
- Technology & Software
people:
- Faraday
- Greg Lui
- Steve Wang
- Yih-Shyan Liaw
locations:
- CoAsia
- Faraday
- Greater China
- Hong Kong
- Malaysia
- Shenzhen
- Singapore
- South Korea
- Southeast Asia
- Taiwan
- US
- Wccftech
organisations:
- AB Kuai.Dong
- AI Frontiers
- BIS
- Bureau of Industry and Security
- CoAsia Electronics
- Earthmade Computer
- Faraday Technology
- HBM
- HBM2E
- HBM3E
- Huawei
- Nvidia
- SBS News
- SK hynix
- SPIL
- Samsung
- SemiAnalysis
- Seoul Economic Daily
- Super Micro
- TSMC
- Taipei Times
- TechRadar Pro
- The Information
- TrendForce
- US Commerce Department
---

![China&#039;s flag overlays laptop screen](https://cdn.mos.cms.futurecdn.net/Vh7faVPCzVhmG9B8VHujyV-1252-80.png)

* **Smugglers are reportedly pairing Samsung and SK hynix HBM with deliberately useless processors so the package passes export regulations as a low-end chip**
* **Shenzhen workshops then heat the packages, pry off the HBM3E, and sell it for about $4,000 a stack, mostly to Huawei customers**
* **The trick exploits a December 2024 BIS exclusion for co-packaged chips, but only "where the dominant function" is processing**

Some of the most sought-after memory in the AI industry is reportedly reaching China attached to processors that were designed never to be used.

A new report from *The Information* claims smugglers are taking high-bandwidth memory (HBM) made by Samsung and SK hynix, packaging it alongside cheap, low-performance server chips, and exporting the combination as an ordinary processor with a CPU that nobody really wants.

Once the packages reach mainland China, workshops heat them until the solder gives way, pry off the memory stacks, and discard the processors.

## A processor nobody wants paired to memory that has Chinese buyers lining up for more

The scheme reached a much wider audience when Chinese tech commentator AB Kuai.Dong summarized the report for his followers on X, describing the decoy chips as "clunky" processors and calling the arrangement a "compliant export.

Reporting from Wccftech sheds more light on the smuggler at the center of the story: a man in his 40s, fluent in Chinese and Korean, with a background in the Korean chip industry.

He runs what is on paper an ordinary chip design firm with an interesting caveat: Its processors are reportedly so weak that no data center would buy them, which is the point: they give the company a reason to order top-tier HBM in volume.

Packaging houses in Taiwan, South Korea and Southeast Asia then reportedly bond the memory and the processor onto a single substrate, and the package ships to Hong Kong declared for export reasons as a processor. From there, it crosses into the mainland in luggage, car trunks, and the bags of daily cross-border commuters, being smuggled en masse to Chinese workshops.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The last step is arguably the riskiest: Seoul Economic Daily reports that excessive or overly rapid heat can warp or crack the memory stacks, and that failure rates are high. The margins are large enough that nobody involved minds the potential risk.

## Skirting export compliance at $4,000 a stack

The entire process is possible due to a gap that sits in the rules the US Commerce Department's Bureau of Industry and Security (BIS) published in December 2024. Those rules require a license to ship standalone HBM with a bandwidth density above 2GB/s/mm^2 to China, but a technical note excludes co-packaged chips that combine HBM and logic.

Those are instead judged by the package's processing performance. Pair a fast memory stack with a slow processor, and you get a chip cleared for export even if the primary goal is to secure the HBM rather than the underlying chip.

To its credit, the BIS did anticipate this in some form: The same note keeps HBM under control when it is permanently affixed to a logic die that merely serves as a control interface to the physical layer, so a memory stack sitting on a thin controller does not escape.

What it did not account for was a processor engineered to be useless. Interestingly, the exclusion applies, in the regulator's own words, only "where the dominant function of the co-packaged integrated circuit is processing." It is hard to argue that processing is the dominant function of a package whose value lies almost entirely in its memory.

Nothing about this approach is new: In April 2025, SemiAnalysis reported that CoAsia Electronics, Samsung's HBM distributor in Greater China, was shipping HBM2E to Taiwanese design services firm Faraday Technology, which had SPIL package it with a low-cost 16nm logic die before sending it on to China, where the memory could reportedly be desoldered. "The HBM export ban is specifically for raw HBM packages," the analysts wrote.

Faraday denied breaching export rules and said it had no ties to Huawei. Company president Steve Wang went further, telling the Taipei Times that "It is impossible to recover an HBM unit through desoldering." A year and a half later, The Information's sources describe Shenzhen workshops doing precisely that even as the approach remains relatively risky.

By September 2025, SemiAnalysis believed the CoAsia and Faraday flow had stopped, though it estimated China had already amassed about 13 million HBM stacks, including 11.4 million directly from Samsung, some 7 million of them in the month between the December 2024 rule's announcement and its subsequent enforcement.

Teardowns have already found Samsung and SK hynix memory inside Huawei's Ascend 910C. As recently as February 2026, AI Frontiers described the packaged HBM breach as apparently contained, while urging BIS to issue red-flag warnings on packaged HBM deployed in ways that tend to "allow the memory to be easily removed from finished chips after export."

If The Information's sources are correct, the technique was never really contained, only made quieter. It has moved up a generation to HBM3E and spread. At $4,000 a stack and willing buyers available across the board, it isn't altogether surprising either.

A Shenzhen broker in his early 20s, about three years into the trade, told The Information that a single HBM3E stack sold for a few hundred dollars in China a year ago. "Today it's about $4,000," he said, highlighting a near-tenfold increase in price due to an HBM-starved Chinese market.

With six to eight stacks required per AI accelerator, memory alone comes to $24,000 to $32,000 per chip, before the processor, server, or power bill is even considered.

TrendForce, also citing the same report, states that Huawei has raised the suggested price of its Ascend 950DT to more than RMB 250,000 (about $37,000), blaming memory costs and tight supply. This means that the black-market HBM for a single accelerator would be considerably more than half of the sticker price, though the 950DT's own stack count is not specified.

SK hynix said in a statement carried by SBS News that it complies with US and South Korean export controls and has not supplied Huawei since US restrictions took effect in 2020. Samsung has not directly commented in any coverage so far, and neither BIS nor the South Korean government has said anything publicly. Seoul Economic Daily notes the precedent Korean suppliers will be watching: TSMC faced a US investigation in 2024 after one of its chips was found in a Huawei product.

This is in the backdrop of US enforcement gathering pace as it goes after some of the allegedly worst offenders: In March, prosecutors charged Super Micro co-founder Yih-Shyan Liaw and two others over an alleged $2.5 billion scheme to route servers built on restricted Nvidia chips to China. On October 1, federal agents arrested Greg Lui, CEO of California-based Earthmade Computer, over more than $300 million of export-controlled servers allegedly shipped via Malaysia and Singapore.

The Information's report, however, leans heavily on anonymous dealers, with no shipment volumes, seizures, company names, or failure-rate figures attached. Despite this, the incentives it describes are real, and the method was documented more than 18 months ago by SemiAnalysis.

Until BIS either counts the memory or holds co-packaged chips to that "dominant function" test, the market for processors nobody wants is likely to stay surprisingly healthy and functional even as Chinese AI memory appetite remains voracious.

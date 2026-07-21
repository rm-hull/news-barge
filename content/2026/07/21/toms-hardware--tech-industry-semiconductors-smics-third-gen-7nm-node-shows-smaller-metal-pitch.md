---
title: SMIC's third-gen 7nm node shows smaller metal pitch than Intel 18A, higher
  transistor density than TSMC N6 without EUV — analysis of N+3 shows significant
  advancement for Chinese semi manufacturing
source_url: https://www.tomshardware.com/tech-industry/semiconductors/smics-third-gen-7nm-node-shows-smaller-metal-pitch-than-intel-18a-higher-transistor-density-than-tsmc-n6-without-euv-analysis-of-n-3-shows-significant-advancement-for-chinese-semi-manufacturing
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-21T14:17:56Z'
published: '2026-07-21T00:00:00Z'
description: But its transistor density is well behind 18A's.
image: https://cdn.mos.cms.futurecdn.net/jNq3T5Z4DQqsDU65zadz5A-1280-80.png
---

![SMIC](https://cdn.mos.cms.futurecdn.net/jNq3T5Z4DQqsDU65zadz5A.png) 

An analysis of Huawei's Kirin 9030 system-on-chip (SoC) for smartphones conducted by SemiAnalysis revealed that SMIC's third-generation 7nm-class fabrication technology (N+3) has smaller metal pitch than Intel's 18A fabrication technology and that China's leading foundry has managed to achieve transistor density on par with manufacturing process that rely on EUV lithography. But does this make SMIC's N+3 node as competitive as Intel's 18A or TSMC's N2 and N3? Not really.

 ![tsmc](https://cdn.mos.cms.futurecdn.net/p2QqhVFP7dTRWfeVBCYBYV.jpg) 


SemiAnalysis' teardown indicates that SMIC's N+3 fabrication process supports a minimum metal pitch of 32.5nm, which is nominally tighter than the approximately 36nm pitch used for many high-performance cells in Intel's Panther Lake CPU, even though 18A can support approximately 32nm metal pitches. The video from SemiAnalysis and High Yield does not reveal other important characteristics of SMIC's N+3, such as contacted gate pitch (CGP), standard cell height (tracks or nm), or fin pitch, so we cannot make direct comparison of this node to Intel's or TSMC's technologies. What it does reveal is estimated transistor density of around 113.4 million transistors per square millimeter (Mtr/mm2), which is even higher than transistor density of TSMC's N6, 107.7 Mtr/mm2.

TSMC's N6 uses multiple EUV layers, so achieving higher transistor density without using EUV lithography is an indisputable technological achievement of SMIC. The foundry achieves this density by using DUV multi-patterning, including self-aligned quadruple patterning on the tightest layers, and extensive design-technology co-optimization (DTCO). In addition, SemiAnalysis believes that SMIC used techniques like reduced fin counts, placing contacts directly over active gates, and tightening cell isolation. Such methods allow for increased transistor density, but at the cost of increased process complexity, cost, yield risks, and design constraints.

![Did China just beat Intel? - YouTube](https://img.youtube.com/vi/NAbpjiQNUMs/maxresdefault.jpg) 

Meanwhile, transistor density does not equal overall process competitiveness. Despite its compact layout, the Kirin 9030 reportedly delivers performance comparable to flagship application processors from roughly three years ago and has a substantial energy-efficiency disadvantage compared with modern Apple, Qualcomm, MediaTek, and Samsung designs. Huawei's highest performing CPU core is characterized as roughly Cortex-X2-class in IPC, while Apple's much smaller efficiency cores reportedly outperform it in integer workloads and consume considerably less power.

Given the fact that Kirin 9030 is neither a performance nor efficiency champion, the provocative comparison with Intel 18A is not exactly justified. Although SMIC N+3 has 32.5nm minimum metal pitch that is nominally tighter than the approximately 36nm pitch used in Panther Lake, 18A offers both higher transistor density and considerably higher performance efficiency. In addition, 18A uses gate-all-around transistors and backside power delivery, which make it particularly suitable both for mobile SoCs and for data center applications.

SemiAnalysis concluded that while export restrictions have slowed China's technological progress, progress is still being made. SMIC could potentially continue increasing density by tightening upper and lower metal layers, shorter standard cells, smaller gate pitches, and eventually backside power delivery. If the company continues scaling, N+4 could approach TSMC N5-class density, while N+5 with backside power might reach Intel 18A-class density, according to SemiAnalysis. Still, transistor density alone does not necessarily bring substantial improvements of performance or power efficiency.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

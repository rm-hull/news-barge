---
title: CXMT's DDR5 RAM isn't as performant or as consistent as SK hynix dies, early
  testing shows — reveals resistance to voltage scaling and inferior manual overclocking
  capabilities
source_url: https://www.tomshardware.com/pc-components/ddr5/cxmts-ddr5-ram-isnt-as-performant-or-as-consistent-as-sk-hynix-dies-early-testing-shows-reveals-resistance-to-voltage-scaling-and-inferior-manual-overclocking-capabilities
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-15T17:34:51Z'
published: '2026-07-15T00:00:00Z'
description: You can't tighten the timings either, apparently.
image: https://cdn.mos.cms.futurecdn.net/SMjmNQxCWZ5mDLST6ojeZE-804-80.jpg
---

![KingBank ddr5](https://cdn.mos.cms.futurecdn.net/SMjmNQxCWZ5mDLST6ojeZE.jpg) 

Homegrown DDR5 memory from China, manufactured by ChangXing Memory Technologies, has been making the rounds lately as more and more vendors start legitimizing it. However, new testing from overclocker Safedisk, shared by Uniko's Hardware, purportedly shows that it actually carries inferior performance compared to similar options from SK Hynix, alongside significant variance in the silicon between different batches.

kingbank 2x24 6000c36 1.25 kit (cxmt 3gb dies) on asus c10amanual oc to 8600c44 mt 100%key characteristics of cxmt dies- dont scale with voltage- cant tighten timings- silicon variance appears to be massive between batches- not as strong as hynix when it comes to manual… pic.twitter.com/WNPRiHj233July 15, 2026


CXMT began producing DDR5 in late 2025 despite lacking any cutting-edge EUV lithography tools. Fast forward to today, and reports of the company matching Micron's memory capacity by this year are now floating around. If true, China would become the second-largest memory maker in the world. At such scale, it's no wonder that many companies in China have already started sourcing CXMT-made RAM to fill the gap in the consumer market.

Throughout 2026, we've seen motherboard manufacturers verify CXMT's DDR5 with official BIOS optimizations that allow it to run beyond 8,000 MT/s at this point. OEMs such as Dell and HP are using CXMT RAM in their region-bound systems, and even proper PC hardware companies like Corsair are using CXMT modules. Lexar, Kingbank, Netac, Asgard, Gloaway and more are also producing retail DDR5 kits with CXMT chips.

As such, the testing features a Kingbank 48GB (2x24) DDR5-6000 kit running at CL36 and found several weaknesses despite successfully achieving an 8,600 MT/s overclock at CL44. The first revelation is that CXMT modules don't scale with voltage, meaning you can't just increase voltage in hopes of achieving higher clocks. CXMT's DDR5 apparently doesn't respond well to tuning sub-timings either, forcing you to remain stuck with baseline CAS latency (or higher, like in this case).

Different batches of CXMT-equipped memory perform differently, too, so silicon lottery plays a much bigger role than it would with other vendors. Speaking of which, SK Hynix-made DDR5 modules allegedly performed better at identical clock speeds, while CXMT's modules were less susceptible to overclocking in general. We didn't get any comparative benchmarks for any metric, so take these claims with a grain of salt.

Overall, if Asus' testing is to be believed, it serves as counterprogramming against the popular narrative forming around China as the savior of consumer interests. CXMT's strength lies in the fact that it doesn't have to cater to opulent AI clients as much as the Big Three, which reduces opportunity cost, allowing CXMT to produce more DDR5 memory. That doesn't mean it would be cheaper, though, or at least no evidence has suggested that so far.

CXMT has remained limited to the Chinese region for now, and breaking through to the Western market would mean impressing a lot of skeptics. Not only would pricing play a big factor, but the reliability of a new DRAM manufacturer would raise serious concerns. Stories like these certainly don't help, but with CXMT's IPO on the way, it's only a matter of time before it becomes a serious mainstream contender.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

- 
I think the real dealbreaker would be the RAM failing quickly instead of lasting decades/indefinitely like you would expect from most RAM. The issues raised could be tolerated (I have never cared about timings), but could suggest higher failure rates are also likely.Reply

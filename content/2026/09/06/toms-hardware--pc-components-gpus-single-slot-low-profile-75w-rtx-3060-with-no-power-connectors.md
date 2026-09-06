---
title: Single-slot low-profile 75W RTX 3060 with no power connectors disappoints in
  tests — GPU runs entirely off the PCIe slot, but offers severely crippled performance
  and frightening thermals
source_url: https://www.tomshardware.com/pc-components/gpus/single-slot-low-profile-75w-rtx-3060-with-no-power-connectors-disappoints-in-tests-gpu-runs-entirely-off-the-pcie-slot-but-offers-severely-crippled-performance-and-frightening-thermals
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-06T15:24:32Z'
published: '2026-09-06T00:00:00Z'
description: 75W might be convenient for very restricted builds, but it drags the
  RTX 3060 performance down into mobile iGPU territory.
image: https://cdn.mos.cms.futurecdn.net/Cw3EjojmcM2CtTBQDSUqRC-1280-80.jpg
---

![A 75W RTX 3060 with no power connectors](https://cdn.mos.cms.futurecdn.net/Cw3EjojmcM2CtTBQDSUqRC.jpg) 

Nvidia launched the GeForce RTX 3060 (12GB) in early 2021 as an affordable mainstream gaming GPU with a 170W TDP, before re-releasing two months ago to offer relief during the ongoing component crisis. Throughout this time, not one person thought that the 3060 consumed too much power... except someone in China who decided to make a 75W version of the card. This blower-style variant has no 6- or 8-pin power connectors and runs entirely off the PCIe slot it'll be connected to, resulting in some expectedly underwhelming performance.

you may wonder why someone would need to set the power limit lower than what nvidia allows. someone in china makes a cableless 3060 that requires no external power connection. an 3060 runs at 170w stock, but it can go as low as 100w.a bilibili channel (WestmereX丶冷月) recently… [https://t.co/Hn9PPrRHRY](https://t.co/Hn9PPrRHRY) pic.twitter.com/pRuuRthwNcSeptember 4, 2026


The RTX 3060 takes very well to undervolting and, therefore, can already be taken all the way down to just 100W at the cost of modestly reduced performance. A single PCIe x16 slot can provide up to 75W of power, so forcing a 3060 down to that number requires a shunt mod. This practice is usually associated with unlocking power limits on a GPU to chase overclocking feats where you decrease resistance, but in this case, you'd be increasing it.

This is a single-slot, low-profile card with a blower-style cooler about the size of a modern smartphone. You get just 1x HDMI and 1x DisplayPort in terms of connectivity. There is no fin stack present either, the PCB lacks a backplate, and the shroud is a thin metal sheet responsible for all the heat dissipation with a rudimentary heatsink in the middle.

A teardown of the GPU on BiliBili shows it's under-equipped from the inside, too. The memory chips have no thermal pads or paste on them. Instead, the metal shroud just touches the core directly to keep the entire thing cool. Remember that there's just one fan at the far end to blow hot air; there is no intake or proper airflow with positive pressure. So far, everything about this card, except its compact size, is looking subpar.

 ![A 75W RTX 3060 with no power connectors](https://cdn.mos.cms.futurecdn.net/EtSK3sLLaPGcwJ4ZWEu89D.png) 


Once we get to testing, any skepticism is validated as the 75W RTX 3060 GPU is barely able to edge past 900 MHz, despite being rated for 1,770 MHz boost clocks. This results in a Time Spy score of just 4,821 points whereas a regular RTX 3060 easily scores upwards of 9,000 points in the same benchmark. Even older budget GPUs like AMD's iconic RX 580 and Nvidia's equally-popular GTX 1060 score more.

 ![A 75W RTX 3060 with no power connectors](https://cdn.mos.cms.futurecdn.net/ZRGX6KPzMHsDqZeqAFdiUC.jpg) 


During the Time Spy run, the GPU hotspot also went past 90 degrees Celsius, proving that the cooler is barely performing if it's struggling to tame even a 75W card. Clearly, this GPU was suffering from severe thermal throttling on top of already having its power budget more than halved. One could make an argument that it's still an Ampere GPU, so it could make sense in low-power, compact systems. But there are now mini PCs with similarly performing or far more potent integrated graphics in 2026.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg) 

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

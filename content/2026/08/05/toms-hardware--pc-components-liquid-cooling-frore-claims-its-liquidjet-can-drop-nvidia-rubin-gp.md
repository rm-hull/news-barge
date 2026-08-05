---
title: Frore claims its LiquidJet can drop Nvidia Rubin GPU temperatures by 10°C —
  can also boost performance by 15% as hyperscalers eye using delidded GPUs in production
  environments
source_url: https://www.tomshardware.com/pc-components/liquid-cooling/frore-claims-its-liquidjet-can-drop-nvidia-rubin-gpu-temperatures-by-10-c-can-also-boost-performance-by-15-percent-as-hyperscalers-eye-using-delidded-gpus-in-production-environments
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-05T14:29:55Z'
published: '2026-08-05T00:00:00Z'
description: The higher the temperature, the higher the leakage power, the lower the
  efficiency.
image: https://cdn.mos.cms.futurecdn.net/bVXRUWhSeXkLtxi35Zp96a-2560-80.jpg
---

![Frore Systems](https://cdn.mos.cms.futurecdn.net/bVXRUWhSeXkLtxi35Zp96a.jpg) 

It is not a secret that proper cooling ensures longevity and enables hardware to demonstrate its full potential. But when it comes to data center AI hardware, proper cooling also means higher sustained performance, which directly translates into money earned by the owner. Frore Systems, a maker of cooling solutions that are made using semiconductor-grade tools, seems to have a perfect idea of how to reduce the temperature of next-generation AI accelerators and increase their performance by 15%.

 ![a snippet from the HBM roadmap article](https://cdn.mos.cms.futurecdn.net/JY32VXJVXoHUR8NRV2Kveb.png) 


Frore Systems last week published a white paper which suggests that improvements to the entire cooling stack — from the GPU packaging and thermal interface materials (TIMs) to coldplates and coolant temperatures — can increase token generation per watt by more than 30%. Meanwhile, one of the company's boldest projections based on an analytical thermal model* is that its LiquidJet coldplate technology alone can lower Nvidia Rubin GPU junction temperatures by up to 12°C, which translates into a 10% to 25% improvement in tokens/Watt, while a 10°C reduction could increase token generation by around 15%.

Indeed, modern AI accelerators, such as the upcoming Nvidia Rubin, can dissipate up to 2,400 W, and their die temperatures can easily hit 95°C or more. But while 95°C is not necessarily a problem for silicon longevity, leakage current certainly is. Leakage current rises exponentially with temperature, approximately doubling for every 10°C increase in maximum junction temperature, which is when transistor switching itself also becomes less efficient. As a consequence, hotter GPUs require higher voltages to sustain clocks, which eventually forces Dynamic Voltage and Frequency Scaling (DVFS) to reduce clocks to remain within thermal limits, which in turn will reduce performance and token generation.

 ![Frore Systems](https://cdn.mos.cms.futurecdn.net/qB8DpvMWbJLFcJDCh42gPK.png) 


This all leads to a simple conclusion: the better the cooling, the higher the performance and token output. Which is generally right. However, cooling is not as simple, as it depends on multiple factors that can be optimized. Furthermore, for AI data centers, cooling itself is no longer a way to preserve CPUs and accelerators from overheating, but really is a way to maximize their performance and token money generation.

Nvidia designs its platforms around Tj(max) temperature; it is one of the fundamental design constraints for the GPU, package, and cooling solution. This works like this:

- Nvidia specifies a maximum allowable junction temperature (Tj,max limit). This is the temperature the silicon must not exceed during normal operation. The exact value is not always public, but Frore uses 95°C for Rubin in its analysis.
- The GPU continuously monitors its junction temperature using tens or hundreds of on-die thermal sensors, yet power management monitors the hottest region.
- DVFS attempts to maximize performance while staying below the thermal and power limits, so if the GPU has thermal headroom, it can sustain higher clocks or lower voltage. If the junction temperature rises, the firmware gradually adjusts voltage and frequency. If necessary, it throttles to prevent exceeding Tj(max).

The problem is that GPUs operate under several simultaneous limits, such as thermal limit (Tj,max), package power limit, current limit, and voltage limit. Usually, power is reached before thermal. Meanwhile, modern cooling systems are designed to prevent silicon from reaching Tj(max). So, even if Nvidia's GPU never reaches Tj(max), lowering the operating junction temperature still improves efficiency because transistor leakage decreases as temperature falls. This is where Frore and its cooling systems come into play.

According to Frore, leakage power approximately doubles for every 10°C increase in junction temperature, while transistor switching power rises by about 2% over the same temperature range, so lowering operating temperatures is beneficial even when the processor is not thermally throttling.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

## Thermal resistance

According to Frore, the maximum GPU junction temperature used by hardware makers is directed by a deceptively simple equation:

Tj(max) = Tinlet + Q × Rtotal

where coolant inlet temperature, GPU power, and total thermal resistance determine how hot the silicon can be. Meanwhile, total thermal resistance depends on three major elements: the GPU package itself, the thermal interface material between the package, and the coldplate design. As each layer adds thermal resistance, it increases die temperature and reduces overall token money generation. That said, thermal resistance is becoming a major problem, according to the paper.

Frore claims that delidding the Rubin package dramatically lowers thermal resistance (while this is obvious, I must add again that the paper is based on an analytical thermal model*). According to the paper, an unlidded Rubin package can reduce junction temperature by as much as 20°C compared to one with an integrated heatspreader (IHS), which potentially improves tokens/Watt by up to 35%. Of course, there are disadvantages, as delidded GPUs have lower mechanical reliability. We will talk about it later on. In any case, there are cloud system providers that explore the use of delidded Rubin GPUs to boost their token money generation despite all the risks, according to Frore.

 ![Frore Systems](https://cdn.mos.cms.futurecdn.net/nzLGTsDqhKKsGBjoDfCwVK.png) 


Frore's own contribution is, of course, its coldplate. Conventional coldplates are typically manufactured using skiving, a machining process that creates long, straight microchannels inside a copper block. Frore instead borrows manufacturing techniques from semiconductor fabrication — etching and bonding — to build intricate three-dimensional copper microstructures that address hotspots on the accelerator's silicon. These unique microstructures cannot be produced using traditional machining, at least not cost-efficiently, according to Frore.

 ![Frore Systems](https://cdn.mos.cms.futurecdn.net/NdQBjsJwuCv2yinuWQauPK.png) 


## Improving efficiency

The LiquidJet design features short microchannels that are etched around hot spots, multiple cooling stages, and flow routing optimized for the GPU's power-density map. According to the company's analysis, this enables a 6°C to 12°C reduction in junction temperature and improves tokens/Watt by 10% to 25% in the case of the Nvidia Rubin GPU*. A roughly 10°C temperature reduction would therefore correspond to about a 15% increase in token generation efficiency, the paper claims.

![Frore Systems](https://cdn.mos.cms.futurecdn.net/fSQJ6EQQweB7uQUsQ9REHK-1053-80.png) 

![Frore Systems](https://cdn.mos.cms.futurecdn.net/STPoaHeKrUKvRubf9ToDEK-1106-80.png) 

![Frore Systems](https://cdn.mos.cms.futurecdn.net/b5MeeewyPVkMtkgCoQv7GK-1200-80.png) 

![Frore Systems](https://cdn.mos.cms.futurecdn.net/fSQJ6EQQweB7uQUsQ9REHK-1053-80.png) 

![Frore Systems](https://cdn.mos.cms.futurecdn.net/STPoaHeKrUKvRubf9ToDEK-1106-80.png) 

![Frore Systems](https://cdn.mos.cms.futurecdn.net/b5MeeewyPVkMtkgCoQv7GK-1280-80.png) 

Frore argues that improved coldplate efficiency changes the economics of facility cooling, which is obviously the most important part of the hyperscalers' consideration. Nvidia designed Rubin to operate with coolant entering at up to 45°C, which enables many AI data centers to rely entirely on 'free' cooling without mechanical chillers. While lowering the inlet temperature can further improve GPU efficiency, doing so only makes economic sense if the energy consumed by the chillers is offset by the resulting increase in money token generation. Meanwhile, because LiquidJet requires a lower coolant flow rate to maintain the same junction temperature, it also reduces the chiller coefficient of performance (COP) required for additional cooling to become worthwhile.

 ![Frore Systems](https://cdn.mos.cms.futurecdn.net/9EwTzGAoosZj2tLiGTKqMK.png) 


In Frore's example, a Rubin GPU equipped with a conventional skived coldplate requires a chiller COP of approximately 6.7 before colder coolant delivers a net efficiency benefit, whereas LiquidJet lowers the break-even COP to around 4.1, which makes mechanical chilling economically attractive across various deployments.

One interesting thing about Frore's analysis is that its LiquidJet is more efficient on Rubin data center GPUs compared to Blackwell data center GPUs* due to the higher transistor density of the former.

Frore's analysis does not stop at exploring the advantages of its own cooling systems, so the company's analytical thermal model extends to other means by which improved cooling and/or lowered thermal resistance can affect temperatures and therefore money token generation.

 ![Frore Systems](https://cdn.mos.cms.futurecdn.net/pXz33FnFpWWjwuSLWcCARK.png) 


One of the most striking claims by Frore concerns Nvidia's upcoming Rubin is that Frore claims that delidding the GPU package — removing the IHS and the graphene TIM placed between the die and the lid — dramatically lowers thermal resistance, which therefore reduces junction temperature by as much as 20°C compared to regular GPUs with IHS, which therefore improves tokens per Watt by up to 35%, according to the model used by Frore.

Meanwhile, mechanical reliability becomes a major concern for delidded GPUs. Without the IHS, the bare Rubin GPU packaged using TSMC's CoWoS-L technology becomes considerably more vulnerable to cracking of bridges that connect the two Rubin dies. In fact, even in the Hopper era, some GPUs literally cracked with certain liquid coolers. Furthermore, maintaining uniform contact pressure across multiple exposed dies is substantially more difficult than in the case of monolithic processors. Nonetheless, there are hyperscalers that are exploring the use of delidded Rubin GPUs to increase their token generation and money output.

Thermal interface materials play an equally important role. By default, Nvidia's Rubin reportedly addresses the thermal penalty of a lidded package by using liquid indium metal TIM with gold-plated contact surfaces. Frore argues that an unlidded package paired with a high-performance phase-change material such as PTM7950 still exhibits lower overall thermal resistance than a lidded package using liquid metal, which turns into as much as a 14°C junction-temperature advantage and up to a 28% increase in money tokens/Watt, according to Frore's model.

## Summary

The key point of Frore's white paper is that cooling has become a key determinant of AI data center profitability, as lower GPU junction temperatures improve token generation efficiency rather than 'just' preventing overheating.

In a white paper based on an analytical thermal model, the company claims that its LiquidJet coldplate can lower Nvidia Rubin junction temperatures by 6°C to 12°C and increase tokens/Watt by 10% to 25%, while a 10°C reduction could boost token generation by about 15%.

In addition, the company argues that more efficient coldplates make mechanical chilling economically viable across a wider range of AI data centers as it lowers the break-even chiller efficiency required to offset cooling power consumption.

Finally, Frore claims that delidding Rubin and optimizing thermal interface materials can reduce thermal resistance further and improve tokens/Watt by up to 35%, albeit at the cost of greater mechanical risk for these accelerators.

*It should be noted that Frore's analysis is based on an analytical thermal model rather than experimental results. The paper builds on the thermal resistance equation (Tj = Tinlet + Q × Rtotal), published or assumed operating parameters for Nvidia's Rubin GPU, and the company's own estimates of how different coldplate designs affect thermal resistance.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

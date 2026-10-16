---
title: China startup demoes prototype EUV light source — 15W of output power and 90%
  domestic components, still years away from viability
source_url: https://www.tomshardware.com/tech-industry/semiconductors/china-startup-demoes-prototype-euv-light-source-15w-of-output-power-and-90-percent-domestic-components-still-years-away-from-viability
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-16T16:37:28Z'
published: '2026-10-16T00:00:00Z'
description: And will not demo one for many years to come.
image: https://cdn.mos.cms.futurecdn.net/JLwxTcuunemSTSeX5zy2bS-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Anton Shilov
- Gigaphoton
- Tom
locations:
- China
- Japan
- Shanghai
organisations:
- 26th China International Industry Fair
- ASML
- ASML/Cymer
- China Langdao Silex
- Cymer
- DPP
- EUV
- FlintMicro-LPP
- Gas Discharge Plasma Laboratory
- Get Tom's Hardware
- Gigaphoton
- Google News
- HVM
- LPP
- Langdao Silex
- Philips Extreme UV
- Tom’s Hardware
- TrendForce
- Tsinghua University
---

![Langdao Silex](https://cdn.mos.cms.futurecdn.net/JLwxTcuunemSTSeX5zy2bS-1920-80.jpg)

Being unable to procure EUV litho tools from ASML, China must develop such systems locally, so from time to time we learn about an EUV-related 'breakthrough' in China that will turn into an actual EUV scanner over the following several years. This week, Chinese startup Langdao Silex demonstrated a prototype extreme ultraviolet (EUV) light source with over 15W of output power, 90% domestic components, and decent uptime. The company will need another three to five years to commercialize its technology, reports TrendForce, citing various sources. Yet, a light source alone does not make an EUV scanner.

![tsmc](https://cdn.mos.cms.futurecdn.net/p2QqhVFP7dTRWfeVBCYBYV-1200-80.jpg)

## An LPP EUV source from China

Langdao Silex, which was established in 2024 by Tsinghua University's Gas Discharge Plasma Laboratory alumni, demonstrated its EUV light source prototype at the 26th China International Industry Fair in Shanghai, for obvious reasons, without lighting it up. Just like modern light sources from ASML, the company's low-power FlintNano LPP-OXXO system uses laser-produced plasma (LPP) technology that produces EUV radiation by bombarding tiny heated metal droplets with high-energy laser pulses to create extremely hot plasma. The system features a 1,000W driving laser (presumably a CO2 one) with an operating frequency of 1 kHz – 20 kHz and conversion efficiency exceeding 2%. Its EUV output exceeds 15W (presumably measured at the plasma rather than at intermediate focus, as the company has not demonstrated a complete EUV collection system) while its brightness reaches 100 W/(mm²·sr). The source has an étendue of 1 × 10⁻³ mm²·sr and generates plasma with a diameter of 60 μm.

![Langdao Silex](https://cdn.mos.cms.futurecdn.net/orngJt5zSqUhUvafimBCQN-1200-80.png)

According to Langdao's specifications, the FlintNano LPP-OXXO can operate continuously for over 100 hours with plasma stability of 3% RMS and EUV output power stability of 5%. These characteristics make the system suitable for semiconductor exposure experiments, although its output remains insufficient for high-volume chip production. Meanwhile, the 'over 100 hours' availability is very impressive for a pre-production light source, though we must admit that there is no way to verify the claim.

Langdao is also developing the FlintMicro-LPP high-power EUV source, which has completed proof-of-principle validation, according to reports. However, Langdao has not disclosed its output power, conversion efficiency, or operating lifetime.

On paper, Langdao's EUV source is comparable in output to some of the earliest EUV sources developed by Western and Japanese equipment makers, albeit with a major caveat: Langdao seems to measure EUV power at the plasma rather than after the collector or at intermediate focus as ASML does. ASML's early EUV demonstration equipment used approximately 10W at intermediate focus DPP sources in 2007, while Cymer's LPP sources installed in early NXE:3100 systems delivered up to 11W during wafer exposure in 2012 (note that ASML's machines are source agnostic, so some NXE:3100 prototypes used DPP sources, while others used LPP sources). By 2013, Cymer demonstrated approximately 40W at intermediate focus over extended operating periods. Meanwhile, Japan's Gigaphoton targeted 25W with its first prototype in 2013 and demonstrated 43W in early 2014. By late 2014, Gigaphoton had achieved 118W during a 10-minute test. However, since these historical figures involve different measurement conditions and operating durations, direct comparisons are vastly inaccurate.

## Not quite there

Langdao Silex has not demonstrated its EUV light source in action, so all we know about it comes from the company itself. As noted, 15W power looks comparable to early EUV sources developed by Philips Extreme UV (DPP) and Cymer (LPP). Meanwhile, early NXE:3400-series machines came with 125W – 150W at intermediate focus sources, which was far from enough for high-volume manufacturing (HVM).

![Langdao Silex](https://cdn.mos.cms.futurecdn.net/LBm5uBtJuKK2D5sVm82MaS-1200-80.jpg)

Modern EUV lithography equipment comes with considerably more powerful sources. ASML introduced 250W-class EUV sources for commercial production in 2018 – 2019 and has since achieved substantially higher output levels. Increasing output requires more powerful CO₂ lasers, highly accurate tin-droplet generators, effective debris mitigation, durable collector mirrors, and considerably better long-term reliability.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Langdao claims that 90% of its prototype's components are domestically sourced and that most critical parts were developed in China. However, the company has not explained whether the localization figure reflects component count, value, or another metric. Furthermore, its representatives reportedly acknowledged that increasing EUV output and improving long-term operational stability are the targets to be achieved in a bid to commercialize the source.

## Not an EUV scanner

Yet, even without complete EUV scanners, Langdao's source could support EUV photoresist development, mask inspection research, development of EUV collection and illumination optics, and eventually experimental exposure testing.

Developing a complete EUV lithography scanner will require further advances in EUV collection and illumination systems, high-precision multilayer mirrors, wafer and reticle stages, overlay accuracy, and system integration. Meanwhile, all of these devices require a separate supply chain that hardly exists in China today.

Therefore, even if Langdao successfully develops its EUV source and increases its output to levels suitable for high-volume manufacturing, this would not necessarily mean that China could manufacture its own EUV lithography machines any time soon. Moreover, while Langdao's progress is impressive, it took ASML/Cymer approximately six years to increase the output of its LPP EUV source from 11W to 125W – 150W at intermediate focus, so there is no way that Langdao's LPP source could be used for anything beyond development tools in the next three to five years.

Meanwhile, Langdao has not disclosed where its reported 15W of EUV output is measured. If this figure represents radiation generated at the plasma rather than power delivered at intermediate focus, the source's usable output would be considerably lower than 15W when measured according to industry-standard practices. That said, it does not look like China got significantly closer to building its own EUV lithography scanners with the current announcement.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV-140-80.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

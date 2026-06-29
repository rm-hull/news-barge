---
title: China’s hollow-core fiber trial pushes 51.3 Tb/s over 128 miles without signal
  regeneration — milestone targets AI-era networking bottlenecks
source_url: https://www.tomshardware.com/networking/chinas-hollow-core-fiber-trial-pushes-51-3-tb-s-over-128-miles-without-signal-regeneration-milestone-targets-ai-era-networking-bottlenecks
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-06-29T11:01:56Z'
published: '2026-06-29T00:00:00Z'
description: China's progress largely sits outside the Western supply chain
image: https://cdn.mos.cms.futurecdn.net/4p6QaCguYKo7wtZbAJmsAC-1920-80.png
---

![A bundle of blue fiber optic cables.](https://cdn.mos.cms.futurecdn.net/4p6QaCguYKo7wtZbAJmsAC.png) 

Chinese firm Yangtze Optical Fiber and Cable Joint Stock Limited Company (YOFC) announced on June 16 that it had successfully completed the world’s first field trial of hollow-core fiber (HCF) wavelength-division multiplexing (WDM) capable of 1.2 Tb/s per wavelength over an ultra-long unrepeatered span. The trial — conducted in collaboration with state-owned China Telecom and optical equipment maker Dekoli — achieved an unprecedented aggregate transmission capacity of 51.3 Tb/s over roughly 128 miles (206.5 km) without signal regeneration.

These figures, which the collaborators describe as a new world record for unrepeatered WDM capacity-distance performance without remote-pumped amplifiers, were achieved using only erbium-doped fiber amplifier amplification. The demonstration was carried out under the framework of the National Key Laboratory for Advanced Manufacturing and Application Technologies of Optical Fibers and Cables.

The success of this trial marks a major leap forward in optical communications. What separates it from earlier HCF results is the combination of capacity, distance, and amplification approach in a live network rather than a lab. China Telecom had previously demonstrated 1.2 Tb/s over a single wavelength, back in July 2024, but only over a 20-kilometer span.

Elsewhere, researchers have pushed unrepeatered HCF spans past 300 kilometers, but at far lower capacities. Pulling 1.2 Tb/s per channel over more than 200 kilometers on a commercial cable, using only conventional erbium-doped fiber amplifiers (EDFAs) rather than the remote-pumped boosters typically needed to extend unrepeatered reach, is the remarkable new achievement YOFC claims.

Hollow-core fiber is a next-generation optical data transmission medium that is rapidly emerging as a leading candidate for high-capacity, low-latency networking. Unlike conventional optical fiber, which guides light through a solid glass (silica) core, HCF guides light through an air-filled channel. This structural difference offers several advantages. Light travels roughly 1.5 times faster through air than through glass, cutting latency. Furthermore, the air core sidesteps some of the nonlinear distortion and dispersion baked into silica. YOFC has previously claimed that its hollow-core fiber technology can deliver 31% lower latency, 47% faster transmission speeds, and near-zero optical nonlinearity compared with conventional solid-core fiber.

In theory, HCF's air core would enable it to carry far more data over far greater distances with fewer amplification points. The trade-off has always been loss. Commercial hollow-core fiber has historically run at higher attenuation than mature silica fiber, limiting how far a signal can travel before it needs a boost. This limitation has been narrowing, with the trial's 200 km-plus unrepeatered span being the latest milestone.

The collaborators achieved this through two main innovations: one at the system level and the other in the amplifier hardware. At the system level, they used a self-developed optimization scheme for per-wavelength rate and channel power allocation. Rather than pushing every wavelength at the same data rate and power, the system adapted each channel to the link conditions, enabling hybrid transmission across multiple data rates, channel spacings, and power levels. The companies say this helped reduce capacity losses caused by gas-absorption peaks inside the hollow core, a quirk specific to guiding light through air rather than glass.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

On the hardware side, the researchers built a high-power amplifier using a cascaded dual-gain-unit architecture and a multi-element doping design, achieving a maximum output of 33.5 dBm (roughly 2.24 W) while maintaining flat gain across the operating band. That higher-power, flatter amplification helped stretch an unrepeatered span without resorting to the remote-pumped amplifiers the team was trying to avoid. Because pushing that much power over a live optical link carries a real risk of failure, the system was wrapped in safeguards, including optical-path power anomaly detection, automatic interlock shutdown, and alarm-linked response mechanisms to catch faults before they damage equipment.

The stakes in this trial, and in HCF more broadly, tie directly to the AI buildout. As hyperscalers race to stand up ever-larger GPU clusters, the network linking those clusters, inside data centers and across the long-haul links between facilities, is fast becoming the bottleneck. HCF's lower latency lets operators site facilities farther from expensive, power-constrained hubs without a speed penalty, while its capacity headroom helps move the enormous traffic AI training and inference generate. The same properties make it attractive for latency-sensitive workloads like financial trading.

That promise is already pulling in serious money, mostly from the West. Microsoft, which moved early via its 2022 Lumenisity acquisition, struck manufacturing deals with Corning and Heraeus in September 2025 to scale production across Azure. AWS has developed its own HCF, claiming a 30% latency improvement over standard fiber, and says it wants more than it can currently get. Corning also has fiber deals with Microsoft, Meta, and Lumen, and is expanding in North Carolina with Nvidia's backing. Trials like YOFC’s are closing existing gaps toward full, widespread HCF deployment, though China's progress largely sits outside the Western supply chain now forming.

  


*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.

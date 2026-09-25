---
title: Nvidia DLSS 5 power draw hits 647W as power connector runs hotter than the
  GPU die, upscales frame rates and flame temps on 16-pin — AI gaming tech pushes
  connector to uncomfortable thermal and power limits
source_url: https://www.tomshardware.com/pc-components/gpus/nvidia-dlss-5-upscales-frame-rates-and-flame-temps-on-16-pin-power-connector-ai-gaming-tech-pushes-connector-to-uncomfortable-thermal-and-power-limits
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-25T13:40:38Z'
published: '2026-09-25T00:00:00Z'
description: Is DLSS 5 playing with fire?
categories:
- Technology & Software
- Hardware
- Video Gaming
image: https://cdn.mos.cms.futurecdn.net/zSDbAK6zJvGgD5vmjfWw3m-2560-80.jpg
locations: []
people:
- Tom
organisations:
- AMD Radeon
- DLSS
- DLSS5
- GPU
- Get Tom's Hardware
- Google News
- HWiNFO
- Nvidia
- PCAT
- PCI-SIG
- QuasarZone
- Reddit
- TDP
- Tom’s Hardware
- Zhiye Liu
---

![Nvidia GeForce RTX 5090 Founders Edition](https://cdn.mos.cms.futurecdn.net/zSDbAK6zJvGgD5vmjfWw3m.jpg)

There is no doubt the GeForce RTX 5090 is one of the best graphics cards and has the full potential to leverage DLSS 5. However, if you plan to hop on the DLSS 5 bandwagon, you may want to keep an eye on your graphics card's temperatures and power consumption. According to tests by Korean outlet QuasarZone, the GeForce RTX 5090 Founders Edition peaked at nearly 650W in power draw, with the highest recorded temperature on the 16-pin (12VHPWR) power connector exceeding 90 degrees Celsius. Notably, that is higher than the standard temperatures measured for the GPU die.

![Asus RTX 5080 Noctua Edition](https://cdn.mos.cms.futurecdn.net/Wh9EZgD8NG9yUioNNgPB3d.png)

While less frequent, user reports of the 16-pin power connector melting are still popping up if you look around the Internet, particularly on Reddit. Even a couple of media outlets have also encountered power connector meltdowns during their use. So, it is not an issue that affects only new users; 16-pin power connector failures extend to seasoned industry veterans, too. There is no prejudice toward Nvidia's Blackwell-powered graphics cards, either. Similar meltdowns have appeared on AMD Radeon graphics cards. Running DLSS 5 may just be adding fuel to the fire, figuratively.

QuasarZone ran *Cyberpunk 2077* in a controlled environment at 27.5 degrees Celsius for 20 minutes. The publication used a 4K (3840x2160) resolution with DLSS Quality and Ultra image settings and monitored the temperature of the 16-pin power connector. The media outlet tested the GeForce RTX 5090 Founders Edition, Asus ROG Astral GeForce RTX 5090, and GeForce RTX 5080 Founders Edition.

## Nvidia DLSS 5 Impact On 16-pin Power Connector Temperatures

| Graphics Card | DLSS 5 Off (Celsius) | DLSS 5 On (Celsius) | Temperature Increase |
| --- | --- | --- | --- |
| GeForce RTX 5090 (Latch Side) | 77.1 | 83.4 | 8% |
| GeForce RTX 5090 (Opposite Side) | 80.9 | 91.7 | 13% |
| GeForce RTX 5080 (Latch Side) | 45.8 | 52.2 | 14% |
| GeForce RTX 5080 (Opposite Side) | 47.6 | 48.6 | 2% |

In the first round of testing using a GeForce RTX 5090 Founders Edition with DLSS 5 disabled, QuasarZone measured 77.1 degrees Celsius on the latch side of the 16-pin power connector and 80.9 degrees Celsius on the opposite side. With DLSS 5 enabled, the temperatures quickly jumped to 83.4 and 91.7 degrees Celsius, respectively.

Before DLSS 5, the average core and peak temperatures for the GeForce RTX 5090 were 79.4 and 82.3 degrees Celsius, respectively. Afterward, they increased to 83 and 86.3 degrees Celsius. As a result, the 16-pin power connector was the hottest spot on the GeForce RTX 5090.

In contrast, the GeForce RTX 5080 Founders Edition ran at significantly lower, more manageable temperatures. Before activating DLSS 5, the temperature on the latch side and opposite the 16-pin power connector registered 45.8 and 47.6 degrees Celsius, respectively. With DLSS 5, the temperatures rose to 52.2 degrees Celsius on the latch side and 48.6 degrees Celsius on the opposite side. The results were not a surprise, since the GeForce RTX 5080 consumes less power than the GeForce RTX 5090.

## Nvidia DLSS 5 Impact On Graphics Card Power Consumption

| Graphics Card | DLSS Off (Watts) | DLSS On (Watts) | Power Draw Increase |
| --- | --- | --- | --- |
| GeForce RTX 5090 | 509.2 | 575.1W | 13% |
| GeForce RTX 5080 | 298.2 | 350.3 | 17% |

Using HWiNFO to measure average power consumption, the GeForce RTX 5090 showed a 13% increase in power draw with DLSS5 enabled. By contrast, the GeForce RTX 5080 showed a 17% increase in average power consumption under the same conditions. Despite these notable increases, both cards seemingly stayed within their official TDP specifications, with the RTX 5090 rated at 575W and the RTX 5080 at 360W.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

HWiNFO uses a software-level API to poll power metrics from the graphics card's telemetry sensors. While it is sufficient for everyday monitoring, nothing is more accurate than measuring power directly from the circuit board. The Nvidia Power Capture Analysis Tool (PCAT) is perfect for that.

| Graphics Card | DLSS Off (Watts) | DLSS On (Watts) | Power Draw Increase |
| --- | --- | --- | --- |
| GeForce RTX 5090 (Peak) | 582.5 | 658.0 | 13% |
| GeForce RTX 5090 (Average) | 527.3 | 593.9 | 13% |
| 16-pin Power Connector | 582.7 | 646.7 | 11% |

QuasarZone found that the GeForce RTX 5090's average and peak power draw increased by 13%, effectively exceeding the graphics card's power limit. The average power consumption readings differed by 3% between HWiNFO and PCAT.

Focusing primarily on the 16-pin power connector, QuasarZone's PCAT measurements showed a 582.7W power draw without DLSS 5 and 646.7W with it on, representing an 11% increase.

While 658W sounds scary, it does not compare to what we have seen on custom GeForce RTX 5090 models. On the GeForce RTX 5090 32G Lightning Z with DLSS 5, we observed the graphics card's power consumption spike to 592W at 1080p, 695W at 1440p, and 848W at 4K.

Using the Asus ROG Astral RTX 5090 as a test subject, QuasarZone recorded the current flowing through each of the six power pins from the 16-pin power connector. Before enabling DLSS 5, the power readings ranged from 6.94A to 7.47A. When activated, the power readings spiked to between 7.83A and 8.51A. While the values remained within PCI-SIG’s requirement of 9.2A per pin, headroom is extremely thin, with just 0.69A between the highest recorded current and the official threshold.

In another simulation, the Korean media outlet explored the consequences of a loose pin or improper connection in the 16-pin power connector. This is the most common scenario that leads to 16-pin power connector meltdowns, due to unbalanced power loading across the connector. With one nonfunctional power pin, the electrical load is redistributed to the remaining pins.

With DLSS 5 off, the highest current registered on a single pin reached 8.9A. This value remains uncomfortably close to PCI-SIG's standard. However, turning on DLSS 5 pushed the power pins to 10.1A, 10% above the specification. The simple test highlights just how easily and quickly things can go wrong.

QuasarZone's alarming test results may look like fuel for fearmongering. However, the publication's tests align closely with our findings that DLSS 5 substantially increases power consumption. At least one user has allegedly reported a 16-pin power connector meltdown while experimenting with DLSS 5.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zhiye Liu](https://cdn.mos.cms.futurecdn.net/HhmwL5w9ggUtLCPfqGjTi4.jpg)

Zhiye Liu is a news editor, memory reviewer, and SSD tester at Tom’s Hardware. Although he loves everything that’s hardware, he has a soft spot for CPUs, GPUs, and RAM.

* * I was testing a couple of games with DLSS 5 and I only had temp monitor going and noticed my temps were a bit higher than usual and concluded the card was working much harder than usual. I also have my card on a profile that voltage limits it to 85percent of max so I figure it would have been even higher without that.Reply

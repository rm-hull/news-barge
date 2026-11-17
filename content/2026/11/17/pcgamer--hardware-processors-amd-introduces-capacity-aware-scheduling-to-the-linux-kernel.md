---
title: AMD introduces Capacity Aware Scheduling to the Linux kernel, suggesting LP
  cores next year
source_url: https://www.pcgamer.com/hardware/processors/amd-introduces-capacity-aware-scheduling-to-the-linux-kernel-which-sure-is-the-thing-id-do-if-i-were-introducing-zen-6-lp-cores-next-year/
source_site: PC Gamer
source_slug: pcgamer
description: Any way that more efficiently uses cores has the thumbs up from me.
image: https://cdn.mos.cms.futurecdn.net/QQoT6dnH3Ysusg7VkJraRk-2560-80.jpg
published: '2026-11-17T00:00:00Z'
scraped_at: '2026-11-17T15:56:35Z'
categories:
- Technology & Software
people:
- Badole
- Zen
locations:
- Panther Lake
organisations:
- AMD LP
- AMD Ryzen
- CAS
- CPU
- Intel
- LPE
- PC Gamer Circuit Breaker
- Vishal Badole
- Zen 6
---

![AMD Ryzen 7 7700X3D CPU](https://cdn.mos.cms.futurecdn.net/QQoT6dnH3Ysusg7VkJraRk-1920-80.jpg)

AMD's Vishal Badole recently posted two Linux kernel patches (via TechPowerUp), and these both pair up to introduce Capacity Aware Scheduling (CAS) for AMD heterogeneous processors. If that sounds like gibberish to you, effectively, this lays the groundwork to more efficiently handle AMD chips that have different core types.

Up until now, AMD's performance scaling driver for Linux (amd-pstate) treated all cores as equal, assigning tasks regardless of core strength. AMD's current heterogeneous design pairs full-fat Zen 5 and lower-caste Zen 5C cores together in Zen 5 chips nowadays, but there is far less actual difference between these two core types than in the P-cores and E-cores of modern Intel architectures.

But Zen 6's full lineup is currently suggested to be quite different. Also shared in a Linux patch earlier this year, Zen 6 is set to introduce a new Low Power core type (which is set to run at a very low power, as you might guess from the name), and that is a core type that would really benefit from Capacity Aware Scheduling.

What AMD has called Performance and Efficiency cores up until now is not the same as what Intel has called Performance and Efficiency cores. AMD's Efficiency cores are effectively just compact versions of the Performance cores, whereas Intel's E and P cores have different microarchitectures and are specifically tailored for different use cases.

The new Zen 6 LP cores appear to be similar to Intel's LPE (Low Power Efficiency) cores you will find in its Panther Lake chips. And as such, the need for CAS makes more sense. If AMD LP cores take after Intel LPE cores, they will be tuned down to run on a very low power limit, so differentiating between cores will allow the system to more efficiently divvy up tasks.

![Photo of an AMD Ryzen 9 9950X3D processor](https://cdn.mos.cms.futurecdn.net/c2rmBHmVaVrxcpCSgyvpoi-1200-80.jpg)

The introduction of CAS isn't just good for the eventual introduction of AMD Zen 6 LP cores (or whatever they will be called when they launch). Badole explained that this change should help even with current heterogeneous processors (Zen 4 and Zen 5). They say, "The scheduler sees every CPU as having identical capacity and treats performance and efficiency cores as interchangeable. Tasks are therefore placed and balanced without regard to core strength, which hurts both throughput and energy efficiency on hybrid systems."

Up until now, the extra efficiency gains from CAS would only be a bonus, but if Zen 6 LP cores are low-power enough, it could be needed for them to operate properly, given what we expect will be a much lower power draw, and therefore much lower performance.

The PC Gamer Circuit Breaker newsletter breaks down the latest PC gaming tech, and finds you the best deals on the best products

![AMD Ryzen 9 9800X3D processor](https://cdn.mos.cms.futurecdn.net/5ryUJb6snbbQMdpHJu7i8W-140-80.jpg)

**1. Best overall:AMD Ryzen 7 9800X3D2. Best budget:AMD Ryzen 5 55003. Best mid-range:Intel Core Ultra 5 250K Plus4. Best high-end:AMD Ryzen 9 9950X3D5. Best AM4 upgrade:AMD Ryzen 7 5700X3D6. Best CPU graphics:AMD Ryzen 7 8700G**

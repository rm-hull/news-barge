---
title: Hotspot temperature sensor on Nvidia's Blackwell gaming GPUs is still accessible
  if you have access to Nvidia's internal MODS tool — Nvidia RTX 5070 Ti caught throttling
  at 107°C over poor TIM application
source_url: https://www.tomshardware.com/pc-components/gpus/hotspot-temperature-sensor-on-nvidias-blackwell-gaming-gpus-is-still-accessible-if-you-have-access-to-nvidias-internal-mods-tool-nvidia-rtx-5070-ti-caught-throttling-at-107-c-over-poor-tim-application
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-11T17:10:53Z'
published: '2026-07-11T00:00:00Z'
description: Changing the application dropped the temperature to 100 degrees Celsius.
image: https://cdn.mos.cms.futurecdn.net/GSB5guPv9JyJQd4axDtzUY-1440-80.jpg
---

![A thermal camera view of the Nintendo Switch 2 in docked mode with a hotspot temperature of 116 °F](https://cdn.mos.cms.futurecdn.net/GSB5guPv9JyJQd4axDtzUY.jpg) 

When the RTX 50 series launched, reviewers quickly discovered that the hotspot temperature was being misreported in standard diagnostics tools such as HWiNFO or MSI Afterburner. Eventually, people realized that Nvidia had outright removed the option to monitor hotspot temps, but it seems like the hardware was never removed from the GPU. New testing by Brazilian repair specialist *Paulo Gomes* has revealed that the sensor is still present and readable with special tools.

In the video, the host shows a Gigabyte variant of the RTX 5070 Ti that was sent to him due to overheating issues. Within Windows, the monitoring tools showed no abnormal signs, as the "average" temperature was reported at 67 to 68 degrees Celsius. However, when diagnosed with a specialized tool called "MODS," the hotspot temperature reached 107 degrees Celsius almost immediately under load.

MODS stands for Modular Diagnostics Software, and it's an internal Nvidia tool used to test GPUs before they hit the shelves or during the RMA process. It's not available to the public and doesn't work on Windows because the OS keeps intercepting calls from the hardware monitoring APIs. You need a Linux distribution that boots directly into a command line, from where MODS (and MATS, for memory testing) can run as intended.

Some repair shops have been known to get access to MODS, such as in this case, which unlocks the hidden hotspot temperature sensor on Blackwell gaming GPUs. Keep in mind that Nvidia ships much more comprehensive diagnostic utilities for its server-grade and workstation GPUs that can actively monitor all aspects of the card. It's unknown why the company decided to keep some sensors locked out of gamers' reach.

![A POLÊMICA da MASSA TÉRMICA nas GIGABYTES! NVIDIA está ESCONDENDO ALGO CRUCIAL do CONSUMIDOR! - YouTube](https://img.youtube.com/vi/iDXwNrqvmjw/maxresdefault.jpg) 

Perhaps we can infer the rationale from last year, when Igor's Lab tested several RTX 50-series GPUs and found a "hotspot issue" affecting all of them. The reason was poor PCB manufacturing — not using heavy-duty materials to build the PCB layers, causing certain parts of the substrate to heat up even when the core was relatively cool. This was exacerbated by Nvidia's own guidelines, which told AIBs to compensate for ideal conditions instead of worst-case scenarios.

Anyhow, as Paulo Gomes and his team discovered, the RTX 5070 Ti's hotspot was hitting 107 degrees Celsius, and the card throttled and dropped its clock speeds right away. Nvidia mandates 107 degrees Celsius as the upper limit for RTX 50-series, so it was clear that the card was slowing down to prevent damage. To inspect what was actually wrong, they opened up the card and found poor thermal contact between the cooler and the componentry.

The TIM (thermal interface material) application was inadequate; the paste had accumulated around the perimeter of the core while the center was mostly dry. The repair personnel removed the old material and replaced it with SnowDog Husky paste, which was enough to drop the hotspot temperatures to 100 degrees Celsius. Now, it was within the safe operating range and no longer thermal throttling under load.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

What would've been a simple fix on the consumer's end was turned into a repair job solely because Nvidia hid the GPU's hotspot temperature, literally misreporting the card's internal condition. Had this RTX 5070 Ti just run at 107 degrees Celsius continuously, the silicon would wear down incredibly fast, and the customer would never even know why. Not to mention some manufacturers' insistence on voiding warranty upon breaking the GPU's "seal," which is an illegal and unenforceable practice in the United States.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

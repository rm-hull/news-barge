---
title: '''Don''t waste your time'': Raspberry Pi expert reveals users are essentially
  unable to swap out RAM chips for repairs or upgrades'
source_url: https://www.techradar.com/pro/dont-waste-your-time-raspberry-pi-expert-reveals-users-are-essentially-unable-to-swap-out-ram-chips-for-repairs-or-upgrades
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-28T22:03:44Z'
published: '2026-09-28T00:00:00Z'
description: Manufacturer locks block that route
image: https://cdn.mos.cms.futurecdn.net/GpZBkNPjhm7uuxGozdEBRN-970-80.jpg
categories:
- Technology & Software
people:
- Phil Elwell
- YouTuber Jeff Geerling
locations:
- GitHub
organisations:
- 2GB
- 4GB
- PhilE
- RAM
- Raspberry Pi
- Raspberry Pi Foundation
- Raspberry Pi Holdings
- TechRadar Pro
---

![Rasprberry Pi](https://cdn.mos.cms.futurecdn.net/GpZBkNPjhm7uuxGozdEBRN-970-80.jpg)

* **Raspberry Pi firmware has refused RAM capacity changes on Pi 5-family boards since at least September 2024, something that was formally confirmed by a company engineer in June 2026**
* **The company states that this is intentional: a lock kills the profit in reselling 2GB boards fitted with untested larger chips as 8GB models, preventing bootlegging with substandard components that causes QC issues**
* **A second Raspberry Pi engineer has stated that same-part repairs still work, and an older bootloader can be flashed onto devices to bypass the check altogether**

Raspberry Pi has spent two years locking its newest boards to the memory capacity they left the factory with to prevent scalpers and bootleggers from hoarding its cheapest, low-memory options for third-party upgrades.

At a time when shortages are dictating supply and pricing for most components with on-board memory, one of Raspberry Pi's engineers has an unusually blunt message for anyone hoping to solder in a bigger chip: "don't waste your time trying - it won't work."

The line comes from Phil Elwell, who posts on Raspberry Pi's official forums as PhilE and is identified as the company's senior principal software engineer, making it essentially an official take on the matter.

## A policy implemented before the RAM apocalypse began

The confirmation given by Elwell builds on the company implementing hardware locks in two different ways: not only are Raspberry Pi models locked to the memory size they ship with, but in certain cases, a same-part repair- essentially a memory swap to replace a faulty module may not work thanks to other protections being enabled on-device.

Elwell replied to a repair technician who tried to upgrade a Compute Module 5 from 2GB to 4GB, first with a spare chip and then with one lifted from a working 4GB donor module. Each time, the system saw only 2GB, even after the technician adjusted the resistor the board uses to signal memory size and tried flash chips carrying older firmware.

The reason given here is one that centers on both the fact that Raspberry Pi paints itself as an entity that buys memory competitively in the market, passing on savings to consumers, while admitting shortfalls during certain windows.

Also, the fact that Raspberry Pi Holdings does not want to become bogged down in both a shortage of lower-memory-configuration options and acting as a support channel for complaints regarding unofficial memory mods, many of which are doomed to fail or act erratically thanks to untested memory being used.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The rationale is hard to argue with from a business perspective, but they could have handled it better. The check shipped in the 2024-09-23 bootloader, published on GitHub on September 25, 2024, and its release notes read: "Minor updates to align with manufacturer test." It makes no mention of memory checks, and the first official confirmation we get comes from a forum nearly 21 months later.

While the lock was in play before the current memory crunch, it complicates matters when replacement units are prohibitively expensive, especially for higher-end (read: high memory) Raspberry Pi SKUs.

YouTuber Jeff Geerling, who covered this, pointed out a workaround: you could flash an older bootloader (v2024.09.10-2712) that doesn't have this memory check. Doing this, however, essentially cuts one's Raspberry Pi off from future firmware upgrades that include a slew of fixes and security patches, something that is a heavy trade-off to make.

The makers could have handled this better, as he puts it: the Raspberry Pi could just void a one-time memory bit, not online how e-fuses work in modern electronics and consoles that would be written to the moment the Pi detected a 3rd party module.

Ironically, the memory shortage has exacerbated the situation, making it likely that even more people would attempt to find a cheaper way to get a memory upgrade, even as the Raspberry Pi Foundation passes on memory costs to end-users, making for an extremely lucrative business had the lock not existed, which would potentially render thousands of complaints on their forums by users attempting such a mod or having been duped into buying a unit with modified memory from the get-go.

Whether a silent firmware change, confirmed 21 months later in a forum reply, was the right approach for a company whose brand was built on tinkering is a story for another day, however.

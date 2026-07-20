---
title: New plugin unlocks granular VRAM temperature tracking on Nvidia RTX 50-series
  GPUs — community cracks open Blackwell's forbidden telemetry sensors
source_url: https://www.tomshardware.com/pc-components/gpus/new-plugin-unlocks-granular-vram-temperature-tracking-on-nvidia-rtx-50-series-gpus-community-cracks-open-blackwells-forbidden-telemetry-sensors
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-20T18:14:12Z'
published: '2026-07-20T00:00:00Z'
description: No more thermal blind spots on Blackwell cards
image: https://cdn.mos.cms.futurecdn.net/4cAm78WQJjTMLP3mhFEZ45-2560-80.jpg
---

![GeForce RTX 5090](https://cdn.mos.cms.futurecdn.net/4cAm78WQJjTMLP3mhFEZ45.jpg) 

It is now possible to monitor every thermal aspect of Nvidia’s GeForce RTX 50-series (codenamed Blackwell) products, renowned for being some of the best graphics cards you can buy. Thanks to the efforts of Overclock.net (OCN) member asder00, users can now monitor the temperatures for each memory module on Blackwell graphics cards in addition to the recently exposed hotspot sensor.

 ![Asus RTX 5080 Noctua Edition](https://cdn.mos.cms.futurecdn.net/Wh9EZgD8NG9yUioNNgPB3d.png) 


Nvidia grants direct access to the company's graphics cards and drivers through Nvidia API (NVAPI). Game and software developers employ NVAPI for a range of advanced features. Developers of monitoring tools, specifically, leverage NVAPI to retrieve real-time thermal sensor data so users can keep a close eye on their graphics card's conditions.

While there is a world of information through NVAPI, there are certain sensor readings that Nvidia intentionally kept hidden from developers. Yet, Nvidia's safeguards have not stopped resourceful enthusiasts from discovering creative workarounds to tap into the previously inaccessible sensors. Skilled modders recently managed to gain access to the hotspot sensor, which was only available on internal Nvidia tools like MODS, and now collaboration within the community has enabled individual memory module monitoring.

The new plugin, aptly named Hotspot.dll, is specifically for MSI Afterburner. It exists because MSI Afterburner is software from MSI, an Nvidia partner, so it cannot legally poll sensor data not officially made available through NVAPI. Nevertheless, third-party software solutions such as AIDA64 and HWiNFO are not bound by the same partner agreements and will likely add the functionality for individual memory module monitoring the same way they previously adopted support for the hotspot sensor. The latest beta version (v8.51-6304) of HWiNFO already has the function and had no issues reporting the temperature of all 16 of the GDDR7 memory modules inside our GeForce RTX 5090.

 ![GeForce RTX 5090 VRAM temperatures](https://cdn.mos.cms.futurecdn.net/oauCFaZkkrfpiJzWNxs3tG.png) 


While asder00 developed the plugin, it is important to highlight that it is part of a collective effort. The list of contributors to the breakthrough includes Alexey “Unwinder” Nicolaychuk, the developer behind MSI Afterburner; olealgoritme, known for his work on the open-source Linux GDDR6/GDDR6X temperature reader; Brazilian hardware modder Paulo Gomes; and Martin “Mumak” Malík, the creator of HWiNFO.

The Hotspot.dll plugin reveals the GPU hotspot temperature, die thermal channel readings, average die temperature, GPU memory junction temperature, and per-chip DRAM thermal data. It is compatible with GDDR6, GDDR6X, and GDDR7 memory modules, so it works with the entire Blackwell product stack from the GeForce RTX 5050 to the GeForce RTX 5090. While the original focus of the development was Blackwell, it should work on previous generations of GeForce RTX graphics cards, including the GeForce RTX 40 (codenamed Ada Lovelace) and GeForce RTX 30 (codenamed Ampere) series.

Access to these new sensor readings opens a new level of transparency and control for Nvidia graphics card owners. They will be very beneficial for those who want to fine-tune their graphics card to maximize performance or those who are diagnosing problems.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zhiye Liu](https://cdn.mos.cms.futurecdn.net/HhmwL5w9ggUtLCPfqGjTi4.jpg)

Zhiye Liu is a news editor, memory reviewer, and SSD tester at Tom’s Hardware. Although he loves everything that’s hardware, he has a soft spot for CPUs, GPUs, and RAM.

---
title: Now that's one way to block annoying online ads — developer uses a $5 dongle
  to squeeze in 537,000 domains into just 4MB of flash memory
source_url: https://www.techradar.com/pro/now-thats-one-way-to-block-annoying-online-ads-developer-uses-a-usd5-dongle-to-squeeze-in-537-000-domains-into-just-4mb-of-flash-memory
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-23T03:39:16Z'
published: '2026-07-22T00:00:00Z'
description: $5 dongle blocks ads with amazing efficiency
image: https://cdn.mos.cms.futurecdn.net/PNsruWPMvFbCGhenSDhZyE-1200-80.jpg
---

![A USB adblocking dongle](https://cdn.mos.cms.futurecdn.net/PNsruWPMvFbCGhenSDhZyE.jpg) 

- **Egyptian developer demonstrates how to block ads with an ESP32-C3 "SuperMini" board**
- **ESP32 ad-blocking dongle costs just $5 to build**
- **537,000 blacklisted domains are stored in the device’s 4MB of flash memory**

When online ads become a problem, ad-blocking software is a good idea, used in conjunction with dedicated hardware like a Raspberry Pi running Pi-Hole. But what if the device is rebooting or otherwise out of action? Egyptian developer ZedAxis claims to have developed a solution that might inspire a rethink on how online whitelisting and blacklisting is processed.

Relying on a sub-$5 ESP32-based mini board, the device somehow squeezes over 500,000 domains into paltry 4MB of onboard flash storage.

The build has been demonstrated on YouTube, with the video of the “DNS sinkhole” apparently providing how simple it is to set up. All the hard work has been done by ZedAxis, with the code available via GitHub.

## What is an ESP32-C3?

ZedAxis has built the compact Pi-Hole substitute from a $5 ESP32-C3 “SuperMini” board, easily available from online stores (currently £3.50 on the UK Amazon). These devices feature USB-C for power, Bluetooth 5.0, and crucially for a project like this, Wi-Fi.

The board has been paired with a USB adapter and a 3D-printed case to enable it to be plugged into a power source – in this case, the back of a router, but it could be a TV, console, or any other always-on device with an unused USB port. Direct access to the device is available through a web dashboard, it supports mDNS for easy discovery, and can download over-the-air (OTA) updates.

Code for the project is available on the developer’s GitHub, where the unusual compression that shrinks over 500,000 domains into 4MB of flash storage is explained.

## Isn’t that a lot of domains for 4MB?

![I built a $2 ad-blocker for my whole network - YouTube](https://img.youtube.com/vi/RaxszOUMi8E/maxresdefault.jpg) 

Strictly speaking, 4MB should not be able to hold 500,000 domains. As described on the project’s GitHub, the actual figure is around half that (141,000 taking up “~2.5 MB of RAM”). So how are the 537,000 domains squeezed into 4MB of RAM?

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The board chosen is specifically free of PSRAM (so it just has the flash) and rather than 32-bit or 64-bit, hashes the domains into 40-bit FNV-1a, an algorithm designed for speed and low-collision rates. So, 141,000 domains can be squeezed into 0.7MB of flash, with under 50 KB of RAM apportioned for matching the blacklisted ad domains.

In most cases, the blacklist is limited to around 250,000 domains as OTA firmware updates need around 1.3MB of the flash. But this can be determined when the device is set up and the first blacklist pull is made. Other features are set to be added to this project, including set up as a DHCP server.

The big question is, could this be adopted by, say, small businesses looking for a reduction in broadband bandwidth being eaten by ad networks?

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Christian Cawley](https://cdn.mos.cms.futurecdn.net/zBDYnjPnB2XPvhKbYX9Kuc.png)

Christian Cawley has extensive experience as a writer and editor in consumer electronics, IT and entertainment media. He has contributed to TechRadar since 2017 and has been published in Computer Weekly, Linux Format, ComputerActive, and other publications.

He currently heads up the team at smart home website Matter Alpha, and writes about retro gaming at Gaming Retro.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

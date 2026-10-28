---
title: Amnezia launches 'Amnezia Pulse' — a live map that tracks internet shutdowns
  as they happen
source_url: https://www.techradar.com/vpn/vpn-services/amnezia-launches-amnezia-pulse-a-live-map-that-tracks-internet-shutdowns-as-they-happen
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-28T19:24:53Z'
published: '2026-10-28T00:00:00Z'
description: The VPN provider's public dashboard uses anonymized connection data to
  flag outages and "whitelist" restrictions in Russia and beyond
image: https://cdn.mos.cms.futurecdn.net/Z8cccYZxkX5QXvAauhJhAn-837-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Amnezia
- Maria Xynou
- Pulse
- Roskomnadzor
locations:
- Africa
- Amnezia
- Gabon
- Krasnodar Krai
- Latin America
- Russia
organisations:
- Amnezia Pulse
- Amnezia VPN
- Beeline
- Dom.ru
- MTS
- MegaFon
- Newsweek
- OONI
- Rostelecom
---

![Amnezia VPN logo on black background](https://cdn.mos.cms.futurecdn.net/Z8cccYZxkX5QXvAauhJhAn-837-80.jpg)

* **Amnezia VPN has opened up Amnezia Pulse, its in-house tool for tracking internet shutdowns, to the public.**
* **The map uses anonymized data from Amnezia's VPN servers to flag outages by region and provider.**
* **Russia is the main focus for now, but the team is already spotting disruptions further afield.**

Censorship-resistant provider Amnezia VPN has launched Amnezia Pulse, a public map that tracks internet outages, slowdowns, and "whitelist" restrictions as they happen.

The tool began life as an internal project, powering the company's monthly digests on Russian internet blocking. Now, anyone can check the live map to see which regions are having problems.

That's a big deal in a country where even the best VPN can struggle to stay connected. Russian authorities have spent well over a year cutting mobile internet across entire regions, often letting only a government-approved list of services load.

## What is Amnezia Pulse?

Amnezia Pulse maps disruptions on both mobile and home networks, and is updated daily. In Russia, it monitors the four most popular mobile operators (MTS, MegaFon, Beeline, and T2) alongside home broadband providers Rostelecom and Dom.ru.

Each region is color-coded by severity. Green means no disruptions, yellow signals problems, and red marks a serious outage. Clicking a region opens an hour-by-hour graph of the incident.

The tool is already making headlines. Newsweek reports that Amnezia Pulse logged 80 incidents across 36 Russian regions between September 15 and October 20, 2026, with Krasnodar Krai hit hardest.

Amnezia also told the outlet it has begun seeing synchronized shutdowns hitting several regions or operators at once.

## How does it work?

Rather than relying on user reports, Pulse reads the traffic passing through Amnezia's own VPN servers, each of which counts incoming and outgoing data and the number of active connections.

The system builds a 14-day baseline of "normal" activity for each region and operator, split into five-minute intervals. It flags an incident when several warning signs coincide, such as a drop lasting over an hour, multiple operators going quiet together, or several regions being hit at the same time.

Amnezia says the data is anonymized. It doesn't collect IP addresses and only processes the region, provider, and connection speed.

Coverage isn't limited to Russia, either. Amnezia has spotted traffic anomalies in Gabon linked to long-running social media restrictions, and plans to expand into Africa and Latin America.

## Who benefits?

For everyday users, Pulse answers a simple question: is the problem on my end, or has the internet been cut? That could save time otherwise spent restarting routers or cycling through VPN apps.

Researchers and rights groups stand to gain even more. Amnezia plans to launch an open API for researchers, human rights organizations, and technical experts.

Maria Xynou of the censorship measurement project OONI called the tool "a valuable resource for both the Russian and global internet freedom communities."

There is a catch, though. Pulse's accuracy depends on how many Amnezia Free and Premium users are connected in a given region.

The project has also faced pushback, with Amnezia telling Newsweek it was forced to pause the tool earlier this year following what it described as an attack by Roskomnadzor. The provider has since reinforced its apps against blocking and says it will keep improving Pulse's accuracy and reach.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

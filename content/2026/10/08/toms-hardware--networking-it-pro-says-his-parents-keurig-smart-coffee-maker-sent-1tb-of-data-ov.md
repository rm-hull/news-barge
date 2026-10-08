---
title: IT pro says his parents’ Keurig smart coffee maker sent 1 terabyte of data
  over their Wi-Fi in 10 days — it saturated an access point on its own, but he says
  most of the traffic never left the home network
source_url: https://www.tomshardware.com/networking/it-pro-says-his-parents-keurig-smart-coffee-maker-sent-1tb-of-data-over-their-wi-fi-in-10-days-it-saturated-an-access-point-on-its-own-but-he-says-most-of-the-traffic-never-left-the-home-network
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-08T10:34:19Z'
published: '2026-10-08T00:00:00Z'
description: Turning it off and on again seems to have fixed the problem, but its
  data was not captured.
image: https://cdn.mos.cms.futurecdn.net/JU4ckMUbpELhGbFejDxXia-1152-80.png
categories:
- Technology & Software
- Hardware
people:
- Nomad
locations:
- Jabil
organisations:
- 1TB
- Alexa
- Boston Globe
- BrewID
- Get Tom's Hardware
- Google Home
- Google News
- IT
- Jabil
- Keurig
- LG
- MAC
- Microsoft
- Nexus
- NomadsGalaxy
- Nypro
- Prusa
- Shane Downing
- Tom’s Hardware
- UniFi
- VLAN
---

![Black Keurig K-Supreme SMART coffee maker brewing into a red mug](https://cdn.mos.cms.futurecdn.net/JU4ckMUbpELhGbFejDxXia-1152-80.png)

A Keurig smart coffee maker owned by a self-described IT pro’s parents sent 1TB over their Wi-Fi in 10 days, saturating an access point on its own, user @NomadsGalaxy said in an X post. Nomad added that most of the traffic “didn’t escape my network” but it’s unclear what data it was trying to send, even though there was a temptation “to scan it’s [sic] packets with Wireshark and other tools.”

> Hey uh, @Keurig - what the hell is a COFFEE MACHINE uploading, let me double check... ONE FUCKING TERABYTE OF DATA IN 10 DAYS!?!? Immediately unplugging that. Getting my parents a new coffee machine. [https://t.co/tTHMYC7hNDOctober](https://t.co/tTHMYC7hNDOctober) 6, 2026

Nomad, a Technical Field & Community Specialist at 3D printer maker Prusa with more than 10 years of IT experience, tagged @Keurig and uploaded a UniFi screenshot, asking what the coffee machine could possibly be uploading. The issue was detected after his parents asked why their network was so slow. He said that he would be unplugging his dad’s machine and getting his parents a new one.

The screenshot names the device starting as “Keurig” on his “Appliance network” with traffic indicated at 9.94GB down and 1,008.45GB up, over the connection of 10 days, 9 hours. It was apparently disconnected the evening of Oct. 5, and he later suspected it was a bug. The amount of data indicated by the screenshot’s numbers suggests an average upstream of about 9 Mbps, which could swamp an access point. This comes out to about 97GB a day, about 27 times the amount of the LG washer’s 3.6GB a day reported in 2024.

The model in question, as linked in a reply, is the K-Supreme SMART with BrewID, according to its product page and Use and Care Guide. This guide details app control for remote brew, remote on and off, and scheduled brews. It also covers Alexa and Google Home voice control. BrewID recognizes Keurig-made pods over Wi-Fi, perhaps fueling his speculation that “it’s just DRM waiting to be enabled,” and applies the roaster’s recommended settings. On this model, it works over 2.4GHz Wi-Fi, presumably for range and compatibility, which does limit its maximum bandwidth.

Later in the X thread, Nomad acknowledged that the UniFi had not reported an actual 1TB upload, so he concluded it was mostly local junk data. The coffee maker was already on a separate IoT network with his parents’ smart devices, but not much was blocked. Rebooting the device and placing it in a segregated VLAN solved the issue, at least temporarily. He did not make any attempts at packet capture, opting to keep it safely offline rather than running captures. He recommended that Keurig fix the potential flaw in the device’s network stack to prevent such issues in the future.

According to the pykeurig GitHub project, which allows Home Assistant integration, information sent to the cloud includes power state, brew state, pod recognition result, and the software version. Keurig’s own open-source notice lists Microsoft’s Azure RTOS, an off-the-shelf operating system and networking stack for IoT. The type of data sent is small, so 1TB does read as a malfunction, but the proprietary firmware isn’t public.

The X screenshot also shows the radio’s MAC address with the block registered to Jabil on Feb. 18, 2021. Jabil’s site lists Wi-Fi and Bluetooth expertise, RF and antenna design, IoT embedded modules, and connected appliances among its capabilities. Keurig has previously listed Nypro, a Jabil subsidiary, as a partner. This does not confirm the origin of the hardware or how the firmware works.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

SMART brewers keep 14 days of brew history and sync it once connected, with brews of Keurig-made pods earning points, according to the Keurig Perks FAQ. The *Boston Globe* reported in 2022 that Keurig shared brewing data with the brands that sell K-Cups, with plans for more personalized marketing.

The event comes at a time when users and privacy advocates are already upset with clandestine data gathering by IoT devices, with LG being a particular focal point in recent years. Last month, Gamers Nexus and security researchers used packet captures and firmware analysis on certain LG TVs.

LG told *Tom’s Hardware* its TVs don’t record conversations unless voice features are turned on, though in standby they listen for a wake word if that feature is enabled. It confirmed the local network scans, adding, “This is a standard function commonly provided by smart TVs and smart home devices.” In that case, actual traffic was captured, and that was part of an intended feature rather than an apparent malfunction.

Currently, no comment from Keurig stands on record for the incident. While the brewer does work without Wi-Fi, many of its marketed features rely on internet access, making the potential flaw a real issue for owners. Nomad and his family are likely revisiting their own smart-device rules. He has said other units could be affected, so more users may encounter the same behavior. That may spur Keurig into offering an official statement or a fix. Either way, the event is a reminder that IoT devices and their manufacturers need to take extra care.



*Follow* * Tom’s Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

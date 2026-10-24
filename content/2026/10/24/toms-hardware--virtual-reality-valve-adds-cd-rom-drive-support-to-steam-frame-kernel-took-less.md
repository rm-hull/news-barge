---
title: Valve adds CD-ROM drive support to Steam Frame kernel, took less than ten minutes
  — update comes one day after user requests for capability in the Steam Community
  forum
source_url: https://www.tomshardware.com/virtual-reality/valve-adds-cd-rom-drive-support-to-steam-frame-kernel-took-less-than-ten-minutes-update-comes-one-day-after-user-requests-for-capability-in-the-steam-community-forum
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-24T15:52:58Z'
published: '2026-10-24T00:00:00Z'
description: This is why gamers love Valve so much.
image: https://cdn.mos.cms.futurecdn.net/GREi4LEjsga68aPho9Xe6B-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Aiodensghost
- Jowi Morales
- Tom
- Valve
locations:
- SteamOS ARM
organisations:
- Aiodensghost
- Google News
- Jowi Morales
- Steam Frame
- Valve
---

![Valve Steam Frame](https://cdn.mos.cms.futurecdn.net/GREi4LEjsga68aPho9Xe6B-1920-80.jpg)

A Steam Frame user asked for the ability to use an external optical drive with their headset, and Valve added the feature a day after one of its developers saw the post. Aiodensghost wrote the post in the Steam Frame General Discussions forum, saying that they wanted to watch a movie on the road and install abandonware from 2006 on their device, with Valve developer gaberowe responding a day after.

“I wanted to use my Steam Frame to be able to watch a movie on the road and thought it was no big deal to use the detachable disc drive I had on my computer,” Aiodensghost said on Oct. 18. “Turns out that the Frame cannot power the player and even if it could, it lacks the drivers to read a disc. Valve, this not only killed my ability to watch a movie, [but it also] killed my ability to install my abandonware from 2006. You don’t sell NFS Carbon anymore, and while I have the disc, the Frame isn’t able to read it.” Just a day later, gaberowe responded with, “We will look into this. Thanks for alerting us.”

The Valve developer then proceeded to add the feature in under 10 minutes, pushing commit b68e4a1 to the deckard-linux-no-oopsies GitHub repository, which is described as “the Linux kernel sources used in SteamOS ARM for the Steam Frame.” While this does not automatically mean that the Steam Frame will get optical drive support in the next update, this development shows that Valve developers take gamers’ requests seriously.

More enterprising users who can’t wait for the feature could also build and install the modified kernel themselves instead of waiting for the official software update. Adding CD-ROM drive support to the Steam Frame is a relatively simple exercise, though, as the commit only enabled a pre-existing Linux kernel feature instead of building an entirely new feature from scratch.

While the Steam Frame is primarily designed as a streaming device, it can also be used for standalone gaming. So, by enabling external CD-ROM drive support, users could let their headset directly read their CDs instead of needing another device to stream the contents of the disc from. It might look awkward, though, if you don’t have a long-enough cable, and you’ll have to hold your external optical drive on your head.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK-140-80.jpg)

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.

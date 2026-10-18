---
title: 'Can you get Blu-ray Dolby Atmos TrueHD sound on an Apple TV 4K? Someone''s
  used a wildly elaborate system to show that the answer is: sort of!'
source_url: https://www.techradar.com/televisions/streaming-devices/someone-got-blu-ray-quality-dolby-atmos-truehd-lossless-sound-working-on-the-apple-tv-4k
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-18T04:23:11Z'
published: '2026-10-18T00:00:00Z'
description: The Nuvio media client can deliver really impressive Blu-ray audio, but
  keeping things open source requires a bit of effort
image: https://cdn.mos.cms.futurecdn.net/UDsQLCikubZL5mvWZQ8auG-2000-80.jpg
categories:
- Technology & Software
- Music
- Film & TV
people:
- Agathorpt
locations: []
organisations:
- 48kHz TrueHD Atmos
- APAC
- Agathorpt
- Apple TV
- Native Player
- Reddit
- Superuser404notfound
- TrueHD Atmos
---

![The Apple TV 4K 2022 with its remote on a grey background](https://cdn.mos.cms.futurecdn.net/UDsQLCikubZL5mvWZQ8auG-1920-80.jpg)

* **For now you need to build the feature yourself on a Mac**
* **Native Player delivers similar audio but isn't open source**
* **Proposed as an extension to the Nuvio media player**

A clever developer has come up with a way to deliver lossless Dolby TrueHD movie soundtracks, complete with Dolby Atmos effects, to home theater speakers from the third-gen Apple TV 4K.

The Apple TV only officially supports Dolby Digital Plus, which is the more compressed Dolby audio codec used by streaming services to reduce the amount of data used, while Dolby TrueHD is used on Blu-rays where bandwidth isn't a problem. So it makes sense for the Apple TV 4K to only use Dolby Digital Plus, since it's a streaming device — but that doesn't stop the enthusiasts from wanting the flexibility of playing files with TrueHD audio on their devices.

The system that Reddit user Agathorpt used to deliver Dolby TrueHD through the Apple TV 4K requires not actually delivering it in TrueHD at all, but converting it to other formats, converting the Dolby Atmos positional data into other formats too, then recombining them in a format that the Apple TV 4K *can* deliver, but in a higher quality.

## How they got TrueHD Atmos on the Apple TV 4K

As mentioned above, the audio takes a bit of a journey here. The path is:

**TrueHD Atmos → decoded audio + timed object metadata → fixed 9.1.6 speaker render → APAC → native tvOS playback.**

APAC is Apple's Positional Audio Codec, and while it's not truly lossless (the source audio, TrueHD, is a lossless format but APAC is not) the consensus is that the results here are really impressive.

Basically, the system decodes the audio and the 3D Atmos positioning data separately, creates a new audio system where the Atmos effects are mapped to a 9.1.6-channel speaker configuration, then converts *that* to Apple's own proprietary spatial audio codec, which can then be played by the Apple TV 4K.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

The goal was to replicate the audio functionality of a closed-source app called Native Player with an open-source alternative because "keeping the implementation closed… leaves everyone dependent on that vendor for fixes and future support," Agathorpt says. "Other players can't reuse or improve that code, and the community can't independently inspect how it handles the audio."

![Apps such as Native Player support TrueHD Atmos but they aren&#039;t open source](https://cdn.mos.cms.futurecdn.net/Cou6NJKuMzEyKsPsLEKGfK-966-80.png)

"The spatial audio has been working amazingly well for me," Agathorpt says. "It sounds excellent on my setup." Other redditors have tried the same software and are reporting great results too.

In order to copy what Agathorpt has created, you'd need several things: a Mac; Apple's Xcode development software; and your own Apple development account to sign an app: the full steps they went through are detailed here. The Apple TV 4K needs to be running tvOS 26 or later, and of course you'll also need movie files with 48kHz TrueHD Atmos audio.

There is hope from home theater enthusiasts that Agathorpt's project will be implemented in the Nuvio player for everyone and in other tvOS apps too, but for now you'll need to build it yourself. It doesn't seem too difficult to do, but if you're not the technical type you might want to wait for it to roll out as part of the app. It's been proposed for addition so hopefully that won't take too long.

Agathorpt is at pains to point out that they didn't write the software projects used in this process. It builds on the work of others, especially Superuser404notfound's work on the AetherEngine media engine and LibTrueHD object audio decoder.

One assumes that this will work with the new Apple TV 4K (2026) that Apple just announced too, though its price hike and lack of big new AV features means fans aren't particularly enamored.

## Thinking of buying a new TV?

*Try our TV size and model finder! You tell it how far you sit from your TV, we'll tell you what size to buy based on viewing angle advice from image quality experts, and we'll recommend our three top TVs at that size for different prices.*

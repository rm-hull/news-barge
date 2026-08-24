---
title: Nintendo takes down over 400 GitHub repositories for Switch emulators in one
  go — Relentless DMCA strikes tied to piracy concerns over illegal cryptographic
  keys
source_url: https://www.tomshardware.com/video-games/nintendo/nintendo-takes-down-over-400-github-repositories-for-switch-emulators-in-one-go-relentless-dmca-strikes-tied-to-piracy-concerns-over-illegal-cryptographic-keys
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-24T11:48:50Z'
published: '2026-08-24T00:00:00Z'
description: Fork found in kitchen.
image: https://cdn.mos.cms.futurecdn.net/kW5bsKx4FR5T3m3PeYqGDL-1920-80.png
---

![Nintendo](https://cdn.mos.cms.futurecdn.net/kW5bsKx4FR5T3m3PeYqGDL.png) 

Nintendo has just issued DMCA takedowns against seven GitHub repositories hosting Switch emulation code, leading to 401 affected repos being removed from the platform. Most of these belonged to a single parent repo of the Suyu emulator, which itself is a fork of the previously shut down Yuzu emulator. Nintendo leveraged GitHub policies to their fullest extent to execute its notice, arguing that emulators inherently rely on circumventing anti-piracy protections built into Switch games.

TorrentFreak reports that this was a coordinated campaign by Nintendo as it filed seven different strikes on the same day. GitHub has a rule that says if a parent repo contains more than 100 forks, then the platform will not look at each one individually but rather remove the entire network. Suyu had 311 of these repos under its parent, so all of them were wiped off the map. Suyu was born in 2024, picking up after Yuzu following a lawsuit against its creators, Tropic Haze, that ended in a settlement.

 ![Nintendo's DMCA takedown for Suyu](https://cdn.mos.cms.futurecdn.net/ze6xGNWYsF96zXxdbj8mTS.png) 


Besides Suyu, the Android-based Skyline emulator was also affected in this campaign, but it has already been defunct for the past three years. It's not based on Yuzu, so it stands out in this lineup. Skyline devs actually stopped development in 2023, fearing legal repercussions, so the source code has remained dormant, but it did have 29 independent forks under the parent repo. Since it's an open-source project, anyone can iterate on it and publish their own versions.

Similarly, Yuzu Android, another fork of Yuzu was also struck with a DMCA notice that took down 8 forks under it. NicholasArvani's Yuzu fork had a network of 14 repos that were removed. A repo focusing on an early access build of Yuzu with 21 forks was taken down as well. Finally, MonoNX and its 17 forks, along with the parent repo of the main Yuzu emulator, were hit by Nintendo, too. These repos now link to the seven DMCA notices Nintendo sent to them, as visible in the sidebar, while their forks may return a 404 error.

 ![Nintendo's DMCA against seven GitHub repos hosting Switch emulation code](https://cdn.mos.cms.futurecdn.net/mUHMcUCR3UWpVMFu8cXAH6.png) 


The reasoning for the takedown is tied to piracy, with the company saying these emulators "illegally circumvent Nintendo's TPM in order to run illegal copies of Nintendo Switch games." Switch games require cryptographic keys upon every boot to verify the authenticity of the title, and emulators rely on a ripped-off *prod.keys* file to bypass this failsafe at runtime. Nintendo argues that, therefore, these keys are used to play pirated games instead of legally acquired ones.

The company lists two previous court cases as justification. The first one is its settlement with Tropic Haze — the devs behind Yuzu — and the second one is a default judgment against streamer EveryGameGuru who streamed pirated copies of Switch games ahead of their release using emulators. According to Nintendo, both convictions prove that merely providing the tools that lead to piracy also constitutes illegal trafficking since they rely on circumventing the company's TPM.

Keep in mind that neither case actually set a legal precedent because they weren't contested rulings where a judge interpreted the law; there was no verdict. Tropic Haze decided to settle, and EveryGameGuru failed to appear in front of a court entirely, granting Nintendo a victory by forfeiture. Still, the outcome of either case sets a strong legal blueprint on which the Japanese game company stands today as it tries to warp the legal precedent surrounding emulation as a whole.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

- 
ReplyBesides Suyu, the Android-based Skyline emulator was also affected in this campaign, but it has already been defunct for the past three years. It's not based on Yuzu, so it stands out in this lineup. Skyline devs actually stopped development in 2023, fearing legal repercussions, so the source code has remained dormant, but it did have 29 independent forks under the parent repo. Since it's an open-source project, anyone can iterate on it and publish their own versions. So I guess the protestations on the previous story that Nintendo is only targeting "illegal" stuff may not be entirely accurate.

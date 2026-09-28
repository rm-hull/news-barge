---
title: You can now play Nintendo Switch games on a jailbroken PS5 — early alpha hits
  40 FPS in lighter titles but chokes on Zelda
source_url: https://www.tomshardware.com/video-games/console-gaming/you-can-now-play-nintendo-switch-games-on-a-jailbroken-ps5-early-alpha-hits-40-fps-in-lighter-titles-but-chokes-on-zelda
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-28T21:07:24Z'
published: '2026-09-28T00:00:00Z'
description: Some games perform better than others, but the fact that it works at
  all isn't to be sniffed at.
image: https://cdn.mos.cms.futurecdn.net/BN3XX6fDoAKNMba69AC2gb-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Oliver Haslam
- Tom
locations:
- GitHub
organisations:
- DualSense
- Get Tom's Hardware
- GitHub
- Google News
- Nintendo Switch
- Oliver Haslam
- PS5
- PlayStations
- ProsperoEden
- Sony
- VideoCardz
- Vulkan
---

![PS5 Dualsense held in front of a PS5 and monitor](https://cdn.mos.cms.futurecdn.net/BN3XX6fDoAKNMba69AC2gb-1920-80.jpg)

PlayStations are traditionally where you go to play PlayStation games, but now you can also use your PS5 to play Nintendo Switch games, too. At least, you can, so long as your PS5 is jailbroken and running the right version of Sony's software. And even then, not all games work, and those that do work might still have performance issues.

Backing up slightly, this whole thing is made possible by a project called ProsperoEden, which is based on the Eden open-source Nintendo Switch emulator that already works on Windows, macOS, and Linux. ProsperoEden takes that open-source base and then adapts it to work on the PS5, and while it's only available as an early alpha version right now, it does indeed work, as reported by VideoCardz.

According to the project's documentation, a number of games have been tested with varying degrees of compatibility. *Cuphead* and*Metroid Dread* are said to run fine, reaching at least 40 FPS.*Hollow Knight*,* Horizon Chase Turbo*,* Mario Kart 8 Deluxe*, and a handful more achieve similar results.

At the other end of the scale, The *Legend of Zelda: Breath of the Wild* is "unplayable," while*Animal Crossing: New Horizons* runs "with major issues" and a frame rate that sits around the nausea-inducing 15 FPS.

The confusing compatibility situation can probably be put down to the fact that the emulator currently uses OpenGL, since there is no Vulkan renderer available to it. The PS5's firmware is also a variable not to be ignored. While most testing was done on a PS5 running the version 6.02 firmware, some builds of the ProsperoEden emulator have been known to work on firmware version 12.70. All of this is to say that your mileage may very well vary if you intend to take ProsperoEden for a spin on your own console.

The good news is that the project is in active development, so compatibility may improve over time. The latest v1.000.010 release promises improved game loading and includes fixes specifically for the *Metroid Dread* and*Super Mario 3D World* titles. It also includes improved OpenGL rendering and performance, including multisample operations, render-target compatibility, shader lifetime handling, and depth copies.

Anyone wondering about connecting their Switch Joy-Con to a PS5 needn't worry; ProsperoEden supports DualSense controllers, and there's even support for saving your game so you won't have to start from scratch every time you play.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

If you want to check out ProsperoEden for yourself, you can. It's available as a free download via the project's GitHub page right now. There's no guarantee it'll hang around for long, though. Nintendo has a history of taking down emulation projects hosted on GitHub.



*Follow* * Tom's Hardware on Google News**,* * or add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Oliver Haslam](https://cdn.mos.cms.futurecdn.net/3XaHYJa7vPsa7PG8i5U8F5-140-80.jpg)

Oliver Haslam has written about technology of all shapes and sizes for over 15 years, both online and in print. He's fascinated by how personal computing continues to change as tower PCs give way to foldable phones and beyond.

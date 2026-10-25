---
title: Cybersecurity bounty hunter says Samsung TVs use AI to record audio and screenshots
  for ads — 'Finally found a company that truly listens to its customers,' says hacker
source_url: https://www.tomshardware.com/tech-industry/cyber-security/hacker-finds-own-samsung-tv-collecting-scary-amounts-of-user-information-and-gets-banned-by-openai-for-cyber-abuse-tv-runs-an-ai-model-that-collects-audio-screenshots-and-plenty-of-other-user-data-for-ad-targeting
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-25T11:20:23Z'
published: '2026-10-25T00:00:00Z'
description: From tracking skipped ads to using connected soundbars as makeshift microphones
image: https://cdn.mos.cms.futurecdn.net/EiDyWR9Yo8wN9DnMZqQdJ4-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
- Creator Economy & Marketing
people:
- Jhet Borja
- Tom
- ngxson
locations:
- TV
- Tizen
organisations:
- Get Tom's Hardware
- Google News
- LG
- Log4j
- OpenAI
- Samsung TV
- Samsung TVs
- Tizen TV
---

![Woman pointing remote at TV](https://cdn.mos.cms.futurecdn.net/EiDyWR9Yo8wN9DnMZqQdJ4-1920-80.jpg)

Reverse engineer and cybersecurity bounty hunter log4j recently found they were getting “weirdly targeted ads” on their Samsung TV and discovered privacy breaches. As they live-tweeted their discoveries, they found increasingly concerning code in the Tizen operating system, including detailed user telemetry from packet logging, audio categorization, screenshots, cross-device identification for ad tracking, and more, all designed to extract as much user information as possible to improve targeted ads.

log4j posted on X that they were concerned with how specific the ads on their 2025 Samsung TV were. They decided to reverse-engineer the Tizen OS on their TV to see what it was doing—they “discovered PRIVACY HORROR,” log4j states, marking the start of subsequent posts sharing more concerning findings.

> i own a relatively new (2025) samsung tv. i kept getting weirdly targeted ads. i tried reversing the firmware but it was aes encrypted and no keys unless tear it apart and do uart/jtag magic. zero days it is. root shell on new samsung TVs! discovered PRIVACY HORROR. write up? [https://t.co/EsxxCy1b6aOctober](https://t.co/EsxxCy1b6aOctober) 21, 2026

The tester theorizes that Samsung TVs are so sluggish because they do a lot of post-processing of user data, including audio, screenshots, and AID (a cross-device tracking ID for ads), plus computer vision processing and models running on the TV. The hacker even found a region-specific convolutional neural network (an AI) that tracks user behavior, citing examples like what videos the user watches, which ads are skipped, and video progress. Log4j also found behavior for TVs without microphones, stating it will find connected devices with microphones, such as a soundbar or a connected Bluetooth device, to record audio.

Hugging Face engineer ngxson commented that they would test the microphone behavior using their Flipper Zero and found that the TV opened the microphone for five seconds, then stopped. ngxson waited for another microphone response but found none hours later. However, ngxson explained that their Tizen TV was already rooted and had multiple settings disabled, so an unmodified TV may behave differently.

## What hardware deals are you hoping to pick up during Black Friday?

The hacker used OpenAI tools to hack the TV, but the company eventually banned them for cyber abuse, as stated in an email they received. log4j defended themselves, saying they never used OpenAI’s tools to exploit or find vulnerabilities, only for local reverse engineering, and that they didn't breach the terms of use. In a comment below their post about the ban, log4j said it seemed OpenAI banned their account because of a primitive classifier.

> @log4j Ok so right off the bat, it opens the mic for exactly 5 seconds then stop. Seems like a strange way to test mic (?) Then no more recording since then, but need to keep observing more to conclude [https://t.co/PSHIfMG2oOOctober](https://t.co/PSHIfMG2oOOctober) 23, 2026

However, Samsung TVs and Tizen aren’t the only culprits in reportedly breaching user privacy; other brands like LG have also been accused of spying on customers. Many owners have also reported their TVs slowing down despite no new features or heavy apps running, suspecting it is mainly bloatware, but it could also be the spying behavior Log4j found. The hacker is also working on a comprehensive write-up of their findings, including how others could do it themselves.

At the end of the post series, they jokingly say they “finally found a company that truly listens to its customers.”

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jhet Borja](https://cdn.mos.cms.futurecdn.net/niBNJTDN6c99Ri7HD5zNZ8-140-80.png)

Jhet Borja is a serial hobbyist who was taking apart toys from childhood and sketching inventions. He now loves doing DIY projects ranging from designing custom 3D-printed parts, building PCs and keyboards, all the way to woodworking. If he's not getting his hands dirty, he's probably brainstorming his next project.

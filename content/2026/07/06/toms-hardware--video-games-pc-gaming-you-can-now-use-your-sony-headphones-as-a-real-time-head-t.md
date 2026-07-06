---
title: You can now use your Sony headphones as a free real-time head tracker for race
  and flight simulators on PC, several hundred games already supported — enthusiast
  creates open-source app that translates live sensor data into in-game camera controls
source_url: https://www.tomshardware.com/video-games/pc-gaming/you-can-now-use-your-sony-headphones-as-a-real-time-head-tracker-for-race-and-flight-simulators-on-pc-several-hundred-games-already-supported-enthusiast-creates-open-source-app-that-translates-live-sensor-data-into-in-game-camera-controls
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-06T18:20:08Z'
published: '2026-07-06T00:00:00Z'
description: A new level of immersion for free.
image: https://cdn.mos.cms.futurecdn.net/aW8RYDVuq3MwJnPU8GoQjn-1280-80.png
---

![Sony WH-1000XM6](https://cdn.mos.cms.futurecdn.net/aW8RYDVuq3MwJnPU8GoQjn.png) 

Sony makes some of the best headphones on the market, and some of their recent models even include a myriad of sensors for spatial audio. These are standard gyroscopes and accelerometers capable of precise tracking, so why keep them limited to just audio features? That's exactly what developer Nicholas Slattery has done with his new project called "Sony Head Tracker" — it's an app that turns your Sony headphones and earbuds into a real-time head tracker for PC games.

The app essentially acts as a bridge between the hardware and the software, which is OpenTrack. Sony baked the Android Head Tracker protocol into its headphones' firmware, which is what enabled spatial audio to expand the soundstage on supported devices. This data is ignored by Windows, but Slattery figured out a way to tap into the protocol and read everything it's capturing.

That includes rotation vectors, gyroscope fields, and Euler Angles (live calculation of yaw, pitch, and roll). The raw data packets are then packaged into a UDP stream that the OpenTrack software can read and understand. OpenTrack supports over 200 PC games and usually works with phones, webcams, and specialized eye or IR trackers, but Slattery's app opens it to an entirely new and ingenious set of devices.

Currently, Sony's WH/WF-1000XM6, WH/WF-1000XM5, and Sony ULT WEAR (WH-ULT900N) are officially compatible. Older models like the WH-1000XM4 or XM3 won't work because they lack the hardware (sensors) required for the head tracking. Apple's AirPods, which popularized Spatial Audio, use the company's proprietary protocol that doesn't open itself up on any device, as you'd expect, so they're also ruled out.

Once everything is set up, you just wear your Sony headphones and the in-camera will respond to your head movements, turning around with you. If you look to the side or glance up, the camera will peep there as well, as if you were wearing a VR headset. But keep in mind that this is not a VR replacement as the screen in front of you is still stationary. Regardless, this unlocks another level of immersion for race and flight sims.

The creator has tested the app to work flawlessly with *Microsoft Flight Simulator*,* Elite Dangerous*, and* Assetto**Corsa* already. For those of us not rocking elaborate multi-monitor configs, something like this can serve as a middle ground between a true 6DoF setup and a simple helmet cam in-game, all for free. Sony Head Tracker is also open-source, so we only expect it to improve over time and expand its compatibility.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

---
title: AliExpress allegedly uses your browser's audio system to fingerprint your PC
  — hidden code runs even when no sound is playing
source_url: https://www.tomshardware.com/tech-industry/cyber-security/aliexpress-allegedly-uses-your-browsers-audio-system-to-fingerprint-your-pc-hidden-code-runs-even-when-no-sound-is-playing
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-25T13:07:37Z'
published: '2026-08-25T00:00:00Z'
description: Hidden code allegedly gathers detailed device data.
image: https://cdn.mos.cms.futurecdn.net/t6UKEpSvF7JMTjpnYQS8Re-2000-80.jpg
---

![Alibaba](https://cdn.mos.cms.futurecdn.net/t6UKEpSvF7JMTjpnYQS8Re.jpg) 

Chinese multinational tech giant Alibaba has been accused of tracking web users after a developer discovered its global online marketplace running hidden audio processes that could be used for sophisticated audio fingerprinting. While investigating an issue with his wireless headphones, Matt Callaghan found that opening an AliExpress webpage in Firefox or Chrome interfered with the multipoint Bluetooth audio feature.

As Callaghan explains in his blog post, “Normally the PC takes priority playing audio, with my phone being able to play audio when nothing is playing on the PC. Usually I listen to music on my phone but with notifications or YouTube playing through the PC.” However, shortly after loading the AliExpress homepage, audio from his phone would stop playing, despite no media playing on his PC. Closing the AliExpress tab immediately fixed the issue, while muting the tab, browser, or Windows did not seem to resolve it.

Their investigation began by inspecting various conventional media elements; however, he did not find any unusual activity. He also zeroed in on the fact that the problem would not begin immediately, but rather after the webpage had been sitting idle for a few seconds. He then moved on to inspect the Web Audio API to wrap the AudioContext constructor so that it would record whenever a page created an audio-processing context. They additionally wrapped AudioNode.prototype.connect() to see whether anything was connected to the context's audio destination.

Eventually, Callaghan found that the page was loading two suspicious scripts named collina.js and fireyejs.js, which appeared to be part of Alibaba's browser security and anti-abuse tooling. With some help from AI during his research, he found that the scripts built a Web Audio graph using a sawtooth oscillator to generate a waveform. An analyzer then measured the results after they passed through the browser's audio implementation, while another script read the resulting frequency data. The scripts also set the volume gain to zero, meaning there was no audible sound or noise, even though the browser continued actively processing the Web Audio graph.

Unlike autoplaying videos, there is no media element playing, which is why the browser's tab mute control does not help. However, the webpage continues performing live audio processing, keeping the Bluetooth audio path active and preventing multipoint Bluetooth headphones from switching between devices. Further investigation also uncovered code collecting information related to screen dimensions, device memory, browser plugins, WebGL rendering, supported audio and video formats, browser performance, mouse events, and more. The scripts also appear to serialize and encrypt the collected data before sending it to Alibaba's telemetry services using fetch() or sendBeacon() functions.

Following the discovery, Firefox said on X that its browser includes built-in protections against fingerprinting. The company pointed to a blog post explaining that Firefox 118, released in September 2023, introduced additional protections against Web Audio-based fingerprinting. Brave also claims to block audio fingerprinting by default. According to the browser maker, it does this by injecting randomized data into the browser's audio output, making the fingerprint appear different to websites and resetting the data between sessions.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Kunal Khullar](https://cdn.mos.cms.futurecdn.net/NDK3ae3zDxAx2BJnMXxBJV.jpg)

Kunal Khullar is a contributing writer at Tom’s Hardware. He is a long time technology journalist and reviewer specializing in PC components and peripherals, and welcomes any and every question around building a PC.

---
title: Ex-Sega engineer creates 'super realistic' CRT monitor emulator — incredible
  retro offering even includes TV screen tapping to fix picture
source_url: https://www.tomshardware.com/video-games/retro-gaming/ex-sega-engineer-creates-super-realistic-crt-monitor-emulator-incredible-retro-offering-even-includes-tv-screen-tapping-to-fix-picture
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-16T10:21:38Z'
published: '2026-07-16T00:00:00Z'
description: Physically satisfying retro simulation tech is the brainchild of an ex-Sega
  employee.
image: https://cdn.mos.cms.futurecdn.net/B2rwkPp8J3AkwWs9NM3efP-1920-80.jpg
---

![GOROman’s famicom-rf-hackrf-decoder software in action](https://cdn.mos.cms.futurecdn.net/B2rwkPp8J3AkwWs9NM3efP.jpg) 

An ex-Sega engineer has created a CRT emulator for macOS so realistic that it even supports screen tapping to fix the notoriously sketchy performance of the technology. On Tuesday, a developer showcased a CRT emulation project which some commenters complained was more like a CRT damage simulator. In other words, the CRT effects like flickering, noise, and aberrations were judged by the masses to be somewhat overdone. Today, @GOROman has followed up by demonstrating that the famicom-rf-hackrf-decoder software’s CRT rendering can be improved via an old-school whack to the top of the monitor. See it with your own eyes, in the video embedded below.

The developer of this CRT emulator, GOROman, is an ex-Sega and ex-Facebook software engineer. They explain that the famicom-rf-hackrf-decoder software receives VHF RF output (NTSC-J) from their Famicom (Nintendo NES) via an open-source SDR (software-defined radio) solution dubbed the HackRF One.

With the software running and the NES plugged into the HackRF One, the console’s RF-modulated video can be displayed on VHF channel 1 or 2. However, here you can see it on a modern LCD, in a window on the desktop. Thus the GOROman project is performing a full NTSC-J color decode in software and displaying the result on the desktop in real time via SDL2.

It is further explained that the Famicom “is not broadcast-compliant (non-interlaced 240p, chroma phase advancing 120° per line, one short line per frame).” Therefore, the decoder has to run several processes in the background to avoid quirks like drifts, wobbles, and color burst instability.

 ![GOROman&rsquo;s famicom-rf-hackrf-decoder software in action](https://cdn.mos.cms.futurecdn.net/K7RX29ANmFcqTjTYXNrBfP.jpg) 


In summary, the Famicom’s RF output isn’t ideal for piping into modern monitors, so the decoder has to effectively simulate an analog TV’s brain, locking in the image stability and color. The initial demo shared by GOROman looked so much like a ‘damaged TV’ because the dev wanted to play around "by shifting the VHF frequency (exaggeratedly)." [machine translation] It was an eye-catching, humorous demo.

So, what’s happening with the new video and demo of percussive maintenance support? On social media, some have guessed that the fun picture stability-fixing mechanic could be using feedback from the Apple MacBook’s lid angle sensor. However, I looked at the GitHub page for GOROman’s famicom-rf-hackrf-decoder software, released under the MIT open-source license, and there appears to be an input variable for "audio tap," so the effect may be based on mic audio input.

Someone in the comments has requested a magnet mode to play with the ‘CRT,’ so guess what might happen tomorrow.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

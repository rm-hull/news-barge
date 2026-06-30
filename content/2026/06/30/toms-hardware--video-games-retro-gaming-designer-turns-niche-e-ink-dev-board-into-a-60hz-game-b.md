---
title: Designer turns discontinued E-Ink dev board into a 60Hz Game Boy handheld —
  dual-core chip runs at 100% to power handheld, 960x540 display employs ultra-low-cost
  ESP32-S3 microcontroller
source_url: https://www.tomshardware.com/video-games/retro-gaming/designer-turns-niche-e-ink-dev-board-into-a-60hz-game-boy-handheld-960x540-display-powered-by-ultra-low-cost-esp32-s3-microcontroller
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-06-30T11:19:05Z'
published: '2026-06-30T00:00:00Z'
description: The practicality of the project isn't really the point; it's mostly a
  fascinating demo of hardware hacking skill.
image: https://cdn.mos.cms.futurecdn.net/gdfk4jCqxB5odRUQCVsVZG-1920-80.jpg
---

![Two photos of the PaperBoyS3 emulator running classic Mario and Pokemon games.](https://cdn.mos.cms.futurecdn.net/gdfk4jCqxB5odRUQCVsVZG.jpg) 

Enterprising enthusiast Wenting has turned an M5Stack PaperS3 dev kit with an e-ink screen into a more-or-less fully functional Game Boy. If you're not a hardware hacker yourself, there's a fair chance you've never heard of Wenting Zhang or Modos Labs. The engineer's "Wenting Channel" on YouTube has been a favorite of niche tech nerds for a long time, showcasing all kinds of hardware hacking expertise. Zhang spent the last several years turning that expertise into Modos Labs, a company whose high-refresh e-Ink displays we've covered before.

Okay, it won't play real cartridges, the sound is kind of jank, and the performance isn't always full speed. Still, this is quite an achievement for a few reasons. The PaperS3 is an e-Ink dev kit, not really a commercial product. It's intended for prototyping and, well, exactly this sort of hardware hacking. A key detail to understand is that this device isn't powered by some multi-core Rockchip or Allwinner SoC, but rather by an ultra-low-cost ESP32-S3 microcontroller with just two cores running at clock rates measured in hundreds of MHz, not GHz. Moreover, its e-Ink display is not really intended for the kind of smooth refresh normally required for playing video games, yet Zhang pulled it off.

 ![Photos of the PaperBoyS3 emulator running multiple games, and being controlled via Bluetooth.](https://cdn.mos.cms.futurecdn.net/eYTHREjBoeChdoG27JNyXh.jpg) 


To understand how this Game Boy emulator is even possible, you have to understand Zhang's breakthrough with E-ink hardware, which he originally developed for his open-source monitor project, the Modos Flow. He has a whole video explaining the tech, but the summary is basically that he replaced the display controller of a typical e-Ink display with a powerful FPGA so that he could treat every single pixel as an independent display region and then only update the parts of the screen that are actually changing each frame.

How, then, did he achieve this on the embedded controller in the PaperS3? It's only possible because the Game Boy screen is very low resolution by modern standards at just 160x144 pixels. The screen on the PaperS3 is 960x540, so he was able to multiply the resolution by three to give him enough room for dithering to reproduce the four possible shades of the original Game Boy screen. This process takes up almost the entirety of the second CPU core in the ESP32, leaving just enough room for audio processing while the actual emulation happens on the first CPU core.

![GameBoy Emulator on ESP32 + Eink (M5Stack PaperS3) - YouTube](https://img.youtube.com/vi/oPbOK90aJEo/maxresdefault.jpg) 

The end result is a very convincing facsimile of the Game Boy's display, except instead of being a tiny and dim LCD, it's a razor-sharp, crystal-clear e-Ink display. Zhang even implemented some quality-of-life features, such as partial Bluetooth LE controller support as well as dedicated quick-save and quick-load touchscreen 'buttons' to save the emulator's state. You can even load a state directly from the front-end, allowing you to instantly resume where you left off when you have to stop.

That's not to say the project is flawless, though. For one thing, it relies on touchscreen controls with no haptic feedback because the device simply doesn't have the requisite hardware for it. Perhaps more pressingly, the PaperS3 only has a simple piezo buzzer for sound, and while Zhang pulled off some real hackery to get recognizable Game Boy audio out of the mono buzzer (by using pseudo-polyphony like a ZX Spectrum hacker), it doesn't quite sound like a real Game Boy. The hacker also doesn't discuss the battery life of the device while running his emulator; given that he's pushing both CPU cores of the microcontroller to their limits, and also that e-Ink displays are actually quite power-thirsty when driven at 60 Hz, we can't imagine it's great.

 ![A screenshot of the M5Burner store showing the PaperBoyS3 emulator.](https://cdn.mos.cms.futurecdn.net/dfkv4quVqrwiLMzoEUXpeQ.jpg) 


If you're keen to try out "Paper Boy S3", Zhang says he's uploaded it to the M5Burner tool that serves as both a firmware flasher and app store for the M5Stack devices. However, as he notes himself in his video on the project, PaperS3 is actually already discontinued by the manufacturer, so you might have a hard time getting hold of one if you don't already. Still, the project serves as a fascinating demo for what can be done with ultra-low-end hardware and a direct counterpoint to at least one of the weaknesses of e-Ink displays.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi.jpg)

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

---
title: PC gamer vibe-codes a safeguard against RTX 5090 power connector failures —
  monitors per-pin power draw, shuts down system if it exceeds 9.5A for more than
  15 seconds
source_url: https://www.tomshardware.com/pc-components/gpus/pc-gamer-vibe-codes-a-safeguard-against-rtx-5090-power-connector-failures-monitors-per-pin-power-draw-shuts-down-system-if-it-exceeds-9-5a-for-more-than-15-seconds
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-06T14:32:40Z'
published: '2026-08-06T00:00:00Z'
description: The 35MB application forcibly shuts the machine down if power exceeds
  configurable limits for too long.
image: https://cdn.mos.cms.futurecdn.net/FVs2BKR6Wu5JzFi2sKtAsD-1280-80.jpg
---

![Astral RTX 5090](https://cdn.mos.cms.futurecdn.net/FVs2BKR6Wu5JzFi2sKtAsD.jpg) 

Many owners of high-end NVIDIA graphics cards live in fear of the high-density 12+4-pin connector that supplies power to their video hardware, as the connector has been shown to have dubious reliability versus the previous-generation PCI Express peripheral power connectors, largely due to an extremely minimal safety margin. A user on Reddit has decided that existing measures to protect his card weren't sufficient, and has now vibe-coded himself up a free tool that shuts the whole PC down if per-pin power draw is too high for too long.

The tool is ironically called "12VHPWR Guard" despite the fact that none of the graphics cards it supports actually have a 12VHPWR connector. The two cards primarily supported are the ASUS ROG Astral GeForce RTX 5080 and GeForce RTX 5090, both of which come with the updated 12V-2x6 connector. The modified plug is an attempt to mitigate the melting issue by slightly adjusting the dimensions, forcing users to make sure it is fully inserted into the card. However, the main power delivery wires and their contact points remain the same, and so the burning issue continues.

The reason the developer says that the tool only supports these two cards is that the ROG Astral GPUs have dedicated per-pin current sensors, although, despite what the author says on Reddit, ASUS' ROG Matrix RTX 4090 and RTX 5090 also have these sensors, and the author lists at least the Matrix RTX 5090 as supported on GitHub. The author also notes that ASUS' GPU Tweak III software can throw a warning when power draw goes too high, but that the warning "does nothing" if he's in-game or AFK, despite the fact that the app does support an audible warning.

 ![A screenshot of ASUS GPU Tweak III software, with an arrow indicating which option enables the audible over-current warning.](https://cdn.mos.cms.futurecdn.net/stHMpqLL2TGmxuyS2D3qik.png) 


In any case, the app by Humza Khalid and Claude AI is a very simple and fully free app that requires 35MB of RAM and a minuscule amount of CPU time to poll the I2C bus on the card for the current values twice per second. You can mouse over the system tray icon to see the current maximum power draw for any of the six +12V pins on the power connector. The pins are rated for about 9 amperes of current, and ASUS' own warning threshold is 9.2A, but Khalid has configured his tool such that it looks for current draw over 9.5A over a period of 15 seconds. If that period is exceeded, the tool abruptly shuts the system down, force-closing blocking apps.

The current threshold and the required duration are both configurable, so if you want more lenient or more vigilant settings, you can set them that way. It's surprisingly full-featured; it supports HWiNFO-based shared memory monitoring if the app is unable to access I2C for whatever reason, and it also supports both toast notifications and Windows Event Viewer logging. It's also apparently smart enough to detect sensor loss and avoid reporting all is well when it doesn't actually know, which is reassuring.

 ![A screenshot of the 12VHPWR Guard application.](https://cdn.mos.cms.futurecdn.net/PWC6ASDKdnidRh2i6vyiTH.png) 


*Alan Wake 2*. (Image credit: Humza Khalid/GitHub)

Given the extreme cost of these GPUs (which are among the best graphics cards, to be fair), it's easy to see why owners would resort to these measures. The cheapest of them, the ROG Astral OC GeForce RTX 5080, is currently starting at about $1810 USD. While there have been attempts to blame user error (and indeed some cases certainly were user error with the 12VHPWR connector), it has been thoroughly proven that this connector can fail through no fault of the user. While these failures aren't really commonplace, the fact that they happen does speak to the razor-thin safety margin built into the connector.

If you have one of the supported graphics cards, you can head over to Khalid's GitHub page to grab the tiny application. Only Windows 10 and 11 are supported for now, and you'll also need Python 3.10 or higher, which is why such a simple application requires 35MB of RAM. Just remember that the app isn't a replacement for making sure your graphics card, including its 12V-2x6 connector, is installed correctly.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi.jpg)

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

- 
I'm sorry but this is Nvidia's problem and the fact that they haven't done anything to own it is dubious and unforgivable. I can't speak for you, but there is literally no way I'm spending an excess of $1000 on a GPU just to worry that it's going to catch fire. Come to think of it, I wouldn't spend $200... Having to worry about your computer catching fire is something no one should opt for.Reply
 
 Nvidia should be bearing the cost of that worry -- by eliminating the potential -- not consumers. I just cannot reward them for pushing that into consumers by paying them obscene $$ for their products.

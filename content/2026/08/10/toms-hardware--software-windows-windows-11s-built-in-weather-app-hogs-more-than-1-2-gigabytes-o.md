---
title: Windows 11's built-in weather app hogs more than 1.2 gigabytes of RAM just
  to tell the forecast — memory-sucking web wrapper filled with ads masquerades as
  an actual application
source_url: https://www.tomshardware.com/software/windows/windows-11s-built-in-weather-app-hogs-more-than-1-2-gigabytes-of-ram-just-to-tell-the-forecast-memory-sucking-web-wrapper-filled-with-ads-masquerades-as-an-actual-application
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-10T13:37:40Z'
published: '2026-08-10T00:00:00Z'
description: 5x more memory consumption than macOS.
image: https://cdn.mos.cms.futurecdn.net/6nCo95QyodqQCx2UzFtjzG-2215-80.png
---

![Windows 11's weather app](https://cdn.mos.cms.futurecdn.net/6nCo95QyodqQCx2UzFtjzG.png) 

Windows is in a tough spot right now, with years of neglect and stagnation reaching a boiling point with customers. Lack of optimization, bloat, ads, forced AI slop, and persistent tracking have forced Microsoft to admit its missteps and commit to fixing the OS at large. Windows Latest's new testing shows that the built-in weather app is a perfect representation of the state of Windows. The "app" consumes up to 1.2GB of RAM while idling, and it serves up a bunch of ads while you check the temperature.

MSN Weather is the default weather app that ships with Windows, which explains why it's filled with promotions throughout, despite being part of a paid OS. To be clear, the app looks very modern and has all the data you could ask for, such as live radar overlays, hourly wind and precipitation breakdowns, air quality index, and moon phases. It's also accurate because the data is sourced from a bunch of different providers across the world, but mostly *Foreca*.

 ![Windows 11's weather app](https://cdn.mos.cms.futurecdn.net/QVABS85AF4Ro83cPRHcNPc.png) 


The author explains that getting accurate forecasts is not a cheap endeavor, so it's not like Microsoft is running a charity. But the comparison falls apart when you look at what the competition is offering. Apple's native weather app on macOS is just as beautiful, detailed, and accurate, yet it's free of ads. It also only consumes about 250MB of memory to show all that data, so 5x less than Windows. This is because MSN Weather is technically not even an app to begin with; it's a web wrapper that's pinging a bunch of browser tabs in real-time.

When the author clicked on the Task Manager entry for MSN Weather, they saw 8 Chromium-based subprocesses, confirming that they're just looking at a website being rendered via WebView 2. For context, native Windows apps are supposed to adhere to the WinUI framework, which the company is slowly adopting over Win32 and UWP. Microsoft is committed to updating all the native apps Windows ships with to Win32, which should significantly improve their optimization, but we don't know if the ads will suddenly disappear as well.

 ![Windows 11's weather app](https://cdn.mos.cms.futurecdn.net/MufHV4ANks7Tsrz7oaxG3G.png) 


The author saw Adobe Acrobat ads while checking the forecast, and we saw two ads — one for LendingTree and another for Spotify. Apart from that, scrolling around the app and clicking on the different menus and boxes was fast enough. We have to emphasize that the app really is granular and well-built from an aesthetic point of view; Microsoft gets full points for that, or is it MSN? That distinction is another issue that makes the weather app conundrum a bit more confusing.

When Microsoft promised to rebuild all native Windows 11 apps, it didn't explicitly say those would include MSN-branded services too, like MSN Weather and MSN News. Seeing as though they're simply called by their utilitarian names in the OS, there's a strong chance that these memory hoggers will also be eventually upgraded. For now, just stick to your phone, especially if you were among those who immediately Googled how to remove the weather widget from your taskbar that fateful day.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

---
title: Discord should be much quicker and less resource-intensive in the near future
source_url: https://www.pcgamer.com/hardware/discord-is-cutting-memory-usage-and-speeding-up-boot-times-joins-xbox-epic-steam-and-more-for-similar-upgrades-just-this-year/
source_site: PC Gamer
source_slug: pcgamer
description: If it's quicker and more efficient, I'm in.
image: https://cdn.mos.cms.futurecdn.net/bK4uZhxvRgcb85EAubQrc-1920-80.jpg
published: '2026-11-06T00:00:00Z'
scraped_at: '2026-11-06T16:53:31Z'
categories:
- Technology & Software
people:
- Jacob
- Stanislav Vishnevskiy
locations:
- Mine
- Rust
organisations:
- CTO
- Discord
- Electron
- PC Gamer Circuit Breaker
---

> We've been early adopters of Rust since 2018 and a lot of our infra, voice tech, and even some of the current client is already Rust, the holy grail was getting the whole client there. That means Electron goes away, and so does React Native, mobile keeps native UI but shares app… [https://t.co/2CgWyOzaq0](https://t.co/2CgWyOzaq0) pic.twitter.com/IdOGd4nUglNovember 4, 2026

Open up Task Manager and check how much memory Discord is currently hogging on your PC. If it's anything like mine, it's probably north of 500 MB. Alas, things should change soon, as Discord is moving the client completely over to a new programming language. It might not sound like that big of a deal, but Discord's CTO, Stanislav Vishnevskiy, shows it running on as little as 290 MB of memory.

Discord is switching from Electron to Rust. Electron is a software framework, a building block that allows JavaScript apps (among others) to run standalone on desktops. Built on Chromium, the underlying model behind Google Chrome, there is an overhead here that swapping to Rust aims to fix.

Vishnevskiy says, "We've been early adopters of Rust since 2018 and a lot of our infra, voice tech, and even some of the current client is already Rust, the holy grail was getting the whole client there. That means Electron goes away, and so does React Native, mobile keeps native UI but shares app code with desktop via Rust."

Though some suspected Discord would be swapping to Rust using Tauri (an open-source framework for desktop and mobile platforms), Vishnevskiy says it's actually using GPUI (a framework written in Rust), but "We have our own patches on top of it".

Vishnevskiy also says the goal is to get the program into testing with users soon, but no official date has been given. Either way, with Vishnevskiy showing off a resource demand of 290.2 MB whilst active, that's still a pretty big dip below what it runs at now. Mine is currently flitting between 500 and 600 MB, and my colleague Jacob saw it go up to 785 MB running on Windows.

> The new Discord client using less RAM is just part of the story. Clicking around feels instant, I can't go back. Check out the boot time. [https://t.co/YF9g9K30b9](https://t.co/YF9g9K30b9) pic.twitter.com/x7ayyWBVQJNovember 5, 2026

Reportedly, the new Discord client is also faster to use, booting much quicker. Vishnevskiy showed two laptops, one with the old client and one with the new, and the new client opens up significantly faster (six seconds versus one in my approximation).

Naturally, we are hearing this from the mouth of the company, so we'll have to get the new Discord client in our hands to see how much faster and how much more efficient it really is, but anyway, to get a little more out of your current memory will always be a boon right now.

The PC Gamer Circuit Breaker newsletter breaks down the latest PC gaming tech, and finds you the best deals on the best products

The memory crisis is continuing to drive the prices of gaming gear up, but software tweaks like this (including both Epic and Steam getting faster) are very much welcome in my eyes.

![Razer Blade 16 gaming laptop](https://cdn.mos.cms.futurecdn.net/YwnnY4PZ7TcCYKRYDho7VW-140-80.jpg)

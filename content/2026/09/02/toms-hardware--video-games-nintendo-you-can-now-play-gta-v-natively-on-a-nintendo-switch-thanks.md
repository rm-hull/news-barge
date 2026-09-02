---
title: You can now play GTA V natively on a Nintendo Switch thanks to unofficial Homebrew
  port — game runs at 30 FPS but requires a jailbroken, overclocked Switch
source_url: https://www.tomshardware.com/video-games/nintendo/you-can-now-play-gta-v-natively-on-a-nintendo-switch-thanks-to-unofficial-homebrew-port-game-runs-at-30-fps-but-requires-a-jailbroken-overclocked-switch
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-02T12:44:58Z'
published: '2026-09-02T00:00:00Z'
description: No, this does not mean GTA VI can run on a Switch 2.
image: https://cdn.mos.cms.futurecdn.net/iwm5jZCX5W5LNzxXPj8VYE-1920-80.jpg
---

![Grand Theft Auto V running natively on a Nintendo Switch](https://cdn.mos.cms.futurecdn.net/iwm5jZCX5W5LNzxXPj8VYE.jpg) 

Grand Theft Auto V came out in late 2013 for PS3 and Xbox 360 before it was ported to eighth-gen consoles. Despite running on seventh-gen hardware, Rockstar never released it on the Nintendo Switch. Fast forward 13 years later and modders have done Rockstar's job for them. An unofficial Homebrew port of GTA V is now available for the Switch, and it runs natively on the hardware at roughly 30 FPS. You do need a jailbroken device, and it needs to be overclocked in order for the game to be playable.

GTA V corriendo en Nintendo Switch.- Nativo sin Android ni Linux (No es Stream).- Pesa 49GB.- Ocupas Overclock (Yo uso Sys-CLK que es seguro) pero si usas Horizon OC irá mucho mejor.- Corriendo en mi OLED sin modificaciones de RAM, puro Overclock seguro.INFO:… pic.twitter.com/ChtFlwq2TKAugust 28, 2026


The port is developed by Paralympics Productions and is based on the leaked source code from 2023. That source code allowed modders to reverse-engineer the game logic and recompile it for Arm, allowing it to run natively on the Switch's Tegra X1 SoC. That means GTA V can technically also run on Android, and sure enough, Paralympics' Discord server teases that an Android port is coming soon.

The Discord server is also where you'll find all the necessary resources required to make this work. There are four key components: a package builder, an asset converter tool, modified config files, and a specific folder layout. They work together to patch the original GTA V files, construct an executable (.NSP), and make the game data compatible with Switch's Horizon OS.

Obviously, we can't detail the entire process here, but it's relatively straightforward, and you'll find detailed guides, including a video tutorial, on the Discord. There are a few bugs to look out for, but personally we did not face any during installation. You can skip all the work and just download the already-prepped archive from Switch piracy sites, too, which is around 50GB.

Once everything is set up, you transfer the NSP to a jailbroken Switch running custom firmware, along with the modified game files, and open GTA V like you would any other game. It's kind of surreal at first, but it boots up and runs directly on the console without any emulation overhead. The load times are alright; it doesn't heat up the handheld like crazy, and battery drain was similar to any other demanding title.

 ![Grand Theft Auto V running natively on a Nintendo Switch](https://cdn.mos.cms.futurecdn.net/9dfNtUgGborUeKjGJ6idWE.jpg) 


Despite that, the performance is quite wonky because the Tegra X1 inside is dated and thermally constrained. You'll get between 10-25 FPS depending on exactly what Switch model you have and the silicon lottery. To get a more stable experience that mostly locks the framerate at 30 FPS, you'll need to overclock your Switch. It's easy enough to do so through sys-clk, and you can create different profiles for handheld, docked, and charging modes.

We tried moderate overclocks across the CPU, GPU and memory on a Switch OLED, and were able to run the game at a "smooth" 30 FPS as long as there wasn't too much action going around. The moment a bunch of NPCs pop up in a mission, or there's an explosion, for instance, the framerate dips quite aggressively. The controls also felt weighty since Joy-Cons aren't suited for precise movement, so the portable experience might be a bit compromised.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

 ![Grand Theft Auto V running natively on a Nintendo Switch](https://cdn.mos.cms.futurecdn.net/dR8ZX7RtcoA9d5mRWiq8WE.jpg) 


Plenty of folks online have gone past the starting mission and explored the open world, too. There are no issues with save states, and the game runs surprisingly well considering the Switch's stature. Keep in mind that the source code making this possible comes from GTA V Legacy in particular, which is the PS4, Xbox One, and PC version. The PS3/Xbox 360 version of the game did not leak, or else scaling down the logic to fit within the Switch's 4GB memory buffer would've been far easier.

Those consoles only shipped with 512MB of unified RAM. Instead, the modders had to deal with high-resolution PC assets that needed to be heavily compressed first. The modified config files mentioned earlier throttle settings like draw distances and particle counts, so the PC engine code doesn't instantly melt the Switch. At the end, the Homebrew port performs similarly to the PS3/Xbox 360 versions of the game.

![Grand Theft Auto V running natively on a Nintendo Switch](https://cdn.mos.cms.futurecdn.net/QwMmmEkFBHcDFpsKvxbrKV.gif)


Paralympics Productions has already put out a few patches that improve performance, with more to come down the line, especially once the Android port rolls around. You can already emulate GTA V on Android phones through apps like GameHub and Winlator that translate x86 instructions into Arm. That will run much better if you have a flagship (Snapdragon) phone from the past few years. You can even emulate this Homebrew port through a Switch emulator if you want to enjoy twice the overhead.

It feels like the emulation and modding community across the entire handheld space is going through a renaissance. Ever since the Steam Deck lit the spark, these developers have made the impossible seem possible. People used to wonder why GTA V never came out on the original Switch (the answer is GTA: Online) up until literally weeks ago, and now we have the game running natively on an almost decade-old device that was underpowered even at the time it came out.

Okay, this is impressive and lends more credibility to my theory that the Switch 2 will probably get a port of both GTAV and GTA6 as well as RDR2. pic.twitter.com/LkEnuQzfmGAugust 28, 2026


This does not suddenly mean that the Switch 2 can run GTA VI. For the PS5/Xbox Series version of the game, you'll need a potential Switch 3 if we follow a similar trajectory. More importantly, though, Rockstar's stance towards Nintendo in general has changed, and that plays a much bigger role in getting GTA VI on Nintendo hardware one day as opposed to just the capabilities of the silicon.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg) 

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

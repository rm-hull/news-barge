---
title: Microsoft shipped a native Xbox 360 emulator with its new backwards-compatible
  releases on PC — modders quickly got 360 games running with minor tweaks
source_url: https://www.tomshardware.com/video-games/xbox/microsoft-shipped-a-native-xbox-360-emulator-with-its-new-backwards-compatible-releases-on-pc-modders-quickly-got-360-games-running-with-minor-tweaks
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-25T13:57:17Z'
published: '2026-07-25T00:00:00Z'
description: The best Xbox 360 emulator ever made?
image: https://cdn.mos.cms.futurecdn.net/tSrSwZTHxykQhTAvpueiGi-1536-80.jpg
---

![Xbox Art](https://cdn.mos.cms.futurecdn.net/tSrSwZTHxykQhTAvpueiGi.jpg) 

Microsoft just released four original Xbox games on PC as part of its efforts to bring backwards compatibility to the platform. For years, Xbox consoles have enjoyed a similar luxury, with the latest Series X|S systems being able to play two-decade-old OG Xbox titles. However, to achieve this on PC, Microsoft used a native x86 version of its in-house Xbox 360 emulator. As you might expect, modders were quick to pounce on the opportunity to run 360 games on PC, with "varying degrees of success" so far.

## How do you log in to your PC?

The discovery was initially made when data miners looked at the package contents of these backwards-compatible titles.*Neo Te Aika* found out that they were packaged as standard Games on Demand, or GOD files, which is the official file format used by Xbox 360 hardware. A GOD package contains the actual game, its headers, and DRM. By using a GOD extractor, modders were able to open them and convert them into a base ISO that can be played with an emulator, or on a jailbroken Xbox 360. All this would be a huge development on its own.

looks like those new backwards compatible PC releases are xbox 360 GOD files, you can use GOD extractors to convert those to xbox 360 isos, which extract into standard Xbox games.there might be a pathway here to use this official emulator release to boot other Xbox games pic.twitter.com/eXYrTFD91QJuly 23, 2026


What followed, though, has the potential to change the original Xbox and Xbox 360 emulation scene forever. *Nathan* on X scoured through those same files to find something called Xe03. Also called Fission, Xe03 is Microsoft's official Xbox 360 emulator that comes baked into the Xbox One and Xbox Series consoles for backwards compatibility. 

Within the Xbox 360 environment, Microsoft already had another emulator called XeFu, or Fusion, that emulates the original Xbox. So, it's basically an emulator within an emulator. That's how modern Xbox consoles have been able to play OG Xbox titles. To Xe03, it's just opening a standard Xbox 360 package, but the binary inside is coded to launch XeFu, which then takes over to run the original Xbox game

When Microsoft released backwards compatible Xbox games on PC, people expected the company to have built an x86-native OG Xbox emulator from scratch. An emulator that didn't rely on an outer layer or any external components. Instead, what Microsoft did was simply recompile Xe03 to run natively on x86 PCs instead, indirectly handing over the ultimate 360 emulator to the community. 

By modifying the app container and swapping out game packages, projects like XWine1 and independent reverse-engineers bypassed the inner OG Xbox layer (Fusion) and managed to load raw Xbox 360 executables (.xex files) directly into Xe03. The results have been mixed but incredibly promising, nonetheless. The XWine1 team was able to get Plants vs. Zombies, Steins: Gate, Fuzion Frenzy, and Midnight Club: Los Angeles to boot and run with varying degrees of stability.

By combining Microsoft's recently-released PC port of XeO3 with specific components of XWine1, SlimEra namely, it becomes possible to run dumped backwards-compatible Xbox 360 and Xbox Original games before they see an official PC release, with varying degrees of success pic.twitter.com/6eocCCT1cWJuly 23, 2026


Fuzion Frenzy is actually one of four OG Xbox titles that Microsoft officially released so that one is particularly well-optimized. Since the hard part of reverse engineering first-party code has already been done by Microsoft, optimization remains the only challenge. As time goes on, and the specific emulator files are fine-tuned for general usage, we should expect more and more titles to run flawlessly. 

Microsoft has also promised to release more official backwards compatible titles on PC, but it hasn't said anything about Xbox 360 games. Therefore, the discovery of Xe03 holds immense potential for the future of Xbox 360 emulation on PC — the community just has to focus on optimization now. This development can be particularly fruitful for handhelds that are power-constrained; Xe03 has very light minimum requirements for devices like the ROG (Xbox) Ally and Lenovo's Legion Go lineup.

Moreover, Microsoft's PC version of Xe03 also upscales the original 480p output of OG Xbox games to 4K. It also adds built-in V-Sync, anisotropic filtering, enhanced anti-aliasing, and borderless windowed modes. Since the games were distributed though the Xbox PC app, they're part of the Xbox Anywhere program so if you own the digital license of said game on console, you get it for free on PC (and other places). Microsoft will also bring Xbox Achievements support to backwards compatible titles soon. 

The last two elements will likely be ignored by the modding community since the OG Xbox virtualization is the important part, enabled by the Xe03 engine that has now become the main takeaway from all this. To be clear, open-source emulators such as Xenia have existed for years and provide a highly-satisfactory Xbox emulation experience, but Microsoft's official, in-house solution should be more efficient. 

What OG Xbox or 360 games would you like play on PC?

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

- 
This story is putting a far more positive spin on the discussion we had yesterday, focused on the overhead of double emulation. Does this just crush the Xbox/Xbox 360 emulator development scene aside from people wanting advanced features?Reply

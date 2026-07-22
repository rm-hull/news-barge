---
title: LG monitors are reportedly automatically installing bloatware on Windows 11
  PCs, but there's an apparent fix
source_url: https://www.techradar.com/computing/monitors/you-can-stop-lg-monitors-that-are-reportedly-installing-bloatware-on-your-windows-11-pc-but-the-fix-shouldnt-require-this-much-effort
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-22T17:37:35Z'
published: '2026-07-22T00:00:00Z'
description: LG's changelog seemingly confirms that monitors install bloatware on
  Windows 11 PCs, and unfortunately, the fix is rather cumbersome.
image: https://cdn.mos.cms.futurecdn.net/sV3QTWQVuKkwzxpG326DEH-2560-80.jpg
---

![An LG Ultragear GX9 on a desk](https://cdn.mos.cms.futurecdn.net/sV3QTWQVuKkwzxpG326DEH.jpg) 

- **LG monitors are reportedly installing bloatware on Windows 11 PCs**
- **The LG Monitor App Installer carries a McAfee pop-up and is automatically installed when connecting an LG monitor to a PC**
- **There's a fix for this, but it's a rather fiddly affair**

It's no secret that Windows 11 users have voiced frustrations regarding bloat on the operating system for years, and unfortunately, LG's monitors are reportedly making the situation worse.

As reported by Windows Latest, LG monitors are installing McAfee bloatware on Windows 11 PCs without consent, and there's evidence of this in the changelog of LG's monitor app on the Microsoft Store.

Even if you don't install the app yourself, Windows Update will do so, and then treat you to a McAfee pop-up. All you have to do is plug in the LG monitor to your PC, and the automatic installation of McAfee is also shown by checking the Windows Reliability Monitor, which documents a 'successful Windows update' for the LG Monitor App Installer package.

We've reached out to LG for a comment, but haven't received a response yet. In the meantime, though, there appears to be a fix that requires users to do the following: **press the Windows key and R, and type 'gpedit.msc', then hit Enter**.

From that point, navigate your way to **Computer Configuration > Administrative Templates > System > Device Installation > "Prevent automatic download of applications associated with device metadata",** then select the 'Enabled' box and apply.

 ![Windows 11 Group Policy Editor](https://cdn.mos.cms.futurecdn.net/gdv6SJAhdHd6dbF2StR3xd.png) 


In theory, this should stop any unwanted applications from being installed, specifically with devices like LG monitors that do so via device metadata.

And if you already installed the LG monitor app manually, you should remove it, because as noted, the description on the Microsoft Store suggests McAfee is a fundamental part of the monitor application.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

Bloatware can be problematic for Windows 11 users because it hogs system resources, and LG is adding to that system drain, not to mention the annoyance of continually seeing that pop-up.

Alongside LG, Microsoft hasn't provided a statement on the matter yet. I'd expect Windows 11 users will want an answer of some kind, especially because of the rather fiddly steps involved to prevent these automatic installations — and frankly, this shouldn't require extra effort from anyone.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Isaiah Williams](https://cdn.mos.cms.futurecdn.net/riqwhsJX2XLMYHR6WeadJD.jpg)

Isaiah is a Staff Writer for the Computing channel at TechRadar. He's spent over two years writing about all things tech, specifically games on PC, consoles, and handhelds. He started off at GameRant in 2022 after graduating from Birmingham City University in the same year, before writing at PC Guide which included work on deals articles, reviews, and news on PC products such as GPUs, CPUs, monitors, and more. He spends most of his time finding out about the exciting new features of upcoming GPUs, and is passionate about new game releases on PC, hoping that the ports aren't a complete mess.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

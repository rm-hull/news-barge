---
title: Microsoft blames RGB peripherals for crashing Windows 11 — RGB software is
  causing blue screens, crashes, and game freezes
source_url: https://www.tomshardware.com/software/windows/microsoft-blames-rgb-peripherals-for-crashing-windows-11-rgb-software-is-causing-blue-screens-crashes-and-game-freezes
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-22T16:36:39Z'
published: '2026-08-22T00:00:00Z'
description: The software interferes with core system files.
image: https://cdn.mos.cms.futurecdn.net/56QCjSmF38j9xBURofZTHL-2560-80.jpg
---

![A closeup of a PC build with lots of RGB lighting in an In Win PC case, this is an example of the kind of PC build you could put together if you're out of the budget realm.](https://cdn.mos.cms.futurecdn.net/56QCjSmF38j9xBURofZTHL.jpg) 

Like clockwork, it's a new month and a new OS-breaking bug has been discovered in Windows 11's latest monthly update, KB5121003. Users reported random system instability, with games freezing or outright crashing, and even BSODs in worst-case scenarios. Microsoft investigated the issue and reached a vindicating conclusion — RGB software installed on affected PCs was interfering with core system components, causing Windows 11 to become unstable.

 ![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7.jpg) 


Online multiplayer titles such as *Arc Raiders*,* Marvel Tokon: Fighting Souls*, and* The Finals* were most affected by this issue. Reports mentioned these games exhibiting a pretty classic crash pattern. They'd suddenly hang and become unresponsive, show an "EXCEPTION_ACCESS_VIOLATION" blue screen, and force your computer to restart automatically.

An official update posted on Microsoft's Windows 11 25H2 health status page says, "this issue is related to peripherals or internal device components which have RGB lighting features." The software governing these devices would install drivers or code components with file names similar to "inpoutx64" to control the RGB. When you'd launch a certain game, inpoutx64 would trigger the issue and cause a crash.

Microsoft didn't explain the underlying cause, but it's likely tied to anti-cheat not appreciating a kernel-mode driver in user space. RGB software, like other apps, should be limited to user space, but the driver it uses to interface with peripheral controllers runs in kernel space. For anti-cheat software, this is essentially an exploit waiting to happen, so it tries to block the driver to make sure it doesn't inject malicious code.

If the driver is blocked upon startup and the RGB software unknowingly tries to push a lighting change or monitor a temp sensor, for instance, it hits a wall, and Windows throws up the EXCEPTION_ACCESS_VIOLATION error. If the driver is terminated mid-use while executing assembly instructions at the Ring 0 level, it causes a critical kernel fault. Kernel space typically can't recover from unhandled errors like these, so Windows triggers a blue screen as a precaution to protect your hardware.

Microsoft says it's "presently working to understand the relationship between these RGB components and the games which trigger this issue." The company will provide more info later, but for now, you can use the Registry Editor to manually disable the driver as a temporary solution. Embark Studios, developers of *Arc Raiders* and*The Finals,* also shared this method to fix crashes for now.

This could break some RGB software functionality, but you can use universal programs like SignalRGB or OpenRGB to control your devices as long as they're supported. Their specialized drivers have strictly defined whitelists that don't scare anti-cheat software. Still, if you're facing this issue, Microsoft suggests reporting it via Feedback Hub—that's how issues like this get prioritized in the first place.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

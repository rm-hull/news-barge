---
title: Tech sleuth claims to have found the oldest GUI application that still works
  with Windows 11 — 34-year-old CDPLAYER.EXE from Windows NT in November 1992 wins
  the prize
source_url: https://www.tomshardware.com/software/windows/tech-sleuth-claims-to-have-found-the-oldest-gui-application-that-still-works-with-windows-11-cdplayer-exe-from-windows-nt-in-november-1992-wins-the-prize
source_site: Tom's Hardware
source_slug: toms-hardware
description: However, if you cheat and enable 16-bit apps in Win11, you can still
  enjoy REVERSI.EXE, as distributed with Windows 1.01 in 1985.
image: https://cdn.mos.cms.futurecdn.net/9WfJEJAx6SPbbBbEXKuZCM-1920-80.jpg
published: '2026-10-31T00:00:00Z'
scraped_at: '2026-10-31T12:19:02Z'
categories:
- Technology & Software
- Hardware
people:
- Enlyth
- Mark Tyson
- Tom
locations: []
organisations:
- CDPLAYER.EXE
- Enlyth
- FREECELL.EXE
- Google News
- Microsoft
- OS
- REVERSI.EXE
- Tom's Hardware
- Winevdm
---

![CD Player image from Microsoft and Wikipedia](https://cdn.mos.cms.futurecdn.net/9WfJEJAx6SPbbBbEXKuZCM-1920-80.jpg)

A technology enthusiast claims that the oldest GUI application that still runs on Windows 11 is CDPLAYER.EXE from November 1992. The app had to run on Microsoft’s newest consumer OS without modifications or emulation involved to be chosen as the ‘winner’ of their experiment. Blogger Enlyth expected something from the early NT era, as Windows 11 doesn’t support 16-bit apps, despite its strong backward compatibility. Finding an app that is almost 34 years old that still works with a simple double-click is a remarkable result.

At the beginning of their journey to find the oldest Windows UI app that just works on Microsoft’s newest OS, Enlyth confirmed FREECELL.EXE from February 1993 would still run without issues. This game was distributed alongside the Win32s environment, designed to allow some 32-bit applications to run on the 16-bit operating systems like Windows 3.1 and 3.11. Win32s was made available in beta in October 1992, but went mainstream in July 1993.

A tip Enlyth received via a tech forum suggested that FREECELL.EXE was a candidate for the oldest GUI app remaining compatible with Windows 11. However, the blogger wasn’t satisfied with this easy win and dug through “some early NT 3.1 pre-release versions that seemed promising.” Build 347 caught the detective’s eye, specifically CDPLAYER.EXE, linked on Nov 16, 1992. That indeed seems to be the earliest GUI app that works without modification or emulation on Windows 11. But this knowledge almost defied Enlyth’s eye as their system is, like many modern systems, optical-drive-less. Luckily, adding a small DLL (cdemu.dll) allowed Enlyth to emulate a CD drive and demonstrate that the 1992-era application still functions as intended.

I wanted to verify that CDPLAYER.EXE was still usable on the latest Windows 11 release. Unfortunately, the multi-part.ARJ archive of Windows NT 3.1 that I found on Archive.org threw up errors when I tried to pick through its contents. I have a USB-attached optical drive that plays CD audio in Windows 11, so I thought I could get CDPLAYER.EXE to run without any extra DLL.

Lastly, Enlyth wanted to push the envelope a little and see what even more ancient Windows apps might work if they got some help from the Winevdm project on 64-bit Windows. “Using otvdm does feel like cheating,” admitted the digital sleuth, and we’d agree. However, being able to run 16-bit apps in Windows 11 ratcheted back the wheels of time. The result was that Enlyth managed to enjoy “a fully playable version of REVERSI.EXE dated 15-Nov-1985.” That’s a GUI-driven game distributed as part of Windows 1.01 and is roughly 41 years old.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR-140-80.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

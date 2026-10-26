---
title: Windows 11’s ‘whole ISO’ squeezed into a CD-ROM — sub-700MB disk ‘boots to
  the desktop, runs apps’ just like the Microsoft original
source_url: https://www.tomshardware.com/software/windows/windows-11s-whole-iso-squeezed-into-a-cd-rom-sub-700mb-disk-boots-to-the-desktop-runs-apps-just-like-the-microsoft-original
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-26T20:35:58Z'
published: '2026-10-26T00:00:00Z'
description: Developer NTDEV indicates this is a teaser for the abilities of the upcoming
  Pico11.
image: https://cdn.mos.cms.futurecdn.net/RScK9KwYmyDkYGr4yWAyfK-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Science
people:
- Mark Tyson
- Tom
locations:
- GitHub
organisations:
- Get Tom's Hardware
- Google News
- ISO
- NTDEV
- Pico11
- Task Manager
- Tiny11 Core
- Tom's Hardware
---

![Pico11 demo](https://cdn.mos.cms.futurecdn.net/RScK9KwYmyDkYGr4yWAyfK-1920-80.jpg)

Professional Windows crusher NTDEV has showcased their next-generation tool for compressing Windows 11 into the tiniest of tiny installs. Based on their newest and unreleased Pico11, they managed to create a “proof of concept I put together to see how small I could make a Windows 11 ISO while keeping a working desktop and a few familiar apps.” Moreover, it’s a perfect installer to shove on a 700MB CD-ROM without wasting space, with this demo version weighing in at 699,811,840 bytes.

![I made Windows 11 fit on a CD - pico11 - YouTube](https://img.youtube.com/vi/c0wDeL_B6yI/maxresdefault.jpg)

*The test system (a VM with 4GB allocated) used around 883MB of RAM.*

In the above video, NTDEV demos a freshly installed Windows 11 ISO that had been processed with Pico11. The desktop looks familiar to anyone currently using Windows 11. “Calculator and Settings still open, Notepad saves files, and Paint still lets me draw questionable logos,” highlights the dev. However, it is also pointed out that “Task Manager might look a little older than you remember.” The older Task Manager seems to be a lightweight legacy version. It may have been possibly swiped from Windows 7, but its exact origin isn’t divulged by NTDEV.

At this time, NTDEV admits what you see is “an experiment, not a replacement for a normal Windows installation,” and that’s mainly because Windows Update and general servicing have been removed to fit inside the constraints of CDR capacity. If you are interested in creating Windows installs like this, the good news is that NTDEV says they are working on adding what they describe as Pico11 capabilities to the Tiny11 builder tool, which you can find on GitHub.

Tiny11 has already demonstrated impressive Windows 11 ISO building capabilities with its Tiny11 mode, Tiny11 Core mode, and Custom mode. Pico11 sounds most closely related to Tiny11 Core as it eschews servicing and recovery support. However, there appears to be some more under-the-hood tweaking, which may have been evidenced in this new showcase by the presence of the older version of Task Manager.

Tiny11 has historically been responsible for even smaller Windows 11 installs, but the extreme 100MB distillation of the OS, for example, came without any Windows 11 UI. Builds could also be remarkable for using tiny amounts of RAM – as little as 176MB. More typical and useful were custom builds powered by Tiny11 where 'bloatware' was removed and that weighed in at around the 2GB mark.

Hopefully we will learn more about Pico11 and get greater insight into its capabilities soon.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR-140-80.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

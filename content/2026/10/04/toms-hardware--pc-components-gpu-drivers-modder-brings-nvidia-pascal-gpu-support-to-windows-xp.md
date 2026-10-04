---
title: Modder brings spport for deade-old Nvidia Pascal GPUs to 24-year-old Windows
  XP 32-bit — modded drivers unlock better DisplayPort and HDMI support for modern
  monitors
source_url: https://www.tomshardware.com/pc-components/gpu-drivers/modder-brings-nvidia-pascal-gpu-support-to-windows-xp-32-bit-modded-drivers-unlock-better-displayport-and-hdmi-support-for-modern-monitors
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-04T17:08:32Z'
published: '2026-10-04T00:00:00Z'
description: Bringing high-performance cards to retro gaming systems.
image: https://cdn.mos.cms.futurecdn.net/JnGyAXb2x6LNKcRbUXHM4F-2048-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Bruno Ferreira
- Maxwell
- Pascal
- Tom
locations:
- Mega
organisations:
- Forceware
- GeForce GTX
- Get Tom's Hardware
- Google News
- Nvidia Control Panel
- PC
- Quadro M4000
- README
- SupraGSX
- TITAN Xp
- Tom's Hardware
---

![Nvidia Titan X anniversary edition](https://cdn.mos.cms.futurecdn.net/JnGyAXb2x6LNKcRbUXHM4F-1920-80.jpg)

One of the many appeals of retrocomputing and emulation is being able to play your old games on much better systems than you or your parents could afford at the time. Along those lines, techie SupraGSX has brought support for Nvidia's Pascal-era cards (mainly 10-series and Quadro P2000-P6000 cards) to Windows XP 32-bit, with a bevy of modern accouterments for DisplayPort and HDMI handling, too.

![Asus RTX 5080 Noctua Edition](https://cdn.mos.cms.futurecdn.net/Wh9EZgD8NG9yUioNNgPB3d-1200-80.png)

The new ForceWare 382.69 (custom numbering) is a spin-off of the existing 368.81 driver, seemingly Nvidia's last Windows XP release that supported 9-series GPUs. The software also pulls card firmware from Quadro 376.84 drivers, and support for Video Protected Region from Windows 7 GeForce 378.78. Although some websites mention that this project was vibe-coded, the repository doesn't mention it, and a cursory look at the build instructions didn't reveal any obvious traces of clanker activity.

Here's the full list of supported cards, taken from the code repository. The one notable omission is GT 1030, based on the GP108 chip. The rest of the lineup is fairly complete, and there's even an experimental build that supports the 1050 Ti. Since the author is releasing new versions as we speak, it's worth checking the project's README for updated information.

* GeForce GTX 970, 980, 980 Ti; GTX TITAN X (Maxwell).
* GeForce GTX 1060 (3/5/6 GB), 1070, 1070 Ti, 1080, 1080 Ti; TITAN X (Pascal), TITAN Xp.
* GeForce GTX 1050 Ti (experimental support)
* Quadro M4000, M5000, M6000, M6000 24GB; P2000, P2200, P4000, P5000, P6000.
* Additional desktop OEM variants of GTX 950 and GTX 960.

Because contemporary displays with high refresh rates and resolutions can be tricky, SupraGSX added DisplayPort HBR2 and HBR3 support (High Bit Rate), HDMI 2.0 identification and mode-retry fail-safes, HDMI/DVI handling, and improved scaling and aspect ratio settings in the Nvidia Control Panel.

Some folks have tested the new driver, and it appears to work mostly fine, with reports of it working well with ultrawide screens at high refresh rates. SupraGSX is active in the Vogons forums, where it seems to take bug reports and feature requests.

If you're interested in revitalizing your retro system with Forceware, you can go to the project's releases section and download the installer package. Enterprising modders can review the extensive build instructions and perhaps roll their own mods.

Since many retro-tinkerers may be asking for Windows XP 64-bit support, a fork of the Forceware driver existed, but it's since been deleted. However, its binaries live on at Mega. Since these are all unofficial drivers, always exercise caution and don't install them on systems where you're concerned about data safety.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

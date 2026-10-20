---
title: Windows 98 SE users get a Thunderbolt 4 driver, thanks to AI assistance — vibe-coded
  xHCI98 driver works in Microsoft OSes up to Windows 7
source_url: https://www.tomshardware.com/peripherals/thunderbolt/windows-98-se-users-get-a-thunderbolt-4-driver-thanks-to-ai-assistance-vibe-coded-xhci98-driver-works-in-microsoft-oses-up-to-windows-7
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-20T14:25:31Z'
published: '2026-10-20T00:00:00Z'
description: If you've ever wanted to run Windows 98 SE on your mid-2010s or newer
  PC with fast USB hub support, here's your chance.
image: https://cdn.mos.cms.futurecdn.net/NoWyHSrvf9AM6sJicvFink-1920-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Claude Fable
- Claude Opus
- Mark Tyson
- Tom
- Yeo Kheng Meng
locations: []
organisations:
- AI
- Astra
- BIOS
- Comet Lake xHCI
- EHCI
- Get Tom's Hardware
- GitHub
- Google News
- Intel
- ME
- Thunderbolt
- Tom's Hardware
- Windows
---

![Windows 98 users get Thunderbolt 4 driver ](https://cdn.mos.cms.futurecdn.net/NoWyHSrvf9AM6sJicvFink-1920-80.jpg)

Windows 98 SE devotees can now enjoy (experimental) support for USB4 and Thunderbolt 3/4. Developer and maker Yeo Kheng Meng, who also enjoys retrocomputing, recently released the vibe-coded xHCI98 v3.0.0.0, enabling the practical use of generic USB 3.x, USB4, and Thunderbolt 3/4 host controllers on systems running Windows 98 SE, ME, 2000, XP, Vista, and 7. An extensive blog post by the dev provides further reading about the driver, compatibility, its creation, and usage.

![xHCI98: xHCI host controller driver for Win 98/ME/2K/XP/Vista/7 Demo - YouTube](https://img.youtube.com/vi/AU77f9CSbYc/maxresdefault.jpg)

*Demo video “shows many different USB devices being hotplugged to a modern 2020 ThinkPad P14s Gen 1 with only xHCI controller.”*

Some of you will be wondering why a project to bring USB4 (Thunderbolt 3 and 4) to PCs running Windows 98 SE exists. Retro computing fan Meng explains on his GitHub that this project should appeal directly to users of PCs from the mid-2010s that have xHCI-only (USB 3.x) chipsets and no legacy EHCI controller. However, older OSes don’t have xHCI drivers, and that’s where xHCI98 steps in. “Without xHCI support, even keyboards, mice, and flash drives need the BIOS's legacy support, cannot be hotplugged, and devices such as Ethernet and audio do not work at all,” explains Meng, revealing his motivation. “This project fills that gap.”

Impressively, xHCI98 drives a lot more than USB storage. It replaces Windows’ own USB port and hub drivers to facilitate the connection and use of USB 1.1 and 2.0 and SuperSpeed (USB 3.x) devices and hubs, UAS (USB Attached SCSI) storage through a second driver (xhciuas.sys), and Thunderbolt 3 and USB4 docks and NVMe enclosures through a third driver (xhcicm.sys).

Meng has developed and tested xHCI98 mostly on Intel hardware, as that is what he owns. Candidly, he admits “this is a solo human's project with AI assistance, so bugs are not unexpected,” even if you do have the same hardware as the dev - a 2020 ThinkPad P14s Gen 1 (Comet Lake xHCI, no EHCI). It stands up pretty well during the plug/unplug video demo above, though the test rig used is not quite the USB cart of death.

![Windows 98 users get Thunderbolt 4 driver](https://cdn.mos.cms.futurecdn.net/LQvFMzX73nYG7JMPE7a2nk-1200-80.jpg)

As a solo developer, Meng isn't shy to admit he leaned heavily on AI assistance to prepare the xHCI98 release. His vibe coding adventure was supported by Claude Fable 5.1 for planning, Claude Opus 5.5 for coding, and Codex GPT 6 Astra as an adversarial reviewer.

In addition to a few bug warnings, there are some other things to know about using this driver with the various older versions of Windows it supports, standby and hibernation, and more. The dev helpfully sketches out a process for checking your hardware, outlines various install methods, discusses updating, and talks about tuning the driver for those who will be jumping in at the deep end with this project.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR-140-80.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

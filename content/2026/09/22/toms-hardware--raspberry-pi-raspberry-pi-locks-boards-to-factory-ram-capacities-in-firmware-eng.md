---
title: Raspberry Pi locks boards to factory RAM capacities in firmware — engineer
  tells DIY modders 'don't waste your time' trying repairs or upgrades, company cites
  shady reseller scams
source_url: https://www.tomshardware.com/raspberry-pi/raspberry-pi-locks-boards-to-factory-ram-capacities-in-firmware-engineer-tells-diy-modders-dont-waste-your-time-trying-repairs-or-upgrades-company-cites-shady-reseller-scams
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-22T13:23:04Z'
published: '2026-09-22T00:00:00Z'
description: SBC supremo blames firms buying cheaper Pis then swapping RAM with ICs
  ‘of dubious origin’ for this change.
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
image: https://cdn.mos.cms.futurecdn.net/FStqSpBaECihHvHVYQqdaW-2560-80.jpg
locations: []
people:
- Jeff Geerling
- Mark Tyson
- PhilE
- RAM MacGyvers
- Tom
organisations:
- AI
- Google News
- RAM IC
- Raspberry Pi
- Raspberry Pi Engineer & Forum Moderator PhilE
- Tom's Hardware
---

![Raspberry Pi 500+](https://cdn.mos.cms.futurecdn.net/FStqSpBaECihHvHVYQqdaW.jpg)

Raspberry Pi users are effectively being blocked from swapping the RAM chips on their SBCs for repairs or upgrades. In a reply on the firm’s forums, Raspberry Pi Engineer & Forum Moderator PhilE told users that the company has been “locking devices to their original RAM size” for some time. This decision was made for the sake of device reliability, says the rep. However, the move seems to go against the grain for a company so involved in the maker, DIY, and tinkerer side of computing.

PhilE explains the problem that faced Raspberry Pi and some users, airing the company’s side of the argument. “If labor is cheap enough then there may be a minor financial gain in buying a part with say a 2GB part, swapping it for an 8GB part of dubious origin, and reselling it as an 8GB device,” says the forum mod. “However, this brings an element of risk to the user - the board hasn't been tested by us - and is a potential support burden for us, with customers complaining of unreliable devices. We therefore remove the commercial incentive by locking devices to their original RAM size.”

In addition, the Pi’s firmware currently “program in some other device attributes, meaning that switching parts of the same size may not work,” says PhilE. This isn’t great for genuine users who might want to tinker with or upgrade the RAM chips or have to replace an IC for repair. The forum mod underlines the effective block by telling would-be RAM MacGyvers to “don't waste your time trying - it won't work.”

Some readers might feel sympathetic towards Raspberry Pi’s RAM tinkering blockade, given PhilE’s reasoned explanation. One surprising aspect of the decision, though, is that the firmware locks of RAM IC swaps began to roll out in updates from late 2024 onwards. So, this change was made well before the crazy RAM chip pricing upswing precipitated by the AI data center boom. Also, it means that if you want to sidestep this RAM tinkering block, you would need to grab and flash a pretty old firmware to your Pi model (if available).

Naturally, the Pi community isn’t celebrating this RAM upgrade/repair block. Some high-profile Pi advocates like Jeff Geerling suggest that implementing a ‘warranty bit’ (similar to older models), or a one-time firmware flag to void support for modified boards, would have been a more agreeable path for Raspberry Pi to take. Here’s a lookup table that you can use to check your Pi’s factory RAM configuration.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

* * It would be great if this otherwise open source device didn't have a closed-source proprietary firmware bootloader. It's entirely likely that the Pi's processor has an undocumented hypervisor and backdoor. I don't definitively know this to be the case, that does seem to be the direction the entire chip industry is moving towards.Reply

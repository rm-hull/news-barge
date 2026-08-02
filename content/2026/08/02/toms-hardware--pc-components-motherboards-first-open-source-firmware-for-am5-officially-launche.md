---
title: First open-source firmware for AM5 officially launches — Dasharo v0.9.0 brings
  Coreboot and openSIL to Zen 4 APUs on MSI B850
source_url: https://www.tomshardware.com/pc-components/motherboards/first-open-source-firmware-for-am5-officially-launches-dasharo-v0-9-0-brings-coreboot-and-opensil-to-zen-4-apus-on-msi-b850
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-02T13:49:21Z'
published: '2026-08-02T00:00:00Z'
description: 3mdeb is the first company to make open-source firmware for the AM5 platform.
image: https://cdn.mos.cms.futurecdn.net/8HRHpufeQP8XBVXitxXV9H-2560-80.jpg
---

![Zen 4 CPU](https://cdn.mos.cms.futurecdn.net/8HRHpufeQP8XBVXitxXV9H.jpg) 

Firmware development company 3mdeb has officially launched the first open-source UEFI firmware for AMD's AM5 platform. In a blog post, the company announced Dasharo v0.9.0, featuring initial support for Zen 4 Phoenix APUs and MSI's Pro B850-P WiFi motherboard. The firmware is built on Coreboot and AMD's openSIL, the latter being AMD’s new open-source firmware framework.

The patch notes are comprised of 19 features to make the open-source code work on the B850 board, including the following: a UEFI-compatible boot interface, UEFI Secure Boot support, fTPM support, fast boot support, EFI system partition scanning, quiet boot and fast boot support, AMD CPU temperature reporting, and integrated SBOM.

Development of this open-source firmware for the MSI Pro B850-P has been an ongoing process over the past several months. We initially saw development announced in February, after 3mdeb developed an open-source firmware for the Gigabyte MZ33-AR1, a server board compatible with AMD EPYC 9005 series CPUs. Development of the open-source firmware version for the MSI Pro B850-P is based on the work done for the MZ33-AR1.

Dasharo is the first development team to produce open-source firmware for AMD's mainstream consumer AM5 platform. AMD is already looking to switch from AGESA to openSIL starting with Zen 6, but 3mdeb has opted to port AMD's openSIL firmware to older Ryzen CPUs.

Open-source firmware represents a big improvement over existing closed-source firmware solutions, particularly AGESA. AMD touts its openSIL firmware as being more secure than AGESA, with better platform security and better vulnerability tracking thanks to its open-source nature. Going open-source opens up room for experts and developers beyond AMD's own firmware development team to check for vulnerabilities in firmware code.

Another benefit of openSIL is that it is compatible with alternative firmware beyond UEFI, including Coreboot, oreboot, FortiBIOS, and Project µ. Projects like Coreboot also provide optimized code compared to closed-source firmwares, improving boot-time performance.

The new firmware can be found on the 3mdeb shop, under the MSI Pro B850-P hardware-firmware bundle.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Aaron Klotz](https://cdn.mos.cms.futurecdn.net/aAk2saHqkgFuTCanz8LnmD.jpg)

Aaron Klotz is a contributing writer for Tom’s Hardware, covering news related to computer hardware such as CPUs, and graphics cards.

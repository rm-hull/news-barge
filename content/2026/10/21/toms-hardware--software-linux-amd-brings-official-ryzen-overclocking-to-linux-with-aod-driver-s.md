---
title: AMD brings official Ryzen overclocking to Linux with AOD driver support — no
  official app, but third-party options should arrive soon
source_url: https://www.tomshardware.com/software/linux/amd-brings-official-ryzen-overclocking-to-linux-with-aod-driver-support-no-official-app-but-third-party-options-should-arrive-soon
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-21T17:13:10Z'
published: '2026-10-21T00:00:00Z'
description: This is a major milestone for improving the DIY tuning experience on
  Linux.
image: https://cdn.mos.cms.futurecdn.net/mGp7GR969s7dxH5AbGf8mg-1920-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Tom
- Zak Killian
locations: []
organisations:
- AMD
- AOD
- CPU
- CoreCtrl
- Google News
- HotHardware
- PC
- Phoronix
- Ryzen Master
- The Tech Report
- Tom's Hardware
- UEFI
- Zak
---

![An AMD Ryzen CPU 3D render overlaid by a Tux the Linux Penguin mascot vector image.](https://cdn.mos.cms.futurecdn.net/mGp7GR969s7dxH5AbGf8mg-1920-80.jpg)

While Windows overclockers have spent years lazily sliding UI controls to adjust frequency curves and tweak voltages inside Ryzen Master, Linux users have largely had to treat their CPU tuning like an archaeological dig into the opaque veil of UEFI/BIOS firmware. Well, rejoice, Linux users, as AMD has officially published a fresh set of patches for the Linux kernel introducing AOD (AMD Overclocking Driver) support for Ryzen processors, *Phoronix* reports.

Instead of forcing developers to reverse-engineer closed-source firmware hooks or rely on messy, machine-specific ACPI workarounds, this new kernel driver is a direct pipeline to AMD's platform adjustments. By exposing core tuning capabilities straight through the standard sysfs interface, AMD is laying down an official, upstreamed foundation for software-level CPU management.

Right out of the gate, the driver handles platform-level SMT toggling, memory clock visibility, and power tunables. That's right: you can now toggle Simultaneous Multithreading (SMT) dynamically through this driver interface. That works through the CPU hotplugging mechanism and acts as a clean alternative to passing the old 'nosmt' boot parameter to the kernel. The new driver also allows real-time monitoring of memory clocks, and initial power controls are being wired up, too.

![A screenshot of AMD&#039;s Ryzen Master CPU tuning tool.](https://cdn.mos.cms.futurecdn.net/WKupAJJrrNXwRmbmpDhYy4-1200-80.png)

Now, if you're expecting a polished, one-click official AMD application equivalent to Ryzen Master for Linux, just pump the brakes. AMD is following its open-source amdgpu graphics driver playbook here, building the kernel plumbing and then leaving the user-space presentation layer entirely up to the community. That means you're going to have to wait for utilities like CoreCtrl to build out interfaces for this new driver, but it shouldn't be long now before that work gets underway in earnest.

This approach is arguably a better fit for the Linux philosophy anyway. Because the controls are being exposed via clean kernel sysfs nodes, it won't be long before independent developers integrate these knobs into powerhouse open-source monitoring and tuning suites, or even write dedicated desktop environment extensions specifically for the purpose of tweaking Ryzen processors.

The new patches are currently winding their way through review on the mailing lists, meaning mainstream kernel integration is on the horizon. For a DIY enthusiast who loves squeezing every last MHz out of silicon while maintaining a fully open-source software stack, this is easily the most exciting hardware-enablement milestone I've seen in a long time.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi-140-80.jpg)

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

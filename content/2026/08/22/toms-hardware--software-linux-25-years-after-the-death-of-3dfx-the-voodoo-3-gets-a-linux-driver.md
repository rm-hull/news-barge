---
title: 25 years after the death of 3dfx, the Voodoo 3 gets a Linux driver update —
  classic Voodoo GPUs can now boot without a PC BIOS
source_url: https://www.tomshardware.com/software/linux/25-years-after-the-death-of-3dfx-the-voodoo-3-gets-a-linux-driver-update-classic-voodoo-gpus-can-now-boot-without-a-pc-bios
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-22T16:36:31Z'
published: '2026-08-22T00:00:00Z'
description: It's been a quarter-century since the firm folded, but the graphics chips
  still have utility in esoteric use cases.
image: https://cdn.mos.cms.futurecdn.net/X6iB5cWC9stabSJtgczKnd-1280-80.jpg
---

![Marketing image for the Voodoo 3 graphics card](https://cdn.mos.cms.futurecdn.net/X6iB5cWC9stabSJtgczKnd.jpg) 

Linux kernel 7.3 is set to bring an oddly nostalgic update for 3dfx's Voodoo 3, one of the most recognizable graphics cards of the late 1990s. Don't get too excited; the venerable PCI-and-AGP accelerator isn't suddenly getting a modern Linux graphics stack, but the kernel's existing tdfxfb framebuffer driver is being updated so that it can initialize a Voodoo 3 itself rather than relying on the system firmware to have already run the card's video BIOS. It's a small change with a surprisingly specific purpose, and one that illustrates why ancient hardware occasionally gets attention in contemporary Linux.

 ![Asus RTX 5080 Noctua Edition](https://cdn.mos.cms.futurecdn.net/Wh9EZgD8NG9yUioNNgPB3d.png) 


The problem is that the tdfxfb driver historically assumed that the Voodoo card had already been initialized by the PC's firmware. That's because, at the time it was written, that was a reasonable assumption on a conventional x86 PC. The system firmware would execute the card's video BIOS during boot, configure the hardware, and then hand Linux something that is already capable of displaying an image. That assumption breaks down on newer and unusual platforms where the firmware cannot or does not execute the VGABIOS. The creator's patch description specifically calls out non-x86 computers, systems where another graphics card is primary, and newer BIOSes that can't run the old video BIOS.

The developer behind the patches, Daniel Palmer, was using a Voodoo 3 in an Amiga 4000 equipped with a PCI bridge when the problem cropped up. Linux could detect the card, but the Voodoo was still completely uninitialized, leaving him staring at "no signal detected." The new code uses configuration information from the card's own video BIOS to perform the initialization from Linux instead, allowing the driver to bring the VGA core up and establish a working display without depending on the system firmware. For now, the new manual initialization code is specifically aimed at the Voodoo 3; he had initially noted support for the VSA-100-based Voodoo 4 and 5 cards, but their BIOS layouts are different, so that support was removed from the current patch series. The code has been tested on both a modern x86-64 system and an Amiga 4000 with a Mediator PCI bridge.

 ![A photograph of an Amiga 4000 with its external case removed.](https://cdn.mos.cms.futurecdn.net/BReyoJk8JpNoSXNNKqJAfF.jpg) 


On a conventional modern-ish x86-64 PC with a Voodoo 3 installed, the practical result is fairly modest. Load tdfxfb and you can get a working Linux framebuffer device, typically exposed as /dev/fb0, with the Voodoo driving a display that can host the Linux virtual console. In other words, this is enough to turn the Voodoo from "a PCI device that Linux can identify" into an actual display adapter capable of putting pixels on the screen even when firmware didn't initialize it first. Applications that know how to use the Linux framebuffer interface can also draw to it, just as they could with other old framebuffer devices.

The thing is, that's also where the limits of this work become apparent. Linux fbdev is a legacy graphics interface and has long been superseded by Linux's DRM/KMS graphics infrastructure, so this ain't a resurrection of the Voodoo 3 as a contemporary Linux GPU. Loading tdfxfb does not give you a Mesa stack, modern OpenGL, Wayland acceleration, or the sort of 3D functionality you would expect. It is essentially a very old-fashioned "squirt pixels at the display" arrangement, but that's useful enough for a Linux console, embedded-style framebuffer applications, and, apparently, people putting exotic PCI graphics cards into even more exotic old computers, but it's not exactly a compelling reason to install a Voodoo 3 in a modern desktop.

The more interesting part is that Palmer is working on a separate 3D path for the Voodoo 3, and that effort is already much further along than the framebuffer work alone might suggest. The experimental interface exposes the Voodoo's register space to userspace through a new /dev/tdfx3d misc device, whose mmap() interface allows software to program the card's 3D hardware directly. On top of that sits smoltdfx, a tiny userspace library for driving the Voodoo 3, and smolminigl, a small OpenGL 1.x implementation built on top of it. Palmer says he has tested the project on real Voodoo 3 hardware and that it can render directly through the card's registers without X, Mesa, or Glide.

 ![A screenshot of Quake's E1M6, The Door to Cthon.](https://cdn.mos.cms.futurecdn.net/G6CagAwqoTv5sFQuP9NXWR.jpg) 


*GLQuake* was the killer app for the original 3dfx Voodoo Graphics cards in 1996. (Image credit: Zak Killian/Future)

Palmer is developing that work alongside a QEMU emulation of the Voodoo 3. The developer says Claude helped build the emulator in the first place to debug the issue of getting the card working on his Amiga. Now, test programs can be run against both the emulated card and the real hardware, with differences fed back into the emulator until the behavior matches. The smoltdfx project now uses the same rendering tests against QEMU and physical Voodoo 3 hardware, comparing frame digests to catch differences. According to Palmer, the resulting MiniGL implementation can already run *Quake* on the real card, although performance isn't great, and some issues with the Voodoo 3's multitexturing capabilities remain to be worked out.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Obviously, that's a lot more interesting than simply putting a Linux console on a Voodoo 3. The sum total is a highly experimental 3dfx graphics stack built from the bottom up: Linux provides the framebuffer and low-level device access, userspace programs the Voodoo directly, and a lightweight OpenGL implementation sits above that to provide enough functionality for classic 3D software to command the card.

 ![A photograph of a 3dfx Voodoo 3 3000 PCI graphics card.](https://cdn.mos.cms.futurecdn.net/RY4rUDcGeTqzY96ZNe9EKk.jpg) 


Indeed, things could get particularly fun for retro-computing and virtualization. A PCI Voodoo 3 is the sort of device that, at least conceptually, could be assigned to a virtual machine using PCI passthrough, letting a guest operating system talk directly to the real accelerator with its period-accurate 3dfx driver. In the fantasy version of that setup, you could have a modern Linux host hand an actual Voodoo 3 to a Windows 98 or DOS-era guest and then let the guest use the very same hardware that the old software expected. The engineering details are much nastier than the concept suggests (particularly around resetting and exposing such old hardware cleanly), but the new ability to initialize an otherwise-dormant Voodoo from Linux is at least a useful piece of that puzzle.

For now, though, the headline is more significant than the immediate feature set. Linux 7.3 isn't suddenly turning a 25-year-old Voodoo 3 into a usable GPU; it's making an existing framebuffer driver capable of bringing the card to life on systems where firmware cannot do the job, which is a very small but very real hole in hardware support. More remarkably, the same effort has already spilled into experimental 3D acceleration on real hardware, with a userspace Voodoo 3 library and an OpenGL implementation capable of running Quake. Voodoo 3 may be over 25 years old by now, but somebody is still teaching Linux new tricks with it in 2026.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi.jpg)

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

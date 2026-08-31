---
title: Nvidia's latest driver update breaks mVolt+ overclocking functionality — Nifty,
  open-source app allowed users to increase the power limit to 700W on their RTX 50-series
  GPUs without hardware mods
source_url: https://www.tomshardware.com/pc-components/gpu-drivers/nvidias-latest-driver-update-breaks-mvolt-overclocking-functionality-nifty-open-source-app-allowed-users-to-increase-the-power-limit-to-700w-on-their-rtx-50-series-gpus-without-hardware-mods
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-31T16:08:26Z'
published: '2026-08-31T00:00:00Z'
description: Using the app results in a driver crash.
image: https://cdn.mos.cms.futurecdn.net/Axh3XNQ6DqK4KMfxtoMRBU-2560-80.jpg
---

![Nvidia GeForce RTX 5090](https://cdn.mos.cms.futurecdn.net/Axh3XNQ6DqK4KMfxtoMRBU.jpg) 

Nvidia's current-gen Blackwell family includes some of the best graphics cards on the market with exceptional performance, but pushing silicon to its limit can always unlock more power. This is where enthusiast software, such as mVolt+, comes in, allowing users to overclock their GPUs beyond what's usually permissible. Unfortunately, it seems like a new driver update has shut down mVolt+ across all RTX 50-series cards.

the latest nvidia driver (615.56) blocks the core power limit settings (which should be the nvvdd overcurrent limit btw) introduced in mvolt+ v0.36.it now blacks out as if the driver has crashed or been disabled, regardless of how much extra current you apply.on the other… [https://t.co/HQb4IEhZQT](https://t.co/HQb4IEhZQT) pic.twitter.com/cBogOJTb5pAugust 28, 2026


Unlike mainstream GPU utilities like MSI Afterburner, mVolt+ bypasses standard driver restrictions and gives you more granular control over a few hardware blocks. The app can tweak separate power targets for the core and memory channels. It can also provide access to voltage and clock offsets for Core, XBAR, SYS, and VRAM. You can manually tune the power across the interconnect and video encoders, for instance, instead of relying on a global slider.

As such, users have been able to nudge their hardware into territory usually only charted by relying on a specialized VBIOS or physically modding the PCB. Last week, an Asus ROG Astra RTX 5080 reached 680W using mVolt+ despite even the official OC BIOS only permitting a 450W TDP. Someone with an RTX 5090 saw their GPU draw 650-700W of power while gaming, compared to 450W it used to suck up previously.

Even though the performance gains were marginal in real-world usage, mVolt+ was still a useful tool for overclocking. It allowed enthusiasts to chart on 3DMark's worldwide rankings just through software, so the fact it has suddenly stopped working is quite disappointing. The latest driver, version 615.56, seems to be blocking the app from making changes, hard crashing anytime you try to adjust the core power limit.

It's unclear if this is an intentional move from Nvidia, or just a compatibility issue that's preventing mVolt+ from properly working on the latest drivers. Some users on the Overclock.net RTX 5090 thread say their GPUs are still able to accept power limit modifications through Hydra 2.3B Pro — another extreme overclocking utility. That suggests mVolt+ wasn't explicitly blocked, and that its creator *b00nz* can push an update to patch this driver conflict soon.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

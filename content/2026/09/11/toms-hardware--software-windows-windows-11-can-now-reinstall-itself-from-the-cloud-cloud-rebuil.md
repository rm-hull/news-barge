---
title: Windows 11 can now reinstall itself from the cloud — Cloud Rebuild revives
  dead systems without secondary boot media, wipes broken installation and downloads
  a fresh copy of the OS
source_url: https://www.tomshardware.com/software/windows/windows-11-can-now-reinstall-itself-from-the-cloud-cloud-rebuild-revives-dead-systems-without-secondary-boot-media-wipes-broken-installation-and-downloads-a-fresh-copy-of-the-os
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-11T12:49:39Z'
published: '2026-09-11T00:00:00Z'
description: Windows recovery gets easier.
image: https://cdn.mos.cms.futurecdn.net/j5zs5ecSDHaXsQ5BGtwxvN-1920-80.jpg
---

![Framework Laptop 13 Pro](https://cdn.mos.cms.futurecdn.net/j5zs5ecSDHaXsQ5BGtwxvN.jpg) 

Microsoft has finally solved one of the biggest pain points of Windows with the rollout of Cloud Rebuild. The new recovery feature can reinstall Windows 11 even when an existing Windows installation is corrupt or refuses to boot. Available as a beta through the newly released Windows 11 Insider Beta Preview Build 26220.9343, the feature is essentially a hassle-free alternative to creating a Windows installation USB drive when a PC needs to be recovered.

According to Microsoft, Cloud Rebuild is designed to restore a Windows 11 PC to a “clean, known-good state” by downloading a fresh image of Windows along with the required drivers directly through Windows Update. Unlike the existing Reset this PC functionality, it does not depend on the health of your existing Windows installation, nor does it require users to have a USB drive or custom recovery image available.

 ![The Cloud rebuild feature available in Windows Recovery](https://cdn.mos.cms.futurecdn.net/4i3Jm4DUZ2QCzYVhztXabM.png) 


Available via the Windows Recovery Environment (WinRE), users can access it by selecting Troubleshoot > Recovery and uninstall > Cloud rebuild from WinRE. Speaking of which, Microsoft has also improved networking support in WinRE. The recovery environment can now reuse eligible Wi-Fi profiles saved within an existing Windows installation, allowing a PC to connect during recovery without requiring administrators to separately configure Wi-Fi credentials in WinRE. Once the PC is connected, Cloud Rebuild checks Windows Update for the target Windows build and downloads the required files. Users can then confirm the Windows edition, language, and build before starting the reinstall.

The only catch here is that Cloud Rebuild completely wipes the system drive, meaning that the process removes all data stored in your main installation or C: drive, including locally stored files, accounts, applications, and settings, before reinstalling Windows. Thus, it is recommended to back up all your important files either locally or using a cloud-based service before starting the process. Once the installation is complete, the PC boots into the Windows out-of-box experience, similar to a fresh installation of Windows. For admin-managed PCs using Windows Autopilot and Microsoft Intune, the system can automatically reconnect to the organization's management infrastructure and restore assigned applications, policies, and backed-up settings.

Cloud Rebuild could particularly be useful when Windows becomes too corrupted to boot normally. Instead of finding another PC, creating installation media, and manually reinstalling Windows, users can potentially perform the entire recovery process directly from WinRE. The feature is still in preview; however, we can expect a wider release later this year.

*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

  


Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Kunal Khullar](https://cdn.mos.cms.futurecdn.net/NDK3ae3zDxAx2BJnMXxBJV.jpg) 

Kunal Khullar is a contributing writer at Tom’s Hardware. He is a long time technology journalist and reviewer specializing in PC components and peripherals, and welcomes any and every question around building a PC.

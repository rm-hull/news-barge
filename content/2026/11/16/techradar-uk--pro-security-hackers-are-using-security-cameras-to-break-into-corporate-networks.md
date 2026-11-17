---
title: Hackers breached 13 organizations in days using exposed GeoVision webcams
source_url: https://www.techradar.com/pro/security/hackers-are-using-security-cameras-to-break-into-corporate-networks-then-switching-off-the-antivirus-to-mine-crypto
source_site: TechRadar UK
source_slug: techradar-uk
description: Exposed security cameras are letting hackers break into Windows networks,
  kill Microsoft Defender, and secretly mine cryptocurrency
image: https://cdn.mos.cms.futurecdn.net/yf4vqPknb8WxxxzfBvhVjZ-1920-80.jpg
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-17T03:46:29Z'
categories:
- Technology & Software
people:
- Huntress
locations:
- Golang
organisations:
- BitTorrent Mainline
- GeoStartupAgentService.exe
- Huntress
- Microsoft Defender
- PackageUpdater
- PackageUpdater\_Startup
- TechRadar Pro
- Windows Security
- XMRig
---

![Hackers using AI](https://cdn.mos.cms.futurecdn.net/yf4vqPknb8WxxxzfBvhVjZ-1920-80.jpg)

* **Hackers exploited exposed GeoVision surveillance systems to gain access to corporate networks**
* **Attackers manipulated Windows settings to interfere with Microsoft Defender protections**
* **Compromised computers were turned into cryptocurrency mining machines using XMRig**

Hackers have exploited internet-accessible surveillance systems to infiltrate corporate networks, disable security protections, and install cryptocurrency mining software on compromised computers.

The attacks abused GeoVision webcam software, allowing intruders to execute malicious commands through exposed services and gain control over affected Windows machines.

Cybersecurity researchers at Huntress identified the activity across 13 organizations, with infections affecting ten accounts between November 8 and November 10 2026.

## Exposed surveillance systems provide an entry point for attackers

The investigation found that attackers exploited publicly accessible GeoVision devices and management interfaces to gain access to connected organizational networks.

Once inside, malicious commands originating from GeoStartupAgentService.exe launched Windows command shells that subsequently executed downloaded PowerShell scripts.

These scripts examined infected computers, checked whether Microsoft Defender was running, and searched for writable directories before introducing additional malicious components.

One downloaded component, kvckiller.sys, was identified as a vulnerable Windows kernel driver previously abused to interfere with antivirus protections.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The attackers also manipulated Windows Registry settings to prevent essential security applications from launching through their normal executable files.

Three Microsoft Defender and Windows Security components were affected, including MsMpEng.exe, SecurityHealthService.exe, and SecurityHealthSystray.exe.

The changes redirected attempts to launch these applications toward systray.exe, potentially preventing their intended security functions from operating normally.

This gave the intruders another opportunity to maintain access while reducing the likelihood that conventional antivirus protections would detect malicious activity.

Huntress also discovered that attackers used scheduled tasks to ensure their malicious programs continued running after initial execution or system restarts.

One task, PackageUpdater, instructed Windows to execute a malicious program called update.exe every 15 minutes, restoring it whenever necessary.

Another scheduled task, PackageUpdater\_Startup, was configured to launch the same program automatically whenever an affected computer started.

## XMRig turns compromised computers into cryptocurrency mining machines

After disabling security protections, the attackers deployed XMRig, an open-source cryptocurrency mining program, through a custom loader written in Golang.

The malicious loader, named update.exe, downloaded another executable called ApplyUpdate.exe, which contained the cryptocurrency mining software.

XMRig uses computer processing resources to perform cryptocurrency mining operations, allowing attackers to generate revenue using machines belonging to unsuspecting organizations.

The loader also incorporated BitTorrent Mainline Distributed Hash Table technology and a PKARR resolver to locate its command infrastructure.

This arrangement allowed the operators to discover changing server addresses without depending entirely on conventional domain registration and fixed infrastructure.

Huntress identified several indicators associated with the campaign, including suspicious connections involving WebCamServer.exe and unusual DNS requests from compromised systems.

Investigators also identified malicious infrastructure associated with the activity, including the domain cctv-update.top and several IP addresses used during different attack stages.

The researchers advised organizations to examine GeoVision installations for unexpected command shells, PowerShell activity, and suspicious scheduled tasks.

They also recommended removing unnecessary public access to surveillance equipment, using VPN connections, and restricting management interfaces to trusted addresses.

For organizations running these systems, keeping camera management software outside unrestricted internet access could reduce opportunities for attackers to exploit exposed services.

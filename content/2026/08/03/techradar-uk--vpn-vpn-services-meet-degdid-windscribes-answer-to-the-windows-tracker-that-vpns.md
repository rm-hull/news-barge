---
title: 'Meet deGDID: Windscribe''s answer to the Windows tracker that VPNs cannot
  mask'
source_url: https://www.techradar.com/vpn/vpn-services/meet-degdid-windscribes-answer-to-the-windows-tracker-that-vpns-cannot-mask
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-03T15:11:50Z'
published: '2026-08-03T00:00:00Z'
description: Microsoft's Global Device Identifier links your machine across sessions
  and IP addresses, and Windscribe's free deGDID tool tries to break the chain
image: https://cdn.mos.cms.futurecdn.net/dTPDs7MHgjoQE9rXcB8uzE-2560-80.jpg
---

![Windscribe VPN on Samsung Galaxy S24 Ultra](https://cdn.mos.cms.futurecdn.net/dTPDs7MHgjoQE9rXcB8uzE.jpg) 

- **Windscribe has released deGDID, a free tool that targets a hidden Windows identifier that VPNs cannot mask**
- **The identifier surfaced in a US court case where it helped trace a suspect's PC across VPNs and three countries**
- **Blocking the identifier can break Microsoft account features like Xbox, Outlook, and the Store**

Windscribe has built a new tool that takes aim at a form of Windows tracking that even the best VPN cannot switch off.

The tool, called deGDID, targets a little-known Microsoft identifier called the Global Device Identifier, or GDID. It is a server-assigned code tied to a Windows installation.

The GDID burst into public view in July after it appeared in a US federal complaint against an alleged member of the Scattered Spider hacking group, where Microsoft gave investigators logs that correlated a Windows GDID with IP activity. Investigators traced the machine through VPN obfuscation across multiple countries over roughly eight months.

![Windscribe: Windscribe:](https://cdn.mos.cms.futurecdn.net/uDFVMwFvv5PRJATMXmEfqk-200-80.jpg.webp)

**Windscribe:** a feature-packed VPN

Windscribe is fast, capable, and stacked with features. While the provider offers one of the best free VPNs around, Windscribe Premium gives you access to the full server network across 115 locations and extra features, including threat protection and port forwarding. If you find that you're unhappy with the product, you can get your money back within a week of signing up. 

## What Microsoft's GDID is, and why a VPN won't help

A Microsoft representative described the GDID in the complaint as a persistent, device-level identifier designed to uniquely identify an installation of Windows on a device.

It survives Windows updates but not a clean reinstall, which generates a fresh one. The privacy risk appears when that stable ID is tied to telemetry, Edge browsing data, Microsoft Store records, and IP addresses, letting Microsoft reconnect the same machine across sessions and services.

A virtual private network (VPN) protects your traffic by masking your IP address and encrypting your data. The GDID sits outside that tunnel, at the layer where Windows talks to Microsoft's cloud, so it ties every session together no matter which IP the traffic came from.

Switching to a local Windows account doesn't fix it either. Windscribe found its test machine still created a GDID even as a local account, and after manually deleting the value from the registry, it reappeared after a reboot.

## How Windscribe's deGDID works, and how to use it

Windscribe's deGDID uses hosts file modifications and firewall rules to block the registration paths Windows uses to fetch a GDID, and wipes known local identity artifacts.

To run it, download the degdid.ps1 script from GitHub and run it in PowerShell with administrator rights. Use the -Status flag for a read-only check, or -Protect for the full block, verify, and wipe routine, with an -Unprotect option to reverse the changes.

The tool deliberately refuses to run on managed, domain-joined, or corporate machines.

Windows is spying on you. By design.Microsoft's GDID is a unique, server-assigned identifier for your Windows install. A recent court filing showed Microsoft was able to connect a GDID to IP activity.VPNs don't help. Local accounts don't fix it.So we built deGDID.July 27, 2026


This is not a clean opt-out. In hands-on testing, the script ran without errors, but then broke logins to Xbox, Outlook, and the Microsoft Store because the firewall rules also cut off the connectivity those services depend on.

Windscribe warns it may also affect OneDrive, passkeys, and Windows Hello, cannot guarantee it catches every GDID pathway, and does not erase records Microsoft already holds server-side.

For most people, this is just another reminder of what it means to be a Windows user, but if you want to inspect or reduce the identifier, deGDID is currently one of the only tools that tries. And if you want a more comprehensive solution, Windscribe suggests giving Linux a go.

*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds. Make sure to click the Follow button!*

![Monica J. White](https://cdn.mos.cms.futurecdn.net/6AQ4y5nzk8kQ47Yp69GERj.jpg)

Monica is a tech journalist with over a decade of experience. She writes about the latest developments in computing, which means anything from computer chips made out of paper to cutting-edge desktop processors.

GPUs are her main area of interest, and nothing thrills her quite like that time every couple of years when new graphics cards hit the market.

She built her first PC nearly 20 years ago, and dozens of builds later, she’s always planning out her next build (or helping her friends with theirs). During her career, Monica has written for many tech-centric outlets, including Digital Trends, SlashGear, WePC, and Tom’s Hardware.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: D-Link, Ubiquiti devices hijacked by hackers to plunder stolen bandwidth
source_url: https://www.techradar.com/pro/security/d-link-ubiquiti-devices-hijacked-by-hackers-to-plunder-stolen-bandwidth
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-16T16:37:19Z'
published: '2026-10-16T00:00:00Z'
description: Someone hacked network-attached devices to install... legitimate software?
image: https://cdn.mos.cms.futurecdn.net/c6nDwMzYYwipHEZpZkRZb4-2560-80.jpg
categories:
- Technology & Software
people:
- GreyNoise
locations: []
organisations:
- D-Link ShareCenter NAS
- Dahua DVR
- GreyNoise
- Hikvision
- IPIDEA
- MCA
- NVR
- NetNut
- Pawns.app
- SAP NetWeaver Visual Composers
- TechRadar Pro
- Ubiquiti UniFi Video NVRs
---

![CDN - Content Delivery Network - Content Distribution Network - A Network of Proxy Server and Data Center Locations Distributed Throughout the World - 3D Illustration](https://cdn.mos.cms.futurecdn.net/c6nDwMzYYwipHEZpZkRZb4-1920-80.jpg)

* **Attackers exploited vulnerable devices to install legitimate bandwidth-sharing software and hijack internet connections**
* **Compromised systems were covertly added to proxy networks, enabling anonymous criminal activity**
* **Campaign affected at least 143 devices across 34 countries, highlighting patching and access-control failures**

When threat actors break into a system, they don’t need to install malware to make use of the compromised endpoint - they can install perfectly legal, normal software, and still walk away with a paycheck they didn’t earn.

A recent proxyjacking campaign spotted by security researchers GreyNoise impacted hundreds of devices in dozens of countries.

## Proxyjacking

Proxyjacking is a type of attack in which a device is hijacked and assimilated into a proxy network. Usually, cybercriminals would break into a computer, install malware and create a proxy network of their own, which they can later rent or use themselves. Threat actors are always in need of “clean” and unflagged devices and IP addresses behind which they can hide, making residential proxies - both malicious and legal - highly wanted services.

Some of the biggest malicious residential proxies out there include IPIDEA, NetNut, and Cloudrouter. All of them are now either entirely dismantled, or severely disrupted, but while they were operational, they offered hundreds of thousands (sometimes millions) of IP addresses associated with an internet connection used in a household (hence the name “residential IP address”).

But malicious proxies are difficult to pull off. To assimilate a device into the network, the threat actor needs to deploy malware which, as soon as it’s spotted, will be flagged by antivirus products and quarantined. In the newest attacks, spotted by GreyNoise, someone went for a legitimate app with similar functionality, instead.

The researchers found someone installing Pawns.app, primarily a rewards platform that lets users earn money by completing online surveys and playing games. However, it used to offer a bandwidth-sharing feature that let users earn money by allowing business clients to route their internet traffic through the user’s residential IP address. At the start of the year, the app discontinued the feature, but it seems it still works for older versions.

“As of 2026, Pawns.app does not offer internet bandwidth sharing,” a notification on the app’s website reads. “This feature was discontinued and is not associated with Pawns.app anymore.” But the app’s Terms of use still describe traffic sharing as available in some versions of the application, and its business website still promotes an SDK for bandwidth monetization.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Targeting D-Link

Apparently, someone picked up on this and went to work. According to GreyNoise, they targeted D-Link ShareCenter NAS devices, Ubiquiti UniFi Video NVRs, as well as SAP NetWeaver Visual Composers. These contained different vulnerabilities: CVE-2024-3272 and CVE-2024-3273 for D-Link, CVE-2021-44228 for Ubiquiti, and

CVE-2025-31324 for SAP, which the threat actor leveraged to deploy Pawns.app. GreyNoise also said that the attackers targeted Hikvision and Dahua DVR/NVR devices, but did not say which vulnerabilities they leveraged against these devices.

At the moment of publication, the researchers identified at least 143 compromised devices worldwide, located in 34 different countries. While they all had legitimate software installed, it was deployed without their knowledge or consent, making the entire ordeal illegal.

“While “earn on your internet” is voluntary, proxyjacking is a crime. Proxyjacking is when an MCA (malicious cyber actor) forces victim devices into proxy networks in order to monetize their bandwidth,” GreyNoise warned.

If you’re worried someone might have done something similar to a device under your control, GreyNoise created a free service that lets you check if your IP interacted with its Global Observation Grid. The researchers said it can serve as a potential indicator of proxyjacking.

Apart from scanning IP addresses, businesses should educate employees about the risks associated with installing free apps, as well as about the importance of keeping devices patched. They should also detect residential proxy IP addresses in authentication logs, as well as deviations in user authentication behavior and characteristics beyond geolocation, such as mismatches in device identifiers, or session identifiers.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

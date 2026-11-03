---
title: Synology NAS devices could be under attack from new ransomware threat — so
  update now
source_url: https://www.techradar.com/pro/security/synology-nas-devices-could-be-under-attack-from-new-ransomware-threat-so-update-now
source_site: TechRadar UK
source_slug: techradar-uk
description: There's been a wave of attacks against Synology devices
image: https://cdn.mos.cms.futurecdn.net/RUyYKopfxTPNGFEJTvqWBk-1366-80.jpg
published: '2026-11-03T00:00:00Z'
scraped_at: '2026-11-03T23:16:44Z'
categories:
- Technology & Software
- Science
people: []
locations: []
organisations:
- DSM
- NAS
- Shadowserver Foundation
- Synology
- TechRadar Pro
---

![](https://cdn.mos.cms.futurecdn.net/RUyYKopfxTPNGFEJTvqWBk-1366-80.jpg)

* **Synology warned of active ransomware attacks exploiting long-patched DSM vulnerabilities on unupdated NAS devices**
* **Attackers are reportedly deploying the C3rb3r encryptor and demanding thousands of dollars in ransom**
* **Users are urged to patch immediately, restrict internet exposure, and secure NAS access to prevent compromise**

Synology, a major network-attached storage (NAS) manufacturer, is warning users about ongoing ransomware attacks targeting devices running outdated software. It urged all users to apply provided patches and secure their devices without delay.

In a brief announcement, Synology said it “identified threat actors exploiting a vulnerability patched in December 2024 to target devices running outdated versions of DSM.” The goal of the attacks seem to be data encryption and a ransom demand.

“Synology strongly urges all users running vulnerable versions to update DSM immediately to protect their systems. Synology also recommends enabling automatic updates to keep DSM up to date at all times.”

## C3rb3r attacks

The announcement is rather stingy on the details. We don’t know which vulnerability the threat actors are exploiting, where exactly, or how successful they are.

We also don’t know how many devices are at risk - the Shadowserver Foundation tracks a total of 380,000 internet-connected endpoints (many of which are, most likely, running the latest software version and are thus protected).

The company also did not say who the threat actors are, but according to *BleepingComputer*, there has been a “massive wave of reports” from Synology customers whose data was apparently locked down by the “C3rb3r” encryptor. These customers were asked to pay “thousands of dollars” in ransom, in exchange for the decryption key. The publication says the first reports started surfacing more than two weeks ago.

There are two main ways for cybercriminals to access an electronic device and encrypt the data found there - either by exploiting a zero-day vulnerability (one that has not yet received a patch), or by exploiting years-old n-day vulnerabilities (ones that were patched months ago) on devices that were never updated and secured.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

With Synology users, the latter seems to be the case. The company said the attackers were exploiting a vulnerability patched in December 2024, and linked to a November 2024 security advisory, in which it listed three fixed bugs: CVE-2024-10441 (arbitrary code execution), CVE-2024-50629 (arbitrary file read), and CVE-2024-10445 (a bug that allows writing files on compromised devices).

DSM 7.2.2 owners should upgrade to 7.2.2-72806-1 or above, DSM 7.2.1 to 7.2.1-69057-6 or above, and DSM 7.2 to 7.2-64570-4 or above. DSM 7.1 should upgrade to 7.1.1-42962-7 or above, while those running DSM 6.2 to 6.2.4-25556-8 or above. Only in the last version - 6.2 - is the vulnerability labeled as “moderate”. In all other cases it was deemed “critical”.

## Why are NAS devices being targeted?

NAS devices are dedicated storage systems that businesses can connect to their local network and allow employees to access, share, and manage files stored in a centralized location. They are rather popular among SMBs that lack the resources to maintain a more complex enterprise storage infrastructure.

Besides being used as a hybrid cloud of sorts, NAS is also used to store business documents and often acts as a centralized backup. The relative low cost, straightforward deployment, and easily expandable storage capacity makes NAS devices an attractive alternative to both dedicated file servers and cloud storage subscriptions.

However, this also makes them a valuable target for cybercriminals, as we’ve seen in this Synology case. The best way to defend against ransomware attackers is to either completely pull the NAS from the public internet or at least limit access to a handful of vetted identities. Keeping the devices updated with the latest firmware and software is also recommended.

It is worth mentioning that NAS devices usually come with RAID redundancy and built-in backup features, but these do not necessarily protect against ransomware encrypting the stored data.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

---
title: Hackers used a fake VPN download page to steal corporate credentials
source_url: https://www.techradar.com/pro/fake-vpn-download-site-steals-administrator-credentials-to-give-attackers-direct-access-to-corporate-networks-but-delivers-official-signed-software-so-victims-never-suspect-a-thing
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-18T20:36:18Z'
published: '2026-10-18T00:00:00Z'
description: Compromised software download site tricks users into typing passwords
  twice to steal backup credentials
image: https://cdn.mos.cms.futurecdn.net/natgb5M8TLEd5x6jw9mHSd-1920-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Huntress
locations: []
organisations:
- Bing
- Huntress
- SSL
- TechRadar Pro
- WatchGuard Technologies
---

![](https://cdn.mos.cms.futurecdn.net/natgb5M8TLEd5x6jw9mHSd-1920-80.jpg)

* **Fake WatchGuard VPN website steals administrator credentials while delivering legitimate software**
* **Attackers collected VPN server addresses, usernames, and passwords**
* **The fraudulent website rejected initial submissions to collect credentials a second time**

A fraudulent WatchGuard download website stole VPN login details while supplying the authentic installation package, experts have claimed.

Security investigators at Huntress traced the activity to a lookalike domain that collected connection details before downloading the legitimate client.

The investigation began after suspicious activity involving an administrator working for a managed service provider was detected.

## Fake download pages harvest user credentials

Investigators found that the user had searched Bing for a WatchGuard VPN download before visiting a deceptive website designed to resemble the vendor's official download pages.

The website, watchguard-vpn[.]net, offered a purported mobile VPN with SSL download and displayed a form requesting the server address, username, and password.

Those details matched information required by the genuine VPN client, making the request appear consistent with an ordinary installation process.

Submitting the form transmitted the information to a separate domain, watchguard-ssl[.]online, where attackers collected the credentials for potential use against the organization's network.

The malicious script rejected the first submission and cleared the fields, prompting the victim to enter the information again and potentially supplying attackers with multiple password attempts.

Huntress revealed that the operators registered the download domain on August 22, 2026, while the credential collection domain appeared on September 14.

WatchGuard had previously reported the lookalike address in January, although researchers then found no functioning mechanism directing visitors through the fraudulent download process.

## Genuine software helps conceal the credential theft

After collecting the second submission, the website initiated a download from WatchGuard's official content delivery network rather than providing a counterfeit installation package.

The file was Mobile VPN with SSL client version 12.11.5, carrying a valid digital signature from WatchGuard Technologies and a timestamp dated November 4, 2025.

Huntress verified that the installer remained unchanged after signing, meaning investigators found no evidence that attackers had modified the legitimate executable.

This approach differs from campaigns that distribute tampered installers or malicious libraries, which endpoint protection products may identify through file inspection.

The authentic download also gives victims little reason to suspect their credentials have already been compromised, since installation can proceed normally afterward.

Huntress found no recorded download from the official server during the investigated incident, suggesting the user might not have completed both credential submissions.

The detection arrived 21 seconds after the malicious website loaded, allowing the security operations team to provide remediation guidance before investigators observed further escalation.

Huntress reported that the main deceptive domain was offline by October 13, although that status does not establish whether associated infrastructure remains active elsewhere.

The attack avoids many malware checks because the fake website steals VPN credentials through the browser before downloading the genuine software.

Organizations should reset compromised passwords, enable multifactor authentication, check for suspicious VPN logins, and direct employees to official software download pages.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

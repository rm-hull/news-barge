---
title: Apple patches CoreGraphics zero-day used in 'extremely sophisticated' targeted
  attacks on iOS devices
source_url: https://www.techradar.com/pro/security/apple-patches-coregraphics-zero-day-used-in-extremely-sophisticated-targeted-attacks-on-ios-devices
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-29T20:03:45Z'
published: '2026-09-29T00:00:00Z'
description: It's the second such zero-day Apple patched this year
image: https://cdn.mos.cms.futurecdn.net/4bhmWz85fUwn539BDDXxeF-1110-80.jpg
categories:
- Technology & Software
people:
- Tim Cooks
locations:
- Sequoia
- Tahoe
organisations:
- Apple
- CVE-2026-86950
- Google
- Google’s Threat Analysis Group
- Meta Product Security
- NVD
- National Vulnerability Database
- TAG
- Tahoe
---

![Apple logo from Tim Cooks &#039;A Big Week Ahead&#039; teaser](https://cdn.mos.cms.futurecdn.net/4bhmWz85fUwn539BDDXxeF-1110-80.jpg)

* **Apple patches high-severity CoreGraphics zero-day reportedly exploited against specific targeted individuals**
* **The vulnerability enables arbitrary code execution through maliciously crafted files on affected Apple devices**
* **Apple urged users to install the latest security updates, particularly high-value targets facing sophisticated attacks**

Apple has released a fix for a zero-day vulnerability it says was allegedly used “in an extremely sophisticated attack against specific targeted individuals”.

The vulnerability was found in iOS 26.7.1 and iPadOS 26.7.1 and users are advised to apply the fix as soon as possible. This is particularly important for high-value targets such as diplomats, dissidents, whistleblowers, political opposition, and journalists.

## Zero-day

The vulnerability was found in CoreGraphics, the company’s low-level 2D graphics framework used across different platforms (iOS, iPadOS, macOS, and more). CoreGraphics provides developers with tools they need to draw and render visual elements (lines, shapes, images, and even text), and can handle operations such as colors, transparency, gradients, clipping, etc. It is usually used when developers need more precise control over how something is drawn.

The vulnerability is tracked as CVE-2026-86950, with a severity score of 8.8/10 (high). The National Vulnerability Database (NVD) describes it as an out-of-bounds issue that allows threat actors to execute arbitrary code via a maliciously crafted file. The bug can also be exploited to crash programs and corrupt data. Besides iOS and iPadOS, it was also fixed in macOS Sequoia 15.8.1, and macOS Tahoe 26.7.1.

Here is the full list of affected devices:

iPhone 11 and later

iPad Pro 12.9-inch 3rd generation and later

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

iPad Pro 11-inch 1st generation and later

iPad Air 3rd generation and later

iPad 8th generation and later

iPad mini 5th generation and later

Mac devices running macOS Sequoia 15.8.1 and Tahoe 26.7.1

Apple fixed it with improved bounds checking, it was said in the security advisory.

## Abused in “extremely sophisticated” attacks

What makes this vulnerability stand out in a sea of zero-days is how Apple described observed exploitation attempts.

“Apple is aware of a report that this issue may have been exploited in an extremely sophisticated attack against specific targeted individuals on versions of iOS before iOS 27.” We don’t know which report Apple is referring to here - we could not find anyone discussing it. The company only said the bug was flagged by Meta Product Security.

This could be deliberate, though. High-profile attacks tend to draw a crowd, as well as increased interest from other threat actors looking to exploit zero-day flaws. Apple is known for hiding details of vulnerabilities until it is confident that a significant majority of affected devices have been patched.

“Extremely sophisticated attacks against specific targeted individuals” is also wording Apple usually uses for state-sponsored espionage attacks against diplomats and politicians, high-value targets such as tech CEOs, journalists, political opponents and dissidents, and similar. Although it is not mentioned in the report, tech companies like Apple and Google tend to notify the victims when they’re being targeted in such attacks.

The last time Apple used similar wording was in February 2026, when it patched CVE-2026-20700. In that incident it also did not discuss the attackers, or the victims, but we do know that it was discovered by Google’s Threat Analysis Group (TAG), a department assigned with investigating primarily state-sponsored hacking campaigns.

CVE-2026-86950 is now the second zero-day vulnerability the company patched this year. Last year, Apple addressed seven zero-day vulnerabilities exploited in the wild: CVE-2025-24085, CVE-2025-24200, CVE-2025-24201, CVE-2025-31200, CVE-2025-31201, CVE-2025-43529, and CVE-2025-14174.

Given the severity of the flaw and what it can be used for, users are advised to apply the patches without delay. Apple users with automatic updates enabled should receive the security fix automatically, but those who haven't yet updated should manually check Settings → General → Software Update and install iOS/iPadOS 26.7.1.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

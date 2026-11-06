---
title: Even Microsoft Paint is being targeted by cyberattackers — update now or face
  the consequences
source_url: https://www.techradar.com/pro/security/even-microsoft-paint-is-being-targeted-by-cyberattackers-update-now-or-face-the-consequences
source_site: TechRadar UK
source_slug: techradar-uk
description: There's a way to execute malicious code remotely through Paint
image: https://cdn.mos.cms.futurecdn.net/fwciwwzCPqD6nyzmyUPHpQ-1200-80.jpg
published: '2026-11-06T00:00:00Z'
scraped_at: '2026-11-06T23:03:17Z'
categories:
- Technology & Software
people:
- Neowin
- Reddit
locations: []
organisations:
- CISA
- KEV
- Microsoft Store
- NVD
- National Vulnerability Database
- Neowin
- Paint
- Reddit
- TechRadar Pro
---

![Microsoft Paint](https://cdn.mos.cms.futurecdn.net/fwciwwzCPqD6nyzmyUPHpQ-1200-80.jpg)

* **Microsoft fixes high-severity Paint vulnerability that could allow remote code execution through crafted image files**
* **Security updates are delivered through the Microsoft Store, leaving some users temporarily stuck on vulnerable versions**
* **Users should verify their Paint version and install the latest update as soon as it becomes available**

Microsoft has addressed a high-severity vulnerability in Paint that allowed threat actors to run malicious code remotely. However, fixing the issue doesn’t seem to be a straightforward process for users, as the patched version, surprisingly, remains unavailable for download for some people.

Tracked as CVE-2026-83844 and with a severity score of 8.1/10 (high), this bug was described by the National Vulnerability Database (NVD) as an “out-of-bounds read in Windows Paint [that] allows an unauthorized attacker to execute code over a network.”

In theory, a threat actor could create a special image that, if opened via paint, can trigger the flaw and execute malicious code on an affected system.

## How to patch Paint

The bad news is that Microsoft added AI into Paint, which makes the idea of malicious packages triggered through the app a lot more viable. The good news is that Microsoft did not publish technical details about the flaw, explaining how one might pull off this kind of attack, and given that there are no confirmed cases of in-the-wild exploitation, or publicly available exploit code, all of this still remains in theoretical domain.

CISA’s Known Exploited Vulnerabilities (KEV) catalog does not have this bug listed, meaning there are no confirmed cases of attacks, especially against government entities.

Whether or not the bug remains theoretical depends on two main things: how potent the bug is, and how easy it is to leverage. With that in mind, it’s worth mentioning that Microsoft classified the attack vector for this flaw as “Network, with no privileges required”, meaning threat actors with previously obtained low-privilege access could use this bug to escalate their privileges or deploy dangerous malware. Both scenarios could lead to credential theft, wire fraud, or even ransomware attacks.

On the other hand, it marked the bug’s complexity as “High”, suggesting that exploiting it is not that easy of a feat. That could limit abuse to state-sponsored actors, or for-profit hacking groups with deeper pockets and plenty of resources.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

It is also worth mentioning that Microsoft moved Paint from Windows to a standalone Microsoft Store app. Consequently, the security fix isn't distributed through the regular Windows Update mechanism, and users must update Paint through the Microsoft Store themselves (unless automatic app updates are enabled).

The company apparently included a fix in Paint version 11.2605.91.0. However, Neowin reports that despite releasing a newer version, Microsoft was still offering a vulnerable one on its app Store - 11.2605.81.0. The problem was apparently evident to multiple people, enough for them to open a discussion on Reddit. One user even shared a PowerShell output showing that Paint remained on a vulnerable version, despite them checking for updates through the store.

## Different people, different versions

We looked for Paint in the Microsoft Store at press time, and saw version 11.2609.401.0 being offered, with November 5 being the date of the newest update. Neowin also said that for some Reddit users, this was the version carrying the fix, instead. It is possible that Microsoft opted for a staggered release instead of a global rollout, which is why some people were late to be offered the patch.

To make sure your systems are secure, simply looking at Microsoft Store might not be enough. Instead, users should double-check their Paint version using PowerShell, using this command: Get-AppxPackage Microsoft.Paint | Select-Object Name, Version. Those that still see the older version should keep an eye on Microsoft Store for the patch and follow Microsoft’s Security Update Guide for the vulnerability. Those who are worried about being targeted could set up temporary restrictions on certain image attachments or remove Paint entirely from the system.

*Via* * Cybernews*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

---
title: Microsoft Exchange flaw allows hackers to read mailboxes across an organization,
  so patch now
source_url: https://www.techradar.com/pro/security/microsoft-exchange-flaw-allows-hackers-to-read-mailboxes-across-an-organization-so-patch-now
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-06T16:01:51Z'
published: '2026-10-06T00:00:00Z'
description: Microsoft Exchange Server 2016 and 2019 affected
image: https://cdn.mos.cms.futurecdn.net/4UHfYZ86Y3TdJhyqxEcnRA-970-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations: []
organisations:
- BEC
- CISA
- CVE-2026-96940
- ESU
- KEV
- Microsoft Exchange Server
- Microsoft’s Exchange Server Health Checker
- NVD
- National Vulnerability Database
- SE
- TechRadar Pro
- US Cybersecurity and Infrastructure Security Agency
- Users of Exchange Online
---

![Microsoft Exchange on laptop](https://cdn.mos.cms.futurecdn.net/4UHfYZ86Y3TdJhyqxEcnRA-970-80.jpg)

* **Microsoft issues fix for CVE-2026-96940, a high-severity Exchange privilege-escalation flaw**
* **Attackers with compromised user credentials could access other employees’ mailboxes and emails**
* **No active exploitation reported, but Microsoft labeled the vulnerability “exploitation more likely"**

Microsoft has pushed an urgent update for Exchange Server which fixes a high-severity flaw that could wreak some serious havoc among email users.

The company patched CVE-2026-96940, a “weak authorization in Microsoft Exchange Server [that] allows an authenticated attacker to elevate privileges over a network,” as per the National Vulnerability Database (NVD).

According to Microsoft’s advisory the bug, which was given a severity rating of 8.8/10 (high), can be abused to gain unauthorized access to people’s inboxes within the same organization.

In theory, threat actors who obtained credentials of a low-privileged Exchange user could exploit CVE-2026-96940 to escalate their privileges within Exchange, and then read confidential emails and attachments belonging to other people working for the same organization.

The bug cannot be exploited for cross-tenant access, though.

## Establishing a foothold

To exploit the vulnerability, the threat actor needs to have authenticated access beforehand. This, however, is not a major obstacle for the attackers, since they can easily purchase login credentials from the dark web, or use phishing to deploy an infostealer capable of extracting these secrets.

Therefore, even an email account of an “ordinary” employee can be enough to establish a foothold, escalate privileges, and access inboxes belonging to higher echelons within an organization.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

At that point, the vulnerability becomes highly valuable. Corporate email accounts can contain confidential documents, contracts, invoices, internal discussions, and other sensitive information, which the attackers can then use for follow-up attacks such as Business Email Compromise (BEC).

It is worth stressing that CVE-2026-96940 is not known to grant administrator or SYSTEM-level privileges on the underlying Windows server. Instead, Microsoft’s disclosed attack scenario focuses on escalating privileges within Exchange and gaining unauthorized access to other users’ mailboxes

Users of Exchange Online are already secured, Microsoft further explained, since it deployed a related “service-side” fix. However, those using on-prem Microsoft Exchange Server products should upgrade to the latest version to avoid being targeted.

Here is a list of the affected versions:

- Microsoft Exchange Server Subscription Edition RTM

- Microsoft Exchange Server 2016 Cumulative Update 23

- Microsoft Exchange Server 2019 Cumulative Update 15

- Microsoft Exchange Server 2019 Cumulative Update 14

Microsoft says there is no evidence of the flaw being abused in the wild, and at press time, the US Cybersecurity and Infrastructure Security Agency (CISA) does not have it listed in its Known Exploited Vulnerabilities (KEV) catalog. However, the Windows maker labeled the bug as “exploitation more likely” suggesting that cybercriminals might try to exploit it, and warning users to apply the provided fix as soon as possible.

It is also worth mentioning that both Exchange Server 2016 and Exchange Server 2019 reached their end of support last year. Microsoft said that these latest security updates are only available to organizations enrolled in its Period 2 Extended Security Update (ESU) program.

The program gives eligible Exchange Server 2016 and 2019 customers access to security updates released between May and the end of October 2026. Organizations that have not enrolled are being urged to migrate to Exchange Server Subscription Edition (SE) if they want to continue receiving the latest security fixes.

## Unusual release

Microsoft issued the patch on October 2, as part of its September 2026 V2 Exchange Server Security Updates. The original September updates were pushed on September 8, and the software giant added that the main difference between these two versions is the fix for CVE-2026-96940.

As it was releasing the patch, it confirmed it was pushing it “ahead of its intended schedule”, without elaborating further. Perhaps labeling it as “exploitation more likely” is elaborating enough, especially since the company urged customers to review its deployment guidance and apply the update as soon as possible.

fter installing the update, administrators are also advised to run Microsoft’s Exchange Server Health Checker. The tool can verify whether the security update was installed successfully and determine whether any additional action is required.

*Via* * The Hacker News*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

---
title: AntiFox AI agents hijacked by hackers to carry out theft of AWS credentials
source_url: https://www.techradar.com/pro/security/antifox-ai-agents-hijacked-by-hackers-to-carry-out-theft-of-aws-credentials
source_site: TechRadar UK
source_slug: techradar-uk
description: ARTEX forks are wreaking havoc
image: https://cdn.mos.cms.futurecdn.net/Dtd9CSn6K6jfEdpnzch4zj-2121-80.jpg
published: '2026-11-12T00:00:00Z'
scraped_at: '2026-11-12T19:51:53Z'
categories:
- Technology & Software
people: []
locations:
- South Korea
organisations:
- ARTEX
- AWS Support
- Alibaba Cloud
- Amazon GuardDuty
- Amazon Web Services
- AntiFox
- Arctic Wolf
- Autumn-27
- BleepingComputer
- Censys
- GitHub
- Microsoft
- Storm-0940
- TechRadar Pro
---

![Security padlock and circuit board to protect data](https://cdn.mos.cms.futurecdn.net/Dtd9CSn6K6jfEdpnzch4zj-1920-80.jpg)

* **Attackers are abusing the AI-powered penetration testing tool AntiFox to search for credentials and compromise AWS environments**
* **Campaigns leveraged web-server intrusions and stolen cloud credentials to map infrastructure and access sensitive resources**
* **Researchers urge organizations to monitor for web shells, rotate exposed secrets, and enforce least-privilege access controls**

Cybercriminals are using an open source AI-powered pentesting platform called AntiFox to steal login credentials and access people’s Amazon Web Services (AWS) environments.

This is according to security researchers Arctic Wolf, who recently disclosed their findings on GitHub, explaining how unnamed threat actors were hosting their own instances of the tool on Alibaba Cloud infrastructure and were using its automated capabilities to analyze compromised systems, search for passwords, and access cloud resources.

## What is AntiFox?

AntiFox is an AI-powered, open source penetration testing platform built by a Chinese developer. Penetration testing is a process cybersecurity professionals usually use to identify weaknesses in their IT infrastructure, and while tools like AntiFox are not malicious by design, they are often abused in different attacks. This happens all the time with tools such as Cobalt Strike or ConnectWise ScreenConnect, too.

Arctic Wolf said that in some of the attacks they observed, threat actors first compromised internet-facing Microsoft IIS web servers, although they could not determine exactly how.

They then installed web shells to execute malicious server commands remotely and from there, they were going through application files and configuration settings, looking for database login credentials and other valuable secrets. The researchers also saw attempts to use these credentials to connect to internal production databases.

In other cases, attackers would use valid AWS credentials obtained elsewhere to sift through cloud environments and uncover accounts, permissions, databases, storage servers, and other important resources.

Commenting on the report, Amazon told *BleepingComputer* its services work as intended and urged customers to keep their passwords a secret: "AWS services were not compromised and operated as designed. The research describes threat actors using credentials taken from customers’ compromised applications to access their AWS accounts. As always, we recommend all customers follow security, identity, and compliance best practices, including granting least-privilege permissions, requiring IMDSv2 on EC2 instances, keeping long-term access keys out of application configurations, and turning on Amazon GuardDuty. Customers who suspect unauthorized activity in their accounts should follow guidance for remediating potentially compromised credentials or contact AWS Support."

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

AntiFox was built as a fork of ARTEX 0.1.1, another Chinese-developed AI-powered penetration testing framework that’s been filling headlines lately. Earlier this week, security researchers Censys said they identified 1,465 hosts running exposed ARTEX consoles, of which roughly 10% also ran at least one other tool commonly used in cyberattacks.

They also found 32 publicly accessible directories on ARTEX hosts, some of which exposed exploit binaries, post-exploitation tools, and other sensitive files.

## The ghost of ARTEX

ARTEX was released in late July 2026 by a developer called Autumn-27, to serve as an AI-powered upgrade to ScopeSentry, a tool Censys described as a “widely used Chinese asset-discovery and vulnerability-scanning platform.” Its popularity skyrocketed, and by early October, reports started coming out of ARTEX being used in cyberattacks. Soon after the developer distanced themselves from these attacks, turned the tool closed-source, and made no subsequent releases.

Since then, numerous researchers observed it being used in different attacks, including a hit on South Korea financial institutions. Microsoft saw China-aligned group Storm-0940 use it, as well.

Arctic Wolf now recommends organizations monitor their web servers for suspicious activity, such as random files appearing on the networks, or operating-system commands being executed unapproved. They should also investigate unusual AWS activity, including rapid requests across multiple services and attempts to access stored credentials from unfamiliar infrastructure.

Unfamiliar web shells should be terminated on the spot, compromised systems reviewed, and any and all exposed passwords, API keys, and cloud credentials rotated without delay. The researchers also advise restricting application permissions to the resources needed for normal operations and enabling detailed logging to help detect suspicious access and unauthorised changes to stored data.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

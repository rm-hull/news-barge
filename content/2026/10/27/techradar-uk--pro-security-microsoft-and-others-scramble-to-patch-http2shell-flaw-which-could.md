---
title: Microsoft and others scramble to patch 'HTTP2Shell' flaw which could be the
  next PHP-level issue — Node.js problem may also affect millions of sites
source_url: https://www.techradar.com/pro/security/microsoft-and-others-scramble-to-patch-http2shell-flaw-which-could-be-the-next-php-level-issue-node-js-problem-may-also-affect-millions-of-sites
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-27T22:09:12Z'
published: '2026-10-27T00:00:00Z'
description: An RCE flaw was found in Brotli
image: https://cdn.mos.cms.futurecdn.net/kCbP2VkzMgQpYqJDgMQ8UZ-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- Brotli
- GitHub
organisations:
- Admins
- BleepingComputer
- Brotli
- Google
- HTTP2Shell
- Microsoft
- Node.js
- PyPI
- TechRadar Pro
- WAF
---

![Cybersecurity](https://cdn.mos.cms.futurecdn.net/kCbP2VkzMgQpYqJDgMQ8UZ-1920-80.jpg)

* **A critical Brotli compression flaw, dubbed HTTP2Shell, could enable memory corruption and remote code execution**
* **The vulnerability affects widely used software including Node.js, Python packages, and .NET applications**
* **Vendors released patches, and administrators are urged to update immediately despite no confirmed in-the-wild exploitation**

Multiple tech companies and projects have recently pushed patches for a vulnerability called “HTTP2Shell” which could enable remote code execution (RCE) attacks, similar to the recent “PHP2Shell” vulnerabilities.

HTTP2Shell was found in Brotli, a Google-built open source data compression algorithm that reduces file sizes without losing information, thus achieving faster transmission times while using less bandwidth.

It is a popular algorithm used on the web to compress HTTP responses such as HTML, CSS, and JavaScript, and is supported by most web browsers, servers, and software libraries.

## Fixes and patches

The bug itself is described as an out-of-bounds write flaw, and is also dubbed Node2Shell, and Broccoli2Shell. It is tracked as CVE-2026-111497, and was given a severity score of 9.2/10 (critical). According to the National Vulnerability Database, the bug causes a buffer overflow which could lead to memory disclosure, denial of service and, in some cases, even remote code execution.

Brotli can be found in all sorts of software, all of which is now at risk. That includes Node.js, brotlicffi, HTTP clients such as Requests, urllib3, httpx and aiohttp, but also other apps that use Brotli decoders such as Bun and Envoy deployments.

Google fixed the bug on October 21 2026, by releasing Brotli versions 1.0.10, 1.1.1, and 1.2.1. However, there are other software that either bundle or use vulnerable Brotli versions, so updating Google’s library alone may not protect every application.

Over the last weekend, Microsoft released an emergency update to sort the bug in .NET, saying successful exploitation could lead to privilege escalation.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Since it also bundles the Brodli decoder, Node.js released its patch on October 21, too. “An invalid block switch was reported as a temporary need for more input instead of a permanent format error, so the streaming decoder kept appending input bytes to an eight-byte internal buffer,” the organization explained. “An attacker who can supply Brotli data that an application decompresses with node:zlib can corrupt process memory, which can lead to a crash, disclosure of process memory, or remote code execution.”

The vulnerability was said to be affecting Node.js 26.x, 24.x, and 22.x.

*BleepingComputer* reports that PyPI packages containing the fixes became available two days later, on October 23.

Here is a detailed list of patched versions:

Google Brotli 1.0.10, 1.1.1, 1.2.1

Node.js 22.23.4, 24.22.1, 26.12.1

Python Brotli 1.2.1

Python brotlicffi 1.2.1.0

## Dedicated website

At the same time, someone set up a dedicated website, Broccoli2Shell.com, which describes the issue, tracks vulnerable versions, and reports on attempted exploits in the wild. On the site, it is said that proof-of-concept (PoC) exploits for the bug already exist, but reports of malicious exploitation in the wild are yet to be seen.

“A public proof of concept appeared on GitHub on 2026-10-22,” the site reads. “It reportedly reaches code execution only on a deliberately weakened build. On standard builds it causes a crash and a limited memory read.”

System administrators are advised to apply the provided patches as soon as possible; restart affected processes and rebuild and redeploy affected container images.

Those that cannot do that immediately can somewhat mitigate the risks. Python users should uninstall the vulnerable Brotli and brotlicffi packages and remove optional dependencies such as httpx[brotli].

Admins can also configure proxies, load balancers or web application firewalls (WAF) to reject incoming requests containing Brotli-compressed bodies. It’s worth mentioning that this doesn’t protect apps that download and decompress malicious HTTP responses.

Node.js has no complete workaround, it was said.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

---
title: Leaked private keys for eight CA certificates let any attacker impersonate
  any domain — billions of older devices and software installations may be vulnerable
  after round of fixes, patch yours immediately
source_url: https://www.tomshardware.com/tech-industry/cyber-security/leaked-private-keys-for-eight-ca-certificates-let-any-attacker-impersonate-any-domain-billions-of-older-devices-and-software-installations-may-be-vulnerable-after-round-of-fixes-patch-yours-immediately
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-22T17:18:44Z'
published: '2026-10-22T00:00:00Z'
description: Stop everything and update your browsers, OSes, development tools, and
  routers.
image: https://cdn.mos.cms.futurecdn.net/9ayjX5pnSftEeACZ5V7XaP-2000-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Tom
locations: []
organisations:
- CA
- Certification Authority
- Get Tom's Hardware
- Google News
- ISP
- Microsoft
- PC
- Tom's Hardware
- eMudhra
---

![Hacker](https://cdn.mos.cms.futurecdn.net/9ayjX5pnSftEeACZ5V7XaP-1920-80.jpg)

Most everyone in the tech space has been living in *interesting* times, but this week isn't done yet, and it's already quite special for systems administrators worldwide. They already had to deal with the critical PHP RCE vulnerability, but they also have to update untold amounts of machines and software, thanks to eight insecure intermediate CA certificates that can allow attackers to impersonate any domain and/or pretend their malware is from a legitimate source.

An attacker anywhere in the path of your network traffic, like, say, in a company or government network, public Wi-Fi, your ISP, or one of any number of government entities, can intercept your connection and pretend that they're **any** website, like apple.com, amazon.com, or bankofamerica.com. If not updated, your operating system and installed software would be none the wiser. Additionally, with the code signing certificates, an application you download can be shown as completely legitimate from, say, Microsoft or Google.

The way that software checks a certificate is legitimate is by verifying its "chain." For example, a website like tomshardware.com has a certificate, issued and signed by an *intermediate* Certification Authority (or CA, a certificate-selling company), and whose certificate, in turn, is trusted and signed by root certificates — whose exceedingly precious keys are kept offline in safes. In this week's event, Indian CA firm eMudhra issued six TLS and two code-signing intermediate certificates with easily guessable keys.

Your operating system and potentially tens of different applications on your machine all keep a list of which root certificates and CAs are trusted. Browsers also keep a list of those **not** to trust, called a revocation list. These lists are updated periodically as screw-ups happen, just like the one that took place this week. And now they all need to be updated again, by revoking the eight CAs, removing the one affected root certificate, or just hard-coding a rejection of all eight affected keys.

There's a silver lining: recent versions of Chrome, Brave, Firefox, and Safari all enforce a feature called Certificate Transparency that consults a public read-only log of certificate issuances, and blocks any that aren't mentioned. Google reports that no certificates signed by the six affected intermediate CAs were logged, so if regular web browsing is all you did, you should be safe — but still check all your software for updates nonetheless.

The problem here is the sheer amount of machines and software that needs updating: PCs, servers, operating systems, phones, tablets, routers, web browsers, web browsers wrapped in apps, virtual servers, virtual machines, Docker and other containers, programming languages like Python, Go, Node.js, Rust, standalone download utilities like curl, and probably tens or hundreds of other categories. Additionally, we discussed things that are expected and likely to get updates. Old routers, smart and IoT appliances, and old computers could eventually present a problem.

As for the technical details, eMudhra issued six intermediate CA certificates and two intermediate code-signing certs with rather unadvisable private keys. The private key is the secret half of the two parts of a certificate, and for some reason, those of the aforementioned certs were only 1 byte long — thus a number from 0 to 255, trivial to brute-force in a split second. How the heck that happened is still under investigation.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

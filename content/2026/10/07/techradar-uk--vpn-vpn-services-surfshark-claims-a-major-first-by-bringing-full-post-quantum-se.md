---
title: Surfshark claims a major first by bringing full post-quantum security to WireGuard
source_url: https://www.techradar.com/vpn/vpn-services/surfshark-claims-a-major-first-by-bringing-full-post-quantum-security-to-wireguard
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-07T13:17:34Z'
published: '2026-10-07T00:00:00Z'
description: The popular VPN provider has implemented ML-DSA authentication to protect
  users from future quantum computer session takeovers.
image: https://cdn.mos.cms.futurecdn.net/pWpou2FvwQCdLVveG7JmGA-1920-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Karolis Kaciulis
- Surfshark
locations:
- Surfshark
- WireGuard
organisations:
- AWS KMS
- Apple
- Big Tech
- Google Cloud KMS
- Leading System Engineer
- ML-DSA
- ML-KEM
- Microsoft
- NordVPN
- Surfshark
- VPNs
- WireGuard
---

![Surfshark VPN app](https://cdn.mos.cms.futurecdn.net/pWpou2FvwQCdLVveG7JmGA-1920-80.jpg)

* **Surfshark has integrated ML-DSA certificates into WireGuard to achieve full post-quantum security.**
* **The upgrade focuses on server authentication to prevent future session takeovers.**
* **The feature is currently live for users on iOS, macOS, and Windows.**

Quantum computers might still sound like science fiction, but cybersecurity experts are already preparing for the day these super-powered machines can effortlessly crack today’s encryption. Now, Surfshark has taken a massive step toward quantum-proofing your daily browsing.

The popular provider has announced the completion of its full post-quantum WireGuard implementation. By tackling the incredibly tricky challenge of server authentication, the company claims it has secured every pillar of a private connection against future quantum threats.

While many tech giants and rival VPNs have begun integrating basic post-quantum key exchanges, fully securing the authentication process remains incredibly rare. Surfshark's latest update ensures bad actors armed with futuristic quantum tech can't impersonate VPN servers and hijack your connection.

## The 'forgotten' pillar of quantum security

Earlier this year, Surfshark rolled out post-quantum encryption and key exchanges (known as ML-KEM) to the WireGuard protocol. Other providers have made similar moves recently, with rivals like NordVPN extending post-quantum protection across its applications.

However, Surfshark has now added the final critical component: certificates using ML-DSA (digital signature algorithm) for authentication.

"A truly full post-quantum secure VPN rests on three pillars: encryption, key exchange, and authentication. While the industry has widely adopted quantum-safe encryption and key exchange (like ML-KEM), authentication remains the 'forgotten' step," explained Karolis Kaciulis, Leading System Engineer at Surfshark.

"Many, including Big Tech, hesitate here because certificates for authentication are difficult to scale and currently lack a global public infrastructure for post-quantum certificates.”

## Beating Big Tech to the punch

So, why does authentication matter for the average user? If an attacker uses a quantum computer to break a VPN's authentication layer, they can perform a session takeover, essentially pretending to be the secure server right as you connect, intercepting all your data.

“However, ignoring this last step creates a vulnerability when quantum computers become accessible," Kaciulis said. "At Surfshark, we took the ML-DSA standards and integrated them with our certificates into a protocol to make the authorization fully quantum-resistant. By using the ML-DSA certificates, we have completed the final pillar, achieving the first full post-quantum WireGuard implementation."

This technical milestone stems from the launch of Dausos, Surfshark’s proprietary VPN protocol engineered with complete post-quantum security from the ground up, which paved the way for this WireGuard upgrade.

Remarkably, Surfshark is deploying a level of security rarely seen in the consumer space. An evaluation by the company of 15 major tech platforms found that only two, AWS KMS and Google Cloud KMS, have actually deployed ML-DSA, and both are cloud key-management services, not consumer applications.

While giants like Apple and Microsoft have access to ML-DSA, neither has enabled it by default in primary user-facing software like Safari or Edge.

“It comes as no surprise that industry peers prioritize implementing ML-KEM key exchange before placing authentication on their engineering roadmaps," Kaciulis noted.

"Although quantum computing poses no immediate threat today, delaying authentication security until these machines emerge leaves connections vulnerable. That is why Surfshark is taking proactive measures to deliver complete post-quantum defense ahead of potential quantum threats.”

If you're eager to test out these proactive protections, Surfshark's fully post-quantum WireGuard implementation is currently accessible to users on iOS, macOS, and Windows. The company plans to bring support to additional platforms in future releases.

Or to read more about this Surfshark upgrade, read its blog post outlining the move to post-quantum.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

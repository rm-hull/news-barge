---
title: 'Behind the tech: How NordVPN''s NordLynx protocol achieves incredible speeds'
source_url: https://www.tomshardware.com/software/vpn/behind-the-tech-how-nordvpns-nordlynx-protocol-achieves-incredible-speeds
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-08T19:25:29Z'
published: '2026-09-08T00:00:00Z'
description: State-of-the-art ChaCha 20 cryptography and an exceptionally lean 10,000-line
  codebase deliver blistering performance
image: https://cdn.mos.cms.futurecdn.net/9g5HrEH8iLTX7cZCUDnvQm-1920-80.png
---

![NordVPN](https://cdn.mos.cms.futurecdn.net/9g5HrEH8iLTX7cZCUDnvQm.png) 

NordLynx is NordVPN's proprietary next-generation VPN protocol. Based on the high-performance WireGuard framework, it delivers blistering speeds – __**up to 57% faster**__ than other protocols such as OpenVPN. By combining the speed of WireGuard with its own custom double NAT implementation, NordVPN can deliver industry-leading data transfer speeds with exceptionally strong security and privacy protection.

## Summary

- NordLynx is the best VPN protocol for online gaming, large file transfers and high quality video streaming due to its high performance, low lag, SmartPlay, Smart DNS and region unblocking
- NordLynx was created by NordVPN and uses the high-speed WireGuard protocol for a very fast and secure VPN connection with a very lean codebase
- NordLynx delivers the best of both worlds: the **high speeds of WireGuard** and NordVPN's own**Double NAT security and privacy protection**
- NordLynx was introduced in 2020 and got a huge upgrade in 2025 with the addition of **post-quantum encryption support**
- NordLynx's lean code – **10,000 lines** compared to 400,000 for OpenVPN – requires less processing power than other VPN protocols, for improved battery life on laptops, phones and tablets

## What is NordLynx?

NordLynx is a next-generation VPN protocol developed by NordVPN to deliver faster and more secure VPN connections. It’s based on the __WireGuard__ framework, which is famed for its high speeds, and NordVPN has added a custom double NAT layer to ensure complete user privacy. In 2025 NordLynx added a significant security boost with post-quantum encryption support.

NordLynx is much more streamlined than the common OpenVPN standard: NordLynx has around 10,000 lines of code compared to OpenVPN’s 400,000. That means it’s easier to troubleshoot and resolve technical issues.

When you click on Connect, your data is instantly encrypted into unreadable code. That information is then sent at high speed through the NordLynx VPN tunnel to the VPN server, which then decrypts your data and forwards your request to the appropriate internet server. This enables you to access web sites and services more privately without your ISP or other third parties being able to see what you are doing or what data you’re transmitting.

## Why should I use NordLynx?

NordLynx is faster, more secure, better for gaming and less demanding on your hardware than other VPN protocols. It supports post-quantum encryption to future-proof your privacy, and as it’s based on the lean code of the WireGuard framework it delivers highly secure connections that are **up to 57% fasterthan the OpenVPN protocol.**

NordLynx is very easy to set up and use, and it can protect and secure not just phones, tablets and PCs but also home entertainment hardware and gaming consoles. It’s a particularly good option for streaming movies, online gaming, and transferring large files safely and securely.

That means NordLynx combines the superb performance of WireGuard with best-in-class security to deliver a very fast and highly secure VPN service that's **up to 57% fasterthan the OpenVPN protocol.** NordLynx is particularly good for high quality video streaming, large file transfers and online gaming.

## Why did NordVPN make NordLynx?

When the WireGuard protocol was released its state-of-the-art cryptography and very efficient code was a game-changer for VPN technology, but while NordVPN's engineers appreciated its speed they recognised that initially its user address handling presented a security risk. So NordVPN created their own flavour of WireGuard, using the same lean codebase but adding extra security.

### How does NordLynx work?

NordLynx enhances WireGuard with a **dynamic double Network Address Translation layer**, double-NAT for short.

As NordVPN's Aurelija Andriekutė __explains__, "While WireGuard is now considered one of the most secure VPN protocols, its original architecture required servers to store a static IP table connecting users to their internal IP addresses. But for us, storing user identities on a VPN server was simply not an option. To solve this privacy vs. speed conundrum, we developed our own double NAT implementation — the heart of NordLynx. This system allows us to harness WireGuard’s speed without compromising security by using two distinct layers":

- The first layer assigns the same local IP address to every user of a server, which masks the individual users' identities.
- The second layer uses the dynamic NAT system to give each VPN tunnel session a unique IP address. That means the data packets go where they're supposed to without getting mixed up.

"The dynamic IP assignment lasts only while the session is active," Andriekutė says. "User authentication is handled through a secure external database, so no identifiable data is ever stored on the VPN server itself."

### How fast is NordLynx?

When __TechRadar__ tested NordLynx on a 10Gbps connection, NordVPN was 29% faster than OpenVPN. __CyberInsider__ found an even bigger difference: OpenVPN was 57% slower than NordLynx. NordLynx delivered "the fastest VPN speed test result we have ever recorded here," reviewer Bill Mann wrote.

## What are the benefits of NordLynx?

- NordLynx is fast, with connection speeds consistently ranking among the very fastest in the entire VPN industry
- NordLynx is great for gaming and movies because its lean code delivers low lag and high data speeds
- NordLynx' is secure because **ChaCha20 encryption** cipher and**Poly1305 authentication** deliver stronger security and faster speeds than older standards
- NordLynx isn't a hardware hog because its compact **10,000-line codebase** uses much less computing power than other VPN protocols, and that means longer battery life for your laptop, phone or tablet
- NordLynx is future-proof because it added __post-quantum encryption__ in 2025 to protect against the next generation of security threats
- NordVPN is regularly voted the best VPN for most people thanks to its user-friendly app and first-class support
- NordVPN can be used on virtually any device because router-level encryption spans all your connected devices

## When should I use NordWhisper instead of NordLynx?

- NordLynx's high-speed traffic has a distinct signature, and in countries with significant online censorship and monitoring that means its use can be detected. In those cases NordVPN recommends using the NordWhisper protocol instead.
- Some restrictive networks, such as universities, workplaces, certain public Wi-Fi , block UDP-based traffic. NordVPN's OpenVPN TCP mode works around this on networks that restrict UDP.

## NordLynx vs. OpenVPN vs. IKEv2

| Header Cell - Column 0 | NordLynx (WireGuard) | OpenVPN | IKEv2/IPSec | 
|---|---|---|---|
| Performance | Extremely fast | Average | Fast | 
| Encryption | ChaCha20 | AES-256 | AES-256 | 
| Codebase weight | Light | Heavy | Medium / Heavy | 
| CPU usage | Low | High | Medium | 
| Setup and configuration | Automatic | Automatic and Manual | Automatic and Manual | 
| Best for | Streaming, gaming, large file downloads | Bypassing strict firewalls and router setup | Mobile users switching between Wi-Fi and mobile data | 

## What other features does NordVPN offer?

NordVPN also gives you **Meshnet private networking** for your home or office plus**SmartPlay for streaming**,** SmartDNS to configure older devices such as smart TVs**, and** regional unblocking**, which bring you buffer-free 4K streaming without the inconsistent speeds and manual server-switching that plague some other VPN providers.

Every NordVPN plan pairs high-speed NordLynx encryption with built-in threat protection to **automatically block malicious domains and phishing links** before they hit your device. You also get**Dark Web Monitoring alerts**, which scan leaked databases for information associated with your email addresses, within one subscription that offers long-term value because it is an all-in-one digital security app under one single, predictable subscription.

__Explore NordVPN packages__ to secure your devices with high-speed NordLynx protection.

## Frequently Asked Questions

### Does NordVPN store browsing history or connection logs?

No, NordVPN has a strict no-logs policy that has been confirmed by multiple independent auditors. NordVPN servers are diskless and RAM-based, not hard disk-based, so there's no hardware logging. **Six ISAE 3000 privacy audits** have verified that no user activity data is logged or stored anywhere by NordVPN or any third parties. And NordVPN operates under Panamanian jurisdiction because of that country's strong privacy-respecting legislation.

### Can NordVPN protect devices that don't have VPN apps?

Yes. NordVPN can be used on many brands of router, which means it then protects any and all devices connected to that router. If your router supports the OpenVPN protocol it should be NordVPN-friendly, but some ISP-provided routers don't support that protocol. Not to worry: you can simply replace the router with one that is either NordVPN compatible or comes with NordVPN already installed.

### How do I use NordVPN to stay safe on public Wi-Fi?

NordVPN protects you automatically. NordVPN's Auto-connect feature turns on your VPN protection when it detects that you've connected to an insecure network. NordVPN also features Kill Switch, which automatically shuts down internet access if the secure connection drops for even a fraction of a second, ensuring that you're still protected from data leaks.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

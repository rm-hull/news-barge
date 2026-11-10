---
title: IPVanish quietly brings quantum-resistant WireGuard to iPhone and iPad — here's
  all we know
source_url: https://www.techradar.com/vpn/vpn-services/ipvanish-quietly-brings-quantum-resistant-wireguard-to-iphone-and-ipad-heres-all-we-know
source_site: TechRadar UK
source_slug: techradar-uk
description: The provider's latest iOS release adds post-quantum protection to WireGuard,
  but key questions remain
image: https://cdn.mos.cms.futurecdn.net/ERozb9wLZjSh2du9E2sqw7-2000-80.jpg
published: '2026-11-10T00:00:00Z'
scraped_at: '2026-11-10T19:46:03Z'
categories:
- Technology & Software
people:
- Subbu Sthanu
locations:
- WireGuard
organisations:
- App Store
- IPVanish
- ML-DSA
- No Trace
- NordVPN
- OpenVPN
- PQE
- Surfshark
- TechNadu
- WireGuard
---

![ipvanish price, free trial and deals](https://cdn.mos.cms.futurecdn.net/ERozb9wLZjSh2du9E2sqw7-1920-80.jpg)

* **IPVanish has added post-quantum encryption (PQE) in latest iOS update**
* **PQE protects your data against "harvest now, decrypt later" attacks**
* **The release notes don't yet reveal how IPVanish's PQE works**

IPVanish has rolled out post-quantum encryption (PQE) in its iOS app, becoming the latest VPN provider to prepare for a future where quantum computers can crack today's encryption.

Version 4.33.2 of the IPVanish app landed on the App Store on Monday, and its release notes confirm in a single line that PQE has been added to the WireGuard protocol.

The move puts IPVanish alongside a growing list of best VPN providers already offering quantum-resistant protection, including NordVPN, Surfshark, ExpressVPN, and Mullvad.

![IPVanish — an ever-evolving VPN]([https://cdn.mos.cms.futurecdn.net/YqebV5aGZfsKo8SWsNFjhB-200-80.jpg.webp](https://cdn.mos.cms.futurecdn.net/YqebV5aGZfsKo8SWsNFjhB-200-80.jpg.webp) "IPVanish — an ever-evolving VPN")

**IPVanish — an ever-evolving VPN**  
IPVanish may not quite match the market leaders, but it is still a strong all-round VPN with plenty of features, high speeds, and better unblocking capabilities than most VPNs. Well worth a try, especially as it keeps improving its infrastructure, speed performance, and feature offerings.

## What we know about IPVanish's post-quantum upgrade

Right now, the facts are limited. According to the App Store listing, PQE applies to WireGuard on iOS. The notes don't mention OpenVPN or IKEv2, and there's no word yet on Android, Windows, macOS, or IPVanish's TV apps.

Several key questions remain, including which algorithm IPVanish is using, whether the setup is hybrid or fully post-quantum, whether it's switched on by default, and when other platforms will follow.

We've contacted IPVanish and will update this article when we hear back.

That said, the upgrade has been in the works for a while. Back in September 2025, IPVanish's Chief Commercial Officer Subbu Sthanu told TechNadu that post-quantum readiness was a major focus for its R&D team, which was exploring hybrid encryption for both WireGuard and OpenVPN.

At the time, Sthanu said the team was "building custom implementations rather than relying on off-the-shelf patches."

The rollout also caps a busy few months for the provider, which recently passed its third independent no-logs audit and continues to expand its RAM-only server network.

## Hybrid or full? Why the details matter

WireGuard isn't quantum-safe out of the box, as its key exchange relies on elliptic-curve cryptography. Providers usually fix this by running a separate post-quantum handshake, typically with the NIST-standardized ML-KEM algorithm, and feeding the result into WireGuard's pre-shared key slot.

Most VPNs, including NordVPN, take a hybrid approach that layers post-quantum protection on top of classical encryption, so a flaw in the newer algorithm wouldn't leave your data exposed.

Some providers are now pushing further. In October 2026, Surfshark added ML-DSA authentication to WireGuard, claiming full post-quantum coverage of encryption, key exchange, and authentication. Without quantum-resistant authentication, a future attacker could, in theory, impersonate a VPN server. NordVPN is also working on post-quantum authentication.

Knowing where IPVanish sits on this spectrum will tell us how complete its protection really is.

![Leave No Trace logo](https://cdn.mos.cms.futurecdn.net/Z7QHFc4GHoMhdps5XmntoC-1200-80.png)

**NEW**:** Leave No Trace** — A weekly newsletter on digital privacy and online surveillance. Leave No Trace investigates the companies and governments putting our digital freedom at risk — and the people fighting back.

📩 Subscribe now to get every edition delivered to your inbox every Friday, launching this September.

## Why post-quantum encryption matters for you

Quantum computers aren't yet powerful enough to break modern encryption, but experts expect that moment, dubbed "Q-Day," to arrive eventually.

The risk is already here, though, as bad actors are already deploying so-called "harvest now, decrypt later" attacks to collect encrypted traffic today and store it until they gain the tools to unlock it.

For most people, this isn't cause for panic. But if you send sensitive information that needs to stay private for years, such as financial, medical, or work data, PQE adds a valuable layer of future-proofing.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

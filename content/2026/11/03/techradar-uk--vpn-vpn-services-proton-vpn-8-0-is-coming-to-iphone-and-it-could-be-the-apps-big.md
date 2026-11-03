---
title: Proton VPN 8.0 is coming to iPhone — and it could be the app's biggest upgrade
  in years
source_url: https://www.techradar.com/vpn/vpn-services/proton-vpn-8-0-is-coming-to-iphone-and-it-could-be-the-apps-biggest-upgrade-in-years
source_site: TechRadar UK
source_slug: techradar-uk
description: A new Rust-based VPN engine, an advanced kill switch, and CarPlay-friendly
  connectivity are all on the way
image: https://cdn.mos.cms.futurecdn.net/wYZjT2CMEhMRLCQ3hrDRp5-1193-80.png
published: '2026-11-03T00:00:00Z'
scraped_at: '2026-11-03T23:16:41Z'
categories:
- Technology & Software
people:
- Antonio Cesarano
- Swift
locations:
- Rust
organisations:
- App Store
- Apple
- GitHub
- Product Lead
- Proton VPN
---

![Proton VPN new mobile app interface – promo image](https://cdn.mos.cms.futurecdn.net/wYZjT2CMEhMRLCQ3hrDRp5-1193-80.png)

* **Proton VPN has published iOS 8.0.0 on GitHub, but the update is yet to reach the App Store**
* **Its primary focus is Proton protocols, a new Rust-based VPN engine aimed at stability and censorship resistance.**
* **An advanced kill switch, an interactive globe map, and better CarPlay support are also on the way.**

Proton VPN users on iPhone have a big update to look forward to. The provider has published iOS 8.0.0 on its GitHub releases page, and it could be the most significant change to the app in years.

The biggest addition is Proton protocols, a new VPN architecture that Proton says is designed for improved stability and censorship resistance. It also makes the advanced kill switch possible on iPhone and iPad, a feature that has so far only been available on iOS in beta.

Proton VPN already sits among the best VPN services we've tested, climbing to third place in our latest round of re-testing. Anything that tightens up its iOS app is good news for privacy-minded iPhone owners.

## What's new in Proton VPN 8.0 for iOS

The biggest change is one you won't see. Proton protocols, known internally as ProTUN, swaps out the standard wireguard-go code for libpvpnclient, Proton's own WireGuard implementation written in Rust.

Proton says wireguard-go never integrated well with Swift, the language it uses to build its iOS app, which made development and debugging harder.

For users, Proton promises faster updates, fewer platform-specific bugs, and a quicker response when censors change tactics.

The new core also lays the groundwork for post-quantum encryption, which Proton lists as a planned feature. Antonio Cesarano, Product Lead at Proton VPN, says it lets the team experiment with "connection stability, battery usage, and resilience".

## A stricter kill switch for your iPhone

A standard kill switch cuts your internet if the VPN connection drops. Proton's advanced kill switch goes further, blocking all internet access unless you're connected to Proton VPN, and it stays active even after you restart your device.

That's a notable step on iOS, where Apple's network restrictions have long made a true kill switch difficult. Proton itself once said a kill switch as it defined it wasn't possible on iOS. Even now, Proton warns that some DNS requests from Apple services can bypass the VPN with the kill switch on.

Version 8.0 also fixes a common frustration. You'll be able to reach LAN devices, like printers, and use Apple CarPlay with either kill switch enabled.

## When can you get Proton VPN 8.0?

Proton hasn't announced a release date. However, with the final 8.0.0 build now tagged on GitHub, the App Store rollout could land any time now, though Apple's review process can add a delay.

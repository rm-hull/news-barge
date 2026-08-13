---
title: Proton VPN rolls out Rust-powered 'Proton Protocols' in beta across all major
  apps
source_url: https://www.techradar.com/vpn/vpn-services/proton-vpn-rolls-out-rust-powered-proton-protocols-in-beta-across-all-major-apps
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-13T13:38:47Z'
published: '2026-08-13T00:00:00Z'
description: The new 'ProTun' architecture brings advanced kill switches, better app
  stability, and a foundation for post-quantum encryption to Windows, iOS, Android,
  and Linux
image: https://cdn.mos.cms.futurecdn.net/3ruJNNTxMpPr8eytE66KgK-1024-80.png
---

![Proton Protocols feature in beta on app settings (August 2026)](https://cdn.mos.cms.futurecdn.net/3ruJNNTxMpPr8eytE66KgK.png) 

- **Proton VPN's new Rust-based Proton Protocols is in beta on all major apps**
- **It replaces WireGuard-go for better stability, speed, post-quantum readiness**
- **It includes an Advanced Kill Switch and Linux Stealth support**

Following up on recent teasers, Proton VPN has officially rolled out a massive under-the-hood update across its consumer apps. Powered by a new custom-built architecture dubbed Proton Protocols (known internally as ProTUN), the update is now live in beta across Windows, iOS, iPadOS, Android, and Linux GUI.

This overhaul aims to improve connection stability and censorship resistance. It's a significant upgrade that further solidifies the provider's spot as one of the best VPN services on the market for privacy purists.

Alongside the stealthy new engine, the beta launch brings a host of highly requested functional tweaks. These include persistent ad-blocker statistics across app sessions, a new interactive globe map for visual server selection, and the highly anticipated Advanced Kill Switch.

The team at Proton VPN notes that the shift to this new protocol resolves multiple quality-of-life issues, paving the way for faster, more reliable connections and noticeably more responsive apps across all supported ecosystems.

![Proton VPN – best for privacy $2.99 per month Proton VPN – best for privacy $2.99 per month](https://cdn.mos.cms.futurecdn.net/z2HZEoVumkC2wAcoak6meP-200-80.jpg.webp)

**Proton VPN – best for privacy** 

The popular privacy-first VPN continues to invest in delivering the best Linux VPN possible. Before adding support for its Stealth protocol, the provider has been upgrading its apps with features like split tunneling, better stability across the board, and broader distro compatibility. Subscriptions start from the equivalent of **$2.99 per month** and are all protected by a 30-day money-back guarantee.

## What is the Advanced Kill Switch?

A standard VPN kill switch is a failsafe that cuts your internet connection if your VPN server unexpectedly drops, preventing your real IP address from leaking. Made possible by the new architecture, the Advanced Kill Switch takes this a step further by operating as a strict, permanent firewall.

As Proton explains, the Advanced Kill Switch functions like a regular failsafe if your connection drops, but it additionally blocks all internet access entirely unless you are actively connected to the VPN. This strict block remains active even if you restart your device.

Platform compatibility for the new feature is currently slightly fragmented. As of the current beta, the Advanced Kill Switch is strictly supported on Windows, iOS, and Linux GUI. It is not available for macOS, Linux CLI, Android TV, or Apple TV.

Android users have a slightly different setup. Google's operating system features built-in "Always-on VPN" and "Block connections without a VPN" toggles. Because of these native OS settings, Android operates very similarly to the Advanced Kill Switch out of the box, even if it isn't utilizing the exact same backend code.

Crucially, Proton has also fixed a long-standing annoyance with regular kill switches. You can now reliably connect to local LAN devices, like network printers, and use Apple CarPlay even with the standard or Advanced Kill Switch enabled.

## A Rust-based core to beat censorship

The shift to Proton Protocols is a fundamental rewrite of how the apps operate. Historically, Proton used the standard wireguard-go implementation. While secure, that code didn't integrate seamlessly with the native languages used to build the provider's mobile apps, like Kotlin for Android and Swift for iOS.

To fix this, Proton has built a new framework in Rust. At its core is *libpvpnclient*, a platform-independent WireGuard implementation that makes it easier to deploy updates and debug issues consistently across desktop and mobile.

This unified approach gives Proton much more flexibility to dodge roadblocks set up by authoritarian regimes. The update has immediately brought the provider's anti-censorship Stealth protocol to the Linux GUI app.

The shift to ProTun also lays the critical groundwork for a future networking layer called *muon*, which will eventually hide VPN API connections from internet service providers to defeat SNI snooping, and sets the stage for post-quantum cryptography.

Antonio Cesarano, Product Lead at Proton VPN, explains that *libpvpnclient* and*muon* together form a new platform that gives engineers far more flexibility.

"This allows us to experiment safely with improvements in connection stability, battery usage, and resilience, and prepares the groundwork for future technologies, like stronger anti-censorship techniques and post-quantum cryptography," said Cesarano.

Users who want to test the new architecture can opt into the beta program via the settings menu in their respective apps.

***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds. Make sure to click the Follow button!*

Sign up for breaking news, reviews, opinion, top tech deals, and more.

![Rene Millman](https://cdn.mos.cms.futurecdn.net/DXDNjzRkphApxN8f5SooCA.png)

Rene Millman is a seasoned technology journalist whose work has appeared in The Guardian, the Financial Times, Computer Weekly, and IT Pro. With over two decades of experience as a reporter and editor, he specializes in making complex topics like cybersecurity, VPNs, and enterprise software accessible and engaging.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

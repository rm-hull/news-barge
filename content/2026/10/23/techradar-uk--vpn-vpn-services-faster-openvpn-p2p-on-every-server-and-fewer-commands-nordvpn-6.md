---
title: 'Faster OpenVPN, P2P on every server, and fewer commands: NordVPN 6.0 lands
  on Linux'
source_url: https://www.techradar.com/vpn/vpn-services/faster-openvpn-p2p-on-every-server-and-fewer-commands-nordvpn-6-0-lands-on-linux
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-23T17:06:19Z'
published: '2026-10-23T00:00:00Z'
description: Version 6.0.0 moves obfuscated servers to NordWhisper, speeds up OpenVPN
  on modern kernels, and clears out legacy commands
image: https://cdn.mos.cms.futurecdn.net/KJBGvudKDPik3xjFe4guxF-1920-80.jpg
categories:
- Technology & Software
people:
- NordWhisper
locations:
- NordWhisper
organisations:
- CLI
- DCO
- Linux Mint
- NordLynx
- NordVPN
- NordWhisper
- OpenVPN
- P2P
---

![NordVPN](https://cdn.mos.cms.futurecdn.net/KJBGvudKDPik3xjFe4guxF-1920-80.jpg)

* **NordVPN 6.0.0 for Linux moves its obfuscated servers onto the in-house NordWhisper protocol.**
* **OpenVPN connections should get faster on newer kernels, and P2P now works on every standard server.**
* **Several legacy commands have been retired, so anyone relying on scripts should check before updating.**

NordVPN has pushed out version 6.0.0 of its Linux app, dated October 22, 2026, and the jump to a new major version number feels earned.

The update reworks how obfuscation works, speeds up OpenVPN on newer kernels, and trims a handful of legacy commands from the CLI.

It’s the latest in a long run of Linux upgrades from the provider. Back in August, version 5.3.0 began installing the GUI app automatically alongside the command-line daemon.

## NordWhisper takes over obfuscation

The biggest change is that NordVPN’s obfuscated servers now run on NordWhisper rather than OpenVPN XOR. Choosing NordWhisper switches obfuscation on automatically, so the old nordvpn set obfuscate command has been removed entirely.

NordWhisper is NordVPN’s own censorship-resistant protocol, launched in January 2025 and aimed at networks that actively block VPNs, such as some workplaces, schools, public Wi-Fi, and heavily censored regions. Until now, using obfuscated servers meant switching to OpenVPN.

The nordvpn set protocol command now picks the technology and protocol in one go; for example, nordvpn set protocol openvpn\_udp.

## Faster OpenVPN and P2P everywhere

OpenVPN has been bumped to version 2.7.7, and Data Channel Offload (DCO) now works out of the box on Linux kernel 6.16 or newer. DCO hands OpenVPN’s data handling to the Linux kernel itself, avoiding slow transfers between kernel space and user space, and the driver was upstreamed into the 6.16 kernel.

OpenVPN still has ground to make up on NordLynx, NordVPN’s WireGuard-based protocol. In TechRadar’s testing, NordLynx consistently hit 780-950+ Mbps, while NordVPN’s OpenVPN implementation managed 109-173 Mbps.

The dedicated P2P server group has also gone, because every regular server now supports P2P, so torrent users can simply pick a location. NordVPN has stopped labelling virtual servers too, explaining that “sometimes a server is just a server."

## Check your scripts before updating

The cleanup is where power users should pay attention. The outdated threatprotectionlite, tplite, tpl, and cybersec aliases have been removed, along with the old whitelist alias for allowlist. Real-time protection is now enabled with nordvpn set protection on. Auto-connect also can no longer target a specific server number, so you’ll need to choose a country, city, server group, or the fastest server instead.

On the fixes front, port forwarding on dedicated servers now works with Meshnet and LAN discovery enabled, nordvpn set defaults properly restores every setting, and the tray Pause menu on Linux Mint works again. LAN discovery also gains multicast and SSDP support, and screen reader navigation has been improved further.

Unlike NordVPN’s other apps, the Linux version doesn’t update automatically. On Debian-based distros, run sudo apt-get update followed by sudo apt-get install nordvpn. If you’re shopping around, our best Linux VPN guide has more options.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

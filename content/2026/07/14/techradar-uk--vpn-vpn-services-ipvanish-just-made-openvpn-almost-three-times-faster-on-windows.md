---
title: IPVanish just made OpenVPN almost three times faster on Windows — but there's
  a catch
source_url: https://www.techradar.com/vpn/vpn-services/ipvanish-just-made-openvpn-almost-three-times-faster-on-windows-but-theres-a-catch
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-14T17:25:21Z'
published: '2026-07-14T00:00:00Z'
description: High-Speed Mode brings OpenVPN Data Channel Offload to the Windows app,
  though it won't work alongside the Scramble option
image: https://cdn.mos.cms.futurecdn.net/uRjGLuUVadcWwMQTmRQuZF-2000-80.jpg
---

![IPVanish VPN running on a Macbook Pro](https://cdn.mos.cms.futurecdn.net/uRjGLuUVadcWwMQTmRQuZF.jpg) 

- **IPVanish added OpenVPN Data Channel Offload (DCO) to its Windows app**
- **Internal testing recorded download increases of up to 196%**
- **The feature cannot be used at the same time as OpenVPN Scramble**

IPVanish has released a new Windows client built around High-Speed Mode, the provider's implementation of OpenVPN Data Channel Offload (DCO). The company claims the feature lifts OpenVPN download speeds by up to 196%.

OpenVPN remains one of the most widely supported protocols in the industry, prized for its maturity and its ability to work almost anywhere. Its weakness has always been pace, which is why so many of the best VPN services now steer users towards WireGuard by default.

OpenVPN DCO addresses this problem. It moves the heavy lifting of encryption out of the app and into the deepest core of the operating system, cutting latency and easing CPU load without changing the protocol's security.

IPVanish has also swapped its Windows OpenVPN cipher from AES-256-CBC to AES-256-GCM, a change it says trims 32% off the time needed to connect to a server.

OpenVPN DCO remains an exclusive for Windows users. As the provider confirms to TechRadar, "OpenVPN DCO isn't possible on macOS, iOS, or Android. Those operating systems have locked-down kernels."

## What IPvanish's High-Speed Mode actually changes, and how to use it

 ![IPVanish's High-Speed Mode settings on Windows](https://cdn.mos.cms.futurecdn.net/EX4uYNkLhk7S85kgbrdNyn.png) 


Standard OpenVPN shuttles data back and forth between the VPN app and the operating system. Every one of those handovers costs time. DCO keeps the data channel closer to the Windows networking layer instead, so encrypted traffic moves through the system with fewer stops.

IPVanish tested servers in New York, London, Berlin, and Tokyo, three times a day across three consecutive days. Averaged out, downloads improved by 131% on TCP and 196% on UDP, while uploads rose 34% and 101% respectively.

"IPVanish is already known for offering fast VPN speeds, and today we're raising the bar for Windows OpenVPN," said Subbu Sthanu, General Manager, Consumer Cybersecurity at IPVanish, adding that streamers, gamers, and remote workers should all feel the difference.

You can turn the feature on by updating your Windows app and going to the OpenVPN protocol in the Settings tab.

One catch is that High-Speed Mode is not compatible with OpenVPN Scramble — IPVanish's obfuscation feature that disguises your VPN traffic to slip past networks that block it. Turn one on, and you lose the other. For anyone connecting from a school, an office, or a country that filters VPNs, Scramble is probably the more important feature.

## Which other VPNs offer OpenVPN DCO

ExpressVPN was among the first providers to unveil OpenVPN DCO in March 2025, claiming a 2,000% jump in UDP performance. Windscribe also added DCO on Windows at the same time, recently extending it to Linux, too.

Norton VPN followed in September 2025, citing doubled speeds and 15% lower latency.

Surfshark, NordVPN, and PrivadoVPN all ship a DCO adapter in their Windows clients, too. It's still a short list, with most providers betting on WireGuard instead.

![Monica J. White](https://cdn.mos.cms.futurecdn.net/6AQ4y5nzk8kQ47Yp69GERj.jpg)

Monica is a tech journalist with over a decade of experience. She writes about the latest developments in computing, which means anything from computer chips made out of paper to cutting-edge desktop processors.

GPUs are her main area of interest, and nothing thrills her quite like that time every couple of years when new graphics cards hit the market.

She built her first PC nearly 20 years ago, and dozens of builds later, she’s always planning out her next build (or helping her friends with theirs). During her career, Monica has written for many tech-centric outlets, including Digital Trends, SlashGear, WePC, and Tom’s Hardware.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: Apple's Private Relay tool can leak users' IP addresses — with OnionBrowser
  also affected
source_url: https://www.techradar.com/pro/security/apples-private-relay-tool-can-leak-users-ip-addresses-with-onionbrowser-also-affected
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-06T10:48:56Z'
published: '2026-08-06T00:00:00Z'
description: While Apple is looking into it, some browser makers have already made
  their moves.
image: https://cdn.mos.cms.futurecdn.net/pVCXKrhThqmUjYVSZBjV5Z-2560-80.jpg
---

![Hands on a laptop with overlaid logos representing network security](https://cdn.mos.cms.futurecdn.net/pVCXKrhThqmUjYVSZBjV5Z.jpg) 

- **Researchers Talal Haj Bakry and Tommy Mysk found three WebKit flaws leaking real IPs despite iCloud Private Relay**
- **DNS prefetching, WebAuthn origin requests, and WebTransport bypass proxy settings, exposing users across all Apple browsers**
- **Tor and Psylo browsers issued fixes; Apple has not confirmed a patch but is reviewing the report**

WebKit, Apple’s engine that powers all web browsers in its ecosystem, contained multiple flaws that helped leak the IP addresses of users who paid to keep them hidden.

This is according to security researchers Talal Haj Bakry and Tommy Mysk who noted they had found “three WebKit features that bypass the proxy configuration and send traffic directly from the device instead,” they wrote.

“DNS prefetching resolves hostnames through the device’s normal DNS path, which reveals the user’s real DNS servers instead of the proxy’s. Available since iOS 26.0; WebAuthn Related Origin Requests make the operating system’s credential service fetch a validation file directly from the device. This exposes the device’s real IP address. Available since iOS 18.0; WebTransport opens a direct HTTP/3 connection and bypasses the proxy, which also exposes the device’s real IP address. Available since iOS 26.4," the researchers said.

## Private Relay

While the bugs are in WebKit, the leaks come via Private Relay - a privacy feature available with iCloud+ that hides a user’s IP address and encrypts Safari web traffic. Private Relay does not work like a VPN, and does not mask the traffic flowing through other apps and programs - it just handles browser traffic.

Since WebKit is mandatory for all browsers running in Apple’s ecosystem, the vulnerability affects all of them. Some, including Tor and Mysk’s very own Psylo browsers, have already issued fixes.

Apple, on the other hand, has not yet confirmed a fix, or even that it was working on one. It did say, according to***404 Media*, that it was looking into the research report.

The researchers built a dedicated website where users can check if Private Relay is working as intended or still leaking the actual IP address into the wild.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

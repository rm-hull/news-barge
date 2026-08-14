---
title: Hundreds of fake Chrome VPN extensions impersonating NordVPN, Proton, and more
  caught hijacking your traffic
source_url: https://www.techradar.com/vpn/vpn-services/hundreds-of-fake-chrome-vpn-extensions-impersonating-nordvpn-proton-and-more-caught-hijacking-your-traffic
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-14T17:05:43Z'
published: '2026-08-14T00:00:00Z'
description: Socket found 737 extensions posing as trusted VPNs while pushing every
  browser request through proxies run by a single operator
image: https://cdn.mos.cms.futurecdn.net/ZfhFwGtGeLFq7LEuTgCMbD-1920-80.jpg
---

![Silhouette of a hand holding a padlock infront of the google chrome logo](https://cdn.mos.cms.futurecdn.net/ZfhFwGtGeLFq7LEuTgCMbD.jpg) 

- **Socket's Threat Research Team found 737 fake VPN and proxy extensions on the Chrome Web Store, with more than 75,000 combined installs**
- **The add-ons pose as trusted names like Proton VPN and NordVPN while routing your entire browser session through proxies run by one operator**
- **Hundreds are still live, so it's worth checking your browser now and removing anything suspicious**

A new investigation has exposed a huge cluster of counterfeit VPN extensions that promise privacy while rerouting your traffic.

Socket's Threat Research Team said it identified 737 free VPN and proxy extensions published across at least 40 Chrome Web Store developer accounts. More than 27o of these impersonate 66 of the best VPN services and privacy brands, including big names like NordVPN and Proton VPN.

Between them, the extensions racked up more than 75,000 installs, mostly among Russian-speaking users hunting for ways to reach blocked services.

If you use Chrome and rely on a browser add-on to stay private, it's worth making sure the one you installed is a genuine product from a real provider rather than one of these lookalikes.

## What the researchers found

Socket's team traced the whole network back to a single Russian VPN subscription business trading as Myxa VPN.

The researchers linked the extensions using a shared analytics account, clustered domain registrations, common hosting, and leaked Windows build paths pointing to one project folder. The free extensions appear to act as a funnel, nudging users toward a paid subscription.

Some of the paid promises were pure fiction. Socket says the premium tiers advertised servers in countries like Japan, Singapore, and Australia, but when it tested 200 premium hostnames across 40 domains, none returned an A record, meaning those servers simply did not exist.

Socket’s Threat Research Team found 737 Chrome VPN extensions in one campaign. 274 impersonated trusted brands, while 520 routed all browser traffic through shared infrastructure.The campaign’s paid plan listed 200 server hostnames. Not one resolved.[https://t.co/Nwz02e3ncbAugust](https://t.co/Nwz02e3ncbAugust) 11, 2026


The core trick is the same across nearly every extension. Once you press Connect, everything you browse gets pushed through a server the operator controls, with no per-site exceptions.

It adds no encryption, so it isn't doing the protective work a real VPN would. Worse, 104 extensions resolved their proxy addresses through Cloudflare or Google DNS-over-HTTPS and handed Chrome a raw IP, a technique that makes the operator's servers harder to block or spot.

## Why fake VPN are dangerous, and how to stay safe

Sitting in the middle of your traffic gives the operator a clear view. Socket says the setup lets whoever runs the proxy observe the websites you visit, TLS SNI metadata, your source IP address, and any data sent over unencrypted HTTP. That means anything you type into a non-HTTPS page, including logins, could be exposed.

Socket doesn't know whether this data has actually been collected or misused, but the fact that it can be is the problem. It's the same pattern behind earlier warnings about fake VPN extensions in the Chrome Web Store and Google's own alerts about spyware posing as VPN apps.

Google has already acted, but not completely. By the time Socket collected its data, 221 of the 737 extensions had been removed, while 516 remained listed, so the threat hasn't fully gone away.

If you think you installed one, the advice from Socket is straightforward. Remove the extension immediately, then check that Chrome's proxy configuration has returned to normal and change any credentials you entered on non-HTTPS sites while it was active. You can review your proxy settings by heading to your browser settings and searching for "proxy."

***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds. Make sure to click the Follow button!*

![Monica J. White](https://cdn.mos.cms.futurecdn.net/6AQ4y5nzk8kQ47Yp69GERj.jpg)

Monica is a tech journalist with over a decade of experience. She writes about the latest developments in computing, which means anything from computer chips made out of paper to cutting-edge desktop processors.

GPUs are her main area of interest, and nothing thrills her quite like that time every couple of years when new graphics cards hit the market.

She built her first PC nearly 20 years ago, and dozens of builds later, she’s always planning out her next build (or helping her friends with theirs). During her career, Monica has written for many tech-centric outlets, including Digital Trends, SlashGear, WePC, and Tom’s Hardware.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

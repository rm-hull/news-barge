---
title: Tor VPN turns one, and anti-censorship and stability take center stage
source_url: https://www.techradar.com/vpn/vpn-privacy-security/tor-vpn-turns-one-and-anti-censorship-and-stability-take-center-stage
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-10T19:07:28Z'
published: '2026-09-10T00:00:00Z'
description: After a year of real-world testing, the Tor Project is doubling down
  on circumvention and reliability instead of commercial-style features
image: https://cdn.mos.cms.futurecdn.net/U24bAE3CMv9iXcbJEMwZta-722-80.png
---

![Tor VPN Beta app on Android phone, promo image](https://cdn.mos.cms.futurecdn.net/U24bAE3CMv9iXcbJEMwZta.png) 

- **The Tor Project's Android VPN marked its first year** 
- **The provider confirms a pivot toward circumvention and reliability**
- **Adoption has been strongest in heavily censored regions**

One year after the Tor Project quietly rolled out Tor VPN Beta, the team behind the anonymity network has shared what it learned, and the message is clear: people are reaching for it to unblock the internet.

The app, which is Android-only for now, was designed to stretch Tor's privacy protections beyond the browser and across an entire device. When it soft-launched last autumn, that primary use case became clear almost immediately, and it has steered how the project prioritizes its work ever since.

Unlike the usual best VPN services, Tor VPN was never built to win speed tests. It routes traffic through the volunteer-run Tor network rather than a company's own servers, trading raw performance for a very different kind of privacy.

 ![Leave No Trace logo](https://cdn.mos.cms.futurecdn.net/Z7QHFc4GHoMhdps5XmntoC.png) 


**NEW**:** Leave No Trace** — A weekly newsletter on digital privacy and online surveillance.

Leave No Trace investigates the companies and governments putting our digital freedom at risk — and the people fighting back.

📩 Subscribe now to get every edition delivered to your inbox every Friday, launching this September.

## What makes Tor VPN different

Instead of pushing every app through a single shared tunnel, Tor VPN gives each app its own Tor circuit and exit IP, so activity in one app cannot easily be linked to another.

The Tor Project frames this as a kind of "per-app pseudonymity," an idea lifted directly from the anti-tracking design of Tor Browser.

Under the hood, the app runs on Arti, Tor's next-generation implementation written in Rust, which brings safer memory handling and a more modern codebase than the older C-based tools. A Rust tunnelling layer called Onionmasq handles the low-level plumbing, capturing device traffic and feeding it into the network.

## A year of hardening, and what's coming next

Much of the past 12 months went into stability rather than flashy additions. The team credits the Arti foundation with fewer crashes and better handling of shifting network conditions, and successive beta releases have steadily chipped away at bugs.

The project also passed an independent security review. As TechRadar reported, a Cure53 penetration test found no fundamental flaws in how Tor VPN routes traffic or builds its tunnels, leaving only lower-level issues to patch.

A year ago, we soft-launched Tor VPN Beta as a way to extend Tor's privacy protections beyond the browser to an entire Android device. Since then, we've been able to learn from how people are actually using it in real-world scenarios. Learn more about what makes our per-app…September 9, 2026


On the circumvention side, the team added WebTunnel bridges, which disguise Tor traffic as ordinary encrypted web traffic and make connections harder to detect and block.

Engagement has been strongest in heavily censored regions such as Iran and Turkmenistan, in fact, a notable contrast to Tor Browser's more Global North audience.

The project also made its builds reproducible and brought the app to F-Droid, so users can verify what they are running and update without leaning on Google Play.

Now, the roadmap leans into building on the features users rely on most.

The Tor Project says it will keep sharpening circumvention in restrictive environments, refine the interface to reduce risky mistakes, and port more of Arti's missing performance features, such as congestion control, into the mobile experience.

Exit selection, which tripped up testers who really needed bridges, is also being reworked.

## Why use Tor VPN, and how

 ![Three smartphones over a blue and purple background, each running the Tor VPN app.](https://cdn.mos.cms.futurecdn.net/F37f7g9znzKUVD2X6e62pj.jpg) 


Tor VPN suits anyone who wants device-wide anonymity that a standard provider cannot match, especially people living with everyday network restrictions. I

If you are mainly after speed and streaming, one of the best mobile VPN apps is probably a better fit, as one hands-on test clocked Tor VPN at just 3 to 4 Mbps.

It's worth stressing that this is still beta software. The Tor Project explicitly warns it is not suitable for high-risk users yet, and some Android device identifiers can still leak.

To try it, head to the Tor Project's download pages, where you can grab it as an APK, from the Google Play Store, or now via F-Droid.

***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds. Make sure to click the Follow button!*

![Monica J. White](https://cdn.mos.cms.futurecdn.net/6AQ4y5nzk8kQ47Yp69GERj.jpg) 

Monica is a tech journalist with over a decade of experience. She writes about the latest developments in computing, which means anything from computer chips made out of paper to cutting-edge desktop processors.

GPUs are her main area of interest, and nothing thrills her quite like that time every couple of years when new graphics cards hit the market.

She built her first PC nearly 20 years ago, and dozens of builds later, she’s always planning out her next build (or helping her friends with theirs). During her career, Monica has written for many tech-centric outlets, including Digital Trends, SlashGear, WePC, and Tom’s Hardware.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

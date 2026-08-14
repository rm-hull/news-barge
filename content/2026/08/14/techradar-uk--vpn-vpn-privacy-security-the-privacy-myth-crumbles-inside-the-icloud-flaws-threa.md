---
title: 'The privacy myth crumbles: Inside the iCloud+ flaws threatening Apple''s most
  valuable promise'
source_url: https://www.techradar.com/vpn/vpn-privacy-security/the-privacy-myth-crumbles-inside-the-icloud-flaws-threatening-apples-most-valuable-promise
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-14T13:35:14Z'
published: '2026-08-14T00:00:00Z'
description: 'Recently uncovered bugs in Private Relay and Hide My Email have exposed
  a glaring truth: no single company can act as your sole privacy shield'
image: https://cdn.mos.cms.futurecdn.net/fFoMeDF6W3WoQiiwUufqzR-2560-80.png
---

![Guy looking at an orange iPhone screen in his bedroom, Leave No Trace logo on top left](https://cdn.mos.cms.futurecdn.net/fFoMeDF6W3WoQiiwUufqzR.png) 

For years, many assumed that buying an Apple device guaranteed out-of-the-box privacy protection. However, this reputation is beginning to unravel.

Last week, researchers found that Apple’s iCloud Private Relay tool — a paid add-on feature that encrypts Safari browser traffic to hide a user's IP address — could leak the very detail it’s expected to protect.

These revelations come about a month after 404 Media reported that Hide My Email, another feature included in the paid iCloud+ subscription, also leaked users’ real email addresses. While Apple has now issued a patch, it only did so after the news broke, despite reportedly being aware of the flaw for at least one year.

The situation raises a critical question: can 'marketing privacy’ ever match technical reality? And if we cannot rely solely on Apple’s tools, what can we do to really protect our privacy online?

## iCloud Private Relay's flaws: How the IP leak unfolded

Apple markets iCloud Private Relay as a feature designed to protect your privacy. By securing your traffic when you browse on Safari, the company claims that "no single party — not even Apple — can see both who you are and what sites you're visiting."

To achieve this, the feature is supposed to route your requests through two separate proxy servers, or relays. This means that the second relay — the one that connects you to the website — can't see your real IP address or original DNS request.

That is what should happen in theory. However, recent findings by security researchers Talal Haj Bakry and Tommy Mysk suggest otherwise.

The iOS developers came across a series of issues in Apple's web browser engine by chance. In June, a user of their Psylo browser — a privacy-first app for iPhone and iPad specifically designed to defeat browser fingerprinting — contacted them to report DNS leaks.

 ![VPN Shield Security. Phone Concept - stock photo](https://cdn.mos.cms.futurecdn.net/v8LYyvBfpYanyKNXKLA8RF.jpg) 


While iCloud Private Relay functions as a proxy limited to Safari browsing, a VPN operates at the operating system level. By encrypting network traffic across the entire device rather than just a single browser, a VPN ensures that all application data, background processes, and connections are protected behind a system-wide encrypted tunnel.

Not only did the duo identify the origin of the DNS exposure, but they also found two additional leaks while investigating. Crucially, neither leak was the fault of their own app. “The problem is not within our implementation, but it’s a systemwide issue in the iOS infrastructure,” Mysk told TechRadar.

The first vulnerability involves **DNS prefetching**, a feature designed to speed up browsing. According to their tests, Safari was incorrectly resolving domain queries outside the secure proxy tunnel, leaking a user’s real DNS server.

The second leak is more troubling and concerns what’s known as **WebTransport**, a protocol designed to enable faster communication between a web browser and a website. Researchers found it was exposing the user’s real IP address — the very detail users believed they were masking by using Private Relay.

Similarly, Bakry and Mysk discovered that the **passkey system** — the framework that allows for passwordless logins — also bypasses the proxy and reveals users’ real IPs.

The impact of these leaks is profound for everyday users. The leaks allow third-party trackers to easily profile users and completely shatter the core promise of iCloud Private Relay, Mysk explained.

While Apple works on patching these flaws in its ecosystem, Psylo’s developers found an emergency, albeit limiting, solution for their users. They simply disabled these features (like passkeys) by default.

However, as Mike Tigas, the creator of OnionBrowser, told 404 Media, the issues are "entirely based on how iOS and WebKit work and solely in Apple's hands."

 ![Leave No Trace logo](https://cdn.mos.cms.futurecdn.net/Z7QHFc4GHoMhdps5XmntoC.png) 


**NEW**:** Leave No Trace** — A weekly newsletter on digital privacy and online surveillance.

Leave No Trace investigates the companies and governments putting our digital freedom at risk — and the people fighting back.

📩 Subscribe now to get every edition delivered to your inbox every Friday, launching this September.

## Hide My Email flop: How the anonymous mask cracked

As the name suggests, Hide My Email is a tool that should "keep your personal email private" by letting users generate a new, anonymous email address to use when signing in or creating a new account. Unfortunately, however, it failed to deliver on that promise for at least the last twelve months.

The founders of EasyOptOuts, Tyler Murphy and Ben Weiner, first noticed they could see the real email address of Hide My Email users in June 2025. The leak was triggered by an email being automatically rejected as spam.

"While we were investigating those bounce issues to try figuring out why emails weren't being delivered, we noticed that we were seeing our customers’ real email addresses in addition to their Hide My Email addresses in the bounce logs," Murphy told TechRadar.

 ![A screenshot showing Hide My Email in the Mail app](https://cdn.mos.cms.futurecdn.net/NhJKejfFerSum2SW4TXEkX.jpg) 


They reported the bug to Apple and waited for the Big Tech giant to patch it. After confirming the fix last March, Murphy and Weiner found it was still exploitable and contacted Apple again. Three additional months and no resolution led the duo to reveal the issue to the media in the hope of a quicker response.

The tactic worked, and Apple released a patch on July 7, a week after the news came out. While Murphy welcomes the security update, he still believes that the risks for users aren’t over.

"Even after the Hide My Email bug is fixed — and even after the Private Relay bug gets fixed in the future — data that was leaked in the past will still be stored by third parties," Murphy told TechRadar, urging Apple to notify all potentially affected users about the leak as soon as possible.

## Apple's privacy fails: how we got here

These two incidents reveal cracks in the Apple ecosystem — something that clashes with the privacy promises made to users when they buy a new device.

Make no mistake: bugs in software are inevitable and always will be. That's not the point. According to Mysk, the problem is how the company reacts to fix it.

"The last security bug that we reported to Apple, which we deemed severe, took Apple around seven months to fix. In this circumstance, it affects our product and our users, and we didn't want to wait that long," Mysk told TechRadar.

Re: Responsible DisclosureWe found ourselves in a bit of a dilemma with these DNS and IP leaks in WebKit and how to handle them responsibly.We first became aware of a DNS leak in Psylo in late June 2026 after a user reported it. During our investigation, we found two… [https://t.co/5kFu0jtUsJAugust](https://t.co/5kFu0jtUsJAugust) 5, 2026


Murphy from EasyOptsOuts agrees with Mysk and suggested the flaws could indicate structural reasons for concern.

"I’m personally a little surprised the [Hide My Email] issue ever even made it into production," Murphy said, questioning why there weren't more thorough tests to check that the product behaved correctly.

“This makes me worry that they're not careful enough, haven't been careful enough, and I wouldn't trust them to be careful enough in the future,” Murphy told me.

That said, experts agree that Apple's hardware and software ecosystem remains robust and, overall, more privacy-preserving and secure than many of its competitors.

The problem is not necessarily with the devices themselves, but in the illusion that a single company can act as a flawless, all-in-one privacy tool. No operating system is immune to vulnerabilities, and when these tools fail, users who rely solely on them are left exposed.

TechRadar has reached out to Apple for comment, but we are still waiting for a response at the time of publication.

Last week, Apple told 404 Media that it's still investigating the Private Relay issues and confirmed that the Hide My Email leak has been completely resolved. As the Private Relay flaws were made public on discovery, Apple has not had long to issue a fix.

## The privacy-by-design trap and the need for layered privacy protection

 ![A person holds a phone in front of their face.](https://cdn.mos.cms.futurecdn.net/mQuPZ7nVy7cErY9TZkc9v6.jpg) 


The problem goes beyond a single company's limitations. Lauren Hendry Parsons, Director of Communications at the Mozilla Foundation, sees these events as emblematic of a broader industry trend: tech companies using privacy as a point of competitive difference.

This means, Parsons told me, that companies and product manufacturers understand that improved digital privacy is what customers want. But the reality doesn’t always stack up.

"We want to see privacy-by-design products, but when you rely exclusively on a single provider or system to protect you, you’re effectively creating a potential single point of failure," she told TechRadar.

This aligns with what the cybersecurity world calls the Swiss cheese model. "The more slices that you have overlay on one another, the less likely it is that a hole will get through from end to end," Parsons said.

Whatever the root causes behind iCloud’s flaws are, the experts TechRadar spoke with agree that the ultimate takeaway for disenchanted Apple users is simple. While Apple devices remain strong on general system security, privacy protection must always be a multi-layered effort.

This wake-up call must have a lasting impact. For too long, many consumers have viewed Apple’s ecosystem as a bulletproof fortress. As those walls begin to shake, it is clear that a strong defense requires more than built-in security features from a single company. The need to bolster your digital arsenal with dedicated privacy tools has never been stronger.

***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds. Make sure to click the Follow button!*

![Chiara Castro](https://cdn.mos.cms.futurecdn.net/dBfKg5tPHAd74JPLWVCzQg.jpg)

Chiara is a multimedia journalist committed to covering stories to help promote the rights and denounce the abuses of the digital side of life – wherever cybersecurity, markets, and politics tangle up. She believes an open, uncensored, and private internet is a basic human need and wants to use her knowledge of VPNs to help readers take back control. She writes news, interviews, and analysis on data privacy, online censorship, digital rights, tech policies, and security software, with a special focus on VPNs, for TechRadar and TechRadar Pro. Got a story, tip-off, or something tech-interesting to say? Reach out to [chiara.castro@futurenet.com](mailto:chiara.castro@futurenet.com)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

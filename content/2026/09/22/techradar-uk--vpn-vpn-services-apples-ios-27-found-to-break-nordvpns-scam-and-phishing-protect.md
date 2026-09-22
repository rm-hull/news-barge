---
title: Apple's iOS 27 found to break NordVPN's scam and phishing protection — and
  it isn't the only privacy tool impacted
source_url: https://www.techradar.com/vpn/vpn-services/apples-ios-27-found-to-break-nordvpns-scam-and-phishing-protection-and-it-isnt-the-only-privacy-tool-impacted
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-22T19:45:20Z'
published: '2026-09-22T00:00:00Z'
description: Connectivity Assist conflicts with NordVPN’s real-time protection, NordVPN
  says
categories:
- Technology & Software
image: https://cdn.mos.cms.futurecdn.net/BKMEyLDxYRs8d9ASpx65R6-2401-80.jpg
---

![NordVPN app icon](https://cdn.mos.cms.futurecdn.net/BKMEyLDxYRs8d9ASpx65R6.jpg)

* **Apple's latest iOS update has been found to undermine NordVPN's anti-phishing tool**
* **The feature that causes the issue, Connectivity Assist, is turned on by default as part of the update**
* **According to NordVPN, the issues could have been prevented**

Apple's new iOS 27 operating system update is undermining NordVPN’s anti-phishing tool, leaving users exposed to privacy vulnerabilities, the VPN has warned.

Connectivity Assist, a Wi-Fi Assist feature included in Apple’s twentieth operating system release, conflicts with NordVPN’s real-time protection, preventing it from working properly, the provider has found.

What’s worse? The tool is enabled by default, meaning users may not even know. What's more, other privacy tools on your phone may also have been compromised.

## The problem with Connectivity Assist

![NordVPN](https://cdn.mos.cms.futurecdn.net/JdeooTDkg6kuSfeespr2Kj.png)

Connectivity Assist optimises your Wi-Fi connection by supplementing slow or unreliable Wi-Fi connections with mobile data, detecting connection issues, and redirecting requests to your mobile operator’s DNS servers instead.

However, when NordVPN’s anti-fraud protection blocks a phishing site, Apple may also interpret the failed connection as a Wi-Fi issue and switch to mobile data—outside the VPN’s protection—thereby compromising the functionality of the NordVPN tool.

The only option currently available to ensure full protection is to disable Connectivity Assistant, so it can’t switch to mobile data when real-time protection blocks a website.

Alternatively, you can choose only to enable real-time protection when using a VPN by disabling NordVPN’s ‘always on’ option - but this still leaves them unprotected when using mobile data - just now by choice.

“People are being made to choose between two things they shouldn't have to choose between, and there's no good way for us to fix it,” Laura Tyrylyte, Head of Public Relations at NordVPN, tells TechRadar.

## Can this be prevented?

Could Apple have helped resolve these issues before the release? Perhaps, according to the VPN representative. “Apple knew the feature interferes with DNS-based filtering before it shipped,” Tyrylyte notes. “Their own support page tells people running an ad blocker to switch Connectivity Assist for that network. Somebody spotted the conflict, it just didn’t get fixed.”

Users of Pi-hole, Firewalla, and other DNS-based filtering tools had previously reported the same behaviour, and Cloudflare's WARP also stopped blocking malicious sites following the update, NordVPN stressed.

Apple engineers have suggested alternative solutions in the forums, but these only work if users configure the DNS settings themselves, notes Tyrylyte.

“Deciding to treat deliberate filtering as a failed connection is a choice somebody made. They could have written it the other way: if a user-installed DNS service decides to resolve or block the query, leave that judgement alone,” Tyrylyte adds.

“Instead, the problem got handed to users, who now need to end up fielding the support tickets for something we can’t change,” she stresses.

NordVPN states that this is not the first time a change made by Apple to the network has compromised a security feature on iOS, with the VPN having to inform users.

In 2023, Apple’s VPN API contained vulnerabilities that disrupted NordVPN operations. “Both times users ended up having to pick between an Apple feature and their own protection, and both times Apple was the only one who could have prevented that,” Tyrylyte says.

“Apple makes the call, and we find out what the call was when the release lands, she stressed.

Whoever’s responsibility this is, one thing is for certain: it is users who stand to pay the highest price when tools quietly stop working. And reporting the issue in the press as a solution seems a poor substitute for preventing the problem in the first place.

Apple is yet to respond to a request for comment.

![Silvia Iacovcich](https://cdn.mos.cms.futurecdn.net/e3cAo9wuAWurJxj5eRkg8M.jpg)

Silvia Iacovcich is a tech journalist with over five years of experience in the field, including AI, cybersecurity, and fintech. She has written for various publications focusing on the evolving regulatory landscape of AI, digital behavior, web3, and blockchain, as well as social media privacy and security regulations.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

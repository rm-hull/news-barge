---
title: Federal bill would force VPN providers, ISPs, and DNS services to block foreign
  piracy sites — yet fuzzy location rules could trigger heavy-handed bans
source_url: https://www.tomshardware.com/software/vpn/federal-bill-would-force-vpn-providers-isps-and-dns-services-to-block-foreign-piracy-sites-yet-fuzzy-location-rules-could-trigger-heavy-handed-bans
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-26T11:25:40Z'
published: '2026-09-26T00:00:00Z'
description: Determining a user's location can be an exercise in quantum mechanics
  when VPNs are involved.
image: https://cdn.mos.cms.futurecdn.net/ZVVUo4RCLgjR5t8FXoXdx4-2560-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Tom
locations:
- France
- Spain
- U.S
- United States
organisations:
- ACPA
- Apple
- Cloudflare
- Google DNS
- Google News
- ISP
- OpenDNS
- PC
- RootedCON
- Tom's Hardware
- U.S. Congress
- VPN
- VPNs
---

![Digital skull and crossbones](https://cdn.mos.cms.futurecdn.net/ZVVUo4RCLgjR5t8FXoXdx4.jpg)

A week and change ago, the U.S. Congress saw yet another anti-piracy bill introduced, H.R. 10364, or by its full name, the American Copyright Protection Act of 2026 (ACPA). It would require internet service providers, DNS resolving services, and virtual private networks, or VPNs, to block foreign websites or services hosting pirated content. The full text for the bill is now public, and it stands out due to its targeting of foreign services and affecting connections "from the United States." That gets complicated pretty quick when VPNs and content delivery networks (CDNs) are in play.

In ACPA, a standard blocking order needs to be court-issued, but would apply in 14 to 30 days. There's a special case seemingly targeted at live-streaming of sports events and shows, or "time-sensitive events" in legal parlance, which can shorten the blocking deadline as a judge sees fit, so long as the first leak of copyrighted material appears within 24 hours after going live.

Blocking at the ISP and DNS level is relatively straightforward. The vast majority of users utilize their ISP's DNS, so not resolving a given domain if it's in the blocklist for its customers is simple enough. Some people, like yours truly, rely on external DNS servers like Google DNS, Cloudflare's 1.1.1.1, OpenDNS, or NextDNS. These too could ignore specific DNS resolution requests from incoming users in the States, the accuracy of geolocation notwithstanding.

Small ISPs and services with less than 100,000 monthly users and public networks are exempted, as are root DNS and top-level domain (TLD) providers. However, the bill does not specify an exact means of blockage, and it's possible that service providers, out of fear of liability, may well take a heavy-handed approach. It also makes no mention of protecting or nullifying encryption.

When it comes to people using VPNs to bounce their connection through another location, things get tricky, as the bill does *not* clearly state what "from the United States" means, and even the definition of "foreign" can get fuzzy. Determining those might well be an exercise in quantum superposition, since any of the below scenarios can be argued to technically fulfill a criteria. We conjured up a handful of possibilities, though we're sure creative techies can come up with many more:

* A connection to a VPN originates from the U.S.
* A VPN's endpoint resides in the U.S.
* A VPN's registered subscriber is a U.S. person, but they are currently outside the U.S.
* The user uses a VPN to a foreign country, but connects to a website that's behind a CDN — does the CDN endpoint count as a destination?
* Same, but the actual website is on U.S. soil despite being accessed from outside; is it "foreign" if the endpoint is?
* For multi-hop VPNs, which hop or hops count towards determining a destination, especially if the traffic passes through the U.S. at some point?
* A U.S. citizen in a boat in international waters using Starlink (a U.S. satellite ISP) counts as foreign?
* A U.S. citizen goes abroad and uses roaming; are they considered foreign due to their physical location, or within the U.S. because they are using stateside infrastructure?

Additional legal questions can be raised with other technological factors. The use of shared IPs in hosting services, or CGNAT implementations, can create obfuscation of the concepts of "destination" and "origin." Is a DNS provider using Oblivious DoH, where the server responds to a request but doesn't know who made it and vice versa, liable? How does Apple's iCloud Private Relay feature, which hides a connection's source and destination from each other, sit within the legal framework? And with encrypted DNS, how much is the ISP liable, since they can't see which domain the user requested?

The neutrality of third-party service providers has come under fire in jurisdictions like France and Spain, where rulings mostly went against claims of neutrality. Some were forced to often enable large-scale blocking, an action likely to trigger more than a few false positives. A Spanish court ruled against Cloudflare and RootedCON for their part in providing CDNs, resulting in mass IP blockings. Over in France, a court found that VPNs do have to comply with blocking orders despite their job as "technical intermediaries."

For what it's worth, ACPA is only one of multiple bills sitting in Congress in the "introduced" state, and currently appears to have no sponsors, scheduled hearings, or even markup. If foreign activities are any indication, though, broad legislation like this may have substantial unintended consequences.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

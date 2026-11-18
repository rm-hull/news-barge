---
title: Tor hit by major DDoS attack, forced to release emergency update to users
source_url: https://www.techradar.com/pro/security/tor-hit-by-major-ddos-attack-forced-to-release-emergency-update-to-users
source_site: TechRadar UK
source_slug: techradar-uk
description: Users are reporting slow and unresponsive Tor networks
image: https://cdn.mos.cms.futurecdn.net/hySqAcuSrjahcQDLNXaEwi-970-80.jpg
published: '2026-11-18T00:00:00Z'
scraped_at: '2026-11-18T20:32:21Z'
categories:
- Technology & Software
people: []
locations: []
organisations:
- Denial of Service
- Guard
- HSDir
- Reddit
- TechRadar Pro
- Tor Project
---

![Tor](https://cdn.mos.cms.futurecdn.net/hySqAcuSrjahcQDLNXaEwi-970-80.jpg)

* **The Tor Project releases urgent updates after large-scale DDoS attacks overwhelmed relay operators across the network**
* **Attackers flooded relays with circuit requests, causing resource exhaustion, degraded performance, and lost relay functionality**
* **Maintainers say the attacks are ongoing and adaptive, urging operators to upgrade immediately and watch for further fixes**

The Tor Project seems to be experiencing major Distributed Denial of Service (DDoS) attacks which have gotten so disruptive that they forced the release of an update in order to address it.

Now, Tor Project says “most relay operators” were affected by an ongoing DDoS attack.

“This release comes in rapid response to the ongoing DDoS attack on the network, which has affected most relay operators,” the patch notes read. “This is not an easy problem to address, as relays across the network are being overwhelmed by a massive flood of client circuits. We are actively evaluating additional defenses and so expect further releases in the near future.”

## Second patch

Tor is a privacy-focused network that routes internet traffic through multiple relays (servers operated by volunteers), allowing users to hide their identities and online activities. The relays work by receiving and forwarding encrypted traffic between users and other parts of the network, and are divided into three categories: Guard (or entry) relays (the first point of contact between a Tor user and the network), Middle relays (these pass traffic between them and add layers of separation), and Exit relays (these send traffic from the Tor network back to the regular internet and the user’s final destination).

The patch brings Tor to version 0.4.9.17 and includes a series of security fixes, including, according to the patch notes, one “especially important for relay DoS defenses related to IPv6 handling."

The project now urges relay operators to upgrade to the latest version as soon as possible, and to keep an eye out for additional updates. It did not share any details about the ongoing DDoS attack.

This doesn’t seem to be the first patch the Tor Project released in response to the DDoS attacks, either.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Approximately three weeks ago, Tor version 0.4.9.15 was introduced, also in response to attacks.

This version, however, seems not to have worked properly. “Tor relay operators are reporting renewed denial-of-service (DoS) attacks despite security mitigations introduced in Tor 0.4.9.15 on October 28,” a Reddit user said in a thread on “renewed DoS attacks”.. “On November 9, one operator reported that two relays lost their HSDir flags after attacks caused severe CPU and memory exhaustion. Another operator reported similar activity on November 10, including thousands of circuit creation requests per second.”

The operator said the reports suggest whoever is behind these attacks managed to bypass Tor’s recent protections. “The full scope of the attacks and their impact on the wider Tor network are not clear,” they said.

## Reddit activity

Reddit has quite a few threads from different Tor users complaining about nodes being saturated and the network being slow or outright unresponsive. On November 9, a person on the Tor Project’s forum said the attacker “successfully stripped the HSDir flag from two [of their] relays” in a few hours, and that one attack saw “high asymmetric egress and one saw high asymmetric ingress (although not nearly as much as the old attacks).”

Both relays lost their HSDir flags as a result.

At press time, no threat actors claimed responsibility for the attacks, so we don’t know who they are or what their motives are. What we do know is that the attacks appear persistent and adaptive, and that relay operators reported multiple waves of attacks and changes in attack patterns.

Whether or not the latest patch finally addresses the attacks in full, remains to be seen. The project maintainers seem to be confident about it.

“Thank you to all… except our attacker(s),” they said in conclusion.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

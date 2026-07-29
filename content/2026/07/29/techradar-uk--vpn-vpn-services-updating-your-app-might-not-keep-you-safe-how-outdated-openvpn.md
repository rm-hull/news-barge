---
title: 'Updating your app might not keep you safe: How outdated OpenVPN code leaves
  VPNs exposed'
source_url: https://www.techradar.com/vpn/vpn-services/updating-your-app-might-not-keep-you-safe-how-outdated-openvpn-code-leaves-vpns-exposed
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-29T17:26:27Z'
published: '2026-07-29T00:00:00Z'
description: Our audit of Windows VPNs uncovers a graveyard of old OpenVPN configurations,
  with more than 50% of apps using versions over a year old.
image: https://cdn.mos.cms.futurecdn.net/k3JwQfF5rbWQ7a3sXgYvGm-2000-80.jpg
---

![OpenVPN logo on left hand side, contrasted with an image of a grey graveyard on the right.](https://cdn.mos.cms.futurecdn.net/k3JwQfF5rbWQ7a3sXgYvGm.jpg) 

Trust your VPN software updates keep you safe? Believe that downloading the latest release protects you from most known threats?

You might be surprised to learn that there could be a set of invisible vulnerabilities lurking inside your state-of-the-art VPN. That's because more than half of Windows VPNs we analyzed include OpenVPN code that hasn’t been updated in over a year — potentially leaving you exposed to a wide range of security and performance threats.

OpenVPN is a protocol that determines how data is encrypted and routed between a user's device and a VPN server. Thanks to its open-source status, it became the industry's de facto standard, serving as the foundation for many commercial VPN services.

Because OpenVPN is developed as a separate open-source project, however, VPN providers often update their apps while leaving the bundled OpenVPN component unchanged. New interfaces, bug fixes, and major features may arrive regularly, but the code responsible for the fundamental VPN connection may be severely out of date.

## Cracking the kernel

This July, we audited 32 Windows VPN clients ranging from established, multinational companies to smaller, older and free apps, to check the OpenVPN version included in their latest release.

The results were shocking. A massive 56% (18 of 32) use an OpenVPN version that is more than **a year old**, 41% (14) use configurations that are over** two years old**, 22% (7) rely on code** more than four years old**. And a terrifying 12.5% (4) use code that is at least* five years old*.

Not all providers were equal. Perhaps unsurprisingly, many of the best VPNs — including NordVPN, Windscribe and Proton VPN — use OpenVPN releases as recent as April 2026. At the other end of the scale, Turbo VPN and VyprVPN continue to use OpenVPN 2.4.7 from April 2019.

It might seem logical that companies with greater commercial resources are the ones investing more into keeping the app's codebase up to date. But having significantly older versions of the OpenVPN protocol raises significant privacy and security concerns regardless.

## A variety of hidden risks

So is this really a big deal?

Marijus Briedis, CTO at NordVPN, tells TechRadar: “Because OpenVPN — like any project — regularly patches vulnerabilities, hardens its codebase, and improves performance, running a version that’s years behind might miss security components that current up-to-date versions offer.”

Jason Xu, senior app developer at Windscribe, argues that previously disclosed vulnerabilities could actually be more serious, precisely because they have been documented. “An attacker doesn’t even need to find a new bug; they can just read the changelog,” he notes.

Indeed, OpenVPN regularly releases Common Vulnerabilities and Exposures (CVEs): six vulnerabilities were registered in 2025, six in 2024, one in 2023, and one in 2022. This means providers with older versions likely did not adopt the upstream releases containing those fixes.

Of course, the risks have nuances. Running an older version does not necessarily mean an application is vulnerable to every newly discovered flaw. For example, if an older build does not include a feature which later caused a vulnerability, it is unaffected.

Briedis stressed that security can be maintained through other means, including backported patches, vendor fixes, configuration mitigations and/or removing vulnerable functions. However, he said the real concern is when none of those measures are in place and when there’s no visibility into whether they are.

The issues involved can be broad and numerous. Outdated dependencies, like running an older version of OpenSSL, are just some of the potential issues.

There is also a broader maintenance cost. According to Dr. Peter Membrey, Chief Research Officer at ExpressVPN, older versions can become increasingly difficult to integrate with current operating systems and cryptographic libraries. “Being several years behind can indicate a growing body of security, compatibility, and operational debt,” he says.

Ultimately, “the further behind you fall, the harder each upgrade gets,” Xu adds. “That’s the trap. Nobody decides to be five years behind; they just keep saying ‘next quarter’”.

## A question of stack

Adopting a new OpenVPN release is a fundamental change requiring compatibility testing across platforms, regression checks, staged rollouts, and validation that nothing breaks in the software stack — a process which often takes months to complete.

Because of that, VPN providers say they are not obliged to adopt every upstream release.

NortonVPN, which is in the process of moving to the cutting-edge OpenVPN version at the moment, explains that each update needs to be assessed and tested carefully to make sure it delivers clear benefits without introducing stability, performance, or compatibility issues for customers.

Indeed, Karolis Kaciulis, Leading System Engineer at Surfshark, agrees that a six-to-18-month delay can be reasonable provided critical vulnerabilities are addressed promptly.

Some VPN providers whose updates date back more than two years have cited specific reasons to justify the delay.

StrongVPN, for example, states that work on its proprietary internal protocol has postponed the planned update to OpenVPN 2.7. Meanwhile, ClearVPN claims to ensure security by applying its own security patches.

Finally, PureVPN states that it is staying with OpenVPN 2.6.12 because it has developed custom technologies based on that version and because OpenVPN 2.7 removes support for the Wintun driver.

## Time to DIY

So what can you do? Is it time to shun anyone not using the most recent version of OpenVPN?

Not necessarily. Many providers now use newer protocols like WireGuard by default, which generally benefit from more active maintenance.

In fact, several providers are in the process of phasing out OpenVPN support for faster, more agile protocols.

Proton VPN is one of the providers keeping pace, running one of the most recent OpenVPN builds on its Windows app. However, a spokesperson said that over time, the company "will start to phase out OpenVPN support in our client apps" while retaining the protocol on servers for legacy routers and older devices.

The spokesperson also noted that the protocol is "slow and bloated" in comparison to Proton VPN's Stealth and WireGuard protocols, though OpenVPN remains "robustly secure."

So whether you're using an app with the latest OpenVPN configuration or not, it might be worth switching protocols anyway.

But if you really want to know, you can audit your VPN by checking the client settings, diagnostic logs, or official release notes to confirm which version of OpenVPN your provider is using and when it was last updated.

A key red flag is protocol dependencies that are more than 12 to 18 months old without a documented security or compatibility reason as it may suggest that critical security updates have been delayed.

If you're still unsure, you can always contact your VPN provider's support team to receive more transparent info about timelines for protocol updates and security patches.

Ultimately, the risk to your security may well be limited. However, in the world of VPNs — where attention to detail in regards to security is the currency of providers — one might well ask: “Why not simply support the latest and most secure option?”

Why not indeed…

![Silvia Iacovcich](https://cdn.mos.cms.futurecdn.net/e3cAo9wuAWurJxj5eRkg8M.jpg)

Silvia Iacovcich is a tech journalist with over five years of experience in the field, including AI, cybersecurity, and fintech. She has written for various publications focusing on the evolving regulatory landscape of AI, digital behavior, web3, and blockchain, as well as social media privacy and security regulations.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

---
title: This Russian VPN has been accused of breaching its no-log policy — here's what
  we know
source_url: https://www.techradar.com/vpn/vpn-privacy-security/this-russian-vpn-has-been-accused-of-breaching-its-no-log-policy-heres-what-we-know
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-07T17:04:42Z'
published: '2026-08-07T00:00:00Z'
description: While SplitVPN claims the allegations are fabricated, the incident exposes
  the limits of no-log VPNs
image: https://cdn.mos.cms.futurecdn.net/v8LYyvBfpYanyKNXKLA8RF-2291-80.jpg
---

![VPN Shield Security. Phone Concept - stock photo](https://cdn.mos.cms.futurecdn.net/v8LYyvBfpYanyKNXKLA8RF.jpg) 

- **Split VPN has been accused of breaching its no-log policies**
- **It allegedly leaked 58M connection logs, which SplitVPN denies as its own**
- **Users trusting a no-log policy is not enough**

Russian SplitVPN (formerly NotVPN) has been accused of breaching its own no-log policy after a data leak exposed a MySQL database containing a variety of data linked to the service, including a staggering 58 million alleged connection logs.

While the VPN provider — whose service is widely used to bypass blocks in countries with heavy censorship — told TechRadar that any allegations it keeps logs are false, the incident highlights the limitations of no-logs policy when things go wrong.

Even with the best VPNs, no-log policies are often based on trust rather than verifiable safeguards, meaning they may not give users a clear picture of the risks users could face if their VPN were exposed to a breach — particularly in countries where criminal prosecution due to the illegal use of VPNs is real.

A no-logs VPN policy means a VPN pledges not to collect or share users' information, including search queries, websites visited, time spent on them, and downloads, while they are connected to one of its servers.

However, it remains difficult for users to verify these claims for themselves. That is why the most secure VPNs have their policies regularly audited by independent organisations, ensuring their privacy promises are genuine and not just a fabricated image.

## SplitVPN's alleged data breach

On July 21, a threat actor on the Altenen cybercrime forum distributed a 17 GB SQL database claimed to have been stolen from SplitVPN and which allegedly contained a staggering amount of connection logs alongside user records, devices and payments.

The research team at Mysterium VPN analysed the database and claimed part of it (known as 'deviceproxy') indeed contained around 58 million connection logs.

Although this consisted of anonymised metadata indicating which device had connected to which server and at what time rather than complete browsing histories, SplitVPN maintains that it does not retain such data in accordance with its no-logs policy.

 ![Graph with SplitVPN alleged data breach's findings (August 2026)](https://cdn.mos.cms.futurecdn.net/HqjssU4k7XjpM9ixd9QWNd.png) 


SplitVPN told TechRadar that while the leaked subscription metadata — including email addresses, users' countries of origin, subscription status, masked credit card information and device names — is authentic, the deviceproxy table instead is entirely fabricated.

"The third-party listing claims 58 million connection logs, but this is a fabrication added to inflate the price," a company spokesperson said.

"Because we do not generate or store device-server-timestamp mappings, any records claiming to show this are not from our infrastructure," they added. "The exposed data contains only basic account information, which fully aligns with our no-logs commitment."

SplitVPN added that immediately after discovering the breach, they changed all VPN server node IPs, rotated all access credentials and encryption keys, closed the vulnerability, and engaged external security specialists to audit their infrastructure. Operations have now returned to normal.

## The lesser of two evils

While it is arguably nearly impossible to independently verify the deviceproxy data’s authenticity, both scenarios present users with fundamental issues.

If allegations are true, the existence of these logs would directly contradict Split VPN's no-logs policy. When cross-referenced with the IP address of the most recent connection and hardware identifiers, these logs could be sufficient to determine who connected, from where, to which server, and when, putting millions of users in areas with heavy censorship at serious risk.

If claims are fabricated, users are still forced to rely on conflicting statements that they cannot independently verify, with leaked official data potentially causing concern amongst users living in countries where VPN usage is banned.

To ensure your privacy is respected, always look for a privacy policy audit and additional security features including kill switches, double VPN servers, and post-quantum encryption. Advanced technologies such as RAM-only servers or advanced cryptographic privacy can really make a difference. Ultimately, words pass, but technical expertise remains —especially when it’s your data that’s under threat.

![Silvia Iacovcich](https://cdn.mos.cms.futurecdn.net/e3cAo9wuAWurJxj5eRkg8M.jpg)

Silvia Iacovcich is a tech journalist with over five years of experience in the field, including AI, cybersecurity, and fintech. She has written for various publications focusing on the evolving regulatory landscape of AI, digital behavior, web3, and blockchain, as well as social media privacy and security regulations.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

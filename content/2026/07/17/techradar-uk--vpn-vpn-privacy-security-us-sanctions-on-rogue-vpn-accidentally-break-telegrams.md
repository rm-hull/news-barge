---
title: US sanctions on rogue VPN accidentally break Telegram's short links worldwide
source_url: https://www.techradar.com/vpn/vpn-privacy-security/us-sanctions-on-rogue-vpn-accidentally-break-telegrams-short-links-worldwide
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-17T17:21:10Z'
published: '2026-07-17T00:00:00Z'
description: A Montenegro-based domain registrar hit the entire t.me domain with a
  global suspension to comply with US sanctions
image: https://cdn.mos.cms.futurecdn.net/Zcpy2igVUaP9YqtCiCVXaE-1920-80.jpg
---

![The Telegram logo appears on the screen of a smartphone that rests on top of a laptop keyboard](https://cdn.mos.cms.futurecdn.net/Zcpy2igVUaP9YqtCiCVXaE.jpg) 

- **The US Treasury sanctioned First VPN Service for aiding ransomware gangs**
- **Complying with the sanctions, the .ME registry wrongly suspended Telegram's entire t.me domain**
- **The domain was restored roughly 19 hours later after Telegram CEO Pavel Durov flagged the issue online**

If you clicked a Telegram link on Monday and stared at a blank screen, you weren't alone. Every shortlink starting with 't.me' suddenly vanished from the global internet, breaking group invites, profile shares, and channel links for roughly a billion users worldwide.

But the outage wasn't caused by a technical glitch or a targeted cyberattack. Instead, it was the unintended collateral damage of a US government crackdown on a cybercriminal proxy network.

On July 13, the US Treasury Department's Office of Foreign Assets Control (OFAC) sanctioned the administrators of a rogue proxy network called First VPN Service (1VPNS), aiming to cut off infrastructure used by ransomware operators.

While anyone shopping for the best VPN expects privacy, First VPN actively courted cybercriminals with promises of total anonymity, leading European law enforcement to pull the plug on the service earlier in May.

As part of the new sanctions, the US Treasury published a list of web addresses associated with the VPN. Buried in that list was a link to First VPN's public Telegram support channel: t.me/FirstVPNService.

## A sledgehammer to crack a nut

 ![This photograph shows a laptop screen displaying the website of Europol featuring the First VPN service website with a message reading, "This service has been seized"](https://cdn.mos.cms.futurecdn.net/qp6PFkub49CUBhgFaHwjeQ.jpg) 


Because top-level domains operate under strict international compliance rules, domain registrars must act quickly when sanctioned entities use their infrastructure.

Identity Digital, the company managing the technical backend for the .me domain, confirmed that the t.me domain had been blocked at the request of OFAC.

However, because a domain registry cannot selectively disable a specific webpage or channel path — like a single Telegram group — the Montenegro-based registry Domain.Me applied a "serverHold" status to Telegram's entire t.me domain.

This sweeping action effectively erased the domain from the global Domain Name System (DNS). The core Telegram app continued to function, and the older telegram.me domain remained active, but the shortlinks the messaging platform is built upon went entirely dark.

## The swift resolution

The sudden shutdown prompted immediate action from Telegram's leadership.

Unaware of the backend domain hold, Telegram CEO Pavel Durov took to X to publicly ask the registrar for an explanation: "Hey @domainME, t.me links stopped working. Can you look into it?"

Once the sanctions issue was identified, Telegram scrubbed the offending channels from its platform. The registry operator subsequently verified the compliance and brought the domain back online.

"On 13 July, 1VPNS was included as a sanctioned entity by the US Department of the Treasury. A Telegram channel using the t.me domain was among 1VPNS identified infrastructure. Accordingly, the t.me domain was suspended," domain.Me confirmed in a statement__ __following the outage.

The registrar clarified that normal service resumed roughly a day later, after Telegram provided confirmation that it had removed its links and affiliations with 1VPNS. "We appreciate Telegram's prompt cooperation in resolving this matter," domain.Me added.

While the outage is now resolved, the incident highlights a glaring vulnerability in the modern web, where a single URL swept up in a government sanctions list can inadvertently silence an essential communication channel for millions.

*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds. Make sure to click the Follow button!*

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

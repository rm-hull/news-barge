---
title: FBI tip line and veterans crisis site among 350 federal web addresses exposing
  visitors to network spies, senator warns
source_url: https://www.techradar.com/pro/security/fbi-tip-line-and-veterans-crisis-site-among-350-federal-web-addresses-exposing-visitors-to-network-spies-senator-warns
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-25T23:13:06Z'
published: '2026-10-25T00:00:00Z'
description: 350 federal web addresses let network snoops see who visited
image: https://cdn.mos.cms.futurecdn.net/AboNpeASJNf5nBHAARoLnF-1920-80.jpg
categories:
- Technology & Software
- News & Politics
people:
- Chris Krebs
- Nick Andersen
- Ron Wyden
- Roskomnadzor
- Thomas Flagg
locations:
- D-Ore
- Russia
- US
organisations:
- Amazon Web Services
- Android 17
- Bureau of Indian Education
- CDC
- CDN
- CISA
- Cloudflare
- DHS
- DNS
- Defense Department
- Department of Veterans Affairs
- ECH
- ESNI
- Education Department
- FBI
- GSA
- Google
- ICE
- Justice Department
- NATO
- NIH
- OMB
- Pentagon
- Rewards for Justice
- SNI
- State Department
- TechRadar Pro
- UN
- USCIS
- VA
---

![A laptop with digitally inserted hack warnings around it](https://cdn.mos.cms.futurecdn.net/AboNpeASJNf5nBHAARoLnF-1920-80.jpg)

* **Sen. Ron Wyden wants CISA and OMB to require Encrypted Client Hello on federal websites and make it a federal contract condition**
* **His list of 350 CDN-hosted addresses without ECH includes the FBI tip portal, the VA's crisis line, and hotlines for whistleblowers and civil rights complaints**
* **ECH hides site names only alongside encrypted DNS, does nothing for server breaches, and is already blocked in Russia, where some listed embassy pages are aimed**

US Senator Ron Wyden (D-Ore.) wants the federal government to turn on a privacy feature that major web browsers have supported for three years, warning that hundreds of agency web addresses still broadcast the name of the site each visitor uses to anyone watching the network along the way.

In a letter to CISA acting director Nick Andersen and deputy federal chief information officer Thomas Flagg, Wyden asked the two agencies to require Encrypted Client Hello (ECH) across federal websites and to make ECH support a condition for cloud and network vendors seeking federal contracts.

The letter attaches a list of 350 executive branch web addresses that use content delivery networks (CDNs) but do not use ECH, while requesting an unclassified response and action plan by November 20 2026.

## The one thing HTTPS leaves in the open is the gap being addressed here

Almost every federal site now encrypts the pages people read and the forms they submit. Standard HTTPS does not hide the hostname. When a browser opens a secure connection, it announces the site it wants in a field called Server Name Indication, in plain text, before encryption begins.

An internet provider, a hostile Wi-Fi network, or a compromised telecom carrier can therefore log that a connection went to tips.fbi.gov without reading a word of the tip itself.

ECH encrypts that part of the handshake. It works best behind a large CDN, where thousands of unrelated sites share the same front door. Cloudflare's implementation, for example, presents every ECH-protected site to the network under one shared name, so an observer can tell a visitor is reaching a Cloudflare-hosted site, but not which one.

Wyden's letter singles out two services. The Department of Veterans Affairs' online suicide prevention service at veteranscrisisline.net is hosted on Amazon Web Services, which the letter says does not currently support ECH. The FBI's tip portal at tips.fbi.gov runs on Cloudflare, which does, but the bureau has not turned it on yet, as Wyden noted, stating: "For the federal domains using a CDN provider with ECH support, such as Cloudflare, turning on domain protection merely requires a configuration update."

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

191 of the 350 addresses, or 54.6%, are diplomatic: 174 embassy sites, three consulates, and 14 missions, mostly to international bodies such as NATO and the UN. Another 53 are subdomains of bie.edu, the Bureau of Indian Education's domain, which appear to be individual school sites. A further 12 are test, training, or staging hosts, including several user acceptance testing subdomains for Education Department debt services.

That leaves 94 addresses outside those groups, and the most troubling entries sit there; they include the DHS inspector general's complaint hotline, the Justice Department's civil rights reporting portal, the intelligence community's job application site, a USCIS tip form, the State Department's Rewards for Justice site, an NIH alcohol treatment navigator, a CDC doxy-PEP site, several federal HIV information sites, and ICE's detainee locator.

Cloudflare's documentation says ECH is enabled by default on Free zones, while customers on other plans must switch it on themselves. That fits the spokesperson's finding: a paying government customer has to opt in. For the FBI, the fix really is a setting.

For the VA, it is not. If Amazon's CDN does not offer ECH, the agency would need to change providers or wait. This is where Wyden's second request, making ECH support a condition of federal contracts, gets complicated.

A procurement rule written today would, in practice, favor a very small pool of providers until others catch up. That may be the intent, since it pressures Amazon and its rivals, but it may be as much a market lever as a security fix, at least in the short term.

ECH does have its limitations, however: the protocol's own specification warns that the destination can still leak through plaintext DNS lookups or the server's IP address. Google made the same point when Android 17 added system-wide ECH in August, saying the feature works "in tandem with private DNS to obscure the domain names you visit."

To reiterate, agencies can enable ECH on their side, but they cannot make a veteran on home broadband use encrypted DNS, therefore leaving the door open to exploitation by someone snooping on the network.

A bigger problem is also international coverage. Many of the highlighted URLs are embassies such as ru.usembassy.gov, by.usembassy.gov, cn.usembassy.gov, and ir.usembassy.gov, all of which arguably have users connecting from relatively hostile networks.

Russia has been blocking Cloudflare's ECH since November 2024, with regulator Roskomnadzor declaring at the time that using it violates Russian law. Russian providers block connections that carry both an ECH extension and Cloudflare's shared outer name, which left Cloudflare customers there choosing between disabling ECH and moving to a domestic CDN.

For an embassy page, enabling ECH could mean trading a visible hostname for an unreachable site in the country where the hostname matters most, making it a difficult tradeoff with only one real solution: skipping ECH for now.

None of this is new territory for Wyden. In October 2018, he wrote to DHS's Chris Krebs urging agencies to adopt encrypted DNS and Encrypted SNI, ECH's predecessor, and asking DHS to work with GSA on making ESNI a condition for CDN vendors selling to the government.

He called that "the next logical step" after DHS's 2017 HTTPS directive, BOD 18-01. The 2026 letter cites the same directive and describes its requests as "the next logical steps." His record on these letters is mixed rather than hopeless. A 2018 HTTPS letter to the Pentagon was followed by a Defense Department plan to secure its websites.

The client side is ready: most major browsers have supported ECH since October 2023, per the letter, and Android 17 now applies it system-wide. The FBI fix is cheap and overdue. But ECH narrows what a passive eavesdropper learns rather than making a visit invisible, and whether this request outlasts the last one may depend less on CISA and OMB than on whether Amazon and others join Cloudflare.

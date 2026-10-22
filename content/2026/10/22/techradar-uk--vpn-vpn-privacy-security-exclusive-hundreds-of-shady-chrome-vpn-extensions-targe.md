---
title: 'Exclusive: Hundreds of shady Chrome VPN extensions target Russians — including
  fakes of Windscribe and ExpressVPN'
source_url: https://www.techradar.com/vpn/vpn-privacy-security/exclusive-hundreds-of-shady-chrome-vpn-extensions-target-russians-including-fakes-of-windscribe-and-expressvpn
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-22T17:21:15Z'
published: '2026-10-22T00:00:00Z'
description: Shady VPNs are giving people a ‘false sense of security.’ But why are
  Russians being targeted?
image: https://cdn.mos.cms.futurecdn.net/bcjLgwWUkB9svavys4tCbN-1686-80.jpg
categories:
- Technology & Software
people:
- Cherlynn Cha
- Rebecca Rosenberg
locations:
- Russia
- Ukraine
organisations:
- Chrome Web Store
- Google Chrome
- Google Chrome Web Store
- Happ
- Head of Growth at Windscribe
- Head of Security Operations at ExpressVPN
- ISP
- Palo Alto
- Palo Alto Networks' Unit
- TechRadar
- Telegram
- VPN
- VPNs
---

![Screenshot of Google Chrome Web Store search results showing four extension listings with Cyrillic text and varied logos using the ExpressVPN name.](https://cdn.mos.cms.futurecdn.net/bcjLgwWUkB9svavys4tCbN-1686-80.jpg)

An exclusive TechRadar investigation into Google’s Chrome Web Store has revealed more than 350 untrustworthy VPN extensions targeting Russian users, with many imitating well-known brands. Combined, these tools have amassed over 218,000 users.

It’s not the first time potentially dangerous VPN extensions have been discovered. Earlier this year, Palo Alto revealed a significant number of dangerous VPN extensions that could leak users’ internet traffic. Alarmingly, we discovered that 89 of those extensions are still active and available.

So, why are there so many shady VPN extensions specifically targeting Russians, and what are the risks of using these low-quality products?

## ‘A game of whack-a-mole’

In total, we discovered that there are 369 Russian VPN extensions available on Google’s Chrome Web Store that fail basic transparency and professionalism tests.

Almost every single extension we analyzed lists a throwaway, anonymous personal Gmail address rather than a professional developer contact. And it appears these operators are running large clusters of extensions — just 70 developers are responsible for all of the extensions we found, with one email address associated with 24 individual apps.

Nearly three-quarters of these VPNs host their privacy policies on Telegram’s anonymous Telegra.ph platform, which hides the true owner of the service, and almost half (47%) have more reviews than users, which may indicate review manipulation.

Perhaps most egregiously, we found over 120 extensions using a name associated with a legitimate brand.

The most frequently hijacked name was Happ — a custom proxy client widely used in Russia — which was co-opted by more than 15 extensions. Among major international commercial providers, we found seven extensions imitating Windscribe and five impersonating ExpressVPN.

Both companies told TechRadar that they are aware of copycat extensions appearing on the Chrome Web Store and said they frequently ask Google to remove them when they are found.

Cherlynn Cha, Head of Security Operations at ExpressVPN, said that “copycat extensions put people at risk” because they give people a “false sense of security”. The company added that it employs an "enforcement partner” to scour the web for unauthorized use of the company’s name.

However, enforcement can be challenging. Rebecca Rosenberg, Head of Growth at Windscribe, said: “It’s pretty much a game of whack-a-mole now, the copycat is pulled and two more pop up.”

And the data backs that up. One email address we uncovered is linked to 14 apps, with the precise number constantly changing as their extensions are removed and new ones take their place.

## Why are unprofessional VPN extensions a threat?

Unlike many other extensions, VPNs have the potential to access a huge amount of sensitive data. In fact, a VPN extension asks “for more access than almost anything else in the store,” Rosenberg said.

A VPN works by encrypting and re-routing your internet connection through one of its servers. While a legitimate VPN improves your digital privacy, it also means you are transferring all your trust from your internet service provider directly to the VPN creator.

In theory, the anonymous developer could see everything your ISP normally monitors. Think: websites visited, time stamps, and your home IP address.

It’s “a lot of trust to hand over," Cha said. Rosenberg added that giving your data “to an anonymous developer with a personal email and a privacy policy that doesn't load is the opposite of privacy”.

![Screenshot showing fake Russian ExpressVPN privacy policy](https://cdn.mos.cms.futurecdn.net/hyFgR9xgKbaDq5NLrj68CD-959-80.png)

## Ongoing security concerns

Without detailed dynamic web testing of all the extensions, it’s impossible to know which may be harmful to users and which are purely unprofessional. However, Palo Alto previously found more than 350 apps that were linked to harvesting user data via traffic interception.

In our tests, 89 of these extensions were still available to Russian users, while email addresses associated with the extensions have continued to launch more apps since initial discovery.

One email address — ‘vale99505@gmail[.]com — was first flagged by Palo Alto in July. According to the company’s threat intel notice, the address was associated with extensions that do not provide “typical encrypted protection like reputed VPN extensions”, adding that the “threat actor” running the apps “has access to all communication”.

According to our most recent tests, six extensions linked to this address are still available for download.

At the time of publication, Google had not responded to requests for comment. TechRadar has shared the full list of extensions with the company and will monitor their availability in the coming weeks.

Windscribe said that Google “should absolutely be doing more” to protect its users from encountering untrustworthy VPN extensions on its Chrome Web Store, while ExpressVPN confirmed the company is in favor of “stronger verification for privacy and security tools”.

Stopping the rise of untrustworthy VPN extensions is important for everyone. But it’s no surprise that this specific network is focussed on Russia.

## Why target Russians?

Since the full-scale invasion of Ukraine in 2022, authorities in Russia have launched an unprecedented crackdown on digital freedom. Thousands of websites have been blocked in the country, including international media, social media and gaming platforms.

In response, VPNs have become a crucial tool for millions of people, which has subsequently prompted coordinated efforts by the government to regulate and restrict access to these vital privacy and security tools.

Most recently, this has included the plan to use AI to detect and block VPN traffic in the country.

In this context, developers looking to make a quick profit may spin up cheap VPN solutions that are poorly designed, entirely fake, or designed to harvest user data to sell to third-party advertisers.

But there’s a darker potential: malicious actors may be intentionally designing VPN extensions to trick Russians into downloading software that can actively monitor their internet browsing behavior.

While there’s no evidence that these extensions are linked to authorities in the country, amid growing concerns about state surveillance and deteriorating internet freedoms, taking extra care when selecting a VPN in Russia today certainly seems sensible.

## How to defend yourself today

There are several steps you can take to make sure you’re downloading a legitimate version of a VPN extension:

* Check the developer’s name and website before downloading anything
* Check that the privacy policy is accessible, informative and related to the app
* If you know which VPN you want to download, go straight to the provider’s website
* Look out for the ‘Established Publisher’ badge on the Chrome Web Store
* Check for any unnecessary permissions like ‘geolocation’

It’s worth remembering that a VPN Chrome extension also only protects your activity in your browser. Anything you do outside of the browser won’t be encrypted so it’s worth using a well-respected VPN where possible.

And, like most things, if a product is free, it’s worth being skeptical. As Cherlynn Cha told us: “Be wary of free VPNs. Running a VPN network costs real money. If a service is free and it’s not clear how it makes money, your data may be what’s paying for it.”

## How we found shady Russian VPN extensions

We compiled our data using a variety of sources, primarily an in-house web scraping tool that identified VPN extensions on the Google Chrome Web Store targeting Russian-language users. We collected metadata including user counts, developer contact emails, and privacy policy URLs.

We then filtered the dataset to remove legitimate, verified corporate VPN providers. The remaining extensions were analyzed for untrustworthy signals, such as using personal email addresses, unprofessional privacy policies and copying established VPN brands.

We also cross-referenced our data with threat intelligence research published earlier this year by Palo Alto Networks' Unit 42 to verify how many malicious extensions previously flagged remained active.

All data and user counts are accurate as of October 12, 2026. Extensions are frequently removed and new copycats are constantly appearing. We continue to monitor their accessibility in the coming weeks.

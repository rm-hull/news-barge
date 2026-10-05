---
title: These social media posts promise big online discounts on Lego, Calvin Klein
  and more — but really they're just phishing scams
source_url: https://www.techradar.com/pro/security/these-social-media-posts-promise-big-online-discounts-on-lego-calvin-klein-and-more-but-really-theyre-just-phishing-scams
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-05T22:00:52Z'
published: '2026-10-05T00:00:00Z'
description: An elaborate scheme is making the rounds on Facebook and TikTok
image: https://cdn.mos.cms.futurecdn.net/HamXBgURVeMtS8ULECqnyn-970-80.png
categories:
- Technology & Software
- Society & Culture
people:
- Calvin Klein
locations:
- Malaysia
- Singapore
- Thailand
organisations:
- FTC Consumer Sentinel
- Facebook
- Group-IB
- Lego
- Milk Dragon
- TechRadar Pro
- Telegram
- TikTok
---

![Mellandagsrea](https://cdn.mos.cms.futurecdn.net/HamXBgURVeMtS8ULECqnyn-970-80.png)

* **Milk Dragon uses fake ecommerce sites and social media deals to steal payment data**
* **Malware captures credentials and MFA codes in real time, even before form submission**
* **Campaign targeted victims in 66 countries, abusing trusted brands and banks**

If you come across a post on social media promoting huge discounts on major brands such as Lego or Calvin Klein, be extra careful, as security researchers Group-IB have warned these could be fake, and part of an elaborate scheme to steal your money.

In their report, the researchers said they uncovered a major scam campaign run by a group they are calling Milk Dragon.

For at least a year now, this threat actor has been using a phishing kit of the same name to create spoofed versions of popular ecommerce websites, sometimes even using AI to create entirely fake listings.

## Phishing with a spin

Fake ecommerce sites with offers simply too good to pass up on are not a new tactic.

Recent FTC Consumer Sentinel data shows 376,830 reports in the "online shopping and negative reviews" category in 2023, with nearly $400 million in reported losses. The median reported loss was $126, with more than half of reports involving financial losses.

What makes this campaign unique is that it abuses trusted channels - social media groups and pages - to deliver the lure. Usually, these lures would be sent out via phishing emails, but since email providers have caught up with most of the tactics and have become rather good at filtering spam, threat actors turned to the next best thing - social media.

In this case, the listings were shared on Facebook and TikTok mostly, Group-IB said, primarily in groups where users hunt for similar bargains. That way, they might not even realize they are actually being targeted by an advanced infostealer.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

As Group-IB explained, the websites come with a piece of malware called BytePress which captures all of the information submitted and sends it to the attackers’ command-and-control panel.

What makes BytePress particularly dangerous is the fact that victims don’t even have to submit the information - simply typing it into the form is enough, since the malware can stream what the victim types character by character, in real-time.

When the victim finally submits the data, it gets relayed through attacker infrastructure to the legitimate website, which often returns requests for one-time passwords and similar multi-factor authentication. The request is sent back to the victim and once again picked up, defeating any multi-factor authentication they might have set up.

## Buying time

In the end, the victim will get a fake order confirmation, and Milk Dragon will display what appears to be a successful purchase. That way, the victim will believe everything is in order and won’t rush to contact their bank and freeze their credit card or reset their credentials. In the meantime, crooks can use those details in whatever malicious way they please.

Milk Dragon doesn’t seem to be targeting any country, or people, specifically. It cast a relatively wide net, with victims being found in 66 countries around the world. However, according to Group-IB’s report, the majority of the victims were found in three countries: Malaysia (1,300+), Singapore (1,200+), and Thailand (1,100+).

The group also doesn’t seem to be particularly fond of any specific brand. A total of 21 popular brands were spoofed, across cosmetics & fashion, food & beverages, home & baby products, as well as toy industries. Regional supermarkets are also frequent impersonation targets, it seems, as well as 36 financial institutions and banks.

The Milk Dragon phishing kit is being sold on Telegram channels as a service, with various hacking groups paying either monthly, or yearly fees. The tool is being sold from 300 USDT (cryptocurrency) a month, with various subscription plans and add-ons.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

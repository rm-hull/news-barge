---
title: Some of the world's largest brands hit following Optimizely flaw — Salesforce,
  CNN, Fox News, BBC sites hit with malware
source_url: https://www.techradar.com/pro/security/some-of-the-worlds-largest-brands-hit-following-optimizely-flaw-salesforce-cnn-fox-news-bbc-sites-hit-with-malware
source_site: TechRadar UK
source_slug: techradar-uk
description: A bug in Optimizely allowed an attacker to deploy malicious JavaScript
  across the web
image: https://cdn.mos.cms.futurecdn.net/Ri2dNNTvgmKGsMuhNDCavZ-2560-80.jpg
published: '2026-11-17T00:00:00Z'
scraped_at: '2026-11-18T00:55:28Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Optimizely
- Scott Helme
locations:
- Cloudflare
organisations:
- ASOS
- Alaska Airlines
- BBC
- CDN
- CNN
- Coruna
- Equifax
- Fox News
- HSBC US
- Hawaiian Airlines
- IKEA
- Ledger
- Optimizely
- Peacock
- Salesforce
- TalkTalk
- TechRadar Pro
- Virgin Media
- Virgin Media O2
- Vodafone Australia
- Zoom
---

![Dark web monitoring](https://cdn.mos.cms.futurecdn.net/Ri2dNNTvgmKGsMuhNDCavZ-1920-80.jpg)

* **Attackers compromised Optimizely and injected malicious JavaScript into more than 100 popular websites through a trusted content delivery path**
* **The payload stole cryptocurrency, harvested payment-card data, captured user information, and targeted iPhone visitors with exploit kits**
* **Optimizely removed the malicious code, revoked access, and patched the signup-flow vulnerability used in the attack**

Threat actors broke into Optimizely and used it to deploy malicious code to more than 100 popular websites across the internet, with the code replacing people’s cryptocurrency wallet addresses, stealing credit card information, and even allowing attackers to take over iPhones, experts have said.

Optimizely is a digital experience platform that businesses use to manage their websites, create and optimize digital content, run A/B tests, and personalize customer experiences. It is used primarily by marketing and product teams to experiment with different features of the website, improving engagement, conversions, and ultimately - sales.

It is a hugely popular tool, one that’s used by hundreds of organizations in all sorts of industries. The attacker deployed 188 snippets onto 178 organizations. Most of them were in banking & finance (32), technology & SaaS (23), and retail & fashion (20), with some major names on the list: HSBC US, Equifax, Zoom, Salesforce, IKEA, ASOS, Peacock, CNN, BBC, Fox News, Alaska Airlines / Hawaiian Airlines, Virgin Media, Virgin Media O2, Vodafone Australia, O2, Ledger, and many others.

## Exploiting a flaw

In a blog post, security researcher Scott Helme, who discovered the attack, explains what happened - each customer loads a JavaScript snippet from Optimizely’s Content Delivery Network (CDN), containing the company’s code, the customer’s experiments, and an optional field called Project JavaScript. This is custom code the customer writes in their own Optimizely dashboard which runs on every page.

According to Helme, the attacker wrote their own code into the Project JavaScript of customer projects and the file was served to multiple victims. It still went out from cdn.optimizely.com, with Optimizely’s certificate, from a known and trusted host.

In a statement, Optimizely said the attacker exploited a flaw in its Experimentation account signup flow to inject the malicious JavaScript code.

"Earlier today, Optimizely identified a security incident in which an unauthorized party exploited a vulnerability in the Experimentation account signup flow," Optimizely said.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

"They used it to add malicious JavaScript to some customer projects. We have blocked access to the vulnerable path and deployed a fix. We have removed the injected code from affected projects. We have also ended active sessions, revoked tokens, and reset access for affected user accounts. Finally, we have blocked any code from being delivered in Cloudflare.

Helme says the threat actors rebuilt the payload 26 times in one day, adding features and cryptocurrency wallets. The payload did four key things: stole people’s crypto, skimmed compromised websites for customer credit cards, stole cookies and took screenshots, and deployed iOS hacking toolkits.

## Fighting back

Crypto theft worked through clipboard jacking: the code would monitor the clipboard for copied wallets and replace them with attacker-owned ones when pasting.

That way, victims would copy one address and unknowingly paste an entirely different one, sending money to the attackers. The skimmer would monitor the sites for card numbers, expiry dates, and CVV secrets, and when it finds all three, it would send them to an attacker-owned server. Cards entered in hosted payment iframes (Stripe, Adyen and similar) were out of its reach, it was said.

Victims opening the websites on iPhones and iPads were served Coruna and DarkSword, exploit kits designed to abuse unpatched iOS vulnerabilities and steal sensitive information, including cryptocurrency wallet credentials and recovery phrases.

Helme says the threat actors stole just over $7,000 in this campaign. Most of it was in bitcoin (around $5,300), with the rest split between litecoin, USDT, and ether.

Most of the malicious code has now been removed, Helme stressed. Less than 24 hours after the first attack was spotted, the number of infected snippets was down to just one - TalkTalk.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

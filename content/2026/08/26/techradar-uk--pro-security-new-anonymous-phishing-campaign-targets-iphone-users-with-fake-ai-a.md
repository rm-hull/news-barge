---
title: New 'AnonyMous' phishing campaign targets iPhone users with fake AI Apple support
  calls
source_url: https://www.techradar.com/pro/security/new-anonymous-phishing-campaign-targets-iphone-users-with-fake-ai-apple-support-calls
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-26T13:11:37Z'
published: '2026-08-26T00:00:00Z'
description: Crooks are automating fake support calls
image: https://cdn.mos.cms.futurecdn.net/kAV78FEzwxTr8Mjix8wrEQ-2560-80.jpg
---

![Girl typing something on mobile phone](https://cdn.mos.cms.futurecdn.net/kAV78FEzwxTr8Mjix8wrEQ.jpg) 

- **SOCRadar uncovers AnonyMousKIT, a phishing kit abusing Apple’s Lost Mode contact info**
- **Crooks spoof Find My pages, trick victims into giving credentials to unlock stolen iPhones**
- **Active since 2024, it operates like a criminal software business with 500+ domains and AI‑driven vishing**

Security researchers have discovered AnonyMousKIT, a new phishing kit designed to bypass the last line of defense for stolen iPhones, which has been in use for more than two years.

Apple devices come with several anti-theft mechanisms working together to make iPhones a lot less attractive to thieves, including Find My, Activation Lock, and Lost Mode.

If a user’s device is lost or stolen, they can use their tablet, laptop, or a similar device to enable Find My iPhone, which can then locate the device through an app or a website. They can also see its location on a map, make it play a sound, remotely wipe it, or receive a notification when it’s found. Enabling the Find My feature also turns on Activation Lock, which locks the phone and prevents it from being set up by someone else.

Even if the thief factory resets it, the phone remains connected to the real owner’s Apple account, and they simply can’t set it up. To do that, they would need the iPhone device passcode to exit Lost Mode, and the Apple account password, if Activation Lock/setup authentication is required.

But there is another feature Apple added, just in case the device isn’t actually stolen, but rather lost. For these occasions, there is an option to display the owner’s contact information on the screen so that a good samaritan who finds it can return it to its rightful owner.

As is the case with many other well-intended features, this one is now also being abused as part of the AnonyMousKIT phishing kit.

## This is why we can't have nice things

According to security researchers SOCRadar, crooks are using AnonyMousKIT to create fake Find My or Apple pages. Then, they use the contact information displayed on the stolen iPhone to reach out to the victim. Through the kit, they can send emails, SMS messages, WhatsApp texts, or even AI-powered phone calls. Reaching out to the victim, the attackers introduce themselves as Apple customer support agents, and tell the victim their smartphone had been retrieved.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

They also provide the victim with the correct model and IMEI details to confirm the authenticity of their claims. Then they require the victim to confirm their identity by visiting the spoofed Find My page and providing the credentials needed to unlock the phone.

The credentials end up with the attackers, who can then unlock the phone, wipe it, and sell it on the black market for a much higher price.

## "Software business"

SOCRadar says the earliest records of the AnonyMousKIT date back to early 2024. Since then it has grown into a major operation, counting more than 500 domains, and having more than 150 storefront brands working as resellers and affiliates.

As part of their investigation, the researchers found records of roughly 200 calls, which the crooks made to victims between August 2025 and May 2026. The calls were done using five different AI agent personas and 55 different interaction transcripts.

Every call had cost the attackers $0.10, and most of them - 90% - were made to Brazilian victims. A small percentage of email correspondence was made towards government and corporate addresses, as well. Just under 30 attempts were made towards South African government domains, and three to a local university. While the campaign is global in its reach, it’s mostly focused on South Africa, Indonesia, India, Kenya, Brazil, and Italy.

SOCRadar describes AnonyMousKIT "not as a phishing kit but as a small software business with a criminal customer base."

"Its primary innovation is an automated, LLM-driven voice vector. At ~$0.10 per call, the platform initiates dynamic vishing across three languages using structured pretexts synced with email and SMS lure data, removing the need for fluent human callers."

At the moment the report was published, the campaign was still ongoing, and the researchers are still tracking it.

*Via**BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

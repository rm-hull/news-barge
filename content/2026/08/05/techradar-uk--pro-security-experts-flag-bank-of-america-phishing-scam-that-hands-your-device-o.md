---
title: Experts flag Bank of America phishing scam that hands your device over to hackers
source_url: https://www.techradar.com/pro/security/experts-flag-bank-of-america-phishing-scam-that-hands-your-device-over-to-hackers
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-05T17:51:24Z'
published: '2026-08-05T00:00:00Z'
description: Why would Bank of America want to install ScreenConnect on your computer?
image: https://cdn.mos.cms.futurecdn.net/vg86aqqGf8Pqp6mnfQPGGf-1920-80.jpg
---

![Phishing](https://cdn.mos.cms.futurecdn.net/vg86aqqGf8Pqp6mnfQPGGf.jpg) 

- **Huntress flags phishing emails spoofing Bank of America, pushing victims into different infection chains on Windows vs. macOS**
- **Windows users were tricked into installing ScreenConnect RMM via fake “Account Guard,” while macOS users faced credential‑harvesting forms for identity theft**
- **Emails mimicked Bank of America branding but came from unrelated domains; users advised to verify sender addresses to spot scams**

Bank of America customers have been warned to take extra caution after experts warned of hackers spoofing the bank into trick you into downloading unwanted software and granting them access to your computer.

Security researchers Huntress revealed how it received a phishing email in their honeypot (an address set up primarily to catch scammers) claiming to have come from Bank of America.

Obviously, the message came from a domain completely unrelated to the company, but looked almost identical to the real thing, with the company logos, color schemes, and other details, meticulously imitated.

## Just another ScreenConnect scam

In the email, the researchers were warned that their account was about to be “restricted” unless they “confirmed” certain information.

Depending on the platform from which the victim views the email, both the infection chain and the end goal are different. For Windows users, victims are invited to install “Account Guard”, which is described as a “powerful tool designed to protect your financial data, prevent unauthorized transactions, and other cyber threats”.

This is no guard - this is a Visual Basic script that leads to an installation of the ScreenConnect Remote Monitoring and Management (RMM) tool. ScreenConnect is not malicious itself - it is a legitimate tool - but it is also one of the most abused software out there, leveraged to grant attackers unabated access to victim computers without triggering any alarms.

For macOS users, on the other hand, the goal is different. Instead of trying to deploy malware, the attackers try to steal sensitive data. First, the victims are asked to log in to their banking account (twice - the first attempt is scripted to fail, in case the victim purposely submits the wrong password the first time).

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Then, once they “log in”, the second web page asks the victims to “confirm” their details - full name, mailing address, government ID details, Social Security number (SSN), and the payment card details. This is more than enough information for an identity theft attack, or even wire fraud.

Huntress is now warning all Bank of America users to double-check the sender address for any email claiming to be from the bank, since that is the best way to know if the email is legitimate, or a scam.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

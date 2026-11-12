---
title: A 2013 hack of a Russian cybercrime forum may have leaked the details of millions
  of users
source_url: https://www.techradar.com/pro/security/a-2013-hack-of-a-russian-cybercrime-forum-may-have-leaked-the-details-of-millions-of-users
source_site: TechRadar UK
source_slug: techradar-uk
description: Details from the YouHack breach have re-emerged on the internet
image: https://cdn.mos.cms.futurecdn.net/TWkP7ZurZMY6uepDxsK6Ha-970-80.jpg
published: '2026-11-12T00:00:00Z'
scraped_at: '2026-11-12T19:51:46Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- Europe
- Russia
- Ukraine
- YouHack
organisations:
- Alfa-Bank
- Eltrans
- HIBP
- NLB
- SberSpasibo
- Sberbank
- TechRadar Pro
- Viasat
- YouHack
---

![Computer Hacked, System Error, Virus, Cyber attack, Malware Concept. Danger Symbol](https://cdn.mos.cms.futurecdn.net/TWkP7ZurZMY6uepDxsK6Ha-970-80.jpg)

* **Data from a 2013 breach of the YouHack cybercrime forum resurfaced online, exposing 7.2 million email addresses and password pairs**
* **The leak also included forum user details, usernames, IP addresses, and weakly protected MD5 password hashes**
* **Researchers warn recycled breach data and cracked passwords remain valuable for credential-stuffing and account takeover attacks**

A large treasure trove of data stolen roughly 13 years ago has again surfaced on the clear web, with millions of email addresses, belonging to both innocent victims and notorious cybercriminals leaked online and found their way to Have I Been Pwned? (HIBP).

HIBP is a free online service that allows users to check whether their email address or phone number appeared in any known data breach.

HIBP recently added a new database containing roughly 7.2 million addresses. As it turns out, these addresses were stolen in May 2013, when an infamous Russian-language hacking forum YouHack suffered a breach at the hands of unnamed miscreants.

The leaked archive contains almost 7.2 million email addresses and password pairs belonging to various victims whose secrets were posted on the forum. It also contains 107,000 forum members’ email addresses, usernames, IP addresses, and MD5 password hashes - “most of which were unsalted” - HIBP said.

## Unsalted MD5 passwords

Decade-old email addresses, usernames, and IP addresses of various hackers are probably not valuable information. Cybercriminals are known for using VPNs and proxy services to hide their locations, as well as disposable emails, so even if the data was recent, its usability would still be questionable, at best. Passwords, however, are a different story.

Just like the rest of us mortals, cybercriminals are known for failing to practice basic cyber-hygiene, often using the same passwords across a myriad of services. When those passwords are hashed with MD5 and unsalted, it becomes a problem.

As a cryptographic hashing algorithm, MD5 converts passwords into fixed-length strings. It is considered wildly outdated and insecure, because threat actors can crack them easily using off-the-shelf software and hardware. The problem is even worse when hashes are unsalted, which means the system hasn’t added a unique random value to each password before hashing it. This allows attackers to use precomputed lookup tables and identify identical passwords across different accounts much more easily. Once cracked, passwords can be used to access other accounts where victims have reused them.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Mother of all breaches

According to*The Register*, this is not the first time this archive has made it to the clearweb. Back in 2024, the “Mother of All Breaches” saw 26 billion records, weighing 12 terabytes, were leaked. This was a bundle of numerous different security incidents, and among them were files grabbed from YouHack, as well.

The same publication reports that this is the second Russian data breach to be reported today. At the same time, a 2023 breach of Sberbank’s loyalty program (SberSpasibo) also leaked, exposing records belonging to 48 million users. Among the records are 3.3 million unique email addresses, people’s phone numbers, and dates of birth. A number of bank card numbers were also leaked, and since these were stored as unsalted SHA-1 hashes, they were also at risk of being fully exposed.

This attack happened sometime between April 2017 and February 2022, the report further states, and was claimed by a pro-Ukraine hacktivist organization calling itself NLB. The same group also claimed responsibility for the attack on Russia’s largest private bank, Alfa-Bank.

Although we cannot know for certain, it is possible the leaks are the result of the war between Russia and Ukraine spilling into cyberspace. The two sides have been trading blows over the internet since the full-scale invasion began, with Russia's February 2022 attack on Viasat's satellite communications network disrupting thousands of connections in Ukraine and across Europe.

Ukraine has also launched destructive cyber operations against Russian targets, including a December 2025 attack on logistics company Eltrans+, which reportedly wiped or encrypted 165TB of data and disabled more than 700 servers.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

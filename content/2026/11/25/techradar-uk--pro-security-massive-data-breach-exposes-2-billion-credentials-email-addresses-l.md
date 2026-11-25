---
title: Massive data breach exposes 2 billion credentials — email addresses, login
  names, passwords, and more all leaked online in major database breach
source_url: https://www.techradar.com/pro/security/massive-data-breach-exposes-2-billion-credentials-email-addresses-login-names-passwords-and-more-all-leaked-online-in-major-database-breach
source_site: TechRadar UK
source_slug: techradar-uk
description: One of the biggest archives ever unveiled
image: https://cdn.mos.cms.futurecdn.net/SEXM8ah9EKKpBKB22d7Ak3-1600-80.jpg
published: '2026-11-25T00:00:00Z'
scraped_at: '2026-11-25T19:10:47Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Jeremiah Fowler
locations:
- DE
- UK
organisations:
- Amazon
- Facebook
- Google Services
- Instagram
- MFA
- TechRadar Pro
- Telegram
---

![Data Breach](https://cdn.mos.cms.futurecdn.net/SEXM8ah9EKKpBKB22d7Ak3-1600-80.jpg)

* **Researchers discovered a publicly exposed database containing roughly 2 billion records, including passwords, session tokens, cookies, and authentication data**
* **The archive appears to aggregate information stolen by infostealer malware, affecting major platforms such as Google, Facebook, Amazon, Instagram, and Roblox**
* **Experts warn exposed session tokens and credentials could enable account takeovers, making password changes and MFA essential defenses**

Security researcher Jeremiah Fowler, known for uncovering unencrypted and non-password-protected databases, just reported finding a behemoth - an enormous publicly exposed database hosting data most likely generated through multiple infostealer malware, including two billion personal records, including passwords and session tokens.

In his report, Fowler said the database contained email addresses, login names, passwords, cookies, session tokens, authentication artifacts, device information, and other application identifiers.

“In volume and scope, this is the largest collection of credentials I have discovered in my years as a security researcher, and it reinforces the growing threat that malware poses globally,” Fowler warned. “This 2 billion record dataset is more than 13 times the size of a previous exposure of 149 million logins and passwords I reported earlier this year.”

He also stressed that with session tokens, cookies, and device data, attackers have more than one way to “get in”.

## .onion addresses exposed as well

The database was apparently well organized. It contained more than 8,400 folders, with credentials and account information sitting in plaintext. Some documents were segmented by country and had abbreviations such as UK, DE, or FR. Some victims even had their own separate folders with cookies, edge, important files, and .txt documents labeled system, process, clipboard, brute force, passwords, and more - most likely for advanced profiling.

The database also contained thousands of Tor .onion addresses associated with account names and passwords, which was a first even for Fowler.

While he says that it’s possible these accounts belonged to cybersecurity researchers, journalists, or whistleblowers, he also stresses that 60% of dark web sites host illegal material and illegal activities, hinting that the accounts probably belong to cybercriminals.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The archive held more than 114 million Google Services accounts, followed by 41 million Roblox accounts. The third biggest batch was Facebook with 88 million, followed by Amazon (36 million), X (32 million), and Instagram (31 million). The researcher stressed that there is a strong possibility of duplicate entries, meaning the actual number of exposed accounts is smaller. He did not analyze it that thoroughly to see how many unique accounts there actually are.

## Data brokers, or security researchers?

When he discovers these databases, Fowler usually manages to attribute them to a company, or an agency. He then reaches out and shares his findings, after which the owners usually lock it down. Most of these archives are left unchecked by mistake, which was probably also the case here.

In this case, however, there were no clues as to who owned or managed this database, which is why Fowler believes it was built by cybercriminals.

“The files referenced or indicated multiple suspected cybercriminal data sources or underground credential operations as the original sources,” Fowler says. He did manage to lock the archive down by reporting it to the hosting provider who quickly restricted access.

Even if it was the work of multiple actors/malware, it is still an extremely large archive. Fowler believes it served as part of a criminal marketplace or aggregation operation, where stolen credentials were collected from different malware logs, Telegram channels, various resellers, and underground communities.

Criminals dealing in data brokerage often aggregate data from multiple sources, so this could also be a package offered to someone for sale. There is also an (ever so slightly) chance the archive was built by security professionals, threat intelligence organizations, academic researchers, or even law enforcement. We wouldn’t hold our breaths, though.

We would, however, make sure to change our passwords across our services every once in a while, and set up two-factor authentication wherever possible - especially on key platforms such as banks and e-commerce providers.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

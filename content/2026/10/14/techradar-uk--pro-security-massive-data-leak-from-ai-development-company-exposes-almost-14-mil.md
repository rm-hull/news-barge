---
title: Massive data leak from AI development company exposes almost 14 million records
  — Vibetech collected data from different breaches and accidentally made them accessible
  online
source_url: https://www.techradar.com/pro/security/massive-data-leak-from-ai-development-company-exposes-almost-14-million-records-vibetech-collected-data-from-different-breaches-and-accidentally-made-them-accessible-online
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-14T17:08:18Z'
published: '2026-10-14T00:00:00Z'
description: Vibetech was harvesting data from different leaks
image: https://cdn.mos.cms.futurecdn.net/GcQXTy4NBXKeoop4V5WQnQ-970-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Jeremiah Fowler
locations:
- Brazil
- Elasticsearch
- US
organisations:
- AT&T
- AWS
- Amazon
- B2B
- BluBank Digital Bank
- Cybernews
- FBI Employee Directory
- IP
- ISMS
- Interpol
- OneMoreLead
- PayPal
- TechRadar Pro
- Vibetech
- Walmart
---

![Data leak](https://cdn.mos.cms.futurecdn.net/GcQXTy4NBXKeoop4V5WQnQ-970-80.jpg)

* **Researchers found an exposed database containing 13.7 million records from past data breaches and leaks**
* **Archive included passwords, banking details, and data tied to major firms like AT&T and Amazon**
* **The database was secured after disclosure, highlighting ongoing risks from exposed breach repositories**

Indian software development platform Vibetech seems to have been collecting data exposed in various leaks and cyberattacks and creating one big repository.

Besides the questionable legality of the whole ordeal, an equally important issue is that the archive was sitting on the open internet, available to anyone who knew where to look.

## AT&T, PayPal, and more

The news comes from Jeremiah Fowler, a security researcher known for hunting down non-encrypted, non-password-protected databases across the web.

Fowler's research found one database containing 13.7 million records, including a “collection of highly sensitive data from previous breaches,” including names, people’s phone numbers, email addresses, passwords, bank account details, and more.

“In a limited sample, I saw accounts and credentials belonging to individuals from multiple countries," Fowler noted.

The archive was split by company names - the majority of the records (almost eight million) came from an AT&T data leak, but other notable mentions include Amazon (1.2 million), Walmart (420,000 records), BluBank Digital Bank (24,000 records), and PayPal (18,000 records). There were even (relatively small) leaks from the FBI Employee Directory (4,084 records), as well as Interpol (929 records).

This is, by no means, your average data breach archive, as it contained passwords and banking details, which makes it infinitely more potent, as threat actors can directly access people’s online accounts, escalate privileges to deploy ransomware, and possibly wire funds directly from people’s bank accounts.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Fowler later discovered that the IP address of the database was connected to a data intelligence platform operated or developed by Vibetech, which, Fowler speculates, was collecting datasets from previous breaches or leaks, and inadvertently made them publicly accessible without authentication.

The researcher notified both the company and the hosting provider, and the database was restricted and made no longer publicly accessible, soon after. Furthermore, a day later the IP address no longer hosted the plaintext credentials and instead displayed an Information Security Management System (ISMS) compliance platform dashboard.

## Unprotected databases - the bane of internet privacy

According to Fowler’s report, there is a “growing number” of organizations that intentionally collect and sell breached credential datasets, apparently for research, monitoring, or threat intelligence purposes, but the question is how legal the activity actually is.

“Although these datasets can provide valuable insights into attack trends, credential reuse, and emerging threats, organizations that collect compromised personal information operate in a legally and ethically complex environment,” Fowler argues.

Unprotected databases are one of the leading causes of data leaks. In many instances, these are unintentional - businesses generating or harvesting data often misconfigure their buckets or are under the impression that securing the data is the cloud provider’s responsibility.

For example, in early 2024, *Cybernews* discovered an archive with personal information on approximately 223 million Brazilians. Brazil is a country of 214 million people, making some researchers speculate if the country’s entire population was exposed. The researchers said they discovered the database after running a query in Elasticsearch but couldn’t determine who the owners were.

Earlier still, in 2021, a B2B sales and marketing company leaked personally identifiable information (PII) of up to 126 million US citizens, when researchers discovered an unsecured database on Amazon’s cloud computing platform AWS. The archive, owned by a US-based marketing company OneMoreLead, included email addresses, home address, and phone numbers, and more could easily have been used to perpetrate identity theft, financial fraud, or be used to devise effective phishing campaigns.

Individuals who think their information may have been exposed in any of these breaches should change their passwords immediately and be careful with incoming email messages.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

---
title: Uber data breach sees hackers steal license information on thousands of drivers
source_url: https://www.techradar.com/pro/security/uber-data-breach-sees-hackers-steal-license-information-on-thousands-of-drivers
source_site: TechRadar UK
source_slug: techradar-uk
description: One of Uber's services was breached
image: https://cdn.mos.cms.futurecdn.net/aFuqJoM5FFuvC5JASPq2TG-1920-80.jpg
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-16T19:33:47Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Uber
locations:
- AI
- California
- Illinois
- Massachusetts
- Rhode Island
- San Francisco
- South Carolina
- US
organisations:
- Cyberscout
- Fireworks AI
- GTIG
- Google
- Google’s Threat Intelligence Group
- LLMjacking
- TechRadar Pro
- UNC6993
- Uber
---

![Close up of UBER sign at their headquarters in San Francisco&#039;s SOMA district](https://cdn.mos.cms.futurecdn.net/aFuqJoM5FFuvC5JASPq2TG-1920-80.jpg)

* **Uber discloses third-party breach that exposed driver data, including driver’s license information for thousands of individuals**
* **The incident stemmed from a compromise at AI infrastructure provider Fireworks, which was also targeted in broader LLMjacking attacks**
* **Uber is notifying affected users and offering identity theft and credit monitoring services while investigations continue**

Popular ride-hailing service Uber has confirmed it lost sensitive data after one of its third-party service providers was hacked.

The company filed a new notice with multiple US Attorney General’s Offices and shared a copy of the letter it is now sending out to affected individuals.

In the letter, it says that a threat actor got ahold of login credentials belonging to an employee of the service and used them to pull Uber’s data.

## Driver’s licenses and other data

The letter does not disclose key details, like the nature of the data that was stolen, or how many people were affected.

According to *TechCrunch*, however, “thousands” of drivers lost personal and driver’s license information, with the stolen data including driver’s licenses of 2,567 individuals in Massachusetts, 3,430 people across South Carolina, and 1,873 residents of Rhode Island.

More drivers in Illinois and California, and possibly elsewhere, may also be affected - but these figures are so far unconfirmed.

While Uber did not say which of its third-party service providers got hacked, the media uncovered it was a company called Fireworks AI which, itself, was also a victim of a third-party supply chain attack. Fireworks is a US-based AI infrastructure company that helps businesses deploy and run AI models at scale. Apparently, it provides access to hundreds of AI models, as well as the computing resources needed to run them, and its clients include heavy-hitters such as Shopify, DoorDash, and Notion.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Fireworks recently issued a notice saying it spotted a threat actor using internal company credentials to access “environment variables used in evaluation jobs” in a “limited number” of customer accounts.

At first, the company said it did not find evidence of unauthorized access to customer models, datasets, training data, personal information, or inference traffic, but a subsequent update changed the wording somewhat: “At the time of publishing the bulletin, only Fireworks stored secrets (e.g. used in evaluation jobs) were known to have been accessed. Since then, we discovered impacts to account and billing information. For a limited set of accounts, we also discovered impact to secrets, datasets, and incomplete models,” it said.

## LLMjacking

The data stolen from Uber seems like added value, not the primary target, as Fireworks says all evidence indicates this was an LLMjacking attack.

LLMjacking is a relatively new term. Google’s Threat Intelligence Group (GTIG) recently described it as “the monetization and resource-hijacking of foundation models, which actors achieve through token proxying, automated model streaming, and GPU hardware provisioning.” In other words, someone else is using your AI subscription while you get the bill.

The attacks are quite disruptive, too. Unlike cryptojacking, which takes a long time to rake up any meaningful bills, LLMjacking costs can go up in mere minutes. Google’s recent report showed how a Chinese actor tracked as UNC6993 cost its victims more than $100,000.

The company suffered a secondary attack, as well, less than a month later. On October 23, someone broke into a third-party cloud provider that hosted the company’s R&D machines and used it to reach Fireworks development machines.

There, they ran unauthorized workloads “that led to additional customer data impact.” The attack was spotted on the same day and stopped. “As of October 25, we have not detected further evidence of successful unauthorized access by the threat actor on the Fireworks platform customers use,” the company concluded.

Both Fireworks and Uber are now notifying affected individuals of the breach, and the latter is also offering free identity theft and credit monitoring through Cyberscout.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

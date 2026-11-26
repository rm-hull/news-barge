---
title: Todoist confirms data breach — says 6% of customers’ details were stolen, including
  email IDs and account info
source_url: https://www.techradar.com/pro/security/todoist-confirms-data-breach-says-6-percent-of-customers-details-were-stolen-including-email-ids-and-account-info
source_site: TechRadar UK
source_slug: techradar-uk
description: Popular task management app broken into when an employee lost vital credentials
image: https://cdn.mos.cms.futurecdn.net/5R7foEPP2acpGQJQ6zgdMh-2560-80.jpg
published: '2026-11-26T00:00:00Z'
scraped_at: '2026-11-26T16:50:59Z'
categories:
- Technology & Software
- Business & Entrepreneurship
- Careers & Productivity
people:
- Amir Salihefendic
- Todoist
locations: []
organisations:
- SHA1
- TechRadar Pro
- Todoist
---

![Todoist app on iPhone](https://cdn.mos.cms.futurecdn.net/5R7foEPP2acpGQJQ6zgdMh-1920-80.jpg)

* **Todoist discloses breach in which attackers used compromised employee credentials to access source code, cloud infrastructure, and customer data**
* **Exposed information included email addresses, account metadata, password hashes, and limited mailbox-related data for some users**
* **The company revoked compromised credentials, secured affected systems, and urged impacted users to change passwords and review linked accounts**

Todoist, a popular task management and productivity app, has disclosed suffering a cyberattack in which it lost sensitive customer information - including password hashes and portions of private email messages.

The threat actors have since been removed from the systems, compromised credentials were revoked, and affected accounts secured.

However, Todoist is urging some customers to change their passwords to remain secure.

## What happened?

As per Todoist’s incident report, the attack took place between November 22 and 23 2026 , when a threat actor used a set of employee credentials for the company’s version control system to break into automated development workflows.

Todoist doesn’t know how the attackers got ahold of these credentials, but said that the employee was most likely struck with infostealer malware:

"Our leading theory is that an employee’s device may have been compromised," they said.

The attackers used the credentials to modify workflows across three repositories, which allowed them to pull even more credentials. They were also able to access the company’s source code, although apparently they didn’t fiddle with it.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

One of the credentials obtained during the attack allowed the attackers to change how employees accessed internal systems, which they used to take over an employee work account and access Todoist’s cloud infrastructure. From there, they downloaded a file with information belonging to early Todoist users, whose passwords were still protected by an outdated hashing method - salted SHA1.

They also searched for credentials, queried account tokens, and accessed information from mailboxes connected through Todoist for Outlook.

## What did the attackers steal?

Todoist split the stolen data into four categories. The largest group represents roughly 6% of its user base, and they lost email addresses, account creation dates, and password hashes.

The second-largest group includes 0.003% of users, while the third and fourth one - 0.001%. The company did not disclose the exact number of affected customers, but since it claims to be trusted by more than 50 million people and teams worldwide, we can deduce that roughly three million people could be at risk.

This is particularly important for users whose passwords were stored using salted SHA1. This is an old encryption method, discontinued more than a decade ago, and as such is at realistic risk of being cracked. Commenting on the fact that they used SHA1 despite it being late 2026, Todoist said these were old passwords that had not changed since before the method was discontinued - the company has now retired support for it.

It also urged its users to change their passwords, both on the platform and elsewhere around the web - in case they were using the same credentials on multiple services (which is quite common these days).

Todoist said it blocked the attacker’s access paths, removed the compromised accounts, revoked the credentials they used, and got rid of the malware that was installed. It also reviewed authentication settings modified during the incident and restricted remote command execution within its cloud infrastructure.

Finally, the company reached out to affected users via email, instructing them what to do:

“Each email is specific to each individual customer’s case,” the company said. “It will describe exactly what information was affected in your case and what you should do.” Some users will have to reset their passwords, others reconnect their Slack integration. Customers who did not receive an incident notification do not need to take any action, according to the company.

At the same time, no one claimed responsibility for the attack. The data has not yet surfaced on the dark web, and no ransom demands have been made.

The company’s founder and CEO, Amir Salihefendic, apologized for the breach on X, and stressed the company will conduct a thorough investigation into the attack.

*Via* * TechCrunch*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

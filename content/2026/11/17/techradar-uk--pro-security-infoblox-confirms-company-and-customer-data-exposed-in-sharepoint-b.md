---
title: Infoblox confirms company and customer data exposed in SharePoint breach
source_url: https://www.techradar.com/pro/security/infoblox-confirms-company-and-customer-data-exposed-in-sharepoint-breach
source_site: TechRadar UK
source_slug: techradar-uk
description: Infoblox says its investigation is ongoing
image: https://cdn.mos.cms.futurecdn.net/37uyEphcLreEFNUVCQzurn-2560-80.jpg
published: '2026-11-17T00:00:00Z'
scraped_at: '2026-11-18T00:58:22Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Scott Harrell
locations: []
organisations:
- Infoblox
- NIOS
- TechRadar Pro
- The Register
---

![World Password Day 2025](https://cdn.mos.cms.futurecdn.net/37uyEphcLreEFNUVCQzurn-1920-80.jpg)

* **Infoblox is investigating a supply-chain breach in which attackers allegedly used a vendor’s access to steal employee and customer data**
* **Exposed information reportedly includes employee personal details and customer network configuration backups**
* **Company is offering identity protection services and warning affected individuals about phishing and fraud risks**

Infoblox has said it is currently investigating reports of a cyberattack and sensitive data theft.

Initial reports describe it as a third-party supply chain attack in which employee data and customer network information were exfiltrated.

*The Register* revealed how Infoblox worked with a third-party data migration vendor which was granted trusted access to its SharePoint system, meaning the unidentified attackers apparently obtained login credentials for vendor accounts, used them to access Infoblox’s Microsoft SharePoint instances, and pulled data straight from there.

## NIOS deployments and personal data

Exactly who the attackers are, or how they obtained the credentials, was not explained. Usually, they either steal the passwords with infostealers, or trick victims into handing over the credentials themselves.

The former method is easy in theory - get the victim to download malware and the program sends over stored passwords, authentication cookies, sensitive documents, and other files. The latter is somewhat more difficult since it involves creating a fake login page of a known - and used - online service that secretly relays all submitted information, sending it to the victim, and hoping they try to log in.

This is usually done through phishing emails that warn the victim they will lose access to accounts, or that the affiliated data will be deleted, making them hurry and not pay attention to what they’re doing.

Among the nabbed information are some customers’ Network Identity Operating System (NIOS) deployments, *The Register* claims. “These are saved snapshots of customers’ network data, such as DNS, DHCP configurations, Grid databases, and reporting logs, that can be used to fully recover the appliance or grid in case of a system failure or faulty upgrade.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

There’s plenty of value in stolen NIOS config backups. These can serve as blueprints of a corporate network, including DNS infrastructure, DHCP settings, internal IP address range, and connected systems.

This kind of information can be useful to map a network, identify critical infrastructure, locate potential weak points, and plan targeted attacks. DNS configurations, for example, can reveal internal hostnames or domain structures, helping crooks identify valuable targets or craft custom-tailored and highly convincing phishing lures. Access to Grid databases and recovery snapshots could also expose sensitive operational details that make it easier to impersonate legitimate infrastructure or disrupt network services.

The attackers also apparently stole employee data. Citing an email Infoblox CEO Scott Harrell allegedly sent to employees, *The Register* says the attackers took financial information such as direct deposit details, contact info, dates of birth, and Social Security numbers for employees and dependents.

## Offering help

This is more than enough information to launch phishing attacks which could very easily turn into ransomware or wire fraud.

When asked for comment, the company told *The Register* that it was “investigating a security event involving unauthorized access to certain company information through a compromised third-party data migration vendor.” No names or concrete figures anywhere in the statement.

“We have sent notifications about this security event and are providing support and guidance as appropriate,” the Infoblox spokesperson said. “Based on our investigation to date, we have no indication that any Infoblox products, cloud services, software updates or build-and-release processes were involved. Our priority is to fully investigate and resolve this issue."

The company is now offering money to the victims - $100 of “spot bonus” to help individuals purchase password management services, as well as two years of free identity theft and credit monitoring services - these days a standard practice in similar incidents. Infoblox also urged everyone to be "especially alert” for phishing, vishing, fraud, or other suspicious communications.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

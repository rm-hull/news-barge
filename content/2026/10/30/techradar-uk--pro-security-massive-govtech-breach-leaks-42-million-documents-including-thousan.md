---
title: Massive GovTech breach leaks 42 million documents — including thousands packed
  with personal information
source_url: https://www.techradar.com/pro/security/massive-govtech-breach-leaks-42-million-documents-including-thousands-packed-with-personal-information
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-30T18:01:03Z'
published: '2026-10-30T00:00:00Z'
description: CitySourced kept an open database available to anyone with a browser
image: https://cdn.mos.cms.futurecdn.net/GcQXTy4NBXKeoop4V5WQnQ-970-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- CitySourced
- Granicus
- Jeremiah Fowler
locations:
- US
organisations:
- CitySourced
- GovTech
- Granicus
- Logs
- PII
- Rock Solid Technologies
- TechRadar Pro
---

![Data leak](https://cdn.mos.cms.futurecdn.net/GcQXTy4NBXKeoop4V5WQnQ-970-80.jpg)

* **Researcher finds exposed database containing 42 million documents and hundreds of thousands of records with personal data**
* **The CitySourced-linked repository exposed names, contact details, complaint reports, and internal records for years**
* **Database was secured after disclosure, highlighting ongoing risks from misconfigured cloud storage**

Millions of documents, many exposing personally identifiable information (PII), were sitting online, in an open database accessible to anyone with a browser and the knowledge of where to look. The database belonged to a GovTech company called CitySourced, and has since been locked down.

Cybersecurity researcher Jeremiah Fowler reported finding a database contained roughly 42 million documents and 450,000 JSON files containing PII in plaintext.

The exposed records consisted primarily of images of complaints or code violation reports, but after analyzing a limited sample, Fowler found the database held people’s names, postal addresses, email addresses, phone numbers, and “thousands of internal records dating from 2016 to 2026”.

This kind of information is a gold mine for cybercriminals. By knowing private information about their targets, they can create custom, personalized phishing messages, increasing their chances of success. Data like this is frequently shared and sold on the dark web, and is often used as leverage in ransomware negotiations.

## CitySourced reacts

The exposed repository contained different top-level application directories, Fowler explained, listing names such as Api, Content, Customers, Data, Developers, FileStorage, json, Product, Public, Support, Widget, temp, Logs, and others. Apparently, the archive also contained multiple .sdk and .exe files - which are quite out of place and could indicate that someone tried to plant malware.

The name of the database and files inside led Fowler to conclude they belonged to a US company called CitySourced. This is a US civic technology company (GovTech) that develops software that residents can use to report local issues such as potholes or malfunctioning streetlights to municipal authorities. It was founded in 2009 and merged with Rock Solid Technologies in 2019. Three years later, the company was acquired by government technology provider Granicus.

When reporting on these databases, Fowler usually stresses that owning and operating are two different things, and that he could not determine if a third-party contractor managed it or not. Still, after reaching out to CitySourced, the company locked the database down and thanked Fowler for his efforts:

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

"Thank you again for the responsible disclosure and for following up,” CitySourced said. “Granicus has reviewed the information you provided, investigated the matter internally, and is taking action to address the issue."

## How to secure a database

Misconfigured databases continue to be one of the leading causes of data leaks. Some businesses don’t know they are responsible for the security of the data they create and instead believe it’s the responsibility of their cloud provider. Others are simply unaware of the misconfiguration, leaving data widely available and risking reputational damage and even class-action lawsuits.

Fowler says businesses can secure their infrastructure by segmenting customer environments and internal data.

There is no reason for all eggs to be in one basket, so in case of a compromise, configuration error, or unauthorized access involving one tenant, information belonging to other organizations remains secure.

“Storage systems, backups, and sensitive data should be encrypted and protected against unauthorized access,” he added. “Tenant isolation, access controls, and encryption provide a good first layer of defense that could limit the overall impact of a data security incident.”

Individuals should assume that cybercriminals already know something about them. There were so many breaches over the years that it’s almost impossible anyone’s data remained entirely private - at least things like names and emails. Therefore, they should always approach incoming email with skepsis, especially unsolicited ones, and those carrying links, attachments, or messages of utmost urgency.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

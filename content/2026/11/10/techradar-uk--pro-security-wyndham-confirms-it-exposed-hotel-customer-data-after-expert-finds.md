---
title: Wyndham confirms it exposed hotel customer data after expert finds flaw in
  app security
source_url: https://www.techradar.com/pro/security/wyndham-confirms-it-exposed-hotel-customer-data-after-expert-finds-flaw-in-app-security
source_site: TechRadar UK
source_slug: techradar-uk
description: Another day, another set of hardcoded credentials discovered
image: https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-2560-80.jpg
published: '2026-11-10T00:00:00Z'
scraped_at: '2026-11-10T19:40:11Z'
categories:
- Technology & Software
people:
- Robert Wiggins
- Wyndham
locations: []
organisations:
- Applebee
- European Securities and Markets Authority
- SEC
- TechCrunch
- TechRadar Pro
- US Securities and Exchange Commission
- What Security
- Wiggins
- Wyndham Hotels & Resorts
- Wyndham’s Android
---

![A hand about to touch a phone. Superimposed on top of it is a pink triangle with exclamation mark inside it. Behind it is a computer display with code on it](https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-1920-80.jpg)

* **Wyndham’s Android app exposed customer data and login tokens through hardcoded credentials embedded in the code**
* **Researchers found access to millions of records, including names, emails, member IDs, and active authentication tokens**
* **Wyndham fixed the issue after disclosure, but the scope of exposure and any prior access remain unclear**

Wyndham Hotels & Resorts, one of the world’s largest hotel chains, has admitted it experienced an embarrassing cybersecurity incident that exposed personally identifiable information and even mobile app login tokens, possibly for millions of people.

The hotel confirmed the news to *TechCrunch* after an independent researcher tipped off the publication about the security mishap.

Security researcher Robert Wiggins from What Security analyzed Wyndham’s Android app and found a set of hardcoded credentials. Those are credentials that are baked into the app’s code and are usually a leftover artifact from earlier development phases. While building an app, software developers would include admin credentials into the code to work faster and not have to log in every time they want to test a feature or a tool.

These credentials are usually removed in the final audit, just before the app is shipped. However, they are sometimes forgotten, which leaves a revolving double door back access for even the lowliest skilled cybercriminals.

## Customer data and login tokens

In this case, the credentials granted Wiggins access to an internal company database containing customer names, email addresses, Wyndham member numbers, and JWTs - customer login tokens that allow users to remain logged into their apps.

These tokens would prove invaluable to malicious actors, since they would allow them to access user instances without knowing their credentials (granted that they are still active and not expired or revoked).

Personally identifiable information, as well as Wyndham files and documents that were also stored in the database, could be used to create highly customized, tailored phishing lures, which could trick victims into installing malware, making fraudulent transactions, or granting attackers access to their employer’s corporate environment.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Wiggins apparently tried reaching out to the hotel but could not find the right channel, so he asked the media for help. When *TechCrunch* made contact, the company confirmed the security blunder but stressed that the issue had already been resolved.

“Our team has taken steps to address the issue,” a Wyndham spokesperson told the publication. “Our security teams have no evidence of any unauthorized access.”

The issue may be resolved, but plenty of questions remain unanswered. For example, we don’t know how many people had their data exposed this way. Wiggins says the database has “millions of entries”, but he could not determine a more concrete number. Wyndham claims it has 129 million enrolled rewards members.

## Wiggins' streak

We also don’t know for how long the database remained exposed this way. When were the credentials hardcoded into the app, and which versions kept them? The company also said there was no evidence of unauthorized access but declined to elaborate. Without a proper audit of server logs, we cannot know for certain if anyone viewed, or downloaded, the information before Wiggins’ discovery.

So far, it doesn’t seem as if Wyndham disclosed the leak publicly, or shared details with its customers whose data was exposed. Usually, incidents like this one need to be reported to appropriate authorities, including data watchdogs and regulators such as the US Securities and Exchange Commission (SEC), the European Securities and Markets Authority, or national data protection authorities.

This is the second instance of hardcoded credentials Wiggins found in just as many weeks. In early November, it was disclosed that the American casual dining restaurant chain Applebee’s kept hardcoded credentials in its Android mobile app, exposing customer names, their email addresses (both verified and unverified ones), dates of birth, phone numbers, ZIP codes, veteran status, the number of logins, dates of account creation, and the IP address of the most recent login session, to anyone who knew where to look.

Just as with Wyndham, we don’t know the exact number of people whose data was exposed this way, but it’s safe to say they are in the millions.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

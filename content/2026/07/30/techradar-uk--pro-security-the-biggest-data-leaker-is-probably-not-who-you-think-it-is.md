---
title: The biggest data leaker is probably not who you think it is
source_url: https://www.techradar.com/pro/security/the-biggest-data-leaker-is-probably-not-who-you-think-it-is
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-30T21:21:08Z'
published: '2026-07-30T00:00:00Z'
description: Misconfigured databases remain the leading threat to data security
image: https://cdn.mos.cms.futurecdn.net/GcQXTy4NBXKeoop4V5WQnQ-970-80.jpg
---

![Data leak](https://cdn.mos.cms.futurecdn.net/GcQXTy4NBXKeoop4V5WQnQ.jpg) 

In a world where data leaks are a constant, misconfigured databases remain the number one cause, exposing sensitive data to anyone who knows where to look.

This unfortunately common human error leaves the affected individuals and organizations open to hackers, cyber threats, scams, and further data leaks.

Even now, as you read this, there are plenty of companies that forgot to, didn’t know they had to, or didn’t care to lock their databases, leaving them open to the wide web.

## Defining misconfigured databases

When we talk about misconfigured databases, we talk about systems that somebody set up without appropriate security settings, leaving them public for all the Internet to see (and potentially exploit).

Access controls may be missing or given to too many people, and default passwords/configurations could be left unchanged by the user.

Additional common issues include giving full administrative control to users and apps where basic is sufficient, storing sensitive information in plain text, and disabling security logs (which prevents tracking unauthorized access).

Everyday Jane and Joe, unfortunately, have no idea how common this issue is – and it’s their data on the line. We’re talking about tens of thousands of major security breaches in a matter of years, and there’s no estimating how many publicly accessible databases are still out there. Here are just three of these many examples.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

In 2026, researchers found that European cloud provider Nextcloud kept an unprotected database on the public internet, containing 367,000 records (8GB) of sensitive employee and client data.

In 2025, IMDataCenter, a Florida-based data hygiene, enhancement, and append services provider, was leaking 38GB of sensitive personal records. The unencrypted and non-password-protected database held 10,820 in total.

In 2024, sports analytics technology company TrackMan exposed sensitive customer data: 110TB and 31,602,260 records. The database had no password.

## The Tribeca Film Festival case

Notably, the above-mentioned examples were the whitehat work of cybersecurity researcher Jeremiah Fowler, who recently uncovered a new data leak affecting the Tribeca Film Festival.

Fowler found four publicly accessible databases without passwords or encryption. These contained 666,369 records in total, timestamped from 2019 to 2026. Among press kits and marketing materials were also full names, email addresses, phone numbers, IP addresses, and hashed passwords.

Some of these are huge names in the film world, including famous directors, producers, and actors.

A found spreadsheet listed data obtained through device/user fingerprinting, such as user-agent data, device information, browser details, and source applications.

Fowler couldn’t say who exactly managed the databases, how long they had been public, or if anybody else had accessed them before him. This is often the case.

 ![Tribeca Film Festival data leak](https://cdn.mos.cms.futurecdn.net/nRmm5rkSQ3PAV36o6hzioE.png) 


## The issue of neglected backup files

Backup files often become forgotten, ignored, or simply deemed irrelevant, even when they contain a significant amount of potentially sensitive data concentrated in one place, aka a scammer’s treasure-trove.

Fowler describes these as some of “the most overlooked assets when it comes to data security.” While organizations often focus on protecting production systems, they put backups, exports, archives, or development environments on the back burner.

Yet, “backup files can become a single point of exposure if improperly secured,” the researcher warns.

## The US case

One may think that it’s only private companies, perhaps smaller ones, that make these seemingly dumb human errors. And yet, the biggest breaches that happened as a result of misconfigured databases all belong to governments.

The United States is often cited as being at the top for these data incidents. Among other events, in early 2011, the Texas Comptroller’s Office revealed a breach of 3.5 million people’s personal information, including Social Security numbers, dates of birth, and driver’s license numbers. The office kept the information on a publicly accessible state server.

In late 2015, computer security researcher Chris Vickery found a database with 191 million voters’ information, 300 GB in total, available for all to see. The cause, you’ve guessed it, is an incorrectly configured database.

“If you know the IP address, boom, you can access all of it,” Vickery said. “No authentication, no password, no security whatsoever involved.”

 ![US voter registration leak](https://cdn.mos.cms.futurecdn.net/EBBLdWJeDVWexFQp6Fyj6e.png) 


In 2017, internet security firm UpGuard revealed that Vickery found a 1.1 TB-heavy database of the Republican National Committee (RNC) with personal details of nearly every registered voter in the U.S., collected on behalf of Donald Trump’s election campaign. It was publicly available for two weeks due to an improperly configured security setting.

## The Brazil Case

Brazil's public sector has also seen a notable number of data exposures stemming from human error, not active hacking.

In 2018, cybersecurity researchers discovered a gigantic, openly accessible database with sensitive information of 120 million Brazilians, more than half of the population. A simple renaming mistake left the directory structure unprotected, which opened the database for viewing and downloading on the web.

2020 saw two significant leaks. Developers left database login credentials hardcoded and weakly encoded in the source code of the Ministry of Health’s official government website. The personal data and medical logs of more than 243 million people were left public for over six months.

Another leak that year exposed more than 16 million COVID-19 patients’ medical records after an employee uploaded a spreadsheet containing sensitive data on GitHub.

## Potential consequences of misconfigured databases

The issues that could arise from misconfigured databases are manifold, with potential consequences hitting in waves years after the initial leak.

Businesses may see financial losses, regulatory fines, lawsuits, operational disruption, and reputational damage. Should hackers find these databases, they may demand payment to restore access, or they may sell the info on the black market.

For an individual whose data has been exposed, the consequences can be severe. Bad actors can abuse individuals’ personal data and financial details, and even use it to scam other people.

Let’s take the above-mentioned cases as examples. Publicly exposed internal data of a large festival could give criminals detailed info on the operations behind the scenes, as well as on the participants.

“This type of information could create privacy and security risks by revealing personal contact information that could be used for phishing, social engineering, identity correlation, impersonation attempts, or further reconnaissance of internal storage systems,” Fowler writes.

Many more people can be targeted with celebrity frauds, where scammers impersonate celebrities, using data as ammunition.

In the US voter data case, it’s not just a matter of each person’s individual data, but the sheer magnitude of the information concentrated into one database. This is very expensive and time-consuming for cybercriminals to do, but it’s incredibly useful for a wide range of fraudulent schemes.

For example, “if a group gets a hold of this, they have phone numbers for the rest of their lives to call,” Vickery said.

UpGuard argued that the fact “that such an enormous national database could be created and hosted online, missing even the simplest of protections against the data being publicly accessible, is troubling.”

“Beyond the almost limitless criminal applications of the exposed data for purposes of identity theft, fraud, and resale on the black market,” UpGuard writes. “The heft of the data and analytical power of the modeling could be applied to even more ambitious efforts – corporate marketing, spam, advanced political targeting.”

As for healthcare-related breaches, these databases can earn sellers a lot of money on the black market, given the amount and the sensitivity of personal information that can be exploited. The risks include identity theft, account takeovers, financial fraud, and creating additional profiles to scam others, indefinitely.

Cybercriminals can even blackmail patients and healthcare providers, typically asking for large sums of money.

Insidiously, the exploit could stay hidden, or the full scale of the consequences may not be visible right away, but weeks or even months later.

## Shared responsibility model

Finally, despite the popular misconception, it’s not Amazon Web Services’ or Microsoft Azure’s duty to protect anyone’s databases. The provider secures the underlying cloud infrastructure, while the customer needs to protect their own data.

Based on the shared responsibility model, the customer must ensure the correct database configurations, securing all data properly.

Amazon writes that the customer assumes responsibility for any updates and security patches, as well as associated application software and the configuration of the AWS-provided security group firewall.

The chart below shows the Security “of” the Cloud versus Security “in” the Cloud.

 ![AWS customer data](https://cdn.mos.cms.futurecdn.net/tPsMxPbrGegg9MNcs33tVC.jpg) 


## Final thoughts

Unsecured databases are the number one cause of data breaches and leaks, spanning industries and governments, which many believe ‘should know better.’ These databases usually contain a variety of sensitive information, inadvertently exposed to the open internet, without any basic security measures being taken.

This makes them a juicy target for hackers, who may utilize them for ransomware, sell them on the black market, or use them for a variety of scams.

Proper database configuration is each database owner’s job.

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

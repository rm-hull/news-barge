---
title: Over 9 million facial recognition images leaked in major breach at reverse
  image search and identity verification service
source_url: https://www.techradar.com/pro/security/over-9-million-facial-recognition-images-leaked-in-major-breach-at-reverse-image-search-and-identity-verification-service
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-20T13:06:52Z'
published: '2026-08-20T00:00:00Z'
description: Another day, another misconfigured database
image: https://cdn.mos.cms.futurecdn.net/BUi4eir3JnCCT2MRGt3weS-2560-80.jpg
---

![Back View of Young Black Man Walking and Looking at Big Digital Screens Glitching While Displaying Code Lines. Professional Hacker Breaking Through Cybersecurity Protection System, Changing Code](https://cdn.mos.cms.futurecdn.net/BUi4eir3JnCCT2MRGt3weS.jpg) 

- **Researcher inds ClarityCheck’s exposed 450GB database with 9M+ user images**
- **Leak included faces, profiles, and photos, risking identity theft and phishing abuse**
- **Company secured access quickly; no evidence of dark web distribution or misuse so far**

An online reverse-lookup platform has inadvertently leaked millions of faces on the internet, putting people at risk of identity theft, phishing, and more, experts have warned.

Jeremiah Fowler, a cybersecurity researcher known for hunting exposed databases, recently found one totaling 450.2GB in size.

It contained exactly 9,042,977 image files - profile pictures, screenshots, and scans of physical photographs - all seemingly uploaded by the users. The images showed adults, teenagers, and even children, and were stored in folders labeled “faces” and “profiles”.

## What happened?

Further investigation showed the database belonging to a company called ClarityCheck. This is a US-registered firm describing itself as a “reverse phone, email, image, vehicle lookup”, allowing users to identify unknown callers, verify online contacts, check photos, and decode vehicles using publicly available data from “trusted sources”.

It is a legitimate business whose use case grows more important by the day - cybercriminals create fake internet personas every day, and use them in all sorts of schemes, from romance scams, to fake job offers, to anything in between. To do that, they will either steal other people’s photos, obtain (or buy) them on the dark web, or generate them using artificial intelligence.

Being able to verify someone’s identity has become everyone’s essential due diligence, regardless of if it’s a personal or business matter.

## How ClarityCheck responded

As soon as Fowler confirmed who owned the database, he reached out to ClarityCheck and responsibly disclosed his findings. The company responded quickly, barring further access, and thanking the researcher for his work.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“I completely understand your concerns regarding the exposure of sensitive images and the associated privacy risks. We greatly appreciate ethical researchers like you who bring these matters to our attention so we can act swiftly to protect our users' data and privacy,” the company’s representative told Fowler.

Unfortunately, without a deeper investigation on ClarityCheck’s end, there is no way of confirming exactly how long the database remained open, or if anyone accessed it before. However, so far there is no evidence of abuse, since a “ClarityCheck photo database” is currently not being distributed or sold anywhere on the dark web.

## Exposing people to hackers

In a world where data theft and leaks are increasingly common, a cause that’s easiest to address, is also the one resulting in most exposures - misconfigured databases. Nowadays, almost every business harvests and stores data about their employees, partners, and customers. Most of them store these files in cloud databases, for easier access and better integration with business intelligence software.

However, cloud service providers work on a so-called “shared responsibility model”, which means they are responsible for providing industry-standard security features. Users, on the other hand, are responsible for using those features and properly configuring their databases (namely, setting up a strong password or encrypting the content). Unfortunately, many organizations don’t seem to be aware of the shared responsibility model, firmly believing it’s the service provider’s task to keep the data safe. Others simply keep these archives accessible by mistake.

Criminals are aware of this, and are taking advantage of the situation to steal valuable information. By using widely available tools like Shodan, Censys, or FOFA, they can scour the web for unencrypted, non-password protected databases, and exfiltrate data to be used in phishing, business email compromise, and other forms of cyberattacks.

Over the years, Fowler and other searchers have found dozens of enormous databases that have leaked sensitive data on hundreds of millions of people.

In 2026, researchers found that European cloud provider Nextcloud kept an unprotected database on the public internet, containing 367,000 records (8GB) of sensitive employee and client data.

In 2025, IMDataCenter, a Florida-based data hygiene, enhancement, and append services provider, was leaking 38GB of sensitive personal records. The unencrypted and non-password-protected database held 10,820 in total.

In 2024, sports analytics technology company TrackMan exposed sensitive customer data: 110TB and 31,602,260 records. The database had no password.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

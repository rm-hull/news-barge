---
title: European cloud giant Nextcloud exposes staff and clients in major data breach
source_url: https://www.techradar.com/pro/security/nextcloud-leaks-367k-records-european-cloud-giant-exposes-staff-and-clients-in-major-breach
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-09T15:31:39Z'
published: '2026-07-09T00:00:00Z'
description: A misconfigured cloud database spills secrets, but Nextcloud was quick
  to remedy.
image: https://cdn.mos.cms.futurecdn.net/S6qqNHNiXvsDD9ymatwGjK-1920-80.jpg
---

![Cloud in Hand](https://cdn.mos.cms.futurecdn.net/S6qqNHNiXvsDD9ymatwGjK.jpg) 

- **Exposed ElasticSearch cluster at Nextcloud contained ~367k records (8GB), including employee data, client contracts, and scripts**
- **Sensitive information such as staff emails and client company details was left unencrypted; Nextcloud secured the archive within two days after notification**
- **Company attributed the incident to hosting misconfiguration, stressing customer servers were unaffected, though researchers warn attackers may have accessed the data**

European cloud provider Nextcloud kept an unprotected database on the public internet, exposing sensitive internal and client data to anyone who knew where to look, experts have revealed.

Nextcloud is a free, open source platform that lets users create their own private cloud. It is often described as an alternative to Google Drive, or Microsoft 365, which allows users to control where their data sits.

In mid-May 2026, security researchers from *Cybernews* discovered a publicly exposed ElasticSearch cluster and, after a deeper investigation, determined it contained around 367,000 records (8GB of data in total). The archive was a mix of Nextcloud employee data, client company data, contracts, and scripts built for the company’s clients.

## Nextcloud reacts

The majority of files were in .PDF format (71k), followed by .PNG (53k) and .MD (23k). All of the exposed records were found in a single index, with some revealing client company information, as well as data on Nextcloud staff. Some of the information was unencrypted, as well, exposing employee email addresses, client company names and addresses, and emails of individuals who sent invoices to Nextcloud.

*Cybernews* reached out to Nextcloud and the company locked the archive down within two days, and notified relevant authorities. It says it found no evidence of unauthorized access, but without a deep forensic analysis, it is impossible to say if that really is the case.

“If our team managed to discover the exposed dataset, threat actors may have too,” the *Cybernews* team wrote. “Malicious attackers operate numerous bots on the web that scour the net looking for exactly that: misconfigured databases with data to steal.”

The company also said this was a misconfiguration issue and that its services are secure: “The issue was caused by a misconfiguration of our hosting infrastructure and is not related to the Nextcloud solution. No other Nextcloud servers belonging to our customers, partners or other users have been affected by this issue,” the company’s spokesperson told the researchers.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

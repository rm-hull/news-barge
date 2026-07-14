---
title: Microsoft introduces security upgrades to tackle ShinyHunters
source_url: https://www.techradar.com/pro/security/a-single-entry-point-can-rapidly-expand-to-greater-enterprise-impacts-microsoft-introduces-changes-to-tackle-shinyhunters
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-14T17:25:17Z'
published: '2026-07-14T00:00:00Z'
description: Greater visibility, better detection, and stronger governance over OAuth-connected
  applications should mitigate ShinyHunters attacks.
image: https://cdn.mos.cms.futurecdn.net/cAewSdXkrLEUsD8muVzGX9-1920-80.jpg
---

![Microsoft logo outside building](https://cdn.mos.cms.futurecdn.net/cAewSdXkrLEUsD8muVzGX9.jpg) 

- **ShinyHunters abused OAuth trust in Salesforce by tricking users and later compromising SaaS integrations, stealing tokens to access hundreds of customer environments**
- **Reports suggested up to 700 victims; attackers exfiltrated data via legitimate APIs, making activity appear normal and persistent**
- **Microsoft responded with Defender for Cloud Apps upgrades, adding richer telemetry, near‑real‑time detection, and stronger governance over OAuth‑connected applications**

The ShinyHunters cybercrime group were so creative in breaking into corporate Salesforce environments that they forced Microsoft’s hand, making the company introduce new security upgrades just to address the attacks.

Microsoft has revealed it is focusing on improving visibility into OAuth-connected applications and strengthening governance over third-party integrations in Microsoft Defender for Cloud Apps. The changes fall into two main categories: Improved detection and investigation, and new posture and governance capabilities.

It makes sense, given that some reports claimed as many as 700 victims of the year-long campaign.

## Changes and improvements

But first, a little context: In August 2025, it was reported that ShinyHunters operatives were calling their targets on the phone, claiming to be IT support, and convincing them to authorize a seemingly legitimate Salesforce Data Loader application. This app was, in fact, controlled by the attackers and requested OAuth permissions which allowed them to access Salesforce data through official APIs.

Since everything happened through legitimate authentication and API calls, the activity looked like normal user behavior.

In the following months, the campaign evolved. Instead of tricking individual employees, ShinyHunters compromised third-party SaaS providers that integrated with Salesforce, including Salesloft's Drift integration, Gainsight, and later Klue.

By stealing OAuth tokens or integration secrets from these vendors, they accessed hundreds of downstream customer Salesforce environments without interacting with each customer individually.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

At one point, Google told reporters it was aware of more than 700 potentially impacted organizations.

“Microsoft consulted with Salesforce to improve granularity in telemetry for Defender for Cloud Apps with near-real-time detection, offering connected application attribution and expanded application permission insights,” the company said in a new report. “This activity was not the result of a vulnerability inherent to Salesforce. Rather, the threat actors abused trusted OAuth relationships for unauthorized access, data exfiltration, and persistence.”

In other words, Microsoft enabled greater visibility into OAuth-connected applications and their activity, allowed for better detection of suspicious API and OAuth behavior through richer telemetry and correlation, and now provides stronger governance of connected apps through permission analysis, risk scoring, and lifecycle management.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

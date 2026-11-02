---
title: Applebee's forced to fix serious security issue which exposed customer data
source_url: https://www.techradar.com/pro/security/applebees-forced-to-fix-serious-security-issue-which-exposed-customer-data
source_site: TechRadar UK
source_slug: techradar-uk
description: Researcher found hardcoded credentials in Applebee's mobile app
image: https://cdn.mos.cms.futurecdn.net/pVCXKrhThqmUjYVSZBjV5Z-2560-80.jpg
published: '2026-11-02T00:00:00Z'
scraped_at: '2026-11-02T21:42:26Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Robert Wiggins
locations:
- Aruba
organisations:
- Applebee
- Applebee’s
- Cisco
- Cybernews
- Dell
- Dine Brands
- Google Play Store
- HPE
- TechCrunch
- TechRadar Pro
- What Security
---

![Hands on a laptop with overlaid logos representing network security](https://cdn.mos.cms.futurecdn.net/pVCXKrhThqmUjYVSZBjV5Z-1920-80.jpg)

* **Applebee’s fixes mobile app flaw that exposed customer data through hardcoded database credentials**
* **Researchers found access to personal information including names, contact details, birthdays, and account metadata**
* **No evidence of abuse was found, but the incident highlights the persistent risk of hardcoded secrets in software**

Applebee’s has fixed a serious flaw in its mobile app that exposed sensitive customer information to pretty much anyone. Whether or not anyone malicious actually found this vulnerability and exploited it is not known at this time.

The chain has an Android mobile app that allows customers to browse the menu, customize meals, place orders for delivery or pickup, save their favorites, or receive personalized food recommendations.

A security researcher from What Security called Robert Wiggins, used AI to analyze the source code of the app and found a gaping hole - hardcoded credentials for a company database.

## Notifying the business

The database contained plenty of sensitive information: customer names, their email addresses (both verified and unverified ones), dates of birth, phone numbers, ZIP codes, veteran status, the number of logins, dates of account creation, and the IP address of the most recent login session.

We don’t know exactly how many people had their sensitive data exposed that way, but the app has more than a million downloads on the Google Play Store.

Wiggins soon realized that there was no way to report the issue either to Applebee’s itself or to its parent company, Dine Brands, so he reached out to *TechCrunch*. The publication verified his claims by finding the exposed credentials itself, and even created a new entry which Wiggins was later able to extract, and also confirmed the credentials allowed users to modify database entries.* TechCrunch* managed to get ahold of Dine Brands, who plugged the hole and thanked everyone involved: “We appreciate TechCrunch and the security researcher for bringing this matter to our attention,” the company said. “Our security team promptly launched an investigation and has not currently found any evidence of unauthorized access.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“Our investigation is ongoing, and we will take appropriate steps based on our findings,” the company added.

Hardcoded credentials are a very common mistake that sometimes has dire consequences. During production, software developers would leave login credentials inside the code to work faster, allowing the app to skip the tedious process of identifying every single time. However, the credentials are supposed to be temporary and are usually removed from the code before launch.

Sometimes, though, the credentials don’t get spotted during final code review and end up in the live version. Crooks who scan the codes for vulnerabilities can then use the information for unauthorized access.

## A common error

Unfortunately, it is a very common problem. In March 2025, security researchers from *Cybernews* analyzed more than 156,000 iOS apps and found more than 815,000 hardcoded secrets, thousands of which were “very sensitive and could lead directly to breaches or data leaks.” It’s worth mentioning that in this case, a “secret” means more than just passwords - it also includes API keys and encryption keys. The average app's code exposed 5.2 secrets, and 71% of apps leak at least one secret, Cybernews reported at the time.

A few months later, in July, HPE patched a similar bug in Aruba Instant On Access Points, and at roughly the same time, a similar flaw was found in Cisco’s Unified CM, enterprise-grade IP telephony call control platform providing voice, video, messaging, mobility, and presence services.

The leaks continued in 2026 - in February, news broke of Chinese state-sponsored threat actors abusing hardcoded credentials found in Dell’s RecoverPoint for Virtual Machines.

Applebee’s did not notify its customers about the incident, and it did not publicly disclose it on its website or social channels, at press time. Also, there are no indications that any threat actors exfiltrated this data or leaked it to the dark web.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

---
title: 355,000 school email addresses belonging to teachers and kids exposed in major
  breach at education firm Bromcom — here's what we know
source_url: https://www.techradar.com/pro/security/355-000-school-email-addresses-belonging-to-teachers-and-kids-exposed-in-major-breach-at-education-firm-bromcom-heres-what-we-know
source_site: TechRadar UK
source_slug: techradar-uk
description: Stolen emails a few months ago have now emerged
image: https://cdn.mos.cms.futurecdn.net/Z3qkzoGTB9FTZ8VMKj9c2K-1000-80.jpg
published: '2026-11-24T00:00:00Z'
scraped_at: '2026-11-24T21:53:12Z'
categories:
- Technology & Software
- Business & Entrepreneurship
- Education & Learning
people:
- Bromcom
locations:
- UK
organisations:
- Bromcom
- Google
- HIBP
- Harvard University
- MIS
- Microsoft
- PennKey SSO
- Princeton University
- Qlik
- SAP
- Salesforce
- TechRadar Pro
- University of Pennsylvania
- VPN
---

![Email warning](https://cdn.mos.cms.futurecdn.net/Z3qkzoGTB9FTZ8VMKj9c2K-1000-80.jpg)

* **Data from Bromcom’s September 2026 breach has surfaced publicly, exposing 355,000 unique school staff and student email addresses**
* **The leaked information also included SSO registration reference numbers, but not passwords, tokens, or authentication credentials**
* **Schools and affected users face elevated phishing risks as attackers can leverage exposed email data for targeted scams.**

Email addresses stolen in the September 2026 breach of Bromcom have leaked to the clearweb and landed on Have I Been Pwned?, a website that aggregates leaked emails and other sensitive data.

The platform now says 355,000 unique email addresses belonging to staff and pupils at UK schools, alongside SSO registration reference numbers, have been made public.

Bromcom is a British software company that builds solutions for day-to-day school operations, such as keeping track of students, their attendance, grades, and timetables, and is also used to communicate with pupils’ parents.

## Bromcom breach

In mid-September 2026, Bromcom disclosed suffering an attack in which hackers accessed parts of its network and ran a script to pull single sign-on (SSO) registration information associated with a number of schools.

The company first spotted the intrusion on September 6 and after a brief investigation, determined that the affected component was part of its Communications Server - separate from Microsoft and Google’s authentication services.

*The Register* describes it as a “legacy SSO registration component”, and a technology which, “had already been superseded but was still running because an internal system continued to use it.”

## Leaking emails (but nothing else)

According to Bromcom, only email addresses its staff and pupils used during SSO registrations were exposed. Passwords, authentication tokens, or other login credentials, were not obtained during the breach.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Bromcom stressed that its main management information system (MIS), the one storing and managing all of schools’ underlying data, was isolated and secured and as such, was never at risk.

The company also said it found no evidence the attackers made their way to the MIS, MyChildAtSchool, or other Bromcom user accounts, and that none of the user accounts were broken into.

To address the issue, Bromcom removed the legacy SSO component and introduced additional security measures, such as stronger school and account authorization checks, restrictions on who can remove SSO registrations, and more detailed logs.

The company said the risk to affected individuals was low since the stolen data did not include passwords or other sensitive information, and stressed that individual schools and trusts need to report the attack to the UK’s data protection watchdog.

Now, roughly two and a half months later, the data landed on HIBP, which claims that nothing besides emails was leaked. While email addresses and SSO registration reference numbers sound relatively harmless compared to passwords or credit card data, pupils and staff who landed on HIBP are still at risk.

Cybercriminals frequently use email data to craft convincing phishing messages and in this case, they can impersonate Bromcom, school administrators, or other trusted institutions and individuals.

## What can threat actors do with just an email?

Recently, hundreds of thousands of email addresses stolen from Harvard University in 2025 leaked on the dark web, mere weeks after both Princeton University and the University of Pennsylvania suffered the same fate.

All three were breached by the hands of the infamous ShinyHunters, who used a university employee’s PennKey SSO account to access the university’s VPN, Salesforce data, Qlik analytics platform, SAP business intelligence system, and SharePoint files.

It might sound superficial, but phishing is extremely dangerous and lucrative for the threat actors. Such messages could try tricking recipients into sharing logging details (by trying to log in on a spoofed website), running malware on their computers, or similar.

With that type of information, attackers can launch ransomware attack and more meaningful data theft, either extorting the victim in the process, or selling the proceeds on the dark web.

The good news is there is no indication that the data was being freely distributed on the dark web. No threat actor has publicly claimed responsibility for the attack, and Bromcom has not disclosed who was behind the intrusion.

The company has also not attributed the incident to any known ransomware group or cybercriminal operation.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

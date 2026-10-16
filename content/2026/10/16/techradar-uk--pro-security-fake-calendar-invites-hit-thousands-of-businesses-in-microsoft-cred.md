---
title: Fake calendar invites hit thousands of businesses in Microsoft credential phishing
  campaign
source_url: https://www.techradar.com/pro/security/fake-calendar-invites-hit-thousands-of-businesses-in-microsoft-credential-phishing-campaign
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-16T16:35:23Z'
published: '2026-10-16T00:00:00Z'
description: Hundreds of thousands of spam emails are carrying .ics attachments
image: https://cdn.mos.cms.futurecdn.net/pNhuQEsYXM8HA7844RaotB-1920-80.png
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations: []
organisations:
- CPR
- Check Point Research
- Microsoft Teams
- TechRadar Pro
---

![A desktop screen showing multiple meeting invites and calendar invites](https://cdn.mos.cms.futurecdn.net/pNhuQEsYXM8HA7844RaotB-1920-80.png)

* **Phishing campaigns are abusing calendar invites and meeting requests to steal Microsoft 365 credentials**
* **Attackers hide malicious links in .ics files, fake meeting details, QR codes, and invite pages**
* **Researchers observed hundreds of thousands of phishing emails targeting over 40,000 organizations**

If you get a calendar invite in your inbox be wary - it might be a carefully created phishing lure, designed to have you hand over Microsoft 365 or other login credentials.

Security firm Check Point Research (CPR) recently sounded the alarm for “several large-scale phishing campaigns,” abusing the fact that businesspeople routinely share calendar invites, and all designed to harvest their victim’s credentials.

## Different approach, same result

CPR says it identified two separate approaches. In some cases, the threat actors would share calendar invites as .ics attachments. These pass email filters (since the file type itself is harmless) and land directly into people’s inboxes. In other cases, the invites would come as links (which end up redirecting the victim away from their calendar and right into a trap).

The former is arguably more dangerous: the attachment is disguised as a meeting request or a payment notification, and when the recipient opens or accepts the invitation, it ends up in their calendar. Sometimes, depending on each user’s settings, the calendar entry may be processed automatically, too. In both cases, the fraudulent content now looks like an ordinary work appointment or service notification.

So far, none of these things are malicious, or dangerous, on their own. There is no vulnerability exploited, or malware deployed, here. However, the event description, location field, or embedded QR code, may direct the victim to a fake Microsoft 365 sign-in page, or a fraudulent payment portal. The victim, not realizing the landing pages were spoofed, may end up sharing their login credentials or payment information with the attackers.

The latter approach is easier to set up, but arguably harder to pull off. A link placed directly in the email, even if it looks benign on the surface, might get flagged by email security services and filtered out into spam. If it passes, though, victims will have a rather difficult time spotting the ruse.

In one of the examples shared by CPR, a victim received a fake Microsoft Teams meeting invite, and simply hovering over the “join” link revealed its real destination - a credential-harvesting page at a third-party website.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Large campaigns

The campaigns are quite large, CPR stressed, and growing. Hundreds of thousands of these emails get sent every month, from countless compromised email addresses:

“Check Point Email researchers are tracking these campaigns and have seen a significant surge starting September 25, 2026,” the report reads.

“A new detection layer specifically designed to identify this type of attack has flagged more than 302,386 unique phishing emails among our customers’ emails, sent to more than 40,000 organizations.”

The campaigns average more than 8,300 emails per active day, CPR said, adding that the messages came from more than 33,890 different sender domains and more than 247,270 unique sender addresses.

“Activity is not fading, it is accelerating. Daily volume grew from a few thousand emails a month in April to more than 118,000 in September, and to more than 740,000 in just the first two weeks of October. The busiest single day so far was October 8, with almost 200,000 emails,” the researchers concluded.

Phishing is one of the oldest and most used attack vectors out there, and for good reason. Besides being omnipresent, it is the cheapest and most effective way to compromise a target network.

That being said, defending against it usually revolves around common sense. Employees should be made aware that unsolicited emails carry real risk of cyberattacks, and that any email or instant message asking the recipient to urgently download a file, or log into a service, is most likely an attempted attack.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

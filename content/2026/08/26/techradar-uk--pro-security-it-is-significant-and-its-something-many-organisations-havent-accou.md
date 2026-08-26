---
title: '''It is significant, and it’s something many organisations haven''t accounted
  for'': The phishing threats hiding in your calendar invites'
source_url: https://www.techradar.com/pro/security/it-is-significant-and-its-something-many-organisations-havent-accounted-for-the-phishing-threats-hiding-in-your-calendar-invites
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-26T13:12:12Z'
published: '2026-08-26T00:00:00Z'
description: Barracuda explains why attackers are moving beyond the inbox and into
  calendar apps, and what security teams need to change to keep up
image: https://cdn.mos.cms.futurecdn.net/5SZMvKovSPYfFCNFA9RxaV-1280-80.jpg
---

![URL phishing](https://cdn.mos.cms.futurecdn.net/5SZMvKovSPYfFCNFA9RxaV.jpg) 

Although many people would think of phishing as a malicious email containing a suspicious link or attachment, hackers have now moved far beyond this to target trusted business tools including calendars and meeting invites.

We spoke to Soundharya Bharani Poomalai, Associate Threat Analyst, Barracuda__,__ to find out more.

- **Why are attackers increasingly turning to calendar invites and .ics files as phishing vehicles, and what has changed in the threat landscape to make this an attractive attack surface now?**

Calendars have become part of daily business admin and are used far beyond meeting scheduling. People now get invites for things like policy acknowledgements, handbook reviews, benefits enrolment windows and compliance training reminders. A calendar invite referencing an HR update or a payroll action doesn't look out of place, and this allows attackers to blend in more easily than a suspicious email ever could.

There's also a structural advantage. Calendar entries get added automatically with little or no interaction from the recipient, and they tend to persist even if the original email is deleted or quarantined. Mobile adds another layer to this. A lot of calendar notifications get handled on phones, which often sit outside the reach of desktop-focused security tools.

- **How significant is the visibility gap between what an email security system can inspect and what is rendered by a calendar application?**

It is significant, and it’s something many organisations haven't accounted for. Traditional email security is built to scan the message body, subject line and attachments, whereas an .ics file often slips through as a calendar object and doesn’t receive the same level of inspection.

The problem is that .ics files carry much more than a date and time. They can include event descriptions, organiser details, locations, attachments, URLs and custom metadata fields, and any of these can be used to hide phishing content. Once the calendar app renders that content, the recipient sees corporate branding, instructions or a QR code that looks entirely legitimate. If the victim then enters their credentials and completes MFA, the attackers can intercept the username, password and session data, giving them full access to the account.

That mismatch between what security tools check and what the user sees is why these attacks succeed.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

- **Are calendar phishing attacks fundamentally a new technique, or are they an evolution of the same social-engineering and evasion techniques we've seen in email phishing – such as QR codes, impersonation and adversary-in-the-middle attacks?**

They’re an evolution rather than an invention. The building blocks are familiar. QR codes hide a destination, brand impersonation builds trust, and adversary-in-the-middle platforms intercept credentials and session data in real time once someone signs in. None of this is new.

What's changed is the delivery container as they’re wrapped inside a calendar invite instead of an email. A QR code buried in an .ics file benefits from all the same advantages it has in a PDF or email body because it avoids text-based detection. It also gets the added benefit of sitting somewhere security tools are paying less attention.

- **What does the rise of .ics phishing tell us about how organisations need to redefine what constitutes ‘malicious content’?**

It tells us that malicious content is no longer confined to a bad link or attachment. Security teams have traditionally focused on email bodies and file attachments because that's historically where the risk sat. Calendar invites increasingly need to be factored into this as a phishing vehicle. The format of the content is not what determines the risk now, it’s what the content does when it reaches the recipient.

All of this means organisations need to start thinking about any workflow that can display or trigger content on a user's behalf.

## What should organisations be inspecting inside a calendar file, and what are the technical challenges involved in doing that effectively at scale?

Calendar files need the same level of scrutiny as a traditional attachment. In practice, this involves parsing the metadata fields, analysing any embedded links or attachments, inspecting HTML-rendered content, and decoding QR codes to check where they lead to.

The technical security challenge is that .ics files were built for interoperability. The format allows an event title, description or organiser field to carry rich content across Outlook, Google Calendar and Apple Calendar, and that flexibility is what makes it hard to inspect consistently at scale.

There's also the matter of what happens after delivery. A calendar entry can sit in someone's diary for days or weeks before a link becomes relevant, so inspection can't just happen once at the point of delivery. It needs to hold up over time.

## If a malicious calendar invite gets through, what should the incident-response process look like? Is deleting or quarantining the original email enough?

Deleting or quarantining the original email doesn't remove the calendar entry itself. Because invites are typically added automatically, the event can remain live in someone's calendar even after the source email is long gone, which means the malicious link or QR code is still sitting there and waiting to be clicked on.

A response will only be effective if it removes both the delivery message and the associated calendar entry from every affected mailbox. Teams also need to check identity activity around the time the invite landed and look for things like sign-ins from unfamiliar devices, unexpected MFA prompts, new session creation or OAuth consent activity. If someone did interact with the invite, credentials or session tokens may already be compromised, so containment can't stop at cleaning up the calendar.

 ![Top view of woman holding smartphone and tablet with calendar on desk](https://cdn.mos.cms.futurecdn.net/NK6WMQwJZAmbq9SfRREf2f.jpg) 


## What are the three most practical things security and business teams can do today to reduce their exposure to calendar-based phishing without disrupting legitimate use of calendars?

First, treat calendar invites as active content rather than passive scheduling data. Apply the same inspection standards to .ics files that already exist for attachments, including checking embedded links, attachments and any QR codes inside the event itself.

Second, strengthen identity security so a successful phishing attempt doesn't automatically become a successful breach. Phishing-resistant MFA such as FIDO2 or WebAuthn, conditional access policies, and the ability to monitor sessions and revoke them quickly all reduce the impact if someone does click through.

Third, update user awareness so people know calendar invites can be malicious too. Employees should be wary of QR codes inside calendar events and treat unexpected HR, payroll or policy notifications arriving as .ics files with the same suspicion as an unusual email.

## Are we reaching a point where organisations need to stop thinking of email as the attack surface, and instead think about all the trusted applications and automated workflows that email can trigger?

Yes, and calendar phishing is a good example of why. An email triggers a calendar entry, a calendar entry contains content, and that content leads somewhere else entirely, whether that's a fake sign-in page or a malicious QR code.

Every one of those steps happens in a different application, often with a different set of security controls, or none at all. Attackers are simply following that chain to find the weakest link, and the weak link tends to sit wherever inspection stops.

Organisations that only defend the inbox are defending one part of a much longer chain.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.* 

![Mike Moore](https://cdn.mos.cms.futurecdn.net/vinm2oPWMvB8yMg7qLhtxg.jpg)

Mike Moore is Deputy Editor at TechRadar Pro. He has worked as a B2B and B2C tech journalist for over a decade, including at one of the UK's leading national newspapers and fellow Future title ITProPortal. When he's not keeping track of all the latest enterprise and workplace trends, he can most likely be found watching, following or taking part in some kind of sport.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.

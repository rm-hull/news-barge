---
title: Elon Musk's Grok Build coding agent is leaking a serious amount of confidential
  data
source_url: https://www.techradar.com/pro/security/elon-musks-grok-build-coding-agent-is-leaking-a-serious-amount-of-confidential-data
source_site: TechRadar UK
source_slug: techradar-uk
description: Default options are wreaking havoc again
image: https://cdn.mos.cms.futurecdn.net/Wk33FJka7nsf7ZHFJcCRik-2000-80.jpg
published: '2026-11-11T00:00:00Z'
scraped_at: '2026-11-11T19:36:30Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Claroc
locations:
- US
organisations:
- Claroc
- Elon Musk
- Google Docs
- Grok Build
- SpaceX
- SpaceXSI
- TechRadar Pro
- xAI
---

![A laptop on an orange background showing the xAI Grok logo](https://cdn.mos.cms.futurecdn.net/Wk33FJka7nsf7ZHFJcCRik-1920-80.jpg)

* **Researchers found Grok Build apps were widely exposed due to insecure default sharing settings and discoverable URLs**
* **Thousands of accessible apps leaked sensitive business data, healthcare records, passwords, and internal documents**
* **SpaceXSI remediated the issue after disclosure, highlighting security risks in AI-generated application platforms**

Grok Build, an AI-powered coding agent built by Elon Musk’s SpaceXSI, has been found leaking a mind-numbing amount of confidential data, thanks to an apparent misconfiguration in how the products are being published on the platform.

SpaceXSI, established when SpaceX and xAI merged, has a product called Grok Build, which allows users to create web applications by simply describing what they want in a chatlike interface. Without having to write any of the code themselves, the users can have an app ready in minutes and publish it directly from the chat interface. The app gets a unique web address in the format <name>.grok.me, where “name” usually consists of four random words. It is something of a privacy feature, to make sure people can’t just guess an app’s location easily.

But according to security researchers Claroc, these addresses can be found through passive DNS services, which collect and index domain names observed in DNS traffic. In other words, anyone can find a published app even if their creator (or no one else, for that matter) ever shared a link for it. As Claroc explained in its report, the researchers did just that, identifying 43,601 addresses under grok.me.

## Unlocked apps

But finding someone’s app shouldn’t be a big deal, right? These apps are all password-protected, right? Well, wrong.

The researchers found that almost all of the apps (35,578, or 94.7%) could be accessed without authentication. That means that whatever data they were holding and generating could be accessed with almost no trouble at all. Further investigation uncovered a major oversight - when users want to publish an app, they are offered three privacy choices: “Anyone with the link”, “Invited Users”, and “Only You”. Similar to how Google Docs does it, when you want to share a document.

The problem here, according to Claroc, is that “Anyone with the link” is set as the default option, suggesting that most people building apps on Grok simply weren’t paying attention to the privacy and sharing options.

But still, simply accessing an app doesn’t necessarily have to be a security disaster, right? It’s just an app, right? Well, wrong again. While most apps were “harmless” in that regard (think games, calculators, landing pages), one in ten contained sensitive or internal business information, and 2% exposed information serious enough to warrant a high, or critical severity rating.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Leaking information

Claroc found a hospital employee directory with more than 3,500 names, an intensive care briefing containing patient information, and a trucking company’s recruitment database listing more than 1,000 individuals. It also found an employee timesheet whose downloadable code contained 18 accounts with plaintext passwords, including administrator credentials.

Even SpaceXSI was leaking its own classified information this way. The researchers found 24 open apps containing onboarding plans, employee names lists, a sales territory map of almost 600 strategic accounts and their pipeline, media plans and advertiser decks (all with budget tiers, including one for a US federal agency marked as confidential), seven campaign reports for advertisers around the world, and much, much more. The researchers found one solitary app, an archive of a streaming service’s ad measurement studies, that asked for a password. Everything else was left wide open.

Claroc also tested to see if they could alter the data found in these apps and built two of their own to test the theory out. One allowed unauthenticated visitor to modify a shared contact database, while another automatically granted access to anyone signing in with a Google account (even if they weren’t part of the team).

The researchers notified SpaceXSI about their findings on November 8, and within two days all SpaceXSI apps were no longer available. They are now working through the list and notifying everyone else.

*Via* * Ars Technica*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

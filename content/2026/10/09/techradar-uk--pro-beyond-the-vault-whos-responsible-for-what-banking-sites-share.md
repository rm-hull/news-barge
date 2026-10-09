---
title: 'Beyond the vault: Who''s responsible for what banking sites share?'
source_url: https://www.techradar.com/pro/beyond-the-vault-whos-responsible-for-what-banking-sites-share
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-09T10:29:20Z'
published: '2026-10-09T00:00:00Z'
description: Banking sites leak financial data via tracking scripts despite consent
image: https://cdn.mos.cms.futurecdn.net/fg7bgy65pWhFo4Qzib58yX-2560-80.jpg
categories:
- Technology & Software
- Personal Finance & Investing
people:
- TikTok
locations:
- Europe
- US
organisations:
- AnyDesk
- CCPA
- CPRA
- DORA
- DoubleClick
- EU
- Evergage
- Future plc
- Google Ads
- Google Analytics
- Jscrambler
- Meta
- PSD2
- TeamViewer
- TechRadar Pro
- TechRadarPro
- TikTok
---

![Phishing, E-Mail, Network Security, Computer Hacker, Cloud Computing Cyber Security 3d Illustration](https://cdn.mos.cms.futurecdn.net/fg7bgy65pWhFo4Qzib58yX-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Banks spend heavily to convince customers they are the most careful custodians of personal and financial data.

Our review of 14 financial-services websites across Europe and the US found otherwise: tracking and personalization scripts embedded in account-opening, mortgage, and loan-application flows sent contact details, financial intent, and device fingerprints to third parties, with 9 of the 14 sites doing so without a valid consent choice in place.

Head of Security Research at Jscrambler.

The failures fall into three patterns, and the distinction between them matters legally.

First, tags fired before the cookie banner had been answered at all, on wealth-management, investment-banking, and payment-provider sites; under the EU's ePrivacy Directive, that behavior never had a lawful basis, since consent is required before anything is stored on or read from a device.

Second, tracking continued after a user actively rejected cookies: at one site, Google Ads and DoubleClick still received the user's hashed email in the request URL alongside the consent-denied signal, meaning the rejection was recorded and then ignored.

Third, financial specifics leaked regardless of consent status: a loan amount of €2,500, a 12-month term, and an insurance selection reached Google Analytics during one personal credit application, and at a Portuguese bank, a customer's name, age, and tax number were sent to Evergage as Base64-encoded text in a request URL during account opening.

At a Dutch banking site, a first-party script combined browser fingerprinting with image requests to 127.0.0.1 on ports 7070 and 5938, the ports associated with AnyDesk and TeamViewer, effectively checking whether remote-access software was running on the visitor's own device.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Where the responsibility lies

Meta and TikTok have each pointed to the website operator as the party in control of what gets collected, in response to earlier research on this topic. Meta cited its privacy controls and its policy against sharing sensitive data. TikTok said advertisers decide what events and parameters they send, and that it only receives what partners intentionally configure.

That framing puts the responsibility entirely on the website operator, and it only holds up if the collection was something the operator deliberately turned on. Often it was not. Meta's Automatic Advanced Matching feature is turned on by default on the Meta Pixel, and in that default state it captures and hashes contact-form data without any separate configuration step from the site owner.

A bank engineer adding a standard tracking snippet is not choosing to send a mortgage applicant's hashed email and phone number to Meta; the pixel does that by default. A policy against collecting sensitive data is difficult to reconcile with a feature that collects it by default.

That does not remove the bank's own responsibility. Banks choose which vendors to deploy, place the consent banners in front of customers, and publish cookie policies that are supposed to name every entity receiving that data. Both sides carry some of the blame: platforms ship defaults that maximize data capture, and banks deploy those defaults into some of their most sensitive flows without validating what they actually do at runtime.

## Closing the gap

This is a compliance question as much as an ethical one.

In the EU, unmanaged third-party scripts in customer-facing flows sit across GDPR and ePrivacy consent requirements and, for regulated financial entities, DORA's third-party risk and operational resilience rules; PSD2 adds its own security obligations for payment flows. In the US, institutions carry duties under the Gramm-Leach-Bliley Act's Safeguards Rule, and increasingly under state laws such as the CCPA/CPRA. Regulatory exposure aside, this is basic operational hygiene.

Fixing this starts with verifying runtime behavior rather than assuming it matches what was configured. That means validating what scripts actually do on live account-opening, mortgage, loan, and simulation pages, since these carry the highest-value data, rather than stopping the checks at the homepage. It also means watching for a tag that starts collecting more than it was originally set up to collect, sometimes called scope creep.

Visibility needs to lead to control. Security teams need the ability to stop third-party scripts from reading sensitive form fields at all, and to block unauthorized data transfers, including the common technique of hiding identifiers and financial details inside a request URL rather than a request body, which is how several of the leaks in our research reached their destination.

Consent needs to mean something in practice, not just on paper. A rejection should stop data from leaving the browser instead of merely getting logged as a denied signal while the tracking call fires anyway. That choice also needs to travel with the customer into any iframe or subdomain the flow touches, rather than resetting at the first boundary it crosses.

Features such as Automatic Advanced Matching, which hash and send contact data by default, should be switched off unless that collection is documented, disclosed, and lawful. First-party code deserves the same scrutiny as third-party tags: fingerprinting and local port-probing built for fraud prevention can be a legitimate control, but building it in-house does not remove the need for disclosure and consent.

None of this requires banks to abandon analytics or personalization. It requires treating scripts on sensitive pages as part of the institution's risk surface, reviewed on the same cycle as any other vendor, rather than configured once and left alone. Nine of the fourteen sites we examined were sending data through a channel their own consent banner said was closed.

That gap, between what a script is allowed to do and what it actually does, is worth closing before a regulator or a customer finds it first.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

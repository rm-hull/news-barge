---
title: 'Authentication does not equal authorization: Are we asking passkeys to prove
  too much?'
source_url: https://www.techradar.com/pro/authentication-does-not-equal-authorization-are-we-asking-passkeys-to-prove-too-much
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-23T11:32:45Z'
published: '2026-10-23T00:00:00Z'
description: A passkey confirms who logged in, not what they intended
image: https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW-1920-80.jpg
categories:
- Technology & Software
- Society & Culture
- Self-Improvement
people: []
locations:
- Daon
- US
organisations:
- FIDO Alliance
- Future plc
- Javelin
- Palo Alto Networks’ Unit
- TechRadar Pro
- TechRadarPro
- The Federal Reserve
---

![Concept art representing cybersecurity principles](https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

By nearly all accounts, we’re inching closer to a passwordless society. The FIDO Alliance, which develops new passwordless authentication standards and whose tagline is quite literally “reducing reliance on passwords”, now estimates that more than 5 billion passkeys are in use worldwide. In fact, more than three-quarters of global consumers have already enabled a passkey on at least one account.

The technology is a boon for the financial industry because it finally removes the sector’s entrenched dependency on knowledge-based credentials – reusable “secrets” that criminals can steal, guess, or extract through social engineering. Suddenly, being able to quote a user’s mother’s maiden name, the town they grew up in, or their several-digit password, isn’t enough – and that makes user access instantly more secure.

Passkeys also give customers a much easier ride when it comes to accessing their accounts, speeding up the process by allowing them to use a key biometric like a fingerprint rather than hopping through two or three screens and entering their “memorable information” each time they log on.

President of Strategic Initiatives at Daon.

So far so good. However, according to research by Javelin, account takeovers still impacted some 6 million US consumers in 2025 – an increase of 18% on the previous year – with losses exceeding $15 billion. Countless other stats and analyses also support this trend, including The Federal Reserve, which reported a 36% increase in account takeovers between 2023-4 – and those are just the incidents that were brought to its attention.

A surface read of these figures suggests that passkeys are failing outright, but dive a little deeper and it’s clear that the problem isn’t with the technology itself, but how it’s implemented and safeguarded. Securing the front door doesn’t work if a fraudster can manipulate the locksmith into handing them a new key.

While a successful passkey authentication establishes control of a device-linked credential, it’s still on financial institutions to prove how that credential came to be enrolled and whether the session it grants access to remains trustworthy. Did the account holder genuinely intend to add that payee, recover that account, or move a huge sum of money? Passkeys are useful, but they were never designed to answer all of these questions on their own.

## In finance, scale doesn’t always equate to risk

Back in August, researchers at Palo Alto Networks’ Unit 42 published details of three proof-of-concept attacks against passkey-protected accounts. They demonstrated how malware on one compromised device could authenticate itself without the account holder even being present. It could even interfere with the registration of a new passkey, or even expose the passkeys synchronized to that user’s environment. Seemingly, another blow for passkeys.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

This is an alarming piece of research for sure, but best taken with a grain of salt. Delve deeper into the report, and it’s clear that every one of these scenarios began with a “poisoned” device, where malware was already present. The most serious cases also depended on a very particular combination of browsers and operating systems with preset security hardware.

Reassuringly, none of the cases had an “Enigma moment” where they broke the cryptography behind passkeys, nor did they uncover a “master vault” of credentials that could be ransacked in a single raid. That means attacks like these, where customers are pursued individually, would be far harder to scale than the kind of breaches we frequently read about in the headlines.

But “hard to scale” isn’t really much of a defense in finance. A criminal doesn’t need to steal access to thousands of accounts if one “whale” justifies the effort, and if successful, that single breach can spell doom for a bank’s reputation or regulatory standing – so warnings, while taken in context, should nevertheless be heeded.

## Account recovery was, and remains, the weakest link

One criticism users often have of passkeys is, “what happens when I lose or switch my device?” It’s an inconvenience for customers, and it's a real headache for banks. Of course, banks want to make the experience of switching devices as quick and painless as possible, but issuing a new passkey isn’t like resetting a password. It will only be as trustworthy as the processes used to issue it.

If passkey recovery falls back on an email, a text, or a PIN sitting in a notebook somewhere, all an attacker has to do is clear that relatively weak hurdle. How can a finance enterprise know if the person claiming to have a new device isn’t just an attacker who has come across this information by chance or while targeting a specific individual? It relegates passkeys to basic, knowledge-based security again, undermining the very purpose they were created for.

A bank simply cannot recover confidence in a customer’s identity if it never established that confidence in the first place. During enrollment, when the bank verifies who an individual is and binds their identity to a trusted record, it’s usually done through a server-held biometric reference – something that is preserved even when the original device is lost.

If a situation arises where a customer needs to recover an account, the bank should always return to that same source of truth rather than create new “evidence” by asking for it through channels that may have already been compromised. So while recovery may not be needed months or years after onboarding, the efficacy of it is really decided on day one.

## Authentication shouldn’t be confused with authorization

The line between authentication and authorization may seem invisible at times, but there’s a canyon between the two – particularly when it comes to moving money. Authentication establishes access, but authorization is what determines less tangible things like permission and intent. A passkey might prove the presence of a credential on the device, while a biometric or PIN check “releases” it and opens it for the user.

That confirms that the authenticator approved the login, but it doesn’t mean that everything that follows on that session is legitimate. Proving a user logged in legitimately at 10:19 doesn’t also prove that they meant to transfer $5,000 to a new payee at 10:26 – and that’s the grand canyon between authentication and authorization.

How the finance industry crosses that canyon depends on their ability to establish user intent in the moment. Of course, they can’t simply add gateways at every single point in the user’s journey – that kind of friction would be enough of an inconvenience for customers to start considering switching to a competitor.

But they can engage in step-up authentication and do what they can to establish contextual baselines. If a user logs on at 9:50 and checks their balance, like they have done countless times before at roughly the same time every few days, the passkey alone is enough. If they want to move money, add a new payee, or – perish the thought – recover their account, they need to reestablish trust by going back to the server stored source of truth outlined above.

Each request should warrant its own process for establishing truth depending on its level of sensitivity and what is at stake.

## Putting passkeys in their place

When it comes to modern banking, passkeys absolutely deserve their seat at the head of the table. They strip away the traditional dependencies on knowledge that can be easily stolen, and replace it with device-based credentials that are far harder to crack from a social engineering perspective. On paper, passkeys should banish account takeovers, but in practice, there’s still work to be done.

Finance enterprises still need to know who was originally bound to a device-based credential, and they need to be able to separate access from intent. Passkeys can carry some of that burden, but not all of it. Increasingly, finance is on the front lines of the new war on trust, and they must do what they can to establish it, nurture it, and preserve it.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

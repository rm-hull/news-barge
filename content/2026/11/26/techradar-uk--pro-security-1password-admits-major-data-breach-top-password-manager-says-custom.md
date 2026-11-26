---
title: 1Password admits major data breach — top password manager says customer details
  leaked, but passwords should be safe
source_url: https://www.techradar.com/pro/security/1password-admits-major-data-breach-top-password-manager-says-customer-details-leaked-but-passwords-should-be-safe
source_site: TechRadar UK
source_slug: techradar-uk
description: A 1Password employee had their GitHub account compromised
image: https://cdn.mos.cms.futurecdn.net/i9zSZktoeHmTBwmxCzjmba-2560-80.jpg
published: '2026-11-26T00:00:00Z'
scraped_at: '2026-11-26T16:51:13Z'
categories:
- Technology & Software
- Business & Entrepreneurship
- Careers & Productivity
people:
- 1Password
locations: []
organisations:
- 1Password
- App Store
- CI
- GitHub
- LastPass
- TechRadar Pro
- mSecure
---

![1Password app is displayed in the App Store on an iPhone. 1Password is a management tool designed for securely storing and organizing login credentials](https://cdn.mos.cms.futurecdn.net/i9zSZktoeHmTBwmxCzjmba-1920-80.jpg)

* **1Password discloses breach after attackers used stolen GitHub credentials to access source code and customer administrative metadata**
* **Exposed information included customer names, email addresses, account metadata, and certain invitation or recovery tokens**
* **The company says password vaults and their contents were never accessed, and it has since rotated affected credentials and strengthened protections**

1Password, one of the most popular password manager companies in the world, has confirmed it recently suffered a cyberattack, but said user vaults and their contents were not compromised.

In a data breach notice published on its website, 1Password said it spotted the attack on November 19 2026. Its investigation found that an employee’s GitHub login credentials were stolen, and the account used to access 1Password’s source code and push infostealer malware to backend servers, which ended up pulling “administrative data pertaining to our customers.”

1Password did not say how many people were affected by the incident, but said the data included customer names and email addresses, as well as “non-secret internal metadata” about the account.

“At no time were customer vault contents accessed by, or available to, the attacker,” the notice reads.

## Stolen tokens

That non-secret metadata includes account user identifiers, dates the accounts were created and last signed into. It also includes public keys which, 1Password stresses, are public by design and have no impact on user security, as well as Secure Remote Password Protocol parameters which, too, cannot be used to access people’s accounts.

The threat actors also ran away with tokens present in certain email links for invitations, provisioning and account recovery, as well as various version numeric identifiers and file numeric identifiers.

When the company sends an email to a customer to accept a provisioning invite to an account, or to accept recovery of their account, that email contains a token. That token is only used to complete the invitation or recovery process, and it needs to be combined with an SSO sign-in, or a six-digit code sent to the user’s email address. On its own, it does not grant access to the account.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“In order to reduce the ability for a malicious third party to successfully guess the code, we’ve expanded the code from six numeric digits to ten alphanumeric digits. This makes brute force guessing practically impossible,” 1Password added.

The threat actors, whose identity remains unknown at this time, also copied source code from private repositories, and gained access to the company’s CI/CD system but this data does not contain user information or secrets. “CI/CD contains infrastructure related secrets in order for our product to work,” the company said.

## LastPass and mSecure

The password manager giant has since rotated all credentials that may have been exposed in the attack, and reiterated that there is no impact to 1Password services, availability, or product security.

Still, that doesn’t mean its users are at no risk whatsoever. Full names and active email addresses are enough information to launch a convincing phishing attack which can trick the users into actually sharing their login credentials with the attackers. Threat actors can spoof the brand, threaten users with swift account termination unless they urgently “verify” their identity, and that way trick them into trying to log in through a spoofed website.

The growing popularity of password managers is making them a growing target for cybercriminals. Less than a month ago, mSecure confirmed suffering a data breach and even told its customers to reset their credentials “out of an abundance of caution”. In late June 2026, another password management giant, LastPass, confirmed losing sensitive data in a supply chain attack that struck a third party.

As the company explained at the time, threat actors first targeted Klue, a third-party market intelligence platform that integrates with its Salesforce and Gong systems. After obtaining its OAuth tokens, the attackers were able to access LastPass’ Salesforce environment and exfiltrate sensitive data stored there.

At press time, no threat actors claimed responsibility for the attack, and the data has not yet surfaced on the dark web. The company has not been called to pay a ransom demand in exchange for keeping the data private.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)

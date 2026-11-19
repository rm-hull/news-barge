---
title: Over 35% of Android banking apps have biometric logins that can be bypassed
source_url: https://www.techradar.com/pro/security/over-half-of-android-and-ios-banking-apps-have-serious-security-flaws-2-686-apps-across-top-global-banks-expose-bypassable-biometric-logins-and-hardcoded-secret-keys
source_site: TechRadar UK
source_slug: techradar-uk
description: More than half of major mobile banking apps have serious security vulnerabilities
  — and digital neobanks scored even worse
image: https://cdn.mos.cms.futurecdn.net/tcF5fR669mhPcH4akLWpTL-1920-80.jpg
published: '2026-11-18T00:00:00Z'
scraped_at: '2026-11-19T02:31:25Z'
categories:
- Technology & Software
- Personal Finance & Investing
- Business & Entrepreneurship
people:
- Ostorlab
locations: []
organisations:
- Firebase
- Google API
- Google Maps
- HarmonyOS
- Huawei
- Ostorlab
- TechRadar Pro
---

![Android apps](https://cdn.mos.cms.futurecdn.net/tcF5fR669mhPcH4akLWpTL-1920-80.jpg)

* **More than half of banking apps contain serious security vulnerabilities**
* **Hundreds of banking apps contain private keys and exposed access credentials**
* **Only 4.9% of banking apps support modern passkey authentication technology**

A security assessment covering 2,686 mobile banking applications has uncovered serious weaknesses that could expose customers to financial fraud and account compromise.

The investigation by Ostorlab examined software from 487 banks across 64 countries, covering Android, iOS and Huawei's HarmonyOS operating systems.

Over half of the examined applications contain high or critical security issues, raising concerns about protections surrounding mobile financial transactions.

## Biometric authentication and embedded credentials expose security weaknesses

According to Ostorlab, over half (51.5%) of examined applications contain at least one high or critical security finding - representing 1,384 applications, while another 18.4% received at least one critical classification during automated security assessments.

Biometric authentication also presents concerns, particularly among Android applications, where identified weaknesses affect fingerprint and facial recognition.

Their scanner successfully bypassed biometric authentication flows in 35.1% of Android applications examined, despite 73.2% of eligible applications connecting biometric verification to cryptographic keys.

Another concern involves sensitive credentials stored directly inside application packages, potentially exposing data that should remain inaccessible to unauthorized parties.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Ostorlab found private keys, cloud credentials, and software service access tokens in 20.3% of applications, representing 544 banking products.

Google API keys appeared separately in 72.5% of examined applications, although their presence does not automatically indicate compromised credentials.

Such keys commonly support services including Google Maps and Firebase, but inadequate restrictions could allow unauthorized parties to misuse associated cloud resources.

The investigation also identified outdated software components containing publicly documented vulnerabilities, creating additional opportunities for attackers seeking weaknesses within banking applications.

Approximately 41.1% contained at least one vulnerable third-party component, while 18.2% included components carrying critical vulnerabilities.

## Weak adoption of modern defenses

Despite the security problems, relatively few banking applications incorporate newer authentication technologies designed to reduce credential theft and unauthorized account access.

Only 4.9% integrated passkey functionality, while 20.2% incorporated application or device attestation mechanisms.

Attestation helps banks establish whether customers are accessing legitimate applications rather than modified copies installed through malicious distribution methods.

However, 79.8% lacked this protection, potentially complicating efforts to identify fraudulent software impersonating genuine banking applications.

Ostorlab also found nearly a quarter (22.3%) of Android applications could recognize remote-control or screen-sharing utilities commonly abused during banking fraud.

Commercial or platform-based application shielding appeared in just 26.9% of Android products examined.

Older operating systems introduce another concern because 99.5% of Android applications supported versions that no longer receive security updates.

Consequently, customers using outdated devices could continue accessing financial services through software environments lacking important manufacturer-issued protections.

Applications from 192 of the 500 banks also appeared on publicly available lists of financial institutions targeted by banking malware.

This represents 38% of the banks studied, although it does not mean their banking applications have been successfully attacked.

Ostorlab emphasized that its findings should not automatically be interpreted as confirmed opportunities for successful attacks.

Rather, it should be treated as “evidence that an issue is present, not proof that it is exploitable in production.”

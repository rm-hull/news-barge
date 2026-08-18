---
title: Russian websites could soon be easy pickings for hackers as security certificates
  expire — banks, emails, and government systems all potentially at risk
source_url: https://www.techradar.com/pro/security/russian-websites-could-soon-be-easy-pickings-for-hackers-as-security-certificates-expire-banks-emails-and-government-systems-all-potentially-at-risk
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-18T01:50:02Z'
published: '2026-08-17T00:00:00Z'
description: A sanction-enforced certificate revocation
image: https://cdn.mos.cms.futurecdn.net/pVCXKrhThqmUjYVSZBjV5Z-2560-80.jpg
---

![Hands on a laptop with overlaid logos representing network security](https://cdn.mos.cms.futurecdn.net/pVCXKrhThqmUjYVSZBjV5Z.jpg) 

- **Japanese certificate authority GlobalSign revoked TLS certificates for thousands of Russian domains in June 2026 as it implemented US and EU sanctions**
- **As a result, seven major Russian banks now serve certificates from a state root that no mainstream browser trusts, forcing users to manually install them**
- **Ukraine's Foreign Intelligence Service says the losses turn Russian banking, email, and internal systems into easier targets**

Russian companies are finding themselves in an extremely tricky situation as US OFAC and EU sanctions now affect international security certificates issued by third-party providers.

A statement issued by Ukraine's Foreign Intelligence Service on August 12 said the certificate withdrawals essentially left the country's internal systems, email, and banking exposed to attack because no internationally recognized certificates were issued for their domains.

It noted Russian state services, including the Federal Tax Service, increasingly fail to load in Chrome, Firefox, and Safari, and estimated that roughly 90% of the Russian market still depends on foreign-issued certificates, and that wide implementation of these sanctions could make it harder for users to access affected sites.

## Web trust certificates sanctioned away?

The move began on June 13 2026 when Japanese certificate authority GlobalSign, which controls much of Russia's commercial foreign certificate market, force-revoked TLS certificates it had previously issued to Russian companies.

Its local arm said that it could not influence the parent company's decision, which came due to new CA/Browser Forum rules, starting May 4. The rules effectively made screening applicants against the US OFAC and BIS lists, and European sanctions lists, mandatory for certificate authorities rather than optional, essentially tying the certificate provider's hands.

The move was implemented in two waves; the first affected an estimated 15,000-20,000 domains, and the second affected a more specific 310 domains across 44 companies, including large domestic names such as Rosneft, Gazprombank, Alrosa, and Positive Technologies.

The Ukrainian side insists that Russian internal systems, messengers, email, and banking APIs have become "ideal targets for hacker attacks," and there is some truth to it, even if mitigation is already underway on the Russian end. It estimates that reconfiguring infrastructure could cost larger corporations as much as 10 to 50 million rubles and take up to six months, and it is an error-prone process.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The move saw Russian domain owners, including its banks and tax services, turn elsewhere, with some moving first to a Greek academic certificate authority, HARICA, before turning to China's TrustAsia, which currently provides its state entities with certificates.

A more complicated play from the Russian end is a homegrown alternative the government continues pushing: state-issued trust root certificates that users must install manually. While the Ministry of Digital Development describes manual installation of its root certificate as "safe" and as having no effect on device function, security researchers have previously warned in 2022 and again in 2026 that a state-controlled root could be abused for "HTTPS traffic interception and man-in-the-middle attacks".

Moscow's other recommendation is that users switch to Yandex Browser, which ships with the domestic root built in. Ukraine's narrative dismisses that as an alternative prone to freezing and cache failures and offering no meaningful data protection, an assessment it attributes to "experts inside Russia."

Whatever the short-term outcomes result in here for .RU domains, a move like this could further disconnect Russia from the rest of the world, with Russian services working smoothly only for users running Russian software with a state root installed.

This might already be the trajectory for a Russia reeling from cyberattacks and sanctions, but one can assume the certificate revocations will only compress the timeline to that point, whether by design or an unintended consequence.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
